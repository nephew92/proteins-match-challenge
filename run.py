#!/usr/bin/python3.6

import sys

def run_test():
	import test
	import unittest
	tests = unittest.TestLoader().discover('test', pattern='*.py')
	unittest.TextTestRunner().run(tests)

def run_application():
	import application

(({
	'test':run_test,
	'app':run_application
}).get(sys.argv[1] if len(sys.argv)>1 else 'app') or run_application)()