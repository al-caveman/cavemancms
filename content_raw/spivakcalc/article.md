axiom:axiomaddass
text : $a+(b+c) = (a+b)+c$.

axiom:axiomaddidentity
text :$a+0 = 0+a = a$.

axiom:axiomaddinverse
text :$a+(-a) = (-a)+a = 0$.

axiom:axiomaddcommutative
text :$a+b=b+a$.

axiom:axiommulass
text :$a(bc) = (ab)c$.

axiom:axiommulidentity
text :$a 1 = 1 a = a$.

axiom:axiommulinverse
text :$aa^{-1} = a^{-1}a = 1$, for all $a \ne 0$.

axiom:axiommulcommutative
text :$ab=ba$.

axiom:axiomdistributive
text :$a(b+c) = ab+ac$.

#spivak_calc_probs spivak's calculus chapter 1

For any numbers $a,b,c$:
[!axiomaddass]
[!axiomaddidentity]
[!axiomaddinverse]
[!axiomaddcommutative]
[!axiommulass]
[!axiommulidentity]
[!axiommulinverse]
[!axiommulcommutative]
[!axiomdistributive]

## problem 1

Prove these:

### If $ax=a$ for some number $a\ne 0$, then $x=1$

  _Proof---_ by using [axiommulinverse]:
  $$\begin{split}
    a^{-1}ax &= a^{-1}a\\
    1 x &= 1\\
  \end{split}$$
  
  By using [axiommulidentity]
  $$\begin{split}
    x &= 1\\
  \end{split}$$

$\blacksquare$

### $x^2 - y^2 = (x-y)(x+y)$

  _Proof---_ by using [axiomdistributive]:
  $$\begin{split}
    (x-y)(x+y) &= x(x-y)+y(x-y) \\
               &= (xx-xy)+(yx-yy) \\
               &= x^2-xy+yx-y^2 \\
               &= x^2-y^2 \\
  \end{split}$$

$\blacksquare$

### If $x^2 = y^2$, then $x=y$ or $x=-y$

  _Proof---_ by using the theorem we proved above:
  $$\begin{split}
    x^2         &= y^2 \\
    x^2 - y^2   &= 0 \\
    (x-y)(x+y)  &= 0 \\
  \end{split}$$

  Then we use [axiommulinverse] and multiply both sides by $(x+y)^{-1}$ or
  $(x-y)^{-1}$.  But since [axiommulinverse] is only defined for non-zero
  numbers, we need to state that those multiplications are for when $x+y\ne0$
  or $x-y\ne0$, respectively.  Hence we need to handle $x+y=0$ or $x-y=0$
  separately as well.

  * Case $x+y \ne 0$:

  Using [axiomaddidentity], [axiommulass], [axiommulidentity] and
  [axiommulinverse]:
  $$\begin{split}
    (x-y)(x+y)(x+y)^{-1}            &= 0(x+y)^{-1} \\
    (x-y)\big((x+y)(x+y)^{-1}\big)  &= 0(x+y)^{-1} \\
    (x-y) 1                    &= 0(x+y)^{-1} \\
    (x-y)                           &= 0 \\
    x                               &= 0 + y\\
    x                               &= y\\
  \end{split}$$

  This case says that, if $x+y\ne0$, then $x^2 = y^2$ would imply that $x=y$.

  Note: $a 0 = 0$ is not listed in the axioms, but can be proven using
  them:
  $$\begin{split}
    a 0 + a 0     &= a(0+0)\\
                            &= a  0 \\
    a 0 + a 0 + (-a0)  &= a 0 + (-a 0)\\
    a 0                &= 0\\
  \end{split}$$

  * Case $x+y = 0$:
  $$\begin{split}
    x+y   &= 0 \\
    x+y+(-y) &= 0 + (-y)\\
    x        &= -y\\
  \end{split}$$

  This case says that, if $x+y=0$, then $x^2 = y^2$ would imply that $x=-y$.

Since the 2 cases above, $x+y\ne0$ and $x+y=0$, are exhaustive, then we can
conclude that $x$ could _only_ be either $y$ or $-y$.

$\blacksquare$

### $x^3-y^3 = (x-y)(x^2+xy+y^2)$

Using [axiomdistributive] two times:

$$\begin{split}
    &(x-y)(x^2 + xy + y^2) \\
    &= (x-y)x^2 + (x-y)xy + (x-y)y^2\\
    &= (x-y)x^2 + (x-y)xy + (x-y)y^2\\
    &= xx^2-yx^2 + xxy-yxy + xy^2-yy^2\\
    &= x^3-yx^2 + x^2y-xy^2 + xy^2 - y^3\\
    &= x^3 - y^3\\
\end{split}$$

$\blacksquare$

