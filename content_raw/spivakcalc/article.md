axiom:axiomaddass
text : $a+(b+c) = (a+b)+c$

axiom:axiomaddidentity
text :$a+0 = 0+a = a$

axiom:axiomaddinverse
text :$a+(-a) = (-a)+a = 0$

axiom:axiomaddcommutative
text :$a+b=b+a$

axiom:axiommulass
text :$a(bc) = (ab)c$

axiom:axiommulidentity
text :$a \cdot 1 = 1 \cdot a = a$

axiom:axiommulinverse
text :$aa^{-1} = a^{-1}a = 1$

axiom:axiommulcommutative
text :$ab=ba$

axiom:axiomdistributive
text :$a(b+c) = ab+ac$

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

  _Proof---_ by using [axiommulinverse]:
  $$\begin{split}
    x^2        &= y^2 \\
    x^2x^{-1}  &= y^2x^{-1} \\
    x          &= y^2x^{-1} \\
  \end{split}$$
