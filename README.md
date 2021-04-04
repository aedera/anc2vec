# Anc2Vec

This repository contains the code of Anc2Vec, a method to embed GO terms into
an Euclidean space. Embeddings are constructed to preserve the uniqueness of
terms, their ancestor terms, and sub-ontology information.

Source code and instructions are provided for reproducibility of the main
results of *"Anc2Vec: embedding Gene Ontology terms by preserving ancestors
relationships,"* by A. A. Edera, D. H. Milone, and G. Stegmayer (under
review). Research Institute for Signals, Systems and Computational
Intelligence, [sinc(i)](https://sinc.unl.edu.ar).


## Embeddings availability

The pre-trained Anc2Vec embeddings built from the Gene Ontology
([obo file](./anc2vec/data/go.obo) release 2020-10-06) are available
[here](./anc2vec/data/embeddings.npz). Once downloaded, they can be easily
loaded with numpy:

```python
import numpy as np
es = np.load('embeddings.npz', allow_pickle=True)
```

`es` is a python dictionary with two elements: `term2index` that maps GO terms
to (row) indexes, and `embeds` a matrix whose rows contain embeddings of GO
terms. For example, to retrieve the embedding of GO:0001780, we first need to
obtain its row index in the embedding matrix:

```python
term2index = es['term2index'].item()
row_id = term2index['GO:0001780'] # recover row index
e = es['embeds'][row_id,:] # retrieve embedding
```

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

* [Ancestors dataset](https://drive.google.com/file/d/1fgK50TNg5nrade22SwmqZYOeAxgPHIHY/view?usp=sharing)
* [Protein function dataset](https://drive.google.com/file/d/1eokaKj20tbFTn9jexQXIkONqwHeiBGS-/view?usp=sharing)
* [STRING dataset](https://drive.google.com/file/d/1dBZqQeBuGf35_pGT6qJWSuX1At32t9CI/view?usp=sharing)
