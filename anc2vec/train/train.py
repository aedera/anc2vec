#!/usr/bin/env python3
import sys
import datetime
import tempfile

import tensorflow as tf

from . import onto
from .utils import Tokenizer
from .models import Embedder
from .dataset import Dataset

def define_callbacks(model_name):
    tmpdir = tempfile.gettempdir()
    model_file = tmpdir + '/models/' + model_name + '/' + 'best.tf'
    datetime_tag = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = tmpdir + "/logs/" + model_name + '/' + datetime_tag
    # tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(
            model_file, save_best_only=True, monitor='loss')
        # tensorboard_callback
    ]

    return callbacks

def fit(obo_fin, embedding_sz=200, batch_sz=64, num_epochs=100):
    go = onto.Ontology(obo_fin, with_rels=True, include_alt_ids=False)
    tok = Tokenizer(go)

    buffer_sz = tok.vocab_sz
    train_set = Dataset(tok,
                        batch_sz,
                        buffer_sz,
                        shuffle=True,
                        seed=1234).build()
    train_set = train_set.take(tok.vocab_sz).cache()

    model = Embedder.build(tok.vocab_sz, embedding_sz)
    print(model.summary())

    model_name = model.name + '_embedding_sz=' + str(embedding_sz)
    model.fit(train_set,
              epochs=num_epochs,
              callbacks=define_callbacks(model_name))

    # recover trained model with best loss
    tmpdir = tempfile.gettempdir()
    model_file = tmpdir + '/models/' + model_name + '/best.tf'

    model = tf.keras.models.load_model(model_file, compile=False)
    embeddings = model.get_layer('embedding').weights[0].numpy()

    # transform embeddings into a dictionary
    embds = {}
    for i, t in enumerate(tok.term2index):
        embds[t] = embeddings[i,:]

    return embds
