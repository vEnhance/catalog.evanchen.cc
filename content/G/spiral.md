+++
title = "Spiral"

[extra]
unit_id = "51"
subject = "G"
classification = "Geometry"
artist_name = "Lum Jerliu"
num_students = 752
num_submissions = 113
num_clubs = 6792
num_hearts = 2608
versions = ["DGW"]
description = '''
Spiral similarity and Miquel points, following up chapter 10 of EGMO.'''
+++
**Spiral** is a D level unit about, unsurprisingly, spiral similarities and Miquel points. These two concepts show up very frequently in all types of geometry problems, ranging from easy to hard, [Config Geo](/G/configgeo) to [Weird Geo](/G/weirdgeo). Together with [Invert](/G/invert), these concepts can be thought as the bread and butter of olympiad geometry. If you've done both, or are feeling adventurous, try doing [Inversion and Spiral](/G/kansas), a Z unit which combines both topics into one unit. In terms of difficulty, this unit is fairly middle of the road for D units, but there are a couple tricky problems.

Note: if you've done all the problems in EGMO chapter 10, then there should be no new content for you, so you don't really need to request this unit. But it is a good practice set of problems to brush up on geo if you are rusty.

## Content

Say you have a quadrilateral <span class="math math-inline">ABCD</span>. If you intersect opposite sides, you get two more points, <span class="math math-inline">P=\overline{AB}\cap\overline{CD}</span> and <span class="math math-inline">Q=\overline{BC}\cap\overline{DA}</span>. You can think of these as the intersection of the diagonals of the self-intersecting quadrilaterals <span class="math math-inline">ACBD</span> and <span class="math math-inline">ADBC</span>. It turns out that 4 circumcircles in this diagram concur at a point <span class="math math-inline">M</span>, called the Miquel point. This point has a plethora of many different properties, the most basic of which is that it is the center of the spiral similarity that sends <span class="math math-inline">\overline{AD}\mapsto\overline{BC}</span>. If <span class="math math-inline">ABCD</span> is cyclic, <span class="math math-inline">M</span> has even more nice properties.

[image:5 align:left size:medium]
    Diagram from EGMO

This configuration is ubiquitous in olympiad geometry for how generic it is. It is like a chameleon, it can change into many different shapes and forms through self-intersecting and even degenerate cases, which can sometimes make it tough spot in the wild. Make sure you know it well!

## Advice

Because spiral sim and Miquel points are basically just abstracted away angle chasing, they aren't really that high powered. So you can often solve many problems using a different method like inversion, bypassing the spiral sim.

## Notable Problems

- [IMO 1979/3](https://aops.com/community/p367352): This problem is from 1979, yet it still finds a way to be quite tricky. It is required, so there's no way around the weird geo.
- T6POP: A very short and sweet problem that makes you feel nice after solving it.
- [TSTST 2013/4](https://aops.com/community/p3181482): This is a locus problem, something you don't see very often. It's quite the oddity.
- [December TST 2013/3](https://aops.com/community/p3161942): This is the final example problem in EGMO, and also appears in [Config Geo](/G/configgeo). Nonetheless, you can solve it here as well. But be warned, it's quite nontrivial.
