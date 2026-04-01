import unittest
from unittest.mock import patch
import io
import sys

import strings as tob

def prompt_input(s: str, fn) -> any:
	# fn is function call with user input
	# s = the user input after function call fn
	with io.StringIO(s) as handle:
		stdin = sys.stdin
		sys.stdin = handle
		# function call with return value
		return_val = fn()
		sys.stdin = stdin
		return return_val
		
def prompt_output(fn=None) -> str:
	# catches prompt output after running function fn
	with patch('sys.stdout', new = io.StringIO()) as mo:
		if not fn is None:
			fn()
		s = mo.getvalue()
	return s


class Testing(unittest.TestCase):
	def test_ask(self):
		a = "dit is een input test"
		aa = prompt_input(a, tob.ask)
		b = "dit is een input test"
		self.assertEqual(aa, b)
		
	def test_make_title_lower(self):
		a = "dit is een output test"
		aa = tob.titlize(a)
		b = "Dit Is Een Output Test"
		self.assertEqual(aa, b)
		
	def test_make_title_upper(self):
		a = "dit is EEN OUTPUT test MET Capitals"
		aa = tob.titlize(a)
		b = "Dit Is Een Output Test Met Capitals"
		self.assertEqual(aa, b)

if __name__ == '__main__':
	unittest.main()
