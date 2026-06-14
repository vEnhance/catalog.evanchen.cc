+++
title = "Equality"

[extra]
unit_id = "14"
subject = "C"
classification = "Combinatorics"
artist_name = "Owen Zhang"
num_students = 2262
num_submissions = 485
num_clubs = 25670
num_hearts = 12242
versions = ["BCW", "DCW", "ZCW"]
description = '''
An important unit about taking advantage of the equality case in combinatorial
problems in order to solve problems. Mandatory for newcomer students.'''
+++
**Equality** is one of the first philosophical units to appear in the OTIS curriculum. It has been described as "mandatory for beginners" and its completion is considered an important part of the OTIS experience. Evan has described it as "the most important unit in OTIS".

Equality is one of the only unit groups that has units in all three of B/D/Z levels.

## Philosophy

Nominally, a "find minimum" problem can usually be thought of as two halves:

1. Proving that <span class="math math-inline">f(x) \ge \lambda</span> for all <span class="math math-inline">x</span>, for some constant <span class="math math-inline">\lambda</span>, and
2. Finding an example of <span class="math math-inline">x&#95;0</span> such that <span class="math math-inline">f(x&#95;0) = \lambda</span>.

Equality pushes the philosophy that these two halves are not really separated. It advocates trying to predict the value of <span class="math math-inline">x&#95;0</span>, placing less importance on the value of <span class="math math-inline">\lambda</span>, and trying to use the predicted <span class="math math-inline">x&#95;0</span> to guide the estimates in the proof. One can discard any approach which does not preserve the equality case <span class="math math-inline">x&#95;0</span>; conversely, one should pay attention to any estimates that do preserve equality case at <span class="math math-inline">x&#95;0</span> even if they might seem silly.

Mentioned in particular is the so-called *Sharpness Principle*: if one succeeds in carrying out the first step in such a way that <span class="math math-inline">x&#95;0</span> has equality preserved in every estimate, then the second step will follow automatically. Thus one often need not take <span class="math math-inline">\lambda</span> itself into consideration when finding a proof.

## Notable problems

The unit features several problems which show off bizarre or outlandish sets of equality cases, and how finding these equality cases can be used to narrow down the correct approach. Some of these are mentioned below.

* [Taiwan Quiz 2014/3J/5](https://aops.com/community/p3551877): one of Evan's favorite problems.
* [Shortlist 2013 A4](https://aops.com/community/p3543362): iconic required problem on all versions of the unit.
* [Shortlist 2018 C5](https://aops.com/community/p12752820): one of the most instructive problems on how to use equality cases to narrow down the search for a solution.
* [Shortlist 2011 C7](https://aops.com/community/p2738027): a required problem on the ZCW version of equality, which is a dramatic example but also arguably one of the hardest required problems.
