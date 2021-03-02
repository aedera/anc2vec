from . import onto
import numpy as np
import tensorflow as tf

class Dataset:
    def __init__(
            self, tokenizer, batch_sz=4, buffer_sz=1000, shuffle=True, seed=65):
        self.tok = tokenizer
        self.buffer_sz = buffer_sz
        self.batch_sz = batch_sz
        self.shuffle = shuffle
        self.seed = seed
        self._build_dataset()

    def _build_dataset(self):
        """Create a train dataset from obo file."""
        import tempfile
        import os

        tmpdir = tempfile.gettempdir()
        dat_fin = os.path.join(tmpdir, 'ds.tsv')

        name2code = {
            'biological_process': 0,
            'cellular_component': 1,
            'molecular_function': 2
        }

        # create dataset
        with open(dat_fin, 'w') as f:
            # loop over GO terms
            for t in self.tok.go.ont:
                # skip roots
                if t == onto.BIOLOGICAL_PROCESS or \
                   t == onto.CELLULAR_COMPONENT or \
                   t == onto.MOLECULAR_FUNCTION:
                    continue
                namespace = self.tok.go.ont[t]['namespace']
                ancestors = self.tok.go.get_ancestors(t)
                ancestors = set([t for a in ancestors for t in a])

                datapoint = '{}\t{}\t{}\n'.format(
                    t, '!'.join(sorted(ancestors)), name2code[namespace])

                f.write(datapoint)

        # generate dataset
        self.data_fin = dat_fin

    def build(self):
        def generator():
            with open(self.data_fin) as f:
                for a in f:
                    term, neighbors, namespace = a.strip().split('\t')
                    term = self.tok.term2index[term]
                    neighbors = [self.tok.term2index[t] for t in neighbors.split('!')]
                    namespace = int(namespace)

                    # term
                    x = tf.one_hot(term,
                                   depth=self.tok.vocab_sz,
                                   dtype=tf.float32)

                    # term's neighborhood
                    y = tf.one_hot(neighbors,
                                   depth=self.tok.vocab_sz,
                                   on_value=1. / len(neighbors),
                                   dtype=tf.float32)
                    y = tf.reduce_sum(y, 0)

                    # term's namespace
                    z = tf.one_hot(namespace, depth=3, dtype=tf.float32)

                    yield (x, (y, z, x))

        types = (tf.float32, (tf.float32, tf.float32, tf.float32))
        shapes = (self.tok.vocab_sz, (self.tok.vocab_sz, 3, self.tok.vocab_sz))
        data = tf.data.Dataset.from_generator(
            generator,
            output_types=types,
            output_shapes=shapes)

        if self.shuffle:
            data = data.shuffle(self.buffer_sz,
                                reshuffle_each_iteration=True,
                                seed=self.seed)

        data = data.batch(self.batch_sz)
        # last operation
        data = data.prefetch(tf.data.experimental.AUTOTUNE)

        return data
