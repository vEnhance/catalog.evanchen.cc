+++
title = "Adv Poly Method"

[extra]
unit_id = "8"
subject = "C"
classification = "Combinatorics"
artist_name = "Arul Kolla"
num_students = 325
num_submissions = 36
num_clubs = 1388
num_hearts = 734
versions = ["ZCW"]
description = '''
Formerly, this was a unit on using combinatorial nullstellensatz, mostly for
fun. It was later expanded to additionally include uses of generating functions
and related polynomial methods on 3/6 level problems, broadening the scope
significantly.'''
+++

This unit used to be only about combinatorial nullstellensatz;
it was expanded in January 2024 to be broader in scope.

## About Adv Poly Method

Adv Poly Method was a relatively short yet very fun unit about the advanced,
extremely over-powered tool known as combinatorial nullstellensatz,
later expanded to include uses of related methods.
It is an easier unit overall for a Z unit,
but it is still recommended to only do this unit after having significant
grounding in more basic combinatorics techniques,
as they are far more important than this (think about learning moving points before similar triangles,
or Eisenstein's criterion before modular arithmetic).
On the other hand, the problems that can be solved by Combo Null are rarely ever
solvable using other techniques (similar to how Hall problems are "hard to
crack" without Hall's Marriage Theorem),
making it worthwhile to learn for those more advanced at combinatorics (looking at you, combo mains!).

With this in mind, the problem set of Combo Null is quite focused on the single
concept of combinatorial nullstellensatz,
so don't expect much diversity or variation out of it (quite similar to the gen
func or ineq func units in that sense).
The manner of applying combo null is somewhat of an art form, so you will never be bored, of course,
but the fact that you know combo null will need to be applied makes the problems
somewhat easier than you might expect.

All in all, it is a fantastic unit to do for people who are looking to learn an interesting trick,
and possibly gain a few points on an olympiad :eyes:

### Combo Null Theorem

Here is the statement of combinatorial nullstellensatz:

Let <span class="math math-inline">f(x&#95;1,\ldots ,x&#95;n)</span> be a
polynomial over a field <span class="math math-inline">\mathbb{F}</span>.
Suppose that the coefficient of the monomial <span class="math
math-inline">x&#95;1^{k&#95;1}\cdots x&#95;n^{k&#95;n}</span> in <span
class="math math-inline">f</span> is nonzero and <span class="math
math-inline">k&#95;1+\cdots +k&#95;n</span> is the total degree of <span class="math math-inline">f</span>.
If <span class="math math-inline">A&#95;1,\ldots ,A&#95;n</span> are finite
subsets of <span class="math math-inline">\mathbb{F}</span> with <span
class="math math-inline">|A&#95;i|>k&#95;i</span> for <span class="math math-inline">i=1,\ldots ,n</span>,
then there are <span class="math math-inline">a&#95;1\in A&#95;1,\ldots
,a&#95;n\in A&#95;n</span> such that <span class="math math-inline">f(a&#95;1,\ldots ,a&#95;n)\neq0</span>.

To learn more about this, you can read [this wikipedia
page](https://en.wikipedia.org/wiki/Restricted_sumset),
or read [this paper](http://www.math.tau.ac.il/~nogaa/PDFS/anrf3.pdf) or [this
paper](http://www.math.tau.ac.il/~nogaa/PDFS/null2.pdf). Alternatively, you can do this unit! :D

## Notable Problems

Note: "Alon" refers to "Noga Alon", the creator of combinatorial nullstellensatz, not "Alon Ragoler",
the creator of this article :P

Some notable problems in this unit include:

* Alon's hyperbase problem - simple application of combo null
* Problem from Alon - Representative of the mid-range of the problem set
* [ISL 2003 N8](https://aops.com/community/p119994) - Representative of the harder range of the problem set
* Problem from Alon and Knuth - Beautiful application of combo null
