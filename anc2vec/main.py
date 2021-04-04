import os
import tempfile
import logging

import numpy as np

SRC_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       'data/')

def get_embeddings():
    emb_fin = os.path.join(SRC_DIR, 'embeddings.npz')
    obj = np.load(emb_fin, allow_pickle=True)

    return {'term2index': obj['term2index'].item(), 'embeddings': obj['embeds']}
