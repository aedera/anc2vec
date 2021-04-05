# Anc2Vec

This repository contains the code of Anc2Vec, a method to embed GO terms into
an Euclidean space. These embeddings can preserve the uniqueness of terms,
their ancestor terms, and sub-ontology information.

Source code and instructions are provided for reproducibility of the main
results of *"Anc2Vec: embedding Gene Ontology terms by preserving ancestors
relationships,"* by A. A. Edera, D. H. Milone, and G. Stegmayer (under
review). Research Institute for Signals, Systems and Computational
Intelligence, [sinc(i)](https://sinc.unl.edu.ar).


<figure>
  <p align="center">
  <img src="img/Fig01.jpg" alt="Anc2Vec" height="400" style="vertical-align:middle"/>
  </p>

  <figcaption> The figure shows schematics of the GO structure and the
  architecture of Anc2Vec. A) GO structure. It is composed of three
  sub-ontologies: BP, CC, and MF. Colored nodes show the ancestors of a sample
  GO term. B) Anc2Vec architecture. The GO term is encoded as a vector x and
  transformed into a vector h , which is mapped into three vectors used to
  optimize Anc2Vec weights.
</figcaption> </figure>

<figure>
  <p align="center">
  <img src="img/Fig02.jpg" alt="Anc2Vec" height="400" style="vertical-align:middle"/>
  </p>

  <figcaption> The figure shows the Anc2Vec embeddings of GO terms in the
  three sub-ontologies. Points depict embeddings of GO terms whose colors
  encode the sub-ontologies: BP (Biological Process), CC (Cellular Component),
  and MF (Molecular Function).
</figcaption>
</figure>

## Embeddings availability

The pre-trained Anc2Vec embeddings built from the Gene Ontology
([obo file](./anc2vec/data/go.obo) release 2020-10-06) are available
[here](./anc2vec/data/embeddings.npz). Once downloaded, they can be easily
loaded as follows:

```python
import numpy as np

es = np.load('embeddings.npz', allow_pickle=True)['embds'].item()

```

`es` is a python dictionary that maps GO terms with their corresponding
embeddings. For example, to retrieve the embedding of the term GO:0001780, we
can use the following command:

```python
e = es['GO:0001780']
```

## Examples

Some examples on how to use `anc2vec` package:

* [Using pre-trained embeddings](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/pretrained_anc2vec_embeddings.ipynb)
* [Projecting pre-trained embeddings onto a 2-D space](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/project_embeddings.ipynb)
*
  [Building own embeddings based on a desired obo file](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/train_anc2vec_embeddings.ipynb)

## Datasets

Datasets used in the experiments of the manuscript:

* [Ancestors dataset](https://drive.google.com/file/d/1fgK50TNg5nrade22SwmqZYOeAxgPHIHY/view?usp=sharing)
* [Protein function dataset](https://drive.google.com/file/d/1eokaKj20tbFTn9jexQXIkONqwHeiBGS-/view?usp=sharing)
* [STRING dataset](https://drive.google.com/file/d/1dBZqQeBuGf35_pGT6qJWSuX1At32t9CI/view?usp=sharing)

## Installation

If you want to build your own embeddings using an obo file of your interest,
you can install `anc2vec` package via pip:

```bash
pip install -U "anc2vec @ git+https://github.com/aedera/anc2vec.git"
```