### $x^n-y^n$ $=$ $(x-y)(x^{n-1}$ $+$ $x^{n-2}y$ $+$ $\ldots$ $+$ $xy^{n-2}$
$+$ $y^{n-1})$

I guess Spivak wants to say:
$$
x^n-y^n = (x-y)\left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)
$$

#### proof by deduction

Using [axiomdistributive]:
$$\begin{split}
& (x-y)\left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)\\
&= x\left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)
   -y\left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)\\
&= x\left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)
   -y\left(x^{n-n}y^{n-1} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i-1}\right)\\
&= x\left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)
   -y\left(x^{0}y^{n-1} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i-1}\right)\\
&= x\left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)
   -y\left(y^{n-1} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i-1}\right)\\
&= x\left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)
   -\left(y^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)\\
&= x\left(x^{n-1}y^{1-1} + \sum_{i=2}^{i=n} x^{n-i}y^{i-1}\right)
   -\left(y^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)\\
&= x\left(x^{n-1}y^{0} + \sum_{i=2}^{i=n} x^{n-i}y^{i-1}\right)
   -\left(y^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)\\
&= x\left(x^{n-1} + \sum_{i=2}^{i=n} x^{n-i}y^{i-1}\right)
   -\left(y^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)\\
&= \left(x^{n} + \sum_{i=2}^{i=n} x^{n-i+1}y^{i-1}\right)
   -\left(y^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)\\
&= \left(x^{n} + \sum_{i=1}^{i=n-1} x^{n-(i+1)+1}y^{(i+1)-1}\right)
   -\left(y^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)\\
&= \left(x^{n} + \sum_{i=1}^{i=n-1} x^{n-i-1+1}y^{i+1-1}\right)
   -\left(y^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)\\
&= \left(x^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)
   -\left(y^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)\\
&= x^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}
   - y^{n} - \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\\
\end{split}$$

Then using [axiomaddass]:
$$\begin{split}
& x^{n} + \sum_{i=1}^{i=n-1} x^{n-i}y^{i}
   - y^{n} - \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\\
&= x^{n}
   - y^{n}
   + \left(\sum_{i=1}^{i=n-1} x^{n-i}y^{i}
   - \sum_{i=1}^{i=n-1} x^{n-i}y^{i}\right)\\
&= x^{n}
   - y^{n}
   + \left(0\right)\\
&= x^{n}
   - y^{n}
\end{split}$$

$\blacksquare$


#### proof by induction

Let:
$$
f(x,y,n) = \left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)
$$

Then we can say (is this sub-proof perfect?):
$$\begin{split}
x^{n+1}-y^{n+1} &= (x-y)\left(\sum_{i=1}^{i=n+1} x^{(n+1)-i}y^{i-1}\right)\\
                &= (x-y)\left(
                        \begin{split}
                            &x^{(n+1)-(n+1)} y^{(n+1)-1}\\
                            &+ \sum_{i=1}^{i=n} x^{(n+1)-i}y^{i-1}
                        \end{split}
                    \right)\\
                &= (x-y)\left(
                        x^{0} y^{n}
                        + \sum_{i=1}^{i=n} x^{(n+1)-i}y^{i-1}
                    \right)\\
                &= (x-y)\left(
                        y^{n}
                        + \sum_{i=1}^{i=n} x^{(n+1)-i}y^{i-1}
                    \right)\\
                &= (x-y)\left(
                        y^{n}
                        + x\sum_{i=1}^{i=n} x^{n-i}y^{i-1}
                    \right)\\
                &= (x-y)\left(
                        y^{n}
                        + xf(x,y,n)
                    \right)\\
\end{split}$$

We can also rewrite what Spivak wants into:
$$
x^n-y^n = (x-y)\Big(y^{n-1} + xf(x,y,n-1)\Big)
$$

We've already proven in [spivak_calc_probs.1.2]:
$$\begin{split}
x^2-y^2 &= (x-y)(x+y)\\
        &= (x-y)\left(\sum_{i=1}^{i=2} x^{2-i}y^{i-1}\right)\\
        &= (x-y)\Big(y^{2-1} + xf(x,y,2-1)\Big)\\
\end{split}$$

Then, by induction, we prove that:
$$\begin{split}
x^2-y^2 &= (x-y)\Big(y^{2-1} + xf(x,y,2-1)\Big)\\
x^3-y^3 &= (x-y)\Big(y^{3-1} + xf(x,y,3-1)\Big)\\
\vdots\\
x^n-y^n &= (x-y)\Big(y^{n-1} + xf(x,y,n-1)\Big)\\
\end{split}$$

