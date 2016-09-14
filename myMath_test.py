import myMath
import operator
from nose.tools import eq_

myObj = myMath.myMath()

def test_sum():
	""" Check if sum is working correctly """
	eq_(myObj.sum(1,1), operator.add(1,1))

def test_sub():
	""" Check if sum is working correctly """
	eq_(myObj.sub(1,1), operator.sub(1,1))