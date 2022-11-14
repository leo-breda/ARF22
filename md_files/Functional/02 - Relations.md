# Def: Relation
A **relation between** $X,Y$ is a subset $R$ of $X\times Y$. We write $R\subseteq X\times Y$ and $xRy$ or $(x,y)\in R$.
# Def: Function
A **function** from $X$ to $Y$ is a relation that $\forall x\in X\quad \exists ! y\in Y$ such that $xRy$.
# Def: Equivalence relation
An **equivalence relation** is a relation such that is:
1. Reflexive
2. Symmetric
3. Transitive
# Def: Equivalence Class
An **equivalence class** of $x\in X$ for the relation $R\subseteq X\times Y$ is 
$$
E_x = \set{ y \in Y : xRy}
$$
# Prop. of equivalence class
We have the following:
$$
X = \bigcup_{x\in X} E_x
$$
and moreover they're disjoint.
# Def: Quotient set
We define:
$$
X/R = \set{ E_x : \text{ is an equivalence class for } x\in X \text{ with } R}
$$
