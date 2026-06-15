+++
title = "Homography"

[extra]
unit_id = "29"
subject = "G"
classification = "Geometry"
artist_name = "Nurtilek Duishobaev"
num_students = 716
num_submissions = 180
num_clubs = 10051
num_hearts = 4578
versions = ["DGY", "ZGY"]
description = '''
A less friendly and more abstract projective geometry unit, with an emphasis on
projective transformations. Most of the theorems will be stated with respect to
an arbitrary conic rather than a circle. Expect lots of Pascal. Includes
Desargues involution theorem (DIT) and its dual (DDIT).'''
+++

Perhaps more aptly named, _"Fancier/Advanced projective geometry"_,
the unit **Homography** talks in more detail about some of the powerful machineries from Projective geometry.
It discusses in depth how one motivates certain re-phrasings,
applications and ideas to make a problem more friendly from a projective standpoint; in turn,
making them more susceptible to the strong projective tools given to us (including but not limited to,
homographies).

If you've done [Harmonic](/G/harmonic) and found it not too hard, then DGY might be a good fit for you,
especially if you are a projective geometry enjoyer.
Though for most non-geo mains, this might be one of the hardest D units.
There is a bit of a jump in difficulty from Harmonic to Homography,
so good geometric intuition and some config knowledge is also helpful.
In particular, [Art School](/G/artschool) may help with this unit (not verified)
as you sometimes need to think about problems differently from a structural point of view.

## Philosophy

The title is clickbait, this unit is **not** about homography.
In reality, it covers a certain intuition and methodology of solving problems
that is quite unique and is not very well-known for how useful it is.

Recall that when a problem is purely projective, it can usually be annihilated by projective geometry tools.
So purely projective problems are good, but very rarely will one ever show up in plain sight.
However, this unit will teach you how to turn problems that _aren't_ purely
projective into problems that _are_ purely projective. There's two steps to this method:

1. First, translate as many "Euclidean conditions" into "projective conditions" as possible (e.g.
   parallel <span class="math math-inline">\mapsto</span> concurrent or
   concyclic <span class="math math-inline">\mapsto</span> coconic).
2. Use projective machinery, like Pascal, Pappus, Brocard, projection, homography,
   or even DDIT to finish off the purely projective problem.

Evan believes that if you have two or less "Euclidean conditions" in your problem,
you can actually ignore them completely when taking a homography!
While this might sound crazy, it is actually true most of the time.
The logic is that a general homography has 8 degrees of freedom,
and these roughly correspond to 2 euclidean conditions.

Finally, note that when doing write ups for the problems, remember to "think backwards,
write forwards." You don't need to include a whole paragraph about how you
reduced the problem to be purely projective, you can just write up step 2 directly once solving the problem.

## Theory

This unit, especially the practice problems, are quite theory heavy.
Therefore, it is highly recommended to have done Harmonic before this or be very
comfortable recognizing and citing Pascal, points at infinity stuff, harmonic quadrilaterals, and duality.

The unit itself elaborates more on homography (projective transformations) than in EGMO chapter 9,
which to be honest, wasn't a great explanation.
In addition, it also introduces _Desargues Involution Theorem_ and its dual aka DDIT.
The exposition is a bit terse,
so a supplemental like [MarkBcc168's DDIT
handout](https://artofproblemsolving.com/community/c6h1509866p8957048) may help with understanding.

## Notable problems

It seems like mid 2010s APMOs often had problems trivialized by projective geometry.

* [ISL 2015/G5](https://aops.com/community/p6622796):
  a difficult walkthrough that really shows how far you can go with the techniques discussed in the reading.
  Expect to spend quite some time on this one, as there are many points.
* Michael Villiers: a really striking example of how parallelism interacts with projective concepts.
  Please try to solve this problem without using an affine transform, it's worth it.
* [Serbia 2017/6](https://aops.com/community/p7978514): short and simple problem statement, with a short,
  technical, and elegant solution. Required on DGY.
* Poncelet's theorem: this is one of those problems that you might get stuck on for quite some time.
  It is quite tricky, but enough patience can bring it home.
* [2012 ELMO Shortlist A10](https://aops.com/community/p2728448):
  This is basically a Pascal's theorem exercise in the Z version.
