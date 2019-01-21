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
text :$a \cdot 1 = 1 \cdot a = a$.

axiom:axiommulinverse
text :$aa^{-1} = a^{-1}a = 1$, for all $a \ne 0$.

axiom:axiommulcommutative
text :$ab=ba$.

axiom:axiomdistributive
text :$a(b+c) = ab+ac$.

# spivak's calculus problems

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

+ If $ax=a$ for some number $a\ne 0$, then $x=1$.

  _Proof---_ by using [axiommulinverse]:
  $$\begin{split}
    a^{-1}ax &= a^{-1}a\\
    1\cdot x &= 1\\
  \end{split}$$
  
  By using [axiommulidentity]
  $$\begin{split}
    x &= 1\\
  \end{split}$$

+ $x^2 - y^2 = (x-y)(x+y)$.

  _Proof---_ by using [axiomdistributive]:
  $$\begin{split}
    (x-y)(x+y) &= x(x-y)+y(x-y) \\
               &= (xx-xy)+(yx-yy) \\
               &= x^2-xy+yx-y^2 \\
               &= x^2-y^2 \\
  \end{split}$$

+ If $x^2 = y^2$, then $x=y$ or $x=-y$.

  _Proof---_ by using the theorem we proved above:
  $$\begin{split}
    x^2         &= y^2 \\
    x^2 - y^2   &= 0 \\
    (x-y)(x+y)  &= 0 \\
  \end{split}$$

  Then we use [axiommulinverse] and multipiply both sides by, first
  $(x+y)^{-1}$, then later by $(x-y)^{-1}$.  But since [axiommulinverse] is
  only defined for non-zero numbers, we need to state that those
  multiplications are for when $(x+y)\ne0$ and $(x-y)\ne0$, respectively.
  Hence we need to handle $(x+y)=0$ and $(x-y)=0$ separately as well.

  * Case $(x+y) = 0$:
  $$\begin{split}
    x+y   &= 0 \\
    x+y+(-y) &= 0 + (-y)\\
    x        &= -y\\
  \end{split}$$

  * Case $(x-y) = 0$:
  $$\begin{split}
    x-y   &= 0 \\
    x-y+y &= 0 + y\\
    x        &= y\\
  \end{split}$$

  * Case $(x+y) \ne 0$:

  Using [axiommulinverse]:
  $$\begin{split}
    (x-y)(x+y)(x+y)^{-1}    &= 0(x+y)^{-1} \\
    (x-y)       &= 0 \\
    x           &= 0 + y\\
    x           &= y\\
  \end{split}$$

  * Case $(x-y) \ne 0$:

  Using [axiommulinverse]:
  $$\begin{split}
    (x-y)(x+y)(x-y)^{-1}    &= 0(x-y)^{-1} \\
    (x+y)       &= 0 \\
    x           &= 0 + (-y)\\
    x           &= -y\\
  \end{split}$$
