import json
import time
from utils import generate_data, get_subword_list
from regex import get_regex_patterns, regex_matcher

def make_vocab(word_list, save=True, name='main'):
	vocab={}
	for each_word in word_list:
		sub_word_list = get_subword_list(each_word)
		for sub_word in sub_word_list:
			if sub_word not in vocab:
				vocab[sub_word] = 0
			vocab[sub_word] += 1
	if save:
		f = open(f'{name}_vocab.json', 'w')
		json.dump(vocab, f, indent=4)
	return vocab
		
def filter(vocab):
	regex_list = set()
	vocab_keys = list(vocab.keys())
	best = vocab_keys[0]
	for i in range(1, len(vocab_keys)):
		curr = vocab_keys[i]
		if vocab[curr] >= vocab[best]:
			best = curr
		else:
			regex_list.add(best)
	return  list(regex_list)
			
if __name__ ==  '__main__':
	# actual_regex = ['GO612', 'G0611', 'LT566', 'QML29', 'LT100', 'LTMN55']
	# actual_regex = ['TIRS40563', 'PIW30546', 'TICSA3945', 'POL940325', 'GICGH9485', 'TJY9485']
	actual_regex = ['TMRQ40561', 'PIV30146', 'TICSV3941', 'QOM940315', 'GLDGH9481', 'MJY1481']
	print('actual : ', actual_regex)
	
	# dataset, word_list = generate_data(actual_regex, num_instances=10,
	# 			    lower_b=1, upper_b=1)
	start = time.time()
	opt = get_regex_patterns(actual_regex)
	print("number of possible regrexes :", len(opt))
	for idx, o in enumerate(opt):
		print(idx, "->", o)
		# regex_matcher(o, word_list)
	end = time.time()
	print('Time taken :', end - start, 'sec')
			
	
	'''print('\n\nWORDS/DATASET\n')
	for w in word_list:
		print(w)
	print('num of instances :', len(word_list))
	
	vocab = make_vocab(word_list)
	regex_codes = filter(vocab)
	
	print('\n\npred :', regex_codes)'''