import os
import tempfile
import logging

import numpy as np

from . import utils

logger = logging.getLogger(__name__)

def get_embeddings():
    tmpdir = tempfile.gettempdir()
    emb_fin = os.path.join(tmpdir, 'embeddings.npz')

    if not os.path.exists(emb_fin):
        logger.info(
            "Start downloading pre-trained Anc2Vec embeddings (~35MB)..."
        )
        utils.download_file_from_google_drive(
            '13DMaWYi-zBF8hbDFvIJM5p5vGb6kUPf3', emb_fin)

    obj = np.load(emb_fin, allow_pickle=True)

    return obj['term2index'].item(), obj['embed']
