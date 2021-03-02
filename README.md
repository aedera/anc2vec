# Anc2Vec

Anc2Vec is a method to embed GO terms into a Euclidean space. Embeddings are
constructed to preserve ancestor terms and sub-ontology information.

## Embeddings availability

The pre-trained Anc2Vec embeddings build from obo file release 2020-10-06 are
available
[here](https://drive.google.com/file/d/1u8bmzv3q1UzfKjc4ZleCIbX5BSoz7mJ7/view?usp=sharing). Once
dowloaded, they can be easily loaded with numpy:

```python
import numpy as np
embeds = np.load('embeddings.npz', allow_pickle=True)
```

`embeds` is a python dictionary with two elements: `term2index` that maps GO
terms to row indexes, and `embeddings` a matrix whose rows contain embeddings
of GO terms.

## Instalation

If you want to construct embeddings for an obo file of your interest, you can install
`anc2vec` package via pip:

```bash
pip install -U "anc2vec @ git+https://github.com/aedera/anc2vec.git"
```

## Examples

You can find examples on how to get the embeddings of specific GO terms in the
`notebooks` folder of this repository:

* [Use pre-trained embeddings](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/pretrained_anc2vec_embeddings.ipynb).
* [Train embeddings for a desired obo file](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/train_anc2vec_embeddings.ipynb).
