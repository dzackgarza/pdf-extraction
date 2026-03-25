# Classification of fibre bundles, gauge theory and D-branes

# Alexander Wijns♯

♯ NORDITA Roslagstullsbacken 23 106 91 Stockholm, Sweden

e-mail: awijns@nordita.org

Based on lectures given by the author at the Fifth International Modave Summer School on Mathematical Physics, held in Modave, Belgium, August 2009.

# Abstract

These notes are aimed at students and young researchers in string and field theory with some working knowledge of manifold theory, but only a rough idea of what fibre bundles are. The aim is to introduce some notions from fibre bundle theory and algebraic topology (mainly homotopy theory) and build up to some results about the classification of principal and vector bundles that are relevant for the understanding of for instance topologically nontrivial solutions and anomalies in gauge theories, and D-branes in string theory. After laying the necessary groundwork, the first goal is the Chern-Weil approach to characteristic classes starting from the theory of connections on principal bundles. Then a more abstract approach to classifying vector bundles using homotopy theory results in the very basics of topological K-theory. These notes are intended to be quite basic, but should provide readers with the necessary background for understanding more serious accounts of such things as index theory, (twisted) K-theory and their applications to theoretical physics.

# Contents

# Introduction

# 3

1.1 Why read this . 3   
1.2 Outline 4

# 2 Preliminaries: Manifolds 6

2.1 Topological spaces and homeomorphisms . 6   
2.2 Manifolds and diffeomorphisms 6   
2.3 Tangent vectors . 8   
2.4 Differential forms and integration 9   
2.5 Lie groups and algebras 10

# 3 De Rham Theory 13

3.1 The de Rham Complex 13

3.2 Homotopy equivalence 14   
3.3 Exact Sequences of cochain complexes 15   
3.4 The Mayer-Vietoris sequence for de Rham 17   
3.5 Why categories? 19

# 4 Fibre Bundles

# 21

4.1 Definitions . 21   
4.2 Vector and principal bundles 23   
4.3 Operations on bundles 26

# 5 Connections on fibre bundles 29

5.1 Parallel transport in a principal bundle . 29   
5.2 Connections . 31   
5.3 Curvature 33   
5.4 Characteristic classes I: Chern-Weil theory . 34   
5.5 The Chern class, monopoles and instantons 36

# 6 Classification of fibre bundles 40

6.1 Homotopy groups . . 40   
6.2 The homotopy exact sequence of a fibre bundle 42   
6.3 Homotopy classification of vector bundles 44   
6.4 Vector bundles over spheres 46   
6.5 Characteristic classes II: algebraic topology approach . 48

# 7 Topological K-theory

# 51

7.1 The functors $K ( X )$ and ${ \overset { \sim } { K } } ( X )$ 51   
7.2 K-groups of spheres and Bott periodicity . 53   
7.3 K-theory and D-branes . . . 55

# Bibliography

# Chapter 1

# Introduction

# 1.1 Why read this

For understanding many aspects – indeed, most topics treated in standard textbooks – of gauge theories one can be largely ignorant about the mathematical structure they are (or at least should be) based on, namely that of fibre bundles. However, once one wants to discuss the global structure of gauge theories, a deeper knowledge of bundle theory becomes indispensable. In a typical gauge theory setting one has some tensor fields (scalar fields, spinor fields, vector fields, differential forms) which have a redundancy in their description under (local) transformations which are part of a given Lie group. This is exactly the kind of structure which is at the heart of fibre bundle theory. The study of the global structure of a gauge theory is not a mere academic issue, but is crucial for a proper treatment of some very important physical phenomena, like semi-classical solutions (monopoles, instantons) and anomalies.

A corner of differential and algebraic topology which very beautifully captures aspects of the non-triviality of fibre bundles, and turns out to be extremely useful for understanding both semi-classical objects and anomalies in gauge theories, is the theory of characteristic classes. The most computationally practical approach to characteristic classes, which is thus most useful for physicists, is the Chern-Weil theory, based on the theory of connections on fibre bundles and their curvature. This will be the culmination of the first part of this text.

For many reasons, these techniques are also very useful in string theory. For instance, the low energy effective approximation to superstring theories are supergravity theories which are of course also gauge theories. Understanding both gravitational and gauge anomalies is helped significantly by the use of characteristic classes. Another place where gauge theories pop up in string theory is as low energy effective world-volume theories on D-branes. Many interesting D-brane systems have a low energy description as a semiclassical object in an auxiliary gauge theory. Here again characteristic classes are all over the place.

But D-branes turn out to be yet another source for applications of fibre bundle theory. A very important problem, still partly unresolved, is the classification of D-brane charges. It turns out that here something called K-theory provides at least part of the answer. Topological K-theory (as opposed to the much more general algebraic K-theory) results from trying to find algebraic structures relevant for the classification of vector bundles. From a physics perspective the vector bundles are related to the Chan-paton degrees of freedom that live on the world-volume of a D-brane. The classification theory of vector (and more generally, fibre) bundles is very rich and beautiful, tying together homotopy theory, more abstract approaches to characteristic classes, and K-theory. These topics will appear in varying degrees of depth and detail in the second part of these notes.

D-branes are actually a source of inspiration for another, perhaps even more exciting field of mathematics related to homological mirror symmetry. A discussion of the beautiful theory behind this would require an introduction to algebraic geometry (and more formal aspects of algebraic topology) culminating in the daunting edifice of homological algebra, and is well beyond the modest goal of this write-up. For a first step into this wonderful and overwhelming world (from a physics perspective) the review [1] is highly recommended.

In this text we will more or less take for granted the usefulness in physics of fibre bundles and related mathematical constructions. The main goal is thus to provide readers with some background in algebraic topology (mainly homotopy theory) and fibre bundle theory, while only some hints towards physics applications will be given. For instance, K-theory will not at all be developed to the extent that it will be possible to discuss its relevance for understanding the classification of D-branes and RR-fields beyond some mere hints. More advanced topics related to topological K-theory, like the Atiyah-Singer index theorem and twisted K-theory will not be discussed at all. The hope is however that after reading this text, one is better prepared for delving into these ultimately more interesting advanced topics with more confidence. In brief, this text assumes only some working knowledge of manifolds and their differential geometry and sets out to explain some notions of fibre bundle theory, algebraic topology and K-theory that prepare the reader for more serious accounts of for instance the twisted K-theory classification of D-branes, or the Atiyah-Singer index theorem and its applications to anomalies in gauge theories.

Emphasis throughout will be on ideas and concepts – less on technical details. In other words, most proofs – especially the lengthier ones – will be skipped. All proofs can be found in the references given throughout the text. Of course, when a simple proof gives some significant insight into the matter, there will be no excuse for skipping it. Especially in the last two sections, the discussion might become fairly colloquial and sketchy at times, although some effort has been put into making it accessible to readers who are able to find their way through the first parts without too much pain.

# 1.2 Outline

The following section on manifolds mainly sets the stage and introduces some notation. For those who need to refresh their memory about tangent vectors fields, differential forms and Lie groups, this section will just about do. For those unfamiliar with these matters, we recommend other texts at the beginning of the section. Section 3 uses de Rham cohomology as an excuse to introduce some notions from algebraic topology in a hopefully familiar setting. The most important idea to remember from this section is the notion of homotopy invariance. We also digress in some detail on one calculational tool which is ubiquitous in algebraic topology, namely that of exact sequences. In particular, we focus on the Mayer-Vietoris sequence for the de Rham complex and use it to compute some cohomology groups. These techniques will however hardly play any role in the remaining sections. Algebraic topology is perhaps the most important discipline in mathematics where it is very natural to use categorical language, e.g. homotopy and (co)homology are all prime examples of functors. We end this section with some comments on why it is useful – and not a burden, as is often still felt in the physics community – to use categorical language, although we will do so only in a very modest and extremely basic way in the rest of the notes. If the reader wishes to acquire more than just a skin-deep understanding of much of modern mathematics, he’d better get used to texts who use a categorical language anyway. This text can be seen as just a very modest first step in this direction.

In section 4 we finally come to fibre bundles. We introduce both the notion of fibre bundle and coordinate bundle. The more general notion of fibre bundle – which in the end is just an equivalence class of coordinate bundles – is used in more abstract discussions, especially in the last two sections. Coordinate bundles are often useful for more practical constructions and will be used a lot in sections 4 and 5. For most purposes, the two notions can be seen as essentially the same, and we will usually refer to both of them as fibre bundles. Some examples of the most important types of fibre bundle, namely vector and principal bundles, are used to explain the importance of associated bundles. We end this section with some operations on bundles, the most important ones being the Whitney sum of vector bundles and the pull-back of fibre bundles in general. Section 5 is our first serious attempt to understand the global structure of fibre bundles. To this end we introduce parallel transport and connections on (mainly) principal bundles, since they are the most natural objects to endow such extra structure with. Some emphasis is placed on going from a global notion of a connection 1-form on the principal bundle to a local 1-form on a patch of the base manifold. The latter is nothing but the gauge field encountered in gauge theory. The local curvature 2-form (or field strength) of this gauge potential is then used to construct polynomials which represent classes in cohomology which are insensitive to the precise connection chosen. They are thus characteristic of the fibre bundle itself. This is the Chern-Weil approach to characteristic classes. The – in some sense – most important characteristic class, the Chern class, is then used to understand Dirac monopoles and $S U ( 2 )$ instantons.

We adopt a slightly more abstract point of view from section 6 onward. After introducing homotopy groups and some techniques which are useful for their computation, especially in a bundle setting, we use notions from homotopy theory to classify vector bundles. This results in the introduction of universal bundles and classifying spaces. The section ends with a brief introduction to characteristic classes from a more abstract point of view than in section 5, namely starting from the cohomology of the classifying space. Finally, section 7 introduces the basics of topological K-theory. This follows naturally from the preceding attempts to classify vector bundles. Namely, the set of all vector bundles over some space is a monoid, but fails to be a group. The different K-groups are then different, but related, ways of turning this monoid into a group. We discuss how this connects beautifully to homotopy theory, a line of reasoning which then relates Bott periodicity for the homotopy groups of the classical Lie groups to a purely K-theoretic version of Bott periodicity. We end these notes with some hints as to why K-theory should be useful for classifying D-branes, and some pointers towards the literature for further study.

# Chapter 2

# Preliminaries: Manifolds

This section mainly serves as a review of hopefully known concepts and some standard notation. Some useful references are [2], [3], [4], [5], [6] and [7].

# 2.1 Topological spaces and homeomorphisms

To set the stage, let us recall some basic notions from topology. A topological space $X$ is a set together with a collection $\mathcal { U } = \{ U _ { i } \}$ of subsets which satisfy the following requirements:

• $\boldsymbol { \mathcal { U } }$ is closed under arbitrary unions and finite intersections.   
• $X$ , $\emptyset \in { \mathcal { U } }$ , where $\varnothing$ denotes the empty set.

The elements of $X$ are usually called points and elements of $\boldsymbol { u }$ open sets. The main reason why this definition is interesting is that it provides a notion of proximity and allows for a general definition of a continuous map. Namely, consider a map $f : X \to Y$ between topological spaces $X$ and $Y$ . Such a map is called continuous if the inverse image $f ^ { - 1 } ( V )$ of an open set $V \subset Y$ is open in $X$ .1 This implies that ‘neighboring points’ in $X$ (belonging to the same open set, say) are mapped to neighboring points in $Y$ . The word map will invariably stand for continuous map (actually, mostly even differentiable or smooth) and the word space will be used for topological space whenever no confusion with for instance vector space is deemed possible.

A continuous bijective map with continuous inverse is called a homeomorphism. Two topological spaces which are mapped into one another by a homeomorphism are called homeomorphic. The main goal of topology can be stated to be the classification of topological spaces up to homeomorphism. Of course, in general this is a hopelessly ambitious goal. To make significant progress one is forced to both narrow down the kind of topological space one wants to consider (e.g. manifold, fibre bundle, ...) and to allow for more rough notions of equivalence (e.g. homotopy type).

To make life significantly simpler, we will talk almost exclusively about a very specific kind of topological space, namely smooth manifolds.

# 2.2 Manifolds and diffeomorphisms

A topological space provides the setting for studying continuity. In physics, one however often requires the arsenal of calculus. To this end, the notion of a manifold is very useful. A manifold is roughly speaking a topological space which ‘locally looks like $\mathbb { R } ^ { n }$ ’ for some $n \in \mathbb N$ . The techniques we know from calculus on $\mathbb { R } ^ { n }$ then carry over to calculus on (differentiable) manifolds.

Let us be a bit more precise. Given a topological space $X$ , an $n$ -dimensional chart on $X$ is a pair $\{ U , \phi \}$ , where $U \in X$ is an open set and $\phi : U \to \mathbb { R } ^ { n }$ is a homeomorphism onto its image $\phi ( U ) \in \mathbb { R } ^ { n }$ . If there exists such a chart around every point of $X$ , we call $X$ locally Euclidean. Furthermore, an $n$ -dimensional $k$ -differentiable structure on $X$ is is a collection of charts $\{ U _ { i } , \phi _ { i } \}$ , called an atlas, such that

• The $U _ { i }$ cover $X$ , i.e. $X = \cup _ { i } U _ { i }$ .   
• For any pair of charts $U _ { i }$ , $U _ { j }$ with $U _ { i } \cap U _ { j } \neq \emptyset$ , the transition function $\phi _ { j } \circ \phi _ { i } ^ { - 1 }$ : $\phi _ { i } ( U _ { i } \cap U _ { j } ) \to \phi _ { j } ( U _ { i } \cap U _ { j } )$ is $k$ -differentiable.

For simplicity, we will take $k$ to infinity, i.e. require the transition maps to be ${ \mathcal { C } } ^ { \infty }$ . In this case we refer to the maps as being smooth and the corresponding differentiable structure is called a ${ \mathcal { C } } ^ { \infty }$ -structure. We then have the following definition:

Definition 1. An $n$ -dimensional smooth manifold $M$ is a locally Euclidian Hausdorff space with an $n$ -dimensional ${ \mathcal { C } } ^ { \infty }$ -structure. Dropping the latter requirement yields the more general notion of topological manifold. 2

All manifolds we will encounter will be smooth, hence we will often simply refer to them as manifolds, leaving the smoothness condition implicit. For connected manifolds, the dimension is obviously well-defined (since the transition functions are diffeomorphisms). We can now exploit the notion of differentiability on $\mathbb { R } ^ { n }$ to define smooth functions on manifolds.

A function $f : M \to \mathbb { R }$ is called smooth if the composite map $f \circ \phi ^ { - 1 } : \phi ( U ) \to \mathbb { R }$ i s smooth on any chart $\{ U , \phi \}$ . All smooth functions on a manifold $M$ form an algebra over $\mathbb { R }$ by point-wise addition and multiplication, and multiplication with a scalar. This algebra is denoted ${ \mathcal { C } } ^ { \infty } ( M )$ .

Similarly there is a well-defined notion of smooth map between two manifolds. Consider two manifolds, $\left( M , \{ U _ { i } , \phi _ { i } \} \right)$ and $\left( N , \{ V _ { a } , \psi _ { a } \} \right)$ . We say that $f : M \to N$ is smooth when $\psi _ { a } \circ f \circ \phi _ { i } ^ { - 1 } : \phi _ { i } ( U _ { i } ) \to \psi _ { a } ( V _ { a } )$ is ${ \mathcal { C } } ^ { \infty }$ for all $i$ and $a$ . When $f$ is a bijection with both $f$ and $f ^ { - 1 }$ smooth, $f$ is called a diffeomorphism. Smooth manifolds are considered equivalent when they are diffeomorphic. Maps between manifolds will always be smooth in what follows, so that often the reference to smoothness will be dropped.

Example 1. Intuitively speaking3, a 2-sphere is diffeomorphic to an ellipsoid, but not to (the boundary of) a cube. It is however homeomorphic to a cube.

Example 2. We hope that the reader is fairly familiar with the $n$ -spheres $S ^ { n }$ . The main thing to remember about them is that they can be covered by two open sets, namely the ‘northern’ and ‘southern’ hemispheres $D _ { + } ^ { n }$ and $D _ { - } ^ { n }$ . Both hemispheres are homeomorphic to an open $n$ -ball and a choice of explicit homeomorphisms can serve as local chart (i.e coordinates). The intersection of $D _ { + } ^ { n }$ and $D _ { - } ^ { n }$ can be regarded as simply the ‘equator’ $S ^ { n - 1 }$ as we will see in the next section. On this intersection the appropriate transition functions then ‘glue’ the two hemispheres together. For instance, for the 2-sphere a stereographic projection is often used to show that it can be regarded as a complex manifold with complex coordinate $z$ on $D _ { + } ^ { 2 }$ and $w$ on $D _ { - } ^ { 2 }$ , and holomorphic transition function $z = 1 / w$ on their intersection. Regarded like this, $S ^ { 2 }$ is called the Riemann sphere.

Example 3. At some point, we will need to talk about projective spaces. Consider $\mathbb { R } ^ { n + 1 } \backslash \{ 0 \}$ with the equivalence relation $x \sim y$ iff $x = k y$ for some $k \in \mathbb R$ . The real projective space $\mathbb { R } P ^ { n }$ is the manifold which results from the identification under this equivalence, i.e. it is the space of lines through the origin in $\mathbb { R } ^ { n + 1 }$ . It can be covered by $n + 1$ charts, one for each region where one of the homogeneous coordinates (i.e. coordinates on $\mathbb { R } ^ { n + 1 } \backslash \{ 0 \} )$ ) is nonzero.

In the complex case, $\mathbb { C } P ^ { n }$ is the space of complex lines through the origin of $\mathbb { C } ^ { n + 1 }$ . Take for example $\mathbb { C } P ^ { 1 }$ with homogeneous coordinates $( z _ { 1 } , z _ { 2 } )$ . It can be covered by two charts, $U _ { 1 }$ where $z _ { 1 } \neq 0$ and $U _ { 2 }$ where $z _ { 2 } \neq 0$ . The homeomorphisms for the charts can be chosen to be

$$
\begin{array} { r l } & { \phi _ { 1 } : U _ { 1 } \to \mathbb { C } : [ ( z _ { 1 } , z _ { 2 } ) ] \mapsto z = z _ { 2 } / z _ { 1 } , } \\ & { \phi _ { 2 } : U _ { 2 } \to \mathbb { C } : [ ( z _ { 1 } , z _ { 2 } ) ] \mapsto w = z _ { 1 } / z _ { 2 } . } \end{array}
$$

Notice that these maps are well defined, since they don’t depend on the representative of the point on $\mathbb { C } P ^ { 1 }$ chosen. On the overlap, both homogeneous coordinates are nonzero and we have the transition function $z = 1 / w$ , i.e. $\mathbb { C } P ^ { 1 }$ is nothing but the Riemann sphere $S ^ { 2 }$ .

# 2.3 Tangent vectors

For any algebra $A$ over a field $K$ , its corresponding vector space of derivations $\mathrm { D e r } ( A )$ is defined as the space of al $K$ -linear maps $X : A  A$ satisfying the Leibnitz rule,

$$
X ( f g ) = f X ( g ) + X ( f ) g , \quad f , g \in A , X \in \operatorname { D e r } ( A ) .
$$

Applying this idea to ${ \mathcal { C } } ^ { \infty } ( M )$ , we get

Definition 2. The set of smooth vector fields $\mathcal { X } ( M )$ on $M$ is the vector space of derivations acting on the algebra of smooth functions, ${ \mathcal { X } } ( M ) = \operatorname { D e r } ( { \mathcal { C } } ^ { \infty } ( M ) )$ .

An element $X$ of $\mathcal { X } ( M )$ is a smooth assignment of a tangent vector $X _ { x }$ to every point $x$ of $M$ . The set of all tangent vectors at a point $x$ is an $n$ -dimensional vector space, called the tangent space $T _ { x } M$ at $x$ .

Given a smooth map $f : M \to N$ , we define the push-forward $( f _ { * } X ) _ { f ( x ) } : { \mathcal { C } } ^ { \infty } ( N ) | _ { f ( x ) } \to$ $\mathbb { R }$ of a tangent vector $X _ { x }$ at $x$ by

$$
( f _ { * } X ) _ { f ( x ) } ( g ) = X _ { x } ( g \circ f ) , \quad \mathrm { f o r } ~ g \in \mathcal { C } ^ { \infty } ( N ) .
$$

In other words, $f _ { * } : T _ { x } M \to T _ { f ( x ) } N$ . It is in general not possible to extend this definition to vector fields. Indeed, say there are two points $x$ and $y$ of $M$ for which $f ( x ) = f ( y ) = z$ . There is in general no guarantee that, given a vector field X, the image under $f _ { * }$ of $X _ { x }$ and $X _ { y }$ are equal. When $f$ is a diffeomorphism the extension of the push-forward to vector fields is however well-defined.

An equivalent way of defining tangent vectors at $x$ is by considering vectors tangent to curves going through $x$ . A curve $\gamma : ( - 1 , 1 ) \to M : t \mapsto \gamma ( t )$ is defined to be smooth at $x$ if $\phi \circ \gamma$ is smooth at $x$ for any chart $\{ U , \phi \}$ , where $U$ is some neighborhood of $x = \gamma ( 0 )$ . A natural tangent vector on $( - 1 , 1 )$ is $d / d t$ . The vector tangent to $\gamma$ at $x = \gamma ( 0 )$ is then defined to be the push-forward,

$$
X _ { x } ( f ) = \gamma _ { * } \left( { \frac { d } { d t } } \right) ( f ) { \bigg | } _ { t = 0 } = \left. { \frac { d } { d t } } ( f \circ \gamma ) \right| _ { t = 0 } .
$$

Since many curves through $x$ can lead to the same tangent vector at $x$ , this leads to a third equivalent way of defining a tangent vector at $x$ as an equivalence class of curves through $x$ . It would however lead us too far to delve into more details here.

The action of a vector field as a derivation can be extended beyond the algebra of smooth functions. This is then called the Lie derivative. On functions the Lie derivative is thus simply defined as

$$
{ \mathcal { L } } _ { X } ( f ) = X ( f ) .
$$

To be able to find a similar action on the vector fields themselves, we first need to make $\mathcal { X } ( M )$ into an algebra. Not surprisingly, both notions are related. Simply multiplying two vector fields $X$ and $Y$ does not result in a vector field. However, the commutator $[ X , Y ]$ is again a vector field. This turns $\mathcal { X } ( M )$ into a Lie algebra over $\mathbb { R }$ . Indeed, the product – being a commutator – is antisymmetric and satisfies the Jacobi identity. The Lie derivative $\mathcal { L } _ { X } : \mathcal { X } ( M ) \to \mathcal { X } ( M )$ is now the inner derivation,

$$
\mathcal { L } _ { X } ( Y ) = [ X , Y ] .
$$

This is indeed a derivation because of the Jacobi identity.

# 2.4 Differential forms and integration

Since $T _ { x } M$ is a vector space, we can define its dual space, the cotangent space $T _ { x } ^ { * } M$ . An element $\omega _ { x } \in T _ { x } ^ { * } M$ is called a cotangent vector and by definition $\omega _ { x } : T _ { x } M \to \mathbb { R }$ . A cotangent vector field or 1-form $\omega$ is a smooth assignment of a cotangent vector $\omega _ { x }$ to every $x$ , i.e. such that $\omega : \mathcal { X } ( M ) \to \mathcal { C } ^ { \infty } ( M )$ . The vector space of 1-forms on $M$ is denoted by $\Omega ( M )$ . More generally, a differential form of degree $p$ , or simply $p$ -form, $\omega$ is a ${ \mathcal { C } } ^ { \infty } ( M )$ - map $\omega : \mathcal { X } ( M ) \times \cdots \times \mathcal { X } ( M ) \to \mathcal { C } ^ { \infty } ( M )$ , which is antisymmetric under interchange of any of its entries

$$
\omega ( X _ { 1 } , . . , X _ { i } , . . , X _ { j } , . . , X _ { p } ) = - \omega ( X _ { 1 } , . . , X _ { j } , . . , X _ { i } , . . , X _ { p } ) .
$$

The space of $p$ -forms is called $\Omega ^ { p } ( M )$ , where obviously $\Omega ^ { 1 } ( M ) = \Omega ( M )$ , and we define $\Omega ^ { 0 } ( M ) = \mathcal { C } ^ { \infty } ( M )$ . The vector space $\begin{array} { r } { \Omega ^ { \bullet } ( M ) = \bigoplus _ { p = 0 } ^ { n } \Omega ^ { p } ( M ) } \end{array}$ is turned into a graded algebra by defining the product between a $p$ -form $\alpha$ and a $q$ -form $\beta$ to be the wedge product

$$
\alpha \wedge \beta = ( - 1 ) ^ { p q } \beta \wedge \alpha .
$$

The exterior derivative $d : \Omega ^ { p } ( M ) \to \Omega ^ { p + 1 } ( M )$ is the unique linear map which satisfies

• For a function $f$ , $d f$ is the 1-form defined by $d f ( X ) = X ( f )$ , for any vector field $X$ .   
• It squares to zero, $d ^ { 2 } = 0$ .   
• It is an anti-derivation, $d ( \alpha \wedge \beta ) = d \alpha \wedge \beta + ( - 1 ) ^ { p } \alpha \wedge d \beta$ , for a $p$ -form $\alpha$ and any form $\beta$ .

Given a map $f : M \to N$ , the pull-back $f ^ { * } : \Omega ^ { p } ( N ) \to \Omega ^ { p } ( M )$ is defined by,

$$
f ^ { * } \omega ( X _ { 1 } , . . , X _ { p } ) = \omega ( f _ { * } X _ { 1 } , . . , f _ { * } X _ { p } ) .
$$

Note that, in contrast to the push-forward, the pull-back can be defined for covector fields, which makes differential forms immensely important and useful objects as we will illustrate more than once in these notes. One can show that the pull-back defined in this way commutes with the exterior derivative, $f ^ { * } d = d f ^ { * }$ , a fact which will also turn out to be important later on. Another nice feature is that $( f \circ g ) ^ { * } = g ^ { * } \circ f ^ { * }$ . 4

As is well known, differential forms are especially interesting because they are the natural objects to integrate over manifolds. We will not go into any details here and assume an at least working knowledge with this in the following. One important theorem to mention however is Stoke’s theorem. For this the notion of manifold with boundary needs to be introduced. Basically this is defined analogously to an ‘ordinary’ manifold, but with $\mathbb { R } ^ { n }$ replaced by the upper-half space of $n$ -tuples, $( x _ { 1 } , . . , x _ { n } )$ with the added requirement that $x _ { n } \geq 0$ . The boundary of the manifold $\partial M$ is then defined as that part of $M$ which is mapped to the subset where $x _ { n } = 0$ by the relevant local charts. Stoke’s theorem then states that for compact $M$ ,

$$
\int _ { M } d \omega = \int _ { \partial M } \omega .
$$

This formula still holds for non-compact $M$ provided we require $\omega$ to have compact support.

# 2.5 Lie groups and algebras

A special class of manifolds are the Lie groups. They are important for many aspects of fibre bundle theory, especially as structure groups as we will see. Here we collect some important results about Lie groups and their associated Lie algebras.

Definition 3. A Lie group $G$ is a smooth manifold which is also a group, such that the map $( g , h ) \mapsto g h ^ { - 1 }$ is smooth for all $g , h \in G$ .

The identity element of $G$ will be denoted by $e$ . Note that by considering the composition of the smooth maps $g \mapsto ( e , g ) \mapsto g ^ { - 1 }$ , it is clear that inversion is also smooth. Similarly the composition $( g , h ) \mapsto ( g , h ^ { - 1 } ) \mapsto g h$ shows that the group operation itself is also smooth.

