+++
title = "Irreducible"

[extra]
unit_id = "38"
subject = "A"
classification = "Algebra"
artist_name = "Azat Madimarov"
num_students = 553
num_submissions = 62
num_clubs = 2880
num_hearts = 1052
versions = ["DAX"]
description = '''
Problems about showing polynomials are irreducible; these are rare in
olympiads, but give you a lot of good intuition about how $\mathbb{Z}[x]$
polynomials behave. Techniques that appear include working in
$\mathbb{F}_p[x]$, looking at the magnitude of complex roots a la Rouche, and
other ad-hoc tricks. More olympiad algebra than the integer polynomials unit.'''
+++

**Irreducible** is a rather technical unit of OTIS.
The ideas in this unit are not limited to just math Olympiads;
this unit can be a reasonable way to get a taste of finite fields and other associated “higher math” topics.
The “spark notes” are just half a page long, but don't let appearances deceive you:
it takes time to internalize and digest the definitions.
This unit is extremely rewarding for developing one's intuition.
However, the journey might as well be grueling because typical “Olympiad trick
collection” strategy (which is a greedy tactic) won't take you too far.

## Philosophy

Let us start by thinking how to think (I wish I could truncate this sentence
here) about polynomials with integer coefficients.
It is a polynomial ring, denoted by <span class="math math-inline">\mathbb{Z}&#91;X&#93;</span>.
Many-a-times, the polynomial ring corresponding to a ring inherits certain properties from its parent.
A good example of this fact is the [_Hilbert Basis
Theorem_](https://en.wikipedia.org/wiki/Hilbert%27s_basis_theorem).
So it makes sense to try to find the “analogs” of properties of <span
class="math math-inline">\mathbb{Z}</span> in <span class="math math-inline">\mathbb{Z}&#91;X&#93;</span>.
We can think of a polynomial:

1. In terms of its roots.
2. Or, its coefficients.
3. As a function of a complex variable

(last one because complex analysis <span class="math math-inline">\gg</span> real analysis; anyways,
exceptions always exist: you cannot do “inequalities” over complex numbers.
You must use <span class="math math-inline">\mathbb{R}</span> in some way,
which we usually do by employing the absolute value).

<span class="math math-inline">\mathbb{Z}</span> is an _integral domain_ (it is
a ring and the product of two non-zero elements is non-zero), which is good.
But if it were a _field_, it would have been even better.
It is _not_ a field, but we can always make use of the homomorphism <span
class="math math-inline">\mathbb{Z}\to\mathbb{F}&#95;p</span>!
From a more algebraic point of view (which means that we are more interested in the roots),
finite fields are really cool.
If you want a certain element, you can just add it in (like for rational numbers: number fields).
But this time, things are much nicer.

For example, if both <span class="math math-inline">2,3</span> are non-quadratic
residues modulo <span class="math math-inline">p</span>,
then <span class="math math-inline">\mathbb{F}&#95;p&#91;\sqrt{2}&#93;=\mathbb{F}&#95;p&#91;\sqrt{3}&#93;</span>,
which is blatantly false for <span class="math math-inline">\mathbb{Q}</span>.
The key players are the algebraic closure <span class="math
math-inline">\overline{\mathbb{F}&#95;p}</span> and the **Frobenius
endomorphism** <span class="math math-inline">x\mapsto x^p</span>, as you shall see.
A classic example of the use of the <span class="math
math-inline">\mathbb{F}&#95;p</span> reduction is the Eisenstein criterion.

## Notable Problems

Some problems are classical; some have a distinct algebraic number theoretic flavor.
Some are rather hard and worth knowing. Others are simply cool.

1. [Frobilinear polynomial's irreducible](/wiki/notable-problems/Z271403C/) Nice
   use of the Frobenius map and use of <span class="math math-inline">\overline{\mathbb{F}&#95;p}</span>.
2. [ELMO 2012 Problem 3](/wiki/notable-problems/12ELMO3/) This is worth knowing in itself;
   a verification of intuition.
3. [pseudo-Eisenstein for differences](/wiki/notable-problems/ZADCAAEE/) This is
   a good example of the reduction we talked about in philosophy (because it's
   not a direct corollary of that; you need to think more).
4. [Romania TST 2010](/wiki/notable-problems/10ROUTST53/) A good portrayal of
   using inequalities and bounding modulus of roots.
5. [Romania TST 2003](/wiki/notable-problems/03ROUTST22/) Wonderful example of
   one algebraic concept<span class="math math-inline">-</span> symmetry.
