import tensorflow as tf
import numpy as np

class Distance2logprob(tf.keras.layers.Layer):
    def __init__(self, ref_layer, activation='gaussian', **kwargs):
        super(Distance2logprob, self).__init__(**kwargs)
        self.ref_layer = ref_layer
        self.activation = activation

    def get_config(self):
        config = super(Distance2logprob, self).get_config()
        config.update({
            'ref_layer': self.ref_layer,
        })
        return config

    def squared_euclidean_distances(self, embeddings, inputs):
        """#

        This method calculate Euclidean distances between each embedding and
        the rest of the embeddings, which are stored in the variable
        ref_layer.weights[0].

        """
        # [batch_sz, vocab_sz, embedding_sz]
        d = self.ref_layer.weights[0] - tf.expand_dims(embeddings, 1)
        d = tf.reduce_sum(tf.math.pow(d, 2), 2) # [batch_sz, vocab_sz]
        # clamp potential negative values yield by underflow errors
        d = tf.nn.relu(d)

        return d

    def tstudent_kernel(self, distances, mask):
        """#

        mask: target terms from which squared euclidean distances were
        calculated.

        """
        complemented_mask = tf.math.logical_not(mask)
        e = 1.0 / (1.0 + distances) # calculate t Student
        e = tf.where(complemented_mask, e, 0.) # assign zero to targets
        # batch-wise normalization constants
        Z = tf.reduce_sum(e, axis=1, keepdims=True)
        #breakpoint()
        log_probs = tf.math.log(e) - tf.math.log(Z)

        return log_probs

    def gaussian_kernel(self, squared_distances, mask):
        """#

        mask: target terms from which squared euclidean distances were
        calculated.

        """
        # calculate partition function
        complemented_mask = tf.math.logical_not(mask)
        e = tf.exp(-squared_distances)
        e = tf.where(complemented_mask, e, 0.) # mask target terms
        Z = tf.reduce_sum(e, 1, keepdims=True)

        # calculate probabilities, i.e., e / Z in log space
        log_probs = -squared_distances - tf.math.log(Z)
        # mask target terms as -inf
        log_probs = tf.where(complemented_mask, log_probs, -np.inf)

        return log_probs

    def call(self, embeddings, inputs):
        out = self.squared_euclidean_distances(embeddings, inputs)
        if self.activation is None:
            return out # return squared distances
        elif self.activation == 'gaussian':
            mask = tf.cast(inputs, tf.bool) # mask for target terms
            return self.gaussian_kernel(out, mask)
        elif self.activation == 'tstudent':
            mask = tf.cast(inputs, tf.bool) # mask for target terms
            return self.tstudent_kernel(out, mask)
