import os
import tempfile
import logging

import numpy as np

from . import utils

def get_embeddings():
    tmpdir = tempfile.gettempdir()
    emb_fin = os.path.join(tmpdir, 'embeddings.npz')

    if not os.path.exists(emb_fin):
        utils.download_file_from_google_drive(
            '13DMaWYi-zBF8hbDFvIJM5p5vGb6kUPf3', emb_fin)

    obj = np.load(emb_fin, allow_pickle=True)

    return {'term2index':obj['term2index'].item(), 'embeddings':obj['embeds']}
