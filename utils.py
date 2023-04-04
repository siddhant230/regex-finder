import random
import secrets

def generate_data(actual_regexes, num_instances=10,
								lower_b=7, upper_b=15):
	dataset = {}
	word_list = []
	for regex in actual_regexes:
		examples = []
		for _ in range(num_instances):
			size = random.randint(lower_b, upper_b)
			token = regex + secrets.token_hex(size)
			examples.append(token)
			word_list.append(token)
		dataset[regex] = examples
	return dataset, word_list
	

def get_subword_list(word, min_word_len=2):
	word_list = []
	for jump in range(min_word_len, len(word)):
		for i in range(len(word)-jump):
			word_list.append(word[:i+jump])
	return word_list
		