# Anc2Vec

## Overview
Anc2Vec is a method to embed GO terms into a Euclidean space. Embeddings are
constructed to preserve ancestor terms and sub-ontology information.

## Embeddings availability

The pre-trained Anc2Vec embeddings build from obo file release XXX are
available [here](https://drive.google.com/file/d/1u8bmzv3q1UzfKjc4ZleCIbX5BSoz7mJ7/view?usp=sharing). Once dowloaded, they can be easily loaded
with numpy:

```python
import numpy as np
embeds = np.load('embeddings.npy')
```

## Instalation

If you want to construct embeddings for an obo file of your interest, you can install
`anc2vec` package via pip:

```bash
pip install -U "anc2vec @ git+https://github.com/aedera/anc2vec.git"
```

## Examples

You can find examples on how to get the embeddings of specific GO terms in the
`notebooks` folder of this repository:

* [Notebook]() Download and use pre-trained embeddings
* [Notebook](https://colab.research.google.com/github/aedera/anc2vec/blob/main/anc2vec_notbook.ipynb) to construct Anc2Vec embeddings for a specific obo file
