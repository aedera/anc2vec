import tensorflow as tf

class NeighborRecoveryLoss(tf.keras.losses.Loss):
    def __init__(self, from_logits=False,
                 reduction=tf.keras.losses.Reduction.AUTO,
                 name='recovery_error'):
        super().__init__(reduction=reduction, name=name)

    def call(self, y_true, y_pred, sample_weight=None):
        """To calculate loss, log probabilities assigned only to neighbors are used.

        Args:
        y_true: neighbors

        y_pred: log probabilities calculated from the distances from target terms
        to the rest of terms
        """

        # get log probabilities only for neighbors
        neighbors_log_probs = tf.boolean_mask(y_pred, y_true)
        loss = tf.reduce_mean(neighbors_log_probs)

        return -loss

    def get_config(self):
        config = super(NeighborRecoveryLoss, self).get_config()
        return config

class Word2vecLoss(tf.keras.losses.Loss):
    def __init__(self, from_logits=False,
                 reduction=tf.keras.losses.Reduction.AUTO,
                 name='recovery_error'):
        super().__init__(reduction=reduction, name=name)

    def call(self, y_true, y_pred, sample_weight=None):
        # get log probabilities only for neighbors
        neighbors_probs = tf.boolean_mask(y_pred, y_true)
        loss = tf.reduce_mean(tf.math.log(neighbors_probs))

        return -loss

    def get_config(self):
        config = super(Word2vecLoss, self).get_config()
        return config
