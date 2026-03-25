SMOOTH   
COMPACTIFICATIONS   
OF LOCALLY   
SYMMETRIC   
VARIETIES

Second Edition

# Smooth Compactifications of Locally Symmetric Varieties

Second Edition

The new edition of this celebrated and long-unavailable book preserves much of the content and structure of the original, which is still unrivalled in its presentation of a universal method for the resolution of a class of singularities in algebraic geometry. At the same time, the book has been completely re-typeset, errors have been eliminated, proofs have been streamlined, the notation has been made consistent and uniform, and an index and a guide to recent literature have been added.

The authors begin by reviewing, in Chapter I, key results in the theory of toroidal embeddings and by explaining examples that illustrate the theory. Chapter II develops the theory of open self-adjoint homogeneous cones and their polyhedral reduction theory. Chapter III is devoted to basic facts on hermitian symmetric domains and culminates in the construction of toroidal compactifications of their quotients by an arithmetic group. The final chapter considers several applications of the general results.

The book brings together ideas from algebraic geometry, differential geometry, representation theory and number theory, and will continue to prove of value for researchers and graduate students in these areas.

# Smooth Compactifications of Locally Symmetric Varieties

Second Edition

AVNER ASH Boston College

DAVID MUMFORD Brown University

MICHAEL RAPOPORT University of Bonn

YUNG-SHENG TAI Haverford College

With the collaboration of

PETER SCHOLZE University of Bonn

CAMBRIDGE UNIVERSITY PRESS   
Cambridge, New York, Melbourne, Madrid, Cape Town, Singapore,   
São Paulo, Delhi, Dubai, Tokyo

Cambridge University Press The Edinburgh Building, Cambridge CB2 8RU, UK

Published in the United States of America by Cambridge University Press, New York

www.cambridge.org Information on this title: www.cambridge.org/9780521739559

$©$ A. Ash, D. Mumford, M. Rapoport and Y. Tai 2010

This publication is in copyright. Subject to statutory exception and to the provision of relevant collective licensing agreements, no reproduction of any part may take place without the written permission of Cambridge University Press.

First published in print format 2010

ISBN-13 978-0-511-67345-0 eBook (EBL) ISBN-13 978-0-521-73955-9 Paperback

# Contents

Preface to the second edition page vii Preface to the first edition ix

# I Basics on torus embeddings; examples 1

1 Torus embeddings over the complex numbers 1   
2 The functor of a torus embedding 7   
3 Toroidal embeddings over the complex numbers 9   
4 Compactification of the universal elliptic curve 14   
5 Hirzebruch’s theory of the Hilbert modular group 25

# II Polyhedral reduction theory in self-adjoint cones 37

1 Homogeneous self-adjoint cones 3843   
2 Jordan algebras   
3 Boundary components and Peirce decompositions   
4 Siegel sets in self-adjoint cones   
5 Cores and co-cores   
6 Positive-definite forms in low dimensions

# III Compactifications of locally symmetric varieties 97

1 Tube domains and compactification of their cusps 97   
2 The structure of bounded symmetric domains 105   
3 Boundary components 123   
4 Siegel domains of the third kind 142   
5 Statement of the Main Theorem 159   
6 Proof of the Main Theorem 164   
7 An intrinsic form of the Main Theorem 176

# IV Further developments

# 189

1 Extension of differential forms to the cusps 189   
2 Projectivity of $\overline { { D / \Gamma } }$ 199   
Supplementary Bibliography 215   
Index 229

# Preface to the second edition

When CUP approached us with the proposal of a second edition to our book, we first consulted graduate students and younger colleagues to test this idea on them. Their enthusiastic response convinced us of the soundness of the proposition.

In order to keep this project within realistic bounds, we did not rewrite the book, but rather TEX-ed the original text and corrected mistakes that have come to our attention. We also smoothed somewhat the presentation and homogenized the notation. Finally, in order to increase its usability, we added an index.

So, all in all, this is still essentially the same book. In particular, the text of this new edition does not reflect the developments in the field in the last 30 years. To compensate for this, we added a guide to the more recent literature at the end of the book.

In this whole project we were assisted by Peter Scholze, who read the whole manuscript, corrected many mistakes, and helped us with the proof-reading. We thank him heartily. We also thank Y. May, who assisted us in TEX-problems.

We also thank all those who pointed out mistakes in the first edition and often indicated to us how to correct them: we are thus grateful to C.-L. Chai, E. Looijenga, R. Pink, Y. Namikawa, and I. Satake. Finally, we thank the staff of CUP, and particularly D. Tranah, for their expert cooperation.

Avner Ash, David Mumford, Michael Rapoport, Yung-sheng Tai.

# Preface to the first edition

Let $D$ be a bounded symmetric domain and let $\Gamma$ be a neat (see Ch. III, $\ S 7$ ) arithmetic subgroup of $\operatorname { A u t } ( D ) ^ { o }$ . The goal of this monograph is the construction of a family of non-singular† compactifications $\overline { { D / \Gamma } }$ of $D / \Gamma$ . This theory was announced and described in rough outline in [2]. Very similar ideas were developed independently by Satake in [3]. Both of us were following the path indicated by the work of Igusa when $\Gamma = \mathrm { S p } \left( 2 n , \mathbb { Z } \right)$ and by Hirzebruch when $\Gamma = \mathrm { S L } ( 2 , \mathcal { O } )$ , where $\mathcal { O } =$ integers in a real quadratic field.

Here is an outline of the monograph. Since this work builds heavily on [1] (referred to as TE I below), we review quickly some of these results and add some comments particular to the complex case in Ch. I, §§1–3. Then, in Ch. I, §§4,5, we describe smooth compactifications of two surfaces $D / \Gamma$ , in order to illustrate the general theory which follows (actually, in $\ S 4 , D$ is not bounded – it is $\Delta \times \mathbb { C } - { \bf s o }$ this is not strictly a special case). Chapter $\mathrm { I I }$ , by A. Ash, is devoted to self-adjoint homogeneous cones. The main result is a comparison of Siegel sets and polyhedral subcones inside such homogeneous cones. These results are essential for the construction of $\overline { { D / \Gamma } }$ . The construction itself is taken up in Ch. III. The final results require considerable notation to state, but may be found in Ch. III, §§5, 7. The principal technical contribution here is M. Rapoport’s calculation of the Satake topology on $D ^ { * } = D \cup$ (rat. boundary comp.) in terms of the presentation of $D$ as a Siegel domain of third kind, which is crucial to proving that our $\overline { { D / \Gamma } }$ is Hausdorff. The final chapter by Y. S. Tai adds two important results. Firstly, he applies the construction to prove that $D / \Gamma$ is a variety “of general type” in Kodaira’s classification when $\Gamma$ is small enough. Secondly, although our general $\overline { { D / \Gamma } }$ is only an analytic compactification of $D / \Gamma$ , he shows that many of these $\overline { { D / \Gamma } }$ ’s are indeed projective varieties.

One of the main obstacles in our research was that none of us were symmetric space specialists when we began, and, of course, roots are the name of the game throughout. For our sake as well as the reader’s, we thought it useful to include a considerable amount of expository material in the hope of making the monograph more self-contained. We were greatly aided by similar expository projects of P. Deligne and I. Satake, who graciously lent us their notes. In general, the expository sections emphasize the geometric aspects somewhat more than the references, and, in particular, develop the ideas in the form in which we need them. Experts can skim rapidly through Ch. II, §§1–3 (note, however, the very crucial tie-up between Pierce decompositions and split tori which appears to be new) and Ch. III, §§2–4 (note here the key role played by the intermediate open set $D ( F ) : D \subset D ( F ) \subset { \check { D } }$ , $D ( F ) = U ( F ) _ { \mathbb { C } } \cdot D$ , in the construction of the Siegel Domain realization).

I hope that the space $\overline { { D / \Gamma } }$ here constructed will have other applications in the theory of automorphic forms, e.g., to calculating invariants of the field $\mathbb { C } ( D / \Gamma )$ and the dimension of the spaces of automorphic forms. Besides these applications, the theory can hopefully be pushed further in three essential directions: (i) at least for $D = \mathrm { S p } ( 2 n , \mathbb { R } ) / K$ , extend it to a construction of a scheme $\overline { { D / \Gamma } }$ over $\mathbb { Z }$ ; (ii) to extend Hirzebruch’s proportionality theorems to the non-compact case; (iii) in view of the fact that the results describe concretely the degeneration of Hodge structures of a very special type – find an extension of them, combining the ideas of Ch. III, $^ { \ S 7 }$ with Schmid’s results on families of Hodge structures over $\mathring \Delta .$ , to describe asymptotically all families of Hodge structures on $( \mathring \Delta ) ^ { k }$ .

David Mumford

# Authorship of the various chapters

Chapter I: David Mumford   
Chapter II: Avner Ash   
Chapter III: Michael Rapoport and David Mumford   
Chapter IV: Yung-sheng Tai

# References

[1] G. Kempf, F. Knudsen, D. Mumford and B. Saint-Donat, Toroidal Embeddings I, Lecture Notes in Mathematics 339. Berlin: Springer 1972.†

[2] D. Mumford, A new approach to compactifying locally symmetric varieties, in Proceedings of the Tata Institute Colloquium, Jan. 1973, Oxford Univ. Press, 1975.

[3] I. Satake, On the arithmetic of tube domains, Bull. Amer. Math. Soc., 79 (1973), 1076-1094.

# I

Basics on torus embeddings; examples

# 1 Torus embeddings over the complex numbers

We wish to review here quickly some results of $\mathrm { T E ~ I ^ { \dagger } }$ and to give a more explicit description of the complex varieties obtained via certain real spaces of half the dimension.

Let $T$ be an algebraic torus, i.e., $T \cong \mathbb { G } _ { m } ^ { n }$ for some $n$ , and let

$$
M = \operatorname { H o m } \left( T , \mathbb { G } _ { m } \right) ,
$$

the character group of $T$ , and

$$
N = \mathrm { H o m } \left( \mathbb { G } _ { m } , T \right) ,
$$

the group of ‘one-parameter’ subgroups of $T$ (in the algebraic sense).

Then $M \cong \mathbb { Z } ^ { n }$ and $N \cong \mathbb { Z } ^ { n }$ , and there is a natural non-degenerate pairing $\left. \cdot , \cdot \right. : M \times N \longrightarrow \mathbb { Z }$ of determinant 1. All this is valid over any field $k$ . When $k = \mathbb { C }$ , however, $T$ can be described analytically as $\widetilde { T } / \pi$ , where $\widetilde { T }$ is a complex vector space and $\pi$ is a discrete subgroup, generating - - $\widetilde { T }$ over $\mathbb { C }$ and isomorphic to $\mathbb { Z } ^ { n }$ . Here $\widetilde { T }$ is the universal covering space of $T$ and $\pi$ is $\pi _ { 1 } ( T )$ acting on $\widetilde { T }$ via translations. Note, however, that for all $a \in \pi$ the map

$$
\begin{array} { r } { \widetilde { \phi } _ { a } : \mathbb { C } \longrightarrow \widetilde { T } \qquad } \\ { \lambda \longmapsto \lambda \cdot a } \end{array}
$$

induces a map

$$
\phi _ { a } : \mathbb { C } / \mathbb { Z } \longrightarrow \widetilde { T } / \pi = T \ ,
$$

and that $\mathbb { C } / \mathbb { Z } \cong \mathbb { G } _ { m }$ canonically via $\lambda \longmapsto \mathbf { e } ^ { 2 \pi \mathrm { i } \lambda }$ . Thus every $a \in \pi$ induces $\phi _ { a } \in N$ , and this is easily checked to be an isomorphism between $\pi$ and $N$ Thus $\pi$ is just $N$ up to a canonical identification. Since $\widetilde { T } = \pi \otimes \mathbb { C }$ , it follows that we have canonical maps:

(i) $N \cong$ the usual topological $\pi _ { 1 }$ of $T$ ;

(ii) $N \otimes \mathbb { C } \cong$ the universal covering space of $T$ ;

(iii) $( N \otimes \mathbb { C } ) / N \cong T$

We abbreviate $N \otimes \mathbb { C }$ by $N _ { \mathbb { C } }$ and $N \otimes \mathbb { R }$ by $N _ { \mathbb { R } }$

Next, in the isomorphism $N _ { \mathbb { C } } / N \cong T$ , consider the subgroup corresponding to $N _ { \mathbb { R } } / N$ : this a compact real torus, and is the maximal compact subgroup of $T$ . We denote it by $T _ { c }$ (short for “compact torus”). Moreover, $N _ { \mathbb { R } } \subset N _ { \mathbb { C } }$ has a natural complement, viz. $\mathrm { i } N _ { \mathbb { R } }$ , and, by quotienting, $\mathrm { i } N _ { \mathbb { R } }$ injects into $N _ { \mathbb { C } } / N$ . In other words, we get a canonical decomposition

$$
N _ { \mathbb { C } } / N \cong ( N _ { \mathbb { R } } / N ) \times ( \mathrm { i } N _ { \mathbb { R } } ) \ ,
$$

and hence (dividing by i in the second factor)

$$
T \cong T _ { c } \times N _ { \mathbb { R } } ~ .
$$

We denote the projection $T \longrightarrow N _ { \mathbb { R } }$ by “ord,” which is then defined by

$$
\mathrm { o r d } ( x + \mathrm { i } y \mathrm { m o d } N ) = y \mathrm { ~ , ~ f o r ~ a l l ~ } x , y \in N _ { \mathbb { R } } \mathrm { ~ . ~ }
$$

If $\alpha \in M$ , and ${ \mathfrak { X } } ^ { \alpha } : T \longrightarrow \mathbb { C } ^ { * }$ is the corresponding function (as in TE I, it is useful to think of $M$ as an additive group, and hence to adopt exponential notation for the characters regarded as functions on $T$ ), we obtain the formula

$$
\mathfrak { X } ^ { \alpha } ( x + \mathrm { i } \mathfrak { y } \mathrm { m o d } N ) = \mathrm { e } ^ { 2 \pi \mathrm { i } ( \langle \alpha , x \rangle + \mathrm { i } \langle \alpha , y \rangle ) } , \mathrm { f o r } \mathrm { a l l } x , y \in N _ { \mathbb { R } } ;
$$

hence

$$
| \mathfrak { X } ^ { \alpha } ( z ) | = \mathrm { e } ^ { - 2 \pi \langle \alpha , \mathrm { o r d } z \rangle } , \mathrm { f o r } \mathrm { a l l } z \in T .
$$

Next, in TE I, Ch. I, §1, we define embeddings of $T$ in normal affine varieties $X _ { \sigma }$ , with the action of $T$ on itself extending to an action of $T$ on $X _ { \sigma }$ , whenever $\sigma \subset N _ { \mathbb { R } }$ is a closed rational polyhedral cone not containing a line. Recall that

$$
X _ { \sigma } = \operatorname { S p e c } \mathbb { C } [ \dots , { \mathfrak { X } } ^ { \alpha } , \dots ] \alpha \in M \cap { \mathfrak { o } } \ ;
$$

here $\check { \sigma } \subset M _ { \mathbb { R } }$ is the dual cone to $\sigma$ , so $M \cap { \check { \sigma } }$ is a sub-semigroup of $M$ . In order to study convergence in the classical topology and other details on $X _ { \sigma }$ , it will be convenient to introduce here the topological space (in the classical, not Zariski, topology) obtained by dividing $X _ { \sigma }$ by $T _ { c }$ . This will look like $N _ { \mathbb { R } }$ with points at infinity added. Let us first construct these embeddings, which we call $N _ { \sigma }$ , of $N _ { \mathbb { R } }$ and then show there is a map ord $: X _ { \sigma } \longrightarrow N _ { \sigma }$ inducing a homeomorphism $X _ { \sigma } / T _ { c } \xrightarrow { \sim } N _ { \sigma }$ .

The simplest way to define $N _ { \sigma }$ is via a basis $\alpha _ { 1 } , \ldots , \alpha _ { m }$ of the semigroup $\check { \sigma } \cap M$ . Then define

$$
\begin{array} { r l } { i : N _ { \mathbb { R } } \longrightarrow \mathbb { R } _ { > 0 } ^ { m } , } & { } \\ { x \longmapsto \big ( \mathrm { e } ^ { - 2 \pi \langle \alpha _ { 1 } , x \rangle } , \ldots , \mathrm { e } ^ { - 2 \pi \langle \alpha _ { m } , x \rangle } \big ) , } \end{array}
$$

and let

$$
N _ { \sigma } = \mathrm { c l o s u r e ~ o f ~ i } N _ { \mathbb { R } } \mathrm { ~ i n ~ } \mathbb { R } _ { \ge 0 } ^ { m } .
$$

It is very easy to see that this space is independent of the choice of basis (check that if you add to the $\alpha _ { i }$ one more $\alpha$ , then $N _ { \sigma }$ does not change). If we let $N _ { \mathbb { R } }$ act on $\mathbb { R } ^ { m }$ by

$$
x \cdot ( y _ { 1 } , \ldots , y _ { m } ) = ( \mathrm { e } ^ { - 2 \pi \langle \alpha _ { 1 } , x \rangle } y _ { 1 } , \ldots , \mathrm { e } ^ { - 2 \pi \langle \alpha _ { m } , x \rangle } y _ { m } ) ,
$$

then $N _ { \sigma }$ is the closure of the orbit of $( 1 , 1 , \ldots , 1 )$ . In particular, $N _ { \mathbb { R } }$ acts on $N _ { \sigma }$ , extending its action on itself by translation. Exactly as in the theory of torus embeddings (see TE I, Ch. I, $\ S 1$ , Theorem 2), we can decompose $N _ { \sigma }$ into $N _ { \mathbb { R } }$ -orbits; these will correspond bijectively to the faces of $\sigma$ , and each one will contain a unique point $\left( y _ { 1 } , \ldots , y _ { m } \right)$ with $y _ { i } = 0$ or 1 for all $i$ . Explicitly, for every face $\tau$ of $\sigma$ , the corresponding orbit is:

$$
{ \cal O } ( \tau ) = \left\{ ( y _ { 1 } , . . . , y _ { m } ) \in N _ { \sigma } \mid _ { y _ { i } } ^ { y _ { i } = 0 \mathrm { i f } \alpha _ { i } > 0 \mathrm { o n I n t } \tau } \right\}
$$

where

$$
\varepsilon _ { i } = \left\{ \begin{array} { l l } { { 0 } } & { { \mathrm { i f } \alpha _ { i } > 0 \mathrm { o n } \mathrm { I n t } \tau } } \\ { { 1 } } & { { \mathrm { i f } \alpha _ { i } \equiv 0 \mathrm { o n } \mathrm { I n t } \tau . } } \end{array} \right.
$$

This can be proven following TE I, substituting the following lemma for the use of $k [ [ t ] ]$ .

Lemma 1.1 If $\{ x _ { k } \}$ is a sequence in $N _ { \mathbb { R } }$ and $S \subset \{ 1 , \ldots , m \}$ satisfies

$$
\begin{array} { r l r } & { } & { \underset { k \longrightarrow \infty } { \operatorname* { l i m } } \alpha _ { i } ( x _ { k } ) = \lambda _ { i } , i \in S , } \\ & { } & { \underset { k \longrightarrow \infty } { \operatorname* { l i m } } \alpha _ { i } ( x _ { k } ) = \infty , i \notin S , } \end{array}
$$

then

(a) there is some $y \in N _ { \mathbb { R } }$ with $\alpha _ { i } ( y ) = 0$ for $i \in S$ ; $\alpha _ { i } ( y ) > 0$ for i ∈/ S ;   
(b) there is some $z \in N _ { \mathbb { R } }$ with $\alpha _ { i } ( z ) = \lambda _ { i }$ for $i \in S$ .

Proof Left to reader.

Now if we map $X _ { \sigma }$ into $\mathbb { R } _ { \geq 0 } ^ { m }$ as follows:

![](images/4cc8e012334f17452327ed9b511f0a97c6746e7d3830a26024e7b50ee63ce271.jpg)

$$
f ( \boldsymbol { x } ) = ( | \mathfrak { X } ^ { \alpha _ { 1 } } ( \boldsymbol { x } ) | , \dots , | \mathfrak { X } ^ { \alpha _ { m } } ( \boldsymbol { x } ) | ) ,
$$

we get a commutative diagram. Since $T$ is dense in $X _ { \sigma }$ , it follows that $f$ defines a map

$$
\operatorname { o r d } : X _ { \sigma } \longrightarrow N _ { \sigma }
$$

and that or $ ( g x ) = \operatorname { o r d } ( x )right.$ for all $g \in T _ { c }$ . Conversely, if $\mathrm { o r d } ( x _ { 1 } ) = \mathrm { o r d } ( x _ { 2 } )$ , it follows that $| \mathfrak { X } ^ { \alpha } ( x _ { 1 } ) | = | \mathfrak { X } ^ { \alpha } ( x _ { 2 } ) |$ for all $\alpha \in \check { \sigma } \cap M$ , from which it follows readily that $x _ { 1 } = g x _ { 2 }$ for some $g \in T _ { c }$ . Note that if $\mathbb { O } ^ { \tau } \subset X _ { \sigma }$ is the orbit corresponding to $\tau$ , then ord $^ { - 1 } ( O ( \tau ) ) = \mathbb { O } ^ { \tau }$ .

For some purposes, it is convenient to have a coordinate-invariant way of describing $N _ { \sigma }$ as $N _ { \mathbb { R } }$ plus a set of ideal points at infinity. To describe $N _ { \sigma }$ this way, for every face $\tau$ of $\sigma$ , let

$$
L ( \tau ) = { \mathrm { s m a l l e s t ~ l i n e a r ~ s p a c e ~ c o n t a i n i n g ~ } } \tau ~ .
$$

Then $L ( \tau )$ is the stabilizer of $\varepsilon _ { \tau }$ , so we get:

$$
\begin{array} { r l r } & { } & { N _ { \mathbb { R } } / L ( \tau ) \xrightarrow { \sim } O ( \tau ) } \\ & { } & { x \longmapsto x \cdot \varepsilon _ { \tau } ~ . } \end{array}
$$

Let $x + \infty \cdot \tau \in N _ { \sigma }$ denote $x \cdot \varepsilon _ { \tau }$ (where $x _ { 1 } + \infty \cdot \tau = x _ { 2 } + \infty \cdot \tau$ if and only if $x _ { 1 } - x _ { 2 } \in L ( \tau ) )$ . The reason for this notation is as follows: decompose   $N _ { \mathbb { R } } =$ $N _ { \mathbb { R } } ^ { \prime } \oplus L ( \tau )$ , choose any sequence $x _ { n } = y _ { n } + z _ { n } \in N _ { \mathbb { R } } = N _ { \mathbb { R } } ^ { \prime } \oplus L ( \tau )$ , and choose any $y \in N _ { \mathbb { R } } ^ { \prime }$ . Then one sees easily that

$$
\left[ \operatorname* { l i m } _ { n \longrightarrow \infty } x _ { n } = y + \infty \cdot \tau \operatorname { i n } N _ { \sigma } \right] \Longleftrightarrow \left[ \begin{array} { c } { \displaystyle \operatorname* { l i m } _ { n \longrightarrow \infty } y _ { n } = y \mathrm { ~ a n d , f o r ~ e v e r y } } \\ { w \in L ( \tau ) , z _ { n } \in \tau + w \mathrm { ~ i f ~ } n \gg 0 . } \end{array} \right]
$$

Heuristically, we have added a lower-dimensional vector space isomorphic to $N _ { \mathbb { R } } / L ( \tau )$ of ideal points $x + \infty \cdot \tau$ obtained by starting at $x$ and moving out to

infinity in the direction determined by the cone $\tau$

![](images/c01ce76e2cd74158ec04cd7144b17e01d8b0b48f55b6125f976e456f38dafc4d.jpg)

Our convergence condition may be rephrased by saying that a fundamental system of neighborhoods of $y + \infty \cdot \tau$ in $N _ { \mathbb { R } }$ is given by

$$
U _ { \varepsilon , w } ^ { 0 } ( y + \infty \cdot \tau ) = y + w + B _ { \varepsilon } + \tau ,
$$

for any $w \in L ( \tau )$ and any $\varepsilon > 0$ , where $B _ { \varepsilon }$ denotes the $\varepsilon$ -ball around 0 (take any metric on $N _ { \mathbb { R } }$ ). More generally, with this notation, a fundamental system of neighborhoods of $y + \infty \cdot \tau$ in $N _ { \sigma }$ is given by

$$
U _ { \varepsilon , w } ( y + \infty \cdot \tau ) = U _ { \varepsilon , w } ^ { 0 } ( y + \infty \cdot \tau ) \cup \bigcup _ { \tau ^ { \prime } \mathrm { ~ f a c e ~ o f ~ } \tau } ( y + w + B _ { \varepsilon } + \tau + \infty \cdot \tau ^ { \prime } ) .
$$

For instance, if $N _ { \mathbb { R } } = \mathbb { R } ^ { 2 }$ and $\sigma$ is the positive quadrant, we get the following

picture:

![](images/8794dad9523d73cb219d1dcc1759d39e0190be420553d6d99781f3e95fd4987a.jpg)

Next recall that in TE I, Ch. I, §2, we glue the affine varieties $X _ { \sigma }$ together: whenever $\{ \sigma _ { \alpha } \}$ is a rational partial polyhedral decomposition of $N _ { \mathbb { R } }$ , meaning (i) if $\sigma$ is a face of $\sigma _ { \alpha }$ , then $\sigma = \sigma _ { \beta }$ , for some $\beta$ ; (ii) for all $\alpha , \beta$ , the cone $\sigma _ { \alpha } \cap \sigma _ { \beta }$ is a face of $\sigma _ { \alpha }$ and $\sigma _ { \beta }$ , then we can glue the $X _ { \sigma _ { \alpha } }$ together, obtaining a scheme $X _ { \{ \sigma _ { \alpha } \} }$ . In TE I, we asked that $\{ \sigma _ { \alpha } \}$ be a finite set, so that $X _ { \{ \sigma _ { \alpha } \} }$ was a variety. This is in fact totally irrelevant: for any set $\{ \sigma _ { \alpha } \}$ as above, we get an $X _ { \{ \sigma _ { \alpha } \} }$ as before, except that it may require an infinite number of affines to cover it. Now $X _ { \{ \sigma _ { \alpha } \} }$ is always a separated normal irreducible scheme, locally of finite type over $\mathbb { C }$ and containing $T$ as an open dense subset. In exactly the same way, we glue the $N _ { \sigma _ { \alpha } }$ together into a topological space $N _ { \{ \sigma _ { \alpha } \} }$ , which is $N _ { \mathbb { R } }$ plus a large number of ideal vector spaces situated at infinity in many different directions. Moreover, we glue the ord maps together into one map:

$$
\mathrm { o r d } : X _ { \{ \sigma _ { \alpha } \} } \longrightarrow N _ { \{ \sigma _ { \alpha } \} } \ .
$$

For instance, $X _ { \{ \sigma _ { \alpha } \} }$ , as a set, is the disjoint union of $T$ -orbits $\mathbb { O } ^ { \sigma _ { \alpha } }$ , one for each $\alpha$ ; likewise $N _ { \{ \sigma _ { \alpha } \} }$ as a set is the disjoint union of $N _ { \mathbb { R } }$ -orbits $O ( \sigma _ { \alpha } )$ , one for each $\alpha$ , and ord $^ { - 1 } ( O ( \sigma _ { \alpha } ) ) = \mathbb { O } ^ { \sigma _ { \alpha } }$ .

# 2 The functor of a torus embedding

In order to make some of our later constructions of compactifications $D / \Gamma$ purely algebraic and valid for schemes over any ground fields, it will be useful to learn what functor a torus embedding represents. This also gives us another view of what torus embeddings are. First some notations and definitions.

(1) If $s$ is a scheme and $X$ is a set, $X _ { S }$ denotes the constant sheaf on $s$ with stalk $X$ .   
(2) Every semigroup or sheaf of semigroups will have an identity element $e$ or identity section $e$ .   
(3) If $\operatorname { \cal { A } } _ { 1 } , \operatorname { \cal { A } } _ { 2 }$ are semigroups, a homomorphism $\phi : A _ { 1 } \longrightarrow A _ { 2 }$ is called strict if $\phi ( e _ { 1 } ) = e _ { 2 }$ and $\phi ( x )$ invertible implies $x$ invertible. If $A _ { 1 } , A _ { 2 }$ are sheaves of semigroups on $s$ , we require that, for every $s \in S$ , the map on stalks $\phi _ { s } : A _ { 1 , s } \longrightarrow A _ { 2 , s }$ is strict.

(4) If $s$ is a scheme, then ${ \mathcal { O } } _ { S } ^ { ( \times ) }$ will be the semigroup sheaf ( ${ \mathcal { O } } _ { S }$ , mult.).

The result is:

Theorem 2.1 Let $T$ be a torus over $k$ and $T \subset X _ { \{ \sigma _ { \alpha } \} }$ a torus embedding, where $\sigma _ { \alpha } \subset N ( T ) _ { \mathbb { R } }$ are polyhedral cones. For any $k$ -scheme $s$ , let $F _ { \{ \sigma _ { \alpha } \} } ( S )$ be the set of pairs $( \Sigma , \pi )$ consisting of a sub-semigroup sheaf $\Sigma \subset M ( T ) _ { S }$ and a strict homomorphism $\pi : \Sigma \longrightarrow { \mathcal { O } } _ { S } ^ { ( \times ) }$ such that, for all $s \in S$ , we have $\Sigma _ { s } = \check { \sigma } _ { \alpha } \cap M ( T )$ for some $\alpha$ . Then there are canonical isomorphisms, functorial in $k$ -schemes $s$ :

$$
\mathrm { H o m } _ { k } ( { \cal S } , X _ { \{ \sigma _ { \alpha } \} } ) \cong F _ { \{ \sigma _ { \alpha } \} } ( { \cal S } ) \ .
$$

Proof We first show how to associate a pair $( \Sigma , \pi )$ to a morphism $f : S \longrightarrow$ $X _ { \{ \sigma _ { \alpha } \} }$ . Define:

$$
\begin{array} { r l } & { U _ { \alpha } = f ^ { - 1 } ( X _ { \sigma _ { \alpha } } ) \ , } \\ & { \quad \Sigma = \mathrm { t h e ~ u n i o n ~ o f ~ t h e ~ s u b s h e a v e s } \ ( \check { \sigma } _ { \alpha } \cap M ( T ) ) _ { U _ { \alpha } } \mathrm { ~ o f ~ } M ( } \end{array}
$$

Note that, for all $s \in S$ , if $f ( s ) \in \mathbb { O } ^ { \alpha }$ , then

$$
\begin{array} { r l } & { s \in U _ { \beta } \Longleftrightarrow f ( s ) \in X _ { \sigma _ { \beta } } } \\ & { \qquad \Longleftrightarrow \mathbb { O } ^ { \alpha } \subset X _ { \sigma _ { \beta } } } \\ & { \qquad \Longleftrightarrow \sigma _ { \alpha } \mathrm { i s ~ a ~ f a c e ~ o f ~ } \sigma _ { \beta } } \\ & { \qquad \Longleftrightarrow \check { \sigma } _ { \beta } \cap M ( T ) \subseteq \check { \sigma } _ { \alpha } \cap M ( T ) ; } \end{array}
$$

hence the stalk of $\Sigma$ at $s$ is the union of the subsets $\check { \sigma } _ { \beta } \cap M ( T )$ of $M ( T )$ for all $\sigma _ { \beta }$ with face $\sigma _ { \alpha }$ , i.e., just $\check { \sigma } _ { \alpha } \cap M ( T )$ . Hence if $r \in \Sigma _ { s }$ , then $\boldsymbol r \in \check { \sigma } _ { \boldsymbol { \alpha } }$ , so

$\mathfrak { X } ^ { r }$ is defined on $X _ { \sigma _ { \alpha } }$ and $f ^ { * } ( { \mathfrak { X } } ^ { r } )$ is defined at $s$ . Therefore we can define $\pi : \Sigma \longrightarrow { \mathcal { O } } _ { S } ^ { ( \times ) }$ by

$$
\pi ( r ) = f ^ { * } ( { \mathfrak { X } } ^ { r } ) .
$$

Note that

$$
\begin{array} { r l } & { \Longleftrightarrow \mathfrak { X } ^ { r } ( f ( s ) ) \neq 0 } \\ & { \Longleftrightarrow \mathfrak { X } ^ { r } \not \equiv 0 \mathrm { o n } \mathbb { O } ^ { \alpha } } \\ & { \Longleftrightarrow r \equiv 0 \mathrm { o n } \sigma _ { \alpha } } \\ & { \Longleftrightarrow - r \in \check { \sigma } _ { \alpha } \cap M ( T ) } \\ & { \Longleftrightarrow r \mathrm { i n v e r t i b l e ~ i n ~ \AA ~ } _ { s } , } \end{array}
$$

hence $\pi$ is a strict homomorphism.

Next, let us start with $( \Sigma , \pi )$ and define a morphism $f$ . Define open sets $U _ { \alpha }$ by

$$
U _ { \alpha } = \left\{ s \in S \vert \check { \sigma } _ { \alpha } \cap M ( T ) \subset \Sigma _ { s } \right\} .
$$

These form an open covering of $s$ such that if $\sigma _ { \alpha }$ is a face of $\sigma _ { \beta }$ , then $U _ { \beta } \subset U _ { \alpha }$ . Next define

$$
f _ { \alpha } : U _ { \alpha } \longrightarrow X _ { \sigma _ { \alpha } } = { \mathrm { S p e c } } k [ . . . , \mathfrak { X } ^ { r } , . . . ] _ { r \in \check { \sigma } _ { \alpha } \cap M ( T ) }
$$

via $f _ { \alpha } ^ { * } ( { \mathfrak { X } } ^ { r } ) = \pi ( r )$ for all $r \in \check { \sigma } _ { \alpha } \cap M ( T )$ : this is correct since such an $r$ is in $\Gamma ( U _ { \alpha } , \Sigma )$ and since $\pi ( r _ { 1 } + r _ { 2 } ) = \pi ( r _ { 1 } ) \cdot \pi ( r _ { 2 } )$ . Now, for any $\alpha$ and $\beta$ , let $\sigma _ { \gamma } = \sigma _ { \alpha } \cap \sigma _ { \beta }$ , which is a face of $\sigma _ { \alpha }$ and $\sigma _ { \beta }$ . Then

$$
U _ { \alpha } \cap U _ { \beta } = \left\{ s \in S \vert \check { \sigma } _ { \alpha } \cap M ( T ) \subset \Sigma _ { s } \mathrm { a n d } \check { \sigma } _ { \beta } \cap M ( T ) \subset \Sigma _ { s } \right\} .
$$

But if $\Sigma _ { s } = \check { \sigma } _ { \delta } \cap M ( T )$ , then

$$
\begin{array} { r l } & { \left[ \begin{array} { l } { \Sigma _ { s } \supset \check { \sigma } _ { \alpha } \cap M ( T ) \mathrm { ~ a n d ~ } } \\ { \Sigma _ { s } \supset \check { \sigma } _ { \beta } \cap M ( T ) } \end{array} \right] \Longleftrightarrow \check { \sigma } _ { \delta } \supset \check { \sigma } _ { \alpha } \mathrm { ~ a n d ~ } \check { \sigma } _ { \delta } \supset \check { \sigma } _ { \beta } } \\ & { \qquad \Longleftrightarrow \sigma _ { \delta } \subset \sigma _ { \alpha } \mathrm { ~ a n d ~ } \sigma _ { \delta } \subset \sigma _ { \beta } } \\ & { \qquad \Longleftrightarrow \sigma _ { \delta } \subset \sigma _ { \gamma } } \\ & { \qquad \Longleftrightarrow \Sigma _ { s } \subset \check { \sigma } _ { \gamma } \cap M ( T ) , } \end{array}
$$

so $U _ { \alpha } \cap U _ { \beta } = U _ { \gamma }$ . Finally, it is clear from the definition that $f _ { \alpha } = \operatorname { r e s } f _ { \beta }$ whenever $U _ { \alpha } \subset U _ { \beta }$ . Therefore the $f _ { \alpha }$ patch together to form a morphism $f : S \longrightarrow X _ { \{ \sigma _ { \alpha } \} }$ .

It is now straightforward to check that these two procedures – associating a $( \Sigma , \pi )$ to an $f$ and associating an $f$ to a $( \Sigma , \pi )$ – are inverse to each other: we leave this to the reader. □

For instance, we find:

If $k = \mathbb { C }$ , one can easily prove also that

$$
\begin{array} { r l } & { N _ { \{ \sigma _ { \alpha } \} } \cong \{ ( \alpha , \rho ) | \rho : \check { \sigma } _ { \alpha } \cap M ( T ) \longrightarrow \mathbb { R } _ { \geq 0 } ^ { ( \times ) } \mathrm { s t r i c t h o m o m o r p h i s m } \} } \\ & { \qquad \cong \{ ( \alpha , \sigma ) | \sigma : \check { \sigma } _ { \alpha } \cap M ( T ) \longrightarrow \mathbb { R } \cup \{ \infty \} \mathrm { s t r i c t h o m o m o r p h i s m } \} , } \end{array}
$$

where $\mathbb { R } \cup \{ \infty \}$ is a semigroup via $^ +$ . Here

$$
\mathrm { o r d } : X _ { \{ \sigma _ { \alpha } \} } \longrightarrow N _ { \{ \sigma _ { \alpha } \} }
$$

is given by

$$
\begin{array} { l } { { \rho ( x ) = \left| \pi ( x ) \right| , } } \\ { { \sigma ( x ) = - \log \rho ( x ) . } } \end{array}
$$

# 3 Toroidal embeddings over the complex numbers

We wish to review here quickly some results of TE I, Ch. II, indicating ways to interpret them over $\mathbb { C }$ , and generalizing them slightly. A pair

$$
U \subset X ,
$$

where $U$ is a Zariski-open subset of a normal variety $X$ , was called a toroidal embedding if, for all $x \in X$ , we have that $( X , U )$ is formally isomorphic at $x$ to $( X _ { \sigma } , T )$ at some $t \in X _ { \sigma }$ (for some torus embedding $T \subset X _ { \sigma }$ ). Equivalently, this means that there is an etale correspondence between ´ $X$ and $X _ { \sigma }$ , relating $x$ and $t$ , with $U$ and $T$ corresponding open sets. Over $\mathbb { C }$ , a pair

$$
U \subset X ,
$$

where $X$ is an analytic space and $U$ is open in the complex topology, will be called a toroidal embedding if, for all $x \in X$ , there exists a small neighborhood $W _ { x } \subset X$ of $x$ such that $( W _ { x } , W _ { x } \cap U )$ is isomorphic to $( V _ { t } , V _ { t } \cap T )$ for some neighborhood $V _ { t } \subset X _ { \sigma }$ of some $t \in X _ { \sigma }$ (for some torus embedding $T \subset X _ { \sigma } .$ ). When $X , U$ are varieties, this coincides with the previous definition. Now, this implies immediately that $W _ { x }$ has a canonical stratification $\{ Y _ { \alpha , x } \}$ into non-singular locally closed analytic strata with $\overline { { Y } } _ { \alpha , x }$ normal: let $E _ { i }$ be the irreducible components of $W _ { x } \setminus W _ { x } \cap U$ , and let the $Y _ { \alpha , x }$ be the sets

$$
\bigcap _ { i \in I } E _ { i } \setminus \bigcup _ { i \notin I } E _ { i } .
$$

We shrink $W _ { x }$ if necessary, so that these $Y _ { \alpha , x }$ are connected. As $x$ varies, these strata patch up on overlaps, so we can uniquely stratify the whole of $X$ into

$\{ Y _ { \alpha } \}$ , where the $Y _ { \alpha }$ are connected, locally closed, non-singular analytic strata, and where $Y _ { \alpha } \cap W _ { x }$ is a union of the $Y _ { \beta , x }$ . However, it may happen that

$$
Y _ { \alpha } \cap W _ { x } \supset { \mathrm { m o r e ~ t h a n ~ o n e ~ } } Y _ { \beta , x } \ .
$$

This means that there is a path in $X$ starting and ending in $W _ { x }$ and lying all in one stratum, but linking two distinct local strata:

![](images/6bcd445b50722dc1ddcc3c55d56160a4e7244e49072272814a30f86748dff8e5.jpg)

Since this will mean that $\overline { { Y } } _ { \alpha }$ has more than one branch through $x$ , it is equivalent to $\overline { { Y } } _ { \alpha }$ being non-normal. As in TE I, p. 57, we say that $( X , U )$ has or has not self-intersection according to whether $Y _ { \alpha } \cap W _ { x }$ can be more than one local stratum, or $Y _ { \alpha } \cap W _ { x }$ is always one local stratum. In TE I, we stuck with $( X , U )$ ’s without self-intersection. However, there is a class of toroidal embeddings with self-intersection that are almost as nice and that arise in the examples we will treat. Suppose $Y _ { \beta _ { 1 } , x }$ and $Y _ { \beta _ { 2 } , x }$ are part of the same global stratum $Y _ { \alpha }$ . Locally at $x$ there is a unique stratum $Y _ { \beta _ { 3 } , x }$ such that

$$
\overline { { Y } } _ { \beta _ { 3 } , x } = \overline { { Y } } _ { \beta _ { 1 } , x } \cap \overline { { Y } } _ { \beta _ { 2 } , x } .
$$

Let $Y _ { \beta _ { 3 } , x }$ define a global stratum $Y _ { \gamma }$ . We say that $( X , U )$ is without monodromy if $Y _ { \gamma }$ has a neighborhood $W$ such that $Y _ { \beta _ { 1 } , x }$ and $Y _ { \beta _ { 2 } , x }$ lie in different components of $Y _ { \alpha } \cap W$ . To visualize this, note that, for every path in $Y _ { \gamma }$ beginning and ending at $x$ , we can uniquely propagate the germ of analytic space $\overline { { Y } } _ { \beta _ { 1 } , x }$ along this path. If this germ can be taken to $\overline { { Y } } _ { \beta _ { 2 } , x }$ by such a path, then, for every neighborhood $W$ of $Y _ { \gamma }$ , we may connect $Y _ { \beta _ { 1 } , x }$ and $Y _ { \beta _ { 2 } , x }$ within $Y _ { \alpha } \cap W$ . If not, then, in some small enough $W$ , they cannot be connected:

![](images/12044c69e331d28e3ebcfb127804131e62b40b3e1a0a93e034a3d3188a96f935.jpg)  
A toroidal embedding with monodromy

If $( X , U )$ is without monodromy, then every stratum $Y _ { \alpha }$ has a small complex neighborhood, which we call $\operatorname { S t a r } _ { 0 } ( Y _ { \alpha } )$ , in which all the local strata $Y _ { \beta , x }$ (where $x \in Y _ { \alpha } , { \overline { { Y } } } _ { \beta , x } \supset Y _ { \alpha } )$ remain distinct; i.e., $\operatorname { S t a r } _ { 0 } ( Y _ { \alpha } )$ is a union of semi-local strata $Y _ { \beta } ^ { ( \alpha ) }$ such that (α) We may even assume that there is a stratum-preserving homeomorphism

$$
{ \mathrm { S t a r } } _ { 0 } ( Y _ { \alpha } ) \approx X _ { \sigma } \times Y _ { \alpha } ~ ,
$$

where $T \subset X _ { \sigma }$ is a true embedding. Of course, in the whole space $X$ , we may have $Y _ { \beta _ { 1 } } ^ { ( \alpha ) }$ and  (αx) as part of the same stratum $Y _ { \gamma }$

The main point of Ch. II, $\ S 1$ of TE I was to associate to each toroidal embedding without self-intersection $( X , U )$ a conical polyhedral complex with integral structure. If we generalize slightly our definition of such a complex, we can do this for any analytic toroidal embedding without monodromy too. The following definition may be compared with the definition in TE I, p. 69.

Definition 3.1 A conical polyhedral complex $\Sigma$ is a topological space $| \Sigma |$ , plus a stratification $\{ S _ { \alpha } \}$ of $| \Sigma |$ (i.e., a partition of $| \Sigma |$ into disjoint locally closed pieces $S _ { \alpha }$ such that each $\overline { { S } } _ { \alpha }$ is a union of finitely many $S _ { \beta }$ ’s), plus, for each $\alpha$ , a finite-dimensional vector space $V _ { \alpha }$ of real-valued continuous functions on $S _ { \alpha }$ such that:

(a) if $n _ { \alpha } = \dim \left( V _ { \alpha } \right)$ and $F _ { 1 } , \ldots , F _ { n _ { \alpha } }$ is a basis of $V _ { \alpha }$ , then

$$
\left( f _ { i } \right) : S _ { \alpha } \longrightarrow \mathbb { R } ^ { n _ { \alpha } }
$$

is a homeomorphism of $S _ { \alpha }$ with an open convex polyhedral cone $C _ { \alpha } \subset$ $\mathbb { R } ^ { n _ { \alpha } }$ ;

(b) $( f _ { i } ) ^ { - 1 }$ extends to a continuous surjective map

$$
( f _ { i } ) ^ { - 1 } : \overline { { C } } \alpha \longrightarrow \overline { { S } } \alpha
$$

mapping the open faces $C _ { \alpha } ^ { ( \beta ) }$ of $\overline { { C } } _ { \alpha }$ homeomorphically to the strata $S _ { \beta }$ in $\overline { { S } } _ { \alpha }$ , and inducing isomorphisms

$$
\mathrm { r e s } _ { C _ { \alpha } ^ { ( \beta ) } } ( \operatorname* { l i n e a r } \mathrm { f u n c t i o n s ~ o n } \mathbb { R } ^ { n _ { \alpha } } ) \xrightarrow { \sim } V _ { \beta } \ .
$$

Note that such a complex has a natural piecewise-linear (or PL) structure.

Definition 3.2 An integral structure on a conical polyhedral complex is a set of finitely generated abelian groups $L _ { \alpha } \subset V _ { \alpha }$ such that

(i) $L _ { \alpha } \otimes \mathbb { R } \cong V _ { \alpha }$ ;   
(ii) if $S _ { \beta }$ is a face of $S _ { \alpha }$ , then res $s _ { \beta } L _ { \alpha } = L _ { \beta }$ .

The changes from TE I are: (a) that the collection $\{ S _ { \alpha } \}$ is not supposed to be finite; and (b) we allow two faces of the same polyhedron $C _ { \alpha }$ in $\mathbb { R } ^ { n }$ to be identified in $X$ . We sketch how to associate a complex $\Sigma = ( | \Sigma | , \{ S _ { \alpha } \} , \{ V _ { \alpha } \} )$ to a toroidal embedding $( X , U )$ without monodromy in the following.

(a) For all strata $Y$ of $( X , U )$ , let

$$
\begin{array} { r l } & { M ^ { Y } = \mathrm { g r o u p ~ o f ~ C a r t i e r ~ d i v i s o r s ~ o n ~ } { \mathrm { S t a r } } _ { 0 } ( Y ) , \mathrm { s u } _ { \mathrm { J } } } \\ & { ~ { \mathrm { S t a r } } _ { 0 } ( Y ) \backslash U \cap { \mathrm { S t a r } } _ { 0 } ( Y ) ~ , } \\ & { M _ { + } ^ { Y } = \mathrm { s u b - s e m i g r o u p ~ o f ~ e f f e c t i v e ~ d i v i s o r s ~ } , } \\ & { N _ { \mathbb { R } } ^ { Y } = \mathrm { H o m } \left( M ^ { Y } , \mathbb { R } \right) ~ , } \\ & { \sigma ^ { Y } = \left\{ x \in N _ { \mathbb { R } } ^ { Y } \mid \langle D , x \rangle \geq 0 , \mathrm { ~ f o r ~ a l l ~ } D \in M _ { + } ^ { Y } \right\} ~ . } \end{array}
$$

(b) For all strata $Z _ { 0 }$ in $\operatorname { S t a r } _ { 0 } ( Y )$ , let $Z$ be the stratum of $X$ containing $Z _ { 0 }$ ; then we get a map

$$
\alpha _ { Z _ { 0 } } : M ^ { Y } \longrightarrow M ^ { Z }
$$

by restricting a divisor on $\operatorname { S t a r } _ { 0 } ( Y )$ to the component of $\operatorname { S t a r } _ { 0 } ( Y ) \cap \operatorname { S t a r } _ { 0 } ( Z )$ containing $Z _ { 0 }$ , and then extending it to $\mathrm { S t a r } _ { 0 } ( Z )$ . This induces an isomorphism

$$
\beta _ { Z _ { 0 } } : \sigma ^ { Z } \stackrel { \sim } { \longrightarrow } \mathrm { ~ a ~ f a c e ~ o f ~ } \sigma ^ { Y } ~ .
$$

(c) Define

$$
\begin{array} { r l } & { | \Sigma | = \bigcup _ { Y } \sigma ^ { Y } / ( \begin{array} { l } { \mathrm { e q u i v a l e n c e r e l a t i o n ~ g e n e r a t e d } } \\ { \mathrm { b y ~ t h e ~ m a p s } \beta _ { Z _ { 0 } } } \end{array} ) \cong \bigcup _ { Y } \mathrm { I n t } \sigma ^ { Y } , } \\ & { S _ { \alpha } = \mathrm { i m a g e ~ o f ~ I n t } ( \sigma ^ { Y _ { \alpha } } ) , } \\ & { V _ { \alpha } = \mathrm { t h e ~ f u n c t i o n s } M ^ { Y _ { \alpha } } \otimes \mathbb { R } \mathrm { ~ o n ~ } \sigma ^ { Y _ { \alpha } } , } \\ & { L _ { \alpha } = \mathrm { t h e ~ f u n c t i o n s } M ^ { Y _ { \alpha } } \mathrm { ~ o n ~ } \sigma ^ { Y _ { \alpha } } . } \end{array}
$$

This is an immediate generalization of the construction of TE I, pp. 59–72. The map “ord” also has an analytic version. Define†

R.S. ${ } ^ { U } ( X ) = \{ \phi : \Delta \longrightarrow X$ holomorphic such that $\phi ( { \mathring { \Delta } } ) \subset U \}$ ,

where $\Delta$ is the open unit disc and $\mathring { \Delta } = \Delta \backslash \{ 0 \}$ . Define

$$
\mathrm { o r d } : \mathbf { R . S . } ^ { U } ( X ) \longrightarrow | \Sigma |
$$

as follows. Let $\phi \in \mathbf { R } . \mathbf { S } . ^ { U } ( X )$ with $\phi ( 0 ) \in \mathrm { S t r a t u m } Y$ . Then, on some smaller disc $\Delta ^ { \prime }$ , we have $\phi \left( \Delta ^ { \prime } \right) \subset \operatorname { S t a r } _ { 0 } ( Y )$ ; hence, for all divisors $D \in M ^ { Y }$ , the pullback $\phi ^ { * } D$ is a divisor on $\Delta ^ { \prime }$ with a definite multiplicity $\mathrm { o r d } _ { 0 } \big ( \phi ^ { \ast } D \big )$ at 0. Define $\operatorname { o r d } ( \phi )$ in $\sigma ^ { Y }$ by

$$
\langle D , \mathrm { o r d } ( \phi ) \rangle = \mathrm { o r d } _ { 0 } ( \phi ^ { * } D ) ,
$$

and define $\operatorname { o r d } ( \phi )$ in $| \Sigma |$ as the image of this.

We may also give a purely topological definition of ord via monodromy. In fact, suppose we choose a nice neighborhood $\mathrm { S t a r _ { 0 } ( Y ) }$ so that

$$
\operatorname { S t a r } _ { 0 } ( Y ) \approx X _ { \tau } \times Y ~ .
$$

Note that in this case we get isomorphisms

$$
M ^ { Y } \cong M ( T ) ;
$$

hence

$$
N _ { \mathbb { R } } ^ { Y } \cong N ( T ) _ { \mathbb { R } }
$$

and

$$
\sigma ^ { Y } \cong \tau .
$$

In particular this shows that

$$
\begin{array} { r l } { \pi _ { 1 } ( \operatorname { S t a r } _ { 0 } ( Y ) \cap U ) \cong \pi _ { 1 } ( T \times Y ) } \\ & { \cong \pi _ { 1 } ( F ) \times \pi _ { 1 } ( Y ) } \\ & { \cong N ( T ) \times \pi _ { 1 } ( Y ) } \\ & { \cong N ^ { Y } \times \pi _ { 1 } ( \operatorname { S t a r } _ { 0 } ( Y ) ) ~ ; } \end{array}
$$

hence

$$
\mathrm { K e r } [ \pi _ { 1 } ( \mathrm { S t a r } _ { 0 } ( Y ) \cap { \cal U } ) \longrightarrow \pi _ { 1 } ( \mathrm { S t a r } _ { 0 } ( Y ) ) ] \stackrel { \sim } { \underset { \zeta } { \longrightarrow } } N ^ { Y } ~ .
$$

Using this isomorphism, we find:

Proposition 3.3 Let $\phi \in \mathbf { R } . \mathbf { S } . ^ { U } ( X )$ and assume $\phi ( 0 ) \in$ stratum Y . For c small, we have

$$
\operatorname { r e s } \phi : \Delta _ { c } = \{ z \mid \left. z \right. \leq c \} \longrightarrow \mathrm { S t a r } _ { 0 } ( Y ) ~ ;
$$

hence res $\phi$ induces

$$
\phi _ { * } : \pi _ { 1 } ( \partial \Delta _ { c } ) \longrightarrow \mathrm { K e r } \left[ \pi _ { 1 } \big ( \mathrm { S t a r } _ { 0 } ( Y ) \cap U \big ) \longrightarrow \pi _ { 1 } \big ( \mathrm { S t a r } _ { 0 } ( Y ) \big ) \right] .
$$

If 1 is the canonical generator of the left-hand side, then

$$
\zeta ( \phi _ { * } ( 1 ) ) = \mathrm { o r d } ( \phi ) \ .
$$

Proof By the way that $\zeta : \pi _ { 1 } ( T ) \xrightarrow { \sim } N ( T )$ is defined, it follows that, for every loop $\lambda$ in $T$ , and every character ${ \mathfrak { X } } ^ { \alpha }$ ,

$$
2 \pi \langle \alpha , \zeta ( \lambda ) \rangle = \mathrm { c h a n g e ~ i n ~ a r g } \mathfrak { X } ^ { \alpha } \ \mathrm { a r o u n d ~ t h e ~ l o o p } \ \lambda \ .
$$

Now let $T \subset X _ { \sigma }$ be a torus embedding, $t \in X _ { \sigma }$ , let $V$ be a neighborhood of $t$ , and let $u \cdot { \mathfrak { X } } ^ { \alpha }$ be a function on $V$ , where $u$ is a unit on $V$ ; moreover, let $\lambda$ be a loop in $V$ arising by restricting to $\partial \Delta _ { c }$ a holomorphic map $\phi : \Delta _ { c } \longrightarrow V$ . Then

$$
2 \pi \langle \alpha , \zeta ( \lambda ) \rangle = \mathrm { c h a n g e ~ i n ~ a r g } \left( u \cdot { \mathfrak { X } } ^ { \alpha } \right) { \mathrm { a r o u n d ~ t h e ~ l o o p ~ } } \lambda ~ .
$$

Next, go over to a toroidal embedding $U \subset X$ , let $x \in X$ and let $V$ be a neighborhood of $x$ , and let $\delta$ be a meromorphic function on $V$ with no zeroes or poles on $V \cap U$ . Moreover, let $\lambda$ be a loop in $V$ arising by restricting to $\partial \Delta _ { c }$ a holomorphic map $\phi : \Delta _ { c } \longrightarrow V$ . Then the principal divisor $( \delta )$ is an element of $M ^ { Y }$ , and

$$
{ \begin{array} { r l } & { 2 \pi \langle ( \delta ) , \zeta ( \lambda ) \rangle = { \mathrm { c h a n g e ~ i n ~ a r g ~ } } \delta { \mathrm { ~ a r o u n d ~ t h e ~ l o o p ~ } } \lambda } \\ & { ~ = { \mathrm { c h a n g e ~ i n ~ a r g } } ( \delta \circ \phi ) { \mathrm { ~ o n ~ } } | z | = c } \\ & { ~ = 2 \pi \cdot { \mathrm { ( o r d e r ~ o f ~ z e r o ~ o r ~ p o l e ~ o f ~ } } \delta \circ \phi { \mathrm { ~ a t ~ } } 0 { \mathrm { ) } } } \\ & { ~ = 2 \pi \langle ( \delta ) , { \mathrm { o r d } } ( \phi ) \rangle ~ . } \end{array} }
$$

Since $\lambda = \phi _ { * } ( 1 )$ , this proves what we want.

# 4 Compactification of the universal elliptic curve

We now take up perhaps the simplest example of our theory. We deal first with this example over the complex numbers.

Fix an integer $k \geq 3$ once and for all. Let

$$
\Gamma = \left\{ \left( \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right) | a \equiv d \equiv 1 { \bmod { k } } , b \equiv c \equiv 0 { \bmod { k } } , a d - b c = 1 \right\}
$$

act on the upper half plane ${ \mathfrak H }$ by

$$
\omega \longmapsto { \frac { a \omega + b } { c \omega + d } } ~ .
$$

Let

$$
\Gamma ^ { A } = \Gamma \ltimes \mathbb { Z } ^ { 2 }
$$

(semidirect product, where $\mathbb { Z } ^ { 2 }$ is normal with $\Gamma$ acting on $\mathbb { Z } ^ { 2 }$ by

$$
( m , n ) \longmapsto ( a m + c n , b m + d n ) ~ ;
$$

“A” stands for “affine”). Then $\Gamma ^ { A }$ acts on $\mathbb { C } \times { \mathfrak { H } }$ by

$$
( z , \omega ) \longmapsto \left( \frac { z + m \omega + n } { c \omega + d } , \frac { a \omega + b } { c \omega + d } \right) .
$$

Then $M = \mathfrak { H } / \Gamma$ is the moduli space for elliptic curves with level- $k$ structure and $\ b X = ( \mathbb C \times \mathfrak { H } ) / \Gamma ^ { \ b A }$ is the universal level- $k$ elliptic curve over $M$ , via the canonical projection $p : X \longrightarrow M$ (see, for example, Lang [2]). The problem is that $M$ , and hence $X$ , are not compact and we seek compactifications:

$$
\begin{array} { l c c c c } { { X } } & { { \longleftarrow } } & { { \longleftrightarrow } } & { { \tilde { X } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \downarrow } } & { { } } & { { } } & { { } } & { { \downarrow } } \\ { { M \ \subset } } & { { } } & { { } } & { {   \ \tilde { M } \ . } } \end{array}
$$

The usual procedure for $M$ is to note that, since it is one-dimensional, there is a unique non-singular complete algebraic curve $\widetilde { M }$ such that $M = \widetilde { M } \backslash \left\{ \begin{array} { r l r l } \end{array} \right.$ {finite set}. Then, from the theory of algebraic surfaces, one can also find a canonical $\widetilde { X }$ : the unique so-called non-singular relatively minimal model over $\widetilde { M }$ . These methods do not however generalize to higher-dimensional cases, and we seek to describe $\widetilde { M }$ and $\widetilde { X }$ by a more direct “scissors and glue” construction involving torus embeddings.

We deal first with the cusp $\mathbf { i } \infty \in \partial \Im$ . Consider the subgroup

$$
\Gamma _ { 1 } = \left\{ \left( \begin{array} { c c } { { 1 } } & { { b } } \\ { { 0 } } & { { 1 } } \end{array} \right) | b \equiv 0 \bmod k \right\}
$$

and factor $\pi : { \mathfrak { H } } \longrightarrow { \mathfrak { H } } / \Gamma = M$ via

![](images/40d8091626ba2e5bd7e40cd3c37076402d9576c636b7ebfb34c7cab59e8f2a1d.jpg)

where $q$ is the coordinate on $\mathring \Delta$ and exp is defined by

$$
\begin{array} { r } { q = \mathrm { e } ^ { 2 \pi \mathrm { i } \omega / k } \ . } \end{array}
$$

This makes $\mathring \Delta$ isomorphic to ${ \mathfrak { H } } / { \Gamma } _ { 1 }$ , hence $\pi$ factors via exp. Moreover, define

$$
\begin{array} { l } { { \mathfrak { H } _ { d } = \left\{ \omega \ : \vert \ : \mathrm { I m } \omega \geq d \right\} , } } \\ { { \mathring { \Delta } _ { d } = \left\{ q \ : \vert \ : 0 < \left. q \right. \leq \mathrm { e } ^ { - 2 \pi d / k } \right\} . } } \end{array}
$$

Then $\mathfrak { H } _ { d } = \exp ^ { - 1 } ( \mathring { \Delta } _ { d } )$ and $\mathring { \Delta } _ { d } \cong \mathfrak { H } _ { d } / \Gamma _ { 1 }$ . The following lemma is easy to check.

Lemma 4.1 There exists $d _ { 0 }$ such that, for all $\omega \in \mathfrak { H } , \gamma \in \Gamma ,$ ,

$$
\iota d \gamma \omega \in \mathfrak { H } _ { d _ { 0 } } \Longrightarrow \gamma \in \Gamma _ { 1 } \ .
$$

Therefore res $\pi ^ { \prime }$ maps $\mathring { \Delta } _ { d _ { 0 } }$ injectively to $M$

![](images/4ca32278039de23fbd2f31993c38552defae7f0f56734f2cbc3ede065205f4d6.jpg)

Moreover, as $d \longrightarrow \infty$ , it is well known that the sets $\pi ( \mathfrak { H } _ { d } ) \subset M$ are a fundamental system of neighborhoods of the cusp i∞. Therefore, we find that we can glue via this map by taking $M$ plus

$$
\Delta _ { d _ { 0 } } = \{ q | | q | \le \mathrm { e } ^ { - 2 \pi d _ { 0 } / k } \}
$$

and identifying them via res $\pi ^ { \prime }$ on $\mathring { \Delta } _ { d _ { 0 } }$ .

Next, every rational point $p / q \in \partial \mathfrak { H }$ also defines a cusp of $M$ , except that $p / q$ and $\gamma ( p / q )$ for $\gamma \in \Gamma$ define the same cusp. Now, a fundamental system of neighborhoods of $p / q$ in $\widetilde { M }$ are the sets $\pi ( W _ { d } ( p / q ) )$ , where $W _ { d } ( p / q )$ is the closed disc in ${ \mathfrak H }$ of radius $d$ , tangent to the real axis at $p / q$ (a so-called horocycle) and, if $d$ is small enough, the  $\Gamma$ -equivalence of points of   $W _ { d } ( p / q )$ becomes $\Gamma _ { 1 } ( p / q )$ -equivalence, where

$$
\begin{array} { r l } & { \Gamma _ { 1 } ( p / q ) = \{ \gamma \in \Gamma \mid \gamma ( p / q ) = p / q \} } \\ & { \qquad = \left\{ \left( \begin{array} { c c } { 1 + p q } & { - p ^ { 2 } } \\ { q ^ { 2 } } & { 1 - p q } \end{array} \right) ^ { n } \mid n \in \mathbb { Z } \right\} . } \end{array}
$$

So we can mimic the above construction to obtain $\widetilde { M }$ by glueing. But, even more simply, we can use the fact that $\operatorname { S L } ( 2 , \mathbb { Z } )$ acts transitively on the set of

rational points plus $\mathrm { \infty }$ , hence ${ \mathrm { S L } } ( 2 , \mathbb { Z } ) / \Gamma$ acts on $M$ and permutes transitively all its cusps. Thus, if we know how to fill in one, we can fill in the others by acting by ${ \mathrm { S L } } ( 2 , \mathbb { Z } ) / \Gamma$ .

Now look upstairs at $\mathbb { C } \times { \mathfrak { H } }$ . Define

$$
\Gamma _ { 1 } ^ { A } = \left( \begin{array} { c } { { \mathrm { s u b g r o u p ~ o f ~ } \Gamma ^ { A } \mathrm { ~ g e n e r a t e d ~ b y } } } \\ { { \left( z , \omega \right) \longmapsto \left( z + 1 , \omega \right) \mathrm { ~ a n d ~ } } } \\ { { \left( z , \omega \right) \longmapsto \left( z , \omega + k \right) } } \end{array} \right) \cong \mathbb { Z } ^ { 2 } ;
$$

$$
\Gamma _ { 2 } ^ { \cal A } = \left( \begin{array} { c } { { \mathrm { s u b g r o u p ~ o f ~ } \Gamma ^ { \cal A } \mathrm { ~ g e n e r a t e d ~ b y ~ } \Gamma _ { 1 } ^ { \cal A } \mathrm { ~ a n d ~ } } } \\ { { \alpha : ( z , \omega ) \longmapsto ( z + \omega , \omega ) } } \end{array} \right) .
$$

Factor $\pi : \mathbb { C } \times { \mathfrak { H } } \longrightarrow ( \mathbb { C } \times { \mathfrak { H } } ) / \Gamma ^ { A } = X$ via:

$$
\begin{array} { c c c } { { \mathbb C \times \mathfrak { H } \displaystyle \longrightarrow } } & { { \exp } } & { { \exp } } \\ { { } } & { { } } & { { \displaystyle \bigoplus _ { \pi \searrow \displaystyle \bigcup } ^ { \mathrm { e x p } } \exp ^ { - \big \langle \mathbb C ^ { * } \times \mathring { \Delta } } } } \\ { { } } & { { } } & { { \displaystyle \qquad \quad _ { M } ^ { \mathrm { m } } } } \end{array}
$$

where $x$ is the coordinate on $\mathbb { C } ^ { * }$ , and $q$ that on $\mathring \Delta .$ , and where exp is defined by

$$
\begin{array} { l } { { x = { \mathrm e } ^ { 2 \pi { \mathrm i } z } \ , } } \\ { { q = { \mathrm e } ^ { 2 \pi { \mathrm i } \omega / k } \ . } } \end{array}
$$

This makes $\mathbb { C } ^ { * } \times \mathring { \Delta }$ isomorphic to $( \mathbb { C } \times { \mathfrak { H } } ) / \Gamma _ { 1 } ^ { A }$ . Now, $\Gamma _ { 1 } ^ { A }$ is a normal subgroup of $\Gamma _ { 2 } ^ { A }$ and $\Gamma _ { 2 } ^ { A } / \Gamma _ { 1 } ^ { A } \cong \mathbb { Z }$ , with generator $\alpha$ , and $\Gamma _ { 2 } ^ { A } / \Gamma _ { 1 } ^ { A }$ acts on $\mathbb { C } ^ { * } \times \mathring { \Delta }$ . The previous lemma now gives us:

Corollary 4.2 There exists $d _ { 0 }$ such that, for all $( z , \omega ) \in \mathbb { C } \times \mathfrak { H }$ and all $\gamma \in \Gamma ^ { A }$ ,

$$
( z , \omega ) \ \mathrm { a n d } \ \gamma ( z , \omega ) \in { \mathbb C } \times \mathfrak { H } _ { d _ { 0 } } \Longrightarrow \gamma \in \Gamma _ { 2 } ^ { A } \ .
$$

Therefore,

$$
\mathrm { r e s } \pi ^ { \prime } : ( \mathbb { C } ^ { * } \times \mathring { \Delta } _ { d _ { 0 } } ) / \{ \alpha ^ { n } \} \longrightarrow X
$$

is injective. To compactify $X$ over $\mathrm { i } \infty \in \stackrel { \sim } { M }$ , it suffices to enlarge $\mathbb { C } ^ { * } \times \mathring { \Delta } _ { d _ { 0 } }$ to an analytic manifold $Y$ over $\Delta _ { d _ { 0 } }$ , equivariantly with respect to the action of $\alpha$ and so that, mod $\alpha$ , we get a manifold proper over $\Delta _ { d _ { 0 } }$ :

Here is where tori come in: think of $\mathbb { C } ^ { * } \times \mathring { \Delta }$ as an open subset of the twodimensional torus $\mathbb { C } ^ { * } \times \mathbb { C } ^ { * }$ (with coordinates $x , q$ ). Thus $\alpha$ acts on the whole torus by

$$
( x , q ) \longmapsto ( q ^ { k } x , q ) ~ .
$$

We shall construct a torus embedding $\mathbb { C } ^ { * } \times \mathbb { C } ^ { * } \subset X _ { \{ \sigma _ { \alpha } \} }$ and the sought-for analytic manifold $Y$ will be the closure of $\mathbb { C } ^ { * } \times \mathring { \Delta } _ { d _ { 0 } }$ in $X _ { \{ \sigma _ { \alpha } \} }$ . In fact, identify $N ( \mathbb { C } ^ { * } \times \mathbb { C } ^ { * } )$ with $\mathbb { Z } \times \mathbb { Z }$ and note that $\alpha$ acts on $N ( \mathbb { C } ^ { * } \times \mathbb { C } ^ { * } )$ by

$$
( a , b ) \longmapsto ( a + k b , b ) ~ .
$$

We choose $\{ \sigma _ { \alpha } \}$ to be the following infinite chain $\sigma _ { n }$ , $n \in \mathbb { Z }$ :

![](images/5ffa4f2f2ad7e9a6934f0dc4ae6c9ad53b07227242be187554b3cdb72ebfc56a.jpg)

Note that $\alpha$ carries $\sigma _ { n }$ to $\sigma _ { n + k }$ , so that, mod $\alpha$ , there are only finitely many

σ. The corresponding $X _ { \{ \sigma _ { n } \} }$ may be pictured as follows:

![](images/a005a06a2c8b8cfdd06381442f044a080cfde32cf83c826ecd37853035123262.jpg)

Clearly $\alpha$ acts on $X _ { \{ \sigma _ { n } \} }$ . Since each $\sigma _ { i }$ is generated by a basis of $\mathbb { Z } \times \mathbb { Z }$ , it follows that $X _ { \{ \sigma _ { n } \} }$ is a manifold, i.e., smooth. Moreover, a whole neighborhood of the boundary $X _ { \{ \sigma _ { n } \} } \setminus \left( \mathbb { C } ^ { * } \times \mathbb { C } ^ { * } \right)$ is contained in $\mathbb { C } ^ { * } \times \mathring { \Delta } _ { d _ { 0 } }$ , so define $Y$ to be

$$
\begin{array} { r l } & { Y = \mathrm { i n t e r i o r ~ o f ~ c l o s u r e ~ o f ~ } \mathbb { C } ^ { * } \times \mathring { \Delta } _ { d _ { 0 } } \mathrm { ~ i n ~ } X _ { \left\{ \begin{array} { l } { l } { \Gamma } \\ { = \big ( \mathbb { C } ^ { * } \times \mathring { \Delta } _ { d _ { 0 } } \big ) \cup \big ( X _ { \left\{ \sigma _ { n } \right\} } \setminus ( \mathbb { C } ^ { * } \times \mathbb { C } ^ { * } ) \big ) ~ . } \right.} \end{array}  } \\ & { \quad = ( \mathbb { C } ^ { * } \times \mathring { \Delta } _ { d _ { 0 } } ) \cup \big ( X _ { \left\{ \sigma _ { n } \right\} } \setminus ( \mathbb { C } ^ { * } \times \mathbb { C } ^ { * } ) \big ) ~ . } \end{array}
$$

What happens when we divide by $\alpha ?$ Clearly $\alpha$ does not act discontinuously on the whole of $\mathbb { C } ^ { * } \times \mathbb { C } ^ { * }$ (i.e., if $| q | = 1 { \dot { } }$ ) so we cannot form $( \mathbb { C } ^ { * } \times \mathbb { C } ^ { * } ) / \{ \alpha ^ { n } \}$ . However, it can be checked to act discontinuously on $Y$ , and the quotient looks

like this:

![](images/6c6d8cc8dd95430afd0fbbfa11ed96206b765ccd7f4c686400b515fbcaafd8f6.jpg)

We can now define that part of $\widetilde { X }$ that lies over $\mathrm { i } \infty \in \widetilde { M }$ by glueing $X$ and $Y / \{ \alpha ^ { n } \}$ together on the common open set $( \mathbb { C } ^ { * } \times \mathring { \Delta } _ { d _ { 0 } } ) / \{ \alpha ^ { n } \}$ . As before, we can take care of the other cusps by pushing this boundary around by ${ \mathrm { S L } } ( 2 , \mathbb { Z } ) / \Gamma$ . This gives us a compact non-singular surface $\widetilde { X }$ , proper over $\widetilde { M }$ , with its fibers elliptic curves over $M$ and rational $k$ -gons over the cusps. In this way, we find an analytic construction not only of $M$ and $X$ , but also of their natural completions $\widetilde { M }$ and $\widetilde { X }$ .

We want to study briefly this same circle of ideas from another point of view, similar to that of the articles of Deligne and Rapoport [1] and of Mumford [3]. Suppose we are over an arbitrary ground field $L$ with a fixed primitive kth root of unity $\zeta$ (here $( \mathrm { c h a r } L , k ) = 1$ ; actually the same ideas work over suitable ground rings too). Then we can define $\widetilde { M }$ and $\widetilde { X }$ over $L$ as the schemes which represent a certain functor. Restricting ourselves to the corresponding formal schemes at the cusps, we can then see directly that $\widetilde { M }$ and $\widetilde { X }$ are quotients of the formal neighborhood of the locus at infinity in the same torus embeddings introduced above.

We need some definitions.

(a) If $E$ is an elliptic curve with given origin $e$ , a level- $k$ -structure on $E$ is a pair of points $x , y \in E$ of order $k$ such that $e _ { k } ( x , y ) = \zeta$ (here $e _ { k }$ is Weil’s pairing); equivalently, if $\mathcal { L }$ is a line bundle of degree $k$ , and $\phi , \psi : \mathcal { L } \longrightarrow \mathcal { L }$ are automorphisms lifting translation by $x .$ , resp. $y$ , then

$$
\phi \circ \psi \circ \phi ^ { - 1 } \circ \psi ^ { - 1 } = \mathrm { m u l t i p l i c a t i o n } \ : \mathsf { b y } \ : \zeta \ : .
$$

(b) If $E$ is a $k$ -gon of rational curves with given group law on $E _ { 0 } \subset E$ (where $E _ { 0 }$ are the smooth points of $E$ ), a level- $k$ -structure on $E$ is a pair of points $x , y \in E _ { 0 }$ of order $k$ such that $e _ { k } ( x , y ) = \zeta$ . Here, to define $e _ { k }$ , let $\mathcal { L }$ be a line

bundle of degree 1 on each component of $E$ : then there exist $\phi , \psi : \mathcal { L } \longrightarrow$ $\mathcal { L }$ lifting translation by ⎧ $x , y : E \longrightarrow E$ . Then

$$
\phi \circ \psi \circ \phi ^ { - 1 } \circ \psi ^ { - 1 } = \mathrm { m u l t i p l i c a t i o n } \ : \mathsf { b y } \ : \zeta \ : .
$$

Then consider the following functor on schemes over ⎪⎪⎪ $L$ :

set of 4-tuples $( p , \sigma , u , \nu )$ where: (a) $p : Y \longrightarrow S$ is a proper flat morphism, all fibers of which are elliptic curves or $k$ -gons of rational curves; M(S) = (b) $\sigma : Y _ { 0 } \times _ { S } Y \longrightarrow Y$ is a morphism (here $Y _ { 0 }$ is the open set in $Y$ where $p$ is smooth), making $Y _ { 0 }$ a group scheme over $s$ and making $Y _ { 0 }$ act on $Y$ ; † (c) $u , \nu : S \longrightarrow Y _ { 0 }$ are sections of order $k$ inducing a level- $k$ -structure on each fiber.

Let ${ \mathfrak { M } } \subset { \widetilde { \mathfrak { M } } }$ be the subfunctor of , where is smooth. Let $\widetilde { \mathfrak { X } } ( S ) = \left\{ \begin{array} { l l } { \begin{array} { r l r } \end{array} } \end{array} \right.$ set of 5-tuples (p, σ, u,v, w), with p, σ, u,v as beforeand w : S −→ Y any section of Y over S  ,- X = subfunctor of $\widetilde { \mathfrak { X } }$ of $\left( p , \sigma , u , \nu , w \right)$ for which $p$ is smooth.

Then the following theorem is well-known (see, e.g., [1]). -

# Theorem 4.3

(a) $\widetilde { \mathfrak { M } }$ is represented by a curve $\widetilde { M }$ smooth and proper over $L$ ;   
(b) $\mathfrak { M }$ is represented by ${ \tilde { M } } \backslash C ,$ , where $C$ is a finite set of “cusps”;   
(c) if $( p , \sigma , \alpha , \beta ) \in \widetilde { { \mathfrak { M } } } ( \widetilde { M } )$ corresponds to the identity map $\widetilde { M } \longrightarrow \widetilde { M } ,$ , and $p$ is the morphism from $\widetilde { X }$ to $\widetilde { M } _ { : }$ , then $\widetilde { X }$ represents $\widetilde { \mathfrak { X } } _ { \mathrm { { \varepsilon } } }$ , and $X = p ^ { - 1 } ( M )$ represents $\mathfrak { X }$ ;   
(d) if $\mathrm { { \dot { L } } = \mathbb { C } , }$ , then $\widetilde { M }$ and $\widetilde { X }$ are the varieties constructed above.

Fix a cusp $c \in C$ , i.e., a 4-tuple

$$
\begin{array} { r l r } & { } & { \overline { { p } } : \overline { { Y } } \longrightarrow \mathrm { S p e c } L , } \\ & { } & { \overline { { \sigma } } : \overline { { Y } } _ { 0 } \times _ { \mathrm { S p e c } L } \overline { { Y } } \longrightarrow \overline { { Y } } , \qquad } \\ & { } & { \overline { { u } } , \overline { { \nu } } : \mathrm { S p e c } L \longrightarrow \overline { { Y } } , \qquad } \end{array}
$$

where $\overline { { Y } }$ is a $k$ -gon. These are all isomorphic modulo the natural action of $\mathrm { S L } _ { 2 } ( \mathbb { Z } / k \mathbb { Z } )$ on $\widetilde { \mathfrak { M } }$ taking

$$
( p , \sigma , u , \nu ) \longmapsto ( p , \sigma , a u + b \nu , c u + d \nu ) .
$$

So let us assume $\bar { \nu }$ is in the identity component of $\overline { { Y } } _ { 0 }$ , and $\overline { { u } }$ is in an adjacent one:

![](images/a4cb852e980ace5aa715e291769c5c44914d9a985976467e5ea14a592bb6948c.jpg)

(When we assume this, $( \overline { { p } } , \overline { { \sigma } } , \overline { { u } } , \overline { { \nu } } )$ is unique up to isomorphism.) Let $\widehat { M }$ (resp.   
${ \widehat { X } } ,$ ) denote the formal completion of $\widetilde { M }$ (resp. $\widetilde { X }$ ) at $c$ (resp. along $p ^ { - 1 } ( c ) _ { \cdot } ^ { \cdot }$ ).

Now go back to the torus embeddings introduced earlier:

$$
\begin{array} { r l r } {  { \mathbb { G } _ { m } \times \mathbb { G } _ { m } \langle \mathrm { ~ { ~ \small ~ \alpha ~ } ~ } } } & { \operatorname { T } _ { \{ \sigma _ { n } \} } } \\ & { } & { \quad p _ { 2 } | \begin{array} { l } { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \mathbb { G } _ { m } \langle \mathrm { ~ { ~ \small ~ \alpha ~ } ~ } } \end{array}  } \end{array}
$$

where $\sigma _ { n }$ is the set of sectors $\langle ( n , 1 ) , ( n { + } 1 , 1 ) \rangle$ , $n \in \mathbb { Z }$ . Let $\alpha : X _ { \{ \sigma _ { n } \} } \longrightarrow X _ { \{ \sigma _ { n } \} }$ be the automorphism $( z , q ) \longrightarrow ( z q ^ { k } , q )$ , where $z$ and $q$ are coordinates on the first and second factor $\mathbb { G } _ { m }$ . Let ${ \widehat { X } } _ { \{ \sigma _ { n } \} }$ (resp. $\widehat { \mathbb { A } } _ { q } ^ { 1 \cdot }$ ) be the formal completion of $X _ { \{ \sigma _ { n } \} }$ (resp. $\mathbb { A } _ { q } ^ { 1 } .$ ) along the complement of the torus. Then we claim that there are canonical isomorphisms:

$$
\begin{array} { r l r } { \widehat { X } _ { \{ \sigma _ { n } \} } / \{ \alpha ^ { n } \} \xrightarrow { \sim } } & { \widehat { X } } \\ { p _ { 2 } \small { \Bigg \downarrow } } & { } & { \small { \Bigg \downarrow } p } \\ { \widehat { \mathbb { A } } _ { q } ^ { 1 } \xrightarrow { \sim } } & { \sim } & { \widehat { M } . } \end{array}
$$

We will show here only how to construct:

(a) a morphism $\widehat { \mathbb { A } } _ { q } ^ { 1 } \longrightarrow \widehat { M }$ ; (b) a map of functors

$$
\widehat { M } ( S ) \longrightarrow \widehat { \mathbb { A } } _ { q } ^ { 1 } ( S )
$$

for $S = { \mathrm { S p e c } } R$ , where $R$ is an Artin local $L$ -algebra with residue field $L$ .

We let the reader check that these are inverse to each other and that we get corresponding maps on the curves over these bases.

Construction (a) The point is that $\widehat { X } _ { \{ \sigma _ { n } \} } / \{ \alpha ^ { n } \}$ itself is flat and proper over $\widehat { \mathbb { A } } _ { q } ^ { 1 }$ and its (one) closed fiber is indeed a $k$ -gon. The action of $\mathbb { G } _ { m } \times \mathbb { G } _ { m }$ on $X _ { \{ \sigma _ { n } \} }$ is a morphism:

$$
\left( \mathbb { G } _ { m } \times \mathbb { G } _ { m } \right) \times _ { \mathbb { A } _ { q } ^ { 1 } } X _ { \{ \sigma _ { n } \} } \longrightarrow X _ { \{ \sigma _ { n } \} } ,
$$

and it is readily checked that this extends to

$$
\sigma : ( X _ { \{ \sigma _ { n } \} } ) _ { 0 } \times _ { \mathbb { A } _ { q } ^ { 1 } } X _ { \{ \sigma _ { n } \} } \longrightarrow X _ { \{ \sigma _ { n } \} } ,
$$

where $( X _ { \{ \sigma _ { n } \} } ) _ { 0 }$ is the open subset where $X _ { \{ \sigma _ { n } \} }$ is smooth over $\mathbb { A } _ { q } ^ { 1 }$ . This induces

$$
\sigma : ( \widehat { X } _ { \{ \sigma _ { n } \} } / \{ \alpha ^ { n } \} ) _ { 0 } \times _ { \mathbb { A } _ { q } ^ { 1 } } ( \widehat { X } _ { \{ \sigma _ { n } \} } / \{ \alpha ^ { n } \} ) \longrightarrow \widehat { X } _ { \{ \sigma _ { n } \} } / \{ \alpha ^ { n } \} \ .
$$

Finally, the sections $z = q$ and $z = \zeta$ of $\mathbb { G } _ { m } \times \mathbb { G } _ { m }$ over $\mathbb { G } _ { m }$ define sections

$$
u , \nu : { \widehat { \mathbb { A } } } _ { q } ^ { 1 } \longrightarrow ( { \widehat { X } } _ { \{ \sigma _ { n } \} } / \{ \alpha ^ { n } \} ) _ { 0 } \ .
$$

Construction (b) Now start with an element of ${ \widehat { M } } ( S )$ , where $S = { \mathrm { S p e c } } R$ as above, i.e., $( p , \sigma , u , \nu )$ , with $Y \longrightarrow S$ , extending the fixed $( \overline { { p } } , \overline { { \sigma } } , \overline { { u } } , \overline { { \nu } } )$ defining the cusp. Then $Y _ { \mathrm { r e d } } = \overline { { Y } }$ is a $k$ -gon of rational curves, so the universal cover $Y ^ { * }$ of $Y$ is locally of finite type over $s$ and $Y _ { \mathrm { r e d } } ^ { * }$ is just an infinite string of copies of $\mathbb { P } ^ { 1 }$ . If we fix an identity $e : S \longrightarrow Y ^ { * }$ over $e : S \longrightarrow Y$ , then we get a unique lifting of $\sigma : Y _ { 0 } \times Y \longrightarrow Y$ to

$$
\sigma ^ { * } : Y _ { 0 } ^ { * } \times Y ^ { * } \longrightarrow Y ^ { * }
$$

such that

$$
\begin{array} { l } { { \sigma ^ { * } ( e , e ) = e \mathrm { , } } } \\ { { \sigma ^ { * } ( x , y ) = \sigma ^ { * } ( y , x ) \ \mathrm { i f } \ x , y \in Y _ { 0 } ^ { * } . } } \end{array}
$$

Next, let $\overline { { Y } } _ { 0 } ( e )$ and $Y _ { 0 } ( e )$ denote the identity components of $\overline { { Y } } _ { 0 }$ and $Y _ { 0 }$ . Then there are two isomorphisms

$$
\overline { { Y } } _ { 0 } ( e ) \cong \mathbb { G } _ { m , L } ,
$$

and we can fix one of them by requiring that the point 0 in the closure of $\mathbb { G } _ { m , L }$ corresponds to the intersection point $Q$ of the closures of $\overline { { Y } } _ { 0 } ( e )$ and $\overline { { Y } } _ { 0 } ( \overline { { u } } )$ in $\overline { { Y } }$ . According to a result of Grothendieck [4], exp. IX, §3, tori are “rigid”, so this isomorphism lifts to a unique $S _ { \mathbf { \partial } }$ -isomorphism

$$
Y _ { 0 } ( e ) \cong \mathbb { G } _ { m , S } .
$$

But $Y _ { 0 } ^ { * } ( e ) \cong Y _ { 0 } ( e )$ , so we get an action of $\mathbb { G } _ { m , S }$ on $Y ^ { * }$ ; now we begin to see why torus embeddings are involved. Let $U ^ { - }$ be the open subset of $Y ^ { * }$ consisting of

“half the string” starting at $Y _ { 0 } ^ { * } ( e )$ and in the direction of the limit point 0 of $\mathbb { G } _ { m , S }$ :

![](images/a02eb711080cc02d91655f4940a6c627708b5e88af813fda428c65317ee99409.jpg)

Also lift $u$ to $u ^ { * } : S \longrightarrow Y ^ { * }$ so as to lie in the component adjacent to $Y _ { 0 } ^ { * } ( e )$ . Then:

Lemma 4.4 There exists a unique $\mathfrak { X } \in \Gamma ( U ^ { - } , \mathcal { O } _ { Y ^ { * } } )$ such that $\mathfrak { X } ( e ) = 1$ , and such that, under the action $\sigma _ { 0 } : \mathbb { G } _ { m , S } \times _ { S } U ^ { - } \longrightarrow U ^ { - }$ of $\mathbb { G } _ { m , S }$ on $U ^ { - }$ ,

$$
\sigma _ { 0 } ^ { * } ( { \mathfrak { X } } ) = z \cdot { \mathfrak { X } } ,
$$

where z is the coordinate on $\mathbb { G } _ { m , S }$

Proof Decompose $\Gamma ( U ^ { - } , \mathcal { O } _ { Y ^ { * } } )$ into eigenspaces under the action of $\mathbb { G } _ { m , S }$ :

$$
\Gamma ( U ^ { - } , \mathcal { O } _ { Y ^ { * } } ) = \bigoplus _ { n = - \infty } ^ { + \infty } W _ { n } ,
$$

where $\sigma _ { 0 } ^ { * } ( f ) = z ^ { n } \cdot f$ if $f \in W _ { n }$ . Since $U ^ { - }$ is flat over $R$ , it follows that $W _ { n }$ is a flat $R$ -module. But

$$
\Gamma ( U ^ { - } , \mathcal { O } _ { \overline { { { Y } } } ^ { * } } ) = \bigoplus _ { n = - \infty } ^ { + \infty } W _ { n } \otimes _ { R } L ,
$$

and since ${ \overline { { Y } } } ^ { * }$ is just a string of copies of $\mathbb { P } ^ { 1 }$ , one sees immediately that

$$
W _ { 1 } \otimes _ { R } L = L \cdot \overline { { { \mathfrak { X } } } } ,
$$

where the function $\overline { { \mathfrak { X } } }$ is $z$ on $\overline { { Y } } _ { 0 } ^ { * } ( e )$ and 0 on all the other components. Therefore $W _ { 1 }$ is a free rank-1 $R$ -module, and the condition $\mathfrak { X } ( e ) = 1$ picks out a unique element.

Now let $\sigma _ { 1 } ( x ) = \sigma ^ { * } ( u ^ { * } , x )$ , giving us an automorphism $\sigma _ { 1 } : Y ^ { * } \longrightarrow Y ^ { * }$ , and a morphism $\sigma _ { 1 } : U ^ { - } \longrightarrow U ^ { - }$ . Then $\sigma _ { 1 } ^ { * } ( { \mathfrak { X } } )$ is another element of $\Gamma ( U ^ { - } , \mathcal { O } _ { Y ^ { * } } )$ in $W _ { 1 }$ (notation as in the proof of the preceding lemma), so

$$
{ \pmb \sigma } _ { 1 } ^ { * } ( { \pmb x } ) = { \pmb q } \cdot { \pmb x } , \mathrm { f o r ~ s o m e ~ } { \pmb q } \in { \pmb R } .
$$

This $q$ is the sought-for period! It defines a homomorphism

$$
L [ [ q ] ] \longrightarrow R \ ,
$$

and hence an element of $\widehat { \mathbb { A } } _ { q } ^ { 1 } ( S )$ .

# 5 Hirzebruch’s theory of the Hilbert modular group

We now investigate a second beautiful example in order to motivate and illustrate further all the theory which follows.

Let $K = \mathbb { Q } ( { \sqrt { d } } )$ be a real quadratic number field and associate to it the following objects:

$\begin{array} { r l } & { \mathcal { O } = \mathrm { r i n g ~ o f ~ i n t e g e r s ~ i n } K , } \\ & { \mathfrak { a } = \mathrm { a } \mathrm { ~ f x e d ~ i d e a l ~ i n } \mathcal { O } , } \\ & { u _ { 0 } = \mathrm { a ~ g e n e r a t o r ~ o f ~ t h e ~ g r o u p ~ o f ~ u n i t s ~ } u \in \mathcal { O } , } \\ & { \qquad u \equiv 1 \mathrm { ~ m o d ~ a ~ } ( \mathrm { o r ~ o f ~ t h i s ~ g r o u p ~ m o d } \pm 1 ) . } \end{array}$ such that

We do not regard $K$ as a subfield of $\mathbb { R }$ , but rather as an abstract field extension of $\mathbb { Q }$ , with two embeddings:

$$
\phi _ { 1 } , \phi _ { 2 } : K \longrightarrow \mathbb { R } \ ,
$$

neither being more important than the other. Let

$$
\Gamma = \left\{ \left( \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right) \in \mathrm { { \bf S L } } ( 2 , \theta ) \mid \left( \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right) \equiv \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right) \ \mathrm { m o d } \mathfrak { a } \right\} \ .
$$

Consider the following embedding:

$$
\begin{array} { r l } & { \quad \mathrm { S L } ( 2 , K ) \longrightarrow \mathrm { S L } ( 2 , \mathbb { R } \times \mathrm { S L } ( 2 , \mathbb { R } ) } \\ & { \left( \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right) \longmapsto \left( \left( \begin{array} { l l } { \phi _ { 1 } ( a ) } & { \phi _ { 1 } ( b ) } \\ { \phi _ { 1 } ( c ) } & { \phi _ { 1 } ( d ) } \end{array} \right) , \left( \begin{array} { l l } { \phi _ { 2 } ( a ) } & { \phi _ { 2 } ( b ) } \\ { \phi _ { 2 } ( c ) } & { \phi _ { 2 } ( d ) } \end{array} \right) \right) \ . } \end{array}
$$

Then there is a unique $\mathbb { Q }$ -structure on $\mathrm { S L } ( 2 , \mathbb { R } ) \times \mathrm { S L } ( 2 , \mathbb { R } )$ with $\operatorname { S L } ( 2 , K )$ as its $\mathbb { Q }$ -rational points and $\Gamma$ is an arithmetic subgroup for this $\mathbb { Q }$ -structure. We let

$\mathrm { S L } ( 2 , \mathbb { R } ) \times \mathrm { S L } ( 2 , \mathbb { R } )$ act componentwise on ${ \mathfrak { H } } \times { \mathfrak { H } }$ and seek to compactify the so-called Hilbert modular surface:

$$
\mathfrak { F } _ { K , \mathfrak { a } } = ( \mathfrak { H } \times \mathfrak { H } ) / \Gamma .
$$

It is known (see Shimizu [5]) that $\mathfrak { F } _ { K , \mathfrak { a } }$ can be embedded in a compact normal analytic surface $\overline { { \mathfrak { F } } } _ { K , \mathfrak { a } }$ by adding only a finite number of points, called cusps $F _ { 1 } , \dots , F _ { N }$ :

![](images/e31d79b8f1347c4eee3aa0152d433f6064428fa45f8371909a97cf1c204881c0.jpg)

Topologically, starting with the simplest cusp “i∞”, here is the picture: let

$$
\begin{array} { r l } & { W _ { d } = \left\{ \left( z _ { 1 } , z _ { 2 } \right) \big \vert \mathrm { I m } z _ { 1 } \cdot \mathrm { I m } z _ { 2 } \geq d \right\} \subset \mathfrak { H } \times \mathfrak { H } ; } \\ & { \Gamma _ { 1 } = \left\{ \left( \begin{array} { l l } { 1 } & { b } \\ { 0 } & { 1 } \end{array} \right) \big \vert b \in \mathfrak { a } \right\} , } \end{array}
$$

and let

$$
\begin{array} { r l } & { \Gamma _ { 2 } = \left\{ \left( \begin{array} { c c } { u _ { 0 } ^ { n } } & { b } \\ { 0 } & { u _ { 0 } ^ { - n } } \end{array} \right) \big | n \in \mathbb { Z } , b \in \mathfrak { a } \right\} } \\ & { \quad = \Gamma \cap \left\{ \left( \begin{array} { c c } { a } & { b } \\ { 0 } & { d } \end{array} \right) \right\} / \Gamma \cap \{ \pm 1 \} . } \end{array}
$$

Then $\Gamma _ { 2 } \cdot W _ { d } = W _ { d }$ (use the fact that $\phi _ { 1 } \left( u _ { 0 } \right) \cdot \phi _ { 2 } \left( u _ { 0 } \right) = \mathrm { N o r m } \left( u _ { 0 } \right) = \pm 1 $ : see (ii) below), and it turns out that if $d \gg 0$ , then $\Gamma$ -equivalence on ${ \mathfrak { H } } \times { \mathfrak { H } }$ reduces on $W _ { d }$ to $\pm \Gamma _ { 2 }$ -equivalence, i.e.,

$$
z _ { 1 } , z _ { 2 } \in W _ { d } , z _ { 1 } = \gamma z _ { 2 } \mathrm { ~ f o r ~ s o m e ~ } \gamma \in \Gamma \Longrightarrow \gamma \in \pm \Gamma _ { 2 }
$$

Since $\pm 1$ acts trivially on ${ \mathfrak { H } } \times { \mathfrak { H } }$ , we get $W _ { d } / \Gamma _ { 2 } \subset ( { \mathfrak { H } } \times { \mathfrak { H } } ) / \Gamma = { \mathfrak { F } } _ { K , { \mathfrak { a } } }$ . But $W _ { d } / \Gamma _ { 2 }$ is easy to visualize:

(i) $\Gamma _ { 1 }$ acts by $( z _ { 1 } , z _ { 2 } ) \mapsto ( z _ { 1 } + \phi _ { 1 } ( b ) , z _ { 2 } + \phi _ { 2 } ( b ) )$ and

$$
\Phi ( { \mathfrak { a } } ) = \{ ( \phi _ { 1 } ( b ) , \phi _ { 2 } ( b ) ) | b \in { \mathfrak { a } } \}
$$

is a lattice in $\mathbb { R } \times \mathbb { R }$ ;

(ii) $\Gamma _ { 1 }$ is a normal subgroup of $\Gamma _ { 2 }$ and $\Gamma _ { 2 } / \Gamma _ { 1 } \cong \mathbb { Z }$ with generator $\%$ equal to the image of $\left( \begin{array} { c c } { { u _ { 0 } } } & { { 0 } } \\ { { 0 } } & { { u _ { 0 } ^ { - 1 } } } \end{array} \right)$ . Now $\Gamma _ { 1 }$ leaves invariant $\mathrm { I m } z _ { 1 }$ and $\mathrm { I m } z _ { 2 }$ , and $\Gamma _ { 2 } / \Gamma _ { 1 }$ acts on these by

$$
\begin{array} { r l } & { \gamma _ { 0 } ^ { * } ( \operatorname { I m } z _ { 1 } ) = \phi _ { 1 } ( u _ { 0 } ) ^ { 2 } \cdot \operatorname { I m } z _ { 1 } , } \\ & { \gamma _ { 0 } ^ { * } ( \operatorname { I m } z _ { 2 } ) = \phi _ { 2 } ( u _ { 0 } ) ^ { 2 } \cdot \operatorname { I m } z _ { 2 } = \phi _ { 1 } ( u _ { 0 } ) ^ { - 2 } \cdot \operatorname { I m } z _ { 2 } ; } \end{array}
$$

(iii) hence $\mathrm { I m } z _ { 1 } \cdot \mathrm { I m } z _ { 2 }$ is invariant under $\Gamma _ { 2 }$ .

Think of $1 / \left( \mathrm { I m } z _ { 1 } \cdot \mathrm { I m } z _ { 2 } \right)$ as measuring the distance to the cusp. For every fixed $e$ , if $z _ { i } = x _ { i } + \mathrm { i } y _ { i }$ , we get a diagram

$$
\begin{array} { r l } & { M _ { e } = \big \{ \big ( z _ { 1 } , z _ { 2 } \big ) \big | \operatorname { I m } z _ { 1 } \cdot \operatorname { I m } z _ { 2 } = e \big \} / \Gamma _ { 2 } } \\ & { \qquad \quad \sqrt { \operatorname { f i b e r } \big \{ \big ( x _ { 1 } , x _ { 2 } \big ) \in \mathbb { R } ^ { 2 } \big \} / \Phi ( \mathfrak { a } ) } } \\ & { \qquad \quad \big \{ \big ( y _ { 1 } , y _ { 2 } \big ) \in \mathbb { R } _ { > 0 } ^ { 2 } \big | y _ { 1 } \cdot y _ { 2 } = e \big \} / \big \{ \gamma _ { 0 } ^ { n } \big \} \quad \overset { \approx } { \underset { \mathrm { h o m e o } } { \approx } } S ^ { 1 } , } \end{array}
$$

from which it follows that $M _ { e }$ is a compact 3-manifold which is an $S ^ { 1 } \times S ^ { 1 }$ bundle over $S ^ { 1 }$ . As $e$ varies, the manifolds $M _ { e }$ are all homeomorphic and we get

$$
\begin{array} { r c l } { { ( z _ { 1 } , z _ { 2 } ) } } & { { \in } } & { { W _ { d } / \Gamma _ { 2 } } } \\ { { \displaystyle { \vphantom { \int } } } } & { { } } & { { \vphantom { \int } } } \\ { { \mathrm { I m } z _ { 1 } \cdot \mathrm { I m } z _ { 2 } } } & { { \in } } & { { [ d , \infty ) ~ , } } \end{array}
$$

i.e.,

$$
W _ { d } / \Gamma _ { 2 } \approx _ { \mathrm { \small h o m e o } } M _ { d } \times \left[ d \infty \right) .
$$

The compactification $\overline { { \mathfrak { F } } } _ { k , { \mathfrak { a } } }$ in the subset $W _ { d } / \Gamma _ { 2 }$ simply results, topologically, by embedding $M _ { d } \times [ d , \infty )$ in the cone over $M _ { d }$ , i.e., the one-point compacti- fication of $W _ { d } / \Gamma _ { 2 }$ . Thus the subsets $M _ { d ^ { \prime } } / \Gamma _ { 2 }$ , as $d ^ { \prime } \longrightarrow \infty$ , are a fundamental system of neighborhoods of the cusp $F _ { 1 } = \mathrm { i } \infty$ .

There may be other cusps too: for every $\gamma \in \mathrm { S L } ( 2 , K )$ , consider the subset $\gamma ( W _ { d } ) \subset { \mathfrak { H } } \times { \mathfrak { H } }$ . If $B \subset \operatorname { S L } ( 2 , K )$ is the subgroup of matrices $\left( \begin{array} { c c } { { a } } & { { b } } \\ { { 0 } } & { { a ^ { - 1 } } } \end{array} \right)$ then $\gamma ( W _ { d } )$ is left invariant by the group $\Gamma \cap \gamma B \gamma ^ { - 1 }$ , and if $d \gg 0$ , then, as before,

$$
\gamma ( W _ { d } ) / \Gamma \cap \gamma B \gamma ^ { - 1 } \subset ( \mathfrak { H } \times \mathfrak { H } ) / \Gamma .
$$

Moreover, $\Gamma \cap \gamma B \gamma ^ { - 1 } \cong \gamma ^ { - 1 } \Gamma \gamma \cap B$ , which is an extension

$$
\begin{array} { r l } & { 1 \longrightarrow \left\{ b \in K \vert \left( \begin{array} { c c } { 1 } & { b } \\ { 0 } & { 1 } \end{array} \right) \in \gamma ^ { - 1 } \Gamma \gamma \right\} \longrightarrow \gamma ^ { - 1 } \Gamma \gamma \cap B \longrightarrow } \\ & { \longrightarrow \left\{ u \in K ^ { * } \vert \left( \begin{array} { c c } { u } & { b } \\ { 0 } & { u ^ { - 1 } } \end{array} \right) \in \gamma ^ { - 1 } \Gamma \gamma \mathrm { ~ f o r ~ s o m e } b \right\} \longrightarrow 1 } \\ & { \qquad \mathbb { Z } \mathrm { ~ o r ~ } \mathbb { Z } \times ( \mathbb { Z } / 2 \mathbb { Z } ) } \end{array}
$$

(the 2-torsion comes from $u = \pm 1$ , and if this occurs it acts trivially on ${ \mathfrak { H } } \times { \mathfrak { H } }$ , so we ignore it), from which it follows, as before, that

$$
\gamma ( W _ { d } ) / \Gamma \cap \gamma B \gamma ^ { - 1 } \underset { \mathrm { h o m e o } } { \approx } M ( \gamma ) \times [ d , \infty )
$$

for some compact 3-manifold  $M ( \gamma )$ which is an  $S ^ { 1 } \times S ^ { 1 }$ -bundle over $S ^ { 1 }$ . Again, we make a one-point compactification.

Actually, there are only finitely many cusps. In fact

(a) if $\gamma ^ { \prime } = \gamma \cdot \delta$ , with $\delta = \left( \begin{array} { c c } { { a } } & { { b } } \\ { { 0 } } & { { a ^ { - 1 } } } \end{array} \right) \in B _ { \sf }$ , then $\gamma ^ { \prime } ( W _ { d } ) = \gamma ( W _ { d ^ { \prime } } )$ , where $d ^ { \prime } = d \cdot \mathrm { N o r m } ( a ) ^ { 2 }$ , and $\Gamma \cap \gamma ^ { \prime } B \gamma ^ { - 1 } = \Gamma \cap \gamma B \gamma ^ { - 1 }$ , so we have the same cusp;

(b) if $\gamma ^ { \prime } = \varepsilon \cdot \gamma$ with $\varepsilon \in \Gamma$ , then the images of $\gamma ( W _ { d } )$ and $\gamma ( W _ { d } )$ in $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma$ are the same, hence

$$
\begin{array} { c } { { \gamma ( { \cal W } _ { d } ) / \Gamma \cap \gamma B \gamma ^ { - 1 } \subset } } \\ { { \big \Vert \qquad \big . \bigcup _ { \zeta ^ { \prime } ( W _ { d } ) / \Gamma \cap \gamma ^ { \prime } B \gamma ^ { - 1 } } \langle \mathnormal { \mathfrak T } \times \mathfrak { H } \rangle / \Gamma } } \end{array}
$$

Hence the cusp depends only on the double coset $\Gamma \gamma B \in \Gamma \backslash \mathrm { S L } ( 2 , K ) / B$ . It is easy to check that if $\Gamma \gamma B \ne \Gamma \gamma ^ { \prime } B$ , then, for $d \gg 0$ , the images of $\gamma ( W _ { d } )$ and $\gamma ( W _ { d } )$ in $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma$ are disjoint; hence if we want $\overline { { \mathfrak { F } } } _ { K , \mathfrak { a } }$ to be normal (and we do), we must have different cusps here. Thus

$$
{ \mathrm { \# c u s p s } } = \# ( \Gamma \backslash \mathrm { S L } ( 2 , K ) / B ) ,
$$

which is finite by a classical theorem (in fact, one can check that if ${ \mathfrak { a } } = { \mathcal { O } }$ , then

$$
\Gamma \backslash { \mathrm { S L } } ( 2 , K ) / B \cong { \mathrm { i d e a l ~ c l a s s ~ g r o u p ~ o f ~ } } K { \mathrm { ) } } \ .
$$

Now, how do we put an analytic structure on $\overline { { \mathfrak { F } } } _ { K , { \mathfrak { a } } } ?$ We shall only do this at the end and instead, by following the suggestions made by the above topological construction, plus our knowledge of toroidal embeddings, define directly a blown-up non-singular compactification $\widetilde { \mathfrak { F } } _ { K , \mathfrak { a } }$ of $\mathfrak { F } _ { K , \mathfrak { a } }$ . Again we start with the cusp $\mathrm { i } \infty$ . The idea is first to factor the canonical map ${ \mathfrak { H } } \times { \mathfrak { H } } \longrightarrow { \mathfrak { F } } _ { K , { \mathfrak { a } } }$ as follows:

$$
{ \mathfrak { H } } \times { \mathfrak { H } } \longrightarrow ( { \mathfrak { H } } \times { \mathfrak { H } } ) / \Gamma _ { 1 } \longrightarrow ( { \mathfrak { H } } \times { \mathfrak { H } } ) / \Gamma _ { 2 } \longrightarrow { \mathfrak { F } } _ { K , \mathfrak { a } } ~ .
$$

We may embed $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 }$ in a torus as follows: $\Gamma _ { 1 }$ acts on ${ \mathfrak { H } } \times { \mathfrak { H } }$ by translations by the lattice $\Phi ( { \mathfrak { a } } )$ in $\mathbb { R } \times \mathbb { R }$ :

$$
( z _ { 1 } , z _ { 2 } ) \longmapsto ( z _ { 1 } + \phi _ { 1 } ( b ) , z _ { 2 } + \phi _ { 2 } ( b ) ) , b \in { \mathfrak { a } } .
$$

Let $T$ be the torus given by $\mathbb { C } \times \mathbb { C }$ modulo the same group of translations:

$$
T = \mathbb { C } \times \mathbb { C } / \Phi ( { \mathfrak { a } } ) ~ ,
$$

so that

$$
\begin{array} { r } { N ( T ) = \Phi ( \mathfrak { a } ) \ , \ } \\ { N ( T ) _ { \mathbb { R } } = \mathbb { R } \times \mathbb { R } \ , \ } \end{array}
$$

and we get the exact sequence:

$$
0 \xrightarrow [ ] { 0 } T _ { c } \xrightarrow [ ] { } T \xrightarrow [ ] { \mathrm { \ o r d } } \mathrm { N } _ { \mathbb { R } } ( T ) \xrightarrow [ ] { } 0
$$

$$
\left( z _ { 1 } , z _ { 2 } \right) \longmapsto \left( \operatorname { I m } z _ { 1 } , \operatorname { I m } z _ { 2 } \right)
$$

It follows that:

$$
\begin{array} { r l } & { ( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 } \cong \mathrm { o r d } ^ { - 1 } ( \mathbb { R } _ { > 0 } \times \mathbb { R } _ { > 0 } ) \ , } \\ & { \qquad W _ { d } / \Gamma _ { 1 } \cong \mathrm { o r d } ^ { - 1 } ( \underbrace { \{ ( y _ { 1 } , y _ { 2 } ) \mid y _ { 1 } y _ { 2 } \geq d , y _ { i } > 0 \} } _ { \mathrm { c a l l ~ t h i s ~ } V _ { d } } ) \ . } \end{array}
$$

The first set is open in $T$ , the second set is closed in the first. Next, $\Gamma _ { 2 } / \Gamma _ { 1 } \cong$ $\{ \gamma _ { 0 } ^ { n } \}$ , and $\%$ acts on ${ \mathfrak { H } } \times { \mathfrak { H } }$ by

$$
\gamma _ { 0 } ( z _ { 1 } , z _ { 2 } ) = ( \phi _ { 1 } ( u _ { 0 } ) ^ { 2 } z _ { 1 } , \phi _ { 1 } ( u _ { 0 } ) ^ { - 2 } z _ { 2 } ) .
$$

Let $\nu _ { 0 } = \phi _ { 1 } ( u _ { 0 } ) ^ { 2 }$ . Now the action of $\gamma _ { 0 }$ on ${ \mathfrak { H } } \times { \mathfrak { H } }$ extends to $\mathbb { C } \times \mathbb { C }$ , hence to $T$ and to the open subset $( { \mathfrak { H } } \times { \mathfrak { H } } ) / { \Gamma _ { 1 } } \subset T$ . In particular, $\gamma _ { 0 }$ acts on $N _ { \mathbb { R } } ( T )$ by

$$
\gamma _ { 0 } ( x _ { 1 } , x _ { 2 } ) = ( \nu _ { 0 } x _ { 1 } , \nu _ { 0 } ^ { - 1 } x _ { 2 } ) ,
$$

an action which preserves the positive quadrant and the (irrational) lattice $\Phi ( { \mathfrak { a } } )$ . We have thus arrived at the following situation: $T$ is a two-dimensional torus and $\gamma _ { 0 } : T \longrightarrow T$ is a hyperbolic automorphism of infinite order (in fact, up to replacing $\%$ by a power or a root, we have obtained the most general hyperbolic automorphism of $\mathbb { G } _ { m } ^ { 2 } .$ ).

At this point, the idea is to enlarge $T$ – and its open subsets $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 }$ and $W _ { d } / \Gamma _ { 1 } - \mathsf { b y }$ adding some analytic boundary $\mathcal { E }$ , so that $\%$ still acts on $T \cup \mathcal { E }$ , and then to divide by $\{ \gamma _ { 0 } ^ { n } \}$ so that $E = \mathcal { E } / \{ \gamma _ { 0 } ^ { n } \}$ is the boundary that can be added to $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma$ ‘in the direction $\mathrm { i } \infty ^ { \cdot }$ :

![](images/b15d6e16b7fef32b390b553c6543864999e7db17bb60c2c823ccb1014dbcc435.jpg)

To enlarge $T$ , we use the theory of torus embeddings. (i) We seek a decomposition of the positive quadrant $\mathbb { R } _ { \geq 0 } \times \mathbb { R } _ { \geq 0 }$ into rational sectors $\{ \sigma _ { \alpha } \}$ .

(ii) These should satisfy: $\gamma _ { 0 } \sigma _ { \alpha } = \mathrm { s o m e } \ \sigma _ { \beta } ; \bigcup \sigma _ { \alpha } = \mathbb { R } _ { \ge 0 } \times \mathbb { R } _ { \ge 0 } ; \sigma _ { \alpha } \cap \sigma _ { \beta } = ( 0$ or a common edge. Note that since $( 0 ) \times \mathbb { R } _ { \geq 0 }$ and $\mathbb { R } _ { \geq 0 } \times ( 0 )$ are irrational half-lines, all $\sigma _ { \alpha }$ are in the interior of the positive quadrant, and we will need an infinite number of $\sigma _ { \alpha }$ . However, we require:

modulo the action of $\%$ , there are only finitely many $\sigma _ { \alpha }$ .

(iii) In this case, if we denote one of the $\sigma _ { \alpha }$ by $\sigma _ { 0 }$ , we can number them uniquely $\ldots , \sigma _ { - 2 } , \sigma _ { - 1 } , \sigma _ { 0 } , \sigma _ { 1 } , \sigma _ { 2 } , \ldots$ so that $\sigma _ { i } \cap \sigma _ { j }$ is a common edge if and only if $i = j \pm 1$ , and $\gamma _ { 0 } \sigma _ { i } = \sigma _ { i + d }$ for all $i$ and some fixed $d$ . Let $\ell _ { i } = \sigma _ { i } \cap \sigma _ { i + 1 }$ . It looks like this:

![](images/1decb0c970e8723aef7242bbadc83a9ac500615cac8348d50295d90be4c6f241.jpg)

(iv) Given such $\{ \sigma _ { \alpha } \}$ , we obtain a torus embedding

$$
T \subset X _ { \{ \sigma _ { \alpha } \} } ,
$$

where $X _ { \{ \sigma _ { \alpha } \} }$ is a scheme locally of finite type over $\mathbb { C }$ (in fact, locally a normal complex variety), with the action of $\%$ extending to $X _ { \{ \sigma _ { \alpha } \} }$ . Moreover, $X _ { \{ \sigma _ { \alpha } \} }$ is the union of $T$ and an infinite chain of non-singular rational curves $E _ { i }$ , one for each half-line $\ell _ { i }$ , meeting at points $P _ { i }$ , one for each sector $\sigma _ { i }$ :

![](images/8e00fb68c08af3b00ece6266e329ea5e97bcbd206448bca7d4163aaf2c9bf819.jpg)

(v) Next enlarge $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 }$ by setting

$$
( \widetilde { \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 } } = ( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 } \cup \bigcup _ { i = - \infty } ^ { + \infty } E _ { i } .
$$

In fact, in the corresponding embedding

$$
N _ { \mathbb { R } } ( T ) \subset N _ { \{ \sigma _ { i } \} } ,
$$

it is clear that

$$
\begin{array} { r } { \bigoplus _ { > 0 } \times \bigoplus _ { > 0 } = \mathbb { R } _ { > 0 } \times \mathbb { R } _ { > 0 } \cup \qquad \quad N _ { \{ \sigma _ { i } \} } \setminus N _ { \mathbb { R } } ( T ) } \end{array}
$$

chain of boundary segments

is the interior of the closure of $\mathbb { R } _ { > 0 } \times \mathbb { R } _ { > 0 }$ in $N _ { \{ \sigma _ { i } \} }$ . Therefore taking ord $^ { - 1 }$ , $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 }$ is the interior of the closure of   $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 }$ in $X _ { \{ \sigma _ { \alpha } \} }$ .

(vi) It is easy to see that $\Gamma _ { 2 } / \Gamma _ { 1 } = \{ \gamma _ { 0 } ^ { n } \}$ acts discontinuously on $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 }$ . In fact, check first that it acts discontinuously on $\mathbb { R } _ { > 0 } \times \mathbb { R } _ { > 0 }$ with fundamental domain $\Omega = \overline { { \binom { d - 1 } { i = 0 } \sigma _ { i } } } \bigg )$

![](images/a882ca50579d64600672743d9a42c7511ee83067358ebc8630038df18a655f6e.jpg)

with quotient looking topologically like this:

![](images/2b76c4f7e8248c8da5b01501b89ed089bcc74eb7860952191e643a2c472f6881.jpg)

Note that $\Omega \cap V _ { d }$ is compact modulo $\mathbb { R } _ { > 0 }$ , hence $V _ { d } / \{ \gamma _ { 0 } ^ { n } \}$ is compact modulo $\mathbb { R } _ { > 0 }$ . Therefore ord $^ { - 1 } ( \Omega )$ is a fundamental domain in $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 }$ and we get an analytic space

$$
( ( \widetilde { \mathfrak { H } \times \mathfrak { H } } ) / \Gamma _ { 1 } ) / ( \Gamma _ { 2 } / \Gamma _ { 1 } ) ,
$$

consisting of the open piece $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 2 }$ and a closed analytic set

$$
E = \left( \bigcup _ { i = - \infty } ^ { + \infty } E _ { i } \right) / \{ \gamma _ { 0 } ^ { n } \} ,
$$

which is a $d$ -sided polygon of rational curves $\overline { { E } } _ { 0 } \cup \cdots \cup \overline { { E } } _ { d - 1 }$ (with $\overline { { E } } _ { i }$ the

image of $E _ { i }$ ):

![](images/25f517808790723fcc5dfac00b913382691a80e638a8d61d0e88578d5515cec6.jpg)

(Here $\overline { { E } } _ { i } \longmapsto \nu _ { i }$ and $\overline { { E } } _ { i } \cap \overline { { E } } _ { i + 1 } \longmapsto \nu _ { i } \cap \nu _ { i + 1 }$ under the ord map.) Moreover, in here, $W _ { d } / \Gamma _ { 2 } \cup E$ is compact (since ord is proper). Thus, as above, since $W _ { d } / \Gamma _ { 2 } \subset \mathfrak { F } _ { K , { \mathfrak { a } } }$ , we can form $\mathfrak { F } _ { K , \mathfrak { a } } \cup E$ and make it into an analytic space by the above analytic structures on the two subsets $\mathfrak { F } _ { K , { \mathfrak { a } } }$ and $W _ { d } / \Gamma _ { 2 } \cup E$ .

To recover our previous compactification of the cusp $\mathrm { i } \infty$ , we shall blow down $E$ to a point. This can be accomplished by checking that $E$ has a fundamental system of strongly pseudoconvex neighborhoods. But in fact, $V _ { d }$ is a strongly convex subset of $\mathbb { R } _ { > 0 } \times \mathbb { R } _ { > 0 }$ in the following sense: for all $x \in \partial V _ { d }$ , the subset $V _ { d }$ is defined near $x$ by an equation $\varphi _ { x } \geq 0$ , where, for all $t \neq 0$ in the tangent space to $\partial V _ { d }$ at $x$ , defined by $\mathrm { d } \varphi _ { x } ( t ) = 0$ , we have

$$
\mathrm { d } ^ { 2 } \varphi _ { x } ( t , t ) < 0 .
$$

It is an easy lemma that, if a closed subset $W \subset \mathbb { C } ^ { n }$ is defined at a boundary point $z \in \partial W$ by

$$
\varphi _ { z } ( \mathsf { R e } z _ { 1 } , \ldots , \mathsf { R e } z _ { n } ) \geq 0 ,
$$

then $W$ is strongly pseudoconvex at $z$ if and only if the closed set $V \subset \mathbb { R } ^ { n }$ given by $\varphi _ { z } ( x _ { 1 } , \ldots , x _ { n } ) \geq 0$ is strongly convex. Since $\log | z _ { i } | = \operatorname { R e } \log z _ { i }$ , this implies that $W _ { d }$ is strongly pseudoconvex. Therefore

$$
\bigcup _ { i = 0 } ^ { d - 1 } \overline { { E } } _ { i } \subset ( ( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 } ) / ( \Gamma _ { 2 } / \Gamma _ { 1 } )
$$

is an exceptional set and can be blown down to a point.

But the advantage of our boundary is that we can make it non-singular. In fact, let $e _ { i }$ be the smallest integral point on the half-line $\ell _ { i }$ , i.e., $e _ { i } \in \ell _ { i } \cap \Phi ( { \mathfrak { a } } )$ . Then from TE I, we know:

$X _ { \{ \sigma _ { i } \} }$ non-singular $\Longleftrightarrow e _ { i }$ and $e _ { i + 1 }$ generate the lattice $\Phi ( { \mathfrak { a } } )$ for all $i$ .

But it is easy to check that, for any two $e , e ^ { \prime } \in \Phi ( { \mathfrak { a } } )$ ,

$$
e , e ^ { \prime } \ \mathrm { g e n e r a t e } \ \Phi ( { \mathfrak a } ) \longleftrightarrow \left[ \begin{array} { c } { \mathrm { t h e \ i n t e r s e c t i o n \ o f \ \Phi ( { \mathfrak a } ) \ a n d \ t h e } } \\ { \mathrm { t r i a n g l e \ { \overline { { 0 , e , e ^ { \prime } } } } \ c o n t a i n s \ o n l y \ 0 , } e \ \mathrm { a n d } e ^ { \prime } } \end{array} \right] \ .
$$

Now introduce

$$
\Sigma = \mathrm { c o n v e x ~ h u l l ~ o f ~ } \mathbb { R } _ { > 0 } \times \mathbb { R } _ { > 0 } \cap \Phi ( \mathfrak { a } )
$$

![](images/7055539ed5f221fcbd8650d59855c24091b78eda3891a9161bde2bf0326a5dba.jpg)  
$x , y$ coordinates for which $\Phi ( { \mathfrak { a } } ) = \mathbb { Z } ^ { 2 }$

It follows that if $X _ { \{ \sigma _ { i } \} }$ is non-singular, then the $e _ { i }$ must include all lattice points on $\partial \Sigma$ . On the other hand, if we take the $e _ { i }$ to be precisely the points $\Phi ( { \boldsymbol { \mathfrak { a } } } ) \cap \partial \Sigma$ , and let $\ell _ { i } = \mathbb { R } _ { \geq 0 } e _ { i }$ , $\sigma _ { i } = \langle e _ { i - 1 } , e _ { i } \rangle$ , then the corresponding $X _ { \{ \sigma _ { i } \} }$ is non-singular. So this is the minimal non-singular choice of $X _ { \{ \sigma _ { i } \} }$ and leads to the minimal desingularization of the old boundary $( 5 \times 5 ) / \Gamma _ { 2 } \cup$ (one point). One can, by the way, easily compute from the theory of TE I the intersection matrix $( \overline { { E } } _ { i } \cdot \overline { { E } } _ { j } )$ for the curves $\overline { { E } } _ { i }$ on $( ( \mathfrak { H } \times \mathfrak { H } ) / \Gamma _ { 1 } ) / ( \Gamma _ { 2 } / \Gamma _ { 1 } )$ by the following recipe:

(a) number the $\overline { { E } } _ { i }$ cyclically, i.e., $\overline { { E } } _ { i + d } = \overline { { E } } _ { i }$ ; (b) then, if $i \neq j$ ,

$$
( \overline { { E } } _ { i } \cdot \overline { { E } } _ { j } ) = \left\{ \begin{array} { l l } { { 0 } } & { { \mathrm { i f } | i - j | > 1 } } \\ { { 1 } } & { { \mathrm { i f } | i - j | = 1 ; } } \end{array} \right.
$$

(c) $( \overline { { E } } _ { i } ^ { 2 } ) = - d _ { i }$ , where $d _ { i }$ is the index in $\Phi ( { \mathfrak { a } } )$ of the subgroup generated by $e _ { i - 1 }$ and $e _ { i + 1 }$ ; alternatively,

$$
d _ { i } = 2 \cdot \mathsf { a r e a } ( \overline { { 0 , e _ { i - 1 } , e _ { i + 1 } } } ) ,
$$

if the area is normalized so that area $( \mathbb { R } \times \mathbb { R } / \Phi ( { \mathfrak { a } } ) ) = 1$

Also, it is well-known that the vertices of $\Sigma$ are nothing but the consecutive

best rational approximations to the irrational lines $( 0 ) \times \mathbb { R }$ and $\mathbb { R } \times ( 0 )$ , generated by the continued fraction expansion of the slope of these lines (expressed via a basis of $\Phi ( { \mathfrak { a } } ) { \big . }$ ).

In the same way, we can handle the other cusps and glue in polygons of rational curves there. For every cusp $F$ corresponding to $\Gamma \gamma B$ , the isomorphism

$$
\begin{array} { r l r } { ( \mathfrak { H } \times \mathfrak { H } ) / \Gamma \overset { \sim } { \longrightarrow } ( \mathfrak { H } \times \mathfrak { H } ) / \gamma ^ { - 1 } \Gamma \gamma , } & { } & \\ { x \longmapsto \gamma ^ { - 1 } x , } & { } & \end{array}
$$

carries $F$ to the standard cusp $\mathrm { i } \infty$ , so it suffices to repeat the above construction, replacing $\Gamma$ by $\gamma ^ { - 1 } \Gamma \gamma$ and then to carry back the resulting boundary piece $E$ to $( \mathfrak { H } \times \mathfrak { H } ) / \Gamma$ via the above isomorphism.

# References

[1] P. Deligne and M. Rapoport, Les schemas de modules de courbes ellip- ´ tiques, in Modular Functions of One Variable, II (Proc. Internat. Summer School, Univ. Antwerp, Antwerp, 1972). Lecture Notes in Mathematics 349. Berlin: Springer, 1973, pp. 143–316.   
[2] S. Lang, Elliptic Functions. Reading, MA: Addison-Wesley Publishing Co., Inc., 1973. With an appendix by J. Tate.   
[3] D. Mumford, An analytic construction of degenerating abelian varieties over complete rings, Compositio Math. 24 (1972), 239–272.   
[4] M. Demazure et A. Grothendieck (eds.), Seminaire de G ´ eom´ etrie ´ Algebrique du Bois Marie 1962/64–Sch ´ emas en groupes (SGA 3)–Vol.2. Lec- ´ ture Notes in Mathematics 152. New York: Springer-Verlag, 1970.   
[5] H. Shimizu, On discontinuous groups operating on the product of the upper half planes, Ann. of Math. 77 (2) (1963), 33–71.

# II

Polyhedral reduction theory in self-adjoint cones

Minkowski was the first to demonstrate the existence of a polyhedral fundamental domain for the action of $\operatorname { G L } ( n , \mathbb { Z } )$ on the self-adjoint cone of all positive-definite quadratic forms in $n$ variables with real coefficients. His work was generalized by Weyl and others to many other cases. Recently, A. Borel has produced a theory of coarse fundamental domains (called Siegel sets) for any arithmetic subgroup $\Gamma$ of a reductive algebraic group with $\mathbb { Q }$ -structure. Using this we have gone back to exact polyhedral fundamental domains, showing their existence in a unified approach for any arithmetic subgroup acting on a self-adjoint homogeneous cone, $C$ . More precisely, a set of closed polyhedral cones $\{ \sigma _ { \alpha } \}$ , such that $\sigma _ { \alpha } \subset \overline { { C } }$ and $\sigma _ { \alpha }$ is spanned by a set of rational vertices for every $\alpha$ , is called a $\Gamma$ -admissible polyhedral decomposition of $C$ when the following hold:

(1) a face of a $\sigma _ { \alpha }$ is a $\sigma _ { \beta }$ ;   
(2) $\sigma _ { \alpha } \cap \sigma _ { \beta }$ is a common face of $\sigma _ { \alpha }$ and $\sigma _ { \beta }$ ;   
(3) $\gamma \sigma _ { \alpha }$ is a $\sigma _ { \beta }$ , for all $\gamma \in \Gamma$ ;   
(4) modulo $\Gamma$ , there are only a finite number of $\sigma _ { \alpha }$ ;   
(5) $\textstyle C = \bigcup _ { \alpha } ( \sigma _ { \alpha } \cap C )$

The result that such decompositions exist is proven at the end of Section 4.

Section 1 and part of Section 2 follows closely some notes of Deligne (unpublished). The first two sections describe the work of Vinberg and Koecher on self-adjoint homogeneous cones and their connection with Jordan algebras. In Section 1 the cones appear by themselves, while in Section 2, after some background on Jordan algebras, the link between cone and algebra is explained in detail. Several small facts for later use also find proof in Section 2.

Section 3 analyzes the structure of the cone, especially with respect to the way its boundary breaks up into the disjoint union of lower-dimensional selfadjoint homogeneous cones, called boundary components. The Peirce decomposition is the main tool used here. We derive a correspondence between maximal split tori in the automorphism group of the cone and maximal strictly commutative rational subalgebras of the Jordan algebra. An easy computation then yields an explicit description of the rational root-space structure of the group of automorphisms.

We use the results of Section 3 to prove in Section 4 the main reduction theorem, roughly that Siegel sets and rational polyhedral cones are “cofinal” with respect to inclusion. In Section 5 we define “cores” and “co-cores” with two purposes: (1) the theorem near the beginning will be used later in comparing the topologies of various compactifications of the locally symmetric varieties $D / \Gamma$ ; and (2) the construction of explicit polyhedral fundamental domains in the spirit of Voronoi. If $L$ is a lattice in $V$ giving the $\mathbb { Q }$ -structure on $V$ , then a typical core is the closed convex hull of $C \cap L$ . A typical co-core is the closed convex hull of $( \overline { { C } } \cap L ) \setminus \{ 0 \}$ . By taking the cones over the faces of a co-core, one obtains a $\Gamma$ -admissible polyhedral decomposition of the cone. Everything in this section uses the existence of some polyhedral fundamental domain, proved in Section 4.

# 1 Homogeneous self-adjoint cones

# 1.1

Let $V$ be a finite-dimensional real vector space. We call $C \subset V \backslash \{ 0 \}$ a cone if $C$ is open and if $\mathbb { R } _ { > 0 } C = C$ . We say that $C$ is non-degenerate if $\overline { { C } }$ does not contain an entire straight line. Another expression for this property is given as follows. Let $\overline { { C } } ^ { * } \subset V ^ { * }$ be the set of linear forms, $\geq 0$ on $C$ . The dual cone $C ^ { * }$ is the interior of $\overline { { C } } ^ { * } \backslash \{ 0 \}$ . Then a convex cone $C$ is non-degenerate if and only if $C ^ { * } \neq \varnothing$ . One always has $C \subset C ^ { * * }$ with equality if and only if $C$ is convex non-degenerate (or $C = V \backslash \{ 0 \}$ ). We say that $C$ is self-dual (or self-adjoint) if there exists a positive-definite form on $V$ such that the resulting isomorphism between $V$ and $V ^ { * }$ transforms $C$ into $C ^ { * }$ .

#

Let $C \subset V$ be a convex non-degenerate cone, with $C ^ { * } \subset V ^ { * }$ its dual. Let $G =$ $\operatorname { A u t } ( C , V )$ be the group of linear transformations of $V$ which preserve $C$ . We are going to define the characteristic function of $C$ . Fix dual Haar measures dx, $\operatorname { d } \boldsymbol { x } ^ { * }$ on $V$ and $V ^ { * }$ .

Proposition 1.1 The expression

$$
\varphi ( x ) = \int _ { C ^ { * } } \mathrm { e } ^ { - \langle x , x ^ { * } \rangle } \mathrm { d } x ^ { * }
$$

defines a real-valued function on $C$ .

Proof Fix a point $x \in C$ . The following condition defines a Haar measure+ + $\mathrm { d } x _ { 1 } ^ { * }$ on the hyperplane $H _ { \alpha } = \{ x ^ { * } \mid \langle x , x ^ { * } \rangle = \alpha \} \subset V ^ { * }$ : For any continuous function $f$ of compact support on $V ^ { * }$ we have

$$
\int f ( x ^ { * } ) \mathrm { d } x ^ { * } = \int _ { - \infty } ^ { \infty } \mathrm { d } \alpha \int f ( x _ { 1 } ^ { * } ) \mathrm { d } x _ { 1 } ^ { * } .
$$

We can thus write

$$
\varphi ( x ) = \int _ { 0 } ^ { \infty } \mathrm { e } ^ { - \alpha } \mathrm { d } \alpha \int _ { H \alpha \cap C ^ { * } } \mathrm { d } x _ { 1 } ^ { * } .
$$

But, as is easily seen, + $H _ { \alpha } \cap \overline { { C ^ { * } } }$ is compact; thus the volume $\nu ( \alpha )$ of $H _ { \alpha } \cap C ^ { * }$ is finite. Since $H _ { \alpha }$ is obtained from $H _ { 1 }$ by a homothety with coefficient $\alpha$ ,

$$
\nu ( \alpha ) = \alpha ^ { n - 1 } \nu ( 1 ) \ .
$$

So $\varphi ( x ) = \nu ( 1 ) \int _ { 0 } ^ { \infty } \mathrm { e } ^ { - \alpha } \alpha ^ { n - 1 } \mathrm { d } \alpha < \infty .$

Remark 1.2 The quantity $\varphi ( x )$ is canonical up to multiplication by a constant (depending on the choice of the Haar measures).

Lemma 1.3 We have $\begin{array} { r } { \varphi ( g x ) = \frac { 1 } { \operatorname* { d e t } ( g ) } \varphi ( x ) } \end{array}$ . In particular, the measure

$$
\mu = \varphi ( x ) { \mathrm { d } } x
$$

on $C$ is $G$ -invariant.

Proof Indeed,

$$
\varphi ( g x ) = \int _ { C ^ { * } } \mathrm { e } ^ { - \langle g x , x ^ { * } \rangle } \mathrm { d } x ^ { * } = \int _ { C ^ { * } } \mathrm { e } ^ { - \langle x , ^ { t } g x ^ { * } \rangle } \mathrm { d } x ^ { * } \ .
$$

Now make a change of variables.

In particular, for $\lambda \in \mathbb { R } _ { > 0 }$ , we have

$$
\varphi ( \lambda x ) = \frac { 1 } { \lambda ^ { n } } \varphi ( x ) ,
$$

where $n = \dim V$ .

Recall that a continuous function $f$ on a convex subset $M$ of affine space is (strictly) convex if, for all $x _ { 1 } , x _ { 2 } \in M$ , for any point $x$ on the interval joining $x _ { 1 }$ and $x _ { 2 }$ and dividing it into the ratio $p : q$ (where $p , q > 0$ and $p + q = 1 { \bmod { \frac { \cdot } { 2 } } }$ ), we have $f ( x ) < p f ( x _ { 1 } ) + q f ( x _ { 2 } )$ . If $M$ is open and $f \in C ^ { 2 }$ , a sufficient condition for $f$ to be convex is that the quadratic form $\mathrm { d } ^ { 2 } f$ be positive-definite at all points of $M$ .

# Proposition 1.4

(i) $\log \varphi$ is convex;   
(ii) $\varphi$ is convex.

Proof We have

$$
\mathrm { d } \log \varphi = \frac { \mathrm { d } \varphi } { \varphi } , \quad \mathrm { d } ^ { 2 } \log \varphi = \frac { \mathrm { d } ^ { 2 } \varphi } { \varphi } - \left( \frac { \mathrm { d } \varphi } { \varphi } \right) ^ { 2 } .
$$

From this it follows that it suffices to show that $\mathrm { d } ^ { 2 } \log \varphi$ is positive-definite. To prove this, we calculate, for $x \in C$ and $a \in V = T _ { x } ( C )$ :

$$
( \mathrm { d } \varphi ( x ) ) ( a ) = - \int _ { C ^ { * } } \mathrm { e } ^ { - \langle x , x ^ { * } \rangle } \langle a , x ^ { * } \rangle \ : \mathrm { d } x ^ { * }
$$

$$
( \mathrm { d } ^ { 2 } \varphi ( x ) ) ( a ) = \int _ { C ^ { * } } \mathrm { e } ^ { - \langle x , x ^ { * } \rangle } { \langle a , x ^ { * } \rangle } ^ { 2 } \mathrm { d } x ^ { * } .
$$

Put $F ( x ^ { * } ) = \mathbf { e } ^ { - { \frac { 1 } { 2 } } \left. x , x ^ { * } \right. }$ , $G ( x ^ { * } ) = \mathrm { e } ^ { - \frac { 1 } { 2 } \langle x , x ^ { * } \rangle } \langle a , x ^ { * } \rangle$ . Then, for $a \neq 0$

$$
( \mathrm { d } ^ { 2 } \log { \varphi ( x ) } ) ( a ) = \frac { 1 } { ( \varphi ( x ) ) ^ { 2 } } \left[ \int { { { \cal C } ^ { * } } } { { \mathrm { d } } x ^ { * } } \int { { { \cal G } ^ { 2 } } } \mathrm { d } x ^ { * } - \left( \int _ { { { \cal C } ^ { * } } } F G \mathrm { d } x ^ { * } \right) ^ { 2 } \right] > 0 ,
$$

because $F$ and $G$ are not proportional functions.

As a consequence of this proposition we have that

$$
g = { \frac { \mathrm { d } ^ { 2 } \log \varphi ( x ) } { \mathrm { d } ^ { 2 } x } } \mathrm { d } x ^ { 2 }
$$

defines a $G$ -invariant Riemannian metric on $C$ .

Example 1.5 Let $V = \mathbb { R }$ , $C = \mathbb { R } _ { > 0 } \subset \mathbb { R }$ . Then $\textstyle \varphi ( x ) = { \frac { 1 } { x } }$ and the Riemannian metric $g$ on $\mathbb { R } _ { > 0 }$ is $\begin{array} { r } { g = \frac { \mathrm { d } x ^ { 2 } } { x ^ { 2 } } } \end{array}$

Proposition $\mathbf { 1 . 6 } \varphi$ goes to infinity upon approach of a point of the boundary of $C$ .

Proof Indeed, if $x _ { k }$ , $k = 1 , 2 , \dots$ , converges to $x _ { 0 } \in \partial C$ , then $f _ { k } ( x ^ { \prime } ) = \mathbf { e } ^ { - \langle x _ { k } , x ^ { \prime } \rangle }$ converges to $f _ { 0 } ( x ^ { \prime } ) = \mathbf { e } ^ { - \langle x _ { 0 } , x ^ { \prime } \rangle }$ uniformly on any bounded set in $V ^ { * }$ . So, it

suffices to show that

$$
\underbrace { \int f _ { 0 } ( x ^ { * } ) \mathrm { d } x } _ { C ^ { * } } .
$$

is a divergent integral.

Let $x _ { 0 } ^ { * } \in \overline { { C ^ { * } } }$ with $x _ { 0 } ^ { * } \neq 0$ , $\left. x _ { 0 } , x _ { 0 } ^ { * } \right. = 0$ . Take a small ball $K$ lying entirely in $C ^ { * }$ and consider the set $L = K + \mathbb { R } _ { \geq 0 } x _ { 0 } ^ { * } \subset C ^ { * }$ . Let $c = \operatorname* { m i n } _ { x ^ { * } \in K } f _ { 0 } ( x ^ { * } )$ . Then $c > 0$ and $c = \operatorname* { m i n } _ { x ^ { * } \in L } f _ { 0 } ( x ^ { * } )$ . So we have

$$
\begin{array} { l } { { \displaystyle \int _ { C ^ { * } } f _ { 0 } ( x ^ { * } ) \mathrm { d } x ^ { * } \geq \int _ { L } f _ { 0 } ( x ^ { * } ) \mathrm { d } x ^ { * } \geq c \int _ { L } \mathrm { d } x ^ { * } . } } \end{array}
$$

The final expression is indeed infinite since $L$ has infinite volume.

# 1.3

Proposition 1.7 Let $C$ be a convex non-degenerate cone in $V$ and let $G =$ $\operatorname { A u t } ( C , V )$ . Then $G$ is a Lie group, the stabilizer of $e \in C$ in $G$ is compact and maximally compact if $C$ is homogeneous.

Proof The first two assertions follow from the existence of the $G$ -invariant Riemannian metric $g$ on $C$ . The final one follows from the fact that any compact subgroup of $G$ has a fixed point in $C$ , as one proves by the usual averaging method. □

Proposition 1.8 Let $C \subset V$ be an open set in $V$ , such that $C ^ { * } \neq \varnothing$ . Let $G \subseteq$ Aut $( C , V )$ . If there is $e \in C$ such that $G \cdot e$ is open in $V$ , then $G \cdot e = C$ and $C$ is a convex homogeneous cone under $G$ .

Corollary 1.9 Let $C \subset V$ be a convex homogeneous cone under $G .$ . Then $C ^ { * } \subset$ $V ^ { * }$ is a convex homogeneous cone under the dual group $G ^ { * }$ .

Proof (of Proposition 1.8) First, $G \cdot e \subset C \subset C ^ { * * }$ , and $C ^ { * * }$ still satisfies the hypotheses of the proposition. So we can suppose that $C$ is non-degenerate convex. Let $r > 0$ such that the ball with radius $r$ around $e$ (with respect to the Riemannian metric $g$ ) is contained in $G \cdot e$ . For every sequence of points $x _ { i }$ such that $d ( x _ { i - 1 } , x _ { i } ) < r$ and $x _ { 0 } = e$ we get $x _ { n } \in G \cdot e$ (because $g$ is $G$ -invariant). Since $C$ is connected, $C = G \cdot e$ . □

Proposition 1.10 Let $\mathcal { G }$ be a reductive connected algebraic group and let $( V , \rho )$ be a representation of $\mathcal { G }$ all defined over $\mathbb { R }$ . Let $e \in V$ and $G = \mathcal { G } ( \mathbb { R } ) ^ { o }$ .

Suppose that the stabilizer in $G$ of e is maximal compact and that $G \cdot e$ is open. Then $G \cdot e$ is a homogeneous self-adjoint cone. Conversely, the automorphism group of a self-adjoint cone is reductive.

Proof Let $K$ be the stabilizer of $e$ . Let $\sigma$ be the Cartan involution and let $B$ be a positive-definite symmetric bilinear form on $V$ such that $\rho ( \sigma ( g ) ) = { } ^ { t } \rho ( g ) ^ { - 1 }$

The corresponding Cartan decompositions are given by

$$
\operatorname { L i e } \left( G \right) = \ell \oplus \mathfrak { p } , G = K \cdot \exp ( \mathfrak { p } ) = K \cdot P .
$$

Let $g _ { 1 } , g _ { 2 } \in G$ and let $\sigma ( g _ { 2 } ) ^ { - 1 } g _ { 1 } = p ^ { 2 } k$ , with $k \in K , p \in P .$ Then

$$
\langle g _ { 1 } e , g _ { 2 } e \rangle = \langle \sigma ( g _ { 2 } ) ^ { - 1 } g _ { 1 } e , e \rangle = \langle p ^ { 2 } e , e \rangle = \langle p e , p e \rangle > 0 .
$$

Thus, identifying $V$ with $V ^ { * }$ by $B$ , we have

$$
G \cdot e \subset ( G \cdot e ) ^ { * } .
$$

But $( G \cdot e ) ^ { * }$ is stable under $G$ : for $x \in ( G \cdot e ) ^ { * }$ , $h \in G$ , and $g \in G$ ,

$$
\langle g e , h x \rangle = \langle \sigma ( h ) g e , x \rangle > 0 \ .
$$

Then Proposition 1.8 applied to $( G \cdot e ) ^ { * }$ shows that $\boldsymbol { G } \cdot \boldsymbol { e } = ( \boldsymbol { G } \cdot \boldsymbol { e } ) ^ { * }$ . Conversely, if $C$ is self-adjoint, then Au ${ \mathfrak { u } } ( C , V )$ is stable under $g \longmapsto ^ { t } g$ (transpose with respect to the positive-definite metric on $V$ making $C$ self-adjoint), and consequently $G$ is reductive. □

Remark 1.11 It may appear at present that the concept of a self-adjoint homogeneous cone is very wide. This is not so. Any convex cone $C$ splits in a unique way into the direct sum of indecomposable convex cones $C _ { i }$ . Then $C$ is homogeneous (respectively self-adjoint) if and only if all the $C _ { i }$ are.

Now the indecomposable self-adjoint homogeneous cones have been completely classified. They are:

(1) the cone of positive-definite symmetric matrices; (2) the cone of positive-definite hermitian complex matrices;2 (3) the cone of positive-definite hermitian quaternion matrices; (4) the spherical cone in $\mathbb { R } ^ { n + 1 }$ of $\left( x _ { 0 } , \ldots , x _ { n } \right)$ with

$$
x _ { 0 } > \sqrt { x _ { 1 } ^ { 2 } + . . . + x _ { n } ^ { 2 } } ;
$$

(5) the 27-dimensional cone of positive-definite hermitian octavic matrices of third order.

Here (1)–(3) are classical, (4) is semi-classical, and (5) is exceptional.

# 2 Jordan algebras

Jordan algebras arose in quantum mechanics from the desire to make operators commute, at the expense of their associativity. Their usefulness for our purposes comes from the one-to-one correspondence between self-adjoint homogeneous cones and formally real Jordan algebras. For comprehensive references, see [5], [7], [8], and [13].

Definition 2.1 A Jordan algebra $A$ over a field $k$ (of char $k \neq 2$ ) is a finitedimensional (non-associative) algebra with unit element $p$ such that, for all $a , b \in A$

(i) $a \cdot b = b \cdot a$ ;   
(ii) $a ^ { 2 } \cdot ( b \cdot a ) = ( a ^ { 2 } \cdot b ) \cdot a$ , where $a ^ { 2 } = a \cdot a$ .

Although not strictly necessary, we will assume for convenience that char $k \neq$ 2, 3. In fact, we will only need the case char $k = 0$ in applications.

Start with a Jordan algebra $A$ over $k$ . For $a \in A$ , we denote by $L _ { a }$ multiplication by $a$ :

$$
L _ { a } ( x ) = x \cdot a .
$$

Set

$$
S ( a , b , c , d ) = ( a \cdot b ) \cdot ( c \cdot d ) + ( a \cdot c ) \cdot ( b \cdot d ) + ( a \cdot d ) \cdot ( b \cdot c ) \ .
$$

By (i) this is symmetric in $a , b , c , d$ . Set

$$
T ( a ; b , c , d ) = ( a \cdot ( b \cdot c ) ) \cdot d + ( a \cdot ( c \cdot d ) ) \cdot b + ( a \cdot ( d \cdot b ) ) \cdot c .
$$

Again using (i), one sees that $T$ is symmetric in $b , c , d$ . Then

$$
S ( a , b , c , d ) = T ( a ; b , c , d ) .
$$

Indeed, for $b = c = d$ this identity reduces to (ii); the general case follows from this by polarization, since 6 is invertible in $k$ . In particular, $T$ is symmetric. This can be expressed as

$$
T ( a ; b , c , d ) = T ( b ; a , c , d ) ,
$$

which can be reformulated by saying that $D _ { a , b } = [ L _ { a } , L _ { b } ]$ is a derivation, i.e.,

$$
D _ { a , b } ( c \cdot d ) = c \cdot D _ { a , b } ( d ) + d \cdot D _ { a , b } ( c ) .
$$

Theorem 2.2 (Vinberg) Let A be an algebra with unit over a field $k$ of characteristic $\neq 2 , 3$ . Let $t : A \longrightarrow k$ be a linear form, the “trace”, such that

(a) $A$ is commutative and $D _ { a , b }$ is a derivation;   
(b) $t ( [ L _ { a } , L _ { b } ] ( c ) ) = 0$ ;

(c) $t ( a \cdot b )$ is a non-degenerate bilinear form.

Then A is a Jordan algebra.

Proof It suffices to prove $S = T$ . Set

$$
\{ a , b , c , d ; e \} = t ( ( S ( a , b , c , d ) - T ( a ; b , c , d ) ) \cdot e ) .
$$

We have just seen that assumption (a) is equivalent to $T$ being symmetric.   
Hence $\{ a , b , c , d ; e \}$ is symmetric in $_ { a , b , c , d }$ .

Observe that

$$
S ( a , b , c , d ) - T ( a ; b , c , d ) = ( D _ { a , b \cdot c } + D _ { b , c \cdot a } + D _ { c , a \cdot b } ) ( d ) .
$$

It follows with (a) and (b) that $\{ a , b , c , d ; e \}$ is anti-symmetric in $d$ and $e$ : indeed,

$$
\{ a , b , c , d ; e \} + \{ a , b , c , e ; d \} = t ( ( D _ { a , b \cdot c } + D _ { b , c \cdot a } + D _ { c , a \cdot b } ) ( d \cdot e ) ) = 0 .
$$

But this implies that the expression $\{ \}$ is identically 0: indeed, $\{ a , b , c , d ; e \} =$ $- \{ a , b , c , e ; d \}$ ; but, whereas the L.H.S. is symmetric in $c$ and $d$ , the R.H.S. is anti-symmetric in $c$ and $d$ .

Since the element $e$ is arbitrary, assumption (c) now implies the assertion.

Definition 2.3 If $A$ is a Jordan algebra, $x , y \in A$ , then $x$ and $y$ are said to commute strictly (or strongly) if $L _ { x }$ and $L _ { y }$ commute. A subalgebra $B \subset A$ is strongly associative if any two elements $x , y \in B$ strongly commute. (This makes sense because it implies that, for all $x , y , z \in B$ ,

$$
x ( z y ) = L _ { x } L _ { y } ( z ) = L _ { y } L _ { x } ( z ) = ( x z ) y ~ . )
$$

Proposition 2.4 For all $x \in A$ , define $x ^ { n }$ inductively by $x ^ { n } = x \cdot x ^ { n - 1 }$ . Then:

(a) $x ^ { i } , x ^ { j }$ strongly commute for all $i , j \geq 0$ ;   
(b) $x ^ { i } \cdot x ^ { j } = x ^ { i + j }$ ;   
(c) $p , x , x ^ { 2 } , \ldots$ span a strongly associative subalgebra $k [ x ] \subset A$ .

Proof Interpret $S = T$ by taking $d$ as a variable. It then says:

$$
L _ { a ( b c ) } = L _ { a b } \cdot L _ { c } + L _ { a c } \cdot L _ { b } + L _ { b c } \cdot L _ { a } - L _ { b } \cdot L _ { a } \cdot L _ { c } - L _ { c } \cdot L _ { a } \cdot L _ { b } \ .
$$

In particular, if $a = b = x$ , $c = x ^ { k }$ , this says:

$$
L _ { x ^ { k + 2 } } = 2 L _ { x ^ { k + 1 } } \cdot L _ { x } + L _ { x ^ { 2 } } \cdot L _ { x ^ { k } } - L _ { x ^ { k } } \cdot L _ { x } ^ { 2 } - L _ { x } ^ { 2 } \cdot L _ { x ^ { k } } \ ,
$$

hence all $L _ { x ^ { k } }$ belong to the subalgebra of ${ \mathrm { H o m } } _ { k } ( A , A )$ generated by $L _ { x } , L _ { x ^ { 2 } }$ . But condition (ii) in the definition of a Jordan algebra says that $L _ { x } , L _ { x ^ { 2 } }$ commute. So all $L _ { x ^ { k } }$ commute. Finally

$$
x ^ { i } \cdot x ^ { j } = L _ { x ^ { i } } ( L _ { x ^ { j - 1 } } ( x ) ) = L _ { x ^ { j - 1 } } ( L _ { x ^ { i } } ( x ) ) = x ^ { j - 1 } \cdot x ^ { i + 1 } \ ,
$$

which, by a simple induction, proves (b), and then (c) is obvious.

A useful identity is:

Lemma 2.5 For all $x , y \in A$ , $x$ and $y ^ { 2 }$ strictly commute if and only if $x \cdot y$ and $y$ strictly commute.

Proof In the equation $S = T$ , take $b = c = y$ , $a = x$ to find $2 [ L _ { x \cdot y } , L _ { y } ] = [ L _ { x } , L _ { y ^ { 2 } } ]$ .

Definition 2.6 For any $x \in A$ , we say that $y \in A$ is the inverse of $x$ if $x$ and $y$ strictly commute and $x \cdot y = p$ .

Note that an inverse is unique: if $y _ { 1 } , y _ { 2 }$ were inverses

$$
{ \begin{array} { r l } & { y _ { 1 } = y _ { 1 } \cdot \left( x \cdot y _ { 2 } \right) } \\ & { \quad = x \cdot \left( y _ { 1 } \cdot y _ { 2 } \right) ( x , y _ { 1 } { \mathrm { ~ s t r o n g l y ~ c o m m u t e } } ) } \\ & { \quad = y _ { 2 } \cdot \left( x \cdot y _ { 1 } \right) ( x , y _ { 2 } { \mathrm { ~ s t r o n g l y ~ c o m m u t e } } ) } \\ & { \quad = y _ { 2 } ~ . } \end{array} }
$$

Lemma 2.7 If $x$ has an inverse $x ^ { - 1 }$ , then $x ^ { - 1 } \in k [ x ]$ .

Proof In fact by Lemma 2.5, $x ^ { - 1 }$ and $x ^ { 2 }$ strictly commute. Since $L _ { x } ^ { k }$ , for $k \geq 3$ , are polynomials in $L _ { x }$ and $L _ { x } ^ { 2 }$ , in fact $x ^ { - 1 }$ and $x ^ { k }$ strictly commute for all $k \geq 1$ . Then if $x$ were a zero divisor in $k [ x ]$ , i.e., $x \cdot f ( x ) = 0$ , for $f ( x ) \neq 0$ , one would get

$$
0 = x ^ { - 1 } \cdot ( x \cdot f ( x ) ) = f ( x ) \cdot ( x \cdot x ^ { - 1 } ) = f ( x ) \ ,
$$

which is a contradiction. But $k [ x ]$ is finite-dimensional, so every non-zero divisor has an inverse in $k [ x ]$ .

Corollary 2.8 If $x$ has an inverse, then $x ^ { 2 }$ has an inverse, and $( x ^ { 2 } ) ^ { - 1 } = ( x ^ { - 1 } ) ^ { 2 }$ .

We now take up the Peirce decomposition of a Jordan algebra with respect to an idempotent $\varepsilon \in A$ . By the recursion formula $( 2 . 3 ) , L _ { \varepsilon }$ satisfies the identity $\varphi ( L _ { \varepsilon } ) = 0$ , where

$$
\varphi ( T ) = 2 T ^ { 3 } - 3 T ^ { 2 } + T \ .
$$

Define

$$
\begin{array} { r c l } { { } } & { { } } & { { \varphi _ { 0 } ( T ) = 2 T ^ { 2 } - 3 T + 1 , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \varphi _ { \frac { 1 } { 2 } } ( T ) = - 4 T ^ { 2 } + 4 T , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \varphi _ { 1 } ( T ) = 2 T ^ { 2 } - T . } } \end{array}
$$

Then $\varphi _ { 0 } + \varphi _ { \frac { 1 } { 2 } } + \varphi _ { 1 } = 1$ , and $\varphi$ divides $( T - \lambda ) \varphi _ { \lambda } ( T )$ for $\lambda = 0$ , $\frac { 1 } { 2 }$ , 1. If $x \in A$ , we get $x = x _ { 0 } + x _ { \frac { 1 } { 2 } } + x _ { 1 }$ with $x _ { \lambda } = \varphi _ { \lambda } ( L _ { \varepsilon } ) x .$ , and $\varepsilon \cdot x _ { \lambda } = \lambda x _ { \lambda }$ .

Writing $A _ { \lambda } = \varphi _ { \lambda } ( L _ { \varepsilon } ) A$ , we have

$$
A = A _ { 0 } \oplus A _ { \frac { 1 } { 2 } } \oplus A _ { 1 }
$$

and $A _ { \lambda }$ is the $\lambda$ -eigenspace for $L _ { \varepsilon }$ . We write $A _ { \lambda } ( \varepsilon )$ for $A _ { \lambda }$ , if necessary to avoid confusion. This is called the Peirce decomposition of $A$ . Note that Lemma 2.5 with $x \in A _ { 0 }$ , $y = \varepsilon$ , implies that $\varepsilon$ and $A _ { 0 }$ strongly commute; hence $L _ { x }$ , for all $x \in A _ { 0 }$ , preserves the eigenspaces of $\varepsilon$ . Similarly, Lemma 2.5 with $x \in A _ { 1 }$ , $y = p - \varepsilon$ , implies that $\varepsilon$ and $A _ { 1 }$ strongly commute; hence $L _ { x }$ , for all $x \in A _ { 1 }$ , preserves the eigenspaces of $\varepsilon$ .

In particular, if $x \in A _ { 0 }$ , $y \in A _ { 1 }$ , then $x \cdot y \in A _ { 0 } \cap A _ { 1 } = ( 0 )$ . In fact, recall that $S = T$ and hence, by (2.1),

$$
D _ { a , b \cdot c } + D _ { b , c \cdot a } + D _ { c , a \cdot b } = 0 .
$$

Take $a = x$ , $b = y$ , $c = \varepsilon$ to see that $x$ and $y$ strongly commute. If one takes $a = \varepsilon$ and $b , c \in A _ { \frac { 1 } { 2 } }$ , and evaluates at $d = \varepsilon$ , we see that $\pmb { \varepsilon } \cdot ( \pmb { \varepsilon } \cdot ( b \cdot c ) ) = \pmb { \varepsilon } \cdot ( b \cdot c )$ , i.e., $\varphi _ { \frac { 1 } { 2 } } ( L _ { \varepsilon } ) ( b \cdot c ) = 0$ . Thus $b \cdot c \in A _ { 0 } + A _ { 1 }$ . We summarize this in the following multiplication table:

![](images/f038ad7b6b85653e3ec2ea96561a1a1f6715fbc05070fa3b4e06740e76fca094.jpg)

Here if $x \in A _ { \mu }$ , $y \in A _ { \lambda }$ , then $x \cdot y \in A _ { \nu }$ , where $\nu$ is graphed as a function of $\mu , \lambda$ in the multiplication table above.

Corollary 2.9 With respect to the inner product $\langle x , y \rangle = \operatorname { T r } \left( L _ { x \cdot y } \right)$ , the spaces $A _ { 0 } , A _ { 1 / 2 }$ , and $A _ { 1 }$ are perpendicular.

We call a set of idempotents $\varepsilon _ { 1 } , \ldots , \varepsilon _ { n }$ mutually orthogonal if $\pmb { \varepsilon } _ { i } \cdot \pmb { \varepsilon } _ { j } = \delta _ { i j } \cdot \pmb { \varepsilon } _ { i }$ , for $1 \leq i , j \leq n$ . By Lemma 2.5 with $x = \varepsilon _ { i }$ , $y = \varepsilon _ { j }$ , the $\varepsilon _ { i }$ all strictly commute, and generate a strongly associative subalgebra $\textstyle W = \bigoplus _ { i = 1 } ^ { n } k \varepsilon _ { i }$ .

We say $\{ \varepsilon _ { 1 } , \ldots , \varepsilon _ { n } \}$ is a complete set of mutually orthogonal idempotents if $\pmb { \varepsilon } _ { 1 } + \cdots + \pmb { \varepsilon } _ { n } = p$ . In this case, we can have a Peirce decomposition for al the $\varepsilon _ { i }$ at once because the $L _ { \varepsilon _ { i } }$ commute with each other. We write $A = \oplus A _ { \nu }$ , where the $A _ { \nu }$ are simultaneous eigenspaces for $L _ { \varepsilon _ { 1 } } , \ldots , L _ { \varepsilon _ { n } }$ . Because $L _ { \varepsilon _ { 1 } } + \cdots + L _ { \varepsilon _ { n } } =$ id, and the various eigenvalues are all 0, $\frac { 1 } { 2 }$ , or 1, we end up with $A = \oplus _ { i \leq j } , A _ { i j }$ where, if $x \in A _ { i j }$ ,

$$
\begin{array} { r } { \pmb { \varepsilon } _ { k } \cdot \pmb { x } = \frac { 1 } { 2 } ( \delta _ { k i } + \delta _ { k j } ) \pmb { x } . } \end{array}
$$

Also, if $x \in A _ { i j }$ , $y \in A _ { k \ell }$ , and $( i , j ) \neq ( k , \ell )$ , then $\mathrm { T r } \left( { \cal L } _ { x \cdot y } \right) = 0$ .

We get the finest decomposition from a maximal set of mutually orthogonal idempotents, that is $\{ \varepsilon _ { 1 } , \cdots , \varepsilon _ { n } \}$ such that the $n$ is maximal for sets of orthogonal idempotents. Note that a maximal set is complete: if $f = \pmb { \varepsilon } _ { 1 } + \cdots + \pmb { \varepsilon } _ { n } \neq p$ , then $\{ \varepsilon _ { 1 } , \ldots , \varepsilon _ { n } , p - f \}$ is a larger set of mutually orthogonal idempotents.

Definition 2.10 If $k = \mathbb { R }$ , then a Jordan algebra $A$ is said to be formally real if

$$
x ^ { 2 } + y ^ { 2 } = 0 \Longrightarrow x = y = 0 .
$$

If $B$ is a subalgebra of $A$ , it too is formally real. An associative Jordan algebra is formally real if and only if it is isomorphic to a product of copies of $\mathbb { R }$ with componentwise multiplication.

Definition 2.11 A positive-definite trace form $t : A \longrightarrow \mathbb { R }$ on a real Jordan algebra is a linear map such that $t ( x ^ { 2 } ) > 0$ for all $x \in A$ , $x \neq 0$ .

Proposition 2.12 Let A be a real Jordan algebra. The following are equivalent:

(a) A is formally real;   
(b) A has a positive-definite trace form $t$ ;   
(c) $t ( x ) = \mathrm { T r } \left( L _ { x } \right)$ is a positive-definite trace form (hence $\langle x , y \rangle = t ( x \cdot y )$ is $a$ positive-definite inner product).

Proof That $\left( \mathrm { c } \right) \Longrightarrow \left( \mathrm { b } \right) \Longrightarrow$ (a) is clear. Assume (a). Then, for all $x \in A$ , $\mathbb { R } [ x ] \cong$ $\oplus _ { i = 1 } ^ { N } \mathbb { R } \varepsilon _ { i }$ , where $\varepsilon _ { i }$ are idempotents. If $x = \Sigma \lambda _ { i } \varepsilon _ { i }$ , it follows that $\boldsymbol { x } ^ { 2 } = \Sigma \lambda _ { i } ^ { 2 } \varepsilon _ { i }$ , hence

$$
\mathrm { T r } \left( { \cal L } _ { x ^ { 2 } } \right) = \sum \lambda _ { i } ^ { 2 } \mathrm { T r } { \cal L } _ { \varepsilon _ { i } } ,
$$

and, by the Peirce decomposition, $\mathrm { T r } L _ { \varepsilon _ { i } } > 0$

The formally real Jordan algebras were classified in 1934 by P. Jordan, Wigner, and von Neumann. This gives the classification of self-adjoint homogeneous cones in Section 1, in light of the following one-to-one correspondence between the two classes of objects. See [5], Ch. 11.

Let $C \subset V$ be a homogeneous self-adjoint cone and let  $e \in C$ , $G = \operatorname { A u t } \left( C , V \right)$ , ${ \mathfrak { g } } = \operatorname { L i e } \left( G \right)$ . Let $K \subset G$ be the stabilizer of $e$ in $G$ and $\mathfrak { k }$ its Lie algebra. Let $\sigma$ be the corresponding Cartan involution with ${ \mathfrak { g } } = { \mathfrak { k } } \oplus { \mathfrak { p } }$ being the Cartan decomposition, i.e.,

$$
\sigma = \left\{ \begin{array} { r l } { { 1 } } & { { \mathrm { o n } \mathfrak { k } , } } \\ { { - 1 } } & { { \mathrm { o n } \mathfrak { p } . } } \end{array} \right.
$$

Now $\mathfrak { g }$ acts on $V$ by taking the differential at 0 of the $G$ -action, $\mathfrak { k }$ is the stabilizer of $e$ , and the map

$$
\pi \longmapsto \pi \cdot e
$$

from $\mathfrak { p }$ into $V$ is bijective. We define an algebra structure on $\mathfrak { p }$ by setting

$$
( \pi \cdot \pi ^ { \prime } ) \cdot e = \pi \cdot ( \pi ^ { \prime } \cdot e ) \ .
$$

Let $p \in { \mathfrak { p } }$ be such that $p \cdot e = e$

One verifies that:

(1) $\pi \cdot \pi ^ { \prime } = \pi ^ { \prime } \cdot \pi { \mathrm { ~ ( i n d e e d ~ } } ( \pi \cdot \pi ^ { \prime } - \pi ^ { \prime } \cdot \pi ) \cdot e = [ \pi , \pi ^ { \prime } ] \cdot e = 0 { \mathrm { ~ } }$ since $[ { \pi } , { \pi } ^ { \prime } ] \in \mathfrak { k } )$ ;   
(2) clearly $p$ is a unit element;   
(3) $\left[ L _ { \pi } , L _ { \pi ^ { \prime } } \right] = \mathrm { a d } \left[ \pi , \pi ^ { \prime } \right]$ .

Furthermore, let $\langle \cdot , \cdot \rangle$ be a positive-definite form on $V$ “which makes $C$ selfadjoint” and such that $\sigma$ is the restriction to ${ \mathfrak { g } } \subset \operatorname { E n d } ( V )$ of $u \longmapsto - { } ^ { t } u$ (such forms exist, see Proposition 1.10 and its proof). Define the linear form $t$ on $\mathfrak { p }$ by

$$
t ( \pi ) = \langle \pi \cdot e , e \rangle ~ .
$$

Then

$$
\begin{array} { r l } & { t ( [ L _ { a } , L _ { b } ] ( c ) ) = \langle [ [ a , b ] , c ] \cdot e , e \rangle \ ( \mathrm { b y ~ ( 3 ) ~ a b o v e } ) } \\ & { \quad \quad = \langle [ a , b ] \cdot c \cdot e , e \rangle - \langle c \cdot [ a , b ] \cdot e , e \rangle } \\ & { \quad \quad = - \langle c \cdot e , [ a , b ] \cdot e \rangle - \langle c \cdot [ a , b ] \cdot e , e \rangle \ ( \mathrm { s i n c e ~ } [ a , b ] } \\ & { \quad \quad = 0 \ ( \mathrm { s i n c e ~ } \mathbb { t } \cdot e = 0 ) . } \end{array}
$$

Also, for $\pi \neq 0$ ,

$$
t ( \pi \cdot \pi ) = \langle \pi \cdot \pi \cdot e , e \rangle = \langle \pi \cdot e , \pi \cdot e \rangle > 0 .
$$

We thus see that $\left( \mathfrak { p } , \cdot , t \right)$ satisfies the hypotheses of Vinberg’s theorem (Theorem 2.2 above), which implies that $( { \mathfrak { p } } , \cdot )$ is a Jordan algebra $( A , \cdot )$ .

Going in the converse direction, the cone $C$ can be recaptured in the following way:

$$
C = \{ \exp ( \rho ( a ) ) \cdot e \mid a \in A \} \ ,
$$

where $\rho : A = { \mathfrak { p } } \longrightarrow \operatorname { E n d } \left( V \right)$ comes from the representation of $\mathfrak { g }$ on $V$ .

Identifying $A$ with $V$ , $\exp ( \rho ( a ) ) \cdot e = \exp _ { J } ( a )$ , where $\begin{array} { r } { \exp _ { J } ( a ) = 1 + a + \frac { a ^ { 2 } } { 2 } + } \end{array}$ $\dots$ is the Jordan algebra exponential which may be calculated in the algebra $\mathbb { R } [ a ]$ generated by $a$ in $A$ . Since $\mathbb { R } [ a ]$ is an associative formally real Jordan algebra, it is a product of copies of $\mathbb { R }$ . In particular, the exponentials in $A$ are also the squares of invertible elements. So, we can also describe the cone as the set of squares of invertible elements.

Finally, starting from a formally real Jordan algebra $A$ , define

$$
{ \mathfrak { g } } = \operatorname { D e r } A \oplus A
$$

(here Der A means derivations of $A$ for its Jordan multiplication). Now $\mathfrak { g }$ is a Lie algebra if we define

$$
\begin{array} { c } { { [ D _ { 1 } , D _ { 2 } ] = D _ { 1 } D _ { 2 } - D _ { 2 } D _ { 1 } \ , } } \\ { { { } } } \\ { { [ D , x ] = D ( x ) \ , } } \\ { { { } } } \\ { { [ x , y ] = L _ { x } L _ { y } - L _ { y } L _ { x } \ , } } \end{array}
$$

for $x , y \in A$ and $D , D _ { 1 } , D _ { 2 } \in \mathrm { D e r } A$ .

In fact, $\mathfrak { g }$ is a subspace of $\mathrm { H o m } _ { \mathbb { R } } ( A , A )$ if $^ { ( D , x ) }$ acts on $A$ by $y \longrightarrow D y + x \cdot y$ . One sees immediately that $[ \cdot , \cdot ]$ on $\mathfrak { g }$ is just the commutator in ${ \mathrm { H o m } } _ { \mathbb { R } } ( A , A )$ . Let $G \subset \operatorname { G L } ( A )$ be the corresponding Lie group, and let $K \subset G$ be the subgroup corresponding to DerA. Putting the inner product $\langle x , y \rangle = \operatorname { T r } \left( L _ { x \cdot y } \right)$ on $A$ , and defining $\sigma : { \mathfrak { g } } \longrightarrow { \mathfrak { g } }$ to be $+ 1$ on DerA, and $^ { - 1 }$ on $A$ , one sees:

(a) exponentiating a derivation leads to an automorphism, so $K$ acts on $A$ by Jordan automorphisms; in particular

$$
\langle k x , y \rangle = \langle x , k ^ { - 1 } y \rangle { \mathrm { ~ f o r ~ a l l ~ } } k \in K ,
$$

and hence

$$
\langle D x , y \rangle = - \langle x , D y \rangle { \mathrm { ~ f o r ~ a l l ~ } } D \in \operatorname { D e r } A { \mathrm { ~ ; } }
$$

(b) equation (2.2) may be written as

$$
L _ { a ( b \cdot c ) } - L _ { b ( a \cdot c ) } = [ L _ { a } L _ { b } , L _ { c } ] + [ L _ { c } , L _ { b } L _ { a } ] ,
$$

hence

$$
\mathrm { T r } L _ { a ( b \cdot c ) } = \mathrm { T r } L _ { b ( a \cdot c ) } ,
$$

and therefore

$$
\langle L _ { z } x , y \rangle = \langle x , L _ { z } y \rangle
$$

for all $z \in A$ .

Thus $\sigma g = - { ^ t g }$ , for all $g \in { \mathfrak { g } }$ ; it follows that $\mathfrak { g }$ is a reductive sub Lie algebra of ${ \mathrm { H o m } } \left( A , A \right)$ and $\sigma$ is a Cartan involution. Finally, since ${ \mathfrak { g } } \cdot p = A$ , the orbit $G \cdot p$ is open in $A$ ; Proposition 1.8 shows that $C = G \cdot p$ is a homogeneous self-adjoint cone and $G \subset \operatorname { A u t } ( C , V ) ^ { o }$ . Here, as above, $G \cdot p = ( \exp A \cdot K ) \cdot p =$ $\{ \exp _ { J } ( a ) \mid a \in A \}$ . Moreover, writing $G ^ { \prime } = \operatorname { A u t } ( C , V ) ^ { o }$ , we see Lie $G ^ { \prime } = { \mathfrak { k } } + { \mathfrak { p } }$ as usual. We have three Lie algebras:

$$
( { \mathrm { I n n e r ~ D e r } } A ) + A \subset { \mathrm { D e r } } A + A \subset { \mathfrak { k } } + { \mathfrak { p } }
$$

(where inner derivations are the derivations $[ L _ { x } , L _ { y } ]$ , for $x , y \in A$ ). Since $\pi \longmapsto$ $\pi \cdot p$ defines ${ \mathfrak { p } } \longrightarrow A$ , and since, for any real reductive Lie group $G$ without compact factors, $\mathfrak { k } = [ \mathfrak { p } , \mathfrak { p } ]$ , it follows that all three are equal! This proves:

Theorem 2.13 Given a real vector space $V$ and a point $p \in V$ , there is $a$ one–one correspondence between homogeneous self-adjoint cones $C \subset V$ , with $p \in C ,$ , and formally real Jordan algebra structures $( V , \cdot )$ on $V$ , with identity $p$ , given by:

$$
C = \{ \exp ( a ) \mid a \in V \} = \{ a ^ { 2 } \mid a { \mathrm { ~ i n v e r t i b l e ~ i n ~ } } V \}
$$

and this cone is self-adjoint w.r.t. $\langle x , y \rangle = \operatorname { T r } \left( L _ { x \cdot y } \right)$ ;

$$
\operatorname { L i e } \left( \operatorname { A u t } ( C , V ) \right) = \operatorname { D e r } V \oplus \left\{ L _ { x } \mid x \in V \right\}
$$

(orthogonal with respect to the Killing form on Lie Aut $( C , V ) )$ .

This description of $C$ is useful for describing the symmetry on $C$ , i.e., picking a base point $p \in C$ , $C \cong G / K$ , and the Cartan involution $\sigma : G \longrightarrow G$ induces ${ \overline { { \sigma } } } : C \longrightarrow C$ : we claim that, in this Jordan algebra structure on $V$ $\overline { { \sigma } } ( x ) = x ^ { - 1 }$ To see this, suppose $x = \exp _ { J } ( a )$ . Then

$$
x = \exp _ { J } a = ( \exp { L _ { a } } ) ( p ) .
$$

Now $L _ { a } \in { \mathfrak { p } }$ , hence $\exp L _ { a } \in \exp { \mathfrak { p } } \subset G .$ , and hence $\sigma ( \exp L _ { a } ) = ( \exp L _ { a } ) ^ { - 1 } =$ $\exp ( - L _ { a } )$ . Thus

$$
\overline { { \sigma } } ( x ) = \sigma ( \exp L _ { a } ) ( p ) = \exp ( - L _ { a } ) ( p ) = \exp _ { J } ( - a ) = \exp _ { J } ( a ) ^ { - 1 } = x ^ { - 1 } .
$$

We mention one more fact about this correspondence. To derive a Jordan algebra from a cone $C \subset V$ , we had to choose a basepoint $p$ . Suppose we choose a new basepoint $p ^ { \prime } = g p$ , with $g \in \exp { \mathfrak { p } }$ . We claim that the new Jordan algebra structure on $V$ is isomorphic to the old one. If ${ \mathfrak { g } } = { \mathfrak { k } } \oplus { \mathfrak { p } }$ is the Cartan decomposition corresponding to $p$ , the new one for $p ^ { \prime }$ is $\mathfrak { g } = \mathrm { A d } \varrho ( \mathfrak { k } ) \oplus \mathrm { A d } \varrho ( \mathfrak { p } )$ .

Say $u _ { 1 } , u _ { 2 } \in V$ and $u _ { i } = \pi _ { i } p$ with $\pi _ { i } \in { \mathfrak { p } }$ . Then $g u _ { i } = ( g \pi _ { i } g ^ { - 1 } ) p ^ { \prime }$ . Therefore, if $\perp$ denotes the new Jordan multiplication, we have

$$
g u _ { 1 } \perp g u _ { 2 } = ( g \pi _ { 1 } g ^ { - 1 } ) ( g \pi _ { 2 } g ^ { - 1 } ) p ^ { \prime } = g ( \pi _ { 1 } ( \pi _ { 2 } p ) ) = g ( u _ { 1 } \cdot u _ { 2 } ) .
$$

Hence $g$ induces an isomorphism $V \longrightarrow V _ { \perp }$

Technically $V _ { \perp }$ is called the mutation of $V$ by $p ^ { \prime }$ . See [5], Ch. 5, or [8], pp. 67ff.

# 3 Boundary components and Peirce decompositions

# 3.1

Let $V$ be a real vector space defined over $\mathbb { Q }$ and let $C \subset V$ be a self-adjoint homogeneous cone. Let $G = { \bf A u t } ( C , V ) ^ { o }$ . Fix once and for all a rational point $p \in C$ to be the basepoint, and let $K$ be the stabilizer of $p$ in $G$ . Since $K$ is maximal compact there corresponds to it a Cartan involution $\sigma$ of $\operatorname { L i e } \left( G \right)$ , so that $\operatorname { L i e } \left( G \right) = \operatorname { L i e } \left( K \right) + { \mathfrak { p } }$ , where $\mathfrak { p }$ is the $^ { - 1 }$ -eigenspace of $\sigma$ and $\operatorname { L i e } \left( K \right)$ is the $+ 1$ -eigenspace. There is an inner product $\langle \cdot , \cdot \rangle$ on $V$ with respect to which $\exp { \sigma g } = { } ^ { t } ( \exp { g } ) ^ { - 1 }$ , where t denotes the adjoint. Thus, elements of $K$ are orthogonal and elements of exp p are self-adjoint w.r.t. this scalar product. As we saw in Section 1, $C$ is self-adjoint for any such inner product.

We assume that the subgroup $G \subset \mathbf { G L } ( V )$ is defined over $\mathbb { Q }$ . This strong assumption implies that Lie $( K )$ and the Killing form are defined over $\mathbb { Q }$ , hence also $\mathfrak { p }$ and $\sigma$ . Therefore we may choose the scalar product so that it is defined over $\mathbb { Q }$ too. Then if $L$ is a lattice in $V$ giving the $\mathbb { Q }$ -structure, $L$ and the dual lattice $L ^ { * }$ are commensurable.

Regard $\operatorname { L i e } \left( \operatorname { A u t } V \right)$ as $\operatorname { E n d } ( V )$ , so that ${ \mathfrak { p } } \subset \operatorname { E n d } ( V )$ . Then we may identify $\mathfrak { p }$ with $V$ by identifying $\pi$ and $\pi p$ for any ${ \boldsymbol { \pi } } \in { \mathfrak { p } }$ . Thus $\mathfrak { p }$ acquires a Jordan algebra structure with Jordan multiplication $\cdot$ defined by $( \pmb { \pi } \cdot \pmb { \pi } ^ { \prime } ) p = \pmb { \pi } ( \pmb { \pi } ^ { \prime } p )$ . We can transfer this structure to $V$ . When we think of the Jordan algebra we will use the symbol $V$ , reserving $\mathfrak { p }$ for the Lie algebra guise. Now $\mathfrak { p }$ has a $\mathbb { Q }$ - structure as a vector space which is identical with that of $V$ . Therefore, $V$ as a Jordan algebra is defined over $\mathbb { Q }$ , since $\mathfrak { p }$ acts $\mathbb { Q }$ -morphically on $V$ , and the Jordan multiplication is just the pullback of this action via ${ \mathfrak { p } } \longrightarrow V$ . Finally, $V$ is formally real, that is, $x ^ { 2 } + y ^ { 2 } = 0 \Longrightarrow x = y = 0$ .

Conversely, given any formally real Jordan algebra $V$ defined over $\mathbb { Q }$ , its identity element $p$ will be rational. Putting

$$
C = \{ x ^ { 2 } \mid x \in V { \mathrm { ~ i s ~ i n v e r t i b l e } } \} ,
$$

we acquire a situation as described above if we let $\langle x , y \rangle = \operatorname { T r } \left( L _ { x \cdot y } \right)$

#

Fix any subfield $k$ of $\mathbb { R }$ , and take rational to mean $k$ -rational.

Let $\varepsilon \in V$ be a rational idempotent. For any $x \in V$ , denote by $L _ { x }$ the map $L _ { x } ( y ) = x \cdot y$ , for $y \in V$ . Then $L _ { \varepsilon }$ is semi-simple and has eigenvalues 0, $\frac { 1 } { 2 }$ , and 1. Let $V _ { i } ( \varepsilon )$ , or $V _ { i }$ when no confusion is possible, denote the $i \cdot$ -eigenspace. This gives the so-called Peirce decomposition

$$
V = V _ { 0 } \oplus V _ { \frac { 1 } { 2 } } \oplus V _ { 1 } ;
$$

see Section 2. In particular,

$$
\begin{array} { r } { V _ { 0 } \cdot V _ { 1 } = 0 , V _ { 0 } \cdot V _ { \frac { 1 } { 2 } } \subset V _ { \frac { 1 } { 2 } } , V _ { 1 } \cdot V _ { \frac { 1 } { 2 } } \subset V _ { \frac { 1 } { 2 } } , V _ { \frac { 1 } { 2 } } \cdot V _ { \frac { 1 } { 2 } } \subset V _ { 0 } \oplus V _ { 1 } \ , } \end{array}
$$

and $V _ { 0 } , V _ { 1 }$ are sub Jordan algebras. Since $p$ is the identity in $V$ , also $p - \varepsilon$ is an idempotent, and $V _ { 0 } ( \varepsilon ) = V _ { 1 } ( p - \varepsilon )$ . The Peirce decomposition is defined over $k$ since $\varepsilon$ is rational.

Thus if $C _ { i } = C _ { i } ( \varepsilon )$ , $i = 0 , 1$ , is the cone of squares of invertible elements in $V _ { i }$ , then $C _ { i }$ is a self-adjoint homogeneous cone since $V _ { i }$ inherits formal-reality from $V$ , and everything is compatibly defined over $k$ . We call $C _ { i }$ a rational boundary component of $C$ . Note that $C$ and $\{ 0 \}$ are, by definition, boundary components; we call them improper boundary components.

Note† that $\overline { { C } }$ , the closure of $C$ , is simply the set of squares in $V$

To persuade ourselves that this is indeed a good notion of boundary component, we prove:

Proposition 3.1 The closure $\overline { { C } }$ of $C$ is the disjoint union of the real boundary components.

Proof Say $y \in { \overline { { C } } }$ and $y = x ^ { 2 }$ for some $x \in V$ . Then $x$ generates a sub Jordan algebra $W$ , consisting of polynomials in $x$ with no constant term. Note that $W \subset \mathbb { R } [ x ]$ and, since $\mathbb { R } [ x ]$ is formally real, $\mathbb { R } [ x ]$ is isomorphic to a product of copies of $\mathbb { R }$ with componentwise multiplication. Hence also any (not necessarily unital) $\mathbb { R }$ -subring of $\mathbb { R } [ x ]$ is isomorphic to a product of copies of $\mathbb { R }$ and, in particular, possesses a unit. Therefore $W$ has a unit $e$ . In $V$ itself, $e$ is an idempotent, and $W \subset V _ { 1 } ( e )$ .

Now $e \in W$ means that $e = a _ { 1 } x + a _ { 2 } x ^ { 2 } + \cdots + a _ { n } x ^ { n }$ for some $a _ { i } \in \mathbb { R }$ . Square both sides to get

$$
a _ { 1 } ^ { 2 } x ^ { 2 } + 2 a _ { 1 } a _ { 2 } x ^ { 3 } + \cdots + a _ { n } ^ { 2 } x ^ { 2 n } = e ,
$$

and therefore

$$
( a _ { 1 } ^ { 2 } x + 2 a _ { 1 } a _ { 2 } x ^ { 2 } + \cdots ) x = e ~ .
$$

Now $a _ { 1 } ^ { 2 } x + 2 a _ { 1 } a _ { 2 } x ^ { 2 } + \cdots$ is in $W$ , so $x$ is invertible in $V _ { 1 } ( e )$ . Thus $y = x ^ { 2 }$ is the square of an invertible element in $V _ { 1 } ( e ) = V _ { 0 } ( p - e )$ and thus is in some boundary component.

To show the boundary components do not overlap, suppose $y$ is an invertible element in both $V _ { 1 } ( \varepsilon _ { 1 } )$ and $V _ { 1 } ( \varepsilon _ { 2 } )$ . There exists $x _ { i } \in V _ { 1 } ( \varepsilon _ { i } )$ with $x _ { i } \cdot y = \varepsilon _ { i }$ , $i = 1 , 2$ . In general, if $y$ is an invertible element in a Jordan algebra, then its inverse is an element in the subalgebra $W$ generated by $y$ and $p$ . Note that $W$ is associative. Applying this to $V _ { 1 } ( \varepsilon _ { 1 } )$ and $V _ { 1 } ( \varepsilon _ { 2 } )$ gives $x _ { 1 } , x _ { 2 } \in W$ . Therefore $x _ { i } \cdot y = \varepsilon _ { i } \in W$ for $i = 1 , 2$ , and so $\varepsilon _ { 1 } = \varepsilon _ { 1 } \cdot \varepsilon _ { 2 } = \varepsilon _ { 2 }$ .

Recall that we have an inner product on ⎛ $V$ , defined by $\langle x , y \rangle = \mathrm { T r } \left( L _ { x \cdot y } \right)$ . The Peirce eigenspaces of $L _ { \varepsilon }$ are mutually orthogonal with respect to it. Thus in⎟ some orthogonal basis, we can write the matrix for ⎜⎜ $L _ { \varepsilon }$ as

$$
L _ { \varepsilon } = \left( \begin{array} { c c c c c c c } { 1 } & & & & & & & \\ & { \ddots } & & & & & { 0 } \\ & & { 1 } & & & & \\ & & & { \frac { 1 } { 2 } } & & & & \\ & & & & { \ddots } & & & \\ & & & & { \frac { 1 } { 2 } } & & & \\ & & & & & { 0 } & \\ & { 0 } & & & & & { \ddots } & \\ & & & & & & { 0 } \end{array} \right) ,
$$

which we will always write using block notation:

$$
L _ { \varepsilon } = \left( \begin{array} { c c c } { { 1 } } & { { } } & { { } } \\ { { } } & { { \frac { 1 } { 2 } } } & { { } } \\ { { } } & { { } } & { { 0 } } \end{array} \right) .
$$

Recall the identification of $\mathfrak { p }$ and $V$ and note that, for any element $x$ $, \exp x =$ $p + x + { \textstyle \frac { 1 } { 2 } } x ^ { 2 } + { \textstyle \frac { 1 } { 6 } } x ^ { 3 } + \cdot \cdot \cdot$ is the same in the Jordan algebra as in the Lie algebra⎜ ⎟ ${ \mathfrak { p } } \subset \operatorname { E n d } ( V )$ . Thus

$$
L _ { \mathrm { e x p } t \varepsilon } = \left( \begin{array} { c c c } { { \mathrm { e } ^ { t } } } & { { } } & { { } } \\ { { } } & { { \mathrm { e } ^ { \frac { 1 } { 2 } t } } } & { { } } \\ { { } } & { { } } & { { 1 } } \end{array} \right) \ .
$$

Introducing the new parameter $s = \mathtt { e } ^ { { \frac { 1 } { 2 } } t }$ , we have

$$
L _ { \mathrm { e x p } t \varepsilon } = \left( \begin{array} { c c c c } { s ^ { 2 } } & { } & { } & { } \\ { } & { s } & { } & { } \\ { } & { } & { 1 } \end{array} \right) = a ( s ) \ ,
$$

where $a ( s )$ is a one-parameter subgroup contained in $\exp { \mathfrak { p } } \subset G$ . Clearly, $a ( s )$ is an algebraic one-parameter subgroup, defined over $k$ if $\varepsilon$ is. Also, $\varepsilon = \varepsilon p =$ ${ \frac { 1 } { 2 } } a ^ { \prime } ( 1 ) p$ , where the prime denotes $\frac { \mathrm { d } } { \mathrm { d } s }$ .

In particular, if we choose for $\varepsilon$ the identity $p$ , we get $a ( s ) = h ( s ^ { 2 } )$ , where $h ( u )$ is the one-parameter subgroup of homotheties.

Since $\boldsymbol { \varepsilon } \cdot \boldsymbol { \varepsilon } = \boldsymbol { \varepsilon }$ , we have $\varepsilon ( \varepsilon p ) = \varepsilon p$ , and thus $\pi _ { \frac { 1 } { 2 } } p = 0$ , where $\pi _ { i }$ is the orthogonal projection onto $V _ { i } ( \varepsilon )$ , for $\begin{array} { r } { i = 0 , \frac { 1 } { 2 } } \end{array}$ , 1. Moreover, if $a ( 0 ) = \operatorname* { l i m } _ { s \longrightarrow 0 } a ( s )$ which exists in $\operatorname { E n d } ( V )$ , then $a ( 0 ) = \pi _ { 0 }$ and $V _ { 0 } ( \pmb { \varepsilon } ) = a ( 0 ) V$ .

Remark 3.2 More generally, let $a ( s )$ be any one-parameter subgroup in $G$ . There exists a unique $n \in \mathbb { Z }$ such that $\operatorname* { l i m } _ { s \to 0 } h ( s ^ { n } ) a ( s )$ exists and is nonzero. Denote the limit by $a ( 0 )$ . We will show later that $a ( 0 ) V$ is a sub Jordan algebra of $V$ , and $a ( 0 ) C$ is a boundary component, $k$ -rational if $a ( s )$ is.

#

Corresponding to any one-parameter subgroup $a$ in $G$ there is a parabolic subgroup $\begin{array} { r } { P ( a ) = \{ x \in G \mid \operatorname* { l i m } _ { s \longrightarrow 0 } a ( s ) ^ { - 1 } x a ( s ) } \end{array}$ exists}, see [11], §2.2. In particular, let $a ( s )$ be the one-parameter subgroup defined over $k$ corresponding, as above, to a rational idempotent $\varepsilon$ . On Lie $( G )$ , $a ( s )$ acts semi-simply in the adjoint representation, so that Lie $( G ) = \oplus _ { \chi } \mathfrak { U } _ { \chi }$ , where $\chi$ is a character of $a ( s )$ and

$$
\mathfrak { U } _ { \chi } = \{ u \in \mathrm { L i e } ( G ) | a ( s ) ^ { - 1 } u a ( s ) = \chi ( s ) u \} \ .
$$

Since $a$ is one-dimensional, $\chi ( s ) = s ^ { m }$ for some $m \in \mathbb { Z }$ . Let $\mathfrak { U } _ { m } = \mathfrak { U } _ { \chi }$ in this case.

Let $Z ( a )$ be the centralizer of $a$ in $G$ and let $U$ be the subgroup of $G$ with Lie algebra equal to $\oplus _ { m > 0 } \mathfrak { U } _ { m }$ . Then $Z ( a )$ normalizes $U$ , and $P ( a ) = Z ( a ) U$ is the parabolic subgroup corresponding to $a ( s )$ . Clearly, $P ( a )$ is $k$ -parabolic since $a ( s )$ is defined over $k$ .

Write $\operatorname { N o r m } \left( C _ { 0 } \right) = \left\{ g \in G \mid g C _ { 0 } \subset C _ { 0 } \right\}$ , where $C _ { 0 }$ is any boundary component. First we establish a lemma.

Lemma 3.3 $\pi _ { 0 } ( C ) = C _ { 0 }$

Proof Since $\pi _ { 0 } = \operatorname* { l i m } _ { s \longrightarrow 0 } a ( s )$ , we see that $\pi _ { 0 } ( x ) \in { \overline { { C } } }$ for any $x \in C$ . Now, by the self-adjoint property of $C$ and $C _ { 0 }$ , we know that

$$
\begin{array} { r l } & { C = \left\{ z \in V \mid \langle z , y ^ { 2 } \rangle > 0 \mathrm { ~ f o r ~ a l l ~ } y \in V , \ y \neq 0 \right\} , } \\ & { C _ { 0 } = \left\{ z \in V _ { 0 } \mid \langle z , y ^ { 2 } \rangle > 0 \mathrm { ~ f o r ~ a l l ~ } y \in V _ { 0 } , \ y \neq 0 \right\} \ . } \end{array}
$$

Because $\pi _ { 0 }$ is an orthogonal projection onto $V _ { 0 }$ , we have $\langle \pi _ { 0 } ( x ) , y ^ { 2 } \rangle = \langle x , y ^ { 2 } \rangle >$ 0 for any $y \in V _ { 0 }$ , since $x \in C$ . Therefore $\pi _ { 0 } ( x ) \in C _ { 0 }$ .

Conversely, suppose $x _ { 0 } \in C _ { 0 }$ . Let $\pmb { \varepsilon } ^ { \prime } = p - \pmb { \varepsilon }$ , so that $\varepsilon ^ { \prime }$ is the identity in $V _ { 0 }$ . Now $x _ { 0 } \in C _ { 0 }$ implies there exist $y , z \in V _ { 0 } ( \varepsilon )$ with $y ^ { 2 } = x _ { 0 }$ and $y \cdot z = \varepsilon ^ { \prime }$ . Then $( y + \varepsilon ) ^ { 2 } = y ^ { 2 } + 2 y \cdot \varepsilon + \varepsilon ^ { 2 } = x _ { 0 } + \varepsilon$ and

$$
( y + \varepsilon ) \cdot ( z + \varepsilon ) = y \cdot z + \varepsilon = \varepsilon ^ { \prime } + \varepsilon = p \ . 
$$

Thus $x _ { 0 } + \varepsilon \in C$ and $\pi _ { 0 } ( x _ { 0 } + \varepsilon ) = x _ { 0 }$

Proposition 3.4 $P ( a ) = \mathrm { N o r m } \left( C _ { 0 } \right)$

Proof Let $u$ be an element of $\mathfrak { U } _ { m }$ for $m > 0$ . Then $s ^ { m } a ( s ) u = u a ( s )$ . Taking the limit as $s \longrightarrow 0$ , we have $u \pi _ { 0 } = 0$ . Thus $u C _ { 0 } = u \pi _ { 0 } ( C ) = 0$ . Hence $\operatorname { e x p } u$ normalizes $C _ { 0 }$ , and in fact restricts to the identity on $C _ { 0 }$ . If $z \in Z ( a )$ , then $z$ commutes with $a ( s )$ for all $s$ , hence also commutes with $\pi _ { 0 }$ , and $z$ normalizes $C _ { 0 }$ as well. Since $P ( a ) = Z ( a ) U$ , we see that $P ( a ) \subset \mathsf { N o r m } \left( C _ { 0 } \right)$ .

If $\mathrm { N o r m } \left( C _ { 0 } \right)$ is actually a larger parabolic than $P ( a )$ , then there must be some $m < 0$ with $\mathfrak { U } _ { m } \cap \mathrm { L i e N o r m } ( C _ { 0 } ) \neq ( 0 )$ (since $\operatorname { A d } a ( s )$ is semi-simple). Pick $\nu \neq 0$ in this intersection. We have $a ( s ) \nu = s ^ { - m } \nu a ( s )$ , and, letting $s \longrightarrow 0$ , we see $\pi _ { 0 } \nu = 0$ . Therefore $\pi _ { 0 } ( \exp \nu ) = \pi _ { 0 }$ . Since $\exp \nu \in \mathrm { N o r m } ( C _ { 0 } )$ , and $p - \varepsilon \in C _ { 0 }$ , we get $( \exp \nu ) ( p - \varepsilon ) = ( p - \varepsilon )$ .

On the other hand, we can apply the first paragraph to the one-parameter subgroup $b ( s ) = a ^ { - 1 } ( s ) h ^ { 2 } ( s )$ corresponding to $p - \varepsilon$ and to $C _ { 1 }$ , the corresponding boundary component in $V _ { 0 } ( p - \varepsilon )$ . This shows that $\mathrm { e x p } \nu$ restricts to the identity on $C _ { 1 }$ . Because $\varepsilon \in C _ { 1 }$ , we get $( \exp \nu ) \varepsilon = \varepsilon$ .

Adding these together gives $( \exp \nu ) p = p$ , which says $\exp \nu \in K$ . But $K$ is compact and $\mathfrak { U } _ { m }$ is nilpotent so $\nu = 0$ , a contradiction.

Proposition 3.5 For any boundary component $C _ { 0 }$ and any $g \in G$ , $g C _ { 0 }$ is also $a$ boundary component.

Proof Let $P = { \mathrm { N o r m } } \left( C _ { 0 } \right)$ . Then $G = K P$ , so it suffices to prove that $g C _ { 0 }$ is a boundary component if $g \in K$ . But $g \in K$ implies that $g$ fixes $p$ , so it is easy to see that $g : V \longrightarrow V$ is an automorphism of Jordan algebras. Thus, if $\varepsilon$ is an idempotent, so is $_ { g \varepsilon }$ , and $g V _ { 0 } ( \pmb { \varepsilon } ) = V _ { 0 } ( g \pmb { \varepsilon } )$ .

# 3.4

Any semi-simple Jordan algebra $W$ over $k$ has a unique decomposition (up to permutation of factors) $W = W _ { 1 } \oplus \cdots \oplus W _ { r }$ , where $W _ { i }$ are simple Jordan algebras over $k$ , ideals in $W$ , and $W _ { i } \cdot W _ { j } = 0$ if $i \neq j$ . In our set-up, we say that the cone $C$ is $k$ -reducible if and only if $C$ can be written as $C = C _ { 1 } + C _ { 2 }$ (or equivalently $\overline { { { C } } } = \overline { { { C } } } _ { 1 } + \overline { { { C } } } _ { 2 } ,$ ), where the $C _ { i }$ are open cones in $k$ -rational linear subspaces $V _ { i } \subset V$ such that $V _ { 1 } \cap V _ { 2 } = ( 0 )$ ; otherwise $C$ is called $k$ -irreducible.

Lemma 3.6 The cone $C$ decomposes uniquely into $C = C _ { 1 } + \cdots + C _ { n }$ with each $C _ { i }$ being $k$ -irreducible in $V _ { i }$ and $V = V _ { 1 } \oplus \cdots \oplus V _ { n }$ .

Proof Suppose $\overline { { C } } = \overline { { C } } _ { 1 } + \overline { { C } } _ { 2 }$ and $\overline { { C } } = \overline { { D } } _ { 1 } + \overline { { D } } _ { 2 }$ are two decompositions of $C$ . We claim that $\overline { { C } } _ { 1 } = ( \overline { { C } } _ { 1 } \cap \overline { { D } } _ { 1 } ) + ( \overline { { C } } _ { 1 } \cap \overline { { D } } _ { 2 } )$ . Indeed, let $x \in { \overline { { C } } } _ { 1 }$ and write $x = d _ { 1 } + d _ { 2 }$ , with $d _ { i } \in \overline { { D } } _ { i }$ . Write $d _ { i } = e _ { i 1 } + e _ { i 2 }$ , $e _ { i j } \in \overline { { C } } _ { j }$ . Then $x - ( e _ { 1 1 } + e _ { 2 1 } ) = ( e _ { 1 2 } + e _ { 2 2 } )$ is in the linear span of $C _ { 1 }$ and of $C _ { 2 }$ . Thus $e _ { 1 2 } + e _ { 2 2 } = 0$ ; hence $e _ { 1 2 } = e _ { 2 2 } = 0$ and $d _ { 1 } , d _ { 2 } \in \overline { { C } } _ { 1 }$ .

By a dimension argument, $C$ has at least one decomposition as desired in the lemma, and the claim shows that it is unique up to permutation of the factors.

Proposition 3.7 The cone $C$ is $k$ -irreducible if and only if $V$ is $k$ -simple as a Jordan algebra.

Proof If $V$ is $k$ -reducible, then $C$ obviously is also. Now suppose $C$ is $k$ - reducible. Write $C = \Sigma C _ { i }$ as a sum of $k$ -irreducible factors. Since this decomposition is unique, any $g \in G ( k )$ acting on $C$ must permute the $C _ { i }$ .

Since $G ( k )$ is Zariski-dense in $G$ , we conclude that each $g \in G$ permutes the factors $C _ { i }$ ; and because $G$ is connected, it actually takes each $C _ { i }$ into itself, i.e., $G = \Pi \operatorname { A u t } ( C _ { i } ) ^ { o }$ . Now it is obvious that $V = \Pi V _ { i }$ as Jordan algebras and $V$ is not $k$ -simple.

# 3.5

Proposition 3.8 Suppose that $\varepsilon _ { 1 } , \ldots , \varepsilon _ { n }$ are a set of $k$ -idempotents which are mutually orthogonal, i.e., $\varepsilon _ { i }$ is $k$ -rational for each $i$ and $\pmb { \varepsilon } _ { i } \cdot \pmb { \varepsilon } _ { j } = \delta _ { i j } \pmb { \varepsilon } _ { j }$ . Then $\textstyle \sum _ { i = 1 } ^ { k } \mathbb { R } \pmb { \varepsilon } _ { i } = \operatorname { L i e } \left( A \right)$ , where $A$ is a $k$ -split torus of rank $k$ and $A \subset$ exp p.

Proof This follows from the following three facts:

(a) In any Jordan algebra, $L _ { u }$ and $L _ { u \cdot \nu }$ commute if and only if $L _ { u ^ { 2 } }$ and $L _ { \nu }$ do. This implies that $\textstyle \sum \mathbb { R } \varepsilon _ { i }$ is a strictly commutative sub Jordan algebra.   
(b) $[ L _ { \pi } , L _ { \pi ^ { \prime } } ] = \mathrm { a d } [ \pi , \pi ^ { \prime } ]$ for $\pi , \pi ^ { \prime } \in \mathfrak { p }$ .   
(c) For any $x \in \operatorname { L i e } \left( K \right)$ , $\operatorname { a d } x ( { \mathfrak { p } } ) = 0 \Longrightarrow x = 0$ . This is because $x \longmapsto \operatorname { a d } x$ defines $\operatorname { L i e } \left( K \right) { \xrightarrow { \sim } } \operatorname { D e r } V$ as we have seen in Section 2, cf. Theorem 2.13.

Thus $\mathfrak { A } = \textstyle \sum \mathbb { R } \varepsilon _ { i }$ is a commutative sub Lie algebra of $\mathfrak { p }$ . Each $\mathbb { R } \pmb { \mathscr { E } } _ { i } = \mathbf { L i e } a _ { i } ( s )$ is an algebraic Lie algebra, where $a _ { i } ( s )$ is the one-parameter subgroup corresponding to $\varepsilon _ { i }$ , so $\mathfrak { A }$ is algebraic too. Then $A = \exp { \mathfrak { A } }$ is a connected diagonalizable algebraic group and Lie A is defined over $k$ , so $A$ is a $k$ -torus. Since each $a _ { i } ( s )$ is a $k$ -one-parameter subgroup, we see that $A$ is $k$ -split. The rank of $A$ is $n$ , because $\begin{array} { r } { \varepsilon _ { i } = \frac { 1 } { 2 } a _ { i } ^ { \prime } ( 1 ) } \end{array}$ , and the $\varepsilon _ { i }$ are linearly independent.

Note that, denoting $Y ( A ) = \operatorname { H o m } \left( \mathbb { G } _ { m } , A \right)$ , there is a canonical isomorphism

$$
\sum _ { i = 1 } ^ { k } \mathbb { Q } \varepsilon _ { i } \xrightarrow { \sim } Y ( A ) \otimes \mathbb { Q }
$$

taking $\varepsilon _ { i }$ to $a _ { i } \in Y ( A )$

# 3.6

Proposition 3.9 Every maximal $\mathbb { R }$ -split torus A, such that $A \subset \exp { \mathfrak { p } }$ , arises as in Proposition 3.8, i.e., $\begin{array} { r } { A = \exp ( { \sum _ { i = 1 } ^ { n } \mathbb { R } } \pmb { \mathscr { E } } _ { i } ) } \end{array}$ , where $\varepsilon _ { i }$ are mutually orthogonal idempotents of $V$ .

Proof First we establish the following lemma:

Lemma 3.10 If $\dim V > 1$ , then $V$ possesses an idempotent different from 0 and $p$ .

Proof Choose $u \in V$ linearly independent from $p$ , and let $W$ be the sub Jordan algebra generated by $u$ . Then $W$ is totally real and strictly commutative, so $W \cong \mathbb { R } ^ { s }$ , where the Jordan multiplication in $\mathbb { R } ^ { s }$ is just componentwise multiplication. If $s > 1$ , then $W$ has at least two non-trivial idempotents, and, if $s = 1$ , some multiple of $u$ works.

Since any two maximal $\mathbb { R }$ -split tori contained in expp are conjugate by an element of $K$ which also acts as an automorphism of $V$ , it suffices to take a maximal set $\varepsilon _ { 1 } , \ldots , \varepsilon _ { n }$ of mutually orthogonal idempotents and check that the resulting $A = \exp ( \textstyle \sum \mathbb { R } \pmb { \varepsilon } _ { i } )$ is maximal. We will prove this by induction on $\mathrm { d i m } V$ . If $\dim V = 1$ , the result is obvious. If $\dim V > 1$ , then $n \geq 2$ by the lemma.

Let $V = V _ { 0 } \oplus V _ { \frac { 1 } { 2 } } \oplus V _ { 1 }$ be the Peirce decomposition of $V$ with respect to $\varepsilon _ { 1 }$ . Then $\{ \varepsilon _ { 2 } , \ldots , \varepsilon _ { n } \}$ are a maximal set of mutually orthogonal idempotents in $V _ { 0 }$ and similarly $\{ \varepsilon _ { 1 } \}$ in $V _ { 1 }$ . For $i = 0$ or 1, let $C _ { i } \subset V _ { i }$ be the boundary components, $G _ { i } = \mathrm { A u t } ( C _ { i } ) ^ { o }$ , $A _ { 1 } = \exp \mathbb { R } \pmb { \varepsilon } _ { 1 }$ , and $A _ { 0 } = \exp { \textstyle \sum _ { i = 2 } ^ { n } \mathbb { R } } \pmb { \varepsilon } _ { i }$ . By induction, $A _ { i }$ is a maximal $\mathbb { R }$ -split torus in $G _ { i }$ . If $A = A _ { 1 } \times A _ { 2 }$ is not maximal, let $A ^ { \prime } \supsetneq A$ be a maximal $\mathbb { R }$ -split torus with $A ^ { \prime } \subset \displaystyle \exp ( \mathfrak { p } )$ . Since $A ^ { \prime }$ commutes with $a _ { 1 }$ , we have $A ^ { \prime } \subset Z ( a _ { 1 } ) \subset \operatorname { N o r m } \left( C _ { 0 } \right) \cap \operatorname { N o r m } \left( C _ { 1 } \right)$ , and we get restriction maps $\varphi :$ $A ^ { \prime } \longrightarrow G _ { 1 } \times G _ { 2 }$ . By the maximality of $A _ { i }$ in $G _ { i }$ , the image $\varphi ( A ^ { \prime } )$ has to be all of $A _ { 1 } \times A _ { 2 }$ . So $\varphi$ has a non-trivial one-parameter subgroup $b ( s )$ in its kernel. But then $b ( s )$ is the identity on $C _ { i }$ ; hence $b ( s ) ( \pmb { \varepsilon } _ { 1 } ) = \pmb { \varepsilon } _ { 1 }$ and $b ( s ) ( p - \pmb { \varepsilon } _ { 1 } ) =$ $p - \varepsilon _ { 1 }$ , hence $b ( s ) ( p ) = p$ , and therefore $b ( s ) \in K$ . Since $K$ is compact, this is a contradiction, so $A ^ { \prime } = A$ . □

# 3.7

Proposition 3.11 For every $k \subset \mathbb { R }$ , there exist maximal $k$ -split tori A such that $A \subset \exp { \mathfrak { p } }$ and all such arise as $\scriptstyle \sum _ { i = 1 } ^ { n } \mathbb { R } \varepsilon _ { i }$ , where $\varepsilon _ { i }$ are mutually orthogonal $k$ -idempotents of $V$ .

Proof The existence of such $A$ follows from:

Lemma 3.12 If $G$ is a reductive algebraic group defined over $k \subset \mathbb { R }$ , $\sigma : G \longrightarrow$ $G$ is a Cartan involution over $\mathbb { R }$ , and $P \subset G$ is a minimal $k$ -parabolic of $G ,$ , then there is a unique torus $S \subset P$ such that

(i) $\sigma ( x ) = x ^ { - 1 }$ , for all $x \in S$ ;   
(ii) $s$ is a lifting into $P$ of the unique maximal $k$ -split torus $T$ in $P / R _ { u } ( P )$ .

If $\sigma$ is defined over $k _ { : }$ , then so is $s$ .

Proof By Proposition 1.8 in [4], there exists a unique Levi subgroup $L$ of $P$ which is stable under the Cartan involution $\sigma$ . The lifting $S _ { 1 }$ of $T$ into this $L$ has the required properties. Conversely, for any such torus $s$ , we know that $P =$ $Z _ { G } ( S ) \ltimes R _ { u } ( P )$ , and $s$ stable by $\sigma$ implies $Z _ { G } ( S )$ stable by $\sigma$ , i.e., $Z _ { G } ( S ) = L$ . Thus $S = S _ { 1 }$ . By the uniqueness of $s$ , $\sigma$ defined over $k$ implies $s$ is $\operatorname { G a l } \left( \mathbb { C } / k \right)$ - invariant, hence $s$ is defined over $k$ .

Going back to the proposition, let $A \subset \exp { \mathfrak { p } }$ be a maximal $k$ -split torus. Then ${ \mathfrak { A } } = \operatorname { L i e } A \subset { \mathfrak { p } }$ is defined over $k$ , so that $\mathfrak { A }$ generates a sub Jordan algebra ${ \mathfrak { A } } _ { 0 } \subset V$ defined over $k$ (identifying $\mathfrak { p }$ and $V$ as usual).

Now $A$ is contained in some maximal $\mathbb { R }$ -split torus $B$ . We may assume $B \subset \exp { \mathfrak { p } }$ . Proposition 3.9 implies that Lie $B$ is a strictly commutative sub Jordan algebra. Therefore ${ \mathfrak { A } } _ { 0 }$ is as well, since $\mathfrak { A } _ { 0 } \subset \mathrm { L i e } B$ .

So we have $\mathfrak { A } _ { 0 } \cong \Sigma _ { i = 1 } ^ { r } \mathbb { R } \varepsilon _ { i }$ (over $\mathbb { R }$ ) and, if $A _ { 0 }$ is the $k$ -torus defined as $\exp ( \mathfrak { A } _ { 0 } )$ ,

$$
\sum \mathbb { Q } \varepsilon _ { i } \cong Y ( A _ { 0 } ) \otimes \mathbb { Q } ~ .
$$

Now $\operatorname { G a l } ( \mathbb { C } / k )$ acts on both ${ \mathfrak { A } } _ { 0 }$ and on $A _ { 0 }$ . Acting on ${ \mathfrak { A } } _ { 0 }$ , it consists of Jordan isomorphisms, and hence is given by permutations of the $\varepsilon _ { i }$ . The above isomorphism is $\operatorname { G a l } ( \mathbb { C } / k )$ -equivariant. If

$$
\{ \varepsilon _ { i ( 1 , 1 ) } , \ldots , \varepsilon _ { i ( 1 , \ell _ { 1 } ) } \} , \ \{ \varepsilon _ { i ( 2 , 1 ) } , \ldots , \varepsilon _ { i ( 2 , \ell _ { 2 } ) } \} , \ \ldots .
$$

are the $\operatorname { G a l } ( \mathbb { C } / k )$ -orbits among the $\left\{ \varepsilon _ { i } \right\}$ , the subspace $( \Sigma \mathbb { Q } \varepsilon _ { i } ) ^ { \mathrm { G a l } ( \mathbb { C } / k ) }$ of invariants under $\operatorname { G a l } ( \mathbb { C } / k )$ in $\textstyle \sum \mathbb { Q } \varepsilon _ { i }$ is generated by

$$
\varepsilon _ { 1 } ^ { \prime } = \sum _ { j = 1 } ^ { \ell _ { 1 } } \varepsilon _ { i ( 1 , j ) } \ , \ \varepsilon _ { 2 } ^ { \prime } = \sum _ { j = 1 } ^ { \ell _ { 2 } } \varepsilon _ { i ( 2 , j ) } \ , \ \ldots \ .
$$

But then $A$ , which is the maximal $k$ -split torus in $A _ { 0 }$ , is given by

$$
A = \exp \left( \left( \sum \mathbb { R } \pmb { \varepsilon } _ { i } \right) ^ { \operatorname { G a l } \left( \mathbb { C } / k \right) } \right) = \exp \left( \sum \mathbb { R } \pmb { \varepsilon } _ { i } ^ { \prime } \right) ,
$$

and, since $\varepsilon _ { i } ^ { \prime }$ are mutually orthogonal idempotents, $A$ has the required form.

# 3.8

Choose a maximal set $\{ \varepsilon _ { 1 } , \ldots , \varepsilon _ { n } \}$ of mutually orthogonal $k$ -idempotents of $V$ . Let $A$ be the corresponding maximal $k$ -split torus, so that $\mathfrak { A } = \mathrm { L i e } \left( A \right) \cong \Sigma \mathbb { R } \varepsilon _ { i }$ , by canonical $k$ -isomorphism. We propose to compute the root structure of $G$ with respect to $A$ .

To do this, we use a Peirce decomposition for all the $\varepsilon _ { i }$ at once. Since $L _ { \varepsilon _ { i } }$ and $L _ { \varepsilon _ { j } }$ commute, and because $L _ { \varepsilon _ { 1 } } + \cdots + L _ { \varepsilon _ { n } } = \mathrm { i d }$ , it is easy to see that $V$ decomposes into simultaneous eigenspaces $V = \oplus _ { r \leq s } V _ { r s }$ with eigenvalues given by

$$
\varepsilon _ { t } \cdot \nu = \frac { 1 } { 2 } ( \delta _ { t r } + \delta _ { t s } ) \nu
$$

if $\nu \in V _ { r s }$

For convenience of notation, write $V _ { s r } = V _ { r s }$ if $s \geq r$ , and $x _ { r s } = x _ { s r }$ for an element of $V _ { r s }$ . For instance, if $\begin{array} { r } { x = \sum _ { k \leq \ell } x _ { k \ell } } \end{array}$ , then $\begin{array} { r } { x \cdot \varepsilon _ { m } = \frac { 1 } { 2 } \sum _ { k \neq m } x _ { k m } + x _ { m m } } \end{array}$ . Note that if $r \neq s$ , $V _ { r s } = V _ { \frac { 1 } { 2 } } ( \pmb { \varepsilon } _ { r } ) \cap V _ { \frac { 1 } { 2 } } ( \pmb { \varepsilon } _ { s } )$ , and $V _ { r r } = V _ { 1 } ( \varepsilon _ { r } )$ .

Let ${ \mathfrak { g } } = \operatorname { L i e } G$ . By Theorem 2.13, we know that ${ \mathfrak { g } } = \operatorname { D e r } V \oplus V$ . Here DerV

are the derivations of $V$ as a Jordan algebra. Hence $\operatorname { D e r } V \subset \operatorname { E n d } ( V )$ , it is defined over $k$ , and $\operatorname { D e r } V \cong \operatorname { L i e } K$ over $k$ . If $D , D ^ { \prime } \in \operatorname { D e r } V$ and $x , y \in V$ , the Lie bracket in $\mathfrak { g }$ is given by

$$
\begin{array} { c } { { [ D , x ] = D x , } } \\ { { { } } } \\ { { [ D , D ^ { \prime } ] = D D ^ { \prime } - D ^ { \prime } D , } } \\ { { { } } } \\ { { { } [ x , y ] = L _ { x } L _ { y } - L _ { y } L _ { x } . } } \end{array}
$$

To find the root structure, we are looking for elements $0 \neq ( D , x ) \in { \mathfrak { g } }$ such that $[ \varepsilon _ { i } , ( D , x ) ] = \lambda _ { i } ( D , x )$ , for $i = 1 , \ldots , n$ , and some $\lambda _ { i } \in \mathbb { C }$ . Thus we require $[ \varepsilon _ { i } , ( D , x ) ] = ( [ L _ { \varepsilon _ { i } } , L _ { x } ] , - D \varepsilon _ { i } ) = \lambda _ { i } ( D , x )$ .

That is,

$$
\begin{array} { r } { D \varepsilon _ { i } = - \lambda _ { i } x , } \\ { \left[ L _ { x } , L _ { \varepsilon _ { i } } \right] = - \lambda _ { i } D . } \end{array}
$$

Applying the lower equation to $\varepsilon _ { j }$ and using the top gives

$$
y \cdot \left( \pmb { \varepsilon } _ { i } \cdot \pmb { \varepsilon } _ { j } \right) - \pmb { \varepsilon } _ { i } \cdot \left( \pmb { x } \cdot \pmb { \varepsilon } _ { j } \right) = - \lambda _ { i } D \pmb { \varepsilon } _ { j } = \lambda _ { i } \lambda _ { j } x \ .
$$

Write $\begin{array} { r } { x = \sum _ { k \leq \ell } x _ { k \ell } } \end{array}$ , with $x _ { k \ell } \in V _ { k \ell }$ . We can deduce the following.

In the case $i = j$

$$
{ \frac { 1 } { 2 } } \sum _ { i \not = \ell } x _ { i \ell } + x _ { i i } - { \frac { 1 } { 4 } } \sum _ { i \not = \ell } x _ { i \ell } - x _ { i i } = \lambda _ { i } ^ { 2 } x .
$$

That is,

$$
{ \frac { 1 } { 4 } } \sum _ { i \not = \ell } x _ { i \ell } = \lambda _ { i } ^ { 2 } x \ .
$$

Hence,

(i) either $x \in \oplus _ { \ell \neq i } V _ { i \ell }$ and $\lambda _ { i } = \pm \frac { 1 } { 2 }$ ;   
(ii) or $x _ { i \ell } = 0$ for $\ell \neq i$ and $\lambda _ { i } = 0$ .

In particular, $\lambda _ { i } \in \{ 0 , \pm \frac { 1 } { 2 } \}$ for all $i$

In the case $i \neq j$

$$
- \frac 1 4 x _ { i j } = \lambda _ { i } \lambda _ { j } x .
$$

Hence,

(i) either $x \in V _ { i j }$ and $- \lambda _ { j } = \lambda _ { i } = \pm \frac { 1 } { 2 }$ ;   
(ii) or $x _ { i j } = 0$ and $\lambda _ { j } = 0$ or $\lambda _ { i } = 0$ .

Putting this information together shows that at most two $\lambda _ { k }$ can be non-zero. There are three possibilities:

(1) $\begin{array} { r } { \lambda _ { i } = \frac { 1 } { 2 } , \lambda _ { j } = - \frac { 1 } { 2 } , x \in V _ { i j } , } \end{array}$ , and all other $\lambda _ { k }$ are 0, where $1 \leq i \leq n , 1 \leq j \leq n$ and $i \neq j$ ;   
(2) all $\lambda _ { k } = 0$ and $x \in \bigoplus V _ { r r }$ ;   
(3) $\lambda _ { i } = \pm \frac { 1 } { 2 }$ , all other $\lambda _ { k }$ are 0, where $1 \leq i \leq n$ .

Possibility (3) is actually impossible. Since $\lambda _ { \ell } = 0$ for $\ell \neq i$ , we know $x _ { i \ell } = 0$ for $i \neq \ell$ , but $\lambda _ { i } = \pm \frac { 1 } { 2 }$ implies $x \in \oplus _ { \ell \neq i } V _ { i \ell }$ . So $x = 0$ , and then $\lambda _ { i } D = - [ L _ { x } , L _ { \varepsilon _ { i } } ]$ makes $D = 0$ also.

Possibility (2) just gives elements that centralize $\mathfrak { A }$ .

Possibility (1) is in fact realized, as long as $V _ { i j } \neq 0$ . To check this, take, without loss of generality, $i = 1$ , $j = 2$ , pick $x \in V _ { 1 2 }$ , and let $D = - 2 [ L _ { x } , L _ { \varepsilon _ { 1 } } ]$ .

# Claim

(a) $[ L _ { x } , L _ { \varepsilon _ { 2 } } ] = - [ L _ { x } , L _ { \varepsilon _ { 1 } } ]$ and $[ L _ { x } , L _ { \varepsilon _ { j } } ] = 0$ for $j \geq 3$ ;   
(b) $\begin{array} { r } { D \varepsilon _ { 1 } = \frac { 1 } { 2 } x , } \end{array}$ ;   
(c) $D \varepsilon _ { 2 } = - { \frac { 1 } { 2 } } x ,$ ;   
(d) $D \varepsilon _ { j } = 0$ for $j \geq 3$ ;   
(e) $^ { ( D , x ) }$ is in a root space for g.

Proof Since $x \in V _ { 1 2 } = V _ { \frac { 1 } { 2 } } ( \pmb { \varepsilon } _ { 1 } ) \cap V _ { \frac { 1 } { 2 } } ( \pmb { \varepsilon } _ { 2 } ) \cap \bigcap _ { j \geq 3 } V _ { 0 } ( \pmb { \varepsilon } _ { j } )$ , we see that (b), (c), and (d) are trivial. Clearly (e) follows from (a), (b), (c), and (d). So it remains to prove (a).

Let $f _ { i } ( y ) = x \cdot ( \varepsilon _ { i } \cdot y ) - \varepsilon _ { i } \cdot ( x \cdot y )$ . Then we must check that:

(1) $f _ { 1 } ( y ) + f _ { 2 } ( y ) = 0$ for all $y \in V$ ;   
(2) $f _ { j } ( y ) = 0$ for all $y \in V$ , $j \geq 3$ .

Since each $f _ { i }$ is linear, it suffices to do this for $y \in V _ { r s }$ for various $1 \leq r , s \leq n$ We have several cases.

(i) $y \in V _ { 1 1 } \oplus V _ { 1 2 } \oplus V _ { 2 2 }$ . This is true if and only if $\textstyle y \in \bigcap _ { j \geq 3 } V _ { 0 } ( \varepsilon _ { j } )$ . Since $V _ { 0 } ( \varepsilon ) \cdot V _ { 0 } ( \varepsilon ) \subset V _ { 0 } ( \varepsilon )$ for any idempotent $\varepsilon$ , we see that $x \cdot y \in V _ { 1 1 } \oplus V _ { 1 2 } \oplus$ $V _ { 2 2 }$ . Thus (1) follows since $\varepsilon _ { 1 } + \varepsilon _ { 2 }$ is the identity on $V _ { 1 1 } \oplus V _ { 1 2 } \oplus V _ { 2 2 }$ , and (2) follows since $\varepsilon _ { j }$ is zero on $V _ { 1 1 } \oplus V _ { 1 2 } \oplus V _ { 2 2 }$ if $j \geq 3$ .   
(ii) $y \in V _ { 1 3 }$ . Then $y \in V _ { 0 } ( \varepsilon _ { 2 } ) \cap V _ { \frac { 1 } { 2 } } ( \varepsilon _ { 3 } )$ . Since $V _ { 0 } ( \pmb \varepsilon ) \cdot V _ { \frac { 1 } { 2 } } ( \pmb \varepsilon ) \subset V _ { \frac { 1 } { 2 } } ( \pmb \varepsilon )$ , we have $x \cdot y \in V _ { 2 3 }$ . Then (1) follows since $\begin{array} { r } { \varepsilon _ { 1 } + \varepsilon _ { 2 } = \frac { 1 } { 2 } } \end{array}$ on $V _ { 2 3 } \oplus V _ { 1 3 }$ , and (2) follows since $\varepsilon _ { 3 }$ is $\frac { 1 } { 2 }$ on $V _ { 2 3 } \oplus V _ { 1 3 }$ and $\varepsilon _ { j } = 0$ on $V _ { 2 3 } \oplus V _ { 1 3 }$ for $j \geq 4$ .   
(iii) $y \in V _ { 1 k }$ or $V _ { 2 k }$ for any $k \geq 3$ is similar to (ii).   
(iv) $y \in V _ { j k }$ with $j , k \geq 3$ . Then $x \cdot y = 0$ : if $j = k$ , this follows from $y \in V _ { 1 } ( \varepsilon _ { j } )$ and $x \in V _ { 0 } ( \varepsilon _ { j } )$ ; if $j \neq k$ , this follows from $x \cdot y \in V _ { \frac { 1 } { 2 } } ( \pmb { \varepsilon } _ { 1 } ) \cap V _ { \frac { 1 } { 2 } } ( \pmb { \varepsilon } _ { 2 } ) \cap V _ { \frac { 1 } { 2 } } ( \pmb { \varepsilon } _ { j } ) \cap$ $V _ { \frac { 1 } { 2 } } ( \varepsilon _ { k } )$ . Hence also $x \cdot ( \varepsilon _ { i } \cdot y ) = 0$ , whence (1) and (2).

Summarizing this discussion, we find

$$
{ \mathfrak { g } } = Z ( { \mathfrak { A } } ) \oplus \bigoplus _ { i \neq j } { \mathfrak { g } } _ { i j } ,
$$

where

$$
{ \mathfrak { g } } _ { i j } = \{ ( D , x ) \mid x \in V _ { i j } , D = - 2 [ L _ { x } , L _ { \varepsilon _ { i } } ] \} \ .
$$

Applying the above formulae, one readily checks:

$$
\begin{array} { r l } & { Z ( \mathfrak { A } ) = \left( Z ( \mathfrak { A } ) \cap \mathrm { D e r } V \right) \oplus \left( Z ( \mathfrak { A } ) \cap V \right) } \\ & { \qquad = \left\{ D \in \mathrm { D e r } V \vert D \varepsilon _ { i } = 0 \mathrm { ~ f o r ~ a l l ~ } i \right\} \oplus \bigoplus _ { i = 1 } ^ { n } V _ { i i } , } \end{array}
$$

and that, if we define for $i < j$

then

$$
\begin{array} { c } { { \mathfrak { g } _ { i j } \oplus \mathfrak { g } _ { j i } \cong V _ { i j } \oplus \mathrm { D e r } ( V ) _ { i j } ~ , } } \\ { { \dim \mathfrak { g } _ { i j } = \dim \mathfrak { g } _ { j i } = \dim V _ { i j } = \dim \mathrm { D e r } ( V ) _ { i j } ~ . } } \end{array}
$$

Finally, we study the set of $( i , j )$ such that $V _ { i j } \neq ( 0 )$ .

Proposition 3.13 Let $\gamma _ { i } \in \mathrm { H o m } \left( \sum _ { i = 1 } ^ { n } \mathbb { R } \varepsilon _ { i } , \mathbb { R } \right)$ be the dual basis to $\varepsilon _ { i }$ . Let $V =$ $\Pi _ { \alpha } V _ { \alpha }$ be the decomposition into $k$ -simple Jordan algebras and let $\{ \varepsilon _ { i } \} _ { i \in I _ { \alpha } }$ be the idempotents in $V _ { \alpha }$ . Then:

(i) $V _ { i j } \neq ( 0 )$ if and only if $i \neq j$ and $i , j$ are in the same $I _ { \alpha }$ ; (ii) the $k$ -roots are $\begin{array} { r } { \frac { 1 } { 2 } ( \gamma _ { i } - \gamma _ { j } ) } \end{array}$ , where $i \neq j$ and $i , j$ are in the same $I _ { \alpha }$ ; (iii) the Weyl group is the group of all permutations of the $\left\{ \varepsilon _ { i } \right\}$ preserving the partition $\{ I _ { \alpha } \}$ .

Proof Since every element of the Weyl group is represented by an element of $K$ , it acts on $\mathfrak { A }$ by a Jordan isomorphism, hence it acts by a permutation of the $\varepsilon _ { i }$ . Now if $V _ { i j } \neq ( 0 )$ , then $\begin{array} { r } { \frac { 1 } { 2 } ( \gamma _ { i } - \gamma _ { j } ) } \end{array}$ is a root and the reflection $w _ { i j }$ in the hyperplane $\gamma _ { i } - \gamma _ { j } = 0$ is in the Weyl group. Since $( \gamma _ { i } - \gamma _ { j } ) ( \pmb { \varepsilon } _ { k } ) = 0$ , for $k \neq i , j$ , this reflection must be the permutation fixing $\varepsilon _ { k }$ for $k \neq i , j$ and interchanging $\varepsilon _ { i } , \varepsilon _ { j }$ . Now any subgroup of the permutation group generated by transpositions is the group of all permutations preserving some partition $\{ J _ { \alpha } \}$ . Thus if $V _ { i j } \neq ( 0 )$ , then $w _ { i j }$ lies in the Weyl group and hence $i , j$ are in the same $J _ { \alpha }$ . Conversely, since the $w _ { i j }$ for $i , j$ such that $V _ { i j } \neq ( 0 )$ generate the Weyl group, if $J _ { \alpha }$ has at least two elements, then $V _ { i _ { 0 } , j _ { 0 } } \neq ( 0 )$ for some $i _ { 0 } , j _ { 0 } \in J _ { \alpha }$ . Then for any $i \neq j$ with $i , j \in J _ { \alpha }$ , there exists $\sigma \in \mathrm { N o r m } _ { K } ( \mathfrak { A } )$ such that $\sigma \varepsilon _ { i _ { 0 } } = \varepsilon _ { i }$ , $\sigma \varepsilon _ { j _ { 0 } } = \varepsilon _ { j }$ . Then $V _ { i , j } = \sigma ( V _ { i _ { 0 } , j _ { 0 } } ) \ne ( 0 )$ . Thus $V _ { i j } \neq ( 0 )$ if and only if $i \neq j$ and $i , j$ are in the same $J _ { \alpha }$ . Finally,

$$
V = \prod _ { \alpha } \prod _ { i , j \in J _ { \alpha } } V _ { i j } ,
$$

and $\textstyle \prod _ { i , j \in J _ { \alpha } } V _ { i j }$ is $k$ -simple. Hence $\begin{array} { r } { V _ { \alpha } = \prod _ { i , j \in J _ { \alpha } } V _ { i j } } \end{array}$ and $I _ { \alpha } = J _ { \alpha }$ .

# 3.9

Let $\varepsilon$ be an idempotent in $V$ , and let $C _ { i } = C _ { i } ( \varepsilon )$ , and $V _ { i } = V _ { i } ( \varepsilon )$ for $i = 0 , 1$ . Let $a ( s )$ be the one-parameter subgroup corresponding to $\varepsilon$ . Denoting by $Z ( a )$ the centralizer of $a$ in $G$ , we know that $Z ( a )$ is the Levi subgroup of $\mathrm { N o r m } \left( C _ { 1 } \right)$ , and also the Levi subgroup of $\mathrm { N o r m } \left( C _ { 0 } \right)$ . In fact, $Z ( a ) = \operatorname { N o r m } \left( C _ { 1 } \right) \cap \operatorname { N o r m } \left( C _ { 0 } \right)$ . Setting $G _ { i } = \operatorname { A u t } ( C _ { i } , V _ { i } ) ^ { o }$ for $i = 0 , 1$ , we get a map

$$
\varphi = \mathrm { r e s } _ { V _ { 0 } } \times \mathrm { r e s } _ { V _ { 1 } } : Z ( a ) ^ { o } \longrightarrow G _ { 0 } \times G _ { 1 } \ .
$$

Proposition 3.14 We have a decomposition:

$$
Z ( a ) ^ { o } = G _ { 0 } ^ { \prime } \cdot G _ { 1 } ^ { \prime } \cdot K _ { 0 }
$$

(a direct product, modulo a finite abelian subgroup), where $K _ { 0 } = \ker \varphi$ is compact, res $\varphi : G _ { i } ^ { \prime } \longrightarrow G _ { i }$ is surjective with finite kernel, and

$$
\operatorname { L i e } G _ { i } ^ { \prime } = [ V _ { i } , V _ { i } ] + V _ { i } \subset \operatorname { L i e } G .
$$

If ε is $k$ -rational, then so is this decomposition.

Proof By Section 2, we know that Lie $G = [ V , V ] \oplus V$ . For $i = 0 , 1$ , define the subalgebra $\mathfrak { g } _ { i } ^ { \prime } = [ V _ { i } , V _ { i } ] \oplus V _ { i } \subset \mathrm { L i e } G$ . Now any element of $V _ { i }$ strictly commutes with $\varepsilon$ , so that actually ${ \mathfrak { g } } _ { i } ^ { \prime } \subset \operatorname { L i e } Z ( a )$ . There are restriction maps $\Psi _ { i } : \mathrm { L i e } Z ( a ) \longrightarrow \mathrm { L i e } G _ { i }$ .

We claim that $\Psi _ { i } | _ { \mathfrak { g } _ { i } ^ { \prime } }$ is an isomorphism. We know by Section 2 that Lie $G _ { i } =$ $[ V _ { i } , V _ { i } ] \oplus V _ { i }$ . By definition, $\Psi _ { i }$ is just the identity on $V _ { i }$ and, since it preserves the Lie bracket, it is also the identity on $[ V _ { i } , V _ { i } ]$ , hence the claim is proven.

Let $K _ { 0 } = \operatorname { K e r } \varphi$ , $\mathfrak { k } _ { 0 } = \mathrm { L i e } K _ { 0 }$ . Note that if $g \in K _ { 0 }$ , then $g \varepsilon = \varepsilon$ and $g ( p - \varepsilon ) =$ $p - \varepsilon$ , hence $g p = p$ ; thus $K _ { 0 } \subset K$ and is compact. Now because Lie $Z ( a ) / \mathfrak { k } _ { 0 } \cong$ Lie $G _ { 0 } \times \mathrm { L i e } G _ { 1 } \cong { \mathfrak { g } } _ { 0 } ^ { \prime } \times { \mathfrak { g } } _ { 1 } ^ { \prime }$ , it follows that we get a vector space decomposition:

$$
\mathrm { L i e } Z ( a ) = { \mathfrak { k } } _ { 0 } \oplus { \mathfrak { g } } _ { 0 } ^ { \prime } \oplus { \mathfrak { g } } _ { 1 } ^ { \prime } ~ .
$$

We claim these factors commute.

(i) To show $[ { \mathfrak { g } } _ { 0 } ^ { \prime } , { \mathfrak { g } } _ { 1 } ^ { \prime } ] = ( 0 )$ , it suffices to show $[ V _ { 0 } , V _ { 1 } ] = ( 0 )$ , but this just says that $V _ { 0 } , V _ { 1 }$ strongly commute, which was shown in Section 2.

(ii) To show $[ \pmb { \mathfrak { k } } _ { 0 } , \pmb { \mathfrak { g } } _ { i } ^ { \prime } ] = ( 0 )$ , it suffices to show $[ \mathfrak { k } _ { 0 } , V _ { i } ] = ( 0 )$ . But $\mathfrak { k } _ { 0 } = \mathrm { K e r } \left( \mathrm { d } \varphi \right)$ is an ideal so $[ \mathfrak { k } _ { 0 } , V _ { i } ] \subset \mathfrak { k } _ { 0 }$ ; while $[ { \mathfrak { k } } , { \mathfrak { p } } ] \subset { \mathfrak { p } }$ implies $[ \mathfrak { k } _ { 0 } , V _ { i } ] \subset \mathfrak { p }$ .

Corollary $3 . 1 5 \mathrm { r e s } _ { V _ { 0 } } : Z ( a ) ^ { o } \longrightarrow G _ { 0 }$ is surjective.

Corollary $3 . 1 6 \mathrm { k e r } ( \mathrm { r e s } _ { V _ { 0 } } | _ { Z ( a ) ^ { o } } ) ^ { o } = G _ { 1 } ^ { \prime } \cdot K _ { 0 } .$

# 3.10

In this subsection, we assume $G$ is $k$ -simple. Let $n$ be the $k$ -rank of $G$ and let $\varepsilon _ { 1 } , \ldots , \varepsilon _ { n }$ be a maximal set of mutually orthogonal $k$ -idempotents. Call $a _ { j } ( s )$ the one-parameter subgroup corresponding to the idempotent $f _ { j } = \pmb { \varepsilon } _ { 1 } + \cdots + \pmb { \varepsilon } _ { j }$ . Note that $a _ { j } ( 0 )$ , defined as $\operatorname* { l i m } _ { s \to 0 } a _ { j } ( s )$ , exists in $\operatorname { E n d } ( V )$ .

Lemma 3.17 $V _ { 0 } ( f _ { j + 1 } ) \subsetneq V _ { 0 } ( f _ { j } )$ .

Proof Pick any $x \in V _ { 0 } ( f _ { j + 1 } )$ . Then $0 = f _ { j + 1 } \cdot x = f _ { j } \cdot x + \pmb { \varepsilon } _ { j + 1 } \cdot x .$ . But $\varepsilon _ { j + 1 } \in$ $V _ { 1 } ( f _ { j + 1 } )$ so $\varepsilon _ { j + 1 } \cdot x = 0$ . Thus $x \in V _ { 0 } ( f _ { j } )$ . Meanwhile $\pmb { \varepsilon } _ { j + 1 } \in V _ { 0 } ( f _ { j } ) \setminus V _ { 0 } ( f _ { j + 1 } )$ .

Thus if we write $C _ { j } = C _ { 0 } ( f _ { j } ) = a _ { j } ( 0 ) C$ , we have

$$
0 = \overline { { C } } _ { n } \subsetneq \overline { { C } } _ { n - 1 } \subsetneq \overline { { C } } _ { n - 2 } \subsetneq \cdots \subsetneq \overline { { C } } _ { 1 } \subsetneq \overline { { C } } _ { 0 } = \overline { { C } } .
$$

We call this a flag of $k$ -boundary components. If we fix $\varepsilon _ { 1 } , \ldots , \varepsilon _ { n }$ once and for all, we call it the standard flag, and its members the standard rational boundary components.

Let $A$ be the maximal $k$ -split torus with Lie $\textstyle A = \sum _ { i = 1 } ^ { n } \mathbb { R } \varepsilon _ { i }$

Proposition 3.18 If $b ( s )$ is any $k$ -split one-parameter subgroup in $G$ such that $b ( 0 ) = \operatorname* { l i m } _ { s \longrightarrow 0 } b ( s )$ exists in $\operatorname { E n d } ( V )$ and is non-zero, then $b ( 0 ) C$ is the image by some $g \in G ( k )$ of a standard rational boundary component. In particular, it is a boundary component.

Proof By conjugating by some $g \in G ( k )$ we may assume that $b ( s )$ is a oneparameter subgroup of $A$ . We may always replace $b$ by $b ^ { n }$ for some positive integer $n$ , since $b ( 0 )$ does not change. From the explicit description of the root structure in Section 3.8, it is easy to check that $\{ a _ { 1 } ^ { m _ { 1 } } a _ { 2 } ^ { m _ { 2 } } \cdot \cdot \cdot a _ { n } ^ { m _ { n } } \mid m _ { i } \geq 0$ for $i =$ $1 , \ldots , n - 1 \big \}$ is a $k$ -Weyl chamber in $A$ . Thus conjugating with some $n \in N ( k )$ , where $N$ is the normalizer of $A$ , we may assume $\begin{array} { r } { b ( s ) = \prod _ { i = 1 } ^ { n } a _ { i } ^ { m _ { i } } ( s ) } \end{array}$ with $m _ { i } \geq 0$ for $i = 1 , \ldots , n - 1 .$ Note that $b ( s ) \pmb { \varepsilon } _ { n } = s ^ { 2 m _ { n } } \pmb { \varepsilon } _ { n }$ . Since $b ( 0 )$ exists, it follows that $m _ { n } \geq 0$ as well. Recall that $a _ { i } ( 0 )$ is the orthogonal projection onto $V _ { 0 } ( f _ { i } )$ and that

$$
0 = V _ { 0 } ( f _ { n } ) \subsetneq V _ { 0 } ( f _ { n - 1 } ) \subsetneq V _ { 0 } ( f _ { n - 2 } ) \subsetneq \cdots \subsetneq V _ { 0 } ( f _ { 1 } ) \subsetneq V \ .
$$

Then $a _ { 1 } ^ { m _ { 1 } } \cdot \cdot \cdot a _ { n } ^ { m _ { n } } ( 0 ) C = C _ { j }$ , where $m _ { j + 1 } = \cdot \cdot \cdot = m _ { n } = 0$ and $m _ { j } > 0$

Note that $b ( 0 ) C$ is always a boundary component, even if $G$ is not $k$ -simple.

Every $k$ -boundary component is the translate of a standard one. If the standard flag were a subflag of some larger flag of $k$ -rational boundary components, any non-standard boundary component would have the same dimension as a standard one and thus be equal to it. So, the standard flag is a maximal flag of $k$ -rational boundary components.

Proposition 3.19 Any flag $\mathfrak { F }$ of $k$ -rational boundary components is the image by some $g \in G ( k )$ of some subflag of the standard flag.

Proof The proof is similar to that of the previous proposition. Let

$$
V _ { s } \subsetneq V _ { s - 1 } \subsetneq \cdots \subsetneq V _ { 1 } \subsetneq V
$$

be the flag of $k$ -boundary components in question. Let $d _ { i }$ be the Jordan identity in $V _ { i }$ . Then $E = \{ p - d _ { 1 } , d _ { 1 } - d _ { 2 } , \ldots , d _ { s - 1 } - d _ { s } , d _ { s } \}$ is a set of mutually orthogonal $k$ -idempotents, and they generate an associative sub Jordan algebra. The corresponding torus $B$ is $k$ -split. So, after conjugating by an element $g \in G ( k )$ , we may assume that $B \subset A$ .

Now, $\operatorname { L i e } A = \textstyle \sum _ { i = 1 } ^ { n } \mathbb { R } \varepsilon _ { i }$ and Lie $B \subset \operatorname { L i e } A$ . Therefore,

$$
E = \left\{ \varepsilon _ { 1 1 } + \dots + \varepsilon _ { 1 j _ { 1 } } , \dots , \varepsilon _ { s 1 } + \dots + \varepsilon _ { s j _ { s } } \right\} .
$$

Since the Weyl group acting on $\{ \varepsilon _ { 1 } , \ldots , \varepsilon _ { n } \}$ is the full group of permutations, after conjugating by some $n \in N ( k )$ we may assume that $d _ { i } = f _ { \varphi ( i ) }$ for some increasing map $\varphi : \{ 1 , \ldots , s \} \longrightarrow \{ 1 , \ldots , n - 1 \}$ . (Here, again, $N$ is the normalizer of $A$ .)

However, $f _ { \varphi ( i ) }$ is the projection onto the $\varphi ( i )$ ’th member of the standard flag. Since the idempotent determines the boundary component, we now have our flag as a subflag of the standard flag.

Proposition 3.20 There is a bijection between the set of flags $\mathfrak { F }$ of $k$ -boundary components and $k$ -parabolics $P \subset G$ given by $\begin{array} { r } { \Phi : \mathfrak { F } \longrightarrow \bigcap _ { C _ { a } \in \mathfrak { F } } \mathrm { N o r m } \left( C _ { a } \right) } \end{array}$ .

Proof From the root structure, we see easily that the minimal $k$ -parabolic corresponding to the set of simple roots $\{ \frac 1 2 ( \gamma _ { i } - \gamma _ { i + 1 } ) | i = 1 , \ldots , n - 1 \}$ normalizes the standard flag. Thus $\cap _ { C _ { a } \in \mathfrak { F } } \mathrm { N o r m } \left( C _ { a } \right)$ actually is a $k$ -parabolic for any flag $\mathfrak { F }$ , by use of the preceding corollary.

Define a standard $k$ -parabolic to be one of the form $\Phi ( \mathfrak { F } )$ , where $\mathfrak { F }$ is a subflag of the standard flag. Then $\mathrm { N o r m } \left( C _ { i } \right)$ for standard $C _ { i }$ , $i = 1 , \ldots , n - 1$ , are the maximal standard $k$ -parabolics. The fact that any $k$ -parabolic is conjugate via some $g \in G ( k )$ to an intersection of maximal standard ones implies that $\Phi$ is surjective.

We show now that $\Phi$ is injective. Since any $k$ -parabolic is uniquely the intersection of maximal $k$ -parabolics, it suffices to show that, for any two $k$ - boundary components, $C _ { a }$ and $C _ { a ^ { \prime } }$ ,

$$
\mathrm { N o r m } \left( C _ { a } \right) = \mathrm { N o r m } \left( C _ { a ^ { \prime } } \right) \Longrightarrow C _ { a } = C _ { a ^ { \prime } } .
$$

By Proposition 3.18, there exist $g , g ^ { \prime } \in G ( k )$ and standard $k$ -boundary components $C _ { i } , C _ { j }$ such that $g C _ { i } = C _ { a }$ and $g ^ { \prime } C _ { j } = C _ { a ^ { \prime } }$ . Therefore,

$$
g \mathrm { N o r m } \left( C _ { i } \right) g ^ { - 1 } = \mathrm { N o r m } \left( C _ { a } \right) = \mathrm { N o r m } \left( C _ { a ^ { \prime } } \right) = g ^ { \prime } \mathrm { N o r m } \left( C _ { j } \right) g ^ { \prime - 1 } \ .
$$

So we get

$$
g ^ { \prime - 1 } g \mathrm { N o r m } ( C _ { i } ) ( g ^ { \prime - 1 } g ) ^ { - 1 } = \mathrm { N o r m } ( C _ { j } ) \ .
$$

However, the standard $k$ -parabolics are not conjugate to each other, so $i =$ $j$ . Then, since the normalizer of any parabolic is equal to itself, we get that $g ^ { \prime - 1 } g \in \operatorname { N o r m } \left( C _ { i } \right)$ . Thus

$$
C _ { a ^ { \prime } } = g ^ { \prime } C _ { i } = g ^ { \prime } ( g ^ { \prime - 1 } g ) C _ { i } = g C _ { i } = C _ { a } \ .
$$

Corollary 3.21 A set of $k$ -parabolics intersect in a $k$ -parabolic if and only if their corresponding boundary components can be arranged into a flag.

Corollary 3.22 A real boundary component $C ^ { \prime }$ of $C$ is $k$ -rational if and only if $\operatorname { N o r m } ( C ^ { \prime } )$ is $k$ -rational.

Proof Combine the theorem over $k$ and the theorem over $\mathbb { R }$ .

Lemma 3.23 A is generated by $a _ { 1 } ( s ) , \ldots , a _ { n } ( s )$ .

Proof $a _ { i } ( s ) = \exp \ b { t } ( \pmb { \varepsilon } _ { 1 } + \cdots + \pmb { \varepsilon } _ { i } )$ where $s = \mathbf { e } ^ { { \frac { 1 } { 2 } } t }$ , so $a _ { 1 } , \ldots , a _ { n }$ generate a torus with Lie algebra  $\scriptstyle \sum _ { i = 1 } ^ { n } \mathbb { R } \varepsilon _ { i }$ . 

What is the orbit $A p \subset C ?$ We compute: for any $q \in V$ , which strongly commutes with the $\varepsilon _ { i }$ ,

$$
\begin{array} { c } { { \exp \left( \sum t _ { j } \varepsilon _ { j } \right) q = \big ( \prod \exp t _ { j } \varepsilon _ { j } \big ) q = \displaystyle \sum ( \exp t _ { j } ) \varepsilon _ { j } q - \sum \varepsilon _ { j } q + q } } \\ { { = \sum ( \exp t _ { j } ) \varepsilon _ { j } q ~ . } } \end{array}
$$

Here we used $\pmb { \varepsilon } _ { i } \cdot \pmb { \varepsilon } _ { j } = \delta _ { i j } \pmb { \varepsilon } _ { i } , \pmb { \Sigma } \pmb { \varepsilon } _ { j } = p$ and

$$
\exp t \varepsilon = 1 + t \varepsilon + { \frac { t ^ { 2 } } { 2 } } \varepsilon + \cdots = \mathrm { e } ^ { t } \varepsilon - \varepsilon + 1 \ .
$$

We are thinking of elements $\pi$ of $V \cong { \mathfrak { p } }$ as being in $\operatorname { E n d } ( V )$ . Thus

$$
\exp \Big ( \sum t _ { i } \varepsilon _ { i } \Big ) p = \sum ( \exp t _ { i } \Big ) \varepsilon _ { i } p = \sum ( \exp t _ { i } \Big ) \varepsilon _ { i } .
$$

Hence:

Proposition 3.24 The orbit of A is “linear,” namely, $\begin{array} { r } { A p = \sum _ { i = 1 } ^ { n } \mathbb { R } _ { > 0 } \pmb { \mathscr { E } } _ { i } } \end{array}$ .

We may use $\varepsilon _ { 1 } , \ldots , \varepsilon _ { n }$ as orthogonal coordinates in ⎪⎪ 7 $A p$ , since $\langle \varepsilon _ { i } , \varepsilon _ { j } \rangle =$ $\mathrm { T r } L _ { \varepsilon _ { i } \cdot \varepsilon _ { j } } = 0$ if $i \neq j$ .

Now $\textstyle { \frac { 1 } { 2 } } a _ { j } ^ { \prime } ( 1 ) = \varepsilon _ { 1 } + \cdots + \varepsilon _ { j }$ and

$$
a _ { j } ( s ) = \left( \begin{array} { c c c c c } { { } } & { { | } } & { { | } } & { { } } & { { } } \\ { { s ^ { 2 } } } & { { | } } & { { | } } & { { } } & { { } } \\ { { - - + - + - { \bf \sigma } | } } & { { } } & { { } } & { { } } \\ { { | } } & { { s } } & { { | } } & { { } } & { { } } \\ { { - - + - + - { \bf \sigma } | - - } } & { { } } & { { } } & { { } } \\ { { | } } & { { | } } & { { | } } & { { | } } & { { | } } \\ { { } } & { { | } } & { { | } } & { { } } & { { } } \end{array} \right) \quad V _ { 1 } ( f _ { j } ) \quad .
$$

Clearly, $\pmb { \mathscr { E } } _ { k } \in V _ { 0 } ( f _ { j } )$ if $k > j$ and $\pmb { \mathscr { E } } _ { k } \in V _ { 1 } ( f _ { j } )$ if $k \leq j$ . Thus

$$
a _ { j } ( s ) \varepsilon _ { k } = { \left\{ \begin{array} { l l } { \varepsilon _ { k } } & { { \mathrm { i f ~ } } k > j } \\ { s ^ { 2 } \varepsilon _ { k } } & { { \mathrm { i f ~ } } k \leq j { \mathrm { ~ . ~ } } } \end{array} \right. }
$$

# 4 Siegel sets in self-adjoint cones

# 4.1

First we recall the general theory of Siegel sets. Let $\mathcal { G }$ be a reductive algebraic group defined over $\mathbb { Q }$ and $G = \mathcal { G } ( \mathbb { R } ) ^ { o }$ and let $X$ be the associated non-compact symmetric space (i.e., the homogeneous space $G / K$ , for a maximal compact subgroup $K \subset G$ ). For every parabolic subgroup $\mathcal { P } \subset \mathcal { G }$ defined over $\mathbb { Q }$ and minimal among such subgroups (“minimal $\mathbb { Q }$ -parabolic” for short), we wish to define a class of subsets ${ \mathfrak { S } } \subset X$ called the Siegel sets associated to $P = \mathcal { P } ( \mathbb { R } ) ^ { o }$ .

Definition 4.1 Choose a basepoint $p \in X$ . Let $A \subset P$ be the unique torus that is a conjugate of the maximal $\mathbb { Q }$ -split torus of $P$ and such that Lie A $\bot \operatorname { L i e } \left( \operatorname { S t a b } p \right)$ (cf. Lemma 3.12). Let $\Delta \subset \operatorname { H o m } \left( A , \mathbb { G } _ { m } \right)$ be the simple positive roots (i.e., the minimal roots in the adjoint action of $A$ on Lie $\mathcal { P }$ ); let $A ^ { + } = \{ g \in A \mid \beta ( g ) \geq$ 1 for all $\beta \in \Delta \}$ . Then the Siegel sets are the subsets of $X$ of the form

$$
\mathfrak { S } _ { \omega } = \omega A ^ { + } p ,
$$

where $\omega \subset P = \mathcal { P } ( \mathbb { R } ) ^ { o }$ is a compact subset.

We make three remarks. First of all, this definition does not depend on the choice of $p$ . In fact, let $p , p ^ { \prime }$ be two basepoints, let $K = \operatorname { S t a b } \left( p \right)$ . Since $G = P \cdot K ,$ , $P$ acts transitively on $X$ and so we may write $p ^ { \prime } = g p$ for some $g \in P$ . Let $A , A ^ { \prime } \subset P$ be the tori corresponding to $p , p ^ { \prime }$ . Then $A ^ { \prime } = g A g ^ { - 1 }$ ; hence, for all $\omega \subset P$ compact,

$$
\mathfrak { S } _ { \omega } ^ { \prime } = \omega ( A ^ { \prime } ) ^ { + } p ^ { \prime } = \omega ( g A ^ { + } g ^ { - 1 } ) ( g p ) = \mathfrak { S } _ { \omega g } .
$$

Secondly, this definition is slightly different from the usual one (see [3], pp. 85ff.). However, we claim that all “usual” Siegel sets are Siegel sets as above, and each of the above is contained in a usual Siegel set. In all applications, it is not the exact shape of the Siegel sets that is important, but rather the way they grow. To be precise, any class of subsets $\{ X _ { \alpha } \}$ cofinal with Siegel sets in the sense:

(i) for all $\alpha$ , there exists $\omega$ such that $X _ { \alpha } \subset \mathfrak { S } _ { \omega }$ ; (ii) for all $\omega$ , there exists $\alpha$ such that ${ \mathfrak { S } } _ { \omega } \subset X _ { \alpha }$ ,

would do just as well.

In our case, the “usual” Siegel sets are defined by decomposing $\mathrm { \bf P }$ into

$$
P = M A N ,
$$

where $N$ is the unipotent radical of $P , A$ is some maximal $\mathbb { Q }$ -split torus in $P$ , and $M$ is the anisotropic part of $Z ( A )$ , and by choosing $p$ such that $\mathbf { L i e } \left( \mathbf { S t a b } { p } \right) \perp$ Lie A. Then one takes the set $\mathfrak { S } _ { \omega , t } ^ { * } = \omega A _ { t } p$ , where $\omega \subset M N$ is compact and $A _ { t } = \{ g \in A \mid \beta ( g ) \geq t$ for all $\beta \in \Delta \}$ . But if $a _ { t } \in A$ satisfies $\beta ( a _ { t } ) = t$ for all $\beta \in \Delta$ , then

$$
\mathfrak { S } _ { \omega , t } ^ { * } = \mathfrak { S } _ { \omega a _ { t } } \ .
$$

In the other direction, if $\omega \subset P$ is compact, then $\omega \subset \omega _ { 1 } \cdot \omega _ { 2 }$ , where $\omega _ { 1 } \subset M N$ and $\omega _ { 2 } \subset A$ are compact. Let

$$
t = \operatorname* { i n f } _ { \beta \in \Delta \atop g \in \omega _ { 2 } } \beta ( g ) ;
$$

then

$$
\mathfrak { S } _ { \omega } \subset \mathfrak { S } _ { \omega _ { 1 } , t } ^ { * } \ .
$$

The third remark is that if $G$ is not $\mathbb { Q }$ -simple, but rather $G = G _ { 1 } \times \cdots \times G _ { k }$ over $\mathbb { Q }$ , then all our sets decompose:

$$
\begin{array} { c } { { X = X _ { 1 } \times \cdots \times X _ { k } ~ , } } \\ { { { } } } \\ { { P = P _ { 1 } \times \cdots \times P _ { k } ~ , } } \\ { { { } } } \\ { { A = A _ { 1 } \times \cdots \times A _ { k } ~ , } } \\ { { { } } } \\ { { A ^ { + } = A _ { 1 } ^ { + } \times \cdots \times A _ { k } ^ { + } ~ . } } \end{array}
$$

So, among all Siegel sets, those with $\omega = \omega _ { 1 } \times \cdot \cdot \cdot \times \omega _ { k }$ are cofinal and these decompose as

$$
\mathfrak { S } _ { \omega } = \mathfrak { S } _ { \omega _ { 1 } } \times \cdots \times \mathfrak { S } _ { \omega _ { k } } .
$$

The virtue of Siegel sets lies in the following two fundamental results of reduction theory. Let $\Gamma \subset G ( \mathbb { Q } )$ be an arithmetic subgroup. Then:

(i) there exist $\omega \subset P$ compact and a finite set $F \subset G ( \mathbb { Q } )$ such that

$$
X = \Gamma \cdot F \cdot \mathfrak { S } _ { \omega } ;
$$

(ii) for all ω compact and all $g _ { 1 } , g _ { 2 } \in G ( \mathbb { Q } )$ , the set

$$
\{ \gamma \in \Gamma | g _ { 1 } \mathfrak { S } _ { \omega } \cap \gamma g _ { 2 } \mathfrak { S } _ { \omega } \neq \emptyset \}
$$

is finite.

# 4.2

Now return to the case of cones: let $G = \operatorname { A u t } ( C , V ) ^ { o }$ , where $C$ is a homogeneous self-adjoint cone, and suppose $V$ and $G$ are defined over $\mathbb { Q }$ . Choose a rational basepoint $p$ , let $K = \mathop { \mathrm { S t a b } } \left( p \right)$ , so that $V$ is a Jordan algebra, and choose a maximal $\mathbb { Q }$ -split torus $A$ perpendicular to $K$ . We also assume that $G$ is $\mathbb { Q }$ - simple. Let $\mathfrak { A } = \mathrm { L i e } A$ , $\mathfrak { A } = \textstyle \sum \mathbb { R } \varepsilon _ { i }$ , where $\pmb { \varepsilon } _ { 1 } + \cdots + \pmb { \varepsilon } _ { n } = p$ as in Section 3. Let $C _ { i }$ be the boundary component containing $p _ { i } = \pmb { \varepsilon } _ { i + 1 } + \cdots + \pmb { \varepsilon } _ { n }$ so that

$$
\mathfrak { F } = \left\{ \overline { { C } } \supset \overline { { C } } _ { 1 } \supset \cdots \supset \overline { { C } } _ { n - 1 } \right\}
$$

is a maximal flag of $\mathbb { Q }$ -rational boundary components corresponding to a minimal $\mathbb { Q }$ -parabolic $P$ containing $A$ . Let

$$
a _ { i } ( \mathrm { e } ^ { \frac { 1 } { 2 } t } ) = \exp ( t ( \varepsilon _ { 1 } + \cdot \cdot \cdot + \varepsilon _ { i } ) )
$$

be the one-parameter subgroup such that $a _ { i } ( 0 ) C = C _ { i }$ and

$$
a _ { i } ( s ) \pmb { \varepsilon } _ { j } = \left\{ \begin{array} { l l } { \pmb { \varepsilon } _ { j } } & { \mathrm { i f } \ j > i } \\ { s \pmb { \varepsilon } _ { j } } & { \mathrm { i f } \ j \leq i . } \end{array} \right.
$$

Let

$$
\widetilde { C } = C \cup C _ { 1 } \cup C _ { 2 } \cup \cdots \cup C _ { n - 1 } \cup \left\{ 0 \right\} .
$$

From our explicit description of the root structure, we see that the set $\Delta$ of simple roots consists in our case of $\beta _ { 1 } , \ldots , \beta _ { n - 1 }$ , where on the Lie algebra level

$$
\mathrm { d } \beta _ { j } ( \varepsilon _ { i } ) = { \left\{ \begin{array} { l l } { - { \frac { 1 } { 2 } } } & { { \mathrm { i f ~ } } i = j } \\ { { \frac { 1 } { 2 } } } & { { \mathrm { i f ~ } } i = j + 1 } \\ { 0 } & { { \mathrm { o t h e r w i s e ~ } } . } \end{array} \right. }
$$

Since $\textstyle { \frac { 1 } { 2 } } a _ { i } ^ { \prime } ( 1 ) = \varepsilon _ { 1 } + \cdots + \varepsilon _ { i }$ , it is easy to see that

$$
\beta _ { j } ( a _ { i } ( s ) ) = s ^ { - \delta _ { i j } } .
$$

Lemma $4 . 2 \overline { { A ^ { + } p } }$ is the closed polyhedral cone $D ^ { + }$ generated by the points $p$ , and $p _ { 1 } , \ldots , p _ { n - 1 }$ .

![](images/9749d370d11811e70856967a3022944cac6288cb49a2604aaf5fc1edbe7569e3.jpg)

Proof Since $\beta _ { i } ( a _ { j } ( s ) ) = s ^ { - \delta _ { i j } }$ , we have

$$
A ^ { + } = \left\{ a _ { 1 } ( s _ { 1 } ) \cdots a _ { n } ( s _ { n } ) \mid s _ { i } \leq 1 { \mathrm { ~ f o r ~ } } i = 1 , \ldots , n - 1 \right\} .
$$

Therefore $A ^ { + } p$ is the set of points

$$
( s _ { 1 } \cdots s _ { n } ) ^ { 2 } \pmb { \varepsilon } _ { 1 } + ( s _ { 2 } \cdots s _ { n } ) ^ { 2 } \pmb { \varepsilon } _ { 2 } + \cdots + s _ { n } ^ { 2 } \pmb { \varepsilon } _ { n } \ ,
$$

with $0 < s _ { i } \le 1$ for $i = 1 , \ldots , n - 1$ and $0 < s _ { n }$ . Moreover, $\overline { { A ^ { + } p } }$ is the set of such points where now $0 \leq s _ { i } \leq 1$ for $i = 1 , \ldots , n - 1$ and $0 \leq s _ { n }$ . The lemma follows easily.

# Corollary $4 . 3 \ : \overline { { { \mathfrak { S } } } } _ { \omega } \subset \widetilde { C } .$

Proof Note that $\omega \subset P$ , hence $\omega$ fixes ${ \widetilde { C } } .$ .

We want to know how the Siegel sets look in the boundary components. By induction, it will be apparent that it suffices to do this for the largest boundary

component, $C _ { 1 }$ . Let $p _ { 1 } = p - \varepsilon _ { 1 } = \varepsilon _ { 2 } + \cdot \cdot \cdot + \varepsilon _ { n }$ be the basepoint in $C _ { 1 }$ and write $G _ { 1 } = \mathrm { A u t } ( C _ { 1 } , V _ { 1 } ) ^ { o }$ . Let $\psi : { \cal P } ( a _ { 1 } ) \longrightarrow { \cal G } _ { 1 }$ be the restriction map. We know $\begin{array} { r } { \psi ( A ) p _ { 1 } = \sum _ { k = 2 } ^ { n } \mathbb { R } _ { > 0 } \pmb { \mathscr { E } } _ { k } } \end{array}$ .

We know that $P$ is the normalizer of the standard flag, and $P$ is a minimal $\mathbb { Q }$ -parabolic in $G$ . Let $P _ { 1 }$ be the normalizer of the inherited standard flag in $C _ { 1 }$ .

By Proposition 3.14, we also have a subgroup $G _ { 1 } ^ { \prime } \subset Z ( a _ { 1 } ) \subset P ( a _ { 1 } )$ , where $\psi ^ { \prime } = \psi | _ { G _ { 1 } ^ { \prime } }$ is an isogeny onto $G _ { 1 }$ . Let

$$
P _ { 1 } ^ { \prime } = \psi ^ { \prime - 1 } ( P _ { 1 } ) = \{ g \in G _ { 1 } ^ { \prime } \mid \psi ( g ) \mathrm { { n o r m a l i z e s } } C _ { 1 } , . . . , C _ { n - 1 } \} = P \cap G _ { 1 } ^ { \prime } .
$$

Proposition 4.4 For any $g \in G _ { 1 }$ , there exists $g ^ { \prime } \in Z ( a _ { 1 } )$ such that $\psi ( g ^ { \prime } ) = g$ and $g ^ { \prime } \varepsilon _ { 1 } = \varepsilon _ { 1 }$ . If $g \in P _ { 1 }$ , we may take $g ^ { \prime }$ to be in $P$

Proof This follows from the above discussion and from the fact that $G _ { 1 } ^ { \prime }$ is in the kernel of the restriction of $Z ( a _ { 1 } )$ to $V _ { 1 } ( \varepsilon _ { 1 } )$ .

Proposition 4.5 For any Siegel set ${ \mathfrak { S } } _ { \omega }$ , we have

$$
\overline { { \mathfrak { S } } } _ { \omega } \cap \overline { { C _ { 1 } } } = \overline { { \mathfrak { S } } } _ { \psi ( \omega ) } \ .
$$

Proof We simply compute:

$$
\begin{array} { r l } & { \overline { { \mathfrak { S } } } _ { \omega } \cap \overline { { C _ { 1 } } } = \overline { { \omega A ^ { + } p } } \cap \overline { { C _ { 1 } } } } \\ & { \qquad = \omega \overline { { A ^ { + } p } } \cap \overline { { C _ { 1 } } } \ \mathrm { ( s i n c e ~ } \omega \mathrm { ~ i s ~ c o m p a c t ) } } \\ & { \qquad = \omega \big ( \overline { { A ^ { + } p } } \cap \overline { { C _ { 1 } } } \big ) \ \big ( \mathrm { s i n c e ~ } \omega \mathrm { ~ n o r m a l i z e s } \overline { { C _ { 1 } } } \big ) } \\ & { \qquad = \psi \big ( \omega \big ) \overline { { A _ { 1 } ^ { + } p _ { 1 } } } \ \big ( \mathrm { b y ~ L e m m a ~ 4 . 2 } \big ) } \\ & { \qquad = \overline { { \psi \big ( \omega \big ) A _ { 1 } ^ { + } p _ { 1 } } } \ \big ( \mathrm { s i n c e ~ } \psi \big ( \omega \big ) \mathrm { ~ i s ~ c o m p a c t } \big ) } \\ & { \qquad = \overline { { \mathfrak { S } } } _ { \psi \left( \omega \right) } . } \end{array}
$$

# 4.3

We now compare Siegel sets with polyhedral cones. First of all, by a polyhedral cone $\pi \subset V$ we mean a closed set defined equivalently as

$$
\{ x \in V \mid \ell _ { i } ( x ) \geq 0 { \mathrm { ~ f o r ~ a l l ~ } } i = 1 , \ldots , k \}
$$

for some finite set of linear functions $\ell _ { i }$ , or as

$$
\left\{ \sum _ { i = 1 } ^ { k } \lambda _ { i } y _ { i } \in V \mid \lambda _ { i } \geq 0 \right\} ,
$$

for some finite set of vectors $y _ { i } \in V$ . A word of caution: by the conventions we have been forced into

a polyhedral cone is, by definition, closed;   
a homogeneous self-adjoint cone is, by definition, open.

Hopefully there are only a few places where this might cause confusion. A polyhedral cone is called $\mathbb { Q }$ -rational if one can choose the $\ell _ { i }$ (or the $y _ { i }$ ) to be $\mathbb { Q }$ -rational.

We assume, as above, that $V$ is defined over $\mathbb { Q }$ , and that $C$ is a homogeneous self-adjoint cone in $V$ , and that $G = \operatorname { A u t } ( C , V ) ^ { o }$ is defined over $\mathbb { Q }$ and is $\mathbb { Q }$ - simple. Let $P \subset G$ be a minimal $\mathbb { Q }$ -parabolic, let $\mathfrak { F } = \{ \overline { { C } } \supset \overline { { C } } _ { 1 } \supset \cdots \supset \overline { { C } } _ { n - 1 } \}$ be the associated flag, and let $\widetilde { C } = C \cup C _ { 1 } \cup \cdots \cup C _ { n - 1 } \cup \{ 0 \}$ . Finally, let $D ^ { + } = \overline { { A ^ { + } p } }$ .

The main result will be as follows.

Theorem 4.6 The closures of the Siegel sets $\overline { { \mathfrak { S } } } _ { \omega } i n \overline { { C } }$ and the polyhedral cones $\pi \subset \widetilde { C }$ are cofinal, i.e., every $\overline { { \mathfrak { S } } } _ { \omega }$ is contained in some $\pi$ and every $\pi$ is contained in some $\overline { { \mathfrak { S } } } _ { \omega }$ .

Proof To prove that every Siegel set is in a polyhedral cone is easy. Start with $\omega D ^ { + }$ with $\omega \subset P$ compact. Then, for $i = 1 , \ldots , n - 1$ , let $\pi _ { i }$ be a polyhedral cone generated by a finite set of elements of $C _ { i }$ such that $\omega p _ { i } \subset \pi _ { i }$ , and let $\pi _ { 0 }$ be a polyhedral cone generated by elements of  ) \* $C$ such that  $\omega p \subset \pi _ { 0 }$ . (This exists because $\omega p _ { i }$ is a compact subset of $C _ { i }$ .)

Then (writing $p _ { 0 }$ for  $p$ for simplicity of notation)

$$
\begin{array} { l } { { \omega D ^ { + } = \left\{ b \left( \displaystyle \sum _ { i = 0 } ^ { n - 1 } \lambda _ { i } p _ { i } \right) \mid \lambda _ { i } \geq 0 , b \in \omega \right\} } } \\ { { \mathrm { } } } \\ { { \mathrm { } \qquad \subset \left\{ \displaystyle \sum _ { i = 0 } ^ { n - 1 } \lambda _ { i } ( b _ { i } p _ { i } ) \mid \lambda _ { i } \geq 0 , b _ { i } \in \omega \right\} } } \\ { { \mathrm { } } } \\ { { \mathrm { } \qquad \subset \left\{ \displaystyle \sum _ { i = 0 } ^ { n - 1 } q _ { i } \mid q _ { i } \in \pi _ { i } \right\} = \pi _ { 0 } + \pi _ { 1 } + \cdots + \pi _ { n - 1 } , } } \end{array}
$$

as asserted.

The other inclusion is harder: as it stands, it is not well adapted to proof by induction and, instead, we prove by induction the following stronger fact.

Proposition 4.7 For every polyhedral cone $\pi \subset { \widetilde { C } } ,$ , there is a compact set $\omega \subset P$ such that

$$
p + \pi \subset \omega ( p + D ^ { + } ) .
$$

Multiplying both sides by homotheties $\mathbb { R } _ { > 0 }$ , it follows that $\pi \subset \omega D ^ { + }$ as asserted.

Proof (of Proposition 4.7) We proceed by induction on $\mathrm { d i m } C$ . Separating the generators of the $\pi$ into those in $C$ and those in $\widetilde { C } _ { 1 } = C _ { 1 } \cup C _ { 2 } \cup \cdots \cup C _ { n - 1 } \cup \{ 0 \}$ , we write $\pi = \pi _ { 0 } + \pi _ { 1 }$ , where $\pi _ { 0 } \subset C$ , $\pi _ { 1 } \subset \widetilde { C } _ { 1 }$ . Let $\mathbb { R } ^ { \geq 1 }$ be the reals $[ 1 , \infty )$ . We claim that, for suitably large $\omega$ ,

$$
p + \pi _ { 0 } \subset \mathbb { R } ^ { \geq 1 } { \omega } p .
$$

Let $H$ be the hyperplane of points of the form $p + q$ , where $\langle p , q \rangle = 0$ . Then $\pi _ { 0 } \cap H$ is compact and, if $\pi _ { 0 } \cap H \subset \omega p$ , it follows that $p + \pi _ { 0 } \subset \mathbb { R } ^ { \geq 1 } ( \pi _ { 0 } \cap H ) \subset$ $\mathbb { R } ^ { \geq 1 } \omega p$ :

![](images/551a7c5d60f8952a6ebe635075448e66b930d28bc9925943af208e919f5f0cb6.jpg)

shaded area is $\mathbb { R } ^ { \geq 1 } \cdot ( \pi _ { 0 } \cap H ) .$

Then

$$
\begin{array} { r l } & { p + \pi = ( p + \pi _ { 0 } ) + \pi _ { 1 } } \\ & { \phantom { p p c } \subset \mathbb { R } ^ { \geq 1 } \omega p + \pi _ { 1 } } \\ & { \phantom { p p c } \subset \mathbb { R } ^ { \geq 1 } \omega ( p + \omega ^ { - 1 } \pi _ { 1 } ) } \\ & { \phantom { p p c } = \mathbb { R } ^ { \geq 1 } \omega ( \varepsilon _ { 1 } + ( p _ { 1 } + \pi _ { 1 } ^ { \prime } ) ) ~ , } \end{array}
$$

where, in the last step, $\pi _ { 1 } ^ { \prime }$ is a larger polyhedral cone in $\widetilde { C } _ { 1 }$ containing $\omega ^ { - 1 } \pi _ { 1 }$ . Now use the induction hypothesis. Hence, there exists a compact subset

$$
\omega _ { 1 } \subset P _ { 1 } = \{ g \in \operatorname { A u t } ( C _ { 1 } ) ^ { o } \mid g { \mathrm { ~ f i x e s ~ t h e ~ f l a g ~ } } { \overline { { C } } } _ { 1 } \supset { \overline { { C } } } _ { 2 } \supset \cdots \supset { \overline { { C } } } _ { n - 1 } \}
$$

such that

$$
p _ { 1 } + \pi _ { 1 } ^ { \prime } \subset \omega _ { 1 } \big ( p _ { 1 } + D _ { 1 } ^ { + } \big ) ,
$$

where $D _ { 1 } ^ { + } = \overline { { A _ { 1 } ^ { + } p _ { 1 } } }$ is the polyhedral cone generated by $p 1 , p 2 , \ldots , p _ { n - 1 }$ . Let $P _ { 1 } ^ { \prime } \subset P$ be the subgroup defined in Section 4.2 such that $P _ { 1 } ^ { \prime } \longrightarrow P _ { 1 }$ is surjective

with finite kernel and $P _ { 1 } ^ { \prime }$ acts identically on the boundary component containing $\varepsilon _ { 1 }$ . Let $\omega _ { 1 } ^ { \prime }$ be the inverse image of $\omega _ { \mathrm { l } }$ in $P _ { 1 } ^ { \prime }$ . Then

$$
\begin{array} { r l } & { p + \pi \subset \mathbb { R } ^ { \geq 1 } \omega ( \varepsilon _ { 1 } + \omega _ { 1 } ( p _ { 1 } + D _ { 1 } ^ { + } ) ) } \\ & { \qquad = \mathbb { R } ^ { \geq 1 } \omega \omega _ { 1 } ^ { \prime } ( \varepsilon _ { 1 } + p _ { 1 } + D _ { 1 } ^ { + } ) } \\ & { \qquad = \omega \omega _ { 1 } ^ { \prime } [ \mathbb { R } ^ { \geq 1 } ( p + D _ { 1 } ^ { + } ) ] . } \end{array}
$$

But

$$
\begin{array} { c } { { \mathbb { R } ^ { \geq 1 } ( p + D _ { 1 } ^ { + } ) = \left\{ ( 1 + \lambda ) ( p + a ) \mid a \in D _ { 1 } ^ { + } , \lambda \geq 0 \right\} } } \\ { { { } } } \\ { { { } = \{ p + ( \lambda p + a ) \mid a \in D _ { 1 } ^ { + } , \lambda \geq 0 \} } } \\ { { { } = p + D ^ { + } \ , } } \end{array}
$$

so $p + \pi \subset \omega \omega _ { 1 } ^ { \prime } ( p + D ^ { + } )$ , as asserted.

If we now drop the assumption that $G$ is $\mathbb { Q }$ -simple, we immediately get the following generalization.

Theorem 4.8 Let

$$
\begin{array} { r c l } { { } } & { { } } & { { G = G ^ { ( 1 ) } \times \cdots \times G ^ { ( k ) } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { C = C ^ { ( 1 ) } \times \cdots \times C ^ { ( k ) } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { P = P ^ { ( 1 ) } \times \cdots \times P ^ { ( k ) } , } } \end{array}
$$

where $G ^ { ( i ) }$ are $\mathbb { Q }$ -simple, $G ^ { ( i ) } = \mathrm { A u t } ( C ^ { ( i ) } , V ^ { ( i ) } ) ^ { o }$ , and $P ^ { ( i ) } \subset G ^ { ( i ) }$ is a minimal $\mathbb { Q }$ -parabolic. Let $P ^ { ( i ) }$ correspond to a flag

$$
\mathfrak { F } ^ { ( i ) } = \{ \overline { { C } } ^ { ( i ) } = \overline { { C } } _ { 0 } ^ { ( i ) } \supset \overline { { C } } _ { 1 } ^ { ( i ) } \supset \cdots \supset \overline { { C } } _ { n _ { i } - 1 } ^ { ( i ) } \} ,
$$

and let

$$
\widetilde C = \prod _ { i = 1 } ^ { k } \bigcup _ { j = 0 } ^ { n _ { i } - 1 } \overline { { C } } _ { j } ^ { ( i ) } .
$$

Then the closures of the Siegel sets $\overline { { \mathfrak { S } } } _ { \omega }$ in $\tilde { C }$ and the polyhedral cones $\pi \subset \widetilde { C }$ are cofinal.

Now let $C ^ { * }$ be the union of $C$ and all its $\mathbb { Q }$ -rational boundary components. Then, combining Theorem 4.8 with the main results of reduction theory (via Siegel sets), we find:

# Corollary 4.9

(i) For every arithmetic subgroup $\Gamma \subset G$ and every pair of closed polyhedral cones $\pi _ { 1 } , \pi _ { 2 } \subset C ^ { * }$ , the set

$$
\{ \gamma \in \Gamma | \gamma \pi _ { 1 } \cap \pi _ { 2 } \cap C \neq \varnothing \}
$$

is finite.

(ii) For every arithmetic subgroup $\Gamma \subset G$ , there exists a closed polyhedral cone $\pi \subset C ^ { * }$ such that $( \Gamma \pi ) \cap C = C$ .

Moreover it is now an easy matter to construct a polyhedral fundamental domain for the action of an arithmetic group $\Gamma$ on $C$ in the following sense.

Definition 4.10 A decomposition of $C$ into rational polyhedral cones $\{ \sigma _ { \alpha } \}$ is called a $\Gamma$ -admissible polyhedral decomposition of $C$ if the following properties are satisfied:

(1) a face of a $\sigma _ { \alpha }$ is a $\sigma _ { \beta }$ ;   
(2) $\sigma _ { \alpha } \cap \sigma _ { \beta }$ is a common face of $\sigma _ { \alpha }$ and $\sigma _ { \beta }$ ;   
(3) $\gamma \sigma _ { \alpha }$ is a $\sigma _ { \beta }$ , for all $\gamma \in \Gamma$ ;   
(4) mod Γ, there are only finitely many $\sigma _ { \alpha }$ ;   
(5) $\textstyle C = \bigcup _ { \alpha } ( \sigma _ { \alpha } \cap C )$

In fact, just choose a Siegel set $\mathfrak { S }$ and a finite set $F \subset G ( \mathbb { Q } )$ such that $C = \Gamma F { \mathfrak { S } }$ . Let $\pi$ be a polyhedral cone with rational vertices in $\tilde { C }$ such that $\mathfrak { S } \subset \pi$ . If $H _ { 1 } , \ldots , H _ { m }$ are the hyperplanes defining $\pi$ , consider

$$
{ \mathcal { H } } = \left\{ \gamma f H _ { i } \mid \gamma f \pi \cap \pi \neq \emptyset , { \mathrm { w h e r e ~ } } \gamma \in \Gamma , f \in F , i = 1 , \ldots , m \right\}
$$

Since $\pi$ is contained in some Siegel set, the property of Siegel sets guarantees that the images by $\Gamma$ of the connected components of $\pi \backslash \bigcup _ { H \in { \mathcal { H } } } H$ and their faces solve the problem.

# 5 Cores and co-cores

# 5.1

We have $C \subset V$ , with a compatible lattice $L \subset V$ as usual. We also have the characteristic function $\varphi : C \longrightarrow \mathbb { R } _ { > 0 }$ , which is defined up to a constant (see Section 1). The following proposition will enable us to make a sensible normalization of $\varphi$ .

Proposition 5.1 The function $\varphi$ is bounded on $C \cap L .$

Proof For any open cone $A$ in $V$ , let $A ^ { * }$ denote its dual in $V ^ { * }$ , as in Section 1. Let $\pi$ be an open simplicial cone in $\overline { { C } }$ with vertices $x _ { 1 } , \ldots , x _ { r } \in { \overline { { C } } } \cap L$ . Then $\pi ^ { * } = \{ \ell \in V ^ { * } \mid \ell ( x _ { i } ) > 0$ for all $i = 1 , \ldots , n \}$ . If we choose $\ell _ { 1 } , \ldots , \ell _ { r } \in V ^ { * }$ to be the dual basis to $x _ { 1 } , \ldots , x _ { r }$ , then $\pi ^ { * }$ is simplicial with vertices $\ell _ { 1 } , \ldots , \ell _ { r }$ and $\ell _ { 1 } , \dots , \ell _ { r } \in L ^ { * } \otimes \mathbb { Q }$ .

Now, for any cone $A$ , let

$$
\varphi _ { A } ( x ) = \int _ { A ^ { * } } \mathrm { e } ^ { - \langle x , \ell \rangle } \mathrm { d } \ell .
$$

Thus our $\varphi$ is just $\varphi _ { C }$

Since $\pi \subset C$ implies that $C ^ { * } \subset \pi ^ { * }$ , we know

$$
\varphi _ { C } ( x ) \leq \varphi _ { \pi } ( x ) = m \int \mathrm { e } ^ { - \langle x , \sum a _ { i } \ell _ { i } \rangle } \mathrm { d } a ,
$$

where $m$ is some constant.

Let $d$ be the volume of the parallelopiped spanned by $x _ { 1 } , \ldots , x _ { r }$ . If now $\textstyle x = \sum b _ { i } x _ { i } \in \pi \cap L$ , then $\begin{array} { r } { b _ { i } \geq \frac { 1 } { d } } \end{array}$ for all $i$ , and

$$
\varphi _ { C } ( x ) \leq \varphi _ { \pi } ( x ) = m \intop _ { \mathbb { R } _ { > 0 } ^ { r } } { \mathrm { e } } ^ { - \Sigma b _ { i } a _ { i } } { \mathrm { d } } a \leq m \intop _ { \mathbb { R } _ { > 0 } ^ { r } } { \mathrm { e } } ^ { - { \frac { 1 } { d } } \Sigma a _ { i } } { \mathrm { d } } a < M ,
$$

where $M$ is some constant depending only on $\pi$ .

By the reduction theory, we have $C = \cup \sigma _ { \alpha }$ , where the $\sigma _ { \alpha }$ are polyhedral rational cones open in their linear span, and there are only a finite number of them modulo Γ. Since any polyhedron can be written as the union of simplices, we may assume each $\sigma _ { \alpha }$ is simplicial. Since $\varphi ( \gamma x ) = \varphi ( x )$ for all $\gamma \in \Gamma$ and $x \in C$ , we have shown that

$\varphi$ is bounded on $L \cap$ (the union of the top-dimensional simplices).

We continue by induction. Assume that $\varphi$ is bounded on $L \cap$ (the union of the $\sigma _ { \alpha }$ with dim α ≥ ).

Suppose $\sigma _ { \beta }$ has dimension $s - 1$ . Let Star $\sigma _ { \beta }$ be the union of all simplices $\sigma _ { \alpha }$ having $\sigma _ { \beta }$ as a face. Then Star $\sigma _ { \beta }$ is a neighborhood of $\sigma _ { \beta }$ . By induction, $\varphi$ is bounded on $L \cap ( \operatorname { S t a r } \sigma _ { \beta } \setminus \sigma _ { \beta } )$ , say by the constant $B$ .

There exists a finite set $\{ \lambda _ { i } \} \subset L ^ { * }$ such that, for any $y \in \partial \mathrm { S t a r } \sigma _ { \beta }$ , we have $\lambda _ { i } ( y ) = 0$ for some $i$ , and $\lambda _ { i } ( z ) > 0$ for every $z \in \sigma _ { \beta }$ and all $i .$ .Because $\lambda _ { i } ( x ) \geq 1$ for each $i$ and each $x \in \sigma _ { \beta } \cap L$ , we see that

$$
\mathrm { d i s t } \big ( L \cap \sigma _ { \beta } , \partial \mathrm { S t a r } \sigma _ { \beta } \big ) > \delta > 0 ,
$$

where dist denotes the distance between the two sets.

Choose $\nu \in ( \operatorname { S t a r } \sigma _ { \beta } \setminus \sigma _ { \beta } ) \cap L$ , and pick $m > { \frac { | \nu | } { \delta } }$ . We claim that, for any $x \in L \cap \sigma _ { \beta }$ , both $m x + \nu$ and $m x - \nu$ are in Star $\sigma _ { \beta } \setminus \sigma _ { \beta }$ . For $m x + \nu$ , the claim is trivial, but, since the $m \delta$ -ball about mx is contained in Star $\sigma _ { \beta }$ and $| \nu | < m \delta$ , the claim is true for $m x - \nu$ as well.

Thus, $\varphi ( m x ) = \varphi { \bigl ( } { \frac { 1 } { 2 } } { \bigl ( } m x - \nu { \bigr ) } + { \frac { 1 } { 2 } } { \bigl ( } m x + \nu { \bigr ) } { \bigr ) } \leq B$ since $\varphi$ is convex. So $\varphi ( x ) \leq$ $m ^ { r } B$ for any $x \in L \cap \sigma _ { \beta }$ , where $\dim V = r$ . As there are only finitely many $\sigma _ { \beta }$ modulo $\Gamma$ , we see that $\varphi$ is bounded on

$$
L \cap ( { \mathrm { u n i o n ~ o f ~ a l l ~ } } \sigma _ { \beta } { \mathrm { ~ w i t h ~ d i m } } \sigma _ { \beta } \geq s - 1 ) .
$$

We normalize $\varphi$ so that ma $: \{ \varphi ( x ) \mid x \in C \cap L \} = 1 .$ . More generally, for any rational boundary component $C _ { 1 }$ , we have an orthogonal projection $\pi _ { C _ { 1 } }$ onto $C _ { 1 }$ and we normalize $\varphi _ { C _ { 1 } }$ such that $\scriptstyle \operatorname { n a x } \{ \varphi ( \pi _ { C _ { 1 } } x ) \mid x \in C \cap L \} = 1$ .

Now consider subsets (called kernels) $K \subset { \overline { { C } } }$ such that $\mathbb { R } ^ { \geq 1 } K \subset K$ , and $C \subset$ $\mathbb { R } _ { > 0 } K$ , and $0 \not \in { \overline { { K } } }$ . We say that two kernels $K _ { 1 } , K _ { 2 }$ are comparable if there exist $\lambda _ { 1 } , \lambda _ { 2 } \in \mathbb { R } _ { > 0 }$ with $\lambda _ { 1 } K _ { 1 } \subset K _ { 2 } \subset \lambda _ { 2 } K _ { 1 }$ . Let $L ^ { \prime }$ denote $L \backslash \{ 0 \}$

Theorem 5.2 The following kernels are comparable:

(a) $\Gamma ( p + C )$ ;   
(b) the convex hull of $C \cap L$ ;   
(c) $\{ x \in C \mid \varphi _ { C _ { 1 } } ( \pi _ { C _ { 1 } } x ) \leq 1$ for any rational boundary component $C _ { 1 } \}$ ;   
(d) $\left\{ x \in C \mid \left. x , y \right. \geq 1 \right.$ for all $y \in \overline { { C } } \cap L ^ { \prime } \}$ ;   
(e) the set

$$
\Gamma \cdot \left( \bigcup _ { i } \omega _ { i } ( A _ { i } ^ { + } p + p ) \right)
$$

for any finite collection $\{ \mathfrak { S } _ { i } = \omega _ { i } A _ { i } ^ { + } p \}$ of Siegel sets with $\textstyle \Gamma \cdot ( \bigcup _ { i } { \mathfrak { S } } _ { i } ) = C$

Note that in (c) we count $C$ as a rational boundary component.

Definition 5.3 This class of comparable kernels are the cores of C.

In order not to interrupt the proof of the theorem, we first prove two lemmas. If $C _ { 1 }$ is a rational boundary component corresponding to an idempotent $\varepsilon$ , we denote by $C _ { 1 } ^ { \perp }$ the boundary component corresponding to $p - \varepsilon$ .

Lemma 5.4 Let $C _ { 1 }$ be a rational boundary component and set $C _ { 0 } = C _ { 1 } ^ { \perp }$ . Take $\gamma \in \Gamma$ arbitrary and let $C _ { 1 } ^ { \prime } = ( \gamma ^ { - 1 } C _ { 0 } ) ^ { \perp }$ . Then

$$
\varphi _ { C _ { 1 } } \pi _ { C _ { 1 } } \gamma = \varphi _ { C _ { 1 } ^ { \prime } } \pi _ { C _ { 1 } ^ { \prime } } \ .
$$

Proof First we show that, for all $g \in \mathrm { N o r m } \left( C _ { 0 } \right)$ , there exists $\overline { { g } } \in \mathrm { N o r m } \left( C _ { 1 } \right) \cap$ $\mathrm { N o r m } \left( C _ { 0 } \right)$ such that $\pi _ { C _ { 1 } } g = \overline { { { g } } } \pi _ { C _ { 1 } }$ .

Let $a ( s )$ be the one-parameter subgroup $\exp ( t \varepsilon )$ , where $\varepsilon$ is the identity

in the Jordan algebra of $C _ { 0 }$ and $s = \mathbf { e } ^ { { \frac { 1 } { 2 } } t }$ . Then $\pi _ { C _ { 1 } } = \operatorname* { l i m } _ { s \longrightarrow 0 } a ( s )$ and hence $\mathrm { N o r m } \left( C _ { 0 } \right) = P ( a ^ { - 1 } )$ . Then

$$
\begin{array} { l } { \pi _ { C _ { 1 } } ( g x ) = \underset { s \longrightarrow 0 } { \operatorname* { l i m } } a ( s ) g x } \\ { \quad \quad = \underset { s \longrightarrow 0 } { \operatorname* { l i m } } a ( s ) g a ^ { - 1 } ( s ) a ( s ) x } \\ { \quad \quad = \overline { { g } } ( \pi _ { C _ { 1 } } x ) , } \end{array}
$$

where $x \in C _ { 1 }$ is arbitrary and ${ \overline { { g } } } = \operatorname* { l i m } _ { s \longrightarrow 0 } a ( s ) g a ^ { - 1 } ( s )$ exists by the definition of $P ( a ^ { - 1 } )$ and is in $Z ( a )$ .

Further, if $g \in { \mathrm { S t a b } } \left( p \right)$ , then $\pi _ { C _ { 1 } } g = g \pi _ { g ^ { - 1 } C _ { 1 } }$ . This is simply because $g$ is an orthogonal transformation.

Now, $\mathrm { N o r m } \left( C _ { 0 } \right)$ and $\operatorname { S t a b } \left( p \right)$ generate $G$ , so write $\gamma = g h$ with $g \in \mathrm { N o r m } \left( C _ { 0 } \right)$ and $h \in \mathrm { S t a b } \left( p \right)$ . Then

$$
\begin{array} { c } { { \pi _ { C _ { 1 } } \gamma = \pi _ { C _ { 1 } } g h } } \\ { { { } } } \\ { { { } = \overline { { { g } } } \pi _ { C _ { 1 } } h } } \\ { { { } } } \\ { { { } = \overline { { { g } } } h \pi _ { h ^ { - 1 } C _ { 1 } } . } } \end{array}
$$

Meanwhile, $\bar { g } h : h ^ { - 1 } C _ { 1 } \longrightarrow C _ { 1 }$ is an isomorphism of homogeneous cones, and, because the characteristic function is unique up to a constant,

$$
\varphi _ { h ^ { - 1 } C _ { 1 } } = \mu \varphi _ { C _ { 1 } } \overline { { { g } } } h ,
$$

for some $\mu \in \mathbb { R } _ { > 0 }$

Thus $\mu \varphi _ { C _ { 1 } } \pi _ { C _ { 1 } } \gamma = \mu \varphi _ { C _ { 1 } } \overline { { g } } h \pi _ { h ^ { - 1 } C _ { 1 } } = \varphi _ { h ^ { - 1 } C _ { 1 } } \pi _ { h ^ { - 1 } C _ { 1 } } \qquad $ . So, by the way we normalized $\varphi _ { C _ { 1 } }$ and $\varphi _ { h ^ { - 1 } C _ { 1 } }$ , and since $\gamma$ fixes the lattice, it is clear that $\mu = 1$ .

It remains to check that $h ^ { - 1 } C _ { 1 } = ( \gamma ^ { - 1 } C _ { 0 } ) ^ { \perp }$ . But $\gamma ^ { - 1 } C _ { 0 } = h ^ { - 1 } g ^ { - 1 } C _ { 0 } =$ $h ^ { - 1 } C _ { 0 }$ , so if $\varepsilon$ is the idempotent of $C _ { 0 }$ , it follows that $h ^ { - 1 } C _ { 0 }$ has $h ^ { - 1 } \varepsilon _ { 0 }$ as its idempotent, and thus $( \gamma ^ { - 1 } C _ { 0 } ) ^ { \perp }$ has $p - h ^ { - 1 } \varepsilon _ { 0 } = h ^ { - 1 } ( p - \varepsilon _ { 0 } )$ , which is the idempotent of $h ^ { - 1 } C _ { 1 }$ .

Corollary 5.5 The set in part (c) in the theorem is $\Gamma$ -invariant.

Proof This follows from the lemma and the fact that application of any $\gamma \in \Gamma$ sets up a bijection of rational boundary components.

Lemma 5.6 Let $\omega A ^ { + } p$ be a Siegel set. For a maximal set $\varepsilon _ { 1 } , \ldots , \varepsilon _ { n }$ of orthogonal idempotents of Lie A, let

$$
\ell ( y ) = { \frac { \langle \pmb { \varepsilon } _ { n } , \pmb { y } \rangle } { \langle \pmb { \varepsilon } _ { n } , \pmb { \varepsilon } _ { n } \rangle } }
$$

for $y \in C$ , where the inner product is chosen as usual so that $A$ consists of self-adjoint transformations.

Then there exists a constant $m > 0$ such that

$$
\ell ( g h p ) \geq R f o r s o m e g \in \omega , h \in A ^ { + } \Longrightarrow \ell ( h p ) \geq \frac { R } { m } .
$$

Proof We know that $\textstyle \bigcup _ { h \in A ^ { + } } \{ h ^ { - 1 } \omega h \}$ is relatively compact, so it makes sense to define

$$
m = \operatorname* { s u p } \{ \ell ( h ^ { - 1 } g h p ) \mid g \in \omega , h \in A ^ { + } \} \ .
$$

Now, if $q \in C$ is arbitrary, we show next that $\ell ( h q ) = \ell ( h p ) \ell ( q )$ . In fact, write $q = \lambda \varepsilon _ { n } + f$ with $\lambda \in \mathbb { R } _ { > 0 }$ and $f$ orthogonal to $\varepsilon _ { n }$ . Since $h \in A$ is self-adjoint, and $\varepsilon _ { n }$ is an eigenvector for anything in $A$ , it follows that $h f$ is orthogonal to $\varepsilon _ { n }$ . Thus,

$$
\ell ( h q ) = \ell ( h \lambda \varepsilon _ { n } + h f ) = \lambda \ell ( h \varepsilon _ { n } ) .
$$

Apply this to $q = p$ , remembering that the $\varepsilon _ { i }$ are mutually orthogonal: $\ell ( h p ) =$ $\ell ( h \varepsilon _ { n } )$ . By definition, $\ell ( q ) = \lambda$ . Thus $\ell ( h q ) = \ell ( h p ) \ell ( q )$ . We conclude that if $\begin{array} { r } { \ell ( h p ) < \frac { R } { m } } \end{array}$ , then $\begin{array} { r } { \ell ( g h p ) = \ell ( h ( h ^ { - 1 } g h ) p ) < \frac { R } { m } \ell ( h ^ { - 1 } g h p ) < R } \end{array}$ , this being the contrapositive of what the lemma states. □

Proof (of Theorem 5.2) We will prove the theorem in a chain, showing each set in parts (a) through (e) is contained in some dilation of the subsequent set.

(1) Let $H$ be the convex hull of $C \cap L .$ . Choose $M \in \mathbb { Z } _ { > 0 }$ such that $M p = w$ for some lattice point $w$ . Since $H$ is $\Gamma$ -invariant, it suffices to show that $p + C \subset$ $\textstyle { \frac { 1 } { M } } H$ . By the reduction theory, $C$ is covered by the $\Gamma$ -translates of a finite union of rational polyhedra $\sigma _ { \alpha }$ . So it is enough to show, given $\gamma \in \Gamma$ and $\sigma _ { \alpha }$ , that $\textstyle p + \gamma ^ { - 1 } \sigma _ { \alpha } \subset { \frac { 1 } { M } } H$ , or, equivalently, that $\gamma p + \sigma _ { \alpha } \subset { \frac { 1 } { M } } H$ .

If $x$ is any point of $\sigma _ { \alpha }$ , we can write $\textstyle x = \sum _ { i = 1 } ^ { k } t _ { i } \nu _ { i }$ , where $\nu _ { i } \in L \cap { \overline { { C } } }$ and $\textstyle \sum t _ { i } \leq 1$ . Then

$$
M ( \gamma p + \sum t _ { i } \nu _ { i } ) = \sum t _ { i } ( M \nu _ { i } + \gamma w ) + \big ( 1 - \sum t _ { i } \big ) ( \gamma w ) \in H
$$

because $M \nu _ { i } + \gamma _ { w }$ and $\gamma _ { w }$ are in $L \cap C$ . We conclude that $\gamma p + \sigma _ { \alpha } \subset { \textstyle { \frac { 1 } { M } } } H$ (2) Let $J$ be the set described in part (c) of the theorem. Then $H \subset J$ simply by the way we normalized the $\varphi _ { C _ { 1 } } \mathbf { s }$ , and by their convexity.

(3) We must show that there exists $\lambda \in \mathbb { R } _ { > 0 }$ such that, if $x \in C$ and $\varphi _ { C _ { 1 } } ( \pi _ { C _ { 1 } } x ) \leq$ 1 for every rational boundary component $C _ { 1 }$ , then $\langle x , y \rangle \geq \lambda$ for all $y \in \overline { { C } } \cap L$ .

We will prove this by induction on dimC. If $\mathrm { d i m } C = 0$ , there is nothing to prove.

Now suppose dim $C > 0$ . If $C _ { 1 }$ is a rational boundary component, the hypothesis for $x$ is inherited by $\pi _ { C _ { 1 } } x$ and so, by induction, there exists $\lambda _ { 1 }$ (depending on $C _ { 1 }$ ) such that $\langle \pi _ { C _ { 1 } } x , y \rangle \geq \lambda _ { 1 }$ for all $y \in \overline { { C } } _ { 1 } \cap L$ . But $\langle x , y \rangle = \langle \pi _ { C _ { 1 } } x , y \rangle$ , so $\langle x , y \rangle \geq \lambda _ { 1 }$ in addition.

Now there are only a finite number of $^ t \Gamma$ -orbits of rational boundary components (see Proposition 15.6 in [3]). Let $C _ { 1 } , \ldots , C _ { s }$ be representatives for the $^ t \Gamma$ -orbits of rational boundary components and let $\lambda = \operatorname* { m i n } \left( \lambda _ { 1 } , . . . , \lambda _ { s } \right)$ . If $C _ { 0 }$ is another rational boundary component, pick $\gamma \in \Gamma$ such that ${ } ^ { t } \gamma C _ { 0 } = C _ { i }$ for some $i$ between 1 and $s$ . If $y \in \overline { { C } } _ { 0 } \cap L ^ { \prime }$ , then ${ } ^ { t } \gamma _ { y } \in \overline { { C } } _ { i } \cap L ^ { \prime }$ and $\gamma ^ { - 1 } x \in K$ by Lemma 5.4 so that

$$
\langle x , y \rangle = \langle \gamma ^ { - 1 } x , { } ^ { t } \gamma y \rangle \geq \lambda \ .
$$

It remains to consider $y \in C \cap L$ . We need only show that there exists some $\lambda ^ { \prime } > 0$ such that $\varphi _ { C } ( x ) \leq 1 \Longrightarrow \langle x , y \rangle \geq \lambda ^ { \prime } > 0$ for all $y \in \pmb { \sigma } \cap \pmb { L } \cap \pmb { C } .$ ,where $\sigma$ is spanned by $y _ { 1 } , \dotsc , y _ { r } \in L \cap { \overline { { C } } }$ . If $\boldsymbol { y } = \sum { a _ { i } } \boldsymbol { y } _ { i }$ and $d = \operatorname* { d e t } ( y _ { 1 } , \dots , y _ { r } )$ , then $\begin{array} { r } { y \in L \cap C \Longrightarrow a _ { i } \in \frac { 1 } { d } \mathbb { Z } } \end{array}$ and $a _ { i } \geq 0$ for each $i$ . Furthermore $\begin{array} { r } { y ^ { \prime } = \sum _ { i | a _ { i } > 0 } y _ { i } \in L \cap C . } \end{array}$ , as otherwise $\{ y _ { i } | a _ { i } > 0 \}$ would be contained in a proper boundary component and hence so would $y$ . But $\begin{array} { r } { \langle x , y \rangle \geq \frac { 1 } { d } \langle x , y ^ { \prime } \rangle } \end{array}$ and $\langle x , y ^ { \prime } \rangle$ is bounded away from zero because

(i) the set $\{ x \mid \varphi _ { C } ( x ) \leq 1 \}$ is in the complement of some ball $B$ around 0 by Proposition 1.6;   
(ii) $\left\{ \left. x , y ^ { \prime } \right. \mid x \in C \setminus B \right\}$ is bounded away from zero because $y ^ { \prime } \in C$ ;   
(iii) there are only finitely many possible $y ^ { \prime }$ .

This gives the desired $\lambda ^ { \prime } > 0$ with the property that $\varphi _ { C } ( x ) \leq 1 \Longrightarrow \langle x , y \rangle \geq \lambda ^ { \prime }$ for all $y \in \pmb { \sigma } \cap \pmb { L } \cap \pmb { C }$ .

(4) We know that $C = \Gamma { \cdot } \bigcup _ { i = 1 } ^ { n } \omega _ { i } A _ { i } ^ { + } p$ , so, for any $x \in C$ , we have $x = \gamma g a p$ with $\gamma \in \Gamma$ , $g \in \omega _ { i }$ and $a \in A _ { i } ^ { + }$ for some $i$ . We must show that there exists $M > 0$ such that $\langle x , y \rangle \geq 1$ for all $y \in \overline { { C } } \cap L ^ { \prime }$ implies that $M \cdot a p \in A _ { i } ^ { + } p + p$ .

Let $\varepsilon _ { 1 } , \ldots , \varepsilon _ { n }$ be the maximal set of orthogonal idempotents of LieA, so that $A _ { i } ^ { + } p$ is the convex cone spanned by $\pmb { \varepsilon } _ { 1 } , \pmb { \varepsilon } _ { 1 } + \pmb { \varepsilon } _ { 2 } , \ldots , \pmb { \varepsilon } _ { 1 } + \cdots + \pmb { \varepsilon } _ { n } = p$ . Then it is easy to see that, if $x \in A _ { i } ^ { + } p$ , then $x \in A _ { i } ^ { + } p + p$ if and only if $\langle \varepsilon _ { n } , x \rangle \geq \langle \varepsilon _ { n } , \varepsilon _ { n } \rangle$ .

Choose $M _ { 1 } \in \mathbb { Z } _ { > 0 }$ so that ${ } ^ { t } \gamma M _ { 1 } \varepsilon _ { n }$ is a lattice point for all $\gamma \in \Gamma$ .(This is possible because $L$ and $L ^ { * }$ are commensurate.) The hypothesis on $x$ says that $\langle { } ^ { t } { \gamma } ^ { - 1 } M _ { 1 } \varepsilon _ { n } , x \rangle \geq 1 .$ . That is,

$$
M _ { 1 } \langle \varepsilon _ { n } , g a p \rangle = M _ { 1 } \langle { } ^ { t } { \gamma } ^ { - 1 } \varepsilon _ { n } , { \gamma } g a p \rangle \ge 1 \ .
$$

Letting $m$ be the constant in Lemma 5.6, we get $\begin{array} { r } { M _ { 1 } \langle \varepsilon _ { n } , a p \rangle \geq \frac { 1 } { m } } \end{array}$ . If $M =$

$M _ { 1 } m \langle \pmb { \varepsilon } _ { n } , \pmb { \varepsilon } _ { n } \rangle$ , then $\langle \pmb { \varepsilon } _ { n } , M a p \rangle \geq \langle \pmb { \varepsilon } _ { n } , \pmb { \varepsilon } _ { n } \rangle$ , and we are done.

(5) For this last step, it clearly is enough to show $M \cdot \omega ( A ^ { + } p + p ) \subset C + p$ for some $M > 0$ .

Now, $A ^ { + } p + p \subset C + p$ , so that $\omega ( A ^ { + } p + p ) \subset \omega C + \omega p = C + \omega p .$ . Since $\omega$ is compact, we may choose $M > 0$ so that $M \cdot \omega p \subset C + p$ . Indeed, just pick $M$ such that $q - { \frac { 1 } { M } } p \in C$ for all $q \in \omega p$ . Then $M \cdot \omega ( A ^ { + } p + p ) \subset M \cdot C + M \cdot \omega p \subset$ $C + C + p \subset C + p$ .

Corollary 5.7 Any core is comparable to its closed convex hull.

Proof Some of the cores in the list of the theorem are closed and convex. Let $A$ be one of them and let $B$ be any core. Then there are $\lambda _ { 1 } , \lambda _ { 2 } , \mu _ { 1 } , \mu _ { 2 } \in \mathbb { R } _ { > 0 }$ such that $\lambda _ { 1 } A \subset B \subset \lambda _ { 2 } A$ and $\mu _ { 1 } B \subset A \subset \mu _ { 2 } B$ . The first implies that

$$
\lambda _ { 1 } A \subset \mathrm { c l o s e d c o n v e x ~ h u l l ~ o f } B \subset \lambda _ { 2 } A \ ,
$$

and so

$$
\lambda _ { 1 } \mu _ { 1 } B \subset \mathrm { c l o s e d ~ c o n v e x ~ h u l l ~ o f } \ : B \subset \mu _ { 2 } \lambda _ { 2 } B \ : .
$$

Thus the closed convex hull of any core is again a core.

# 5.2

We need another class of comparable kernels that stand in duality to the cores of $C$ . Recall that $\mathbb { R } ^ { \geq 1 }$ denotes the set of real numbers $[ 1 , \infty )$ . We call $A \subset V$ a semi-conical convex set if $A$ is convex and $\mathbb { R } ^ { \geq 1 } A = A$ . For any set $A \subset V$ define:

$$
\begin{array} { r l } & { \mathrel { \phantom { = } } \mathrm { x m i - h u l l } ( A ) = \mathrm { c l o s e d ~ c o n v e x ~ h u l l ~ o f ~ } \mathbb { R } ^ { \geq 1 } A \mathrm { ~ ; ~ } } \\ & { \mathrel { \phantom { = } } \check { A } = \{ x \in V \mid \langle x , a \rangle \geq 1 \mathrm { ~ f o r ~ a l l ~ } a \in A \} \mathrm { ~ . ~ } } \end{array}
$$

Note that ${ \check { A } } = \emptyset$ if $0 \in { \overline { { A } } }$ .

Proposition 5.8 If semi-hull $( A )$ does not contain 0, then

$$
\check { \check { A } } = \mathrm { s e m i - h u l l } ( A ) .
$$

Proof Clearly $A \subset { \check { X } }$ . Let $b \in { \check { \check { A } } }$ and suppose $b \notin$ semi-hull $( A )$ . Then by the separating hyperplane theorem, there is a $y \in V$ such that $\langle y , b \rangle < \lambda$ and $\langle y , a \rangle \geq \lambda$ for all $a \in$ semi-hull $( A )$ , for some $\lambda \in \mathbb { R }$ .

If $\lambda > 0$ , replace $y$ by ${ \frac { 1 } { \lambda } } y$ This gives $\langle y , b \rangle < 1$ and $\langle y , a \rangle \geq 1$ for all $a \in$ semi-hull $( A )$ , which implies that $y \in { \check { A } }$ and so $b \not \in { \check { \check { A } } }$ , a contradiction.

Meanwhile, if $\langle y , a \rangle < 0$ for some $a \in A$ , then $\langle y , t a \rangle \longrightarrow - \infty$ as $t \longrightarrow + \infty$ , which is impossible. Thus only the case $\lambda = 0$ remains. Now we have $\langle y , a \rangle \geq 0$ for all $a \in \mathrm { s e m i - h u l l } ( A )$ and $\left. y , b \right. < 0$ .

By the separating hyperplane theorem applied to 0 and semi-hull $( A )$ , there exists $z \in V$ with $\langle z , a \rangle \geq \mu$ for all $a \in \mathrm { s e m i - h u l l } ( A )$ and $0 = \langle z , 0 \rangle < \mu$ . That is, $\mu > 0$ . Pick a small positive number $\delta$ so that $\langle y + \delta z , b \rangle < 0$ still holds. But $\langle y + \delta z , a \rangle \geq \delta \mu > 0$ for all $a \in$ semi-hull $( A )$ . So we are back to the previous case.

Proposition 5.9 If K is a kernel of C, then so is $\check { K }$ .

Proof By definition, $K$ is a kernel if and only if $K \subset { \overline { { C } } }$ , and $\mathbb { R } ^ { \geq 1 } K \subset K$ , and $C \subset \mathbb { R } _ { > 0 } K$ , and $0 \not \in { \overline { { K } } }$ . Now, for $\check { K }$ , it is automatic that $\mathbb { R } ^ { \geq 1 } \check { K } \subset \check { K }$ and $0 \not \in$ ${ \check { K } } = { \overline { { \check { K } } } }$ . Also, $C \subset \mathbb { R } _ { > 0 } K$ implies that, for any $x \in { \check { K } }$ and any $y \in C$ , we have $\langle x , y \rangle > 0$ , so that $\check { K } \subset \overline { { C } }$ . Finally, for any $y \in C$ , $\langle y , x \rangle$ is bounded away from 0 as $x$ runs through $K$ because $0 \not \in { \overline { { K } } }$ . Thus $C \subset \mathbb { R } _ { > 0 } \check { K }$ . □

Proposition 5.10 If two kernels $K _ { 1 }$ and $K _ { 2 }$ are comparable, then so are $\check { K } _ { 1 }$ and ${ \check { K } } _ { 2 }$ .

Proof This follows because, if $\mu > 0$ , then $( \mu K ) ^ { \vee } = \mu ^ { - 1 } \check { K }$ for any set $K$ , and, if $K _ { 1 } \subset K _ { 2 }$ , then ${ \check { K } } _ { 2 } \subset { \check { K } } _ { 1 }$ for any two sets $K _ { 1 }$ and $K _ { 2 }$ .

So $K \mapsto { \check { K } }$ sets up a duality among closed convex kernels, and even among equivalence classes of comparable kernels which have the property of being comparable with their closed convex hulls (e.g., cores). Thus the duals of the cores (see Section 5.1) are a new class of comparable kernels, called co-cores.

In particular, denote two of the cores by

$$
\begin{array} { r l } & { \Sigma _ { 1 } = \mathrm { c l o s e d c o n v e x h u l l o f } C \cap L , } \\ & { \Sigma _ { 2 } = \left\{ x \in C \mid \langle x , y \rangle \geq 1 \mathrm { f o r a l l } y \in \overline { { C } } \cap L ^ { \prime } \right\} . } \end{array}
$$

Then the corresponding co-cores are

$$
\begin{array} { r l } & { \check { \Sigma } _ { 1 } = \left\{ x \in \overline { { C } } \mid \langle x , y \rangle \geq 1 \mathrm { ~ f o r ~ a l l ~ } y \in C \cap L \right\} , } \\ & { \check { \Sigma } _ { 2 } = \operatorname { c l o s e d } \operatorname { c o n v e x } \mathrm { ~ h u l l ~ o f } \overline { { C } } \cap L ^ { \prime } . } \end{array}
$$

Using these co-cores we will construct some new $\Gamma$ -admissible polyhedral decompositions of $C$ .

First we must prove a few general propositions. Recall that $e$ is an extreme point of a closed convex set $A$ if and only if, for all $x , y \in A$ , if $\begin{array} { r } { e = \frac { 1 } { 2 } ( x + { } } \end{array}$ y), then $x = y = e$ . We denote by $E ( A )$ the set of all extreme points of $A$ . The Krein–Milman theorem says that any compact convex set $\Sigma$ is the closed convex hull of its extreme points. This fails if $\Sigma$ is not compact, but we can say the following:

Proposition 5.11 If $\Sigma$ is a closed convex kernel, then $\Sigma$ is the closed convex hull of $\textstyle \bigcup _ { e \in E ( \Sigma ) } ( e + C )$ .

Proof For any $e \in E ( \Sigma )$ , $r \in C$ , there is a $\lambda \in \mathbb { R } _ { > 0 }$ such that $\lambda r \in \Sigma$ , since $\Sigma$ is a kernel. Then we have $\begin{array} { r } { \frac { \lambda } { \lambda + 1 } e + \frac { 1 } { \lambda + 1 } ( \lambda r ) \in \Sigma } \end{array}$ ; that is, $\frac { 1 } { \lambda + 1 } ( e + r ) \in \Sigma$ .Since $\Sigma$ is a semi-cone, $e + r \in \Sigma$ . Thus $\Sigma$ contains the closed convex hull of $\bigcup ( e + C )$ .

Conversely, suppose $q \in \Sigma$ , but $q$ is not contained in the closed convex hull of $\bigcup ( e + C )$ . By the separating hyperplane theorem, there exists $\lambda \in \mathbb { R }$ , $w \in V$ such that $\langle w , e + r \rangle \geq \lambda$ for all $e \in E ( \Sigma )$ , $r \in C$ , but $\langle w , q \rangle < \lambda$ .

If we had $\langle w , r \rangle < 0$ for some $r \in C$ , then $\langle w , e + t r \rangle \longrightarrow - \infty$ as $t \longrightarrow \infty$ , which is impossible. Therefore $w \in { \overline { { C } } }$ , and then $\langle w , q \rangle < \lambda$ implies that $\lambda >$ 0. In the case when $w \in \partial C$ , choose $y \in C$ of small enough norm so that $\langle w + y , q \rangle < \lambda$ . Of course, $\langle w + y , e + r \rangle \geq \lambda$ still, so, replacing $w$ by $w + y$ , we may always assume $w \in C$ .

Let $H = \left\{ z \in V \mid \left. z , w \right. \leq \lambda \right\}$ . Then $H \cap \Sigma$ is closed and convex. It is also compact, since $w \in C$ . By the Krein–Milman theorem, since $q \in H \cap \Sigma$ and $\langle q , w \rangle < \lambda$ , there must exist an extreme point $e _ { 0 }$ of $H \cap \Sigma$ not on the hyperplane $\{ z \mid \langle z , w \rangle = \lambda \}$ . Then $e _ { 0 }$ is an extreme point of $\Sigma$ and $\langle w , e _ { 0 } \rangle < \lambda$ , a contradiction. □

Corollary 5.12 If $\Sigma$ is a closed convex kernel, $\check { \Sigma } = E ( \Sigma ) ^ { \vee } \cap \overline { { C } }$

Proof Clearly, $E ( \Sigma ) \subset \Sigma$ , so $\check { \Sigma } \subset E ( \Sigma ) ^ { \vee }$ . Conversely, suppose $\langle w , e \rangle \geq 1$ for all $e \in E ( \Sigma )$ , for some $w \in \overline { { C } }$ . Then $\langle w , e + r \rangle \geq 1$ for all $e \in E ( \Sigma )$ , $r \in C$ , so, by the previous proposition, $\langle w , s \rangle \geq 1$ for all $s \in \Sigma$ . □

Next we show that among $\Gamma \cdot$ -invariant kernels, cores and co-cores represent the two extremes. Precisely, we have:

Proposition 5.13 If $\Sigma$ is a $\Gamma$ -invariant closed convex kernel, then there is a core $K _ { 1 }$ and a co-core $K _ { 2 }$ such that $K _ { 1 } \subset \Sigma \subset K _ { 2 }$ .

Proof Since $\Sigma$ is a kernel, we have $\lambda p \in \Sigma$ for some $\lambda \in \mathbb { R } _ { > 0 }$ . Then $\lambda ( \Gamma p ) \subset \Sigma$ . Dualizing gives

$$
\check { \Sigma } \subset [ \lambda ( \Gamma p ) ] ^ { \vee } .
$$

We know a priori that $\check { \Sigma } { \subset } \overline { { C } }$ , so, just as in the proof of the corollary above, we have

$$
\begin{array} { r } { \check { \Sigma } \subset [ \lambda ( \Gamma p ) ] ^ { \vee } \cap \overline { { C } } = [ \lambda ( \Gamma p ) + C ] ^ { \vee } = [ \lambda \Gamma ( p + C ) ] ^ { \vee } . } \end{array}
$$

Thus $K _ { 1 } = [ \lambda \Gamma ( p + C ) ] ^ { \vee \vee }$ is a core and $K _ { 1 } \subset \Sigma$ . Now $\check { \Sigma }$ is itself a ${ } ^ { t } \Gamma$ -invariant closed convex kernel, so, by what we have just proved, there is a core $K _ { 2 } \subset { \check { \Sigma } }$ . Then $K _ { 3 } = \check { K } _ { 2 }$ is a co-core and $\Sigma = \check { \check { \Sigma } } \subset K _ { 3 }$ .

# 5.3

The idea is to make a $\Gamma \cdot$ -admissible polyhedral decomposition by taking the cones over the faces of some $\Gamma$ -invariant kernel $\Sigma$ . Roughly speaking, $\Sigma$ must be “locally polyhedral”, so that its faces will be polygons. We also want the number of faces to be finite modulo $\Gamma$ .

For example, take $C = \mathbb { R } _ { > 0 } ^ { 2 }$ , $L = \mathbb { Z } ^ { 2 }$ . In this case the cores $\Sigma _ { 1 }$ , $\Sigma _ { 2 }$ in (5.1) coincide.

![](images/5edc03654794d8936d62e468425106fcc6819fd316045469b764432a47597ac2.jpg)

One sees that the problem with a core is that a face can be parallel to the boundary of the cone, and so contain an infinite number of vertices. We will deal with co-cores instead.

Let $C ^ { * }$ be the union of $C$ with all rational boundary components.

Definition $5 . 1 4 \dagger$ A closed convex kernel $\Sigma$ is called rationally locally polyhedral if, for any rational polyhedral cone $\Pi$ with vertices in $C ^ { * }$ , there exist $x _ { 1 } , \dots , x _ { s } \in V ( \mathbb { Q } ) \cap { \overline { { C } } }$ and $\lambda _ { 1 } , \dots , \lambda _ { s } \in \mathbb { Q } _ { > 0 }$ such that

$$
\Pi \cap \Sigma = \left\{ y \in \Pi \mid \langle x _ { i } , y \rangle \geq \lambda _ { i } { \mathrm { ~ f o r ~ } } i = 1 , \dots , s \right\} .
$$

Definition 5.15 We shall call a $\Gamma$ -invariant rational locally polyhedral closed and convex kernel a $\Gamma$ -polyhedral kernel.

Proposition 5.16 If $\Sigma$ is a $\Gamma$ -polyhedral kernel, then there exists $M \in \mathbb { Z }$ such that $\begin{array} { r } { E ( \Sigma ) \subset \frac { 1 } { M } L . } \end{array}$ .

$^ \dagger$ This definition differs from the corresponding definition in the first edition.

Proof Using our reduction theory, choose $\Pi _ { 1 } , \ldots , \Pi _ { n }$ , a fundamental set of rational polyhedra for Γ. It is easy to see that they may be chosen so that their projections into any standard boundary component form a fundamental set in the boundary component. So,

$$
\bigcup _ { \gamma \in \Gamma } \gamma \Pi _ { i } = C ^ { * } .
$$

Clearly, $E ( \Sigma ) \cap \Pi _ { i } \subset E ( \Sigma \cap \Pi _ { i } )$ for $i = 1 , \ldots , n$

By the definition of $\Gamma$ -polyhedral, $\Sigma \cap \Pi _ { i }$ is cut out of $V$ by a finite number of rational hyperplanes. Therefore, $E ( \Sigma \cap \Pi _ { i } )$ is a finite set of rational points, and there exists $M \in \mathbb { Z }$ such that $\begin{array} { r } { E ( \Sigma \cap \Pi _ { i } ) \subset \frac { 1 } { M } L . } \end{array}$ , for $i = 1 , \ldots , n$ .

For any $e \in E ( \Sigma ) \cap C ^ { * }$ there is a $\gamma \in \Gamma$ and $i \in \{ 1 , \ldots , n \}$ such that $\gamma e \in \Pi _ { i }$ . Since $\Sigma$ is $\Gamma$ -invariant, we have $\gamma e \in E ( \Sigma )$ . Thus $E ( \Sigma ) \cap C ^ { * } = \bigcup \Gamma [ E ( \Sigma ) \cap \Pi _ { i } ] \subset$ $\begin{array} { r } { \frac { 1 } { M } L } \end{array}$ .

Furthermore, $\Sigma \cap C$ is contained in the closed convex hull $\Sigma ^ { \prime }$ of the set $E ( \Sigma ) \cap$ $C ^ { * } + C$ , since, clearly, $\Sigma \cap \Pi _ { i }$ is contained in $\Sigma ^ { \prime }$ and $\Sigma ^ { \prime }$ is $\Gamma$ -invariant. Because $\Sigma \cap C$ is dense in $\Sigma$ , also $\Sigma \subset \Sigma ^ { \prime }$ . But $\Sigma$ is convex and closed, so that $\Sigma = \Sigma ^ { \prime }$ . Now we need the following lemma†:

Lemma 5.17 Let $D$ be a discrete subset of $\overline { { C } }$ and let $X$ be the closed convex hull of $D + C .$ . Then every extreme point of $X$ belongs to $D$ .

Proof Recall the definition of an exposed point: a point $p$ in a closed convex set $Y$ is said to be exposed if there exists a linear function $\phi$ such that $\phi ( p ) = 0$ but $\phi \left| _ { Y \backslash \{ p \} } > 0 \right.$ . Then Straszewicz’s theorem (see [12], Theorem 18.6) states that the exposed points are dense in the extreme points. Since $D$ is discrete, it is enough to see that every exposed point $p$ of $X$ belongs to $D$ .

Since $p + { \overline { { C } } } \subset X$ , we have $\phi | _ { \overline { { C } } } \geq 0$ and $\phi _ { \overline { { C } } \backslash \{ 0 \} } > 0$ . But then

$$
\phi ( p ) = \operatorname* { i n f } ( \phi | _ { X } ) = \operatorname* { i n f } ( \phi | _ { D + C } ) = \operatorname* { i n f } ( \phi | _ { D } )
$$

is assumed in some point $p ^ { \prime } \in D$ and hence $p = p ^ { \prime } \in D$ .

Taking $D = E ( \Sigma ) \cap C ^ { * }$ in the lemma, we have $\boldsymbol { X } = \boldsymbol { \Sigma } ^ { \prime } = \boldsymbol { \Sigma }$ . We conclude that $E ( \Sigma ) = E ( X ) \subset D = E ( \Sigma ) \cap C ^ { * }$ , and we have already seen that $E ( \Sigma ) \cap C ^ { * } \subset$ $\scriptstyle { \frac { 1 } { M } } L$ .

For any $y \in C$ , write

$$
H _ { y } = \{ z \in V \mid \langle z , y \rangle = 1 \} .
$$

$^ \dagger$ This lemma is taken from [9] and replaces an incorrect argument in the first edition.

The following proposition will give us some explicit $\Gamma \cdot$ -admissible decompositions of $C$ . Recall that if $X$ is a closed convex set and $H$ is a hyperplane, then $H$ is said to be a supporting hyperplane of $X$ if $X$ lies entirely in one of the two closed half-planes defined by $H$ and $X \cap H \neq \emptyset$ . In particular, $X \cap H$ is a face of $X$ .

Proposition 5.18 Let $\Sigma$ be a Γ-polyhedral co-core, and let $Y$ be the set of $y \in { \overline { { C } } }$ such that $H _ { y }$ is a supporting hyperplane of $\Sigma$ which meets $E ( \Sigma )$ in a set of points spanning $V$ . Let $\sigma _ { y }$ be the cone over $H _ { y } \cap \Sigma$ . Then the set $\mathcal { S }$ of all faces of $\sigma _ { y }$ (including $\sigma _ { y }$ ), as y ranges through $Y$ , is a $\Gamma$ -admissible polyhedral decomposition of $C _ { i }$ , cf. Definition 4.10.

Proof First, we claim that in fact $Y \subset C$ . Indeed, assume $y \in Y \cap \partial C$ . By Proposition 5.16, $y$ must be rational. Hence there exists some $z \in \overline { { C } } \backslash \{ 0 \}$ rational with $\langle y , z \rangle = 0$ . But then some multiple of $z$ lies in ${ \overline { { C } } } \cap L \backslash \{ 0 \}$ , and hence some multiple of z lies in the co-core $\Sigma$ . But this contradicts the assumption that $H _ { y }$ is a supporting hyperplane of $\Sigma$ .

We have several things to check.

(1) Since $y \in C$ , it follows that $H _ { \mathrm { y } } \cap \Sigma$ is compact and so is supported by its extreme points. Since $H _ { y }$ is a supporting hyperplane, $E ( H _ { y } \cap \Sigma ) \subset E ( \Sigma )$ . By Proposition 5.16, $\begin{array} { r } { E ( H _ { y } \cap \Sigma ) \subset \frac { 1 } { M } L } \end{array}$ for some $M \in \mathbb { Z }$ , and so $H _ { \mathrm { y } } \cap \Sigma$ is the closed convex hull of a finite set of points. Therefore $\sigma _ { y }$ is truly a polyhedral cone, and so is each of its faces.

(2) By definition, $\mathcal { S }$ is $\Gamma \cdot$ -invariant and, if $\sigma \in \mathcal { S }$ , then any face of $\sigma$ is in $\mathcal { S }$ (3) We show that if $\sigma , \tau \in \mathcal { S }$ , then $\sigma \cap \tau$ is a face of both $\sigma$ and $\tau$ . First, suppose both $\sigma$ and $\tau$ are top-dimensional, so $\sigma = \sigma _ { y }$ and $\tau = \sigma _ { z }$ for some $y , z \in Y$ . Then $\sigma _ { y } = \mathbb { R } _ { \geq 0 } ( H _ { y } \cap \Sigma )$ and $\sigma _ { z } = \mathbb { R } _ { \geq 0 } ( H _ { z } \cap \Sigma )$ . Clearly, $\mathbb { R } _ { \geq 0 } ( H _ { z } \cap$ $H _ { \mathrm { y } } \cap \Sigma ) \subset \sigma _ { \mathrm { y } } \cap \sigma _ { z }$ . If $0 \neq w \in \sigma _ { y } \cap \sigma _ { z }$ , there exist $\lambda , \mu \in \mathbb { R } _ { > 0 }$ with $\lambda w \in H _ { y } \cap \Sigma$ and $\mu w \in H _ { z } \cap \Sigma$ . We must have $\lambda = \mu$ , for, if $\lambda > \mu$ , say, then $\langle \lambda w , y \rangle = 1 \Longrightarrow$ $\langle \mu w , y \rangle < 1 \Longrightarrow \mu w \notin \Sigma$ . Thus $\sigma _ { y } \cap \sigma _ { z } = \mathbb { R } _ { \ge 0 } ( H _ { z } \cap H _ { y } \cap \Sigma )$ . Since $H _ { z } \cap H _ { y } \cap \Sigma$ is a face of $H _ { \mathrm { y } } \cap \Sigma$ , we conclude that $\sigma _ { y } \cap \sigma _ { z }$ is a face of $\sigma _ { y }$ , and similarly of $\sigma _ { z }$ .

Now suppose $\sigma$ and $\tau$ are arbitrary, so that $\sigma = \sigma _ { y } \cap K _ { 1 } \cap K _ { 2 } \cap \cdot \cdot \cdot \cap K _ { n }$ , where $K _ { 1 } , \ldots , K _ { n }$ are supporting hyperplanes of $\sigma _ { y }$ , and $\tau = \sigma _ { z } \cap K _ { n + 1 } \cap \cdots \cap K _ { m }$ , where $K _ { n + 1 } , \ldots , K _ { m }$ are supporting hyperplanes of $\sigma _ { z }$ . Then $\pmb { \sigma } \cap \tau = \pmb { \sigma } _ { y } \cap \pmb { \sigma } _ { z } \cap$ $K _ { 1 } \cap \cdots \cap K _ { m }$ . We have just seen that there is a hyperplane $K$ supporting $\sigma _ { y }$ , so that $\sigma _ { y } \cap \sigma _ { z } = \sigma _ { y } \cap K$ . So

$$
\sigma \cap \tau = \sigma _ { \mathrm { y } } \cap K \cap K _ { 1 } \cap \cdots \cap K _ { m } = \sigma \cap K \cap K _ { n + 1 } \cap \cdots \cap K _ { m } .
$$

Since $\sigma \cap K \subset \sigma _ { y } \cap K = \sigma _ { y } \cap \sigma _ { z }$ , we know that $K _ { n + 1 } , \ldots , K _ { m }$ all support $\sigma \cap K$ , and $K$ supports $\sigma \subset \sigma _ { y }$ . Therefore $\sigma \cap \tau$ is a face of $\sigma$ . Similarly, it is a face of $\tau$ .

(4) Finally we show that $C \subset \bigcup _ { \sigma \in { \mathcal { S } } } \sigma$ and that $\mathcal { S }$ is a finite set modulo $\Gamma$

Let $\Pi _ { 1 } , \ldots , \Pi _ { n }$ be a fundamental set of rational polyhedra, as in the proof of the previous proposition.

For any $i \in \{ 1 , \ldots , n \}$ , we know that $\Sigma \cap \Pi _ { i }$ is cut out by a finite number of half-spaces. In fact, there are $w _ { 1 } , \ldots , w _ { m } \in V$ such that

$$
\Pi _ { i } = \left\{ z \in V \mid \langle w _ { k } , z \rangle \geq 0 \mathrm { ~ f o r ~ } k = 1 , \ldots , m \right\} ,
$$

and $x _ { 1 } , \dots , x _ { t } \in V , \lambda _ { 1 } , \dots , \lambda _ { t } \in \mathbb { R }$ such that

$$
\Sigma \cap \Pi _ { i } = \left\{ z \in \Pi _ { i } \mid \langle x _ { \ell } , z \rangle \geq \lambda _ { \ell } { \mathrm { ~ f o r ~ } } \ell = 1 , \ldots , t \right\} .
$$

Clearly, $\Sigma \cap \Pi _ { i }$ is the union of the semi-hulls over its faces of top dimension. A face giving such a top-dimensional semi-hull will be cut out by a hyperplane $K$ which supports $\Sigma \cap \Pi _ { i }$ such that there are $\nu _ { 1 } , \dots , \nu _ { N } \in K \cap \Sigma \cap \Pi _ { i }$ spanning $V$ and either

(i) $\left. w _ { k _ { 0 } } , \nu _ { a } \right. = 0$ for some $k _ { 0 } \in \{ 1 , \ldots , m \}$ and all $a = 1 , \ldots , N$ , or (ii) $\langle x _ { \ell _ { 0 } } , \nu _ { a } \rangle = \lambda _ { \ell _ { 0 } }$ for some $\ell _ { 0 } \in \{ 1 , \ldots , t \}$ and all $a = 1 , \ldots , N$ .

Obviously (i) is impossible because the $\nu _ { a }$ span $V$ , and (ii) is possible only if $\lambda _ { \ell _ { 0 } } \neq 0$ and $K = \{ z \in V \mid \langle x _ { \ell _ { 0 } } , z \rangle = \lambda _ { \ell _ { 0 } } \}$ . Letting $\begin{array} { r } { { \boldsymbol y } = \frac { 1 } { \lambda _ { \ell _ { 0 } } } { \boldsymbol x } _ { \ell _ { 0 } } } \end{array}$ , we have $K = H _ { y }$ . By definition, $y \in Y$ . Let $Y _ { 0 } \subset Y$ be the set of all $y$ obtained in this way. Clearly, $Y _ { 0 }$ is finite.

For any $x \in C$ , we have $\lambda x \in \Sigma$ for some $\lambda \in \mathbb { R } _ { > 0 }$ . Thus $\gamma \lambda x \in \Sigma \cap \Pi _ { i }$ for some $\gamma \in \Gamma$ and $i \in \{ 1 , \ldots , n \}$ , or, in other words, $\gamma x \in \sigma _ { y }$ for some $y \in Y _ { 0 }$ . Since $\Sigma$ is $\Gamma$ -invariant, this says $x \in \tau$ for some $\tau \in \mathcal S$ .

Meanwhile, for any $\tau \in \mathcal S$ , let $x \in \tau$ be in the interior. Then again $\gamma x \in \sigma _ { y }$ for some $y \in Y _ { 0 }$ and some $\gamma \in \Gamma$ . By (3) above, $\gamma \tau \cap \sigma _ { y }$ is a face of both $\gamma \tau$ and $\sigma _ { y }$ . Since $\gamma { x }$ lies in the interior of $\gamma \tau$ and in $\sigma _ { y }$ , this implies that $\gamma \tau$ is a face of $\sigma _ { y }$ . Since $Y _ { 0 }$ is a finite set, we are done.

# 5.4

Let $\Sigma$ be a $\Gamma$ -polyhedral kernel. It is easy to see from the definition and the proof of Proposition 5.18 that there are a finite number of points $x _ { 1 } , \ldots , x _ { n } \in$ $V ( \mathbb { Q } ) \cap { \overline { { C } } }$ such that

$$
\Sigma = \{ y \in \overline { { C } } \mid \langle y , ^ { t } \gamma x _ { i } \rangle \geq 1 \mathrm { ~ f o r ~ a l l ~ } \gamma \in \Gamma , i = 1 , \ldots , n \}
$$

In general, let $N$ be a positive integer and ${ \cal T } \subset \overline { { C } } \cap { \textstyle { \frac { 1 } { N } } } L ^ { \prime }$ (recall $L ^ { \prime } = L \backslash \{ 0 \} )$ . Denote $\Sigma _ { T } = \{ x \in \overline { { C } } \mid \langle x , y \rangle \geq 1$ for all $y \in T \}$ . Sometimes we will simply write $\Sigma$ if the $T$ is understood.

Proposition 5.19 For any $^ t \Gamma$ -invariant subset ${ \cal T } \subset \overline { { C } } \cap { \textstyle { \frac { 1 } { N } } } L ^ { \prime }$ , $\Sigma _ { T }$ is a Γ-polyhedral kernel.

Proof First, $\Sigma _ { T }$ is clearly closed, convex, and $\Gamma$ -invariant. Also $\mathbb { R } ^ { \geq 1 } \Sigma _ { T } \subset \Sigma _ { T }$ , $0 \not \in \Sigma _ { T }$ , and $C \subset \mathbb { R } _ { > 0 } \Sigma _ { T }$ . In other words, $\Sigma _ { T }$ is a kernel.

Let $\Pi$ be a polyhedral cone with rational vertices contained in $C ^ { * }$ . Since $\Pi$ can be written as the union of simplicial cones with rational vertices, we may assume that $\Pi$ is spanned by $z _ { 1 } , \dots , z _ { r } \in N L ^ { * } \cap \overline { { C } }$ , where $r = \dim V$ . Then

$$
\Pi = \left\{ \sum a _ { i } z _ { i } \mid a _ { i } \geq 0 { \mathrm { ~ f o r ~ } } i = 1 , \ldots , r \right\} .
$$

We want to show that there exists a finite set $t _ { 1 } , \dots , t _ { k } \in T$ such that, if $z \in \Pi$ and $\langle t _ { j } , z \rangle \geq 1$ for all $j = 1 , \dots , k$ , then $\langle t , z \rangle \geq 1$ for all $t \in T$ . For then we would have,

$$
\Pi \cap \Sigma _ { T } = \left\{ z \in \Pi \mid \langle z , t _ { j } \rangle \geq 1 { \mathrm { ~ f o r ~ a l l ~ } } j = 1 , \ldots , k \right\} .
$$

To do this we use the following. Let $\mathbb { Z } _ { \geq 0 }$ denote the non-negative integers. For $a = ( a _ { 1 } , \ldots , a _ { m } ) \in ( \mathbb { Z } _ { \geq 0 } ) ^ { m }$ and $b = ( b _ { 1 } , \dots , b _ { m } ) \in ( \mathbb { Z } _ { \geq 0 } ) ^ { m }$ , we write $b \geq a$ if and only if $b _ { i } \geq a _ { i }$ for all $i = 1 , \ldots , m$ .

Lemma 5.20 For any set $S \subset ( \mathbb { Z } _ { \geq 0 } ) ^ { m }$ , there exists a finite subset $S _ { 0 } \subset S$ such that, for all $b \in S _ { \mathrm { { \mathrm { * } } } }$ , there exists some $a \in S _ { 0 }$ with $b \geq a$ .

Proof For $m = 1$ , it is clear. We proceed by induction on $m$ , assuming the lemma for $m - 1$ . Let $\pi _ { j } : ( \mathbb { Z } _ { \geq 0 } ) ^ { m } \longrightarrow ( \mathbb { Z } _ { \geq 0 } ) ^ { m - 1 }$ be the projection omitting the $j ^ { \ast }$ th coordinate. Fix some $c = ( c _ { 1 } , \ldots , c _ { m } ) \in S$ . For each $j = 1 , \ldots , m$ and each $q = 0 , \ldots , c _ { j } - 1$ , write $S _ { j , q } = \{ s \in S \mid s _ { j } = q \}$ . By induction applied to $\pi _ { j } ( S _ { j , q } )$ , we get a finite set $S _ { j , q } ^ { 0 } \subset S _ { j , q }$ such that, for all $b \in S _ { j , q }$ , there exists some $a \in S _ { j , q } ^ { 0 }$ with $b \geq a$ . Now $\begin{array} { r } { \dot { \boldsymbol { S } } _ { 0 } = \bigcup _ { j , q } \boldsymbol { S } _ { j , q } ^ { 0 } \cup \{ c \} } \end{array}$ satisfies the lemma.

We continue with the proof of the proposition. Define $\Phi : L \cap { \overline { { C } } } \longrightarrow ( \mathbb { Z } _ { \geq 0 } ) ^ { r }$ by $\Phi ( y ) = ( \langle y , z \rangle , \dots , \langle y , z _ { r } \rangle )$ . Let $S _ { 0 } \subset \Phi ( T )$ be as in the lemma, and choose a section $\{ t _ { 1 } , \ldots , t _ { k } \}$ of $\Phi$ over $S _ { 0 }$ .

For any $\begin{array} { r } { z = \sum a _ { i } z _ { i } \in \Pi } \end{array}$ , suppose $\langle t _ { j } , z \rangle \geq 1$ for all $j = 1 , \dots , k$ . Then, for any $t \in T$ , there is a $j \in \left\{ { 1 , \ldots , k } \right\}$ such that $\langle t , z _ { i } \rangle \geq \langle t _ { j } , z _ { i } \rangle$ for all $i = 1 , \ldots , r .$ Thus

$$
\langle t , z \rangle = \sum a _ { i } \langle t , z _ { i } \rangle \geq \sum a _ { i } \langle t _ { j } , z _ { i } \rangle = \langle t _ { j } , z \rangle \geq 1
$$

because $a _ { i } \geq 0$ for all i. $\mathbf { S o } t _ { 1 } , \ldots , t _ { k }$ do the trick.

Proposition 5.21 If $\Sigma$ is a Γ-polyhedral kernel, then $\check { \Sigma }$ is a $^ t \Gamma$ -polyhedral kernel.

Proof By Corollary 5.12, we have that $\check { \Sigma } = \{ y \in \overline { { C } } \mid \langle y , \xi \rangle \geq 1$ for all $\xi \in \mathbf { \Xi }$ $E ( \Sigma ) \}$ . So what we want to show is that, given $\Pi$ , there exists a finite number of extreme points $\xi _ { 1 } , \dots , \xi _ { t } \in E ( \Sigma )$ such that if $z \in \Pi$ and $\langle \xi _ { i } , z \rangle \geq 1$ for $i =$ $1 , \ldots , t$ , then $\langle \xi , z \rangle \geq 1$ for every extreme point $\xi$ . This will follow precisely as in the proof of Proposition 5.19, if we use Proposition 5.16.

We can summarize all this as follows:

Proposition 5.22 The following three statements are equivalent:

(a) $\Sigma$ is a Γ-polyhedral kernel;   
(b) $\Sigma = \{ y \in \overline { { C } } \mid \langle y , ^ { t } \gamma x _ { i } \rangle \geq 1$ for all $\gamma \in \Gamma , i = 1 , \dotsc , n \}$ for some $x _ { 1 } , \ldots , x _ { n } \in$ $V ( \mathbb { Q } ) \cap { \overline { { C } } }$ ;   
(c) $\Sigma$ is the closed convex hull of

$$
\bigcup _ { i = 1 , \ldots , n \atop \gamma \in \Gamma } ( \gamma x _ { i } + C )
$$

for some $x _ { 1 } , \ldots , x _ { n } \in V ( \mathbb { Q } ) \cap { \overline { { C } } }$ .

Apply this to $\Sigma _ { 1 } , \Sigma _ { 2 } , \check { \Sigma } _ { 1 } , \check { \Sigma } _ { 2 }$ of (5.1):

$$
\Sigma _ { 2 } = \left\{ x \in \overline { { C } } \mid \langle x , y \rangle \geq 1 \mathrm { ~ f o r ~ a l l ~ } y \in \overline { { C } } \cap L ^ { \prime } \right\}
$$

and

$$
\check { \Sigma } _ { 1 } = \{ x \in \overline { { C } } \mid \langle x , y \rangle \geq 1 \mathrm { ~ f o r ~ a l l ~ } y \in C \cap L \}
$$

are rationally locally polyhedral by Proposition 5.19. Then, by Proposition 5.21, the same is true of

$$
\Sigma _ { 1 } = \check { \check { \Sigma } } _ { 1 } = \mathrm { c l o s e d c o n v e x h u l l o f } C \cap L
$$

and

$$
\breve { \Sigma } _ { 2 } = \mathrm { c l o s e d c o n v e x h u l l o f } \overline { { C } } \cap L ^ { \prime } .
$$

To obtain $\Gamma$ -admissible decompositions of the cone, we need only take into account Proposition 5.18.

Now $\check { \Sigma } _ { 2 }$ is $\Gamma$ -invariant, but $\check { \Sigma } _ { 1 }$ is only $^ t \Gamma$ -invariant. We may use instead $\check { \Sigma } _ { 1 } ^ { * } = \{ x \in \overline { { C } } | \langle x , y \rangle \geq 1$ for all $y \in C \cap L ^ { * } \}$ . Then we may summarize:

Corollary 5.23 Taking cones over the faces of the closed convex hull of $\overline { { C } } \cap L ^ { \prime }$ (resp. $\left\{ x \in { \overline { { C } } } \mid \left. x , y \right. \geq 1 \right.$ for all $y \in C \cap L ^ { * } \}$ ) yields a $\Gamma$ -admissible polyhedral decomposition of $C$ .

The first kind is called a Voronoi decomposition (of the first type) and the second is called a decomposition into central cones, since in each case they generalize known constructions for the cone of positive-definite quadratic forms in a given number of variables.

# 6 Positive-definite forms in low dimensions

We consider the most classical example of the above theory:

$$
\begin{array} { l } { { V _ { n } = \mathrm { v e c t o r ~ s p a c e ~ o f ~ s y m m e t r i c } \ n \times n \ \mathrm { r e a l ~ m a t r i c e s } \ ; } } \\ { { \nonumber } } \\ { { C _ { n } = \mathrm { c o n e ~ o f ~ p o s i t i v e ~ d e f n i t e ~ e l e m e n t s } \ \mathrm { i n } \ V _ { n } \ . } } \end{array}
$$

Then $V _ { n }$ has a natural $\mathbb { Q }$ -structure given by the rational $n \times n$ matrices and is a Jordan algebra via

$$
\begin{array} { r } { X \cdot Y = \frac { 1 } { 2 } ( X Y + Y X ) . } \end{array}
$$

So Aut $\left( C _ { n } \right)$ is just $\mathrm { { G L } } ( n , \mathbb { R } ) / ( \pm I _ { n } )$ acting via

$$
{ \cal X } \longmapsto { } ^ { t } { \cal A } { \cal X } { \cal A } , \quad { \cal A } \in { \bf G } { \bf L } ( n , \mathbb { R } ) \ ,
$$

and the characteristic function of the cone is given by

$$
\varphi ( X ) = { \frac { 1 } { \operatorname* { d e t } ( X ) ^ { ( n + 1 ) / 2 } } } \ .
$$

There are two natural lattices in $V _ { n }$ :

$$
\begin{array} { l } { { L _ { n } = \mathrm { i n t e g r a l } n \times n { \mathrm { - m a t r i c e s } } X , } } \\ { { L _ { n } ^ { * } = \mathrm { s e m i - i n t e g r a l } n \times n { \mathrm { - m a t r i c e s } } X , } } \end{array}
$$

i.e.,

$$
L _ { n } ^ { * } = \left\{ X \in V _ { n } \mid X _ { i i } \in \mathbb { Z } , X _ { i j } \in { \frac { 1 } { 2 } } \mathbb { Z } { \mathrm { ~ i f ~ } } i \neq j \right\} .
$$

If $I _ { n } \in C _ { n }$ is taken as the basepoint, we get the inner product

$$
\langle X , Y \rangle = \operatorname { T r } \left( X Y \right)
$$

on $V _ { n }$ for which:

(i) $C _ { n }$ is self-adjoint;   
(ii) $\mathrm { S t a b } \left( I _ { n } \right) = O ( n , \mathbb { R } ) / ( \pm I _ { n } )$ acts orthogonally;   
(iii) its polar complement $P$ , the set of symmetric matrices in $\mathrm { G L } ( n , \mathbb { R } )$ , acts by self-adjoint maps; and   
(iv) the notation $L _ { n } ^ { * }$ is justified:

$$
L _ { n } ^ { * } = \{ x \in V _ { n } \mid \langle x , y \rangle \in \mathbb { Z } { \mathrm { ~ f o r ~ a l l ~ } } y \in L _ { n } \} ~ .
$$

The arithmetic group

$$
\Gamma _ { n } = \mathbf { G } \mathbf { L } ( n , \mathbb { Z } ) / ( \pm I _ { n } )
$$

preserves both lattices. The rational boundary components of  ;; $C _ { n }$ correspond one-to-one with the subspaces $W \subset \mathbb { R } ^ { n }$ defined over $\mathbb { Q }$ , the correspondence being given by

$$
W \longleftrightarrow C ( W ) = \left\{ X \in V _ { n } { \left| \begin{array} { l } { X { \mathrm { ~ p o s i t i v e ~ s e m i - d e f i n i t e } } } \\ { { \mathrm { ~ w i t h ~ n u l l ~ s p a c e ~ } } W } \end{array} \right. } \right\} .
$$

Thus

$$
\left. \begin{array} { l } { C _ { n } ^ { * } = C _ { n } \cup \bigcup _ { W } C ( W ) } \\ { \qquad = \left. X \in V _ { n } \Big \vert \begin{array} { l } { X \mathrm { p o s i t i v e ~ s e m i – d e f i n i t e } } \\ { \mathrm { w i t h ~ r a t i o n a l ~ n u l l ~ s p a c e ~ } W } \end{array} \right. . } \end{array} \right.
$$

The problem of finding an explicit decomposition of $C _ { n } ^ { * }$ into rational polyhedral cones $\{ \sigma _ { \alpha } \}$ invariant under ; $\Gamma _ { n }$ , and hence of finding a fundamental domain for $\Gamma _ { n }$ , is a very old one. For all ; $n$ , an important role is played by the fundamental cone $\phi _ { n } \subset C _ { n } ^ { * }$ :

$$
\phi _ { n } = \left\{ X \in V _ { n } \Big | \begin{array} { l } { \mathrm { o f f - d i a g o n a l \ e n t r i e s } \ X _ { i j } \mathrm { \ n o n { - } p o s i t i v e } } \\ { \mathrm { r o w \ s u m s } \sum _ { i = 1 } ^ { n } X _ { i j } \mathrm { \ n o n { - } n e g a t i v e } } \end{array} \right\} .
$$

In fact, $\phi _ { n }$ is a simplicial cone, being expressible also as

$$
\phi _ { n } = \left\{ \sum _ { i = 1 } ^ { n } \lambda _ { i } x _ { i } ^ { 2 } + \sum _ { 1 \leq i < j \leq n } \lambda _ { i j } ( x _ { i } - x _ { j } ) ^ { 2 } \Big | \lambda _ { i } \geq 0 , \lambda _ { i j } \geq 0 \right\} .
$$

In some areas of applied mathematics, the cone $\phi _ { n }$ plays a role – basically because the inequalities $x _ { i j } \le 0$ for $i \neq j$ and $\textstyle \sum _ { i = 1 } ^ { n } x _ { i j } \geq 0$ are the simplest linear way to force a matrix to be positive semi-definite. A basic result is:

$$
C _ { n } ^ { * } = \bigcup _ { \gamma \in \mathrm { G L } ( n , \mathbb { Z } ) } \gamma \phi _ { n } \Longleftrightarrow n \leq 3 .
$$

This illustrates the interesting fact that only in 4-space or higher do lattice packing problems and related geometry of numbers problems get interesting. For $n = 2$ or 3, however, all “reasonable” admissible polyhedral decompositions of $C _ { n } ^ { * }$ are based on $\left\{ \gamma \phi _ { n } \right\}$ – either $\{ \sigma _ { \alpha } \}$ equals $\left\{ \gamma \phi _ { n } \right\}$ , or it equals $\{ \gamma \psi _ { i } \}$ , where $\left\{ \psi _ { i } \right\}$ is a decomposition of $\phi _ { n }$ . Thus the standard fundamental domain for $n = 2$ ,

$$
\tilde { \phi } _ { 2 } = \left\{ \left( \begin{array} { c c } { { a } } & { { - b } } \\ { { - b } } & { { c } } \end{array} \right) \Big | 0 \leq 2 b \leq a \leq c \right\} ,
$$

comes about by barycentric subdivision of $\phi _ { 2 }$ :

![](images/60e40fd4bfb5edf56f8c97f21a4e5439a4fd011da86a86ce17dae8ab4d963d0b.jpg)

Since $\phi _ { 2 }$ is mapped into itself by the group of order six,

$$
\left\{ I _ { 2 } , \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right) , \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - 1 } } & { { 1 } } \end{array} \right) , \left( \begin{array} { c c } { { 1 } } & { { - 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right) , \left( \begin{array} { c c } { { 1 } } & { { - 1 } } \\ { { 0 } } & { { - 1 } } \end{array} \right) , \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 1 } } & { { - 1 } } \end{array} \right) \right\} ,
$$

we see that $\tilde { \phi } _ { 2 } \cap \gamma \tilde { \phi } _ { 2 }$ is at most a face of $\tilde { \phi } _ { 2 }$ , if $\gamma \neq \mathrm { i d }$

For $n \geq 4$ , we need more cones. To find them systematically, we use a cocore. In fact, there are apparently two very natural co-cores in $C _ { n }$ , which we call the perfect and central co-cores:

$$
\begin{array} { r l } & { K _ { \mathrm { p e r f } } = \mathrm { t h e ~ c l o s e d ~ c o n v e x ~ h u l l ~ o f ~ } L _ { n } ^ { * } \cap \overline { { C } } _ { n } \setminus \{ 0 \} \mathrm { ~ ; ~ } } \\ & { K _ { \mathrm { c e n t } } = \left\{ X \in \overline { { C } } _ { n } \ : \big | \ : \mathrm { T r } \left( X Y \right) \geq 1 \ : \mathrm { f o r ~ a l l ~ } Y \in L _ { n } ^ { * } \cap C _ { n } \right\} . } \end{array}
$$

The dual cores are:

$$
\begin{array} { r l } & { \check { K } _ { \mathrm { p e r f } } = \left\{ X \in C _ { n } \ : | \ : \mathrm { T r } \left( X Y \right) \geq 1 \ : \mathrm { f o r } \ : \mathrm { a l l } \ : Y \in L _ { n } ^ { * } \cap \overline { { C } } _ { n } \ : \setminus \left\{ 0 \right\} \right\} } \\ & { \check { K } _ { \mathrm { c e n t } } = \mathrm { t h e } \ : \mathrm { c l o s e d } \ : \mathrm { c o n v e x } \ : \mathrm { h u l l } \ : \mathrm { o f } \ : L _ { n } ^ { * } \cap C _ { n } . } \end{array}
$$

According to a result of Barnes and Cohn [2],

$$
\operatorname* { m i n } _ { Y \in L _ { n } ^ { * } \cap \overline { { { C } } } _ { n } \setminus \{ 0 \} } \mathrm { T r } \left( X Y \right) = \operatorname* { m i n } _ { m \in \mathbb { Z } ^ { n } \setminus \{ 0 \} } { { ^ t } m X m } \ ,
$$

and hence we get a second definition of the perfect co-core and core:

$$
\begin{array} { r l } & { \check { K } _ { \mathrm { p e r f } } = \left\{ X \in C _ { n } \middle | { } ^ { t } m X m \geq 1 \mathrm { ~ f o r ~ a l l ~ } m \in \mathbb { Z } ^ { n } \setminus \left\{ 0 \right\} \right\} ; } \\ & { K _ { \mathrm { p e r f } } = \mathrm { c l o s e d ~ c o n v e x ~ h u l l ~ o f ~ t h e ~ r a n k - 1 ~ m a t r i c e s ~ } X _ { i j } } \end{array}
$$

Furthermore,

$$
\mu ( X ) = \operatorname* { m i n } _ { m \in \mathbb { Z } ^ { n } \setminus \{ 0 \} } t _ { m X m }
$$

is the piecewise-linear function which is 1 on $\partial \check { K } _ { \mathrm { p e r f } }$ .

Finally, we say that a form $X \in C _ { n }$ is perfect, (resp. central), if it is a vertex of $\check { K } _ { \mathrm { p e r f } }$ , (resp. $\check { K } _ { \mathrm { c e n t . } }$ ). By the general theory, perfect (resp. central) forms correspond one-to-one with the top-dimensional faces of $K _ { \mathrm { p e r f } }$ , (resp. $K _ { \mathrm { c e n t } } )$ , hence to the $\frac { n ( n + 1 ) } { 2 }$ -dimensional cones in the decomposition of $C _ { n }$ defined by $K _ { \mathrm { p e r f } }$ , (resp. $K _ { \mathrm { c e n t } }$ ), which we call the perfect cones (resp. central cones). In the case of perfect forms, we see easily that $X$ is perfect if and only if $\mu ( X ) = 1$ and $X$ is the only solution to the equations

$$
{ } ^ { t } m Y m = 1 { \mathrm { ~ f o r ~ a l l ~ } } m \in \mathbb { Z } ^ { n } { \mathrm { ~ s u c h ~ t h a t ~ } } ^ { t } m X m = 1 ,
$$

and that the corresponding perfect cone is the convex hull of the rank-1 forms $X _ { i j } = m _ { i } m _ { j }$ for all $m \in \mathbb { Z } ^ { n }$ such that ${ } ^ { t } m X m = 1$ . Central cones, on the other hand, are given by

$$
\begin{array} { r } { \sigma _ { Y } = \left\{ X \in C _ { n } ^ { * } \mid \mathrm { T r } \left( X Y \right) \leq \mathrm { T r } \left( X Z \right) \mathrm { f o r } \mathrm { a l l } Z \in L _ { n } ^ { * } \cap C _ { n } \right\} , } \end{array}
$$

where $Y$ is a central form.

For $n \leq 6$ , all perfect forms have been listed; see [1] and [6]. For example, consider the form

$$
\alpha _ { n } = { \frac { 1 } { 2 } } \left( x _ { 1 } ^ { 2 } + \cdots + x _ { n } ^ { 2 } + ( x _ { 1 } + \cdots + x _ { n } ) ^ { 2 } \right)
$$

corresponding to the matrix

$$
\left( \begin{array} { l l l l } { 1 } & { \frac 1 2 } & { \cdots } & { \frac 1 2 } \\ { \frac 1 2 } & { 1 } & { \cdots } & { \frac 1 2 } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { \frac 1 2 } & { \frac 1 2 } & { \cdots } & { 1 } \end{array} \right) .
$$

Note that $\alpha _ { n }$ , up to unimodular equivalence, may be described as the Killing form for the root system $A _ { n }$ , written with respect to a basis of the lattice generated by the roots. This may be shown to be both perfect and central and it corresponds to a common face of $K _ { \mathrm { c e n t } }$ and $K _ { \mathrm { p e r f } }$ , namely the simplex in $C _ { n } ^ { * }$ with vertices $x _ { i } ^ { 2 }$ , $( x _ { i } - x _ { j } ) ^ { 2 }$ , where $1 \leq i , j \leq n$ . This shows that $\phi _ { n }$ is both a central and a perfect cone.

Another important form is

$$
\delta _ { n } = { \frac { 1 } { 2 } } \left( ( x _ { 1 } - x _ { 2 } ) ^ { 2 } + x _ { 3 } ^ { 2 } + \cdots + x _ { n } ^ { 2 } + ( x _ { 1 } + \cdots + x _ { n } ) ^ { 2 } \right)
$$

corresponding to the matrix⎜⎜

$$
\left( \begin{array} { l l l l l } { 1 } & { 0 } & { \frac { 1 } { 2 } } & { \cdots } & { \frac { 1 } { 2 } } \\ { 0 } & { 1 } & { \frac { 1 } { 2 } } & { \cdots } & { \frac { 1 } { 2 } } \\ { \frac { 1 } { 2 } } & { \frac { 1 } { 2 } } & { 1 } & { \cdots } & { \frac { 1 } { 2 } } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { \frac { 1 } { 2 } } & { \frac { 1 } { 2 } } & { \frac { 1 } { 2 } } & { \cdots } & { 1 } \end{array} \right) .
$$

Note that $\delta _ { n }$ , up to unimodular equivalence, may be described as the Killing form for the root system $D _ { n }$ , written with respect to a basis of the lattice generated by the roots. This form is also both perfect and central, but it does not seem to be known whether it defines identical faces of $K _ { \mathrm { c e n t } }$ and $K _ { \mathrm { p e r f } }$ .

Note that

$$
K _ { \mathrm { c e n t } } \supseteq K _ { \mathrm { p e r f } } \ : ; \ : \check { K } _ { \mathrm { c e n t } } \subseteq \check { K } _ { \mathrm { p e r f } } \ : .
$$

It may be shown that equality holds if and only if $n \leq 5$ . In particular, for $n = 4$ , $K _ { \mathrm { c e n t } } = K _ { \mathrm { p e r f } } $ , and forms are perfect if and only if they are central. It turns out that, in this case, $\alpha _ { 4 } , \delta _ { 4 }$ , and their images under $\Gamma _ { 4 }$ are the only perfect forms; hence, if $\psi _ { 4 }$ is the perfect cone corresponding to $\delta _ { 4 }$ , we conclude that, for $n = 4$ , the cones $\gamma \phi _ { 4 }$ and $\gamma \psi _ { 4 }$ for $\gamma \in \Gamma _ { 4 }$ form an admissible polyhedral decomposition of $C _ { 4 } ^ { * }$ .

# References

[1] E. S. Barnes, The complete enumeration of extreme senary forms, Phil. Trans. Royal Soc. London 249 (1957), 461–506.   
[2] E. S. Barnes and M. J. Cohn, On the inner product of positive quadratic forms, J. London Math. Soc. 12 (2) (1975/76), 32–36.   
[3] A. Borel, Introduction aux Groupes Arithmetiques. Paris: Hermann, 1969. [4] A. Borel and J.-P. Serre, Corners and arithmetic groups, Comm. Math. Helv. 48 (1973), 436–491.   
[5] H. Braun and M. Koecher, Jordan-Algebren. Berlin: Springer-Verlag, 1966. [6] H. S. M. Coxeter, Extreme forms, Canad. J. Math. 3 (1951), 391–441. [7] N. Jacobson, Structure and Representations of Jordan Algebras. Providence, RI: American Mathematical Society, 1968.   
[8] M. Koecher, Jordan Algebras and their Applications. Lecture Notes. University of Minnesota, 1962. [9] E. Looijenga, Semi-Toric Partial Compactifications I. Preprint series of Department of Mathematics, Catholic University, Nijmegen, The Netherlands, June 1985.   
[10] O. Loos, Symmetric Spaces I: General Theory. New York: Benjamin, 1969.   
[11] D. Mumford, Geometric Invariant Theory. Berlin: Springer-Verlag, 1965. [12] R. T. Rockafellar, Convex Analysis. Princeton, NJ: Princeton University Press, 1970.   
[13] T. A. Springer, Jordan Algebras and Algebraic Groups. Berlin: Springer-Verlag, 1973.   
[14] G. Voronoi, Nouvelles applications des parametres continus \` a la th \` eorie ´ des formes quadratiques I, J. Reine Angew. Math. 133 (1907), 97–178.

# III

Compactifications of locally symmetric varieties

This chapter presents the main results of this book. In order to make the book reasonably self-contained, and because of the difficulty in assembling the known results from a very diffuse and often hard-to-read literature, we have tried to include, with at least sketches of proof, a large proportion of the needed background on hermitian symmetric spaces. We have profited greatly from lectures on hermitian symmetric spaces given by P. Deligne in Paris in 1973. Large parts of Sections 2 and 3 are no more than an elaboration of his work. One of us (Rapoport) profited also from conversations with R. P. Langlands.

Section 1 explains the method of compactification in the case of a tube domain; some of the facts established there are used later. This is also done in Satake [10].

Sections 2, 3, and 4 review facts about hermitian symmetric domains and their boundary theory. In addition to help from Deligne and Langlands, we have used principally Helgason [6] and Wolf [12], but also Harish-Chandra [5], Langlands [8], Koranyi and Wolf [7], and Satake [11].

Section 5 states the Main Theorem; Section 6 contains its proof. Here basic facts from the fundamental paper by Baily and Borel [1] are used. For the reduction theory, we have found the book by Borel [2] very useful.

Finally Section 7 contains a more intrinsic formulation of the Main Theorem.

# 1 Tube domains and compactification of their cusps

Let $N _ { \mathbb { R } }$ be a finite-dimensional $\mathbb { R }$ -vector space and let $C \subset N _ { \mathbb { R } }$ be a homogeneous self-adjoint cone. Set $\overline { { G } } = \mathrm { A u t } ( C , N _ { \mathbb { R } } ) ^ { o }$ (this notation thus differs from that in Chapter II).

Definition 1.1 The open subset

$$
U = N _ { \mathbb { R } } + \mathrm { i } C = \left\{ x + \mathrm { i } y \mid x \in N _ { \mathbb { R } } , y \in C \right\}
$$

of $N _ { \mathbb { C } }$ is called a tube domain.

Let $G$ be the group of complex-analytic automorphisms of $U$

# Proposition 1.2

(1) $U$ is a bounded symmetric domain.   
(2) $G _ { : }$ , equipped with the compact open topology, is a Lie group.

Proof (2) follows from (1) by general theory: $U$ , as a bounded domain, is equipped with the Bergman metric. Moreover, $G$ is a closed subgroup of the Lie group of isometries with respect to this metric. Thus $G$ itself is a Lie group.

To see that $U$ is a bounded domain, choose a basis of $N _ { \mathbb { R } }$ such that $C \subset \{ y _ { 1 } >$ $0 , \ldots , y _ { n } > 0 \}$ (this is obviously possible). This embeds $U$ into ${ \mathfrak { H } } ^ { n }$ , where as usual ${ \mathfrak H }$ denotes the upper half-plane. Since ${ \mathfrak H }$ is a bounded domain (isomorphic to the unit disc), so is ${ \mathfrak { H } } ^ { n }$ and thus also $U$ .

To see that $U$ is a homogeneous domain, note that the real translations by $N _ { \mathbb { R } }$ and the complex-linear extensions of the linear maps in $\overline { G }$ take $U$ to $U$ and act transitively on $U$ .

Finally, to see that $U$ is symmetric, it suffices to construct an involutive symmetry around the point $\mathrm { i } e \in U$ (here $e = a$ , the basepoint in $C$ ). As in Chapter II, Section 2, we describe $C$ as the set of exponentials for a real Jordan algebra structure on $N _ { \mathbb { R } }$ with identity $e$ ; this algebra structure extends to a complex Jordan algebra structure on $N _ { \mathbb { C } }$ . We claim that, in this algebra structure, every $x \in U$ is invertible, that $- x ^ { - 1 } \in U$ , and that the map $x \longmapsto - x ^ { - 1 }$ is the required symmetry. But for any algebra structure with identity $e$ , we have that $- ( \mathrm { i } e ) ^ { - 1 } = \mathrm { i } e$ , and $x \longmapsto - x ^ { - 1 }$ is an involution near ie with no other fixed point. It remains to show that every $x \in U$ is Jordan-invertible and that $- x ^ { - 1 } \in U$ . First of all, for every $g \in { \overline { { G } } }$ , we claim that

$x$ invertible implies $g x$ invertible, and $( g x ) ^ { - 1 } = \sigma ( g ) \cdot x ^ { - 1 } ,$ where $\sigma : \overline { { G } } \longrightarrow \overline { { G } }$ is the Cartan involution fixing $\overline { { G } } \cap \mathbf { S t a b } \left( e \right)$ . In fact, we saw in Chapter $\mathrm { I I }$ , Section 2, that $( g \cdot e ) ^ { - 1 } = \sigma ( g ) \cdot e$ , hence if $g , g _ { 1 } \in { \overline { { G } } }$ , then

$$
( g \cdot g _ { 1 } \cdot ( \mathrm { i } e ) ) ^ { - 1 } = - \mathrm { i } \sigma ( g \cdot g _ { 1 } ) \cdot e = - \mathrm { i } \sigma ( g ) \cdot \sigma ( g _ { 1 } ) \cdot e = \sigma ( g ) \cdot ( g _ { 1 } \cdot ( \mathrm { i } e ) ) ^ { - 1 } \ ,
$$

i.e., (1.1) holds for $x \in \mathrm { i } C$ . By analytic continuation it holds for all invertible $x \in$ $N _ { \mathbb { C } }$ . This reduces our problem to showing that, for all $x \in N _ { \mathbb { R } }$ , $x + \mathrm { i } e$ is invertible and $- ( x + \mathrm { i } e ) ^ { - 1 } \in U$ . To see this, let $\mathbb { R } [ x ]$ be the real Jordan subalgebra of $N _ { \mathbb { R } }$ generated by $x$ and $e$ . As in Chapter II, $\mathbb { R } [ x ] \cong \Sigma _ { i = 1 } ^ { n } \mathbb { R } \varepsilon _ { i }$ , where $\varepsilon _ { i }$ are idempotents, and $\begin{array} { r } { \mathbb { R } [ x ] \cap C \cong \sum _ { i = 1 } ^ { n } \mathbb { R } _ { > 0 } \pmb { \varepsilon } _ { i } } \end{array}$ . Indeed, $C$ is self-adjoint w.r.t. the pairing $\langle y , z \rangle = \mathrm { T r } \left( L _ { y \cdot z } \right)$ by Chapter $\mathrm { I I }$ , Theorem 2.13. Then, for $\begin{array} { r } { y = \sum _ { i = 1 } ^ { n } y _ { i } \pmb { \varepsilon } _ { i } \in \pmb { \mathrm { ~ } } } \end{array}$ $\mathbb { R } [ x ] \cap C$ , we have

$$
y _ { i } \langle \pmb { \varepsilon } _ { i } , \pmb { \varepsilon } _ { i } \rangle = \langle y \pmb { \varepsilon } _ { i } , \pmb { \varepsilon } _ { i } \rangle = \langle y , \pmb { \varepsilon } _ { i } ^ { 2 } \rangle > 0 ,
$$

and hence $\boldsymbol { y } \in \Sigma _ { i = 1 } ^ { n } \mathbb { R } _ { > 0 } \pmb { \varepsilon } _ { i }$ . Conversely, any such element is a square of an invertible element and thus lies in $C$ . Since $x + \mathrm { i } e$ lies in the subalgebra $\mathbb { C } [ x ]$ , we are reduced to checking the one-dimensional case $N _ { \mathbb { R } } = \mathbb { R }$ . But it is obvious that, for all $a \in \mathbb { R }$ , $a + \mathrm { i } \in \mathbb { C }$ is invertible and $- ( a + \mathrm { i } ) ^ { - 1 } \in \mathfrak { H }$ , the upper halfplane. □

Now start with

(1) an algebraic group $\mathcal { G }$ over $\mathbb { Q }$ such that   
(2) its associated Lie group $G = \mathcal { G } ( \mathbb { R } ) ^ { o }$ is the connected component of the group of complex-analytic automorphisms of $U$ .

We also assume that

(3) the subgroup $P \subset G$ , which is the semi-direct product of $\overline { { G } } = \mathrm { A u t } ( C , N _ { \mathbb { R } } ) ^ { o }$ by the group of real translations $N _ { \mathbb { R } }$ , is defined over $\mathbb { Q }$ , i.e., $P = \mathcal { P } ( \mathbb { R } ) ^ { o }$ , where $\mathcal { P } \subset \mathcal { G }$ is an algebraic subgroup defined over $\mathbb { Q }$ . This defines a rational structure on $N _ { \mathbb { R } }$ and $\overline { G }$ such that $\overline { G }$ acts rationally on $N _ { \mathbb { R } }$ .

Let $\Gamma \subset { \mathcal { G } } ( \mathbb { Q } ) \cap G$ be an arithmetic subgroup. Let $N _ { \mathbb { Z } }$ be the group of translations contained in $\Gamma$ : this is a lattice in $N _ { \mathbb { R } }$ . We set $\overline { { \Gamma } } = ( \Gamma \cap P ) / N _ { \mathbb { Z } }$ , which is the image of $\Gamma$ via $P \longrightarrow \overline { { G } }$ .

Here is an example of the situation we consider.

# Example 1.3 (Siegel case)

$N _ { \mathbb { R } } = \operatorname { S y m } ^ { 2 } ( \mathbb { R } ^ { n } )$ ; $C$ is the cone of positive-definite quadratic forms on $\mathbb { R } ^ { n }$ ; $U$ is the Siegel upper half space in $\mathbb { C } ^ { n ( n + 1 ) / 2 }$ ; $\begin{array} { r l } & { G = { \mathrm { S p } } \left( 2 n , \mathbb { R } \right) / \left\{ \pm 1 \right\} , \Gamma = { \mathrm { S p } } \left( 2 n , \mathbb { Z } \right) / \left\{ \pm 1 \right\} ; } \\ &  { { \overline { { G } } } = \mathrm { G L } \left( n , \mathbb { R } \right) / \left\{ \pm 1 \right\} , { \overline { { \Gamma } } = \mathrm { G L } \left( n , \mathbb { Z } \right) / \left\{ \pm 1 \right\} } ; } \\ & { \left( \begin{array} { l l } { a } & { b } \\ { a } & { d } \end{array} \right) \in G \mathrm { a c t s ~ o n ~ } U \mathrm { ~ b y ~ } z \longmapsto \left( a z + b \right) \cdot \left( c z + d \right) ^ { - 1 } ; } \\ & { \left( \begin{array} { l l } { a } & { 0 } \\ { 0 } & { { ^ { t } a ^ { - 1 } } } \end{array} \right) \in { \overline { { G } } } \mathrm { ~ a c t s ~ o n ~ } N _ { \mathbb { R } } \mathrm { ~ b y ~ } x \longmapsto a \cdot x \cdot { ^ { t } a } ; } \\ & { P = \left( \begin{array} { l l } { * } & { * } \\ { 0 } & { * } \end{array} \right) \cap { \mathrm { S p } } \left( 2 n , \mathbb { R } \right) / \left\{ \pm 1 \right\} . } \end{array}$

Let $\{ \sigma _ { \alpha } \}$ be a $\overline { { \Gamma } }$ -admissible polyhedral decomposition of $C$ . We now come to the main idea of this whole volume.

Let $T = N _ { \mathbb { C } } / N _ { \mathbb { Z } }$ : this is a torus in the algebraic group sense with

$$
\begin{array} { r } { N _ { \mathbb { Z } } \cong \operatorname { H o m } \big ( \mathbb { G } _ { m } , T \big ) , } \end{array}
$$

the group of one-parameter subgroups of $T$ .

As in Chapter I, we have an exact sequence:

$$
0 \longrightarrow T _ { c } \longrightarrow T \stackrel { \mathrm { o r d } } { \longrightarrow } N _ { \mathbb { R } } \longrightarrow 0 .
$$

Since $U$ is $N _ { \mathbb { Z } }$ -invariant, it is the inverse image of an open subset $U ^ { \prime } \subset T$ ; alternatively, $U ^ { \prime } = { \mathrm { o r d } } ^ { - 1 } ( C )$ . For every $\varepsilon \in C$ , set

$$
C _ { \varepsilon } = C + \varepsilon \ , \ U _ { \varepsilon } = N _ { \mathbb { R } } + \mathrm { i } C _ { \varepsilon } \ , \ U _ { \varepsilon } ^ { \prime } = \mathrm { o r d } ^ { - 1 } ( C _ { \varepsilon } ) = U _ { \varepsilon } / N _ { \mathbb { Z } } \ .
$$

(The $U _ { \varepsilon }$ are nothing but Piatetskii-Shapiro’s cylindrical sets.) Next, by the theory of TE I†, $\{ \sigma _ { \alpha } \}$ defines a $T$ -equivariant embedding:

$$
T \subset X _ { \{ \sigma _ { \alpha } \} } \ .
$$

Let

$$
\begin{array} { r l } & { U ^ { \prime \prime } = \operatorname { i n t e r i o r \ o f \ t h e \ c l o s u r e \ o f } U ^ { \prime } \operatorname { i n } X _ { \{ \sigma _ { \alpha } \} } \ ; } \\ & { U _ { \varepsilon } ^ { \prime \prime } = \operatorname { i n t e r i o r \ o f \ t h e \ c l o s u r e \ o f } U _ { \varepsilon } ^ { \prime } \operatorname { i n } X _ { \{ \sigma _ { \alpha } \} } \ . } \end{array}
$$

Now, $\overline { { \Gamma } }$ acts on $\{ \sigma _ { \alpha } \}$ , as well as on $T$ . So $\overline { { \Gamma } }$ acts on $X _ { \{ \sigma _ { \alpha } \} }$ , prolonging its action on $T$ ; this action preserves $U ^ { \prime \prime }$ .

# Theorem 1.4

(i) $\overline { { \Gamma } }$ acts properly discontinuously on $U ^ { \prime \prime }$ . (ii) $( \overline { { \Gamma } } \cdot U _ { \varepsilon } ^ { \prime \prime } ) / \overline { { \Gamma } }$ is open and relatively compact in $U ^ { \prime \prime } / \overline { { \Gamma } }$

We use the commutative diagram introduced in Chapter I, Section 1:

$$
\begin{array} { c c c c } { { X _ { \{ \sigma _ { \alpha } \} } } } & { { \xrightarrow [ ] { \mathrm { ~ \ o r d ~ \_ ~ } } } } & { { N _ { \{ \sigma _ { \alpha } \} } } } \\ { { \cup } } & { { } } & { { } } & { { \cup } } \\ { { T } } & { { \xrightarrow [ ] { \mathrm { ~ \ o r d ~ \_ ~ } } } } & { { N _ { \mathbb { R } } } } \\ { { \cup } } & { { } } & { { } } & { { \cup } } \\ { { U ^ { \prime } } } & { { } } & { { } } & { { C } } \end{array}
$$

Proof of (i) We know that ord is a continuous $\overline { { \Gamma } }$ -equivariant map. It thus suffices to show that $\overline { { \Gamma } }$ acts properly discontinuously on ord $( U ^ { \prime \prime } )$ . Because ord is a quotient map by the compact group $T _ { c }$ by Chapter I, and, in particular, an open map, $U ^ { \prime \prime } { = } \operatorname { o r d } ^ { - 1 } ( C ^ { \prime \prime } )$ , where $C ^ { \prime \prime }$ is the interior of the closure of $C$ inside

$N _ { \{ \sigma _ { \alpha } \} }$ . As in Chapter I, Section 1, we can describe the points of $N _ { \{ \sigma _ { \alpha } \} }$ by symbols $x + \infty \cdot \sigma _ { \alpha }$ , for $x \in N _ { \mathbb { R } }$ , and a fundamental system of neighborhoods of $x + \infty \cdot \sigma _ { \alpha }$ meets $C$ in the sets $x + y + B _ { \varepsilon } + \sigma _ { \alpha }$ , where $B _ { \varepsilon }$ is the $\varepsilon$ -ball around 0, and $y \in \sigma _ { \alpha }$ . It follows that if $x + \infty \cdot \sigma _ { \alpha } \in C ^ { \prime \prime }$ , then $x + y + B _ { \varepsilon } + \sigma _ { \alpha } \subset C$ for suitable $y , \varepsilon$ . But $x + y + \infty \cdot \sigma _ { \alpha } = x + \infty \cdot \sigma _ { \alpha }$ , so all points of $C ^ { \prime \prime }$ are represented by symbols $x + \infty \cdot \sigma _ { \alpha }$ with $x \in C$ . Conversely, if $x \in C$ , then, for small enough $\varepsilon$ , we have $x + B _ { \varepsilon } + \sigma _ { \alpha } \subset C$ ; hence,

$$
x + y + z + \infty \cdot \sigma _ { \beta } \in \mathrm { c l o s u r e ~ o f } C \mathrm { i n } N _ { \{ \sigma _ { \alpha } \} } ,
$$

for all $y \in \sigma _ { \alpha }$ and $z \in B _ { \varepsilon }$ , and for all faces $\sigma _ { \beta }$ of $\sigma _ { \alpha }$ . This means that $x + \infty$ · $\sigma _ { \alpha } \in C ^ { \prime \prime }$ . Thus

$$
C ^ { \prime \prime } { = } \bigcup _ { \alpha } \bigcup _ { x \in C } \{ x + \infty \cdot \sigma _ { \alpha } \} \ .
$$

Next, for all $x + \infty \cdot \sigma _ { \alpha }$ , we claim that there is a finite set $\sigma _ { \alpha _ { 1 } } , \ldots , \sigma _ { \alpha _ { n } }$ of polyhedral cones such that

$$
\bigcup _ { i = 1 } ^ { n } { \boldsymbol { \sigma } } _ { \alpha _ { i } } { \mathrm { ~ i s ~ a ~ n e i g h b o r h o o d ~ o f ~ } } x + \infty \cdot { \boldsymbol { \sigma } } _ { \alpha _ { } } .
$$

In fact, let $y _ { 1 } , . . . , y _ { m } \in C$ have the property that $x$ is in the interior of the polyhedral cone $\langle y _ { 1 } , \ldots , y _ { m } \rangle$ spanned by the $y _ { i }$ ; more precisely, suppose $x + B _ { \varepsilon } \subset$ $\langle y _ { 1 } , \ldots , y _ { m } \rangle$ . Let $\tau$ be the polyhedral cone spanned by $\sigma _ { \alpha }$ and the $y _ { i }$ . We apply the main theorem of reduction theory (Chapter II, Corollary 4.9), plus the fact that mod $\overline { { \Gamma } }$ there are only finitely many $\sigma _ { \alpha }$ , to conclude that

$$
\{ \alpha | \sigma _ { \alpha } \cap \tau \cap C \neq \pmb { \emptyset } \}
$$

is finite. Since the $\sigma _ { \alpha }$ cover $C$ , it follows that

$$
\tau \cap C \subset ( \sigma _ { \alpha _ { 1 } } \cup \cdots \cup \sigma _ { \alpha _ { n } } )
$$

for suitable $\sigma _ { \alpha _ { i } }$ . Therefore

$$
x + B _ { \varepsilon } + \sigma _ { \alpha } \subset \left( \sigma _ { \alpha _ { 1 } } \cup \ldots \cup \sigma _ { \alpha _ { n } } \right) .
$$

This proves (1.2).

Now let $x _ { i } \in C ^ { \prime \prime }$ be a sequence of points converging to $x \in C ^ { \prime \prime }$ and let $\gamma _ { i } \in \overline { { \Gamma } }$ be such that $y _ { i } : = \mathscr { \gamma } _ { i } \cdot x _ { i }$ converges to a point $y \in C ^ { \prime \prime }$ . We have to show that the set of $\gamma _ { i }$ for $i \gg 0$ consists of only finitely many elements $\{ \gamma ^ { 1 } , \ldots , \gamma ^ { n } \}$ and that $\gamma ^ { j } \cdot x = y$ , for $j = 1 , \dotsc , n$ . Since $C$ is a $\overline { { \Gamma } }$ -invariant open dense subset of $C ^ { \prime \prime }$ , we may suppose that $x _ { i } \in C$ .

Now, by the preceding discussion, there exist finitely many polyhedra $\sigma _ { \alpha _ { i } }$ and $\sigma _ { \alpha _ { j } ^ { \prime } }$ such that

$$
x _ { k } \in \sigma _ { \alpha _ { i } } , y _ { k } \in \sigma _ { \alpha _ { j } ^ { \prime } } .
$$

By taking a subsequence if necessary, we may suppose that $x _ { i } \in \sigma$ , $y _ { i } \in \sigma ^ { \prime }$ . It follows that $\gamma _ { i } \sigma \cap \sigma ^ { \prime } \cap C \neq \emptyset$ . By Corollary 4.9 of Chapter II, this implies that the set of the $\gamma _ { i }$ , for $i \gg 0$ , consists of only finitely many elements $\{ \gamma ^ { 1 } , \ldots , \gamma ^ { n } \}$ which necessarily satisfy $\gamma ^ { j } \cdot x = y$ , for $j = 1 , \dotsc , n$ .

Proof of (ii) The openness is clear. Since $C ^ { \prime }$ is the quotient of $U ^ { \prime }$ by a compact group we have to show the following statement:

$( \mathrm { i i } ^ { \prime } ) L e t \bar { z } _ { 1 } , \bar { z } _ { 2 } , \dots i$ be a sequence of points in $C _ { \varepsilon }$ ; then there exist elements $\gamma _ { i } \in \overline { { \Gamma } }$ , such that, after passing to a subsequence, the sequence $\gamma _ { i } \overline { { z } } _ { i }$ converges to a point in $C ^ { \prime \prime }$ .

Now, by conditions (4) and (5) of a $\overline { { \Gamma } }$ -admissible decomposition, applied to $\{ \sigma _ { \alpha } \}$ (see Definition 4.10 in Chapter $\mathrm { I I }$ ), we can find $\overline { { z } } _ { i } ^ { \prime } = \gamma _ { i } \cdot \overline { { z } } _ { i }$ such that, after passing to a subsequence, all $\overline { { z } } _ { i } ^ { \prime }$ lie in one and the same $\sigma _ { \alpha }$ . It follows from the description of the topology of $N _ { \sigma _ { \alpha } }$ given in Chapter I that a subsequence of the $\left\{ \overline { { z } } _ { i } ^ { \prime } \right\}$ converges to a point $\overline { z } ^ { \prime } \in N _ { \sigma _ { \alpha } }$ . It remains to show that ${ \overline { { z } } } ^ { \prime } \in C ^ { \prime \prime }$ . This is clear if $\sigma _ { \alpha } \setminus \{ 0 \} \subset C$ .

In general, $\sigma _ { \alpha } \cap \partial C$ is contained in a finite union of rational boundary components $\overline { { C } } _ { k } = N _ { k , \mathbb { R } } \cap \overline { { C } }$ of $C$ for $k = 1 , \ldots , n$ . Here $N _ { k , \mathbb { R } } \subset N _ { \mathbb { R } }$ is a rational subspace and we may choose a rational linear functional $\ell _ { k }$ on $N _ { \mathbb { R } }$ such that $\ell _ { k } \geq 0$ on $\overline { { C } }$ and $\left( \ell _ { k } = 0 \right) \cap \overline { { C } } = \overline { { C } } _ { k }$ . We may assume that $\varepsilon \in L$ , where $L$ is a lattice fixed by $\overline { { \Gamma } }$ and commensurable with $N _ { \mathbb { Z } }$ . It follows that $\gamma _ { i } \varepsilon \in L$ . Furthermore, $\ell _ { k }$ on $L \cap C$ is bounded away from zero, say by $c _ { k }$ , as the image of $L$ in $N _ { \mathbb { R } } / N _ { k , \mathbb { R } }$ is a lattice. Since

$$
\overline { { z } } _ { i } ^ { \prime } \in \gamma _ { i } \varepsilon + C \ ,
$$

it follows that $\ell _ { k } ( \overline { { z } } _ { i } ^ { \prime } ) > \ell _ { k } ( \gamma _ { i } \varepsilon ) \geq c _ { k }$ . Since this is true for all $k$ , the limit $\overline { { z } } ^ { \prime }$ of the sequence $\{ \overline { { z } } _ { i } ^ { \prime } \}$ lies in $C ^ { \prime \prime }$ .

Now, the basic idea to compactify $U / \Gamma$ is to glue $U / \Gamma$ and $( \overline { { \Gamma } } \cdot U _ { \varepsilon } ^ { \prime } ) / \overline { { \Gamma } }$ along the set $( \overline { { \Gamma } } \cdot U _ { \varepsilon } ^ { \prime } ) / \overline { { \Gamma } } = \big ( ( \Gamma \cap P ) \cdot U _ { \varepsilon } \big ) / ( \Gamma \cap P )$ . Roughly speaking, this will add to $U / \Gamma$ points at infinity at the cusp $\mathrm { i } \infty \cdot C$ of $U$ . To glue, we must know that $( \overline { { \Gamma } } \cdot U _ { \varepsilon } ^ { \prime } ) / \overline { { \Gamma } }$ is a subset of $U / \Gamma$ , i.e., that if $\varepsilon$ is large enough, two $\Gamma \cdot$ -equivalent points of $U _ { \varepsilon }$ are in fact $\Gamma \cap P$ -equivalent. This is a consequence of “Piatetskii-Shapiro’s lemma.”

We will not pursue the construction further at this stage because we will also have to treat the “higher-dimensional cusps,” i.e., the cusps at $\infty$ in Siegel domains of the third kind. And we will then use Siegel sets instead of Piatetskii-Shapiro’s cylindrical sets $U _ { \varepsilon }$ to carry out the details. However, before launching into the morass of the general cusps, it is nice to look at the case where the above, relatively simple, construction is sufficient – the case of $\mathbb { Q }$ -rank 1. This is what we will do in the following appendix.

# Appendix: Groups of $\mathbb { Q }$ -rank 1 acting on tube domains

We keep the notations from Section 1.

Proposition 1.5 The following conditions are equivalent:

(i) $C / \overline { { \Gamma } } \cdot \mathbb { R } _ { > 0 }$ is compact;   
(ii) the $\mathbb { Q }$ -rank of $\overline { G }$ is 1;   
(iii) the only rational point on ∂C is 0;   
(iv) the $\mathbb { Q }$ -rank of $G$ is 1;   
(v) the (proper) rational boundary components of the hermitian symmetric domain $U$ are all zero- dimensional.

Proof That (ii $) \Longleftrightarrow ( \mathbf { i v } )$ follows from the facts that, first, a $\mathbb { Q }$ -parabolic contains a maximal $\mathbb { Q }$ -split torus of $\mathbf { G }$ and, second, that $\overline { G }$ is the reductive part of the parabolic subgroup $P$ of $G$ ; hence $\overline { G }$ contains a maximal $\mathbb { Q }$ -split torus of $G$ .

The equivalence of (ii) and (iii) comes from the correspondence between parabolic subgroups and rational boundary components, see Chapter II, Section 3.10. Similarly, the equivalence of (iv) and (v) comes from the general theory of bounded domains (see Section 3, Proposition 3.9, below). Finally, the equivalence (iii) $\Longleftrightarrow ( \mathrm { i } )$ is a consequence of the reduction theory for cones.

Example 1.6 Let $k$ be a totally real extension of degree $n$ of $\mathbb { Q }$ . Let

$$
\begin{array} { r l } & { C = \mathbb { R } _ { > 0 } ^ { n } \subset \mathbb { R } ^ { n } \ ; } \\ & { \overline { { \mathcal { G } } } = R _ { k / \mathbb { Q } } ( \mathbb { G } _ { m } ) \quad ( \mathrm { W e i l ' s ~ r e s t r i c t i o n ~ o f ~ s c a l a r s } ) \ ; } \\ & { \mathcal { G } = R _ { k / \mathbb { Q } } ( { \mathrm { S L } } ( 2 ) ) \ . } \end{array}
$$

In this case $U$ is the $n$ -fold product of ${ \mathfrak H }$ with itself. Also $\Gamma$ is commensurable with ${ \mathrm { S L } } ( 2 , { \mathcal { O } } )$ , where $\mathcal { O }$ is the ring of integers in $k$ , and $\overline { { \Gamma } }$ is commensurable with the group of units of $k$ . This example is called the Hilbert case, and for $n = 2$ was treated in Chapter I, Section 5.

In this appendix, we want to look more closely at the $\mathbb { Q }$ -rank 1 case. In this case, we see immediately that $U ^ { \prime \prime } \backslash U ^ { \prime } \subset U _ { \varepsilon } ^ { \prime \prime }$ for every $\varepsilon$

Therefore, $U ^ { \prime \prime } / \overline { { \Gamma } } = ( U ^ { \prime } / \overline { { \Gamma } } ) \cup \big ( ( \overline { { \Gamma } } \cdot U _ { \varepsilon } ^ { \prime \prime } ) / \overline { { \Gamma } } \big )$ . Let

$$
E = ( U ^ { \prime \prime } / \overline { { \Gamma } } ) \backslash ( U ^ { \prime } / \overline { { \Gamma } } )
$$

be the locus at infinity that is added on. Then $E \subset ( \overline { { \Gamma } } \cdot U _ { \varepsilon } ^ { \prime \prime } ) / \overline { { \Gamma } }$ for every $\varepsilon$ , so, by Theorem $1 . 4 , E$ is relatively compact in $U ^ { \prime \prime } / \overline { { \Gamma } }$ . But $E$ is closed in $U ^ { \prime \prime } / \overline { { \Gamma } }$ , so

$E$ is itself compact. Put another way, we have an analytic space $U ^ { \prime \prime } / \overline { { \Gamma } }$ and a compact analytic subset $E$ , and $U ^ { \prime } / \overline { { \Gamma } }$ is just $( U ^ { \prime \prime } / \overline { { \Gamma } } ) \backslash E$ :

![](images/92e4f70c3f3bfc6b87f6bcb0849b5dcc3f9f06f6c1ae2947641c5531ba4c3be7.jpg)

The main result of this appendix is as follows.

Theorem 1.7 The set $E$ is exceptional, i.e., can be blown down in $U ^ { \prime \prime } / \overline { { \Gamma } }$ to $a$ point.

Proof We may, if we like, pass to a subgroup of finite index $\overline { { \Gamma } } ^ { \prime }$ of $\overline { { \Gamma } }$ and prove that $( U ^ { \prime \prime } \backslash U ^ { \prime } ) / \overline { { \Gamma } } ^ { \prime }$ can be blown down.

So we can assume from the beginning that $\overline { { \Gamma } }$ acts freely on $U ^ { \prime \prime }$ ; in particular, $U ^ { \prime } / \overline { { \Gamma } }$ is a manifold.

We are going to apply the following fact (cf. [4]).

Let $A \subset X$ be a compact analytic subset of an analytic space, where $X \backslash$ A is a manifold. If A possesses arbitrarily small strictly Levi-pseudoconvex neighborhoods, then A can be blown down to a point.

(Recall that an open subset $U \subset X$ is called strictly Levi-pseudoconvex if, for all $y \in \partial U$ , there exists a real $C ^ { 2 }$ -function $\varphi$ defined in a neighborhood $V$ of $y$ such that

(i) $U \cap V = \left\{ x \in V \mid \varphi ( x ) < 0 \right\} ;$ (ii) (convexity condition) for $0 \neq t \in T _ { y }$ with $\mathrm { d } \varphi ( t ) = 0$ , one has $\partial \bar { \partial } \varphi ( t ) > 0 .$ )

As in the previous section, let $C ^ { \prime \prime }$ be the interior of the closure of $C$ in $N _ { \{ \sigma _ { \alpha } \} }$ . We will use the characteristic function $\varphi$ of the cone $C$ introduced in Chapter II, Section 1. It is easy to see that $\varphi$ extends to a continuous function $\varphi$ on $C ^ { \prime \prime }$ with $\varphi \equiv 0$ on $C ^ { \prime \prime } \backslash C$ . Moreover, $\varphi$ is $\overline { { \Gamma } }$ -invariant, and hence comes from a function $\overline { { \varphi } }$ on $C ^ { \prime \prime } / \overline { { \Gamma } }$ . Let $f = \varphi \circ$ ord be the induced function on $U ^ { \prime \prime }$ . Then $f$ comes from a function $\overline { { f } }$ on $U ^ { \prime \prime } / \overline { { \Gamma } }$ . Since $\varphi ( x ) = 0$ if and only if $x \in C ^ { \prime \prime } \backslash C$ , we get ${ \overline { { f } } } ( x ) = 0$ if and only if $x \in E$ . Therefore the open sets

$$
V _ { c } = \{ X \in U ^ { \prime \prime } / \overline { { \Gamma } } | \overline { { f } } ( x ) < c \}
$$

form a family of arbitrarily small neighborhoods of $E$ . Hence it suffices to

show that $V _ { c }$ is pseudoconvex, or to check the Levi condition at the points of the boundary of $V _ { c }$ .

We can choose coordinates $z _ { i } = x _ { i } + \mathbf { i } \cdot y _ { i }$ on $U ^ { \prime }$ such that $f$ becomes

$$
f ( z _ { 1 } , \ldots , z _ { n } ) = \varphi ( y _ { 1 } , \ldots , y _ { n } ) .
$$

Since $\varphi$ is strictly convex (see Chapter $\mathrm { I I }$ , Proposition 1.4), $f$ is strictly Leviconvex, and the theorem is proven.

Remarks (i) In the Hilbert case, the function $\varphi : \mathbb { R } ^ { n } \longrightarrow \mathbb { R }$ considered in the above proof is simply $\varphi ( x _ { 1 } , \ldots , x _ { n } ) = 1 / ( x _ { 1 } \cdot \cdot \cdot x _ { n } )$ . For $n = 2$ , the constructed neighborhoods coincide with the ones considered in Chapter I, Section 5.

(ii) By applying the above procedure to all cusps we obtain in the end a compactification of $U / \Gamma$ , which is just $U / \Gamma$ with a finite number of points added: we recover in the $\mathbb { Q }$ -rank 1 case the so-called Baily–Borel compactification.

# 2 The structure of bounded symmetric domains

In this section we summarize the standard theory of symmetric spaces. One of its purposes is to introduce notation.

# 2.1

A Riemannian symmetric space is a connected Riemannian manifold $D$ such that, for every point $x \in D$ , there exists an involutive automorphism $s _ { x }$ which has $x$ as an isolated fixed point.

If $M$ is a complex hermitian manifold, then $D$ is a hermitian symmetric space if, for every point $x \in D$ , there exists an involutive automorphism $s _ { x }$ which has $x$ as an isolated fixed point (here, of course, the condition that $s _ { x }$ is an automorphism means that $s _ { x }$ is holomorphic as well as isometric).

If $D$ is a hermitian symmetric space, then the Riemannian manifold $D$ decomposes† as

$$
D = D _ { 0 } \times D _ { 1 } \times \cdot \cdot \cdot \times D _ { n } \ ,
$$

where:

• $D _ { 0 }$ is the quotient of a complex vector space with a translation-invariant metric by a discrete group of translations (such a hermitian symmetric space is said to be of euclidean type); • $D _ { i } , i \neq 0$ , is an irreducible and non-euclidean hermitian symmetric space.

$^ \dagger$ If $D$ is simply connected, this is well known and can be found, for instance, in Helgason [6]. In the hermitian case, simply connectedness is not needed: see Wolf [13], p. 490, Lemma 1.

Those factors $D _ { i }$ , for $i \neq 0$ , which are compact are said to be of compact type and are rational projective varieties; a non-compact factor $D _ { i }$ with $i \neq 0$ is said to be of non-compact type and is a bounded domain in $\mathbb { C } ^ { n }$ (we will prove this later).

The space $D$ is called non-euclidean, resp. symmetric domain, resp. of compact type, if, respectively, the factor $D _ { 0 }$ is absent in the above decomposition, or all the $D _ { i }$ are of non-compact type, or all $D _ { i }$ are of compact type. In the latter two cases $D$ is simply connected. If, in addition, there is only one factor present, $D$ is called simple.

Let $D$ be a non-euclidean hermitian symmetric space and denote by $G$ the identity component of its (Lie) group of automorphisms. Then the group $G$ acts transitively on the space $D$ and, choosing a basepoint $o \in D$ , we may write

$$
D = G / K ,
$$

where $K \subset G$ is a compact subgroup.

The symmetry $s _ { o }$ induces an automorphism $\sigma$ of the group $G$ such that $K =$ $K ^ { \sigma }$ . Letting

$$
\begin{array} { r l } & { \mathfrak { g } = \mathrm { L i e } \left( G \right) , } \\ & { \mathfrak { k } = \mathrm { L i e } \left( K \right) = \mathrm { s u b s p a c e ~ o f ~ } \mathfrak { g } , \mathrm { ~ w h e r e ~ } \sigma = \mathrm { I d ~ } , } \\ & { \mathfrak { p } = \mathrm { s u b s p a c e ~ o f ~ } \mathfrak { g } , \mathrm { ~ w h e r e ~ } \sigma = - \mathrm { I d ~ } , } \end{array}
$$

we get a decomposition

$$
\displaystyle { { \mathfrak { g } } = { \mathfrak { k } } \oplus { \mathfrak { p } } } \ .
$$

Note that there is a canonical isomorphism $p \longrightarrow T _ { o }$ , the tangent space to $D$ at $o$ .

If $D$ is now a hermitian symmetric domain, then the group $G$ is semi-simple and adjoint, $K$ is a maximal compact subgroup, and the above direct sum decomposition is a Cartan decomposition.

Note that $G$ is the connected component ${ \mathcal { G } } ( \mathbb { R } ) ^ { o }$ of the set of real points of a unique algebraic group $\mathcal { G }$ defined over $\mathbb { R }$ : via the adjoint representation

$$
\mathrm { A d } : G \longrightarrow \mathrm { G L } ( { \mathfrak { g } } ) \ ,
$$

$\mathcal { G }$ is the Zariski closure of $\mathrm { I m } ( \mathrm { A d } )$

Set

$$
\begin{array} { r c l } { { } } & { { } } & { { \ell _ { c } = \ell ~ , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \mathfrak { p } _ { c } = \mathrm { i } \mathfrak { p } ( \subset \mathfrak { g } _ { \mathbb { C } } ) ~ , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \mathfrak { g } _ { c } = \mathfrak { k } _ { c } \oplus \mathfrak { p } _ { c } ~ . } } \end{array}
$$

Then ${ \mathfrak { g } } _ { c }$ is a compact real form of ${ \mathfrak { g } } \mathbb { C }$ . Passing to the group level, we can define

the compact dual of $D$ by

$$
\check { D } = G _ { c } / K _ { c } .
$$

Conversely, starting with a hermitian symmetric space of compact type $\check { D }$ , one gets back to the space $D$ by the same construction.

Let $D$ be a non-euclidean hermitian symmetric space. Then there exists a morphism

$$
u _ { o } : U ^ { 1 } \longrightarrow G
$$

from the circle group $U ^ { 1 }$ into $G$ such that $u _ { o } ( z ) \in K$ for any $z \in U ^ { 1 }$ and $u _ { o } ( z )$ induces the multiplication by $z$ on the tangent space $T _ { o }$ of $D$ at $o$ . The group $K \subset G$ is the centralizer of $u _ { o } ( U ^ { 1 } )$ in $G$ , and hence is connected. Further, if $D$ is simple, $u _ { o } ( U ^ { 1 } )$ is the center of $K \subset G$ .

We set

$$
h _ { o } = u _ { o } ^ { 2 } .
$$

Noting that, via the isomorphism ${ \mathfrak { p } } \longrightarrow T _ { o }$ the adjoint action of $K$ on $\mathfrak { p }$ corresponds to the action of $K$ on $T _ { o }$ , we see that

$$
J = \mathrm { A d } \left( h _ { o } \left( \mathrm { e } ^ { 2 \pi \mathrm { i } / 8 } \right) \right) \big | _ { \mathfrak { p } }
$$

defines the given complex structure on $T _ { o }$ , whereas

$$
\begin{array} { r } { \sigma = \operatorname { A d } \left( h _ { o } ( \operatorname { i } ) \right) . } \end{array}
$$

Let

$$
{ \mathfrak { p } } _ { \mathbb { C } } = { \mathfrak { p } } _ { + } \oplus { \mathfrak { p } } _ { - }
$$

be the decomposition into $\pm \mathrm i$ -eigenspaces for $J$ . Note that these are abelian subalgebras of ${ \mathfrak { g } } _ { \mathbb { C } }$ since, e.g.,

$$
\left[ { \mathfrak { p } } _ { + } , { \mathfrak { p } } _ { + } \right] \subset \left\{ x \in { \mathfrak { g } } \mid J x = - x \right\} = ( 0 ) .
$$

Denote by $P _ { \pm }$ the subgroup of $G _ { \mathbb { C } }$ generated by $\exp ( { \mathfrak { p } } _ { \pm } )$ . Then $K _ { \mathbb { C } }$ normalizes $P _ { \pm }$ and $K _ { \mathbb { C } } \cdot P _ { - }$ is a parabolic subgroup of $G _ { \mathbb { C } }$ with unipotent radical $P _ { - }$ ; hence $G _ { \mathbb { C } } / K _ { \mathbb { C } } \cdot P _ { - }$ is a projective algebraic variety, which we call for the moment $X$ .

# Theorem 2.1 (Borel and Harish-Chandra embedding theorem)

(a) The map $P _ { + } \times K _ { \mathbb { C } } \times P _ { - } \longrightarrow G _ { \mathbb { C } }$ given by multiplication is injective, $G$ is contained in the image, and $\left( K _ { \mathbb { C } } \cdot P _ { - } \right) \cap G = K$ .

(b) Hence we have the following maps:

$$
\begin{array} { r c l l } { { G / K } } & { { \longrightarrow } } & { { P _ { + } \times K _ { \mathbb { C } } \times P _ { - } / K _ { \mathbb { C } } \cdot P _ { - } } } & { { \longrightarrow } } & { { G _ { \mathbb { C } } / K _ { \mathbb { C } } \cdot P _ { - } } } \\ { { \downarrow \vert } } & { { } } & { { \downarrow \vert } } & { { } } \\ { { D } } & { { } } & { { P _ { + } } } & { { \qquad X } } \\ { { } } & { { } } & { { \downarrow \uparrow \exp } } & { { } } \\ { { } } & { { } } & { { \mathfrak { p } _ { + } } } & { { } } \end{array}
$$

These maps are holomorphic open immersions, the image of $D$ in ${ \mathfrak { p } } _ { + }$ is $a$ bounded domain, and the image of ${ \mathfrak { p } } _ { + }$ in $X$ is a dense Zariski open set.

(c) Finally, the compact form $G _ { c } \subset G _ { \mathbb { C } }$ of $G$ acts transitively on $X$ ; furthermore, $G _ { c } \cap { \left( K _ { \mathbb { C } } \cdot P _ { - } \right) } = K$ so that

$$
X \cong \check { D } : = G _ { c } / K ,
$$

i.e., $X$ is the compact dual of $D$ .

For a full proof of this, we refer the reader to Helgason [6], Ch. 8, $^ { \ S 7 }$ , and we give here only a brief indication; thus, on the Lie algebra level, we have

$$
\begin{array} { r l } & { \mathfrak { g } _ { \mathbb { C } } = \mathfrak { k } _ { \mathbb { C } } \oplus \mathfrak { p } _ { + } \oplus \mathfrak { p } _ { - } \ , } \\ & { \quad \mathfrak { k } = \mathfrak { g } \cap \left( \mathfrak { k } _ { \mathbb { C } } \oplus \mathfrak { p } _ { - } \right) = \mathfrak { g } _ { c } \cap \left( \mathfrak { k } _ { \mathbb { C } } \oplus \mathfrak { p } _ { - } \right) , } \end{array}
$$

and

$$
\dim D = \dim \breve { D } = \dim { \mathfrak { p } } _ { + } = \dim P _ { + } = \dim G _ { \mathbb { C } } / K _ { \mathbb { C } } \cdot P _ { - } \ ,
$$

from which we deduce that all the assertions are “true locally,” e.g., the natural maps $D \longrightarrow X$ , and $P _ { + } \longrightarrow X$ , and $G _ { c } / K \longrightarrow X$ are local immersions. The main step is to check

$$
G \subset ( \mathrm { b o u n d e d ~ s u b s e t ~ o f ~ } P _ { + } ) \cdot K _ { \mathbb { C } } \cdot P _ { - } \ .
$$

This can be done by using Theorem 2.4 below to reduce to the simplest case $G = \mathrm { S L } ( 2 , \mathbb { R } ) / \{ \pm 1 \}$ , where it follows by an explicit explicit calculation. The rest is straightforward.

#

We want next to look at holomorphic maps between bounded symmetric domains $f : D _ { 1 } \longrightarrow D _ { 2 }$ . The maps which have good Lie-theoretic meaning are the symmetric maps; this means that, for every $x \in D _ { 1 }$ ,

$$
f \circ s _ { x } ^ { ( 1 ) } = s _ { f ( x ) } ^ { ( 2 ) } \circ f ,
$$

where $s _ { x } ^ { ( 1 ) }$ , resp. $s _ { f ( x ) } ^ { ( 2 ) }$ , are the symmetries of $D _ { 1 }$ , resp. $D _ { 2 }$ , with respect to $x$ , resp. $f ( x )$ . It is readily checked that this implies that, if $G _ { i } = \mathrm { A u t } ( D _ { i } ) ^ { o }$ , then there is a covering $G _ { 1 } ^ { \prime }$ of $G _ { 1 }$ and a homomorphism

$$
\varphi : G _ { 1 } ^ { \prime } \longrightarrow G _ { 2 }
$$

for which $f$ is equivariant:

$$
f ( g \cdot x ) = \varphi ( g ) \cdot f ( x ) ~ .
$$

To see this, let $G _ { 1 } ^ { \prime \prime } \subset G _ { 1 } \times G _ { 2 }$ be the connected component of the set of pairs $( g _ { 1 } , g _ { 2 } )$ such that $f ( g _ { 1 } \cdot x ) = g _ { 2 } \cdot f ( x )$ ; via (2.1), check that $p _ { 1 } : G _ { 1 } ^ { \prime \prime } \longrightarrow G _ { 1 }$ is surjective; now let $G _ { 1 } ^ { \prime }$ be the product of those simple factors of $G _ { 1 } ^ { \prime \prime }$ that map non-trivially to $G _ { 1 }$ . Note that we may assume $G _ { 1 } ^ { \prime } \subset G _ { 1 } \times G _ { 2 }$ , hence $G _ { 1 } ^ { \prime } =$ $\mathcal { G } ^ { \prime } ( \mathbb { R } ) ^ { o }$ , where $\mathcal { G } ^ { \prime }$ is an algebraic group over $\mathbb { R }$ , and $G _ { 1 } ^ { \prime } \longrightarrow G _ { 1 }$ is a finite covering.

Proposition $2 . 2 \dagger L e t D _ { 1 }$ and $D _ { 2 }$ be bounded symmetric domains, let $o _ { i } \in D _ { i }$ be basepoints, and let $G _ { i } = \mathrm { A u t } ( D _ { i } ) ^ { o }$ . There are natural bijections between the following sets:

(a) holomorphic symmetric maps $f : D _ { 1 } \longrightarrow D _ { 2 }$ such that $f ( o _ { 1 } ) = o _ { 2 }$ ; (b) maps $f : D _ { 1 } \longrightarrow D _ { 2 }$ such that $f ( o _ { 1 } ) = o _ { 2 }$ and, for all $x \in D _ { 1 } , \theta \in \mathbb { R } ,$ ,

$$
f \circ u _ { x } ( \mathrm { e } ^ { \mathrm { i } \theta } ) = u _ { f ( x ) } ( \mathrm { e } ^ { \mathrm { i } \theta } ) \circ f ,
$$

where $u _ { x } ( \mathrm { e } ^ { \mathrm { i } \theta } )$ , resp. $u _ { f ( x ) } ( \mathrm { e } ^ { \mathrm { i } \theta } )$ , are the automorphisms fixing $x ,$ , resp. $f ( x )$ , and multiplying by $\mathrm { e } ^ { \mathrm { i } \theta }$ in the tangent spaces;

(c) connected coverings $\pi : G _ { 1 } ^ { \prime } \longrightarrow G _ { 1 }$ and homomorphisms

$$
\varphi = \varphi _ { 1 } \times \varphi _ { 2 } : \mathbb { R } \times G _ { 1 } ^ { \prime } \longrightarrow G _ { 2 } \ ,
$$

such that $\pi \times \varphi _ { 2 } : G _ { 1 } ^ { \prime } \longrightarrow G _ { 1 } \times G _ { 2 }$ is injective and such that, if we lift the homomorphism $\theta \longmapsto u _ { o _ { 1 } } ( \mathrm { e } ^ { \mathrm { i } \theta } )$ as follows:

$$
\mathbb { R } \xrightarrow [ ] { - \int _ { \theta _ { 1 } } ^ { u ^ { \prime } - 1 } \int _ { \theta _ { 1 } } ^ { \theta _ { 1 } } \int _ { \theta _ { 1 } } ^ { u } } \mathrm { d } u _ { 1 } ^ { \prime }
$$

then $u _ { o _ { 2 } } ( \mathbf { e } ^ { \mathrm { i } \theta } ) = \varphi ( \theta , u ^ { \prime } ( \theta ) )$ .

Proof First of all, note that any map $f : D _ { 1 } \longrightarrow D _ { 2 }$ is $\varphi _ { 2 }$ -equivariant for at most one $\varphi _ { 2 } : G _ { 1 } ^ { \prime } \longrightarrow G _ { 2 }$ . Indeed, introduce $G _ { 1 } ^ { \prime \prime } \subset G _ { 1 } \times G _ { 2 }$ as above. Then

Lie $G _ { 1 } ^ { \prime \prime } { = } \mathrm { L i e } G _ { 1 } \times \mathrm { L i e } \widetilde { K }$ , where $\widetilde { K } = \left\{ g _ { 2 } \in G _ { 2 } \vert g _ { 2 } \circ f = f \right\}$ . Now - $\widetilde { K } \subset \mathsf { S t a b } _ { o _ { 2 } }$ , so $\widetilde { K }$ is compact. Furthermore, since $f$ is $\varphi _ { 2 }$ -equivariant, the map $\pi \times \varphi _ { 2 }$ : $G _ { 1 } ^ { \prime } \longrightarrow G _ { 1 } \times G _ { 2 }$ factors through $G _ { 1 } ^ { \prime \prime }$ . We thus get a map

$$
\operatorname { L i e } G _ { 1 } = \operatorname { L i e } G _ { 1 } ^ { \prime } \longrightarrow \operatorname { L i e } G _ { 1 } ^ { \prime \prime } = \operatorname { L i e } G _ { 1 } \times \operatorname { L i e } \widetilde { K } .
$$

As $G _ { 1 }$ is semisimple without compact factors, there are no homomorphisms from $G _ { 1 }$ to $\widetilde { K }$ , so it follows that the image of Lie $G _ { 1 } ^ { \prime }$ in Lie $G _ { 1 } \times \mathrm { L i e } G _ { 2 }$ is uniquely determined. Since $G _ { 1 } ^ { \prime }$ is connected and $\pi \times \varphi _ { 2 }$ is injective, $G _ { 1 } ^ { \prime }$ and $\varphi _ { 2 }$ are uniquely determined.

Now start with $f : D _ { 1 } \longrightarrow D _ { 2 }$ , holomorphic and symmetric. Construct $\varphi _ { 2 } :$ $G _ { 1 } ^ { \prime }  G _ { 2 }$ as above. Let $\sigma _ { i } : G _ { i } \longrightarrow G _ { i }$ be the Cartan involution with respect to $K _ { i } = \mathsf { S t a b } _ { o _ { i } }$ . Then $f$ is also $\sigma _ { 2 } \circ \varphi _ { 2 } \circ \sigma _ { 1 }$ -equivariant, so $\varphi _ { 2 } \circ \sigma _ { 1 } = \sigma _ { 2 } \circ \varphi _ { 2 }$ . Therefore $\mathrm { d } \varphi _ { 2 }$ preserves the Cartan decomposition, in particular $\mathsf { d } \varphi _ { 2 } ( { \mathsf { p } } _ { 1 } ) \subset { \mathsf { p } } _ { 2 }$ . Also, since $f$ is holomorphic, $\mathrm { d } \varphi _ { 2 } : { \mathfrak { p } } _ { 1 } \longrightarrow { \mathfrak { p } } _ { 2 }$ is complex-linear. Now, every element of $D _ { 1 }$ equals $\exp ( a ) \cdot o _ { 1 }$ , with $a \in { \mathfrak { p } } _ { 1 }$ . So calculate:

$$
{ \begin{array} { r l } { f \circ u _ { \sigma _ { 1 } } ( \mathbf { e } ^ { \mathrm { i } \theta } ) \left( \exp { a \cdot \sigma _ { 1 } } \right) = f \left( \exp ( \mathbf { e } ^ { \mathrm { i } \theta } a ) \cdot \sigma _ { 1 } \right) } & { } \\ & { = \varphi \left( \exp ( \mathbf { e } ^ { \mathrm { i } \theta } a ) \right) \cdot \sigma _ { 2 } } \\ & { = \exp \left( \mathrm { d } \varphi _ { 2 } ( \mathbf { e } ^ { \mathrm { i } \theta } \cdot a ) \right) \cdot \sigma _ { 2 } } \\ & { = \exp \left( \mathbf { e } ^ { \mathrm { i } \theta } \cdot \mathbf { d } \varphi _ { 2 } ( a ) \right) \cdot \sigma _ { 2 } } \\ & { = u _ { \sigma _ { 2 } } ( \mathbf { e } ^ { \mathrm { i } \theta } ) \cdot \varphi _ { 2 } \left( \exp { a } \right) \cdot \sigma _ { 2 } } \\ & { = u _ { \sigma _ { 2 } } ( \mathbf { e } ^ { \mathrm { i } \theta } ) \cdot f ( \exp { a } \cdot \sigma _ { 1 } ) \ . } \end{array} }
$$

This proves that $f$ has the property in (b) for $x = o _ { 1 }$ ; the general case follows by conjugating.

To go from (b) to (c), let $\alpha _ { \theta } : G _ { 1 } ^ { \prime } \longrightarrow G _ { 1 } ^ { \prime }$ be conjugation by $u ^ { \prime } ( \theta )$ , and let $\beta _ { \theta } : G _ { 2 } \longrightarrow G _ { 2 }$ be conjugation by $u _ { o _ { 2 } } ( \mathrm { e } ^ { \mathrm { i } \theta } )$ . Then (b) shows that $f$ is both $\varphi _ { 2 }$ equivariant and $\beta _ { \theta } ^ { - 1 } \circ \varphi _ { 2 } \circ \alpha _ { \theta }$ -equivariant. This means that $\varphi _ { 2 } ( G _ { 1 } )$ commutes with $u _ { o _ { 2 } } ( \mathrm { e } ^ { \mathrm { i } \theta } ) \cdot \varphi _ { 2 } ( u ^ { \prime } ( \theta ) ) ^ { - 1 }$ for all $\theta$ , which means precisely that $\varphi : \mathbb { R } \times G _ { 1 } ^ { \prime } \longrightarrow$ $G _ { 2 }$ as in (c) can be constructed.

Conversely, given $\varphi : \mathbb { R } \times G _ { 1 } ^ { \prime } \longrightarrow G _ { 2 }$ , let $K _ { 1 } ^ { \prime }$ be the centralizer of $u ^ { \prime }$ , and let $K _ { 2 }$ be the centralizer of $u _ { o _ { 2 } }$ . Then $\varphi ( \mathbb { R } \times K _ { 1 } ^ { \prime } ) \subset K _ { 2 }$ , so $\varphi$ defines $f : ( \mathbb { R } \times$ ${ G } _ { 1 } ^ { \prime } ) / ( \mathbb { R } \times K _ { 1 } ^ { \prime } ) \longrightarrow { G _ { 2 } } / K _ { 2 }$ , i.e., $f : D _ { 1 } \longrightarrow D _ { 2 }$ . Using the fact that $\varphi _ { 1 } ( \theta ) =$ $u _ { o _ { 2 } } ( \mathrm { e } ^ { \mathrm { i } \theta } ) \cdot \varphi _ { 2 } ( u ^ { \prime } ( \theta ) ) ^ { - 1 }$ centralizes $\operatorname { I m } \varphi$ , we check easily the identity in (b).

Corollary 2.3 There is a bijection between the following two sets:

(a) holomorphic symmetric maps $f : \mathfrak { H } \longrightarrow D$ such that $f ( \mathrm { i } ) = o$ ; and (b) homomorphisms $\varphi : U ^ { 1 } \times { \mathrm { S L } } ( 2 , \mathbb { R } ) \longrightarrow G$ such that

$$
\varphi \left( \mathrm { e } ^ { \mathrm { i } \theta } , h ^ { S L } ( \mathrm { e } ^ { \mathrm { i } \theta } ) \right) = h _ { o } ( \mathrm { e } ^ { \mathrm { i } \theta } ) ,
$$

where

$$
h ^ { S L } ( \mathrm { e } ^ { \mathrm { i } \theta } ) = \left( \begin{array} { c c } { { \cos \theta } } & { { \sin \theta } } \\ { { - \sin \theta } } & { { \cos \theta } } \end{array} \right) .
$$

Proof The only new point here is that SL(2) is simply connected as an algebraic group, so, if $G _ { 1 } = \mathrm { A u t } ( \mathfrak { H } )$ , we can assume $G _ { 1 } ^ { \prime } = \mathbf { S } \mathbf { L } ( 2 , \mathbb { R } )$ .

We remark that, if

$$
\begin{array} { c } { { f : D _ { 1 } \longrightarrow D _ { 2 } \ : , } } \\ { { \varphi _ { 2 } : G _ { 1 } ^ { \prime } \longrightarrow G _ { 2 } } } \end{array}
$$

have the properties of Proposition 2.2, then $\mathbf { d } \varphi _ { 2 } : { \mathfrak { g } } _ { 1 } \longrightarrow { \mathfrak { g } } _ { 2 }$ commutes with the Cartan involutions, and hence

$$
\begin{array} { r l } & { \mathrm { d } \varphi _ { 2 } ( \mathfrak { k } _ { 1 } ) \subset \mathfrak { k } _ { 2 } \ , } \\ & { \mathrm { d } \varphi _ { 2 } ( \mathfrak { p } _ { 1 } ) \subset \mathfrak { p } _ { 2 } \ , } \\ & { \mathrm { d } \varphi _ { 2 } ( \mathfrak { p } _ { 1 , \pm } ) \subset \mathfrak { p } _ { 2 , \pm } \ ; } \end{array}
$$

hence, extending $\varphi _ { 2 }$ to $\varphi _ { 2 } ^ { \prime } : G _ { \mathrm { 1 , C } } ^ { \prime } \longrightarrow G _ { 2 , \mathbb { C } }$ , we have

$$
\begin{array} { r } { \varphi _ { 2 } ^ { \prime } ( K _ { 1 , \mathbb { C } } ^ { \prime } ) \subset K _ { 2 , \mathbb { C } } \ , } \\ { \varphi _ { 2 } ^ { \prime } ( P _ { 1 , \pm } ^ { \prime } ) \subset P _ { 2 , \pm } \ . } \end{array}
$$

Therefore we can extend $f$ , getting the following commutative diagram:

$$
\begin{array} { r c l } { { D _ { 1 } } } & { { \cfrac { f } { f } } } & { { D _ { 2 } } } \\ { { \cap } } & { { } } & { { \cap } } \\ { { { \mathfrak { p } } _ { 1 , + } } } & { { \cfrac { f } { f } } } & { { { \mathfrak { p } } _ { 2 , + } } } \\ { { \cap } } & { { } } & { { \cap } } \\ { { \check { D } _ { 1 } } } & { { \cfrac { f } { f } } } & { { \to } } & { { \check { D } _ { 2 } } } \end{array}
$$

# 2.3

We now take up the study of the roots of $G$ and $G _ { \mathbb { C } }$ .

Let ${ \mathfrak { t } } \subset { \mathfrak { k } }$ be a Cartan subalgebra of k. Then t contains $\operatorname { I m } \left( \mathrm { d } h _ { o } \right)$ , so that t is also a Cartan subalgebra of $\mathfrak { g }$ . Let

$$
\Psi = \mathrm { t c - r o o t ~ s y s t e m ~ o f ~ } \mathfrak { g } _ { \mathbb { C } } ,
$$

so that

$$
{ \mathfrak { g } } _ { \mathbb { C } } = { \mathfrak { t } } _ { \mathbb { C } } + \sum _ { \varphi \in \Psi } { \mathfrak { g } } ^ { \varphi } \ .
$$

A root $\varphi$ is called compact if ${ \mathfrak { g } } ^ { \varphi } \subset { \mathfrak { k } } _ { \mathbb { C } }$ ; it is called non-compact if ${ \mathfrak { g } } ^ { \varphi } \subset { \mathfrak { p } } _ { \mathbb { C } }$ . We denote:

$$
\begin{array} { r l } & { \Psi _ { K } = \mathrm { t h e ~ c o m p a c t ~ r o o t s } ~ , } \\ & { \Psi _ { p } ^ { + } = \mathrm { t h e ~ n o n - c o m p a c t ~ r o o t s ~ w i t h ~ } \mathfrak { g } ^ { \varphi } \subset \mathfrak { p } _ { + } ~ , } \\ & { \Psi _ { p } ^ { - } = \mathrm { n o n - c o m p a c t ~ r o o t s ~ w i t h ~ } \mathfrak { g } ^ { \varphi } \subset \mathfrak { p } _ { - } ~ , } \end{array}
$$

and

$$
\Psi _ { p } = \Psi _ { p } ^ { + } \cup \Psi _ { p } ^ { - } \mathrm { ~ . ~ }
$$

One can choose a linear ordering on $\Psi$ such that $\Psi _ { p } ^ { + } \subset \{ \mathrm { p o s i t i v e ~ r o o t s } \}$ and $\Psi _ { p } ^ { - } \subset \{ \mathrm { n e g a t i v e ~ r o o t s } \}$ . For example, we may choose as positive roots those corresponding to a Weyl chamber in it whose closure contains $\left( \mathrm { d } h _ { o } \right) ( \mathrm { i } )$ .

For $\varphi \in \Psi$ , define

$$
h _ { \varphi } \in \mathrm { i t }
$$

$$
2 \frac { \langle \varphi , \psi \rangle } { \langle \varphi , \varphi \rangle } = \psi ( h _ { \varphi } ) \ \mathrm { f o r \ a l l } \ \psi \in { \mathfrak { t } } ^ { * } \ ,
$$

where $\langle \cdot , \cdot \rangle$ denotes the Killing form. Choose root vectors

$$
e _ { \varphi } \in { \mathfrak { g } } ^ { \varphi }
$$

such that

$$
[ e _ { \varphi } , e _ { - \varphi } ] = h _ { \varphi } ~ ,
$$

and such that the complex conjugation of ${ \mathfrak { g } } _ { \mathbb { C } }$ with respect to $\mathfrak { g }$ permutes $e _ { \varphi }$ and $e _ { - \varphi }$ , whenever $\varphi \in \Psi _ { p }$ . Let

$$
\begin{array} { r l } & { x _ { \varphi } = e _ { \varphi } + e _ { - \varphi } ~ , } \\ & { y _ { \varphi } = \mathrm { i } ( e _ { \varphi } - e _ { - \varphi } ) ~ \mathrm { f o r } ~ \varphi \in \Psi _ { p } ^ { + } ~ . } \end{array}
$$

These elements form a basis over $\mathbb { R }$ of $\mathfrak { p }$ such that $J x _ { \varphi } = y _ { \varphi } , J y _ { \varphi } = - x _ { \varphi }$

Two roots $\varphi$ and $\psi$ are called strongly orthogonal, denoted by

$$
\varphi \perp \perp \psi ,
$$

if neither of $\varphi \pm \psi$ is a root; in this case $\varphi$ and $\psi$ are orthogonal. Harish-Chandra [5], p. 583, chooses in the following inductive way a maximal set of strongly orthogonal roots:

$$
\gamma _ { 1 } , \ldots , \gamma _ { r } ^ { / }
$$

is the maximal set of roots such that each $\gamma _ { i } ^ { \prime }$ is the smallest element of $\Psi _ { p } ^ { + }$ strongly orthogonal to γ1, . . ., γi−1.† We write hi, xi, ei, e−i, yi for hγ , xγ , eγ , $e _ { - \gamma _ { i } } , y _ { \gamma _ { i } }$ (where $i = 1 , \ldots , r )$ .

The following theorem is basic to the theory of hermitian symmetric domains.

# Theorem 2.4 (Harish-Chandra)

(i) The subspace $\mathfrak { a } = \textstyle \sum _ { i = 1 } ^ { r } \mathbb { R } x _ { i } \subset \mathfrak { p }$ is a maximal commutative subalgebra of p; hence $A = \exp ( { \mathfrak { a } } )$ is the connected component of the group of real points of a maximal split torus $\mathcal { A }$ in $\mathcal { G }$ , i.e., $A = { \mathcal { A } } ( \mathbb { R } ) ^ { o }$ . Moreover, the action of $K \cdot A$ is transitive, i.e., $K \cdot A \cdot o = D$ .

(ii) There exists a morphism

$$
\varphi : U ^ { 1 } \times \mathrm { S L } ( 2 , \mathbb { R } ) ^ { r } \longrightarrow G
$$

such that:

(a) $\varphi \left( u , h ^ { S L } ( u ) , \ldots , h ^ { S L } ( u ) \right) = h _ { o } ( u ) ;$ (b) dϕ on the ith factor $\mathrm { S L } ( 2 , \mathbb { R } )$ is given by

$$
\mathrm { d } \varphi \left( \begin{array} { l l } { a } & { b } \\ { c } & { - a } \end{array} \right) = a \cdot x _ { i } - \frac { b + c } { 2 } \cdot y _ { i } + \frac { b - c } { 2 } \cdot \mathrm { i } h _ { i } ,
$$

and hence

$$
\mathrm { d } \varphi \left( \mathfrak { s l } ( 2 , \mathbb { R } ) ^ { r } \right) = \mathfrak { a } + J \mathfrak { a } + \left[ \mathfrak { a } , J \mathfrak { a } \right] ;
$$

in particular, dϕ induces an isomorphism between the subalgebra of “diagonal matrices” in ${ \mathfrak { s l } } ( 2 , \mathbb { R } ) ^ { r }$ and $\mathfrak { a }$ ;

(c) $\varphi$ induces a symmetric holomorphic map

$$
\widetilde { \varphi } : \mathfrak { H } ^ { r } \longrightarrow D
$$

equivariant with respect to $\varphi$ , where $\mathrm { S L } ( 2 , \mathbb { R } )$ acts on ${ \mathfrak H }$ as usual and $U ^ { 1 }$ acts trivially, taking $( \mathrm { i } , \mathrm { i } , \dots , \mathrm { i } ) \in \mathfrak { H } ^ { r }$ to $o \in D$ .

Proof (i) We refer the reader to Helgason [6], p. 314, for the somewhat delicate, but elementary, verification that $\mathfrak { a }$ is maximal. Let $A = \exp ( { \mathfrak { a } } ) \subset G$ . Then, by Cartan,

$$
{ \cal G } = { \cal K } \cdot { \cal A } \cdot { \cal K } ,
$$

and hence

$$
D = K \cdot A \cdot K \cdot o = K \cdot A \cdot o \ .
$$

(ii) Let ${ \mathfrak { g } } _ { i } = \mathbb { R } x _ { i } + \mathbb { R } y _ { i } + \mathbb { R } \mathrm { i } h _ { i }$ ; then

$$
\mathfrak { g } _ { i } \xrightarrow { \sim } \mathfrak { s l } ( 2 , \mathbb { R } )
$$

by the map indicated in (ii), (b). We thus obtain

$$
\varphi _ { 2 } : \mathrm { S L } ( 2 , \mathbb { R } ) ^ { r } \longrightarrow G
$$

such that $\mathrm { d } \varphi _ { 2 }$ is given by (ii), (b). Moreover, noting that $\operatorname { A d } h _ { o } ( u )$ fixes each $h _ { i }$ , and multiplies $e _ { i }$ by $u ^ { 2 }$ and $e _ { - i }$ by $u ^ { - 2 }$ , one checks easily that

$$
\left. \mathrm { A d } h _ { o } ( u ) \right| _ { \mathbb { g } _ { i } } = \mathrm { A d } \varphi _ { 2 } \left( I , \ldots , \left( \begin{array} { c c } { \cos \theta } & { \sin \theta } \\ { - \sin \theta } & { \cos \theta } \end{array} \right) , \ldots , I \right) \Big | _ { \mathbb { g } _ { i } } \mathrm { i f } u = \mathrm { e } ^ { i \theta } \ ,
$$

and hence that

$$
\left. \mathrm { A d } h _ { o } ( u ) \right| _ { \sum _ { \ P _ { i } } } = \mathrm { A d } \varphi _ { 2 } \left( \left( \begin{array} { c c } { { \cos \theta } } & { { \sin \theta } } \\ { { - \sin \theta } } & { { \cos \theta } } \end{array} \right) , \dots , \left( \begin{array} { c c } { { \cos \theta } } & { { \sin \theta } } \\ { { - \sin \theta } } & { { \cos \theta } } \end{array} \right) \right) \Big | _ { \sum _ { \ P _ { i } } } .
$$

Since $h _ { o } ( u )$ and $\varphi _ { 2 } \left( \left( \begin{array} { c c } { { \cos \theta } } & { { \sin \theta } } \\ { { - \sin \theta } } & { { \cos \theta } } \end{array} \right) , \ldots \right)$ both lie in   $T = \exp \mathrm { t }$ , they commute, and we may write:

$$
h _ { o } ( u ) = \varphi _ { 1 } ( u ) \cdot \varphi _ { 2 } \left( \left( \begin{array} { c c } { { \cos \theta } } & { { \sin \theta } } \\ { { - \sin \theta } } & { { \cos \theta } } \end{array} \right) , \ldots \right) ,
$$

where $\varphi _ { 1 } ( u )$ centralizes $\operatorname { I m } \varphi _ { 2 }$ . Defining $\varphi$ by

$$
\varphi = \varphi _ { 1 } \times \varphi _ { 2 } : U ^ { 1 } \times { \bf S } \mathrm { L } ( 2 , \mathbb { R } ) ^ { r } \longrightarrow G \ ,
$$

it satisfies both (ii), (a) and (b).

Finally, (ii), (c) follows from Proposition 2.2.

Definition 2.5 The number $r$ appearing in the above theorem is called the rank of $D$ or the $\mathbb { R }$ -rank of $G$ .

The map $\widetilde { \varphi }$ has the following strong universal property.

Proposition 2.6 (Satake) Every symmetric holomorphic map-

$$
\widetilde { \psi } : \mathfrak { H } \longrightarrow D
$$

such that $\widetilde \psi ( \mathrm { i } ) = o$ is of the form

$$
\widetilde { \pmb { \psi } } ( z ) = \boldsymbol { k } \cdot \widetilde { \pmb { \varphi } } ( \dots , z , \dots , \mathbf { i } , \dots )
$$

for some $k \in K$ and some distribution of z’s and i’s among the $r$ variables of $\widetilde { \varphi }$

Proof According to Corollary 2.3,   $\widetilde { \psi }$ is $\psi _ { 2 }$ -equivariant for some homomorphism

$$
\psi = \psi _ { 1 } \times \psi _ { 2 } : U ^ { 1 } \times \mathrm { S L } ( 2 , \mathbb { R } ) \longrightarrow G
$$

such that $h _ { o } ( \mathrm { e } ^ { \mathrm { i } \theta } ) = \psi \left( \mathrm { e } ^ { \mathrm { i } \theta } , h ^ { \mathrm { S L } } ( \mathrm { e } ^ { \mathrm { i } \theta } ) \right)$ . It follows that:

$$
\mathsf { d } \psi \left( \mathbb { R } \cdot \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { - 1 } \end{array} \right) \right) \subset \mathfrak { p } .
$$

We use the fact that every element of $\mathfrak { p }$ is in $\operatorname { A d } K \cdot { \mathfrak { a } }$ (the polar decomposition in $\mathfrak { g }$ ). Therefore, replacing $\widetilde { \psi }$ by $\boldsymbol { k } \cdot \widetilde { \boldsymbol { \psi } }$ and $\psi$ by $k \psi k ^ { - 1 }$ , we can assume

$$
\mathsf { d } \psi \left( \mathbb { R } \cdot \left( \begin{array} { r r } { 1 } & { 0 } \\ { 0 } & { - 1 } \end{array} \right) \right) \subset \mathsf { a } .
$$

Then

$$
\mathrm { d } \psi \left( \mathbb { R } \cdot \left( \begin{array} { c c } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right) \right) \subset J \mathfrak { a }
$$

and

$$
\mathrm { d } \psi \left( \mathbb { R } \cdot \left( \begin{array} { c c } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right) \right) \subset \left[ \mathfrak { a } , J \mathfrak { a } \right] .
$$

This shows that $\psi$ factors through $\operatorname { I m } \varphi \subset G$ , and hence that $\psi _ { 2 }$ factors through

$$
\psi _ { 2 } ^ { * } : { \mathrm { S L } } ( 2 , \mathbb { R } ) \longrightarrow { \mathrm { S L } } ( 2 , \mathbb { R } ) ^ { r } \ : .
$$

Now, $\mathrm { p r } _ { i } \circ \psi _ { 2 } ^ { * }$ is either trivial or conjugate to the identity by some element of $k _ { i } \in \mathbf { S O } ( 2 , \mathbb { R } )$ , from which we see that $\varphi _ { 2 } ( k _ { 1 } , \ldots , k _ { r } ) \cdot \widetilde { \psi }$ has the required form.

Next, we want to decompose $\mathfrak { g }$ into irreducible pieces under the restriction of the adjoint representation to $U ^ { 1 } \times { \bf S } \mathrm { L } ( 2 , \mathbb { R } ) ^ { r }$ . The irreducible real representations of $U ^ { 1 } \times { \bf S } \mathrm { L } ( 2 , \mathbb { R } ) ^ { r }$ are easily enumerated as follows.

(a) The irreducible real representations of  $U ^ { 1 }$ are:

• $U _ { 0 } = \mathbb { R }$ , trivial representation; • $U _ { k } = \mathbb { R } ^ { 2 }$ , with action

$$
{ \mathrm { e } } ^ { { \mathrm { i } } \theta } \longmapsto { \left( \begin{array} { l l } { \cos k \theta } & { \sin k \theta } \\ { - \sin k \theta } & { \cos k \theta } \end{array} \right) } ~ ,
$$

for $k = 1 , 2 , \ldots$ .

Note that these representations are only irreducible as real representations: they split over $\mathbb { C }$ into the direct sum of two one-dimensional representations with characters

$$
\mathrm { e } ^ { \mathrm { i } \theta } \longmapsto ( \mathrm { e } ^ { \mathrm { i } \theta } ) ^ { \pm k } \ ,
$$

respectively.

(b) The irreducible representations of $\mathrm { S L } ( 2 , \mathbb { R } )$ are

• $W _ { k }$ , the $k$ ’th symmetric power of the standard representation, for $k =$ $0 , 1 , 2 , \ldots$ .

Note that these are complex-irreducible as well.

It follows easily that the irreducible representation of $U ^ { 1 } \times { \bf S } \mathrm { L } ( 2 , \mathbb { R } ) ^ { r }$ are of the form

$$
U _ { i } \otimes W _ { j _ { 1 } } \otimes \ldots \otimes W _ { j _ { r } } ~ .
$$

The fact that $U ^ { 1 }$ , acting via $h _ { o }$ on ${ \mathfrak { g } } _ { \mathbb { C } }$ , has only the characters $z ^ { 2 } , 1 , z ^ { - 2 }$ implies easily that, if this representation appears in ${ \mathfrak { g } } _ { \mathbb { C } }$ , then

$$
i + \sum _ { k = 1 } ^ { r } j _ { k } = 0 \mathrm { o r } 2 ,
$$

and we get:

Proposition 2.7 The irreducible representations of $U ^ { 1 } \times { \mathrm { S L } } ( 2 , \mathbb { R } ) ^ { r }$ which appear in $\mathfrak { g }$ are at most the following:

$$
\begin{array} { r l } & { U _ { 0 } \otimes \left( W _ { 0 } \otimes \cdots \otimes W _ { 2 } \otimes \cdots \otimes W _ { 0 } \right) \quad \left( \mathrm { o n e ~ } W _ { 2 } \right) ; } \\ & { U _ { 0 } \otimes \left( W _ { 0 } \otimes \cdots \otimes W _ { 1 } \otimes \cdots \otimes W _ { 1 } \otimes \ldots \otimes W _ { 0 } \right) \quad \left( \mathrm { t w o ~ } W _ { 1 } \right) ; } \\ & { U _ { 1 } \otimes \left( W _ { 0 } \otimes \cdots \otimes W _ { 1 } \otimes \cdots \otimes W _ { 0 } \right) \quad \left( \mathrm { o n e ~ } W _ { 1 } \right) ; } \\ & { U _ { 2 } \otimes \mathrm { t r i v i a l ~ } ; } \\ & { U _ { 0 } \otimes \mathrm { t r i v i a l ~ } . } \end{array}
$$

Moreover, the image via dϕ of the ith copy of $\mathrm { S L } ( 2 , \mathbb { R } ) ^ { r }$ defines a representation of type $\left( \mathbf { a } _ { i } \right)$ , and this is the only one of this type. Furthermore, (d) does not occur at all.

Proof Let $V$ be a representation of type $\left( \mathbf { a } _ { i } \right)$ or (d). Then, in both cases, $V$ contains a 2-dimensional subrepresentation $W$ , where $h _ { 0 }$ acts by the representation $U _ { 2 }$ , containing some $0 \neq w \in W$ on which $\mathfrak { a }$ acts trivially. The first condition implies that $w \in { \mathfrak { p } }$ , whence by the maximality of $\mathfrak { a }$ we get $w \in { \mathfrak { a } }$ . This leads to the given factors of type $\left( \mathbf { a } _ { i } \right)$ .

This proposition gives us a bird’s-eye view of the complex root decomposition of ${ \mathfrak { g } } _ { \mathbb { C } }$ in which ad $\mathbf { t } _ { \mathbb { C } }$ is diagonalized, and, simultaneously, of the real root decomposition of $\mathfrak { g }$ in which ad $\mathfrak { a }$ is diagonalized. To be precise, let

$$
{ \mathfrak { a } } ^ { \prime } = \sum _ { i = 1 } ^ { r } \mathbb { R } \cdot h _ { i } \subset \mathrm { i t } ~ ,
$$

and define

$$
\varphi \sim \psi \Longleftrightarrow \varphi - \psi | _ { \mathfrak { a } ^ { \prime } } \equiv 0 , { \mathrm { f o r } } \varphi , \psi \in \Psi .
$$

Proposition 2.7 tells us which representations of ${ \mathfrak { a } } ^ { \prime }$ may occur in $\mathfrak { g }$ and, in particular, tells us that, for all $\varphi \in \Psi$ , one of the following occurs:

(I) $\varphi \sim \pm \gamma _ { i } ^ { \prime }$ , for some $i$ , in which case

$$
{ \mathfrak { g } } ^ { \varphi } \subset \operatorname { f a c t o r \ o f \ t y p e \ } ( { \mathfrak { a } } _ { i } ) , \operatorname { h e n c e \ i n \ f a c t \ } { \varphi } = \pm \gamma _ { i } ^ { \prime } ;
$$

(II) $\begin{array} { r } { \varphi \sim \frac { 1 } { 2 } ( \pm \gamma _ { i } ^ { \prime } \pm \gamma _ { j } ^ { \prime } ) } \end{array}$ , for some $i \neq j$ , in which case

$$
{ \mathfrak { g } } ^ { \varphi } \subset { \mathrm { f a c t o r ~ o f ~ t y p e ~ ( b } _ { i j } ) } ~ ;
$$

(III) $\varphi \sim \pm { \frac { 1 } { 2 } } \gamma _ { i } ^ { \prime }$ , for some $i$ , in which case

$$
\mathfrak { g } ^ { \varphi } \subset \mathrm { f a c t o r o f t y p e } \left( \mathbf { c } _ { i } \right) ;
$$

(IV) $\varphi \sim 0$ , in which case

$$
{ \mathfrak { g } } ^ { \varphi } \subset \operatorname { f a c t o r } { \mathrm { o f ~ t y p e ~ ( e ) } } .
$$

But because we also know how $h _ { o }$ acts on each of these factors, we can say more:

(I) each $\left( \mathbf { a } _ { i } \right)$ -factor is just $\mathbb { R } ( \mathrm { i } h _ { i } ) + \mathbb { R } x _ { i } + \mathbb { R } y _ { i }$ , giving one positive non-compact root $\gamma _ { i } ^ { \prime }$ and one negative non-compact root $- \gamma _ { i } ^ { \prime }$ ;   
(II) each of the $( \mathbf { b } _ { i j } )$ -factors is 4-dimensional and each gives one positive noncompact root, $\begin{array} { r } { \sim \frac { \gamma _ { i } ^ { \prime } + \gamma _ { j } ^ { \prime } } { 2 } } \end{array}$ ; two compact roots, one positive and one negative, $\sim \pm \frac { \gamma _ { i } ^ { \prime } - \gamma _ { j } ^ { \prime } } { 2 }$ , respectively, and one negative non-compact root, $\begin{array} { r } { \sim - \frac { \gamma _ { i } ^ { \prime } + \gamma _ { j } ^ { \prime } } { 2 } } \end{array}$   
(III) each of the $( \mathrm { c } _ { i } )$ -factors is 4-dimensional and each gives one positive noncompact root, $\sim \gamma _ { i } ^ { \prime } / 2$ , two compact roots, one positive and one negative, $\sim \pm \gamma _ { i } ^ { \prime } / 2$ , respectively, and one negative non-compact root, $\sim - \gamma _ { i } ^ { \prime } / 2$ ;   
(IV) each of the (e)-factors is 1-dimensional and gives a compact root, $\sim 0$ .

We can coarsen our complex root decomposition

$$
{ \mathfrak { g } } = { \mathfrak { t } } _ { \mathbb { C } } \oplus \sum _ { \varphi \in \Psi } { \mathfrak { g } } ^ { \varphi }
$$

by lumping together root spaces with equivalent roots. Let $\mathbf { \mathbb { R } } ^ { \Psi ^ { \prime } }$ be the set of non-zero linear maps ${ \mathfrak { a } } ^ { \prime } \longrightarrow \mathbb { R }$ given by restricting roots $\varphi \in \Psi$ to ${ \mathfrak { a } } ^ { \prime }$ , so that

$$
{ \mathfrak { g } } _ { \mathbb { C } } = Z ( { \mathfrak { a } } ^ { \prime } ) _ { \mathbb { C } } \oplus \sum _ { \psi ^ { \prime } \in _ { \mathbb { R } } \Psi ^ { \prime } } { \mathfrak { g } } ^ { \psi ^ { \prime } } ,
$$

where

$$
\begin{array} { r l } & { Z ( \mathfrak { a } ^ { \prime } ) _ { \mathbb { C } } = \mathfrak { a } _ { \mathbb { C } } \oplus \sum _ { \varphi \sim 0 } \mathfrak { g } ^ { \varphi } \ , } \\ & { \qquad \mathfrak { g } ^ { \psi ^ { \prime } } = \sum _ { \varphi \in \Psi , \varphi \sim \psi ^ { \prime } } \mathfrak { g } ^ { \varphi } } \\ & { \qquad = \mathrm { e i g e n s p a c e \ i n \ \mathfrak { g } _ { \mathbb { C } } , \ w h e r e \ a d \mathfrak { a } ^ { \prime } \ i s \ g i v e n b y \ t h e \ c h a r a c t e r } } \end{array}
$$

Then this is essentially the real root decomposition of $\mathfrak { g }$ with respect to the split torus $A = \exp { \mathfrak { a } }$ . In fact, if

$$
c = \varphi \left( . . . , \frac { 1 } { \sqrt { 2 } } \left( \begin{array} { c c } { { 1 } } & { { \mathrm { i } } } \\ { { \mathrm { i } } } & { { 1 } } \end{array} \right) , . . . \right) ,
$$

then $\mathbf { A d } c ( \mathfrak { a } ) = \mathfrak { a } ^ { \prime }$ . Therefore, if $\mathbb { R } ^ { \Psi } = ( \mathbf { A d } c ) ^ { * } ( \mathbf { \mathbb { R } ^ { \Psi ^ { \prime } } } )$ is the induced set of linear maps ${ \mathfrak { a } } \longrightarrow \mathbb { R }$ , we get an isomorphic decomposition of $\mathfrak { g }$ via ad $\mathfrak { a }$ . But now $\mathfrak { a }$ is real, so it is a real decomposition:

$$
{ \mathfrak { g } } = Z ( { \mathfrak { a } } ) \oplus \sum _ { \psi \in \mathbb { R } ^ { \Psi } } { \mathfrak { g } } ^ { \psi } ,
$$

where

What is $\mathbb { R } ^ { \Psi }$ , i.e., which combinations of factors actually occur in $\mathfrak { g }$ in the above proposition? First of all, $\left( \mathbf { a } _ { i } \right)$ occurs once. We will denote the corresponding roots of $\mathfrak { a }$ by $\pm \gamma _ { i }$ : these are simply the roots of $\mathfrak { a }$ occurring in the image under ${ \mathrm { d } } \varphi$ of the ith copy of ${ \mathfrak { s l } } ( 2 , \mathbb { R } )$ ; in fact, in $\mathbb { R } x _ { i } + \mathbb { R } y _ { i } + \mathbb { R } \mathbf { i } h _ { i }$ . As for the rest, the result is:

Proposition 2.8 Let $D$ be simple of rank $r$ . Then either of the following two possibilities occurs:

Case $C _ { r } : \qquad \mathbb { R } ^ { \Psi } = \left\{ \pm { \textstyle \frac { 1 } { 2 } } ( \gamma _ { i } + \gamma _ { j } ) \mathrm { f o r } i \geq j ; \pm { \textstyle \frac { 1 } { 2 } } ( \gamma _ { i } - \gamma _ { j } ) \mathrm { f o r } i > j \right\}$ all $\left( \mathbf { b } _ { i j } \right)$ -factors occur, but no $\left( \mathrm { c } _ { i } \right)$ -factors occur;

Case $B C _ { r }$ : ${ \scriptstyle { \mathbb R } } \Psi = \left\{ \pm \frac { 1 } { 2 } ( \gamma _ { i } + \gamma _ { j } ) \mathrm { ~ f o r ~ } i \geq j ; \pm \frac { 1 } { 2 } ( \gamma _ { i } - \gamma _ { j } ) \mathrm { ~ f o r ~ } i > j ; \pm \frac { 1 } { 2 } \gamma _ { i } \right\} ,$ all $\left( \mathbf { b } _ { i j } \right)$ - and all $\left( \mathrm { c } _ { i } \right)$ -factors occur.

In both of these cases, the Weyl group (the automorphisms of a induced by $\operatorname { A d N o r m } \left( A \right) )$ is the group of all signed permutations $\gamma _ { i } \longmapsto \pm \gamma _ { \sigma ( i ) }$ with $\sigma \ a$ permutation of $\{ 1 , \ldots , r \}$ . If we order the real roots so that $\gamma _ { 1 } > \cdots > \gamma _ { r }$ , the simple roots $\mathbb { R } ^ { \Delta }$ are:

$$
\alpha _ { i } = ( \gamma _ { i } - \gamma _ { i + 1 } ) / 2 , 1 \leq i \leq r - 1 ; \quad a n d \quad \alpha _ { r } = \left\{ \begin{array} { l l } { \gamma _ { r } } & { \mathrm { C a s e } \ : C _ { r } } \\ { \gamma _ { r } / 2 } & { \mathrm { C a s e } \ : B C _ { r } . } \end{array} \right.
$$

Proof In the image under $\varphi$ of the ith factor of $\mathrm { S L } ( 2 , \mathbb { R } )$ there exists an element $w _ { i }$ which normalizes $\mathfrak { a }$ , sends $\gamma _ { i }$ into $- \gamma _ { i }$ , and fixes the $\gamma _ { j }$ for $j \neq i$ . Let $s _ { i } =$ $\operatorname { A d } \left( w _ { i } \right)$ : then $s _ { i }$ belongs to the Weyl group $W$ . In particular, this implies that the $\gamma _ { i }$ are orthogonal to each other. By Proposition 2.7, the other roots are among the following:

$$
\begin{array} { c } { { ( { \bf b } _ { i j } ) : \frac 1 2 ( \pm \gamma _ { i } \pm \gamma _ { j } ) , } } \\ { { ( { \bf c } _ { i } ) : \pm \frac 1 2 \gamma _ { i } . } } \end{array}
$$

The Weyl group $W$ is generated by the reflections around the roots, i.e., by the $s _ { i }$ and, if $\textstyle { \frac { 1 } { 2 } } ( \pm \gamma _ { i } \pm \gamma _ { j } )$ occurs as a root, by the symmetry which interchanges the two roots $\gamma _ { i }$ and $\gamma _ { j }$ , leaving fixed the roots $\gamma _ { k }$ , for $k \neq i , j$ . Since $D$ is simple, $W$ acts irreducibly on $\mathfrak { a }$ ; i.e., $W / {  }$ (sign changes) is a transitive group of permutations of $\{ 1 , \ldots , r \}$ generated by transpositions. It follows that $W$ contains all permutations of the $\gamma _ { i }$ among themselves. This implies that all $\textstyle { \frac { 1 } { 2 } } ( \pm \gamma _ { i } \pm \gamma _ { j } )$ are roots and that either all or none of the $\textstyle { \frac { 1 } { 2 } } \gamma _ { i }$ are roots. The first case leads to the type $C _ { r }$ , and the second case leads to the type $B C _ { r }$ . The simple roots are now easily written down.

# 2.4

We now return to the general case, i.e., drop the assumption that $D$ is simple. Theorem 2.9 below determines the position of $D$ inside ${ \mathfrak { p } } _ { + }$ , with $D$ sitting inside ${ \mathfrak { p } } _ { + }$ via the Harish-Chandra embedding.

For $X \in { \mathfrak { p } } _ { + }$ , define the linear operator

$$
\begin{array} { r } { { T ( X ) : { \mathfrak { p } } _ { - } \longrightarrow { \mathfrak { k } } _ { \mathbb { C } } \ , \ } } \\ { { Y \longmapsto [ Y , X ] \ . } } \end{array}
$$

If

$$
\tau : { \mathfrak { g } } _ { \mathbb { C } } \longrightarrow { \mathfrak { g } } _ { \mathbb { C } }
$$

denotes complex conjugation with respect to ${ \mathfrak { g } } _ { c }$ , we put a positive-definite hermitian form on ${ \mathfrak { g } } \mathbb { C }$ :

$$
B _ { \tau } ( u , \nu ) = - B ( u , \tau \nu ) , \mathrm { f o r } u , \nu \in \mathfrak { g } _ { \mathbb { C } } .
$$

Let

$$
T ^ { * } ( X ) : { \mathfrak { k } } _ { \mathbb { C } } \longrightarrow { \mathfrak { p } } _ { - }
$$

be the adjoint of $T ( X )$ with respect to $B _ { \tau }$ .

# Theorem 2.9 (Harish-Chandra, Hermann) Let

$$
D _ { 0 } = D \cap \sum _ { i = 1 } ^ { r } \mathbb { C } \cdot e _ { i } .
$$

Then

(i) with $\widetilde { \varphi }$ defined as in Theorem 2.4,

$$
D _ { 0 } = \left\{ \sum _ { i = 1 } ^ { r } a _ { i } e _ { i } \mid | a _ { i } | < 1 \right\} = \operatorname { I m } \left( { \widetilde { \varphi } } : { \mathfrak { H } } ^ { r } \longrightarrow D \right) ;
$$

$$
D = \mathrm { A d } K ( D _ { 0 } ) = \{ X \in { \mathfrak { p } } _ { + } \mid T ^ { * } ( X ) \circ T ( X ) < 2 \mathrm { I d } _ { \mathfrak { p } _ { - } } \} \ .
$$

In particular, if $a , b \in \mathbb { C } ,$ , with $| a | + | b | \leq 1$ , then

$$
X , Y \in D \Longrightarrow a X + b Y \in D .
$$

(Part (ii) is called the Hermann convexity theorem.)

Proof We use the fact that $D \longrightarrow { \mathfrak { p } } _ { + }$ is $K \cdot$ -equivariant, where $K$ acts via Ad on ${ \mathfrak { p } } _ { + }$ . Thus $D = K \cdot A \cdot o$ , so $D$ can be described inside ${ \mathfrak { p } } _ { + }$ as $D = \operatorname { A d } K ( A \cdot o )$ . Now, a calculation with SL(2) shows that

$$
A \cdot o = \left\{ \sum _ { i = 1 } ^ { r } a _ { i } e _ { i } \mid a _ { i } \in \mathbb { R } , - 1 < a _ { i } < 1 \right\}
$$

and

$$
\operatorname { I m } { \widetilde { \varphi } } = \left\{ \sum _ { i = 1 } ^ { r } a _ { i } e _ { i } \mid a _ { i } \in \mathbb { C } , \vert a _ { i } \vert < 1 \right\} .
$$

The isomorphism ${ \mathfrak { p } } _ { + } \cong { \mathfrak { p } }$ is also $K$ -equivariant and it is well-known that in $\mathfrak { p }$ for every $k \in K$ , either

(a) $\mathbf { A d } k ( { \mathfrak { a } } ) \cap { \mathfrak { a } } \subset$ singular subalgebra of $\mathfrak { a }$ ; or (b) $\mathbf { A d } k ( \mathfrak { a } ) = \mathfrak { a }$ , and hence $k$ lies in the Weyl group.

Thus, if $D \cap \Sigma _ { i = 1 } ^ { r } \mathbb { R } e _ { i }$ were bigger than $\Pi _ { i = 1 } ^ { r } ( - 1 , + 1 ) e _ { i }$ , then one could find $x \in$ $D \cap \Sigma _ { i = 1 } ^ { r } \mathbb { R } e _ { i }$ such that $x$ lies in no singular subalgebra and $x \notin \Pi _ { i = 1 } ^ { r } ( - 1 , + 1 ) e _ { i }$ with

$$
x = ( \mathrm { A d } k ) ( y ) , \quad y \in \prod _ { i = 1 } ^ { r } ( - 1 , + 1 ) e _ { i } .
$$

Then $k$ would be in the Weyl group, and hence $\operatorname { A d } k$ would be a permutation plus sign change, and hence $x \in \Pi _ { i = 1 } ^ { r } ( - 1 , + 1 ) e _ { i }$ , a contradiction. Therefore $D \cap \Sigma _ { i = 1 } ^ { r } \mathbb { R } e _ { i } = \prod _ { i = 1 } ^ { r } ( - 1 , + 1 ) e _ { i }$ . Since Ad $K$ contains rotations in the planes $\mathbb { C }$ · $e _ { i }$ (via $\varphi ( \mathbf { \boldsymbol { S } } \mathbf { \boldsymbol { O } } ( 2 , \mathbb { R } ) ^ { r } ) )$ , it follows that $D _ { 0 }$ is rotation-invariant and (i) is proven.

To prove (ii), note that the sets on both sides are $K$ -invariant, so it suffices to consider elements

$$
X = \sum _ { i = 1 } ^ { r } a _ { i } e _ { i } \ , \quad a _ { i } \in \mathbb { R } \ ,
$$

and show that

$$
T ^ { * } ( X ) \circ T ( X ) < 2 \mathrm { I d } \iff | a _ { i } | < 1 { \mathrm { ~ f o r ~ } } i = 1 , \dots , r .
$$

Expressed in terms of operator norms,

$$
\mid \mid S \mid \mid ^ { 2 } = \operatorname * { s u p } \{ B _ { \tau } ( S ( Y ) , S ( Y ) ) \mid B _ { \tau } ( Y , Y ) = 1 \} ,
$$

the condition on the LHS is just

$$
\parallel T ( X ) \parallel < { \sqrt { 2 } } .
$$

We thus have to show that

$$
\parallel T ( X ) \parallel < \sqrt { 2 } \Longleftrightarrow | a _ { i } | < 1 \mathrm { f o r } i = 1 , \ldots , r .
$$

This is done by an explicit computation: write $Y \in { \mathfrak { p } } _ { - }$ as

$$
Y = \sum _ { i = 1 } ^ { r } b _ { i } e _ { - i } + \sum _ { i = 1 } ^ { r } \sum _ { \alpha \in P _ { i } } b _ { \alpha } e _ { - \alpha } + \sum _ { i < j } \sum _ { \alpha \in P _ { i j } } b _ { \alpha } e _ { - \alpha } \ ,
$$

where

$$
\begin{array} { r l } & { P _ { i } = \mathrm { \{ p o s i t i v e ~ n o n - c o m p a c t ~ r o o t s ~ } } \varphi \mathrm { ~ w i t h ~ } \varphi \sim \frac { 1 } { 2 } \gamma _ { i } ^ { \prime } \mathrm { \} \ , } \\ & { P _ { i j } = \mathrm { \{ p o s i t i v e ~ n o n - c o m p a c t ~ r o o t s ~ } } \varphi \mathrm { ~ w i t h ~ } \varphi \sim \frac { 1 } { 2 } ( \gamma _ { i } ^ { \prime } + \gamma _ { j } ^ { \prime } ) \mathrm { \} . } \end{array}
$$

We compute $[ X , Y ]$ , using the vanishing of various brackets:

$$
[ X , Y ] = \sum _ { i } a _ { i } b _ { i } [ e _ { i } , e _ { - i } ] + \sum _ { i } \sum _ { \alpha \in P _ { i } } a _ { i } b _ { \alpha } [ e _ { i } , e _ { - \alpha } ] + \sum _ { i \neq j } \sum _ { \alpha \in P _ { i j } } a _ { i } b _ { \alpha } [ e _ { i } , e _ { - \alpha } ] .
$$

Furthermore, by our normalization of the $e _ { \alpha }$ ,

$$
\tau ( e _ { \alpha } ) = - e _ { - \alpha } ;
$$

hence $\alpha \neq \beta \Longrightarrow B _ { \tau } ( e _ { \alpha } , e _ { \beta } ) = 0$ , and all terms in the sum (2.2) are orthogonal to each other. Using this, together with the Jacobi identity, one computes

$$
B _ { \tau } ( [ e _ { i } , e _ { - \alpha } ] , [ e _ { i } , e _ { - \beta } ] ) = \alpha ( h _ { i } ) \cdot B ( e _ { - \alpha } , e _ { \beta } ) ~ ,
$$

and this expression vanishes unless $\alpha = \beta$ . Thus the brackets in sum (2.3) are orthogonal to each other.

We may now compare

$$
\begin{array} { r } { \parallel Y \parallel ^ { 2 } = \underset { i } { \sum } \left| b _ { i } \right| ^ { 2 } \parallel e _ { - i } \parallel ^ { 2 } + \underset { i < j } { \sum } \underset { \alpha \in P _ { i } } { \sum } \left| b _ { \alpha } \right| ^ { 2 } \parallel e _ { - \alpha } \parallel ^ { 2 } } \\ { + \underset { i < j } { \sum } \underset { \alpha \in P _ { i j } } { \sum } \left| b _ { \alpha } \right| ^ { 2 } \parallel e _ { - \alpha } \parallel ^ { 2 } } \end{array}
$$

with

$$
\begin{array} { l } { { \displaystyle \| { \bf \Pi } [ { \cal X } , { \cal Y } ] \| ^ { 2 } = \sum _ { i } | b _ { i } | ^ { 2 } | a _ { i } | ^ { 2 } | \gamma _ { i } ( h _ { i } ) | \mathrm { ~ } \| e _ { - i } \| ^ { 2 } } } \\ { { \displaystyle ~ + \sum _ { i } \sum _ { \alpha \in { \cal P } _ { i } } | b _ { \alpha } | ^ { 2 } | a _ { i } | ^ { 2 } | \alpha ( h _ { i } ) | \mathrm { ~ } \| e _ { - \alpha } \| ^ { 2 } } } \\ { { \displaystyle ~ + \sum _ { i < j } \sum _ { \alpha \in { \cal P } _ { i j } } \left( | a _ { i } | ^ { 2 } | b _ { \alpha } | ^ { 2 } | \alpha ( h _ { i } ) | + | a _ { j } | ^ { 2 } | b _ { \alpha } | ^ { 2 } | \alpha ( h _ { j } ) | \right) \| e _ { - \alpha } \| ^ { 2 } } } .  \end{array}
$$

Thus, if $\left| a _ { i } \right| < 1$ , for $i = 1 , \ldots , r$ , it is evident that $\parallel T ( X ) \parallel ^ { 2 } < 2 .$ Conversely, if $\parallel \left[ X , Y \right] \parallel < { \sqrt { 2 } } \parallel Y \parallel$ , for all $Y \in { \mathfrak { p } } _ { - }$ , then, as one sees by plugging $Y = e _ { - i }$ into the above expression, we must have $\left| a _ { i } \right| < 1$ for $i = 1 , \ldots , r$ .

Corollary 2.10 (of proof) Let $X \in D$ and write

$$
X = \sum a _ { i } e _ { i } + \sum b _ { \alpha } e _ { \alpha } ,
$$

where $\alpha$ runs through all positive non-compact roots restricting to either $\textstyle { \frac { 1 } { 2 } } \gamma _ { i }$ or $\begin{array} { r } { \frac { 1 } { 2 } \left( \gamma _ { i } + \gamma _ { j } \right) } \end{array}$ (i.e., not restricting to $\gamma _ { i }$ ).

Then $\left| a _ { i } \right| < 1$ for $i = 1 , \ldots , r .$

This can be seen by calculating $[ X , e _ { - i } ]$ in the same way as above; cf. Langlands [8], p. 110.

#

As a final topic, suppose $\mathcal { G }$ is a semi-simple algebraic group defined over $\mathbb { Q }$ such that $D = \mathcal { G } ( \mathbb { R } ) ^ { o } / K$ , for $K \subset \mathcal { G } ( \mathbb { R } ) ^ { o }$ maximal compact, is a bounded symmetric domain. (This usually means that $\mathcal { G } ( \mathbb { R } ) ^ { o } / ( \mathrm { c e n t e r } ) = \mathrm { A u t } ( D ) ^ { o }$ , but it also allows ${ \mathcal { G } } ( \mathbb { R } ) ^ { o }$ to have compact factors, i.e.,

$$
{ \mathcal { G } } ( { \mathbb { R } } ) ^ { o } / ( \mathrm { c o m p a c t ~ n o r m a l ~ s u b g r o u p } ) = \mathrm { A u t } ( D ) ^ { o } ~ . )
$$

In this case, an important role is played by the maximal $\mathbb { Q }$ -split tori $\mathcal { A } \subset \mathcal { G }$ . (If $\mathcal { A }$ is non-trivial and $\mathcal { G }$ is $\mathbb { Q }$ -simple, then, in fact, ${ \mathcal { G } } ( \mathbb { R } ) ^ { o }$ has no compact factors.) Choose $\mathcal { B } \subset \mathcal { G }$ , a maximal $\mathbb { R }$ -split torus such that ${ \mathcal { A } } \subset { \mathcal { B } }$ . Let $s = \dim { \mathcal { A } } = \mathbb { Q }$ -rank $\mathcal { G }$ and $r = \dim { \mathcal { B } } = \mathbb { R }$ -rank $\mathcal { G }$ . Note that compact factors do not change the root structure so that the preceding results are still applicable. The roots of $\mathcal { G }$ with respect to $\mathcal { B }$ are a basis

$$
\gamma _ { i } \in X _ { \mathbb { Q } } ( \mathcal { B } ) = \mathrm { H o m } \left( \mathcal { B } , \mathbb { G } _ { m } \right) \otimes \mathbb { Q } \mathrm { ~ f o r ~ } 1 \leq i \leq r
$$

plus some subset of the further elements,

$$
\begin{array} { r } { \frac 1 2 ( \pm \gamma _ { i } \pm \gamma _ { j } ) , \quad 1 \le i < j \le r ; \quad \pm \frac { 1 } { 2 } \gamma _ { i } , \quad 1 \le i \le r . } \end{array}
$$

Baily and Borel [1], pp. 467–468, prove by a purely root-theoretic analysis the following basic fact.

Proposition 2.11 There is a partition

$$
\{ 1 , \ldots , s \} = I _ { 0 } \cup I _ { 1 } \cup I _ { 2 } \cup \ldots \cup I _ { r }
$$

such that the subtorus $\mathcal { A }$ is defined by

$$
{ \mathcal { A } } = \left\{ \gamma _ { i } = 1 { \mathrm { ~ f o r ~ } } i \in I _ { 0 } \ ; \quad \ \gamma _ { i } = \gamma _ { j } { \mathrm { ~ f o r ~ } } i , j \in I _ { k } , { \mathrm { ~ w h e r e ~ } } k > 0 \right\}
$$

or, in additive notation,

$$
\begin{array} { r l } & { X _ { \mathbb { Q } } ( \mathcal { A } ) \cong X _ { \mathbb { Q } } ( \mathcal { B } ) / \left\{ \begin{array} { l l } { \mathrm { s u b s p a c e ~ s p a n n e d ~ b y ~ } \gamma _ { i } \mathrm { ~ f o r ~ } i \in I _ { 0 } } \\ { \mathrm { a n d ~ } \gamma _ { i } - \gamma _ { j } f o r i , j \in I _ { k } , \mathrm { ~ w h e r e ~ } k > 0 } \end{array} \right\} ; } \\ & { \qquad \cong \underset { i = 1 } { \overset { s } { \sum } } \mathbb { Q } \beta _ { i } , \mathrm { ~ w h e r e ~ } \beta _ { i } = \mathrm { i m a g e ~ o f ~ a n y ~ } \gamma _ { j } , j \in I _ { i } . } \end{array}
$$

(Their result is stated differently, but boils down to the above.)

Corollary 2.12 The $\mathbb { Q }$ -roots are $\pm \beta _ { 1 } , \ldots , \pm \beta _ { s }$ plus a subset of the further elements $\pm \beta _ { i } / 2$ , $( \pm \beta _ { i } \pm \beta _ { j } ) / 2$ for $i \neq j .$ . If $\mathcal { G }$ is $\mathbb { Q }$ -simple, then all $( \pm \beta _ { i } \pm \beta _ { j } ) / 2$ occur and either all $\pm \beta _ { i } / 2$ occur or none do. The $\mathbb { Q }$ -Weyl group is then the full group of permutations and sign changes of the $\beta _ { i }$ .

# 3 Boundary components

In this section we decompose the closure $\overline { { D } }$ of $D$ inside ${ \mathfrak { p } } _ { + }$ into the disjoint union of lower-dimensional bounded domains, the boundary component. We analyze the structure of boundary components and determine their normalizers and centralizers.

# 3.1

Start with

$$
\mathsf { a } = \sum \mathbb { R } x _ { i } \subset \mathsf { p }
$$

and

$$
\mathfrak { s l } ( 2 , \mathbb { R } ) ^ { r } \cong \sum \mathbb { R } x _ { i } + \sum \mathbb { R } y _ { i } + \sum \mathbb { R } \mathfrak { i } h _ { i } \subset \mathfrak { g }
$$

as in Theorem 2.4. Let $S \subset \{ 1 , \ldots , r \}$ be any subset. $^ \dagger$ Define the subalgebra $\rho _ { S }$ of $\mathfrak { g }$ :

$$
\begin{array} { r } { \mathrm { I } _ { S } = \displaystyle \sum _ { \varphi \in \mathbb R ^ { \Psi } } \left( \mathfrak { g } ^ { \varphi } + [ \mathfrak { g } ^ { \varphi } , \mathfrak { g } ^ { - \varphi } ] \right) \ : . } \\ { \quad \varphi { = } \displaystyle \sum _ { j \notin S } a _ { j } \gamma _ { j } \quad \quad } \end{array}
$$

In the decomposition of Proposition 2.7,  $\rho _ { S }$ may be described as follows:

$$
\mathrm { l } _ { S } = \sum _ { i \notin S } ( \mathrm { a } _ { i } \mathrm { - f a c t o r } ) \oplus \sum _ { i < j \atop i , j \notin S } ( \mathrm { b } _ { i j } \mathrm { - f a c t o r s } ) \oplus \sum _ { i \notin S } ( \mathrm { c } _ { i } \mathrm { - f a c t o r } )
$$

Hence $\mathfrak { l } _ { S , \mathbb { C } }$ can be written as a sum over the complex roots $\varphi \in \Psi$ :

$$
{ \mathfrak { l } } _ { S , \mathbb { C } } = \sum _ { \varphi \sim \sum _ { j \not \in S } a _ { j } \gamma _ { j } ^ { \prime } } \left( { \mathfrak { g } } ^ { \varphi } + [ { \mathfrak { g } } ^ { \varphi } , { \mathfrak { g } } ^ { - \varphi } ] \right) ~ .
$$

This shows that $\updownarrow _ { S }$ is stable under $\boldsymbol { \mathrm { A d } } h _ { o } ( \boldsymbol { \mathrm { e } } ^ { \mathrm { i } \theta } )$ ; hence

(a) $\updownarrow _ { S } = \updownarrow \cap \updownarrow _ { S } \oplus \ p \cap \updownarrow _ { S }$

and

$$
{ \mathfrak { p } } _ { \mathbb { C } } \cap { \mathfrak { l } } _ { S , \mathbb { C } } = { \mathfrak { p } } _ { + } \cap { \mathfrak { l } } _ { S , \mathbb { C } } \oplus { \mathfrak { p } } _ { - } \cap { \mathfrak { l } } _ { S , \mathbb { C } } ,
$$

which we abbreviate as follows:

$$
\mathfrak { p } _ { S , \mathbb { C } } = \mathfrak { p } _ { + , S } \oplus \mathfrak { p } _ { - , S } .
$$

By (a), $\rho _ { S }$ is a reductive subalgebra of $\mathfrak { g }$ , and, since it is generated by nilpotent elements, $\rho _ { S }$ is semi-simple without compact factors. By (b), $\rho _ { S }$ is of hermitian type. Let $L _ { S } \subset G$ be the corresponding subgroup. Then

$$
D _ { S } = L _ { S } / L _ { S } \cap K
$$

is a bounded symmetric domain and we have a symmetric embedding of $D _ { S }$ in $D$ . In fact, we have even more, because $L _ { S }$ commutes with the subgroup (modulo center)

$$
\prod _ { i \in S } \operatorname { S L } ( 2 , \mathbb { R } ) _ { i }
$$

$^ \dagger$ In what follows, we consider $S$ interchangeably as $S \subset \{ \gamma _ { 1 } , \ldots , \gamma _ { r } \}$ or $S \subset \{ 1 , \ldots , r \}$ .

arising from the subalgebra

$$
\sum _ { i \in S } ( \mathbb { R } x _ { i } + \mathbb { R } y _ { i } + \mathbb { R } \mathbf { i } h _ { i } ) \ .
$$

This shows that we get a whole equivariant diagram of symmetric holomorphic maps:

$$
{ \begin{array} { c c c c c } { \Delta ^ { s } \times D _ { S } } & { { \xrightarrow { f _ { 1 } } } } & { D } & { } \\ { \cap } & { } & { } & { \cap } \\ { \mathbb { C } ^ { s } \times { \mathfrak { p } } _ { + , S } } & { { \xrightarrow { f _ { 2 } } } } & { } & { \emptyset _ { + } } \\ { \cap } & { } & { } & { } & { \cap } \\ { \left( \mathbb { P } ^ { 1 } \right) ^ { s } \times { \check { D } } _ { S } } & { { \xrightarrow { f _ { 3 } } } } & { } & { { \check { D } } } \end{array} }
$$

where $s = | S |$ . (Here we identify the domain $\mathrm { S L } ( 2 , \mathbb { R } ) / \mathrm { S O } ( 2 )$ with the open unit disc $\Delta$ instead of ${ \mathfrak H }$ ; we will only do this for the purpose of the discussion that follows in Subsection 3.1.)

Define

$$
\begin{array} { l } { { F _ { S } = f _ { 2 } ( ( 1 , \ldots , 1 ) \times D _ { S } ) \subset { \mathfrak { p } } _ { + } , } } \\ { { { \check { F } } _ { S } = f _ { 3 } ( ( 1 , \ldots , 1 ) \times { \check { D } } _ { S } ) \subset { \check { D } } . } } \end{array}
$$

Note that $F _ { S }$ lies in $\partial D$ and is a complex submanifold of ${ \mathfrak { p } } _ { + }$ . In fact, $f _ { 2 }$ is linear and is just the inclusion map of the following subspace of ${ \mathfrak { p } } _ { + }$ :

$$
\sum _ { i \in S } \mathbb { C } e _ { i } + \left[ \underbrace { \sum _ { i \notin S } \mathbb { C } e _ { i } + \sum _ { i < j } \sum _ { \alpha \in P _ { i j } } \mathbb { C } e _ { \alpha } + \sum _ { i \notin S } \sum _ { \alpha \in P _ { i } } \mathbb { C } e _ { \alpha } } _ { i , j \notin S } \right] .
$$

Here, as in Subsection 2.4,

$$
\begin{array} { r l } & { P _ { i j } = \left\{ \varphi \in \Psi _ { p } ^ { + } \mid \varphi \sim \frac { 1 } { 2 } ( \gamma _ { i } ^ { \prime } + \gamma _ { j } ^ { \prime } ) \right\} , } \\ & { P _ { i } = \left\{ \varphi \in \Psi _ { p } ^ { + } \mid \varphi \sim \frac { 1 } { 2 } \gamma _ { i } ^ { \prime } \right\} . } \end{array}
$$

Thus by Hermann convexity applied to $D _ { S }$ :

$$
F _ { S } = \sum _ { i \in S } e _ { i } + \left\{ \overline { { X } } \in { \mathfrak { p } } _ { + , S } \mid T _ { S } ( \overline { { X } } ) ^ { * } \circ T _ { S } ( \overline { { X } } ) < 2 \mathrm { I d } _ { { \mathfrak { p } } _ { - , S } } \right\} \ ,
$$

where

$$
T _ { S } ( { \overline { { X } } } ) : { \mathfrak { p } } _ { - , S } \longrightarrow { \mathfrak { l } } _ { S , \mathbb { C } } \cap { \mathfrak { k } } _ { \mathbb { C } }
$$

is given by

$$
T _ { S } ( { \overline { { X } } } ) ( { \overline { { Y } } } ) = [ { \overline { { Y } } } , { \overline { { X } } } ] .
$$

We use this last description to prove:

Lemma 3.1 $\overline { { F } } _ { S } = \check { F } _ { S } \cap \overline { { D } }$ and all holomorphic maps

$$
\lambda : \Delta \longrightarrow { \mathfrak { p } } _ { + }
$$

such that

$$
\mathrm { I m } ( \lambda ) \subset \overline { { { D } } } , \qquad \mathrm { I m } \lambda \cap F _ { S } \neq \emptyset ,
$$

map $\Delta$ into $F _ { S }$ .

Proof Let $\begin{array} { r } { X = \sum _ { i } a _ { i } e _ { i } + \sum _ { i } \sum _ { \alpha \in P _ { i } } a _ { \alpha } e _ { \alpha } + \sum _ { i j } \sum _ { \alpha \in P _ { i j } } a _ { \alpha } e _ { \alpha } \in \mathfrak { p } _ { + } } \end{array}$ and assume that $X \in { \overline { { D } } }$ and $a _ { i } = 1$ , for $i \in S$ . Then we claim that $a _ { \alpha } = 0$ for $\alpha \in P _ { i }$ , $i \in S$ , and $a _ { \alpha } = 0$ for $\alpha \in P _ { i j }$ , $i$ or $j \in S$ .

For this, calculate $[ X , e _ { - i } ]$ as in the proof of the Hermann convexity theorem:

$$
\left[ X , e _ { - i } \right] = a _ { i } [ e _ { i } , e _ { - i } ] + \sum _ { \alpha \in P _ { i } \atop i \not = j } a _ { \alpha } [ e _ { \alpha } , e _ { - i } ] + \sum _ { \alpha \in P _ { i j } \atop i \not = j } a _ { \alpha } [ e _ { \alpha } , e _ { - i } ] \ ,
$$

hence

$$
\begin{array} { r l r } {  { \Vert [ X , e _ { - i } ] \Vert ^ { 2 } = 2 | a _ { i } | ^ { 2 } \Vert e _ { - i } \Vert ^ { 2 } } } \\ & { } & { + [ \sum _ { \alpha \in P _ { i } } | a _ { \alpha } | ^ { 2 } \Vert e _ { \alpha } \Vert ^ { 2 } + \sum _ { \alpha \in P _ { i j } } | a _ { \alpha } | ^ { 2 } \Vert e _ { \alpha } \Vert ^ { 2 } ] . } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

Since $X \in { \overline { { D } } }$ , we must have $\parallel [ X , e _ { - i } ] \parallel ^ { 2 } \leq 2 \parallel e _ { - i } \parallel ^ { 2 }$ by the Hermann convexity theorem. Hence, if $a _ { i } = + 1$ , then

$$
2 \parallel e _ { - i } \parallel ^ { 2 } + \left[ \sum _ { \alpha \in P _ { i } } | a _ { \alpha } | ^ { 2 } \parallel e _ { \alpha } \parallel ^ { 2 } + \sum _ { \alpha \in P _ { i j } \atop i \neq j } | a _ { \alpha } | ^ { 2 } \parallel e _ { \alpha } \parallel ^ { 2 } \right] \leq 2 \parallel e _ { - i } \parallel ^ { 2 } ,
$$

which shows the claim.

Hence, for such $X$ , we may write

$$
X = \sum _ { i \in S } e _ { i } + \overline { { { X } } } ,
$$

where $\overline { { X } } \in { \mathfrak { p } } _ { + , S }$ . But, since, for $\overline { { Y } } \in { \mathfrak { p } } _ { - , S }$ , $[ X , { \overline { { Y } } } ] = [ { \overline { { X } } } , { \overline { { Y } } } ]$ , we conclude that $T _ { S } ( { \overline { { X } } } ) ^ { * } \circ T _ { S } ( { \overline { { X } } } ) \leq 2 \mathrm { I d } _ { { \mathfrak { p } } _ { - , S } }$ , i.e., $\overline { { X } } \in \overline { { D } } _ { S } =$ closure of $D _ { S }$ inside $\mathfrak { p } _ { + , S }$ . This proves:

$$
{ \overline { { D } } } \cap \{ X \mid \mathrm { c o e f f . ~ } a _ { i } \mathrm { ~ o f ~ } e _ { i } \mathrm { ~ i s ~ } 1 , \mathrm { ~ f o r ~ } i \in S \} = \overline { { F } } _ { S } .
$$

We can now prove the lemma. The function $f _ { i }$ , which to

$$
x = \sum _ { i \in S } a _ { i } e _ { i } + \sum _ { i } \sum _ { \alpha \in P _ { i } } b _ { \alpha } e _ { \alpha } + \sum _ { i < j } \sum _ { \alpha \in P _ { i j } } b _ { \alpha } e _ { \alpha } \in \mathfrak { p } _ { + }
$$

associates $a _ { i } \in \mathbb { C }$ , is a linear function bounded above by 1 on $\overline { { D } }$ ; if $i \in S$ , then $f _ { i }$ takes on the value 1 on $F _ { S }$ . The maximum principle, applied to the holomorphic function $f _ { i } \circ \lambda : \Delta \longrightarrow \mathbb { C }$ , implies now that $f _ { i } \circ \lambda \equiv 1$ on $\Delta$ .

The preceding considerations show that $\lambda ( \Delta ) \subset \overline { { F } } _ { S }$ . But, by the Hermann convexity theorem, $D _ { S }$ is a convex subset of $\mathfrak { p } _ { + , S }$ , thought of as a real vector space; hence, for every $x \in \partial F _ { S } \subset \sum _ { i \in S } e _ { i } + { \mathfrak { p } } _ { + , S }$ , there exists a linear functional $\ell$ on ${ \mathfrak { p } } _ { + }$ and a real number $a$ such that $\ell > a$ on $F _ { S }$ and $\ell ( x ) = a$ . Now, again by the maximum principle, this time applied to $\ell \circ \lambda$ , we conclude that

$$
\mathrm { I m } ( \lambda ) \cap \partial F _ { S } \not = \emptyset \Longrightarrow \mathrm { I m } \lambda \subset \partial F _ { S } , \quad \mathrm { i . e . , I m } \lambda \cap F _ { S } = \emptyset ,
$$

which contradicts our assumptions; hence ${ \mathrm { I m } } \lambda \subset F _ { S }$ .

This proves that $F _ { S }$ is a boundary component of $D$ in the following sense.

Definition 3.2 A boundary component of a bounded symmetric domain $D$ is an equivalence class in $\overline { { D } }$ under the equivalence relation generated by $x \sim y$ if there exists a holomorphic map

$$
\lambda : \Delta \longrightarrow { \mathfrak { p } } _ { + }
$$

such that $\operatorname { I m } ( \lambda ) \subset { \overline { { D } } }$ , and $x , y \in \operatorname { I m } \lambda$ .

We now have:

# Theorem 3.3

(i) $\overline { { D } }$ is the disjoint union of boundary components.

(ii) The boundary components of $D$ are just the sets

$$
k \cdot F _ { S } ; k \in { \cal K } , \quad S \subset \{ 1 , . . . , r \} ,
$$

with possible repetitions. They are hermitian symmetric domains of rank $r - | S |$ .

(iii) Decompose

$$
D = D _ { 1 } \times \cdots \times D _ { n }
$$

into simple factors. Then the boundary components of $D$ are the products of boundary components of the simple factors $D _ { i }$ .

(iv) A boundary component of a boundary component is a boundary component.

(v) For every boundary component $F$ , there are holomorphic symmetric maps

![](images/529eb8cbf2ba43891009026641c5bcf8904dd9acb176d08c792b355805ec00b2.jpg)

such that $f _ { F } ( \mathrm { i } ) = o$ , $f _ { F } ( \infty ) \in F$ , and equivariant with respect to a morphism

$$
\varphi _ { F } : U ^ { 1 } \times { \mathrm { S L } } ( 2 , \mathbb { R } ) \longrightarrow G ,
$$

such that $\varphi _ { F } ( \mathrm { e } ^ { \mathrm { i } \theta } , h ^ { S L } ( \mathrm { e } ^ { \mathrm { i } \theta } ) ) = h _ { o } ( \mathrm { e } ^ { \mathrm { i } \theta } ) . ^ { \cdot }$ †

Proof Part (i) is trivial. For part (ii), let

$$
X \in { \cal F } = \mathrm { b o u n d a r y ~ c o m p o n e n t ~ o f } { \cal D } \ : .
$$

Since $K$ is maximal compact, $\begin{array} { r } { \overline { { D } } = { \mathrm { A d } } K \cdot \left( \prod _ { i = 1 } ^ { r } [ - 1 , + 1 ] \cdot e _ { i } \right) } \end{array}$ ; hence we can find $k \in K$ and a subset $S \subset \{ \gamma _ { 1 } , \ldots , \gamma _ { r } \}$ such that

$$
\operatorname { A d } \left( k \right) \left( X \right) = \sum _ { i = 1 } ^ { r } a _ { i } e _ { i } , a _ { i } \in [ - 1 , + 1 ] .
$$

But $K$ also contains elements normalizing $\mathfrak { a }$ and inducing arbitrary sign changes, so we may assume $a _ { i } \geq 0$ . Let $S = \{ i \mid a _ { i } = 1 \}$ . Then $\mathbf { A d } ( k ) ( X ) \in F _ { S }$ .

Part (iii) is straightforward; check that $x = ( x _ { 1 } , \ldots , x _ { n } )$ and $y = ( y _ { 1 } , \ldots , y _ { n } )$ in $\overline { { D } }$ are equivalent if and only if $x _ { i } \sim y _ { i }$ in $\overline { { D } } _ { i }$ for all $i$ . Part (iv) is an immediate consequence of (ii): let $D _ { 1 }$ be a boundary component of $D$ , and let $D _ { 2 }$ be a boundary component of $D _ { 1 }$ . Then

$$
D _ { 1 } = k \cdot F _ { S } = k \cdot \left( \sum _ { i \in S } e _ { i } + D _ { S } \right) \ ,
$$

and hence

$$
D _ { 2 } = k \cdot \left( \sum _ { i \in S } e _ { i } + D _ { 2 } ^ { \prime } \right) ~ ,
$$

where $D _ { 2 } ^ { \prime }$ is a boundary component of $D _ { S }$ . But then

$$
D _ { 2 } ^ { \prime } = k ^ { \prime } \cdot \left( \sum _ { i \in S ^ { \prime } } e _ { i } + D _ { S \cup S ^ { \prime } } \right)
$$

for some $k ^ { \prime } \in L _ { S } \cap K , S ^ { \prime } \subset \{ 1 , . . . , r \} \setminus S $ , by (ii) applied to $D = D _ { S }$ . Thus

$$
\begin{array} { l } { { \displaystyle { D _ { 2 } = k \cdot k ^ { \prime } \cdot \left( \sum _ { i \in S \cup S ^ { \prime } } e _ { i } + D _ { S \cup S ^ { \prime } } \right) } } } \\ { { \displaystyle ~ = k \cdot k ^ { \prime } \cdot F _ { S \cup S ^ { \prime } } } } \end{array}
$$

is a boundary component of $D$ .

$^ \dagger$ The question of uniqueness of the pair $\left( f _ { F } , \varphi _ { F } \right)$ is taken up in Theorem 3.7 below.

Part (v), when $F = F _ { S }$ , follows by taking $\varphi _ { F } = \varphi _ { S }$ , where

$$
\varphi _ { S } ( \mathrm { e } ^ { \mathrm { i } \theta } , x ) = \varphi \left( \mathrm { e } ^ { \mathrm { i } \theta } ; \dots , \underbrace { x } _ { \mathrm { i f } ~ i \in S } , \dots , \underbrace { \mathrm { e } ^ { \mathrm { i } \theta } } _ { \mathrm { i f } ~ i \notin S } , \dots \right) ,
$$

where $\varphi : U ^ { 1 } \times \mathrm { S L } ( 2 , \mathbb { R } ) ^ { r } \longrightarrow G$ is Harish-Chandra’s map (see Section 2.3), and taking $f _ { F } = f _ { S }$ to be the corresponding map of symmetric spaces. For general $F = k \cdot F _ { S }$ , let $\varphi _ { F } = k \varphi _ { S } k ^ { - 1 }$ and $f _ { F } = k f _ { S }$ . □

This theorem shows that the $F _ { S }$ are good models for studying any one boundary component. They are equally good for studying arbitrary flags of boundary components because of the next result.

# Proposition 3.4

(i) If $S _ { 1 } \subset S _ { 2 }$ , then $\overline { { F } } _ { S _ { 1 } } \supset \overline { { F } } _ { S _ { 2 } }$ . (ii) If

$$
\overline { { D } } \supset \overline { { F } } _ { 1 } \supset \overline { { F } } _ { 2 } \supset \cdots \supset \overline { { F } } _ { t }
$$

is any flag of boundary components, then there are subsets

$$
S _ { 1 } \subset S _ { 2 } \subset \cdots \subset S _ { t } \subset \{ 1 , \ldots , r \}
$$

and an element $k \in K$ such that

$$
k \cdot F _ { i } = F _ { S _ { i } } \ , \quad 1 \leq i \leq t .
$$

Proof If $S _ { 1 } \subset S _ { 2 }$ , then $L _ { S _ { 1 } } \supset L _ { S _ { 2 } }$ , hence ( $D _ { S _ { 1 } } \supset D _ { S _ { 2 } }$ and (

$$
\overline { { D } } \supset \left( \underbrace { \sum _ { i \in S _ { 1 } } e _ { i } + \overline { { D } } _ { S _ { 1 } } } _ { \overline { { F } } _ { S _ { 1 } } } \right) \supset \left( \underbrace { \sum _ { i \in S _ { 2 } } e _ { i } + \overline { { D } } _ { S _ { 2 } } } _ { \overline { { F } } _ { S _ { 2 } } } \right) ,
$$

since $\Sigma _ { i \in S _ { 2 } \backslash S _ { 1 } } e _ { i } \in \overline { { D } } _ { S _ { 1 } }$ . The second part is proved just as part (iv) above: first find $k _ { 1 } \in K$ such that $k _ { 1 } \cdot F _ { 1 } = F _ { S _ { 1 } }$ ; then find $k _ { 2 } \in K \cap L _ { S _ { 1 } }$ such that $k _ { 2 } k _ { 1 } \cdot F _ { 2 } =$ $F _ { S _ { 2 } }$ , and so on.

# 3.2

Our next purpose is to determine the normalizer $N ( F )$ of a boundary component $F$ :

$$
N ( F ) = \left\{ g \in G \vert g F = F \right\} ,
$$

and to show that the pair $\left( f _ { F } , \varphi _ { F } \right)$ in part (v) is unique. It is easiest to attack $N ( F _ { S } )$ first. As in the proof of the theorem, let

$$
\varphi _ { S } : U ^ { 1 } \times \mathrm { S L } ( 2 , \mathbb { R } ) \longrightarrow G
$$

be given by

$$
\varphi _ { S } ( \mathrm { e } ^ { \mathrm { i } \theta } , x ) = \varphi ( \mathrm { e } ^ { \mathrm { i } \theta } ; \dots , \underbrace { \mathrm { e } ^ { \mathrm { i } \theta } } _ { \mathrm { i f ~ } i \notin S } , \dots , \underbrace { x } _ { \mathrm { i f ~ } i \in S } , \dots ) \ ,
$$

where again $\varphi$ is Harish-Chandra’s map. Let $w _ { S } : \mathbb { G } _ { m } \longrightarrow \mathcal { G }$ be

$$
w _ { S } ( t ) = \varphi _ { S } \left( 1 , \left( \begin{array} { c c } { { t } } & { { 0 } } \\ { { 0 } } & { { t ^ { - 1 } } } \end{array} \right) \right) .
$$

Consider the associated parabolic subgroup

$$
P _ { S } = P ( w _ { S } ^ { - 1 } ) = \left\{ g \in G \vert \operatorname * { l i m } _ { t \longrightarrow 0 } w _ { S } ( t ) g w _ { S } ( t ) ^ { - 1 } \operatorname { e x i s t s } \right\} ,
$$

which is the intersection of $G$ with a real parabolic subgroup $\mathcal { P } _ { S } \subset \mathcal { G }$

It is easy to calculate Lie $P _ { S }$ using the real root decomposition:

$$
\mathrm { L i e } P _ { S } = Z ( { \mathfrak { a } } ) + \sum _ { \varphi \in { \mathbb R } ^ { \Psi } \atop \langle \mathrm { d } w _ { S } , \varphi \rangle \geq 0 } { \mathfrak { g } } ^ { \varphi } \ ,
$$

where $\langle \mathrm { d } w _ { S } , \varphi \rangle$ is the inner product of $\mathtt { d } w _ { S } ( 1 ) \in \mathfrak { a }$ and $\varphi \in \operatorname { H o m } \left( \mathfrak { a } , \mathbb { R } \right)$ . Since

$$
\langle \mathrm { d } w _ { S } , \gamma _ { i } \rangle = \left\{ \begin{array} { l l } { 1 } & { i \in S } \\ { 0 } & { i \notin S , } \end{array} \right.
$$

it follows that

$$
\begin{array} { r l } & { \left\{ \varphi \in _ { \mathbb R } \Psi \vert \langle { \mathrm d } w _ { S } , \varphi \rangle \geq 0 \right\} = \left\{ \frac { 1 } { 2 } ( \pm \gamma _ { i } \pm \gamma _ { j } ) , \pm \frac { 1 } { 2 } \gamma _ { i } , i , j \notin S \right\} } \\ & { \qquad \cup \left\{ \frac { 1 } { 2 } ( \gamma _ { i } \pm \gamma _ { j } ) , \frac { 1 } { 2 } \gamma _ { i } , i \in S , \mathrm { a n y ~ } j \right\} . } \end{array}
$$

Lemma 3.5 $P _ { S } \subset N ( F _ { S } )$ .

Proof We use the Cayley transformation

$$
c _ { S } = \varphi _ { S } \left( 1 , \frac { 1 } { 1 - \mathrm { i } } \left( \begin{array} { c c } { 1 } & { \mathrm { i } } \\ { 1 } & { - \mathrm { i } } \end{array} \right) \right) .
$$

Here $c _ { S } \in G _ { \mathbb { C } }$ , and one checks, via the equivariant map $\mathfrak { H } ^ { s } \times D _ { S } \xrightarrow { f _ { S } } D$ and its extension $( \mathbb { P } ^ { 1 } ) ^ { s } \times \check { D } s \xrightarrow { f _ { S } } \check { D }$ , that

$$
c _ { S } ( D _ { S } ) = F _ { S } \quad \mathrm { a n d } \quad c _ { S } ( \check { D } _ { S } ) = \check { F } _ { S } ,
$$

where we identify $D _ { S }$ with $L _ { S } \cdot o$ in $D$ .

Now, every $g \in P _ { S }$ either carries $F _ { S }$ to $F _ { S }$ or to a boundary component disjoint from $F _ { S }$ . Therefore it suffices to show that

$$
g \cdot c _ { S } ( o ) \in c _ { S } ( \check { D } _ { S } )
$$

for every $g \in P _ { S , \mathbb { C } }$ , because then, for $g \in P _ { S }$ , $g \cdot c _ { S } ( o ) \in \overline { { D } } \cap c _ { S } ( \check { D } _ { S } ) = c _ { S } ( \overline { { D } } _ { S } )$ , hence $g ( F _ { S } ) \subset { \overline { { F } } } _ { S }$ ; since $\dim g ( F _ { S } ) = \dim F _ { S }$ , it then follows that $g F _ { S } = F _ { S }$ .

Therefore we only need to show that

$$
c _ { S } ^ { - 1 } g c _ { S } ( o ) \in \check { D } _ { S } ,
$$

or

$$
c _ { S } ^ { - 1 } g c _ { S } \in L _ { S , \mathbb { C } } \cdot K _ { \mathbb { C } } \cdot P _ { - } \ .
$$

But define

$$
P _ { S , \mathbb { C } } ^ { \prime } = c _ { S } ^ { - 1 } P _ { S , \mathbb { C } } c _ { S } = \left\{ g \in G _ { \mathbb { C } } \ \vert \ \operatorname* { l i m } _ { t \longrightarrow 0 } w _ { S } ^ { \prime } ( t ) g w _ { S } ^ { \prime } ( t ) ^ { - 1 } \ \mathrm { e x i s t s } \right\} \ ,
$$

where

$$
w _ { S } ^ { \prime } = c _ { S } ^ { - 1 } w _ { S } c _ { S } : \mathbb { G } _ { m , \mathbb { C } } \longrightarrow G _ { \mathbb { C } } ~ .
$$

Then

$$
w _ { S } ^ { \prime } ( \mathrm { e } ^ { \mathrm { i } \theta } ) = \varphi _ { S } \left( 1 , \left( \begin{array} { c c } { { \cos \theta } } & { { - \sin \theta } } \\ { { \sin \theta } } & { { \cos \theta } } \end{array} \right) \right) ,
$$

and Lie $P _ { S , \mathbb { C } } ^ { \prime }$ is easy to calculate using the complex root decomposition:

$$
\begin{array} { r l } { \mathrm { L i e } P _ { S , \mathbb C } ^ { \prime } = \mathbf { t } _ { \mathbb C } \oplus } & { \displaystyle \sum _ { \varphi \in \Psi } \mathfrak { g } ^ { \varphi } } \\ { \langle \mathrm { d } w _ { S } ^ { \prime } , \varphi \rangle \geq 0 } \\ { = \mathbf { t } _ { \mathbb C } \oplus } & { \displaystyle \sum _ { \varphi \sim \frac { \pm \gamma _ { i } ^ { \prime } + \gamma _ { j } ^ { \prime } } { 2 } \mathrm { ~ o r ~ } \frac { \pm \gamma _ { i } ^ { \prime } } { 2 } } \oplus \quad \sum _ { \ell } \mathfrak { g } ^ { \varphi } \quad \oplus \quad \sum _ { \ell } \mathfrak { g } ^ { \varphi } \quad \oplus \displaystyle \sum _ { \varphi \sim 0 } \mathfrak { g } ^ { \varphi } . } \\ { \varphi { \sim } \frac { \pm \gamma _ { i } ^ { \prime } \pm \gamma _ { j } ^ { \prime } } { 2 } \mathrm { ~ o r ~ } \frac { \pm \gamma _ { i } ^ { \prime } } { 2 } \quad \varphi { \sim } \frac { - \gamma _ { i } ^ { \prime } - \gamma _ { j } ^ { \prime } } { 2 } \mathrm { ~ o r ~ } \frac { - \gamma _ { i } ^ { \prime } } { 2 } \quad \varphi { \sim } \frac { - \gamma _ { i } ^ { \prime } + \gamma _ { j } ^ { \prime } } { 2 } \quad } & { \varphi { \sim } \frac { - \gamma _ { i } ^ { \prime } } { 2 } } \\ { i , j \notin S } \end{array}
$$

Then $\mathbf { t } _ { \mathbb { C } } \subset \mathsf { \pmb { \mathsf { E } } } _ { \mathbb { C } }$ , the second term generates $\mathfrak { l } _ { S , \mathbb { C } }$ , the third term is in ${ \mathfrak { p } } _ { - }$ , and the fourth and fifth terms are in $\mathfrak { k } _ { \mathbb { C } }$ . Let $\mathfrak { b }$ be the subalgebra generated by the first, third, and fourth term, and let c be the subalgebra generated by the first four terms. Then $\mathfrak { b }$ and c are ideals, and $\mathfrak { b }$ generates a normal subgroup contained in $K _ { \mathbb { C } } \cdot P _ { - }$ . Therefore, c generates a normal subgroup contained in $L _ { S , \mathbb { C } } \cdot K _ { \mathbb { C } } \cdot P _ { - }$ , and, since the fifth term is contained in $\mathfrak { k } _ { \mathbb { C } }$ , we finally get $P _ { S , \mathbb { C } } ^ { \prime } \subset$ $\begin{array} { r } { L _ { S , \mathbb { C } } \cdot K _ { \mathbb { C } } \cdot P _ { - } \cdot K _ { \mathbb { C } } = L _ { S , \mathbb { C } } \cdot K _ { \mathbb { C } } \cdot P _ { - } } \end{array}$ , as required.

Proposition $3 . 6 \ : P _ { S } = N ( { F _ { S } } )$ .

Proof It suffices to show this when $G$ is simple because, in the general case, everything decomposes into a product. But when $G$ is simple, applying the Weyl group, we can assume that $S = \{ 1 , \ldots , b \}$ . Then note that all but one of the simple roots $\alpha _ { i }$ is zero on $\operatorname { I m } \mathrm { d } \omega _ { S }$ . Therefore the associated parabolic $\mathcal { P } _ { S }$ is a maximal real parabolic subgroup of $\mathcal { G }$ . Since

$$
P _ { S } \subset N ( F _ { S } ) \subsetneq G ,
$$

the connected components of $P _ { S }$ and $N ( F _ { S } )$ coincide. But then $N ( F _ { S } )$ normalizes $N ( F _ { S } ) ^ { o }$ , and hence normalizes Lie $N ( F _ { S } )$ , which equals the Lie algebra Lie $P _ { S }$ . But $P _ { S , \mathbb { C } }$ is the full normalizer of Lie $P _ { S }$ inside $G _ { \mathbb { C } }$ , so

$$
N ( F _ { S } ) \subset G \cap P _ { S , \mathbb { C } } = P _ { S } ,
$$

hence the asserted equality.

We now prove:

Theorem 3.7 For all boundary components $F \subset { \overline { { D } } }$ , the equivariant pair $\left( f _ { F } , \varphi _ { F } \right)$

$$
\begin{array} { r l } & { f _ { F } : \mathfrak { H } \longrightarrow D \ , } \\ & { \varphi _ { F } : U ^ { 1 } \times \mathrm { S L } ( 2 , \mathbb { R } ) \longrightarrow G \ , } \end{array}
$$

where $f _ { F }$ is symmetric with $f _ { F } ( i ) = o$ and $f _ { F } ( \infty ) \in F$ , is unique, and, if wF is defined by

$$
w _ { F } ( t ) = \varphi _ { F } \left( 1 , \left( \begin{array} { c c } { { t } } & { { 0 } } \\ { { 0 } } & { { t ^ { - 1 } } } \end{array} \right) \right) ,
$$

then

$$
N ( F ) = P ( w _ { F } ^ { - 1 } ) = \left\{ g \in G \ | \ \operatorname * { l i m } _ { t \longrightarrow 0 } w _ { F } ( t ) g w _ { F } ( t ) ^ { - 1 } \ \mathrm { e x i s t s } \right\} .
$$

Finally, if $N ( F _ { 1 } ) = N ( F _ { 2 } )$ , then $F _ { 1 } = F _ { 2 }$ .

Proof Because of Proposition 3.6, the middle part follows from the first part. Moreover, because of Theorem 3.3 (iii), to prove the rest we may assume $G$ simple. Now, by Proposition 2.6, all such $\varphi _ { F }$ arise as $k \varphi _ { S } k ^ { - 1 }$ , for some $k \in K$ . The first part therefore amounts to the following statement:

$$
k \cdot F _ { S _ { 1 } } = F _ { S _ { 2 } } \ , k \in K \Longrightarrow k \varphi _ { S _ { 1 } } k ^ { - 1 } = \varphi _ { S _ { 2 } } \ .
$$

But $k \cdot F _ { S _ { 1 } } = F _ { S _ { 2 } }$ implies r $\mathrm { a n k } ( F _ { S _ { 1 } } ) = \mathrm { r a n k } ( F _ { S _ { 2 } } )$ , hence $\left| S _ { 1 } \right| = \left| S _ { 2 } \right|$ . Therefore, by Proposition 2.8, there is an element $w$ of the Weyl group $\mathrm { N o r m } ( { \mathfrak { a } } ) / \mathrm { C e n t } ( { \mathfrak { a } } )$ inducing a permutation of the $x _ { i }$ such that $w S _ { 1 } = S _ { 2 }$ : we may realize $w$ as an element of $K \cap \operatorname { N o r m } \left( { \mathfrak { a } } \right)$ . This reduces us to proving

$$
k \in K \cap N ( F _ { S } ) \Longrightarrow k \varphi _ { S } = \varphi _ { S } k .
$$

Let $\sigma$ be the Cartan involution. Then

$$
\begin{array} { r l } & { k \in { \cal N } ( { \cal F } _ { { \cal S } } ) \Longrightarrow \underset { t \longrightarrow 0 } { \operatorname* { l i m } } w _ { { \cal S } } ( t ) k w _ { { \cal S } } ( t ) ^ { - 1 } \mathrm { ~ e x i s t s } } \\ & { ~ \Longrightarrow \underset { t \longrightarrow 0 } { \operatorname* { l i m } } \sigma ( w _ { { \cal S } } ( t ) ) \sigma ( k ) \sigma ( w _ { { \cal S } } ( t ) ) ^ { - 1 } \mathrm { ~ e x i s t s } } \\ & { ~ \Longrightarrow \underset { t \longrightarrow 0 } { \operatorname* { l i m } } w _ { { \cal S } } ( t ) ^ { - 1 } k w _ { { \cal S } } ( t ) \mathrm { ~ e x i s t s . } } \end{array}
$$

Thus $t \mapsto w _ { S } ( t ) k w _ { S } ( t ) ^ { - 1 }$ extends to a morphism $\mathbb { P } ^ { 1 } \longrightarrow \mathcal { G }$ . This must be constant, i.e., $k w _ { S } = w _ { S } k$ . But $k \in K$ implies $k h _ { o } = h _ { o } k$ . Thus

$$
\varphi _ { S } \left( 1 , { \left( \begin{array} { l l } { t } & { 0 } \\ { 0 } & { t ^ { - 1 } } \end{array} \right) } \right) \quad { \mathrm { a n d } } \quad \varphi _ { S } \left( \mathrm { e } ^ { \mathrm { i } \theta } , { \left( \begin{array} { l l } { \cos \theta } & { \sin \theta } \\ { - \sin \theta } & { \cos \theta } \end{array} \right) } \right)
$$

both centralize $k$ . Since these elements generate $U ^ { 1 } \times \mathrm { S L } ( 2 , \mathbb { R } )$ , we also get $k \varphi _ { S } = \varphi _ { S } k$ . As for the final assertion, when $G$ is simple, we saw in (the proof of) Proposition 3.6 that all the $N ( F )$ are maximal parabolic. Let $g \in G$ with $g F _ { 1 } = F _ { 2 }$ . Then $g N ( F _ { 1 } ) g ^ { - 1 } = N ( F _ { 2 } ) = N ( F _ { 1 } )$ , hence $g$ normalizes $N ( F _ { 1 } )$ so that $g \in N ( F _ { 1 } )$ , whence $F _ { 1 } = g F _ { 1 } = F _ { 2 }$ . □

Corollary 3.8 If $\overline { { F } } _ { 1 } \supset F _ { 2 }$ are two boundary components of $D$ , then there is $a$ unique symmetric holomorphic map

$$
f : { \mathfrak { H } } ^ { 2 } \longrightarrow D
$$

such that

$$
\begin{array} { c } { { f ( \mathrm { i } , \mathrm { i } ) = o ~ , } } \\ { { { } } } \\ { { f ( \mathrm { i } , \infty ) \in F _ { 1 } ~ , } } \\ { { { } } } \\ { { f ( \infty , \infty ) \in F _ { 2 } ~ . } } \end{array}
$$

In particular, $w _ { F _ { 1 } }$ and $w _ { F _ { 2 } }$ commute with each other.

Proof Combine Proposition 3.4 with Theorem 3.7.

Let $o _ { F } = f _ { F } ( \infty )$ : this is the natural basepoint of $F$ determined by the basepoint $o \in D$ .

Proposition 3.9 When $G$ is simple and hence $D$ is irreducible, the association $F \longmapsto N ( F )$ defines a bijection between the set of boundary components of $D$ and the set of maximal real parabolic subgroups of $G$ .

In general, if $G = G _ { 1 } \times \cdots \times G _ { k }$ , $D = D _ { 1 } \times \cdots \times D _ { k } ,$ , where $G _ { i } = \mathrm { A u t } ( D _ { i } ) ^ { o }$ , with $G _ { i }$ simple, then $F \longmapsto N ( F )$ defines a bijection between the set of boundary components $F = F _ { 1 } \times \cdots \times F _ { k }$ of $D$ , where here we allow $F _ { i } = D _ { i }$ , and the set of real parabolics $P = P _ { 1 } \times \cdots \times P _ { k }$ of $G _ { ; }$ , with $P _ { i }$ either maximal real parabolic in $G _ { i } ,$ , or $P _ { i } = G _ { i }$ .

Proof The general case reduces immediately to the case where $G$ is simple. Theorem 3.7 shows injectivity. Proposition 3.6 shows that $N ( F )$ is maximal. Moreover, by the proof of Proposition 3.6, the maximal real parabolic corresponding to any simple root do occur as $N ( F _ { S } )$ for suitable $s$ , hence we get surjectivity. □

# 3.3

Pursuing the same ideas, we can determine the centralizer $Z ( F )$ of a boundary component $F$ :

$$
Z ( F ) = \left\{ g \in G \mid g x = x { \mathrm { ~ f o r ~ a l l ~ } } x \in F \right\} ~ .
$$

The result is (for the connected component $Z ( F ) ^ { o } )$ :

Theorem 3.10 Let $F \subset { \overline { { D } } }$ be a boundary component and let $w _ { F } : \mathbb { G } _ { m } \longrightarrow \mathcal { G }$ be as in Theorem 3.7. Then

(1) $N ( F ) ^ { o }$ is a semi-direct product:

$$
N ( F ) ^ { o } = Z ( w _ { F } ) ^ { o } \ltimes W ( F ) \ ,
$$

where

$$
\begin{array} { l } { { { \cal W } ( { \cal F } ) = \{ g \in { \cal G } \ \vert \ \displaystyle \operatorname* { l i m } _ { t \longrightarrow 0 } w _ { \cal F } ( t ) g w _ { \cal F } ( t ) ^ { - 1 } = e \} } } \\ { { \displaystyle ~ = \mathrm { u n i p o t e n t ~ r a d i c a l ~ o f } \ N ( { \cal F } ) ^ { o } ~ , } } \\ { { { \cal Z } ( w _ { \cal F } ) ^ { o } = \mathrm { c o n n e c t e d ~ c o m p o n e n t ~ o f ~ c e n t r a l i z e r ~ c ~ } } } \\ { { \displaystyle ~ = \mathrm { a ~ L e v i ~ c o m p o n e n t ~ o f } \ N ( { \cal F } ) ^ { o } ~ . } } \end{array}
$$

(2) $Z ( w _ { \ / F } ) ^ { o }$ is generated by two commuting connected subgroups $G _ { h } ( F )$ and $\widetilde { G } _ { \ell } ( F )$ with finite intersection $A$ (so that $Z ( w _ { F } ) ^ { o } \cong ( G _ { h } \times \widetilde { G } _ { \ell } ) / A )$ and

$$
Z ( F ) ^ { o } = { \widetilde G } _ { \ell } ( F ) \ltimes W ( F ) ~ .
$$

(3) When $F = F _ { S }$ , then $G _ { h } ( F _ { S } ) = L _ { S }$ ; in general, $G _ { h }$ is semi-simple without compact factors and $G _ { h } /$ (center) is isomorphic to Aut $( F ) ^ { o }$ .

Proof The first part is a simple decomposition which applies to any parabolic subgroup $P ( w )$ for any one-parameter subgroup $w$ , and is proved by decomposing $\mathfrak { g }$ into $0 , +$ , and − eigenspaces under $\mathbf { A } \mathrm { d } w$ and exponentiating. To prove (2) and (3), we may assume $F = F _ { S }$ (getting the general case by conjugating by $k \in K$ ). In the notation above, note that

$$
\mathrm { L i e } Z ( w _ { S } ) = Z ( { \mathfrak { a } } ) + \sum _ { \varphi \in _ { \mathbb { R } } \Psi } { \mathfrak { g } } ^ { \varphi } ~ .
$$

Moreover, the $\varphi \in \mathbb { R } ^ { \Psi }$ with $\langle \mathrm { d } w _ { S } , \varphi \rangle = 0$ are of two types:

$$
\begin{array} { l } { { \varphi = \frac { 1 } { 2 } ( \pm \gamma _ { i } \pm \gamma _ { j } ) , \pm \frac { 1 } { 2 } \gamma _ { i } \ , \quad i , j \not \in S \ , } } \\ { { \varphi = \frac { 1 } { 2 } ( \gamma _ { i } - \gamma _ { j } ) \ , \quad i , j \in S \ . } } \end{array}
$$

Clearly, $\ l _ { S } \subset \operatorname { L i e } Z ( w _ { S } )$ . But also, since no roots of type (a) and of type (b) add up to a root, it follows that $\rho _ { S }$ is an ideal in Lie $Z ( w _ { S } )$ . This proves that we have a decomposition $Z ( w _ { S } ) ^ { o } \cong ( L _ { S } \times \widetilde { G } _ { \ell , S } ) / A$ as required. By Proposition 2.7, we know that

$$
Z ( { \mathfrak { a } } ) = { \mathfrak { a } } \oplus m ( { \mathfrak { a } } ) ~ ,
$$

where

$$
m ( { \mathfrak { a } } ) = { \mathrm { t y p e ~ ( e ) \mathrm { - } f a c t o r s ~ i n ~ t h e ~ d e c o m p o s i t i o n ~ o f ~ } } { \mathfrak { g } } = Z ( { \mathfrak { a } } ) \cap { \mathfrak { k } } \ .
$$

Note that if $\sigma$ is the Cartan involution of $\mathfrak { g }$ , then

$$
\sigma ( { \mathfrak { g } } ^ { \varphi } ) = { \mathfrak { g } } ^ { - \varphi } ;
$$

hence, as has already been noted earlier,

$$
\sigma ( \mathfrak { l } _ { S } ) = \mathfrak { l } _ { S } .
$$

Taking into account the fact that

$$
\mathrm { L i e } \widetilde { G } _ { \ell , S } = \{ x \in \mathrm { L i e } Z ( w _ { S } ) \mid [ x , \mathsf { l } _ { S } ] = 0 \} \ ,
$$

it follows that $\sigma ( \operatorname { L i e } \widetilde { G } _ { \ell , S } ) = \operatorname { L i e } \widetilde { G } _ { \ell , S }$ . Since Lie $\widetilde { G } _ { \ell , S }$ is normalized by $\mathfrak { a }$ , we deduce the following explicit expression:

$$
\mathrm { L i e } \widetilde { G } _ { \ell , S } = \sum _ { \varphi = \frac { \gamma _ { i } - \gamma _ { j } } { 2 } } \mathfrak { g } ^ { \varphi } + \sum _ { i \in S } \mathbb { R } x _ { i } + ( \mathrm { i d e a l ~ i n } m ( \mathfrak { a } ) ) \ .
$$

(The middle factor comes from the fact that-

$$
\sum _ { i \in S } \mathbb { R } x _ { i } = \{ x \in \mathfrak { a } \mid \gamma _ { i } ( x ) = 0 , \quad i \notin S \} = \{ x \in \mathfrak { a } \mid [ x , \mathfrak { l } _ { S } ] = ( 0 ) \} . \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ }
$$

Next, we check that $\widetilde { G } _ { \ell } ( F _ { S } )$ acts identically on $F _ { S }$ . Since it commutes with $L _ { S }$ , which acts transitively on $F _ { S }$ , it suffices to check that

$$
g c _ { S } ( o ) = c _ { S } ( o ) \mathrm { f o r a l l } g \in \widetilde { \cal G } _ { \ell , S } ,
$$

or that

$$
c _ { S } ^ { - 1 } g c _ { S } ( o ) = o \mathrm { f o r \ a l l \ g } \in \widetilde { G } _ { \ell , S } ,
$$

or that

$$
\mathsf { A d } c _ { S } ( \mathrm { L i e } \widetilde { G } _ { \ell , S } ) \subset \mathfrak { t } _ { \mathbb { C } } + \mathfrak { p } _ { - } \ .
$$

But

$$
\begin{array} { l } { \displaystyle \mathrm { A d } c _ { S } ( \mathfrak { g } ^ { \varphi } ) = \displaystyle \sum _ { \varphi ^ { \prime } \sim \frac { \gamma _ { i } ^ { \prime } - \gamma _ { j } ^ { \prime } } { 2 } } \mathfrak { g } ^ { \varphi ^ { \prime } } \quad \mathrm { i f } \varphi = \frac { 1 } { 2 } ( \gamma _ { i } - \gamma _ { j } ) , \quad i , j \in S , } \\ { \displaystyle \mathrm { A d } c _ { S } ( x _ { i } ) = h _ { i } \quad \mathrm { i f } i \in S , } \end{array}
$$

and hence

$$
\mathop { \mathrm { A d } c _ { S } } ( \mathop { \mathrm { L i e } } \widetilde { G } _ { \ell , S } ) \subset \ \sum _ { \varphi ^ { \prime } \sim \frac { \gamma _ { i } ^ { \prime } - \gamma _ { j } ^ { \prime } } { 2 } } \mathfrak { g } ^ { \varphi ^ { \prime } } + \mathfrak { t } _ { \mathbb { C } } + m ( \mathfrak { a } ) \ .
$$

All these factors are in $\mathfrak { k } _ { \mathbb { C } }$ , so $\widetilde { G } _ { \ell , S }$ centralizes $F _ { S }$

Next, we check that $W ( F _ { S } )$ centralizes $F _ { S }$ . Again, since $W ( F _ { S } )$ is normalized by $L _ { S }$ , it suffices to show that

$$
g c _ { S } ( o ) = c _ { S } ( o ) ~ , ~ \mathrm { f o r \ a l l } ~ g \in W ( F _ { S } ) ~ ,
$$

or that

$$
\pounds \mathrm { d } c _ { S } ( \mathrm { L i e } W ( F _ { S } ) ) \subset \mathfrak { k } _ { \mathbb { C } } + \mathfrak { p } _ { - } \ .
$$

But

$$
\mathrm { A d } c _ { S } ( \mathrm { L i e } W ( F _ { S } ) ) = \sum _ { \varphi \in \Psi \atop { \langle \mathrm { d } w _ { S } ^ { \prime } , \varphi \rangle < 0 } } \mathfrak { g } ^ { \varphi } .
$$

These roots are:

(i) $\begin{array} { r } { \varphi \sim - \frac { 1 } { 2 } ( \gamma _ { i } ^ { \prime } + \gamma _ { j } ^ { \prime } ) } \end{array}$ or − 12 (γi ), i ∈ S, any - $j$ ; (ii) $\begin{array} { r } { \varphi \sim - \frac { 1 } { 2 } ( \gamma _ { i } ^ { \prime } - \gamma _ { j } ^ { \prime } ) } \end{array}$ , i ∈ S, j ∈/ S ,

which are all compact, or negative non-compact. This proves that

$$
{ \widetilde G } _ { \ell , S } \ltimes W ( F _ { S } ) \subset Z ( F _ { S } ) ^ { o } ~ .
$$

Since $L _ { S } /$ (center) acts faithfully on $F _ { S }$ , we must have equality here, and this finishes the proof.

The above proof gives us another useful piece of information: for all $F$ , let

$$
\begin{array} { c c c c c } { { \ 5 } } & { { \stackrel { } { \longrightarrow } } } & { { { \cal D } } } & { { } } & { { } } \\ { { \bigcap } } & { { } } & { { } } & { { \bigcap } } \\ { { \mathbb { P } ^ { 1 } } } & { { \stackrel { } { \longrightarrow } } } & { { f _ { F } } } & { { \stackrel { } { \longrightarrow } } } & { { \check { D } } } \end{array}
$$

be as in Theorem 3.3; in particular,

$$
\begin{array} { c } { { f _ { F } ( \mathrm { i } ) = o , } } \\ { { { } } } \\ { { f _ { F } ( \infty ) = o _ { F } . } } \end{array}
$$

Define now (recall that $s _ { o }$ denotes the symmetry of $D$ at $o$ ):

$o _ { F } ^ { 0 } = f _ { F } ( 0 ) = s _ { o } ( o _ { F } ) ,$ F0 = so(F) = boundary component containing $o _ { F } ^ { 0 }$ .

![](images/d130ab09f1cec60bdde5a886ba677f15cd4dac5e61d66bbe1dffd619443cc0a2.jpg)

If $F = F _ { S }$ , then

$$
o _ { F _ { S } } ^ { 0 } \neq c _ { S } ^ { - 1 } ( o ) .
$$

In general, since ${ \left( \begin{array} { l l } { 1 } & { - \mathrm { i } } \\ { 0 } & { 1 } \end{array} \right) } \in \mathrm { S L } ( 2 , \mathbb { C } )$ carries i to 0,

$$
o _ { F } ^ { 0 } = \varphi _ { F } \left( 1 , \left( \begin{array} { l l } { { 1 } } & { { - \mathrm { i } } } \\ { { 0 } } & { { 1 } } \end{array} \right) \right) \cdot o \ .
$$

Proposition 3.11 $\widetilde { G } _ { \ell } ( F )$ fixes $o _ { F } ^ { 0 }$

Proof Note that the symmetry $s _ { o }$ interchanges $o _ { F } ^ { 0 }$ and the basepoint $o _ { F } \in F$ , hence, for $g \in \widetilde { G } _ { \ell } ( F )$ , -

$$
g o _ { F } ^ { 0 } = g s _ { o } ( o _ { F } ) = s _ { o } ( \sigma ( g ) ( o _ { F } ) ) = s _ { o } ( o _ { F } ) = o _ { F } ^ { 0 } ,
$$

because $\sigma$ preserves ${ \widetilde { G } } _ { \ell } \subset N ( F )$

# 3.4

The next topic we want to discuss is the natural projection of $D$ onto one of its boundary components $F$ :

$$
\pi _ { F } : D \longrightarrow F \ .
$$

We begin by considering an analog of the linear projection $\pi : C \longrightarrow C _ { 1 }$ of a cone onto one of its boundary components, discussed in Chapter II, Section 3. Please bear with us though – this will not immediately define $\pi _ { F }$ , as it is the “wrong projection.”

Fix a basepoint $o \in D$ and let $w _ { F } : \mathbb { G } _ { m } \longrightarrow \mathcal { G }$ be the homomorphism associated to $F$ and $o$ , i.e., the equivariant pair

$$
\begin{array} { r l } & { f : \mathfrak { H } \longrightarrow D , } \\ & { \varphi : U ^ { 1 } \times \mathrm { S L } ( 2 , \mathbb { R } ) \longrightarrow G , } \end{array}
$$

with $f ( \mathrm { i } ) = o , f ( \infty ) \in F$ , and let $w _ { F } ( t ) = \varphi \left( 1 , \left( \begin{array} { c c } { t } & { 0 } \\ { 0 } & { t ^ { - 1 } } \end{array} \right) \right) .$ . Then $\mathbb { G } _ { m }$ acts via $w _ { F }$ algebraically on the projective variety $\check { D }$ ; hence, for all $x \in \check { D }$ , we may define:

$$
p _ { F } ( x ) = \varinjlim _ { t \longrightarrow 0 } w _ { F } ( t ) \cdot x .
$$

For instance, $p _ { F } ( o ) = o _ { F } ^ { 0 }$ . Now, for all $g \in N ( F ) _ { \mathbb { C } } = P ( w _ { F } ^ { - 1 } ) _ { \mathbb { C } }$ , we calculate:

$$
\begin{array} { l } { { p _ { F } ( g o ) = \displaystyle \operatorname* { l i m } _ { t \longrightarrow 0 } w _ { F } ( t ) \cdot g \cdot o } } \\ { { \qquad = \displaystyle \operatorname* { l i m } _ { t \longrightarrow 0 } ( w _ { F } ( t ) g w _ { F } ( t ) ^ { - 1 } ) ( w _ { F } ( t ) \cdot o ) } } \\ { { \qquad = \overline { { { g } } } ( o _ { F } ^ { 0 } ) , } } \end{array}
$$

where $\overline { { g } } = \operatorname* { l i m } _ { t \longrightarrow 0 } w _ { F } ( t ) g w _ { F } ( t ) ^ { - 1 }$ , which exists by assumption. Moreover, note that

$$
\begin{array} { r } { N ( F ) _ { \mathbb { C } } = Z ( w _ { F } ) _ { \mathbb { C } } \cdot W ( F ) _ { \mathbb { C } } \ , } \\ { N ( F ^ { 0 } ) _ { \mathbb { C } } = Z ( w _ { F } ) _ { \mathbb { C } } \cdot W ( F ^ { 0 } ) _ { \mathbb { C } } \ , } \end{array}
$$

and that $\overline { { g } }$ is just the projection of $g$ into its $Z ( w _ { F } ) _ { \mathbb { C } }$ -component. Therefore $\overline { { g } } \in N ( F ^ { 0 } ) _ { \mathbb { C } }$ , hence ${ \overline { { g } } } \cdot o _ { F } ^ { 0 } \in F ^ { 0 }$ . Now define the open subset $D ( { \check { F } } ) \subset { \check { D } }$ by

$$
D ( { \check { F } } ) = \bigcup _ { g \in N ( F ) _ { \mathbb { C } } } g \cdot D = N ( F ) _ { \mathbb { C } } \cdot o
$$

(the last equality occurs because $N ( F )$ acts transitively on $D$ ). By the first description, $D ( { \check { F } } )$ is open; by the second, it is the orbit of an algebraic group acting on a projective variety $\check { D }$ , and hence it is a Zariski-open subset of a subvariety. Therefore $D ( { \check { F } } )$ is a Zariski-open subset of $\check { D }$ . Now formula (3.1) shows that

(a) $p _ { F } ( D ( \check { F } ) ) \subset \check { F } ^ { 0 }$ and $p _ { F } ( D ) \subset F ^ { 0 }$ , (b) $p _ { F } : D ( \check { F } ) \longrightarrow \check { F } ^ { 0 }$ is equivariant for $N ( F ) _ { \mathbb { C } }$ (not $N ( F ^ { 0 } ) _ { \mathbb { C } } ! )$ , where $N ( F ) _ { \mathbb { C } }$ acts on ${ \check { F } } ^ { 0 }$ by

$$
N ( F ) _ { \mathbb { C } } \longrightarrow Z ( w _ { F } ) _ { \mathbb { C } } \longrightarrow N ( F ^ { 0 } ) _ { \mathbb { C } } \longrightarrow \mathrm { A u t } ( D _ { F } ) _ { \mathbb { C } } \ ;
$$

hence $p _ { F }$ is continuous on $\mathsf { D } ( \check { F } )$ .

But now a map defined like $p _ { F }$ is automatically a morphism of varieties whenever it is continuous. In fact, embed ${ \check { D } } \subset \mathbb { P } _ { \mathbb { C } } ^ { n }$ such that $\check { D } \notin$ hyperplane, and such that $w _ { F }$ acts on $\mathbb { P } ^ { n }$ too, via $\left( x _ { 0 } , \ldots , x _ { n } \right) \longmapsto \left( t ^ { t _ { 0 } } x _ { 0 } , \ldots , t ^ { r _ { n } } x _ { n } \right)$ , where $r _ { 0 } \geq \cdots \geq r _ { n }$ . Let $r _ { m - 1 } > r _ { m } = r _ { n }$ . Let $L _ { 1 }$ , resp. $L _ { 2 }$ , be the linear spaces $x _ { 0 } = \cdot \cdot \cdot = x _ { m - 1 } = 0$ , resp. $x _ { m } = \cdots = x _ { n } = 0$ . Then $p _ { F }$ on $\mathbb { P } ^ { n } \backslash L _ { 2 }$ is the linear projection with center $L _ { 2 }$ and image $L _ { 1 }$ . Moreover, $L _ { 1 } \cap L _ { 2 } = \emptyset$ and $p _ { F } ( L _ { 2 } ) \subset$ $L _ { 2 }$ . Thus, if $p _ { F }$ is continuous in the classical topology on any connected $S \subset \mathbb { P } ^ { n }$ , then either $S \subset L _ { 2 }$ or $S \subset \mathbb { P } ^ { n } \backslash L _ { 2 }$ . It follows that $D ( { \check { F } } ) \subset \mathbb { P } ^ { n } \setminus L _ { 2 }$ .

Now, to define $\pi _ { F } : D ( \check { F } ) \longrightarrow \check { F }$ , we proceed as follows. Take the symmetries

$$
\begin{array} { r } { s _ { o } : \check { D } \longrightarrow \check { D } , } \\ { s _ { o _ { F } } : \check { F } \longrightarrow \check { F } . } \end{array}
$$

Define

$$
\pi _ { F } ( x ) = s _ { o _ { F } } ( s _ { o } ( p _ { F } ( x ) ) )
$$

(since $s _ { o } ( F ^ { 0 } ) = F$ , this makes sense). Then, for all $g \in N ( F ) _ { \mathbb { C } }$ , if $\overline { { g } }$ is its projection into $Z ( w _ { F } ) _ { \mathbb { C } }$ and $\overline { { \overline { { g } } } }$ is its projection into $\operatorname { A u t } ( D _ { F } ) _ { \mathbb { C } }$ , then

$$
\begin{array} { r l } & { \pi _ { F } ( g x ) = s _ { o _ { F } } ( s _ { o } ( p _ { F } ( g x ) ) ) } \\ & { \quad \quad \quad = s _ { o _ { F } } ( s _ { o } ( \overline { { g } } ( p _ { F } x ) ) ) } \\ & { \quad \quad \quad = s _ { o _ { F } } ( \sigma ( \overline { { g } } ) ( s _ { o } ( p _ { F } x ) ) ) } \\ & { \quad \quad \quad = s _ { o _ { F } } ( \sigma _ { F } ( \overline { { g } } ) ( s _ { o } ( p _ { F } x ) ) ) } \\ & { \quad \quad \quad = \overline { { g } } ( s _ { o _ { F } } ( s _ { o } ( p _ { F } x ) ) ) } \\ & { \quad \quad \quad = \overline { { g } } \pi _ { F } ( x ) . } \end{array}
$$

Here $\sigma : G _ { \mathbb { C } } \longrightarrow G _ { \mathbb { C } }$ denotes the Cartan involution relative to the basepoint $o$ , and $\sigma _ { F } : \mathrm { A u t } ( D _ { F } ) _ { \mathbb { C } } \longrightarrow \mathrm { A u t } ( D _ { F } ) _ { \mathbb { C } }$ denotes the Cartan involution relative to the basepoint $o _ { F }$ . Therefore

(a ) $\pi _ { F } ( D ( \check { F } ) ) \subset \check { F }$ and $\pi _ { F } ( D ) \subset F$ ;   
$( \mathsf { b } ^ { \prime } )$ $\pi _ { F }$ is equivariant for $N ( F ) _ { \mathbb { C } }$ acting on $D ( { \check { F } } )$ and on $\check { F }$ in the natural way, i.e., restricting the action of $G _ { \mathbb { C } }$ on $\check { D }$ ;   
$( \mathrm { c ^ { \prime } } )$ $\pi _ { F }$ is a morphism of varieties.

As a corollary of $( \mathsf { b } ^ { \prime } )$ , we deduce the following intrinsic definition of $\pi _ { F }$ independent of the choice of basepoint:

$( \mathrm { d ^ { \prime } } )$ ) $\pi _ { F } ( x ) =$ the point of $\check { F }$ with stabilizer equal to the image in Au $\operatorname { t } ( D _ { F } ) _ { \mathbb { C } }$ of $N ( F ) _ { \mathbb { C } } \cap ( { \mathrm { S t a b . ~ o f ~ } } x ) .$

Sometimes $\pi _ { F }$ on $D$ is called the geodesic projection of $D$ onto $F$ . The reason for this is as follows: for all $x \in D$ , let $f _ { F , x }$ be the unique symmetric holomorphic map defined by

$$
\begin{array} { r l } & { f _ { F , x } : \mathfrak { H } \longrightarrow D \ , } \\ & { \qquad \mathrm { i } \longmapsto x \ , } \\ & { \qquad \infty \longmapsto \mathrm { p t . ~ o f ~ } F \ . } \end{array}
$$

Then $f _ { F , x } ( \mathrm { i } \mathbb { R } )$ is a geodesic in $D$ through $x$ and one checks easily – check it first for $x = o$ , then use $( { \bf { b } } ^ { \prime } ) -$ that

$$
\pi _ { F } ( x ) = f _ { F , x } ( \infty ) = \operatorname* { l i m } _ { t \longrightarrow \infty } f _ { F , x } ( \mathrm { i } t ) .
$$

Note that if, at the beginning of Subsection 3.4, we had interchanged the roles of $F$ and $F ^ { 0 }$ and defined $p _ { F ^ { 0 } } : D \longrightarrow F$ by

$$
p _ { F ^ { 0 } } ( x ) = \operatorname* { l i m } _ { t \longrightarrow \infty } w _ { F } ( t ) \cdot x \ ,
$$

this would look similar to (3.2). However, $w _ { F } ( \mathbb { R } ) \cdot x$ is not a geodesic in general, and $p _ { F ^ { 0 } }$ is definitely not $N ( F )$ -equivariant! Incidentally, an alternative to our round-about approach via $p _ { F }$ would be to define - $\pi _ { F }$ directly using $( \mathsf { b } ^ { \prime } )$ ; this would require a careful root analysis via Proposition 2.7 to establish the key lemma:

$$
N ( F ) _ { \mathbb { C } } \cap ( K _ { \mathbb { C } } \cdot P _ { - } ) \subset K _ { h , \mathbb { C } } \cdot P _ { h , - } \cdot \widetilde { G } _ { \ell , \mathbb { C } } \cdot W _ { \mathbb { C } } \ ,
$$

where $K _ { h } , P _ { h }$ are the subgroups of $G _ { h }$ analogous to $K$ and $P$ in $G$ .

# 3.5

The final topic we want to discuss is that of rational boundary components. As in Subsection 2.5, say $D = \mathcal { G } ( \mathbb { R } ) ^ { o } / K$ , where $\mathcal { G }$ is an algebraic group defined over $\mathbb { Q }$ .

Definition 3.12 A boundary component $F$ of $D$ is rational if its normalizer $N ( F )$ is defined over $\mathbb { Q }$ (i.e., $N ( F ) = \mathcal { N } ( F ) ( \mathbb { R } ) \cap \mathcal { G } ( \mathbb { R } ) ^ { o }$ for some algebraic subgroup ${ \mathcal { N } } ( F )$ defined over $\mathbb { Q }$ ).

To understand the effect of this definition, let $\mathcal { A } \subset \mathcal { G }$ be a maximal $\mathbb { Q }$ - split torus, and let $\mathcal { B } \subset \mathcal { G }$ be a maximal $\mathbb { R }$ -split torus with ${ \mathcal { A } } \subset { \mathcal { B } }$ . As in Subsection 2.5, let $\gamma _ { i }$ , $1 \leq i \leq r$ , be the strongly orthogonal real roots and let $\{ 1 , \ldots , r \} = I _ { 0 } \cup \cdot \cdot \cdot \cup I _ { s }$ be the partition so that $\mathcal { A }$ is defined by $\gamma _ { i } = 1$ for $i \in I _ { 0 }$ and $\gamma _ { i } = \gamma _ { j }$ for $i , j \in I _ { k }$ , $k = 1 , \hdots , s$ . For $i \geq 1$ , let $\beta _ { i }$ be the restriction to $\mathcal { A }$ of $\gamma _ { j }$ $j \in I _ { i }$ . For all $S \subset \{ 1 , \ldots , r \}$ , let $F _ { S }$ be the associated boundary component. Then we may state:

Lemma 3.13 The boundary component $F _ { S }$ is rational if and only if $S = I _ { i _ { 1 } } \cup$ $\cdots \cup I _ { i _ { t } }$ , where $1 \leq i _ { 1 } , \ldots , i _ { t } \leq s$ .

Proof If $s$ has the above property, then $w _ { S } ( \mathbb { G } _ { m } )$ is a one-parameter subgroup of $\mathcal { A }$ . Since $\mathcal { A }$ is split, $w _ { S }$ is defined over $\mathbb { Q }$ , and hence so is $P _ { S }$ . By Proposition 3.6, this means $F _ { S }$ is rational. Note that if $\mathcal { G }$ is $\mathbb { Q }$ -simple, then this construction gives all maximal $\mathbb { Q }$ -rational parabolics containing $\mathcal { A }$ . To prove the converse, we may assume that $\mathcal { G }$ is $\mathbb { Q }$ -simple since $\mathcal { A }$ and $\mathcal { N } ( F _ { S } )$ are products of their intersections with the $\mathbb { Q }$ -simple factors. Then $\mathcal { N } ( F _ { S } )$ is a maximal $\mathbb { Q }$ -rational parabolic (see (2) in the following list), and hence $s$ is of the desired form.

In general, rational boundary components behave just like ordinary boundary components. Thus one proves easily the following.

(1) If we decompose $\mathcal { G }$ into its $\mathbb { Q }$ -simple factors as $\mathcal { G } = \mathcal { G } _ { 1 } \times \cdots \times \mathcal { G } _ { k }$ , and let $D = D _ { 1 } \times \cdots \times D _ { k }$ be the corresponding decomposition, then a boundary component $F = F _ { 1 } \times \cdots \times F _ { k }$ is rational if and only if the $F _ { i }$ are rational.

(2) If $\mathcal { G }$ is $\mathbb { Q }$ -simple, then the association $F \longmapsto N ( F )$ defines a bijection between the set of rational boundary components and the set of maximal $\mathbb { Q }$ - parabolics of $\mathcal { G }$ . If $\mathcal { G } = \mathcal { G } _ { 1 } \times \cdots \times \mathcal { G } _ { t }$ over $\mathbb { R }$ , then each rational $F$ decomposes as $F = F _ { 1 } \times \cdots \times F _ { t }$ , with $\overline { { F } } _ { i } \subsetneq \overline { { D } } _ { i }$ ; hence every maximal $\mathbb { Q }$ -parabolic $\mathcal { P }$ decomposes as $\mathcal { P } = \mathcal { P } _ { 1 } \times \cdots \times \mathcal { P } _ { t }$ , with $\mathcal { P } _ { i } \subset \mathcal { G } _ { i }$ a maximal $\mathbb { R }$ -parabolic.

(3) Every rational boundary component equals $g F _ { S }$ for some $g \in \mathcal { G } ( \mathbb { Q } )$ and some $s$ (for which $F _ { S }$ is rational).

(4) If $s = \mathbb { Q }$ -rank $\mathcal { G }$ , there is a symmetric holomorphic map

$$
\begin{array} { r c l l } { { \mathfrak { H } } ^ { s } } & { { \xrightarrow { } } } & { { f _ { 1 } } } & { { } } & { { D } } \\ { { \bigcap } } & { { } } & { { } } & { { \bigcap } } \\ { { ( \mathbb { P } ^ { 1 } ) ^ { s } } } & { { \xrightarrow { } } } & { { f _ { 2 } } } & { { \breve { D } } } \end{array}
$$

associated to

$$
\varphi : U ^ { 1 } \times \mathrm { S L } ( 2 , \mathbb { R } ) ^ { s } \longrightarrow G
$$

such that $\varphi ( 1$ , diagonal matrices) is a maximal $\mathbb { Q }$ -split torus and the rational boundary components are the $\mathcal { G } ( \mathbb { Q } )$ -transforms of the boundary components $F _ { S }$ containing

$$
f _ { 2 } ( \ldots , \underbrace { \mathrm { i } } _ { i \not \in S } , \ldots , \underbrace { \infty } _ { i \in S } , \ldots ) .
$$

(5) Jumping ahead and using the results of Section 4, we may ask, for $F$ a rational boundary component, which of the factors of ${ \mathcal { N } } ( F )$ is $\mathbb { Q }$ -rational. We will have (see Section 4) that the algebraic connected component of ${ \mathcal { N } } ( F )$ equals

$$
\begin{array} { r } { [ \mathcal { G } _ { h } ( F ) \cdot \mathcal { G } _ { \ell } ( F ) \cdot \mathcal { M } ( F ) ] \cdot \mathcal { V } ( F ) \cdot \mathcal { U } ( F ) . } \end{array}
$$

Then

(a) $w _ { F }$ is in a maximal $\mathbb { Q }$ -split torus so it is rational; hence $\mathscr { G } _ { h } \cdot \mathscr { G } _ { \ell } \cdot \mathscr { M }$ , and $\boldsymbol { \mathcal U }$ and $\mathcal { V }$ , as 0, 1, 2-eigenspaces for $\mathbf { A d } w _ { F }$ , are $\mathbb { Q }$ -rational;   
(b) $\mathcal { G } _ { h } \cdot \mathcal { M }$ as the centralizer of $\boldsymbol { \mathcal U }$ in $\mathscr { G } _ { h } \cdot \mathscr { G } _ { \ell } \cdot \mathscr { M }$ is $\mathbb { Q }$ -rational; hence $\mathcal { G } _ { \ell }$ as the normal complement to $\mathcal { G } _ { h } \cdot \mathcal { M }$ in $\mathscr { G } _ { h } \cdot \mathscr { G } _ { l } \cdot \mathscr { M }$ is $\mathbb { Q }$ -rational.

(6) Because of (5), we may speak of rational boundary components of rational boundary components and we claim: given boundary components $F _ { 1 } < F _ { 2 }$ , with $F _ { 2 }$ rational, then $F _ { 1 }$ is rational as a boundary component of $F _ { 2 }$ if and only if it is rational as a boundary component of $D$ . In fact, our assumptions say that $N ( F _ { 1 } ) \cap N ( F _ { 2 } )$ is a real parabolic, with $N ( F _ { 2 } )$ defined over $\mathbb { Q }$ . We may assume $\mathcal { G }$ is $\mathbb { Q }$ -simple. By the uniqueness of the expression of parabolics as an intersection of maximal parabolics, $N ( F _ { 1 } ) \cap N ( F _ { 2 } )$ is defined over $\mathbb { Q }$ if and only if $N ( F _ { 1 } )$ is defined over $\mathbb { Q }$ .

Note that if $G = \operatorname { A u t } ( D ) ^ { o }$ , then we may have $\mathscr { G } ( \mathbb { R } ) ^ { o } = G \cdot M _ { 0 }$ , with $M _ { 0 }$ compact and acting trivially on $D$ . From the point of view of algebraic groups over $\mathbb { Q }$ , $M _ { 0 }$ may be conjugate to simple factors of $G$ , and hence not defined over $\mathbb { Q }$ and impossible to throw out. Then $M _ { 0 }$ appears as an “extra” factor in each $\mathcal { N } ( F ) ( \mathbb { R } )$ and combines with the $M ( F )$ to be introduced in Section 4. In particular, $\mathcal { G } _ { h } ( F ) \cdot \mathcal { M } ( F )$ is a semi-simple algebraic group over $\mathbb { Q }$ such that $F = [ \mathcal { G } _ { h } ( F ) \cdot \mathcal { M } ( F ) ] ( \mathbb { R } ) ^ { o } / ( \mathrm { m a x . \ c o m p a c t } )$ , i.e., we recover for $F$ the presentation we have for $D$ .

# 4 Siegel domains of the third kind

# 4.1

Let $D$ be a bounded symmetric domain, and let $F$ be a boundary component. The purpose of this section is to work out in considerable detail the structure of the group $N ( F )$ and from this to realize $D$ as a particular open subset of a rather simple ambient space $D ( F )$ : this is an abstract version of Piatetskii-Shapiro’s models of $D$ as “Siegel domains of third kind.” We will briefly indicate at the end how to make the link with the more concrete Siegel domains.

First we study $N ( F )$ more closely. As in Section 3, it is easiest to write things out explicitly for $N ( F _ { S } )$ , and then to observe that the same things happen for every $F$ by conjugating. In this way, we now want to introduce the fundamental 5-factor decomposition of $N ( F )$ .

Special case $F = F _ { S }$ We have seen that

$$
\mathfrak { n } ( F _ { S } ) : = \mathrm { L i e } N ( F _ { S } ) = Z ( \mathfrak { a } ) \oplus \sum _ { \varphi = \frac { \pm \gamma _ { i } + \gamma _ { j } } { 2 } \ \textnormal { o r } \frac { \pm \gamma _ { i } } { 2 } } \mathfrak { g } ^ { \varphi } \oplus \sum _ { \varphi = \frac { \gamma _ { i } + \gamma _ { j } } { 2 } \ \textnormal { o r } \frac { \gamma _ { i } } { 2 } } \mathfrak { g } ^ { \varphi } .
$$

Under the homomorphism $w _ { S } : \mathbb { G } _ { m } \longrightarrow N ( F _ { S } )$ , we may decompose Lie ${ } : N ( F _ { S } )$ into the direct sum of three eigenspaces, where $\operatorname { A d } \left( w _ { S } ( t ) \right)$ is multiplication by $1 , t , t ^ { 2 }$ , respectively:

$$
\begin{array} { r l } & { \mathfrak { n } ( F _ { S } ) _ { 0 } = Z ( \mathfrak { a } ) \oplus \displaystyle \sum _ { \vartheta = \frac { \pm \gamma \hat { n } + \gamma _ { j } } { 2 } \quad \mathrm { o r } \quad \frac { 9 } { 2 } } \oplus \displaystyle \bigoplus _ { \vartheta = \frac { \gamma \hat { n } - \gamma _ { j } } { 2 } } \mathfrak { g } ^ { \varphi } \mathbin { \overbrace { \mathfrak { p } \varphi - \frac { \gamma } { 2 } \gamma _ { j } } } ^ { \sharp } \mathfrak { g } ^ { \varphi } ; } \\ & { \mathfrak { n } ( F _ { S } ) _ { 1 } = \displaystyle \sum _ { \vartheta = \frac { \gamma \hat { n } + \gamma _ { j } } { 2 } \quad \mathrm { o r } \quad \frac { \gamma \mathfrak { g } } { 2 } \colon \quad \mathrm { c a l l ~ t h i s ~ } \mathfrak { v } ( F _ { S } ) } ; } \\ & { \mathfrak { n } ( F _ { S } ) _ { 2 } = \displaystyle \sum _ { \vartheta = \frac { \gamma \hat { n } + \gamma _ { j } } { 2 } \mathfrak { h } ^ { \varphi } } \mathfrak { g } ^ { \varphi } ; \quad \mathrm { c a l l ~ t h i s ~ } \mathfrak { u } ( F _ { S } ) . } \end{array}
$$

These are the root spaces ${ \mathfrak { g } } ^ { \varphi }$ , where $\langle d w _ { S } , \varphi \rangle = 0 ,$ , 1, or 2, respectively. Then ${ \mathfrak { u } } + { \mathfrak { v } }$ is the maximal nilpotent ideal, so, defining as in Theorem 3.10

$$
W ( F _ { S } ) = \mathrm { u n i p o t e n t r a d i c a l o f } { \cal N } ( F _ { S } ) ,
$$

we have

$$
\mathsf { u } ( F _ { S } ) + \mathsf { v } ( F _ { S } ) = \mathsf { L i e } W ( F _ { S } ) .
$$

Define:

Then

$$
W ( F _ { S } ) \cong V ( F _ { S } ) \times U ( F _ { S } ) \ ,
$$

where

$$
U ( F _ { S } ) \subset \mathrm { c e n t e r } W ( F _ { S } )
$$

and

$W ( F _ { S } ) / U ( F _ { S } )$ is an abelian Lie group $\cong V ( F _ { S } )$ .

We also want to refine the decomposition of $Z ( w _ { S } )$ introduced in Theorem 3.10. If $\sigma$ is the Cartan involution of $\mathfrak { g }$ then

$$
{ \boldsymbol { \sigma } } ( { \mathfrak { g } } ^ { \varphi } ) = { \mathfrak { g } } ^ { - \varphi } { \mathrm { ~ f o r ~ a l l ~ } } \varphi \in { \mathfrak { g } } ^ { + } ;
$$

hence

$$
\sigma ( [ { \mathfrak { g } } ^ { \varphi } , { \mathfrak { g } } ^ { - \varphi } ] ) = [ { \mathfrak { g } } ^ { \varphi } , { \mathfrak { g } } ^ { - \varphi } ] ,
$$

and

$$
[ \mathfrak { g } ^ { \varphi } , \mathfrak { g } ^ { - \varphi } ] = [ \mathfrak { g } ^ { \varphi } , \mathfrak { g } ^ { - \varphi } ] \cap \mathfrak { a } \oplus \underbrace { [ \mathfrak { g } ^ { \varphi } , \mathfrak { g } ^ { - \varphi } ] \cap m ( \mathfrak { a } ) } _ { \mathrm { c a l l ~ t h i s ~ } [ \mathfrak { g } ^ { \varphi } , \mathfrak { g } ^ { - \varphi } ] _ { ( e ) } } .
$$

Note that we have

$$
\mathrm { I } _ { S } = \mathfrak { g } _ { h } ( F _ { S } ) = \sum _ { \varphi = \frac { \pm \gamma _ { i } \pm \gamma _ { j } } { 2 } \mathrm { ~ o r ~ } \frac { \pm \gamma _ { i } } { 2 } } ( \mathfrak { g } ^ { \varphi } + [ \mathfrak { g } ^ { \varphi } , \mathfrak { g } ^ { - \varphi } ] _ { ( e ) } ) + \sum _ { i \notin S } \mathbb { R } x _ { i } .
$$

Define analogously:

$$
{ \mathfrak { g } } _ { \ell } ( F _ { S } ) = \sum _ { \varphi = { \frac { \gamma _ { i } - \gamma _ { j } } { 2 } } \atop { i , j \in S } } ( { \mathfrak { g } } ^ { \varphi } + [ { \mathfrak { g } } ^ { \varphi } , { \mathfrak { g } } ^ { - \varphi } ] _ { ( e ) } ) + \sum _ { i \in S } { \mathbb { R } } x _ { i } .
$$

This is the subalgebra of Lie $\widetilde { G } _ { \ell } ( F _ { S } )$ generated by the ${ \mathfrak { g } } ^ { \varphi }$ and the $x _ { i }$ . It is also an ideal in Lie $\widetilde { G } _ { \ell } ( F _ { S } )$ , so Lie $\widetilde { G } _ { \ell } ( F _ { S } )$ is the sum of ${ \mathfrak { g } } _ { \ell } ( F _ { S } )$ and a compact ideal $\mathfrak { m } ( F _ { S } )$ . Therefore, we have

$$
\mathfrak { n } ( F _ { S } ) _ { 0 } = \mathfrak { g } _ { h } ( F _ { S } ) \oplus \mathfrak { g } _ { \ell } ( F _ { S } ) \oplus \mathfrak { m } ( F _ { S } ) ~ .
$$

Globally,

$$
Z ( w _ { S } ) ^ { o } = G _ { h } ( F _ { S } ) \cdot \underbrace { G _ { \ell } ( F _ { S } ) \cdot M ( F _ { S } ) } _ { \mathrm { t h i s ~ i s ~ } \tilde { G } _ { \ell } ( F _ { S } ) }
$$

(which stands for the direct product of three groups modulo a finite subgroup), where

$$
\begin{array} { r l } & { G _ { h } ( F _ { S } ) \mathrm { i s ~ s e m i - s i m p l e , ~ w i t h ~ n o ~ c o m p a c t ~ f a c t o r s ~ } , } \\ & { G _ { \ell } ( F _ { S } ) \mathrm { i s ~ r e d u c t i v e , ~ w i t h ~ n o ~ c o m p a c t ~ f a c t o r s ~ } , } \\ & { M ( F _ { S } ) \mathrm { i s ~ c o m p a c t } . } \end{array}
$$

Thus, finally,

$$
N ( F _ { S } ) ^ { o } = [ G _ { h } ( F _ { S } ) \cdot G _ { \ell } ( F _ { S } ) \cdot M ( F _ { S } ) ] \times V ( F _ { S } ) \times U ( F _ { S } ) ~ .
$$

General case We can use that $F = k \cdot F _ { S }$ , for some $k \in K$ , $S \subset \{ 1 , \ldots , r \}$ , and hence $N ( F ) = k N ( F _ { S } ) k ^ { - 1 }$ , to get the same decomposition for $N ( F )$ . However, we may also characterize the decomposition intrinsically using the homomorphism $w _ { F }$ associated canonically to $F$ . Then

$$
\begin{array} { c } { { \mathrm { L i e } N ( F ) = \mathrm { s u m } \mathrm { o f } \ 0 , 1 , 2 \mathrm { - e i g e n s p a c e s \ f o r \ A d } w _ { F } ( t ) } } \\ { { { } } } \\ { { { } = \mathrm { L i e } Z ( w _ { F } ) \oplus \mathsf { v } ( F ) \oplus \mathsf { u } ( F ) ~ . } } \end{array}
$$

Let $V ( F ) = \exp { \mathfrak { v } } ( F )$ , $U ( F ) = \exp { \mathfrak { u } } ( F )$ . Next, $Z ( w _ { \ / F } ) ^ { o }$ decomposes into $G _ { h } ( F )$ and $\widetilde { G } _ { \ell } ( F )$ , as in Theorem 3.10, where $\widetilde { G } _ { \ell }$ acts identically on $F$ . Writing $\widetilde { G } _ { \ell }$ as a product of its non-compact and compact factors, we obtain

$$
N ( F ) ^ { o } = [ G _ { h } ( F ) \cdot G _ { \ell } ( F ) \cdot M ( F ) ] \times V ( F ) \times U ( F ) \ .
$$

# 4.2

t result, te that maps the  pace for Ad $N ( F ) ^ { o }$ $\mathrm { d } \varphi _ { F }$ $k$ $\left( \begin{array} { c c } { t } & { 0 } \\ { 0 } & { t ^ { - 1 } } \end{array} \right)$ $\mathrm { S L } ( 2 , \mathbb { R } )$ $k$ $\boldsymbol { { \vert w _ { F } ( t ) } }$ $\mathfrak { g }$

$$
\omega _ { F } : = \mathrm { d } \varphi _ { F } \left( 0 , \left( \begin{array} { l l } { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } \end{array} \right) \right) \in \mathrm { u } ( F ) ,
$$

and hence

$$
\Omega _ { F } : = \varphi _ { F } \left( 1 , \left( \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right) \right) = \exp \omega _ { F } \in U ( F ) \ .
$$

With this definition, we have:

# Theorem 4.1

(1) $\left[ G _ { h } ( F ) \cdot M ( F ) \right] \times W ( F )$ centralizes $U ( F )$ and $\mathfrak { u } ( F )$ . (2) The orbit of $\Omega _ { F }$ by $G _ { \ell } ( F )$ ,

$$
C ( F ) = \left\{ g \Omega _ { F } g ^ { - 1 } \ : | \ : g \in G _ { \ell } ( F ) \right\} ,
$$

is an open homogeneous cone in $U ( F )$ , self-adjoint with respect to the positive-definite quadratic form

$$
\langle x , y \rangle = - B ( x , \sigma ( y ) )
$$

on $\mathfrak { u } ( F )$ , hence on $U ( F )$ . The centralizer of $\Omega _ { F }$ in $G _ { \ell } ( F )$ is the maximal compact subgroup $G _ { \ell } ( F ) \cap K$ , hence

$$
C ( F ) \cong G _ { \ell } ( F ) / G _ { \ell } ( F ) \cap K .
$$

Proof We show first that†

$$
G _ { \ell } ( F ) \cap K = \{ g \in G _ { \ell } ( F ) \mid \mathrm { A d } g ( \omega _ { F } ) = \omega _ { F } \} \ ,
$$

and that $\operatorname { A d } M ( F )$ fixes $\omega _ { F }$ . In fact, note that

$$
\begin{array} { l } { { \displaystyle o _ { F } ^ { 0 } = \varphi _ { F } \left( 1 , \left( \begin{array} { l l } { { 1 } } & { { - \mathrm { i } } } \\ { { 0 } } & { { 1 } } \end{array} \right) \right) \cdot o } } \\ { { \displaystyle ~ = \exp ( - \mathrm { i } \omega _ { F } ) \cdot o } ~ ; } \end{array}
$$

hence, for all $g \in \widetilde { G } _ { \ell } ( F ) = G _ { \ell } ( F ) \cdot M ( F )$ ,

$$
\begin{array} { r } { g \cdot o = g \exp ( \mathrm { i } \omega _ { F } ) \cdot \exp ( - \mathrm { i } \omega _ { F } ) \cdot o } \\ { = \exp ( \mathrm { i } \mathrm { A d } g ( \omega _ { F } ) ) \cdot g o _ { F } ^ { 0 } \ . \qquad } \end{array}
$$

By Proposition 3.11, $g o _ { F } ^ { 0 } = o _ { F } ^ { 0 }$ . So

$$
\begin{array} { r l } & { g \cdot o = \exp ( \mathrm { i } \mathrm { A d } g ( \omega _ { F } ) ) \cdot \exp ( - \mathrm { i } \omega _ { F } ) \cdot o } \\ & { \qquad = \exp ( \mathrm { i } \big ( \mathrm { A d } g ( \omega _ { F } ) - \omega _ { F } ) \big ) \cdot o ~ . } \end{array}
$$

But nothing in $U _ { \mathbb { C } }$ fixes $o$ , so $g \in K$ if and only if $\operatorname { A d } g ( \omega _ { F } ) = \omega _ { F }$ . Next, count dimensions taking $F = F _ { S }$ . Using the fact that $\sigma ( { \mathfrak { g } } ^ { \varphi } ) = { \mathfrak { g } } ^ { - \varphi }$ , we find

$$
\dim G _ { \ell } ( F ) / G _ { \ell } ( F ) \cap K = \dim \left\{ - { \mathrm { 1 - e i g e n s p a c e ~ o f ~ } } \sigma { \mathrm { ~ i n ~ g } } _ { \ell } ( F ) \right\}
$$

But, using Proposition 2.7 and the remarks following it, we have

$$
\dim { \mathfrak { g } } ^ { ( \gamma _ { i } - \gamma _ { j } ) / 2 } = \# \operatorname { o f } { ( { \mathfrak { b } } _ { i j } ) } \mathrm { - f a c t o r s ~ i n ~ } { \mathfrak { g } } = \dim { \mathfrak { g } } ^ { ( \gamma _ { i } + \gamma _ { j } ) / 2 } \ , \ \operatorname { f o r } { i > j } \ ,
$$

and moreover ${ \mathfrak { g } } ^ { \gamma _ { i } }$ is 1-dimensional and lies entirely in the $\left( \mathbf { a } _ { i } \right)$ -factor, i.e., the i’th copy of ${ \mathfrak { s l } } ( 2 , \mathbb { R } )$ . Thus,

$$
| S | + \sum _ { \stackrel { i > j } { i , j \in S } } \dim \mathfrak { g } ^ { ( \gamma _ { i } - \gamma _ { j } ) / 2 } = \sum _ { \stackrel { i \geq j } { i , j \in S } } \dim \mathfrak { g } ^ { ( \gamma _ { i } + \gamma _ { j } ) / 2 } = \dim \mathfrak { u } ( F ) .
$$

Therefore,

$$
g \longmapsto \operatorname { A d } g ( \omega _ { F } )
$$

defines an isomorphism of $G _ { \ell } ( F ) / G _ { \ell } ( F ) \cap K$ with an open subset $C ( F )$ of $\mathfrak { u } ( F )$ . It follows from Chapter II, Proposition 1.10, that $C ( F )$ is a homogeneous cone, self-adjoint for any inner product $\langle \cdot , \cdot \rangle$ such that ${ } ^ { t } ( \operatorname { A d } g ) ^ { - 1 } = \operatorname { A d } \left( { \boldsymbol { \sigma } } ( g ) \right)$ , or

$$
\langle \operatorname { A d } g ( x ) , \operatorname { A d } \sigma g ( y ) \rangle = \langle x , y \rangle { \mathrm { ~ f o r ~ a l l ~ } } x , y \in \mathfrak { u } ( F ) .
$$

$^ \dagger$ This argument is due to P. Deligne.

The inner product $- B ( x , \sigma ( y ) )$ has this property. This proves (2).

As for (1), by checking roots one sees

$$
[ \mathfrak { g } _ { h } ( F ) , \mathfrak { u } ( F ) ] = [ \mathfrak { v } ( F ) + \mathfrak { u } ( F ) , \mathfrak { u } ( F ) ] = ( 0 ) \ ,
$$

and hence $G _ { h } ( F ) \times W ( F )$ centralizes $U ( F )$ . Finally, since

$$
[ { \mathfrak { m } } ( F ) , \omega _ { F } ] = ( 0 ) ~ ,
$$

we have, for all $x \in { \mathfrak { g } } _ { \ell } ( F )$ ,

$$
[ { \mathfrak m } ( F ) , [ x , \omega _ { F } ] ] = [ [ { \mathfrak m } ( F ) , x ] , \omega _ { F } ] = ( 0 ) ,
$$

hence

$$
[ \mathfrak { m } ( F ) , \mathfrak { u } ( F ) ] = ( 0 ) \ ,
$$

and $M ( F )$ centralizes $U ( F )$ .

Corollary $4 . 2 \ : \varphi _ { F } ( U ^ { 1 } ) \subset G _ { h } ( F ) \times M ( F ) .$

Proof Since $\varphi _ { F } ( U ^ { 1 } )$ and $w _ { F }$ commute, $\varphi _ { F } ( U ^ { 1 } ) \subset G _ { h } \times G _ { \ell } \times M$ and, by Theorem 4.1, it suffices to show that $\varphi _ { F }$ centralizes $\mathfrak { u } ( F )$ . But if $F = F _ { S }$ , then

$$
{ \mathfrak { u } } ( F ) \subset { \mathrm { f a c t o r s ~ o f ~ t y p e ~ } } ( { \mathfrak { a } } _ { i } ) , ( { \mathfrak { b } } _ { i j } ) , \quad i , j \in S \ ,
$$

and

$$
\varphi _ { F _ { S } } ( \mathrm { e } ^ { \mathrm { i } \theta } ) = \varphi ( \mathrm { e } ^ { \mathrm { i } \theta } ; \dots , \underbrace { 1 } _ { \mathrm { i f } \ i \in { \cal S } } , \dots , \underbrace { \mathrm { e } ^ { \mathrm { i } \theta } } _ { \mathrm { i f } \ i \notin { \cal S } } , \dots ) \ .
$$

The next theorem will show that $U ( F )$ is the center of the unipotent radical $W ( { \boldsymbol { F } } )$ of the parabolic subgroup $N ( F )$ . We denote by $J$ the operator on the vector space ${ \mathfrak { v } } ( F )$

$$
J = \mathrm { A d } \left( \varphi _ { F } ( - \mathrm { i } , I ) \right) .
$$

Then, clearly, $J$ defines a complex structure on $\mathfrak { v } ( F ) \colon \varphi _ { F } ( - 1 , - I ) = h _ { 0 } ( - 1 ) =$ $u _ { 0 } ( 1 ) = e$ ; hence

$$
J ^ { 2 } = \mathrm { A d } \varphi _ { F } ( - 1 , I ) = \mathrm { A d } \varphi _ { F } ( 1 , - I ) = w _ { F } ( - 1 ) ,
$$

which is $- \mathrm { I d }$ on ${ \mathfrak { v } } ( F )$ .

Theorem 4.3 $[ \nu , J \nu ] \in \overline { { C ( F ) } } \setminus \{ 0 \}$ , for all $0 \neq \nu \in { \mathfrak { v } } ( F )$ .

We have the consequence:

Corollary 4.4 $U ( F )$ is the center of $W ( { \boldsymbol { F } } )$ .

Proof of Theorem 4.3 Since $C$ is self-adjoint with respect to $\langle \cdot , \cdot \rangle$ , it is sufficient to show that

$$
\nu \neq 0 \Longrightarrow \langle [ \nu , J \nu ] , y \rangle > 0 { \mathrm { ~ f o r ~ a l l ~ } } y \in C .
$$

But, writing $y = \operatorname { A d } g ^ { - 1 } ( \omega _ { F } )$ with $g \in G _ { \ell }$ , and noting that

$$
\langle \operatorname { A d } ( \sigma ( g ) ) u , u ^ { \prime } \rangle = \langle u , \operatorname { A d } ( g ) ^ { - 1 } u ^ { \prime } \rangle \operatorname { f o r } \operatorname { a l l } u , u ^ { \prime } \in U ( F ) ,
$$

we obtain

$$
\begin{array} { r l } & { \langle [ \nu , J \nu ] , y \rangle = \langle [ \nu , J \nu ] , \mathrm { A d } g ^ { - 1 } ( \omega _ { F } ) \rangle = \langle \mathrm { A d } \sigma ( g ) [ \nu , J \nu ] , \omega _ { F } \rangle } \\ & { \quad \quad = \langle [ \mathrm { A d } \sigma ( g ) \nu , \mathrm { A d } \sigma ( g ) J \nu ] , \omega _ { F } \rangle } \\ & { \quad \quad \quad = \langle [ \mathrm { A d } \sigma ( g ) \nu , J \mathrm { A d } \sigma ( g ) \nu ] , \omega _ { F } \rangle , } \end{array}
$$

where, for the last equality, we used $\varphi _ { F } ( U ^ { 1 } ) \subset G _ { h } \times M$ , so $\varphi _ { F } ( U ^ { 1 } )$ and $G _ { \ell }$ commute. Thus it suffices to show

$$
\nu \ne 0 \Longrightarrow \left. [ \nu , J \nu ] , \omega _ { F } \right. > 0 \ .
$$

Now,

$$
\begin{array} { r l } & { \langle [ \nu , J \nu ] , \omega _ { F } \rangle = - B ( [ \nu , J \nu ] , \sigma ( \omega _ { F } ) ) } \\ & { \qquad = B ( \nu , [ \sigma ( \omega _ { F } ) , J \nu ] ) } \\ & { \qquad = B ( \nu , \sigma ( [ \omega _ { F } , \sigma J \nu ] ) ) \ . } \end{array}
$$

So it suffices to prove

$$
[ \omega _ { F } , \sigma J \nu ] = - \nu , { \mathrm { f o r ~ a l l ~ } } 0 \not = \nu \in { \mathfrak { v } } ( F ) \ ,
$$

and use the fact that $B ( x , \sigma ( y ) )$ is negative-definite. But 

$$
\begin{array} { r l } & { \sigma \circ J = \mathrm { A d } \varphi _ { F } \left( \mathrm { i } , \left( \begin{array} { c c } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right) \right) \circ \mathrm { A d } \varphi _ { F } ( - \mathrm { i } , I ) \quad } \\ & { \qquad = \mathrm { A d } \varphi _ { F } \left( 1 , \left( \begin{array} { c c } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right) \right) , } \end{array}
$$

and hence

$$
\begin{array} { r l } & { [ \omega _ { F } , \sigma J \nu ] = \left( \mathrm { A d } \Omega _ { F } - I \right) \left( \mathrm { A d } \varphi _ { F } \left( 1 , \left( \begin{array} { c c } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right) \right) \nu \right) } \\ & { \qquad = \mathrm { A d } \varphi _ { F } \left( 1 , \left( \begin{array} { c c } { - 1 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right) \right) \nu - \mathrm { A d } \varphi _ { F } \left( 1 , \left( \begin{array} { c c } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right) \right) \nu . } \end{array}
$$

Now suppose we put together the $+ 1$ and $^ { - 1 }$ -eigenspaces for $\operatorname { A d } w _ { F } ( t )$ : the $+ 1$ -space is ${ \mathfrak { v } } ( F )$ and the whole space is given by

$$
\mathfrak { h } = \{ x \in \mathfrak { g } \mid \mathrm { A d } w _ { F } ( - 1 ) x = - x \} \ ,
$$

which is a subspace invariant under SL(2,R). Since  t 00 t −1  has only ±1-          $\mathbb { R } ^ { 2 }$ . Therefore we need only calculate in $\mathbb { R } ^ { 2 }$ , with $\nu = \left( \begin{array} { l } { 1 } \\ { 0 } \end{array} \right)$ :

$$
\left( \begin{array} { c c } { { - 1 } } & { { 1 } } \\ { { - 1 } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { 1 } } \\ { { 0 } } \end{array} \right) - \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - 1 } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { 1 } } \\ { { 0 } } \end{array} \right) = - \left( \begin{array} { c } { { 1 } } \\ { { 0 } } \end{array} \right) .
$$

# 4.3

Next, we want to interpret the group-theoretic structure of $N ( F ) ^ { o }$ geometrically as a decomposition of $D$ . First, by Proposition 3.6, $N ( F )$ , and hence $N ( F ) ^ { o }$ , acts transitively on $D$ , so that, using our more refined decomposition of $N ( F ) ^ { o }$ , we can write

$$
D \cong ( [ G _ { h } ( F ) \cdot G _ { \ell } ( F ) \cdot M ( F ) ] \times W ( F ) ) / [ K _ { h } ( F ) \cdot K _ { \ell } ( F ) \cdot M ( F ) ] ,
$$

where

$$
\begin{array} { r l } & { K _ { h } ( F ) = G _ { h } ( F ) \cap K = \mathrm { a ~ m a x i m a l ~ c o m p a c t ~ s u b g r o u p ~ o f ~ } G _ { h } ( F ) \ , } \\ & { K _ { \ell } ( F ) = G _ { \ell } ( F ) \cap K = \mathrm { a ~ m a x i m a l ~ c o m p a c t ~ s u b g r o u p ~ o f ~ } G _ { \ell } ( F ) \ . } \end{array}
$$

Therefore, firstly, there is an $N ( F ) ^ { o }$ -equivariant mapping

$$
\Phi _ { F } : D \longrightarrow C ( F ) \mathrm { w i t h } \Phi _ { F } ( o ) = \Omega _ { F } ,
$$

defined by the map of homogeneous spaces

$$
\begin{array} { r l r } & { } & { \left( \left[ G _ { h } \cdot G _ { \ell } \cdot M \right] \times W \right) / \left[ K _ { h } \cdot K _ { \ell } \cdot M \right] } \\ & { } & { \longrightarrow \left( \left[ G _ { h } \cdot G _ { \ell } \cdot M \right] \times W \right) / \left( \left[ G _ { h } \cdot K _ { \ell } \cdot M \right] \times W \right) \cong G _ { \ell } / K _ { \ell } \ . } \end{array}
$$

Secondly, the whole domain $D$ can be decomposed as a real manifold:

$$
D \cong F \times C ( F ) \times W ( F )
$$

by

$$
x \longmapsto \left( \pi _ { F } ( x ) , \Phi _ { F } ( x ) , w ( x ) \right) ,
$$

where $w ( x )$ is defined as follows. Let

$$
\begin{array} { r l } & { \pi _ { F } ( x ) = g _ { h } { ( \pi _ { F } ( o ) ) } \mathrm { ~ w i t h ~ } g _ { h } \in G _ { h } \ , } \\ & { \Phi _ { F } ( x ) = g _ { \ell } { ( \Omega _ { F } ) } \mathrm { ~ w i t h ~ } g _ { \ell } \in G _ { \ell } \ , } \end{array}
$$

then

$$
x = w ( x ) \cdot g _ { h } \cdot g _ { \ell } \cdot o \mathrm { w i t h } w ( x ) \in W ( F ) \ .
$$

To understand the situation better, we introduce a new open subset $D ( F ) \subset { \check { D } }$

Definition 4.5 Let $D ( F ) = U ( F ) _ { \mathbb { C } } \cdot D = \cup _ { g \in U ( F ) _ { \mathbb { C } } } g \cdot D .$

Note that, since $U ( F )$ is a normal subgroup of $N ( F ) ^ { o }$ , it follows that $N ( F ) ^ { o }$ · $U ( F ) _ { \mathbb { C } }$ is a subgroup of $G _ { \mathbb { C } }$ , which clearly acts transitively on $D ( F )$ . Recall the point:

$$
\begin{array} { c } { o _ { F } ^ { 0 } = \exp ( - \mathrm { i } \omega _ { F } ) \cdot o \in D ( F ) . } \\ { { } } \\ { K _ { h } ( F ) \cdot G _ { \ell } ( F ) \cdot M ( F ) = \{ g \in N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } } \mid g o _ { F } ^ { 0 } = o _ { F } ^ { 0 } \} . } \end{array}
$$

Proof We saw in Proposition 3.11 that $G _ { \ell } \cdot M$ fixes $o _ { F } ^ { 0 }$ . Moreover, $K _ { h }$ fixes $o$ and $K _ { h }$ commutes with $\exp ( - \mathrm { i } \omega _ { F } )$ , so $K _ { h }$ fixes $o _ { F } ^ { 0 }$ . This shows ” $\subset$ .” But, since $K _ { \mathbb { C } } \cdot P _ { - }$ is the stabilizer of $o$ in $G _ { \mathbb { C } }$ , the RHS equals

$$
N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } } \cap \exp ( - \mathrm { i } \omega _ { F } ) \cdot K _ { \mathbb { C } } P _ { - } \cdot \exp ( \mathrm { i } \omega _ { F } )
$$

(intersection inside $G _ { \mathbb { C } }$ ). A simple root calculation shows that the Lie algebra of this group equals the Lie algebra of the LHS. But considering $G _ { \mathbb { C } }$ as the real points of $R _ { \mathbb { C } / \mathbb { R } } \mathcal { G } _ { \mathbb { C } }$ , both $N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } }$ and $K _ { \mathbb { C } } \cdot P _ { - }$ are the connected components of the real points of algebraic subgroups. So this intersection has finitely many components. Since $K _ { h } \subset G _ { h }$ is maximal compact, and $W ( F ) \cdot U ( F ) _ { \mathbb { C } }$ is torsion-free, there is no group $H$ with

$$
N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } } \supset H \underset { \mathrm { ( f i n i t e ~ i n d e x ) } } { \supseteq } K _ { h } \times G _ { \ell } \times M .
$$

Therefore, if we take $o _ { F } ^ { 0 }$ as basepoint of $D ( F )$ , we get an isomorphism:

$$
\begin{array} { r l r } { \big ( G _ { h } ( F ) / K _ { h } ( F ) \big ) \times { \cal W } ( F ) \cdot { \cal U } ( F ) _ { \mathbb { C } } } & { \stackrel { \sim } { \longrightarrow } { \cal D } ( F ) ~ , } & { } \\ { ( g , w ) \longmapsto } & { w \cdot g \big ( o _ { F } ^ { 0 } \big ) ~ , } & { } \end{array}
$$

and hence

$$
{ \cal F } \times { \cal V } ( { \cal F } ) \times { \cal U } ( { \cal F } ) _ { \mathbb { C } } \cong { \cal D } ( { \cal F } ) \ .
$$

The projection $\pi _ { F }$ to $F$ is again just given by

$$
\begin{array} { c c c } { { N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } } / K _ { h } \cdot G _ { \ell } \cdot M } } & { { \longrightarrow } } & { { N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } } / K _ { h } \cdot G _ { \ell } \cdot M \cdot W \cdot U _ { \mathbb { C } } \ , } } \\ { { \downarrow | } } & { { } } & { { } } \\ { { D ( F ) } } & { { } } & { { G _ { h } / K _ { h } } } \end{array}
$$

which is $N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } }$ -equivariant, and hence is the $\pi _ { F }$ defined in Section 3.4. Also $N ( F ) ^ { o }$ is a subgroup of $N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } }$ , so projection onto the imaginary part of the $U$ -coordinate is given by

$$
\begin{array} { c c c c } { { N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } } / K _ { h } \cdot G _ { \ell } \cdot M } } & { { \longrightarrow } } & { { N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } } / N ( F ) ^ { o } \ , } } \\ { { } } & { { } } & { { } } & { { \psi \ } } \\ { { D ( F ) } } & { { } } & { { } } & { { U ( F ) } } \end{array}
$$

which is also $N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } }$ -equivariant, where $N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } }$ acts on $U ( F )$ via the vertical isomorphism in the preceding diagram, which amounts to letting $N ( F ) ^ { o }$ act on $U ( F )$ by conjugation and letting $\operatorname { i } U ( F )$ act on $U ( F )$ by translation. We call this $\Phi _ { F }$ because we claim that we get a commutative diagram involving this projection:

$$
\begin{array} { c c c c } { { D } } & { { \stackrel { } { \longrightarrow } } } & { { C ( F ) } } \\ { { \cap } } & { { } } & { { \bigcap } } \\ { { D ( F ) } } & { { \stackrel { } { \longrightarrow } } } & { { U ( F ) . } } \end{array}
$$

To see this, let $x = w \cdot g _ { h } \cdot g _ { \ell } \cdot o \in D$ , with $w \in W$ , $g _ { h } \in G _ { h }$ , $g _ { \ell } \in G _ { \ell }$ . Then $\Phi _ { F } ( x ) = g _ { \ell } ( \Omega _ { F } )$ , and, since $G _ { \ell }$ acts on $C ( F )$ by conjugation, we obtain

$$
\Phi _ { F } ( x ) = g _ { \ell } \exp ( \omega _ { F } ) g _ { \ell } ^ { - 1 } .
$$

But

$$
\begin{array} { r l } & { x = w \cdot g _ { h } \cdot g _ { \ell } \cdot \exp ( \mathrm { i } \omega _ { F } ) \cdot \exp ( - \mathrm { i } \omega _ { F } ) \cdot o } \\ & { \quad = w \cdot g _ { h } \cdot g _ { \ell } \cdot \exp ( \mathrm { i } \omega _ { F } ) \cdot g _ { \ell } ^ { - 1 } \cdot o _ { F } ^ { 0 } \quad ( \mathrm { s i n c e } ~ g _ { \ell } o _ { F } ^ { 0 } = o _ { F } ^ { 0 } ) . } \end{array}
$$

Since $w \cdot g _ { h } \in N ( F )$ , and $g _ { \ell } \cdot \exp ( \mathrm { i } \omega _ { F } ) \cdot g _ { \ell } ^ { - 1 } \in \mathrm { i } U ( F ) \subset U ( F ) _ { \mathbb { C } }$ , the imaginary part of the $U ( F ) _ { \mathbb { C } }$ -coordinate of $x$ is just $g _ { \ell } \cdot \exp ( \omega _ { F } ) \cdot g _ { \ell } ^ { - 1 }$ . In fact:

Lemma 4.7 $D = \{ x \in D ( F ) \mid \Phi _ { F } ( x ) \in C ( F ) \} .$

Proof Let $x = g \cdot \exp ( \mathrm { i } u ) \cdot o _ { F } ^ { 0 }$ be any element of $D ( F )$ , where $g \in N ( F ) ^ { o }$ and $u \in { \mathfrak { u } } ( F )$ . If $u \in C ( F )$ , then $u = \mathrm { A d } h ( \omega _ { F } )$ with $h \in G _ { \ell }$ , and hence

$$
\begin{array} { r l } & { x = g \cdot \left( h \exp ( \mathrm { i } \omega _ { F } ) h ^ { - 1 } \right) \cdot o _ { F } ^ { 0 } } \\ & { \quad = g \cdot h \cdot \exp ( \mathrm { i } \omega _ { F } ) \cdot o _ { F } ^ { 0 } \quad ( \mathrm { s i n c e } h \cdot o _ { F } ^ { 0 } = o _ { F } ^ { 0 } ) } \\ & { \quad = g \cdot h \cdot o \in D . } \end{array}
$$

The idea of Siegel domains is that $D ( F )$ is a much simpler complex manifold than $D$ , and that $D$ is defined inside $D ( F )$ by the tube-domain-like requirement

$$
\Phi _ { F } ( x ) \in C ( F ) .
$$

To see what $D ( F )$ is, note that because of the isomorphism (4.2) above, $U ( F ) _ { \mathbb { C } }$ acts freely on $D ( F )$ , making it into a principal homogeneous space over

$$
\begin{array} { r l } & { D ( F ) ^ { \prime } : = D ( F ) / U ( F ) _ { \mathbb { C } } } \\ & { \qquad \cong N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } } / K _ { h } \cdot G _ { \ell } \cdot M \cdot U ( F ) _ { \mathbb { C } } } \\ & { \qquad = N ( F ) ^ { o } / K _ { h } \cdot G _ { \ell } \cdot M \cdot U ( F ) ~ . } \end{array}
$$

In turn, $V ( F )$ acts freely on $D ( F ) ^ { \prime }$ , making it into a principal homogeneous space over $F$ :

$$
\pi _ { F } \left( \begin{array} { c } { { D ( F ) } } \\ { { } } \\ { { \pi _ { F } ^ { \prime } \left| \mathrm { { f i b e r s ~ } } U ( F ) _ { \mathbb { C } } \right| } } \\ { { } } \\ { { D ( F ) ^ { \prime } } } \\ { { } } \\ { { p _ { F } \left| \mathrm { { f i b e r s ~ } } V ( F ) \right. } } \\ { { } } \\ { { \left. F \right. } } \end{array} \right)
$$

Since $U ( F ) _ { \mathbb { C } }$ is a complex subgroup of $G _ { \mathbb { C } }$ , we have that $U ( F ) _ { \mathbb { C } }$ acts holomorphically on $D ( F )$ , and $D ( F ) ^ { \prime }$ has a complex structure making all the maps holomorphic. Note, however, that $V ( F )$ has no natural complex structure and that $D ( F ) ^ { \prime } \longrightarrow F$ is only real-analytically a principal homogeneous space with group $V ( F )$ .

This is as far as we need to carry this analysis of $D$ and $D ( F )$ . The full picture, however, is the following.

(i) There is a holomorphic section of $D ( F )$ over $D ( F ) ^ { \prime }$ , such that

$$
{ \cal D } ( { \cal F } ) \cong { \cal D } ( { \cal F } ) ^ { \prime } \times { \cal U } ( { \cal F } ) _ { \mathbb { C } } \ .
$$

(ii) For each $x \in F$ , there is a complex structure $J _ { x } : V ( F ) \longrightarrow V ( F )$ (with $J _ { o _ { F } }$ being the $J$ defined above) such that $( V ( F ) , J _ { x } )$ acts complex-analytically on $p _ { F } ^ { - 1 } ( x )$ .

(iii) Altogether, $D ( F ) ^ { \prime }$ is a complex vector bundle over $F$ , which can be trivialized as

$$
D ( F ) ^ { \prime } \cong \mathbb { C } ^ { k } \times F ~ ,
$$

such that each $\nu \in V ( F )$ acts as

$$
( x , a ) \longmapsto ( x + \lambda _ { \nu } ( a ) , a )
$$

where $\lambda _ { \nu } ( a )$ is holomorphic in $a$ and linear in $\nu$ .

Via (i) and (iii), we get a holomorphic isomorphism:

$$
D ( F ) \cong U ( F ) _ { \mathbb { C } } \times \mathbb { C } ^ { k } \times F
$$

(NB not the same as the more elementary group-theoretic isomorphism $D ( F ) { \cong }$ $U ( F ) _ { \mathbb { C } } \times V ( F ) \times F$ in (4.2) above).

(iv) In this product representation

$$
\Phi _ { F } ( x , y , z ) = \mathrm { I m } x - h _ { z } ( y , y ) ,
$$

where $h _ { z }$ is a real-bilinear quadratic form

$$
\mathbb { C } ^ { k } \times \mathbb { C } ^ { k } \longrightarrow U ( F )
$$

depending real-analytically on z.9

Thus

$$
D \cong \left\{ ( x , y , z ) \in U ( F ) _ { \mathbb { C } } \times \mathbb { C } ^ { k } \times F \mid \operatorname { I m } x \in C ( F ) + h _ { z } ( y , y ) \right\} .
$$

For proofs, see Koranyi–Wolf [7] and Satake [11]. We summarize the essential maps that we will use in Section 5 below:

$$
\begin{array} { r l } { { C ( F ) } } & { { } { \subset } \quad U ( F ) } \\ { { \Biggl \{ \Phi _ { F } } } & { { \Biggl \{ \Phi _ { F } } } \\ { { D } } & { { \subset } \quad D ( F ) \quad \subset \quad { \breve { D } } } \\  { \Biggl \} } & { { \Biggl \{ \pi _ { F } ^ { \prime } \colon { \textrm { p h s } } \mathrm { ~ f o r } \ : U ( F ) _ { \Sigma } } } \\ { { \pi _ { F } \setminus D ( F ) ^ { \prime } } } & { { } } \\ { { \setminus \Biggl \{ p _ { F } \colon { \textrm { p h s } } \mathrm { ~ f o r } \ : V ( F ) } } \\ { { \quad } } &  { \Biggl \} } \end{array}
$$

This whole diagram is $N ( F ) ^ { o }$ -equivariant; all but $D$ and $C ( F )$ is $N ( F ) ^ { o } \cdot U ( F ) _ { \mathbb { C } }$ - equivariant.

An interesting topic that we have not seen explored is to investigate the third open subset of $\check { D }$ :

$$
{ \cal D } ( \check { F } ) = { \cal N } ( F ) _ { \mathbb { C } } \cdot { \cal D } = \bigcup _ { g \in { \cal N } ( F ) _ { \mathbb { C } } } g \cdot { \cal D } .
$$

Here, $D ( \check { F } )$ is a Zariski-open subset of $\check { D }$ (see Subsection 3.4) and appears to sit in a double fibration:

$$
\begin{array} { r l } & { D ( \check { F } ) } \\ & { \begin{array} { l } { \biggl | \mathrm { p . h . s . f o r } U ( F ) _ { \mathbb { C } } } \\ { \check { V } } \end{array} } \\ & { D ( \check { F } ) ^ { \prime } } \\ & { \begin{array} { l } { \biggl | \mathrm { c x . v e c t o r ~ b u n d l e ~ a n d ~ p . h . s . ~ f o r } V ( F ) } \\ { \check { V } } \end{array} } \\ & { \begin{array} { r l } { \check { F } } & { } \end{array} } \end{array}
$$

in which $D ( F )$ and $D ( F ) ^ { \prime }$ are just the inverse images of $F \subset { \check { F } }$ .

# 4.4

The final point of this section is to compare $N ( F )$ and $N ( F ^ { \prime } )$ and their decompositions when $F \subset { \overline { { F ^ { \prime } } } }$ . We formulate the situation in the following theorem.

Theorem 4.8 Let $F \subset { \overline { { F ^ { \prime } } } }$ be two boundary components of $D$ . Then

(i) $U ( F ) \supset U ( F ^ { \prime } )$ , $G _ { \ell } ( F ) \supset G _ { \ell } ( F ^ { \prime } )$ , $G _ { h } ( F ) \subset G _ { h } ( F ^ { \prime } ) .$ .   
(ii) $C ( F ^ { \prime } )$ is a boundary component of $C ( F )$ . Moreover, fixing $F$ , then the map $F ^ { \prime } \longmapsto C ( F ^ { \prime } )$ is an order-reversing bijection between the set of boundary components $F ^ { \prime }$ with $F \subset { \overline { { F ^ { \prime } } } }$ of $D$ and the set of boundary components of $C ( F )$ .

(iii) Now assume $F = F _ { S }$ , $F ^ { \prime } = F _ { S ^ { \prime } }$ , where $S \supset S ^ { \prime }$ . Then

$$
A _ { S } = ( A \cap G _ { \ell } ( F _ { S } ) ) ^ { o }
$$

is a maximal split torus of $G _ { \ell } ( F _ { S } )$ . Let $\begin{array} { r } { U _ { D } = \prod _ { i \in S } \exp ( \mathfrak { g } ^ { \gamma _ { j } } ) \subset U ( F _ { S } ) } \end{array}$ and define coordinates $x _ { 1 } , \ldots , x _ { d }$ on $U _ { D }$ by $x _ { i } ( \exp { \mathfrak { g } } ^ { \gamma _ { j } } ) = 0$ if $i \neq j$ and $x _ { i } ( \Omega _ { F _ { S } } ) = 1$ . Then

$$
\begin{array} { r l } & { \mathrm { i } _ { S } \cdot \Omega _ { F _ { S } } = \{ ( x _ { 1 } , \dots , x _ { d } ) \in U _ { D } \mid x _ { i } > 0 \mathrm { ~ f o r ~ a l l } i = 1 , \dots , d \} , } \\ & { \quad \Omega _ { F _ { S ^ { \prime } } } = ( \dots , \underbrace { 0 } _ { i \in S \backslash S ^ { \prime } } , \dots , \underbrace { 1 } _ { i \in S ^ { \prime } } , \dots ) \in U _ { D } , } \end{array}
$$

and $C ( F _ { S ^ { \prime } } )$ is the boundary component of $C ( F _ { S } )$ whose intersection with $U _ { D }$ is given by

$$
\left\{ \left( x _ { 1 } , \dots , x _ { n } \right) \big | x _ { i } = 0 \mathrm { i f } i \in S \setminus S ^ { \prime } , x _ { i } > 0 \mathrm { i f } i \in S ^ { \prime } \right\} .
$$

(iv) Finally, if $D = \mathcal { G } ( \mathbb { R } ) ^ { o } / K$ , with $\mathcal { G }$ defined over $\mathbb { Q }$ , and $F$ is $a$ rational boundary component, then the subgroups $U ( F )$ , $G _ { \ell } ( F ) \subset N ( F )$ are defined over $\mathbb { Q }$ ; in particular, $U ( F )$ comes from a $\mathbb { Q }$ -vector space and for all $F ^ { \prime }$ with $F \subset { \overline { { F ^ { \prime } } } }$ ,

$$
\left[ \begin{array} { c } { F ^ { \prime } \mathrm { i s ~ a ~ r a t i o n a l ~ b o u n d a r y } } \\ { \mathrm { c o m p o n e n t ~ o f } D } \end{array} \right] \Longleftrightarrow \left[ \begin{array} { c } { C ( F ^ { \prime } ) \mathrm { ~ i s ~ a ~ r a t i o n a l } } \\ { \mathrm { b o u n d a r y ~ c o m p o n e n t ~ o f } C ( F ) } \end{array} \right] .
$$

Proof By Proposition 3.4, any pair $F \subset { \overline { { F ^ { \prime } } } }$ is conjugate by some $k \in K$ to a pair $F _ { S } \subset { \overline { { F } } } _ { S ^ { \prime } }$ , where $S \supset S ^ { \prime }$ . For such pairs, (i) is immediate by the explicit formulae at the beginning of this section. Now, $A \subset G _ { \ell } ( F _ { S } ) \cdot G _ { h } ( F _ { S } )$ and is a maximal split torus in $G$ . So $A = A _ { \ell } \cdot A _ { h }$ , where $A _ { \ell } = ( A \cap G _ { \ell } ( F _ { S } ) ) ^ { o }$ and $A _ { h } = ( A \cap G _ { h } ( F _ { S } ) ) ^ { o }$ are maximal split tori in $G _ { \ell } ( F _ { S } )$ and $G _ { h } ( F _ { S } )$ . In fact, $A _ { \ell } =$ $\textstyle \exp \left( \sum _ { i \in S } { \mathbb { R } } x _ { i } \right)$ . To investigate about the situation in $U ( F )$ , let us identify $U ( F )$ and $\mathfrak { u } ( F )$ via exp, and calculate instead in $\mathfrak { u } ( F )$ . First of all, $\omega _ { F _ { S } }$ is the natural basepoint in

$$
\sum _ { i \in S } \mathfrak { g } ^ { \gamma _ { i } } \ .
$$

(In the notation of Theorem 2.4, it is $\textstyle \sum _ { i \in S } { \frac { - y _ { i } + \mathrm { i } h _ { i } } { 2 } }$ −yi+ihi .) Since A acts on gγi via the character $\mathrm { e } ^ { \gamma _ { i } }$ , it is a simple calculation to describe $A _ { S } \cdot \omega _ { F _ { S } }$ as in part (iii) of the theorem. And if $S \supset S ^ { \prime }$ , then, by definition, $\omega _ { F _ { S ^ { \prime } } }$ is just the projection of $\omega _ { F _ { S } }$ into the subspace

$$
\sum _ { i \in S ^ { \prime } } \mathfrak { g } ^ { \gamma _ { i } } .
$$

Now, by definition,

$$
C ( F _ { S ^ { \prime } } ) = \left\{ \mathrm { A d } g ( \omega _ { F _ { S ^ { \prime } } } ) \vert g \in N ( F _ { S ^ { \prime } } ) \right\} .
$$

But as $\begin{array} { r } { N ( F _ { S ^ { \prime } } ) = G _ { \ell } ( F _ { S ^ { \prime } } ) . } \end{array}$ (centralizer of $U ( F _ { S ^ { \prime } } ) _ { . }$ ), in fact for any group $H$ with

$$
G _ { \ell } ( F _ { S ^ { \prime } } ) \subset H \subset N ( F _ { S ^ { \prime } } ) ,
$$

we have

$$
C ( F _ { S ^ { \prime } } ) = \{ \mathrm { A d } g ( \omega _ { F _ { S ^ { \prime } } } ) \mid g \in H \} \ .
$$

For instance, since $G _ { \ell } ( F _ { S } ) \supset G _ { \ell } ( F _ { S } ^ { \prime } )$ , it follows that $H = N ( F _ { S ^ { \prime } } ) \cap G _ { \ell } ( F _ { S } )$ will do. But let

$$
w _ { S ^ { \prime } } : \mathbb { G } _ { m } \longrightarrow \mathcal { A }
$$

be the homomorphism defined above, relative to $S ^ { \prime }$ . Then $N ( F _ { S ^ { \prime } } ) = P ( w _ { S ^ { \prime } } ^ { - 1 } )$ , so $H$ is the parabolic subgroup $P ( w _ { S ^ { \prime } } ^ { - 1 } ) _ { G _ { \ell } ( F _ { S } ) }$ of $G _ { \ell } ( F _ { S } )$ defined by $w _ { S ^ { \prime } } ^ { - 1 }$ , i.e.,

$$
H = \left\{ g \in G _ { \ell } ( F _ { S } ) \vert \operatorname* { l i m } _ { t \longrightarrow 0 } w _ { S ^ { \prime } } ( t ) g w _ { S ^ { \prime } } ( t ) ^ { - 1 } \mathrm { e x i s t s } \right\} .
$$

But $w _ { S ^ { \prime } }$ is a one-parameter subgroup of $G _ { \ell } ( F _ { S } ) / ( \mathrm { c e n t e r } ) = \mathrm { A u t } ( C ( F _ { S } ) ) ^ { o }$ (via Ad ). Acting on the basepoint $\omega _ { F _ { S } }$ ,

$$
\operatorname * { l i m } _ { t \longrightarrow 0 } \mathrm { A d } w _ { S \backslash S ^ { \prime } } ( t ) \omega _ { F _ { S } } = \omega _ { F _ { S ^ { \prime } } } .
$$

Note that the parabolic subgroups $P ( w _ { S ^ { \prime } } ^ { - 1 } ) _ { G _ { \ell } ( F _ { S } ) }$ and $P ( w _ { S \backslash S ^ { \prime } } ) _ { G _ { \ell } ( F _ { S } ) }$ of $G _ { \ell } ( F _ { S } )$ agree, since $w _ { S }$ is central in $G _ { \ell }$ . Therefore, by Chapter $\mathrm { I I }$ , Proposition 3.4, the boundary component of $C ( F _ { S } )$ through $\omega _ { F _ { S ^ { \prime } } }$ is the orbit of $\omega _ { F _ { S ^ { \prime } } }$ under $P ( w _ { S \setminus S ^ { \prime } } ) _ { G _ { \ell } ( F _ { S } ) } = P ( w _ { S ^ { \prime } } ^ { - 1 } ) _ { G _ { \ell } ( F _ { S } ) }$ in $\mathfrak { u } ( F _ { S } )$ , which is just $C ( F _ { S ^ { \prime } } )$ , namely the locus of points $\operatorname { A d } g ( \omega _ { F _ { S ^ { \prime } } } )$ , with $g \in H$ .

To prove the second part of (ii), we no longer normalize $F$ and $F ^ { \prime }$ , but instead we may assume $G$ is simple because, in the general case, everything breaks up into a product. The first step is to check that, for any two boundary components $F , F ^ { \prime }$ ,

$$
{ \cal F } \subset \overline { { { \cal F } ^ { \prime } } } \mathrm { o r } F ^ { \prime } \subset \overline { { { \cal F } } } \Longleftrightarrow { \cal N } ( F ) \cap { \cal N } ( F ^ { \prime } ) \mathrm { i s } 1
$$

Ordering the roots $\textstyle \sum u _ { i } \gamma _ { i }$ lexicographically, the corresponding minimal real parabolic $P \supset A$ is given by

$$
\mathrm { L i e } P = Z ( { \mathfrak { a } } ) + \sum _ { \mathrm { a l l } ~ i , j } { \mathfrak { g } } ^ { \gamma _ { i } + \gamma _ { j } } + \sum _ { i < j } { \mathfrak { g } } ^ { \frac { \gamma _ { i } - \gamma _ { j } } { 2 } } + \sum _ { i } { \mathfrak { g } } ^ { \frac { \gamma _ { i } } { 2 } } ~ ;
$$

and the maximal real parabolics containing $P$ are $P _ { S }$ for

$$
S = \left\{ 1 \right\} , \left\{ 1 , 2 \right\} , \ldots , \left\{ 1 , 2 , \ldots , r \right\} .
$$

To prove implication $\Longrightarrow$ , if for instance $F \subset { \overline { { F ^ { \prime } } } }$ , we may assume $F = F _ { S }$ , $F ^ { \prime } = F _ { S ^ { \prime } }$ , with $S \supset S ^ { \prime }$ ; applying the Weyl group, we may even assume $S =$ $\{ 1 , \ldots , s \}$ , $S ^ { \prime } = \{ 1 , \ldots , s ^ { \prime } \}$ , with $s \geq s ^ { \prime }$ . Thus $N ( F _ { S } ) \cap N ( F _ { S ^ { \prime } } ) \supset P$ . Conversely, if $N ( F ) \cap N ( F ^ { \prime } )$ contains a parabolic, by conjugating we can assume it contains $P$ . Then $N ( F ) = P _ { \{ 1 , \ldots , s \} }$ and $N ( F ^ { \prime } ) = P _ { \{ 1 , \ldots , s ^ { \prime } \} }$ for some $s , s ^ { \prime }$ . Thus $F = F _ { \{ 1 , \ldots , s \} }$ and $F ^ { \prime } { = } F _ { \{ 1 , \ldots , s ^ { \prime } \} }$ and, depending on whether $s > s ^ { \prime }$ or $s < s ^ { \prime }$ , we get $F \subset { \overline { { F ^ { \prime } } } }$ or $F ^ { \prime } \subset \overline { { F } }$ . Therefore, fixing $F$ , and using the unique representation of parabolics as intersections of maximal parabolics, we find a bijection:

$$
\left\{ F ^ { \prime } | F \subset { \overline { { F ^ { \prime } } } } { \mathrm { o r } } F ^ { \prime } \subset { \overline { { F } } } \right\} \cong \left\{ P \subset N ( F ) \right.
$$

But now $N ( F ) \cong G _ { \ell } ( F ) \cdot G _ { h } ( F ) \cdot M ( F ) \cdot W ( F )$ , so the maximal real parabolics $P \subset N ( F )$ are of the form

$$
P = P _ { \ell } \cdot G _ { h } ( F ) \cdot M ( F ) \cdot W ( F ) , \quad P _ { \ell } \mathrm { m a x i m a l p a r a b o l i c i n } G _ { \ell } ( F ) ,
$$

or

$$
P = G _ { \ell } ( F ) \cdot P _ { h } \cdot M ( F ) \cdot W ( F ) , \quad P _ { h } \mathrm { m a x i m a l p a r a b o l i c i n } G _ { h } ( F ) .
$$

Using our standard models again, it is easy to see that 6 7 $F \subset { \overline { { F ^ { \prime } } } }$ corresponds to the first type and $F ^ { \prime } \subset { \overline { { F } } }$ to the second; i.e., we get bijections:

$$
\begin{array} { r l } & { \left\{ F ^ { \prime } \ : | \ : F \subset \overline { { F ^ { \prime } } } \right\} \cong \left\{ P \subset G _ { \ell } ( F ) \ : \mathrm { m a x i m a l ~ r e a l ~ p a r a b o l i c } \right\} \ : , } \\ & { \left\{ F ^ { \prime } \ : | \ : F ^ { \prime } \subset \overline { { F } } \right\} \cong \left\{ P \subset G _ { h } ( F ) \ : \mathrm { m a x i m a l ~ r e a l ~ p a r a b o l i c } \right\} \ : . } \end{array}
$$

But if $G$ is simple then so is $G _ { \ell } ( F )$ (and $G _ { h } ( F ) )$ : for our purposes, it is enough to check this for $G _ { \ell } ( F _ { S } )$ . Then, for every permutation $\sigma$ of $\{ 1 , \ldots , r \}$ which preserves $s$ , there is an element $w _ { \sigma } \in \operatorname { N o r m } \left( A \right)$ , such that $w _ { \sigma } \gamma _ { i } w _ { \sigma } ^ { - 1 } = \gamma _ { \sigma ( i ) }$ hence $w _ { \sigma } w _ { S } = w _ { S } w _ { \sigma }$ and $w _ { \mathscr { O } } \in N \left( F _ { S } \right)$ . Hence $w _ { \sigma }$ projects to give an element of the Weyl group of the root system of $G _ { \ell } ( F _ { S } )$ , and it follows that the Weyl group of the root system of $G _ { \ell } ( F _ { S } )$ is the full permutation group of $s$ , and hence $G _ { \ell } ( F _ { S } )$ is simple.

Therefore there is a bijection between maximal real parabolics in $G _ { \ell } ( F )$ and boundary components of $C ( F )$ . Altogether we have a bijection from the $F ^ { \prime }$ with $F \subset { \overline { { F ^ { \prime } } } }$ to the boundary components $C ^ { \prime }$ of $C ( F )$ defined by

$$
N _ { G } ( F ^ { \prime } ) \cap G _ { \ell } ( F ) = N _ { G _ { \ell } ( F ) } ( C ^ { \prime } ) ~ .
$$

In fact, this $C ^ { \prime }$ is just $C ( F ^ { \prime } )$ because $N _ { G } ( F ^ { \prime } ) \cap G _ { \ell } ( F ) \subset N _ { G _ { \ell } ( F ) } ( C ( F ^ { \prime } ) )$ and $N _ { G _ { \ell } ( F ) } ( C ^ { \prime } )$ is maximal. This proves (ii).

Finally, if we have a $\mathbb { Q }$ -structure and $F$ is $\mathbb { Q }$ -rational, then $U ( F )$ is the center of the unipotent radical of $F$ , and hence is defined over $\mathbb { Q }$ , and $G _ { \ell } ( F )$ is the factor of $Z ( w _ { F } )$ which acts non-trivially on $U ( F )$ , and hence is defined over $\mathbb { Q }$ . Then, for all ${ \overline { { F ^ { \prime } } } } \supset F$ ,

# Appendix: Connected components

We need to know in Section 5 that the key diagram of Section 4, namely is, in fact, $N ( F )$ -equivariant, in addition to being $N ( F ) ^ { o }$ -equivariant. To check this, note that $U ( F )$ , being the center of the unipotent radical of $N ( F ) ^ { o }$ , is invariant under all outer automorphisms of $N ( F ) ^ { o }$ , and hence is normal in $N ( F )$ . Therefore conjugation by $N ( F )$ carries $U ( F ) _ { \mathbb { C } }$ into itself, and hence $N ( F )$ maps $D ( F )$ into itself. Since ${ \cal D } ( \boldsymbol { F } ) ^ { \prime } \cong { \cal D } ( \boldsymbol { F } ) / U ( \boldsymbol { F } ) _ { \mathbb { C } }$ , we may define the action of $N ( F )$ on $D ( F ) ^ { \prime }$ to make $\pi _ { F } ^ { \prime }$ equivariant. But $\pi _ { F }$ was seen to be $N ( F )$ - equivariant in Subsection 3.4, and hence $p _ { F }$ is also $N ( F )$ -equivariant. Next define the action of $N ( F )$ on $U ( F )$ to be conjugation. Then the equivariance of $\Phi _ { F }$ follows from:

![](images/b9d94b71faf315451eb5c9bae32308430d61edea5447483e5372fa9096c230a4.jpg)

Lemma 4.9 Let $G \subset G ^ { \prime }$ be groups, $G$ normal in $G ^ { \prime }$ . Let $f : X \longrightarrow Y$ be $a$ $G$ -equivariant map of $G ^ { \prime }$ -spaces. If

(i) $G$ is transitive on $X$ , and   
(ii) there is a point $o \in X$ such that $f ( o )$ is the only point of $Y$ fixed by Stab $_ G ( o )$ ,

then $f$ is $G ^ { \prime }$ -equivariant.

Proof Easy.

Apply the lemma with $G = N ( F ) ^ { o }$ , $G ^ { \prime } = N ( F ) , X = D ( F ) , Y = U ( F ) , f = \Phi _ { F }$ , $o = \omega _ { F }$ , noting that $o _ { F } ^ { 0 } \in U ( F )$ is the only point fixed by $K _ { \ell }$ . Finally, in view of the fact that the action of $N ( F )$ on $D ( F )$ maps $D$ into itself, it follows that the action of $N ( F )$ on $U ( F )$ maps $C ( F )$ into itself.

A few remarks on connected components may be in order.

(1) By definition, $G$ is the connected component both of $\operatorname { A u t } ( D )$ and of ${ \mathcal { G } } ( \mathbb { R } )$ ,   
(2) $N ( F )$ is the full subgroup of $G$ fixing $F$ , but may be of finite index in the corresponding subgroup of $\operatorname { A u t } ( D )$ or in the real points of the algebraic subgroup $\mathcal { N } ( F ) \subset \mathcal { G } ( F )$ .

(3) By definition, we made $G _ { h } ( F ) , G _ { \ell } ( F ) , M ( F ) , W ( F )$ connected, getting

$$
N ( F ) ^ { o } = [ G _ { h } \cdot G _ { \ell } \cdot M ] \times W ( F ) ~ .
$$

Then $G _ { h } ( F )$ is the connected component of the real points of the algebraic subgroup ${ \mathcal { G } } _ { h } ( F )$ of $\mathcal { G }$ , and $G _ { \ell } ( F )$ is the connected component of the real points of the algebraic subgroup $\mathcal { G } _ { \ell } ( F )$ of $\mathcal { G }$ . There are projections $G _ { h } ( F ) \to \operatorname { A u t } \left( F \right)$ , resp. $G _ { \ell } ( F ) \longrightarrow \mathrm { A u t } \left( C ( F ) \right)$ , which identify the connected components $\operatorname { A u t } ( F ) ^ { o }$ , resp. $\operatorname { A u t } ( C ( F ) ) ^ { o }$ , with $G _ { h } ( F ) /$ (center), resp. $G _ { \ell } ( F ) /$ (center). However, $W ( { \boldsymbol { F } } )$ , being nilpotent, equals $\mathcal { W } ( F ) ( \mathbb { R } )$ .

# 5 Statement of the Main Theorem

Let $\mathcal { G }$ be a connected semi-simple linear algebraic group defined over $\mathbb { Q }$ such that $G = \mathcal { G } ( \mathbb { R } ) ^ { o }$ is the connected component of the group of automorphisms of a hermitian symmetric domain $D$ .

For a boundary component $F$ of $D$ , we get the associated groups

$$
N ( F ) , W ( F ) , U ( F ) \qquad ( \sec \mathrm { { S e c t i o n } } 4 ) ;
$$

if $F$ is rational, these are algebraic groups defined over $\mathbb { Q }$ .

Let $\Gamma \subset G$ be an arithmetic group, i.e., $\Gamma \subset { \mathcal { G } } ( \mathbb { Q } )$ , and, for any faithful rational representation $\rho : { \mathcal { G } } \longrightarrow \mathrm { G L } ( n )$ , the subgroup $\rho ( \Gamma )$ of $\mathrm { G L } ( n , \mathbb { Q } )$ is commensurable with $\rho ( G ) \cap \mathbf { G L } ( n , \mathbb { Z } )$ . If $F$ is a rational boundary component of $D$ , we let

$$
\begin{array} { r l } & { \Gamma _ { F } = \Gamma \cap N ( F ) \mathrm { ~ , ~ } } \\ & { \Gamma _ { F } ^ { \prime } = \mathrm { s u b g r o u p } \mathrm { ~ o ~ } } \end{array}
$$

$$
U ( { \boldsymbol { F } } ) _ { \mathbb { Z } } = \Gamma \cap U ( { \boldsymbol { F } } ) ~ .
$$

Note that we have an exact sequence of groups:

$$
1 \to \Gamma _ { F } ^ { \prime } \to \Gamma _ { F } \to \overline { { { \Gamma } } } _ { F } \to 1 \ .
$$

Let $\{ \sigma _ { \alpha } \}$ be a $\overline { { \Gamma } } _ { F }$ -admissible polyhedral decomposition of $C ( F ) \subset U ( F )$ (see Chapter II, Definition 4.10).

We now construct a “partial compactification in the direction $F$ ” of $D / U ( F ) _ { \mathbb { Z } }$

$$
( D / U ( { \cal F } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} } .
$$

Reconsider the fiber bundle from Section 4:

$$
{ \cal D } ( { \cal F } ) ( = U ( { \cal F } ) _ { \mathbb { C } } \cdot { \cal D } ) ) \stackrel { \pi _ { 1 } } { \longrightarrow } { \cal D } ( { \cal F } ) ^ { \prime } ( = { \cal D } ( { \cal F } ) / U ( { \cal F } ) _ { \mathbb { C } } ) ,
$$

where $\pi _ { 1 }$ makes $D ( F )$ into a principal fiber bundle over $D ( F ) ^ { \prime }$ with structure group $U ( F ) _ { \mathbb { C } }$ .

From this, we get a quotient fiber bundle $D ( F ) / U ( F ) _ { \mathbb { Z } } \xrightarrow { \overline { { \pi } } _ { 1 } } D ( F ) ^ { \prime }$ , where $\overline { { \pi } } _ { 1 }$ is a principal fiber bundle under the algebraic torus (over $\mathbb { C }$ )

$$
T ( F ) = U ( F ) _ { \mathbb { C } } / U ( F ) _ { \mathbb { Z } } ~ .
$$

The chosen collection $\{ \sigma _ { \alpha } \}$ defines an equivariant embedding (see Chapter I, Section 1)

$$
T ( F ) \subset T ( F ) _ { \{ \sigma _ { \alpha } \} } .
$$

We form

$$
( D ( F ) / U ( F ) _ { \mathbb { Z } } ) \times ^ { T ( F ) } T ( F ) _ { \{ \sigma _ { \alpha } \} } ;
$$

this is the fiber bundle over $D ( F ) ^ { \prime }$ associated to $\overline { { \pi } } _ { 1 }$ with fiber $T ( F ) _  \{ \sigma _ { \alpha \} \} }$ . Finally, define:

$$
\begin{array} { r } { ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} } = \mathrm { i n t e r i o r ~ o f ~ c l o s u r e ~ o f } \ : D / U ( F ) _ { \mathbb { Z } } \mathrm { ~ i n ~ } } \\ { ( D ( F ) / U ( F ) _ { \mathbb { Z } } ) \times ^ { T ( F ) } T ( F ) _ { \{ \sigma _ { \alpha } \} } . } \end{array}
$$

Note that, since $\{ \sigma _ { \alpha } \}$ is a $\overline { { \Gamma } } _ { F }$ -invariant collection, the group $\Gamma _ { F }$ is still acting on $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} }$ ; we will see later that, in fact, $\Gamma _ { F } / U ( F ) _ { \mathbb { Z } }$ acts properly discontinuously on $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} }$ .

Moreover, recall from Section 4 that we have a map

$$
\Phi : D ( F ) \longrightarrow U ( F )
$$

such that

(a) $\Phi$ is equivariant for $N ( F ) \cdot U ( F ) _ { \mathbb { C } }$ , where $N ( F )$ acts on $U ( F )$ by inner automorphisms and $\mathrm { i } a \in \mathrm { i } U ( F )$ acts on $U ( F )$ by translation by $a$ ;   
(b) $\Phi ^ { - 1 } ( C ( F ) ) = D$ ;   
(c) $\Phi$ induces a trivialization of the $U ( F ) _ { \mathbb { C } }$ -bundle $\pi _ { 1 }$ in the imaginary direction:

$$
{ \cal D } ( F ) / U ( F ) \mathop \longrightarrow _ { ( \Phi , \pi _ { 1 } ) } U ( F ) \times { \cal D } ( F ) ^ { \prime } .
$$

Therefore, denoting as in Chapter I, Section 1 by $T ( F ) _ { c }$ the maximal compact torus in $T ( F )$ , i.e., $U ( F ) / U ( F ) _ { \mathbb { Z } }$ , we see that $\Phi$ induces a trivialization in the “absolute value direction” of the $T ( F )$ -bundle $\overline { { \pi } } _ { 1 }$ ;

Moreover, $\Phi$ extends continuously to maps (which we also call $\Phi$ ):

$$
\begin{array} { c c c } { { ( D ( F ) / U ( F ) _ { \mathbb { Z } } ) \times ^ { T ( F ) } T ( F ) _ { \{ \sigma _ { \alpha } \} } } } &  { { { \stackrel { \Phi } { - \to } } } } & { { U ( F ) _ { \{ \sigma _ { \alpha } \} } } } \\ { { \cup } } & { { } } & { { \cup } } \\ { { D ( F ) / U ( F ) _ { \mathbb { Z } } } } & { { { \stackrel { \Phi } { \longrightarrow } } } } & { { U ( F ) } } \end{array}
$$

by the definition

$$
\Phi ( x , y ) = \Phi ( x ) \cdot \mathrm { o r d } ( y ) \ .
$$

Here “·” denotes the action of $U ( F )$ on the partial compactification $U ( F ) _ { \{ \sigma _ { \alpha } \} }$ , and this definition is justified by the second equivariance assertion in (a). As in Section 1, define

$$
C ( F ) ^ { \prime \prime } { = } \mathrm { i n t e r i o r ~ o f ~ c l o s u r e ~ o f } C ( F ) \mathrm { i n } U ( F ) _ { \{ \sigma _ { \alpha } \} } .
$$

The quotient

$$
\Bigl ( ( D ( F ) / U ( F ) _ { \mathbb { Z } } ) \times ^ { T ( F ) } T ( F ) _ { \{ \sigma _ { \alpha } \} } \Bigr ) \Bigl / T ( F ) _ { c }
$$

is a fiber bundle over $D ( F ) ^ { \prime }$ with fiber $U ( F ) _ { \{ \sigma _ { \alpha } \} }$ . It is, again via $\Phi$ , just the product

$$
U ( F ) _ { \{ \sigma _ { \alpha } \} } \times D ( F ) ^ { \prime } .
$$

It therefore follows easily from (b) that $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} }$ can also be described as $\Phi ^ { - 1 } ( C ( F ) ^ { \prime \prime } )$ as follows:

$$
\begin{array} { c c c } { { ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} } = \Phi ^ { - 1 } ( C ( F ) ^ { \prime \prime } ) } } & { { \stackrel { \Phi } { \longrightarrow } } } & { { C ( F ) ^ { \prime \prime } } } \\ { { \cap } } & { { \cap } } \\ { { ( D ( F ) / U ( F ) _ { \mathbb { Z } } ) \times ^ { T ( F ) } T ( F ) _ { \{ \sigma _ { \alpha } \} } } } & { { \stackrel { \Phi } { \longrightarrow } } } & { { U ( F ) _ { \{ \sigma _ { \alpha } \} } . } } \end{array}
$$

These maps will be useful later in the study of $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} }$

The following definition describes the simplicial data on which our compactification will depend.

Definition 5.1 A $\Gamma$ -admissible collection of polyhedra $\{ \sigma _ { \alpha } \}$ is a collection of polyhedra

$$
\left\{ \sigma _ { \alpha } ^ { F } \right\} \subset { \overline { { C ( F ) } } } ,
$$

one for every rational boundary component 9 : 9 $F$ of : $D$ , which are $\overline { { \Gamma } } _ { F }$ -admissible and which satisfy the following two compatibility conditions:

(1) if $F _ { 1 } = \gamma \cdot F _ { 2 }$ with $\gamma \in \Gamma$ , then

$$
\left\{ \sigma _ { \alpha } ^ { F _ { 1 } } \right\} = \left\{ \gamma \cdot \sigma _ { \alpha } ^ { F _ { 2 } } \right\}
$$

via the natural isomorphism

$$
\gamma { : } C ( F _ { 2 } ) \ \xrightarrow { \sim } C ( F _ { 1 } ) \ ;
$$

(2) if $F _ { 1 } \subset { \overline { { F } } } _ { 2 }$ , then

$\left\{ \sigma _ { \alpha } ^ { F _ { 2 } } \right\}$ is exactly the set of cones $\sigma _ { \alpha } ^ { F _ { 1 } } \cap \overline { { { C ( F _ { 2 } ) } } }$ (recall that $\overline { { C ( F _ { 2 } ) } } = \overline { { C ( F _ { 1 } ) } } \cap U ( F _ { 1 } )$ (see Subsection 4.4)).

We can now formulate our main theorem.

Theorem 5.2 (Main Theorem I) Let $\mathcal { G }$ be a semi-simple algebraic group defined over $\mathbb { Q }$ such that $G = \mathcal { G } ( \mathbb { R } ) ^ { o }$ is the connected component of the automorphism group of a hermitian symmetric domain $D$ . Let $\Gamma \subset G$ be an arithmetic group. Let $\{ \sigma _ { \alpha } \}$ be a $\Gamma$ -admissible collection of polyhedra. Then there exists a unique Hausdorff analytic variety $\overline { { D / \Gamma } }$ containing $D / \Gamma$ as an open dense subset and such that, for every rational boundary component $F$ of $D$ , there are open analytic morphisms $\pi _ { F }$ making the following diagram commutative:

$$
\begin{array} { l l } { { D / U ( F ) _ { \mathbb { Z } } } } & { { \longrightarrow \ ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } } } \\ { { \downarrow } } & { { \qquad \begin{array} { l l l } { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } \\ { { D / \Gamma } } & { { \longrightarrow \ } } & { { } } \end{array} } } \end{array}
$$

and such that every point of = $\overline { { D / \Gamma } }$ is in the image of one of the maps $\pi _ { F }$ . Furthermore, = $\overline { { D / \Gamma } }$ is a compact algebraic space.

Proof of uniqueness Set $\widetilde { { \cal D } / \Gamma } = \sqcup _ { F } ( { \cal D } / { \cal U } ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } .$ Then $\overline { { D / \Gamma } }$ is the quotient of $\widetilde { D / \Gamma }$ by an equivalence relation which is described by a closed graph (closed because $\overline { { D / \Gamma } }$ is a Hausdorff space):

$$
\Lambda \subset \widetilde { D / \Gamma } \times \widetilde { D / \Gamma } .
$$

But because the $\pi _ { F }$ are open, $\Lambda$ is just the closure of the equivalence relation defined on $\textstyle \bigcup _ { F } D / U ( F ) _ { \mathbb { Z } }$ by the action of $\Gamma$ ; this shows that $\overline { { D / \Gamma } }$ is unique.

The fact that $\overline { { D / \Gamma } }$ is an algebraic space comes from the following by-product of the proof of the Main Theorem.

Proposition 5.3 There exists a natural morphism from $\overline { { D / \Gamma } }$ to the Baily–Borel “minimal” compactification $( D / \Gamma ) ^ { * }$ , inducing the identity morphism on $D / \Gamma$ .

Now, $( D / \Gamma ) ^ { * }$ is a projective algebraic variety; hence this proposition implies that $\overline { { D / \Gamma } }$ is a Moishezon space, i.e., an algebraic space over $\mathbb { C }$ .

Note also that, to prove the proposition, it suffices to construct a continuous map from $\overline { { D / \Gamma } }$ to $( D / \Gamma ) ^ { * }$ : the fact that this map is holomorphic will then follow from the Riemann extension theorem.

To construct $\overline { { D / \Gamma } }$ , we shall construct the equivalence relation $\Lambda$ explicitly and show in Section 6 that $\Lambda$ is closed.

We use the following straightforward lemma.

Lemma 5.4 Let $F$ and $F ^ { \prime }$ be two rational boundary components such that $F ^ { \prime } \subset \overline { { F } }$ . Then

(1) $U ( F ^ { \prime } ) \subset U ( F ) \subset N ( F ^ { \prime } )$ and $T ( F ^ { \prime } ) \subset T ( F )$ ; (2) $T ( F ) _ { \{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} } \cong T ( F ) \times ^ { T ( F ^ { \prime } ) } T ( F ^ { \prime } ) _ { \{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} }$ , an open subset of $T ( F ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$

(3) the quotient by the action of $U ( F ) _ { \mathbb { Z } }$ on the left factor of

$$
( D ( F ^ { \prime } ) / U ( F ^ { \prime } ) _ { \mathbb { Z } } ) \times ^ { T ( F ^ { \prime } ) } T ( F ^ { \prime } ) _ { \{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} }
$$

is canonically isomorphic to an open subset of

$$
\left( D ( F ) / U ( F ) _ { \mathbb { Z } } \right) \times ^ { T ( F ) } T ( F ) _ { \{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} } ,
$$

which is an open subset of

$$
( D ( F ) / U ( F ) _ { \mathbb { Z } } ) \times ^ { T ( F ) } T ( F ) _ { \{ \sigma _ { \alpha } ^ { F } \} } ;
$$

(4) this induces an etale map ´

$$
\left( D / U ( F ^ { \prime } ) _ { \mathbb { Z } } \right) _ { \{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} } \longrightarrow \left( D / U ( F ) _ { \mathbb { Z } } \right) _ { \{ \sigma _ { \alpha } ^ { F } \} } .
$$

Now introduce the following equivalence relation on $\widetilde { D / \Gamma }$ . Let

$$
x _ { 1 } \in ( D / U ( F _ { 1 } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { 1 } } \} } \mathrm { a n d } x _ { 2 } \in ( D / U ( F _ { 2 } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { 2 } } \} } .
$$

Then $x _ { 1 } \sim x _ { 2 }$ if and only if

(1) there is a rational boundary component $F$ and an element $\gamma \in \Gamma$ , such that

$$
{ \cal F } _ { 1 } \subset \overline { { { \cal F } } } \qquad \mathrm { a n d } \qquad { \boldsymbol \gamma } { \cdot } { \cal F } _ { 2 } \subset \overline { { { \cal F } } } ~ ;
$$

(2) there is a point $x \in ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ that

(a) projects to $x _ { 1 }$ via the canonical map defined by Lemma 5.4,

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow ( D / U ( F _ { 1 } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { 1 } } \} } ,
$$

(b) projects to $\gamma \cdot x _ { 2 }$ via the canonical map

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow ( D / U ( \gamma \cdot F _ { 2 } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { \gamma \cdot F _ { 2 } } \} } .
$$

The transitivity condition of this relation is an easy consequence of Lemma 5.4 plus the following result.

# Lemma 5.5 Let

$$
x \in ( D / U ( { \cal F } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \ .
$$

Among all rational boundary components $F ^ { \prime }$ such that there is some $x ^ { \prime } \in$ $\left( D / U ( F ^ { \prime } ) _ { \mathbb { Z } } \right) _ { \{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} }$ projecting to $x \in ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ via the canonical map

$$
\left( D / U ( F ^ { \prime } ) _ { \mathbb { Z } } \right) _ { \{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} } \longrightarrow \left( D / U ( F ) _ { \mathbb { Z } } \right) _ { \{ \sigma _ { \alpha } ^ { F } \} } ,
$$

there is a maximal one $F _ { x }$ , i.e., $F ^ { \prime } \subset \overline { { F } } _ { x }$ .

We will call this boundary component $F _ { x }$ the boundary component associated with $x$ or say that $x$ belongs to the $F _ { x }$ -stratum.

Proof To the point $x$ there is associated, in a canonical way, a polyhedron $\sigma _ { \alpha } \subset U ( { \cal F } )$ : it is the unique polyhedron such that, via the map $\Phi$ defined above,

$$
\Phi ( x ) = z + \infty \cdot \sigma _ { \alpha }
$$

(in the notation of Chapter I).

Let $C _ { x } \subset C ( F )$ be the smallest boundary component such that $\sigma _ { \alpha } \subset \overline { { C } } _ { x }$ . This defines a rational boundary component $F _ { x }$ such that

$$
F \subset \overline { { F } } _ { x } , C _ { x } = C ( F _ { x } ) ;
$$

see Subsection 4.4. It is immediate that there exists a point in $\left( D / U ( F _ { x } ) _ { \mathbb { Z } } \right) _ { \{ \sigma _ { \alpha } ^ { F _ { x } } \} }$ projecting to $x$ via the canonical map

$$
( D / U ( F _ { x } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { x } } \} } \longrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } .
$$

This argument also shows that $F _ { x }$ is the maximal element with the required properties.

# 6 Proof of the Main Theorem

# 6.1

Let $\mathcal { G }$ be a connected semi-simple algebraic group defined over $\mathbb { Q }$ such that $D = \mathcal { G } ( \mathbb { R } ) ^ { o } / K$ is a bounded symmetric domain. Let $D ^ { * }$ be the union of $D$ and its rational boundary components. In Chapter $\mathrm { I I }$ , Subsection 4.1, we defined Siegel sets ${ \mathfrak { S } } _ { \omega } \subset D$ , associated to a minimal $\mathbb { Q }$ -parabolic subgroup $\mathcal { P } \subset \mathcal { G }$ and a relatively compact subset $\omega \subset \mathcal { P } ( \mathbb { R } ) ^ { o }$ . Our first goal is to analyze the “Satake topology” on $D ^ { * }$ , introduced by Satake (see Baily and Borel [1], §4.8), using Siegel sets.

The Satake topology is a topology on $D ^ { * }$ which is different from the topology induced via the Harish-Chandra embedding from the vector space topology on ${ \mathfrak { p } } _ { + }$ . To define it, take any arithmetic subgroup $\Gamma \subset { \mathcal { G } } ( \mathbb { Q } )$ and choose any fundamental set for $\Gamma$ :

$$
\Omega = C \cdot \mathfrak { S } _ { \omega } \ ,
$$

where $C \subset { \mathcal { G } } ( \mathbb { Q } )$ is a finite subset and where ${ \mathfrak { S } } _ { \omega }$ is a Siegel set with respect to a minimal $\mathbb { Q }$ -parabolic. A fundamental system of neighborhoods of $x \in D ^ { * }$ is, by definition, given by all subsets $U \subset D ^ { * }$ such that

$$
\Gamma _ { x } \cdot U = U , { \mathrm { w h e r e } } \Gamma _ { x } = \{ \gamma \in \Gamma | \gamma \cdot x = x \}
$$

and such that $\gamma \cdot U \cap { \overline { { \Omega } } }$ is a neighborhood of $\gamma \cdot x$ in $\overline { { \Omega } }$ (for the topology on $\overline { { \Omega } }$ induced from $\overline { { D } } \subset { \mathfrak { p } } _ { + } .$ ), whenever $\gamma \cdot x \in { \overline { { \Omega } } }$ .

The topology is characterized by the following theorem.

Theorem 6.1 The Satake topology is the unique topology on $D ^ { * }$ having the following properties:

(i) it induces the natural topology on $D$ and on the closure $\overline { { \mathfrak { S } } } _ { \omega }$ of any Siegel set ${ \mathfrak { S } } _ { \omega }$ ;

(ii) the group ${ \mathcal { G } } ( \mathbb { Q } )$ acts continuously on $D ^ { * }$ ;

(iii) if $x , x ^ { \prime } \in D ^ { * }$ are not equivalent with respect to the action of an arithmetic group $\Gamma \subset { \mathcal { G } } ( \mathbb { Q } )$ , then there exist neighborhoods $U$ of $x$ and $U ^ { \prime }$ of $x ^ { \prime }$ such that $\Gamma \cdot U \cap U ^ { \prime } = \emptyset$ ;

(iv) let $\Gamma \subset { \mathcal { G } } ( \mathbb { Q } )$ be an arithmetic group. For every $x \in D ^ { * }$ , there exists $a$ fundamental set of neighborhoods $\{ U \}$ of $x$ such that

$$
{ \begin{array} { r } { \gamma \cdot U = U { \mathrm { ~ i f ~ } } \gamma \cdot x = x , } \\ { \gamma \cdot U \cap U = \emptyset { \mathrm { ~ i f ~ } } \gamma \cdot x \neq x . } \end{array} }
$$

The Baily–Borel compactification $( D / \Gamma ) ^ { * }$ of $D / \Gamma$ is the quotient

$$
\left( D / \Gamma \right) ^ { * } = D ^ { * } / \Gamma ,
$$

equipped with the quotient topology. Baily and Borel [1] proved:

Theorem 6.2 The compactification $( D / \Gamma ) ^ { * }$ is a compact Hausdorff space containing $D / \Gamma$ as an open dense subset. The compactification $( D / \Gamma ) ^ { * }$ is a finite union of subspaces of the form

$$
F / \Gamma _ { F } ,
$$

where $F$ is a rational boundary component.

The closure of $F / \Gamma _ { F }$ in $( D / \Gamma ) ^ { * }$ is the union of $F / \Gamma _ { F }$ and of subspaces $F ^ { \prime } / \Gamma _ { F ^ { \prime } }$ , of strictly smaller dimension.

We wish to describe explicitly the Satake topology in terms of the coordinates on $D$ given by its presentation as a Siegel domain, and, in particular, we want to show that a fundamental system of open sets can be given using the concept of rational core of a cone (see Chapter II, Subsection 5.1). The result is as follows.

Theorem 6.3 Let $F$ be a rational boundary component of D and let $x \in F$ . Let

$C _ { 0 } ( F ) \subset C ( F )$ be a rational core. Let⎦ $U \subset D$ be an open set. Then

$$
\left[ \begin{array} { c } { \mathrm { t h e r e ~ e x i s t s ~ a } } \\ { \mathrm { n e i g h b o r h o o d } V \ o f x \in D ^ { * } } \\ { \mathrm { i n ~ t h e ~ S a t a k e ~ t o p o l o g y } } \\ { \mathrm { s u c h ~ t h a t } U \supset V \cap D } \end{array} \right] \Longleftrightarrow \left[ \begin{array} { c } { \mathrm { t h e r e ~ e x i s t s ~ a } } \\ { \mathrm { n e i g h b o r h o o d } E \ { \mathrm { o f } } x \in F } \\ { \mathrm { a n d } \ 1 \leq t < \infty , \ \mathrm { s u c h ~ t h a t } } \\ { U \supset \pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( t C _ { 0 } ) } \end{array} \right] .
$$

Proof Fix an arithmetic group $\Gamma \subset { \mathcal { G } } ( \mathbb { Q } )$ , and let $\Gamma _ { x } = \{ \gamma \in \Gamma \mid \gamma x = x \}$ . On the LHS, we can assume $V$ is $\Gamma _ { x }$ -invariant; on the RHS, we can assume $C _ { 0 }$ is $\overline { { \Gamma } } _ { F }$ -invariant and $E$ is $\Gamma _ { x }$ -invariant. Thus we are comparing $\Gamma _ { x }$ -invariant open subsets of $D$ , namely $V \cap D$ and $\pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( C _ { 0 } )$ , so we may as well assume $U$ is $\Gamma _ { x }$ -invariant. Similarly, if $\mathcal { G } = \mathcal { G } _ { 1 } \times \mathcal { G } _ { 2 }$ over $\mathbb { Q }$ , and this corresponds to $D = D _ { 1 } \times D _ { 2 }$ , then the Satake topology on $D$ is the product of the Satake topology on $D _ { 1 }$ and on $D _ { 2 }$ ; hence, both the sets $V \cap D$ and the sets

$$
\pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( C _ { 0 } )
$$

can be assumed to be products. Therefore we may as well assume $U$ is a product too, and thus the result for $D _ { 1 }$ and $D _ { 2 }$ implies it for $D$ . So we may assume $\mathcal { G }$ is $\mathbb { Q }$ -simple. We start on the left:

Here we mean any Siegel set ${ \mathfrak { S } } _ { \omega }$ with respect to any minimal $\mathbb { Q }$ -parabolic $\mathcal { P }$ This is straightforward.

Next we need a lemma about when $x \in \overline { { \mathfrak { S } } } _ { \omega }$ .

Lemma 6.4 If ${ \mathfrak { S } } _ { \omega }$ is a Siegel set with respect to $\mathcal { P }$ , and $F$ is a boundary component of $D$ , then

$$
\overline { { \mathfrak { S } } } _ { \omega } \cap F \neq \emptyset \Longleftrightarrow \mathcal { P } \subset \mathcal { N } ( F ) \mathrm { ~ a n d ~ } F \mathrm { ~ i s ~ r a t i o n a l ~ } .
$$

Proof Let ${ \mathcal { A } } \subset { \mathcal { P } }$ be a maximal $\mathbb { Q }$ -split torus, $A = { \mathcal { A } } ( \mathbb { R } ) ^ { o }$ and $A ^ { + }$ the positive piece, see Chapter $\mathrm { I I }$ , Definition 4.1. Let $K$ be a maximal compact subgroup such that Lie $K \perp$ Lie A, and let $p$ be fixed by $K$ . Then it suffices to show

$$
\overline { { A ^ { + } p } } \cap { \cal F } \not = \emptyset \Longleftrightarrow \mathcal { P } \subset \mathcal { N } ( { \cal F } ) \mathrm { , ~ } { \cal F } \mathrm { ~ r a t i o n a l \ : , }
$$

because, if $\omega \subset { \mathcal { P } } ( \mathbb { R } )$ is compact with $\overline { { \mathfrak { S } } } _ { \omega } = \omega \cdot \overline { { A ^ { + } p } }$ , then $\omega$ leaves fixed every $F$ such that ${ \mathcal { P } } \subset { \mathcal { N } } ( F )$ . Let $s = \dim A$ , and let

$$
{ \scriptstyle { \frac { 1 } { 2 } } } ( \beta _ { 1 } - \beta _ { 2 } ) , { \scriptstyle { \frac { 1 } { 2 } } } ( \beta _ { 2 } - \beta _ { 3 } ) , \ldots , { \scriptstyle { \frac { 1 } { 2 } } } ( \beta _ { s - 1 } - \beta _ { s } ) , \beta _ { s } , \mathrm { o r } { \ \frac { 1 } { 2 } } \beta _ { s }
$$

be the simple positive roots (ordering defined by $\mathcal { P }$ ) as usual. We constructed

in Subsection 3.5 symmetric holomorphic maps

$$
\begin{array} { c c c } { { \mathfrak { H } ^ { s } } } & { { \xrightarrow { f _ { 1 } } } } & { { D } } \\ { { \bigcap } } & { { } } & { { \bigcap } } \\ { { ( \mathbb { P } ^ { 1 } ) ^ { s } } } & { { \xrightarrow { f _ { 2 } } } } & { { \check { D } } } \end{array}
$$

associated to

$$
\varphi : U ^ { 1 } \times \mathrm { S L } ( 2 , \mathbb { R } ) ^ { s } \longrightarrow G
$$

with $\varphi ( 1 , \mathrm { d i a g . \ m a t r i c e s } ) = A$ and with

$$
x = \varphi \left( 1 , \left( \begin{array} { c c } { { t _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { t _ { 1 } ^ { - 1 } } } \end{array} \right) , . . . , \left( \begin{array} { c c } { { t _ { s } } } & { { 0 } } \\ { { 0 } } & { { t _ { s } ^ { - 1 } } } \end{array} \right) \right) \in A \ ,
$$

such that $\beta _ { i } ( x ) = t _ { i } ^ { 2 }$ . Then $A ^ { + }$ is the image of elements

$$
\left( \begin{array} { c c } { { t _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { t _ { 1 } ^ { - 1 } } } \end{array} \right) , \ldots , \left( \begin{array} { c c } { { t _ { s } } } & { { 0 } } \\ { { 0 } } & { { t _ { s } ^ { - 1 } } } \end{array} \right) \ ,
$$

where $t _ { 1 } \geq t _ { 2 } \geq \dots \geq t _ { s } \geq 1$ . Then

$$
{ \overline { { A ^ { + } p } } } = f _ { 2 } \left( \left\{ \left( { \mathrm { i } x } _ { 1 } , \ldots , { \mathrm { i } x } _ { s } \right) \vert \infty \geq x _ { 1 } \geq \cdots \geq x _ { s } \geq 1 \right\} \right) ,
$$

i.e., $\overline { { A ^ { + } p } }$ meets the boundary components   $F _ { 1 } , \ldots , F _ { s }$ , where

$$
f _ { 2 } ( \infty , \mathbf { i } , \ldots , \mathbf { i } ) \in F _ { 1 } , f _ { 2 } ( \infty , \infty , \mathbf { i } , \ldots , \mathbf { i } ) \in F _ { 2 } , \ldots , f _ { 2 } ( \infty , \infty , \ldots , \infty ) \in F _ { s } .
$$

Now, if

$$
w _ { i } ( t ) = \varphi ( 1 , \underbrace { \left( \begin{array} { c c } { t } & { 0 } \\ { 0 } & { t ^ { - 1 } } \end{array} \right) , \ldots , \left( \begin{array} { c c } { t } & { 0 } \\ { 0 } & { t ^ { - 1 } } \end{array} \right) } _ { i \mathrm { ~ f a c t o r s } } , I , \ldots , I ) ,
$$

then all but the i’th simple root vanishes on $w _ { i }$ ; hence, $\mathcal { P } = \mathcal { P } ( w _ { 1 } ^ { - 1 } ) \cap \cdots \cap$ $\mathcal { P } ( w _ { r } ^ { - 1 } )$ expresses $\mathcal { P }$ as an intersection of maximal - $\mathbb { Q }$ -parabolics, and it is immediate that $\mathcal { P } _ { i } = \mathcal { N } ( F _ { i } )$ . □

Next, write out the algebraic connected component of ${ \mathcal { N } } ( F )$ as

$$
\widetilde { \mathcal { G } } _ { h } ( F ) \cdot \mathcal { G } _ { \ell } ( F ) \cdot \mathcal { W } ( F ) \ ,
$$

where all these factors are defined over  $\mathbb { Q }$ , ${ \widetilde { \mathcal { G } } } _ { h } ( F ) ( \mathbb { R } ) ^ { o } = G _ { h } ( F ) \cdot M ( F )$ in the notation of Section 4, and $\mathcal { W }$ is the unipotent radical. Then a minimal $\mathbb { Q }$ - parabolic ${ \mathcal { P } } \subset { \mathcal { N } } ( F )$ is equal to

$$
\mathcal { P } = \widetilde { \mathcal { P } _ { h } } \cdot \mathcal { P } _ { \ell } \cdot \mathcal { W } ,
$$

where $\widetilde { \mathcal { P } } _ { h } \subset \widetilde { \mathcal { G } } _ { h }$ and $\mathcal { P } _ { \ell } \subset \mathcal { G } _ { \ell }$ are minimal $\mathbb { Q }$ -parabolics. Then, for any basepoint $o \in D$ , a cofinal collection of Siegel sets for $\mathcal { P }$ is given as

$$
\mathfrak { S } _ { \omega } = \left( \omega _ { W } \cdot \omega _ { h } \cdot \omega _ { \ell } \right) \cdot A ^ { + } \cdot o \ ,
$$

where

$$
\omega _ { h } \subset \widetilde { P } _ { h } = \widetilde { \mathcal { P } } _ { h } ( \mathbb { R } ) ^ { o } \ , \ \omega _ { \ell } \subset P _ { \ell } = \mathcal { P } _ { \ell } ( \mathbb { R } ) ^ { o } \ , \ \omega _ { W } \subset W = \mathcal { W } ( \mathbb { R } )
$$

are compact, and where ${ \mathcal { A } } \subset { \mathcal { P } }$ is a maximal $\mathbb { Q }$ -split torus conjugate to the original maximal split torus in $\mathcal { P }$ , with Lie $\mathcal { A } \perp \mathsf { S t a b } \left( o \right)$ , and where

$$
\begin{array} { r } { A ^ { + } = \left\{ g \in A = \mathcal { A } ( \mathbb { R } ) ^ { o } \mid \begin{array} { l } { \beta ( g ) \geq 1 \mathrm { ~ f o r ~ a l l ~ p o s i t i v e ~ r o o t s ~ } \beta \mathrm { ~ o f ~ } A } \\ { \mathrm { ~ i . e . , r o o t s ~ o c c u r r i n g ~ i n ~ L i e ~ } \mathcal { P } } \end{array} \right\} . } \end{array}
$$

Note that $A = A _ { h } \cdot A _ { \ell }$ , where $A _ { h } \subset \widetilde { P } _ { h }$ and $A _ { \ell } \subset P _ { \ell }$ are conjugates of the maximal $\mathbb { Q }$ -split tori in $\widetilde { \mathcal P _ { h } }$ and $\mathcal { P } _ { \ell }$ . Moreover, the root system of $A$ (written multiplicatively, i.e., as a subset $\Phi \subset { \mathrm { H o m } } ( A , \mathbb { R } _ { > 0 } ) )$ is given by

$$
\begin{array} { r l r } { \beta _ { i } ^ { \pm 1 } , \ } & { { } \beta _ { i } ^ { \pm 1 / 2 } \beta _ { j } ^ { \pm 1 / 2 } } & { ( \mathrm { p l u s } \mathrm { p o s s i b l y } \beta _ { i } ^ { \pm 1 / 2 } ) , } \\ { 1 \le i \le s } & { { } 1 \le i < j \le s } & { 1 \le i \le s } \end{array}
$$

with simple positive roots

$$
\beta _ { 1 } ^ { 1 / 2 } \beta _ { 2 } ^ { - 1 / 2 } , \beta _ { 2 } ^ { 1 / 2 } \beta _ { 3 } ^ { - 1 / 2 } , \ldots , \beta _ { s - 1 } ^ { 1 / 2 } \beta _ { s } ^ { - 1 / 2 } , \mathrm { a n d } \beta _ { s } \mathrm { o r } \beta _ { s } ^ { 1 / 2 } ,
$$

and with

$$
\begin{array} { l } { A _ { h } = \left\{ g \in A \ | \ \beta _ { 1 } ( g ) = \cdots = \beta _ { u } ( g ) = 1 \right\} } \\ { A _ { \ell } = \left\{ g \in A \ | \ \beta _ { u + 1 } ( g ) = \cdots = \beta _ { s } ( g ) = 1 \right\} . } \end{array}
$$

Our next step is the following lemma.

Lemma 6.5 Assume $\omega _ { \ell }$ is large enough so that $x \in \mathrm { I n t } _ { F } ( \omega _ { \ell } \cdot \pi _ { F } ( o ) )$ . Let $U _ { n } \subset$ $G _ { h } ( F )$ be sets such that $U _ { n } \cdot \pi _ { F } ( o )$ is a fundamental system of neighborhoods of $x \in F$ , for $n = 1 , 2 , \ldots$ Then the intersection with ${ \mathfrak { S } } _ { \omega }$ of a fundamental system of neighborhoods of $x \in \overline { { \mathfrak { S } } } _ { \omega }$ is given by

$$
S _ { n , t } = \omega _ { W } \cdot U _ { n } \cdot \omega _ { \ell } \cdot A _ { \ell , t } \cdot o \ ,
$$

where

$$
A _ { \ell , t } = \left\{ x \in A _ { \ell } \vert \beta _ { 1 } ( x ) \ge \beta _ { 2 } ( x ) \ge \cdots \ge \beta _ { u } ( x ) \ge t \right\} .
$$

Proof Recall from Section 3 that we can map $\mathrm { S L } ( 2 , \mathbb { R } ) ^ { u } \longrightarrow G _ { \cdot }$ , taking diagonal matrices $\delta = \left( \left( \begin{array} { c c } { { t _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { t _ { 1 } ^ { - 1 } } } \end{array} \right) , \ldots \right)$ to elements $x \in A _ { \ell }$ with $\beta _ { i } ( x ) = t _ { i } ^ { 2 }$ , and from this obtain a homomorphism

$$
\varphi : G _ { h } ( F ) \times { \mathrm { S L } } ( 2 , \mathbb { R } ) ^ { u } \longrightarrow G
$$

plus a symmetric holomorphic map for $\varphi$ :

$$
\begin{array} { c c c } { { F \times \mathfrak { H } ^ { u } } } & { { \stackrel { f _ { 1 } } { \longrightarrow } } } & { { D } } \\ { { \bigcap } } & { { \bigcap } } & { { \bigcap } } \\ { { \check { F } \times ( \mathbb { P } ^ { 1 } ) ^ { u } } } & { { \stackrel { f _ { 2 } } { \longrightarrow } } } & { { \check { D } . } } \end{array}
$$

Consider the map

$$
g : \omega _ { W } \times \omega _ { \ell } \times \overline { { { F } } } \times A _ { \ell , 1 } ^ { \prime } \longrightarrow \overline { { { D } } } ,
$$

where

$$
A _ { \ell , t } ^ { \prime } = \{ \underline { { t } } = ( t _ { 1 } , \dots , t _ { u } ) | \infty \ge t _ { 1 } \ge t _ { 2 } \ge \cdots \ge t _ { u } \ge t ^ { 1 / 2 } \} ,
$$

given by

$$
g ( u , \nu , a , \mathrm { i } \underline { { t } } ) = u \cdot \nu \cdot f _ { 2 } ( a , \mathrm { i } \underline { { t } } ) .
$$

Note that $\operatorname { I m } g$ is compact, hence closed, and that ${ \mathfrak { S } } _ { \omega } \subset { \mathrm { I m } } g$ . Therefore, $\overline { { \mathfrak { S } } } _ { \omega } \subset \mathrm { I m } g$ , which is why we have introduced $g$ . On the other hand, $f _ { 2 } ^ { - 1 } ( x ) =$ $\{ ( x , \infty , \ldots , \infty ) \}$ , and hence

$$
g ^ { - 1 } ( x ) = \omega _ { W } \times \omega _ { \ell } \times \{ x \} \times \{ ( \infty , \ldots , \infty ) \} .
$$

Since $\omega _ { W }$ and $\omega _ { \ell }$ are compact, any open subset of $\omega _ { W } \times \omega _ { \ell } \times \overline { { F } } \times A _ { \ell , 1 } ^ { \prime }$ containing $g ^ { - 1 } ( x )$ contains

$$
\omega _ { W } \times \omega _ { \ell } \times \{ U _ { n } \cdot \pi _ { F } ( o ) \} \times A _ { \ell , t } ^ { \prime }
$$

for some $n$ and $t$ ; and, since $g$ is a proper map, the images $S _ { n , t }$ by $g$ of these sets are a fundamental system of neighborhoods in $\operatorname { I m } g$ of $x$ . But, for $n$ large, these are subsets of $\overline { { \mathfrak { S } } } _ { \omega }$ , hence the lemma follows.

Corollary 6.6 Let $U \subset D$ be an open subset. Then there exists an open neighborhood $V$ of $x \in D ^ { * }$ in the Satake topology with $U \supset V \cap D$ if and only if, for all minimal $\mathbb { Q }$ -parabolics $\mathcal { P } _ { \ell } \subset \mathcal { G } _ { \ell }$ and all compact subsets $\omega _ { W } \subset W$ and $\omega _ { \ell } \subset P _ { \ell } ,$

$$
U \supset S _ { n , t }
$$

for some $n \geq 1 , t \geq 1$ , where $S _ { n , t }$ are defined as in Lemma 6.5 above.

We now use the product representation

$$
D \cong F \times C ( F ) \times W ( F )
$$

introduced in Subsection 4.3. In this representation

$$
S _ { n , t } = ( U _ { n } \cdot \pi _ { F } ( o ) ) \times ( \omega _ { \ell } \cdot A _ { \ell , t } \cdot \Omega _ { F } ) \times \omega _ { W } ;
$$

here $\Omega _ { F }$ is the basepoint of $C ( F )$ . If $E _ { n } = U _ { n } \cdot \pi _ { F } ( o )$ , then, by definition, the

$E _ { n }$ are a fundamental set of neighborhoods of $x$ in $F$ . Now $U$ is $\Gamma _ { x }$ -invariant, and hence $U \supset S _ { n , t }$ implies

$$
U \supset E _ { n } \times ( \overline { { \Gamma } } _ { F } \cdot \omega _ { \ell } \cdot A _ { \ell , t } \cdot \Omega _ { F } ) \times ( \Gamma \cap W ) \cdot \omega _ { W } .
$$

If $\omega _ { W }$ is large enough, $( \Gamma \cap W ) \cdot \omega _ { W } = W$ , so there is no condition on the third factor. Moreover, if we take a finite union of the sets in the middle factor, one for each $\overline { { \Gamma } } _ { F }$ -conjugacy class of minimal $\mathbb { Q }$ -parabolics $\mathcal { P } _ { \ell } \subset \mathcal { G } _ { \ell }$ , while taking the $\omega _ { \ell }$ large enough, then

$$
\bigcup _ { i } \overline { { \Gamma } } _ { F } \cdot \boldsymbol { \omega } _ { \ell } ^ { ( i ) } \cdot \boldsymbol { A } _ { \ell } ^ { ( i ) } \cdot \boldsymbol { \Omega } _ { F } = C ( F ) ,
$$

while

$$
\bigcup _ { i } \overline { { \Gamma } } _ { F } \cdot \omega _ { \ell } ^ { ( i ) } \cdot A _ { \ell , t } ^ { ( i ) } \cdot \Omega _ { F } = t \cdot C _ { 0 } ( F ) ,
$$

where $C _ { 0 } ( F )$ lies between two rational cores of $C ( F )$ . Thus the condition on $U$ is equivalent to

$$
U \supset \pi _ { F } ^ { - 1 } ( E _ { n } ) \cap \Phi _ { F } ^ { - 1 } ( t C _ { 0 } ( F ) ) { \mathrm { ~ f o r ~ s o m e ~ } } n \geq 1 , t \geq 1 \ .
$$

This concludes the proof of Theorem 6.3.

In fact, if one adjoins to $\pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( t C _ { 0 } ( F ) )$ a suitable set of elements of the rational boundary components $F ^ { \prime }$ with ${ \overline { { F ^ { \prime } } } } \supset F$ , then one can prove that these extended sets, as $F , E$ , and $t$ vary $E$ is open and relatively compact in $F$ ), form a basis of open sets for the Satake topology on $D ^ { * }$ . However, we do not need this additional fact.

Combining the above proof with the results of Chapter II, Subsection 4.3, we find:

Corollary 6.7 Every Siegel set ${ \mathfrak { S } } _ { \omega } \subset D$ is covered by a finite number of sets of the form

$$
E \times ( C _ { 0 } \cap \sigma _ { \alpha } ^ { F } ) \times \omega _ { W } \subset F \times C ( F ) \times W ( F ) \cong D ,
$$

where $E \subset F$ and $\omega _ { W } \subset W ( F )$ are compact, $C _ { 0 } \subset C ( F )$ is a rational core, and $\sigma _ { \alpha } ^ { F }$ is one of the polyhedra in our decomposition of $C ( F )$

# 6.2

The next step is to define a map

$$
f \colon \widetilde { { \cal D } / \Gamma } = \bigsqcup _ { F } ( { \cal D } / { \cal U } ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow ( { \cal D } / \Gamma ) ^ { * } \ .
$$

Let $x \in ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ and let $F _ { x }$ nent; hence there exists a point $x ^ { \prime } \in ( D / U ( F _ { x } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { x } } \} }$ projecting to $x$ via the canonical map

$$
( D / U ( F _ { x } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { x } } \} } \longrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } .
$$

We then define the image via $f$ of $x$ as the image of $x ^ { \prime }$ via the succession of maps

$$
( D / U ( F _ { x } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} } { \xrightarrow { \pi _ { F _ { x } } } } F _ { x } \subset D ^ { * } \longrightarrow ( D / \Gamma ) ^ { * } .
$$

The following facts are immediate.=

(1) The definition of $f ( x )$ is independent of the choice of $x ^ { \prime }$ .   
(2) The restriction $f | _ { D }$ is just the natural projection from $D$ to $D / \Gamma \subset ( D / \Gamma ) ^ { * }$ .   
(3) Two points in $\widetilde { D / \Gamma }$ that are equivalent under the equivalence relation introduced in Section 5 have the same image in $( D / \Gamma ) ^ { * }$ . Indeed, $F _ { \gamma \cdot x } = \gamma \cdot F _ { x }$ , for all $\gamma \in \Gamma$ .

(4) f |(D/U(F)Z){σα} factors as

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} } { \stackrel { f _ { F } } { \longrightarrow } } D ^ { * } / U ( F ) _ { \mathbb { Z } } \longrightarrow ( D / \Gamma ) ^ { * } .
$$

Proposition 6.8 If $( D / \Gamma ) ^ { * }$ and $D ^ { * } / U ( F ) _ { \mathbb { Z } }$ are given the Satake topology, the map

$$
f : \widetilde { D / \Gamma } \longrightarrow ( D / \Gamma ) ^ { * }
$$

and the maps fF through which it factors are continuous.

Proof It is clearly sufficient to show that $f _ { F }$ is continuous. We use the following elementary lemma.

Lemma 6.9 Let $\overline { { X } }$ and $\overline { { Y } }$ be two topological spaces which are second countable, $\overline { { Y } }$ also being a $T _ { 3 }$ -space, and let $X \subset { \overline { { X } } }$ , resp. $Y \subset { \overline { { Y } } } $ , be an open and dense, resp. open, subset. Let

$$
f : \overline { { { X } } } \longrightarrow \overline { { { Y } } }
$$

be a map such that $f ( X ) \subset Y$ . Assume that, for every $x \in { \overline { { X } } }$ and $y = f ( x ) \in { \overline { { Y } } }$ , and for any neighborhood $V$ of y, $f ^ { - 1 } ( V \cap Y )$ contains $a$ set of the form $U \cap X$ , where $U$ is a neighborhood of $x .$ . Then $f$ is continuous.

Proof We have to show that if

$$
x _ { 1 } , x _ { 2 } , \ldots \longrightarrow x ,
$$

then

$$
y _ { 1 } = f ( x _ { 1 } ) , y _ { 2 } = f ( x _ { 2 } ) , \ldots \longrightarrow y = f ( x ) \ .
$$

Suppose first that $x _ { i } \in X \subset { \overline { { X } } }$ . Let $V$ be any neighborhood of $y$ and choose a neighborhood $U$ of $x$ as in the hypotheses of the lemma. Then, for large enough $i$ , we have

$$
x _ { i } \in U \cap X .
$$

Hence we get $y _ { i } \in f ( U \cap X ) \subset V$ for $i \gg 0$ , i.e., $y _ { i } \longrightarrow y$ .

Now consider the general case. Since $X \subset { \overline { { X } } }$ is dense, we may find convergent sequences

$$
x _ { i 1 } , x _ { i 2 } , \ldots \longrightarrow x _ { i } \mathrm { w i t h } x _ { i j } \in X \ .
$$

Let $V$ be an arbitrary open neighborhood of $y$ and let $V _ { 1 }$ be a neighborhood of $y$ such that

$$
V _ { 1 } \subset \overline { { { V } } } _ { 1 } \subset V \ .
$$

(We use the fact that $\overline { { Y } }$ is a $T _ { 3 }$ -space.) Denote by $U$ , resp. $U _ { 1 }$ , the neighborhoods of $x$ whose existence is guaranteed by hypothesis. Then, for $i \gg 0$ , we have $x _ { i } \in U _ { 1 }$ . Since $U _ { 1 }$ is a neighborhood of $x _ { i }$ for $i \gg 0$ , we have

$$
x _ { i j } \in U _ { 1 } { \mathrm { ~ f o r ~ } } i \gg 0 , j > J ( i ) ~ .
$$

This shows that $y _ { i j } \in V _ { 1 }$ for $i \gg 0$ , $j > J ( i )$ . Since, by the first part of the proof, the sequence $y _ { i j }$ converges to $y _ { i }$ we conclude that $y _ { i } \in \overline { { V } } _ { 1 } \subset V$ for $i \gg 0$ . This finishes the proof.

To verify the assumptions of the lemma for $f _ { F }$ , we use induction on codim $F$ . Therefore we may assume $f _ { F ^ { \prime } }$ continuous for all $F ^ { \prime }$ with ${ \overline { { F ^ { \prime } } } } \supset F$ .

Then to check $f _ { F }$ itself is continuous, we need only verify the assumption for $x$ in the $F$ -stratum of $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ Let $y = f _ { F } ( x ) \in F$ Then a fundamental system of neighborhoods of $y$ in the Satake topology, intersected with $D$ , is given, according to Theorem 6.3, by the sets $\pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( C _ { 0 } )$ , where $E \subset F$ is a neighborhood of $x$ and where $C _ { 0 }$ is a rational core of $C ( F )$ . But $\pi _ { F }$ extends to a continuous map

$$
\overline { { { \pi } } } _ { F } : ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \to F ,
$$

and $\Phi _ { F }$ extends to a continuous map

$$
\begin{array} { r } { \overline { { \Phi } } _ { F } : ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow C ( F ) ^ { \prime \prime } . } \end{array}
$$

(Recall that $C ( F ) ^ { \prime \prime }$ is the interior of the closure of $C ( F )$ in $U ( F ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ Moreover, $C _ { 0 }$ contains some cylindrical set $a + C ( F ) \subset C ( F )$ , and

$$
( a + C ( F ) ) ^ { \prime \prime } : = \mathrm { i n t e r i o r ~ o f ~ c l o s u r e ~ o f } \ : a + C ( F ) \mathrm { i n } U ( F ) _ { \{ \sigma _ { \alpha } ^ { F } \} }
$$

is an open subset of $C ( F ) ^ { \prime \prime }$ containing all points of  $U ( F ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ in the $F$ -stratum, i.e., points $x + \infty \cdot \sigma _ { \alpha } ^ { F }$ , where $\sigma _ { \alpha } ^ { F }$ meets $C ( F )$ (or $\sigma _ { \alpha } ^ { F } \not \subset \partial { \cal C } ( F ) )$ .Therefore $\pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( C _ { 0 } )$ (inverse image in ${ \cal D } / { U ( F ) _ { \mathbb { Z } } } )$ contains

$$
D / U ( F ) _ { \mathbb { Z } } \cap \underbrace { \overline { { \pi } } _ { F } ^ { - 1 } ( E ) \cap \overline { { \Phi } } _ { F } ^ { - 1 } \big ( ( a + C ( F ) ) ^ { \prime \prime } \big ) } _ { \mathrm { i n v e r s e ~ i m a g e ~ i n ~ } ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } } ,
$$

and the latter terms are neighborhoods of $x$ in $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$

# 6.3

We now show that the equivalence relation $\Lambda$ is closed. Since any pair $( y , z )$ of equivalent points in $\widetilde { D / \Gamma }$ is a limit of equivalent points $( y _ { i } , z _ { i } )$ , where

$$
\begin{array} { l } { { \displaystyle y _ { i } \in ( D / U ( F _ { 1 } ) _ { \mathbb { Z } } ) \subset \widetilde { D / \Gamma } , } } \\ { { \displaystyle z _ { i } \in ( D / U ( F _ { 2 } ) _ { \mathbb { Z } } ) \subset \widetilde { D / \Gamma } , } } \end{array}
$$

it suffices to show that, for any two sequences $y _ { i } , z _ { i } \in D$ , where $y _ { i } = \gamma _ { i } z _ { i }$ with $\gamma _ { i } \in \Gamma$ , such that

$$
\begin{array} { r l } & { y _ { i } \bmod U ( F _ { 1 } ) _ { \mathbb { Z } } \longrightarrow \bar { y } \in ( D / U ( F _ { 1 } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { 1 } } \} } , } \\ & { } \\ & { z _ { i } \bmod U ( F _ { 2 } ) _ { \mathbb { Z } } \longrightarrow \bar { z } \in ( D / U ( F _ { 2 } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { 2 } } \} } , } \end{array}
$$

it follows that $( { \bar { y } } , { \bar { z } } ) \in \Lambda$ . But, by Proposition 6.8, the images of $\bar { y }$ and $\overline { z }$ in $( D / \Gamma ) ^ { * }$ are equal, and hence lie in the same stratum $F / \Gamma _ { F }$ of $( D / \Gamma ) ^ { * }$ . By the definition of $f$ , it follows that $\overline { { \delta _ { 1 } F } } \supset F _ { 1 }$ , $\overline { { \delta _ { 2 } F } } \supset F _ { 2 }$ , for some $\delta _ { 1 } , \delta _ { 2 } \in \Gamma$ , and where $\bar { y }$ lies in the $\delta _ { 1 } F$ -stratum, and $\overline { z }$ lies in the $\delta _ { 2 } F$ -stratum. Replacing $y _ { i } , \bar { y }$ by $\delta _ { 1 } ^ { - 1 } y _ { i }$ , $\delta _ { 1 } ^ { - 1 } { \overline { { y } } }$ and $z _ { i } , { \bar { z } }$ by $\delta _ { 2 } ^ { - 1 } z _ { i }$ , $\delta _ { 2 } ^ { - 1 } \overline { { z } } .$ , we can assume $\overline { { F } } \supset F _ { 1 }$ and $\overline { { F } } \supset F _ { 2 }$ .

Next, lift $\overline { { y } } , \overline { { z } }$ to points $y ^ { * }$ , $z ^ { * } \in ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ Since

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow ( D / U ( F _ { i } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { i } } \} }
$$

is obtained by dividing by $U ( F _ { i } ) _ { \mathbb { Z } }$ plus an open immersion, it follows that

$$
\begin{array} { r } { y ^ { * } = \underset { i \longrightarrow \infty } { \operatorname* { l i m } } \lambda _ { i } \cdot y _ { i } \mathrm { , } \lambda _ { i } \in U ( F _ { 1 } ) _ { \mathbb { Z } } \mathrm { , } } \\ { z ^ { * } = \underset { i \longrightarrow \infty } { \operatorname* { l i m } } \mu _ { i } \cdot z _ { i } \mathrm { , } \mu _ { i } \in U ( F _ { 2 } ) _ { \mathbb { Z } } \mathrm { . } } \end{array}
$$

So, replacing $y _ { i }$ by $\lambda _ { i } \cdot y _ { i }$ , and $z _ { i }$ by $\mu _ { i } \cdot z _ { i }$ , and $\bar { y }$ by $y ^ { * }$ , and $\overline { z }$ by $z ^ { * }$ , it suffices to prove the assertion in the special case:

$$
\begin{array} { c } { { F _ { 1 } = F _ { 2 } : \ \mathrm { c a l l \ t h i s \ j u s t } \ : F \ : ; } } \\ { { \bar { y } , \bar { z } \in F \mathrm { - s t r a t u m \ o f \ } ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } . } } \end{array}
$$

Now consider the following continuous maps:

$$
\begin{array} { l c c c l } { { ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } } } & { { \stackrel { f _ { F } } { \longrightarrow } } } & { { D ^ { * } / U ( F ) _ { \mathbb { Z } } } } & { { \longrightarrow } } & { { ( D / \Gamma ) ^ { * } } } \\ { { } } & { { } } & { { \cup } } & { { \cup } } \\ { { } } & { { F } } & { { \longrightarrow } } & { { F / \Gamma _ { F } . } } \end{array}
$$

Since $\textstyle { \overline { { y } } } , { \overline { { z } } }$ have the same image in $( D / \Gamma ) ^ { * }$ , their images in $D ^ { * } / U ( F ) _ { \mathbb { Z } }$ differ by $\gamma \in \Gamma _ { F }$ . Again, replacing $z _ { i }$ , $\bar { z }$ by $\gamma ^ { - 1 } z _ { i } , \gamma ^ { - 1 } \overline { { z } }$ , we may assume that $\bar { y }$ and $\bar { z }$ have the same image $p \in F \subset D ^ { * } / U ( F ) _ { \mathbb { Z } }$ . Let $U _ { 1 } \subset D ^ { * }$ be a neighborhood of $p$ in the Satake topology such that $\boldsymbol { \Gamma } _ { p } \boldsymbol { \cdot } \boldsymbol { U } _ { 1 } = \boldsymbol { U } _ { 1 }$ and $\gamma U _ { 1 } \cap U _ { 1 } = \emptyset$ if $\gamma \notin \Gamma _ { p }$ . Then

$$
U _ { 2 } = f _ { F } ^ { - 1 } ( U _ { 1 } / U ( F ) _ { \mathbb { Z } } )
$$

is an open subset of $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ containing $\bar { y }$ and z. Therefore $y _ { i }$ mod $U ( F ) _ { \mathbb { Z } }$ and $z _ { i }$ mod $U ( F ) _ { \mathbb { Z } }$ lie in $U _ { 2 }$ if $i \gg 0$ . In other words, the points $y _ { i } , z _ { i }$ in $D$ lie in $U _ { 1 }$ if $i \gg 0$ . Now $y _ { i } = \gamma _ { i } z _ { i }$ , for $\gamma _ { i } \in \Gamma$ , so, by the assumption on $U _ { 1 }$ , we have $\gamma _ { i } \in \Gamma _ { p }$ , hence $\gamma _ { i } \in \Gamma _ { F }$ . This reduces us to the following assertion.

Proposition 6.10 The action of $\Gamma _ { F } / U ( F ) _ { \mathbb { Z } }$ on $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ is properly discontinuous. Consequently, $\Gamma _ { F }$ -equivalence is a closed equivalence relation in $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \times ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } .$

Proof We use the double fibration:

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \xrightarrow { \pi _ { F } ^ { \prime } } D ( F ) ^ { \prime } \xrightarrow { p _ { F } } F .
$$

Recall that $U ( F ) \subset W ( F ) \subset N ( F )$ are all defined over $\mathbb { Q }$ ; hence, the quotient group by which $N ( F )$ acts on $U ( F )$ , namely the image of

$$
{ \cal N } ( { \cal F } ) \longrightarrow \mathrm { A u t } \left( U ( { \cal F } ) \right) ,
$$

is also defined over $\mathbb { Q }$ . Let $N ( F ) ^ { \prime } { = } \mathrm { K e r } \left( N ( F ) { \longrightarrow } \mathrm { A u t } \left( U ( F ) \right) \right)$ ; this is defined over $\mathbb { Q }$ . Finally, $N ( F ) ^ { \prime } / W ( F )$ is defined over $\mathbb { Q }$ and equals $G _ { h }$ up to compact factors. Therefore all the following are arithmetic, hence discrete subgroups:

$$
\begin{array} { r l } & { \Gamma _ { F } \subset N ( F ) \ , } \\ & { \Gamma _ { F } ^ { \prime } \subset N ( F ) ^ { \prime } , } \\ & { \Gamma \cap W ( F ) = W ( F ) _ { \mathbb { Z } } \subset W ( F ) \ , } \\ & { \Gamma \cap U ( F ) = U ( F ) _ { \mathbb { Z } } \subset U ( F ) \ , } \\ & { \overline { { \Gamma } } _ { F } \subset \mathrm { A u t } ( U ( F ) ) \ , } \\ & { \Gamma _ { F } ^ { \prime } / W ( F ) _ { \mathbb { Z } } \subset G _ { h } ( F ) \cdot ( \mathrm { c o m p . ~ f a c t o r s } ) \ . } \end{array}
$$

We use the following elementary lemma.

Lemma 6.11 Let $X , Y$ be two Hausdorff topological spaces acted on by groups G, resp. $H$ , and let

$$
\begin{array} { r } { \phi : G \longrightarrow H , } \\ { f : X \longrightarrow Y } \end{array}
$$

be a homomorphism and an equivariant continuous map. If $H$ acts properly discontinuously on $Y$ and $\mathrm { K e r } \phi$ acts properly discontinuously on $X$ , then $G$ acts properly discontinuously on $X$ . □

We deduce:

(2) $\Gamma _ { F } ^ { \prime } / U ( F ) _ { \mathbb { Z } }$ acts properly discontinuously on $D ( F ) ^ { \prime }$ by the lemma; hence,

(3) $\Gamma _ { F } ^ { \prime } / U ( F ) _ { \mathbb { Z } }$ acts properly discontinuously on $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} }$

Next we make use of the $\Gamma _ { F }$ -equivariant map

$$
\Phi _ { F } : ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow C ( F ) ^ { \prime \prime } \ .
$$

Since, by the method of proof of Theorem 1.4, $\overline { { \Gamma } } _ { F }$ acts properly discontinu-= ously on $C ( F ) ^ { \prime \prime }$ , the lemma plus (3) above give the proposition.

This proves that $\Lambda$ is closed. Let $\overline { { D / \Gamma } }$ be the quotient of $\widetilde { D / \Gamma }$ by the equivalence relation $\Lambda$ . The above proof shows that $\overline { { D / \Gamma } }$ is locally isomorphic at all points of the $F$ -stratum to

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } / ( \Gamma _ { F } / U ( F ) _ { \mathbb { Z } } ) \ .
$$

Since this is an analytic space modulo a properly discontinuous group action, $\overline { { D / \Gamma } }$ has an analytic structure, and the maps

$$
\pi _ { F } : ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow \overline { { D / \Gamma } }
$$

are open. This, together with the fact that the maps $f _ { F }$ are continuous, also shows that the natural map from $\overline { { D / \Gamma } }$ to $( D / \Gamma ) ^ { * }$ is continuous.

It remains to check that $\overline { { D / \Gamma } }$ is compact. Now, $D / \Gamma$ it is covered by the images of finitely many Siegel sets hence, by Corollary 6.7, is covered by the images of finitely many sets of the form

$$
S = E \times ( C _ { 0 } \cap \sigma _ { \alpha } ) \times \omega _ { W } \subset F \times C ( F ) \times W ( F ) \cong D .
$$

We claim that the closures of the images of these sets in $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ are

already compact, and hence so are the closures of their images in $\overline { { D / \Gamma } }$ . To see this, recall that, dividing by the compact group $T ( F ) _ { c }$ ,

$$
\begin{array} { r l } & { ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} } / T ( F ) _ { c } \cong C ( F ) ^ { \prime \prime } \times D ( F ) ^ { \prime } } \\ & { \qquad \cong F \times C ( F ) ^ { \prime \prime } \times V ( F ) . } \end{array}
$$

Now, $C _ { 0 } \cap \sigma _ { \alpha }$ has compact closure in $C ( F ) ^ { \prime \prime }$ , and this decomposition is related to our previous one by

$$
\begin{array} { r c l l } { { D } } & { { \cong } } & { { F \times C ( F ) \times V ( F ) \times U ( F ) } } \\ { { \downarrow } } & { { \downarrow } } & { { } } \\ { { D / U ( F ) } } & { { \cong } } & { { F \times C ( F ) \times V ( F ) } } \\ { { \bigcap } } & { { } } & { { \bigcap } } \\ { { ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } / T ( F ) _ { c } } } & { { \cong } } & { { F \times C ( F ) ^ { \prime \prime } \times V ( F ) , } } \end{array}
$$

so the closure of the image of our set $s$ in $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } / T ( F ) _ { c }$ is compact, hence the same happens in (D/U(F)Z){σF

# 7 An intrinsic form of the Main Theorem

Recall from Borel [2], §17.1, the concept of a neat subgroup $\Gamma \subset { \mathcal { G } } ( \mathbb { C } )$ : this is a subgroup consisting of elements $g$ such that, for one faithful representation,

$$
\rho : { \mathcal { G } } \longrightarrow \mathrm { G L } ( n )
$$

(and hence for all representations $\rho$ ), the group inside $\mathbb { C } ^ { * }$ generated by the eigenvalues of $\rho ( g )$ is torsion-free. Such a $\Gamma$ is itself torsion-free. But, even more, for every pair of subgroups

$$
\mathcal { H } _ { 1 } \subset \mathcal { H } _ { 2 } \subset \mathcal { G } ,
$$

with $\mathcal { H } _ { 1 }$ normal in $\mathcal { H } _ { 2 }$ , the group

$$
\Gamma \cap \mathcal { H } _ { 2 } ( \mathbb { C } ) / \Gamma \cap \mathcal { H } _ { 1 } ( \mathbb { C } )
$$

is also torsion-free.

We now return to the set-up of Sections 5 and 6: $\mathcal { G }$ is semi-simple, defined over $\mathbb { Q }$ , and $G = \mathcal { G } ( \mathbb { R } ) ^ { o }$ is the connected group of automorphisms of a bounded symmetric domain $D$ ; $\Gamma \subset { \mathcal { G } } ( \mathbb { Q } ) \subset G$ is an arithmetic subgroup. We will assume throughout this section that $\Gamma$ is also neat. Since by [2], Proposition 17.6, any $\Gamma$ has a neat subgroup $\Gamma _ { 1 } \subset \Gamma$ of finite index, this is not too restrictive. It has the effect that not only does $\Gamma$ act freely on $D$ , hence $\Gamma { \stackrel { \sim } { \longrightarrow } } \pi _ { 1 } \left( D / \Gamma \right)$ , but that also for all rational boundary components $F$ , the group $\operatorname { I m } \left( \Gamma _ { F } \longrightarrow \operatorname { A u t } \left( F \right) \right)$ acts freely on $F$ , and $\overline { { \Gamma } } _ { F }$ acts freely on $C ( F )$ , and $\Gamma _ { F } / U ( F ) _ { \mathbb { Z } }$ acts freely on $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ ; hence

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow \overline { { D / \Gamma } }
$$

is etale. ´

Borel [3] showed that the Baily–Borel compactification $( D / \Gamma ) ^ { * }$ enjoys the following property:

Every holomorphic map

$$
f : ( { \mathring { \Delta } } ) ^ { k } \times \Delta ^ { n - k } { \longrightarrow } D / \Gamma
$$

extends to a holomorphic map

$$
f ^ { * } : \Delta ^ { n } \longrightarrow ( D / \Gamma ) ^ { * } \ .
$$

Here, as usual, $\Delta$ is the unit disc, and $\mathring { \Delta } = \Delta \backslash \{ 0 \}$ . Letting $\exp : { \mathfrak { H } } \longrightarrow { \hat { \Delta } }$ be the universal covering as usual, such an $f$ lifts to an equivariant map $\tilde { f }$ and a homomorphism $\phi$ :

$$
\begin{array} { r l } & { \phi : \mathbb { Z } ^ { k } \longrightarrow \Gamma , } \\ & { \tilde { f } : \mathfrak { H } ^ { k } \times \Delta ^ { n - k } \longrightarrow D . } \end{array}
$$

Let

$$
\gamma _ { i } = \phi ( \ldots , 0 , \underbrace { 1 } _ { \mathrm { p l a c e } ~ i } , 0 , \ldots ) ,
$$

i.e., $\gamma _ { i }$ is the image under $\phi$ of the covering map $z \longmapsto z + 1$ in the $i ^ { * }$ ’th factor ${ \mathfrak H }$ .

Now, $f$ will not in general extend to

$$
{ \overline { { f } } } : { \Delta } ^ { n } \longrightarrow \overline { { { D / \Gamma } } } ,
$$

and we will analyze here when it does. Enlarge ${ \mathfrak H }$ to

$$
{ \mathfrak { H } } ^ { * } = { \mathfrak { H } } \cup \left\{ { \mathrm { i } } \infty \right\} ,
$$

where a fundamental system of neighborhoods of $\mathrm { i } \infty$ is given by

$$
\begin{array} { r } { W _ { c } = \left\{ z \in \mathfrak { H } \ \middle | \ \mathrm { I m } z > c \right\} \cup \left\{ \mathrm { i } \infty \right\} . } \end{array}
$$

Extend the map exp : $\mathfrak { H } \to \mathring { \Delta }$ to $\exp : { \mathfrak { H } } ^ { * } \to \Delta$ by $\mathrm { e x p } ( \mathrm { i } \infty ) = 0$ .

As a preliminary remark, we have

Proposition 7.1 The map $f ^ { * }$ above lifts to a continuous map

$$
\tilde { f } ^ { * } : ( \mathfrak { H } ^ { * } ) ^ { k } \times \Delta ^ { n - k } \longrightarrow D ^ { * } ,
$$

extending the map $\tilde { f } : \mathfrak { H } ^ { k } \times \Delta ^ { n - k } \longrightarrow D ;$ , where here we put on $D ^ { * }$ the Satake topology (see Subsection 6.1).

Proof Let $x \in ( { \mathfrak { H } } ^ { * } ) ^ { k } \times \Delta ^ { n - k }$ , let $\exp ( x )$ be its image in ${ \Delta ^ { k } } \times { \Delta ^ { n - k } }$ , and let $P = f ^ { \ast } ( \exp x )$ . Let $Q \in D ^ { * }$ lie over $P$ , and let $U _ { 1 }$ be a neighborhood of $Q$ in the Satake topology such that, for all $\gamma \in \Gamma$ , we have $\gamma U _ { 1 } = U _ { 1 }$ if $\gamma Q = Q$ , but $\gamma U _ { 1 } \cap U _ { 1 } = \emptyset$ if $\gamma Q \neq Q$ . Let $U _ { 2 }$ be the image of $U _ { 1 }$ in $( D / \Gamma ) ^ { * }$ . Then $\exp ( x )$ has a neighborhood $V _ { 2 }$ such that $f ^ { * } ( V _ { 2 } ) \subset U _ { 2 }$ . Let $V _ { 1 }$ be the component of $\mathrm { e x p } ^ { - 1 } ( V _ { 2 } )$ containing $x$ . Then

$$
\begin{array} { r } { \tilde { f } \left( V _ { 1 } \cap ( \mathfrak { H } ^ { k } \times \Delta ^ { n - k } ) \right) \subset \bigcup _ { \gamma \in \Gamma } \gamma U _ { 1 } . } \end{array}
$$

We may assume $V _ { 1 }$ is a product of sets of the type $W _ { c }$ and discs in $\mathbb { C }$ , and hence that $V _ { 1 } \cap ( { \mathfrak { H } } ^ { k } \times \Delta ^ { n - k } )$ is still connected. Therefore

$$
\tilde { f } \left( V _ { 1 } \cap ( \mathfrak { H } ^ { k } \times \Delta ^ { n - k } ) \right) \subset \gamma \cdot U _ { 1 }
$$

for some $\gamma \in \Gamma$ . We then define

$$
\tilde { f } ^ { * } ( x ) = \gamma \cdot Q .
$$

It is easy to check that this $\tilde { f } ^ { * }$ is continuous.

Consider the point $P = \tilde { f } ^ { * } ( \mathfrak { i } \infty , \ldots , \mathrm { i } \infty , 0 , \ldots , 0 )$ in $D ^ { * }$ . Let $F$ be the unique boundary component containing it. Then

$$
\begin{array} { r } { \operatorname { I m } \tilde { f } ^ { * } \subset D \cup \bigcup _ { \overline { { F } } _ { 1 } \supset F } F _ { 1 } \ . } \end{array}
$$

Note that, by continuity, $\gamma _ { i } P = P$ , for all $i = 1 , \ldots , k$ , hence $\gamma _ { i } \in \Gamma _ { F }$ .

The next result was suggested to us by P. Deligne; it generalizes a result of Y. Namikawa [9].

Theorem 7.2 In the notation introduced above, $\gamma _ { i } \in \overline { { C ( F ) } } \cap U ( F ) _ { \mathbb { Z } }$ for all $i =$ $1 , \ldots , k$ ; hence, $\tilde { f }$ induces a holomorphic map

$$
f ^ { 0 } : ( \mathring { \Delta } ) ^ { k } \times \Delta ^ { n - k } \longrightarrow D / U ( F ) _ { \mathbb { Z } } ,
$$

and the following statements are equivalent:

(i) all $\gamma _ { i }$ are in one and the same $\sigma _ { \alpha } ^ { F } \subset C ( F )$ for some $\alpha$ (ii) $f ^ { 0 }$ extends to a holomorphic map

$$
\overline { { { f } } } ^ { 0 } : \Delta ^ { n } \longrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } ;
$$

(iii) $f$ extends to a holomorphic map

$$
{ \overline { { f } } } : { \Delta } ^ { n } \longrightarrow \overline { { D / \Gamma } } \ : .
$$

Proof We prove first that $\gamma _ { i } \in U ( F ) _ { \mathbb { Z } }$ : in fact, restricting $f$ to the $i ^ { \because }$ th factor $\mathring \Delta .$ , holding all other variables constant, we get a map

$$
f _ { i } : \mathring { \Delta } \longrightarrow D / \Gamma
$$

that extends to $\Delta \longrightarrow ( D / \Gamma ) ^ { * }$ , and hence has no essential singularity at $0 \in \Delta$ . Since dim $\Delta = 1$ and $\overline { { D / \Gamma } }$ is compact, $f _ { i }$ also extends to a map

$$
{ \overline { { f } } } _ { i } : \Delta \longrightarrow { \overline { { D / \Gamma } } } .
$$

Also $\overline { { f } } _ { i } ( 0 )$ maps to a point of $( D / \Gamma ) ^ { * }$ which is in the image by $D ^ { * } \longrightarrow ( D / \Gamma ) ^ { * }$ of a stratum $F _ { 1 }$ , where ${ \overline { { F } } } _ { 1 } \supset F$ . Therefore $\overline { { f } } _ { i } ( 0 )$ is in the image of the map

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow \overline { { D / \Gamma } } .
$$

Since this map is etale, it follows that ´ ${ \overline { { f } } } _ { i }$ lifts, in a small neighborhood $\Delta ^ { \prime } \subset \Delta$ of 0, to

$$
\overline { { { f } } } _ { i } ^ { 0 } : \Delta ^ { \prime } \longrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } ,
$$

and hence $f _ { i }$ lifts to

$$
f _ { i } ^ { 0 } : \mathring { \Delta } ^ { \prime } = \Delta ^ { \prime } \backslash \left\{ 0 \right\} \longrightarrow D / U ( F ) _ { \mathbb { Z } } .
$$

$$
\gamma _ { i } \in \mathrm { I m } \Big ( f _ { i , * } ^ { 0 } : \pi _ { 1 } ( \mathring \Delta ^ { \prime } ) \longrightarrow \pi _ { 1 } ( D / U ( F ) _ { \mathbb { Z } } ) \Big ) , \mathrm { s o } \ \gamma _ { i } \in U ( F ) _ { \mathbb { Z } } .
$$

In particular, we know now that $f ^ { 0 }$ is defined. Next, we show that $f ^ { 0 }$ always extends to what we will call here a semi-proper meromorphic map $\overline { { f } } ^ { 0 }$ from $\Delta ^ { n }$ to $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ ; i.e, amany-valued map whose graph

$$
\mathrm { G r } ( \overline { { f } } ^ { 0 } ) \subset \Delta ^ { n } \times ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }
$$

is a closed analytic subset, mapping properly to $\Delta ^ { n }$ , and restricting to $f ^ { 0 }$ on $( { \mathring { \Delta } } ) ^ { k } \times \Delta ^ { n - k }$ . To see this, consider the following diagram:

$$
\begin{array} { r l r }  \Delta ^ { n } \times ( D / U ( F ) \mathbb { Z } ) _ { \{ \sigma _ { u } ^ { p \} \} } \supset \ \overline { { \operatorname { G r } } } ( f ^ { 0 } ) } & { \supset \ } & { \operatorname { G r } ( f ^ { 0 } ) } \\ { \bigg \downarrow \mathrm { ~ c a l e } } & { } & { \bigg \downarrow } \\ { \Delta ^ { n } \times \overline { { D / \Gamma } } } & { \supset \ } & { \overline { { \operatorname { G r } ( f ) } } } & { \big \{ \begin{array} { r l r } { \frac { \ 1 } { 2 } } & { \frac { \big | \sqrt { 3 } } { 2 } } & { \frac { \big | \sqrt { 3 } } { 2 } } \\ { \frac { \big | \sqrt { 3 } } { 2 } } & { \frac { \big | \sqrt { 3 } } { 2 } } & { \frac { \big | \sqrt { 3 } } { 2 } } \end{array} } \\ { \bigg \downarrow \mathrm { b r a t o r a l } } & { } & { \bigg \downarrow } & { \bigg \downarrow } \\ { \Delta ^ { n } \times ( D / \Gamma ) ^ { * } } & { \supset \ } & { \operatorname { G r } ( f ^ { * } ) } & { \big \{ \begin{array} { r l r } { \frac { \sqrt { 3 } } { 2 } } & { \frac { \big | \sqrt { 3 } } { 2 } } & { \frac { \big | \sqrt { 3 } } { 2 } } \\ { \frac { \sqrt { 3 } } { 2 } } & { \frac { \big | \sqrt { 3 } } { 2 } } & { \frac { \big | \sqrt { 3 } } { 2 } } \end{array} \bigg \} } & \end{array}
$$

Since $f ^ { * }$ exists, it follows that $\operatorname { G r } \left( f ^ { * } \right)$ is a closed analytic set isomorphic to $\Delta ^ { n }$ . Since $\overline { { D / \Gamma } } \longrightarrow ( D / \Gamma ) ^ { * }$ is proper and birational, the closure $\overline { { \operatorname { G r } \left( f \right) } }$ of $\operatorname { G r } \left( f \right)$ is also analytic, and maps properly to $\operatorname { G r } \left( f ^ { * } \right)$ , hence to $\Delta ^ { n }$ . Since $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow \overline { { D / \Gamma } }$ is étale, the closure $\overline { { \mathrm { G r } ( f ^ { 0 } ) } }$ is étale over $\overline { { \operatorname { G r } ( f ) } }$ and in particular is analytic. Since $\mathrm { G r } ( f ^ { 0 } ) = \mathrm { G r } ( f )$ is open dense in both $\overline { { \mathrm { G r } ( f ^ { 0 } ) } }$ and $\overline { { \operatorname { G r } \left( f \right) } }$ , in fact $\overline { { \mathrm { G r } ( f ^ { 0 } ) } }$ is just an open subset of $\overline { { \operatorname { G r } \left( f \right) } }$ .

Finally, $\overline { { \operatorname { G r } \left( f ^ { 0 } \right) } } = \overline { { \operatorname { G r } \left( f \right) } }$ . To see this, let $x _ { i } \in \mathfrak { H } ^ { k } \times \Delta ^ { n - k }$ be a sequence with $x _ { i } \longrightarrow x \in ( \mathfrak { H } ^ { * } ) ^ { k } \times \Delta ^ { n - k }$ , such that $f ( \exp x _ { i } ) \longrightarrow y \in \overline { { D / \Gamma } }$ . But $\tilde { f } ( x _ { i } ) \longrightarrow$ $\tilde { f } ^ { \ast } ( x )$ and $\tilde { f } ^ { \ast } ( x ) \in F _ { 1 }$ for some rational boundary component $F _ { 1 }$ with $\overline { { F } } _ { 1 } \supset$ $F$ . Then the image of $y$ in $( D / \Gamma ) ^ { * }$ is in the image of $F _ { 1 }$ , so $y$ lifts to a point $z$ in the $F _ { 1 }$ -stratum of $\left( D / U ( F _ { 1 } ) _ { \mathbb { Z } } \right) _ { \{ \sigma _ { \alpha } ^ { F _ { 1 } } \} }$ ; we may choose $z$ so that $z$ maps to ${ \tilde { f } } ^ { * } ( x ) { \bmod { U } } ( F _ { 1 } ) _ { \mathbb { Z } }$ via $\begin{array} { r } { ( D / U ( F _ { 1 } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { 1 } } \} } \longrightarrow D ^ { * } / U ( F _ { 1 } ) _ { \mathbb { Z } } } \end{array}$ . Now, since $\left( D / U ( F _ { 1 } ) _ { \mathbb { Z } } \right) _ { \{ \sigma _ { \alpha } ^ { F _ { 1 } } \} } \longrightarrow \overline { { D / \Gamma } }$ , $z _ { i } \in D / U ( F _ { 1 } ) _ { \mathbb { Z } }$ converging to z, with $z _ { i }$ over $f ( \exp x _ { i } )$ . In fact, $\left\{ z _ { i } \right\}$ must be equal to $\gamma \cdot$ $\tilde { f } ( x _ { i } ) \bmod U ( F _ { 1 } ) _ { \mathbb { Z } }$ , for some $\gamma \in \Gamma$ . But then, in $D ^ { * } / U ( F _ { 1 } ) _ { \mathbb { Z } }$ ,

$$
\begin{array} { r l r } { \mathrm { I m } \left( \gamma \cdot f ( x _ { i } ) \right) } & { \stackrel { i \to \infty } { \longrightarrow } } & { \mathrm { I m } \left( z \right) = \tilde { f } ^ { \ast } ( x ) \bmod U ( F _ { 1 } ) _ { \mathbb { Z } } } \\ { \parallel } & { } & \\ { \gamma \cdot \mathrm { I m } \left( \tilde { f } ( x _ { i } ) \right) } & { \stackrel { i \to \infty } { \longrightarrow } } & { \gamma \cdot \tilde { f } ^ { \ast } ( x ) \bmod U ( F _ { 1 } ) _ { \mathbb { Z } } , } \end{array}
$$

i.e., $\gamma \cdot \tilde { f } ^ { * } ( x ) = \tilde { f } ^ { * } ( x )$ mod $U ( F _ { 1 } ) _ { \mathbb { Z } }$ . Thus $\gamma \in \Gamma _ { F _ { 1 } }$ . Replace $z$ by $\gamma ^ { - 1 } z$ ; then $f ^ { 0 } ( \exp x _ { i } ) = \tilde { f } ( x _ { i } )$ mod $U ( F _ { 1 } ) _ { \mathbb { Z } }$ converges to $z$ , so $( \exp ( x ) , z ) \in { \overline { { \operatorname { G r } \left( f ^ { 0 } \right) } } }$ , as required.

The equivalence of (ii) and (iii) is now clear: since $\operatorname { G r } ( { \overline { { f ^ { 0 } } } } ) \ { \overset { \sim } { \longrightarrow } } \operatorname { G r } ( { \overline { { f } } } )$ , we see that $\overline { { f } }$ is single-valued if and only if $\overline { { f ^ { 0 } } }$ is single-valued. To bring in (i), use the following maps:

$$
\begin{array} { l c l } { { ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \subset } } & { { ( D ( F ) / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } } } \\ { { } } & { { } } & { { \overline { { { \pi } } } _ { 1 } \left| T ( F ) - \mathrm { b u n d l e } \right. } } \\ { { } } & { { } } & { { \left. \begin{array} { c } { { \forall } } \\ { { D ( F ) ^ { \prime } } } \\ { { \downarrow } } \end{array} \right. } } \\ { { } } & { { } } & { { \left. \begin{array} { c } { { \downarrow } } \\ { { F } } \end{array} \right. } } \end{array}
$$

For all $x \in \Delta ^ { n }$ , ${ \overline { { f } } } ( x )$ is a connected compact analytic set. But $F$ is a bounded domain and $D ( F ) ^ { \prime }$ is an affine bundle over $F$ ; so $D ( F ) ^ { \prime }$ contains no positivedimensional compact analytic sets. Thus $\overline { { \pi } } _ { 1 } \circ \overline { { f } }$ is single-valued. We can now apply:

# Lemma 7.3 Let

(1) $g : \Delta ^ { n } \longrightarrow Y$ be an analytic map;   
(2) $\pi : E \longrightarrow Y$ be a topologically trivial principal analytic fiber bundle with fiber an algebraic torus $T$ ; let $T \subset X _ { \{ \sigma _ { \alpha } \} }$ be a torus embedding and let $\pi : E _ { \{ \sigma _ { \alpha } \} } \longrightarrow Y$ be the associated fiber bundle;

(3) $h : ( \mathring { \Delta } ) ^ { k } \times \Delta ^ { n - k } \longrightarrow E$ be a lifting of g, which extends to a semi-proper⎡ ⎤ meromorphic map $\Delta ^ { n } \longrightarrow E _ { \{ \sigma _ { \alpha } \} }$ .

Then

$$
\left[ \begin{array} { c } { h \mathrm { e x t e n d s ~ t o } } \\ { \overline { { h } } : \Delta ^ { n } \longrightarrow E _ { \{ \sigma _ { \alpha } \} } } \end{array} \right] \Longleftrightarrow \left[ \begin{array} { c } { \mathrm { t h e ~ m o n o d r o m y ~ e l e m e n t s } } \\ { \gamma _ { i } \in \pi _ { 1 } ( T ) = \mathrm { K e r } \left( \pi _ { 1 } ( E ) \longrightarrow \pi _ { 1 } ( Y ) \right) } \\ { \mathrm { a l l ~ l i e ~ i n ~ o n e ~ } \sigma _ { \alpha } } \end{array} \right]
$$

and, in this case, $h$ extends to $\overline { { h } } : \Delta ^ { n } \to E _ { \sigma _ { \alpha } }$ , where $\alpha$ is as in the assertion on the right. Here the γi are the images of the generators in $\pi _ { 1 } ( ( \mathring { \Delta } ) ^ { k } )$ .

Proof Firstly, the result is local on $\Delta ^ { n }$ , so it is also local on $Y$ . So we may assume $E \cong T \times Y$ . Following $h$ by projection onto $T$ , it suffices to prove the lemma when $Y$ is a point and $E = T$ . Since $h$ is semi-proper meromorphic, for all $\beta \in M ( T ) = \operatorname { H o m } \left( T , \mathbb { G } _ { m } \right)$ , we have that $\beta \circ h$ is a meromorphic function on $\Delta ^ { n }$ and

$h$ extends to $\overline { { h } } : \Delta ^ { n } \to E _ { \sigma _ { \alpha } } \Longleftrightarrow$ for all $\beta \in \check { \sigma } _ { \alpha } \cap M ( T )$ , $\beta \circ h$ is holomorphic on $\Delta ^ { n }$

But for all $\beta \in M ( T ) , \beta \circ h$ has zeroes and poles only on the coordinate hyperplanes $H _ { i } \subset \Delta ^ { n }$ , so we may write

$$
( \beta \circ h ) = \sum _ { i = 1 } ^ { k } \ell _ { i } ( \beta ) \cdot H _ { i } ,
$$

where $\ell _ { i }$ is a linear function from $M ( T )$ to $\mathbb { Z }$ . But then $\arg \left( { \boldsymbol { \beta } } \circ h \right)$ changes by $2 \pi \ell _ { i } ( \beta )$ when going in a loop around $H _ { i }$ ; i.e., $\mathrm { a r g } \beta$ changes by $2 \pi \ell _ { i } ( \beta )$ when traversing the loop $\gamma _ { i }$ in $T$ . But, identifying $\pi _ { 1 } ( T )$ with $N ( T )$ , hence with ${ \mathrm { H o m } } \left( M ( T ) , \mathbb { Z } \right)$ , $\arg \mathfrak { X } ^ { \beta }$ in fact changes by $2 \pi \langle \gamma , \beta \rangle$ in a loop homologous to $\gamma .$ Thus

$$
\ell _ { i } ( \beta ) = \left. \gamma _ { i } , \beta \right. .
$$

Therefore

hence

Now, if $h$ extends to $\overline { { h } } : \Delta ^ { n } \longrightarrow E _ { \{ \sigma _ { \alpha } \} }$ , then $\overline { { h } } ( 0 , \dots , 0 ) \in E _ { \sigma _ { \alpha } }$ , for some $\sigma _ { \alpha }$ , and hence for all $\beta \in \check { \sigma } _ { \alpha }$ , the function $\beta \circ h$ is holomorphic on $\Delta ^ { n }$ , i.e., by what precedes, $\langle \gamma _ { i } , \beta \rangle \geq 0$ for all $i$ , and all $\beta \in \check { \sigma } _ { \alpha }$ ; hence $\gamma _ { i } \in \check { \check { \sigma } } _ { \alpha } = \sigma _ { \alpha }$ for all $i$

The only question now is why $\gamma _ { i } \in { \overline { { C ( F ) } } }$ in all cases. But this follows because $f _ { i } =$ restriction of $f$ to i’th $\mathring \Delta$ always extends, so, by (iii $) \Rightarrow \mathrm { ( i ) }$ , we have that $\gamma _ { i } \in$ some $\sigma _ { \alpha }$ , hence $\gamma _ { i } \in { \overline { { C ( F ) } } }$ . □

The theorem easily extends to the more general setting in which the inclusion

$$
( \mathring { \Delta } ) ^ { k } \times \Delta ^ { n - k } \subset \Delta ^ { n }
$$

is replaced by

$$
U \cap T \subset U ,
$$

where $U$ is a nice neighborhood of a point in the closed orbit of $X _ { \sigma }$ , with $T \subset X _ { \sigma }$ a torus embedding. The condition that $U \cap T \longrightarrow D / \Gamma$ extends to $U \longrightarrow \overline { { D / \Gamma } }$ is that the image of a certain natural map

$$
\sigma \longrightarrow { \overline { { C ( F ) } } }
$$

should lie in some $\sigma _ { \alpha }$

The above theorem in the special case $k = n = 1$ says: starting with any $f : { \mathring { \Delta } } \longrightarrow D / \Gamma$ , we lift it to an equivariant  $\tilde { f } : \mathfrak { H } \to D$ . Then the monodromy< $\gamma$ is in ${ \overline { { C ( F ) } } } \cap U ( F ) _ { \mathbb { Z } }$ . If we alter the lifting $\tilde { f }$ of $f$ to $\delta \cdot \tilde { f }$ , then $\gamma$ changes to $\delta \gamma \delta ^ { - 1 }$ . Thus $f$ alone determines canonically an element

$$
\begin{array} { r } { \mu ( f ) \in \Sigma _ { \mathbb { Z } } = \left( \bigcup _ { F } \overline { { C ( F ) } } \cap U ( F ) _ { \mathbb { Z } } \right) \Big / \Gamma . } \end{array}
$$

(Here the union is over all rational boundary components $F$ , and the $\overline { { C ( F ) } } \cap$ $U ( F ) _ { \mathbb { Z } }$ are considered as subsets of - $G$ ; the action of  $\Gamma$ is through conjugation; $\mu$ is short for monodromy.) Let us clarify the meaning of $\Sigma _ { \mathbb { Z } }$ . First of all, inside $G$ itself, let

$$
\begin{array} { r l } & { \lvert \widetilde \Sigma \rvert = \bigcup _ { F } \overline { { C ( F ) } } = \bigcup _ { F } C ( F ) \ , } \\ & { \widetilde \Sigma _ { \mathbb { Z } } = \Gamma \cap \lvert \widetilde \Sigma \rvert = \bigsqcup _ { F } C ( F ) \cap U ( F ) _ { \mathbb { Z } } \ . } \end{array}
$$

If $\{ \sigma _ { \alpha } \}$ is a $\Gamma$ -admissible collection of polyhedra as in Section 5, and $\widetilde { V } _ { \alpha } =$ res $\operatorname { I n t } \sigma _ { \alpha }$ (linear functions on $U ( F ) _ { \negmedspace \cdot }$ ), then $\widetilde { \Sigma } = ( | \widetilde { \Sigma } | , \{ \sigma _ { \alpha } \} , \{ \widetilde { V } _ { \alpha } \} )$ is a (infinite) conical polyhedral complex in the sense of Chapter I, Section 3, and $\widetilde { \Sigma } _ { \mathbb { Z } }$ defines an integral structure on $\widetilde { \Sigma }$ ; namely, on each $\sigma _ { \alpha }$ , let $\widetilde { L } _ { \alpha }$ be the linear functions which are integral on $\widetilde { \Sigma } _ { \mathbb { Z } }$ .

Since $\Gamma$ is neat, $\Gamma$ acts freely on $| \widetilde { \Sigma } |$ . And, for every $\Gamma$ -admissible collection $\{ \sigma _ { \alpha } \}$ , this action permutes the strata $\operatorname { I n t } \sigma _ { \alpha }$ and preserves the spaces $\widetilde { V } _ { \alpha }$ of linear functions, so we may form a quotient conical polyhedral complex:

$$
\begin{array} { r l } & { | \Sigma | = | \widetilde { \Sigma } | / \Gamma , } \\ & { S _ { \alpha } = \mathrm { I m } \left( \mathrm { I n t } \sigma _ { \alpha } \right) , } \\ & { V _ { \alpha } = \widetilde { V } _ { \alpha } . } \end{array}
$$

As a topological space with piecewise-linear structure, $| \Sigma |$ is independent of $\{ \sigma _ { \alpha } \}$ . And $\Sigma _ { \mathbb { Z } }$ is a subset of $| \Sigma |$ and defines an integral structure on the conical polyhedral complex $\Sigma = ( | \Sigma | , \{ S _ { \alpha } \} , \{ V _ { \alpha } \} )$ , by taking $L _ { \alpha }$ to be the linear functions which are integral on $\Sigma _ { \mathbb { Z } }$ . Note that, whereas there are infinitely many $\sigma _ { \alpha }$ , $\Sigma$ has only a finite number of strata $S _ { \alpha }$ , and, in fact, if $\mathbb { R } _ { > 0 }$ acts by homotheties on the cones of $\Sigma$ , then $| \Sigma | / \mathbb { R } _ { > 0 }$ is compact. Heuristically, $| \Sigma | / \mathbb { R } _ { > 0 }$ should be thought of as the set of all directions of approach to $\infty$ in $D / \Gamma$ , as described by ratios of exponents.

Definition 7.4 A structure $\{ S _ { \alpha } , V _ { \alpha } \}$ of conical polyhedral complexes on $| \Sigma |$ is admissible if it is induced by a $\Gamma$ -admissible collection $\{ \sigma _ { \alpha } \}$ .

Note that an admissible structure $\{ S _ { \alpha } , V _ { \alpha } \}$ on $| \Sigma |$ comes from only one collection $\{ \sigma _ { \alpha } \}$ : in fact, we can recover the $\sigma _ { \alpha }$ by looking at

$$
C ( F ) \hookrightarrow | \widetilde { \Sigma } | \longrightarrow | \Sigma |
$$

and (i) taking inverse images of the $S _ { \alpha }$ , (ii) taking their connected components, and (iii) closing them up in $\overline { { C ( F ) } }$ .

Next, define, in analogy with the definition for a toroidal embedding in Chapter I, Section 3,

$$
R . S . ( D / \Gamma ) = \left\{ \varphi : \Delta \longrightarrow ( D / \Gamma ) ^ { * } \mathrm { a n a l y t i c } | \varphi ( \mathring { \Delta } ) \subset D / \Gamma \right\}
$$

Then, as above, we get a map

$$
\mu : R . S . ( D / \Gamma ) \longrightarrow \Sigma _ { \mathbb { Z } }
$$

by lifting and considering the monodromy. We can now formulate the Main Theorem I (Theorem 5.2) in a more intrinsic way.

Theorem 7.5 (Main Theorem II) Let ⎨ ⎬ ⎨ ${ \mathcal { G } } , G , D$ , and $\Gamma$ be as in Theorem 5.2,⎬ where Γ is neat, and define the piecewise-linear topological space $| \Sigma |$ as above. Then there is a map

$$
\left\{ \begin{array} { l } { \mathrm { ~ a d m i s s i b l e ~ c o n i c a l } } \\ { \mathrm { p o l y h e d r a l ~ s t u c t u r e s } } \\ { \Sigma = \{ | \Sigma | , S _ { \alpha } , V _ { \alpha } \} \} } \end{array} \right\} \longrightarrow \left\{ \begin{array} { l } { \mathrm { t o r o i d a l ~ e m b e d d i n g s ~ } D / \Gamma \subset \overline { { D / \Gamma } } } \\ { \mathrm { w i t h o u t ~ m o n o d r o m y , w h e r e } \overline { { D / \Gamma } } } \\ { \mathrm { i s ~ a ~ c o m p a c t ~ a l g e b r a i c ~ s p a c e } } \end{array} \right\}
$$

such that, if $\Sigma ( \overline { { D / \Gamma } } )$ is the conical polyhedral complex with integral structure

associated by the theory of Chapter I, Section 3, to the toroidal embedding on the right, there is a unique isomorphism $\varphi$ making the diagram

commute. In particular, there is a bijection between the set of strata of $\overline { { D / \Gamma } }$ and the set of strata $\{ S _ { \alpha } \}$ of $\Sigma$ . Furthermore, if $\{ S _ { \alpha } ^ { ( 1 ) } \}$ is a subdivision of $\{ S _ { \alpha } ^ { ( 2 ) } \}$ , then $\overline { { D / \Gamma } } ^ { ( 1 ) }$ dominates $\overline { { D / \Gamma } } ^ { ( 2 ) }$ .

Proof Since $D / \Gamma \subset { \overline { { D / \Gamma } } }$ is locally like $D / U ( F ) _ { \mathbb { Z } } \subset ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ , it is certainly a toroidal embedding. Also

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } / ( \Gamma _ { F } / U ( F ) _ { \mathbb { Z } } ) \longrightarrow \overline { { D / \Gamma } }
$$

is bijective on the strata of type $F$ . Morever, denoting, as in the proof of Proposition 6.10, by $\Gamma _ { F } ^ { \prime }$ the intersection $\Gamma \cap N ( F ) ^ { \prime }$ and by $\overline { { \Gamma } } _ { F }$ the image of $\Gamma$ in $\operatorname { A u t } { ( U ( F ) ) } , \Gamma _ { F } ^ { \prime } / U ( F ) _ { \mathbb { Z } }$ fixes every stratum of $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} }$ , while $\overline { { \Gamma } } _ { F }$ permutes without fixed points the strata of type $F$ in $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} }$ . It follows that the strata of $\overline { { D / \Gamma } }$ are all of the form

$$
Y _ { \alpha } / ( \Gamma _ { F } ^ { \prime } / U ( F ) _ { \mathbb { Z } } ) ,
$$

where

$$
Y _ { \alpha } \subset ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }
$$

is a stratum corresponding to a $\sigma _ { \alpha }$ meeting $C ( F )$ . The main point here is that $\Gamma _ { F } ^ { \prime } / U ( F ) _ { \mathbb { Z } }$ acts on $\overline { { Y } } _ { \alpha }$ so as to fix each stratum $Y _ { \beta } \subset { \overline { { Y } } } _ { \alpha }$ . Since $D / U ( F ) _ { \mathbb { Z } } \subset$ $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ is a toroidal embedding without self-intersection, it follows that, even though  $D / \Gamma \subset { \overline { { D / \Gamma } } }$ may have self-intersection, it is without mon- odromy (in the sense of Chapter I, Section 3). Moreover, the polyhedral complex $C ( F ) ^ { * }$ associated to $D / U ( F ) _ { \mathbb { Z } } \subset ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ is given by

Here $C ^ { \prime }$ runs through the rational boundary components of $C$ . The equivalence relation $\Lambda$ is generated by

(i) the isomorphisms

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \stackrel { \gamma } { \longrightarrow } ( D / U ( \gamma F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { \gamma F } \} } , \mathrm { f o r } \gamma \in \Gamma ,
$$

(ii) the etale maps ´

$$
( D / U ( F _ { 1 } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F _ { 1 } } \} } \longrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } ,
$$

whenever ${ \overline { { F } } } _ { 1 } \supset F$ .

So the polyhedral complex $\Sigma ( \overline { { D / \Gamma } } )$ is obtained by dividing $\sqcup _ { F } C ( F ) ^ { * }$ by

(i) the isomorphisms $\gamma : C ( F ) ^ { * } \longrightarrow C ( \gamma F ) ^ { * }$ (ii) the inclusions, whenever ${ \overline { { F } } } _ { 1 } \supset F$ ,

$$
C ( F _ { 1 } ) ^ { * } \hookrightarrow C ( F ) ^ { * } \ .
$$

Modulo the latter we get $\widetilde { \Sigma }$ , and modulo the former we get $\Sigma$ ; this yields

$$
\varphi : \Sigma \stackrel { \sim } { \longrightarrow } \Sigma ( \overline { { { D / \Gamma } } } ) \ .
$$

The fact that the diagram in the theorem commutes is implied by the commutativity of the following analogous diagram:

$$
\left\{ \begin{array} { l l } { \mathrm { m a p s } ~ \phi : \Delta \longrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } } \\ { \mathrm { w h e r e } ~ \phi ( \mathring { \Delta } ) \subset D / U ( F ) _ { \mathbb { Z } } } \end{array} \right\}
$$

The commutativity here is a consequence of Proposition 3.3 in Chapter I. The uniqueness assertion about $\varphi$ follows from the fact that the image of ord, modulo homotheties, is dense. Finally, if $\{ S _ { \alpha } ^ { ( 1 ) } \}$ is a subdivision of $\{ S _ { \alpha } ^ { ( 2 ) } \}$ , then $\{ \sigma _ { \alpha } ^ { ( 1 ) } \}$ is a subdivision of $\{ \sigma _ { \alpha } ^ { ( 2 ) } \}$ ; hence there are vertical maps in the diagram

$$
\begin{array} { r } { D / U ( F ) _ { \mathbb { Z } } { \stackrel { \longleftrightarrow } { \longrightarrow } } \stackrel { \displaystyle ( D / U ( F ) _ { \mathbb { Z } } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { ( 1 ) , F } \} } } { \ ! } } \\ { { \longrightarrow } \stackrel { \mathbb { V } } { \longrightarrow } ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { ( 2 ) , F } \} } } \end{array}
$$

which induce a map in the vertical direction:

Finally, let us show that there are plenty of non-singular compactifications among those constructed. Recall that we assume throughout this section that $\Gamma$ is neat.

Corollary 7.6 For every $\Gamma$ -admissible collection $\{ \sigma _ { \alpha } \}$ of polyhedra, there exists exists a subdivision $\{ \sigma _ { \alpha } ^ { \prime } \}$ such that the morphism $\pi : \overline { { D / \Gamma } } ^ { \prime } \longrightarrow \overline { { D / \Gamma } }$ is projective and $\overline { { D / \Gamma } } ^ { \prime }$ is smooth.

Proof Because $\Gamma$ is neat, the morphism $\pi _ { F }$ in the diagram

$$
\begin{array} { l } { { D / U ( F ) _ { \mathbb { Z } } \quad \underbrace { \bigcirc \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } _ { D / \Gamma } } } \\ { { \downarrow \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } } \\ { { D / \Gamma \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \frac { \sqrt { \pi _ { F } } } { D / \Gamma } } } \end{array}
$$

is etale. Consequently, it is enough to find, compatibly for all ´ $F$ , a subdivision $\sigma _ { \alpha } ^ { \prime F }$ $\sigma _ { \alpha } ^ { F }$ such that $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { \prime F } \} }$ is smooth and

$$
( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { \prime F } \} } \longrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }
$$

is projective. Now Theorem 4 of TE I , Ch.I, $\ S 1$ , tells us that $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { \prime F } \} }$ is smooth if all cones $\sigma _ { \alpha } ^ { \prime F }$ ar gat by par b $U ( F ) _ { \mathbb { Z } }$ , and Theorem 11 of TE I , Ch.I, $\ S 1$ , constructs such a subdivision by an inductive procedure. It is also shown there that the resulting morphism will be a normalized blow-up and is, in particular, projective. □

# References

[1] W. Baily and A. Borel, Compactification of arithmetic quotients of bounded symmetric domains, Annals of Math. 84 (1966), 442–528.

[2] A. Borel, Introduction aux Groupes Arithmetiques ´ . Paris: Hermann, 1969. [3] A. Borel, Some metric properties of arithmetic quotients of symmetric spaces and an extension theorem, J. Diff. Geom. 6 (1972), 543–560.   
[4] R. Gunning and H. Rossi, Analytic Functions. Englewood Cliffs, NJ: Prentice Hall, 1965.   
[5] Harish-Chandra, Representations of semi-simple Lie groups VI, Am. J. Math. 78 (1956), 564–628.   
[6] S. Helgason, Differential Geometry and Symmetric Spaces. New York: Academic Press, 1962. [7] A. Koranyi and J. Wolf, Generalized Cayley transformations of bounded symmetric domains, Am. J. Math. 87 (1965), 899–939.   
[8] R. P. Langlands, The dimension of spaces of automorphic forms, Am. J. Math. 85 (1963), 99–125.   
[9] Y. Namikawa, On the canonical holomorphic map from the moduli space of stable curves to the Igusa monoidal transform, Nagoya Math. J. 52 (1973), 197–259.   
[10] I. Satake, On the arithmetic of tube domains (blowing up of the point at infinity), Bull. Am. Math. Soc. 79 (1973), 1076–1094.   
[11] I. Satake, Realization of Symmetric Domains as Siegel Domains of the Third Kind. Lecture notes, Berkeley, 1972.   
[12] J. Wolf, Fine structure of hermitian symmetric spaces, in Symmetric Spaces, eds. W. Boothby and G. Weiss. New York: Marcel Dekker, 1972, pp. 271–357.   
[13] J. Wolf, On the classification of hermitian symmetric spaces, J. Math. Mechanics, 13 (1964), 489–495.

# IV

# Further developments

This chapter is divided into two sections.

The first section is an immediate application of the construction of $\overline { { D / \Gamma } }$ in the previous chapter. With explicit local coordinates, we are able to give a criterion for the holomorphic extension of higher-order differential forms to cusps. We have also computed the local codimension of the space of “extendable forms” in the space of cusp forms in the case of Hilbert modular surfaces, from which one can compute the plurigenera of Hilbert modular surfaces.

The second section concerns a criterion for the projectivity of $\overline { { D / \Gamma } }$ . We shall show that certain $\overline { { D / \Gamma } }$ ’s are obtained by blowing up Baily–Borel’s compactification. Our method follows essentially that of Igusa [5], but the situation is much clearer now, since $\overline { { D / \Gamma } }$ has already been constructed.

# 1 Extension of differential forms to the cusps

# 1.1

Following the notations of the previous chapter, let

$$
G = \mathcal { G } ( \mathbb { R } ) ^ { o } ,
$$

Our purpose is to investigate when a top differential form extends to all “cusps” $\overline { { D / \Gamma } } \backslash ( D / \Gamma )$ .

Let $f$ be an automorphic form of weight $\ell$ with respect to $\Gamma$ :

$$
f ( \gamma z ) j ( \gamma , z ) ^ { \ell } = f ( z ) \mathrm { f o r } \mathrm { a l l } \gamma \in \Gamma , z \in D ,
$$

where $j ( \gamma , z )$ is the jacobian of the map $\gamma : D \longrightarrow D$ at $z$ , i.e., if

$$
\omega = \mathrm { d } z _ { 1 } \wedge \cdot \cdot \cdot \wedge \mathrm { d } z _ { N } , \mathrm { t h e n } \gamma ^ { * } \omega = j ( \gamma , z ) \omega
$$

The differential form $f \omega ^ { \otimes \ell }$ is invariant under $\Gamma$ , and hence can be considered as a form $^ \dagger$ in $\Omega ^ { N } ( D / \Gamma ) ^ { \otimes \ell }$ , and every element in $\Omega ^ { N } ( D / \Gamma ) ^ { \otimes \ell }$ is of this type.

Our problem is: when does $f \omega ^ { \otimes \ell }$ extend to $\overline { { D / \Gamma } } ?$

Let us first recall how $\overline { { D / \Gamma } }$ was constructed. By Chapter III, Theorem 5.2 (Main Theorem I), we have the following diagram:

$$
\begin{array} { l l } { { D / U ( F ) _ { \mathbb { Z } } } } & { { \longleftrightarrow \ ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } } } \\ { { \downarrow } } & { { \qquad } } \\ { { D / \Gamma } } & { { \longleftrightarrow \qquad \xrightarrow [ D / \Gamma ] { \qquad } } } \end{array}
$$

for every rational boundary component $F$ .

Furthermore, if $\Gamma$ is neat [1] (comp. also Chapter III, Section 7), and if each $\sigma _ { \alpha } ^ { F }$ can be generated by a part of a basis of $U ( F ) _ { \mathbb { Z } }$ , then $\pi _ { F }$ is unramified and $\overline { { D / \Gamma } }$ is non-singular (see Chapter III, Corollary 7.6).

Assume this is the case.

Hence, to see if $f \omega ^ { \otimes \ell }$ extends, it is enough to check if it extends for

$$
D / U ( F ) _ { \mathbb { Z } } \hookrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }
$$

for every $F$ . In fact, we only need to check this for $D / U ( F ) _ { \mathbb { Z } } \hookrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } ^ { F } }$ for each top-dimensional simplicial cone $\sigma _ { \alpha } ^ { F }$

Let us fix a rational boundary component $F$ , and embed $D$ into $D ( F )$ :

$$
\begin{array} { r l } & { D ( F ) = U ( F ) _ { \mathbb { C } } \times \mathbb { C } ^ { m } \times F \ , } \\ & { \qquad D = \{ ( z , u , t ) \in D ( F ) \mid \mathrm { I m } z - h _ { t } ( u , u ) \in C ( F ) \} \ . } \end{array}
$$

Introduce local coordinates $( z _ { i } ) , ( u _ { j } ) , ( t _ { k } )$ for each component; we may take $\omega$ as

$$
\omega = \bigwedge _ { i } \mathrm { d } z _ { i } \wedge \bigwedge _ { j } \mathrm { d } u _ { j } \wedge \bigwedge _ { k } \mathrm { d } t _ { k } .
$$

Now, $f$ has an expansion as a Fourier–Jacobi series:

$$
f = \sum _ { \rho \in L ^ { * } } \varphi _ { \rho } ( u , t ) \exp ( 2 \pi \mathrm { i } \langle \rho , z \rangle ) \ ,
$$

$^ \dagger$ Assume there are no singularities in $D / \Gamma$ .

where $\langle ~ , ~ \rangle$ is a positive-definite inner product on $U ( F )$ for which $C ( F )$ is self-adjoint, as defined in Chapter II, Section 1, and

$$
L ^ { * } = \left\{ \rho \in U ( F ) \mid \langle \rho , x \rangle \in \mathbb { Z } , { \mathrm { f o r ~ a l l } } x \in U ( F ) _ { \mathbb { Z } } \right\} .
$$

This series is convergent in some cylindrical set

$$
S ( K , r ) = \left\{ ( z , u , t ) \in D ( F ) \mid t \in K , \mathrm { I m } z - h _ { t } ( u , u ) - r \in C ( F ) \right\} ,
$$

where $K$ is a compact set in $F$ .

If none of the $\mathbb { Q }$ -simple components of $\mathcal { G }$ is isomorphic to $\mathrm { S L } _ { 2 } / \mathbb { Q }$ , then we have “Koecher’s theorem”:

$$
\varphi _ { \rho } \neq 0 \mathrm { o n l y f o r } \rho \in L ^ { * } \cap { \overline { { C ( F ) } } } ,
$$

(see Baily [1], p. 299).

We now express $f \omega ^ { \otimes \ell }$ in terms of the local coordinates in $( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } ^ { F } }$

Recall that $( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } ^ { F } }$ is the interior of the closure of $( D / U ( F ) _ { \mathbb { Z } } )$ in $( D / U ( F ) _ { \mathbb { Z } } ) \times ^ { T ( F ) } T ( F ) _ { \sigma _ { \alpha } ^ { F } }$ , and $T ( F ) = U ( F ) \mathbb { C } / U ( F ) \mathbb { z }$ . And, by our assumption,

Let $\{ Q _ { 1 } , \ldots , Q _ { n } \} \subset L ^ { * }$ be the dual basis of $\{ P _ { 1 } , \ldots , P _ { n } \}$ , $\begin{array} { r } { \check { \sigma } _ { \alpha } = \sum \mathbb { R } _ { \ge 0 } Q _ { i } } \end{array}$ . Then $T ( F ) _ { \sigma _ { \alpha } ^ { F } }$ is isomorphic to $\mathbb { C } ^ { n }$ with coordinates $\left\{ w _ { r } \right\}$

$$
w _ { r } = \exp ( 2 \pi \mathrm { i } \langle Q _ { r } , z \rangle ) \ .
$$

In terms of $( w _ { r } ) , ~ ( u _ { j } ) , ~ ( t _ { k } )$ , which are coordinates on $( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } ^ { F } }$ , we may write

$$
\begin{array} { l } { f = \displaystyle \sum _ { \rho } \varphi _ { \rho } ( u , t ) \exp ( 2 \pi \mathsf { i } \langle \rho , z \rangle ) } \\ { \displaystyle = \sum _ { \rho } \varphi _ { \rho } ( u , t ) \exp ( 2 \pi \mathsf { i } \langle \sum \rho _ { r } Q _ { r } , z \rangle ) \left( \mathrm { w h e r e ~ } \rho _ { r } = \langle \rho , P _ { r } \rangle \right) } \\ { \displaystyle = \sum _ { \rho } \varphi _ { \rho } ( u , t ) \prod _ { r } w _ { r } ^ { \rho _ { r } } , } \\ { \displaystyle \omega = \bigwedge _ { i } \mathbf { d } _ { i } \wedge \bigwedge _ { j } \mathbf { d } u _ { j } \wedge \bigwedge _ { k } \mathbf { d } t _ { k } } \\ { \displaystyle = \mathrm { c o n s t a n } \cdot \bigwedge _ { r } \mathbf { d } w _ { r } \wedge \bigwedge _ { k } \mathbf { d } u _ { j } \wedge \bigwedge _ { k } \mathbf { d } t _ { k } \frac { 1 } { \prod _ { r } w _ { r } } . } \end{array}
$$

Hence,

$$
f \omega ^ { \otimes \ell } = \mathrm { c o n s t . } \sum _ { \rho } \varphi _ { \rho } \prod _ { r } w _ { r } ^ { \rho _ { r } } \frac { 1 } { ( \prod _ { r } w _ { r } ) ^ { \ell } } \left( \bigwedge _ { r } \mathrm { d } w _ { r } \wedge \bigwedge _ { j } \mathrm { d } u _ { j } \wedge \bigwedge _ { k } \mathrm { d } t _ { k } \right) ^ { \otimes \ell } .
$$

Now, $( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } ^ { F } } \setminus ( D / U ( F ) _ { \mathbb { Z } } )$ is given by $\textstyle \bigcup _ { r } \{ w _ { r } = 0 \}$ , and hence $f \omega ^ { \otimes \ell }$ extends to $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ if and only if

$$
\varphi _ { \rho } \neq 0 { \mathrm { i m p l i e s } } \langle \rho , P _ { r } \rangle \geq \ell { \mathrm { f o r ~ a l l } } r .
$$

Since $\{ P _ { r } \}$ form a basis for $U ( F ) _ { \mathbb { Z } }$ and $\{ \sigma _ { \alpha } ^ { F } \}$ is admissible, there exists, for every $P \in U ( F ) _ { \mathbb { Z } } \cap { \overline { { C ( F ) } } }$ , an $\alpha$ such that $P$ can be expressed as follows:

If $P \neq 0$ , then

$$
\langle \rho , P \rangle = \sum a _ { r } \langle \rho , P _ { r } \rangle \geq ( \sum a _ { r } ) \ell \geq \ell .
$$

This proves

Theorem 1.1 Let $D$ be a bounded symmetric domain in $\mathbb { C } ^ { N }$ , let $\Gamma$ be a neat arithmetic subgroup of Aut $( D ) ^ { o }$ , let $f$ be an automorphic form of weight $\ell$ with respect to $\Gamma _ { \mathrm { { } } }$ , i.e., $f \omega ^ { \otimes \ell } \in \Omega ^ { N } ( D / \Gamma ) ^ { \otimes \ell }$ , and let $\overline { { D / \Gamma } }$ be the compactification of $D / \Gamma$ corresponding to a $\Gamma$ -admissible collection of polyhedra $\{ \sigma _ { \alpha } ^ { F } \}$ , where each $\sigma _ { \alpha } ^ { F }$ can be generated by a part of a basis of $U ( F ) _ { \mathbb { Z } }$ .Then $f \omega ^ { \otimes \ell }$ extends to $\overline { { D / \Gamma } }$ if and only if, for every rational boundary component $F$ , in the Fourier expansion of $f$ at $F$ , namely

$$
f = \sum _ { \rho \in U ( F ) _ { \mathbb { Z } } ^ { * } } \varphi _ { \rho } ^ { F } ( u , t ) \exp ( 2 \pi \mathrm { i } \langle \rho , z \rangle ) \ ,
$$

$\varphi _ { \rho } ^ { F }$ satisfies

$$
\varphi _ { \rho } ^ { F } \neq 0 \Longrightarrow \langle \rho , P \rangle \geq \ell
$$

for all non-zero $P \in U ( F ) _ { \mathbb { Z } } \cap { \overline { { C ( F ) } } }$ .

Now, on any complex manifold $U$ of dimension $N$ , let us call sections of $( \Omega _ { U } ^ { N } ) ^ { \otimes \ell }$ -fold top differentials. Recall the general fact that, if $V _ { 1 } , V _ { 2 }$ are bimeromorphic compact analytic manifolds, and $\omega _ { 1 } , \omega _ { 2 }$ are meromorphic $\ell \cdot$ - fold top differentials on $V _ { 1 } , \ V _ { 2 }$ which correspond to each other, then $\omega _ { \mathrm { l } }$ is regular, i.e., without poles, if and only if $\omega _ { 2 }$ is regular. Therefore, for any noncompact analytic manifold $U$ of the form ${ \overline { { U } } } \setminus Z$ , with $\overline { U }$ a compact manifold, and $Z$ a closed analytic subset, and for any holomorphic $\ell$ -fold top differential $\eta$ on $U$ , the condition that $\eta$ extend to $\overline { U }$ is independent of the choice of $\overline { U }$ Let us call such $\eta$ simply extendable forms. We see indeed from the above theorem that the criterion for $f \omega ^ { \otimes \ell }$ to extend to $\overline { { D / \Gamma } }$ is independent of the choice of $\{ \sigma _ { \alpha } ^ { F } \}$ . Thus we may rephrase the conclusion as:

Corollary 1.2 The $\ell$ -fold top differential $f \omega ^ { \otimes \ell }$ on $D / \Gamma$ is extendable if and only if, for every $F$ , we have that $\varphi _ { \rho } ^ { F } \neq 0$ implies $\langle \rho , P \rangle \geq \ell ,$ for all $0 \neq P \in$ $U ( F ) _ { \mathbb { Z } } \cap { \overline { { C ( F ) } } }$ . □

#

Let $\Gamma ^ { \prime } \subset \Gamma$ be an arithmetic subgroup of $G$ , and define $U ( F ) _ { \mathbb { Z } } ^ { \prime } = U ( F ) \cap \Gamma ^ { \prime }$

Apply the previous theorem to $\Gamma ^ { \prime }$ , but keep $f$ as an automorphic form with respect to $\Gamma$ . Then $f \omega ^ { \otimes \ell }$ extends to $\overline { { D / \Gamma ^ { \prime } } }$ if and only if we have

$$
\varphi _ { \rho } ^ { F } \neq 0 \Longrightarrow \langle \rho , P \rangle \geq \ell { \mathrm { ~ f o r ~ a l l ~ } } F { \mathrm { ~ a n d ~ a l l ~ } } 0 \neq P \in U ( F ) _ { \mathbb { Z } } ^ { \prime } \cap { \overline { { C ( F ) } } } .
$$

Assume that, for some positive integer $q$ , $U ( F ) _ { \mathbb { Z } } ^ { \prime } \subseteq q U ( F ) _ { \mathbb { Z } }$ for all $F$ . Then (1.1) is a consequence of the following condition:

$$
\begin{array} { r } { \varphi _ { \rho } ^ { F } \neq 0 \Longrightarrow \langle \rho , P \rangle \geq \frac { \ell } { q } \mathrm { ~ f o r ~ a l l ~ } F \mathrm { ~ a n d ~ a l l ~ } 0 \neq P \in U ( F ) _ { \mathbb { Z } } ^ { \prime } \cap \overline { { C ( F ) } } . } \end{array}
$$

Now start with a cusp form of weight $\ell$ with respect to $\Gamma$ and choose $q \geq \ell$ ; then $f$ will satisfy (1.2) via the following proposition.

Proposition 1.3 If $f$ is a cusp form on $D$ of weight $\ell$ with respect to $\Gamma$ , then, for every rational boundary component $F$ of $D$ ,

$$
\varphi _ { \rho } ^ { F } \neq 0 \Longrightarrow \langle \rho , P \rangle \geq 1 , f o r a l l n o n \mathrm { - } z e r o P \in U ( F ) _ { \mathbb { Z } } \cap \overline { { C ( F ) } } .
$$

Proof Since $f$ is a cusp form, $\varphi _ { 0 } ^ { F } = 0$ for every boundary component $F$

Assume $\varphi _ { \tau } ^ { F } \neq 0$ for some $\tau \in L ^ { * } \cap { \overline { { C ( F ) } } }$ , with

$$
\langle \tau , P \rangle = 0 \mathrm { f o r } \mathrm { a l l } 0 \ne P \in U ( P ) _ { \mathbb { Z } } \cap \overline { { C ( F ) } } .
$$

Define

$$
H _ { \tau } = \{ x \in U ( F ) \mid \langle \tau , x \rangle = 0 \} .
$$

Then $H _ { \tau } \cap \overline { { C ( F ) } }$ defines a rational boundary component of $C ( F )$ . By Chapter III, Theorem 4.8, there is a rational boundary component $F ^ { \prime }$ , with

$$
F \subset \overline { { F } } ^ { \prime } \mathrm { a n d } \overline { { C ( F ^ { \prime } ) } } = H _ { \tau } \cap \overline { { C ( F ) } }
$$

Consider the Fourier expansion of $f$ at $F ^ { \prime }$ :

$$
f = \sum _ { \rho ^ { \prime } \in L ^ { * } \cap \overline { { C ( F ^ { \prime } ) } } } \varphi _ { \rho ^ { \prime } } ^ { F ^ { \prime } } ( u ^ { \prime } , t ^ { \prime } ) \exp ( 2 \pi \mathrm { i } \langle \rho ^ { \prime } , z ^ { \prime } \rangle ) \ .
$$

Decompose $U ( F ) _ { \mathbb { C } }$ into

$$
\begin{array} { c } { { U ( F ) \mathbb { C } = U ( F ^ { \prime } ) \mathbb { c } \oplus \mathbb { C } ^ { k } } } \\ { { z = z ^ { \prime } + z ^ { \prime \prime } . } } \end{array}
$$

Then

$$
\varphi _ { 0 } ^ { F ^ { \prime } } = \sum _ { \stackrel { \rho \in L ^ { * } \cap \overline { { C ( F ^ { \prime } ) } } } { \langle \rho , C ( F ^ { \prime } ) \rangle = 0 } } \varphi _ { \rho } ^ { F } ( u , t ) \exp ( 2 \pi \mathrm { i } \langle \rho , z ^ { \prime \prime } \rangle ) \mathrm { } ,
$$

which would not be identically zero because $\varphi _ { \tau } ^ { F } \neq 0$ .But this contradicts the fact that $f$ is a cusp form.

We recall that, for any compact analytic manifold $V$ of dimension $N$ , the Kodaira dimension of $V$ is defined to be

$$
\kappa ( V ) = \mathrm { t r . d e g _ { C } } \left( { \bigoplus _ { \ell = 0 } ^ { \infty } \Gamma ( V , ( \Omega _ { V } ^ { N } ) ^ { \otimes \ell } ) } \right) - 1 .
$$

Then $- 1 \le \kappa ( V ) \le N$ , and $V$ is said to be of general type if $\kappa ( V ) = N$ . Equivalently, this means that, for some $\ell$ , there are $N + 1$ $\ell$ -fold top differentials $\omega _ { 0 } , \ldots , \omega _ { N }$ such that $\omega _ { 1 } / \omega _ { 0 } , \ldots , \omega _ { N } / \omega _ { 0 }$ are algebraically independent meromorphic functions on $V$ . If $U$ is a non-compact manifold of type ${ \overline { { U } } } \setminus X$ , with $\overline { U }$ a compact analytic manifold and $X$ a closed analytic subset, then we make the same definitions but using extendable $\ell$ -fold top differentials on $U$ . Note that, in both cases, the Kodaira dimension is a biholomorphic invariant.

Theorem 1.4 There exists $\Gamma ^ { \prime } \subset \Gamma$ such that $D / \Gamma ^ { \prime }$ is of general type.

Proof Let $f _ { 0 } , \ldots , f _ { N }$ be modular forms of weight $\ell$ such that $f _ { 1 } / f _ { 0 } , \ldots , f _ { N } / f _ { 0 }$ are algebraically independent, and let $f$ be a cusp form of weight $m$ with respect to $\Gamma$ . Then $f \cdot f _ { 0 } , \ldots , f \cdot f _ { N }$ are cusp forms of weight $\ell + m$ .

Let $\Gamma ^ { \prime } \subset \Gamma$ be an arithmetic subgroup of $G$ such that, for all rational boundary components $F$ , we have

$$
\begin{array} { r } { \left( \ell + m + 1 \right) \cdot U ( F ) _ { \mathbb { Z } } \supset U ( F ) _ { \mathbb { Z } } ^ { \prime } . } \end{array}
$$

Then $f \cdot f _ { i }$ all extend to sections of $( \Omega ^ { N } ) ^ { \otimes ( \ell + m ) }$ over $\overline { { D / \Gamma ^ { \prime } } }$ . Hence the Kodaira dimension of $\overline { { D / \Gamma ^ { \prime } } }$ is equal to $N$ .

# 1.3

Let

$\gamma = \left( \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right) \in \Gamma$ acts on $z = ( z _ { 1 } , z _ { 2 } ) \in D$

$$
\gamma z = \left( { \frac { a z _ { 1 } + b } { c z _ { 1 } + d } } , { \frac { a ^ { \prime } z _ { 2 } + b ^ { \prime } } { c ^ { \prime } z _ { 2 } + d ^ { \prime } } } \right) ,
$$

where $x \mapsto x ^ { \prime }$ is the conjugation automorphism of $K$ .

Let $f$ be an automorphic form of weight $\ell$ :

$$
f ( \gamma z ) = ( c z _ { 1 } + d ) ^ { 2 \ell } ( c ^ { \prime } z _ { 2 } + d ^ { \prime } ) ^ { 2 \ell } f ( z ) ~ .
$$

Then $f$ has a Fourier expansion:

$$
f ( z ) = \sum _ { \alpha \in L ^ { * } \cap \overline { { V } } } a _ { \alpha } \exp ( 2 \pi \mathrm { i } \langle \alpha , z \rangle ) \ ,
$$

where

$V =$ the positive quadrant in $\mathbb { R } ^ { 2 }$ ,

$$
\begin{array} { r l } & { \mathrm { ~ , ~ } z \rangle = \alpha _ { 1 } z _ { 1 } + \alpha _ { 2 } z _ { 2 } , \mathrm { ~ f o r ~ } \alpha = ( \alpha _ { 1 } , \alpha _ { 2 } ) , z = ( z _ { 1 } , z } \\ & { \mathrm { ~ \ } L = \{ a \in \mathbb { R } ^ { 2 } \mid z \longmapsto z + a \mathrm { \ l i e s \ i n \Gamma } \} , } \\ & { \mathrm { ~ \ } L ^ { * } = \{ \alpha \in \mathbb { R } ^ { 2 } \mid \langle \alpha , a \rangle \in \mathbb { Z } \mathrm { \ f o r \ a l l \ } a \in L \} , } \end{array}
$$

and this series is convergent for $\mathrm { I m } z _ { 1 } \mathrm { I m } z _ { 2 } \gg 0$ .

Theorem 1.1 implies that $f ( \mathbf { d } z _ { 1 } \wedge \mathbf { d } z _ { 2 } ) ^ { \otimes \ell }$ extends to $\overline { { D / \Gamma } }$ if and only if

$a _ { \alpha } = 0$ for all $\alpha$ such that $\langle \alpha , a \rangle < \ell$ , for some $0 \neq a \in L \cap { \overline { { V } } }$ .

We are going to study the number of those terms modulo the unit action. More precisely, if we identify $L$ with $\mathcal { O }$ , and define

$$
( x , y ) = x y + x ^ { \prime } y ^ { \prime } { \mathrm { ~ f o r ~ } } x , y \in K \ ,
$$

then

$$
L ^ { * } = \left\{ \rho \in K \vert ( \rho , x ) \in \mathbb { Z } , { \mathrm { f o r ~ a l l } } x \in \mathcal { O } \right\} .
$$

It is known as the complementary module of $L$ . If we fix a base for $L$ :

$$
\begin{array} { r } { L = \mathbb { Z } \cdot 1 + \mathbb { Z } \cdot W \ , } \end{array}
$$

then

$$
L ^ { * } = \mathbb { Z } \cdot \frac { 1 } { W - W ^ { \prime } } + \mathbb { Z } \cdot \frac { W } { W - W ^ { \prime } } \ .
$$

Let $C$ be the cone of totally positive numbers in $K$ . Also fix some positive integer $\ell .$ . Define

$$
\varphi ( \alpha ) = \operatorname* { m i n } _ { 0 \neq x \in L \cap \overline { { C } } } ( \alpha , x ) = \operatorname* { m i n } _ { x \in L \cap C } ( \alpha , x ) \ ,
$$

$$
\mathcal S = \{ \alpha \in L ^ { * } \cap \overline { { C } } \mid \varphi ( \alpha ) < \ell \} .
$$

The group of totally positive units $U _ { + }$ in $\mathcal { O }$ acts on $\mathcal { S }$ via $\varepsilon : \alpha \mapsto \varepsilon \alpha$ .† The following theorem was conjectured by Hirzebruch.

Theorem 1.5 The set $\mathcal { S } / U _ { + }$ has

$$
{ \frac { 1 } { 2 } } \ell ( \ell - 1 ) \sum _ { k = 1 } ^ { r } ( b _ { k } - 2 )
$$

elements, where $\left( b _ { 1 } , \ldots , b _ { r } \right)$ is the cycle associated to the continued fraction expansion of $W$ .

Before proving the theorem, we first construct a decomposition of $C ^ { * }$ such that $\varphi$ is linear on each sector.

By taking the convex hull of $L \cap C$ , we obtain an admissible decomposition of $C$ . Write each vertex $V _ { k }$ as $V _ { k } = p _ { k } - q _ { k } W$ with $p _ { k }$ $k , q _ { k } \in \mathbb { Z }$ . Assume $W >$ $1 > W ^ { \prime }$ . Then we have

$$
p _ { k - 1 } q _ { k } - q _ { k - 1 } p _ { k } = 1 ,
$$

$$
p _ { k - 1 } q _ { k + 1 } - q _ { k - 1 } p _ { k + 1 } = b _ { k } \geq 2 ,
$$

$$
V _ { k } > V _ { k + 1 } , V _ { k + 1 } ^ { \prime } > V _ { k } ^ { \prime } \ ,
$$

$$
\begin{array} { r } { V _ { k + 1 } + V _ { k - 1 } = b _ { k } V _ { k } , } \end{array}
$$

$$
\operatorname* { l i m } _ { k \longrightarrow \infty } \frac { p _ { k } } { q _ { k } } = W , \operatorname* { l i m } _ { k \longrightarrow - \infty } \frac { p _ { k } } { q _ { k } } = W ^ { \prime } .
$$

The union of $r$ consecutive sectors forms a fundamental domain with respect to the action of totally positive units (see Chapter I, Section 5, or Hirzebruch [4]).

For each $k$ , define

$$
W _ { k } = \frac { p _ { k + 1 } - p _ { k } } { W - W ^ { \prime } } - \frac { q _ { k + 1 } - q _ { k } } { W - W ^ { \prime } } W ^ { \prime } \in { \cal L } ^ { * } .
$$

By (1.5), $W _ { k } > 0$ and $W _ { k } ^ { \prime } > 0$ , hence $W _ { k } \in L ^ { * } \cap C$ . Furthermore,

$$
\begin{array} { l } { ( W _ { k } , V _ { k } ) = \left( \displaystyle \frac { p _ { k + 1 } - p _ { k } } { W - W ^ { \prime } } - \displaystyle \frac { q _ { k + 1 } - q _ { k } } { W - W ^ { \prime } } W ^ { \prime } \right) ( p _ { k } - q _ { k } W ) } \\ { \displaystyle \qquad + \left( - \displaystyle \frac { p _ { k + 1 } - p _ { k } } { W - W ^ { \prime } } - \displaystyle \frac { q _ { k + 1 } - q _ { k } } { W - W ^ { \prime } } W \right) ( p _ { k } - q _ { k } W ^ { \prime } ) } \\ { \displaystyle \qquad = p _ { k } ( q _ { k + 1 } - q _ { k } ) - q _ { k } ( p _ { k + 1 } - p _ { k } ) } \\ { \displaystyle \qquad = 1 , \mathrm { ~ b y ~ } ( 1 . 3 ) . } \end{array}
$$

$^ \dagger$ The action induced by $\Gamma$ is actually $\alpha \mapsto \varepsilon ^ { 2 } \alpha$ , which will change our number by a factor of 1 or 2.

Similarly,

$$
\left( W _ { k - 1 } , V _ { k } \right) = 1 .
$$

Define

$$
C _ { k } ^ { * } = \mathbb { R } _ { > 0 } W _ { k } + \mathbb { R } _ { \ge 0 } W _ { k - 1 } \ .
$$

Note from (1.3) and (1.4) that

$$
{ \frac { p _ { k + 1 } - p _ { k } } { q _ { k + 1 } - q _ { k } } } \geq { \frac { p _ { k } - p _ { k - 1 } } { q _ { k } - q _ { k - 1 } } } ,
$$

with equality holding only when

$$
b _ { k } = 2 ,
$$

in which case $W _ { k } = W _ { k - 1 }$ and $C _ { k } ^ { * }$ is only a ray.

The collection of $C _ { k } ^ { * }$ with $b _ { k } \geq 3$ covers $C ^ { * }$ because

$$
\frac { a } { W - W ^ { \prime } } - \frac { b W } { W - W ^ { \prime } } \in C ^ { * } \Longleftrightarrow W > \frac { a } { b } > W ^ { \prime } ,
$$

and the fact that

$$
\operatorname* { l i m } _ { k \longrightarrow \infty } \frac { p _ { k } - p _ { k - 1 } } { q _ { k } - q _ { k - 1 } } = W , \operatorname* { l i m } _ { k \longrightarrow - \infty } \frac { p _ { k } - p _ { k - 1 } } { q _ { k } - q _ { k - 1 } } = W ^ { \prime } .
$$

Proof Start with an element on the left. Now,

$$
\begin{array} { r l r } & { } & { \alpha \in \overline { { C _ { k } ^ { * } } } \Longrightarrow \alpha = a W _ { k - 1 } + b W _ { k } \mathrm { , ~ f o r ~ s o m e ~ } a , b \geq 0 \mathrm { } } \\ & { } & { \qquad \Longrightarrow \left( \alpha , V _ { k } \right) = a + b \leq \left( \alpha , x \right) \mathrm { , ~ f o r ~ a l l ~ } x \in L \cap C \mathrm { . } } \end{array}
$$

Conversely, suppose $\varphi ( \alpha ) = ( \alpha , V _ { k } ) \neq 0$ . Since $\{ \mathbb { R } _ { > 0 } W _ { i } + \mathbb { R } _ { > 0 } W _ { i - 1 } \}$ covers $C ^ { * }$ , we have $\alpha \in \mathbb { R } _ { > 0 } W _ { i } + \mathbb { R } _ { > 0 } W _ { i - 1 }$ for some $i$ . Assume that $i \neq k$ . Without loss of generality, let us consider the case $i < k$ . Then $\alpha = a W _ { i - 1 } + b W _ { i }$ for some $a , b > 0$ ; hence

$$
a ( W _ { i - 1 } , V _ { k } ) + b ( W _ { i } , V _ { k } ) = ( \alpha , V _ { k } ) \leq ( \alpha , V _ { i } ) = a + b ,
$$

and

$$
\left( W _ { i - 1 } , V _ { k } \right) = 1 .
$$

But we know that

$$
( W _ { i - 1 } , V _ { i - 1 } ) = ( W _ { i - 1 } , V _ { i } ) = 1 \ .
$$

Hence $V _ { k }$ lies on the straight line joining $V _ { i - 1 }$ and $V _ { i }$ . By convexity, all the vertices $V _ { i - 1 } , V _ { i } , \dots , V _ { k }$ lie on the same line, and we get

$$
\overline { { C _ { i } ^ { * } } } = \overline { { C _ { i + 1 } ^ { * } } } = \cdots = \overline { { C _ { k - 1 } ^ { * } } } \subset \overline { { C _ { k } ^ { * } } } ~ ,
$$

hence $\alpha \in \overline { { C _ { k } ^ { * } } }$

The collection of $r$ consecutive $C _ { k } ^ { * }$ forms a fundamental domain in $C ^ { * }$ with respect to the action of totally positive units.

Define $N _ { k } = \# \{ \alpha \in L ^ { * } \cap C _ { k } ^ { * } \mid \varphi ( \alpha ) < \ell \}$ , so that

$$
\# ( \mathcal { S } / U ^ { + } ) = \sum _ { b _ { k } \geq 3 } N _ { k } .
$$

Proof of Theorem 1.5 It suffices to prove

$$
\begin{array} { r } { N _ { k } = \frac { 1 } { 2 } \ell ( \ell - 1 ) ( b _ { k } - 2 ) . } \end{array}
$$

Introduce the following elements of $L ^ { * }$ :

$$
\begin{array} { r } { P = \frac { - p _ { k - 1 } } { W - W ^ { \prime } } + \frac { q _ { k - 1 } } { W - W ^ { \prime } } W ^ { \prime } , } \\ { Q = \frac { p _ { k + 1 } } { W + W ^ { \prime } } + \frac { q _ { k + 1 } } { W - W ^ { \prime } } W ^ { \prime } . } \end{array}
$$

Define

$$
P _ { i } = \frac { i } { b _ { k } } P + \frac { b _ { k } - i } { b _ { k } } Q \mathrm { f o r } 1 \leq i \leq b _ { k } .
$$

We have

(1) $P _ { 1 } = W _ { k }$ , $P _ { b _ { k } - 1 } = W _ { k - 1 }$ (from (1.6));   
(2) $P _ { i } \in L ^ { * }$ , because $\begin{array} { r } { \frac { 1 } { b _ { k } } ( P - Q ) = \frac { - p _ { k } } { W - W ^ { \prime } } + \frac { q _ { k } } { W - W ^ { \prime } } W ^ { \prime } } \end{array}$ (from (1.6));   
(3) $( P _ { i } , V _ { k } ) = 1$ (from (1));   
(4) $\left\{ { P } _ { i } , { P } _ { i + 1 } \right\}$ form a basis for ;; $L ^ { * }$ .

e the last point, calculate the determinant with respect to the basis ;;; ;;; ;; ;; $\left\{ \frac 1 { W - W ^ { \prime } } , \frac { W ^ { \prime } } { W - W ^ { \prime } } \right\}$ $L ^ { * }$

$$
\operatorname * { d e t } \{ P _ { i } , P _ { i + 1 } \} = { \left| \begin{array} { l l } { { \frac { i + 1 } { b _ { k } } } } & { { \frac { b _ { k } - i - 1 } { b _ { k } } } } \\ { { \frac { i } { b _ { k } } } } & { { \frac { b _ { k } - i } { b _ { k } } } } \end{array} \right| } { \left| \begin{array} { l l } { - p _ { k - 1 } } & { q _ { k - 1 } } \\ { \quad p _ { k + 1 } } & { - q _ { k + 1 } } \end{array} \right| } = { \frac { 1 } { b _ { k } } } \cdot b _ { k } = 1 .
$$

Define $C _ { k , i } ^ { * } = \mathbb { R } _ { > 0 } P _ { i } + \mathbb { R } _ { \ge 0 } P _ { i + 1 }$ for $i = 1 , \ldots , b _ { k } - 2$ , and let

$$
N _ { k , i } = \# \{ \alpha \in L ^ { * } \cap C _ { k , i } ^ { * } \mid \varphi ( \alpha ) < \ell \} \ ,
$$

so that $N _ { k } = \Sigma N _ { k , i }$

Since $\left\{ { P } _ { i } , { P } _ { i + 1 } \right\}$ forms a base for $L ^ { * }$ , and $\varphi ( P _ { i } ) = \varphi ( P _ { i + 1 } ) = 1$ , we get

$$
N _ { k , i } = 1 + 2 + \cdots + ( \ell - 1 ) = { \textstyle { \frac { 1 } { 2 } } } \ell ( \ell - 1 ) ,
$$

and hence

$$
\begin{array} { r } { N _ { k } = ( b _ { k } - 2 ) \cdot \frac { 1 } { 2 } \ell ( \ell - 1 ) . } \end{array}
$$

# 2 Projectivity of $\overline { { D / \Gamma } }$

# 2.1

Let $D$ be a bounded symmetric domain, let $\Gamma$ be an arithmetic subgroup of $\operatorname { A u t } ( D ) ^ { o }$ , and let $\{ \sigma _ { \alpha } ^ { F } \}$ be a $\Gamma$ -admissible decomposition. Then we have constructed the associated compactification $\overline { { D / \Gamma } }$ of $D / \Gamma$ . In this section, we are going to study the relation between $\overline { { D / \Gamma } }$ and Baily–Borel’s compactification $( D / \Gamma ) ^ { * } = D ^ { * } / \Gamma$ . The main result is that $\overline { { D / \Gamma } }$ , for certain $\{ \sigma _ { \alpha } ^ { F } \}$ , is the blowingup of $D ^ { * } / \Gamma$ at a certain sheaf of ideals. Consequently $\overline { { D / \Gamma } }$ is projective in these cases.

For simplicity, we shall assume in this section that $\Gamma$ is neat. (Things can be worked out without this assumption, but things will be much cleaner if we assume $\Gamma$ to be neat.)

The relevant decompositions are similar to the projective subdivisions in-  - TE $^ { \mathrm { I , \dag } }$ Ch. III, $\ S 1$ . We shall describe them first.

As in Chapter III, Section 7, define

$$
| \widetilde { \Sigma } | = \bigsqcup _ { F } C ( F ) \ , \ | \Sigma | = | \widetilde { \Sigma } | / \Gamma \mathrm { a n d } \Sigma _ { \mathbb { Z } } \ .
$$

Definition 2.1 A $\Gamma$ -admissible decomposition $\{ \sigma _ { \alpha } ^ { F } \}$ is projective if there exists a continuous convex piecewise-linear function $\varphi : | \Sigma | \longrightarrow \mathbb { R }$ such that

(1) $\varphi ( x ) > 0 \mathrm { f o r } x \neq 0 ;$ ;

(2) $\varphi$ is linear on the image of $\sigma _ { \alpha } ^ { F }$ , and $\sigma _ { \alpha } ^ { F }$ are the maximal polyhedral cones in $\overline { { C ( F ) } }$ on which $\varphi$ is linear ;

(3) $\varphi$ is integral on $\Sigma _ { \mathbb { Z } }$ .

The existence of such decompositions follows from the theory of co-cores (see Chapter $\mathrm { I I }$ , Section 5). Indeed, let $\{ \Delta _ { F } \}$ be a system of $\overline { { \Gamma } } _ { F }$ -polyhedral co-cores, one for each rational boundary component $F$ , such that

(1) $\mathrm { f o r } F \subset \overline { { F } } ^ { \prime } , \Delta _ { F } \cap \overline { { C ( F ^ { \prime } ) } } = \Delta _ { F ^ { \prime } } ,$ (2) for $F ^ { \prime } = \gamma F$ with $\gamma \in \Gamma$ , we have $\Delta _ { F ^ { \prime } } = \gamma \Delta _ { F }$

From Chapter $\mathrm { I I }$ , Section 5, we know that the cones over the faces of $\Delta _ { F }$ define a $\Gamma$ -admissible decomposition. Fix a sufficiently divisible integer $N$ . For each $F$ , let $\varphi _ { F }$ be the unique convex piecewise-linear function on $\overline { { C ( F ) } }$ such that it has value $N$ at each face of $\Delta _ { F }$ and is linear on the cone over each face. Then $\big \{ \varphi _ { F } \big \}$ defines a function $\varphi$ on $| \Sigma |$ with the required properties.

Let us start with a projective $\Gamma$ -admissible decomposition $\{ \sigma _ { \alpha } ^ { F } \}$ and $\varphi :$ $| \Sigma | \longrightarrow \mathbb { R }$ satisfying the required properties. Then $\varphi$ defines a collection of continuous piecewise-linear functions $\big \{ \varphi _ { F } \big \}$ on $\{ { \overline { { C ( F ) } } } \}$ such that $\varphi _ { F }$ is linear on each $\sigma _ { \alpha } ^ { F }$ . We define a dual piecewise-linear function $\varphi _ { F } ^ { * }$ on $C ( F )$ such that, in the terminology of Chapter II, Subsection 5.2,

$$
\{ \varphi _ { F } ^ { \ast } ( \lambda ) \geq 1 \} = \operatorname { t h e ~ c o r e ~ d u a l ~ t o ~ t h e ~ c o - c o r e } \left\{ \varphi _ { F } ( x ) \geq 1 \right\} .
$$

More explicitly, let

$$
\{ P _ { \alpha , i } \} = \mathrm { v e r t i c e s ~ o f } \ \sigma _ { \alpha } ^ { F } \cap \{ \varphi _ { F } = 1 \} \ ,
$$

and define

$$
\varphi _ { F } ^ { * } ( \lambda ) = \operatorname* { m i n } _ { \alpha , i } \left. \lambda , P _ { \alpha , i } \right. , \mathrm { f o r } \lambda \in C ( F ) .
$$

Moreover, for all top-dimensional $\sigma _ { \alpha } ^ { F }$ , let

$$
\lambda _ { \alpha } \in { U } ( F ) _ { \mathbb { Z } } ^ { * } = \operatorname { H o m } { \left( U ( F ) _ { \mathbb { Z } } , \mathbb { Z } \right) }
$$

be the linear function such that

$$
\lambda _ { \alpha } | _ { \sigma _ { \alpha } ^ { F } } = \varphi _ { F } | _ { \sigma _ { \alpha } ^ { F } }
$$

(this exists by assumptions (2) and (3) on $\varphi$ ). Note that $\varphi _ { F } ^ { * } ( \lambda _ { \alpha } ) = 1$ . Now we can define the ideal of the blowing-up as follows.

Let $x \in F / \Gamma ( F ) \subset D ^ { * } / \Gamma$ . Then the holomorphic functions around $x$ are described by the Fourier–Jacobi series (for notation, see Subsection 2.2 below) of the following form:

$$
f = \sum _ { \rho \in C ( F ) \cap U ( F ) _ { \mathbb { Z } } ^ { * } } \theta _ { \rho } ( u , t ) \exp ( 2 \pi \mathrm { i } \langle \rho , z \rangle ) \ .
$$

Define

$\mathcal { I } _ { m , x } = \{ f \in \mathcal { O } _ { x } | \theta _ { \rho } \neq 0 \mathrm { o n l y } \mathrm { f o r } \rho \in U ( F ) _ { \mathbb { Z } } ^ { * } \cap C ( F )$ and $\varphi _ { F } ^ { * } ( \rho ) \geq m \}$ .

Since $\varphi _ { F } ^ { * }$ is convex, $\mathcal { I } _ { m , x }$ is an ideal. We shall see later that $\{ \mathcal { I } _ { m , x } \}$ form a coherent sheaf of ideals ${ \mathcal { I } } _ { m }$ concentrated at the boundary. (Note that ${ \mathcal { I } } _ { m }$ depends on the choice of $\varphi$ as well as on $m$ .) We shall often denote ${ \mathcal { I } } _ { m }$ simply by $\mathcal { I }$ .

Our aim is to prove the following theorem.

Theorem 2.2 Let $\{ \sigma _ { \alpha } ^ { F } \}$ be a projective $\Gamma$ -admissible decomposition, let ${ \mathcal { I } } _ { m }$ be the sheaf of ideals on $D ^ { * } / \Gamma$ constructed as above (with a suitable m fixed in the course of the proof), and let $\widetilde { ( D / \Gamma ) } _ { \mathcal { S } }$ be the normalization of the blowing-up at $\mathcal { I }$ . Then $\widetilde { ( D / \Gamma ) } _ { \mathcal { I } }$ is isomorphic to the compactification $\overline { { D / \Gamma } }$ associated to $\{ \sigma _ { \alpha } ^ { F } \}$

Corollary 2.3 If $\{ \sigma _ { \alpha } ^ { F } \}$ is projective, then the associated $\overline { { D / \Gamma } }$ is projective.

Corollary 2.4 There are $\Gamma$ -admissible collections $\{ \sigma _ { \alpha } \}$ of polyhedra such that the associated compactification $\overline { { D / \Gamma } }$ is non-singular and projective.

Proof Indeed, start with some projective $\{ \sigma _ { \alpha } ^ { F } \}$ and then apply the refining procedure of Chapter III, Corollary 7.6.

# 2.2

Let $F$ be a rational boundary component of $D$ , let $x ^ { \prime } \in F \subset D ^ { * }$ , let $x$ be the image of $x ^ { \prime }$ in $D ^ { * } / \Gamma$ , and let $U$ be a neighborhood of $x ^ { \prime }$ in $\mathbf { D } ^ { * }$ such that

$$
U \cap D = \pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( \ell C _ { 0 } ) ,
$$

where $E$ is a relatively compact open neighborhood of $x ^ { \prime }$ in $F$ such that

$$
\begin{array} { r l } & { \bullet \gamma E \cap E = \emptyset \mathrm { ~ f o r ~ i d } \neq \gamma \in \Gamma ( F ) , } \\ & { \bullet C _ { 0 } \mathrm { ~ i s ~ t h e ~ i n t e r i o r ~ o f ~ a ~ c o r e ~ i n ~ } C ( F ) , } \\ & { \bullet \ell > 0 , } \\ & { \bullet \gamma U = U \mathrm { ~ f o r ~ } \gamma \in \Gamma _ { x ^ { \prime } } . } \end{array}
$$

By Chapter III, Section 6, such $U$ actually form a fundamental system of neighborhoods of $x ^ { \prime }$ .

Let $f$ be a holomorphic function on $U \cap D$ ; such an $f$ defines an element in $\mathcal { O } _ { x }$ if, for all $y \in U \cap D$ ,

$$
f ( \gamma y ) = f ( y ) \mathrm { ~ f o r ~ a l l ~ } \gamma \in \Gamma _ { x ^ { \prime } } .
$$

To study this invariance condition we need explicit forms of the $N ( F )$ - action. As in Chapter III, Section 4, and in Koranyi–Wolf [7], $D$ can be realized as a Siegel domain of the third kind:

$$
{ \cal D } \cong \{ ( t , u , z ) \in F \times \mathbb { C } ^ { k } \times U ( F ) _ { \mathbb { C } } \mid \mathrm { I m } z - \mathrm { R e } L _ { t } ( u , u ) \in C ( F ) \} ,
$$

where $L _ { t }$ is a quasi-hermitian form (a sum of a hermitian form $H _ { t }$ and a symmetric form $S _ { t }$ ) depending analytically on $t$ , where $2 k = \dim V ( F )$ , and where $H _ { t } ( u , u ) \in \overline { { C ( F ) } }$ , for all $u$ . Recall that, for each $t _ { 0 } \in F$ , the action of $V ( F )$ on the points $\left( t _ { 0 } , \boldsymbol { u } , \cdot \right) \in D$ makes $\mathbb { C } ^ { k }$ into a principal homogeneous space over $V ( F )$ , and hence identifies $V ( F )$ with $\mathbb { C } ^ { k }$ via mapping $x$ to the second coordinate of $x ( t _ { 0 } , 0 , \cdot )$ . But this identification varies with $t _ { 0 }$ .

# Proposition 2.5

(1) In the coordinates $( t , u , z )$ , the action of $N ( F )$ consists of quasi-linear

transformations, i.e., every $\gamma \in N ( F )$ acts by:

$$
\begin{array} { r l } & { z \longmapsto A z + a ( u , t ) \ , } \\ & { u \longmapsto B _ { t } u + b _ { t } \ , } \\ & { t \longmapsto g ( t ) \ , } \end{array}
$$

where $A \in \operatorname { A u t } ( C ( F ) ) , B _ { t }$ is linear in $u$ , and $B _ { t } , \ b _ { t } , \ g ( t )$ , and $a ( u , t )$ are analytic in t and $u$ .

(2) $W ( { \boldsymbol { F } } )$ consists of the following transformations:

$$
( b , a ) = \left\{ \begin{array} { c c c } { { z } } & { { \longmapsto } } & { { z + a + 2 \mathrm { i } L _ { t } ( u , b _ { t } ) + \mathrm { i } L _ { t } ( b _ { t } , b _ { t } ) , } } \\ { { u } } & { { \longmapsto } } & { { u + b _ { t } , } } \\ { { t } } & { { \longmapsto } } & { { t , } } \end{array} \right.
$$

where $a \in U ( F ) , b \in V ( F )$ , and $b _ { t } \in \mathbb { C } ^ { k }$ is given by the identification of $V ( F )$ and $\mathbb { C } ^ { k }$ , depending analytically on⎨ $t$ .

(3) Let $Z ^ { \prime } ( F ) \subset Z ( F )$ be the subgroup consisting of transformations of the form:

$$
\begin{array} { r } { ( B , A ) = \left\{ \begin{array} { l l l } { z } & { \longmapsto } & { A z + \mathrm { i } L _ { t } \bigl ( B _ { t } u , B _ { t } u \bigr ) - \mathrm { i } A L _ { t } \bigl ( u , u \bigr ) , } \\ { u } & { \longmapsto } & { B _ { t } u , } \\ { t } & { \longmapsto } & { t , } \end{array} \right. } \end{array}
$$

with $A$ , $B _ { t }$ satisfying

$$
A H _ { t } ( u , u ) = H _ { t } ( B _ { t } u , B _ { t } u ) , A \in \mathrm { A u t } ( C ( F ) ) \ .
$$

Then we have the semi-direct product decomposition:

$$
Z ( F ) = Z ^ { \prime } ( F ) \ltimes W ( F ) \ .
$$

For the proof of (1) and (2), see [7] and [9]; for (3), see [6]. We make some remarks about (2) and (3).

(i) By simple computations, one can show

$$
( b , a ) ( b ^ { \prime } , a ^ { \prime } ) = ( b + b ^ { \prime } , a + a ^ { \prime } + 2 [ b , b ^ { \prime } ] ) ,
$$

where $[ b , b ^ { \prime } ] = \mathrm { I m } H _ { t } ( b _ { t } , b _ { t } ^ { \prime } )$ . Hence

$$
( b , a ) ( b ^ { \prime } , a ^ { \prime } ) ( b , a ) ^ { - 1 } ( b ^ { \prime } , a ^ { \prime } ) ^ { - 1 } = ( 0 , 4 [ b , b ^ { \prime } ] ) .
$$

(ii) The form that $^ { ( B , A ) }$ is given shows that $^ { ( B , A ) }$ transforms $D$ to $D$ (in the given realization). The condition $A H _ { t } ( u , u ) = H _ { t } ( B _ { t } u , B _ { t } u )$ guarantees that $Z ^ { \prime } ( F )$ normalizes $W ( { \boldsymbol { F } } )$ . By computation, we have that, if $\gamma =$ $( b , a ) ( B , A )$ , then

$$
\gamma ( b ^ { \prime } , a ^ { \prime } ) \gamma ^ { - 1 } = ( B b ^ { \prime } , A a ^ { \prime } + 4 [ b , B b ^ { \prime } ] ) .
$$

(iii) For every $\beta \in V ( F )$ , there is a unique function $b _ { t }$ as in (2) such that $( b , 0 )$ represents the action of $\beta$ , and all the $b _ { t }$ correspond to some $\beta$ .   
(iv) In the notation of Chapter III, Section 4, $G _ { \ell } ( F ) \cdot M ( F )$ is the identity component of $Z ^ { \prime } ( F )$ .

Let $V ( F ) _ { \mathbb { Z } }$ be the image of $W ( F ) \cap \Gamma$ in $V ( F )$ considered as the quotient $W ( F ) / U ( F )$ .

Let $\overline { { \Gamma } } _ { F }$ be the image of $Z ( F ) \cap \Gamma$ in Aut $( C ( F ) )$ . Note that this is a subgroup of finite index in the $\overline { { \Gamma } } _ { F }$ defined in Chapter III, Section 5, which was the image of $N ( F ) \cap \Gamma$ in $\operatorname { A u t } ( C ( F ) )$ .

Lemma 2.6 The following sequences are exact:

$$
\begin{array} { r c c c c c c l c l } { { 1 } } & { { \longrightarrow } } & { { U ( F ) _ { \mathbb { Z } } } } & { { \longrightarrow } } & { { W ( F ) \cap \Gamma } } & { { \longrightarrow } } & { { V ( F ) _ { \mathbb { Z } } } } & { { \longrightarrow } } & { { 1 , } } \\ { { 1 } } & { { \longrightarrow } } & { { W ( F ) \cap \Gamma } } & { { \longrightarrow } } & { { Z ( F ) \cap \Gamma } } & { { \longrightarrow } } & { { \overline { { { \Gamma } } } _ { F } } } & { { \longrightarrow } } & { { 1 . } } \end{array}
$$

Proof The exactness of the first sequence follows from the definition of $V ( F ) _ { \mathbb { Z } }$ To prove that the second sequence is exact, we need to prove

$$
\ker \left( Z ( F ) \cap \Gamma \longrightarrow \mathrm { A u t } \left( C ( F ) \right) \right) = W ( F ) \cap \Gamma .
$$

Recall from Chapter III, Section 4, that we have

$$
Z ( F ) ^ { o } = [ G _ { \ell } ( F ) \cdot M ( F ) ] \ltimes W ( F ) ~ .
$$

Therefore $\ker \left( Z ( F ) \cap \Gamma \longrightarrow \mathrm { A u t } ( C ( F ) ) \right) / W ( F ) \cap \Gamma$ is contained in the compact factors, and, since it is discrete, it is finite. But

$\ker \left( Z ( F ) \cap \Gamma \to \operatorname { A u t } ( C ( F ) ) \right) / W ( F ) \cap \Gamma \subset ( { \mathcal { N } } ( F ) \cap \Gamma ) / { \mathcal { W } } ( F ) \cap \Gamma ,$ which is torsion-free, since $\Gamma$ is neat and ${ \mathcal { N } } ( F )$ and $\mathcal { W } ( F )$ are both defined over $\mathbb { Q }$ . □

Lemma 2.7 $[ G _ { \ell } ( F ) \cap \Gamma ] \ltimes [ W ( F ) \cap \Gamma ]$ is of finite index in $Z ( F ) \cap \Gamma$ .

Proof Since $G _ { \ell } , W$ , and $G _ { \ell } \ltimes W$ are defined over $\mathbb { Q }$ , the following are arithmetic subgroups:

$$
\begin{array} { r l } & { G _ { \ell } ( F ) \cap \Gamma \subset G _ { \ell } ( F ) \ , } \\ & { \quad W ( F ) \cap \Gamma \subset W ( F ) \ , } \\ & { \quad ( G _ { \ell } ( F ) \ltimes W ( F ) ) \cap \Gamma \subset G _ { \ell } ( F ) \ltimes W ( F ) \ . } \end{array}
$$

From the general theory of arithmetic subgroups, $( G _ { \ell } ( F ) \cap \Gamma ) \ltimes ( W ( F ) \cap \Gamma )$ is also an arithmetic subgroup of $G _ { \ell } ( F ) \ltimes W ( F )$ , and hence $( G _ { \ell } ( F ) \cap \Gamma ) \ltimes$ $\left( W ( F ) \cap \Gamma \right)$ is of finite index in $( G _ { \ell } ( F ) \ltimes W ( F ) ) \cap \Gamma$ . But $Z ( F ) / ( G _ { \ell } ( F ) \ltimes$ $W ( { \boldsymbol { F } } ) )$ is compact, so $Z ( F ) \cap \Gamma / ( G _ { \ell } ( F ) \ltimes W ( F ) ) \cap \Gamma$ is also finite.

Going back to our invariance condition, if we start with $f$ in ${ \mathcal { O } } _ { x }$ , then $f ( \gamma y ) =$ $f ( y )$ , for all $\gamma \in \Gamma _ { x }$ , $y \in U \cap D$ .

The invariance condition by the elements in $U ( F ) _ { \mathbb { Z } }$ implies that $f$ admits the Fourier–Jacobi series expansion:

$$
f ( t , u , z ) = \sum _ { \rho \in U ( F ) _ { \mathbb { Z } } ^ { * } } \theta _ { \rho } ( u , t ) \exp ( 2 \pi \mathrm { i } \langle \rho , z \rangle ) \ .
$$

If $\gamma \in V ( F ) _ { \mathbb { Z } }$ and lifts to $( b , a ) \in W ( F ) \cap \Gamma$ , the invariance condition shows

$$
\theta _ { \rho } ( u + b _ { t } , t ) = \theta _ { \rho } ( u , t ) \exp ( 2 \pi \mathrm { i } \langle \rho , - 2 \mathrm { i } L _ { t } ( u , b _ { t } ) - \mathrm { i } L _ { t } ( b _ { t } , b _ { t } ) - a \rangle ) ~ .
$$

For simplicity, call $\mathrm { e } _ { b _ { t } } ( u )$ the exponential factor appearing here. (Note that $a$ is uniquely determined modulo $U ( F ) _ { \mathbb { Z } }$ .) Define the line bundle $\mathcal { L } _ { \rho }$ on the family of complex tori $( \mathbb { C } ^ { k } \times F ) / V ( F ) _ { \mathbb { Z } } \xrightarrow { \pi } F$ as $\mathbb { C } \times \mathbb { C } ^ { k } \times F$ modulo the following action of $V ( F ) _ { \mathbb { Z } }$ :

$$
\begin{array} { r } { ( \alpha , u , t ) \longmapsto ( e _ { \nu _ { t } } ( u ) \alpha , \nu _ { t } + u , t ) , \nu \in V ( F ) _ { \mathbb { Z } } . } \end{array}
$$

Equation (2.1) just means $\theta _ { \rho } \in \Gamma ( \pi ^ { - 1 } ( E ) , \mathcal { L } _ { \rho } )$ .

It is shown in [9] and [1] that the convergence of the series for $f$ requires that $\rho \in { \overline { { C ( F ) } } }$ whenever $\theta _ { \rho } \neq 0$ .

Define

$$
\begin{array} { r } { g ( u ) = \exp ( - 2 \pi \langle \rho , S _ { t } ( u , u ) \rangle ) \mathrm { , } } \\ { \mathrm { e } _ { \nu _ { t } } ^ { \prime } ( u ) = \mathrm { e } _ { \nu _ { t } } ( u ) g ( \nu _ { t } + u ) g ( u ) ^ { - 1 } \mathrm { . } } \end{array}
$$

By simple computations,

$$
\boldsymbol { \mathrm { e } } _ { \nu _ { t } } ^ { \prime } ( u ) = \mathrm { e x p } ( 2 \pi \langle \rho , 2 H _ { t } ( u , \nu ) + H _ { t } ( \nu , \nu ) \rangle ) \cdot \mathrm { e x p } ( - 2 \pi \mathrm { i } \langle \rho , a \rangle ) \ .
$$

In the notation of [8], this shows that the line bundle $\mathcal { L } _ { \rho } | _ { \pi ^ { - 1 } ( t ) }$ is algebraically equivalent to $\mathcal { L } ( 4 \langle \rho , H _ { t } \rangle )$ .

Furthermore, for $\rho \in L ^ { * } \cap C ( F ) ^ { * }$ , since $H _ { t } ( u , u ) \in \overline { { C ( F ) } }$ for all $u$ , we have that $4 \langle \rho , H _ { t } \rangle$ is positive-definite. By the remarks following Proposition 2.5, $\mathrm { I m } 4 \langle \rho , H _ { t } ( u , \nu ) \rangle$ is integral on $V ( F ) _ { \mathbb { Z } } \times V ( F ) _ { \mathbb { Z } }$ . In particular, for our $\lambda _ { \alpha }$ defined in Subsection 2.1, we know $\mathcal { L } _ { m \lambda _ { \alpha } } | _ { \pi ^ { - 1 } ( t ) }$ is generated by its sections if m ≥ 2, and hence so is Lmλα |π−1(E).

Now consider $A \in \overline { { \Gamma } } _ { F }$ , and assume it lifts to $( d , c ) ( B , A )$ in $Z ( F ) \cap \Gamma$ . By Lemma 2.7, for all $A \in { \overline { { \Gamma } } } _ { F }$ , we can get such liftings while choosing $( d , c )$ in a finite set.

For $\gamma = ( d , c ) ( B , A )$ , the invariance condition gives:

$$
\theta _ { A ^ { * } \rho } ( u , t ) = \theta _ { \rho } \left( B _ { t } u + d _ { t } , t \right) \exp ( 2 \pi \mathrm { i } \langle \rho , a ( u , t ) \rangle ) ,
$$

where

$$
a ( u , t ) = \mathrm { i } L _ { t } ( B _ { t } u , B _ { t } u ) - \mathrm { i } A L _ { t } ( u , u ) + 2 \mathrm { i } L _ { t } ( B _ { t } u , d _ { t } ) + \mathrm { i } L _ { t } ( d _ { t } , d _ { t } ) + c \ .
$$

Note that by Lemma 2.6, if $A \in { \overline { { \Gamma } } } _ { F }$ , then $( d , c )$ is uniquely determined modulo $W ( F ) \cap \Gamma$ , and $B _ { t }$ is uniquely determined.

Conversely, start with $\theta _ { \lambda } \in \Gamma ( \pi ^ { - 1 } ( E ) , { \mathcal { L } } _ { \lambda } )$ for some neighborhood $E$ of $x ^ { \prime }$ in $F$ and define $\theta _ { A ^ { * } \lambda }$ by (2.2) $\left( A \in { \overline { { \Gamma } } } _ { F } \right)$ ). Then form the sum

$$
f _ { \theta _ { \lambda } } = \sum _ { A \in \overline { { \Gamma } } _ { F } } \theta _ { A ^ { * } \lambda } \exp ( 2 \pi \mathrm { i } \langle A ^ { * } \lambda , z \rangle ) .
$$

By Lemma 2.6, and the discussion above, the local ring $\mathcal { O } _ { x }$ is generated by such $f _ { \theta _ { \lambda } }$ if we know their convergence. For this, we prove the following proposition.

Proposition 2.8 For all $A \in { \overline { { \Gamma } } } _ { F }$ , $a \in C ( F )$ , and $\theta _ { \lambda }$ as above, there is an $M > 0$ such that

$$
| f _ { \theta _ { \lambda } } | \le M \mathrm { i n } \pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( a + C ( F ) ) .
$$

Proof Since $F$ is $\mathbb { Q }$ -rational, $V ( F ) / V ( F ) _ { \mathbb { Z } }$ is compact. Let $S \subset V ( F )$ be a compact fundamental set for $V ( F ) _ { \mathbb { Z } }$ . Using the action of $V ( F )$ on $\mathbb { C } ^ { k } \times F$ , let $S _ { 1 } \subset \mathbb { C } ^ { k }$ be a compact set such that $S \cdot [ ( 0 ) \times E ] \subset S _ { 1 } \times E$ .

By (2.2), we have

$$
\vert \theta _ { A ^ { \ast } \lambda } ( u , t ) \vert = \vert \theta _ { \lambda } ( B _ { t } u + d _ { t } , t ) \vert \exp ( - 2 \pi \langle \lambda , \mathrm { I m } a ( u , t ) \rangle ) .
$$

Writing $h _ { t } = \mathrm { R e } L _ { t }$ , we find

$$
\mathrm { I m } a ( u , t ) = h _ { t } ( B _ { t } u , B _ { t } u ) - A h _ { t } ( u , u ) + 2 h _ { t } ( B _ { t } u , d _ { t } ) + h _ { t } ( d _ { t } , d _ { t } ) ~ .
$$

Decompose $B _ { t } u$ as ${ u } _ { t } + { b } _ { t }$ , with $u _ { t } \in S _ { 1 }$ and $b \in V ( F ) _ { \mathbb { Z } }$ . Then

$$
\begin{array} { r } { | \theta _ { \lambda } ( B _ { t } u + d _ { t } , t ) | = | \theta _ { \lambda } ( u _ { t } + d _ { t } + b _ { t } , t ) |  \qquad } \\ {  \qquad = | \theta _ { \lambda } ( u _ { t } + d _ { t } , t ) | \exp ( - 2 \pi \langle \lambda , a ^ { \prime } ( u , t ) \rangle ) \ : , \ :  } \end{array}
$$

where, by (2.1),

$$
\begin{array} { r l } & { a ^ { \prime } ( u , t ) = - 2 h _ { t } ( u _ { t } + d _ { t } , b _ { t } ) - h _ { t } ( b _ { t } , b _ { t } ) } \\ & { \qquad = - 2 h _ { t } ( d _ { t } , b _ { t } ) + h _ { t } ( u _ { t } , u _ { t } ) - h _ { t } ( u _ { t } + b _ { t } , u _ { t } + b _ { t } ) } \\ & { \qquad = - 2 h _ { t } ( d _ { t } , B _ { t } u ) + 2 h _ { t } ( d _ { t } , u _ { t } ) + h _ { t } ( u _ { t } , u _ { t } ) - h _ { t } ( B _ { t } u , B _ { t } u ) . } \end{array}
$$

Since $t$ is in a compact set and the $( d , c )$ are in a finite set, the $d _ { t }$ are in a compact set. Further, $u _ { t } \in S _ { 1 }$ , which is compact. Hence

$$
\begin{array} { r l } & { | \theta _ { A ^ { * } \lambda } ( u , t ) \exp ( 2 \pi \mathrm { i } \langle A ^ { * } \lambda , z \rangle ) | \leq C \cdot \exp ( - 2 \pi \langle A ^ { * } \lambda , \mathrm { I m } z \rangle \exp ( 2 \pi \langle \lambda , A h _ { t } ( u , u ) \rangle ) } \\ & { \qquad = C ^ { \prime } \cdot \exp ( - 2 \pi \langle A ^ { * } \lambda , \mathrm { I m } z - h _ { t } ( u , u ) \rangle ) } \\ & { \qquad \leq C ^ { \prime \prime } \cdot \exp ( - 2 \pi \langle A ^ { * } \lambda , a \rangle ) \ , } \end{array}
$$

for suitable constants $C , C ^ { \prime } , C ^ { \prime \prime }$ . Let

$$
a _ { n } = \# \{ A \in \overline { { \Gamma } } _ { F } \ | \ n \leq \langle A ^ { * } \lambda , a \rangle \leq n + 1 \} \ ;
$$

then (because the action of $\overline { { \Gamma } } _ { F }$ is fixed-point free)

$$
a _ { n } \leq \# \left\{ x \in U ( F ) _ { \mathbb { Z } } ^ { * } \cap C ( F ) \mid n \leq ( x , a ) \leq n + 1 \right\} ,
$$

which grows like the volume of $C ( F ) \cap \left\{ ( x , a ) = n \right\}$ . Hence $a _ { n } \leq$ const. $n ^ { K }$ for some constant $K$ . Therefore,

$$
\sum \exp ( - 2 \pi \langle A ^ { * } \lambda , a \rangle ) \leq \sum _ { n \geq 0 } a _ { n } \exp ( - 2 \pi n ) \leq \mathrm { c o n s t . } \cdot \sum _ { n \geq 0 } n ^ { K } \exp ( - 2 \pi n ) < \infty .
$$

Proposition 2.9 ${ \mathcal { O } } _ { x }$ is generated by $f _ { \boldsymbol { \theta } _ { \lambda } }$ with $\theta _ { \lambda } \in \Gamma ( \pi ^ { - 1 } ( E ) , { \mathcal { L } } _ { \lambda } )$ and $\lambda \in$ $\overline { { C ( F ) } } \cap U ( F ) _ { \mathbb { Z } } ^ { * }$ .

Proof This follows from Proposition 2.8 and the fact that $\ell C _ { 0 }$ is, modulo $\overline { { \Gamma } } _ { F }$ , contained in a finite union of cylindrical sets $a + C ( F )$ .

Proposition 2.10 Assume ${ \mathrm { I n t } } \sigma _ { \alpha } ^ { F } \subset C ( F )$ , with $\sigma _ { \alpha } ^ { F }$ top-dimensional. Fix $a \in$ $C ( F ) , K > 0 ,$ , and $\theta _ { \lambda } \in \Gamma ( \pi ^ { - 1 } ( E ) , { \mathcal { L } } _ { \lambda } )$ , where $\varphi _ { F } ^ { * } ( \lambda ) \geq m$ . Then there exists $M > 0$ such that

$$
\begin{array} { c } { \left| f _ { \theta _ { \lambda } } \exp ( \langle - m \lambda _ { \alpha } , z \rangle ) \right| < M } \\ { \displaystyle \pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( \sigma _ { \alpha } ^ { F } + a ) \cap \{ | u | \leq K \} . } \end{array}
$$

Proof Recall the definition of $\varphi _ { F } ^ { * }$ : we have points $\{ P _ { i , \alpha } \}$ such that

$$
\begin{array} { r l } & { ~ \sigma _ { \alpha } ^ { F } = \sum \mathbb { R } _ { \geq 0 } P _ { i , \alpha } \mathrm { ~ a n d ~ } \langle \lambda _ { \alpha } , P _ { i , \alpha } \rangle = 1 \mathrm { ~ , ~ } } \\ & { \varphi _ { F } ^ { * } ( \lambda ) = \displaystyle \operatorname* { m i n } _ { i , \alpha } \langle \lambda , P _ { i , \alpha } \rangle \mathrm { ~ . ~ } } \end{array}
$$

Since $\varphi _ { F } ^ { * } ( A ^ { * } \lambda ) = \varphi _ { F } ^ { * } ( \lambda ) \geq m$ , we have $A ^ { * } \lambda - m \lambda _ { \alpha } \geq 0$ in $\sigma _ { \alpha }$ , and hence

$$
\langle A ^ { * } \lambda - m \lambda _ { \alpha } , a \rangle \geq 0 \mathrm { f o r } \mathrm { a l l } A \in \overline { { { \Gamma } } } _ { F } .
$$

The rest of the proof runs parallel to that of Proposition 2.8, where we proved the similar statement for $f _ { \boldsymbol { \theta } _ { \lambda } }$ .

We now prove that the ideals $\mathcal { I } _ { m , x }$ defined in Subsection 2.1 form a coherent sheaf of ideals. We first define a sheaf of principal ideals $\mathcal { J }$ on $\overline { { D / \Gamma } }$ in the following steps.

(1) Define $\mathcal { J } _ { F }$ on $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ : Let $X _ { \alpha } = ( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } ^ { F } }$ , and, for all topdimensional $\sigma _ { \alpha } ^ { F }$ , let

$$
\mathcal { J } _ { F , \alpha } = \mathcal { O } _ { X _ { \alpha } } \mathfrak { X } ^ { \lambda _ { \alpha } } \ , \ \mathrm { w h e r e } \ \mathfrak { X } ^ { \lambda _ { \alpha } } = \exp ( 2 \pi \mathrm { i } \langle \lambda _ { \alpha } , z \rangle ) \ .
$$

The $\{ { \mathcal { J } } _ { F , \alpha } \}$ define an ideal $\mathcal { J } _ { F }$ on $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} }$ since, if $\sigma _ { \alpha } \cap \sigma _ { \beta } = \sigma _ { \gamma }$ then on $X _ { \gamma }$ we have $\mathcal { J } _ { F , \gamma } = \mathcal { O } _ { X _ { \gamma } } \mathfrak { X } ^ { \lambda _ { \alpha } } = \mathcal { O } _ { X _ { \gamma } } \mathfrak { X } ^ { \lambda _ { \beta } }$ .

(2) If $F \subset { \overline { { F ^ { \prime } } } }$ , then $\overline { { C ( F ) } } \supset \overline { { C ( F ^ { \prime } ) } }$ , and we have the glueing map:

$$
\alpha _ { F ^ { \prime } , F } : ( D / U ( F ^ { \prime } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} } \longrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } .
$$

The $\{ \sigma _ { \alpha } ^ { F ^ { \prime } } \}$ are the cones $\sigma _ { \alpha } ^ { F } \cap \overline { { C ( F ^ { \prime } ) } }$ . We get $\alpha _ { F ^ { \prime } , F }$ by dividing out $U ( F ) _ { \mathbb { Z } }$ , plus an open immersion. If $\sigma _ { \alpha } ^ { F ^ { \prime } } = \sigma _ { \alpha } ^ { F } \cap \overline { { C ( F ^ { \prime } ) } }$ , then $\lambda _ { \alpha } = \lambda _ { \alpha } ^ { \prime }$ on $\sigma _ { \alpha } ^ { F ^ { \prime } }$ , hence

$$
\alpha _ { F ^ { \prime } , F } ^ { * } ( \mathcal { J } _ { F } ) = \mathcal { J } _ { F ^ { \prime } } .
$$

(3) Similarly, if $F ^ { \prime } = \gamma F$ for some $\gamma \in \Gamma$ , then we have

$$
\alpha _ { F ^ { \prime } , F } : ( D / U ( F ^ { \prime } ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} } \longrightarrow ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } ,
$$

with $\{ \sigma _ { \alpha } ^ { F ^ { \prime } } \} = \{ \gamma \sigma _ { \alpha } ^ { F } \}$ .Now, $\{ \lambda _ { \alpha } ^ { \prime } \}$ is just $\{ \gamma ^ { * } \lambda _ { \alpha } \}$ , hence

$$
\alpha _ { F ^ { \prime } , F } ^ { * } ( \mathcal { J } _ { F } ) = \mathcal { J } _ { F ^ { \prime } } .
$$

(4) As in Chapter III, Section 6, define

$$
\widetilde { { \cal D } / \Gamma } = \bigsqcup _ { F } ( { \cal D } / { \cal U } ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } .
$$

Let $\imath _ { F }$ be the injection  $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } \longrightarrow \widetilde { D / \Gamma }$ and define $\widehat { \mathcal { J } }$ on $\widetilde { D / \Gamma }$ as $\oplus _ { F } \imath _ { F , * } \mathcal { J } _ { F }$ .

(5) Let $p$ be the map $\widetilde { D / \Gamma } \longrightarrow \overline { { D / \Gamma } }$ , and define $\mathcal { J }$ by

$$
\Gamma ( U , { \mathcal { J } } ) = \left\{ s \in \Gamma ( p ^ { - 1 } ( U ) , \widetilde { { \mathcal { J } } } ) \mid \begin{array} { l } { \alpha _ { F ^ { \prime } , F } ^ { * } \iota _ { F } ^ { * } ( s ) = \iota _ { F ^ { \prime } } ^ { * } ( s ) \mathrm { ~ i f ~ } F \subset \overline { { F ^ { \prime } } } } \\ { \mathrm { ~ o r ~ } F ^ { \prime } = \gamma F \mathrm { ~ f o r ~ s o m e ~ } \gamma \in \Gamma } \end{array} \right\} \mathrm { . }
$$

It is easy to check that in each step we get a principal sheaf of ideals and that $\mathcal { J }$ is locally generated by $\mathfrak { X } ^ { \lambda _ { \alpha } }$ .

Proposition 2.11 Let $f : \overline { { D / \Gamma } } \longrightarrow D ^ { * } / \Gamma$ be the map defined in Chapter III, Section 5, and let $\mathcal { I } _ { m } = f _ { * } \mathcal { J } ^ { m }$ . Then

(1) ${ \mathcal { I } } _ { m }$ is a coherent sheaf of ideals.

(2) Let $x \in F / \Gamma ( F ) \subset D ^ { * } / \Gamma$ . Then $\mathcal { I } _ { m , x }$ is the ideal of holomorphic functions around $x$ such that in their Fourier–Jacobi series expansion,

$$
\sum \theta _ { \rho } \exp ( 2 \pi \mathrm { i } \langle \rho , z \rangle ) ,
$$

the coefficient $\theta _ { \rho } \neq 0$ only for $\rho \in U ( F ) _ { \mathbb { Z } } ^ { * } \cap C ( F )$ and $\varphi _ { F } ^ { * } ( \rho ) \geq m$ .

Proof (1) follows from Grauert’s coherency theorem, since $f$ is obviously proper.

To prove (2), let $V$ be an open neighborhood of $x$ in $D ^ { * } / \Gamma$ ; let $U$ be a connected component of the inverse image of $V$ in $D ^ { * }$ . We may choose $U$ as at the beginning of this section:

$$
U \cap D = \pi _ { F } ^ { - 1 } ( E ) \cap \Phi _ { F } ^ { - 1 } ( \ell C _ { 0 } ) .
$$

Let $U _ { \alpha } = U \cap \Phi _ { F } ^ { - 1 } ( \sigma _ { \alpha } ^ { F } )$ .Then

If $f \in \Gamma ( V , \mathcal { S } _ { m } )$ , consider the Fourier expansion of $f$ :

$$
f = \sum \theta _ { \rho } \exp ( 2 \pi \mathrm { i } \langle \rho , z \rangle ) \ .
$$

As above, let $P _ { i , \alpha }$ be the vertices of $\sigma _ { \alpha } ^ { F }$ , and let $D _ { i , \alpha }$ be the corresponding codimension-one strata of $U _ { \alpha } \backslash U _ { \alpha } \cap D$ . Then a term

$$
\begin{array} { r } { \theta _ { \rho } \exp ( 2 \pi \mathrm { i } \langle \rho - m \lambda _ { \alpha } , z \rangle ) } \end{array}
$$

of $f \cdot { \mathfrak { X } } ^ { - m \lambda _ { \alpha } }$ vanishes on $D _ { i , \alpha }$ to order $\langle \rho - m \lambda _ { \alpha } , P _ { i , \alpha } \rangle$ (or has a pole on $D _ { i , \alpha }$ if $\langle \rho - m \lambda _ { \alpha } , P _ { i , \alpha } \rangle < 0 )$ . Thus $f \in \Gamma ( V , \mathcal { S } _ { m } )$ implies that $\theta _ { \rho } \neq 0$ only when

$$
\langle \rho - m \lambda _ { \alpha } , P _ { i , \alpha } \rangle \geq 0 { \mathrm { f o r } } { \mathrm { a l l } } i , \alpha .
$$

But this means that

$$
\varphi _ { F } ^ { \ast } ( \rho ) = \operatorname* { m i n } \left. \rho , P _ { i , \alpha } \right. \geq \operatorname* { m i n } \left. m \lambda _ { \alpha } , P _ { i , \alpha } \right. = m .
$$

Conversely, if $\varphi _ { F } ^ { * } ( \rho ) \geq m$ whenever $\theta _ { \rho } \neq 0$ , then, by Proposition 2.10, the function $\boldsymbol { f } \cdot \mathfrak { X } ^ { - m \lambda _ { \alpha } }$ is bounded on $U \cap D \cap \Phi _ { F } ^ { - 1 } ( \sigma _ { \alpha } + a )$ , for all $\alpha$ and $a$ , hence extends holomorphically to $U _ { \alpha }$ .

# 2.3

We will now give the proof of Theorem 2.2. We shall in fact prove slightly more: namely, in the notation of Proposition 2.11, we shall prove that, for suitable $m$ ,

Step $I$ We first remark that it suffices to prove the theorem for some normal subgroup $\Gamma ^ { \prime }$ of finite index in $\Gamma$ .

Write $X = \overline { { D / \Gamma } }$ and $H = \Gamma / \Gamma ^ { \prime }$ , and let $X ^ { \prime } = \overline { { D / \Gamma ^ { \prime } } }$ be the compactification corresponding to the same $\{ \sigma _ { \alpha } ^ { F } \}$ . By uniqueness of $\overline { { D / \Gamma } }$ , we have

$$
X \cong X ^ { \prime } / H .
$$

Write $S = D ^ { * } / \Gamma$ and $S ^ { \prime } { = } D ^ { * } / \Gamma ^ { \prime }$ . The group $H$ acts on $S ^ { \prime }$ and defines a map $h : S ^ { \prime } \longrightarrow S$ which induces an isomorphism $S ^ { \prime } / H \cong S$ .

Lemma 2.12 $( h _ { * } \mathcal { S } _ { m } ^ { \prime } ) ^ { H } = \mathcal { S } _ { m }$ .

Proof Consider the following commutative diagram:

$$
\begin{array} { l } { { X ^ { \prime } \xrightarrow { g } \times X } } \\ { { \downarrow } } \\ { { V ^ { \prime } } } \\ { { S ^ { \prime } \xrightarrow { h } \quad h } } \end{array} \downarrow f
$$

We have $\mathcal { J }$ and ${ \mathcal { J } } ^ { \prime }$ on $X$ and $X ^ { \prime }$ , both are generated locally by $\mathfrak { X } ^ { \lambda _ { \alpha } }$ , and $f _ { * } \mathcal { J } ^ { m } = \mathcal { I } _ { m }$ and $f _ { * } ^ { \prime } \mathcal { J } ^ { \prime m } = \mathcal { S } _ { m } ^ { \prime }$ . Moreover $\mathcal { J }$ and ${ \mathcal { J } } ^ { \prime }$ are related by ${ \mathcal { J } } =$ $( g _ { * } \mathcal { J } ^ { \prime } ) ^ { H }$ ; hence

$$
\begin{array} { r } { ( h _ { \ast } \mathcal { I } _ { m } ^ { \prime } ) ^ { H } = ( h _ { \ast } f _ { \ast } ^ { \prime } \mathcal { J } ^ { m } ) ^ { H } = ( f _ { \ast } g _ { \ast } \mathcal { J } ^ { m } ) ^ { H } = f _ { \ast } ( g _ { \ast } \mathcal { J } ^ { \prime m } ) ^ { H } = f _ { \ast } \mathcal { J } ^ { \prime m } = \mathcal { I } _ { m } . } \end{array}
$$

Lemma 2.13 IfB $f ^ { \prime } { } ^ { * } { \mathcal { I } } _ { m } ^ { \prime } = { \mathcal { J } } ^ { \prime } { } ^ { m }$ , then $\mathcal { I } _ { m k } ^ { \prime }$ is the integral closure $\widehat { \mathcal { S } _ { m } ^ { \prime k } }$ of $\mathcal { I } _ { m } ^ { \prime k }$ for all $k \geq 1$ .

Proof Since $f ^ { \prime }$ is proper, whenever $f ^ { \prime * } { \mathcal { H } }$ is a sheaf of principal ideals, then $f _ { * } ^ { \prime } f ^ { \prime * } { \mathcal { H } } = { \widehat { \mathcal { H } } }$ . Therefore

$$
\mathcal { I } _ { m k } ^ { \prime } = f _ { * } ^ { \prime } ( \mathcal { J } ^ { m k } ) = f _ { * } ^ { \prime } f ^ { \prime * } ( \mathcal { I } _ { m } ^ { \prime k } ) = \widehat { \mathcal { I } _ { m } ^ { \prime k } } .
$$

Introduce the notation - - # $\widetilde { X } _ { \mathcal { I } }$ for the normalization of the blow-up of a variety $X$ along a coherent sheaf of ideals $\mathcal { I }$ . It is well known that

(a) $\widetilde { X } _ { \mathcal { I } } \cong \widetilde { X } _ { \mathcal { I } ^ { n } }$ for all $n \geq 1$ , (b) $\widetilde { X } _ { \mathcal { I } } \cong \widetilde { X } _ { \widehat { \mathcal { I } } }$ with $\hat { \mathcal { I } }$ the integral closure of $\mathcal { I }$ .

We will apply the general fact:

Lemma 2.14 Let $X$ be a normal quasi-projective variety, let $H$ be a finite group acting on $X$ , and let $\mathcal { I }$ be an $H$ -invariant coherent sheaf of ideals on= $X$ . If $n$ denotes the order of $H _ { \mathrm { { ; } } }$ , and $\pi : X \longrightarrow X / H$ the canonical map and $\mathcal { J } = \pi _ { * } ( \mathcal { S } ^ { n } ) ^ { H }$ , then

$$
\widetilde { X } _ { \mathcal { I } } / { H } \cong \widetilde { ( X / H ) } _ { \mathcal { J } } ~ .
$$

Moreover, $\mathcal { J }$ induces the ideal - $\mathcal { S } ^ { n } \cdot \mathcal { O } _ { \widetilde { X } _ { \mathcal { I } } }$ on $\widetilde { X } _ { I }$

Proof It is easy to check that

$$
\widetilde { X } _ { \pi ^ { * } { \mathcal J } } / H \cong \widetilde { ( X / H ) } _ { { \mathcal J } } ~ ,
$$

and hence the lemma follows if we prove that - - ${ \widehat { \mathcal { I } } } ^ { n } = { \widehat { \pi } } ^ { * } { \widehat { \mathcal { I } } }$ . To do this, itsuffices to prove that ${ \mathcal { S } } ^ { n }$ and $\pi ^ { * } { \mathcal { J } }$ generate the same sheaf of ideals on $\widehat { X } _ { \mathcal { I } }$ . The difficult point here is to check that $\mathcal { J }$ generates the full sheaf $( \mathcal { I } \cdot \mathcal { O } _ { \widetilde { X } _ { \mathcal { I } } } ) ^ { n }$ . Take any point $\widetilde { x } \in \widetilde { X } _ { \mathcal { I } }$ , let $x$ be its image in- $X$ , and let $U \subset X$ be an $H$ -invariant affine neighborhood of $x$ . It is easy to see that there is an $f \in \Gamma ( U , { \mathcal { S } } )$ thatgenerates the principal ideal sheaf $\mathcal { I } \cdot \mathcal { O } _ { \widetilde { X } _ { \mathcal { I } } }$ at each of the points $\sigma \widetilde { x }$ , $\sigma \in H$ . Then $f ^ { \prime } { = } \Pi _ { \sigma \in H } ( \sigma f )$ is a section of $\mathcal { J }$ XI on $U / H$ which generates B $( \mathcal { I } \cdot \mathcal { O } _ { \widetilde { X } _ { \mathcal { I } } } ) ^ { n }$ at $\widetilde { x }$ . −

Corollary 2.15 The same thing holds if we let $\mathcal { J }$ equal $\pi _ { * } ( \widehat { \mathcal { I } ^ { n } } ) ^ { H }$ .

Proof The same proof works in fact.

Now, assuming the theorem for $\Gamma ^ { \prime }$ , we have an $m$ such that

$$
X ^ { \prime } \cong \widetilde { S } _ { \mathcal { I } _ { m } ^ { \prime } } ^ { \prime } \ , f ^ { \prime * } \mathcal { I } _ { m } ^ { \prime } = \mathcal { J } ^ { \prime m } \ .
$$

Therefore, by Lemmas 2.12 and 2.13,

$$
( h _ { * } \widehat { ( \mathcal { I } _ { m } ^ { \prime } ) ^ { k } } ) ^ { H } = ( h _ { * } \mathcal { I } _ { m k } ^ { \prime } ) ^ { H } = \mathcal { I } _ { m k } ,
$$

and, by Lemma 2.14,

$$
X \cong X ^ { \prime } / H \cong \widetilde { S } _ { \mathcal { S } _ { m } ^ { \prime } } ^ { \prime } / H \cong ( \widetilde { S ^ { \prime } / H } ) _ { \mathcal { I } _ { m k } } = \widetilde { S } _ { \mathcal { I } _ { m k } } \ ,
$$

and $\mathcal { I } _ { m k }$ induces the ideal $\mathcal { J } ^ { \prime m k }$ on $X ^ { \prime }$ , hence $\mathcal { I } _ { m k }$ induces the ideal ${ \mathcal { J } } ^ { m k }$ on $X$ .

Step $\boldsymbol { { I I } }$ Since, by Step I, it suffices to prove the theorem for some normal subgroup of finite index of $\Gamma$ , we can make the following assumption about $\Gamma$ .

For each $\sigma _ { \alpha } ^ { F }$ , let $\widetilde { \sigma } _ { \alpha } ^ { F } = \sigma _ { \alpha } ^ { F } \backslash \sigma _ { \alpha } ^ { F } \cap \partial { \cal C } ( F )$ . (When there is no confusion, we shall drop the superscript or subscript $F$ .)

Assumption $\langle \lambda _ { \alpha } , x \rangle < \langle A ^ { * } \lambda _ { \alpha } , x \rangle$ for all $x \in \tilde { \sigma } _ { \alpha }$ , ${ \mathrm { i d } } \neq A \in { \overline { { \Gamma } } } _ { F }$ .

This assumption is justified for the following reason. There are only finitely many $A \in { \overline { { \Gamma } } } _ { F }$ such that $A \sigma _ { \alpha } \cap \sigma _ { \alpha } \cap C ( F ) \neq \emptyset$ ; since there are only finitely many $\sigma _ { \alpha }$ modulo $\overline { { \Gamma } } _ { F }$ , we may take a subgroup $\Gamma ^ { \prime }$ of finite index (e.g., a suitable congruence subgroup) such that all such $A$ are not in $\overline { { \Gamma } } _ { F } ^ { \prime }$ for all $F$ .

With the above assumption, we have:

# Proposition 2.16

(1) Let $x _ { n } = ( t _ { n } , u _ { n } , z _ { n } )$ be a sequence in $D$ , with $\mathrm { l i m } ( t _ { n } , u _ { n } ) = ( \bar { t } , \overline { { u } } )$ , $\operatorname* { l i m } \mathbf { R e } z _ { n } =$ $\textstyle { \overline { { x } } }$ and l $\mathrm { i m I m } z _ { n } = \overline { { y } } + \infty \cdot \sigma _ { \gamma } ,$ where $\sigma _ { \gamma }$ is a face of the top-dimensional $\sigma _ { \alpha }$ and Int $\sigma _ { \gamma } \subset C ( F )$ . Then

$$
\operatorname * { l i m } _ { n \longrightarrow \infty } f _ { \theta _ { m \lambda _ { \alpha } } } ( x _ { n } ) { \mathfrak X } ^ { - m \lambda _ { \alpha } } ( z _ { n } ) = \theta _ { m \lambda _ { \alpha } } ( \bar { t } , \overline { { u } } ) .
$$

(2) Assume further that $\sigma _ { \gamma }$ is $a$ face of the top-dimensional $\sigma _ { \alpha }$ and $\sigma _ { \beta }$ , with $\theta _ { m \lambda _ { \alpha } } ( \bar { t } , \overline { { u } } ) \not = 0$ , and let $\overline { { z } } = \overline { { x } } + \mathrm { i }$ y. Then

$$
\operatorname* { l i m } _ { n \longrightarrow \infty } \frac { f _ { \theta _ { m \lambda _ { \beta } } } \left( x _ { n } \right) } { f _ { \theta _ { m \lambda _ { \alpha } } } \left( x _ { n } \right) } = \mathfrak { X } ^ { m ( \lambda _ { \beta } - \lambda _ { \alpha } ) } ( \bar { z } ) \cdot \frac { \theta _ { m \lambda _ { \beta } } \left( \bar { t } , \overline { { u } } \right) } { \theta _ { m \lambda _ { \alpha } } \left( \bar { t } , \overline { { u } } \right) } \ .
$$

Proof For the proof of (1), by the same argument as in Proposition 2.8,

$$
\left| \theta _ { m A ^ { * } \lambda _ { \alpha } } \mathfrak { X } ^ { m ( A ^ { * } \lambda _ { \alpha } - \lambda _ { \alpha } ) } ( z _ { n } ) \right| \le \mathrm { c o n s t . } \cdot \exp ( - 2 \pi m \langle A ^ { * } \lambda _ { \alpha } - \lambda _ { \alpha } , \mathrm { I m } z _ { n } \rangle ) ~ .
$$

By the assumption on $\Gamma$ , for $A \neq \mathrm { i d }$ , we have that $A ^ { * } \lambda _ { \alpha } - \lambda _ { \alpha }$ is positive on $\sigma _ { \gamma }$ ,and $\left. A ^ { * } \lambda _ { \alpha } - \lambda _ { \alpha } , \mathrm { I m } z _ { n } \right. \longrightarrow \infty$ uniformly as $n \longrightarrow \infty$ ; therefore, except for $A = \mathrm { i d }$ , every term of $f _ { \theta _ { m \lambda _ { \alpha } } } \cdot \mathfrak { X } ^ { - m \lambda _ { \alpha } } \left( z _ { n } \right)$ tends to zero uniformly.

(2) follows from (1), since $\mathrm { I m } z _ { n } = \overline { { y } } + \pmb { \varepsilon } _ { n } + w _ { n }$ with $\varepsilon _ { n } \longrightarrow 0 , w _ { n } \in \sigma _ { \gamma }$ ; hence

$$
\begin{array} { r } { \operatorname* { l i m } { \mathfrak { X } } ^ { \lambda _ { \beta } - \lambda _ { \alpha } } ( z _ { n } ) = \operatorname* { l i m } \exp ( - 2 \pi \mathrm { i } \langle \lambda _ { \beta } - \lambda _ { \alpha } , { \bar { z } } + \varepsilon _ { n } + w _ { n } \rangle ) = { \mathfrak { X } } ^ { \lambda _ { \beta } - \lambda _ { \alpha } } ( { \bar { z } } ) ~ . } \end{array}
$$

For later use, we may put (2) in a slightly more general form. Define # $\widehat { \sigma } _ { \alpha } =$ $\{ \lambda \in U ( F ) ^ { * } \mid \lambda \geq 0 \mathrm { o n } \sigma _ { \alpha } \}$ .

Since $\{ \sigma _ { \alpha } \}$ is the biggest decomposition such that $\lambda _ { \alpha }$ is linear on each $\sigma _ { \alpha }$ it follows that $\widehat { \sigma } _ { \alpha }$ is generated by the $\lambda _ { \beta } - \lambda _ { \alpha }$ , where $\beta$ runs through the topdimensional simplices such that $\sigma _ { \beta } \cap \sigma _ { \alpha }$ has codimension one.

Let $I _ { \gamma } = \{ \lambda \in \widehat { \sigma } _ { \alpha } \cap U ( F ) _ { \mathbb { Z } } ^ { * } | \lambda \equiv 0$ on $\sigma _ { \gamma } \}$ . Then $I _ { \gamma }$ is generated by the $\lambda _ { \beta _ { i } } -$ $\lambda _ { \alpha }$ with $\lambda _ { \beta _ { i } } \equiv \lambda _ { \alpha }$ on $\sigma _ { \gamma }$ ,i.e., every $\lambda \in I _ { \gamma }$ is of the form $\begin{array} { r } { \lambda = \sum a _ { i } ( \lambda _ { \beta _ { i } } - \lambda _ { \alpha } ) } \end{array}$ where the $a _ { i }$ are positive rational numbers.

There exists $k \in \mathbb { Z } _ { \geq 0 }$ such that $\lambda + k \lambda _ { \alpha } \in C ( F )$ , and is a positive linear combination of the $\lambda _ { \beta _ { i } }$ and $\lambda _ { \alpha }$ ; hence

$$
\begin{array} { r } { \langle \lambda + k \lambda _ { \alpha } , x \rangle < \langle \lambda + k \lambda _ { \alpha } , A x \rangle \ , \ \mathrm { f o r ~ a l l ~ i d } \neq A \in \overline { { \Gamma } } _ { F } \ , \ x \in \mathrm { I n t } \sigma _ { \gamma } \ . } \end{array}
$$

Proposition 2.17 With the same notation as in Proposition 2.16, and for $\lambda , k$ as above, if $\theta _ { k \lambda _ { \alpha } } ( \bar { t } , \overline { { u } } ) \not = 0$ , then

$$
\operatorname* { l i m } _ { n \longrightarrow \infty } \frac { f _ { \theta _ { \lambda + k \lambda _ { \alpha } } } ( x _ { n } ) } { f _ { \theta _ { k \lambda _ { \alpha } } } ( x _ { n } ) } = \frac { \theta _ { \lambda + k \lambda _ { \alpha } } ( \bar { t } , \overline { { u } } ) } { \theta _ { k \lambda _ { \alpha } } ( \bar { t } , \overline { { u } } ) } \mathfrak { X } ^ { \lambda } ( \bar { z } ) \ .
$$

Step III Recall from Chapter III, Section 5 the following commutative diagram:

$$
\begin{array} { l l l l } { { D / U ( F ) _ { \mathbb { Z } } } } & { { \longrightarrow } } & { { ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } ^ { F } \} } } } \\ { { \downarrow } } & { { } } & { { } } & { { \downarrow \pi _ { F } } } \\ { { \vphantom { \int } } } & { { } } & { { \vphantom { \int } } } & { { \vphantom { \int } } } \\ { { D / \Gamma } } & { { \longrightarrow } } & { { \frac { \vphantom { \int } } { D / \Gamma } } } \end{array}
$$

The map $\pi _ { F }$ is etale, ´ $\sqcup \pi _ { F }$ is surjective, and $\overline { { D / \Gamma } }$ is the unique compact analytic space with these properties. Consider the map

$$
f : \overline { { { D / \Gamma } } } \longrightarrow D ^ { * } / \Gamma .
$$

By Proposition 2.11, $f ^ { * } { \mathcal { I } } _ { m }$ is a subsheaf of ${ \mathcal { J } } ^ { m }$ . By Proposition 2.16, (1), if $m \geq 2$ , then ${ \mathcal { I } } _ { m }$ has a section at each point which, locally on $\overline { { D / \Gamma } }$ , is a unit times ${ \mathfrak { X } } ^ { m \lambda _ { \alpha } }$ : this is because, if = $m \geq 2$ , then $\mathcal { L } _ { m \lambda _ { \alpha } } | _ { \pi ^ { - 1 } ( E ) }$ is generated by its sections, so we can find $\theta _ { m \lambda _ { \alpha } }$ with $\theta _ { m \lambda _ { \alpha } } ( \bar { t } , \overline { { u } } ) \not = 0$ . Therefore, if $m \geq 2$ , we have $f ^ { * } { \mathcal { I } } _ { m } = { \mathcal { J } } ^ { m }$ , hence $f ^ { * } { \mathcal { I } } _ { m }$ is principal. Since $\overline { { D / \Gamma } }$ is normal, by the universal property of $Y = ( \bar { D } / \Gamma ) _ { \mathcal { S } }$ , there is an analytic morphism $\psi$ such that the following diagram is commutative:

$$
\overline { { D / \Gamma } } \xrightarrow [ \Gamma ] { \quad \quad } \overline { { \sum _ { f \quad \searrow \quad \swarrow \quad } ^ { \psi } Y } }
$$

We shall prove that $\psi$ is a local isomorphism, i.e.,

$$
\psi ^ { * } : \mathcal { O } _ { y } \stackrel { \sim } { \longrightarrow } \mathcal { O } _ { x } \mathrm { , \ f o r \ a l l \ } x \in D / \Gamma \mathrm { , \ w h e r e \ } y = \psi ( x ) \mathrm { . }
$$

Then $Y$ will have the property characterizing $\overline { { D / \Gamma } }$ , and hence $\psi$ will be an isomorphism.

Step $I V$ Since $\psi$ induces the identity map on $D / \Gamma$ , it is clear that $\psi ^ { * }$ is injective, so it suffices to prove $\psi ^ { * }$ is surjective, and again we only need to check this for each stratum of (D/U(F)Z){σα}.

We first recall the notion of strata of $( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } }$

For each face $\sigma _ { \gamma }$ of $\sigma _ { \alpha }$ , we have the orbit $\mathbb { O } ^ { \gamma }$ of $T ( F )$ in $T ( F ) _ { \sigma _ { \alpha } }$ , cf. TE I, Ch. I; see also Chapter I, Section 1.

Let $S _ { \gamma }$ be the subset of $( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } }$ given by>

$$
S _ { \gamma } = ( D ( F ) / U ( F ) _ { \mathbb { Z } } ) \times ^ { T ( F ) } \mathbb { O } ^ { \gamma } .
$$

Then $( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } }$ can be broken up into $\bigcup S _ { \gamma }$ . For $x \in S _ { \gamma }$ , $\mathcal { O } _ { S _ { \gamma } , x }$ is generated by $t , u$ , and by ${ \mathfrak { X } } ^ { \lambda }$ with $\lambda \in I _ { \gamma } = \{ \lambda \in U ( F ) _ { \mathbb { Z } } ^ { * } \mid \lambda \equiv 0$ on $\sigma _ { \gamma } \}$ .

We have a sequence of maps:

$$
S _ { \gamma } { \stackrel { \iota _ { \gamma } } { \longleftrightarrow } } ( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} } { \stackrel { \pi _ { F } } { \longrightarrow } } \overline { { D / \Gamma } } { \stackrel { \psi } { \longrightarrow } } Y \ .
$$

Claim To prove $\psi ^ { * }$ is surjective, it is sufficient to prove that $( \psi \circ \pi _ { F } \circ \iota _ { \gamma } ) ^ { * }$ is surjective for all $F$ , $\alpha$ , γ.

Proof of the claim Indeed, assume $\psi ^ { * }$ is not surjective at $y \in Y$ . Then there is a curve in $\overline { { D / \Gamma } }$ mapping to $y$ under $\psi$ . (By Zariski’s Main Theorem, if $\psi ^ { - 1 } ( y )$ is finite, then $\psi$ is a local isomorphism at each point of $\psi ^ { - 1 } ( y )$ .) Hence there is a curve in $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} }$ mapping to $y$ under $\psi \circ \pi _ { F }$ for some $F$ . It follows that, for some stratum $S _ { \gamma }$ in $( D / U ( F ) _ { \mathbb { Z } } ) _ { \sigma _ { \alpha } }$ , there is a curve in $S _ { \gamma }$ mapping to $y$ under $\psi \circ \pi _ { F } \circ \iota _ { \gamma }$ .

If we can prove that $( \psi \circ \pi _ { F } \circ \iota _ { \gamma } ) ^ { * }$ is surjective at $y$ for all $F , \alpha , \gamma .$ , then such a curve cannot occur in any stratum $S _ { \gamma }$ , and hence $\psi ^ { * }$ is surjective. □

By this reduction step, we only need to consider the situation

$$
\psi : S _ { \gamma } \longrightarrow Y \ ,
$$

with $x \in S _ { \gamma } .$ , $\psi ( x ) = y \in Y$ , and to prove that $\psi ^ { * } \mathcal { O } _ { Y , y } = \mathcal { O } _ { S _ { \gamma } , x }$

Note that, if $S _ { \gamma }$ is a stratum in $( D / U ( F ) _ { \mathbb { Z } } ) _ { \{ \sigma _ { \alpha } \} }$ , we may choose $F$ to be the associated boundary component of $x$ , i.e., Int $\operatorname { \mathrm { : } } \sigma _ { \gamma } \subset C ( F )$ .

The local ring $\mathcal { O } _ { S _ { \gamma } , x }$ is generated by $t , u ,$ , and ${ \mathfrak { X } } ^ { \lambda }$ with $\lambda \in I _ { \gamma }$ . Let $t ( x ) = { \bar { t } }$ $u ( x ) = \overline { { u } }$ .

We now assume $m \geq 3$ , so that $\mathcal { L } _ { m \lambda _ { \alpha } } | _ { \pi ^ { - 1 } ( \bar { t } ) }$ is very ample and we can choose mλα ∈ $\theta _ { m \lambda _ { \alpha } } ^ { ( i ) } \in \Gamma ( \pi ^ { - 1 } ( \bar { t } ) , \mathcal { L } _ { m \lambda _ { \alpha } } )$ with $0 \leq i \leq \dim V ( F )$ so that

$$
u \longmapsto { \frac { \theta _ { m \lambda _ { \alpha } } ^ { ( i ) } ( { \bar { t } } , u ) } { \theta _ { m \lambda _ { \alpha } } ^ { ( 0 ) } ( { \bar { t } } , u ) } }
$$

is a local isomorphism at $\bar { u }$ . Therefore, $\mathcal { O } _ { S _ { \gamma } , x }$ is generated by $t ,$ $\frac { \theta _ { m \lambda \alpha } ^ { ( i ) } } { \theta _ { m \lambda \alpha } ^ { ( 0 ) } }$ and ${ \mathfrak { X } } ^ { \lambda }$ for $\lambda \in I _ { \gamma }$ .

Applying Proposition 2.16, (2) for $f _ { \theta _ { m \lambda _ { c } } ^ { ( i ) } }$ , we know that all the $\theta$ ’s are in $\psi ^ { * } \mathcal { O } _ { Y , y }$ Then applying Proposition . ${ \mathfrak { X } } ^ { \lambda }$ with $\lambda \in I _ { \gamma }$ are in $\psi ^ { * } \mathcal { O } _ { Y , y }$ Hence $\psi ^ { * }$ is surjective, and the proof of Theorem 2.2 is complete.

# References

[1] W. L. Baily, Fourier–Jacobi series, in Proc. Symp. Pure Math IX. Providence, RI: American Mathematical Society, 1966, pp. 296–300,   
[2] W. L. Baily and A. Borel, Compactification of arithmetic quotients of bounded symmetric domains, Ann. of Math. 84 (1966), 442–528.   
[3] A. Borel and Harish-Chandra, Arithmetic subgroups of algebraic groups, Ann. of Math. 75 (1962), 485–535.   
[4] F. Hirzebruch, Hilbert Modular Surfaces. Monographie No. 21 de L’Enseignement Mathematique, 1973.   
[5] I. Igusa, A desingularization problem in the theory of Siegel modular functions, Math. Ann. 168 (1967), 228–260.   
[6] I. Igusa, On the theory of compactifications, in AMS Summer Institute on Algebraic Geometry, Woods Hole, (1964), Lecture Note.   
[7] A. Koranyi and J. Wolf, Generalized Cayley transformations of bounded ´ symmetric domains, Am. J. Math. 87 (1965), 899–939.   
[8] D. Mumford, Abelian Varieties. Oxford: Oxford University Press, 1970. [9] I. Piatetskii-Shapiro, Geometry of Classical Domains and Theory of Automorphic Functions. New York: Gordon and Breach, 1969.

# Supplementary Bibliography

The following is a list of references to the more recent literature in the subject.

# Survey Papers and General Expositions

[1] Ching-Li Chai. Compactification of Siegel Moduli Schemes, volume 107 of London Mathematical Society Lecture Note Series. Cambridge University Press, Cambridge, 1985.

[2] Ching-Li Chai. Arithmetic compactification of the Siegel moduli space. In Theta functions—Bowdoin 1987, Part 2 (Brunswick, ME, 1987), volume 49 of Proc. Sympos. Pure Math., pages 19–44. Amer. Math. Soc., Providence, RI, 1989

[3] Gerd Faltings and Ching-Li Chai. Degeneration of Abelian Varieties, volume 22 of Ergebnisse der Mathematik und ihrer Grenzgebiete (Series 3). Springer-Verlag, Berlin, 1990. With an appendix by David Mumford.

[4] Mark Goresky. Compactifications and cohomology of modular varieties. In Harmonic Analysis, the Trace Formula, and Shimura Varieties, volume 4 of Clay Math. Proc., pages 551–582. Amer. Math. Soc., Providence, RI, 2005.

[5] K. Hulek and G. K. Sankaran. The geometry of Siegel modular varieties.   
In Higher Dimensional Birational Geometry (Kyoto, 1997), volume 35 of Adv.   
Stud. Pure Math., pages 89–156. Math. Soc. Japan, Tokyo, 2002.

[6] Klaus Hulek, Constantin Kahn, and Steven H. Weintraub. Moduli Spaces of Abelian Surfaces: Compactification, Degenerations, and Theta Functions, volume 12 of de Gruyter Expositions in Mathematics. Walter de Gruyter & Co., Berlin, 1993.

[7] Lizhen Ji. Buildings and their applications in geometry and topology. Asian J. Math., 10(1):11–80, 2006.

[8] Lizhen Ji. Arithmetic Groups and their Generalizations: What, Why, and How, volume 43 of AMS/IP Studies in Advanced Mathematics. American Mathematical Society, Providence, RI, 2008.

[9] Yukihiko Namikawa. Toroidal Compactification of Siegel Spaces, volume 812 of Lecture Notes in Mathematics. Springer-Verlag, Berlin, 1980.

[10] Ichiro Satake. ˆ Algebraic Structures of Symmetric Domains, volume 4 of Kano Memorial Lectures ˆ . Iwanami Shoten, Tokyo, 1980.

[11] Ichiro Satake. ˆ Compactifications, Old and New. Sugaku Expositions, 14(2):175–189, 2001. [Translation of Sugaku ¯ 51 (1999), no. 2, 129–141.]

[12] Gerard van der Geer. Hilbert Modular Surfaces, volume 16 of Ergebnisse der Mathematik und ihrer Grenzgebiete (Series 3). Springer-Verlag, Berlin, 1988.

[13] Gerard van der Geer and Frans Oort. Moduli of abelian varieties: a short introduction and survey. In Moduli of Curves and Abelian Varieties, Aspects Math., E33, pages 1–21. Vieweg, Braunschweig, 1999.

# Geometric applications and classification problems

[1] Alessandro Arsie. Very ampleness of multiples of principal polarization on degenerate abelian surfaces. Rev. Mat. Complut., 18(1):119–141, 2005.

[2] C. Erdenberger. The Kodaira dimension of certain moduli spaces of abelian surfaces. Math. Nachr., 274/275:32–39, 2004.

[3] Eberhard Freitag. Die Kodairadimension von Korpern automorpher Funk- ¨ tionen. J. Reine Angew. Math., 296:162–170, 1977.

[4] V. Gritsenko, K. Hulek, and G. K. Sankaran. The Hirzebruch-Mumford volume for the orthogonal group and applications. Doc. Math., 12:215–241 (electronic), 2007.

[5] V. Gritsenko, K. Hulek, and G. K. Sankaran. The Kodaira dimension of the moduli of $K 3$ surfaces. Invent. Math., 169(3):519–567, 2007.

[6] J. William Hoffman and Steven H. Weintraub. Cohomology of the Siegel modular group of degree two and level four, Mem. Amer. Math. Soc., 133(631):ix,59–75, 1998.

[7] J. William Hoffman and Steven H. Weintraub. The Siegel modular variety of degree two and level three. Trans. Amer. Math. Soc., 353(8):3267–3305 (electronic), 2001.

[8] Rolf-Peter Holzapfel. Ball and Surface Arithmetics. Aspects of Mathematics, E29. Friedr. Vieweg & Sohn, Braunschweig, 1998.

[9] K. Hulek and G. K. Sankaran. The Kodaira dimension of certain moduli spaces of abelian surfaces. Compositio Math., 90(1):1–35, 1994.

[10] K. Hulek and G. K. Sankaran. The nef cone of toroidal compactifications of ${ \mathcal { A } } _ { 4 }$ . Proc. London Math. Soc. (3), 88(3):659–704, 2004.

[11] Klaus Hulek. Nef divisors on moduli spaces of abelian varieties. In Complex Analysis and Algebraic Geometry, pages 255–274. de Gruyter, Berlin, 2000.

[12] Klaus Hulek. Igusa’s modular form and the classification of Siegel modular threefolds. In Moduli of abelian varieties (Texel Island, 1999), volume 195 of Progr. Math., pages 217–229. Birkhauser, Basel, 2001.¨

[13] Jun-Muk Hwang. On the volumes of complex hyperbolic manifolds with cusps. Internat. J. Math., 15(6):567–572, 2004.

[14] Jun-ichi Igusa. A desingularization problem in the theory of Siegel modular functions. Math. Ann., 168:228–260, 1967.

[15] Friedrich W. Knoller. ¨ Uber die Plurigeschlechter Hilbertscher Modulman- ¨ nigfaltigkeiten. Math. Ann., 264(4):413–422, 1983.

[16] Shigeyuki Kondo. On the Kodaira dimension of the moduli space of ¯ $K 3$ surfaces, Compositio Math., 89(3):251–299, 1993.

[17] David Mumford. On the Kodaira dimension of the Siegel modular variety. In Algebraic Geometry—Open Problems (Ravello, 1982), volume 997 of Lecture Notes in Math., pages 348–375, Springer, Berlin, 1983.

[18] E. Oeljeklaus and C. Schmerling. Hyperbolicity properties of quotient surfaces by freely operating arithmetic lattices. Ann. Inst. Fourier (Grenoble), 50(1):197–210, 2000.

[19] G. K. Sankaran. Fundamental group of locally symmetric varieties.   
Manuscripta Math., 90(1):39–48, 1996.

[20] G. K. Sankaran. Moduli of polarised abelian surfaces. Math. Nachr., 188:321–340, 1997.

[21] G. K. Sankaran and J. G. Spandaw. The moduli space of bilevel-6 abelian surfaces. Nagoya Math. J., 168:113–125, 2002.

[22] Eric Schellhammer. The Kodaira dimension of Siegel modular varieties of genus 3 or higher. Boll. Unione Mat. Ital. Sez. B Artic. Ric. Mat. (8), 9(3):749– 776, 2006.

[23] N. I. Shepherd-Barron. Perfect forms and the moduli space of abelian varieties. Invent. Math., 163(1):25–45, 2006.

[24] Yung-Sheng Tai. On the Kodaira dimension of the moduli space of abelian varieties. Invent. Math., 68(3):425–439, 1982.

[25] Yung-Sheng Tai. On the Kodaira dimension of moduli spaces of abelian varieties with non-principal polarizations. In Abelian varieties (Egloffstein, 1993), pages 293–302. de Gruyter, Berlin, 1995.

[26] Wing-Keung To. Total geodesy of proper holomorphic immersions between complex hyperbolic space forms of finite volume. Math. Ann., 297(1):59–84, 1993.

[27] R. Weissauer. Untervarietaten der Siegelschen Modulmannigfaltigkeiten ¨ von allgemeinem Typ, Math. Ann., 275(2):207–220, 1986.

[28] R. Weissauer. The Picard group of Siegel modular threefolds. J. Reine Angew. Math., 430: 179–211, 1992. With an erratum by the author: “Differential forms attached to subgroups of the Siegel modular group of degree two” [J. Reine Angew. Math. 391: 100–156, 1988; MR0961166 (89i:32074)].

[29] Jorg Zintl. Invariants of moduli spaces of abelian surfaces. ¨ Internat. J.   
Math., 11(1):113–131, 2000.

# Cohomological applications

[1] Jonas Bergstrom, Carel Faber, and Gerard van der Geer. Siegel modular ¨ forms of genus 2 and level 2: cohomological computations and conjectures. Int. Math. Res. Not. IMRN, Art. ID rnn 100, 20, 2008.

[2] Jan H. Bruinier, Jose I. Burgos Gil, and Ulf K ´ uhn. Borcherds products and ¨ arithmetic intersection theory on Hilbert modular surfaces. , Duke Math. J., 139(1):1–88, 2007.

[3] Jose I. Burgos and J ´ org Wildeshaus. Hodge modules on Shimura varieties ¨ and their higher direct images in the Baily-Borel compactification, Ann. Sci. Ecole Norm. Sup. (4) ´ , 37(3):363–413, 2004.

[4] W. Casselman. Introduction to the $L ^ { 2 }$ -cohomology of arithmetic quotients of bounded symmetric domains. In Complex Analytic Singularities, volume 8 of Adv. Stud. Pure Math., pages 69–93. North-Holland, Amsterdam, 1987.

[5] Torsten Ekedahl and Gerard van der Geer. Cycles representing the top Chern class of the Hodge bundle on the moduli space of abelian varieties. Duke Math. J., 129(1):187–199, 2005.

[6] Carel Faber and Gerard van der Geer. Sur la cohomologie des systemes \` locaux sur les espaces de modules des courbes de genre 2 et des surfaces abeliennes. I. ´ C. R. Math. Acad. Sci. Paris, 338(5):381–384, 2004.

[7] Carel Faber and Gerard van der Geer. Sur la cohomologie des systemes \` locaux sur les espaces de modules des courbes de genre 2 et des surfaces abeliennes. II. ´ C. R. Math. Acad. Sci. Paris, 338(6):467–470, 2004.

[8] Gerd Faltings. On the cohomology of locally symmetric Hermitian spaces. In Paul Dubreil and Marie-Paule Malliavin algebra seminar, 35th year (Paris, 1982), volume 1029 of Lecture Notes in Math., pages 55–98. Springer, Berlin, 1983.

[9] M. Goresky, G. Harder, and R. MacPherson. Weighted cohomology. Invent.   
Math., 116(1-3):139–213, 1994.

[10] M. Goresky, G. Harder, R. MacPherson, and A. Nair. Local intersection cohomology of Baily–Borel compactifications. Compositio Math., 134(3):243–268, 2002.

[11] Mark Goresky and Robert MacPherson. The topological trace formula. J.   
Reine Angew. Math., 560:77–150, 2003.

[12] Mark Goresky and William Pardon. Chern classes of automorphic vector bundles. Invent. Math., 147(3):561–612, 2002.

[13] Michael Harris. Automorphic forms and the cohomology of vector bundles on Shimura varieties. In Automorphic forms, Shimura varieties, and $L$ - functions, Vol. II (Ann Arbor, MI, 1988), volume 11 of Perspect. Math., pages 41–91. Academic Press, Boston, MA, 1990.

[14] Michael Harris. Automorphic forms of $\overline { { \partial } }$ -cohomology type as coherent cohomology classes. J. Differential Geom., 32(1):1–63, 1990.

[15] Michael Harris and Steven Zucker. Boundary cohomology of Shimura varieties. I. Coherent cohomology on toroidal compactifications. Ann. Sci. Ecole ´ Norm. Sup. (4), 27(3):249–344, 1994.

[16] Michael Harris and Steven Zucker. Boundary cohomology of Shimura varieties. II. Hodge theory at the boundary. Invent. Math., 116(1-3):243–308, 1994.

[17] Michael Harris and Steven Zucker. Boundary cohomology of Shimura varieties. III. Coherent cohomology on higher-rank boundary strata and applications to Hodge theory. Mem. Soc. Math. Fr. (N.S.) ´ , 85:vi+116, 2001.

[18] J. William Hoffman and Steven H. Weintraub. Cohomology of the boundary of Siegel modular varieties of degree two, with applications. Fund. Math., 178(1):1–47, 2003.

[20] E. Looijenga and M. Rapoport. Weights in the local cohomology of a Baily–Borel compactification. In Complex Geometry and Lie Theory (Sundance, UT, 1989), volume 53 of Proc. Sympos. Pure Math., pages 223–260. Amer. Math. Soc., Providence, RI, 1991.

[20] Eduard Looijenga. $L ^ { 2 }$ -cohomology of locally symmetric varieties. Compositio Math., 67(1):3–20, 1988.

[21] David Mumford. Hirzebruch’s proportionality theorem in the noncompact case. Invent. Math., 42:239–272, 1977.

[22] Richard Pink. On the calculation of local terms in the Lefschetz–Verdier trace formula and its application to a conjecture of Deligne. Ann. of Math. (2), 135(3):483–525, 1992.

[23] Leslie Saper. On the cohomology of locally symmetric spaces and of their compactifications. In Current Developments in Mathematics, 2002, pages 219– 289. Int. Press, Somerville, MA, 2003.

[24] Leslie Saper. $L ^ { 2 }$ -cohomology of locally symmetric spaces. I. Pure Appl.   
Math. Q.,1(4, part 3):889–937, 2005.

[25] Leslie Saper. $\mathcal { L }$ -modules and the conjecture of Rapoport and Goresky– MacPherson. In Automorphic forms. I, Asterisque ´ , 298:319–334, 2005.

[26] Leslie Saper and Mark Stern. $L _ { 2 }$ -cohomology of arithmetic varieties. Ann.   
of Math. (2), 132(1):1–69, 1990.

[27] Gerard van der Geer. The Chow ring of the moduli space of abelian threefolds. J. Algebraic Geom., 7(4):753–770, 1998.

[28] Steven Zucker. On the reductive Borel-Serre compactification: $L ^ { p }$ - cohomology of arithmetic groups (for large $p$ ). Amer. J. Math., 123(5):951– 984, 2001.

# Papers with an arithmetic flavor or functor descriptions

[1] Valery Alexeev. On extra components in the functorial compactification of $A _ { g }$ . In Moduli of Abelian Varieties (Texel Island, 1999), volume 195 of Progr. Math., pages 1–9. Birkhauser, Basel, 2001. ¨

[2] Valery Alexeev. Complete moduli in the presence of semiabelian group action. Ann. of Math. (2), 155(3):611–708, 2002.

[3] Valery Alexeev and Iku Nakamura. On Mumford’s construction of degenerating abelian varieties. Tohoku Math. J. (2), 51(3):399–420, 1999.

[4] Michel Brion. Compactification de l’espace des modules des variet´ es´ abeliennes principalement polaris ´ ees (d’apr ´ es V. Alexeev). In \` Seminaire Bour- ´ baki. Vol. 2005/2006. Asterisque ´ , (311):Exp. No. 952, vii, 1–31, 2007.

[5] J. I. Burgos Gil, J. Kramer, and U. Kuhn. Arithmetic characteristic classes ¨ of automorphic vector bundles. Doc. Math., 10:619–716 (electronic), 2005.

[6] Alexander Caspar. Realisations of Kummer–Chern–Eisenstein-motives.   
Manuscripta Math., 122(1):23–57, 2007.

[7] C.-L. Chai. Arithmetic minimal compactification of the Hilbert-Blumenthal moduli spaces. Ann. of Math. (2), 131(3):541–554, 1990.

[8] David A. Cox. The functor of a smooth toric variety. Tohoku Math. J. (2), 47(2):251–262, 1995.

[9] Mladen Dimitrov. Compactifications arithmetiques des vari´ et´ es de Hilbert´ et formes modulaires de Hilbert pour $\Gamma _ { 1 } ( \mathfrak { c } , \mathfrak { n } )$ . In Geometric Aspects of Dwork Theory. Vol. I, II, pages 527–554. Walter de Gruyter GmbH & Co. KG, Berlin, 2004.

[10] Michael Harris. Functorial properties of toroidal compactifications of locally symmetric varieties. Proc. London Math. Soc. (3), 59(1):1–22, 1989.

[11] Takeshi Kajiwara, Kazuya Kato, and Chikara Nakayama. Logarithmic abelian varieties. I. Complex analytic theory. J. Math. Sci. Univ. Tokyo, 15(1):69–193, 2008.

[12] Robert E. Kottwitz and Michael Rapoport. Contribution of the points at the boundary. In The Zeta Functions of Picard Modular Surfaces, pages 111–150. Univ. Montreal, Montreal, QC, 1992. ´

[13] Michael J. Larsen. Arithmetic compactification of some Shimura surfaces. In The Zeta Functions of Picard Modular Surfaces, pages 31–45. Univ. Montreal, Montreal, QC, 1992. ´

[14] A. Miller, S. Muller-Stach, S. Wortmann, Y.-H. Yang, and K. Zuo. Chow– ¨ Kunneth decomposition for universal families over Picard modular surfaces. ¨ In Algebraic Cycles and Motives. Vol. 2, volume 344 of London Math. Soc. Lecture Note Ser., pages 241–276. Cambridge University Press, Cambridge, 2007.

[15] Abdellah Mokrane and Jacques Tilouine. Cohomology of Siegel varieties with $p$ -adic integral coefficients and applications. In Cohomology of Siegel varieties. Asterisque ´ , (280):1–95, 2002.

[16] Sophie Morel. Complexes ponder´ es sur les compactifications de Baily– ´ Borel: le cas des variet´ es de Siegel. ´ J. Amer. Math. Soc., 21(1):23–61 (electronic), 2008.

[17] Iku Nakamura. On moduli of stable quasi abelian varieties. Nagoya Math. J., 58:149–214, 1975.

[18] Yukihiko Namikawa. A new compactification of the Siegel space and degeneration of Abelian varieties. I, II. Math. Ann., 221(2, 3):97–141, 201– 241, 1976.

[19] Martin C. Olsson. Semistable degenerations and period spaces for polarized $K 3$ surfaces. Duke Math. J., 125(1):121–203, 2004.

[20] Martin C. Olsson. Compactifying Moduli Spaces for Abelian Varieties, volume 1958 of Lecture Notes in Mathematics. Springer-Verlag, Berlin, 2008.

[21] Richard Pink. Arithmetical Compactification of Mixed Shimura Varieties. Bonner Mathematische Schriften [Bonn Mathematical Publications], 209. Universitat Bonn Mathematisches Institut, Bonn, 1990. Dissertation, Rheinische¨ Friedrich-Wilhelms-Universitat Bonn, Bonn, 1989.¨

[22] Richard Pink. On $l$ -adic sheaves on Shimura varieties and their higher direct images in the Baily–Borel compactification. Math. Ann., 292(2):197– 240, 1992.

[23] Michael Rapoport. Compactifications de l’espace de modules de Hilbert-Blumenthal. Compositio Math., 36(3):255–335, 1978.

[24] Michael Rapoport. On the shape of the contribution of a fixed point on the boundary: the case of Q-rank one. In The Zeta Functions of Picard Modular Surfaces, pages 479–491. Univ. Montreal, Montreal, QC, 1992. With an ´ appendix by Leslie Saper and Mark A. Stern.

[25] Eric Urban. Sur les representations ´ $p$ -adiques associees aux ´ representations cuspidales de´ $\mathrm { G S p } _ { 4 / \mathbb { Q } }$ . In Formes automorphes. II. Le cas du groupe ${ \mathrm { G } } S p ( 4 )$ . Asterisque ´ , (302):151–176, 2005.

[26] Jorg Wildeshaus. On the boundary motive of a Shimura variety. ¨ Compos.   
Math., 143(4):959–985, 2007.

# Comparison with other compactifications

[1] Armand Borel and Lizhen Ji. Compactifications of symmetric and locally symmetric spaces. Math. Res. Lett., 9(5-6):725–739, 2002.

[2] Armand Borel and Lizhen Ji. Compactifications of locally symmetric spaces. J. Differential Geom., 73(2):263–317, 2006.

[3] Armand Borel and Lizhen Ji. Compactifications of symmetric spaces. J.   
Differential Geom., 75(1):1–56, 2007.

[4] Mark Goresky and Yung-Sheng Tai. Toroidal and reductive Borel–Serre compactifications of locally symmetric spaces. Amer. J. Math., 121(5):1095– 1151, 1999.

[5] L. Ji. The greatest common quotient of Borel–Serre and the toroidal compactifications of locally symmetric spaces. Geom. Funct. Anal., 8(6):978– 1015, 1998.

[6] L. Ji and R. MacPherson. Geometry of compactifications of locally symmetric spaces. Ann. Inst. Fourier (Grenoble), 52(2):457–559, 2002.

[7] Lizhen Ji. Metric compactifications of locally symmetric spaces. Internat.   
J. Math., 9(4):465–491, 1998. [8] Adam Koranyi. Remarks on the Satake compactifications. ´ Pure Appl.   
Math. Q., 1(4, part 3):851–866, 2005.

[9] Eduard Looijenga. New compactifications of locally symmetric varieties. In Proceedings of the 1984 Vancouver Conference in Algebraic Geometry, volume 6 of CMS Conf. Proc., pages 341–364, Providence, RI, 1986. Amer. Math. Soc.

[10] Eduard Looijenga. Compactifications defined by arrangements. I. The ball quotient case. Duke Math. J., 118(1):151–187, 2003.

[11] Eduard Looijenga. Compactifications defined by arrangements. II. Locally symmetric varieties of type IV. Duke Math. J., 119(3):527–588, 2003.

[12] Steven Zucker. On the reductive Borel-Serre compactification. III. Mixed Hodge structures. Asian J. Math., 8(4):881–911, 2004.

[13] Steven Zucker. Excentric compactifications. Q. J. Pure Appl. Math., 1(1):222–226, 2005.

[14] Steven Zucker. On the reductive Borel-Serre compactification. II. Excentric quotients and least common modifications. Amer. J. Math., 130(4):859– 912, 2008.

# Explicit resolutions

[1] Fritz Ehlers. Eine Klasse komplexer Mannigfaltigkeiten und die Auflosung ¨ einiger isolierter Singularitaten. ¨ Math. Ann., 218(2):127–156, 1975.

[2] C. Erdenberger, S. Grushevsky, and K. Hulek. Intersection theory of toroidal compactifications of ${ \mathcal { A } } _ { 4 }$ . Bull. London Math. Soc., 38(3):396–400, 2006.   
[3] H. G. Grundman. Explicit resolutions of cubic cusp singularities. Math. Comp., 69(230):815–825, 2000.   
[4] K. Hulek and G. K. Sankaran. The Kodaira dimension of certain moduli spaces of abelian surfaces. Compositio Math., 90(1):1–35, 1994.   
[5] K. Hulek and G. K. Sankaran. The fundamental group of some Siegel modular threefolds. In Abelian Varieties (Egloffstein, 1993), pages 141–150. de Gruyter, Berlin, 1995.   
[6] K. Hulek and G. K. Sankaran. The nef cone of toroidal compactifications of $\mathcal { A } _ { 4 }$ . Proc. London Math. Soc. (3), 88(3):659–704, 2004.   
[7] Ichiro Satake. On the blowing-ups of Hilbert modular surfaces. ¯ J. Fac. Sci. Univ. Tokyo Sect. IA Math., 24(1):221–229, 1977.   
[8] Ichiro Satake. On numerical invariants of arithmetic varieties of ¯ Q-rank one. In Automorphic Forms of Several Variables (Katata, 1983), volume 46 of Progr. Math., pages 353–369. Birkhauser Boston, Boston, MA, 1984. ¨ [9] E. Thomas and A. T. Vasquez. On the resolution of cusp singularities and the Shintani decomposition in totally real cubic number fields. Math. Ann., 247(1):1–20, 1980.   
[10] G. van der Geer. On the geometry of a Siegel modular threefold. Math. Ann., 260(3):317–350, 1982.   
[11] G. van der Geer and A. van de Ven. On the minimality of certain Hilbert modular surfaces. In Complex Analysis and Algebraic Geometry, pages 137– 150. Iwanami Shoten, Tokyo, 1977.

# Higher weight Hodge structures

[1] James A. Carlson, Eduardo H. Cattani, and Aroldo G. Kaplan. Mixed Hodge structures and compactifications of Siegel’s space (preliminary report). In Journees de G ´ eometrie Alg ´ ebrique d’Angers, Juillet 1979/Algebraic Geom- ´ etry, Angers, 1979, pages 77–105. Sijthoff & Noordhoff, Alphen aan den Rijn, 1980.

[2] Eduardo Cattani, Aroldo Kaplan, and Wilfried Schmid. Variations of polarized Hodge structure: asymptotics and monodromy. In Hodge theory (Sant Cugat, 1985), volume 1246 of Lecture Notes in Math., pages 16–31. Springer, Berlin, 1987.

[3] Eduardo H. Cattani and Aroldo G. Kaplan. Extension of period mappings for Hodge structures of weight two. Duke Math. J., 44(1):1–43, 1977.

[4] Phillip Griffiths, editor. Topics in Transcendental Algebraic Geometry, volume 106 of Annals of Mathematics Studies, Princeton, NJ, 1984. Princeton University Press.

[5] Kazuya Kato and Sampei Usui. Logarithmic Hodge structures and classifying spaces. In The Arithmetic and Geometry of Algebraic Cycles (Banff, AB, 1998), volume 24 of CRM Proc. Lecture Notes, pages 115–130. Amer. Math. Soc., Providence, RI, 2000.

[6] Kazuya Kato and Sampei Usui. Borel–Serre spaces and spaces of SL(2)- orbits. In Algebraic Geometry 2000, Azumino (Hotaka), volume 36 of Adv. Stud. Pure Math., pages 321–382. Math. Soc. Japan, Tokyo, 2002.

[7] Kazuya Kato and Sampei Usui. Classifying Spaces of Degenerating Polarized Hodge Structures, volume 169 of Annals of Mathematics Studies. Princeton University Press, Princeton, NJ, 2009.

[8] Gregory Pearlstein. $\mathrm { S L } _ { 2 }$ -orbits and degenerations of mixed Hodge structure. J. Differential Geom., 74(1):1–67, 2006.

[9] Joseph Steenbrink and Steven Zucker. Variation of mixed Hodge structure.   
I. Invent. Math., 80(3):489–542, 1985.

[10] Sampei Usui. Complex structures on partial compactifications of arithmetic quotients of classifying spaces of Hodge structures. Tohoku Math. J. (2), 47(3):405–429, 1995.

[11] Sampei Usui. Images of extended period maps. J. Algebraic Geom., 15(4):603–621, 2006.

# Reduction theory

[1] Avner Ash. Deformation retracts with lowest possible dimension of arithmetic quotients of self-adjoint homogeneous cones. Math. Ann., 225(1):69– 76, 1977.

[2] Avner Ash. On eutactic forms. Canad. J. Math., 29(5):1040–1054, 1977.

[3] Avner Ash. Cohomology of congruence subgroups $\operatorname { S L } ( n , \mathbf { Z } )$ . Math. Ann., 249(1):55–73, 1980.

[4] Avner Ash. Small-dimensional classifying spaces for arithmetic subgroups of general linear groups. Duke Math. J., 51(2):459–468, 1984.

[5] Avner Ash, Paul E. Gunnells, and Mark McConnell. Cohomology of congruence subgroups of $\operatorname { S L } _ { 4 } ( \mathbb { Z } )$ . J. Number Theory, 94(1):181–212, 2002.

[6] Avner Ash, Paul E. Gunnells, and Mark McConnell. Cohomology of congruence subgroups of ${ \mathrm { S L } } ( 4 , \mathbb { Z } )$ . II. J. Number Theory, 128(8):2263–2274, 2008.

[7] E. S. Barnes and M. J. Cohn. On Minkowski reduction of positive quaternary quadratic forms. Mathematika, 23(2):156–158, 1976.

[8] E. S. Barnes and M. J. Cohn. On the reduction of positive quaternary quadratic forms. J. Austral. Math. Soc. Ser. A, 22(1):54–64, 1976.

[9] Bill Casselman. Stability of lattices and the partition of arithmetic quotients. Asian J. Math., 8(4):607–637, 2004.

[10] W. A. Casselman. Geometric rationality of Satake compactifications. In Algebraic Groups and Lie Groups, volume 9 of Austral. Math. Soc. Lect. Ser., pages 81–103. Cambridge University Press, Cambridge, 1997.

[11] Mathieu Dutour Sikiric, Achill Sch ´ urmann, and Frank Vallentin. A gen- ¨ eralization of Voronoi’s reduction theory and its application. Duke Math. J., 142(1):127–164, 2008.

[12] R. M. Erdahl and S. S. Ryshkov. The empty sphere. Canad. J. Math., 39(4):794–824, 1987.

[13] Paul E. Gunnells. Modular symbols for Q-rank one groups and Vorono˘ı reduction. J. Number Theory, 75(2):198–219, 1999.

[14] Paul E. Gunnells and Mark McConnell. Hecke operators and $\mathbb { Q }$ -groups associated to self-adjoint homogeneous cones. J. Number Theory, 100(1):46– 71, 2003.

[15] Peter Kiernan and Shoshichi Kobayashi. Comments on Satake compactification and Picard theorem, J. Math. Soc. Japan, 28(3):577–580, 1976.

[16] Enrico Leuzinger. An exhaustion of locally symmetric spaces by compact submanifolds with corners. Invent. Math., 121(2):389–410, 1995.

[17] Robert MacPherson and Mark McConnell. Explicit reduction theory for Siegel modular threefolds. Invent. Math., 111(3):575–625, 1993.

[18] S. S. Ryshkov and R. M. Erdahl. The empty sphere. II. Canad. J. Math., 40(5):1058–1073, 1988.

[19] Leslie Saper. Tilings and finite energy retractions of locally symmetric spaces. Comment. Math. Helv., 72(2):167–202, 1997.

[20] Leslie Saper. Geometric rationality of equal-rank Satake compactifications. Math. Res. Lett., 11(5-6):653–671, 2004.   
[21] Mathieu Dutour Sikiric, Achill Sch ´ urmann, and Frank Vallentin. Classi- ¨ fication of eight-dimensional perfect forms. Electron. Res. Announc. Amer. Math. Soc., 13:21–32 (electronic), 2007.   
[22] C. Soule. Perfect forms and the Vandiver conjecture. ´ J. Reine Angew. Math., 517:209–221, 1999.   
[23] Christophe Soule. The cohomology of´ $\mathrm { S L } _ { 3 } ( \mathbf { Z } )$ . Topology, 17(1):1–22, 1978.   
[24] Dan Yasaki. On the existence of spines for $\mathbb { Q }$ -rank 1 groups. Selecta Math. (N.S.), 12(3-4):541–564, 2006.   
[25] Dan Yasaki. An explicit spine for the Picard modular group over the Gaussian integers. J. Number Theory, 128(1):207–234, 2008.

# Index

$\Gamma$ -admissible collection of polyhedra, 161   
$\Gamma$ -admissible polyhedral decomposition, 37,   
75   
$\ell$ -fold top differentials, 192   
$k$ -gon of rational curves, 20

admissible structure of polyhedral complexes, 183 associated boundary component, 164

Baily–Borel compactification, 165   
best rational approximations, 35   
boundary component rational of a bounded domain, 140 of a homogeneous self-adjoint cone, 52   
boundary component of a bounded domain, 127   
central co-core, 92   
centralizer of a boundary component, 134   
characteristic function of a convex non-degenerate cone, 38   
co-core, 82   
compact root, 112   
compact torus, 2   
complementary module, 195   
cone, 38 $k$ -irreducible, 56 central, 93 non-degenerate, 38 perfect, 93 self-adjoint, 38 self-dual, 38   
conical polyhedral complex, 11   
core, 77   
cusp, 15, 26   
cylindrical set, 100   
decomposition into central cones, 90   
exposed point, 85

extendable form, 192   
extreme point, 82

flag of $k$ -boundary components, 64 standard, 64 fundamental 5-factor decomposition, 143 geodesic projection, 140

Hermann convexity theorem, 120   
hermitian symmetric space, 105   
Hilbert modular surface, 26   
Hilbert modular variety, 103   
horocycle, 16

idempotents mutually orthogonal, 46 complete set of, 47 maximal set of, 47   
integral structure on a conical polyhedral complex, 12

Jordan algebra, 43   
formally real, 47   
kernel, 77   
rationally locally polyhedral, 84   
Kodaira dimension, 194   
Koecher’s theorem, 191   
Krein–Milman theorem, 82   
level- $k$ structure, 20   
Levi-pseudoconvex, 104   
manifold of general type, 194   
mutation, 51   
natural basepoint   
of a boundary component, 133   
neat subgroup, 176   
non-compact root, 112   
normalizer of a boundary component, 129

ord, 2

Peirce decomposition, 46   
perfect co-core, 92   
polyhedral cone, 71   
$\mathbb { Q }$ -rational, 72   
polyhedral kernel, 84   
projective Γ-admissible decomposition, 199

quasi-hermitian form, 201

rank of a hermitian symmetric domain, 114   
rational boundary component, 140   
rational partial polyhedral decomposition, 6   
real root decomposition, 118   
Riemannian symmetric space, 105

Satake topology, 164   
semi-conical convex set, 81   
semi-proper meromorphic map, 179   
Siegel set, 37, 67   
strict homomorphism (of semi-groups), 7   
strictly or strongly commuting elements, 44   
strongly convex subset (of euclidean space), 33   
strongly orthogonal roots, 112   
strongly pseudoconvex subset (of a complex manifold), 33   
symmetric domain, 106   
symmetric map, 108   
symmetric space non-euclidean, 106 of compact type, 106 of non-compact type, 106 simple, 106   
toroidal embedding, 9 of analytic spaces, 9 without monodromy, 10 without self-intersection, 10   
torus embedding, 2   
tube domain, 98   
universal elliptic curve, 15   
Voronoi decomposition of the first type, 90   
Weil pairing, 20