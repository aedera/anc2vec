import tensorflow as tf
import numpy as np

from . import losses
from .layers import Distance2logprob

class Embedder(tf.keras.Model):
    def _build(vocab_sz, embedding_sz):
        inputs = tf.keras.Input(shape=(vocab_sz), dtype=tf.float32)

        hidden = tf.keras.layers.Dense(
            embedding_sz,
            kernel_initializer=tf.keras.initializers.GlorotUniform(seed=1234),
            use_bias=False,
            name='embedding')(inputs)

        y = tf.keras.layers.Dense(
            vocab_sz,
            kernel_initializer=tf.keras.initializers.GlorotUniform(seed=1234))(hidden)
        y = tf.keras.layers.Activation('softmax', name='ance')(y)

        # predict namespace (BP, CC, & MF)
        z = tf.keras.layers.Dense(
            3,
            kernel_initializer=tf.keras.initializers.GlorotUniform(seed=1234))(hidden)
        z = tf.keras.layers.Activation('softmax', name='name')(z)

        w = tf.keras.layers.Dense(
            vocab_sz,
            kernel_initializer=tf.keras.initializers.GlorotUniform(seed=1234))(hidden)
        w = tf.keras.layers.Activation('softmax', name='auto')(w)

        return tf.keras.Model(inputs, [y, z, w])

    def build(vocab_sz, embedding_sz):
        m = Embedder._build(vocab_sz, embedding_sz)
        model = Embedder(m.input, m.output, name='Embedder')

        optimizer = tf.keras.optimizers.Adam()

        model.compile(optimizer=optimizer,
                      loss=[
                          losses.Word2vecLoss(),
                          tf.keras.losses.CategoricalCrossentropy(),
                          losses.Word2vecLoss(),
                      ],
                      metrics={
                          'ance': tf.keras.metrics.Recall(name='rc'),
                          'name': tf.keras.metrics.CategoricalAccuracy(name='ac'),
                          'auto': tf.keras.metrics.MeanSquaredError(name='ms'),
                      },
                      #run_eagerly=True,
        )

        return model

    @tf.function
    def test_step(self, batch):
        x, y = batch
        y_pred = self(x, training=False)
        loss = self.compiled_loss(y, y_pred)

        # update loss
        self.compiled_metrics.update_state(y, y_pred, [])
        self.metrics[4].update_state(y[0], y_pred[0]) # neighbors
        self.metrics[5].update_state(y[1], y_pred[1]) # namespace
        self.metrics[6].update_state(y[2], y_pred[2]) # auto

        return { m.name: m.result() for m in self.metrics }

    @tf.function
    def train_step(self, batch):
        x, y = batch

        with tf.GradientTape() as tape:
            y_pred = self(x, training=True) # forward pass
            loss = self.compiled_loss(y, y_pred)
            #loss +=  self.foo_loss(y_pred[0], y[1]) # second-order NCA

        # compute gradients
        variables = self.trainable_variables
        grad = tape.gradient(loss, variables)
        # update weights
        self.optimizer.apply_gradients(zip(grad, variables))

        # update loss
        self.compiled_metrics.update_state(y, y_pred, [])
        self.metrics[4].update_state(y[0], y_pred[0]) # neighbors
        self.metrics[5].update_state(y[1], y_pred[1]) # namespace
        self.metrics[6].update_state(y[2], y_pred[2]) # auto

        return { m.name: m.result() for m in self.metrics }

    def reset_states(self):
        super().reset_metrics()
        for m in self.metrics:
            m.reset_states()
        for m in self.my_metrics:
            m.reset_states()
