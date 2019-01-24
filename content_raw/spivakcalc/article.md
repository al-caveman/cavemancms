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

#spivak_calc_probs spivak's calculus problems

## chapter 1

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

### problem 1

Prove these:

#### If $ax=a$ for some number $a\ne 0$, then $x=1$

  _Proof---_ by using [axiommulinverse]:
  $$\begin{split}
    a^{-1}ax &= a^{-1}a\\
    1 x &= 1\\
  \end{split}$$
  
  By using [axiommulidentity]
  $$\begin{split}
    x &= 1\\
  \end{split}$$

#### $x^2 - y^2 = (x-y)(x+y)$

  _Proof---_ by using [axiomdistributive]:
  $$\begin{split}
    (x-y)(x+y) &= x(x-y)+y(x-y) \\
               &= (xx-xy)+(yx-yy) \\
               &= x^2-xy+yx-y^2 \\
               &= x^2-y^2 \\
  \end{split}$$

#### If $x^2 = y^2$, then $x=y$ or $x=-y$

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

#### $x^3-y^3 = (x-y)(x^2+xy+y^2)$

Using [axiomdistributive] two times:

$$\begin{split}
    &(x-y)(x^2 + xy + y^2) \\
    &= (x-y)x^2 + (x-y)xy + (x-y)y^2\\
    &= (x-y)x^2 + (x-y)xy + (x-y)y^2\\
    &= xx^2-yx^2 + xxy-yxy + xy^2-yy^2\\
    &= x^3-yx^2 + x^2y-xy^2 + xy^2 - y^3\\
    &= x^3 - y^3\\
\end{split}$$

#### $x^n-y^n$ $=$ $(x-y)(x^{n-1}$ $+$ $x^{n-2}y$ $+$ $\ldots$ $+$ $xy^{n-2}$
$+$ $y^{n-1})$

I guess Spivak wants to say:
$$
x^n-y^n = (x-y)\left(\sum_{i=1}^{i=n} x^{n-i}y^{i-1}\right)
$$

##### easy proof

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



##### hard proof

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

We've already proven in [spivak_calc_probs.1.1.2]:
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
wants, i.e. $(x-y)(x^{n-1}$ $+$ $x^{n-2}y$ $+$ $\ldots$ $+$ $xy^{n-2})$,
therefore Q.E.D already.
