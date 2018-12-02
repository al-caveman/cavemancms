link:occamsrazor
url :https://simple.wikipedia.org/wiki/Occam%27s_razor
text:Occam's razor

link:occamsrazormath
url :https://en.wikipedia.org/wiki/Occam%27s_razor#Mathematical

quotation:occamsrazorquote
text     :More things should not be used than are necessary
author   :William of Ockham, 14th century

quotation:occamsrazorquotemath
text     :By definition, all assumptions introduce possibilities for error; if
          an assumption does not improve the accuracy of a theory, its only
          effect is to increase the probability that the overall theory is
          wrong.
author   :[occamsrazormath:Wikipedia]


#imo_occams_razor_is_abused imo [occamsrazor] is abused

IMO nothing is wrong with [occamsrazor] statement in [occamsrazorquote], so I
agree with it.

Here is another way to say [occamsrazorquote] but in more mathy terms:

[!occamsrazorquotemath]

##notabused a case where [occamsrazor] is _not_ abused

Before I show you how [occamsrazor] is abused, let me show you a case
where it is not abused.

Suppose that we want to predict how far would a 100kg stone travel after being
thrown by a catapult.  Then, someone proposes function
$$f : x_1,_2,\ldots,x_n \to [0, \infty]$$
where $x_1,x_2,\ldots,x_n$ are some input numbers that quantify things, such as
stone's mass, stone's shape, length of the catapult's arm, amount of force that
moves the arm, etc.

Suppose that $f$ is pretty accurate in predicting how far the stone would
travel, with an error that follows the normal distribution $N(\mu, \sigma^2)$.

Nice, right?  So now we can use the function $f$, feed it with input, and
pretty accurately get where the projectile would land.

But now imagine some other dude found that the $n^{th}$ input of $f$ was not
needed, so he came up with another function
$$g : x_1,_2,\ldots,x_{n-1} \to [0, \infty]$$
that needs 1 less input (no need for $x_n$), and is also exactly as accurate
with an error that follows the same normal distribution $N(\mu, \sigma^2)$.

As you see, the utility of $f$ is exactly identical to $g$'s, and hence the
extra complexity of $f$ due to it needing $n$ many arguments (instead of $n-1$
as in $g$), is _unnecessary_ complexity.

Hence, we can rightfully conclude that $g$ is a better model in explaining the
phenomenon than $f$.

##abused a case where [occamsrazor] _is_ abused

What if I tell you that, while $f$ needs an extra argument that $g$ does not
need:

* $f$ is _much faster_ when implemented in a computer, which allows calculating
  catapult's expected accuracy much faster in field, hence increasing its fire
  rate.
* The extra argument that only $f$ needs, i.e. $x_n$, is a constant specific to
  the catapult, and is easy to obtain.

In this case, $f$'s extra arguments is suddenly _not_ unnecessary any more
because the extra argument allows to increase the _utility_ of $f$ in a
scenario that we care about.  Therefore, IMO using [occamsrazor] here to reject
$f$ is wrong.

See, _utility_ is important.  If more things increase a thing's utility, then
those more things are no longer _unnecessary_, and hence [occamsrazor] does not
apply to them.

_Utility_ depends on the domain/scenario.  E.g. in the scenario of
[imo_occams_razor_is_abused.notabused] $f$'s more things is unnecessary, and
hence [occamsrazor] applies to eliminate $f$.  But in this section's scenario
$f$'s more things is not unnecessary and hence [occamsrazor] does not apply.

##isGodnoneed is believe in God unnecessary?

I agree that, say, physics' models probably don't need believe in God.  E.g. if
you give me an equation to model _gravity_ that somehow incorporates _believe
in God_ into it, then most likely your model has a unnecessary complexity over
the existing physics model for gravity, which lacks believe in God.

But does this mean that, _in all scenarios_, believe in God is an unnecessary
addition?  Simply because adding believe in God in some models, such as
physic's models for gravity, is unnecessary, it does not mean that believe in
God is unnecessary in virtually every other scenario.

E.g. $f$ is not virtually unnecessary in all scenarios.  $f$ was only
unnecessary in [imo_occams_razor_is_abused.notabused]'s scenario, but it was
totally necessary in [imo_occams_razor_is_abused.abused]'s scenario.

Therefore, if any person claims that _"believe in God is unnecessary.
Period!''_, then that person _must_ prove that there is virtually no scenario
at all where believe in God has any utility.

I have never seen any person manage to back the claim that "_there is no
scenario where God is necessary_''.  Therefore, by the same sciencey stuff they
claim they like, I hereby call their claims _unsubstantiated_.

