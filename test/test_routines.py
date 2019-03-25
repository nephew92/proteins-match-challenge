import unittest
from application import routines as rt 

file_to_test = 'test/file_to_test.tsv'

class LoadFileTests(unittest.TestCase):
	"""docstring for RoutineTests"""
	def setUp(self):
		self.result = rt.s0_load_file(file_to_test,1,'\t')

	def test__return_a_list_based(self, error='Não retorna um list-based'):
		self.assertIsInstance(list(self.result),list,msg=error)

	def test__return_a_set_of_strings(self, error='Não retorna strings'):
		type_str = map(lambda s: type(s)==str,self.result)
		self.assertTrue(all(type_str),msg=error)

	def test__return_right_column(self, error='Não retorna a coluna correta'):
		self.assertListEqual(list(self.result),['name', 'prot1', 'prot2'],msg=error) 

class PreProcessName(unittest.TestCase):
	"""docstring for PreProcessName"""

	def test__return_list_based(self, error='Não retorna um list-based'):
		result = rt.s1_pre_process_name('protein name')
		self.assertIsInstance(list(result),list,msg=error)

	def test__ignore_hypothetical(self, error='Não ignora a palavra `hypothetical`'):
		result = rt.s1_pre_process_name('hypothetical protein name')
		self.assertFalse(list(result),msg=error)

	def test__ignore_words_less_than_three_characters(self, error='Não ignora palavras com 3 ou menos caracteres'):
		result = rt.s1_pre_process_name('the protein of name p')
		self.assertSetEqual(set(result),set(['protein','name']),msg=error)

	def test__ignore_alphanumeric_words(self, error='Não ignora palavras alfanuméricas'):
		result = rt.s1_pre_process_name('protein name fr43fg 5223')
		self.assertSetEqual(set(result),set(['protein','name','5223']),msg=error)

	def test__ignore_especial_character(self, error='Não ignora caracteres especiais'):
		result = rt.s1_pre_process_name('protein name / * _ 3 + . .;4 ')
		self.assertSetEqual(set(result),set(['protein','name']),msg=error)

	def test__ignore_words_in_brackets(self, error='Não ignora palavras dentro de colchetes'):
		result = rt.s1_pre_process_name('protein name [protein name]')
		self.assertSetEqual(set(result),set(['protein','name']),msg=error)

class FindMatch(unittest.TestCase):
	"""docstring for FindMatch"""
	def setUp(self):
		self.keys_a = ('foo', 'bar', 'foobar')
		self.keys_b = ('barfoo','bar')

	def test__return_value_between_zero_and_one(self, error='Valor retornado não está entre 0 e 1'):
		result = rt.s2_find_match(self.keys_a,self.keys_b)
		self.assertLessEqual(result, 1, msg=error)	
		self.assertGreaterEqual(result, 0, msg=error)	

	def test__return_zero_to_null_name(self, error='Não retorna 0 quando algum nome é vazio'):
		result = rt.s2_find_match(self.keys_a,[])
		self.assertFalse(result, msg=error)
		result = rt.s2_find_match([],self.keys_b)
		self.assertFalse(result, msg=error)
		result = rt.s2_find_match([],[])
		self.assertFalse(result, msg=error)

	def test__ignore_biggest_one(self, error='O tamanho do maior nome influencia na similaridade'):
		self.assertEqual(rt.s2_find_match(('foo', 'foobar','foofoo','bar'),('barfoo','bar','foo','barbar','barbarbar','foobarfoo','barfoofoo','barbarfoo')), 0.5, msg=error)
		self.assertEqual(rt.s2_find_match(('barfoo','bar','foo','barbar','barbarbar','foobarfoo','barfoofoo','barbarfoo'),('foo', 'foobar','foofoo','bar')), 0.5, msg=error)

	def test__example_cases(self, error='Não passou nos casos de exemplo'):
		self.assertEqual(rt.s2_find_match(('foo', 'bar', 'foobar'),('barfoo','bar')), 0.5, msg=error)
		self.assertEqual(rt.s2_find_match(('foo', 'bar', 'foobar'),('foo','bar')), 1, msg=error)
		self.assertEqual(rt.s2_find_match(('foo', 'bar', 'foobar'),('barfoo','bar','barbar')), 1.0/3, msg=error)
		self.assertEqual(rt.s2_find_match(('foo', 'foobar'),('barfoo','bar','foo','barbar')), 0.5, msg=error)

class CompareMatches(object):
	"""docstring for CompareMatches"""
	def test__example_cases(self, error='Não passou nos casos de exemplo'):
		p = 'putative'
		q = 'predicted'
		self.assertLess(rt.s3_compare_match("",p+q), 0, msg=error)
		self.assertLess(rt.s3_compare_match("",q+p), 0, msg=error)
		self.assertLess(rt.s3_compare_match("",q), 0, msg=error)
		self.assertLess(rt.s3_compare_match(p,q+p), 0, msg=error)
		self.assertLess(rt.s3_compare_match(p,p+q), 0, msg=error)
		self.assertLess(rt.s3_compare_match(p,q), 0, msg=error)
		self.assertLess(rt.s3_compare_match(q,q+p), 0, msg=error)
		self.assertLess(rt.s3_compare_match("",p), 0, msg=error)
		self.assertLess(rt.s3_compare_match(q,p+q), 0, msg=error)
		self.assertEqual(rt.s3_compare_match(p,p), 0, msg=error)
		self.assertEqual(rt.s3_compare_match(q+p,p+q), 0, msg=error)
		self.assertEqual(rt.s3_compare_match(p+q,q+p), 0, msg=error)
		self.assertEqual(rt.s3_compare_match(q,q), 0, msg=error)
		self.assertEqual(rt.s3_compare_match("",""), 0, msg=error)
		self.assertEqual(rt.s3_compare_match(p+q,p+q), 0, msg=error)
		self.assertEqual(rt.s3_compare_match(q+p,q+p), 0, msg=error)
		self.assertGreater(rt.s3_compare_match(p+q,q), 0, msg=error)
		self.assertGreater(rt.s3_compare_match(q+p,q), 0, msg=error)
		self.assertGreater(rt.s3_compare_match(p,""), 0, msg=error)
		self.assertGreater(rt.s3_compare_match(q,p), 0, msg=error)
		self.assertGreater(rt.s3_compare_match(q,""), 0, msg=error)
		self.assertGreater(rt.s3_compare_match(p+q,p), 0, msg=error)
		self.assertGreater(rt.s3_compare_match(q+p,p), 0, msg=error)
		self.assertGreater(rt.s3_compare_match(p+q,""), 0, msg=error)
		self.assertGreater(rt.s3_compare_match(q+p,""), 0, msg=error)
		