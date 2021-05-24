from collections import defaultdict

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
import sys
from sklearn.metrics.pairwise import cosine_similarity

# "https://tfhub.dev/google/universal-sentence-encoder/2",
# "https://tfhub.dev/google/universal-sentence-encoder-large/3"
model_url = "https://tfhub.dev/google/universal-sentence-encoder/2"

embedder = hub.Module(model_url)

# Reduce logging output.
tf.logging.set_verbosity(tf.logging.ERROR)

sentences_list = [
    # phone related
    'My phone is slow',
    'My phone is not good',
    'I need to change my phone. It does not work well',
    'How is your phone?',

    # age related
    'What is your age?',
    'How old are you?',
    'I am 10 years old',

    # weather related
    'It is raining today',
    'Would it be sunny tomorrow?',
    'The summers are here.'
]


class Compare:

    def __init__(self):
        # Import the Universal Sentence Encoder's TF Hub module
        pass

    # get cosine sim matrix
    def cos_sim(self, input_vectors):
        similarity = cosine_similarity(input_vectors)
        return similarity

    # get topN similar sentences
    def get_top_similar(self, sentence, sentence_list, similarity_matrix, topN):
        # find the index of sentence in list
        index = sentence_list.index(sentence)
        # get the corresponding row in similarity matrix
        similarity_row = np.array(similarity_matrix[index, :])
        # get the indices of top similar
        indices = similarity_row.argsort()[-topN:][::-1]
        return [sentence_list[i] for i in indices]

    def prepare(self):
        with tf.Session() as session:

            session.run([tf.global_variables_initializer(),
                        tf.tables_initializer()])
            sentences_embeddings = session.run(embedder(sentences_list))

            similarity_matrix = self.cos_sim(np.array(sentences_embeddings))

            sentence = "It is raining today"
            top_similar = self.get_top_similar(
                sentence, sentences_list, similarity_matrix, 3)

            # printing the list using loop
            for x in range(len(top_similar)):
                print(top_similar[x])
