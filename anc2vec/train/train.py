#!/usr/bin/env python3
import sys
import datetime

import tensorflow as tf

from . import onto
from .utils import Tokenizer
from .models import Embedder
from .dataset import Dataset

def define_callbacks(model_name):
    ##
    models_dir = 'models/' + model_name + '/'
    datetime_tag = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = "logs/" + model_name + '/' + datetime_tag
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    #breakpoint()
    callbacks = [
        # tf.keras.callbacks.ModelCheckpoint(filepath=models_dir + datetime_tag + '!{epoch:05d}.tf'),
        # tensorboard_callback
    ]

    return callbacks

def fit(obo_fin, embedding_sz=2, batch_sz=4, num_epochs=10):
    go = onto.Ontology(obo_fin, with_rels=True, include_alt_ids=False)
    tok = Tokenizer(go)

    buffer_sz = tok.vocab_sz
    train_set = Dataset(tok,
                        batch_sz,
                        buffer_sz,
                        shuffle=True,
                        seed=1234).build()
    #train_set = train_set.take(tok.vocab_sz).cache()

    model = Embedder.build(tok.vocab_sz, embedding_sz)
    print(model.summary())

    model.fit(train_set,
              epochs=num_epochs,
              callbacks=define_callbacks(model.name + '_embedding_sz=' + str(embedding_sz)))

    # load model with best loss
    #tf.models.load_model(
    #return {'term2index': tok.term2index, 'embeddings': model.get_layer('embedding').numpy()}
