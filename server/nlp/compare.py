from collections import defaultdict

import tensorflow as tf
import tensorflow_hub as hub

embed_module = hub.Module(
    "https://tfhub.dev/google/universal-sentence-encoder/4")


class Compare:

    # def __init__(self) -> None:
    #     pass

    def make_embeddings_fn(self):
        placeholder = tf.placeholder(dtype=tf.string)
        embed = embed_module(placeholder)
        session = tf.Session()
        session.run([tf.global_variables_initializer(),
                    tf.tables_initializer()])

        def _embeddings_fn(sentences):
            computed_embeddings = session.run(
                embed, feed_dict={placeholder: sentences})
            return computed_embeddings

        return _embeddings_fn

    def verify(self, intent_training_phrases):
        generate_embeddings = self.make_embeddings_fn()
        training_phrases_with_embeddings = defaultdict(list)
        for intent_name, training_phrases_list in intent_training_phrases.items():
            computed_embeddings = generate_embeddings(training_phrases_list)
            training_phrases_with_embeddings[intent_name] = dict(
                zip(training_phrases_list, computed_embeddings))
