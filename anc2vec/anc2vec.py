import os
import tempfile
import requests
import logging

import numpy as np

logger = logging.getLogger(__name__)

#print  # prints the current temporary directory

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

            return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)


def get_embeddings():
    tmpdir = tempfile.gettempdir()
    emb_fin = os.path.join(tmpdir, 'embeddings.npy')

    if not os.path.exists(emb_fin):
        logger.info(
            "Start downloading pre-trained Anc2Vec embeddings (~36MB)..."
        )
        download_file_from_google_drive('1u8bmzv3q1UzfKjc4ZleCIbX5BSoz7mJ7', emb_fin)

    return np.load(emb_fin)
