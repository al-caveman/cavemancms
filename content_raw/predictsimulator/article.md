link: maybesimulator
url : https://www.scientificamerican.com/article/are-we-living-in-a-computer-simulation/
text:we _might_ be in a simulation

link:ligo
url:https://en.wikipedia.org/wiki/LIGO
text:Laser Interferometer Gravitational-Wave Observatory (LIGO)

link:uncountableset
url:https://en.wikipedia.org/wiki/Uncountable_set
text:uncountable set

image:7skies
url:https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Mohammed%C2%B4s_Paradise.jpg/220px-Mohammed%C2%B4s_Paradise.jpg
alt:Seven paradises
caption:An ancient dude's imagination of a 7 layered worlds view.  Was he
thinking \(m=-7\)?

footnote:future
text:This column is written in 2018.

# parent existence observatory (PEO)

As you might have already heard, [maybesimulator] right now.  In this column I
describe a test that lays the foundation for a principled approach to estimate
properties about the parent existence that is simulating us!

The shit herein is _pretty dope_ and opens new gates to a whole new class of
observatories.  If you think that the [ligo] was _freaking_ cool, then my shit
herein is _OMG mega freaking dope cool_ cool.

## how many nested simulations?

If we are in a simulation, we don't know whether the form of existence outside
this simulation is, _itself_, real either.  We might be in a pretty deep
recursion of simulations.

To simplify the language, let \(e_0\) be the form of existence that we refer to
as _"the universe''_, and \(e_{-1}\) be the form of existence that is hosting a
machine that is simulating the form of existence \(e_0\).

You may subjectively think that the form of existence \(e_{-1}\) is more real
than the one referred to by \(e_0\), but \(e_{-1}\) itself could also be
nothing but a yet another simulation in a yet grander parent form of existence
\(e_{-2}\).

Generally, for any \(i > m\), let \(e_i\) be a form of existence that is being
simulated in a machine in \(e_{i-1}\).  Let \(e_m\) be the master form of
existence that is not simulated by any other simulation.  If \(m = \infty\),
then the recursion of simulations keeps going on indefinitely.

Is the ancient concept of a multi-layered skies, or worlds, related to this
concept of nested simulations?  [7skies] shows an example of such ancient
imaginations that might suggest that \(m=-7\).

## what to know about \(e_{i-1}\)?

Basically we want to answer some binary questions about the existences \(e_0,
e_{-1}, \ldots, e_m\).  Let's put them in a matrix:

$$
\mathbf{Q} =
\begin{bmatrix}
    q_{e_0, 1} & q_{e_0, 2} & q_{e_0, 3} & \dots & q_{e_0, n} \\
    q_{e_{-1}, 1} & q_{e_{-1}, 2} & q_{e_{-1}, 3} & \dots & q_{e_{-1}, n} \\
    \vdots \\
    q_{e_m, 1} & q_{e_m, 2} & q_{e_m, 3} & \dots & q_{e_m, n} \\
\end{bmatrix}
$$

Obviously you can see that each row contains questions about a specific
existence.  Here are some examples for questions about existence \(e_{-1}\):
  
* Question \(q_{e_{-1}, 1}\): did \(e_{-1}\) simulate a child existence to test
  criminals in their existence?
* Question \(q_{e_{-1}, 2}\): did \(e_{-1}\) simulate a child existence to infer
  information their parent existence?
* ...

Then our _wish_ is to find the answers matrix:
$$
\mathbf{A} =
\begin{bmatrix}
    a_{e_0, 1} & a_{e_0, 2} & a_{e_0, 3} & \dots & a_{e_0, n} \\
    a_{e_{-1}, 1} & a_{e_{-1}, 2} & a_{e_{-1}, 3} & \dots & a_{e_{-1}, n} \\
    \vdots \\
    a_{e_m, 1} & a_{e_m, 2} & a_{e_m, 3} & \dots & a_{e_m, n} \\
\end{bmatrix}
$$

We can estimate answers in matrix \(\mathbf{A}\) by estimating the probability
\(\Pr(a_{j, j} = \text{Yes})\), for every answer in the matrix.  I.e.:
$$
\mathbf{\hat A} =
\begin{bmatrix}
    \hat\Pr(a_{e_0, 1}    = \text{Yes}) & \dots & \hat\Pr(a_{e_0, n} = \text{Yes}) \\
    \hat\Pr(a_{e_{-1}, 1} = \text{Yes}) & \dots & \hat\Pr(a_{e_{-1}, n} = \text{Yes}) \\
    \vdots \\
    \hat\Pr(a_{e_m, 1}    = \text{Yes}) & \dots & \hat\Pr(a_{e_m, n} = \text{Yes}) \\
