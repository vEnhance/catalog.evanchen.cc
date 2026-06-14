+++
title = "Ineq Standard"

[extra]
unit_id = "34"
subject = "A"
classification = "Algebra"
artist_name = "Shrrivathsa Mahesh"
num_students = 990
num_submissions = 189
num_clubs = 12803
num_hearts = 4680
versions = ["DAX"]
description = '''
Inequalities which can be approached using all the standard methods. This is
sort of a combination of Ineq Basic and Ineq Func.'''
+++
The **Ineq Standard** unit is basically what is as advertised: inequalities that you solve using standard methods. That's pretty much it, not much to talk about. These methods include:

- Homogenization/dehomogenization
- Basic substitutions

Well-known named inequalities like:

- AM-GM/Power-Mean
- Muirhead
- Cauchy/Hölder

And reappearances from [Ineq Func](/A/ineqfunc):

- Jensen/Karamata
- Tangent Line
- <span class="math math-inline">n-1</span> EV
- Isolated Fudging
- Smoothing

though the last three only show up in one or two practice problems. If you've done [Ineq Basic](/A/ineqbasic) and/or [Ineq Func](/A/ineqfunc), then you are certainly prepared for this unit, as there is some overlap between the problems and overall it's not too hard for a D unit. If you already have significant experience using these tools, then this unit will provide nothing new, though some more inequality practice probably wouldn't hurt. It might be a waste of time though, but who knows when Mount Inequality will erupt again.

## Philosophy

Like in all inequality units, there is a sort of philosophical talk about olympiad inequalities. There are two different types of difficulty: sharpness and tractability.

**Sharpness** is a measure of how tight the inequality is. That is, how close the LHS and RHS are to each other. For example, an inequality like Nesbitt's inequality,
<span class="math math-inline">\frac a{b+c}+ \frac b{c+a}+ \frac c{a+b}\ge\frac32</span>
is not very sharp. This is because the only equality case is when <span class="math math-inline">a=b=c</span> and generally there are many different methods that you can use to prove it. However,
<span class="math math-inline">\frac x{y+z}+\frac y{z+x}+\frac z{x+y}\ge\sqrt{\frac94+\frac32\cdot\frac{(y-z)^2}{xy+yz+zx}}</span>
is much, much stronger as the RHS of the above inequality is always in between <span class="math math-inline">\sum\frac a{b+c}</span> and <span class="math math-inline">\frac32</span>. ([Taken from MSE.](https://math.stackexchange.com/questions/1444352/stronger-than-nesbitt-inequality)) Sharper inequalities generally mean that you cannot naively apply inequalities like AM-GM or Cauchy. While certainly it may be possible using these tools, it won't be as straightforward.

The second type of difficulty is **tractability**, which is to say, how ugly the inequality looks. Take for instance [any](https://artofproblemsolving.com/community/c6h2977507p26691085) [sqing](https://artofproblemsolving.com/community/c6h2974462p26660669) [inequality](https://artofproblemsolving.com/community/c6h2970816p26623534). Here's another [example](https://artofproblemsolving.com/community/c6h2948867p26419126):
Let <span class="math math-inline">a>b\geq0</span> and <span class="math math-inline">a^3+b^5\leq a^2+b^2</span>. Prove that
<span class="math math-inline">5b+\frac{9}{a^2+b^2}>8.</span> You kinda just look at it, realize that you have no idea how to approach it, then wonder what the person who created the inequality was smoking. While the solution itself may not be too complicated, the cleverness involved in manipulating variables in a not so straightforward way is what gives the problem most of its difficulty.

## Notable Problems

- [IMO 2001/2](https://aops.com/community/p119168): One of the most famous olympiad inequalities, featuring as a walkthrough. While many ways to solve it exist, you will be tinkering with Hölder this time.
- MOP 2002. An instructive inequality with two parts. Highly recommend solving this one, and proceed with caution.
- [ELMO 2003/4](https://aops.com/community/p2887981): It's very clean. Captures the essence of wishful thinking.
- [IMO 2020/2](https://aops.com/community/p17821569): One of the most infamous olympiad problems from the last couple years, and not for being difficult. It is required so have fun and enjoy the problem.
- [Hong Kong TST 2019/1/6](https://aops.com/community/p10846227): This inequality might look pretty out there at first, but once you see what's going on, the idea is pretty nice. 
- [ISL 2016/A1](https://aops.com/community/p8639254): This is a very tough A1 in my opinion, and it is required. Don't feel bad if you need hints!
