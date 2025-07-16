import numpy as np
from dataset import positive_words, negative_words


def vectorize(phrase):
	"""
		Vectorize
		=========

		Converts the list to a vector of 1s and 0s, depending on whether the word is positive or negative

		ARGS:
		-----
			phrase: text to vectorize 
	"""
	phrase = phrase.lower()
	vector_pos = np.array([1 if word in phrase else 0 for word in positive_words])
	vector_neg = np.array([1 if word in phrase else 0 for word in negative_words])
	
	return vector_pos, vector_neg


def clasificator(phrase):
	"""
		Clasificator
		=========

		To indicate whether the sentence is positive, negative or neutral 
		we look at the number of words of each type.

		ARGS:
		-----
			phrase: text to verify
	"""
	res = ""
	vec_pos, vec_neg = vectorize(phrase)
	amount_pos = np.sum(vec_pos)
	amount_neg = np.sum(vec_neg)

	if amount_pos > amount_neg:
		res = "POSITIVE"
	elif amount_pos < amount_neg:
		res = "NEGATIVE"
	else:
		res = "NEUTRAL"

	return res
