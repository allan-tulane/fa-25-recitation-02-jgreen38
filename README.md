# CMPS 2200  Recitation 02

**Name (Team Member 1):**Justin Green 
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

|     n |   f(n) = 1 |   f(n) = log(n) |   f(n) = n |
|-------|------------|-----------------|------------|
|    10 |         15 |          19.966 |         36 |
|    20 |         31 |          44.253 |         92 |
|    50 |         63 |         107.311 |        276 |
|   100 |        127 |         221.265 |        652 |
|  1000 |       1023 |        1896.421 |       9120 |
|  5000 |       8191 |       12497.283 |      61728 |
| 10000 |      16383 |       25007.854 |     133456 |
Deriving the asymptotic behaviors and growth rates, f(n) = 1 and f(n) = log n are supposed to be Θ(n) since they are sublinear, and f(n) = n is supposed to be Θ(n log n) since it is linear. To check our accuracy, we must divide W(n) by the predicted asymptotic growth and assess their stability as we move across sizes. Since we are using (a,b) = (2,2), computing d = logb a gives us d = 1. Resultingly, for f(n) = 1 and f(n) = log n, we use W/n. For f(n) = n, we use W/(n log n). We will find that f(n) = 1 and f(n) = log n grow roughly constant as we move along the sizes, and f(n) = n grows almost perfectly constant. This signifies that the derivations determined are appropriate and generally consistent the growth patterns found here.


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

|     n |       W_1 |    W_2 |         W_3 |
|-------|-----------|--------|-------------|
|    10 |    21.291 |     36 |      73.297 |
|    20 |    47.055 |     92 |     236.037 |
|    50 |   110.236 |    276 |    1002.544 |
|   100 |   230.472 |    652 |    3005.088 |
|  1000 |  2075.117 |   9120 |  102240.295 |
|  5000 | 14251.208 |  61728 | 1184225.930 |
| 10000 | 28602.416 | 133456 | 3368451.860 |
Using d to represent log(b)a, d will be equal to one since a and b will be equally set to 2. We want to look at the relationship between c and d here, so we must isolate them and not keep everything else constant. To examine this relationship, we establish three conditional values of c for the three conditions asked for in the question, c < d, c = d, and c > d. Since d = 1, we will use [0.5, 1, 1.5] for the test values of c. When c < d, we predict Θ(n^d) = Θ(n) so linear growth. When c = d, we predict Θ(n^d log n) = Θ(n log n), so super-linear growth. When c > d, we predict Θ(n^c) = Θ(n^1.5), so evidently faster than linear. Our empirical results show when c = 0.5, we experience roughly linear growth (roughly doubling n across sizes). When c and d are equally, our growth is slighly faster than before (ex: 2.16x from n = 5000 to n = 10000). When c > d, we experience the fastest growth of the three(ex: 2.84x from n = 5000 to n = 10000). Comparing our theoretical predictions to the empirical trends, our ratios are roughly constant meaning we can confirm the trends we observe. 

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

|     n |   f(n) = 1 |   f(n) = log(n) |   f(n) = n |
|-------|------------|-----------------|------------|
|    10 |          4 |           7.644 |         18 |
|    20 |          5 |          11.966 |         38 |
|    50 |          6 |          19.043 |         97 |
|   100 |          7 |          25.686 |        197 |
|  1000 |         10 |          54.071 |       1994 |
|  5000 |         13 |          81.710 |       9995 |
| 10000 |         14 |          94.998 |      19995 |
f(n) = 1 is supposed to follow span S(n) = Θ(logn), f(n) = log n is supposed to follow span S(n) = Θ((logn)^2), and f(n) = n is supposed to follow span S(n) = Θ(n).
The smaller samples are host to irregularities in the pattern, so looking at our larger sizes, we can see that the theoretical predictions roughly match the empirical spans. For f(n) = 1, if n = 10000, span is about 13.3. We found at n = 10000, our span is 14. For f(n) = n, span should be linear and we observed a pattern of 2*n for our span from sizes 10 to 10000. The biggest discrepancy appears in f(n) = log n. However, this is likely because of hidden constraints and constant factors that are not considered in asymptotic notation.