And since $(x-y)(y^{n-1} + xf(x,y,n-1))$ is only a rewrite of what Spivak
wants, i.e. $(x-y)(x^{n-1}$ $+$ $x^{n-2}y$ $+$ $\ldots$ $+$ $xy^{n-2})$.

$\blacksquare$

### $x^3 + y^3 = (x+y)(x^2 - xy + y^2)$

#### boring proof

Using [axiomdistributive] and [axiommulcommutative]
$$\begin{split}
    &(x+y)(x^2 - xy + y^2)\\
    &= (x+y)x^2 - (x+y)xy + (x+y)y^2\\
    &= (x^3+x^2y) - (x^2y+xy^2) + (xy^2+y^3)\\
    &= x^3 + x^2y - x^2y - xy^2 + xy^2 + y^3\\
    &= x^3 + y^3\\
\end{split}$$

$\blacksquare$

#### fun proof

First, let's prove that $(-a) (-b) = ab$, by using [axiomaddinverse],
[axiommulass] and [axiomdistributive]:

$$\begin{split}
    (-a) (-b) + (-ab)  &=(-a) (-b) + (-a) b \\
                          &=(-a) \big((-b) + b\big) \\
                          &=-a \times 0 \\
                          &=0\\
    (-a) (-b) + (-ab) + ab &= ab\\
    (-a) (-b) &= ab\\
\end{split}$$

Now we know that $(-y)^2 = y^2$. and:

$$\begin{split}
(-y)^3      &=      (-y)^2 (-y)\\
            &=      y^2 (-y)\\
            &=      -y^3\\
\end{split}$$


Then by substituting $y$ in the proof in [spivak_calc_probs.1.4] by $(-y)$ we
get:

$$\begin{split}
x^3 - (-y)^3    &= (x-(-y)) (x^2 + x(-y) + (-y)^2)\\
x^3 + y^3      &= (x + y) (x^2 - xy + y^2)\\
\end{split}$$

$\blacksquare$


## problem 2

What's wrong with this proof?  Let $x=y$, then:

$$\begin{split}
    x^2         &= xy\\
    x^2 - y^2   &= xy - y^2\\
   (x+y)(x-y)   &= y(x - y)\\
   x+y          &= y\\
   2y           &= y\\
   2            &= 1\\
\end{split}$$

_Answer:_

The steps:

$$\begin{split}
   (x+y)(x-y)   &= y(x - y)\\
   x+y          &= y\\
\end{split}$$

made use of multiplication of both sides by $(x-y)^{-1}$, which is undefined,
since $x=y$ implies $(x-y)^{-1} = 0^{-1}$.  Note [axiommulinverse] is not
defined for when $a=0$.


## problem 3

Prove the following.

### $\frac{a}{b} = \frac{ac}{bc}$, if $b,c\ne 0$

IMO Spivak wants to say $ab^{-1} = acb^{-1}c^{-1}$.

_Proof---_ Using [axiommulass]:

$$\begin{split}
    acb^{-1}c^{-1} &= ab^{-1}(cc^{-1})\\
\end{split}$$

Using [axiommulinverse]:

$$\begin{split}
    ab^{-1}(cc^{-1}) &= ab^{-1}(1)\\
\end{split}$$

Using [axiommulidentity]:

$$\begin{split}
    ab^{-1}(1) &= ab^{-1}\\
\end{split}$$

$\blacksquare$

### $\frac{a}{b}+\frac{c}{d} = \frac{ad+bc}{bd}$, if $b,d\ne 0$

IMO Spivak wants to say:

$$ab^{-1} + cd^{-1} = (ad+bc)b^{-1}d^{-1}$$

_Proof---_ Using [axiomdistributive]:

$$\begin{split}
    (ad+bc)b^{-1}d^{-1} &= adb^{-1}d^{-1}+bcb^{-1}d^{-1}\\
\end{split}$$

Using [axiommulass]:

$$\begin{split}
    adb^{-1}d^{-1}+bcb^{-1}d^{-1} &= ab^{-1}(dd^{-1}) + c(bb^{-1})d^{-1}\\
\end{split}$$

Using [axiommulinverse]:

$$\begin{split}
    ab^{-1}(dd^{-1}) + c(bb^{-1})d^{-1} &= ab^{-1}(1) + c(1)d^{-1}\\
\end{split}$$

Using [axiommulidentity]:

$$\begin{split}
    ab^{-1}(1) + c(1)d^{-1} &= ab^{-1} + cd^{-1}\\
\end{split}$$

$\blacksquare$


### $(ab)^{-1} = a^{-1}b^{-1}$, if $a,b\ne 0$

_Proof---_ If $a$ and $b$ are numbers, then their product, $(ab)$, is a number
too.

By [axiommulinverse], we know that:
$$(ab)(ab)^{-1}=1$$

