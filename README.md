# Anc2Vec

This repository contains the code of Anc2Vec, a method to embed GO terms into
an Euclidean space. Embeddings are constructed to preserve the uniqueness of
terms, their ancestor terms, and sub-ontology information.

## Embeddings availability

The pre-trained Anc2Vec embeddings build from [obo file](https://drive.google.com/file/d/1HEB9cVP6S63bi8nv7IrzXSYLLy5EPwBW/view?usp=sharing) release 2020-10-06 are
available
[here](https://drive.google.com/file/d/13DMaWYi-zBF8hbDFvIJM5p5vGb6kUPf3/view?usp=sharing). Once
dowloaded, they can be easily loaded with numpy:

```python
import numpy as np
es = np.load('embeddings.npz', allow_pickle=True)
```

`es` is a python dictionary with two elements: `term2index` that maps GO
terms to (row) indexes, and `embeds` a matrix whose rows contain embeddings of
GO terms.

## Installation

If you want to construct embeddings using an obo file of your interest, you
can install `anc2vec` package via pip:

```bash
pip install -U "anc2vec @ git+https://github.com/aedera/anc2vec.git"
```

## Examples

Some examples on how to use `anc2vec` package:

* [Use pre-trained embeddings](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/pretrained_anc2vec_embeddings.ipynb)
* [Project pre-trained embeddings onto a 2-D space](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/project_embeddings.ipynb)
* [Construct embeddings based on a desired obo file](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/train_anc2vec_embeddings.ipynb)

## Datasets

Datasets used for our experiments:

* [Links dataset](https://drive.google.com/file/d/14gu6XqoTUa8dNSqW1sTY_CHHQrVAyhEa/view?usp=sharing)
* [Ancestors dataset](https://drive.google.com/file/d/1fgK50TNg5nrade22SwmqZYOeAxgPHIHY/view?usp=sharing)
* [Protein function dataset](https://drive.google.com/file/d/1eokaKj20tbFTn9jexQXIkONqwHeiBGS-/view?usp=sharing)
* [STRING dataset](https://drive.google.com/file/d/1dBZqQeBuGf35_pGT6qJWSuX1At32t9CI/view?usp=sharing)
