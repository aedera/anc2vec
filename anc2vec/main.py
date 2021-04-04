import os
import gzip
import pickle

import numpy as np

from .train import onto

SRC_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       'data/')

def get_embeddings():
    fname = os.path.join(SRC_DIR, 'embeddings.pklz')
    f = gzip.open(fname, 'rb')
    embs = pickle.load(f)
    f.close()

    return embs

def get_go():
    fname = os.path.join(SRC_DIR, 'go.obo')
    go = onto.Ontology(fname, with_rels=True, include_alt_ids=False)

    return go