Given an element $g \in G$ , we can define the left- and right-translation of an element $h \in G$ by $g$ ,

$$
\begin{array} { r c l } { { { \cal L } _ { g } ( h ) } } & { { = } } & { { g h ; } } \\ { { { \cal R } _ { g } ( h ) } } & { { = } } & { { h g . } } \end{array}
$$

These induce the following push-forwards in the tangent space

$$
\begin{array} { r l r } { L _ { g * } : } & { { } } & { T _ { h } G  T _ { g h } G ; } \\ { R _ { g * } : } & { { } } & { T _ { h } G  T _ { h g } G . } \end{array}
$$

We say that a vector field $X \in { \mathcal { X } } ( G )$ is left-invariant if it satisfies

$$
L _ { g * } \left( X _ { h } \right) = X _ { g h } .
$$

Notice that in this case it makes sense to speak of a push-forward of a vector field, since left-translation is a diffeomorphism. For a diffeomorphism $f$ one also easily shows that

$$
f _ { * } [ X , Y ] = [ f _ { * } X , f _ { * } Y ] .
$$

This implies that the Lie bracket of two left-invariant vector fields is again left-invariant, so they form a subalgebra of $\mathcal { X } ( G )$ . This Lie subalgebra is called the Lie algebra $\mathfrak { g }$ associated to the Lie group $G$ . Because of (2.5.5) every element $A$ of $T _ { e } G$ generates a unique vector field $X _ { A }$ in $\mathfrak { g }$ such that $( X _ { A } ) _ { g } = L _ { g * } A$ . This establishes an algebra isomorphism between $T _ { e } G$ and $^ { 9 }$ . From now on we will not make the distinction between the two anymore and say that the Lie algebra $\mathfrak { g }$ is the tangent space at the identity in $G$ , endowed with the product it inherits from the Lie bracket between left-invariant vector fields. The generators $T _ { a }$ , $a \in \{ 1 , . . . , r \}$ ( $r = \mathrm { d i m } { \mathfrak { g } } = \mathrm { d i m } G$ ) of $\mathfrak { g }$ thus satisfy

$$
\left[ T _ { a } , T _ { b } \right] = f _ { a b } ^ { \ c } T _ { c } ,
$$

where ${ f _ { a b } } ^ { c }$ are the structure constants of $\mathfrak { g }$ . That they are indeed constant follows from (2.5.5) and (2.5.6).

For concreteness, by Lie group we will mean a matrix group (subgroup of $G L ( n )$ with matrix multiplication as group operation) from now on. It is not hard to show that, given an element $A$ of the Lie algebra, its push-forward $\ b { L _ { g * } A }$ by a $g \in G$ is represented in matrix notation simply by $g A$ . In other words the left-invariant vector field generated by $A$ i s $( X _ { A } ) _ { g } = g A$ in matrix notation.

Example 4. In what follows, we will encounter $S U ( 2 )$ several times in examples. Its elements $U$ are unitary two by two matrices with unit determinant. It is easy to see that this implies that they are of the form

$$
U = \left( \begin{array} { c c } { { a } } & { { b } } \\ { { - \bar { b } } } & { { \bar { a } } } \end{array} \right) , \quad | a | ^ { 2 } + | b | ^ { 2 } = 1 ,
$$

where $a$ and $b$ are complex numbers. As a manifold, we thus get $S U ( 2 ) = S ^ { 3 }$ . Writing $a = x _ { 0 } + i x _ { 3 }$ and $b = x _ { 2 } + i x _ { 1 }$ , we can rewrite this as,

$$
U = \sum _ { a = 0 } ^ { 3 } x _ { a } \tau _ { a } ,
$$

where $\tau _ { 0 } = 1 _ { 2 \times 2 }$ and $\tau _ { i } = i \sigma _ { i }$ , where the $\sigma _ { i }$ are the Pauli matrices, $i \in \{ 1 , 2 , 3 \}$ . To find the Lie algebra $\mathfrak { s u } ( 2 )$ ,5 we use equation (2.3.3) to find the tangent vectors at the identity $\tau _ { 0 }$ . Consider a curve $\gamma ( t ) = \sum x _ { a } ( t ) \tau _ { a }$ with $x _ { 0 } ( 0 ) = 1$ and $x _ { i } ( 0 ) = 0$ , so that $\gamma ( 0 ) = \tau _ { 0 }$ , i.e. the identity element. According to (2.3.3), a vector tangent to $\gamma$ at the identity is then of the form,6

$$
X = \left. \frac { d } { d t } \gamma ( t ) \right| _ { t = 0 } = \sum x _ { a } ^ { \prime } ( 0 ) \tau _ { a } ,
$$

where the prime is shorthand for derivative with respect to $t$ . We however still have to take the constraint $\sum x _ { a } ( t ) x _ { a } ( t ) = 1$ into account, which should be satisfied for all $t$ if $\gamma$ is to be a curve on $S U ( 2 )$ . Taking the derivative of this, and implementing the boundary conditions at $0$ , we find that $x _ { 0 } ^ { \prime } ( 0 ) = 0$ . We conclude that an element of $\mathfrak { s u } ( 2 )$ is of the form,

$$
X = i \sum _ { j = 1 } ^ { 3 } y _ { j } \sigma _ { j } ,
$$

i.e. these are all the traceless anti-hermitian two by two matrices. This is exactly what we would have found by the more naive procedure of writing an element of $S U ( 2 )$ as $U = \exp ( X )$ and imposing the unitarity and determinant conditions.

From our experience with matrix groups we know that the exponential map sends elements of the Lie algebra to elements of the Lie group. Consequently, $A \in { \mathfrak { g } }$ generates a curve (one-parameter subgroup) through $g$ in $G$ by

$$
\sigma _ { t } ( g ) = g \exp ( t A ) = R _ { \exp ( t A ) } ( g ) .
$$

The tangent vector to this one-parameter flow, obtained as in (2.3.3) by making use of a function $f : G \to \mathbb { R }$ , is nothing but the invariant vector field generated by $A$ at $g$ ,

$$
X _ { A } ( f ( g ) ) = \left. { \frac { d } { d t } } f ( \sigma _ { t } ( g ) ) \right| _ { t = 0 } .
$$

This is easily seen in matrix notation, where we simply have to note that

$$
{ \frac { d } { d t } } \sigma _ { t } ( g ) { \Big | } _ { t = 0 } = g A = ( X _ { A } ) _ { g } .
$$

We will need one more ingredient coming from Lie group theory when we come to fibre bundles. The adjoint map

$$
a d _ { g } : G \to G : h \mapsto g h g ^ { - 1 } ,
$$

induces a map in the tangent space

$$
a d _ { g * } : T _ { h } G \to T _ { g h g ^ { - 1 } } G .
$$

When we restrict this map to $h = e$ , we get an automorphism of $T _ { e } G \cong { \mathfrak { g } }$ (again in matrix notation),

$$
A d ( g ) : { \mathfrak { g } } \to { \mathfrak { g } } : V \mapsto g V g ^ { - 1 } .
$$

The adjoint representation of $G$ is then defined as

$$
A d : G \to G L ( { \mathfrak { g } } , r ) : g \mapsto A d ( g ) .
$$

It is straightforward to show that this is indeed a homomorphism, namely $A d ( g h ) \ =$ $A d ( g ) A d ( h )$ . In what follows, we will write $A d _ { g }$ instead of $A d ( g )$ .

# Chapter 3

# De Rham Theory

In order to give a flavor of some tools and concepts from algebraic topology in a reasonably familiar setting, we now discuss de Rham theory in some detail. This section was inspired by [6], which is the perfect preparation for [8], a classic on more advanced versions of cohomology.

# 3.1 The de Rham Complex

A $p$ -form $\omega$ for which $d \omega = 0$ is called closed, while a $p$ -form $\omega$ for which a $( p - 1 )$ -form $\alpha$ exists such that $\omega = d \alpha$ is called exact. In other words closed forms are in the kernel of $d$ and exact forms are in the image of $d$ . Since $d ^ { 2 } = 0$ , all exact forms are closed. An often interesting question to ask is under which conditions a closed form is automatically exact, or in which way it fails to be so. In other words, one is lead to the classification of closed forms modulo exact forms, i.e. two closed forms $\alpha$ and $\beta$ are said to be equivalent when there exists a form $\gamma$ such that $\alpha = \beta + d \gamma$ . We write this as $\alpha \sim \beta$ . This is clearly an equivalence relation and the vector spaces of equivalence classes are denoted by

$$
H ^ { p } ( M , \mathbb { R } ) = { \frac { \ker d _ { p } } { \operatorname { i m } d _ { p - 1 } } } .
$$

The vector space $H ^ { p } ( M , \mathbb { R } )$ is called the $p$ -th de Rham cohomology group (a vector space is in the first place an abelian group) and an equivalence class $[ \alpha ]$ is called a de Rham cohomology class with representative $\alpha$ . The reason why these cohomology groups are so interesting is because they tell us a lot (but far from everything) about the topology of $M$ . This is actually not so hard to see. Consider a map $f : { \cal M }  N$ and its pullback $f ^ { * } : \Omega ^ { \bullet } ( N ) \to \Omega ^ { \bullet } ( M )$ . Remember that this commutes with the exterior derivative, $f ^ { * } d = d f ^ { * }$ . This implies that the pull-back is well-defined on equivalence classes. Indeed, if $d \omega = 0$ , we find $d ( f ^ { * } \omega ) = f ^ { * } d \omega = 0$ , and if $\omega = d \alpha$ , then $f ^ { * } \omega = f ^ { * } d \alpha = d ( f ^ { * } \alpha )$ . So $f ^ { * }$ maps closed/exact forms to closed/exact forms and descends down to cohomology. So if we define $f ^ { * } [ \alpha ] = [ f ^ { * } \alpha ]$ , we get the map

$$
f ^ { * } : H ^ { \bullet } ( N , \mathbb { R } ) \to H ^ { \bullet } ( M , \mathbb { R } ) .
$$

Now just as for the pull-back on forms, we have that $( f \circ g ) ^ { * } = g ^ { * } \circ f ^ { * }$ and $1 ^ { * } = 1$ . This implies that if $f$ is a diffeomorphism with smooth inverse $f ^ { - 1 }$ , $f ^ { * }$ is an isomorphism of vector spaces with inverse $( f ^ { - 1 } ) ^ { * } = ( f ^ { * } ) ^ { - 1 }$ . In other words, diffeomorphic manifolds have isomorphic de Rham cohomology groups. For short, we say that de Rham cohomology yields topological invariants.

The structure of de Rham cohomology can be formalized and generalized. A set of abelian groups $A ^ { p }$ and homomorphisms, $d _ { p } : A ^ { p } \to A ^ { p + 1 }$ , often called coboundary operators, such that $d _ { p + 1 } \circ d _ { p } = 0$ , is called a cochain1 (or differential) complex. This is usually denoted as

$$
\cdot \cdot \cdot \xrightarrow { d _ { p - 2 } } { } _ { A } p ^ { p - 1 } \xrightarrow { d _ { p - 1 } } { } _ { A } p ^ { \textit { \textbf { d } } } \xrightarrow { d _ { p } } { } _ { A } p ^ { + 1 } \xrightarrow { d _ { p + 1 } } { } _ { \textbf { . . . } }
$$

In the case where $A ^ { p } = \Omega ^ { p } ( M )$ and $d _ { p } = d$ , the exterior derivative, this cochain complex is called the de Rham complex. In this context closed forms are called cocycles and exact forms coboundaries. Clearly however – since $\mathrm { i m } d _ { p } \subset \ker d _ { p + 1 }$ – one can define the cohomology groups for any cochain complex. So more generally the $p$ -th cohomology group of a cochain complex is defined as

$$
H ^ { p } = { \frac { \ker d _ { p } } { \operatorname { i m } d _ { p - 1 } } } .
$$

as we did for the de Rham complex.

# 3.2 Homotopy equivalence

We established that the de Rham cohomology of a manifold is a topological invariant, but actually it turns out to be a courser characteristic than that. We will now discuss how it is not only invariant under diffeomorphisms but also under homotopy equivalence. This fact actually provides a powerful tool for computing cohomology.

Definition 4. Two maps $f , g : X \to Y$ between two topological spaces are called homotopic if there exists a continuous map $F : X \times [ 0 , 1 ] \to Y$ such that $F ( x , 0 ) = f ( x )$ and $F ( x , 1 ) = g ( x )$ . $F$ is called a homotopy from $f$ to $g$ .

The relation $f \sim g$ when $f$ and $g$ are homotopic is an equivalence relation and we denote the homotopy class of $f$ by $[ f ]$ . As an example, it is easy to show that all maps from a manifold $M$ to $\mathbb { R } ^ { n }$ are homotopic, a possible homotopy between maps $f$ and $g$ being the straight-line homotopy

$$
\begin{array} { r } { F ( x , t ) = ( 1 - t ) f ( x ) + t g ( x ) . } \end{array}
$$

Definition 5. A map $f : X \to Y$ is called a homotopy equivalence if it has a homotopy inverse, i.e. a map $g : Y  X$ such that $g \circ f \sim 1 _ { X }$ and $f \circ g \sim 1 _ { Y }$ . If this is the case we say that $X$ and $Y$ are of the same homotopy type. This is an equivalence relation on topological spaces.

Clearly, a diffeomorphism is a homotopy equivalence. Another example is a deformation retraction.

Example 5. A retraction from $X$ to a subspace $A$ is a map $r : X \to A$ that restricts to the identity map on $A$ . Another way to say this is that $r \circ i = 1 _ { A }$ , where $i : A \to X$ is the inclusion map. A deformation retraction from $X$ to $A$ is a homotopy from the identity $1 _ { X }$ to $i \circ r$ , where $r$ is a retraction from $X$ to $A$ , which leaves $A$ fixed for all $t$ . In short, $r \circ i = 1 _ { A }$ and $i \circ r \sim 1 _ { X }$ , so that $r$ and $i$ are homotopy inverses and $X$ and $A$ are of the same homotopy type.

A space is called contractible if it has the homotopy type of a point. For instance, $\mathbb { R } ^ { n }$ is contractible for any $n$ . Indeed, the constant map $r : \mathbb { R } ^ { n }  \{ p \}$ , where $p$ is some point in $\mathbb { R } ^ { n }$ , is a retraction. The straight-line homotopy from $i \circ r$ to the identity on $\mathbb { R } ^ { n }$ is then a deformation retraction from $\mathbb { R } ^ { n }$ to a point.

Exercise 1. Show that the circle and the annulus or cylinder are homotopy equivalent.

The following important theorem is usually called the homotopy axiom for de Rham cohomology.

Theorem 1. Homotopic maps $f , g : M \to N$ between manifolds induce the same map $f ^ { * } = g ^ { * } : H ^ { \bullet } ( N , \mathbb { R } ) \to H ^ { \bullet } ( M , \mathbb { R } )$ in de Rham cohomology.

We will not give the proof of this theorem here (see e.g. [6]), but just mention that the usual method for showing that two cochain maps $f ^ { * }$ , $g ^ { * } : \Omega ^ { \bullet } ( N ) \to \Omega ^ { \bullet } ( M )$ reduce to the same map in cohomology is to find a cochain homotopy, i.e. a map $K : \Omega ^ { \bullet } ( N ) \to \Omega ^ { \bullet - 1 } ( M )$ of degree $^ { - 1 }$ such that

$$
f ^ { * } - g ^ { * } = d K \pm K d .
$$

Clearly the demonstration of the existence of such a map proves that there is no difference between $f ^ { * }$ and $g ^ { * }$ in cohomology. An immediate consequence of this theorem is the following.

Corollary 1. Manifolds of the same homotopy type have isomorphic de Rham cohomology rings.

From this we easily deduce a well-known theorem known as the Poincar´e Lemma. First note that the cohomology of a point, which we denote simply by $^ *$ , is easy to compute. Since the only forms on a point are (constant) $0$ -forms, or functions, it is immediate that $H ^ { 0 } ( * , \mathbb { R } ) = \mathbb { R }$ and $H ^ { k } ( * , \mathbb { R } ) = 0$ for $k > 0$ . This then leads to:

Theorem 2 (Poincar´e Lemma). Since $\mathbb { R } ^ { n }$ has the homotopy type of a point, its de Rham cohomology reads as follows

