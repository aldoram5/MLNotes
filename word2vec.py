import numpy as np
import tensorflow as tf
import string

corpus_raw = 'He is the king . The king is royal . She is the royal  queen '
# convert to lower case
corpus_raw = corpus_raw.lower()

class Word2Vec(object):

    """
    Word2Vec Vectorize
    
    
    """
    @staticmethod
    def vectorize(corpus, ignore_case=False, ignore_chars=None, ignore_punctuation=False, window_size=2):
        words = []
        corpus_clean = corpus
        if ignore_punctuation:
            translator=str.maketrans('','',string.punctuation)
            corpus_clean=corpus_clean.translate(translator)
        if ignore_chars is not None:
            translator=str.maketrans('','', ignore_chars)
            corpus_clean=corpus_clean.translate(translator)
        if ignore_case :
            corpus_clean = corpus_clean.lower()
        for word in corpus_clean.split():
            words.append(word)
        words = set(words)  # remove duplicates
        word2int = {}
        int2word = {}
        vocab_size = len(words)  # gives the total number of unique words
        for i, word in enumerate(words):
            word2int[word] = i
            int2word[i] = word

        # raw sentences is a list of sentences.
        raw_sentences = corpus_raw.split('.')
        sentences = []
        for sentence in raw_sentences:
            sentences.append(sentence.split())
        data = []
        for sentence in sentences:
            for word_index, word in enumerate(sentence):
                for nb_word in sentence[
                               max(word_index - window_size, 0): min(word_index + window_size, len(sentence)) + 1]:
                    if nb_word != word:
                        data.append([word, nb_word])


        return
       
