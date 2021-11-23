# Anc2Vec

Anc2Vec is a novel method based on neural networks to construct embeddings of
GO terms. These embeddings can preserve the ontological uniqueness of terms,
their ancestor relationships and sub-ontology information.

This repository contains the source code and instructions for reproducibility
of the main results of *"Anc2Vec: embedding Gene Ontology terms by preserving
ancestors relationships,"* by A. A. Edera, D. H. Milone, and G. Stegmayer
(under review). Research Institute for Signals, Systems and Computational
Intelligence, [sinc(i)](https://sinc.unl.edu.ar).

<figure>
  <p align="center">
  <img src="img/Fig01.jpg" alt="Anc2Vec" height="400" style="vertical-align:middle"/>
  </p>

  <figcaption> Fig. 1. Schematics of the GO structure and the architecture of
  Anc2Vec. A) GO structure. It is composed of three sub-ontologies: BP, CC,
  and MF. Colored nodes show the ancestors of a sample GO term. B) Anc2Vec
  architecture. The GO term is encoded as a vector x and transformed into a
  vector h , which is mapped into three vectors used to optimize Anc2Vec
  weights.  </figcaption> </figure>

<figure>
  <p align="center">
  <img src="img/Fig02.jpg" alt="Anc2Vec" height="400" style="vertical-align:middle"/>
  </p>

  <figcaption> Fig. 2. Anc2Vec embeddings of GO terms in the three
  sub-ontologies. Points depict embeddings of GO terms whose colors encode the
  sub-ontologies: BP (Biological Process), CC (Cellular Component), and MF
  (Molecular Function).
</figcaption> </figure>

## Requirements

`anc2vec` requires Python 3.6 and TensorFlow 2.3.1.

## Installation

To install `anc2vec` is recommendable to have installed
[Conda](https://docs.conda.io/en/latest/), to avoid package conflicts.

After having Conda installed, create and activate a conda environment, for
example, named anc2vec:

```bash
conda create --name anc2vec python=3.6
conda activate anc2vec
```
Next, install the `anc2vec` package via pip:

```bash
pip install -U "anc2vec @ git+https://github.com/aedera/anc2vec.git"
```

## `anc2vec` functionalities

### Pre-trained `anc2vec` embeddings

The `anc2vec` package has already available the embedding of GO terms used in
the study. These embeddings were built from the Gene Ontology release
[2020-10-06](./anc2vec/data/go.obo). The embeddings can be easily accessed on
Python with this command:

```python
import anc2vec

es = anc2vec.get_embeddings()

```

Here, `es` is a python dictionary that maps GO terms with their corresponding
200-dimensional embeddings. For example, this command uses this dictionary to
retrieve the embedding corresponding to the term `GO:0001780`:

```python
e = es['GO:0001780']
```

This returns a [Numpy](https://numpy.org/) array containing the embedding

```python
array([ 0.55203265, -0.23133564,  0.1983797 , -0.3251996 ,  0.20564775,
       -0.32133245, -0.25364587, -0.16675541, -0.46832997, -0.40702957,
       ...
       -0.29757708, -0.33143485, -0.31099185,  0.24465033, -0.25458524,
       -0.24525951, -0.366758  , -0.04628978,  0.29378492,  0.31249675],
      dtype=float32)
```

These `anc2vec` embeddings are ready to be used for semantic similarity
task. Below there are examples showing how to use the `anc2vec` embeddings for
calculating cosine distances.

### Built `anc2vec` embeddings

The package also contains all the code needed for building `anc2vec`
embeddings from scratch for a given OBO file. Please check the examples below
for more information.


## Examples on how to use `anc2vec`

* [Using `anc2vec` pre-trained embeddings](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/pretrained_anc2vec_embeddings.ipynb)

* [Projecting `anc2vec` pre-trained embeddings](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/project_embeddings.ipynb)

* [Building `anc2vec` embeddings based on a desired obo file](https://colab.research.google.com/github/aedera/anc2vec/blob/main/examples/train_anc2vec_embeddings.ipynb)

## Datasets

Datasets used in the experiments of the manuscript:

* [Ancestors dataset](https://drive.google.com/file/d/1fgK50TNg5nrade22SwmqZYOeAxgPHIHY/view?usp=sharing)
* [Protein function dataset](https://drive.google.com/file/d/1eokaKj20tbFTn9jexQXIkONqwHeiBGS-/view?usp=sharing)
* [STRING dataset](https://drive.google.com/file/d/1dBZqQeBuGf35_pGT6qJWSuX1At32t9CI/view?usp=sharing)

## License

`anc2vec` is released under the [MIT License](LICENSE).
