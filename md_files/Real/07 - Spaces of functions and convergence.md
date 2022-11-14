# Def: ae equivalence relation
We say $f\sim g\iff f=g$ ae. This is an equivalence relation. From this we get the following equivalence calss $$ [f] = \set{\hat f\in\L^1:f=\hat f \text { ae}}$$
# Def: $L^1$
$$ L^1(X)=\set{[f]:f\in\L^1(X)}=\L^1/\sim$$
This is a vector space and moreover with $d_1([f],[g]) = \int_X\abs{f-g}\dmu$ we got a metric space.
# Def: essentially bounded function
Let $f:X\to\R^*$ measurable. It is called essentially bounded if 
$$ \exists M>0 \quad \mu\p{\set{x\in X:\abs{f(x)}\geq M}} =0$$
# Def: essential supremum
If $f$ is essentially bounded it is well defined the essential supremum 
$$ess\sup_X f = \inf\set{M>0:f\leq M\text { ae on } X} = \inf\set{M>0:\mu\p{\set{f\geq M}}=0}$$
# Def: $\L^\infty$ and $L^\infty$
$$
\begin{aligned}
\L^\infty &= \set{f:X\to\R^*: f\text{ is measurable and ess. bounded}}\\
 L^\infty(X)&=\set{[f]:f\in\L^\infty(X)}=\L^\infty/\sim
\end{aligned}
$$
and they're both vector spaces. More over $(L^\infty,d_\infty)$ is a metric space with $d_\infty([f],[g]) = ess\sup\abs{f-g}$.
# Def: point-wise convergence
We say $f_n\to f$ point-wise (everywhere) on X if
$$
f_n(x)\to f(x)\quad\forall x\in X
$$

# Def: uniformly convergence
We say $f_n\to f$ uniformly on X if
$$
\sup_X\abs{f_n(x)-f(x)}\to 0\quad n\to\infty
$$

# Def: ae convergence
We say $f_n\to f$ ae on X if
$$
f_n(x)\to f(x)\quad\text{ae on }x\in X\iff\mu\p{\set{x\in X: \lim_n f_n \neq f \text{ or }\nexists}} = 0
$$

# Def: measure convergence
We say $f_n\to f$ in measure if
$$
\forall \alpha>0 \quad\lim_n\mu\p{\set{\abs{f_n-f}\geq \alpha} }=0
$$

# Def: $L^1$ convergence
We say $f_n\to f$ in $L^1$ on X if
$$
\int_X\abs{f_n-f}\dmu \to 0
$$

# Prop. of convergences
1. uniform $\implies$ point-wise $\implies$ ae
2. let $\mu(X)<\infty$ and $f_n\to f$ ae on $X$. Then $f_n\to f$ in measure on $X$.
3. let $\mu(X)<\infty$ and $f_n\to f$ in measure on $X$. Then $\exists\set{f_{n_k}}$ sub-sequence such that $f_{n_k}\to f$ ae on $X$.
4. let $f_{n}\subseteq L^1(X)$ and $f\in L^1(X)$. Then $f_n\to f$ in $L^1\implies f_n\to f$  in measure.
5. ae $\centernot\implies L^1$ and $L^1 \centernot\implies$ ae
6. $f_n\to f$ ae on $X$ and it exists a dominating function. Then $f_n\to f$ in $L^1$.
7. $f_n\to f$ in $L^1\implies\exists\set{f_{n_k}},w\in L^1$ such that $f_{n_k}\to f$ ae on $X$ and $\abs{f_{n_k}}\leq w(x)$ ae on $X$.

# Thm: Egorov-Severini
Let $\mu(X)<\infty$ and $f_n\to f$ ae on $X$. Then $$\forall\varepsilon>0\quad\exists X_\varepsilon\subseteq X\quad \mu\p{X\setminus X_\varepsilon}<\varepsilon,\,f_n\to f \text{ uniformly on } X_\varepsilon$$