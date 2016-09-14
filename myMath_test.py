import myMath
import operator
from nose.tools import eq_
from nose.plugins.attrib import attr


myObj = myMath.myMath()

@attr('critical')
def test_sum():
	""" Check if sum is working correctly """
	eq_(myObj.sum(1,1), operator.add(1,1))

def test_sub():
	""" Check if subtract is working correctly """
	eq_(myObj.sub(1,1), operator.sub(1,1))


def test_mul():
	""" Check if multiply is working correctly """
	eq_(myObj.mul(1,1), operator.mul(1,1))