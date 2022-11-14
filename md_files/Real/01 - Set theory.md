# Def: Power set
Let \(X\) be a set. The collection $\mathcal{P} = \{ y : y\subseteq X\}$ is called **power set**.

# Def: Family/collection, sequence
Let $I\in\R$ be a set of indexes. A **family** of set induced by $I$ is $\{E_i\}_{i\in I}$. If $I=\Na$ we call this a **sequence**.

# Def: Monotone increasing (dec) seq.
We say a sequence is **monotone increasing** if 
$$
E_n\subseteq E_{n+1} \quad \forall n
$$
and we write $\{E\}\!\!\nearrow$. 

# Def: $\lim\inf$ and $\lim\sup$
Let $\p{E_n}$. We define
$$
\begin{aligned}
\lim\sup E_n = \bigcap^{\infty}_{n=1}\p{\bigcup^n_{k=1}E_k}\\
\lim\inf E_n = \bigcup^{\infty}_{n=1}\p{\bigcap^n_{k=1}E_k}
\end{aligned}
$$
and 
$$
\lim\sup E_n = \lim\inf E_n = \lim E_n
$$
>[!hint] 
>Sup in montagna

# Prop. of $\lim\sup E_n$ and $\lim\inf E_n$
1. $$\lim\sup E_n = \set{ x\in X : x\in E_n \text{ for inf. many indexes}}$$
2. $$\lim\inf E_n = \set{ x\in X : x\in E_n \text{ for all but finitely many indexes}}$$
3. $$\lim\inf E_n \subseteq \lim\sup E_n$$
4.  $$ \p{\lim\inf E_n}^C = \lim\sup E_n^C$$
5. If  $\{E\}\!\!\nearrow$  then $\exists \lim E_n = \bigcup^\infty E_n$
6. If  $\{E\}\!\!\searrow$  then $\exists \lim E_n = \bigcap^\infty E_n$
7. If $Q = \lim\inf E_n$ then $\chi_Q = \lim\inf \chi_{E_n}$ and the other way around.

# Def. Covering
Let $\{E_n\}$. If $A\subseteq\bigcup^\infty E_n$ we say that $\{E_n\}$ is a **cover** of $A$. If we can extract a sub-sequence such that the above holds we have a **subcover**.