We also know that the equality holds if we multiply both sides by the same
numbers[:I think we need axioms to define how equality works.  Maybe Spivak
will define equality axioms later on?  Dunno.]:

$$(ab)(ab)^{-1} a^{-1} b^{-1}=(1) a^{-1} b^{-1}$$

By applying [axiommulass] we get[:note we cannot pop $(ab)^{-1}$ and spread the
$-1$ exponent because there is no axiom for it, so we cannot apply
[axiommulass] on $(ab)^{-1}$.  The reason there is no axiom for it is because
of the fact that the exponent $-1$ has a special meaning used in
[axiommulinverse], and ---so far--- is not just a normal number]:
$$(aa^{-1}) (bb^{-1}) (ab)^{-1} =(1) a^{-1} b^{-1}$$

By applying [axiommulinverse] we get:

$$(1) (1) (ab)^{-1} =(1) a^{-1} b^{-1}$$

By applying [axiommulidentity] we get:

$$(ab)^{-1} = a^{-1} b^{-1}$$

$\blacksquare$


### $\frac{a}{b}\cdot \frac{c}{d} = \frac{ac}{db}$, if $b,d\ne 0$

IMO Spivak wants to say $(ab^{1})(cd^{-1}) = (ac)(db)^{-1}$.

_Proof---_ By proof in [spivak_calc_probs.3.3], the right hand becomes:

$$
(ac)(db)^{-1} = (ac)(d^{-1}b^{-1})
$$

By [axiommulass]:

$$
(ac)(d^{-1}b^{-1}) = (ab^{-1})(cd^{-1}) 
$$

$\blacksquare$


### $\frac{a}{b}/\frac{c}{d} = \frac{ad}{bc}$, if $b,c,d\ne 0$

IMO Spivak wants to say prove this:

$$
(ab^{-1})(cd^{-1})^{-1} = adb^{-1}c^{-1}
$$


#### intermediate proof to massage things a bit

_Proof---_ First let's prove that $(x^{-1})^{-1} = x$.

By [axiommulinverse] we know that:

$$\begin{split}
x^{-1} x &= 1\\
\end{split}$$

Since $x^{-1}$ is, itself, yet another number, then we can also apply
[axiommulinverse] to get:

$$\begin{split}
(x^{-1})^{-1} x^{-1} &= 1\\
\end{split}$$

Since both of the expressions equal $1$, we can put them in an equation:

$$\begin{split}
(x^{-1})^{-1} x^{-1} &= x^{-1}x\\
\end{split}$$

By multiplying both sides by $x$:

$$\begin{split}
(x^{-1})^{-1} x^{-1} x &= x^{-1}xx\\
\end{split}$$

By [axiommulass]:

$$\begin{split}
(x^{-1})^{-1} (x^{-1} x) &= (x^{-1}x)x\\
\end{split}$$

By [axiommulinverse]:

$$\begin{split}
(x^{-1})^{-1} (1) &= (1)x\\
\end{split}$$

By [axiommulidentity]:

$$\begin{split}
(x^{-1})^{-1} &= x\\
\end{split}$$

$\blacksquare$

#### actual proof

_Proof---_ By proof in [spivak_calc_probs.3.3], we can spread the exponent of
$(cd^{-1})^{-1}$ as follows:

$$\begin{split}
(ab^{-1})(cd^{-1})^{-1} = (ab^{-1})c^{-1}(d^{-1})^{-1}
\end{split}$$

By proof in [spivak_calc_probs.3.5.1]:

$$\begin{split}
(ab^{-1})c^{-1}(d^{-1})^{-1} = (ab^{-1})c^{-1}d
\end{split}$$

By [axiommulass]:

$$\begin{split}
(ab^{-1})c^{-1}d &= (ad)(b^{-1}c^{-1}) \\
                 &= adb^{-1}c^{-1} \\
\end{split}$$

$\blacksquare$

### if $b,d\ne 0$, then $\frac{a}{b} = \frac{c}{d}$ if and only if $ad = bc$.
also determine when $\frac{a}{b} = \frac{b}{a}$

IMO Spivak wants me to prove $ab^{-1} = cd^{-1}$ if and only if $ad = bc$ (of
course, $b,d\ne 0$), and then show all cases where $ab^{-1} = ba^{-1}$ is
possible.

_Proof---_ By multiplying both sides by $bd$:

$$
ab^{-1}bd = cd^{-1}bd
$$

By [axiommulass]

$$
a(b^{-1}b)d = c(d^{-1}d)b
$$

By [axiommulinverse]:

$$
a(1)d = c(1)b
$$

By [axiommulidentity]:

$$
ad = cb
$$

$\blacksquare$

## find all numbers $x$ for which

### $4-x < 3-2x$
