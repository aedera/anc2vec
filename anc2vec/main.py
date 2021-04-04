import os
import gzip
import pickle

import numpy as np

SRC_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       'data/')

def get_embeddings():
    fname = os.path.join(SRC_DIR, 'embeddings.pklz')
    f = gzip.open(fname, 'rb')
    embs = pickle.load(f)
    f.close()

    return embs
