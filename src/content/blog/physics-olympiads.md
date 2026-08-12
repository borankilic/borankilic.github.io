---
title: Five Years of Physics Olympiad
description: What olympiad problems demand that syllabus problems do not, and what five years of them changed about the way I approach a physical system.
date: 2026-08-11
tags: [Physics, Problem solving, Olympiad]
draft: false
---

I competed in the Turkish National Physics Olympiad from 2018 to 2022. I started in my first year of
high school, at fourteen.

I should be clear about the circumstances, because they did a great deal of the work. My school was a
pilot school organised around science olympiad training in mathematics, biology, chemistry and physics.
We had teachers who knew the material properly and taught it regularly, and a university professor who
came in once a week. Very few students get that, and much of what follows is downstream of it rather
than of anything I did. What I can speak to is what the problems themselves demanded, and what changed
in how I work as a result.

## What an olympiad problem asks for

A syllabus problem is posed inside a chapter, and the chapter constrains the answer. The relevant law
has usually been named in the preceding pages, so the task reduces to recognising which template
applies and substituting into it.

An olympiad problem gives you a physical scenario — a rotating pendulum, a non-trivial circuit — along
with its geometry and parameters, and stops there. The remaining decisions are yours: how to model the
system, what behaviour to expect before you calculate anything, which laws are the economical ones to
impose, how to set up the resulting equations, and what the solution means once you have it. You are
not being directed, and the problem will not tell you when you have chosen badly.

Several consequences follow. The problems routinely combine topics that were taught separately, so the
partition of physics into chapters stops being useful. They are long, in the specific sense that the
solution is a chain of steps in which an early modelling error is not recoverable later. And the
algebra, which is usually the most time-consuming stage, is rarely the difficult one.

One convention matters more than it appears to. Olympiad problems are almost entirely symbolic; numbers
are substituted at the end, if at all. Working in symbols keeps the structure of the result visible —
which quantities appear, in what combination, and with what scaling — and that structure is what
transfers to the next system. A numerical answer tells you about one configuration; a symbolic one
tells you about the family it belongs to.

## A worked example: the wobbling washing machine

The problem I still return to modelled a washing machine as a cube of side *L* containing a cylindrical
cavity of radius *R*, with a rectangular rod fixed at the centre and rotating at angular frequency *ω*.
It asked for the maximum *ω* before the machine begins to wobble.

The first task is translation. *Wobbling* is not a mechanical quantity, and the problem does not define
it. The usable statement is that one edge of the cube loses contact with the ground — that is, the
normal force distributed over the base is driven to zero along one edge. Tipping about that edge then
becomes the condition to analyse: the rotating rod is an unbalanced mass, so in the frame of the machine
it contributes an inertial load that varies sinusoidally over each revolution, and the question is
whether its torque about the opposite bottom edge can exceed the restoring torque from the weight.

Writing the equations of motion is straightforward. Solving them is not — they admit no closed form, and
which curves you are comparing depends on the regime of *ω*. In some regimes the two relevant curves
intersect and in others they do not, which is exactly the structure you would expect from a threshold
problem, and exactly what makes it awkward to attack head-on.

The step that resolves it is to characterise the threshold rather than solve for it. At the critical
condition the two curves neither cross nor separate: they touch. Tangency is a double root, so instead
of solving one intractable equation you impose two simpler simultaneous ones — that the curves meet, and
that their slopes agree there. In this case the derivatives were algebraically far lighter than the
expressions they came from, and the system became tractable.

I find that worth recording because the insight was not additional physics. The mechanics was already on
the page. What was required was noticing that the boundary between two regimes has a cleaner
characterisation than either regime does — a substitution of one question for an equivalent, easier one.

## Working while stuck

Being stuck is the ordinary condition, not a sign that something has gone wrong. There were many
problems I never solved. The habit I settled on was to leave a problem deliberately and return days or
weeks later, which was more productive than any amount of continuous effort.

