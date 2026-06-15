+++
title = "Prime Exponents"

[extra]
unit_id = "45"
subject = "N"
classification = "Number Theory"
artist_name = "Heyang Ni"
num_students = 1593
num_submissions = 436
num_clubs = 21927
num_hearts = 9727
versions = ["BNW", "DNW"]
description = '''
The use of $\nu_p$ in handling olympiad problems.'''
+++

In **Prime Exponents**, the main focus is $\nu_p$.
Lifting the Exponent and Legendre are also discussed. These tools are a big part of simplifying the problem.
Additionally, one will learn the properties and how to apply $\nu_p$.

If you don't know what $\nu_p$ is,
$\nu_p(a)$ is the exponent of the
largest power of $p$ that divides $a$. For example, $\nu_5(250) = 3$.
This definition naturally extends to rationals using the property $\nu_p(a/b) = \nu_p(a) - \nu_p(b)$.

## Philosophy

The main focus is learning how to use and manipulate $\nu_p$.
This unit covers properties like:

1. $\nu_p(ab) = \nu_p(a) + \nu_p(b)$
2. $\nu_p(a/b) = \nu_p(a) - \nu_p(b)$
3. $\nu_p(\gcd(a,b)) = \min(\nu_p(a), \nu_p(b))$
4. $\nu_p(\operatorname{lcm}(a,b)) = \max(\nu_p(a), \nu_p(b))$
5. $\nu_p(a+b) \ge \min(\nu_p(a), \nu_p(b))$

In many problems, one can look at a single prime and prove something which is true for all primes.
For example, there may be an equation that needs to be proven.
Instead of looking at the whole picture,
one can take $\nu_p$ of both sides.
Now it can be much easier to prove both sides are equal.
Since a general prime was looked at, equality will hold for all primes.

Another case where $\nu_p$ is very
helpful are problems involving $\gcd$ or
$\operatorname{lcm}$,
since properties $3$ and $4$ can be used.

## Notable Problems:

Some problems in this unit have weird conditions and expressions but they really
show how much $\nu_p$ can make them more manageable.

* [BAMO 2018/4](https://aops.com/community/p13026024): required problem and an instructive example
* [TSTST 2019/7](https://aops.com/community/p12608512): good example that has a strange FE
* [Shortlist 2017 N4](https://aops.com/community/p10632689): has a nice idea

## Advice

This unit is in the harder side of B-units so try to engage well...
