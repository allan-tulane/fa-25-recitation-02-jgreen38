"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	if n <= 1:
		return 1
	else:
		return a * simple_work_calc(n // b, a, b) + n
	

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	if n <= 1:
		return 1
	else:
		return a * work_calc(n // b, a, b, f) + f(n)

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	if n <= 1:
		return 1
	else:
		return span_calc(n // b, a, b, f) + f(n)



def compare_work(*work_fns, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		row = [n] + [fn(n) for fn in work_fns]
		result.append(tuple(row))
	return result

def print_results(results):
	""" done """
	headers = ["n"] + [f"W_{i}" for i in range(1, len(results[0]))]
	print(tabulate.tabulate(results,
							headers=headers,
							floatfmt=".3f",
							tablefmt="github"))



def compare_span(span_fn1, span_fn2, span_fn3, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1(n),
			span_fn2(n),
			span_fn3(n)
			))
	return result

def f_constant(n):
	return 1

def f_linear(n):
	return n

def f_logn(n):
	return math.log(n, 2) if n > 0 else 0

# results = compare_work(
#	lambda n: work_calc(n, 2, 2, f_constant),
#	lambda n: work_calc(n, 2, 2, f_logn),
#	lambda n: work_calc(n, 2, 2, f_linear)
#	)

# print_results(results)

powers = [0.5, 1, 1.5]
work_fns = [lambda n, c=c: work_calc(n, 2, 2, lambda x: x**c) for c in powers]

results = compare_work(*work_fns)
print_results(results)

# span_results = compare_span(
#	lambda n: span_calc(n, 2, 2, f_constant),
#	lambda n: span_calc(n, 2, 2, f_logn),
#	lambda n: span_calc(n, 2, 2, f_linear)
#	)
# print_results(span_results)