When a problem would not move, I worked backwards. The books gave final answers but not solutions, so I
would examine the form of the answer and ask what it implied: which quantities appear, which are absent,
how it behaves in limiting cases, what dimensional structure it has. From that I could usually
reconstruct a plausible set of governing equations and test whether they led there. The reconstruction is
the part with any value; the answer on its own has almost none.

The more useful lesson was about persistence, which this kind of training supplies in quantity without
teaching you where to point it. After long enough on one approach, I would stop being able to see the
problem from any other angle and would begin defending the method I had already invested in. Recognising
that state took me a long time. The remedy was not to push harder but to stop and return the following
morning, when a different formulation was often immediately available. Persistence and rigidity are
difficult to tell apart from the inside, and I do not think I ever fully learned to.

A great many days ended with nothing solved. Those days were frustrating, and I suspect they contributed
more than the productive ones.

## An unexpected route: the magnetron

One episode I have never been able to account for properly.

I was working on a magnetron — the component in a microwave oven that generates the microwaves — trying
to find the final velocity of the electrons. I was doing it directly: writing down the electric and
magnetic fields, resolving the motion into radial and tangential components, and grinding through the
resulting integrals. It was not converging on anything.

The resolution came in a dream, and it was that none of that was necessary — the problem yields to
conservation of energy and momentum. I woke in the middle of the night, wrote it down, and it was
correct.

The reason it works is worth stating, since it is the general lesson rather than a trick. The magnetic
force acts perpendicular to the velocity and therefore does no work, so the entire energy budget is set
by the electric potential difference the electron has traversed; that fixes the speed without any
reference to the path taken to acquire it. The symmetry of the configuration supplies a second conserved
quantity, and two scalar constraints are enough to determine what integrating the trajectory would have
given far more laboriously. Conservation laws are indifferent to the route between endpoints, which is
precisely why they are cheap when the route is complicated.

It has happened more than once, though never as usefully. I would not read much into the dream itself.
My suspicion is that it is what follows from holding a problem in mind continuously enough that some
part of the work proceeds without deliberate attention — and that its real contribution was permission
to abandon an approach I had committed to, which was the one thing I could not do while awake.

## What it gives you

There is a particular state that arrives when a system finally becomes clear, and it is the reason to do
any of this. It is closer to relief than to excitement. The system decomposes into parts that can be
held separately and reassembled at will, and it stops being something you are working against. What
makes it substantial is the contrast with the position you occupied an hour or a week earlier, when none
of it resolved.

The feeling after solving a hard problem is quieter than people expect. Relief, mostly, and something
like having set down a weight.

That was most of why I continued. There were practical reasons as well — additional credit on the
university entrance examination, and a scholarship — and it would be dishonest to leave them out.

## What carried into research

The habit that persisted is that I want to derive things concretely. I find it harder than most of my
colleagues to build on an assumption I have not checked or an equation I have not worked through myself.
Once something is written out from first principles I stop having reservations about it, and I am
considerably more confident in the measurement I am setting up.

The practical benefit is less about confidence than about control. When I can derive what a system
should do, I can predict what a modification will do and change the setup deliberately, rather than
reasoning by analogy with what a related experiment happened to do. I should say that this is not
uniformly an advantage: it is slower, and there are situations where a well-established result should
simply be used. Colleagues who are more comfortable proceeding on established ground often get there
first.

## Whether it is worth doing

I would recommend it to someone prepared for what it involves, which is not everyone and is not a
judgement about ability. It is demanding, and it is more isolating than it is usually described as being
— a considerable amount of time spent alone with a problem that is winning.

What I took from it was a tolerance for not knowing yet, and the habit of looking for another route
rather than concluding there isn't one. That generalises well beyond physics, and it is the part I still
rely on. I am reasoning from a single case and a fortunate set of circumstances, so I would not push the
recommendation further than that — but given the choice again, I would make the same one.
