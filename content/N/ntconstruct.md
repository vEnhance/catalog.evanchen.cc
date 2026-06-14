+++
title = "NT Construct"

[extra]
unit_id = "43"
subject = "N"
classification = "Number Theory"
artist_name = "Heyang Ni"
num_students = 983
num_submissions = 141
num_clubs = 7756
num_hearts = 3432
versions = ["DNY", "ZNY"]
description = '''
Construction problems in number theory. In some ways it's like the free unit
because you get to make some decisions, but in other ways Z has a lot of
structure that you might know things about, and you'll have to balance these
two intuitions.'''
+++
## Philosophy
This unit is very similar to the [Free](https://otis.evanchen.cc/wiki/units/list-of-combinatorics-units/free/) unit, where there is a lot of choices to make. They share strategies such as

- Experimenting: trying easy cases, looking for simple or motivated designs
- Restricting: looking for any constraints you can prove are necessary, adding constraints yourself (could mean restricting to a certain number set)
 
However, NT Construct is a step up from the Free unit, as each step requires NT skill. When doing this unit, it's is alright to feel "wasteful", such as using only very specific and large numbers, but this is alright since there are an infinite number of integers. Additionally, it is important that you pick your constraints well, as it can be difficult to prove there are an infinite number of integers that follow that certain constraint. For example, if you choose your constraint to be numbers such in the form <span class="math math-inline">n^2+1</span> that are prime, you have the extra task of proving there are an infinite number of numbers like that.

## Strategies

Of course, this unit will be very similar to the Free unit in terms of Strategy, but there are a few more things to consider when making a construction, for example:

- Choosing larger numbers with many factors
- Using CRT which allows you to add modular constraints
- Using theorems such as:
    - Bertrand: there always exists at least one prime number <span class="math math-inline">p</span> with <span class="math math-inline">n<p<2n-2</span>)
    - Dirichlet: there are an infinite number of prime numbers in the form <span class="math math-inline">an+b</span>, where <span class="math math-inline">\gcd(a,b)=1</span>
    - Zsigmondy's: there exists a prime number <span class="math math-inline">p</span> that divides <span class="math math-inline">a^n-b^n</span> but not <span class="math math-inline">a^k-b^k</span> for <span class="math math-inline">k\leq n</span>, with a few exceptions (<span class="math math-inline">n=1</span>, <span class="math math-inline">n=2</span> and <span class="math math-inline">a+b=2^k</span>, <span class="math math-inline">n=6</span> and <span class="math math-inline">a=2, b=1</span>)
    - Kobayashi: if <span class="math math-inline">M</span> is a infinite set of positive integers such that the prime divisors of the numbers are finite, then the set <span class="math math-inline">M+a</span>, where <span class="math math-inline">a</span> is a fixed integer has an infinite set of primes dividing numbers in the set. 

## Difficulty

This unit is on the tougher side of D leveled units. If you have trouble with this unit, it may be beneficial to try [Free](https://otis.evanchen.cc/wiki/units/list-of-combinatorics-units/free/) first. You could also just check it out since it is a sample unit.

## Notable Problems 
* [IMO 2003/6](https://aops.com/community/p266): A tricky problem which demonstrates narrowing down the search (the Restricting idea).
* [APMO 2009/4](https://aops.com/community/p1434408): A required problem that demonstrates the power of CRT.
* [USAMO 2012/3](https://aops.com/community/p2669119): A 9 pointer - instructive and beautiful, but very difficult.
