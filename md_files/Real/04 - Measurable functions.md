# Def: counter image
Let $f:X\to Y$. Then it is well defined
$$
f^{-1}: \P(Y)\to\P(X)\quad B\mapsto f^{-1}(B)=\set{x\in X: f(x)\in B}
$$
# Prop. of counter image
1. $f^{-1}$ preserves union, intersection and complements
2. if $\N$ is a $\sa$ on $Y$ then $f^{-1}(\N)$ is a $\sa$ on $X$
# Def: measurable function
A function $f:(X,\M)\to(Y,\N)$ is said to be measurable if $$\forall B\in\N\quad f^{-1}(B)\in\M$$
# Prop. of measurable functions
1. check for measurability: Let $(X,\M)$ and $(Y,\N)$ measurable sets. Let $F\subseteq\P(Y)$ such that $\N=\sigma_0(F)$. Then $f$ is measurable if and only if $f^{-1}(E)\in\M\quad\forall E\in F$
2. continuity and measurability:
	1. Let $(X,d_x),(Y,d_y)$ two metric spaces. If $f:X\to Y$ is continuous then it is Borel-measurable. 
	2. Let $(Y,d_y)$ metric space. If $f:\R^n\to Y$ is continuous then it is Lebesgue-measurable. 
	3. composition and measurability: Let $(Z,d_z),(Y,d_y)$ two metric spaces, $(X,\M)$ measurable space. If $f:X\to Y$ is measurable and $g:Y\to Z$ is continuous, then $g\circ f:x\to Z$ is $(\M\mathcal{B}(Z))$-measurable.
3. binary function and measurability: Let $(X,\M)$ measurable space and $u,v:X\to\R$ measurable functions. Let $\Phi :\R^2\to Y$ be continuous with $(Y,d_y)$ metric space. Then $h(x)=\Phi(u(x),v(x))$ is $(\M,\mathcal{B}(y))$-measurable 
4. limits and measurability: Let $(X,\M)$ measurable space and $f_n:X\to\R^*$ measurable. Then $\sup,\inf,\lim\inf,\lim\sup,\lim$ are all measurable.
5. let $(X,\M)$, $A\subseteq X$ is measurable iff $\chi_A$ is measurable
6. $f$ measurable $\implies \abs{f}$ measurable
7. Let (X,\M,\mu) a complete measure space. Then
	1. $f:X\to\R$ measurable, $g=f$ ae on $X \implies$ $g$ measurable
	2. $f_n\to f$ as on $X$, $f_n$ measurable $\forall n \implies f$ measurable
# Def: simple/step functions
Let $(X,\M)$ a measurable space. We say that $s:X\to\R^*$ measurable is **simple** if $s(X)$ is finite. If this holds we can write $$
s(x) = \sum a_n\chi_{E_n}(x)
$$ and if each $E_n$ is a finite union of intervals we call $s$ a **step** function.

# Thm: approximation result
Let (X,\M) measurable space and $f:X\to[0,\infty]$ a measurable function. Then
$$ \exists \set{S_n} \text{ of simple function such that }s_1\leq...\leq s_n\quad \forall x\in X \text{ and } s_n(x)\to f(x)$$Moreover if $f$ is bounded the convergence is uniform on $X$.
