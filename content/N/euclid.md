+++
title = "Euclid Alg"

[extra]
unit_id = "15"
subject = "N"
classification = "Number Theory"
+++
**EuclidAlg** is one of the units that revolves around a particular instinct and has a certain philosophy.
Eulidean algorithm, remainder bounding and adjacent ideas are the topic of this unit.

## Philosophy

Suppose we are dealing with a divisibility $A \mid B$.
Then, we can do the following things:

1. Subtract a multiple of $A$ from $B$, and divisibility still holds
2. Throw out factors of $B$ that are coprime
   with $A$, and divisibility still holds.
3. If we end up with a situation where |RHS|<|LHS|, deduce that |RHS|=0.

In many number theory problems, this technique is useful.
Evan calls it "remainder bounding",
because we want to take the remainder of $B$
mod $A$ and compare it with $A$.

This unit is a collection of problems where this technique is useful.

## What you can take from this unit

If you want to get comfortable with solving most of the easy-medium level number theory problems,
you should master this instinct.

## Notable problems

There are many FEs where this philosophy is useful. Here are some of them.

* [Shortlist 2011 N3](https://aops.com/community/p2737651): A very interesting FEs from the IMO shortlist.
* [Shortlist 2013 N1](https://aops.com/community/p3544096):
  An easier problem from which beginners can understand remainder bounding.
* [Shortlist 2016 N6](https://aops.com/community/p8639255): This one is a nice ego booster.
* [Shortlist 2004 N3](https://aops.com/community/p169519):
  A typical FE where remainder bounding is a necessary technique.

Non-FE problems

* [HMMT 2017 A4](https://aops.com/community/p7710425):
  A nice problem from HMMT that demonstrates this philosophy well.
* [Shortlist 2016 N4](https://aops.com/community/p8639358): This is the crown example of remainder bounding.
