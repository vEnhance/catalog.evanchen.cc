+++
title = "Local"

[extra]
unit_id = "40"
subject = "C"
classification = "Combinatorics"
+++
**Local** is about zooming into a small portion of a problem.
This includes things like smoothing and making perturbations.
Very often, local solutions are based on algorithms (which are based on heuristics).
When we are lazy, we use the _algo-extremal duality_ and write shorter solutions
by considering an extremal object (which usually correspond to the last step of our algorithm).
You may need a “global” quantity that shows you are making progress.
e.g., if you want to improve the grade that you see in your report card,
you use the greedy strategy “focus on the subject that you got the least marks in”.
But due to this, you are getting some marks lesser in other subjects that you earlier got.
To justify that you are performing better, you show your mom that your aggregate marks are increasing.

## Philosophy

The problem is usually symmetric: all the parts (a.k.a. protagonists) tend to be similar.
There are two main lines of thought. The first one:

1. Let me do something that makes partial progress towards the problem.
   (e.g., you want to choose a bunch of points, so you start by choosing any point).
2. You then analyze how many choices remain after your initial choice (e.g.,
   maybe the problem tells you that three or more points shouldn't be collinear.
   That may reduce your possible choices).
3. You repeat until stuck (**RUST**).

We may call the last strategy as “_expand your tiny world_”. The second line of thought is:

1. Wow, some cases of this problem are really easy.
2. Can I “push” (or _perturb_) the other cases so that they become like these easy cases?

This line of thought typically needs you to think of a way to perturb the
problem _that preserves the properties of the problem_ (so, au fond, similar to circular optimization).
We call this approach “_just fix it_”.

## Notable Problems

* **Putnam 2016 A5**: iconic portrayal of “expand your tiny world”.
  Don't be too quick to click, you need some group theory to understand the problem.
* **HMMT 2018 T6**: required problem in the DCW version.
  Rather than “expand your tiny world”, this is more like “watch your tiny world expand”.
* **MP4G 2010**: good example of an extremal solution motivated by greedy algorithmic heuristics.
* **Russia 2004**: Somewhat different in flavor than rest of the problems.
  This is like the first line of the intro, literally - zoom into a tiny portion.
* **USA TST 2017**: A five pointer on DCW and a very nice portrayal of local philosophy indeed.
