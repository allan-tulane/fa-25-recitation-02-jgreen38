from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(40, 5, 2) == 5390
	assert simple_work_calc(50, 6, 2) == 13592
	assert simple_work_calc(60, 7, 2) == 27416

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(40, 4, 2, lambda n: n*n) == 8448
	assert work_calc(50, 5, 2, lambda n: n) == 6225
	assert work_calc(60, 6, 2, lambda n: n*n) == 47124


def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work

	# create work_fn1
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: 1)
	# create work_fn2
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n*n)
	# create work_fn3
	work_fn3 = lambda n: work_calc(n, 2, 2, lambda n: n)

	res = compare_work(work_fn1, work_fn2, work_fn3)

	print(res)

	
def test_compare_span():
	# curry span_calc to create multiple span
	# functions that can be passed to compare_span

	# create span_fn1
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)
	# create span_fn2
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n*n)
	# create span_fn3
	span_fn3 = lambda n: span_calc(n, 2, 2, lambda n: n)

	res = compare_span(span_fn1, span_fn2, span_fn3)

	print(res)