$$
H ^ { k } ( \mathbb { R } ^ { n } , \mathbb { R } ) = { \left\{ \begin{array} { l l } { \mathbb { R } } & { { \mathrm { f o r } } \quad k = 0 } \\ { 0 } & { { \mathrm { f o r } } \quad k > 0 } \end{array} \right. }
$$

More generally, every contractible manifold has the cohomology of a point. We will refer to the cohomology of a point as trivial. Apart from its theoretical significance, the homotopy ‘axiom’ is also of great use for actually computing cohomology groups. For instance, to compute the de Rham cohomology of a cylinder or annulus, it suffices to know the de Rham cohomology of a circle.

This will however only lead us so far. We haven’t actually computed the cohomology of a circle yet! There are many techniques for computing cohomology. We will discuss one important such technique here which is based on the machinery of exact sequences.

# 3.3 Exact Sequences of cochain complexes

A sequence of homomorphisms $\alpha _ { p }$ between abelian groups $A ^ { p }$

$$
\cdots \xrightarrow { } A ^ { p - 1 } \xrightarrow { \alpha _ { p - 1 } } A ^ { p } \xrightarrow { \alpha _ { p } } \ M ^ { p + 1 } \xrightarrow { } \cdots
$$

is called exact if ker $\alpha _ { p } = \mathrm { i m } \alpha _ { p - 1 }$ for each $p$ . The statement $\mathrm { i m } \alpha _ { p - 1 } \subset \mathrm { k e r }$ $\alpha _ { p }$ is equivalent to $\alpha _ { p } \alpha _ { p - 1 } = 0$ , so that an exact sequence is a cochain complex. The opposite inclusion implies that all cohomology groups of this cochain complex are trivial. The following statements are almost immediate,

1. $0 \longrightarrow A \stackrel { \alpha } { \longrightarrow } B$ is exact iff $\alpha$ is injective, and $A / \ker \alpha = A \cong \operatorname { i m } \alpha$ as a consequence of the first isomorphism theorem for groups.   
2. $A \xrightarrow { \alpha } B \longrightarrow 0$ is exact iff $\alpha$ is surjective, and $\operatorname { i m } \alpha = B \cong A / \ker \alpha$ again by the first isomorphism theorem for groups.

3. $0 \longrightarrow A \stackrel { \alpha } { \longrightarrow } B \longrightarrow 0$ is exact iff $\alpha$ is an isomorphism.

4. $0 \longrightarrow A { \stackrel { \alpha } { \longrightarrow } } B { \stackrel { \beta } { \longrightarrow } } C \longrightarrow 0$ is exact iff $\alpha$ is injective, $\beta$ is surjective and ker $\beta = \operatorname { i m } \alpha$ . As a consequence of the first two cases, this implies that $\beta$ induces an isomorphism $C \cong B / \ker \beta = B / \mathrm { i m } \alpha \cong B / A$ . An exact sequence of this kind is called a short exact sequence.

Now, assume that we have three cochain complexes of abelian groups $A ^ { p }$ , $B ^ { p }$ and $C ^ { p }$ , and that for each $p$ the sequence

$$
0 \xrightarrow [ ] { } \begin{array} { c c c } { { A ^ { p } } } & { { \stackrel { i } { \longrightarrow } } } & { { B ^ { p } } } \end{array} \xrightarrow [ ] { { \stackrel { j } { \longrightarrow } } } \begin{array} { c c c } { { C ^ { p } } } & { { \longrightarrow } } & { { 0 } } \end{array}
$$

is exact. For simplicity, we denote all appearing coboundary operators by $d$ , although in principle all these homomorphisms could be different. We also assume that $i$ and $j$ are cochain maps, i.e. $i \circ d = d \circ i$ and $j \circ d = d \circ j$ . Summarizing, we have the large commutative diagram called a short exact sequence of cochain complexes:

$$
\begin{array} { c } { { 0 } } \\ { { \Big \downarrow } } \\ { { \cdots \cdots \cdots \cdots \cdots \cdots \cdots \ A ^ { p - 1 } \ \cdots \ A ^ { p + 1 } \ \cdots \ A ^ { p + 1 } \ \cdots \cdots } } \\ { { \Big \downarrow } } \\ { { \cdots \cdots \cdots \ B ^ { p - 1 } \ \cdots \ B ^ { p } \ \cdots \ B ^ { p + 1 } \ \cdots \cdots } } \\ { { \Big \downarrow } } \\ { { \cdots \cdots \cdots \ C ^ { p - 1 } \ \cdots \ \underline { { { \epsilon } } } ( \underline { { { \epsilon } } } ) } } \\ { { \Big \downarrow } } \\ { { \cdots \cdots \cdots \ C ^ { p - 1 } \ \cdots \ \epsilon ^ { p - \ \ \underline { { { \epsilon } } } } \ \cdots \ \zeta ^ { p + 1 } \ \cdots \cdots } } \\ { { \Big \downarrow } } \\ { { \ o } } \\ { { \qquad \mathrm { ~ o } } } \end{array}
$$

This is commutative because $i$ and $j$ are cochain maps (e.g. the pull-back map $f ^ { * }$ we encountered before). The claim is now that to this short exact sequence one can associate a long exact sequence of cohomology groups,

$$
\quad \dots { \longrightarrow } H ^ { p } ( A ) \ { \stackrel { i ^ { * } } { \longrightarrow } } \ H ^ { p } ( B ) \ { \stackrel { j ^ { * } } { \longrightarrow } } \ H ^ { p } ( C ) \ { \stackrel { d ^ { * } } { \longrightarrow } } \ H ^ { p + 1 } ( A ) \ { \stackrel { i ^ { * } } { \longrightarrow } } \ H ^ { p + 1 } ( B ) \longrightarrow \ldots . . .
$$

Here $i ^ { * }$ and $j ^ { * }$ are induced by the cochain maps $i$ and $j$ . For instance, $i ^ { * } [ a ] = [ i ( a ) ]$ for $a \in A ^ { p }$ . As we showed for the pull-back map, this is well defined because $_ i$ is a cochain map. The homomorphism $d ^ { * } : H ^ { p } ( C ) \to H ^ { p + 1 } ( A )$ is defined as follows. Let $c \in C ^ { p }$ be a cocycle. Since $j$ is onto, $c = j ( b )$ for some $b \in B ^ { p }$ . The coboundary $d b \in B ^ { p + 1 }$ is in the kernel of $j$ , since $j ( d b ) = d j ( b ) = d c = 0$ . Since $\operatorname { t e r } j = \operatorname { i m } i$ , this implies $d b = i ( a )$ for some $a \in A ^ { p + 1 }$ . The element $a$ is also a cocycle since $i ( d a ) = d i ( a ) = d ^ { 2 } b = 0$ and $_ i$ i s injective. Intuitively, because $c$ is a cocycle, its coboundary should be zero modulo some element $a$ (remember that $C ^ { p } = B ^ { p } / A ^ { p }$ ). The map $d ^ { * }$ is precisely defined to be $d ^ { * } [ c ] = [ a ]$ . It is not very hard to show that this map is well-defined, i.e. independent of the choice of representative of $[ c ]$ and of intermediate element $b$ as long as $j ( b ) = c$ .

The theorem that to every short exact sequence of (co)chain complexes one can associate a long exact sequence of (co)homology groups represents the beginnings of the subject called homological algebra, its main method of proof sometimes being referred to as “diagram chasing”. For instance, the proof that the above long sequence of cohomology groups is exact is simply a succession of quite elementary examples of diagram chasing.2 Starting from this algebraic structure, one can now define different exact sequences of cohomology groups depending on which short exact sequence of cochain complexes one starts from. In the next subsection we will discuss one of the more important ones, namely the Mayer-Vietoris sequence.

# 3.4 The Mayer-Vietoris sequence for de Rham

Let $\{ U , V \}$ be an open cover of a manifold $M$ . Corresponding to this, there is the following commutative diagram of inclusion maps

![](images/33c63dd1fe6904148fb84e660b417f3908429dd49308771aae3d32f5288072ae.jpg)

These inclusion maps induce the following maps on $p$ -forms

$$
i : \Omega ^ { p } ( M ) \to \Omega ^ { p } ( U ) \oplus \Omega ^ { p } ( V ) : \alpha \mapsto ( i _ { U } ^ { * } \alpha , i _ { V } ^ { * } \alpha ) .
$$

and

$$
j : \Omega ^ { p } ( U ) \oplus \Omega ^ { p } ( V ) \to \Omega ^ { p } ( U \cap V ) : ( \alpha , \beta ) \mapsto j _ { V } ^ { * } \beta - j _ { U } ^ { * } \alpha .
$$

Assuming the inclusions implicitly, we will simply write: $i ( \alpha ) = ( \alpha , \alpha )$ and $j ( \alpha , \beta ) = \beta - \alpha$ . Since $i$ and $j$ are constructed out of pull-backs, they are cochain maps. It turns out that the sequence

$$
0 \longrightarrow \Omega ^ { p } ( M ) \stackrel { i } { \longrightarrow } \Omega ^ { p } ( U ) \oplus \Omega ^ { p } ( V ) \stackrel { j } { \longrightarrow } \Omega ^ { p } ( U \cap V ) \longrightarrow 0 |
$$

is exact. From this we automatically get the long exact sequence of cohomology groups (where we have omitted the reference to the real numbers for convenience)

$$
\cdots { \longrightarrow } H ^ { p } ( M ) \ { \stackrel { i ^ { * } } { \longrightarrow } } \ H ^ { p } ( U ) \oplus H ^ { p } ( V ) \ { \stackrel { j ^ { * } } { \longrightarrow } } \ H ^ { p } ( U \cap V ) \ { \stackrel { d ^ { * } } { \longrightarrow } } \ H ^ { p + 1 } ( M ) \longrightarrow \cdots . . .
$$

called the Mayer-Vietoris sequence for the de Rham complex. See [6] and [8] for more details and proofs.

We now illustrate its usefulness by computing some cohomology groups.

Example 6. First of all, from the Mayer-Vietoris sequence it follows that if $U$ , $V$ and $U \cap V$ are connected, then $M = U \cup V$ is connected.3 Indeed, the zeroth cohomology of a connected space is simply $\mathbb { R }$ (the vector space of constant functions). Since every real number can be written as the difference of two real numbers, this implies that $j ^ { * } : H ^ { 0 } ( U ) \oplus H ^ { 0 } ( V ) \to$ $H ^ { 0 } ( U \cap V )$ is surjective. Since $\operatorname { i m } j ^ { * } = \ker d ^ { * }$ , this implies that $d ^ { * } : H ^ { 0 } ( U \cap V ) \to H ^ { 1 } ( M )$ is the zero map. In other words, we get the short exact sequence

$$
0 \longrightarrow H ^ { 0 } ( M ) \stackrel { i ^ { * } } { \longrightarrow } \mathbb { R } \oplus \mathbb { R } \stackrel { j ^ { * } } { \longrightarrow } \mathbb { R } \longrightarrow 0
$$

This implies that $H ^ { 0 } ( M ) = \mathbb { R }$ , i.e. $M$ is connected. This also implies that the Mayer-Vietoris sequence can in this particular case be replaced by

$$
0 \longrightarrow H ^ { 1 } ( M ) \stackrel { i ^ { * } } { \longrightarrow } H ^ { 1 } ( U ) \oplus H ^ { 1 } ( V ) \stackrel { j ^ { * } } { \longrightarrow } H ^ { 1 } ( U \cap V ) \stackrel { d ^ { * } } { \longrightarrow } H ^ { 2 } ( M ) \longrightarrow \cdots .
$$

Exercise 2. Show that for an exact sequence

$$
0 \xrightarrow [ ] { } \kappa _ { \pm } ^ { 0 } \xrightarrow [ ] { \alpha _ { 0 } } \kappa _ { \pm } ^ { 1 } \xrightarrow [ ] { \alpha _ { 1 } } \kappa _ { \pm } ^ { 2 } \xrightarrow [ ] { \alpha _ { 2 } } \kappa \cdots \xrightarrow [ ] { \alpha _ { n - 1 } } \kappa _ { \pm } ^ { n } \xrightarrow [ ] { } 0
$$

of finite dimensional vector spaces, one has

$$
\sum _ { k = 0 } ^ { n } ( - 1 ) ^ { k } \dim A ^ { k } = 0
$$

In the case of de Rham cohomology groups $b ^ { p } = \dim { \cal H } ^ { p } ( M , \mathbb { R } )$ is called the $p$ -th Betti number of $M$ . The Euler characteristic of $M$ is defined as

$$
\chi ( M ) = \sum _ { p = 0 } ^ { n } ( - 1 ) ^ { p } \dim b ^ { p } ,
$$

where $\dim M = n$ . Show that the above implies that

$$
\chi ( M ) = \chi ( U ) + \chi ( V ) - \chi ( U \cap V ) .
$$

Example 7. Cover the circle $S ^ { 1 }$ by two arcs whose intersection is of the homotopy type of two points. This implies the exact sequence

$$
0 \longrightarrow \mathbb { R } \stackrel { i ^ { * } } { \longrightarrow } \mathbb { R } \oplus \mathbb { R } \stackrel { j ^ { * } } { \longrightarrow } \mathbb { R } \oplus \mathbb { R } \stackrel { d ^ { * } } { \longrightarrow } H ^ { 1 } ( S ^ { 1 } , \mathbb { R } ) \longrightarrow 0
$$

where we used that both arcs are of the homotopy type of a point. From (3.4.3) we find that this last vector space needs to be one-dimensional, so that

$$
H ^ { 1 } ( S ^ { 1 } , \mathbb { R } ) = \mathbb { R } .
$$

Finally (3.4.5) yields $\chi ( S ^ { 1 } ) = 1 + 1 - 2 = 0$ .

Knowing the cohomology of a circle, that of a torus is but a stone’s throw away.

Exercise 3. Decompose the 2-torus $T ^ { 2 }$ as the union of two cylinders $C _ { 1 }$ and $C _ { 2 }$ such that their intersection is homotopy equivalent to the disjoint union of two circles, $C _ { 1 } \cap C _ { 2 } =$ $S ^ { 1 } { \sqcup S ^ { 1 } }$ . It is easy to see from the Mayer-Vietoris sequence that $H ^ { p } ( A \sqcup B ) = H ^ { p } ( A ) \oplus H ^ { p } ( B )$ for any two manifolds $A$ and $B$ since their intersection is by definition zero. Convince yourself of the fact that the induced map $j ^ { \ast } : H ^ { 1 } ( C _ { 1 } ) \oplus H ^ { 1 } ( C _ { 2 } )  H ^ { 1 } ( C _ { 1 } \cap C _ { 2 } )$ is essentially of the form

$$
j ^ { \ast } : \mathbb { R } \oplus \mathbb { R } \to \mathbb { R } \oplus \mathbb { R } : ( a , b ) \mapsto ( b - a , b - a ) .
$$

Show that this implies that

$$
H ^ { 2 } ( T ^ { 2 } , \mathbb { R } ) = \mathbb { R } ^ { 2 } / \mathrm { i m } j ^ { * } = \mathbb { R } .
$$

Finally, use the Mayer-Vietoris sequence for the above decomposition to show that $b ^ { 1 } ( T ^ { 2 } ) =$ $b ^ { 2 } ( T ^ { 2 } ) + 1$ . Conclude that $H ^ { 1 } ( T ^ { 2 } , \mathbb { R } ) = \mathbb { R } \oplus \mathbb { R }$ .

Another way to decompose the 2-torus is by viewing it as a square with opposite edges identified. Delete one point $^ *$ from the interior of the square. An open covering of the torus is then given by the open sets $X = T ^ { 2 } - *$ and a small disc $Y$ which is an open neighborhood of $^ *$ . The space $X$ is of the homotopy type of a wedge $S ^ { 1 } \vee S ^ { 1 }$ of two circles. A wedge of two spaces is their disjoint union with one point of each space (the base point) identified. The cohomology of $Y$ is trivial, so the cohomology of $T ^ { 2 }$ can be computed from the cohomology of $S ^ { 1 } \vee S ^ { 1 }$ , which is easily done using the Mayer-Vietoris sequence. The nice thing about this procedure is that it can be extended to any higher genus orientable surface. A genus $g$ surface $\Sigma _ { g }$ can be constructed by identifying appropriate edges of a polygon with $2 g$ edges. Deleting one point from $\Sigma _ { g }$ results in a space homotopy equivalent to the wedge of $2 g$ circles. This can then be used to how that

$$
b ^ { 1 } ( \Sigma _ { g } ) = 2 g .
$$

Exercise 4. An $n$ -sphere $S ^ { n }$ can be covered by two hemispheres (essentially two open $n$ -balls), which intersect in a space of the homotopy type of an $S ^ { n - 1 }$ . Use this and the Mayer-Vietoris sequence to show that $H ^ { 1 } ( S ^ { n } ) = 0$ for $n > 1$ (what is different for $n = 1 ?$ ) and $H ^ { k } ( S ^ { n } ) = H ^ { k - 1 } ( S ^ { n - 1 } )$ for $k > 1$ and $n > 1$ . Conclude that

$$
H ^ { k } ( S ^ { n } ) = \left\{ \begin{array} { c c c } { { \mathbb { R } } } & { { \mathrm { f o r } } } & { { k = 0 , n } } \\ { { 0 } } & { { \mathrm { f o r } } } & { { 0 < k < n } } \end{array} \right. .
$$

# 3.5 Why categories?

It turns out that the most important properties of many constructions in algebraic topology – such as (co)homology and homotopy – can be rephrased very naturally in the language of category theory. Category theory is extremely useful for understanding the form and consequences of recurring structures in mathematics (and hence physics and other sciences) in full generality. Since categories are still quite generally avoided by the physics community, this section hopes to illustrate that they, at least sometimes, help to understand rather than obscure.

A category $c$ is a class4 of elements called objects and for each two objects $A$ and $B$ a set ${ \mathrm { H o m } } ( A , B )$ of morphisms, such that whenever $f \in \mathrm { H o m } ( A , B )$ and $g \in { \mathrm { H o m } } ( B , C )$ , their composite $g \circ f \in \operatorname { H o m } ( A , C )$ is defined. Furthermore, the composition is required to satisfy two further axioms:

1. The identity axiom. For every object $A$ there is an identity element $1 _ { A } \in \operatorname { H o m } ( A , A )$ such that for any $f \in \mathrm { H o m } ( A , B )$ and $g \in { \mathrm { H o m } } ( B , A )$

$$
f \circ 1 _ { A } = f \quad 1 _ { A } \circ g = g
$$

2. The associativity axiom. For every $f ~ \in ~ \operatorname { H o m } ( A , B )$ , $g \in \mathrm { H o m } ( B , C )$ and $h \in$ ${ \mathrm { H o m } } ( C , D )$

$$
h \circ ( g \circ f ) = ( h \circ g ) \circ f .
$$

Example 8. The category with groups as objects and group homomorphisms as morphisms will be denoted by $\mathcal { G }$ . Likewise, we have $\nu$ , the category of all vector spaces and linear homomorphisms, $\boldsymbol { \tau }$ , the category of all topological spaces and continuous maps, and $\boldsymbol { S }$ , the category of all smooth manifolds and smooth maps.

Definition 6. Two objects $A$ and $B$ in a category $c$ are called isomorphic if there exist $f \in \operatorname { H o m } ( A , B )$ and $g \in { \mathrm { H o m } } ( B , A )$ such that

$$
g \circ f = 1 _ { A } , \quad f \circ g = 1 _ { B }
$$

For a very basic example of a categorical proof, assume that given an $f \in \mathrm { H o m } ( A , B )$ there exist two maps $g , g ^ { \prime } \in \operatorname { H o m } ( B , A )$ that satisfy the above criterion for isomorphism. In that case we immediately deduce that (we drop the composition symbol for convenience) $g = g 1 _ { B } = g f g ^ { \prime } = 1 _ { A } g ^ { \prime } = g ^ { \prime }$ so that both maps are necessarily equal. This implies that we can call $g = g ^ { \prime } = f ^ { - 1 }$ the (unique) inverse of $f$ . Note that we only used the axioms of a category and the fact that $f$ is an isomorphism, so that this uniqueness theorem applies to every category we can think of. We never have to prove this again.

Definition 7. A covariant functor $F : C  \mathcal { D }$ between categories $\boldsymbol { \mathscr { C } }$ and $\mathcal { D }$ is a mapping of objects to objects and morphisms to morphisms, in such a way that:

1. $F ( f : A \to B ) = F ( f ) : F ( A ) \to F ( B )$ ,   
2. $F ( g \circ f ) = F ( g ) \circ F ( f )$ ,   
3. F (1A) = 1F (A).

For a contravariant functor $F$ the second condition is replaced by $F ( g \circ f ) = F ( f ) \circ F ( g )$ .

Exercise 5. Let $F : { \mathcal { C } }  { \mathcal { D } }$ be a (co- or contravariant) functor. Show that if $f : A  B$ is an isomorphism in $\boldsymbol { \mathscr { C } }$ , then $F ( f ) : F ( A ) \to F ( B )$ is an isomorphism in $\mathcal { D }$ .

This last result has very interesting consequences for us, as we now illustrate with some examples.

Example 9. A pointed manifold $( M , x )$ is simply a manifold $M$ with one of its points $x$ singled out. This point is usually called the base point. Now the tangent space construction we reviewed above is easily seen to be a covariant functor from the category of pointed manifolds to the category $\nu$ of vector spaces. To every pointed manifold $( M , x )$ we associate a tangent space $T _ { x } M$ and to every map $f : ( M , x )  ( N , f ( x ) )$ we associate a push forward $f _ { * } : T _ { x } M \to T _ { f ( x ) } N$ . It is easy to see that indeed $( f g ) _ { * } = f _ { * } g _ { * }$ and ${ { 1 } _ { * } } = 1$ . As a consequence, when $f$ is a diffeomorphism, $T _ { x } M$ and $T _ { f ( x ) } N$ are isomorphic as vector spaces for all $x$ . The cotangent space construction is similarly a contravariant functor.

Example 10. From the discussions in previous sections it should be clear that the $p$ -th de Rham cohomology is a contravariant functor from $\boldsymbol { S }$ to $\mathcal { G }$ or $\nu$ . It associates to every manifold $M$ a cohomology group $H ^ { p } ( M , \mathbb { R } )$ and to every map $f : M \to N$ , an induced map $f ^ { * } : H ^ { p } ( N , \mathbb { R } ) \to H ^ { p } ( M , \mathbb { R } )$ . Actually, de Rham cohomology is a functor from $\boldsymbol { S }$ to $\mathcal { R }$ , the category of rings and ring homomorphisms, by sending a manifold $M$ to the cohomology ring $H ^ { \bullet } ( M , \mathbb { R } )$ . This implies that diffeomorphic manifolds have isomorphic cohomology rings, as we mentioned before.

Example 11. By theorem 1, the map from a homotopy class of maps $[ f ]$ to the induced map in cohomology $f ^ { * }$ is well defined (does not depend on the representative of the class). We say that the cohomology functor is homotopy invariant. By the same arguments as in the previous examples, this implies that manifolds of the same homotopy type have isomorphic de Rham cohomology rings.

# Chapter 4

# Fibre Bundles

We now finally turn to fibre bundles. Classic references are [9] and [10], although the uninitiated reader might find it more useful to consult [2], [3], [5] or [7] for more details about the material in this section.

# 4.1 Definitions

A fibre bundle is usually defined as follows:

Definition 8. A fibre bundle consists of the data $( E , \pi , B , F )$ , where $\pi : E  B$ is a continuous surjection, called the projection, between topological spaces, where $E$ is called the total space and $B$ is called the base space. The projection is required to be locally trivial, i.e. for any $b \in B$ there is an open neighborhood $U$ of $b$ such that $\pi ^ { - 1 } ( U )$ is homeomorphic to the product space $U \times F$ in such a way that the diagram

![](images/6fe3c3572c1866dc87eb0237cc78fec260d18bcd38c1a97e2d78aec2af67a548.jpg)

commutes. The topological space $F ^ { \dagger }$ is called the fibre and $U$ is usually called a trivializing neighborhood.

In short, a fibre bundle is a topological space $E$ which locally looks like the product of an open set with a prescribed fibre space $F ^ { \dagger }$ . Intuitively, one can view a fibre bundle as a manifold $B$ with a copy of the fibre $F$ at every point of $B$ . The simplest example is of course a product manifold $\pi : B \times F \to B$ , which is called a trivial bundle. More generally however, the fibres can be ‘twisted’ so that the global structure becomes more intricate than a product. To make this twisting more apparent it is often helpful to cover the base space $B$ with a collection of trivializing open sets $\{ U _ { i } \}$ . On each $U _ { i }$ we thus define a homomorphism between $\pi ^ { - 1 } ( U _ { i } )$ and $U _ { i } \times F$ , called a local trivialization. The twisting – or better, deviation from a product – of the bundle then comes about by ‘gluing’ the fibres together in a nontrivial way. This gluing and twisting is encoded in what are called transition functions which are elements of a topological group $G$ , called the structure group of the bundle. A fibre bundle endowed with an open cover and collection of local trivializations, which give rise to an explicit set of transition functions is called a coordinate bundle. More precisely:1

Definition 9. A coordinate bundle $( E , \pi , B , F , G )$ consists of the following elements:

(i) A smooth manifold $E$ called the total space.

(ii) A smooth manifold $B$ called the base space.

(iii) A Lie group $G$ called the structure group. Sometimes $G$ will be taken to be a discrete group which, given the discrete topology, can be seen as a topological group.

(iv) A left $G$ -space $F ^ { \dagger }$ , called the (typical) fibre. By left $G$ -space we mean that $G$ acts on $F ^ { \dagger }$ from the left,

$$
\begin{array} { r l r l } { g ( h t ) = ( g h ) t , } & { { } \quad } & { } & { { } g , h \in G , \quad t \in F , } \\ { e ( t ) = t } & { { } \quad } & { } & { { } t \in F . } \end{array}
$$

(v) A surjection $\pi : E  B$ called the projection. For $b \in \ B$ , the inverse image $\pi ^ { - 1 } ( b ) \equiv F _ { b } \cong F$ is called the fibre at $b$ .   
(vi) An open covering $\{ U _ { i } \}$ of $B$ and a set of diffeomorphisms $\phi _ { i } : U _ { i } \times F \to \pi ^ { - 1 } ( U _ { i } )$ such that $\pi \phi _ { i } ( b , t ) = b$ . The map $\phi _ { i }$ is called a local trivialization.   
(vii) At each point $b \in B$ , $\phi _ { i , b } ( t ) \equiv \phi _ { i } ( b , t )$ is a diffeomorphism, $\phi _ { i , b } : F \to F _ { b }$ . On each overlap $U _ { i } \cap U _ { j } \neq \emptyset$ , we require $g _ { i j } = \phi _ { i , b } ^ { - 1 } \phi _ { j , b } : F \longrightarrow F$ to be an element of $G$ , i.e. we have a smooth map $g _ { i j } : U _ { i } \cap U _ { j } \to G$ such that

$$
\phi _ { j } ( b , t ) = \phi _ { i } ( b , g _ { i j } ( b ) t ) .
$$

Of course the properties of a fibre bundle should not depend on the specific covering of the base manifold or choice of local trivialisations. A fibre bundle should therefore be seen as an equivalence class of coordinate bundles2. For practical purposes it is however often useful and sufficient to study coordinate bundles. In most of this and the next section we will work with coordinate bundles, although we will simply refer to them as fibre bundles as well. In the last two chapters (and the last subsection of this section), we will have less need for explicit trivializations and effectively switch back to the first general definition of fibre bundle. For convenience we will use $F \longrightarrow E \longrightarrow B$ or simply $E$ , to denote $( E , \pi , B , F , G )$ .

Let us look at some of the consequences of the above definition. From their definition (vii), it is clear that on triple overlaps, the transition functions obey what are called cocycle conditions

$$
g _ { i j } g _ { j k } = g _ { i k } , \qquad \mathrm { o n } \quad U _ { i } \cap U _ { j } \cap U _ { k } \neq \emptyset .
$$

Taking $i = k$ in the above equation shows that

$$
g _ { i j } ^ { - 1 } = g _ { j i } , \qquad \mathrm { o n } \quad U _ { i } \cap U _ { j } \neq \emptyset .
$$

These conditions evidently have to be fulfilled to be able to glue all local pieces of the bundle together in a consistent way. One can show that, given a base manifold, fibre and set of transition functions satisfying the cocycle conditions, one can completely reconstruct the fibre bundle. In this sense the transition functions thus completely characterize a fibre bundle. Consequently, a fibre bundle is trivial if and only if all transition functions can be chosen to be identity maps. Since a choice of local trivialization $\phi _ { i }$ results in a choice of local coordinates, the transition functions are nothing but a transformation of ‘coordinates’ in going from one open subset of $B$ to another. When we will discuss gauge theories they will represent gauge transformations in going from one patch to another.

Of course, one should be able to change the choice of local trivializations (coordinates) within one patch. Say that for an open covering $U _ { i }$ of $M$ we have two sets of trivializations $\{ \phi _ { i } \}$ and $\{ \phi _ { i } \}$ of the same fibre bundle. Define a map $f _ { i } : F \to F$ at each point $b \in U _ { i }$

$$
f _ { i } ( b ) = \phi _ { i , b } ^ { - 1 } \widetilde { \phi } _ { i , b } .
$$

It is easy to show that the transition functions corresponding to both trivializations are related by

$$
\widetilde { g } _ { i j } ( b ) = f _ { i } ( b ) ^ { - 1 } g _ { i j } ( b ) f _ { j } ( b ) .
$$

In the language of $\check { \mathrm { C } }$ ech cohomology one would say that both cocycles are the same up to a coboundary. While the $g _ { i j }$ will be gauge transformations for gluing patches together, the $f _ { i }$ will be gauge transformations within a patch. From eq. (4.1.7) it is clear that in general the transition functions of a trivial bundle will have the factorized form

$$
g _ { i j } ( b ) = f _ { i } ( b ) ^ { - 1 } f _ { j } ( b ) .
$$

In the language of $\check { \mathrm { C } }$ ech cohomology this would be a pure coboundary.

Definition 10. A section $s$ is a smooth map $s : B \to E$ such that $\pi s ( b ) = b$ for all $b \in B$ . In other words, $s ( b ) \in \pi ^ { - 1 } ( b )$ for all $b \in B$ . This is sometimes also referred to as a global section. If a section can only be defined on an open set $U$ of $B$ , it is called a local section. The set of all sections of $E$ is denoted by $\Gamma ( B , E )$ or simply $\Gamma ( E )$ , while the set of all local sections over $U$ is denoted by $\Gamma ( U , E )$ .

# 4.2 Vector and principal bundles

Usually one studies fibre bundles for which the fibre has additional structure. Of particular importance are cases where the fibre is either a vector space or the structure group itself. Let us start with the former.

Definition 11. A vector bundle $( E , \pi , B , V , G )$ of rank $n$ is a fibre bundle where the fibre is an $n$ -dimensional vector space $V$ and the structure group acts linearly on the fibres. The structure group is thus a subgroup of $G L ( n )$ .

Example 12. The prototype of a vector bundle is the tangent bundle of a manifold. As we reviewed in subsection 2.3, to every point $x$ of a manifold $M$ we associate a vector space $T _ { x } M$ . The disjoint union of all these vector spaces is called the tangent bundle $^ { T M }$ . Note that vector fields are thus sections of the tangent bundle, $\mathcal { X } ( M ) = \Gamma ( T M )$ . Over an open subset $U \subset M$ one can define a frame, i.e. a set of $n$ linearly independent vector fields, $e _ { a } \in \Gamma ( U , T M )$ , $a \in \{ 1 , \ldots , n \}$ . This allows one to write any vector field over $U$ as $X = X ^ { a } e _ { a }$ , where the $X ^ { a }$ are called the components of the vector field. Over $U$ a local trivialization is then

$$
\phi ^ { - 1 } ( p ) = \left( \pi ( p ) , V ^ { a } \right) , \qquad p = V ^ { a } e _ { a } \in E ,
$$

where the $n$ -tuple ( $V ^ { a }$ ) is seen as a set of coordinates on the standard $n$ -dimensional vector space $\mathbb { R } ^ { n }$ . Of course one can just as well start from another frame $\tilde { e } _ { a }$ . This leads to a local trivialization $\ddot { \phi } ^ { - 1 } ( p ) = ( \pi ( p ) , \ddot { V } ^ { a } )$ . Both frames are related by a $G L ( n )$ transformation, showing that the transition functions are indeed elements of $G L ( n )$ . Given a metric on $M$ , one can always choose the frames to be orthonormal, so that the structure group reduces to $O ( n )$ .3

An interesting question arises related to the previous example. Given a frame on $U$ , can one extend it over the whole manifold? If this were the case, one would be able to define a local trivialization over the whole manifold and the tangent bundle would be trivial. A manifold with trivial tangent bundle is called parallelizable. Notice that Lie groups are always parallelizable. Even in less extreme cases, one could wonder whether one could reduce the structure group further down to some $G \subset G L ( n )$ . Indeed, if all transition functions can be chosen to lie in this subgroup $G$ , this group would be equally well-suited for defining the bundle. It is of interest to find the smallest such subgroup, since it tells us how close – or far – the bundle is from being trivial. Since this question is intimately related to the existence of certain frames on $M$ , why not study a “bundle of frames”.

Example 13. The frame bundle $F M$ of a manifold $M$ is the fibre bundle with as fibre over $x$ the set of all frames at $x$ . Since, given a ‘reference’ frame at $x$ , all other frames are unambiguously related to it by a $G L ( n )$ transformation, the fibre is isomorphic to $G L ( n )$ itself. The frame bundle is thus a fibre bundle with as typical fibre the structure group $G L ( n )$ itself. A section of $F M$ over some $U \subset M$ is simply a frame over $U$ . The existence of a global frame for $^ { T M }$ – and hence the triviality of $^ { T M }$ – is thus equivalent to the existence of a global section of $F M$ .

It thus appears that fibre bundles with as fibre the structure group itself might be fundamental to understanding fibre bundles in general. Such fibre bundles are called principal bundles. Remember that the fibre is required be a left $G$ -space by definition. A crucial property of the structure group (as fibre) is that it simultaneously is a right $G$ -space. Both left and right actions are simply left and right multiplication within the group, so that by associativity both actions commute.

In general an action of $G$ on a $G$ -space $X$ leads to several interesting constructions:

• The isotropy group $H _ { x }$ of $x \in X$ is comprised of all group elements which leave $x$ fixed: $H _ { x } = \{ g \in G : g x = x \}$ .   
• The orbit $G _ { x }$ of an $x \in X$ is the set of all elements which can be reached from $x$ by an action of $G$ , $G _ { x } = \{ y \in X : \exists g \in G , y = g x \}$ .

The action is called free if the only element of $G$ which has fixed points is the identity, i.e. the isotropy group $H _ { x } = \{ e \}$ for all $x$ ; it is called transitive if starting from a fixed element of $X$ every other element of $X$ can be obtained by an action of an element in $G$ , i.e the orbit $G _ { x } = X$ for every $x$ . The quotient, $X / G _ { x }$ is then called the orbit space. Clearly, the actions defined by left and right multiplication within a group are both free and transitive. For instance $G _ { g } = G$ for all $g \in G$ . We use the right action on $G$ to define a principal bundle.

Definition 12. A principal bundle $( P , \pi , B , G )$ is a fibre bundle which is a right $G$ -space such that the action is free and $\pi ( p g ) = \pi ( p )$ for $p \in { \cal P }$ and $g \in G$ . When restricted to a fibre $\pi ^ { - 1 } ( b )$ the action is also transitive. This implies that the fibre (i.e. the orbit of any point $p$ ) is isomorphic to the structure group $G$ iself, and the base $B$ is isomorphic to the orbit space $P / G$ . A principal bundle is usually denoted by $P ( B , G )$ and called a (principal) $G$ -bundle over $B$ .

Note that the left $G$ -action is ‘local’, i.e. it depends on the local trivialization (and is thus a gauge symmetry), while the right $G$ -action is defined in a ‘global’ sense, i.e. without referring to a local trivialization. Obviously, in principle it doesn’t matter which one is right or which is left, the main point is that for a principal bundle the $G$ -action makes sense globally.

Exercise 6. For a local trivialization $p = \phi ( b , g )$ , we define the right action to be $p a =$ $\phi ( b , g a )$ for $a \in G$ . This obviously satisfies $\pi ( p a ) = \pi ( p ) = b$ . Show that the action defined in this way is indeed independent of the choice of local trivialization. Which basic group property is responsible for this?

Given a section $s : U \to \pi ^ { - 1 } ( U )$ , we can always choose a local trivialization such that $s ( x ) = \phi ( x , e )$ . This is called the canonical local trivialization with respect to $s$ . This means that for a point $p = s ( x ) g$ for some $g \in G$ , we get $p = \phi ( x , g )$ . On an overlap it is easy to convince yourself that for $g _ { i } = g _ { i j } g _ { j }$ , we find $s _ { i } ( x ) = s _ { j } ( x ) g _ { j i }$ .

Example 14. In a sense principal bundles are probably not such unfamiliar objects. The homogeneous space construction is a classic example. Given a (finite dimensional) Lie group $G$ and any closed Lie subgroup $H$ , the quotient $M = G / H$ can be shown to be a manifold, called a homogeneous space. The quotient map $\pi : G \to G / H$ is clearly a projection. The inverse image $\pi ^ { - 1 } ( x )$ of any point $x$ in $M$ is diffeomorphic to $H$ , which is thus the fibre. The right action $H \times G \to G : ( h , g ) \mapsto g h$ indeed satisfies $\pi ( g h ) = \pi ( g )$ by definition. A well known example is $S O ( 2 )  S O ( 3 )  S ^ { 2 }$ . This is because $S O ( 3 )$ acts transitively on $S ^ { 2 }$ and $S O ( 2 )$ is the isotropy subgroup of any point on $S ^ { 2 }$ . This generalizes to

$$
S O ( n + 1 ) / S O ( n ) = S ^ { n } .
$$

The frame bundle introduced above is another example of a principal bundle $F M \equiv$ $F M ( M , G L ( n ) )$ . Clearly, $^ { T M }$ and $F M$ are somehow associated and their triviality – or more generally, their amount of ‘twisting’ – are intimately related. This notion of associated bundles can be generalized and made more precise.

Definition 13. Consider a principal $G$ -bundle $P ( B , G )$ and a left $G$ -space $F$ . The fibre bundle $E _ { P }$ with fibre $F ^ { \dagger }$ , base space $B$ and structure group $G$ associated to $P$ is defined as follows. Consider the product $P \times P$ and the equivalence relation $( p g , t ) \sim ( p , g t )$ for all $g \in G$ , $p \in P$ and $t \in F$ . The total space of $E _ { P }$ is $P \times F / \sim$ and the projection $\pi _ { E } [ ( p , t ) ] = \pi _ { P } ( p )$ .

What this does effectively is changing the fibre from $G$ to $F ^ { \dagger }$ (remember that the action   
of $G$ on itself is transitive). The transition functions are essentially unchanged so that the   
global twisting of both bundles are related. To see this last point more clearly, assume   
$F ~ = ~ V$ , some vector space, and the left $G$ -action is provided by some representation   
$\rho : G \to G L ( n )$ . Given a local trivialization on $U$ for $P$ , $p = \phi ^ { F } ( b , g )$ , we define the   
associated trivialization for $E _ { P }$ by $[ ( p , v ) ] = \phi ^ { E } ( b , \rho ( g ) v )$ . Show that this is well-defined,   
i.e. independent of the equivalence class. Now assume that on some overlap $U _ { i } \cap U _ { j }$ we   
have that the transition functions in $P$ are related by . Then we find that $g _ { i } = g _ { i j } g _ { j }$

$$
\phi _ { j } ^ { E } ( b , \rho ( g _ { j } ) v ) = \phi _ { i } ^ { E } ( b , \rho ( g _ { i j } ) \rho ( g _ { j } ) v ) .
$$

Comparing this to (4.1.3) we see that the new transition functions are of the form $\rho ( g _ { i j } )$ , i.e. they are simply representations of the original transition functions. The situation for more general fibres follows along roughly the same lines. Two fibre bundles with same base space and structure group are more generally called associated if their respective associated principal bundles are equivalent (in the sense which we will discuss in the next subsection). In gauge theory it is important to be able to associate a vector bundle to a given principal bundle and vice versa.

We end this section by collecting, without proof, some theorems which were hinted at throughout this section. They illustrate the importance of the notion of associated bundles.

Theorem 3. Triviality versus existence of sections:

A vector bundle of rank $n$ is trivial iff it admits $n$ linearly independent sections, i.e if it admits a global frame.

A principal bundle is trivial iff it admits a section.

Theorem 4. A fibre bundle is trivial if its associated principal bundle is trivial.

Corollary 2. A fibre bundle is trivial if its associated principal bundle admits a section.

Summarizing, to establish the triviality of a fibre bundle it suffices to find one global section of its associated principal bundle. Needless to say the existence of a global section on a principal bundle is a strong requirement. But even when the fibre bundle is not trivial, its global structure can be unraveled by studying its associated principal bundle. This will be amply illustrated in the next section. First we turn to some more constructions with bundles.

# 4.3 Operations on bundles

In this subsection, we temporarily switch back to the more general definition 8 of fibre bundle.

To meaningfully compare two bundles we need more structure than just continuous maps. This leads to the definition of a bundle map.

Definition 14. Given two bundles $( E , \pi , B )$ and $( E ^ { \prime } , \pi ^ { \prime } , B ^ { \prime } )$ , a bundle map is a pair $( u , f )$ of continuous maps $u : E \to E ^ { \prime }$ and $f : B  B ^ { \prime }$ such that the diagram below is commutative, i.e. $\pi ^ { \prime } u = f \pi$ .

![](images/5f2c389778d72006af55bb9f9e943a8bc6da1bd995683d37ed99e1371030589f.jpg)

Said differently, this means that the fibre $\pi ^ { - 1 } ( b )$ over $b$ is mapped to the fibre $\pi ^ { \prime - 1 } ( f ( b ) )$ over $f ( b )$ . When $B = B ^ { \prime }$ , we will refer to the above bundle map as a $B$ -map, i.e. a map $u : E \to E ^ { \prime }$ for which $\pi = \pi ^ { \prime } u$ , or the diagram

![](images/3b40a9dd51977e5c900b7c6ca69533d5688a73fc3a36de03e7c6837600180961.jpg)

commutes. We already secretly encountered an example of a $B$ -map. Indeed, sections are precisely the bundle maps $s : ( B , 1 _ { B } , B ) \to ( E , \pi , B )$ . This implies that all properties of $B$ -maps are also true for sections.4

Exercise 7. Defining the identity bundle map to be $( 1 _ { E } , 1 _ { B } )$ and composition of bundle maps in the natural way, namely $( v , g ) \circ ( u , f ) = ( v u , g f )$ , show that this turns the collection of bundles and bundle maps into a category $\boldsymbol { B }$ . Likewise we have the category of bundles over $B$ and $B$ -maps.

Definition 15. Two bundles are called equivalent if they are isomorphic in $\boldsymbol { B }$ , the category of bundles and bundle maps. The inverse of the bundle map $( u , f )$ is $( u ^ { - 1 } , f ^ { - 1 } )$ .

Using the same notation as before, we get that two fibre bundles are equivalent if $u$ restricted to the fibres is a homeomorphism u|b : Eb → E′f(b).

Example 15. For a bundle map between vector bundles, the restriction of $u$ to the fibres is required to act linearly. This implies that a $B$ -map between vector bundles over $B$ is an isomorphism if and only if the map $u$ restricted to each fibre is a vector space isomorphism. For any vector bundle $E$ , one can define its dual $E ^ { * }$ , where the fibre over a point $b$ is simply the vector space dual to the fibre of $E$ over $b$ . For real vector bundles, given a metric, there is a natural isomorphism between the fibres and their duals. For instance, the tangent bundle to a manifold $^ { T M }$ is isomorphic to its dual, the cotangent bundle $T ^ { * } M$ . For complex vector bundles, a bundle is not necessarily isomorphic to its dual.

In terms of local transition functions two $\check { \mathrm { C } }$ ech cocycles which differ by a coboundary determine equivalent bundles. Thus the set of 1-cocycles modulo coboundaries is bijective to the set of equivalence classes of fibre bundles over a given space.

Once one has collected some examples of bundles, one likes to have some ways of building new ones out of them. A straight forward construction is simply taking the cartesian product of two bundles. Indeed, given two bundles $( E , \pi , B )$ and $( E ^ { \prime } , \pi ^ { \prime } , B ^ { \prime } )$ , the product $( E \times E ^ { \prime } , \pi \times \pi ^ { \prime } , B \times B ^ { \prime } )$ is also a bundle. More interesting however, is the fibre product.

Definition 16. The fibre product of two bundles $( E , \pi , B )$ and $( E ^ { \prime } , \pi ^ { \prime } , B )$ is the bundle $( E \times _ { B } E ^ { \prime } , \bar { \pi } , B )$ , where $E \times _ { B } E ^ { \prime }$ is comprised of elements $( p , p ^ { \prime } ) \in E \times E ^ { \prime }$ such that $\pi ( p ) = \pi ^ { \prime } ( p ^ { \prime } )$ and $\bar { \pi } ( p , p ^ { \prime } ) = \pi ( p ) = \pi ^ { \prime } ( p ^ { \prime } )$ .

The fibre of $E \times _ { B } E ^ { \prime }$ over $b$ is $\pi ^ { - 1 } ( b ) \times \pi ^ { \prime - 1 } ( b )$ , whence the name fibre product. Note that $\pi ( p ) = \pi ^ { \prime } ( p ^ { \prime } ) $ implies that of the pairs $( b , \bar { b } ) \in B \times B$ only the diagonal elements remain. The resulting bundle has thus again base space $B$ . This construction becomes very transparent for vector bundles where it is called the Whitney sum. The Whitney sum of two vector bundles $( E , \pi , B , V , G )$ and $( E ^ { \prime } , \pi ^ { \prime } , B , V ^ { \prime } , G ^ { \prime } )$ is thus a vector bundle with base manifold $B$ and fibre $V \oplus V ^ { \prime }$ . The transition functions are of block diagonal form, the upper block being a representation of $G$ , and the lower of $G ^ { \prime }$ . The Whitney sum of vector bundles $E$ and $E ^ { \prime }$ is denoted by $E \oplus E ^ { \prime }$ .

Example 16. Consider the two sphere as an embedded submanifold in $\mathbb { R } ^ { 3 }$ , $S ^ { 2 } = \{ ( x , y , z ) \in$ $\mathbb { R } ^ { 3 } : x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 1 \}$ . Both the tangent bundle $T S ^ { 2 }$ and the normal bundle $N S ^ { 2 }$ are subbundles of the product bundle $\left( S ^ { 2 } \times \mathbb { R } ^ { 3 } , \pi , S ^ { 2 } \right)$ . The total space of $T S ^ { 2 }$ are all $( b , v ) \in S ^ { 2 } \times \mathbb { R } ^ { 3 }$ for which $b \cdot v = 0$ , where the dot represents the standard Euclidean inner product on $\mathbb { R } ^ { 3 }$ , and is a non-trivial bundle. In fact, $T S ^ { 2 }$ does not even admit one everywhere non-zero section, let alone a frame. This is often paraphrased as “One cannot comb hair on a twosphere”. The total space of $N S ^ { 2 }$ on the other hand is composed of all pairs $( b , v )$ for which $v = k b$ , $k \in \mathbb R$ and is trivial. The Whitney sum $T S ^ { 2 } \oplus N S ^ { 2 } = S ^ { 2 } \times \mathbb { R } ^ { 3 }$ is trivial.

Example 17. In generalized complex geometry many notions of complex (and symplectic) geometry are generalized by applying them not to the tangent bundle $^ { T M }$ , but to $T M \oplus$ $^ { T * } M$ . If $M$ is Riemannian a relevant structure group is then a subgroup of $O ( n ) \times O ( n )$ .

We now turn to a notion which is crucial for the classification of bundles, namely the pull-back of a bundle. To motivate this, let us first discuss restrictions of bundles. Let $( E , \pi , B )$ be a bundle and consider a subspace $A$ of $B$ . Then the restriction of $E$ to $A$ i s the bundle $( E ^ { \prime } , \pi ^ { \prime } , A )$ where $E ^ { \prime } = \pi ^ { - 1 } ( A )$ and $\pi ^ { \prime } = \pi | _ { E ^ { \prime } }$ . Another way to say this is that $E ^ { \prime }$ is comprised of all $p \in E$ for which $\pi ( p ) = i ( a )$ , where $i : A  B$ is the inclusion map. The restricted bundle is often denoted by $E | _ { A }$ . This is now easily generalized.

Definition 17. Given a bundle $( E , \pi , B )$ and a map $f : B ^ { \prime } \to B$ . The pull-back of $E$ (often also called the induced bundle) under the map $f$ is the bundle $f ^ { * } ( E , \pi , B ) =$ $( f ^ { \ast } E , \pi _ { 1 } , B ^ { \prime } )$ , where $f ^ { * } E$ is the subspace of $B ^ { \prime } \times E$ of all pairs $( b ^ { \prime } , p )$ for which $\pi ( p ) = f ( b ^ { \prime } )$ and $\pi _ { 1 } ( b ^ { \prime } , p ) = b ^ { \prime } $ . In other words, the fibre over $b ^ { \prime }$ in $f ^ { * } E$ is $\pi ^ { - 1 } ( f ( b ^ { \prime } ) )$ , which is simply the fibre over $f ( b ^ { \prime } )$ in $E$ .

Let $g _ { i j } : U _ { i } \cap U _ { j } \to G$ be a transition function for $E$ , the corresponding transition function of the pull-back bundle is easily seen to be of the form $g _ { i j } \circ f : f ^ { - 1 } ( U _ { i } ) \cap f ^ { - 1 } ( U _ { j } ) \to$ $G$ . Clearly, given the inclusion map $i : A  B$ from before, $E | _ { A } = i ^ { * } E$ . Another way of saying that a bundle $E$ is locally trivial is saying that for any point of the base there is a neighborhood $U$ such that $E | _ { U }$ is trivial. One can show that the pull-back of a locally trivial bundle is locally trivial, of a vector bundle is a vector bundle, and of a principal bundle is a principal bundle.

Exercise 8. Show that $1 ^ { * } E$ and $E$ are $B$ -equivalent bundles. For maps $g : B _ { 2 } \to B _ { 1 }$ and $f : B _ { 1 } \to B$ , show that $( f g ) ^ { * } E$ and $g ^ { \ast } ( f ^ { \ast } E )$ are $B _ { 2 }$ - equivalent. This makes the pull-back a contravariant functor. In which sense exactly will be discussed in a later section.

There exists a natural map $( w , f ) : f ^ { * } E \to E$ such that $w ( b ^ { \prime } , p ) = p$ . This is clearly a bundle map called the natural $f$ -map. If $f$ is a homeomorphism, then it is easy to see that $f ^ { * } E$ is isomorphic to $E$ . To show this, one needs to construct an inverse for the natural $f$ -map. This is provided by the map $E \to f ^ { * } E : p \mapsto ( f ^ { - 1 } \pi ( p ) , p )$ . To establish some kind of reverse to this statement, let us focus on vector bundles. Given a bundle map between vector bundles $( u , f ) : E ^ { \prime } \to E$ , one can always factor through the natural $f$ -map

$$
\begin{array} { l c l } { { E ^ { \prime } \xrightarrow { v } \longrightarrow f ^ { * } E \xrightarrow { w } } } & { { E } } \\ { { \Bigg | \pi ^ { \prime } } } & { { \Bigg | \pi _ { 1 } } } & { { \Bigg | \pi } } \\ { { \Bigg . } } & { { 1 _ { B ^ { \prime } } \Bigg . } } & { { \Bigg \downarrow } } \\ { { B ^ { \prime } \xrightarrow [ ] { 1 _ { B ^ { \prime } } } \Delta ^ { \prime } \xrightarrow [ ] { } { \Bigg | \pi ^ { \prime } } } } & { { f } } & { { \Bigg \downarrow } } \end{array}
$$

where $v ( p ^ { \prime } ) = ( \pi ^ { \prime } ( p ^ { \prime } ) , u ( p ^ { \prime } ) )$ so that $\pi ^ { \prime } = \pi _ { 1 } v$ . Note also that indeed $u \ = \ w v$ . Note now that if $u$ is a bundle morphism which restricts to vector space isomorphisms on the fibres5, $v$ is a vector space isomorphism when restricted to fibres. This implies that $v$ i s an isomorphism of vector bundles, since it can be seen as a $B ^ { \prime }$ -map. In conclusion, when $( u , f ) : E ^ { \prime } \to E$ is a vector bundle map which restricts to isomorphisms on the fibres, $E ^ { \prime }$ is isomorphic to $f ^ { * } E$ . A special case of this is of course that if $( u , f )$ is an isomorphism, both $E$ and $E ^ { \prime }$ are isomorphic to $f ^ { * } E$ as well.

# Chapter 5

# Connections on fibre bundles

We would like to have some more elaborate means for studying the non-triviality of fibre bundles. One way about this is by introducing a notion of parallel transport. Indeed, we know that parallel transporting a tangent vector along a closed path in a manifold $M$ and comparing initial and final ‘states’, we can deduce something about ‘curvature’. This curvature can tell us something about the non-triviality of the tangent bundle, e.g. when integrated along certain submanifolds. A classic example of this is the Gauss-Bonnet theorem which states that the integral of the curvature two-form over a two-dimensional surface is proportional to its Euler characteristic.

Given a curve in $M$ , there are many possible choices for transporting a given tangent vector along this curve which are all equally valid as a choice for what ‘parallel’ might mean1. Translated into the language of fibre bundles, we want to, given a curve $\gamma$ in the base $M$ , find a way of assigning a corresponding section of the tangent bundle $s ^ { \gamma } \in T M$ .

In the above construction, there is nothing particular about the tangent bundle which makes this work. For a general fibre bundle, given a certain motion in the base manifold, we can set out to define a corresponding motion in the fibre. Since, given a fibre bundle, there is no a priori notion of what ‘parallel’ should mean, we need some additional structure to give meaning to the notion of ‘parallel motion’. This will be provided by the choice of a connection on the bundle. The most natural and straight forward setting for defining a connection is a principal bundle $P$ . Most of the following discussion will thus be focussed on principal bundles. How to go from a connection on $P$ to a connection on an associated bundle $E _ { P }$ will be sketched at the end of the section.

In this section, we mainly follow the presentation in [2] and [11], although [5] and [7] are also useful references. A lot of the proofs which are skipped in this section can also be found in [12].

# 5.1 Parallel transport in a principal bundle

Consider a principal bundle $P ( M , G )$ . Given a curve $\gamma$ in the base $M$ , to define parallel transport we want to define a corresponding choice of curve $\gamma _ { P }$ in the total space $P$ . There are of course many possible choices. We will use the vectors tangent to $\gamma _ { P }$ to characterize a particular choice. Note that these vectors live in the tangent bundle $T P$ of the total space $P$ . Given a vector $X _ { x }$ in $T _ { x } M$ tangent to $\gamma$ at some point $x$ along $\gamma$ , the curve $\gamma _ { P }$ through the fibre $G _ { x }$ above $x$ will be characterized by a ‘lift’ of $X _ { x }$ , namely an element of $T _ { p } P$ for some $p$ such that $\pi ( p ) = x$ .

The question is then how to lift a vector in $T _ { \gamma } M$ to $T P$ . At every point $p \in { \cal P }$ , we can decompose $T _ { p } P$ into a subspace of vectors tangent to the fibre $G$ , called the vertical subspace $V _ { p } P$ and a complement $H _ { p } P$ , called the horizontal subspace, such that $T _ { p } P =$ $V _ { p } P \oplus H _ { p } P$ . Since $V _ { p } P$ corresponds to motion along the fibres and is essentially fixed, a choice of $H _ { p } P$ is the crucial ingredient in the definition of parallel transport. We will require the vectors tangent to $\gamma _ { P }$ at $p$ to lie in $H _ { p } P$ .

A choice of connection now essentially boils down to a choice of horizontal subspace. Let us be a bit more precise.

Definition 18. A connection on $P$ is a smooth and unique separation of the tangent space $T _ { p } P$ at each $p$ into a vertical subspace $V _ { p } P$ and a horizontal subspace $H _ { p } P$ such that

(i) $T _ { p } P = V _ { p } P \oplus H _ { p } P .$ (ii) $H _ { p g } P = R _ { g * } H _ { p } P$ for every $g \in G$ .

Condition (i) just means that every $X \in T _ { p } P$ can be written in a unique way as a sum $X = X ^ { V } + X ^ { H }$ , where $X ^ { V } \in V _ { p } P$ and $X ^ { H } \in H _ { p } P$ . The equivariance condition (ii) means that the choice of horizontal subspace at $p$ determines all the horizontal subspaces at points $p g$ . This roughly means that all points above the same point $x = \pi ( p )$ in the base space will be parallel transported in the same way (recall that $\pi ( p ) = \pi ( p g )$ ). It is for this second requirement that we need the bundle to be principal. Notice also that we have the short exact sequence

$$
0 \longrightarrow V _ { p } { \cal P } \stackrel { i } { \longrightarrow } T _ { p } { \cal P } = V _ { p } { \cal P } \oplus { \cal H } _ { p } { \cal P } \stackrel { \pi _ { * } } { \longrightarrow } T _ { \pi ( p ) } { \cal M } \longrightarrow 0 ,
$$

which implies that $\pi _ { * }$ provides an explicit isomorphism between $H _ { p } P$ and $T _ { \pi ( p ) } M$ .

Parallel transport can now immediately be defined by what is called a horizontal lift.

Definition 19. Let $\gamma : [ 0 , 1 ] \to M$ be a curve in the base manifold (a base curve). A curve $\gamma _ { P } : [ 0 , 1 ]  P$ is called the horizontal lift of $\gamma$ if

(i) $\pi ( \gamma _ { P } ) = \gamma$ , (ii) All vectors $X _ { P }$ tangent to $\gamma _ { P }$ are horizontal: $X _ { P } \in H _ { \gamma _ { P } } P$ .

Theorem 5. Let $\gamma : [ 0 , 1 ] \to M$ be a base curve and let $p \in \pi ^ { - 1 } ( \gamma ( 0 ) )$ . Given a connection, there exists a unique horizontal lift $\gamma _ { P }$ such that $\gamma _ { P } ( 0 ) = p$ .

This means that we can (given a connection) uniquely define the parallel transport of a point $p$ in $P$ along a curve $\gamma$ in $M$ by moving it along the unique horizontal lift of $\gamma$ through $p$ . Note that the point $p$ is here the analog of the tangent vector at $x = \pi ( p )$ in the tangent bundle. We have defined parallel transport in a principal bundle!

A loop in $M$ is defined to be a curve $\gamma$ with $\gamma ( 0 ) = \gamma ( 1 )$ . It is interesting to see what happens to a horizontal lift of this loop. In other words, what happens if we parallel transport an element of $P$ along a closed loop in the base? Starting from a point $p$ and moving it along a horizontal lift of a loop, there is no guarantee that we will end up at the same point. In general we will obtain a different point $p _ { \gamma }$ , which depends on the loop $\gamma$ . Since

$$
\pi ( \gamma _ { P } ( 0 ) ) = \gamma ( 0 ) = \gamma ( 1 ) = \pi ( \gamma _ { P } ( 1 ) ) ,
$$

we know that both points will belong to the same fibre, $\pi ( p ) = \pi ( p _ { \gamma } )$ . This means that $p _ { \gamma } = p g$ for some $g \in G$ . If we vary the loop $\gamma$ , but keep the base point $p$ fixed, we generate a group called the holonomy group $H o l _ { p } ( P )$ of $P$ at $p$ , which by definition is a subgroup of $G$ . This group of course also depends on the connection, so $H o l _ { p } ( P )$ is a characteristic not only of $P$ , but also of the connection. If $M$ is connected the holonomy group at all points of $M$ are isomorphic and we can essentially speak of the holonomy group of $P$ ,

$H o l ( P )$ . It is important to add that what we call holonomy here is more general than what is usually referred to as holonomy in the physics literature. For the tangent bundle $^ { T M }$ , what we call holonomy here is there called structure, the name holonomy being reserved only for structure with respect to the Levy-Civita connection.

Given a notion of parallel transport in a principal bundle $P$ , one can easily define parallel transport in an associated bundle $E _ { \rho }$ by

Definition 20. If $\gamma _ { P } ( t )$ is a horizontal lift of $\gamma ( t ) \in M$ in $P$ , then $\gamma _ { E } ( t )$ is defined to be the horizontal lift of $\gamma ( t )$ in $E _ { \rho }$ if

$$
\gamma _ { E } ( t ) = [ ( \gamma _ { P } ( t ) , v ) ] ,
$$

where $v$ is a constant element of $V$ .

Exercise 9. Show that if parallel transport in $P$ is described by $g ( t )$ , then parallel transport in $E _ { \rho }$ is defined by $\rho ( g ( t ) )$ .

# 5.2 Connections

Up to this point, the reader might be confused as to what all this has to do with gauge theories and the usual definition of a connection in physics. To establish the link with physics, we now introduce the connection one-form and clarify its relation to the gauge potential in Yang-Mills theories.

To define the connection one-form properly, we need a more specific construction of the vertical subspace $V _ { p } P$ . Let $A \in { \mathfrak { g } } = T _ { e } G$ be an element of the Lie algebra of $G$ . We saw in subsection 2.5 that $A$ generates a one-parameter flow $\sigma _ { t } ( g )$ through $g$ in $G$ . A slight modification of this construction shows that $A$ will generate a flow in $P$ along the fibre at each point of $M$ by the right action of $G$ on $P$ :

$$
\sigma _ { t } ( p ) = R _ { \exp ( t A ) } p = p \exp ( t A ) .
$$

Note that $\pi ( p ) = \pi ( \sigma _ { t } ( p ) )$ , so that indeed vectors tangent to the curves are elements of $V _ { p } P$ . We now define a map ${ \mathfrak { g } } \to V _ { p } P$ which maps $A$ to the vector tangent to $\sigma _ { t } ( p )$ for $t = 0$ , which we will call (with slight abuse of notation with respect to equation (2.5.13)) $X _ { A } \in V _ { p } P$ . The equivalent of the flow equation (2.5.13) now becomes

$$
X _ { A } ( f ( p ) ) = \left. { \frac { d } { d t } } f ( \sigma _ { t } ( p ) ) \right| _ { t = 0 } .
$$

$X _ { A }$ is called the fundamental vector field associated with $A$ . The fundamental vector fields associated to a basis of the Lie algebra form a basis of the vertical subspace. A connection one-form is now defined as follows.

Definition 21. A connection one-form $\omega \in \Omega P \otimes { \mathfrak { g } }$ (where $\Omega P \equiv \Gamma ( T ^ { * } P ) ,$ is a Lie algebra valued one-form on $P$ satisfying

(i) $\omega ( X _ { A } ) = A$ for every $A \in { \mathfrak { g } }$ ;   
(ii) $R _ { g } ^ { * } \omega = A d _ { g ^ { - 1 } } \omega$ for every $g \in G$ .

More concretely $^ 2$ , (ii) means that for $X \in T _ { p } P$ ,

$$
\begin{array} { r } { \boldsymbol { R _ { g } } ^ { * } \omega _ { p } ( \boldsymbol { X } ) = \omega _ { p g } ( R _ { g * } \boldsymbol { X } ) = g ^ { - 1 } \omega ( \boldsymbol { X } ) g . } \end{array}
$$

The horizontal subspace is then defined as the set

$$
H _ { p } P = \{ X \in T _ { p } P | \omega ( X ) = 0 \} .
$$

When defined in this way, $H _ { p } P$ still satisfies the equivariance condition. To see this, take $X \in H _ { p } P$ and construct $R _ { g * } X \in T _ { p g } P$ . This is an element of $H _ { p g }$ because

$$
\omega ( R _ { g * } X ) = R _ { g } ^ { * } \omega ( X ) = g ^ { - 1 } \omega ( X ) g = 0 .
$$

So both definitions of a connection are equivalent. This connection is defined over all of $P$ . To connect to physics, we have to relate this to a one-form in the base $M$ . It turns out that this can only be done locally (when $P$ is non-trivial).

Definition 22. Let $U$ be an open subset of $M$ . Choose a local section $s$ on $U$

$$
s : U \to \pi ^ { - 1 } ( U ) .
$$

The local connection one-form or gauge potential is now defined as

$$
A \equiv s ^ { * } \omega \in \Gamma ( U , T ^ { * } M , ) \otimes { \mathfrak { g } } = \Omega U \otimes { \mathfrak { g } }
$$

Given a section $s$ on a patch $U$ and a canonical local trivialization, such that every $p = s y$ for some $g \in G$ , it turns out that the way to go back is by the formula

$$
\omega | _ { U } = g ^ { - 1 } \pi ^ { * } A g + g ^ { - 1 } d _ { P } g ,
$$

where $d _ { P }$ is the exterior derivative on $P$ . When writing an expression like the second term on the right hand side, we assume $G$ is a matrix group as before and we use an explicit matrix notation.3

Exercise 10. Show that with the above definition $s ^ { * } \omega | _ { U } ( X ) = A ( X )$ for any $X \in T _ { x } M$ for $x \in U$ , and that $\omega | _ { U }$ satisfies the proper conditions, definition 21, for being a connection one form.

This shows the existence ‘locally’ of $\omega$ . What remains to be shown is that a collection of local connection one-forms $A _ { i }$ on an open cover $\{ U _ { i } \}$ of $M$ gives rise in a unique and well defined way to a (global) connection on $P$ . Clearly, for this to be possible, we need some way to relate $A _ { i }$ and $A _ { j }$ on $U _ { i } \cap U _ { j }$ through the transition function $g _ { i j }$ . The required relation is not hard to deduce from (5.2.8),

$$
A _ { j } = g _ { i j } ^ { - 1 } A _ { i } g _ { i j } + g _ { i j } ^ { - 1 } d g _ { i j } .
$$

This is the important point we wanted to reach. Note that the connection one-form $\omega$ on $P$ is defined globally; it contains global information on the non-triviality of $P$ . The gauge potentials $\{ A _ { i } \}$ are defined locally and we have just seen that if the fibres over two intersecting open sets on the base space have to be identified in a non-trivial way, the two gauge potentials defined on the overlap are necessarily different. One local gauge potential has no global information, only the collection of all locally defined gauge potentials knows about the global topology. This means that gauge freedom is sometimes not just a matter of choice, but more of necessity!

Of course also in this language gauge freedom is a reflection of choice. Say that on an open set $U$ , two sections are related by $s ^ { \prime } = s g$ . We can choose either section to define a local gauge potential and almost the same reasoning as above shows that both are related as follows

$$
A ^ { \prime } = g ^ { - 1 } A g + g ^ { - 1 } d g .
$$

We see that in the bundle language, gauge freedom is equivalent to the freedom to choose local coordinates on a principal bundle!

# 5.3 Curvature

A very important notion is of course the curvature of a connection. To introduce this, we first define the concept of a covariant derivative on a principal bundle.

Definition 23. Consider a Lie algebra valued $p$ -form, $\alpha \in \Omega ^ { p } P \otimes { \mathfrak { g } }$ that can be decomposed as $\alpha = \alpha ^ { a } \otimes T _ { a }$ , where $\alpha ^ { a }$ is an ordinary $p$ -form and $T _ { a }$ is a basis of $\mathfrak { g }$ . Let $X _ { 1 } , . . . , X _ { p + 1 } \in T _ { p } P$ be $p + 1$ tangent vectors on $P$ . The exterior covariant derivative of $\alpha$ is defined by

$$
D \alpha ( X _ { 1 } , . . . , X _ { p + 1 } ) = d _ { P } \alpha ( X _ { 1 } ^ { H } , . . . , X _ { p + 1 } ^ { H } ) ,
$$

where $X _ { i } ^ { H } \in H _ { p } P$ is the horizontal component of $X _ { i } \in T _ { p } P$ and $d _ { P } \alpha = \left( d _ { P } \alpha ^ { a } \right) \otimes T _ { a }$ .

The curvature is now readily defined.

Definition 24. The curvature 2-form $\Omega$ of a connection $\omega$ on $P$ is defined as

$$
\Omega = D \omega \in \Omega ^ { 2 } P \otimes \mathfrak { g }
$$

At every point $p \in { \cal P }$ , the horizontal vectors define a subspace of $T _ { p } P$ . The assignment of such a subspace at every point of $P$ is called a distribution. Since in this case the distribution is defined by the equation $\omega = 0$ , the Frobenius condition for integrability of the submanifold of $P$ tangent to this distribution is exactly the vanishing of $d \omega$ along the distribution, that is, the vanishing of the curvature. As such, the curvature is an obstruction to finding a submanifold of $P$ that is ‘completely horizontal’. A connection for which $\Omega = 0$ is called a flat connection. When a flat connection exists on a principal bundle, it is thus possible to find a ‘horizontal’ submanifold of $P$ .

Let $\alpha \in \Omega ^ { p } \otimes { \mathfrak { g } }$ and $\beta \in \Omega ^ { q } \otimes \mathfrak { g }$ be two Lie algebra valued forms. The Lie bracket (commutator) between the two is defined as

$$
[ \alpha , \beta ] \equiv \alpha \wedge \beta - ( - ) ^ { p q } \beta \wedge \alpha = [ T _ { a } , T _ { b } ] \alpha ^ { a } \wedge \beta ^ { b } .
$$

Note that for odd $p$ this means that

$$
[ \alpha , \alpha ] = 2 \alpha \wedge \alpha \neq 0 ,
$$

while for even $p$ , $[ \alpha , \alpha ] = 0$ . We state without proof the following important theorem:

Theorem 6. $\Omega$ and $\omega$ satisfy the Cartan structure equations ( $X$ $, Y \in T _ { p } P$ )

$$
\Omega ( X , Y ) = d _ { P } \omega ( X , Y ) + [ \omega ( X ) , \omega ( Y ) ] ,
$$

or

$$
\Omega = d _ { P } \omega + \omega \wedge \omega = d _ { P } \omega + \frac { 1 } { 2 } [ \omega , \omega ] .
$$

We will now again use a section to pull back this globally defined object on $P$ to a local object defined on a patch on $M$ .

Definition 25. Given a section $s$ on $U$ , the local (Yang-Mills) field strength is defined by

$$
F = s ^ { * } \Omega \in \Omega ^ { 2 } U \otimes { \mathfrak { g } } .
$$

The relation with the gauge potential is now easily obtained

$$
\begin{array} { r c l } { { F } } & { { = } } & { { { s } ^ { * } d _ { P } \omega + { s } ^ { * } ( \omega \wedge \omega ) = d ( s ^ { * } \omega ) + s ^ { * } \omega \wedge s ^ { * } \omega } } \\ { { } } & { { = } } & { { d A + A \wedge A . } } \end{array}
$$

Writing $A = A _ { a } d x ^ { a }$ and $F = { \textstyle { \frac { 1 } { 2 } } } F _ { a b } d x ^ { a } \wedge d x ^ { b }$ , we find the usual expression,

$$
F _ { a b } = \partial _ { a } A _ { b } - \partial _ { b } A _ { a } + [ A _ { a } , A _ { b } ] .
$$

The effect of a coordinate change on the field strength 2-form can be deduced (as usual) from the transformation properties of the gauge potential 1-form (5.2.10). More specifically, if two sections are related by $s ^ { \prime } = s g$ , the corresponding field strengths are related by

$$
{ \cal F } ^ { \prime } = g ^ { - 1 } { \cal F } g .
$$

To find the Bianchi identities, we use a section $s$ to pull back the relation

$$
d _ { P } \Omega = d _ { P } \omega \wedge \omega - \omega \wedge d _ { P } \omega .
$$

This results in

$$
\begin{array} { l c l } { { d F } } & { { = } } & { { d s ^ { * } \Omega = s ^ { * } d _ { P } \Omega = s ^ { * } ( d _ { P } \omega \wedge \omega - \omega \wedge d _ { P } \omega ) } } \\ { { } } & { { = } } & { { d s ^ { * } \omega \wedge s ^ { * } \omega - s ^ { * } \omega \wedge d s ^ { * } \omega = d A \wedge A - A \wedge d A } } \\ { { } } & { { = } } & { { F \wedge A - A \wedge F = - [ A , F ] . } } \end{array}
$$

So we find the local identity

$$
{ \mathcal { D } } F = d F + [ A , F ] = 0 ,
$$

where we defined the covariant derivative ${ \mathcal { D } } = d + [ A , \ ]$ .

Given a local connection one-form $A$ for $P$ on some open set $U$ , and a rank $n$ vector bundle $E$ associated to $P$ through some representation $\rho$ , a covariant derivative $\nabla : \mathbf { \tau }$ $\Gamma ( U , E ) \to \Gamma ( U , E ) \otimes \Omega ( U )$ is defined as follows. Given a section $s$ of $P$ , consider a section $\sigma _ { i } = [ ( s , e _ { i } ) ]$ , where $e _ { i }$ , $i \in \{ 1 , \ldots , n \}$ is a basis for the fibre $V$ of $E$ . Then

$$
\nabla \sigma _ { i } = \rho ( A ) ^ { j } { } _ { i } \sigma _ { j } ,
$$

where $\rho ( A ) = A _ { a } \rho ( T ^ { a } )$ is related to the local connection one-form $A = A _ { a } T ^ { a }$ on $P$ through $\rho$ . From this one then goes on to define the covariant derivative acting on a generic section $\sigma$ . The directional derivative with respect to some $X \in \Gamma ( U , T M )$ is defined by $\nabla _ { X } \sigma = \nabla \sigma ( X )$ and can be shown to satisfy the usual linearity and Leibnitz conditions. We will not be bothered with these issues here. The main point we want to make is that a connection on $P$ completely determines a connection on $E$ through $\rho$ .

# 5.4 Characteristic classes I: Chern-Weil theory

The link between connections (and their curvature) and topology is provided by the Chern-Weil theory of characteristic classes. In this approach, characteristic classes are constructed as invariant polynomials of the curvature two-form. First we thus need to define what we mean by invariant polynomial.

Definition 26. Let $\mathfrak { g }$ be the Lie algebra of some Lie group $G$ . A totally symmetric and $n$ -linear polynomial

$$
P ( X _ { 1 } , . . . , X _ { i } , . . . , X _ { j } , . . . , X _ { n } ) = P ( X _ { 1 } , . . . , X _ { j } , . . . , X _ { i } , . . . , X _ { n } ) , \quad \forall i , j ,
$$

where $X _ { i }$ , $i \in \{ 1 , . . . , n \}$ are elements of $\mathfrak { g }$ , is called a symmetric invariant polynomial if

$$
P ( g ^ { - 1 } X _ { 1 } g , . . . , g ^ { - 1 } X _ { n } g ) = P ( X _ { 1 } , . . . , X _ { n } ) , \quad g \in G .
$$

An immediate consequence of this definition is that (take $g$ close to the identity, $g =$ $1 + t Y$ , and expand (5.4.2) to first order in $t$ ),

$$
\sum _ { i = 1 } ^ { n } P ( X _ { 1 } , . . . , X _ { i - 1 } , [ Y , X _ { i } ] , X _ { i + 1 } , . . . , X _ { n } ) = 0 , \quad \forall Y \in { \mathfrak { g } } .
$$

Definition 27. An invariant polynomial of degree $n$ is defined as a symmetric invariant polynomial with all its entries equal,

$$
P _ { n } ( X ) \equiv P ( \underbrace { X , . . . , X } _ { n } ) \equiv P ( X ^ { n } )
$$

Now we want to extend this definition to $^ { 9 }$ -valued differential forms on a manifold. Consider a $\mathfrak { g }$ -valued $p$ -form $\alpha _ { i }$ which can be written as (no sum over $i$ ) $\alpha _ { i } = \eta _ { i } X _ { i }$ , where $\eta _ { i }$ is an ordinary $p$ -form and $X _ { i }$ again an element of $\mathfrak { g }$ . The general case follows by linearity. We then extend the previous definition as follows:

Definition 28. An invariant polynomial for $\mathfrak { g }$ -valued forms is defined as

$$
P ( \alpha _ { 1 } , . . . , \alpha _ { n } ) = P ( X _ { 1 } , . . . , X _ { n } ) \eta _ { 1 } \land . . . \land \eta _ { n } ,
$$

where the first factor on the right hand side is a symmetric invariant polynomial as defined above. The diagonal combination is again called an invariant polynomial of degree $n$ ,

$$
P _ { n } ( \alpha ) = P ( \alpha ^ { n } ) = P ( X ^ { n } ) \eta \wedge \ldots \wedge \eta .
$$

From (5.4.3) we find that

$$
d P ( \alpha _ { 1 } , . . . , \alpha _ { n } ) = \sum _ { i = 1 } ^ { n } ( - ) ^ { p _ { 1 } + . . . + p _ { i - 1 } } P ( \alpha _ { 1 } , . . . , \alpha _ { i - 1 } , \mathcal { D } \alpha _ { i } , \alpha _ { i + 1 } , . . . , \alpha _ { n } ) .
$$

where as before ${ \mathcal { D } } = d + [ A , \quad ]$ , where $A$ is any $\mathfrak { g }$ -valued one form. Of course we are interested in the case where $A$ is a local gauge potential associated to a connection on a principal bundle $P ( M , G )$ .

The objects of interest are invariant polynomials in the field strength two-form $F$ , $P _ { n } ( F )$ , because these turn out to have very interesting properties. Indeed, the following important theorem is due to Chern and Weil.

Theorem 7. Let $P _ { n } ( F )$ be an invariant polynomial, then (i) $P _ { n } ( F )$ is closed, $d P _ { n } ( F ) = 0$ . (ii) Let $F$ and $F ^ { \prime }$ be local curvature 2-forms corresponding to two different connections on the same bundle. Then the difference $P _ { n } ( F ) - P _ { n } ( F ^ { \prime } )$ is exact.

Note that, since $P _ { n } ( F )$ is closed, it can always locally be written as the $d$ of something (Poincar´e’s lemma). The important point about this theorem is that the difference $P _ { n } ( F ) -$ $P _ { n } ( F ^ { \prime } ) = d Q$ is exact in a global sense (which is of course the meaning of exact), meaning that $Q$ is globally defined.

The first part of the theorem follows immediately from (5.4.7), because of the Bianchi identity $\mathcal { D } \boldsymbol { F } = 0$ , see (5.3.12).

The second part is a bit harder to prove and we will only mention the conclusion. To this end, consider two 1-form gauge potentials $A$ and $A ^ { \prime }$ , both referring to the same system of local trivializations, and their respective 2-form field strengths $F$ and $F ^ { \prime }$ . We define the homotopic connection

$$
A _ { t } = A + t \theta , \quad \theta = A ^ { \prime } - A ,
$$

so that $A _ { 0 } = A$ and $A _ { 1 } = A ^ { \prime }$ , and its field strength

$$
F _ { t } = d A _ { t } + A _ { t } \wedge A _ { t } = F + t { \mathcal { D } } \theta + t ^ { 2 } \theta \wedge \theta ,
$$

where ${ \mathcal { D } } = d + \lfloor A , \ \rfloor$ . In terms of these, one finds

$$
P _ { n } ( F ^ { \prime } ) - P _ { n } ( F ) = d Q _ { 2 n - 1 } ( A ^ { \prime } , A ) ,
$$

where the transgression $Q _ { 2 n - 1 } ( A ^ { \prime } , A )$ is defined as

$$
Q _ { 2 n - 1 } ( A ^ { \prime } , A ) = n \int _ { 0 } ^ { 1 } d t P ( A ^ { \prime } - A , F _ { t } ^ { n - 1 } ) .
$$

Note that $Q _ { 2 n - 1 } ( A ^ { \prime } , A )$ is indeed a gauge invariant and hence globally defined object, since under a gauge transformation (the inhomogeneous term cancels) $\theta ^ { \prime } = g ^ { - 1 } \theta g$ and $P$ is invariant.

Equation (5.4.10) is called a transgression formula and is quite important in the study of anomalies. On the other hand it is closely related to the Chern-Simons form. Indeed, on a local patch one can always choose $A ^ { \prime } = 0$ . If the bundle is trivial, we saw that this can be done globally. We know that since $P _ { n } ( F )$ is closed, it is locally exact, i.e. it can locally be written as the $d$ of a Chern-Simons form. The transgression formula provides a means for calculating this Chern-Simons form. Indeed, from (5.4.10) we find

$$
P _ { n } ( F ) = d Q _ { 2 n - 1 } ( A ) ,
$$

where we defined the Chern-Simons form

$$
Q _ { 2 n - 1 } ( A ) \equiv Q _ { 2 n - 1 } ( A , 0 ) = n \int _ { 0 } ^ { 1 } d t P ( A , F _ { t } ^ { n - 1 } ) ,
$$

where now,

$$
A _ { t } = t A , \quad F _ { t } = t F + ( t ^ { 2 } - t ) A \wedge A
$$

So given an invariant polynomial $P _ { n } ( F )$ , we can always construct the associated Chern-Simons form $Q _ { 2 n - 1 } ( A )$ from (5.4.13). Obviously, $P _ { n } ( F )$ is a $2 n$ -form, while $Q _ { 2 n - 1 }$ is a $( 2 n - 1 )$ -form.

Note that, since an associated vector bundle has the same connection one-forms (modulo representations), exactly the same holds for vector bundles. In the following all statements are thus for a principal or vector bundle $E$ . Since an invariant polynomial in $F$ , $P ( F )$ , is closed, it represents a de Rham cohomology class $\chi _ { P } ( E ) = [ P ( F ) ] \in H ^ { 2 n } ( M , \mathbb { R } )$ , which is called a characteristic class. Since we have shown that the difference of two invariant polynomials defined with respect to two different connections is exact, the characteristic class does not depend on the specific connection chosen and is truly a characteristic of the bundle $E$ . More formally, denoting the ring of invariant polynomials by $I ( G )$ , one defines the map $\chi : I ( G ) \to H ^ { 2 \bullet } ( M , \mathbb { R } )$ by $\chi ( P ) = [ P ( F ) ]$ , where $F ^ { \dagger }$ corresponds to any connection on $E$ . This is a ring homomorphism called the Chern-Weil homomorphism. The above discussion shows that this is well-defined. In particular, it does not depend on the choise of $F$ . The most important characteristic class is the Chern class, to which we turn now.

# 5.5 The Chern class, monopoles and instantons

Let $E$ be a principal or complex vector bundle with structure group $G = G L ( k , \mathbb { C } )$ or a subgroup thereof ( $U ( k )$ , SU(k),...). The total Chern class is defined by

$$
c ( { \boldsymbol { F } } ) = \operatorname* { d e t } \left( 1 + { \frac { i } { 2 \pi } } { \boldsymbol { F } } \right) ,
$$

where “1” stands for the unit matrix of the appropriate dimension corresponding to the representation used. The determinant is computed by considering $F$ as a matrix of 2-forms. Since $F$ is a 2-form, $c ( F )$ is a sum of forms of even degrees,

$$
c ( F ) = 1 + c _ { 1 } ( F ) + c _ { 2 } ( F ) + \ldots
$$

where $c _ { n } ( F ) \in \Omega ^ { 2 n } M$ and its cohomology class is called the $n$ -th Chern class.4 If $\mathrm { d i m } M =$ $m$ , all Chern classes $c _ { n } ( F )$ of degree $2 n > m$ obviously vanish. More importantly, all $c _ { n } ( F )$ for $n > k$ vanish. In general it can be quite cumbersome to compute this determinant for higher rank bundles. Therefore we will diagonalize the matrix ${ \frac { i } { 2 \pi } } F$ (if for instance $G = S U ( k )$ , $F$ is anti-hermitian, so $i F$ can be diagonalized by an $S U ( k )$ rotation ) to a $_ { g }$ matrix $\widetilde { F }$ , with 2-forms $x _ { i }$ on the diagonal. This leads to

$$
\begin{array} { r c l } { \operatorname* { d e t } ( 1 + \widetilde { F } ) } & { = } & { \operatorname* { d e t } [ \operatorname { d i a g } ( 1 + x _ { 1 } , . . . , 1 + x _ { k } ) ] = \displaystyle \prod _ { i = 1 } ^ { k } ( 1 + x _ { i } ) } \\ & { = } & { 1 + ( x _ { 1 } + . . . + x _ { k } ) + ( x _ { 1 } x _ { 2 } + . . . + x _ { k - 1 } x _ { k } ) + . . . + ( x _ { 1 } x _ { 2 } . . . x _ { k } ) } \\ & { = } & { 1 + \mathrm { T r } \widetilde { F } + \displaystyle \frac { 1 } { 2 } \left[ ( \mathrm { T r } \widetilde { F } ) ^ { 2 } - \mathrm { T r } \widetilde { F } ^ { 2 } \right] + . . . + \operatorname* { d e t } \widetilde { F } . } \end{array}
$$

Note that in the second line we encounter the elementary symmetric functions of $\{ x _ { i } \}$ and that all manipulations are well defined since the $x _ { i }$ are 2-forms and thus commute (the wedge product is always understood). For an invariant polynomial $P _ { n } ( F ) = P _ { n } ( g ^ { - 1 } F g ) =$ $P _ { n } ( 2 \pi \tilde { F } / i )$ , so we find the following expressions for the Chern classes:

$$
{ \begin{array} { l l l } { c _ { 1 } ( F ) } & { = } & { \operatorname { T r } { \widetilde { F } } = { \frac { i } { 2 \pi } } \operatorname { T r } F } \\ { c _ { 2 } ( F ) } & { = } & { { \frac { 1 } { 2 } } \left[ ( \operatorname { T r } { \widetilde { F } } ) ^ { 2 } - \operatorname { T r } { \widetilde { F } } ^ { 2 } \right] = { \frac { 1 } { 8 \pi ^ { 2 } } } \left[ \operatorname { T r } ( F \wedge F ) - \operatorname { T r } F \wedge \operatorname { T r } F \right] } \\ & { \vdots } \\ { c _ { k } ( F ) } & { = } & { \operatorname* { d e t } { \widetilde { F } } = \left( { \frac { i } { 2 \pi } } \right) ^ { k } \operatorname* { d e t } F } \end{array} }
$$

A submanifold of $M$ without boundary is called a cycle.5 The integrals of $c _ { n } ( F )$ over a basis of $2 n$ -dimensional cycles in $M$ are called periods of $c _ { n } ( F )$ , or Chern numbers, and, given this basis of cycles, these periods fully specify the cohomology class. Because of Stoke’s theorem, the periods are well-defined, i.e. independent of the representative of the class. In other words, they are topological numbers, which, as we discussed above, do not depend on the connection chosen, and are thus intrinsic characteristics of the bundle. The Chern numbers of a compact manifold can be shown to be integral numbers. This implies that Chern classes are examples of generators of the integral cohomology ring $H ^ { \bullet } ( M , \mathbb { Z } )$ . Unfortunately we have no time to go into the very rich subject of integral cohomology, which can be seen as a refinement of de Rham cohomology. An orientable $n$ -dimensional manifold $M$ is itself a cycle and fully generates the $n$ -th homology group of $M$ . The period of the top Chern class $c _ { n } ( F )$ on a $2 n$ -dimensional manifold occurs in some basic examples of gauge theory constructions. Let us illustrate this with two examples.

Example 18. Let us start with the easiest one. Consider a $U ( 1 )$ -gauge theory on $\mathbb { R } ^ { 3 }$ with a Dirac monopole placed at the origin. Since the gauge field becomes singular at the origin, we had better consider the gauge theory on $\mathbb { R } ^ { 3 } - \{ 0 , 0 , 0 \}$ , which is homotopy equivalent to $S ^ { 2 }$ . We are thus led to consider a $U ( 1 )$ -bundle over $S ^ { 2 }$ . The only Chern class which can be defined is $c _ { 1 } ( F )$ and obviously, since locally $F = d A$ , we find

$$
c _ { 1 } ( F ) = d \left( \frac { i } { 2 \pi } A \right) , \mathrm { s o ~ t h a t } Q _ { 1 } ( A ) = \frac { i } { 2 \pi } A ,
$$

which is indeed the same expression as would be obtained from formula (5.4.13). To compute the period of $c _ { 1 } ( F )$ over $S ^ { 2 }$ , cover $S ^ { 2 }$ by two hemispheres $D _ { + }$ and $D _ { - }$ so that $D _ { + } \cap D _ { - } \sim S ^ { 1 }$ . On the equator $S ^ { 1 }$ the two gauge potentials are related by $A _ { - } = A _ { + } + g ^ { - 1 } d g$ for $g \in U ( 1 )$ . We then find

$$
\int _ { S ^ { 2 } } c _ { 1 } ( F ) = { \frac { i } { 2 \pi } } \left( \int _ { D _ { + } } F + \int _ { D _ { - } } F \right) = { \frac { i } { 2 \pi } } \int _ { S ^ { 1 } } \left( A _ { + } - A _ { - } \right) = { \frac { 1 } { 2 \pi i } } \int _ { S ^ { 1 } } g ^ { - 1 } d g .
$$

This last expression computes the winding number of the map $g : S ^ { 1 } \to U ( 1 )$ . Take for instance $g _ { q } : t \mapsto e ^ { i q t }$ , $q \in \mathbb { Z }$ , (where $S ^ { 1 }$ is seen as the interval $[ 0 , 2 \pi ]$ with endpoints identified and $U ( 1 ) \cong S ^ { 1 }$ is the unit circle in the complex plane) to convince yourself that this expression yields the integer $q$ . We will in the next section argue that for classification purposes all maps from $S ^ { 1 }$ to $S ^ { 1 }$ can be taken to be of this form. This illustrates the integrality of Chern numbers. In this physical context, $q$ is called the monopole charge. Note that since seeing a monopole as a fibre bundle over $S ^ { 2 }$ automatically leads to a quantized monopole charge, we are automatically in the quantum realm. A generic twoform describes a classical configuration, while an integral two-form (or equivalently a Chern class of a fibre bundle) describes a quantum system.

Example 19. Moving on to a more complicated example, consider an $S U ( 2 )$ -bundle on a 4-dimensional manifold. Since for $S U ( k )$ we have that $ { \mathrm { T r } } F = 0$ , the first Chern class vanishes. To compute the Chern-Simons form related to the second Chern class, we use (5.4.13),

$$
\begin{array} { l l l } { { Q _ { 3 } ( A ) } } & { { = } } & { { 2 \displaystyle \int _ { 0 } ^ { 1 } d t { \cal P } ( A , F _ { t } ) = \displaystyle \frac { 1 } { 4 \pi ^ { 2 } } \int _ { 0 } ^ { 1 } d t \mathrm { T r } ( A \wedge F _ { t } ) } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { 8 \pi ^ { 2 } } \mathrm { T r } \left( A \wedge d A + \frac { 2 } { 3 } A \wedge A \wedge A \right) . } } \end{array}
$$

This is of course the most famous example of a Chern-Simons form in physics. Consider now an $S U ( 2 )$ instanton on $S ^ { 4 }$ .6 This is a self- or anti-selfdual (SD or ASD) solution, $F = \pm { \star } F$ , of the Euclidian Yang-Mills action

$$
S _ { E } = - \int \mathrm { T r } ( F \wedge \star F ) .
$$

Because of the relation

$$
- \int \operatorname { T r } ( F \wedge \star F ) = - \frac { 1 } { 2 } \int \operatorname { T r } \left[ ( F \pm \star F ) \wedge \star ( F \pm \star F ) \right] \pm \int \operatorname { T r } ( F \wedge F ) ,
$$

and the fact that the first term on the right hand side is positive definite, we have that $S _ { E } \geq 8 \pi ^ { 2 } | k |$ , where $k$ is the instanton number

$$
k = - \int _ { S ^ { 4 } } c _ { 2 } ( F ) .
$$

Instanton configurations clearly saturate this bound and are thus indeed saddle points of the Euclidean action. The minus sign makes that a SD instanton has positive instanton number, while an ASD instanton has negative $k$ . This is in fact again an integer winding number. To see this, cover $S ^ { 4 }$ by two hemispheres $D _ { + }$ and $D _ { - }$ such that $D _ { + } \cap D _ { - } \sim S ^ { 3 }$ . On the ‘equator’ $S ^ { 3 }$ we find that $A _ { + }$ and $A _ { - }$ are related by an equation like (5.2.10) with $g : S ^ { 3 }  S U ( 2 )$ and since $S U ( 2 ) \cong S ^ { 3 }$ this map is again characterized by a winding number. Computing the Chern number, we find that this is indeed exactly the winding number of the map $g$ ,

$$
\begin{array} { r c l } { { \displaystyle \int _ { S ^ { 4 } } c _ { 2 } ( F ) } } & { { = } } & { { \displaystyle \int _ { D _ { + } } d Q _ { 3 } ( A _ { + } ) + \int _ { D _ { - } } d Q _ { 3 } ( A _ { - } ) = \int _ { S ^ { 3 } } \left( Q _ { 3 } ( A _ { + } ) - Q _ { 3 } ( A _ { - } ) \right) } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { 2 4 \pi ^ { 2 } } \int _ { S ^ { 3 } } \mathrm { T r } \left( g ^ { - 1 } d g \wedge g ^ { - 1 } d g \wedge g ^ { - 1 } d g \right) . } } \end{array}
$$

That this is indeed a winding number follows from the fact that it is of the form $\int g ^ { * } \Omega$ where $\Omega$ is the Haar volume form on the group manifold $S U ( 2 )$ . Thus here again the integrality of a Chern number follows from its identification with a winding number. Summarizing, a charge $k$ instanton is a nontrivial connection on an $S U ( 2 )$ -bundle on $S ^ { 4 }$ with second Chern number (or, by slight abuse of nomenclature, class) $k$ .

# Chapter 6

# Classification of fibre bundles

The above treatment of characteristic classes and classification issues involving fibre bundles followed from considering connections on fibre bundles. This approach is part of what is called differential topology. Now we will venture into a slightly more abstract take on these issues, which leads us into the world of algebraic topology. For this it will prove useful to know a bit more about homotopy groups. A references for algebraic topology is [13]. Much of the discussion of homotopy theory is inspired by the presentation in the very useful book [14]. A more advanced treatment of algebraic topology can be found in [15]. For more about the homotopy classification of fibre bundles see [10], [16], [17] or the standard references for K-theory mentioned at the beginning of the next section. These references all discuss characteristic classes as well. Also, a classic on characteristic classes is [18].

# 6.1 Homotopy groups

We already introduced homotopy classes of maps between two spaces $X$ and $Y$ . We will denote the set of all such homotopy classes by $[ X , Y ]$ . If $Y \sim Y ^ { \prime }$ are of the same homotopy type, it is not hard to see that

$$
[ X , Y ] \cong [ X , Y ^ { \prime } ] .
$$

This implies that $[ X , Y ]$ is a homotopy invariant (and thus also a topological invariant) of $Y$ when we keep $X$ fixed. One very important example is the set

$$
\pi _ { 1 } ( X ) = [ S ^ { 1 } , X ] .
$$

Actually frequently it is useful to only consider maps which map a chosen base point in $X$ to a base point in $Y$ . Denoting the base point by $^ *$ , this means considering maps $( X , * ) \to ( Y , * )$ . A space $X$ together with its base point $^ *$ is called a pointed space. The corresponding homotopy classes of base point preserving maps are denoted by $[ X , Y ] _ { * }$ and again important is

$$
\pi _ { 1 } ( X , * ) = [ S ^ { 1 } , X ] _ { * } .
$$

This is a quotient of $\mathrm { H o m } ( S ^ { 1 } , X ) _ { * } = \Omega X$ , the space of based loops on $X$ , or the loop space of $X$ for short.

It is often useful to represent $\pi _ { 1 } ( X , * )$ in a slightly different way. Namely as homotopy classes of maps from $I = [ 0 , 1 ]$ to $X$ where the boundary $\partial I = \{ 0 , 1 \}$ is mapped to the base point $^ *$ of $X$ . It is now easy to see a group structure emerging as follows. Given two maps $f , g \in \Omega X$ representing two classes $[ f ]$ and $[ g ]$ , the product is defined as $[ f ] [ g ] = [ f \cdot g ]$ , where $f \cdot g$ is the loop defined as follows

$$
( f \cdot g ) ( t ) = { \left\{ \begin{array} { l l } { f ( 2 t ) } & { { \mathrm { f o r ~ } } t \in [ 0 , { \frac { 1 } { 2 } } ] } \\ { g ( 2 t - 1 ) } & { { \mathrm { f o r ~ } } t \in [ { \frac { 1 } { 2 } } , 1 ] } \end{array} \right. }
$$

It is straightforward to check that the product of classes defined in this way is associative. The identity is the class of the constant map which sends the whole of $S ^ { 1 }$ to the base point of $X$ . The inverse of a class $[ f ]$ is $[ f ]$ where $f ( t ) = f ( 1 - t )$ . This turns $\pi _ { 1 } ( X , * )$ into a group called the fundamental group of $( X , * )$ .

The higher homotopy groups are defined similarly as

$$
\pi _ { n } ( X , * ) = [ S ^ { n } , X ] _ { * } .
$$

As was the case for the fundamental group it is sometimes more useful to represent the higher homotopy groups by looking at homotopy classes of maps from $I ^ { \pi }$ to $X$ where again $\partial I ^ { n }$ is sent to the base point $^ *$ . Here $\partial I ^ { n }$ is the collection of faces of the hypercube $I ^ { n }$ . A group structure arises analogously to the case $n = 1$ . For $n > 1$ it turns out however that the resulting group is always commutative (while the fundamental group need not be). For $n = 0$ we take $S ^ { 0 }$ to be simply a point and we drop the base point requirement. $\pi _ { 0 } ( X )$ is thus the set of all homotopy classes of points on $X$ , i.e this counts all path components of $X$ . Generically, $\pi _ { 0 } ( X )$ is not a group, although it can be. For instance for a Lie group $G$ , the identity component $H$ is a normal subgroup of $G$ . This implies that $\pi _ { 0 } ( G ) = G / H$ is also a group.

Every map $\phi : ( X , * ) \ : \longrightarrow \ : ( Y , * )$ of pointed spaces induces a homomorphism $\phi _ { * }$ of homotopy groups. Indeed, given an $[ f ] \in [ S ^ { n } , X ] _ { * }$ , clearly $[ \phi \circ f ] \in [ S ^ { n } , Y ] _ { * }$ . We define $\phi _ { * } [ f ] = [ \phi \circ f ]$ , thus yielding a map

$$
\phi _ { * } : \pi _ { n } ( X , * ) \to \pi _ { n } ( Y , * ) .
$$

If $F$ is a homotopy between $f$ and $f ^ { \prime }$ then $\phi \circ F$ is a homotopy between $\phi \circ f$ and $\phi \circ f ^ { \prime }$ so that this map is well defined. Important properties of the induced map $\phi _ { * }$ are that $1 _ { * } ~ = ~ 1$ and $( \phi \psi ) _ { * } = \phi _ { * } \psi _ { * }$ . Lo and behold, homotopy is a covariant functor from the category of pointed spaces and base point preserving maps to $\mathcal { G }$ the category of groups and homomorphisms. As was explained in subsection 3.5, this immediately implies that homeomorphic spaces have isomorphic homotopy groups, making the latter topological invariants. As we mentioned before, homotopy groups are actually invariants of homotopy type. Said differently, it almost sounds tautological: homotopy is a homotopy invariant functor.

Later on we will need the notion of suspension. Given a pointed space $( X , * )$ , its suspension is defined by

$$
S X = ( I \times X ) / ( \partial I \times X ) .
$$

In other words, we ‘smear’ $X$ over an interval and pinch the ends down to points. The downside is that this suspended space has no natural base point – the original one has been smeared over the entire interval. To amend this, we introduce the reduced suspension

$$
\Sigma X = S X / ( I \times * ) .
$$

Note that $S X \sim \Sigma X$ are of the same homotopy type. By induction, we define the $n$ - th suspension $S ^ { n } X$ and reduced suspension $\Sigma ^ { n } X$ . An innocent looking but important example is, $S ^ { n } S ^ { m } \sim S ^ { n + m } \sim \Sigma ^ { n } S ^ { m }$ . As a tantalizing aside, it turns out that the (reduced) suspension functor $\Sigma$ and loop space functor $\Omega$ are ‘adjoint’ 1

$$
[ \Sigma X , Y ] _ { * } = [ X , \Omega Y ] _ { * } .
$$

Taking $X$ to be $S ^ { n - 1 }$ we find

$$
\pi _ { n } ( X , * ) = \pi _ { n - 1 } ( \Omega X , * ) .
$$

For a path connected space one can easily show that homotopy groups at different base points are isomorphic. It thus makes sense to simply speak of the homotopy groups of a space without reference to the base point. With this in mind, we will drop the reference to the base point in subsequent discussions. Keep in mind however that we are not talking about the base point-free homotopy spaces we mentioned at the beginning of this section. They are still different, although of course related, objects. Since we will blur the dependence on the base point later on, we will simply denote the (reduced) suspension by $S$ .

# 6.2 The homotopy exact sequence of a fibre bundle

In general, homotopy groups are – easy as they are to define – very hard to compute. There is a vast field of research concerned essentially with trying to compute the higher homotopy groups of the spheres. Indeed, contrary to (co)homology groups which are zero in dimensions higher than the dimension of the space under investigation, the sequence of homotopy groups for a given space can go on and on.

One interesting and easy to prove fact about homotopy groups is

$$
\pi _ { n } ( X \times Y ) = \pi _ { n } ( X ) \oplus \pi _ { n } ( Y ) , \quad n > 0 .
$$

This gives a nice way of computing homotopy groups of product spaces. This is one of the few ways in which homotopy turns out to be a bit simpler than (co)homology. For fibre bundles2 there exists an important tool which in a sense generalizes this (and which does not exist for (co)homology) called the homotopy exact sequence (HES) for a fibre bundle $F \longrightarrow E \longrightarrow B$

$$
\begin{array} { r } { \dots { \longrightarrow } { \pi } _ { n } ( F ) \overset { i _ { * } } { \longrightarrow } { \pi } _ { n } ( E ) \overset { { \pi } _ { * } } { \longrightarrow } { \pi } _ { n } ( B ) \overset { \partial _ { * } } { \longrightarrow } { \pi } _ { n - 1 } ( F ) \overset { i _ { * } } { \longrightarrow } { \pi } _ { n - 1 } ( E ) \longrightarrow \dots } \end{array}
$$

This sequence possibly continuous for ever on the left and ends as follows on the right

$$
\dots { \longrightarrow } \pi _ { 1 } ( B ) \longrightarrow \pi _ { 0 } ( F ) \longrightarrow \pi _ { 0 } ( E ) \longrightarrow \pi _ { 0 } ( B ) \longrightarrow 0 \nonumber
$$

The maps involving $\pi _ { 0 }$ are not homomorphisms but simply set maps. An important application of this exact sequence is the classification of covering spaces.

Definition 29. A covering space is a fibre bundle with discrete fibre $\Gamma$ .

Consider a covering space $\Gamma  \tilde { X }  X$ . Usually, this is written as ${ \tilde { X } } / { \Gamma } = X$ . Obviously, $\pi _ { 0 } ( \Gamma ) = \Gamma$ and $\pi _ { n } ( \Gamma ) = 0$ for $n > 0$ . The above HES for $n > 1$ then implies that $\pi _ { n } ( { \tilde { X } } ) \cong \pi _ { n } ( X )$ for $n > 1$ . Assuming that the covering $\tilde { X }$ is path connected, the HES also implies

$$
0 \longrightarrow \pi _ { 1 } ( { \tilde { X } } ) \longrightarrow \pi _ { 1 } ( X ) \longrightarrow \Gamma \longrightarrow 0
$$

This is a short exact sequence and, as reviewed in subsection 3.3, implies that

$$
\pi _ { 1 } ( X ) / \pi _ { 1 } ( { \tilde { X } } ) \cong \Gamma .
$$

A universal cover is a covering space for which $\tilde { X }$ is simply connected, i.e $\tilde { X }$ is connected and $\pi _ { 1 } ( { \tilde { X } } ) = 0$ . For a universal cover ${ \tilde { X } } / { \Gamma } = X$ , we find that $\pi _ { 1 } ( X ) = \Gamma$ . This provides a nice way of computing fundamental groups.

Example 20. The real line $\mathbb { R }$ is the universal cover of $S ^ { 1 }$ , namely $\mathbb { R } / \mathbb { Z } = S ^ { 1 }$ . This implies that $\pi _ { n } ( S ^ { 1 } ) = 0$ for $n > 1$ and $\pi _ { 1 } ( S ^ { \mathrm { 1 } } ) = \mathbb { Z }$ . We just computed our first homotopy groups!

One can show that $\pi _ { k } ( S ^ { n } ) = 0$ for $k < n$ and that $\pi _ { n } ( S ^ { n } ) = \mathbb { Z }$ . One way to do this is by comparing to the corresponding (always abelian) homology groups, which are generically much easier to compute. Unfortunately we have no time to treat them in any detail. Let us simply mention two very useful theorems:

Theorem 8. For a path connected space $X$ , $H _ { 1 } ( X , \mathbb { Z } )$ is the abelianization of $\pi _ { 1 } ( X )$ , i.e. $\pi _ { 1 } ( X ) / N = H _ { 1 } ( X , \mathbb { Z } )$ , where $N = [ \pi _ { 1 } ( X ) , \pi _ { 1 } ( X ) ]$ is the commutator subgroup – the subgroup generated by all elements of the form $a b a ^ { - 1 } b ^ { - 1 }$ – of $\pi _ { 1 } ( X )$ . In particular, when both groups are abelian, we get $\pi _ { 1 } ( X ) = H _ { 1 } ( X , \mathbb { Z } )$ .

Theorem 9. (Hurewicz Isomorphism theorem) For a path connected and simply connected space $X$ , the first nontrivial homotopy and homology occur in the same dimension and are equal, i.e. for a positive integer $n$ , if $\pi _ { k } ( X ) = 0$ for all $0 < k < n$ , then also $H _ { k } ( X , \mathbb { Z } ) = 0$ , and $\pi _ { n } ( X ) = H _ { n } ( X , \mathbb { Z } )$ .

The homology groups of spheres are quite easy to compute. For instance, for $n > 1$ all $H _ { 1 } ( S ^ { n } )$ are trivial, so all $S ^ { n }$ are simply connected for $n > 1$ . The only nontrivial group $H _ { n } ( S ^ { n } ) = \mathbb { Z }$ is generated by $S ^ { n }$ itself.

Sometimes one is lucky enough to find a fibre bundle construction that helps significantly.

Example 21. Consider $S ^ { 3 }$ as the ‘circle’ in $\mathbb { C } ^ { 2 }$ , i.e. pairs $( z _ { 1 } , z _ { 2 } )$ of complex numbers satisfying $| z _ { 1 } | ^ { 2 } + | z _ { 2 } | ^ { 2 } = 1$ . Consider the map

$$
\pi : S ^ { 3 }  \mathbb { C } P ^ { 1 } : ( z _ { 1 } , z _ { 2 } ) \mapsto [ ( z _ { 1 } , z _ { 2 } ) ] .
$$

Pairs $( z _ { 1 } , z _ { 2 } )$ and $\lambda ( z _ { 1 } , z _ { 2 } )$ are mapped to the same point, but of course $| \lambda | = 1$ , otherwise both pairs can not simultaneously belong to $S ^ { 3 }$ . In other words, $\pi ^ { - 1 } ( [ ( z _ { 1 } , z _ { 2 } ) ] ) = U ( 1 ) =$ $S ^ { 1 }$ . Remembering that $\mathbb { C } P ^ { 1 } = S ^ { 2 }$ , we thus get the circle bundle $S ^ { 1 } \to S ^ { 3 } \to S ^ { 2 }$ , called the Hopf fibration or bundle. One can show that the Hopf bundle is the principal bundle corresponding to a charge one Dirac monopole.

We now easily deduce from the HES that $\pi _ { k } ( S ^ { 3 } ) = \pi _ { k } ( S ^ { 2 } )$ for all $k > 2$ , and – using the above stated fact $\pi _ { 1 } ( S ^ { 3 } ) = \pi _ { 2 } ( S ^ { 3 } ) = 0$ – that $\pi _ { 2 } ( S ^ { 2 } ) = \pi _ { 1 } ( S ^ { 1 } ) = \mathbb { Z }$ . Using the fact that $\pi _ { 3 } ( S ^ { 3 } ) = \mathbb { Z }$ , the former result also implies that $\pi _ { 3 } ( S ^ { 2 } ) = \mathbb { Z }$ . This is a nontrivial result! It shows that indeed homotopy groups need not be zero for dimensions higher than the space under investigation.

Exercise 11. There is a similar construction using the quaternions $\mathbb { H }$ . A ‘circle’ in $\mathbb { H } ^ { 2 }$ is $S ^ { 7 }$ , $\mathbb { H } P ^ { 1 } = S ^ { 4 }$ and the space of unit quaternions is $S ^ { 3 }$ . This results in the bundle $S ^ { 3 }  S ^ { 7 }  S ^ { 4 }$ . This is the principal bundle corresponding to an $S U ( 2 )$ instanton of unit charge. What does this teach us about the homotopy groups of $S ^ { 3 }$ and $S ^ { 4 }$ ?

Example 22. As we already mentioned, the real projective space $\mathbb { R } P ^ { n }$ for $n > 1$ is the space of straight lines through the origin of $\mathbb { R } ^ { n + 1 }$ . It is often useful to see it as $S ^ { n }$ with opposite points identified. This implies $\mathbb { R } P ^ { n } = S ^ { n } / \mathbb { Z } _ { 2 }$ in the above covering space sense, i.e $S ^ { n }$ is the universal cover of $\mathbb { R } P ^ { n }$ and $\mathbb { Z } _ { 2 } \to S ^ { n } \to \mathbb { R } P ^ { n }$ is a fibre bundle. This implies that $\pi _ { 1 } ( \mathbb { R } P ^ { n } ) = \mathbb { Z } _ { 2 }$ and $\pi _ { k } ( \mathbb { R } P ^ { n } ) = \pi _ { k } ( S ^ { n } )$ for $k > 1$ .

Example 23. Represent an element of $g ~ \in ~ S O ( 3 )$ by a vector in $\mathbb { R } ^ { 3 }$ with orientation specified by the axis of rotation of $g$ and length by the angle of rotation of $g$ . This shows that $S O ( 3 )$ can be seen as a solid ball in $\mathbb { R } ^ { 3 }$ of radius $\pi$ with antipodal points on the bounding sphere identified. A moment’s thought then leads to the conclusion that $S O ( 3 )$ is homeomorphic to $\mathbb { R } P ^ { 3 }$ . This means that $S ^ { 3 } \cong S U ( 2 )$ is the universal cover of $S O ( 3 )$ and $\pi _ { 1 } ( S O ( 3 ) ) = \mathbb { Z } _ { 2 }$ . It turns out that for all $n > 2$ , $\pi _ { 1 } ( S O ( n ) ) = \mathbb { Z } _ { 2 }$ and the universal cover of $S O ( n )$ is a double cover denoted by $S p i n ( n )$ . Thus $S p i n ( 3 ) = S U ( 2 )$ .

Example 24. Consider the $( 2 p + 1 )$ -sphere $S ^ { 2 p + 1 }$ as a ‘complex $p$ -sphere’, namely the manifold defined by the condition $Z ^ { \dagger } Z = 1$ in $\mathbb { C } ^ { p + 1 }$ , where

$$
\begin{array} { r } { Z = \left( \begin{array} { c } { z _ { 1 } } \\ { z _ { 2 } } \\ { \vdots } \\ { z _ { p + 1 } } \end{array} \right) . } \end{array}
$$

This equation is invariant under $Z \mapsto U Z$ , where $U \in U ( p + 1 )$ . This action of $U ( p + 1 )$ on $S ^ { 2 p + 1 }$ is transitive and the stability subgroup of any point is $U ( p )$ . We thus get the principal $U ( p )$ -bundle $U ( p ) \to U ( p + 1 ) \to S ^ { 2 p + 1 }$ . From the HES and the fact that $\pi _ { i } ( S ^ { 2 p + 1 } ) = 0$ for $0 < i < 2 p + 1$ , find that

$$
\pi _ { i } ( U ( p ) ) \cong \pi _ { i } ( U ( p + 1 ) ) , \quad p > \frac { i } { 2 } .
$$

For this reason $p > i / 2$ is called the stable range. The above fact can be expressed quite concisely by introducing the inductive (or direct) limit of the series of inclusions $U ( 1 ) \subset U ( 2 ) \subset \cdots U ( i ) \subset U ( i + 1 ) \subset \cdots$ . This limit is roughly the union $U ( \infty ) = \bigcup U ( i )$ , and can intuitively be thought of as the group $U ( k )$ for $k$ going to infinity. Using this object, we rephrase the above result by saying that in the stable range all homotopy groups of the unitary groups are equal to $\pi _ { i } ( U ( \infty ) )$ for the relevant $_ i$ .

Example 25. Given a poined space $( X , * )$ , the path space of $X$ , called $P X$ is the space of all paths in $X$ with the base point $^ *$ as starting point, i.e. all $\gamma : \lfloor 0 , 1 \rfloor \to X$ for which $\gamma ( 0 ) = *$ . This is a fibre bundle $\pi : P X \to X$ , where $\pi ( \gamma ) = \gamma ( 1 )$ . Clearly, $\pi ^ { - 1 } ( * )$ consists of all $\gamma$ such that $\gamma ( 0 ) = \gamma ( 1 )$ , which is the loop space $\Omega X$ . We thus get the fibre bundle $\Omega X \to P X \to X$ . Now the crucial point is that $P X$ is always contractible, so that all its homotopy groups are trivial. From the HES we thus get that $\pi _ { n } ( X ) = \pi _ { n + 1 } ( \Omega X )$ as we mentioned before.

# 6.3 Homotopy classification of vector bundles

Let us focus mainly on vector bundles from now on. For simplicity, we restrict to the case of complex vector bundles, only occasionally commenting on the real case. Consider the set $\mathrm { V e c t } ^ { n } ( M )$ of equivalence classes of complex rank $n$ vector bundles over a manifold $M$ , two bundles being equivalent if they are isomorphic in the bundle sense. In subsection 4.3, we saw that we can easily add two vector bundles $E$ and $E ^ { \prime }$ by constructing their Whitney sum $E \oplus E ^ { \prime }$ . Denoting their respective fibres over $x \in M$ by $E _ { x }$ and $E _ { x } ^ { \prime }$ , the sum bundle is simply the bundle with as fibre over $x$ the direct sum of the vector spaces $E _ { x } \oplus E _ { x } ^ { \prime }$ .

This construction is just a special case of the fibre product for general bundles, but given the additional structure on a vector bundle, we can of course think of many more ways to build new bundles from old. Also of importance to us will be the tensor product $E \otimes E ^ { \prime }$ with fibres $E _ { x } \otimes E _ { x } ^ { \prime }$ , the tensor product of the two vector spaces. The transition functions are tensor products of the respective matrices representing the transition functions of $E$ and $E ^ { \prime }$ .

Example 26. Let us give an example involving real vector bundles. We already introduced the real projective space $\mathbb { R } P ^ { n }$ . The canonical line bundle over $\mathbb { R } P ^ { n }$ has as total space the subspace of $\mathbb { R } P ^ { n } \times \mathbb { R } ^ { n + 1 }$ consisting of pairs $( x , v )$ with $v \in x$ , where we remind the reader that $x$ is a line through the origin in $\mathbb { R } ^ { n + 1 }$ . Now, $\mathbb { R } P ^ { 1 }$ is homeomorphic to $S ^ { 1 }$ and the canonical line bundle over $\mathbb { R } P ^ { 1 }$ is nothing but the (infinite) M¨obius band, which in this context we will call the M¨obius bundle $M o$ . The transition functions of $M o$ form the group $\mathbb { Z } _ { 2 }$ , the nontrivial element needed to flip the orientation of the line when going once around the circle. It now easily follows that $M o \otimes M o = S ^ { \mathrm { 1 } } \times \mathbb { R }$ , the trivial line bundle over $S ^ { 1 }$ .

This follows because on the overlap with the nontrival transition function $^ { - 1 }$ , the product bundle has transition function $( - 1 ) \times ( - 1 ) = 1$ .

We mentioned before that the tangent bundle $T S ^ { 2 }$ is nontrivial. It can be proven that the only $n$ for which $T S ^ { n }$ is a trivial bundle are $n = 1$ , 3 or 7. For $n = 1$ or 3, this follows immediately from the fact that $S ^ { 1 } = U ( 1 )$ and $S ^ { 3 } = S U ( 2 )$ are both Lie groups. The underlying reason which works for all three cases is the existence of the normed division algebras (over $\mathbb { R }$ ) of the complex numbers $\mathbb { C }$ , the quaternions $\mathbb { H }$ and the octonions or Cayley numbers.

There is however a sense in which $T S ^ { n }$ is ‘not too far’ from being trivial. We argued in subsection 4.3 that adding the normal bundle $N S ^ { 2 }$ to $T S ^ { 2 }$ yields a trivial bundle. This easily generalizes to $T S ^ { n } \oplus N S ^ { n } = S ^ { n } \times \mathbb { R } ^ { n + 1 }$ , where $N S ^ { n }$ is actually also a trivial bundle. We will denote the trivial bundle of rank $n$ by $I ^ { n }$ , hoping that its base space will be clear from the context. A vector bundle $E$ for which an $k$ exists such that $E \oplus I ^ { k }$ is trivial will be called stably trivial. So $T S ^ { n }$ is stably trivial for all $n$ .

Theorem 10. For each vector bundle $E$ over a compact manifold, there exists a vector bundle $E ^ { \prime }$ , called the complementary bundle, such that $E \oplus E ^ { \prime }$ is trivial.

Note that this by no means implies that all vector bundles over compact manifolds are stably trivial, since $E ^ { \prime }$ need not be trivial.

In subsection 4.3, we also introduced the notion of the pull-back bundle $f ^ { * } E  A$ of $E  B$ for a map $f : A  B$ . It can be shown that the pull-back satisfies the following conditions

$$
( f g ) ^ { * } E = g ^ { * } ( f ^ { * } E ) , \quad 1 ^ { * } E = E ,
$$

where the equal signs are more precisely bundle isomorphisms.

The following important theorem is a first big step towards the classification of fibre bundles.

Theorem 11. Given a fibre bundle $E  B$ and a manifold $A$ , homotopic maps $f , g : A $ $B$ induce equivalent bundles $f ^ { * } E \cong g ^ { * } E$ .

An interesting immediate consequence is that fibre bundles over contractible manifolds are trivial. Indeed, for a contractible manifold $M$ , the identity map is homotopic to the constant map $c : M \to M : x \mapsto x _ { 0 }$ for some fixed $x _ { 0 }$ . By the above theorem, this implies $E = 1 ^ { * } E = c ^ { * } E$ for any bundle $E$ over $M$ . On the other hand $c ^ { * } E$ is the trivial bundle $M \times \pi ^ { - 1 } ( x _ { 0 } )$ . The result follows.

Consider now a map $f : M \to N$ . This induces a map $f ^ { * } : \mathrm { V e c t } ^ { n } ( N ) \to \mathrm { V e c t } ^ { n } ( M )$ and because of (6.3.1) this is a contravariant functor from $\boldsymbol { S }$ , the category of manifolds and smooth maps, to the category of sets and maps. As was discussed in subsection 3.5, this implies that homeomeorphic manifolds have bijective sets of rank $n$ vector bundles over them. Theorem 11 actually implies that this functor is homotopy invariant, so that we can see it as a functor from the category of manifolds and homotopy classes of maps to the category of sets and maps. This in turn implies that manifolds of the same homotopy type have bijective sets ${ \mathrm { V e c t } } ^ { n }$ . For instance $\mathrm { V e c t } ^ { n } ( * ) \cong \mathrm { V e c t } ^ { n } ( \mathbb { C } ^ { k } )$ . They both only contain the trivial bundle.

The existence of complementary bundles over compact manifolds together with theorem 11 leads to a classification of vector bundles. Again we consider only the complex case. This classification involves Grassmann manifolds.

Example 27. Just like in the real case, we can introduce the complex projective space $\mathbb { C } P ^ { n }$ as the space of all complex lines $l$ through the origin of $\mathbb { C } ^ { n + 1 }$ . The canonical line bundle over $\mathbb { C } P ^ { n }$ is now the line bundle with as fibre over $[ l ] \in \mathbb { C } P ^ { n }$ the complex line $\it l$ . The Grassmann manifold $G _ { n } ( \mathbb { C } ^ { k } )$ is a generalization of this, namely the space of all $n$ -dimensional subspaces $W$ of $\mathbb { C } ^ { k }$ , or

$$
G _ { n } ( \mathbb { C } ^ { k } ) = \frac { U ( k ) } { U ( n ) U ( k - n ) } .
$$

This is because $G _ { n } ( \mathbb { C } ^ { k } )$ is a left $U ( k )$ -space, with the left action inherited from $\mathbb { C } ^ { k }$ . One can show that this action is transitive. On the other hand, the isotropy subgroup of any point in $G _ { n } ( \mathbb { C } ^ { k } )$ is $U ( n ) U ( k - n )$ ; the $U ( n )$ just rotates the basis spanning the relevant $n$ -subspace $W$ , while the $U ( k - n )$ acts on its orthogonal complement and thus also leaves $W$ invariant. The canonical bundle $Q _ { n , k }$ over $G _ { n } ( \mathbb { C } ^ { k } )$ is now simply the rank $n$ complex vector bundle with fibre $W$ over $[ W ] \in G _ { n } ( \mathbb { C } ^ { k } )$ .

Now consider a complex rank $n$ vector bundle $E$ over a compact manifold $M$ . The existence of a complementary bundle $E ^ { \prime }$ means that $E \oplus E ^ { \prime } = M \times \mathbb { C } ^ { k }$ for some $k$ . We thus have the injective bundle map $i : E \to M \times \mathbb { C } ^ { k }$ with over each $x \in M$ an injective linear map $i _ { x } : E _ { x } \to \mathbb { C } ^ { k }$ . This implies that $E _ { x }$ is naturally isomorphic with $\mathrm { i m } i _ { x }$ . All this provides us with a natural map

$$
f : M  G _ { n } ( \mathbb { C } ^ { k } ) : x \mapsto \operatorname { i m } i _ { x } .
$$

Note that a different complementary bundle might lead to a different map $g$ , but the important point is that $f$ and $g$ would turn out be homotopic. Now the pull-back $f ^ { * } Q _ { n , k }$ of the canonical bundle over $G _ { n } ( \mathbb { C } ^ { k } )$ is equivalent to $E$ . This follows immediately from the definition of the pull-back bundle. Indeed, the fibre of $f ^ { * } Q _ { n , k }$ over $x \in M$ is the fibre of $Q _ { n , k }$ over $f ( x ) = \mathrm { i m } i _ { x }$ . As we said $E _ { x }$ is isomorphic to $\mathrm { i m } i _ { x }$ and we know that an $M$ -map of vector bundles which reduces to an isomorphism on the fibres is a bundle isomorphism.

There is one subtlety however. The more complicated the bundle $E$ gets, the higher $k$ will turn out to be, even for fixed $n$ . In order to discuss all rank $n$ vector bundles over $M$ at the same time, one introduces the ‘infinite Grassmannian’ $G _ { n } \equiv G _ { n } ( \mathbb { C } ^ { \infty } )$ , which is roughly the union of all $G _ { n } ( \mathbb { C } ^ { k } )$ (i.e. for all $k$ ) through a direct limit. The canonical bundle $Q _ { n } \to G _ { n }$ can similarly be defined. Remember that homotopic maps induce equivalent pull-back bundles. Since we argued above that every complex vector bundle over $M$ corresponds uniquely to a homotopy class in $[ M , G _ { n } ]$ , we arrive at the following theorem of great theoretical importance.

Theorem 12. The sets $[ M , G _ { n } ]$ and ${ \mathrm { V e c t } } ^ { n } ( M )$ are bijective.

For this reason, $G _ { n }$ and $Q _ { n }$ are called the classifying space and universal bundle for rank $n$ complex vector bundles, respectively.

This actually connects to the classification of general fibre bundles in the following way. Fibre bundles with structure group $G$ over a manifold $M$ are classified by $[ M , B G ]$ , where $_ { B G }$ is called the classifying space for fibre bundles with structure group $G$ . We have just argued that $B G L _ { n } \sim G _ { n }$ . $G L _ { n }$ actually deformation retracts to $U ( n )$ in the complex case and $O ( n )$ in the real case, so that we get that $B U ( n ) = G _ { n }$ and $B O ( n ) = G _ { n } ^ { \mathbb { k } }$ , the real analog of $G _ { n }$ .

# 6.4 Vector bundles over spheres

Since fibre bundles over contractible spaces are trivial, the easiest non-trivial thing to look at seems to be the classification of vector bundles over spheres. This is done by something called clutching. Consider a complex rank $n$ vector bundle $E \to S ^ { k }$ with a sphere as base. We can cover $S ^ { k }$ by two hemispheres $D _ { + }$ and $D _ { - }$ with overlap $D _ { + } \cap D _ { - } \ = \ S ^ { k - 1 }$ . On this overlap the fibres are related by a transition function $f : S ^ { k - 1 } \to G L ( n , \mathbb { C } )$ , which is used to glue the respective bundles over $D _ { + }$ and $D _ { - }$ together. Using a different language, the transition function is also called a clutching function. Conversely, given a clutching function $f$ , one can construct an element $E _ { f } \in \mathrm { V e c t } ^ { n } ( S ^ { k } )$ . One can then prove that homotopic clutching functions yield equivalent bundles. Since, as we mentioned before, $[ X , Y ] = [ X , Y ^ { \prime } ]$ if $Y \sim Y ^ { \prime }$ are homotopy equivalent, we can just as well use $U ( n )$ instead of $G L ( n , \mathbb { C } )$ to classify bundles over spheres.

Theorem 13. The map $\pi _ { k - 1 } ( G L ( n , \mathbb { C } ) ) = \pi _ { k - 1 } ( U ( n ) ) \to { \mathrm { V e c t } } ^ { n } ( S ^ { k } )$ is bijective.

In other words, vector bundles over spheres are classified by homotopy groups.

Example 28. Every complex vector bundle over $S ^ { 1 }$ is trivial since $\pi _ { 0 }$ counts the number of path components and $G L ( n , \mathbb { C } ) \sim U ( n )$ is path connected. For real vector bundles this is different since $G L ( n , \mathbb { R } ) \sim O ( n )$ has two disconnected components. For instance, real line bundles over $S ^ { 1 }$ are classified by $\pi _ { 0 } ( G L ( 1 , \mathbb { R } ) )$ and $G L ( 1 , \mathbb { R } ) = \mathbb { R } - \{ 0 \}$ has two components. So $\mathrm { V e c t } _ { \mathbb { R } } ^ { 1 } ( S ^ { 1 } )$ has two elements, the trivial bundle and $M o$ , the M¨obius bundle.

Example 29. Slightly more interesting is $\mathrm { V e c t } ^ { n } ( S ^ { 2 } ) = \pi _ { 1 } ( U ( n ) )$ . In case of line bundles we already know the answer, namely $\pi _ { 1 } ( U ( 1 ) ) = \mathbb { Z }$ . We already encountered almost exactly this situation before when considering the Dirac monopole. There it was mentioned that maps $g _ { n } : S _ { 1 } \to S ^ { 1 } : z \mapsto z ^ { n }$ (with $S ^ { 1 }$ taken to be the unit circle in the complex plane) suffice to classify principal $U ( 1 )$ -bundles $P$ over $S ^ { 2 }$ . We are now simply considering the vector bundles associated to these principal bundles, which amounts to essentially the same thing. Our assumption there was thus completely justified. It is interesting to note that the same classification was achieved by looking at the first Chern class $c _ { 1 } ( P ) \in H ^ { 2 } ( S ^ { 2 } , \mathbb { Z } ) = \mathbb { Z }$ . Exactly the same actually holds for higher rank bundles over $S ^ { 2 }$ , since $\pi _ { 1 } ( U ( n ) ) = \mathbb { Z }$ for all higher $n$ as well. This invariant can each time be identified with the first Chern class of the bundle. Complex vector bundles over $S ^ { 2 }$ are thus completely classified by their rank an their first Chern class.

The reader might be confused at this point, as we showed in the previous subsection that complex rank $n$ vector bundles over $S ^ { k }$ are classified by $[ S ^ { k } , G _ { n } ] = \pi _ { k } ( G _ { n } )$ , while now we claim the same for $\pi _ { k - 1 } ( U ( n ) )$ . This however resembles (6.1.10), and indeed it turns out that this argument can be made more generally. It can be shown (and is in fact quite crucial) that the total space of a universal bundle is weakly contractible (i.e. all its homotopy groups are trivial). For a classifying bundle $G  E G  B G$ the HES then impies that $\pi _ { k - 1 } ( G ) = \pi _ { k } ( B G )$ . For any Lie group $G$ we thus find,

$$
[ S ^ { k - 1 } , G ] = [ S ^ { k } , B G ] = [ S S ^ { k - 1 } , B G ] = [ S ^ { k - 1 } , \Omega B G ] ,
$$

so the operator $\Omega$ is a kind of homotopy inverse of the ‘classifying operator’ $B$ . As a side comment, from a homotopy theory point of view, it is the classification of principal bundles which is more natural. One can show that for any topological group $G$ , there exists a classifying space $_ { B G }$ and a weakly contractible universal principal $G$ -bundle $P G$ over it so that any principal $G$ -bundle $P  X$ is isomorphic to $f ^ { * } P G$ , where $f : X \to B G$ . As before, the set of isomorphism classes of principal $G$ -budles over $M$ is isomorphic to $[ M , B G ]$ . For instance, from our discussion of covering spaces the reader could have guessed that the circle is a classifying space for $\mathbb { Z }$ , $S ^ { 1 } = B \mathbb { Z }$ , and $\mathbb { Z } \to \mathbb { R } \to S ^ { 1 }$ is the associated universal bundle. For $U ( n )$ , the resulting classifying spaces should be equivalent to those coming from the vector bundle construction. Indeed, in this case the classifying space will always have the same homotopy groups as the infinite Grassmanian $G _ { n }$ .

Example 30. To connect these ideas to the instantons on $S ^ { 4 }$ we discussed before, note that $\mathrm { V e c t } ^ { 2 } ( S ^ { 4 } ) = \pi _ { 3 } ( U ( 2 ) ) = \pi _ { 3 } ( S ^ { 3 } ) ) = \mathbb { Z }$ . More generally, one can show that, denoting the set of all equivalence classes of $G$ -principal bundles over $X$ by $\operatorname { P r i n } _ { G } ( X )$ , one has

$$
\operatorname* { P r i n } _ { G L _ { n } ( \mathbb { C } ) } ( X ) \cong \operatorname { V e c t } ^ { n } ( X ) \cong [ X , B U ( n ) ] .
$$

In particular, $\operatorname* { P r i n } _ { G L _ { 2 } ( \mathbb { C } ) } ( S ^ { 4 } ) \cong \operatorname { V e c t } ^ { 2 } ( S ^ { 4 } ) \cong \pi _ { 4 } ( B U ( 2 ) ) = \pi _ { 3 } ( U ( 2 ) ) = \mathbb { Z }$ .

# 6.5 Characteristic classes II: algebraic topology approach

There is a purely homotopy theoretic way of defining cohomology. This is done by first introducing Eilenberg-Maclane spaces.

Definition 30. An Eilenberg-Maclane space $K ( G , n )$ is a space for which

$$
\pi _ { i } ( K ( G , n ) ) = { \left\{ \begin{array} { l l } { G } & { { \mathrm { f o r } } \quad i = n } \\ { 0 } & { { \mathrm { f o r } } \quad i \neq n } \end{array} \right. }
$$

For instance $K ( \mathbb { Z } , 1 ) ~ = ~ S ^ { 1 }$ , since its covering space $\mathbb { R }$ is contractible. In general Eilenberg-Maclane spaces are quite complicated although they can be shown to exist for any group $G$ . To illustrate this, remember that the classifying space for complex line bundles is $G _ { 1 } = \mathbb { C } P _ { \infty }$ , the ‘infinite’ projective space. This can thus also be taken to be the classifying space for principal $U ( 1 )$ -bundles. In this case the principal universal bundle turns out to be $S ^ { 1 } \to S ^ { \infty } \to \mathbb { C } P _ { \infty }$ , which is an inductive limit of the collection of principal bundles $U ( 1 ) \to S ^ { 2 n + 1 } \to \mathbb { C } P ^ { n }$ , which are easy generalizations of the Hopf bundle. The main point is that $\pi _ { k } ( S ^ { \infty } ) = 0$ for all $k$ . Therefore it follows from the HES for this bundle that

$$
\pi _ { k } ( \mathbb { C } P _ { \infty } ) = \pi _ { k - 1 } ( S ^ { 1 } ) .
$$

This shows that $K ( \mathbb { Z } , 2 ) = \mathbb { C } P _ { \infty }$

Now cohomology groups for any coefficient group $G$ can be defined as follows:

$$
H ^ { n } ( X , G ) = [ X , K ( G , n ) ] .
$$

Note that this is a kind of dual to the Hurewitz isomorphism, which says $H _ { n } ( K ( G , n ) ) = G$ . Since we mainly need this for motivational purposes and can take it to be a definition of cohomology, we will not explain this any further and simply take it as it is. The point we want to make is the following: take for instance $G _ { 1 } = \mathbb { C } P _ { \infty }$ from the previous paragraph; this is a classifying space for complex line bundles and the set $[ X , G _ { 1 } ]$ is thus isomorphic to the set of line bundles over $X$ . We now see that this is just as well classified by $H ^ { 2 } ( X , \mathbb { Z } )$ . As we hinted at before, this is precisely the first Chern class of the line bundle. This realization is a first step in the topological approach to characteristic classes, to which we now turn.

We saw that any complex rank $k$ vector bundle $E  X$ is equivalent to a pull-back $f ^ { * } Q _ { k }$ of the universal bundle $Q _ { k }$ over the classifying space $B U ( k ) \sim G _ { k }$ , where the effect of $f$ only depends on its class in $[ X , B U ( k ) ]$ . Now the cohomology ring $H ^ { \bullet } ( G _ { k } , \mathbb { Z } )$ has even degree generators $c _ { n } ( Q _ { k } ) \in H ^ { 2 n } ( G _ { k } , \mathbb { Z } )$ . The $n$ -th Chern class $c _ { n } ( E )$ of the bunlde $E$ is defined to be

$$
c _ { n } ( E ) = c _ { n } ( f ^ { * } Q _ { k } ) = f ^ { * } c _ { n } ( Q _ { k } ) \in H ^ { 2 n } ( X , \mathbb { Z } ) .
$$

The total Chern class is then $c ( E ) = 1 + c _ { 1 } ( E ) + c _ { 2 } ( E ) + \cdot \cdot \cdot$ . The precise definition of the Chern class is however less important than its properties

1. Naturality: given a complex vector bundle $E  X$ and a map $f : Y \to X$ , the Chern class satisfies

$$
c ( f ^ { * } E ) = f ^ { * } c ( E ) .
$$

Note that on the left hand side $f ^ { * } E$ is the pull-back bundle of $E$ , while on the right hand side $f ^ { * }$ denotes the pull-back acting on differential forms. This implies that equivalent bundles have the same Chern classes (indeed, characteristic classes in general) since they will both be induced from the universal bundle by homotopic maps, and cohomology is a homotopy invariant functor.

2. For $E \oplus E ^ { \prime }$ the Chern class is $c ( E \oplus E ^ { \prime } ) = c ( E ) c ( E ^ { \prime } )$ .

3. For a complex line bundle $L$ , we get $c ( L ) = 1 + c _ { 1 } ( E )$ , where $c _ { 1 } ( E )$ should be interpreted in the sense explained above, i.e as an element of $H ^ { 2 } ( X , \mathbb { Z } ) = [ X , K ( \mathbb { Z } , 2 ) ] =$ $[ X , G _ { 1 } ]$ .

The first property is actually the definition what is called a characteristic class in general. The other two properties are quite useful in actual computations, as well as making contact with the previously given construction for characteristic classes. For this we need a very useful technical tool called the splitting principle. This follows essentially from the fact that any rank $n$ complex vector bundle $E$ over a compact manifold can always be pulled back to a direct sum of complex line bundles $L _ { i }$ over some other compact manifold, i.e. there exists a map $f$ such that

$$
f ^ { * } E = L _ { 1 } \oplus L _ { 2 } \oplus \cdots \oplus L _ { n } .
$$

We will not go into the details of the arguments here, but because of the naturality property this implies the following

Theorem 14. (Splitting principle) To prove polynomial identities of Chern classes one can assume that the bundles involved are direct sums of line bundles.

Actually, using the splitting principle, one can show that the above list of properties of the Chern class uniquely defines it, so that it can be taken as a definition of the Chern class. The splitting principle allows us to write the Chern class itself as

$$
c ( E ) = \prod _ { i = 1 } ^ { k } ( 1 + x _ { i } ) ,
$$

where $x _ { i } = c _ { 1 } ( L _ { i } )$ for some line bundle $\boldsymbol { L } _ { i }$ . This resembles a lot expressions appearing in (5.5.3), where the $x _ { i }$ were essentially the eigenvalues of the curvature two-form matrix. Indeed, the two-forms appearing in the diagonal form of the curvature could be seen as curvature two-forms on some line bundles. In that computation we thus already saw a hint of the splitting principle: as far as Chern classes are concerned, we might as well take the curvature to be diagonal, i.e the curvature of a connection on a direct sum of line bundles. This also more or less shows that the Chern class presented here is the same object as the Chern class presented in subsection 5.5. More precisely, the object presented before was a representation of the Chern class using de Rham cohomology.

Example 31. For two line bundles $L$ and $L ^ { \prime }$ , $c _ { 1 } ( L \otimes L ^ { \prime } ) = c _ { 1 } ( L ) + c _ { 1 } ( L ^ { \prime } )$ . On the other hand, for a line bundle $L$ and its dual $L ^ { * }$ the transition functions are related by $g _ { L ^ { * } } = ( g _ { L } ) ^ { - 1 }$ , so that $L \otimes L ^ { * } = I ^ { 1 }$ . This implies that $c _ { 1 } ( L ) = - c _ { 1 } ( L ^ { * } )$ . This shows that in the complex case, a vector bundle is not generically equivalent with its dual.

Using the splitting principle, we can also define other characteristic classes, all sharing the naturality property. We will only introduce one more very important one, called the Chern character. Given the expression (6.5.5) for the Chern class, the Chern character is defined to be

$$
c h ( E ) = \sum _ { i = 1 } ^ { n } e ^ { x _ { i } } = \operatorname { r a n k } E + c _ { 1 } ( E ) + \left( { \frac { 1 } { 2 } } c _ { 1 } ( E ) ^ { 2 } - c _ { 2 } ( E ) \right) + \cdots .
$$

What makes the Chern characteristic so interesting is its behavior under sums and products of vector bundles

$$
c h ( E \oplus E ^ { \prime } ) = c h ( E ) + c h ( E ^ { \prime } ) , \quad c h ( E \otimes E ^ { \prime } ) = c h ( E ) c h ( E ^ { \prime } ) .
$$

Exercise 12. Show the two properties above, starting from the behavior of the Chern class under the same operations on bundles.

In Chern-Weil theory, the Chern character can be represented by

$$
c h ( F ) = \mathrm { T r } \exp \left( \frac { 1 } { 4 \pi i } F \right) .
$$

More characteristic classes can be obtained in a similar way by starting from different polynomials in the variables $x _ { i }$ . For instance, the cohomology formulation of the Atiyah-Singer index theorem requires, apart from the Chern character, the introduction of the Todd class. For real vector bundles, one defines the Pontryagin class as the Chern class of the complexified bundle and then uses these to define the $\hat { A }$ class (also known as the Aroof genus). For instance, in the absence of a $B$ -field the Wess-Zumino part of a D -brane $p$ effective action takes the form

$$
S \propto \int { \left[ { C \wedge { c h ( E ) } \wedge \frac { \sqrt { \hat { A } ( T N ) } } { \sqrt { \hat { A } ( N N ) } } } \right] _ { p + 1 } } ,
$$

where the brane wraps a submanifold $N$ with tangent bundle $^ { T M }$ and normal bundle $N N$ , and there is complex vector bundle $E  N$ , defined on the brane. The division is roughly speaking an inverse of the wedge product. The rest of the notation is explained in the next section.

The characteristic class for real vector bundles which has properties formally analogous to those of the Chern class for complex vector bundles, is called the Stiefel-Whitney class. It is an element $w ( E )$ of $H ^ { \bullet } ( X , \mathbb { Z } _ { 2 } )$ because one can show that $K ( \mathbb { Z } _ { 2 } , 1 ) = \mathbb { R } P _ { \infty }$ , which is the classifying space for real line bundles or double coverings (i.e principal bundles with as fibre $S ^ { 0 } = \{ 0 , 1 \}$ ). They play an important role in many parts of theoretical physics. For instance, a manifold $M$ is orientable iff $w _ { 1 } ( T M ) = 0$ , and admits a spin structure iff $w _ { 1 } ( T M ) = w _ { 2 } ( T M ) = 0$ . A real vector bundle $E$ is said to admit a spin $c$ structure iff it is orientable $-$ i.e. $w _ { 1 } ( E ) = 0$ – and $w _ { 3 } ( E ) = 0$ . Although we will not have time to go into this, K-theory predicts that for trivial NSNS 3-form $H$ D-branes always wrap spin $\boldsymbol { \cdot }$ manifolds (i.e manifolds which allow for bundles with a spin $\mathbf { \Psi } _ { . } ^ { c }$ structure).

# Chapter 7

# Topological K-theory

In this final section we introduce the very basics of what is called topological K-theory. It arises when trying to build a (generalized) cohomology theory starting from $\mathrm { V e c t } ( X )$ for some manifold $X$ , where $\mathrm { V e c t } ( X )$ is the space of all complex vector bundles (of arbitrary rank) over $X$ . From now on $X$ is taken to be compact. The standard references are [19] and [20]. Also [10], [14], [16] and [17] are useful. The first part of the physics oriented review [21] also contains a useful survey.

# 7.1 The functors $K ( X )$ and $\widetilde K ( X )$

We already introduced a binary operation on $\mathrm { V e c t } ( X )$

$$
\oplus : \operatorname { V e c t } ( X ) \times \operatorname { V e c t } ( X ) \to \operatorname { V e c t } ( X ) : ( E , F ) \mapsto E \oplus F .
$$

We would very much like this operation to yield a group structure on $\mathrm { V e c t } ( X )$ . The problem is that in general there is no cancellation law

$$
E \oplus G = F \oplus G \Rightarrow E = F .
$$

This implies that $\mathrm { V e c t } ( X )$ is a monoid, but not a group – there are no inverses in general. For example we already noticed that $T S ^ { n } \oplus I ^ { \scriptscriptstyle 1 } = I ^ { n + 1 } = I ^ { n } \oplus I ^ { \scriptscriptstyle 1 }$ , but $T S ^ { n }$ itself is only trivial for $n = 1$ , $_ 3$ and 7. This example however gives us already one idea about how to fix this problem. Define two vector bundles $E$ and $F$ to be stably equivalent, denoted $E \sim F$ , if $E \oplus I ^ { n } = F \oplus I ^ { m }$ , where $n$ and $m$ need not be equal, so $E$ and $F$ need not have equal rank. For instance, $T S ^ { n }$ is stably equivalent to a trivial bundle of any rank, and is thus called stably trivial.

Call ${ \overset { \sim } { K } } ( X )$ the set of all equivalence classes of $\mathrm { V e c t } ( X )$ under stable equivalence, or stable equivalence classes for short. In ${ \tilde { K } } ( X )$ there is a cancellation law. Indeed, since $X$ is compact, every $G$ has a complementary bundle $G ^ { \prime }$ , for which $G \oplus G ^ { \prime } = I ^ { n }$ for some $n$ . Thus $E \oplus G \sim F \oplus G$ implies $E \oplus I ^ { m } = F \oplus I ^ { m }$ for some $m$ , so that $E \sim F$ . ${ \tilde { K } } ( X )$ is then given a group structure by defining $( E ) + ( F ) = ( E \oplus F )$ , where ( $E$ ) denotes the stable equivalence class of $E$ .

Theorem 15. ${ \overset { \sim } { K } } ( X )$ is a group for $X$ compact. The identity is the class of $I ^ { n }$ for any $n$ , or equivalently the class of all stably trivial bundles. The inverse of ( $E$ ) is $( E ^ { \prime } )$ , where $E ^ { \prime }$ is complementary to $E$ .

For example, since all bundles over a point $^ *$ are trivial, they are also stably trivial, so that $\widetilde K ( * ) = 0$ . As another example, the tangent bundle $T S ^ { n }$ represents the identity element of $\tilde { K } ( S ^ { n } )$ .

There is another way of defining a group starting from $\mathrm { V e c t } ( X )$ , which works for all abelian monoids. As an elementary example, consider the natural numbers N. $( \mathbb { N } , + )$ forms a monoid, but not a group, since there are no inverses in $\mathbb { N }$ . Now define an equivalence relation $\sim$ on $\mathbb { N } \times \mathbb { N }$ as follows

$$
( a , b ) \sim ( c , d ) \quad { \mathrm { i f f } } \quad a + d = b + c .
$$

This can be read as $( a , b ) = a - b$ and the condition as $a - b = c - d$ . Addition is defined by $( a , b ) + ( c , d ) = ( a + c , b + d )$ . Clearly, the identity is the class of $( a , a )$ for any $a \in \mathbb N$ , and every class $[ ( a , b ) ]$ has an inverse $[ ( b , a ) ]$ . The quotient $\mathbb { N } \times \mathbb { N } / \sim$ together with the above defined addition is of course nothing but the abelian group $( \mathbb { Z } , + )$ . A similar construction takes us from the multiplicative monoid $( \mathbb { Z } , \cdot )$ to the group of rationals $( \mathbb { Q } , \cdot )$ .

Theorem 16. Given a monoid $( A , + )$ , define the equivalence relation $\sim$ on $A \times A$ by

$$
( a , b ) \sim ( c , d ) \quad { \mathrm { i f ~ t h e r e ~ e x i s t s ~ a n ~ } } e \in A { \mathrm { ~ s u c h ~ t h a t ~ } } a + d + e = b + c + e
$$

The quotient $A \times A / \sim$ together with the operation $( a , b ) + ( c , d ) = ( a + c , b + d )$ forms a group. In a more general categorical context, this is called the Grothendieck group of $A$ .

The extra ingredient $e \in A$ compared to the case of the natural numbers is required because sometimes there is no cancellation law. This is indeed the case for the addition of vector bundles as we saw above.

Definition 31. The Grothendieck group of $\mathrm { V e c t } ( X )$ is denoted by $K ( X )$ .

Elements of $K ( X )$ can thus be seen as formal differences of vector bundles. More precisely, we will denote $[ ( E , 0 ) ]$ by $[ E ]$ and $[ ( E , F ) ]$ by $[ E ] - [ F ]$ . Note that this is consistent with $\lfloor E \rfloor + \lfloor F \rfloor = \lfloor E \oplus F \rfloor$ . Adding the bundle complementary to $F$ , we see that every element can be written as $[ E ] - [ I ^ { n } ]$ for some $n$ . Such formal differences of bundles are sometimes called virtual bundles.

Now, consider elements of the form $[ E _ { n } ] - [ I ^ { n } ]$ , where $n$ is the rank of the bundle $E _ { n }$ . They clearly form a subgroup of $K ( X )$ . Suppose that $[ E _ { n } ] - [ I ^ { n } ] = [ F _ { m } ] - [ I ^ { m } ]$ . This immediately implies that $( E _ { n } \oplus G ) = ( F _ { m } \oplus G )$ for some $G$ (and the round brackets denote stable equivalence as before). Since for stable equivalence classes the cancellation law holds, it follows that $E _ { n } \sim F _ { m }$ are stably equivalent. Conversely, for $E _ { n } \sim F _ { m }$ it is not hard to show that

$$
E _ { n } \oplus I ^ { m } \oplus G = F _ { m } \oplus I ^ { n } \oplus G ,
$$

where $G = I ^ { k }$ for some $k$ . This implies that $[ E _ { n } ] - [ I ^ { n } ] = [ F _ { m } ] - [ I ^ { m } ]$ in $K ( X )$ . This implies that ${ \overset { \sim } { K } } ( X )$ is the subgroup of $K ( X )$ with elements of the form $\left[ E _ { n } \right] - \left[ I ^ { n } \right]$ . As another way of contrasting the groups $K ( X )$ and ${ \overset { \sim } { K } } ( X )$ , note that in $K ( X )$ $[ E ] = [ F ]$ if and only if there exists an $n$ such that $E \oplus I ^ { n } = F \oplus I ^ { n }$ . Notice thus that elements of $K ( X )$ are also stable equivalence classes, but in contrast to ${ \overset { \sim } { K } } ( X )$ the respective ranks of the trivial bundles on the left and right have to be the same.

Consider next a map $f : X \to Y$ . We saw that this induces a map $f ^ { * } : \mathrm { V e c t } ( Y ) \to$ $\mathrm { V e c t } ( X )$ . Defining $f ^ { * } ( [ E ] - [ F ] ) = [ f ^ { * } E ] - [ f ^ { * } F ]$ , this factors through to K-theory, $f ^ { * } :$ $K ( Y )  K ( X )$ . This is a homotopy invariant contravariant functor from $\boldsymbol { S }$ to $\mathcal { G }$ . This implies that homotopy equivalent manifolds have isomorphic K-groups. The same applies to $f ^ { * } : \widetilde K ( Y )  \widetilde K ( X )$ .

For instance, the inclusion map $i : * \to X$ induces the epimorphism

$$
i ^ { * } : K ( X )  K ( * ) = \mathbb { Z } .
$$

It is easy to see that the kernel of this homomorphism is comprised of elements of the form $\left[ E _ { n } \right] - \left[ I ^ { n } \right]$ , i.e. $\ker i ^ { * } = { \tilde { K } } ( X )$ . More precisely, it is not hard to show that there is a splitting,

$$
K ( X ) = { \tilde { K } } ( X ) \oplus \mathbb { Z } .
$$

For this reason, ${ \overset { \sim } { K } } ( X )$ is called a reduced K-group.

The K-groups are actually rings. The multiplication simply carries over from the tensor product $E \otimes F$ on vector bundles,

$$
( [ E ] - [ F ] ) \otimes ( [ E ^ { \prime } ] - [ F ^ { \prime } ] ) = [ E \otimes E ^ { \prime } ] + [ F \otimes F ^ { \prime } ] - [ E \otimes F ^ { \prime } ] - [ F \otimes E ^ { \prime } ] .
$$

This brings them even closer to cohomology, which is also a ring. Actually, the Chern character provides a map from K-theory to cohomology

$$
c h : K ( X ) \to H ^ { \bullet } ( X , \mathbb { Q } ) : [ E ] - [ F ] \mapsto c h ( E ) - c h ( F ) .
$$

This does not depend on the representative of the K-theory class because of the nice behavior of the Chern character under addition of bundles (6.5.7). Actually, because of (6.5.7) this map is a ring homomorphism. Even stronger it induces the following isomorphism

$$
K ( X ) \otimes \mathbb { Q } \cong H ^ { 2 \bullet } ( X , \mathbb { Q } ) .
$$

Note that, although Chern classes are integral classes, Chern characters are rational combinations of them, so that they are merely rational classes themselves. That is why the tensor product with $\mathbb { Q }$ appears in the above equation. This isomorphism shows that approximating K-theory by cohomology might cause one to miss issues involving torsion.1 D-brane charges, like monopole charges, are integer valued because of Dirac quantization conditions. Classically, the charges are however not quantized and the relevant cohomology groups are real valued. The above isomorphism (7.1.6) shows that classically – i.e. in the supergravity approximation to string theory – K-theory and cohomology contain essentially the same information.

The isomorphism (7.1.6) is also important for relating the K-theory version of the Atiyah-Singer index theorem to its more practical formulation using cohomology. In particular, it hints at the relevance of the Chern character in index theory. For more details, see e.g. [14] and [22]. Especially the former reference is surprisingly readable, given the nontrivial nature of the material involved. It offers many insights in some of the topological foundations behind much of the formalism in theoretical physics, ranging from gauge theory and topological field theory to conformal field theory and string theory. Highly recommended for physicists with an interest in some math behind and related to a lot of modern physics.

# 7.2 K-groups of spheres and Bott periodicity

We would like to compute some K-groups. To his end, we start with the following observation.

Theorem 17. For real vector bundles over an $n$ -dimensional manifold $X$ , all vector bundles of rank $k$ , higher than $n$ , are stably equivalent to some vector bundle of rank $n$ . The range $k > n$ is called the stable range. For complex vector bundles (of complex rank $k$ ) the stable range is $k > [ ( n + 1 ) / 2 ]$ , where $[ m ]$ denotes the integral part of $m$ .

This implies that in ${ \overset { \sim } { K } } ( X )$ all classes can be represented by vector bundles with rank at most $\mathrm { d i m } X$ . As far as K-theory is concerned, nothing can be gained by looking at vector bundles of rank higher than $\mathrm { d i m } X$ . Furthermore, it turns out that in the stable range two vector bundles of the same rank are isomorphic if and only if they are stably equivalent. In ${ \tilde { K } } ( X )$ we can always take the representatives to be of a definite rank. Taking this rank to be some $k$ in the stable range (for the complex case, we can simply take $k > n / 2$ ), we get

$$
\widetilde K ( X ) \cong \mathrm { V e c t } ^ { k } ( X ) = [ X , G _ { k } ] , \quad k \mathrm { i n t h e ~ s t a b l e ~ r a n g e }
$$

An immediate consequence is that $\tilde { K } ( S ^ { n } )$ can be computed using homotopy groups,

$$
\widetilde K ( S ^ { n } ) = \pi _ { n } ( G _ { k } ) = \pi _ { n } ( B U ( k ) ) = \pi _ { n - 1 } ( U ( k ) ) , \quad k > n / 2 .
$$

That this stable range is exactly the same as the one we defined for the unitary groups is thus not a coincidence. Using the ‘infinite unitary group’ $U ( \infty )$ we introduced before, the above can be restated as

$$
{ \tilde { K } } ( S ^ { n } ) = \pi _ { n - 1 } ( U ( \infty ) ) .
$$

The corresponding K-groups for real vector bundles are called $K O ( X )$ and ${ \widetilde { K O } } ( X )$ . In this case we get similarly

$$
\widetilde { K O } ( S ^ { n } ) = \pi _ { n - 1 } ( O ( \infty ) ) = \pi _ { n - 1 } ( O ( k ) ) , \quad k > n .
$$

In the stable range the homotopy groups of the classical groups are known. For instance, we find $\pi _ { 2 n } ( U ( k ) ) ~ = ~ 0$ and $\pi _ { 2 n + 1 } ( U ( k ) ) ~ = ~ \mathbb { Z }$ for $k > n$ . This was obtained by explicit computation for low enough values of $n$ and $k$ , and the observation by Bott that $\pi _ { n } ( U ( \infty ) ) = \pi _ { n + 2 } ( U ( \infty ) )$ , a phenomenon thus called Bott periodicity. Here, in the complex case, the periodicity is 2. In the real case the periodicity turns out to be 8. Clearly these periodicities now occur very naturally in the K-groups,

$$
\widetilde K ( S ^ { n } ) = \widetilde K ( S ^ { n + 2 } ) .
$$

Similarly we have $\widetilde { K O } ( S ^ { n } ) = \widetilde { K O } ( S ^ { n + 8 } )$ . We can now compute the K-groups of all the spheres. Notice first that since $S ^ { 0 }$ is just two points and thus disconnected, the rank of the fibre over each point can differ, so that vector bundles over $S ^ { 0 }$ are characterized by two integers. Stable equivalence only kills one of them, thus leaving $\tilde { K } ( S ^ { 0 } ) = \mathbb { Z }$ . Using the stated results on the homotopy groups of the unitary groups and (7.1.3), we get

$$
\begin{array} { c c c c c } { { \widetilde K ( S ^ { 0 } ) = \mathbb { Z } , } } & { { \widetilde K ( S ^ { 1 } ) = 0 , } } & { { \widetilde K ( S ^ { 2 } ) = \mathbb { Z } , } } & { { \widetilde K ( S ^ { 3 } ) = 0 , } } & { { \cdot \cdot \cdot } } \\ { { K ( S ^ { 0 } ) = \mathbb { Z } ^ { 2 } , } } & { { K ( S ^ { 1 } ) = \mathbb { Z } , } } & { { K ( S ^ { 2 } ) = \mathbb { Z } ^ { 2 } , } } & { { K ( S ^ { 3 } ) = \mathbb { Z } , } } & { { \cdot \cdot \cdot } } \end{array}
$$

Note that indeed all complex bundles over $S ^ { 1 }$ are trivial so that $\widetilde K ( S ^ { 1 } )$ is necessarily trivial.   
The only nontrivial result – apart from of course Bott periodicity $-$ is thus $\tilde { K } ( S ^ { 2 } ) = \mathbb { Z }$ .

Since Bott periodicity can be stated so easily in K-theory, we expect there to exist a natural proof of Bott periodicity in K-theory. And indeed there is, although Bott proved it before the advent of K-theory, by proving that $\Omega ^ { 2 } U ( k ) \sim U ( k )$ for $k$ going to infinity.

We don’t have time to discuss the K-theory proof here, but simply give the statement of the K-theory version of Bott periodicity. This is usually done using the higher $\mathbf { K }$ -groups

$$
\begin{array} { r c l } { { { \widetilde K } ^ { - n } ( X ) } } & { { = } } & { { { \widetilde K } ( S ^ { n } X ) , } } \\ { { { \cal K } ^ { - n } ( X ) } } & { { = } } & { { { \widetilde K } ^ { - n } ( X _ { + } ) , } } \end{array}
$$

where $X _ { + } = X \sqcup *$ , the disjoint union of $X$ and a point $^ *$ , and the (reduced) suspension $S X$ of a space $X$ was introduced in (6.1.8). The original K-groups are the zeroth level groups $K ^ { 0 } ( X ) \equiv K ( X )$ and $\widetilde K ^ { 0 } ( X ) \equiv \widetilde K ( X )$ . It follows easily that

$$
K ^ { - n } ( * ) = { \widetilde K } ( S ^ { n } ) = { \left\{ \begin{array} { l l } { \mathbb { Z } } & { { \mathrm { f o r ~ } } n { \mathrm { ~ e v e n } } } \\ { 0 } & { { \mathrm { f o r ~ } } n { \mathrm { ~ o d d } } } \end{array} \right. }
$$

Using this the second definition above can be restated as

$$
K ^ { - n } ( X ) = \widetilde { K } ^ { - n } ( X ) \oplus K ^ { - n } ( * ) .
$$

So the groups $K ^ { - n } ( X )$ and ${ \tilde { K } } ^ { - n } ( X )$ are equal for odd $n$ and differ by $\mathbb { Z }$ for even $n$ . This agrees with equation (7.1.3) for $n = 0$ . Bott periodicity is then stated as follows

$$
K ^ { - n } ( X ) = K ^ { - n - 2 } ( X ) ,
$$

or similarly with $K$ replaced by $\widetilde { K }$ . Notice that this statement is actually quite a bit more general than the original Bott periodicity statement for the classical groups.

Clearly, the introduction of the higher K-groups doesn’t give more information, since they are completely determined in terms of the level zero groups. Also Bott periodicity can be easily stated without them, namely $\tilde { K } ( X ) = \tilde { K } ( S ^ { 2 } X )$ . This naively superfluous construction does have a great advantage, because it makes clear that K-theory is very close to a ‘usual’ cohomology. A construction in algebraic topology is called a (co)homology theory if it satisfied the Eilenberg-Steenrod axioms [23]. It turns out that $K ^ { \bullet }$ satisfies all these axioms except for one, which is called the dimension axiom. Therefore K-theory is sometimes referred to as a generalized or extraordinary cohomology theory, although people start using the term cohomology in a wider sense which includes K-theory these days.

Unfortunately, this very basic account of the beginnings of K-theory does not show the advantages of rephrasing K-theory as a cohomology theory. For instance, it (and its brother called relative K-theory) satisfies the same kind of long exact sequences as cohomology does. Since we reviewed the Mayer-Vietoris sequence for de Rham cohomology in these notes, let us simply mention that there is a similar Mayer-Vietoris sequence for K-groups,

$$
\begin{array} { r } { \cdots \longrightarrow K ^ { - n } ( U \cap V ) \longrightarrow K ^ { - n } ( U ) \oplus K ^ { - n } ( V ) \longrightarrow K ^ { - n } ( X ) \longrightarrow K ^ { - n + 1 } ( U \cap V ) \longrightarrow \cdots } \end{array}
$$

where $U$ and $V$ form an open cover of $X$ .

# 7.3 K-theory and D-branes

With only this brief introduction to K-theory behind us, we are already able to grasp some of the ideas behind the K-theory classification of D-branes. D-branes are sources for what are called Ramond-Ramond fields in string theory. These R-R fields are also classified by some version of K-theory. Here, we will only focus on some ideas behind the classification of D-branes, although the discussion of the classification of R-R fields should essentially be dual to this. We assume that the R-R forms are thus all zero. For the most part of the discussion we also assume a trivial NS-NS two-form or B-field. We comment on the complications involving the B-field at the end. We will assume familiarity with all the string theory ingredients involved. We will also take a(n even) more physics oriented perspective towards mathematical rigor in this final subsection.

Originally it was thought that D-branes would be appropriately classified by homology, at least at the classical (or at best semi-classical) level where a space-time interpretation is available. A D-brane was thought to be stable2 if it wraps a homologically nontrivial cycle, i.e a subspace without boundary which is itself not a boundary. There are two important problems with this idea. First of all, because of something called the Freed-Witten anomaly, not all cycles which are nontrivial in homology can be consistently wrapped by a D-brane, only those which are spinc can be. Secondly, some D-branes which seem to be stable in the homology classification can actually decay by something called D-brane instantons.

These effects are captured by the (twisted) K-theory classification. These issues are well beyond the scope of this text, but are discussed in great detail – along with many other more subtle advantages and disadvantages of the use of K-theory in this context – in [24]. We will content ourselves here with the first hints as to why D-branes could possibly be classified by K-theory.

The most intuitive approach to the appearance of K-theory ideas in the classification of D-branes is due to Edward Witten and starts from some insights of Ashoke Sen. The latter conjectured that all D-branes in type IIB string theory on some 10-manifold $M$ are classified by considering a stack of $N$ space-filling D9-branes and an equal amount of anti-D9 branes. On each stack of (anti-)D9-branes one finds a $U ( N )$ gauge bundle, which implies that we are in the realm of complex vector bundles. Now if the bundles on both stacks are equal, the stack of D9s will annihilate with the stack of anti-D9s, leaving only energy – i.e. closed strings – behind. More generally, say that there is a vector bundle $E$ living on the D9s and a vector bundle $F ^ { \dagger }$ on the anti-D9s. We denote this system by $( E , F )$ . The same reasoning as before then implies that adding the same bundle $G$ to both ‘sides’ results in a pair $( E \oplus G , F \oplus G )$ , which, after annihilation of the pair $( G , G )$ , is physically equivalent to the original pair $( E , F )$ . This is exactly the structure which defines $K ( M )$ or its reduced version.

If the pair $( E , F )$ consists of non-equivalent bundles, after the annihilation of the D9s and anti-D9s, a system of lower dimensional branes will remain, the precise nature of the resulting brane system depending in the precise nature of the bundles $E$ and $F ^ { \dagger }$ . Even stronger, according to Sen’s conjectures, every possible system of type IIB branes can be obtained in this way. To see that a non-trivial gauge bundle on a D-brane can encode a lower dimensional D-brane, consider the Wess-Zumino term in the D $p$ -brane low energy effective action (again with trivial B-field, and we assume that the A-roof genus contribution appearing in (6.5.9) can be neglected),

$$
S _ { W Z } \propto \int \left[ C \wedge e ^ { F } \right] _ { p + 1 } .
$$

Here $C$ is a formal sum over all R-R forms (which we resurrected just for this argument) and $F$ is the curvature of the connection on the bundle over the D-brane (not to be confused with the notation for the vector bundle $F ^ { \dagger }$ ). The notation $[ \cdot ] _ { p + 1 }$ means that only the $( p + 1 )$ - form component of the expression between the brackets should be considered, appropriate for integration over the $( p { + } 1 )$ -dimensional world-volume of the D $p$ -brane. Take for instance a D4-brane. Its low energy effective action would contain

$$
S _ { W Z } \propto \int C _ { 5 } + C _ { 3 } \wedge F + C _ { 1 } \wedge F \wedge F .
$$

The first term is what one would expect in the absence of a non-trivial bundle on the brane, as the D $p$ -brane is charged under the $C _ { 5 }$ flux. If the bundle on the D4 world-volume has non-trivial first Chern class, the second term suggests that it couples non-trivially to a D2-brane which is charged under the $C _ { 3 }$ . In the same way a non-trivial second Chern class (or better Chern character) suggests a coupling to a D0 through the third term.

Let us now take for granted that non-trivial bundles on the stacks of D9s encode lower dimensional branes. The process of annihilation resulting in those lower dimensional branes is called tachyon condensation. The instability of the original system manifests itself through the appearance of a tachyon in the spectrum of the strings stretching between the D9 branes. Tachyon condensation is thus the flow to a stable situation through the disappearance of the tachyon. More precisely, the tachyon field develops a vacuum (vev) expectation value and tachyon condensation can be seen as a spontaneous symmetry breaking. The situation is actually similar to the construction of the ’t Hooft-Polyakov monopole.

Example 32. Consider a gauge theory with gauge group $G$ on $\mathbb { R } ^ { 3 }$ . A Higgs field $\Phi$ charged under $G$ is a section of a vector bundle associated to a principal $G$ -bundle through some representation $\rho$ . Although $\mathbb { R } ^ { 3 }$ is contractible, there can be topologically nontrivial solutions because of finite energy conditions which result in boundary conditions on the fields involved (the Higgs and the gauge connection). More precisely, in order to have a finite energy solution, the Higgs field needs to develop a vev ‘at infinity’. This breaks the original gauge group $G$ down to a subgroup $H$ . The set of genuinely different vevs the Higgs field can thus settle into is the coset $G / H$ . This is called the vacuum manifold. Now, if the boundary condition at infinity were simply $\partial \Phi = 0$ , the Higgs field would have to go to the same value $\Phi _ { 0 }$ everywhere along the two-sphere at infinity $S _ { \infty } ^ { 2 }$ and there would be no way to associate a topological charge to the solution. Since the Higgs is charged, the right condition is however

$$
\nabla _ { a } \Phi ^ { i } = \partial _ { a } \Phi ^ { i } + \rho ( A _ { a } ) ^ { i } { } _ { j } \Phi ^ { j } = 0 ,
$$

where $A$ is the local connection one-form on the associated principal bundle. Through a balancing act between $\Phi$ and $A$ it is thus possible to make $\Phi$ vary along the vacuum manifold $G / H$ while tracing out the $S _ { \infty } ^ { 2 }$ . A finite energy solution of this system is thus characterized by a map $S _ { \infty } ^ { 2 }  G / H$ and such maps are classified by $\pi _ { 2 } ( G / H )$ . As an example, the ’t Hooft-Polyakov monopole occurs in the case where $G = S U ( 2 )$ and the Higgs in the adjoint representation of $G$ . In this case, a vev of $\Phi$ breaks $G$ down to $H = U ( 1 )$ so that the vacuum manifold is a $S U ( 2 ) / U ( 1 ) = S ^ { 2 }$ . Monopoles in this theory are thus characterized by a topological winding number in $\pi _ { 2 } ( S ^ { 2 } ) = \mathbb { Z }$ , called the monopole charge.

Let us come back to the tachyon condensation of stacks of D9s in type IIB string theory and specialize to 10-dimensional Minkowski space. The tachyon $T$ is charged under $U ( N ) \times U ( N )$ , one factor of $U ( N )$ for each end of the open string corresponding to $T$ . The condensation turns out to break this to a diagonal subgroup, so that the relevant vacuum manifold is $U ( N )$ . Now a tachyon field describing a D-brane of codimension $n$ in the D9s can be shown to vanish on exactly the hyperplane of codimension $n$ ultimately occupied by the resulting lower dimensional D-brane. A codimension $n$ hyperplane can be surrounded by an $S ^ { n - 1 }$ . Just as for the ’t Hooft-Polyakov monopole, such field configurations are thus classified by homotopy classes of maps from the surrounding sphere ‘at infinity’ to the vacuum manifold, i.e by $\pi _ { n - 1 } ( U ( N ) )$ . We can take $N$ to be large enough so that it lies in the stable range. A flat codimension $n$ brane is thus classified by

$$
\begin{array} { r } { \tilde { K } ( S ^ { n } ) = \pi _ { n - 1 } ( U ( \infty ) ) . } \end{array}
$$

We now know that these groups are trivial for $n$ odd and equal to $\mathbb { Z }$ for $n$ even. K-theory thus ‘predicts’ that type IIB string theory only has odd-dimensional stable D-branes, while the even-dimensional D-branes are necessarily unstable since they do not carry nontrivial K-theory charge. The nontrivial element of $\widetilde { K } ( S ^ { 2 k } ) = \mathbb { Z }$ corresponds to the D-brane charge.

One can show that similarly D-branes in type IIA are classified by $K ^ { - 1 } ( X )$ or its reduced version. This is consistent with the discussion in the previous subsection and the fact that type IIA only contains even-dimensional branes in its spectrum, although the details are a bit less straightforward. The K-groups $K O ( X )$ and their reduced versions appear in the classification of D-branes in type I string theory. Indeed, note that here the gauge group $S O ( 3 2 )$ plays an important role, which hints at the relevance of real K-theory.

Note that there are quite some gaps in the above discussion of branes in IIB. First of all the discussion needs to be extended to general space-time manifolds. A bigger gap is however that from the discussion it is unclear whether the K-theory of the full space-time or that of certain submanifolds is important. The link between the two can be obtained using the Atiyah-Bott-Shapiro construction of K-theory and the Thom isomorphism, which we didn’t have time to get into. These matters are reviewed in great detail in the review [21]. Also the original paper by Witten [25] can be quite helpful to read.

Then there is the problem of the $H$ field. The Sen construction above only works for nontrivial $H$ . The extension of the classification of D-branes to backgrounds with nontrivial $H$ requires the introduction of twisted K-theory, which is a great deal more abstract than the K-theory constructions presented here and is less straightforward to interpret geometrically. For a review which is nonetheless packed with physical insight, see [24], where also the limitations of the twisted K-theory classification are discussed. For instance, since twisted K-theory treats NSNS and RR fluxes very differently, it is incompatible with S-duality. For the mathematically inclined (and perhaps courageous) reader, the text [16] is recommended for a grand tour of fibre bundle theory, algebraic topology and K-theory, all the way up to twisted K-theory. For instance it provides a formal introduction (for a more ‘computational’ one see [24] and references therein) to the Atiyah-Hirzebruch spectral sequence which is crucial for computations with (twisted) Ktheory and relating it to physics – although the reader might want to consult [8] first for an introduction to spectral sequences.

Finally, the solution of for instance the S-duality puzzle might be provided by some construction in algebraic K-theory, which is a generalization of the topological version presented here, and is very important in modern day algebraic geometry. Also in cases where there is no clear space-time interpretation of a D-brane as an object (e.g. a vector bundle) wrapping a submanifold, algebraic K-theory might become important. In this case, a possible approach is the interpretation of D-branes as boundary conditions in a world-sheet conformal field theory. There has indeed been quite some progress in relating D-branes in WZW models to twisted K-theory. For a review of this with many references to the literature, see [26].

# Acknowledgments

The author would like to thank the organizers of the 5th Modave Summer School for giving him an excuse for studying some exciting mathematics and physics. Also many thanks to Daniel Persson for proofreading most of the manuscript and for providing some extra pressure to make parts of it more readable and complete. The author is supported in part by grant 070034022 from the Icelandic Research Fund.

# Bibliography

[1] P. S. Aspinwall, (2004), hep-th/0403166.   
[2] M. Nakahara, Geometry, Topology and Physics (Institute of Physics Publishing, London, 1990).   
[3] C. Nash and S. Sen, Topology and Geometry for Physicists (Academic Press, San Diego, 1983).   
[4] T. Eguchi, P. B. Gilkey, and A. J. Hanson, Phys. Rept. 66, 213 (1980).   
[5] C. J. Isham, Modern Differential Geometry for Physicists (World Scientific Publishing, Singapore, 2001).   
[6] L. Tu, An Introduction to Manifolds (Springer Science $^ +$ Business Media, LLC, New York, 2008).   
[7] S. Morita, Geometry of Differential Forms (American Mathematical Society, Providence, Rhode Island, 2001).   
[8] R. Bott and L. Tu, Differential Forms in Algebraic Topology (Springer-Verlag, New York, 1982).   
[9] N. Steenrod, The Topology of Fibre Bundles (Princeton University Press, New Jersey, 1951).   
[10] D. Husemoller, Fibre Bundles, 3rd ed. (Springer-Verlag, New York, 1994).   
[11] R. Bertlmann, Anomalies in Quantum Field Theory (Oxford University Press, Oxford, 2000).   
[12] A. Collinucci and A. Wijns, (2006), hep-th/0611201.   
[13] A. Hatcher, Algebraic Topology (Cambridge University Press, Cambridge, 2002), or at author’s home page http://www.math.cornell.edu/\~hatcher/AT/ATpage.html.   
[14] C. Nash, Differential Topology and Quantum Field Theory (Academic Press, San Diego, 1991).   
[15] J. P. May, A Concise Course in Algebraic Topology (University of Chicago Press, Chicago, 1990), or at author’s home page www.math.uchicago.edu/\~may/CONCISE/ ConciseRevised.pdf.   
[16] D. Husem¨oller, M. Joachim, B. Jurˇco, and M. Schottenloher, Basic Bundle Theory and K-Cohomology Invariants (Springer, Berlin Heidelberg, 2008), or at http://www.mathematik.uni-muenchen.de/\~schotten/Texte/ 978-3-540-74955-4_Book_LNP726.pdf.   
[17] A. Hatcher, Vector Bundles and K-theory (, 2003), draft of unfinished book at author’s home page http://www.math.cornell.edu/\~hatcher/VBKT/VBpage.html.   
[18] J. Milnor and J. D. Stasheff, Characteristic Classes (Princeton University Press, New Jersey, 1974).   
[19] M. Atiyah, K-theory (Westview Press, New York, 1967).   
[20] M. Karoubi, K-theory: An Introduction (Springer, Berlin Heidelberg, 1978).   
[21] K. Olsen and R. J. Szabo, Adv. Theor. Math. Phys. 3, 889 (1999), hep-th/9907140.   
[22] H. B. Lawson and M. Michelsohn, Spin Geometry (Princeton University Press, New Jersey, 1989).   
[23] S. Eilenberg and N. Steenrod, Foundations of Algebraic Topology (Princeton University Press, New Jersey, 1952).   
[24] J. Evslin, (2006), hep-th/0610328.   
[25] E. Witten, JHEP 12, 019 (1998), hep-th/9810188.   
[26] G. W. Moore, (2003), hep-th/0304018.