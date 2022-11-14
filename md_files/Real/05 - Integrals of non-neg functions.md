# Def: Integral for simple functions
Let $(X,\M,\mu)$ a complete measure space and $s:X\to[0,\infty]$ a measurable simple function. Then we can write 
$$
s(x) = \sum a_n\chi_{D_n}(x)
$$
where $D_n$ are measurable, disjoint and their union is the whole $X$. Then $\forall E\in \M$ we have
$$
\int_E s\dmu = \sum_{D_n} a_n\mu(D_n\cap E)
$$
# Def: Integral for non-neg functions
Let $(X,\M,\mu)$ a complete measure space and $f:X\to[0,\infty]$ a measurable function. Then the lebesgue integral for $f$ over $E\in\M$ is 
$$
\int_Ef\dmu = \sup\set{\int_E s\dmu : 0\leq s\leq f,s \text{ is simple}}
$$
>[!note] Remark:
>1. if $f$ is simple the definitions are consistent
>2. If we have $(\Na,\P(\Na),\mu_c)$ then $f:\Na\to\R$ is just a sequence and the integral becomes a series $$\int_\Na f\,d\mu_c = \sum_{n=0}^\infty a_n$$

# Prop. of the Lebesgue integral for non-neg
1. $\int_E f\dmu = \int_X f\chi_E\dmu$
2. $\mu(E) = 0\implies \int_E f\dmu =0$
3. $E\subseteq F\implies \int_E f\dmu \leq\int_F f\dmu$
4. $f\leq g$ in $E\implies \int_E f\dmu \leq \int_E g\dmu$
5. the integral is linear:
	1. $\alpha\geq 0 \implies \int_E \alpha f\dmu = \alpha\int_E f\dmu$ 
	2. $\int_E (f+g)\dmu  = \int_E f\dmu  + \int_E g\dmu$ 
6. $s:X\to[0,\infty]$ a simple function, then $\phi:\M\to[0,\infty]$ defined as $\phi(E)=\int_E s\dmu$ is a measure.
7. $\int_X f\dmu<\infty\implies \mu\p{\set{f= \infty}} = 0$
# Prop:  Chebychev inequality
Let $c>0$ then $$\mu\p{\set{f\geq c}}\leq\frac1c\int_\set{f\geq c} f\dmu\leq\frac 1c\int_Xf\dmu $$
# Prop: Vanishing lemma: 
$$ \int _ E f\dmu=0\iff f= 0\text { ae on }E $$
This leads to for a complete measure space
$$
f=g \text{ ae on } X \iff \int_E f\dmu=\int_E g\dmu \quad \forall E\in\M
$$
# Def: integrable function
If $f:X\to [0,\infty]$ measurable has $\int_X f\dmu<\infty$ we say $f$ is **integrable**.
# Thm: Monotone convergence, Beppo-Levi
Let $f_ n:X\to [0,\infty]$ measurable. Suppose that:
1. $f_n\leq f_{n+1} \quad\forall x \in X \,\,\forall n$
2. $f_n\to f$ ae on $X$ 
Then$$ \int _ X f\dmu=\lim_n\int_X f_n\dmu$$
# Thm: corollary of Beppo-Levi
$$\int_X\p{\sum^\infty_{n=0}f_n}\dmu=\sum^\infty_{n=0}\int_X f_n\dmu $$
# Thm: Fatou's Lemma
Let $\{f_{n}\}$ be a sequence of measurable non-negative functions. Then
$$\int_X\lim\inf f_{n}\dmu\leq\lim\inf\int_Xf_{n}$$
and if $f_n\to f$ ae on $X$ we have
$$\int_X f\dmu\leq\lim\inf\int_Xf_{n}$$
# Thm: measures from integrals, Radon-Nykodym def.
Let $\Phi:X\to [0,\infty]$ measurable. If we define $\nu(E) = \int_E\Phi\dmu\quad\forall E\in\M$ we have:
1. $\nu$ is a measure
2. if $f:X\to [0,\infty]$ is measurable $\implies \int_X f\,d\nu = \int_X f\Phi\dmu$

If this holds we say that $\Phi$ is the RN-derivative of $\nu$ wrt to $\mu$ that is $\Phi = \frac{d\nu}{d\mu}$

# Def: absolute continuity of a measure
Let $\mu,\nu$ measures on $(X,\M)$. We say that $\nu$ is **absolutely continuous** wrt $\mu$ and we write $\nu<<\mu$ if $$ \mu(E) = 0\implies \nu(E) = 0
$$
# Lemma: on abs. continuity of measures
 $$\exists\frac{d\nu}{d\mu} \implies \nu<<\mu$$
# Thm: Radon-Nykodym
Let $\mu,\nu$ measures on $(X,\M)$, $\nu<<\mu$ and $\mu$ is $\sigma$-finite. Then it exists (unique ae on $X$) $\Phi:X\to [0,\infty]$ measurable that is $\Phi =\frac{d\nu}{d\mu}$ namely $\nu(E) = \int_E\Phi\dmu\quad\forall E\in\M$
