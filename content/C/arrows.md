+++
title = "Arrows"

[extra]
unit_id = "6"
subject = "C"
classification = "Combinatorics"
artist_name = "Alon Ragoler"
num_students = 836
num_submissions = 114
num_clubs = 5754
num_hearts = 2562
versions = ["DCW", "ZCW"]
description = '''
Some selected problems revolving around the idea that a function from a set to
itself can be thought of as a directed graph with all outdegrees equal to 1. In
particular, iterating such a function often involves looking at its cycle
decomposition.'''
+++

**Arrows** is a very satisfying combinatorics unit.
It is one of the combo units where not only combo problems appear.
As you can see, among the notable problems, there is a number theory problem, an algebra problem, and an FE.
The unit is about a technique of considering the arrow decomposition of a function from a set into itself.
There is a class of problems where this technique is useful, and this unit is a collection of such problems.

## Philosophy

Suppose we have a function $f$ from a set
$S$ to itself.
From high school math classes, you know that to analyze functions it is useful to look at their graphs.
When the function is defined on objects that are not numbers (and thus cannot be plotted on a number line),
we still can consider its "graph".

Imagine all the elements of $S$ on a plane (even if the set is infinite).
Then, for every element $x \in S$ imagine
drawing an **arrow** from $x$ to $f(x)$.
This way, we get a picture of a bunch of points connected by a bunch of arrows.
Exactly this picture is useful to consider when solving this class of problems.
For some cases, this picture will be "nice".
For example, if $f$ is a permutation of
$S$, then the picture is just a union of directed cycles.
Sometimes, when considering the "picture" it is possible to prove statements
like "this picture consists of only cycles" or "this picture consists of rays and cycles only".
Proving such statements are often the key steps when solving problems from this unit.

## Notable problems

In most of the problems, imagining everything in terms of arrows significantly
increases the chances of solving.

* [IMO 1987/4](https://aops.com/community/p366539): This is a functional equation.
  Solving it like a regular FE leads nowhere (i.e. plug and chug).
  Thinking in terms of arrows, however, makes life significantly easier.
* [Shortlist 2017 N3](https://aops.com/community/p10632346):
  This is a number theory problem in which thinking in terms of arrows is useful.
* [Shortlist 2017 A3](https://aops.com/community/p10632599):
  This is an algebra problem in which thinking in terms of arrows is useful.
* [Shortlist 2012 A6](https://aops.com/community/p3160555): A hard problem featuring many classical ideas.
* [IMO 2015/6](https://aops.com/community/p5083494): A classical arrows problem from a recent IMO.
