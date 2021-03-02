class Tokenizer():
    def __init__(self, go):
        # add GO terms in the tokenizer
        self.go = go
        self.terms = sorted(list(set(go.ont.keys())))
        self.vocab_sz = len(self.terms)
        # zero is padding
        self.term2index = dict(
        [(term, i) for i, term in enumerate(self.terms)])
        self.index2term = dict(
        [(i, term) for i, term in enumerate(self.terms)])