## proof that believe in God is necessary

[imo_occams_razor_is_abused.isGodnoneed] showed how the claim "_believe in God
is unnecessary_'' is actually _unsubstantiated_.  In _this_ section, I will
take it further by showing you that it is actually  _false_.

theorem :believeGodnecessary
text    :Believe in God is necessary.

[!believeGodnecessary]

### [believeGodnecessary]'s proof

First let's define some basic tools[:IMO the tools are pretty fair and you
shouldn't face much unease accepting them.]:

link    :goodmore
url     :https://cave.mn/page/2/#what_is_good

link    :godoptiscope
url     :https://cave.mn/page/4/#God_extends_optimization_scope

link    :fornicationdivorce
url     :https://www.dailymail.co.uk/femail/article-4085758/Experts-reveal-sexual-partners-ve-determine-likely-DIVORCE.html

link    :singlemomsuicide
url     :https://www.webmd.com/baby/news/20030123/absent-parent-doubles-child-suicide-risk#1

link    :lgbtsuicide
url     :https://www.reuters.com/article/us-health-lgbt-teen-suicide/lgbt-youth-at-higher-risk-for-suicide-attempts-idUSKCN1MI1SL

link    :helllowerscrime
url     :https://www.huffingtonpost.com/2012/06/19/belief-in-hell-lowers-cri_n_1609247.html

link    :religiouswars
url     :https://en.wikipedia.org/wiki/Religious_war


definition  :necessary
text        :For a thing $a$ to be necessary, there must be a senario $s$ where
             $a$ has maximum utility over its alternative things.

definition  :utility
text        :For any scenario $s$, and for any pair of things $a$ and $b$,
             $a$'s utility is more than $b$'s in scenario $s$, if and only if
             $a$ achieves the goal of $s$ better than $b$.

axiom   :goal
text    :Our goal in reality/nature is to maximize what is good.

definition  :good
text        :A thing is good if it maximizes our survivability.
             [goodmore:Click here] for more info about this definition.

[!necessary] [!utility] [!goal] [!good] 

In order to prove [believeGodnecessary], all we need to do is to show that
there exists a scenario $s$ where believe in God has a higher utility than
otherwise.

Below is a list of scenarios where believe in God results in a higher
survivability of its followers (one is enough, but I show more):

* Statistics show that [fornicationdivorce:those who commit fornication
  increase their divorce risk by more than the double].

  Logically, it's no brainer to see that more divorce implies more kids that
  are raised by single-parents.  Statistics show that
  [singlemomsuicide:single-parented children are more than _twice_ as likely to
  commit suicide].

  As you know, Abrahamic religions forbid sin, and therefore this is a scenario
  where believing in the Abrahamic God results in saving some lives, aka
  maximizing the survivability.

  You may say, but what if parents never get married?  Well, stats show that
  they have even higher separation/dumping rate.  So.. really, the best way for
  your children is a proper Abrahamic marriage.

* [lgbtsuicide:LGBTs have increased suicide risk].  Obviously Abrahaic
  religions are against this faggy shit, and hence believing in the Abrahamic
  God helps saving lives (aka increasing survivability).

* [helllowerscrime:Believe in hell lowers the crime rate].  Obviously, another
  property of Abrahaic religion is hell.  This is why I also personally think
  "_hell_'' is a mercy, as it lowers all kinds of crime rate including
  homicide.  For those who complain about the Abrahamic God for having hell,
  think again.

* Believe in God extends our optimization scope, which allows us to
  be more likely to invest in _good_ very long-term projects that non-believers
  won' --- for more info [godoptiscope:read this].

* I can pull more, but I got tired.  So let's stop here.

On the other hand, I don't know any general statistics that show that
believe in the Abrahamic God is harmful.  You might be thinking of ISIS, or
religious wars.  But I have two points for you:

* ISIS exists in a proxy war situation and receives foreign funds, plus they
  themselves violate Abrahamic teachings as they kill innocents, even by
  Quranic standards.
* In the history of all wars, [religiouswars:religious wars make up _only_
  6.97% of them].  Meaning, non-religiousness resulted in much more wars.
  Meaning, religiousness correlate with reduced wars.

IMO it should be very clear that believe in the Abrahamic God increases our
survivability.  Then:

+ By [good] we can see that believe in the Abrahamic God is _good_.
+ By [goal] we can see that believe in the Abrahamic God allows us to meet _our
  goal_ better
+ By [utility] we can see that there is at least a scenario $s$ where believe
  in the Abrahamic God has _more utility_ than otherwise.
+ By [necessary] we can see that believe in the Abrahamic God is necessary.

Q.E.D.
