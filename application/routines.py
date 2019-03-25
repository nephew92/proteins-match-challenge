def s0_load_file(f_name,column_to_return,column_delimiter,):
	'''
		Load a file from disk and return its content.
		args:
			f_name [str]: the file name to load.
			column_to_return [int]: the column index for the names of proteins.
			column_delimiter [str]: the character used to delimit the columns.
		return:
			[list]: The lines of the file.
	'''
	raise Exception('not implemented yet')

def s1_pre_process_name(protein_name):
	'''
		Extract from a string the keys (most important) words.
		args:
			protein_name [str]: the original protein name.
		return:
			[list or set]: the keys words in the protein name in lower case.
	'''
	raise Exception('not implemented yet')

def s2_find_match(keys_a, keys_b):
	'''
		Compare two set of keywords to find their similarity.
		args:
			keys_a [list or set]: the keyswords in the protein name A.
			keys_b [list or set]: the keyswords in the protein name B.
		return:
			[float]: a value between 0 and 1 (inclusive) tha represents how much the keys are similar. It should 1 if at least one of the keys_a or keys_b is fully contained on each other. Otherwise if both have nothing in commom it should 0.
	'''
	raise Exception('not implemented yet')

def s3_compare_match(keys_a,keys_b):
	'''
		Check weight between two sets of keywords.
		args:
			keys_a [list or set]: the keywords in the protein name A.
			keys_b [list or set]: the keywords in the protein name B.
		return:
			[float]: a value that represents which set of keywords is most important. Returns the negative value if keys_a is more important than keys_b, positive if keys_b are more important than keys_a and 0 if both are equally.
	'''
	raise Exception('not implemented yet')
