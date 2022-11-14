# Def: integral and integrability for real valued functions
Let $(X,\M,\mu)$ a complete measure space. We say that $f:X\to\R^*$ measurable is integrable if $\int_X \abs f\dmu<\infty$. If this holds we define
$$
\int_Xf\dmu = \int_Xf^+\dmu - \int_Xf^-\dmu
$$

# Def: integral of real valued function over a domain
$$E\in\M \implies \int_E f\dmu = \int_X f\chi_E\dmu$$
# Def: Lebesgue space (integrable functions)
$$\L^1(X,\M,\mu) = \set{f:X\to\R^*: f\text{ is measurable}}$$
>[!note] Remark:
>$$f\in\L^1\implies \int_Xf\dmu<\infty$$

# Prop. of integrable functions
1. $\L^1$ is a vector space and integral is linear.
2. $f\in\L^1\iff\abs{f}\in\L^1\iff\text{ both }f^+,f^-\in\L^1$
3. triangular ineq.: $f\in\L^1\implies\abs{\int_X f\dmu}\leq\int_X\abs{f}\dmu$
4. $f\in\L^1\implies\mu\p{\set{\abs{f}=\infty}}=0$
5. $\set{f_n}\subseteq \L^1$ and $\sum^\infty\int_X\abs{f_n}\dmu<\infty$ then
	1. $\sum^\infty f_n$ converges ae on $X$
	2. $\sum^\infty f_n\in\L^1$
	3. $\int_X\p{\sum^\infty f_n}\dmu = \sum^\infty\int_X f_n\dmu$

# Thm: ae equality for $\L^1$ functions
Let f,g\in\L^1, then for a complete measure space we have
$$
f=g\text{ ae on } X\iff\int_X\abs{f-g}\dmu = 0\iff \int_Ef\dmu=\int_E g\dmu\quad\forall E\in\M
$$
# Thm: dominate convergence 
Suppose that for a $\set {f_n}$ measurable sequence from $X\to\R^*$ we have:
1. $f_n\to f$ ae on $X$
2. $\exists g:X\to\R^*, g\in\L^1(X)$ such that $\abs{f_n(x)}\leq g(x)\quad\text{ae on }X,\,\forall n$ 
Then:
1. $f\in\L^1(X)$
2. $$\lim_n\int_X\abs{f_n-f}\dmu = 0 \quad\quad\p{\implies \int_X f\dmu = \lim_n\int_X f_n\dmu}$$
# Thm: relation with R-integral
1. Let $f:I\to\R$ be R-integrable with $I$ closed and bounded interval. Then $f\in\L^1(I)$ and the two integrals coincide.
2. $f\in\mathcal{R}(X)\iff f \text{ cont on } x \text{ ae on } X$ with the $\lambda$ measure
3. Let $\mathcal{R}^g$ the generalized R-integrals. Let $a,b\in\R^g$ then
	1. $f\in\mathcal{R}^g\implies f \text{ is } \p{[a,b],\L([a,b])}\text{ measurable}$
	2. $f\geq 0 \implies f\in\L^1([a,b])$ and the two integral coincide
	3. $\abs{f}\in\mathcal{R}^g\implies f\in\L^1([a,b])$ and the two integral coincide
4.  if $f\in\mathcal{R}^g(a,b),\abs{f}\notin\mathcal{R}^g(a,b)$  the two integrals are not really related.