\end{bmatrix}
$$


## how to find \(\hat\Pr(a_{i, j} = \text{Yes})\)?

The short answer is:  in a similar way to how people predict the future.  E.g.
some predict future stock market prices by analyzing past years (2018, 2017,
...).  It generally works for them, and their models offer answers notably
better than random-chance guessing.

The future stock market prediction works, because we have seen input from the
past years.  E.g.:

+ Analyze past data gathered from years 2010 and 2011, then hypothesize a model
  \(m_1\) about price changes.  Test \(m_1\) on year 2012.  
+ Analyze past data gathered from years 2010, 2011 and 2012, then hypothesize a
  model \(m_2\) by improving  \(m_2\).  Test \(m_1\) on data from year 2013.  
+ ...
+ Analyze past data gathered from years 2010, 2011, ...,  2018, then
  hypothesize a model \(m_6\) by improving  \(m_5\).  Use model \(m_6\) to
  predict the future that is 2019[future]!.  

But the problem with finding \(\hat\Pr(a_{i, j} = \text{Yes})\) is that we
currently lack any past observations.  Therefore, if we try to define
\(\mathbf{\hat A}\) now, with our little knowledge, it might look like this:

$$
\mathbf{\hat A_1} =
\begin{bmatrix}
    0.5 & 0.5 & \dots & 0.5 \\
    0.5 & 0.5 & \dots & 0.5 \\
    \vdots \\
    0.5 & 0.5 & \dots & 0.5 \\
\end{bmatrix}
$$

\(\mathbf{\hat A_1}\) is obviously pretty useless!

Here is my suggestion in PEO:

+ Using computers, or some machines, we run existence simulations.  E.g.
  imagine a large super computer simulating big bang, with some laws of
  physics.  We may try laws of physics similar to our's, or try random laws of
  physics for each simulation instance.  E.g. thousands of big bang
  simulations,each with their own laws of physics.
+ We observe the existences that form in the simulations.
+ Some of those simulations may develop intelligent life that, themselves, will
  create their own simulation (inside our super computers), and have their own
  big bangs!
+ We observe simulations in the simulations, too.  This way, we keep collecting
  information about existences \(e_{0+1}, e_{0+2}, \ldots\) that are children
  to our existence \(e_0\).  Since they are running in our supercomputers, we
  can also find the correct answers to questions, such as \(q_{e_1, 1}\).  Eventually, we end up creating a new questions matrix:
+ Then, observing all that, we create these matrices:
    $$
    \mathbf{Q_s} =
    \begin{bmatrix}
        q_{e_0, 1} & q_{e_0, 2} & q_{e_0, 3} & \dots & q_{e_0, n} \\
        q_{e_{1}, 1} & q_{e_{1}, 2} & q_{e_{1}, 3} & \dots & q_{e_{1}, n} \\
        \vdots \\
        q_{e_w, 1} & q_{e_w, 2} & q_{e_w, 3} & \dots & q_{e_w, n} \\
    \end{bmatrix}
    $$

    And also its answers matrix!
    $$
    \mathbf{A_s} =
    \begin{bmatrix}
        a_{e_0, 1} & a_{e_0, 2} & a_{e_0, 3} & \dots & a_{e_0, n} \\
        a_{e_{1}, 1} & a_{e_{1}, 2} & a_{e_{1}, 3} & \dots & a_{e_{1}, n} \\
        \vdots \\
        a_{e_w, 1} & a_{e_w, 2} & a_{e_w, 3} & \dots & a_{e_w, n} \\
    \end{bmatrix}
    $$

By analyzing \(\mathbf{Q_s}\) and \(\mathbf{A_s}\), we _may_ identify
patterns that link properties in child simulations against their parent
simulations.  We can also test the model using _train/validation/test_ splits.
Until we find an answering model that has an error that is low enough.  Let's
call this model \(\hat g\).

Finally, by running model \(\hat g\) on the original questions \(\mathcal{Q}\),
we get a better answers matrix \(\mathcal{\hat A_2}\):

$$
\mathbf{\hat A_2} =
\begin{bmatrix}
    0.55 & 0.49 & \dots & 0.38 \\
    0.51 & 0.5 & \dots & 0.43 \\
    \vdots \\
    0.5 & 0.5 & \dots & 0.5 \\
\end{bmatrix}
$$

There you go! By analyzing our universe, and child simulations of other
existences in our universe that we made, we might be able to answer questions
about the parent existence that is simulating us (if we are being simulated)!
