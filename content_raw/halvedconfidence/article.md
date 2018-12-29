link:maxentropyprinciple
url :https://en.wikipedia.org/wiki/Principle_of_maximum_entropy

#imo_our_confidence_should_halved imo our confidence should halved

When a human makes a claim $c$, almost all people try to find this probability
in order to find how likely the claim is:

$$
\Pr(c \text{ is right})
$$

But that seems a bit narrow-mined as it ignores our brain's error.  So let's
re-write it while accounting our brain's error:

$$
Pr(c \text{ right} \cap \text{brain right})
$$

Let's expand it:
$$
\begin{split}
    &\Pr(c \text{ right} \cap \text{brain right})\\
    &=\Pr(\text{brain right}) \Pr(c\text{ right } | \text{ brain right})\\
\end{split}
$$

Since "_is the brain right?_'' is a binary question, by
[maxentropyprinciple:the maximum entropy principle]:

$$\Pr(\text{brain right})=0.5$$

IMO we can't do any better than this, because how can we test whether our brain
is right by using the brain itself?  IMO there is always chances of us being
delusional.  So I think the maximum entropy principle is the best we have.

Another point is that it is trivial to see that the following is true, since a
claim $c$ being right is not dependant on whether our brain is right:

$$
\Pr(c\text{ right } | \text{ brain right}) = \Pr(c\text{ right })
$$

To wrap it up, the best our brain can hope for is:

$$
\begin{split}
    &\Pr(c \text{ right} \cap \text{brain right})\\
    &=\Pr(\text{brain right}) \Pr(c\text{ right } | \text{ brain right})\\
    &=\frac{1}{2} \Pr(c\text{ right } | \text{ brain right})\\
    &=\frac{1}{2} \Pr(c\text{ right})\\
\end{split}
$$

In other words, the biggest probability that _truely_ reflects our certainty
can never exceed $0.5$!

E.g. if our brain estimates that $\Pr(c\text{ right})=1$, which is the
strongest case of confidence, then:

$$
\begin{split}
    &\Pr(c \text{ right} \cap \text{brain right})\\
    &=\frac{1}{2} \Pr(c\text{ right})\\
    &=\frac{1}{2} \times 1\\
    &=\frac{1}{2}\\
\end{split}
$$
