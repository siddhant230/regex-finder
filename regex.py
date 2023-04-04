import re
from collections import defaultdict

def get_regex_patterns(word_list):
	each_regex = []
	for word in word_list:
		std_form = get_standard_form(word)
		opt = convert_seq_to_regex(std_form)
		each_regex.append(opt)
	regex_patterns = merge_patterns(each_regex)
	return regex_patterns

def merge_patterns(each_regex):
	unique_regexes = defaultdict(list)
	for i in range(len(each_regex)):
		unique_regexes[each_regex[i][0]].append(each_regex[i][1])
	unique_regexe_maps = {}
	for k in unique_regexes:
		mapper = {}
		for u in unique_regexes[k]:
			for id, each_tk in enumerate(u):
				tk, count = each_tk
				idx = f'{id}_{tk}'
				if idx not in mapper:
					mapper[idx] = [10**5, -10**5]
				mapper[idx][0] = min(mapper[idx][0], count)
				mapper[idx][1] = max(mapper[idx][1], count)
		unique_regexe_maps[k] = mapper

	regex_outputs = []
	for k in unique_regexes:
		reg_str = ''
		for id in unique_regexe_maps[k]:
			min_, max_ = unique_regexe_maps[k][id]
			token = id.split('_')[1]
			reg_str += token + '{' + f'{min_},{max_}' + '}'
		regex_outputs.append(reg_str)
	return regex_outputs

def get_token(c):
	if c.isdigit():
		return '\d'
	elif c.islower():
		return '[a-z]'
	elif c.isupper():
		return '[A-Z]'
	else:
		return '\D'
			
def get_standard_form(word):
	std_list = []
	for w in word:
		tkn = get_token(w)
		std_list.append(tkn)
	return  std_list
		
def convert_seq_to_regex(sequence):
	sequence += ['']
	prev = sequence[0]
	opt_regex = []
	seq = []
	i = 1
	while i < len(sequence):
		count = 1
		while sequence[i] == prev:
			count += 1
			i += 1
		seq.append(prev)
		opt_regex.append([prev, count])
		prev = sequence[i]
		i += 1
	seq = ''.join(seq)
	return [seq, opt_regex]
	
def regex_matcher(regex, codes):
	print(f'for regex : {regex} matches are')
	for word in codes:
		val = re.match(regex, word)
		if val is not None:
			print(val.string)
	print('\n')
	
	
'''actual_regex = ['GO612', 'G0611', 'LT566', 'QML29', 'LT100', 'LTMN55', '12AB' 'AB34B']

#actual_regex = ['A1', 'AA2']
print('codes', actual_regex)

opt = construct_metadata(actual_regex)
print('generated regex :', opt)
print('\n\n')

for o in opt:
	regex_matcher(o, actual_regex)'''