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
In **Prime Exponents**, the main focus is <span class="math math-inline">\nu&#95;p</span>. Lifting the Exponent and Legendre are also discussed. These tools are a big part of simplifying the problem. Additionally, one will learn the properties and how to apply <span class="math math-inline">\nu&#95;p</span>. 

If you don't know what <span class="math math-inline">\nu&#95;p</span> is, <span class="math math-inline">\nu&#95;p(a)</span> is the exponent of the largest power of <span class="math math-inline">p</span> that divides <span class="math math-inline">a</span>. For example, <span class="math math-inline">\nu&#95;5(250) = 3</span>. This definition naturally extends to rationals using the property <span class="math math-inline">\nu&#95;p(a/b) = \nu&#95;p(a) - \nu&#95;p(b)</span>.

## Philosophy

The main focus is learning how to use and manipulate <span class="math math-inline">\nu&#95;p</span>. This unit covers properties like:

1. <span class="math math-inline">\nu&#95;p(ab) = \nu&#95;p(a) + \nu&#95;p(b)</span>
2. <span class="math math-inline">\nu&#95;p(a/b) = \nu&#95;p(a) - \nu&#95;p(b)</span>
3. <span class="math math-inline">\nu&#95;p(\gcd(a,b)) = \min(\nu&#95;p(a), \nu&#95;p(b))</span>
4. <span class="math math-inline">\nu&#95;p(\operatorname{lcm}(a,b)) = \max(\nu&#95;p(a), \nu&#95;p(b))</span>
5. <span class="math math-inline">\nu&#95;p(a+b) \ge \min(\nu&#95;p(a), \nu&#95;p(b))</span>

In many problems, one can look at a single prime and prove something which is true for all primes. For example, there may be an equation that needs to be proven. Instead of looking at the whole picture, one can take <span class="math math-inline">\nu&#95;p</span> of both sides. Now it can be much easier to prove both sides are equal. Since a general prime was looked at, equality will hold for all primes.

Another case where <span class="math math-inline">\nu&#95;p</span> is very helpful are problems involving <span class="math math-inline">\gcd</span> or <span class="math math-inline">\operatorname{lcm}</span>, since properties <span class="math math-inline">3</span> and <span class="math math-inline">4</span> can be used.

## Notable Problems: 

Some problems in this unit have weird conditions and expressions but they really show how much <span class="math math-inline">\nu&#95;p</span> can make them more manageable.

* [BAMO 2018/4](https://aops.com/community/p13026024): required problem and an instructive example
* [TSTST 2019/7](https://aops.com/community/p12608512): good example that has a strange FE
* [Shortlist 2017 N4](https://aops.com/community/p10632689): has a nice idea

## Advice
This unit is in the harder side of B-units so try to engage well...
