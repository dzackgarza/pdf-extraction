# Algebraic Geometry

Andreas Gathmann

Class Notes TU Kaiserslautern 2019/20

# Contents

0. Introduction 3   
1. Affine Varieties 6   
2. The Zariski Topology 12   
3. The Sheaf of Regular Functions . 22   
4. Morphisms. 29   
5. Varieties 35   
6. Projective Varieties I: Topology . 43   
7. Projective Varieties II: Ringed Spaces . 53   
8. Grassmannians 62   
9. Birational Maps and Blowing Up 68   
10. Smooth Varieties . 78   
11. The 27 Lines on a Smooth Cubic Surface . 85   
12. Schemes 90   
13. Sheaves of Modules . 102   
14. Quasi-coherent Sheaves 110   
15. Differentials 118   
16. Cohomology of Sheaves . . 124

# References. 133

Index 134

# 0. Introduction

The main goal of algebraic geometry is to study solution sets of polynomial equations in several variables. So, in its easiest form, if $f _ { 1 } , \dots , f _ { k } \in K [ x _ { 1 } , \dots , x _ { n } ]$ are polynomials in $n$ variables over a given ground field $K$ we want to consider the set

$$
X = \{ x \in K ^ { n } : f _ { 1 } ( x ) = \cdots = f _ { k } ( x ) = 0 \}
$$

which is called an (affine) variety. Usually, we will ask geometric questions about such a variety $X$ and try to answer them by an algebraic study of the polynomials $f _ { 1 } , \ldots , f _ { k }$ in the polynomial ring. Hence the following two previously taught classes are of particular importance and will be prerequisites for our work:

• In the “Plane Algebraic Curves” class [G2] we have considered the case $n = 2$ and $k = 1$ in detail, i. e. zero loci of a single polynomial in two variables, which we can then think of as a curve in the plane. As illustrated by the examples in the picture below, we have studied many geometric properties of such curves: The real curve in (a) has a singular point at the origin [G2, Definition 2.22] and consists of two parts that are algebraic curves themselves [G2, Definition 1.5 (c)], the real curve in (b) has two connected components in the usual topology of the plane [G2, Proposition 5.10], and the complex curve in (c) (which is then a real surface) is topologically a torus [G2, Proposition 5.16]. We have also determined how many intersection points two curves can have [G2, Chapter 4], and how many rational functions with prescribed zeros and poles we can find on a curve [G2, Chapter 8]. It is one of the main goals of this class to consider questions of similar type in the higher-dimensional case.

![](images/45b107c855664f61c69b28e812fbfc80fe07082f9a36a698621e788540a12df5.jpg)

• In the “Commutative Algebra” class [G3] we would study the given polynomials algebraically, i. e. consider the ideal $I = \langle f _ { 1 } , \ldots , f _ { k } \rangle$ in the polynomial ring $K [ x _ { 1 } , \ldots , x _ { n } ]$ , or its quotient ring $R = K [ x _ { 1 } , \ldots , x _ { n } ] / I$ , which is called the coordinate ring of the variety $X$ and can be thought of as the ring of polynomial functions on $X$ . We can then ask algebraic questions about this: For example, is $R$ an integral domain, or a unique factorization domain [G3, Definition 8.1]? What is the Krull dimension of $R$ [G3, Definition 11.1], or the primary decomposition of $I$ [G3, Definition 8.15]?

In these notes, we will set up a category that can be interpreted geometrically as well as algebraically, so that we can combine geometric and algebraic methods in our study. For example, in the above setting we can either think geometrically of the variety $X$ or algebraically of the coordinate ring $R$ — they both carry exactly the same information, and (geometric) morphisms of varieties will precisely correspond to (algebraic) $K$ -algebra homomorphisms between their coordinate rings.

Many of the geometric questions studied for plane curves in [G2] were related to their topology, asking in some sense for the “shape” of the varieties. Such topological questions are still very interesting when we now extend our objects of study to arbitrary dimensions, but there are also entirely new types of questions that we could ask. Here are two examples:

Example 0.1 (Lines on cubic surfaces). Consider the real cubic surface

$$
X = \{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) \in \mathbb { R } ^ { 3 } : 1 + x _ { 1 } ^ { 3 } + x _ { 2 } ^ { 3 } + x _ { 3 } ^ { 3 } - ( 1 + x _ { 1 } + x _ { 2 } + x _ { 3 } ) ^ { 3 } = 0 \} \quad \subset \mathbb { R } ^ { 3 } .
$$

It is shown in the picture on the right, where we have used a linear projection to map the real 3-dimensional space onto the drawing plane (and not just a topologically correct picture). We can therefore see from the picture that there are some straight lines contained in $X$ . In fact, we will show in Chapter 11 that (after a suitable compactification) every smooth cubic surface has exactly 27 lines on it. This is another sort of question that one can ask about varieties: Do they contain curves with some prescribed properties (in this case lines), and if so, how many? This branch of algebraic geometry is usually called enumerative geometry.

![](images/9ccce032317da634c8b3d826cdf3bf5717bd19ffabd8c800cdd72546432727ca.jpg)

Example 0.2 (Curves in 3-space). Even curves can give rise to new phenomena if they are not contained in the plane. Consider e. g. the space curve

$$
X = \{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = ( t ^ { 3 } , t ^ { 4 } , t ^ { 5 } ) : t \in \mathbb { C } \} \quad \subset \mathbb { C } ^ { 3 } .
$$

We have given it parametrically here, but it is in fact easy to see that we can describe it equally well in terms of polynomial equations as

$$
X = \{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) \in \mathbb { C } ^ { 3 } : x _ { 1 } ^ { 3 } = x _ { 2 } x _ { 3 } , x _ { 2 } ^ { 2 } = x _ { 1 } x _ { 3 } , x _ { 3 } ^ { 2 } = x _ { 1 } ^ { 2 } x _ { 2 } \} .
$$

What is striking here is that we have three equations, although we would expect that a 1-dimensional object in 3-dimensional space should be given by only two equations. But if we leave out any of the three equations above, we would change the set that it describes: Leaving out e. g. the last equation $x _ { 3 } ^ { 2 } = x _ { 1 } ^ { 2 } x _ { 2 }$ would yield the whole $x _ { 3 }$ -axis $\left\{ \left( x _ { 1 } , x _ { 2 } , x _ { 3 } \right) : x _ { 1 } = x _ { 2 } = 0 \right\}$ as additional points that do satisfy the first two equations but not the last one. Similarly, leaving out the first or second equation would again add a coordinate line to $X$ .

So, in contrast to the linear algebra situation, it is not clear whether a given object of codimension $d$ can be given by $d$ equations. Even worse, for a given set of equations it is in general a difficult task to figure out what dimension their solution has. There do exist algorithms to find this out for any given set of polynomials — similarly to the Gaussian algorithm for linear equations — but they are so complicated that one would usually want to use a computer program to perform the calculations. This is a simple example of an application of computer algebra to algebraic geometry.

However, if we replace the three equations above (over the complex numbers) by

$$
x _ { 1 } ^ { 3 } = x _ { 2 } x _ { 3 } , x _ { 2 } ^ { 2 } = x _ { 1 } x _ { 3 } , x _ { 3 } ^ { 2 } = x _ { 1 } ^ { 2 } x _ { 2 } + \varepsilon
$$

for a (small) non-zero $\varepsilon \in \mathbb { C }$ , the resulting set of solutions would actually become 0-dimensional, as expected from three equations in 3-dimensional space. So we see that very small changes in the equations can make a very big difference in the resulting solution set. This means that we usually cannot apply numerical methods to our problems.

Remark 0.3 (Algebraic geometry over different ground fields). Depending on the chosen ground field, algebraic geometry also has relations to the following fields of mathematics:

(a) Over the ground field $\mathbb { R }$ or $\mathbb { C }$ we can use real resp. complex analysis to study varieties, as we occasionally did already for plane curves e. g. in [G2, Chapter 7 or Remark 8.5]. In fact, many results in algebraic geometry can also be proven using analytic methods.   
(b) When using (extensions of) finite fields or the rational numbers as the ground field one enters the area of number theory. For example, the famous Fermat’s Last Theorem is just asking a seemingly simple question about a variety $\{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) \in \mathbb { Q } ^ { 3 } : x _ { 1 } ^ { n } + x _ { 2 } ^ { n } = x _ { 3 } ^ { n } \}$ over the rationals,

namely for which $n \in \mathbb { N }$ it contains any non-trivial points at all. As you probably know, the proof of the fact that there are no such non-trivial points for $n \geq 3$ is very complicated — but even if this type of question is very different from the questions that we would usually ask for real or complex varieties, the proof uses many concepts and techniques from the theory of algebraic geometry.

With this many relations to other fields of mathematics, it is obvious that we have to restrict our attention in this class to a rather small subset of the possible questions and applications. As already mentioned, our focus will mainly be on algebraic methods and geometric questions. In this way, we can keep the prerequisites for this class to a minimum, requiring except for the “Plane Algebraic Curves” and “Commutative Algebra” classes only a very basic topological knowledge up to the definitions and first properties of topological spaces, open and closed sets, neighborhoods, and continuous maps.

# 1. Affine Varieties

As explained in the introduction, the goal of algebraic geometry is to study solutions of polynomial equations in several variables over a fixed ground field, so we will start by making the corresponding definitions. In order to make the correspondence between geometry and algebra as clear as possible (in particular to allow for Hilbert’s Nullstellensatz in Proposition 1.10) we will restrict to the case of algebraically closed ground fields first. In particular, if we draw pictures over $\mathbb { R }$ they should always be interpreted as the real points of an underlying complex situation.

# Convention 1.1.

(a) In the following, until we introduce schemes in Chapter 12, $K$ will always denote a fixed algebraically closed ground field.   
(b) Rings are always assumed to be commutative with a multiplicative unit 1. If $J$ is an ideal in a ring $R$ we will write this as $J \triangleleft R$ , and denote the radical of $J$ by ${ \sqrt { J } } : = \{ f \in R : f ^ { k } \in J { \mathrm { ~ f o r ~ s o m e ~ } } k \in \mathbb { N } \} .$ The ideal generated by a subset $s$ of a ring will be written as $\langle S \rangle$ .   
(c) As usual, we will denote the polynomial ring in $n$ variables $x _ { 1 } , \ldots , x _ { n }$ over $K$ by $K [ x _ { 1 } , \ldots , x _ { n } ]$ , and the value of a polynomial $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ at a point $a = ( a _ { 1 } , \dots , a _ { n } ) \in K ^ { n }$ by $f ( a )$ . If there is no risk of confusion we will often denote a point in $K ^ { n }$ by the same letter $x$ as we used for the formal variables, writing $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ for the polynomial and $f ( x )$ for its value at a point $x \in K ^ { n }$ . The degree of a non-zero polynomial $f$ is always meant to be its total degree, i. e. the biggest integer $d \in \mathbb { N }$ such that $f$ contains a non-zero monomial $x _ { 1 } ^ { i _ { 1 } } \cdot \cdot \cdot x _ { n } ^ { i _ { n } }$ with $i _ { 1 } + \cdots + i _ { n } = d$ .

Definition 1.2 (Affine varieties).

(a) We call

$$
{ \mathbb { A } } ^ { n } : = { \mathbb { A } } _ { K } ^ { n } : = \{ ( a _ { 1 } , \ldots , a _ { n } ) : a _ { i } \in K { \mathrm { ~ f o r ~ } } i = 1 , \ldots , n \}
$$

the affine $n$ -space over $K$

Note that $\mathbb { A } _ { K } ^ { n }$ is just $K ^ { n }$ as a set. It is customary to use two different notations here since $K ^ { n }$ is also a $K$ -vector space and a ring. We will usually use the notation $\mathbb { A } _ { K } ^ { n }$ if we want to ignore these additional structures: For example, addition and scalar multiplication are defined on $K ^ { n }$ , but not on $\mathbb { A } _ { K } ^ { n }$ . The affine space $\mathbb { A } _ { K } ^ { n }$ will be the ambient space for our zero loci of polynomials below.

(b) For a subset $S \subset K [ x _ { 1 } , \ldots , x _ { n } ]$ of polynomials we call

$$
V ( S ) : = \{ x \in \mathbb { A } ^ { n } : f ( x ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } f \in S \} \quad \subset \mathbb { A } ^ { n }
$$

the (affine) zero locus of S. Subsets of $\mathbb { A } ^ { n }$ of this form are called (affine) varieties. If $S = \{ f _ { 1 } , \ldots , f _ { k } \}$ is a finite set, we will write $V ( S ) = V ( \{ f _ { 1 } , \dots , f _ { k } \} )$ also as $V ( f _ { 1 } , \ldots , f _ { k } )$ .

Remark 1.3. Some authors refer to zero loci of polynomials in $\mathbb { A } ^ { n }$ as in Definition 1.2 (b) as (affine) algebraic sets, reserving the name “affine variety” for such zero loci that are in addition irreducible (a concept that we will introduce in Definition 2.5 (a)).

Lemma 1.4. Let $X$ be an affine variety.

(a) For any $S _ { 1 } \subset S _ { 2 } \subset K [ x _ { 1 } , \ldots , x _ { n } ]$ we have $V ( S _ { 1 } ) \supset V ( S _ { 2 } )$ .   
(b) For any $S _ { 1 } , S _ { 2 } \subset K [ x _ { 1 } , \dotsc , x _ { n } ]$ we have $V ( S _ { 1 } ) \cup V ( S _ { 2 } ) = V ( S _ { 1 } S _ { 2 } )$ , where as usual we set $S _ { 1 } S _ { 2 } : = \{ f g : f \in S _ { 1 } , g \in S _ { 2 } \}$ .

(c) If J is any index set and $S _ { i } \subset K [ x _ { 1 } , \dotsc , x _ { n } ]$ for all $i \in J$ then $\begin{array} { r } { \bigcap _ { i \in J } V ( S _ { i } ) = V ( \bigcup _ { i \in J } S _ { i } ) } \end{array}$ .

In particular, finite unions and arbitrary intersections of affine varieties are again affine varieties.

# Proof.

(a) If $x \in V ( S _ { 2 } )$ , i. e. $f ( x ) = 0$ for all $f \in S _ { 2 }$ , then in particular $f ( x ) = 0$ for all $f \in S _ { 1 }$ , and hence $x \in V ( S _ { 1 } )$ .   
(b) $^ { 6 } \subset { \mathcal { } }$ ” If $x \in V ( S _ { 1 } ) \cup V ( S _ { 2 } )$ then $f ( x ) = 0$ for all $f \in S _ { 1 }$ or $g ( x ) = 0$ for all $g \in S _ { 2 }$ . In any case this means that $( f g ) ( x ) = 0$ for all $f \in S _ { 1 }$ and $g \in S _ { 2 }$ , i. e. that $x \in V ( S _ { 1 } S _ { 2 } )$ . “ $\Bumpeq$ ” If $x \not \in V ( S _ { 1 } ) \cup V ( S _ { 2 } )$ , i. e. $x \notin V ( S _ { 1 } )$ and $x \notin V ( S _ { 2 } )$ , then there are $f \in S _ { 1 }$ and $g \in S _ { 2 }$ with $f ( x ) \neq 0$ and $g ( x ) \neq 0$ . Then $( f g ) ( x ) \neq 0$ , and hence $x \not \in V ( S _ { 1 } S _ { 2 } )$ .

(c) We have $\textstyle x \in \bigcap _ { i \in J } V ( S _ { i } )$ if and only if $f ( x ) = 0$ for all $f \in S _ { i }$ for all $i \in J$ , which is the case if and only if $x \in V ( \textstyle \bigcup _ { i \in J } S _ { i } )$ . 

Example 1.5. Some simple examples of affine varieties are:

(a) The affine $n$ -space itself is an affine variety, since $\mathbb { A } ^ { n } = V ( 0 )$ . Similarly, the empty set $\varnothing = V ( 1 )$ is an affine variety.   
(b) Any point in $a = ( a _ { 1 } , \ldots , a _ { n } ) \in \mathbb { A } ^ { n }$ is an affine variety, since $\{ a \} = V ( x _ { 1 } - a _ { 1 } , \ldots , x _ { n } - a _ { n } )$ . By Lemma 1.4 (b), finite subsets of $\mathbb { A } ^ { n }$ are then affine varieties as well. In the special case of $\mathbb { A } ^ { 1 }$ , note that the zero locus of any non-zero polynomial in $K [ x _ { 1 } ]$ is already finite. Hence the affine varieties in $\mathbb { A } ^ { 1 }$ are exactly $\mathbb { A } ^ { 1 }$ itself and all finite sets.   
(c) Linear subspaces of $\mathbb { A } ^ { n } = K ^ { n }$ are affine varieties.   
(d) If $X \subset \mathbb { A } ^ { n }$ and $Y \subset \mathbb { A } ^ { m }$ are affine varieties then so is the product ${ X \times Y } \subset \mathbb { A } ^ { n } \times \mathbb { A } ^ { m } = \mathbb { A } ^ { n + m }$ .

Remark 1.6 (Affine varieties are zero loci of ideals). Let $f$ and $g$ be polynomials that vanish on a certain subset $X \subset \mathbb { A } ^ { n }$ . Then $f + g$ and $h f$ for any polynomial $h$ clearly vanish on $X$ as well. This means that the set $S \subset K [ x _ { 1 } , \ldots , x _ { n } ]$ defining an affine variety $X = V ( S )$ is certainly not unique: For any $f , g \in S$ and any polynomial $h$ we can add $f + g$ and $h f$ to $s$ without changing its zero locus, so that we always have $V ( \left. S \right. ) = V ( S )$ . In particular, any affine variety in $\mathbb { A } ^ { n }$ can be written as the zero locus of an ideal in $K [ x _ { 1 } , \ldots , x _ { n } ]$ .

As any ideal in $K [ x _ { 1 } , \ldots , x _ { n } ]$ is finitely generated by Hilbert’s Basis Theorem [G3, Proposition 7.13 and Remark 7.15], this means moreover that any affine variety can be written as the zero locus of finitely many polynomials.

By Remark 1.6 we often can (and will) restrict our attention to zero loci of ideals. Let us therefore reformulate the results of Lemma 1.4 in terms of standard ideal-theoretic operations.

Lemma 1.7 (Properties of $V ( \cdot ) )$ . For any ideals $J , J _ { 1 } , J _ { 2 }$ in $K [ x _ { 1 } , \ldots , x _ { n } ]$ we have

(a) $V ( \sqrt { J } ) = V ( J )$ ;   
(b) $V ( J _ { 1 } ) \cup V ( J _ { 2 } ) = V ( J _ { 1 } J _ { 2 } ) = V ( J _ { 1 } \cap J _ { 2 } ) ;$ ;   
(c) $V ( J _ { 1 } ) \cap V ( J _ { 2 } ) = V ( J _ { 1 } + J _ { 2 } )$ .

# Proof.

(a) The inclusion “ $\subset$ ” follows directly from Lemma 1.4 (a) since √ $\sqrt { J } \supset J$ . For the other inclusion assume that $x \in V ( J )$ and $f \in { \sqrt { J } }$ . Then √ $f ^ { k } \in J$ for some $k \in \mathbb N$ , so that $f ^ { k } ( x ) = 0$ , and hence also $f ( x ) = 0$ . This means that $x \in V ( { \sqrt { J } } )$ .

(b) The first equation is just a reformulation of Lemma 1.4 (b), the second then follows from (a) since ${ \sqrt { J _ { 1 } J _ { 2 } } } = { \sqrt { J _ { 1 } \cap J _ { 2 } } }$ [G3, Lemma 1.7 (b)].

(c) This follows from Lemma 1.4 (c) together with Remark 1.6 since $J _ { 1 } + J _ { 2 }$ is just the ideal generated by $J _ { 1 } \cup J _ { 2 }$ . 

Remark 1.6 is important since it is in some sense the basis of algebraic geometry: It relates geometric objects (affine varieties) to algebraic objects (ideals). In fact, it will be the main goal of this first chapter to study this correspondence in detail. We have already assigned affine varieties to ideals in Definition 1.2 (b) and Remark 1.6, so let us now introduce an operation that does the opposite job.

Definition 1.8 (Ideal of a subset of $\mathbb { A } ^ { n }$ ). Let $X \subset \mathbb { A } ^ { n }$ be any subset. Then

$$
I ( X ) : = \{ f \in K [ x _ { 1 } , \ldots , x _ { n } ] : f ( x ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } x \in X \}
$$

is called the ideal of $X$ (note that this is indeed an ideal by Remark 1.6).

# Remark 1.9.

(a) In analogy to Lemma 1.4 (a), it is obvious that the ideal of a subset reverses inclusions as well: If $X _ { 1 } \subset X _ { 2 } \subset \mathbb { A } ^ { n }$ then $I ( X _ { 1 } ) \supset I ( X _ { 2 } )$ .   
(b) Note that $I ( X )$ is always a radical ideal: If $f ^ { k } \in I ( X )$ for some $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ and $k \in \mathbb N$ , then $f ^ { k } ( x ) = 0$ for all $x \in X$ , hence $f ( x ) = 0$ for all $x \in X$ , and thus $f \in I ( X )$ .

Hence, the operation $I ( \cdot )$ of Definition 1.8 maps an affine variety to a radical ideal, and the operation $V ( \cdot )$ of Definition 1.2 (b) can map a radical ideal back to an affine variety. It is a central result of commutative algebra that this is actually a bijection. Let us briefly recall this result, which even in the English literature is usually referred to by its German name as Hilbert’s Nullstellensatz (“theorem of the zeros”).

# Proposition 1.10 (Hilbert’s Nullstellensatz).

(a) For any affine variety $X \subset \mathbb { A } ^ { n }$ we have $V ( I ( X ) ) = X$ .   
(b) For any ideal $J \triangleleft K [ x _ { 1 } , \ldots , x _ { n } ]$ we have $I ( V ( J ) ) = \sqrt { J }$ .

In particular, there is an inclusion-reversing bijection

$$
\begin{array} { r c l } { { \{ a f f u e \nu a r i e t i e s i n \mathbb { A } ^ { n } \} } } & { { \stackrel { \cdot \cdot \cdot 1 } { \longleftrightarrow } } } & { { \{ r a d i c a l i d e a l s i n K [ x _ { 1 } , \ldots , x _ { n } ] \} } } \\ { { X } } & { { \longmapsto } } & { { I ( X ) } } \\ { { V ( J ) } } & { { \longleftarrow } } & { { J . } } \end{array}
$$

Proof. Three of the four inclusions of (a) and (b) are actually easy:

(a) “ $\cdot \supset ^ { \cdot }$ ”: If $x \in X$ then $f ( x ) = 0$ for all $f \in I ( X )$ , and hence $x \in V ( I ( X ) )$ .   
(b) $\vartriangleleft$ If $f \in { \sqrt { J } }$ then $f ^ { k } \in J$ for some $k \in \mathbb N$ . It follows that $f ^ { k } ( x ) = 0$ for all $x \in V ( J )$ , hence also $f ( x ) = 0$ for all $x \in V ( J )$ , and thus $f \in I ( V ( J ) )$ .   
(a) “⊂”: As $X$ is an affine variety we know by Remark 1.6 that $X = V ( J )$ for some ideal $J$ . Then $I ( V ( J ) ) \supset \sqrt { J } \supset J$ by (b) $\cdot \bigcirc ^ { \bullet \bullet } \bigcirc ^ { \bullet \bullet }$ , so taking the zero locus we obtain $V ( I ( V ( J ) ) ) ) \subset V ( J )$ by Lemma 1.4 (a). This means exactly that $V ( I ( X ) ) \subset X$ .

Only the inclusion $I ( V ( J ) ) \subset { \sqrt { J } }$ of (b) “ $\cdot \subset '$ is hard; a proof of this result from commutative algebra can be found in [G3, Corollary 10.14]. It uses our Convention 1.1 (a) that $K$ is algebraically closed. The additional bijection statement now follows directly from (a) and (b), together with the observations that ${ \sqrt { J } } = J$ since $J$ is radical, $I ( X )$ is actually a radical ideal by Remark 1.9 (b), and both operations reverse inclusions by Lemma 1.4 (a) and Remark 1.9 (a). 

# Example 1.11.

(a) Let $J \triangleleft K [ x _ { 1 } ]$ be a non-zero ideal. As $K [ x _ { 1 } ]$ is a principal ideal domain, we have $J = \langle f \rangle$ for a polynomial $f = ( x _ { 1 } - a _ { 1 } ) ^ { k _ { 1 } } \cdots ( x _ { 1 } - a _ { r } ) ^ { k _ { r } }$ for some distinct points $a _ { 1 } , \dots , a _ { r } \in \mathbb { A } ^ { 1 }$ and $k _ { 1 } , \ldots , k _ { r } \in \mathbb { N } _ { > 0 }$ . The zero locus $V ( J ) = V ( f ) = \{ a _ { 1 } , \ldots , a _ { r } \} \subset \mathbb { A } ^ { 1 }$ then contains the data of the zeros of $f$ , but no longer of the multiplicities $k _ { 1 } , \ldots , k _ { r }$ . Consequently, by Proposition 1.10

$$
I ( V ( J ) ) = { \sqrt { J } } = \langle ( x _ { 1 } - a _ { 1 } ) \cdots ( x _ { 1 } - a _ { r } ) \rangle
$$

is just the ideal of all polynomials vanishing at $a _ { 1 } , \ldots , a _ { r }$ (with any order).

(b) If we had not assumed $K$ to be algebraically closed, the Nullstellensatz would already break down in the simple example (a): The prime (and hence radical) ideal $J = \langle x _ { 1 } ^ { 2 } + 1 \rangle \leq \mathbb { R } [ x _ { 1 } ]$ has empty zero locus in $\mathbb { A } _ { \mathbb { R } } ^ { 1 }$ , so we would obtain $I ( V ( J ) ) = I ( \emptyset ) = \mathbb { R } [ x _ { 1 } ] \neq J = \sqrt { J }$ .

(c) The ideal $J = \langle x _ { 1 } - a _ { 1 } , \ldots , x _ { n } - a _ { n } \rangle \triangleleft K [ x _ { 1 } , \ldots , x _ { n } ]$ is maximal (since $K [ x _ { 1 } , \ldots , x _ { n } ] / J \cong K$ is a field), and hence radical. As its zero locus is $V ( J ) = \{ a \}$ for $a = \left( a _ { 1 } , \ldots , a _ { n } \right)$ , we conclude by Proposition 1.10 that the ideal of the point $a$ is

$$
I ( \{ a \} ) = I ( V ( J ) ) = J = \langle x _ { 1 } - a _ { 1 } , \ldots , x _ { n } - a _ { n } \rangle .
$$

In fact, points of $\mathbb { A } ^ { n }$ are clearly just the minimal non-empty varieties in $\mathbb { A } ^ { n }$ , so by the inclusion-reversing operations of the Nullstellensatz they correspond exactly to the maximal (proper) ideals in $K [ x _ { 1 } , \ldots , x _ { n } ]$ . Hence the bijection of Proposition 1.10 restricts to a bijection

$$
\{ \mathrm { p o i n t s ~ i n ~ \mathbb { A } ^ { n } } \} \quad \stackrel { \cdot \downarrow : 1 } { \longleftrightarrow } \quad \{ \mathrm { m a x i m a l ~ i d e a l s ~ i n ~ } K [ x _ { 1 } , \ldots , x _ { n } ] \} ,
$$

so the maximal ideals considered above are actually the only maximal ideals in the polynomial ring.

First of all, Hilbert’s Nullstellensatz of Proposition 1.10 allows us to translate the properties of $V ( \cdot )$ in Lemma 1.7 to corresponding properties of the opposite operation $I ( \cdot )$ :

Lemma 1.12 (Properties of $I ( \cdot ) \rangle$ ). For any affine varieties $X _ { 1 }$ and $X _ { 2 }$ in $\mathbb { A } ^ { n }$ we have

(a) $I ( X _ { 1 } \cup X _ { 2 } ) = I ( X _ { 1 } ) \cap I ( X _ { 2 } ) ,$ ;   
(b) $I ( X _ { 1 } \cap X _ { 2 } ) = { \sqrt { I ( X _ { 1 } ) + I ( X _ { 2 } ) } } .$ .

# Proof.

(a) A polynomial $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ is contained in $I ( X _ { 1 } \cup X _ { 2 } )$ if and only if $f ( x ) = 0$ for all $x \in X _ { 1 }$ and all $x \in X _ { 2 }$ , which is the case if and only if $f \in I ( X _ { 1 } ) \cap I ( X _ { 2 } )$ .

(b) By the Nullstellensatz of Proposition 1.10 we obtain

$$
I ( X _ { 1 } \cap X _ { 2 } ) \stackrel { \scriptscriptstyle \mathrm { 1 . 1 0 } } { = } I ( V ( I ( X _ { 1 } ) ) \cap V ( I ( X _ { 2 } ) ) ) \stackrel { \scriptscriptstyle \mathrm { 1 . 7 } } { = } I ( V ( I ( X _ { 1 } ) + I ( X _ { 2 } ) ) ) \stackrel { \scriptscriptstyle \mathrm { 1 . 1 0 } } { = } \sqrt { I ( X _ { 1 } ) + I ( X _ { 2 } ) } .
$$

Remark 1.13. Recall from Remark 1.9 (b) that ideals of affine varieties are always radical. So in particular, Lemma 1.12 (a) shows that intersections of radical ideals are again radical — which could of course also be checked directly. In contrast, sums of radical ideals are in general not radical, which is why taking the radical in Lemma 1.12 (b) is really necessary.

There is also a geometric interpretation behind this fact. Consider for example the affine varieties $X _ { 1 } , X _ { 2 } \subset \mathbb { A } _ { \mathbb { C } } ^ { 2 }$ with ideals $I ( X _ { 1 } ) = \langle x _ { 2 } - x _ { 1 } ^ { 2 } \rangle$ and $I ( X _ { 2 } ) = \left. { x _ { 2 } } \right.$ whose real points are shown on the right. Their intersection $X _ { 1 } \cap X _ { 2 }$ is just the origin, with ideal $I ( X _ { 1 } \cap X _ { 2 } ) = I ( 0 ) = \langle x _ { 1 } , x _ { 2 } \rangle$ by Example 1.11 (c). But

![](images/926c4d174aab78814b94a2b5fe3cac2a2abd9332f140fc6f0cdfb29c420eeef4.jpg)

$$
I ( X _ { 1 } ) + I ( X _ { 2 } ) = \langle x _ { 2 } - x _ { 1 } ^ { 2 } , x _ { 2 } \rangle = \langle x _ { 1 } ^ { 2 } , x _ { 2 } \rangle
$$

is not a radical ideal; only its radical is equal to $I ( X _ { 1 } \cap X _ { 2 } ) = \langle x _ { 1 } , x _ { 2 } \rangle .$ .

The geometric meaning of the non-radical ideal $I ( X _ { 1 } ) + I ( X _ { 2 } ) = \langle x _ { 1 } ^ { 2 } , x _ { 2 } \rangle$ is simply that $X _ { 1 }$ and $X _ { 2 }$ are tangent at their intersection point: In a linear approximation their defining equations $x _ { 2 } = x _ { 1 } ^ { 2 }$ and $x _ { 2 } = 0$ coincide and both describe the $x _ { 1 }$ -axis. Hence we could imagine that the intersection $X _ { 1 } \cap X _ { 2 }$ extends from the origin to an infinitesimally small amount in the $x _ { 1 }$ -direction, as indicated in the picture — so that ${ } ^ { \cdot \cdot } x _ { 1 }$ does not quite vanish on the intersection (i. e. it does not lie in $I ( X _ { 1 } ) + I ( X _ { 2 } ) )$ , only $x _ { 1 } ^ { 2 }$ does”.

There are various ways to make this idea precise. In the “Plane Algebraic Curves” class, we would have said that $X _ { 1 }$ and $X _ { 2 }$ have intersection multiplicity $\dim _ { \mathbb { C } } \mathbb { C } [ x _ { 1 } , x _ { 2 } ] / \langle x _ { 1 } ^ { 2 } , x _ { 2 } \rangle = 2$ at the origin, encoding their tangential intersection numerically [G2, Chapter 2]. Here in these notes, we will instead introduce the notion of schemes in Chapter 12 that enlarges the geometric category of varieties to include “objects extending by infinitesimally small amounts in some directions”, which will then yield a statement analogous to Proposition 1.10 that affine subschemes of $\mathbb { A } ^ { n }$ are in bijection to arbitrary ideals in $K [ x _ { 1 } , \ldots , x _ { n } ]$ . In this language, the intersection of $X _ { 1 }$ and $X _ { 2 }$ will then be the scheme corresponding to the non-radical ideal $\langle x _ { 1 } ^ { 2 } , x _ { 2 } \rangle$ (see Construction 12.33).

# Remark 1.14.

(a) (Weak Nullstellensatz) Let $J \triangleleft K [ x _ { 1 } , \ldots , x _ { n } ]$ be an ideal in the polynomial ring. If $J \neq K [ x _ { 1 } , \ldots , x _ { n } ]$ then $J$ has a zero, i. e. $V ( J )$ is non-empty: Otherwise we would have ${ \sqrt { J } } = I ( V ( J ) ) = I ( \emptyset ) = K [ x _ { 1 } , \dots , x _ { n } ]$ by Proposition 1.10, which means $1 \in { \sqrt { J } }$ and gives us the contradiction $1 \in J$ . This statement is usually called the weak Nullstellensatz; it can be thought of as a generalization of the algebraic closure property that a non-constant univariate polynomial has a zero. It also explains the origin of the name “Nullstellensatz” for Proposition 1.10.

(b) Another easy consequence of Proposition 1.10 is that polynomials and polynomial functions on $\mathbb { A } ^ { n }$ agree: If $f , g \in K [ x _ { 1 } , \ldots , x _ { n } ]$ are two polynomials defining the same function on $\mathbb { A } ^ { n }$ , i. e. such that $f ( x ) = g ( x )$ for all $x \in \mathbb { A } ^ { n }$ , then

$$
f - g \in I ( \mathbb { A } ^ { n } ) = I ( V ( 0 ) ) = { \sqrt { \langle 0 \rangle } } = \langle 0 \rangle
$$

and hence $f = g$ in $K [ x _ { 1 } , \ldots , x _ { n } ]$ . So $K [ x _ { 1 } , \ldots , x _ { n } ]$ can be thought of as the ring of polynomial functions on $\mathbb { A } ^ { n }$ .

It is easy to generalize this to an affine variety $X \subset \mathbb { A } ^ { n }$ : Two polynomials $f , g \in K [ x _ { 1 } , \ldots , x _ { n } ]$ define the same polynomial function on $X$ , i. e. we have $f ( x ) = g ( x )$ for all $x \in X$ , if and only if $f - g \in I ( X )$ . So the quotient ring $K [ x _ { 1 } , \ldots , x _ { n } ] / I ( X )$ can be thought of as the ring of polynomial functions on $X$ . Let us make this into a precise definition.

Definition 1.15 (Polynomial functions and coordinate rings). Let $X \subset \mathbb { A } ^ { n }$ be an affine variety. A polynomial function on $X$ is a map $X \to K$ that is of the form $x \mapsto f ( x )$ for some $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ . By Remark 1.14 (b) the ring of all polynomial functions on $X$ is just the quotient ring

$$
A ( X ) : = K [ x _ { 1 } , \ldots , x _ { n } ] / I ( X ) .
$$

It is called the coordinate ring of the affine variety $X$ .

Remark 1.16 (Coordinate rings are $K$ -algebras). Note that the coordinate ring $A ( X )$ of an affine variety $X$ is not just a ring, but also a $K$ -algebra (i. e. it is also a $K$ -vector space such that its ring multiplication is $K$ -bilinear [G3, Definition 1.23 and Remark 1.24]). In fact, in the following we will often consider $A ( X )$ as a $K$ -algebra, despite its common name “coordinate ring” in the literature.

According to Definition 1.15, we can think of the elements of $A ( X )$ both as functions on $X$ and as elements of the quotient $K [ x _ { 1 } , \ldots , x _ { n } ] / I ( X )$ . We can therefore use coordinate rings to define the concepts introduced so far in a relative setting, i. e. consider zero loci of ideals in $A ( Y )$ and varieties contained in Y for a fixed ambient affine variety $Y$ that is not necessarily $\mathbb { A } ^ { n }$ .

Construction 1.17 (Relative version of $V ( \cdot )$ and $I ( \cdot ) )$ . Let $Y \subset \mathbb { A } ^ { n }$ be a fixed affine variety. The following two constructions are then completely analogous to those in Definitions 1.2 (b) and 1.8:

(a) For a subset $S \subset A ( Y )$ of polynomial functions on $Y$ we define its zero locus as

$$
V ( S ) : = V _ { Y } ( S ) : = \left\{ x \in Y : f ( x ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } f \in S \right\} \quad \subset Y .
$$

The subsets that are of this form are obviously precisely the affine varieties contained in $X$ .   
They are called affine subvarieties of $Y$ .

(b) For a subset $X \subset Y$ the ideal of $X$ in $Y$ is defined to be

$$
I ( X ) : = I _ { Y } ( X ) : = \{ f \in A ( Y ) : f ( x ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } x \in X \} \quad \leq A ( Y ) .
$$

Remark 1.18. Let $Y$ be an affine variety. With essentially the same arguments as before, all results considered in this chapter then hold in the relative setting of Construction 1.17 as well. Let us summarize them here again:

(a) In the same way as in Remark 1.14 (b) we see that $A ( X ) \cong A ( Y ) / I _ { Y } ( X )$ for any affine subvariety $X$ of $Y$ .   
(b) (Relative Nullstellensatz) As in Proposition 1.10, we have √ $V _ { Y } ( I _ { Y } ( X ) ) = X$ for any affine subvariety $X$ of $Y$ and $I _ { Y } ( V _ { Y } ( J ) ) = \sqrt { J }$ for any ideal $J { \triangleleft ( Y ) }$ , giving rise to a bijection $\{ { \mathrm { a f f i n e ~ s u b v a r i e t i e s ~ o f ~ } } Y \} \quad \stackrel { \cdot \cdot \cdot } { \longleftrightarrow } \quad \{ \mathrm { r a d i c a l ~ i d e a l s ~ i n ~ }  A ( Y ) \} .$ A possible way to derive this from the absolute version is presented in Exercise 1.23.   
(c) (Relative properties of $V ( \cdot )$ and $I ( \cdot )$ ) With the same proofs, the properties of $V ( \cdot )$ of Lemma 1.7 and the properties of $I ( \cdot )$ of Lemma 1.12 hold in the relative setting for ideals of $A ( Y )$ resp. affine subvarieties of $Y$ as well.

Exercise 1.19. Prove that every affine variety $X \subset \mathbb { A } ^ { n }$ consisting of only finitely many points can be written as the zero locus of $n$ polynomials.

(Hint: Use interpolation. It is useful to assume first that all points in $X$ have different $x _ { 1 }$ -coordinates.)

Exercise 1.20. Let $X$ be an affine variety. Show that the coordinate ring $A ( X )$ is a field if and only if $X$ is a single point.

Exercise 1.21. Determine the radical of the ideal $\langle x _ { 1 } ^ { 3 } - x _ { 2 } ^ { 6 } , x _ { 1 } x _ { 2 } - x _ { 2 } ^ { 3 } \rangle \triangleleft { \mathbb { C } } [ x _ { 1 } , x _ { 2 } ] .$ .

(Hint: Hilbert’s Nullstellensatz may be useful here.)

Exercise 1.22. Let $X \subset \mathbb { A } ^ { 3 }$ be the union of the three coordinate axes. Compute generators for the ideal $I ( X )$ , and show that $I ( X )$ cannot be generated by fewer than three elements.

Exercise 1.23 (Relative Nullstellensatz, see Remark 1.18 (b)). Let $Y \subset \mathbb { A } ^ { n }$ be an affine variety, and denote by $\pi \colon K [ x _ { 1 } , \ldots , x _ { n } ] \to K [ x _ { 1 } , \ldots , x _ { n } ] / I ( Y ) = A ( Y )$ the quotient map.

(a) Show that $V _ { Y } ( J ) = V ( \pi ^ { - 1 } ( J ) )$ for every ideal $J$ in $A ( Y )$ .   
(b) Show that $\pi ^ { - 1 } ( I _ { Y } ( X ) ) = I ( X )$ for every affine subvariety $X$ of $Y$ .   
(c) Use (a) and (b) to deduce the (interesting part of the) relative Nullstellensatz $I _ { Y } ( V _ { Y } ( J ) ) \subset \sqrt { J }$ for every ideal $J { \triangleleft { A ( Y ) } }$ from the corresponding absolute statement $I ( V ( J ) ) \subset \sqrt { J }$ for every ideal $J \triangleleft K [ x _ { 1 } , \ldots , x _ { n } ]$ in Proposition 1.10. In particular, conclude that there is an inclusionreversing bijection between affine subvarieties of $Y$ and radical ideals in $A ( Y )$ .

# 2. The Zariski Topology

In this chapter we will define a topology on an affine variety $X$ , i. e. a notion of open and closed subsets of $X$ . We will see that many properties of $X$ can be expressed purely in terms of this topology, e. g. its dimension or the question whether it consists of several components. The advantage of this is that these concepts can then easily be reused later in Chapter 5 when we consider more general varieties — which are still topological spaces, but arise in a slightly different way.

Compared to e. g. the standard topology on subsets of real vector spaces, the properties of our topology on affine varieties will be very unusual. Consequently, most concepts and results covered in a standard introductory course on topology will be trivial or useless in our case, so that we will only need the very first definitions of general topology. Let us quickly review them here.

Remark 2.1 (Topologies). A topology on a set $X$ is given by declaring some subsets of $X$ to be closed, such that the following properties hold:

(a) the empty set $\varnothing$ and the whole space $X$ are closed;   
(b) arbitrary intersections of closed sets are closed;   
(c) finite unions of closed sets are closed.

Given such a topology on $X$ , a subset $U$ of $X$ is then called open if its complement $X \backslash U$ is closed. The closure $\overline { { A } }$ of a subset $A \subset X$ is defined to be the smallest closed subset containing $A$ , or more precisely the intersection of all closed subsets containing $A$ (which is closed again by (b)).

A topology on $X$ induces a subspace topology on any subset $A \subset X$ by declaring the subsets of $A$ to be closed that are of the form $A \cap Y$ for a closed subset $Y$ of $X$ (or equivalently the subsets of $A$ to be open that are of the form $A \cap U$ for an open subset $U$ of $X$ ). Subsets of topological spaces will always be equipped with this subspace topology unless stated otherwise. Note that if $A$ is closed itself then the closed subsets of $A$ in the subspace topology are exactly the closed subsets of $X$ contained in $A$ ; if $A$ is open then the open subsets of $A$ in the subspace topology are exactly the open subsets of $X$ contained in $A$ .

A map $f \colon X \to Y$ between topological spaces is called continuous if inverse images of closed subsets of $Y$ under $f$ are closed in $X$ , or equivalently if inverse images of open subsets are open.

Note that the standard definition of closed subsets in $\mathbb { R } ^ { n }$ (or more generally in metric spaces) that you know from real analysis satisfies the conditions (a), (b), and (c), and leads with the above definitions to the well-known notions of open subsets, closures, and continuous functions.

With these preparations we can now define the standard topology used in algebraic geometry.

Definition 2.2 (Zariski topology). Let $X$ be an affine variety. We define the Zariski topology on $X$ to be the topology whose closed sets are exactly the affine subvarieties of $X$ , i. e. the subsets of the form $V ( S )$ for some $S \subset A ( X )$ . Note that this in fact a topology by (the relative version of) Lemma 1.4 and Example 1.5 (a).

Unless stated otherwise, topological notions for affine varieties (and their subsets, using the subspace topology of Remark 2.1) will always be understood with respect to this topology.

Remark 2.3. Let $X \subset \mathbb { A } ^ { n }$ be an affine variety. Then we have just defined two topologies on $X$ :

(a) the Zariski topology on $X$ , whose closed subsets are the affine subvarieties of $X$ ; and (b) the subspace topology of $X$ in $\mathbb { A } ^ { n }$ , whose closed subsets are the sets of the form $X \cap Y$ , with $Y$ a variety in $\mathbb { A } ^ { n }$ .

These two topologies agree, since the affine subvarieties of $X$ are precisely the affine varieties contained in $X$ , and the intersection of two affine varieties is again an affine variety. Hence it will not lead to confusion if we consider both these topologies to be the standard topology on $X$ .

Example 2.4 (Topologies on complex varieties). Compared to the classical metric topology in the case of the ground field $\mathbb { C }$ , the Zariski topology is certainly unusual:

(a) The metric unit ball $A = \left\{ x \in \mathbb { A } _ { \mathbb { C } } ^ { 1 } : | x | \leq 1 \right\}$ in $\mathbb { A } _ { \mathbb { C } } ^ { 1 }$ is clearly closed in the classical topology, but not in the Zariski topology. In fact, by Example 1.5 (b) the Zariski-closed subsets of $\mathbb { A } ^ { 1 }$ are only the finite sets and $\mathbb { A } ^ { 1 }$ itself. In particular, the closure of $A$ in the Zariski topology is all of $\mathbb { A } ^ { 1 }$ . Intuitively, we can say that the closed subsets in the Zariski topology are very “small”, and hence that the open subsets are very “big” (see also Remark 2.16). Any Zariski-closed subset is also closed in the classical topology (since it is given by equations among polynomial functions, which are continuous in the classical topology), but as the above example shows only “very few” closed subsets in the classical topology are also Zariski-closed.   
(b) Let $f \colon \mathbb { A } ^ { 1 } \to \mathbb { A } ^ { 1 }$ be any injective map. Then $f$ is automatically continuous in the Zariski topology by Example 1.5 (b), since inverse images of finite subsets of $\mathbb { A } ^ { 1 }$ under $f$ are again finite. This statement is essentially useless however, as we will not define morphisms of affine varieties as just being continuous maps with respect to the Zariski topology. In fact, this example gives us a strong hint that we should not do so.   
(c) In general topology there is a notion of a product topology: If $X$ and $Y$ are topological spaces then $X \times Y$ has a natural structure of a topological space by saying that a subset of $X \times Y$ is open if and only if it is a union of products $U _ { i } \times V _ { i }$ for open subsets $U _ { i } \subset X$ and $V _ { i } \subset Y$ with $i$ in an arbitrary index set. With this construction, note however that the Zariski topology of an affine product variety $X \times Y$ is not the product topology: For example, the subset $V ( x _ { 1 } - x _ { 2 } ) = \{ ( a , a ) : a \in K \} \subset \mathbb { A } ^ { 2 }$ is closed in the Zariski topology, but not in the product topology of $\mathbb { A } ^ { 1 } \times \mathbb { A } ^ { 1 }$ . In fact, we will see in Proposition 4.10 that the Zariski topology is the “correct” one, whereas the product topology is useless in algebraic geometry.

But let us now start with the discussion of the topological concepts that are actually useful in the Zariski topology. The first ones concern components of an affine variety: The affine variety $X = V ( x _ { 1 } x _ { 2 } ) \subset \mathbb { A } ^ { 2 }$ as in the picture on the right can be written as the union of the two coordinate axes $X _ { 1 } = V ( x _ { 1 } )$ and $X _ { 2 } = V ( x _ { 2 } )$ , which are themselves affine varieties. However, $X _ { 1 }$ and $X _ { 2 }$ cannot be decomposed further into finite unions of smaller affine varieties. The following notion generalizes this idea.

![](images/d5dad74ec2f6d77c4bf6041840d0809e5a457b7b342d3bae0122d84941ce8a0b.jpg)

Definition 2.5 (Irreducible and connected spaces). Let $X$ be a topological space.

(a) We say that $X$ is reducible if it can be written as $X = X _ { 1 } \cup X _ { 2 }$ for closed subsets $X _ { 1 } , X _ { 2 } \subset X$ . Otherwise $X$ is called irreducible.   
(b) The space $X$ is called disconnected if it can be written as $X = X _ { 1 } \cup X _ { 2 }$ for closed subsets $X _ { 1 } , X _ { 2 } \subset X$ with $X _ { 1 } \cap X _ { 2 } = \emptyset$ . Otherwise $X$ is called connected.

Remark 2.6. Although we have given this definition for arbitrary topological spaces, we will usually want to apply the notion of irreducibility only in the Zariski topology. For example, in the classical topology, the complex plane $\mathbb { A } _ { \mathbb { C } } ^ { 1 }$ is reducible because it can be written as a union of closed subsets e. g. as

$$
\mathbb { A } _ { \mathbb { C } } ^ { 1 } = \{ x \in \mathbb { C } : | x | \leq 1 \} \cup \{ x \in \mathbb { C } : | x | \geq 1 \} .
$$

In the Zariski topology however, $\mathbb { A } ^ { 1 }$ is irreducible by Example 1.5 (b) (as it should be).

In contrast, the notion of connectedness can be used in the “usual” topology as well and does mean there what you think it should mean.

In the Zariski topology, the algebraic characterization of irreducibility and connectedness is the following.

Proposition 2.7. Let $X$ be a disconnected affine variety, with $X = X _ { 1 } \cup X _ { 2 }$ for two disjoint closed subsets $X _ { 1 } , X _ { 2 } \subset X$ . Then $A ( X ) \cong A ( X _ { 1 } ) \times A ( X _ { 2 } )$ .

Proof. As $X _ { 1 } \cup X _ { 2 } = X$ we obtain in $A ( X )$

$$
I ( X _ { 1 } ) \cap I ( X _ { 2 } ) \stackrel { 1 . 1 8 } { = } I ( X _ { 1 } \cup X _ { 2 } ) = I ( X ) = \{ 0 \} .
$$

On the other hand, from $X _ { 1 } \cap X _ { 2 } = \emptyset$ we have in $A ( X )$

$$
{ \sqrt { I ( X _ { 1 } ) + I ( X _ { 2 } ) } } \mathrel { \stackrel { 1 . 1 8 } { = } } \mathrm { { } } ^ { ( \mathrm { c } ) } I ( X _ { 1 } \cap X _ { 2 } ) = I ( \emptyset ) = \langle 1 \rangle ,
$$

and thus also $I ( X _ { 1 } ) + I ( X _ { 2 } ) = \langle 1 \rangle$ . So by the Chinese Remainder Theorem [G3, Proposition 1.14] we conclude that

$$
A ( X ) \cong A ( X ) / I ( X _ { 1 } ) \times A ( X ) / I ( X _ { 2 } ) ,
$$

which by Remark 1.18 (a) is exactly the statement of the proposition.

Proposition 2.8. An affine variety $X$ is irreducible if and only $i f A ( X )$ is an integral domain.

# Proof.

$\ " \Rightarrow \ "$ : Assume that $A ( X )$ is not an integral domain, i. e. there are non-zero $f _ { 1 } , f _ { 2 } \in A ( X )$ such that $f _ { 1 } f _ { 2 } = 0$ . Then $X _ { 1 } = V ( f _ { 1 } )$ and $X _ { 2 } = V \big ( f _ { 2 } \big )$ are closed, not equal to $X$ (since $f _ { 1 }$ and $f _ { 2 }$ are non-zero), and $X _ { 1 } \cup X _ { 2 } = V ( f _ { 1 } ) \cup V ( f _ { 2 } ) = V ( f _ { 1 } f _ { 2 } ) = V ( 0 ) = X$ . Hence $X$ is reducible.

$" \Leftarrow 2 ^ { , 3 }$ : Assume that $X$ is reducible, with $X = X _ { 1 } \cup X _ { 2 }$ for closed subsets $X _ { 1 } , X _ { 2 } \subset X$ . By the bijection of the relative Nullstellensatz as in Remark 1.18 (b) this means that $I ( X _ { i } ) \neq \{ 0 \}$ in $A ( X )$ for $i = 1 , 2$ , and so we can choose non-zero $f _ { i } \in I ( X _ { i } )$ . Then $f _ { 1 } f _ { 2 }$ vanishes on $X _ { 1 } \cup X _ { 2 } = X$ . Hence $f _ { 1 } f _ { 2 } = 0 \in A ( X )$ , i. e. $A ( X )$ is not an integral domain. 

Remark 2.9 (Irreducible subvarieties prime ideals). Let $Y$ be an affine variety. By Remark 1.18 (a) we have $A ( X ) \cong A ( Y ) / I _ { Y } ( X )$ for any non-empty affine subvariety $X$ of $Y$ , and this ring is an integral domain if and only if $I _ { Y } ( X )$ is a prime ideal. Hence, by Proposition 2.8 the bijection of the relative Nullstellensatz of Remark 1.18 (b) restricts to a bijection

$$
\{ \mathrm { n o n - e m p t y ~ i r r e d u c i b l e ~ a f f i n e ~ s u b v a r i e t i e s ~ o f } Y \} \quad \stackrel { \cdot 1 : 1 } { \longleftrightarrow } \quad \{ \mathrm { p r i m e ~ i d e a l s ~ i n } A ( Y ) \}
$$

for any affine variety $Y$ .

# Example 2.10.

(a) A finite affine variety is irreducible if and only if it is connected: namely if and only if it contains at most one point.   
(b) Any irreducible space is connected.   
(c) The affine space $\mathbb { A } ^ { n }$ is irreducible (and thus connected) by Proposition 2.8 since its coordinate ring $A ( \mathbb { A } ^ { n } ) = K [ x _ { 1 } , \ldots , x _ { n } ]$ is an integral domain. More generally, this holds for any affine variety given by linear equations, since again its coordinate ring is isomorphic to a polynomial ring.   
(d) The union $X = V ( x _ { 1 } x _ { 2 } ) \subset \mathbb { A } ^ { 2 }$ of the two coordinate axes $X _ { 1 } = V ( x _ { 1 } )$ and $X _ { 2 } = V ( x _ { 2 } )$ is not irreducible, since $X = X _ { 1 } \cup X _ { 2 }$ . But $X _ { 1 }$ and $X _ { 2 }$ themselves are irreducible by (c). Hence we have decomposed $X$ into a union of two irreducible spaces.

As already announced, we now want to see that such a decomposition into finitely many irreducible spaces is possible for any affine variety. In fact, this works for a much larger class of topological spaces, the so-called Noetherian spaces:

Definition 2.11 (Noetherian topological spaces). A topological space $X$ is called Noetherian if there is no infinite strictly decreasing chain

$$
X _ { 0 } \supsetneq X _ { 1 } \supset X _ { 2 } \supset \cdots
$$

of closed subsets of $X$ .

Lemma 2.12. Any affine variety is a Noetherian topological space.

Proof. Let $X$ be an affine variety. By the relative Nullstellensatz of Remark 1.18 (b) an infinite decreasing chain $X _ { 0 } \supsetneq X _ { 1 } \supset X _ { 2 } \supset \cdots$ of affine subvarieties of $X$ would give rise to an infinite increasing chain $I ( X _ { 0 } ) \subsetneq I ( X _ { 1 } ) \subsetneq \cdots$ of ideals in $A ( X )$ , which does not exist since $A ( X )$ is Noetherian [G3, Corollary 7.14]. Hence $X$ is a Noetherian topological space. 

Remark 2.13 (Subspaces of Noetherian spaces are Noetherian). Let $A$ be a subset of a Noetherian topological space $X$ . Then $A$ is also Noetherian: Otherwise we would have an infinite strictly descending chain of closed subsets of $A$ , which by definition of the subspace topology we can write as

$$
A \cap X _ { 0 } \supsetneq A \cap X _ { 1 } \supset A \cap X _ { 2 } \supset \cdots
$$

for closed subsets $X _ { 0 } , X _ { 1 } , X _ { 2 } , \dots$ of $X$ . Then

$$
X _ { 0 } \supset X _ { 0 } \cap X _ { 1 } \supset X _ { 0 } \cap X _ { 1 } \cap X _ { 2 } \supset \cdots
$$

is a decreasing chain of closed subsets of $X$ . In fact, in contradiction to our assumption it is also strictly decreasing, since $X _ { 0 } \cap \cdots \cap X _ { k } = X _ { 0 } \cap \cdots \cap X _ { k + 1 }$ for some $k \in \mathbb { N }$ would imply $A \cap X _ { k } = A \cap X _ { k + 1 }$ by intersecting with $A$ .

Combining Lemma 2.12 with Remark 2.13 we therefore see that any subset of an affine variety is a Noetherian topological space. In fact, all topological spaces occurring in this class will be Noetherian, and thus we can safely restrict our attention to this class of spaces.

Proposition 2.14 (Irreducible decomposition of Noetherian spaces). Every Noetherian topological space $X$ can be written as a finite union $X = X _ { 1 } \cup \cdots \cup X _ { r }$ of irreducible closed subsets. If one assumes that $X _ { i } \not \subset X _ { j }$ for all $i \neq j$ , then $X _ { 1 } , \ldots , X _ { r }$ are unique (up to permutation). They are called the irreducible components of $X$ .

Proof. To prove existence, assume that there is a topological space $X$ for which the statement is false. In particular, $X$ is reducible, hence $X = X _ { 1 } \cup X _ { 1 } ^ { \prime }$ as in Definition 2.5 (a). Moreover, the statement of the proposition must be false for at least one of these two subsets, say $X _ { 1 }$ . Continuing this construction, one arrives at an infinite chain $X \ni X _ { 1 } \supset X _ { 2 } \supset \cdots$ of closed subsets, which is a contradiction as $X$ is Noetherian.

To show uniqueness, assume that we have two decompositions

$$
X = X _ { 1 } \cup \cdots \cup X _ { r } = X _ { 1 } ^ { \prime } \cup \cdots \cup X _ { s } ^ { \prime } .
$$

Then for any fixed $i \in \{ 1 , \ldots , r \}$ we have $X _ { i } \subset \cup _ { j } X _ { j } ^ { \prime }$ , so $X _ { i } = \cup _ { j } ( X _ { i } \cap X _ { j } ^ { \prime } )$ . But $X _ { i }$ is irreducible, and so we must have $X _ { i } = X _ { i } \cap X _ { j } ^ { \prime }$ , i. e. $X _ { i } \subset X _ { j } ^ { \prime }$ for some $j$ . In the same way we conclude that $X _ { j } ^ { \prime } \subset X _ { k }$ for some $k$ , so that $X _ { i } \subset X _ { j } ^ { \prime } \subset X _ { k }$ . By assumption this is only possible for $i = k$ , and consequently $X _ { i } = X _ { j } ^ { \prime }$ . Hence every set appearing on the left side of $( \ast )$ also appears on the right side (and vice versa), which means that the two decompositions agree. 

Remark 2.15 (Irreducible decomposition of affine varieties). The irreducible decomposition of an affine variety $X \subset \mathbb { A } ^ { n }$ can be computed from the primary decomposition of its ideal: If

$$
\begin{array} { r l } { I ( X ) = Q _ { 1 } \cap \cdots \cap Q _ { r } } & { { } \preceq K [ x _ { 1 } , \ldots , x _ { n } ] } \end{array}
$$

is a primary decomposition of $I ( X )$ with primary ideals $Q _ { 1 } , \ldots , Q _ { r }$ as in [G3, Chapter 8], we obtain by Hilbert’s Nullstellensatz

$$
X = V ( I ( X ) ) \stackrel { 1 . 7 ( \mathfrak { b } ) } { = } V ( Q _ { 1 } ) \cup \cdots \cup V ( Q _ { r } ) \stackrel { 1 . 7 ( \mathfrak { a } ) } { = } V ( P _ { 1 } ) \cup \cdots \cup V ( P _ { r } )
$$

for the prime ideals $P _ { i } = \sqrt { Q _ { i } }$ for $i = 1 , \ldots , r .$ Note that all varieties $V ( P _ { i } )$ in this union are irreducible by Remark 2.9. So keeping only the minimal prime ideals, i. e. the maximal varieties, among them, we obtain the irreducible decomposition of $X$ as in Proposition 2.14. Note that they correspond exactly to the minimal prime ideals in $A ( X )$ , so that we obtain the following additional bijection from the relative Nullstellensatz of Remark 1.18 (b):

$$
\{ { \mathrm { i r r e d u c i b l e ~ c o m p o n e n t s ~ o f } } X \} \quad \longleftrightarrow \quad \{ { \mathrm { m i n i m a l ~ p r i m e ~ i d e a l s ~ i n } } A ( X ) \} .
$$

Remark 2.16 (Open subsets of irreducible spaces are dense). We have already seen in Example 2.4 (a) that open subsets tend to be very “big” in the Zariski topology. Here are two precise statements along these lines. Let $X$ be an irreducible topological space, and let $U$ and $U ^ { \prime }$ be non-empty open subsets of $X$ . Then:

(a) The intersection $U \cap U ^ { \prime }$ is never empty. In fact, by taking complements this is just equivalent to saying that the union of the two proper closed subsets $X \backslash U$ and $X \backslash U ^ { \prime }$ is not equal to $X$ , i. e. to the definition of irreducibility.   
(b) The closure $\overline { U }$ of $U$ is all of $X$ — one says that $U$ is dense in $X$ . This is easily seen: If $Y \subset X$ is any closed subset containing $U$ then $X = Y \cup ( X \backslash U )$ , and since $X$ is irreducible and $X \backslash U \neq X$ we must have $Y = X$ .

Exercise 2.17. Find the irreducible components of the affine variety $V ( x _ { 1 } - x _ { 2 } x _ { 3 } , x _ { 1 } x _ { 3 } - x _ { 2 } ^ { 2 } ) \subset \mathbb { A } _ { \mathbb { C } } ^ { 3 }$

Exercise 2.18. Let $X \subset \mathbb { A } ^ { n }$ be an arbitrary subset. Prove that $V ( I ( X ) ) = { \overline { { X } } }$ .

Exercise 2.19. Let $X$ be a topological space.

(a) If $X$ is Noetherian show that we can write it as a finite disjoint union $X = X _ { 1 } \cup \cdots \cup X _ { r }$ of non-empty connected closed subsets of $X$ , and that this decomposition is unique up to permutation. We call $X _ { 1 } , \ldots , X _ { r }$ the connected components of $X$ .   
(b) Let $X _ { 1 } , \ldots , X _ { r }$ be any subsets of $X$ with $X = X _ { 1 } \cup \cdots \cup X _ { r }$ . If all $X _ { 1 } , \ldots , X _ { r }$ are Noetherian, prove that $X$ is Noetherian as well.

Exercise 2.20. Let $A$ be a subset of a topological space $X$ . Prove:

(a) If $Y \subset A$ is closed in the subspace topology of $A$ then ${ \overline { { Y } } } \cap A = Y$ .   
(b) $A$ is irreducible if and only if $\overline { { A } }$ is irreducible.

Exercise 2.21. Let $\{ U _ { i } : i \in I \}$ be an open cover of a topological space $X$ , and assume that $U _ { i } \cap U _ { j } \neq \emptyset$ for all $i , j \in I$ . Show:

(a) If $U _ { i }$ is connected for all $i \in I$ then $X$ is connected.   
(b) If $U _ { i }$ is irreducible for all $i \in I$ then $X$ is irreducible.

Exercise 2.22. Let $f \colon X \to Y$ be a continuous map of topological spaces. Prove:

(a) If $X$ is connected then so is $f ( X )$ .   
(b) If $X$ is irreducible then so is $f ( X )$ .

Exercise 2.23. Recall that for two ideals $J _ { 1 }$ and $J _ { 2 }$ in a ring $R$ the ideal quotient is defined by

$$
J _ { 1 } : J _ { 2 } = \{ f \in R : f J _ { 2 } \subset J _ { 1 } \} .
$$

Show that ideal quotients correspond to differences of varieties in the following sense: If $X$ is an affine variety and . . .

(a) $Y _ { 1 }$ and $Y _ { 2 }$ are subvarieties of $X$ then $I ( \overline { { Y _ { 1 } \backslash Y _ { 2 } } } ) = I ( Y _ { 1 } ) : I ( Y _ { 2 } )$ in $A ( X )$ (b) $J _ { 1 }$ and $J _ { 2 }$ are radical ideals in $A ( X )$ then $\overline { { { V ( J _ { 1 } ) \backslash V ( J _ { 2 } ) } } } = V ( J _ { 1 } : J _ { 2 } )$ .

Exercise 2.24. Let $X \subset \mathbb { A } ^ { n }$ and $Y \subset \mathbb { A } ^ { m }$ be irreducible affine varieties. Prove that their product ${ X \times Y } \subset \mathbb { A } ^ { n + m }$ is irreducible as well.

An important application of the notion of irreducibility is the definition of the dimension of an affine variety (or more generally of a topological space — but as with our other concepts above you will only want to apply it to the Zariski topology). Of course, at least in the case of complex varieties we have a geometric idea what the dimension of an affine variety should be: the number of coordinates that you need to describe $X$ locally around any point. Although there are algebraic definitions of dimension that mimic this intuitive one [G3, Proposition 11.31], the standard definition of dimension that we will give here uses only the language of topological spaces. Its idea is simply that, if $X$ is an irreducible topological space, then any closed subset of $X$ not equal to $X$ should have smaller dimension. The resulting definition is the following.

Definition 2.25 (Dimension and codimension). Let $X$ be a non-empty topological space.

(a) The dimension $\mathrm { d i m } X \in \mathbb { N } \cup \{ \infty \}$ is the supremum over all $n \in \mathbb { N }$ such that there is a chai

$$
\emptyset \neq Y _ { 0 } \subsetneq Y _ { 1 } \subsetneq \cdots \subsetneq Y _ { n } \subset X
$$

of length $n$ of irreducible closed subsets $Y _ { 1 } , \dots , Y _ { n }$ of $X$ .

(b) If $Y \subset X$ is a non-empty irreducible closed subset of $X$ the codimension codimX $Y$ of $Y$ in $X$ is again the supremum over all $n$ such that there is a chain

$$
Y \subset Y _ { 0 } \subsetneq Y _ { 1 } \subsetneq \cdots \subsetneq Y _ { n } \subset X
$$

of irreducible closed subsets $Y _ { 1 } , \dots , Y _ { n }$ of $X$ containing $Y$ .

To avoid confusion, we will always denote the dimension of a $K$ -vector space $V$ by $\mathrm { d i m } _ { K } V$ , leaving the notation $\mathrm { d i m } X$ (without an index) for the dimension of a topological space $X$ as above.

According to the above idea, one should imagine each $Y _ { i }$ as having dimension $i$ in a maximal chain as in Definition 2.25 (a), so that finally $\mathrm { d i m } X = n$ . In the same way, each $Y _ { i }$ in Definition 2.25 (b) should have dimension $i + \dim Y$ in a maximal chain, so that $n = \dim X - \dim Y$ can be thought of as the difference of the dimensions of $X$ and $Y$ .

# Example 2.26.

(a) By Example 1.5 (b) the affine space $\mathbb { A } ^ { 1 }$ has dimension 1, since the maximal chains of nonempty irreducible closed subsets of $\mathbb { A } ^ { 1 }$ are exactly $\{ a \} \subsetneq \mathbb { A } ^ { 1 }$ for any point $a \in \mathbb { A } ^ { 1 }$ . The codimension of $\{ a \}$ in $\mathbb { A } ^ { 1 }$ is 1.   
(b) One might be tempted to think that the “finiteness condition” of a Noetherian topological space $X$ ensures that $\mathrm { d i m } X$ is always finite. This is not true however: If we equip the natural numbers $X = \mathbb { N }$ with the topology in which (except $\varnothing$ and $X$ ) exactly the subsets $Y _ { n } : = \{ 0 , \ldots , n \}$ for $n \in \mathbb { N }$ are closed, then $X$ is Noetherian, but has chains $Y _ { 0 } \subsetneq Y _ { 1 } \subsetneq \cdots \subsetneq Y _ { n }$ of non-empty irreducible closed subsets of arbitrary length.

However, for affine varieties infinite dimensions cannot occur, since in this case the notions of dimension and codimension reduce immediately to the concepts of the Krull dimension of a ring and the codimension (also called height) of a prime ideal that we know from commutative algebra [G3, Definition 11.1]:

Lemma 2.27 (Dimension and codimension of affine varieties). Let Y be a non-empty irreducible subvariety of an affine variety $X$ .

(a) The dimension dim X of X is equal to the Krull dimension of the coordinate ring $A ( X )$ .

(b) The codimension codimX $Y$ of $Y$ in $X$ is equal to the codimension of the prime ideal $I ( Y )$ in $A ( X )$ .

In particular, dimensions and codimensions of (irreducible) affine varieties are always finite.

Proof. By Remark 2.9, chains of non-empty irreducible closed subsets of $X$ (containing Y ) correspond exactly to chains of prime ideals of $A ( X )$ (contained in $I ( Y ) )$ . Hence, Definition 2.25 is directly equivalent to the definition of the Krull dimension of $A ( X )$ and the codimension of $I ( Y )$

in $A ( X )$ , respectively. By [G3, Remark 11.10], these numbers are finite since $A ( X )$ is a finitely generated $K$ -algebra. 

In fact, this correspondence allows us to transfer many results on Krull dimensions from commutative algebra immediately to statements on dimensions of affine varieties. For better reference, let us quickly recall the results that we will need in this class. We will list them only for irreducible varieties, since we will see in Remark 2.31 (a) that the general case can then easily be obtained by considering irreducible decompositions. The results are all very intuitive:

Proposition 2.28 (Properties of dimension). Let $X$ and $Y$ be non-empty irreducible affine varieties.

(a) We have $\mathrm { d i m } ( X \times Y ) = \mathrm { d i m } X + \mathrm { d i m } Y$ . In particular, $\dim \mathbb { A } ^ { n } = n$ .   
(b) If $Y \subset X$ we have $\mathrm { d i m } X = \mathrm { d i m } Y + \mathrm { c o d i m } _ { X } Y$ . In particular, cod $\operatorname { i m } _ { X } \{ a \} = \dim X$ for every point $a \in X$ .   
(c) If $f \in A ( X )$ is non-zero every irreducible component of $V ( f )$ has codimension 1 in $X$ (and hence dimension $\mathrm { d i m } X - 1$ by $( b )$ ).

Proof. Statement (a) is [G3, Proposition 11.9 (a) and Exercise 11.33 (a)]; the proof relies on Noether normalization.

Part (b) is [G3, Example 11.13 (a)]; the main non-trivial fact here (which would be false in arbitrary rings) is that all maximal chains of prime ideals in $A ( X )$ have the same length, so that a maximal chain containing the prime ideal $I ( Y )$ also has length $\mathrm { d i m } X$ .

Finally, statement (c) is just Krull’s Principal Ideal Theorem [G3, Proposition 11.15 and Corollary 11.19].

Example 2.29. Let $X = V \big ( x _ { 2 } - x _ { 1 } ^ { 2 } \big ) \subset \mathbb { A } _ { \mathbb { C } } ^ { 2 }$ be the affine variety whose real points are shown in the picture on the right. Then we have as expected:

(a) $X$ is irreducible by Proposition 2.8 since its coordinate ring $A ( X ) = \mathbb { C } [ x _ { 1 } , x _ { 2 } ] / ( x _ { 2 } - x _ { 1 } ^ { 2 } ) \cong \mathbb { C } [ x _ { 1 } ]$ is an integral domain.   
(b) $X$ has dimension 1 by Proposition 2.28 (c), since it is the zero locus of one non-zero polynomial in the affine space $\mathbb { A } ^ { 2 }$ , and dim $\mathbb { A } ^ { 2 } = 2$ by Proposition 2.28 (a).

![](images/6dd075dd87002a445ecc9f1d415239c138b6186c9dfeca2e353822e06660b352.jpg)

Exercise 2.30. Let $A$ be an arbitrary subset of a topological space $X$ . Prove that $\mathrm { d i m } A \le \mathrm { d i m } X$ .

Remark 2.31. Depending on where our chains of irreducible closed subvarieties end resp. start, we can break up the supremum in Definition 2.25 into irreducible components or local contributions:

(a) If $X = X _ { 1 } \cup \cdots \cup X _ { r }$ is the irreducible decomposition of a Noetherian topological space as in Proposition 2.14, we have

$$
\dim X = \operatorname* { m a x } \{ \dim X _ { 1 } , \dots , \dim X _ { r } \} :
$$

“≤” Assume that $\dim X \geq n$ , so that there is a chain $Y _ { 0 } \subsetneq \cdots \subsetneq Y _ { n }$ of non-empty irreducible closed subvarieties of $X$ . Then $Y _ { n } = \left( Y _ { n } \cap X _ { 1 } \right) \cup \cdots \cup \left( Y _ { n } \cap X _ { r } \right)$ is a union of closed subsets. So as $Y _ { n }$ is irreducible we must have $Y _ { n } = Y _ { n } \cap X _ { i }$ , and hence $Y _ { n } \subset X _ { i }$ , for some $i .$ . But then $Y _ { 0 } \subsetneq \cdots \subsetneq Y _ { n }$ is a chain of non-empty irreducible closed subsets in $X _ { i }$ , and hence $\dim X _ { i } \geq n$ .   
“≥” Let $\operatorname* { m a x } \{ \dim X _ { 1 } , \ldots , \dim X _ { r } \} \geq n$ . Then there is a chain of non-empty irreducible closed subsets $Y _ { 0 } \subsetneq \cdots \subsetneq Y _ { n }$ in some $X _ { i }$ . This is also such a chain in $X$ , and hence $\dim X \geq n .$ .

So for many purposes it suffices to consider the dimension of irreducible spaces.

(b) We always have $\dim X = \operatorname* { s u p } \{ \operatorname { c o d i m } _ { X } \{ a \} : a \in X \}$ $\leq$ ” If $\dim X \geq n$ there is a chain $Y _ { 0 } \subsetneq \cdots \subsetneq Y _ { n }$ of non-empty irreducible closed subsets of $X$ . For any $a \in Y _ { 0 }$ this chain then shows that $\mathrm { c o d i m } _ { X } \{ a \} \ge n$ .

$\ { \stackrel { \scriptscriptstyle 4  } { \geq } } \ { \mathrm { I f } } \ { \mathrm { c o d i m } } _ { X } \{ a \} \geq n$ for some $a \in X$ there is a chain $\{ a \} \subset Y _ { 0 } \subsetneq \cdots \subsetneq Y _ { n }$ of non-empty irreducible closed subsets of $X$ , which also shows that $\dim X \geq n$ .

The picture below illustrates these two equations: The affine variety $X = V ( x _ { 1 } x _ { 3 } , x _ { 2 } x _ { 3 } ) \subset \mathbb { A } ^ { 3 }$ is a union of two irreducible components, a line $V ( x _ { 1 } , x _ { 2 } )$ of dimension 1 and a plane $V ( x _ { 3 } )$ of dimension 2 (see Proposition 2.28 (a)). So by (a) we have $\mathrm { d i m } X = 2$ (with a maximal chain of length 2 as in Definition 2.25 (a) given by $Y _ { 0 } \subsetneq Y _ { 1 } \subsetneq Y _ { 2 } ,$ ).

![](images/f73cd7b114df9d9b0d5dd53132ef3fe41ec3982f59931a8219b3586a82bf5ed1.jpg)

As for (b), the codimension of the point $Y _ { 0 }$ is 2, whereas the codimension of the point $X _ { 0 }$ is 1, as illustrated by the chains in the picture. Note that this codimension of a point can be interpreted geometrically as the local dimension of $X$ at this point. Hence Proposition 2.28 (b) can also be interpreted as saying that the local dimension of an irreducible variety is the same at every point.

In practice, we will usually be concerned with affine varieties all of whose components have the same dimension. These spaces have special names that we want to introduce now. Note however that (as with the definition of a variety, see Remark 1.3) these terms are not used consistently throughout the literature — sometimes e. g. a curve is required to be irreducible, and sometimes it might be allowed to have additional components of dimension less than 1.

Definition 2.32 (Pure-dimensional spaces).

(a) A Noetherian topological space $X$ is said to be of pure dimension $n$ if every irreducible component of $X$ has dimension $n$ .   
(b) An affine variety is called . . . • a curve if it is of pure dimension 1; • a surface if it is of pure dimension 2; • a hypersurface in an irreducible affine variety $Y \supset X$ if it is an affine subvariety of pure dimension $\dim Y - 1$ .

Exercise 2.33. Let $X$ be the set of all $2 \times 3$ matrices over a field $K$ that have rank at most 1, considered as a subset of $\mathbb { A } ^ { 6 } = \mathbf { M } \mathrm { a t } ( 2 \times 3 , K )$ .

Show that $X$ is an irreducible affine variety. What is its dimension?

Exercise 2.34. Let $X$ be a topological space. Prove:

(a) If $\{ U _ { i } : i \in I \}$ is an open cover of $X$ then $\dim X = \operatorname* { s u p } \{ \dim U _ { i } : i \in I \} .$ . (b) If $X$ is an irreducible affine variety and $U \subset X$ a non-empty open subset then $\mathrm { d i m } X = \mathrm { d i m } U$ . Does this statement hold more generally for any irreducible topological space?

Exercise 2.35. Let $X$ be an affine variety with irreducible decomposition $X = X _ { 1 } \cup \cdots \cup X _ { r }$ , and let $a \in X$ . Show that the local dimension $\operatorname { c o d i m } _ { X } \{ a \}$ of $X$ at $a$ is given by

$$
\mathrm { c o d i m } _ { X } \{ a \} = \operatorname* { m a x } \{ \dim X _ { i } : a \in X _ { i } \} .
$$

Exercise 2.36. Prove:

(a) Every Noetherian topological space is compact. In particular, every open subset of an affine variety is compact in the Zariski topology. (Recall that by definition a topological space $X$ is compact if every open cover of $X$ has a finite subcover.)   
(b) A complex affine variety of dimension at least 1 is never compact in the classical topology.

We have seen in Proposition 2.28 (c) that the zero locus of a single polynomial in an irreducible affine variety is a hypersurface. Let us now address the opposite question: Is every (irreducible) hypersurface of a given irreducible affine variety $X$ the zero locus of a single polynomial? Surprisingly, it turns out that the answer to this question depends on a rather subtle algebraic property of the coordinate ring $A ( X )$ , namely on whether it is a unique factorization domain, i. e. whether every non-zero non-unit in $A ( X )$ can be written as a product of prime elements [G3, Definition 8.1]. The reason for this is the following result from commutative algebra.

Proposition 2.37. Let $R$ be a Noetherian integral domain (e. g. the coordinate ring $A ( X )$ of an irreducible affine variety $X$ ). Then the following two statements are equivalent:

(a) Every prime ideal of codimension 1 in $R$ is principal.   
(b) $R$ is a unique factorization domain.

# Proof.

(a) $\Rightarrow ( { \mathsf { b } } )$ : First of all, similarly to the proof of Proposition 2.14 we can decompose any nonzero non-unit $f \in R$ as a product of irreducible elements since $R$ is Noetherian: Otherwise $f$ cannot be irreducible itself, so we must have a decomposition $f = f _ { 1 } f _ { 1 } ^ { \prime }$ into non-units, of which at least one factor, say $f _ { 1 }$ , is not a product of irreducible elements. We can then continue this process, i. e. write $f _ { 1 } = f _ { 2 } f _ { 2 } ^ { \prime }$ where $f _ { 2 }$ is not a product of irreducibles, and so on. We thus obtain an infinite chain $\left. f \right. \subsetneq \left. f _ { 1 } \right. \subsetneq \left. f _ { 2 } \right. \subsetneq \cdots$ , in contradiction to $R$ being Noetherian.

To prove that $R$ is a unique factorization domain it therefore suffices to show that every irreducible element $f \in R$ is prime. To see this, choose a minimal prime ideal $P$ containing $f$ . By Krull’s Principal Ideal Theorem [G3, Proposition 11.15] we then have codim $P = 1$ so by assumption $P$ is principal, i. e. we have $P = \langle g \rangle$ for a prime element $g$ . But $g$ divides $f$ and $f$ is irreducible, so that $f$ and $g$ agree up to units, and we obtain that $f$ is prime as well.

$( \mathbf { b } ) \Rightarrow ( \mathbf { a } )$ : Let $P$ be a prime ideal of codimension 1 in $R$ . If $P = \{ 0 \}$ then $P$ is clearly principal. Otherwise, since $P \neq \langle 1 \rangle$ , we can choose a non-zero non-unit $f \in P$ .

As $R$ is a unique factorization domain, we can write $f = f _ { 1 } \cdot \cdot \cdot \cdot \cdot f _ { k }$ for some prime elements $f _ { 1 } , \dots , f _ { k } \in R$ . Since $P$ is a prime ideal we must then have $f _ { i } \in P$ for some $i$ . We thus obtain a chain $\{ 0 \} \subsetneq \langle f _ { i } \rangle \subset P$ of prime ideals in $P$ . But as the codimension of $P$ is 1 this requires that $P = \langle f _ { i } \rangle$ , i. e. that $P$ is principal. 

Remark 2.38 (Ideal of hypersurfaces in $\mathbb { A } ^ { n }$ ). Let $X$ be an irreducible hypersurface in $\mathbb { A } ^ { n }$ . Then $I ( X ) { \overset { \underset { \mathrm { \Large ~ \ 4 ~ } } { } } { \mathop { \leq } } } K [ x _ { 1 } , \ldots , x _ { n } ]$ is a prime ideal of codimension 1. As the polynomial ring is a unique factorization domain [G3, Proposition 8.5] it follows from Proposition 2.37 that $I ( X ) = \langle f \rangle$ for an irreducible polynomial $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ .

If $X \subset \mathbb { A } ^ { n }$ is still a hypersurface, but not necessarily irreducible, we can apply the same argument to each component of its irreducible decomposition $X = X _ { 1 } \cup \dots \cup X _ { k }$ to obtain $I ( X _ { j } ) = \langle f _ { j } \rangle$ for some $f _ { j } \in K [ x _ { 1 } , \ldots , x _ { n } ]$ and all $j$ . By Lemma 1.12 (a) the ideal $I ( X ) = \langle f \rangle$ with $f = f _ { 1 } \cdot \cdots \cdot f _ { k }$ is then again principal.

As $f$ is clearly unique up to units, we can associate its degree naturally to the hypersurface $X$ :

Definition 2.39 (Degree of an affine hypersurface). Let $X$ be an affine hypersurface in $\mathbb { A } ^ { n }$ , with ideal $I ( X ) = \langle f \rangle$ as in Remark 2.38. Then the degree of $f$ is also called the degree of $X$ , denoted $\deg X$ . For the degrees 1, 2, 3 one calls $X$ a linear, quadric, or cubic hypersurface, respectively.

In general, it is a hard problem to figure out if the coordinate ring of a given affine variety is a unique factorization domain. Let us therefore just give a single example in which this is not the case, and hence in which by Proposition 2.37 there is an irreducible codimension-1 hypersurface whose ideal is not principal.

Exercise 2.40. Let $R = K [ x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ] / \langle x _ { 1 } x _ { 4 } - x _ { 2 } x _ { 3 } \rangle$ . Show:

(a) $R$ is an integral domain of dimension 3.   
(b) $x _ { 1 } , \ldots , x _ { 4 }$ are irreducible, but not prime in $R$ . In particular, $R$ is not a unique factorization domain.   
(c) $x _ { 1 } x _ { 4 }$ and $x _ { 2 } x _ { 3 }$ are two decompositions of the same element of $R$ into irreducible elements that do not agree up to units.   
(d) $\left. x _ { 1 } , x _ { 2 } \right.$ is a prime ideal of codimension 1 in $R$ that is not principal.

In particular, the plane $V ( x _ { 1 } , x _ { 2 } )$ is a hypersurface in the affine variety $X = V ( x _ { 1 } x _ { 4 } - x _ { 2 } x _ { 3 } )$ whose ideal cannot be generated by one element in $A ( X )$ .

# 3. The Sheaf of Regular Functions

After having defined affine varieties, our next goal must be to say what kind of maps between them we want to consider as morphisms, i. e. as “nice maps preserving the structure of the variety”. In this chapter we will look at the easiest case of this: the so-called regular functions, i. e. maps to the ground field $K = \mathbb { A } ^ { 1 }$ . They should be thought of as the analogue of continuous functions in topology, differentiable functions in real analysis, or holomorphic functions in complex analysis.

So what kind of nice “algebraic” functions should we consider on an affine variety $X ?$ First of all, as in the case of continuous or differentiable functions, we should not only aim for a definition of functions on all of $X$ , but also on an arbitrary open subset $U$ of $X$ . In contrast to the coordinate ring $A ( X )$ of polynomial functions on the whole space $X$ , this allows us to consider quotients $\frac { g } { f }$ of polynomial functions $f , g \in A ( X )$ with $f \neq 0$ as well, since we can exclude the zero set $V ( f )$ of the denominator from the domain of definition of the function.

But taking our functions to be quotients of polynomials turns out to be a little bit too restrictive. The problem with this definition would be that it is not local : Recall that the condition on a function to be continuous or differentiable is local in the sense that it can be checked at every point, with the whole function then being continuous or differentiable if it has this property at every point. Being a quotient of polynomials however is not a condition of this type — we would have to find one global representation as a quotient of polynomials that is then valid at every point. Imposing such non-local conditions is usually not a good thing to do, since it would be hard in practice to find the required global representations of the functions.

The way out of this problem is to consider functions that are only locally quotients of polynomials, i. e. functions $\varphi \colon U \to K$ such that each point $a \in U$ has a neighborhood in $U$ in which $\textstyle \varphi = { \frac { g } { f } }$ holds for two polynomials $f$ and $g$ (that may depend on $a$ ). In fact, we will see in Example 3.3 that passing from global to local quotients of polynomials really sometimes makes a difference. So let us now give the corresponding formal definition of regular functions.

Definition 3.1 (Regular functions). Let $X$ be an affine variety, and let $U$ be an open subset of $X$ . A regular function on $U$ is a map $\varphi \colon U \to K$ with the following property: For every $a \in U$ there are polynomial functions $f , g \in A ( X )$ with $f ( x ) \neq 0$ and

$$
\varphi ( x ) = { \frac { g ( x ) } { f ( x ) } }
$$

for all $x$ in an open subset $U _ { a }$ with $a \in U _ { a } \subset U$ . The set of all such regular functions on $U$ will be denoted ${ \mathcal { O } } _ { X } ( U )$ ; it is clearly a $K$ -algebra (with pointwise addition and multiplication of functions, and pointwise scalar multiplication).

Notation 3.2. We will usually write the condition $\begin{array} { r } { { \ddot { \varphi } } ( x ) = { \frac { g ( x ) } { f ( x ) } } } \end{array}$ for all $x \in U _ { a } { } ^ { \prime } { } ^ { \prime }$ of Definition 3.1 simply as $\begin{array} { r } { { \bf \ddot { \varphi } } ^ { } \varphi = \frac { g } { f } } \end{array}$ on $U _ { a } { } ^ { , }$ ”. This is certainly an intuitive notation that should not lead to any confusion. Note however that this means that the notation $\textstyle { \frac { g } { f } }$ denotes a pointwise quotient of functions in this case, and not an element in a localized ring. We will see an interpretation of regular functions in terms of localized rings in Corollary 3.10 and Lemma 3.19.

Example 3.3 (Local $\neq$ global quotients of polynomials). Consider the 3-dimensional affine variety $X = V ( x _ { 1 } x _ { 4 } - x _ { 2 } x _ { 3 } ) \subset \mathbb { A } ^ { 4 }$ and the open subset

$$
U = X \backslash V ( x _ { 2 } , x _ { 4 } ) = \{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ) \in X : x _ { 2 } \neq 0 { \mathrm { ~ o r ~ } } x _ { 4 } \neq 0 \} \quad \subset X .
$$

Then

$$
\varphi \colon U  K , ( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ) \mapsto { \{ \begin{array} { l l } { { \frac { x _ { 1 } } { x _ { 2 } } } } & { { \mathrm { i f } } x _ { 2 } \not = 0 , } \\ { { \frac { x _ { 3 } } { x _ { 4 } } } } & { { \mathrm { i f } } x _ { 4 } \not = 0 } \end{array}  }
$$

is a regular function on $U$ : It is well-defined since the defining equation for $X$ implies $\begin{array} { r } { \frac { x _ { 1 } } { x _ { 2 } } = \frac { x _ { 3 } } { x _ { 4 } } } \end{array}$ whenever $x _ { 2 } \neq 0$ and $x _ { 4 } \neq 0$ , and it is obviously locally a quotient of polynomials. But none of the two representations in $( \ast )$ as quotients of polynomials can be used on all of $U$ , since the first one does not work e. g. at the point $( 0 , 0 , 0 , 1 ) \in U$ , whereas the second one does not work at $( 0 , 1 , 0 , 0 ) \in U$ . Algebraically, this just exploits the fact that $A ( X ) = K [ x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ] / \langle x _ { 1 } x _ { 4 } - x _ { 2 } x _ { 3 } \rangle$ is not a unique factorization domain, as we have seen in Exercise 2.40.

In fact, one can show that there is also no other global representation of $\varphi$ as a quotient of two polynomials. We will not need this statement here, and so we do not prove it — we should just keep in mind that representations of regular functions as quotients of polynomials will in general not be valid on the complete domain of definition of the function.

As a first result, let us prove the expected statement that zero loci of regular functions are always closed in their domain of definition.

Lemma 3.4 (Zero loci of regular functions are closed). Let $U$ be an open subset of an affine variety $X$ , and let $\varphi \in { \mathcal { O } } _ { X } ( U )$ be a regular function on $U$ . Then

$$
V ( \varphi ) : = \{ x \in U : \varphi ( x ) = 0 \}
$$

is closed in $U$

Proofsome n 3.1 (with y point nowhe $a \in U$ has on open neighborhood ). So the set $U _ { a }$ $U$ on which $\textstyle \varphi = { \frac { g _ { a } } { f _ { a } } }$ for $f _ { a } , g _ { a } \in A ( X )$ $f _ { a }$ $U _ { a }$

$$
\{ x \in U _ { a } : \varphi ( x ) \neq 0 \} = U _ { a } \backslash V ( g _ { a } )
$$

is open in $X$ , and hence so is their union over all $a \in U$ , which is just $U \backslash V ( \varphi )$ . This means that $V ( \varphi )$ is closed in $U$ . 

Remark 3.5 (Identity Theorem for regular functions). A simple but remarkable consequence of Lemma 3.4 is the following: Let $U \subset V$ be non-empty open subsets of an irreducible affine variety $X$ . If $\varphi _ { 1 } , \varphi _ { 2 } \in { \mathcal { O } } _ { X } ( V )$ are two regular functions on $V$ that agree on $U$ , then they must agree on all of $V$ : The locus $V { \big ( } \varphi _ { 1 } - \varphi _ { 2 } { \big ) }$ where the two functions agree contains $U$ and is closed in $V$ by Lemma 3.4, hence it also contains the closure $\overline { U }$ of $U$ in $V$ . But ${ \overline { { V } } } = X$ by Remark 2.16 (b), hence $V$ is irreducible by Exercise 2.20 (b), which again by Remark 2.16 (b) means that the closure of $U$ in $V$ is $V$ . Consequently, we have $\varphi _ { 1 } = \varphi _ { 2 }$ on $V$ .

Note that this statement is not really surprising since the open subsets in the Zariski topology are so big: Over the ground field $\mathbb { C }$ , for example, it is also true in the classical topology that the closure of $U$ in $V$ is $V$ , and hence the equation $\varphi _ { 1 } = \varphi _ { 2 }$ on $V$ already follows from $\varphi _ { 1 } | _ { U } = \varphi _ { 2 } | _ { U }$ by the (classical) continuity of $\varphi _ { 1 }$ and $\varphi _ { 2 }$ . The interesting fact here is that the very same statement holds in complex analysis for holomorphic (i. e. complex differentiable) functions as well: Two holomorphic functions on a (connected) open subset $V \subset \mathbb { C } ^ { n }$ must already be the same if they agree on a smaller non-empty open subset $U \subset V$ . This is called the Identity Theorem for holomorphic functions. In complex analysis this is an actual theorem because the open subset $U$ can be very small, so that the uniqueness of the extension to $V$ is much more surprising than it is here in algebraic geometry. Still this is an example of a statement that is true in literally the same way in both algebraic and complex geometry, although these two theories are very different a priori. We will see another case of this in Example 3.11.

Let us now go ahead and compute the $K$ -algebras ${ \mathcal { O } } _ { X } ( U )$ in some cases. A particularly important result in this direction can be obtained if $U$ is the complement of the zero locus of a single polynomial function $f \in A ( X )$ . In this case it turns out that (in contrast to Example 3.3) the regular functions on $U$ can always be written with a single representation as a fraction, whose denominator is in addition a power of $f$ .

Definition 3.6 (Distinguished open subsets). For an affine variety $X$ and a polynomial function $f \in A ( X )$ on $X$ we call

$$
D ( f ) : = X \backslash V ( f ) = \{ x \in X : f ( x ) \neq 0 \}
$$

the distinguished open subset of $f$ in $X$ .

Remark 3.7. The distinguished open subsets of an affine variety $X$ behave nicely with respect to intersections and unions:

(a) For any $f , g \in A ( X )$ we have $D ( f ) \cap D ( g ) = D ( f g )$ , since $f ( x ) \neq 0$ and $g ( x ) \neq 0$ is equivalent to $( f g ) ( x ) \neq 0$ for all $x \in X$ . In particular, finite intersections of distinguished open subsets are again distinguished open subsets.

(b) Any open subset $U \subset X$ is a finite union of distinguished open subsets: By definition of the Zariski topology it is the complement of an affine variety, which in turn is the zero locus of finitely many polynomial functions $f _ { 1 } , \dots , f _ { k } \in A ( X )$ by Remark 1.6. Hence we have

$$
U = X \backslash V ( f _ { 1 } , \ldots , f _ { k } ) = X \backslash ( V ( f _ { 1 } ) \cap \cdots \cap V ( f _ { k } ) ) = D ( f _ { 1 } ) \cup \cdots \cup D ( f _ { k } ) .
$$

We can therefore think of the distinguished open subsets as the “smallest” open subsets of $X$ — in topology, the correct notion for this would be to say that they form a basis of the Zariski topology on $X$ .

Proposition 3.8 (Regular functions on distinguished open subsets). Let $X$ be an affine variety, and let $f \in A ( X )$ . Then

$$
\mathcal { O } _ { X } ( D ( f ) ) = \bigg \{ \frac { g } { f ^ { n } } : g \in A ( X ) , n \in \mathbb { N } \bigg \} .
$$

In particular,

• setting $f = 1$ we see that ${ \mathcal { O } } _ { X } ( X ) = A ( X )$ , i. e. the regular functions on all of $X$ are exactly the polynomial functions;

• on a distinguished open subset a regular function is always globally the quotient of two polynomial functions.

Proof. The inclusion “ $\supset ^ { \prime \prime }$ is obvious: Every function of the form $\frac { g } { f ^ { n } }$ for $g \in A ( X )$ and $n \in \mathbb { N }$ is clearly regular on $D ( f )$ .

For the opposite inclusion “ $\cdot \subset '$ , let $\varphi \colon D ( f ) \to K$ be a regular function. By Definition 3.1 we obtain for every $a \in D ( f )$ a local representation $\textstyle \varphi = { \frac { g _ { a } } { f _ { a } } }$ for some $f _ { a } , g _ { a } \in A ( X )$ which is valid on an open neighborhood of $a$ in $D ( f )$ . After possibly shrinking these neighborhoods we may assume by Remark 3.7 (b) that they are distinguished open subsets $D ( h _ { a } )$ for some $h _ { a } \in A ( X )$ . Moreover, we may replace $g _ { a }$ and $f _ { a }$ by $g _ { a } h _ { a }$ and $f _ { a } h _ { a }$ (which does not change their quotient on $D ( h _ { a } ) )$ to assume that both the numerator and denominator of $\varphi$ (which we will again call $g _ { a }$ and $f _ { a , }$ ) vanish on the complement $V ( h _ { a } )$ of $D ( h _ { a } )$ . Finally, this means that $f _ { a }$ vanishes on $V ( h _ { a } )$ and does not vanish on $D ( h _ { a } ) - { \mathsf { s o } } h _ { a }$ and $f _ { a }$ have the same zero locus, and we can therefore assume that $h _ { a } = f _ { a }$ .

As a consequence, note that in $A ( X )$ we have

$$
g _ { a } f _ { b } = g _ { b } f _ { a } \quad { \mathrm { f o r ~ a l l ~ } } a , b \in D ( f ) :
$$

These two functions agree on $D ( f _ { a } ) \cap D ( f _ { b } )$ since $\begin{array} { r } { \varphi = { \frac { g _ { a } } { f _ { a } } } = { \frac { g _ { b } } { f _ { b } } } } \end{array}$ there, and they are both zero otherwise since by our construction we have $g _ { a } ( x ) = f _ { a } ( x ) \dot { = } 0$ for all $x \in V ( f _ { a } )$ and $g _ { b } ( x ) = f _ { b } ( x ) = 0$ for all $x \in V ( f _ { b } )$ .

Now all our open neighborhoods cover $D ( f )$ , i. e. we have $\begin{array} { r } { D ( f ) = \bigcup _ { a \in D ( f ) } D ( f _ { a } ) } \end{array}$ . Passing to the complement we obtain

$$
V ( f ) = \bigcap _ { a \in D ( f ) } V ( f _ { a } ) = V { \bigl ( } \{ f _ { a } : a \in D ( f ) \} { \bigr ) } ,
$$

and thus by the relative Nullstellensatz of Remark 1.18 (b)

$$
f \in I ( V ( f ) ) = I { \big ( } V { \big ( } \{ f _ { a } : a \in D ( f ) \} { \big ) } { \big ) } = { \sqrt { \langle f _ { a } : a \in D ( f ) \rangle } } .
$$

This means that $\begin{array} { r } { f ^ { n } = \sum _ { a } k _ { a } f _ { a } } \end{array}$ for some $n \in \mathbb { N }$ and $k _ { a } \in A ( X )$ for finitely many elements $a \in D ( f )$ . Setting $\boldsymbol { g } : = \sum _ { a } k _ { a } \boldsymbol { g } _ { a }$ , we then claim that $\textstyle \varphi = { \frac { g } { f ^ { n } } }$ on all of $D ( f )$ : For all $b \in D ( f )$ we have $\begin{array} { r } { \varphi = \frac { g _ { b } } { f _ { b } } } \end{array}$ and

$$
g f _ { b } = \sum _ { a } k _ { a } g _ { a } f _ { b } \overset { ( * ) } { = } \sum _ { a } k _ { a } g _ { b } f _ { a } = g _ { b } f ^ { n }
$$

on $D ( f _ { b } )$ , and these open subsets cover $D ( f )$

Remark 3.9. In the proof of Proposition 3.8 we had to use Hilbert’s Nullstellensatz again. In fact, the statement is false without our assumption of an algebraically closed ground field, as you can see from the example of the real function $\frac { \overset { \underset { 1 } { } } { } } { x ^ { 2 } + 1 }$ that is defined on all of $\mathbb { R }$ , but not a polynomial function.

The statement of Proposition 3.8 is deeply linked to commutative algebra. Although we considered the quotients $\frac { g } { f ^ { n } }$ in this statement to be fractions of polynomial functions, we can now also interpret them as elements of a certain algebraic localization of the coordinate ring.

Corollary 3.10 (Regular functions as localizations). Let $X$ be an affine variety, and let $f \in A ( X )$ . Then $\mathcal { O } _ { X } ( D ( f ) )$ is isomorphic (as a $K$ -algebra) to the localization $A ( X ) _ { f }$ of the coordinate ring $A ( X )$ at the multiplicatively closed subset $\{ f ^ { n } : n \in \mathbb { N } \}$ .

Proof. There is an obvious $K$ -algebra homomorphism

$$
A ( X ) _ { f }  \mathcal { O } _ { X } ( D ( f ) ) , \frac { g } { f ^ { n } } \mapsto \frac { g } { f ^ { n } }
$$

that interprets a formal fraction in the localization $A ( X ) _ { f }$ as an actual quotient of polynomial functions on $D ( f )$ . It is in fact well-defined: If $\begin{array} { r } { { \frac { g } { f ^ { n } } } = { \frac { g ^ { \prime } } { f ^ { m } } } } \end{array}$ as formal fractions in the localization $A ( X ) _ { f }$ then $f ^ { k } \left( g f ^ { m } - g ^ { \prime } f ^ { n } \right) = 0$ in $A ( X )$ for some $k \in \mathbb N$ , which means that $g f ^ { m } = g ^ { \prime } f ^ { n }$ and thus $\begin{array} { r } { { \frac { g } { f ^ { n } } } = { \frac { g ^ { \prime } } { f ^ { m } } } } \end{array}$ as functions on $D ( f )$ .

The homomorphism is surjective by Proposition 3.8. It is also injective: If $\textstyle { \frac { g } { f ^ { n } } } = 0$ as a function on $D ( f )$ then $g = 0$ on $D ( f )$ and hence $f g = 0$ on all of $X$ , which means $f ( g \cdot { \mathrm { 1 } } - 0 \cdot f ^ { n } ) = 0$ in $A ( X )$ and thus $\begin{array} { r } { { \frac { g } { f n } } = { \frac { 0 } { 1 } } } \end{array}$ as formal fractions in the localization $A ( X ) _ { f }$ . 

Example 3.11 (Regular functions on $\mathbb { A } ^ { 2 } \backslash \{ 0 \} )$ . Probably the easiest case of an open subset of an affine variety that is not a distinguished open subset is the complement $U = \mathbb { A } ^ { 2 } \backslash \{ 0 \}$ of the origin in the affine plane $X = \mathbb { A } ^ { 2 }$ . We claim that

$$
\mathcal { O } _ { \mathbb { A } ^ { 2 } } ( \mathbb { A } ^ { 2 } \backslash \{ 0 \} ) = K [ x _ { 1 } , x _ { 2 } ] ,
$$

and thus that ${ \mathcal { O } } _ { X } ( U ) = { \mathcal { O } } _ { X } ( X )$ , i. e. every regular function on $U$ can be extended to $X$ . Note that this is another result that is true in the same way in complex analysis: There is a Removable Singularity Theorem that implies that every holomorphic function on $\mathbb { C } ^ { 2 } \backslash \{ 0 \}$ can be extended holomorphically to $\mathbb { C } ^ { 2 }$ .

To prove our claim let $\varphi \in { \mathcal { O } } _ { X } ( U )$ . Note that $\varphi$ is regular on the two distinguished open subsets $D ( x _ { 1 } ) = ( \mathbb { A } ^ { 1 } \backslash \{ 0 \} ) \times \mathbb { A } ^ { 1 }$ and $D ( x _ { 2 } ) = \mathbb { A } ^ { 1 } \times ( \mathbb { A } ^ { 1 } \backslash \{ 0 \} )$ , and so by Proposition 3.8 we can write $\textstyle \varphi = { \frac { f } { x _ { 1 } ^ { m } } }$ on $D ( x _ { 1 } )$ and $\begin{array} { r } { \varphi = \frac { g } { x _ { 2 } ^ { n } } } \end{array}$ on $D ( x _ { 2 } )$ for some $f , g \in K [ x _ { 1 } , x _ { 2 } ]$ and $m , n \in \mathbb { N }$ . Of course we can do this so that $x _ { 1 } \ / \ f$ and $x _ { 2 } \ / \ g$ .

On the intersection $D ( x _ { 1 } ) \cap D ( x _ { 2 } )$ both representations of $\varphi$ are valid, and so we have $f x _ { 2 } ^ { n } = g x _ { 1 } ^ { m }$ on $D ( x _ { 1 } ) \cap D ( x _ { 2 } )$ . But the locus $V ( f x _ { 2 } ^ { n } - g x _ { 1 } ^ { m } )$ where this equation holds is closed, and hence we see that $f x _ { 2 } ^ { n } = g x _ { 1 } ^ { m }$ also on $\overline { { D ( x _ { 1 } ) \cap D ( x _ { 2 } ) } } = \mathbb { A } ^ { 2 }$ . In other words, we have $f x _ { 2 } ^ { n } = g x _ { 1 } ^ { m }$ in the polynomial $\mathrm { r i n g } A ( \mathbb { A } ^ { 2 } ) = K [ x _ { 1 } , x _ { 2 } ]$ .

Now if we had $m > 0$ then $x _ { 1 }$ must divide $f x _ { 2 } ^ { n }$ , which is only possible if $x _ { 1 } \mid f$ as $K [ x _ { 1 } , x _ { 2 } ]$ is a unique factorization domain. This is a contradiction, and so it follows that $m = 0$ . But then $\varphi = f$ is a polynomial, as we have claimed.

Exercise 3.12. Show that Example 3.11 can be generalized as follows: Let $Y$ be a non-empty irreducible subvariety of an affine variety $X$ , and set $U = X \backslash Y$ .

(a) Assume that $A ( X )$ is a unique factorization domain. Show that ${ \mathcal { O } } _ { X } ( U ) = A ( X )$ if and only if codim $Y \geq 2$ .   
(b) Show by example that the equivalence of (a) is in general false if $A ( X )$ is not assumed to be a unique factorization domain.

Recall that we have defined regular functions on an open subset $U$ of an affine variety as set-theoretic functions from $U$ to the ground field $K$ that satisfy some local property. Local constructions of function-like objects occur in many places in algebraic geometry (and also in other “topological” fields of mathematics), and so we will spend the rest of this chapter to formalize the idea of such objects. This will have the advantage that it gives us an “automatic” definition of morphisms between affine varieties in Chapter 4, and in fact also between more general varieties in Chapter 5.

Definition 3.13 (Sheaves). A presheaf $\mathcal { F }$ (of rings) on a topological space $X$ consists of the data:

• for every open set $U \subset X$ a ring ${ \mathcal { F } } ( U )$ (think of this as the ring of functions on $U$ ), • for every inclusion $U \subset V$ of open sets in $X$ a ring homomorphism $\rho _ { V , U } \colon { \mathcal { F } } ( V ) \to { \mathcal { F } } ( U )$ called the restriction map (think of this as the usual restriction of functions to a subset),

such that

• $\mathcal { F } ( \pmb { \emptyset } ) = 0 .$ ,   
• $\rho _ { U , U }$ is the identity map on ${ \mathcal { F } } ( U )$ for all $U$ ,   
• for any inclusion $U \subset V \subset W$ of open sets in $X$ we have $\rho _ { V , U } \circ \rho _ { W , V } = \rho _ { W , U }$ .

The elements of ${ \mathcal { F } } ( U )$ are usually called the sections of $\mathcal { F }$ over $U$ , and the restriction maps $\rho _ { V , U }$ are written as $\varphi \mapsto \varphi | _ { U }$ .

A presheaf $\mathcal { F }$ is called a sheaf of rings if it satisfies the following gluing property: If $U \subset X$ is an open set, $\{ U _ { i } : i \in I \}$ an arbitrary open cover of $U$ and $\varphi _ { i } \in { \mathcal { F } } ( U _ { i } )$ sections for all $i$ such that $\varphi _ { i } | _ { U _ { i } \cap U _ { j } } = \varphi _ { j } | _ { U _ { i } \cap U _ { j } }$ for all $i , j \in I$ , then there is a unique $\varphi \in { \mathcal { F } } ( U )$ such that $\varphi | _ { U _ { i } } = \varphi _ { i }$ for all $i$ .

Remark 3.14 (Sheaves for other categories). In Definition 3.13 we have constructed (pre-)sheaves of rings. In the same way one can define (pre-)sheaves of $K$ -algebras, Abelian groups, or other suitable categories, by requiring that all ${ \mathcal { F } } ( U )$ are objects and all restriction maps are morphisms in the corresponding category. In the following, we will mainly be concerned with sheaves of rings and $K$ -algebras, and sheaves of modules later in Chapter 13.

Example 3.15. Intuitively speaking, any “function-like” object forms a presheaf; it is a sheaf if the conditions imposed on the “functions” are local (i. e. if they can be checked on an open cover). The following examples illustrate this.

(a) Let $X$ be an affine variety. Then the rings ${ \mathcal { O } } _ { X } ( U )$ of regular functions on open subsets $U \subset X$ , together with the usual restriction maps of functions, form a sheaf ${ \mathcal { O } } _ { X }$ of $K$ -algebras on $X$ . In fact, the presheaf axioms are obvious, and the gluing property just means that a function $\varphi \colon U \to K$ is regular if it is regular on each element of an open cover of $U$ (which follows from the definition that $\varphi$ is regular if it is locally a quotient of polynomial functions). We call ${ \mathcal { O } } _ { X }$ the sheaf of regular functions on $X$ .

(b) Similarly, on $X = \mathbb { R } ^ { n }$ with the standard topology the rings

$$
{ \mathcal { F } } ( U ) = \{ \varphi \colon U \to \mathbb { R } \operatorname { c o n t i n u o u s } \}
$$

for open subsets $U \subset X$ form a sheaf $\mathcal { F }$ on $X$ with the usual restriction maps. In the same way we can consider on $X$ the sheaves of differentiable functions, analytic functions, arbitrary functions, and so on.

(c) Again on $X = \mathbb { R } ^ { n }$ let

$$
\mathcal { F } ( U ) = \{ \varphi \colon U \to \mathbb { R } \mathrm { c o n s t a n t f u n c t i o n } \}
$$

with the usual restriction maps. Then $\mathcal { F }$ is a presheaf, but not a sheaf, since being a constant function is not a local condition. More precisely, let $U _ { 1 }$ and $U _ { 2 }$ be any non-empty disjoint open subsets of $X$ , and let $\varphi _ { 1 } \in { \mathcal { F } } ( U _ { 1 } )$ and $\varphi _ { 2 } \in { \mathcal { F } } ( U _ { 2 } )$ be constant functions with different values. Then $\varphi _ { 1 }$ and $\varphi _ { 2 }$ trivially agree on $U _ { 1 } \cap U _ { 2 } = \emptyset$ , but there is still no constant function on $U = U _ { 1 } \cup U _ { 2 }$ that restricts to both $\varphi _ { 1 }$ on $U _ { 1 }$ and $\varphi _ { 2 }$ on $U _ { 2 }$ . Hence $\mathcal { F }$ does not satisfy the gluing property. Note however that we would obtain a sheaf if we considered locally constant functions instead of constant ones.

In order to get used to the language of sheaves let us now consider two common constructions with them.

Definition 3.16 (Restrictions of (pre-)sheaves). Let $\mathcal { F }$ be a presheaf on a topological space $X$ , and let $U \subset X$ be an open subset. Then the restriction of $\mathcal { F }$ to $U$ is defined to be the presheaf $\mathcal { F } | _ { U }$ on $U$ with

$$
\mathcal { F } | _ { U } ( V ) : = \mathcal { F } ( V )
$$

for every open subset $V \subset U$ , and with the restriction maps taken from $\mathcal { F }$ . Note that if $\mathcal { F }$ is a sheaf then so is $\mathcal { F } | _ { U }$ .

Construction 3.17 (Stalks of (pre-)sheaves). Again let $\mathcal { F }$ be a presheaf on a topological space $X$ , and let $a \in X$ . Then the stalk of $\mathcal { F }$ at $a$ is defined as

$\mathcal { F } _ { a } : = \{ ( U , \varphi ) : U \subset X$ open with $a \in U$ , and $\varphi \in { \mathcal { F } } ( U ) \} / \sim$ , where $( U , \varphi ) \sim ( U ^ { \prime } , \varphi ^ { \prime } )$ if there is an open subset $V$ with $a \in V \subset U \cap U ^ { \prime }$ and $\varphi | _ { V } = \varphi ^ { \prime } | _ { V }$ . It is easy to check that this is indeed an equivalence relation, and that $\mathcal { F } _ { a }$ inherits the structure of a ring (or $K$ -algebra) from ${ \mathcal { F } } ( U )$ .

The elements of $\mathcal { F } _ { a }$ are called germs of $\mathcal { F }$ at $a$ . In the case of the sheaf ${ \mathcal { O } } _ { X }$ on an affine variety $X$ , it is customary to write its stalk at a point $a \in X$ as ${ \mathcal { O } } _ { X , a }$ instead of as $( { \mathcal { O } } _ { X } ) _ { a }$ .

Remark 3.18. The geometric interpretation of the germs of a sheaf is that they are functions (resp. sections of the sheaf) that are defined in an arbitrarily small neighborhood of the given point — we will also refer to these objects as local functions at this point. For example:

(a) For the sheaf of differentiable functions on the real line, a germ at a point $a \in \mathbb { R }$ allows to compute the derivative of this function at $a$ , but none of the actual values of the function at any point except $a$ . On the other hand, we have seen in Remark 3.5 that holomorphic functions on a (connected) open subset of $\mathbb { C } ^ { n }$ are already determined by their values on any smaller open set. So in this sense germs of holomorphic functions carry “much more information” than germs of differentiable functions.   
(b) In algebraic geometry, for a point $a$ on an affine variety $X$ there is at least a well-defined evaluation map ${ \mathcal { O } } _ { X , a } \to K$ , $\varphi \mapsto \varphi ( a )$ at $a$ (but again not at any other point).

Germs of regular functions on an affine variety $X$ can also be described algebraically in terms of localizations — which is in fact the reason why this algebraic concept is called “localization”. As one might expect, such a germ at a point $a \in X$ , i. e. a regular function in a small neighborhood of $a$ , is given by an element in the localization of $A ( X )$ for which we allow as denominators all polynomials that do not vanish at $a$ .

Lemma and Definition 3.19 (Germs of regular functions as localizations). Let a be a point on an affine variety $X$ . Then the stalk ${ \mathcal { O } } _ { X , a }$ of ${ \mathcal { O } } _ { X }$ at a is isomorphic (as a $K$ -algebra) to the localization $A ( X ) _ { I ( a ) }$ of the coordinate ring $A ( X )$ at the maximal ideal $I ( a ) \triangleleft A ( X )$ , i. e. we have

$$
\mathcal { O } _ { X , a } \cong \Bigg \{ \frac { g } { f } : f , g \in A ( X ) \ w i t h \ f ( a ) \neq 0 \Bigg \} .
$$

In particular, ${ \mathcal { O } } _ { X , a }$ is a local ring (in the algebraic sense), with unique maximal ideal

$$
I _ { a } : = \{ \varphi \in { \mathcal { O } } _ { X , a } : \varphi ( a ) = 0 \} \cong \left\{ { \frac { g } { f } } : f , g \in A ( X ) { \mathrm { ~ } } w i t h g ( a ) = 0 a n d f ( a ) \neq 0 \right\} .
$$

It is called the local ring of $X$ at $a$ .

Proof. Consider the $K$ -algebra homomorphism

$$
A ( X ) _ { I ( a ) } \to \mathcal { O } _ { X , a } , { \frac { g } { f } } \mapsto { \overline { { \left( D ( f ) , { \frac { g } { f } } \right) } } }
$$

that maps a formal fraction $\textstyle { \frac { g } { f } }$ to the corresponding quotient of polynomial functions on the open neighborhood of $a$ where the denominator does not vanish. It is indeed well-defined: If $\begin{array} { r } { \frac { g } { f } = \frac { g ^ { \prime } } { f ^ { \prime } } } \end{array}$ in the localization then $h ( g f ^ { \prime } - g ^ { \prime } f ) = 0$ for some $h \in A ( X ) \backslash I ( a )$ . Hence the functions $\textstyle { \frac { g } { f } }$ and $\frac { g ^ { \prime } } { f ^ { \prime } }$ agree on the open neighborhood $D ( h ) \cap D ( f ) \cap D ( f ^ { \prime } )$ of $a$ , and thus they determine the same element in the stalk ${ \mathcal { O } } _ { X , a }$ .

This $K$ -algebra homomorphism is surjective since by definition any regular function in a sufficiently small neighborhood of $a$ must be representable by a fraction $\textstyle { \frac { g } { f } }$ with $g \in A ( X )$ and $f \in A ( X ) \backslash I ( a )$ . It is also injective: Assume that a function $\frac { g } { f }$ represents the zero element in the stalk ${ \mathcal { O } } _ { X , a }$ , i. e. that it is zero in an open neighborhood of $a$ . By possibly shrinking this neighborhood we may assume by Remark 3.7 (b) that it is a distinguished open subset $D ( h )$ containing $a$ , i. e. with $h \in A ( X ) \backslash I ( a )$ . But then $h ( g \cdot 1 - 0 \cdot f )$ is zero on all of $X$ , hence zero in $A ( X )$ , and thus $\begin{array} { r } { \frac { g } { f } = \frac { 0 } { 1 } } \end{array}$ in the localization $A ( X ) _ { I ( a ) }$ . 

Exercise 3.20. Let $X \subset \mathbb { A } ^ { n }$ be an affine variety, and let $a \in X$ . Show that ${ \mathcal { O } } _ { X , a } \cong { \mathcal { O } } _ { \mathbb { A } ^ { n } , a } / I ( X ) \operatorname { \mathcal { O } } _ { \mathbb { A } ^ { n } , a }$ , where $I ( X ) \mathcal { O } _ { \mathbb { A } ^ { n } , a }$ denotes the ideal in $\mathcal { O } _ { \mathbb { A } ^ { n } , a }$ generated by all quotients $\frac { f } { 1 }$ for $f \in I ( X )$ .

Exercise 3.21. Let $a$ be any point on the real line $\mathbb { R }$ . For which of the following sheaves $\mathcal { F }$ on $\mathbb { R }$ (with the standard topology) is the stalk $\mathcal { F } _ { a }$ actually a local ring in the algebraic sense (i. e. it has exactly one maximal ideal)?

(a) $\mathcal { F }$ is the sheaf of continuous functions;   
(b) $\mathcal { F }$ is the sheaf of locally polynomial functions.

Exercise 3.22. Let $\varphi , \psi \in { \mathcal { F } } ( U )$ be two sections of a sheaf $\mathcal { F }$ on an open subset $U$ of a topological space $X$ . Show:

(a) If $\varphi$ and $\psi$ agree in all stalks, i. e. $\overline { { ( U , \varphi ) } } = \overline { { ( U , \psi ) } } \in \mathcal { F } _ { a }$ for all $a \in U$ , then $\varphi = \psi$ . (b) If $\mathcal { F } = \mathcal { O } _ { X }$ is the sheaf of regular functions on an irreducible affine variety $X$ then we can already conclude that $\varphi = \psi$ if we only know that they agree in one stalk $\mathcal { F } _ { a }$ for $a \in U$ . (c) For a general sheaf $\mathcal { F }$ on a topological space $X$ the statement of (b) is false.

Exercise 3.23. Let $\mathcal { F }$ be a sheaf on a topological space $X$ , and let $Y$ be a non-empty irreducible closed subset of $X$ . We define the stalk of $\mathcal { F }$ at $Y$ to be

$\mathcal { F } _ { Y } : = \{ ( U , \varphi ) : U$ is an open subset of $X$ with $U \cap Y \neq \emptyset$ , and $\varphi \in { \mathcal { F } } ( U ) \} / \sim$ where $( U , \varphi ) \sim ( U ^ { \prime } , \varphi ^ { \prime } )$ if and only if there is an open set $V \subset U \cap U ^ { \prime }$ with $V \cap Y \neq \emptyset$ and $\varphi | _ { V } = \varphi ^ { \prime } | _ { V }$ . It therefore describes functions in an arbitrarily small neighborhood of an arbitrary dense open subset of $Y$ .

If $Y$ is a non-empty irreducible subvariety of an affine variety $X$ , prove that the stalk ${ \mathcal { O } } _ { X , Y }$ of ${ \mathcal { O } } _ { X }$ at $Y$ is a $K$ -algebra isomorphic to the localization $A ( X ) _ { I ( Y ) }$ (hence giving a geometric meaning to this algebraic localization).

Exercise 3.24. Let $\mathcal { F }$ be a sheaf on a topological space $X$ , and let $a \in X$ . Show that the stalk $\mathcal { F } _ { a }$ is a local object in the following sense: If $U \subset X$ is an open neighborhood of $a$ then $\mathcal { F } _ { a }$ is isomorphic to the stalk of $\mathcal { F } | _ { U }$ at $a$ on the topological space $U$ .

# 4. Morphisms

So far we have defined and studied regular functions on an affine variety $X$ . They can be thought of as the morphisms (i. e. the “nice” maps) from open subsets of $X$ to the ground field $K = \mathbb { A } ^ { 1 }$ . We now want to extend this notion of morphisms to maps to other affine varieties than just $\mathbb { A } ^ { 1 }$ (and in fact also to maps between more general varieties in Chapter 5). It turns out that there is a very natural way to define these morphisms once you know what the regular functions are on the source and target variety. So let us start by attaching the data of the regular functions to the structure of an affine variety, or rather more generally of a topological space.

Definition 4.1 (Ringed spaces).

(a) A ringed space is a topological space $X$ together with a sheaf of rings on $X$ . In this situation the given sheaf will always be denoted ${ \mathcal { O } } _ { X }$ and called the structure sheaf of the ringed space. Usually we will write this ringed space simply as $X$ , with the structure sheaf ${ \mathcal { O } } _ { X }$ being understood.   
(b) An affine variety will always be considered as a ringed space together with its sheaf of regular functions as the structure sheaf.   
(c) An open subset $U$ of a ringed space $X$ (e. g. of an affine variety) will always be considered as a ringed space with the structure sheaf being the restriction ${ \mathcal { O } } _ { X } | _ { U }$ as in Definition 3.16.

With this idea that the regular functions make up the structure of an affine variety the obvious idea to define a morphism $f \colon X \to Y$ between affine varieties (or more generally ringed spaces) is now that they should preserve this structure in the sense that for any regular function $\varphi \colon U \to K$ on an open subset $U$ of $Y$ the composition $\varphi \circ f \colon f ^ { - 1 } ( U ) \to K$ is again a regular function.

However, there is a slight technical problem with this approach. Whereas there is no doubt about what the composition $\varphi \circ f$ above should mean for a regular function $\varphi$ on an affine variety, this notion is a priori undefined for general ringed spaces: Recall that in this case by Definition 3.13 the structure sheaves ${ \mathcal { O } } _ { X }$ and ${ \mathcal { O } } _ { Y }$ are given by the data of arbitrary rings ${ \mathcal { O } } _ { X } ( U )$ and ${ \mathcal { O } } _ { Y } ( V )$ for open subsets $U \subset X$ and $V \subset Y$ . So although we usually think of the elements of ${ \mathcal { O } } _ { X } ( U )$ and ${ \mathcal { O } } _ { Y } ( V )$ as functions on $U$ resp. $V$ there is nothing in the definition that guarantees us such an interpretation, and consequently there is no well-defined notion of composing these sections of the structure sheaves with the map $f \colon X \to Y$ . So in order to be able to proceed without too many technicalities let us assume for the moment that all our sheaves are in fact sheaves of functions with some properties:

Convention 4.2 (Sheaves of rings $=$ sheaves of $K \cdot$ -valued functions). From now on until we discuss schemes in Chapter 12, for every sheaf of rings $\mathcal { F }$ on a topological space $X$ we will assume that ${ \mathcal { F } } ( U )$ for any open subset $U \subset X$ is a subring of the ring of all functions from $U$ to $K$ (with the usual pointwise addition and multiplication) containing all constant functions, and that the restriction maps are the ordinary restrictions of such functions. In particular, this makes every such sheaf also into a sheaf of $K \cdot$ -algebras, with the scalar multiplication by elements of $K$ again given by pointwise multiplication. So in short we can say:

Every sheaf of rings is assumed to be a sheaf of $K$ -valued functions.

With this convention we can now go ahead and define morphisms between ringed spaces as motivated above.

Definition 4.3 (Morphisms of ringed spaces). Let $f \colon X \to Y$ be a map of ringed spaces.

(a) For any map $\varphi \colon U \to K$ from an open subset $U$ of $Y$ to the ground field $K$ we denote the composition $\varphi \circ f \colon f ^ { - 1 } ( U ) \to K$ (which is well-defined by Convention 4.2) by $f ^ { * } \varphi$ . It is called the pull-back of $\varphi$ by $f$ .

(b) The map $f$ is called a morphism (of ringed spaces) if it is continuous, and if for all open subsets $U \subset Y$ and $\varphi \in { \mathcal { O } } _ { Y } ( U )$ we have $f ^ { * } \varphi \in { \mathcal { O } } _ { X } ( f ^ { - 1 } ( U ) )$ . So in this case pulling back by $f$ yields $K$ -algebra homomorphisms

$$
f ^ { * } \colon { \mathcal { O } } _ { Y } ( U ) \to { \mathcal { O } } _ { X } ( f ^ { - 1 } ( U ) ) , \ \varphi \mapsto f ^ { * } \varphi .
$$

(c) We say that $f$ is an isomorphism (of ringed spaces) if it has a two-sided inverse, i. e. if it is bijective, and both $f \colon X \to Y$ and $f ^ { - 1 } \colon Y \to X$ are morphisms.

Morphisms and isomorphisms of (open subsets of) affine varieties are morphisms (resp. isomorphisms) as ringed spaces.

# Remark 4.4.

(a) The requirement of $f$ being continuous is necessary in Definition $4 . 3 \ ( \mathbf { b } )$ to formulate the second condition: It ensures that $f ^ { - 1 } ( U )$ is open in $X$ if $U$ is open in Y , i. e. that ${ \mathcal { O } } _ { X } ( f ^ { - 1 } ( U ) )$ is well-defined.   
(b) Without our Convention 4.2, i. e. for ringed spaces without a natural notion of a pull-back of elements of ${ \mathcal { O } } _ { Y } ( U )$ , one would actually have to include suitable ring homomorphisms ${ \mathcal { O } } _ { Y } ( U ) \to { \mathcal { O } } _ { X } ( f ^ { - 1 } ( U ) )$ in the data needed to specify a morphism. In other words, in this case a morphism would no longer be just a set-theoretic map satisfying certain properties. This happens for schemes that we will discuss in Chapter 12 (see Definition 12.26), and it would indeed be the “correct” general notion of morphisms of arbitrary ringed spaces. For the moment however, we will not do this here as it would clearly make our current discussion of morphisms more complicated than necessary.

Remark 4.5 (Properties of morphisms). The following two properties of morphisms are obvious from the definition:

(a) Compositions of morphisms are morphisms: If $f \colon X \to Y$ and $g \colon Y \to Z$ are morphisms of ringed spaces then so is $g \circ f \colon X \to Z$ .   
(b) Restrictions of morphisms are morphisms: If $f \colon X \to Y$ is a morphism of ringed spaces and $U \subset X$ and $V \subset Y$ are open subsets such that $f ( U ) \subset V$ then the restricted map $f | _ { U } \colon U \to V$ is again a morphism of ringed spaces. Conversely, morphisms satisfy a “gluing property” similar to that of a sheaf in Definition 3.13:

Lemma 4.6 (Gluing property for morphisms). Let $f \colon X \to Y$ be a map of ringed spaces. Assume that there is an open cover $\{ U _ { i } : i \in I \}$ of $X$ such that all restrictions $f | _ { U _ { i } } \colon U _ { i } \to Y$ are morphisms. Then $f$ is a morphism.

Proof. By Definition 4.3 (b) we have to check two things:

(a) The map $f$ is continuous: Let $V \subset Y$ be an open subset. Then

$$
f ^ { - 1 } ( V ) = \bigcup _ { i \in I } ( U _ { i } \cap f ^ { - 1 } ( V ) ) = \bigcup _ { i \in I } ( f | _ { U _ { i } } ) ^ { - 1 } ( V ) .
$$

But as all restrictions $f | _ { U _ { i } }$ are continuous the sets $( f | _ { U _ { i } } ) ^ { - 1 } ( V )$ are open in $U _ { i }$ , and hence open in $X$ . So $f ^ { - 1 } ( V )$ is open in $X$ , which means that $f$ is continuous.

Of course, this is just the well-known topological statement that continuity is a local property.

(b) The map $f$ pulls back sections of ${ \mathcal { O } } _ { Y }$ to sections of ${ \mathcal { O } } _ { X }$ : Let $V \subset Y$ be an open subset and $\varphi \in { \mathcal { O } } _ { Y } ( V )$ . Then $( f ^ { * } \varphi ) | _ { U _ { i } \cap f ^ { - 1 } ( V ) } = ( f | _ { U _ { i } \cap f ^ { - 1 } ( V ) } ) ^ { * } \varphi \in \mathcal { O } _ { X } ( U _ { i } \cap f ^ { - 1 } ( V ) )$ since $f | _ { U _ { i } }$ (and thus also $f | _ { U _ { i } \cap f ^ { - 1 } ( V ) }$ by Remark 4.5 (b)) is a morphism. By the gluing property for sheaves in Definition 3.13 this means that $f ^ { * } \varphi \in { \mathcal { O } } _ { X } ( f ^ { - 1 } ( V ) )$ . 

Let us now apply our definition of morphisms to (open subsets of) affine varieties. The following proposition can be viewed as a confirmation that our constructions above were reasonable: As one would certainly expect, a morphism to an affine variety $Y \subset \mathbb { A } ^ { n }$ is simply given by an $n$ -tuple of regular functions whose image lies in $Y$ .

Proposition 4.7 (Morphisms between affine varieties). Let $U$ be an open subset of an affine variety $X$ , and let $Y \subset \mathbb { A } ^ { n }$ be another affine variety. Then the morphisms $f \colon U \to Y$ are exactly the maps of the form

$$
f = ( \varphi _ { 1 } , \ldots , \varphi _ { n } ) \colon U \to Y , x \mapsto ( \varphi _ { 1 } ( x ) , \ldots , \varphi _ { n } ( x ) )
$$

with $\varphi _ { i } \in { \mathcal { O } } _ { X } ( U )$ for all $i = 1 , \ldots , n$ .

In particular, the morphisms from $U$ to $\mathbb { A } ^ { 1 }$ are exactly the regular functions in ${ \mathcal { O } } _ { X } ( U )$

Proof. First assume that $f \colon U \to Y$ is a morphism. For $i = 1 , \ldots , n$ the $i$ -th coordinate function $y _ { i }$ on $Y \subset \mathbb { A } ^ { n }$ is clearly regular on $Y$ , and so $\varphi _ { i } : = f ^ { * } y _ { i } \in { \mathcal { O } } _ { X } ( f ^ { - 1 } ( Y ) ) = { \mathcal { O } } _ { X } ( U )$ by Definition 4.3 (b). But this is just the $i .$ -th component function of $f$ , and so we have $f = \left( \varphi _ { 1 } , \ldots , \varphi _ { n } \right)$ .

Conversely, let now $f = \left( \varphi _ { 1 } , \ldots , \varphi _ { n } \right)$ with $\varphi _ { 1 } , \ldots , \varphi _ { n } \in { \mathcal { O } } _ { X } ( U )$ and $f ( U ) \subset Y$ . First of all $f$ is continuous: Let $Z$ be any closed subset of $Y$ . Then $Z$ is of the form $V ( g _ { 1 } , \ldots , g _ { m } )$ for some $g _ { 1 } , \ldots , g _ { m } \in A ( Y )$ , and

$$
f ^ { - 1 } ( Z ) = \{ x \in U : g _ { i } ( \varphi _ { 1 } ( x ) , \ldots , \varphi _ { n } ( x ) ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } i = 1 , \ldots , m \} .
$$

But the functions $x \mapsto g _ { i } ( \varphi _ { 1 } ( x ) , \ldots , \varphi _ { n } ( x ) )$ are regular on $U$ since locally plugging in quotients of polynomial functions for the variables of a polynomial gives again locally a quotient of polynomial functions. Hence $f ^ { - 1 } ( Z )$ is closed in $U$ by Lemma 3.4, and thus $f$ is continuous. Similarly, if $\varphi \in { \mathcal { O } } _ { Y } ( W )$ is a regular function on some open subset $W \subset Y$ then

$$
f ^ { * } \varphi = \varphi \circ f \colon f ^ { - 1 } ( W ) \to K , x \mapsto \varphi ( \varphi _ { 1 } ( x ) , \ldots , \varphi _ { n } ( x ) )
$$

is regular again, since if we replace the variables in a quotient of polynomial functions by other quotients of polynomial functions we obtain again a quotient of polynomial functions. Hence $f$ is a morphism. 

For affine varieties themselves (rather than their open subsets) we obtain as a consequence the following useful corollary that translates our geometric notion of morphisms entirely into the language of commutative algebra.

Corollary 4.8. For any two affine varieties $X$ and $Y$ there is a bijection

$$
\begin{array} { r c l } { { \{ m o r p h i s m s X  Y \} } } & { { \stackrel { . ! \cdot 1 } { \longleftrightarrow } } } & { { \{ K - a l g e b r a { h o m o m o r p h i s m s A } ( Y )  A ( X ) \} } } \\ { { } } & { { } } & { { f } } & { { \longmapsto } } & { { f ^ { * } . } } \end{array}
$$

In particular, isomorphisms of affine varieties correspond exactly to $K$ -algebra isomorphisms in this way.

Proof. By Definition 4.3 it is clear that any morphism $f \colon X \to Y$ determines a $K$ -algebra homomorphism $f ^ { * } \colon { \mathcal { O } } _ { Y } ( Y ) \to { \mathcal { O } } _ { X } ( X )$ , i. e. $f ^ { * } \colon A ( Y ) \to A ( X )$ by Proposition 3.8.

Conversely, let $g \colon A ( Y ) \to A ( X )$ be a $K$ -algebra homomorphism. Assume that $Y \subset \mathbb { A } ^ { n }$ and denote by $y _ { 1 } , \ldots , y _ { n }$ the coordinate functions of $\mathbb { A } ^ { n }$ . Then $\varphi _ { i } : = g ( y _ { i } ) \in A ( X ) = \varnothing _ { X } ( X )$ for all $i = 1 , \ldots , n$ . If we set $f = ( \varphi _ { 1 } , \ldots , \varphi _ { n } ) \colon X \to { \mathbb { A } } ^ { n }$ then we obtain for any $h \in K [ y _ { 1 } , \ldots , y _ { n } ]$

$$
( f ^ { * } h ) ( x ) = h ( f ( x ) ) = h ( \varphi _ { 1 } ( x ) , \ldots , \varphi _ { n } ( x ) ) { \stackrel { ( * ) } { = } } g ( h ) ( x ) \quad { \mathrm { f o r ~ a l l ~ } } x \in X ,
$$

where $( \ast )$ holds since both sides of the equation are $K$ -algebra homomorphisms in $h$ and equal to $\varphi _ { i } ( x )$ on the generators $y _ { i }$ for $i = 1 , \ldots , n$ of $K [ y _ { 1 } , \ldots , y _ { n } ]$ .

First of all this shows that $h ( f ( x ) ) = 0$ for all $h \in I ( Y )$ , since these polynomials are zero in $A ( Y )$ , so that $g$ vanishes on them. Hence the image of $f$ lies in $V ( I ( Y ) ) = Y$ , i. e. we have constructed a map $f \colon X \to Y$ . As its coordinate functions are regular, it is indeed a morphism by Proposition 4.7, and moreover the above relation shows that $f ^ { * } = g$ so that we get the bijection as stated in the corollary.

The additional statement about isomorphisms now follows immediately since $( f \circ g ) ^ { * } = g ^ { * } \circ f ^ { * }$ and $( g \circ f ) ^ { * } = f ^ { * } \circ g ^ { * }$ for all $f \colon X \to Y$ and $g \colon Y \to X$ . 

Example 4.9 (Isomorphisms $\neq$ bijective morphisms). Let $X = V ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 3 } ) \subset \mathbb { A } ^ { 2 }$ be the cubic curve as in the picture below on the right. It has a singular point at the origin in the sense of [G2, Definition 2.22] (or Definition 10.7 (a)).

Now consider the map

$$
f \colon \mathbb { A } ^ { 1 } \to X , t \mapsto ( t ^ { 3 } , t ^ { 2 } )
$$

which is a morphism by Proposition 4.7. Its corresponding $K$ -algebra homomorphism $f ^ { * } \colon A ( X ) \to A ( \mathbb { A } ^ { 1 } )$ as in Corollary 4.8 is given by

$$
\begin{array} { c } { { K [ x _ { 1 } , x _ { 2 } ] / ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 3 } )  K [ t ] } } \\ { { { } } } \\ { { { \overline { { x _ { 1 } } } } \mapsto t ^ { 3 } } } \\ { { { } } } \\ { { { \overline { { x _ { 2 } } } } \mapsto t ^ { 2 } } } \end{array}
$$

![](images/ac48937a918ddb2cfbc970fc70a20665bb69380c592345e6b62e77405bce0709.jpg)

which can be seen by composing $f$ with the two coordinate functions of $\mathbb { A } ^ { 2 }$ .

Note that $f$ is bijective with inverse map

$$
f ^ { - 1 } \colon X \to { \mathbb { A } } ^ { 1 } , ( x _ { 1 } , x _ { 2 } ) \mapsto { \left\{ \begin{array} { l l } { { \frac { x _ { 1 } } { x _ { 2 } } } } & { { \mathrm { i f ~ } } x _ { 2 } \not = 0 } \\ { 0 } & { { \mathrm { i f ~ } } x _ { 2 } = 0 . } \end{array} \right. }
$$

But $f$ is not an isomorphism (i. e. $f ^ { - 1 }$ is not a morphism), since otherwise by Corollary 4.8 the map $f ^ { * }$ above would have to be an isomorphism as well — which is false since the linear polynomial $t$ is clearly not in its image. So we have to be careful not to confuse isomorphisms with bijective morphisms.

Another consequence of Proposition 4.7 concerns our definition of the product $X \times Y$ of two affine varieties $X$ and $Y$ in Example 1.5 (d). Recall from Example 2.4 (c) that $X \times Y$ does not carry the product topology — which might seem strange at first. The following proposition however justifies this choice, since it shows that our definition of the product satisfies the so-called universal property that giving a morphism to $X \times Y$ is the same as giving a morphism each to $X$ and $Y$ . In fact, when we introduce more general varieties in the next chapter we will define their products using this certainly desirable universal property.

Proposition 4.10 (Universal property of products). Let $X$ and $Y$ be affine varieties, and let $\pi _ { X } \colon X \times Y \to X$ and $\pi _ { Y } \colon X \times Y \to Y$ be the projection morphisms from the product onto the two factors. Then for every affine variety $Z$ and two morphisms $f _ { X } \colon Z \to X$ and $f _ { Y } \colon Z \to Y$ there is a unique morphism $f \colon Z \to X \times Y$ such that $f _ { X } = \pi _ { X } \circ f$ and $f _ { Y } = \pi _ { Y } \circ f$ . In other words, giving a morphism from an affine variety to the product $X \times Y$ is the same as giving a morphism to each of the factors $X$ and $Y$ .

$$
\begin{array}{c} \begin{array} { l } { Z \xrightarrow [ \displaystyle \prod _ { \begin{array} { c } { Y } \\ { Y } \\ { Y } \end{array} } ] { \overset { f _ { X } } { \sim } } \mathrm { ~ } } \\ { f _ { Y } \xrightarrow [ \end{array} } \left. \begin{array} { c } { X \times Y } \\ { \overline { { \pi _ { X } } } ^ { \star } } \\ { \pi _ { Y } } \\ { Y } \end{array} \right.  \end{array}
$$

Proof. Obviously, the only way to obtain the relations $f _ { X } = \pi _ { X } \circ f$ and $f _ { Y } = \pi _ { Y } \circ f$ is to take the map $f \colon Z \to X \times Y$ , $z \mapsto ( f _ { X } ( z ) , f _ { Y } ( z ) )$ . But this is clearly a morphism by Proposition 4.7: As $f _ { X }$ and $f _ { Y }$ must be given by regular functions in each coordinate, the same is then true for $f$ . 

Remark 4.11 (Coordinate ring of a product). The universal property of the product in Proposition 4.10 corresponds exactly to the universal property of tensor products using the translation between morphisms of affine varieties and $K$ -algebra homomorphisms of Corollary 4.8. Hence the coordinate ring $A ( X \times Y )$ of the product is just the tensor product $A ( X ) \otimes _ { K } A ( Y )$ .

Exercise 4.12 (Affine conics). An irreducible quadric curve in $\mathbb { A } ^ { 2 }$ is also called an affine conic. Show that every affine conic over a field of characteristic not equal to 2 is isomorphic to exactly one of the varieties $X _ { 1 } = V \big ( x _ { 2 } - x _ { 1 } ^ { 2 } \big )$ and $X _ { 2 } = V \big ( x _ { 1 } x _ { 2 } - 1 \big )$ , with an isomorphism given by a linear coordinate transformation followed by a translation.

Exercise 4.13. Let $f \colon X \to Y$ be a morphism of affine varieties and $f ^ { * } \colon A ( Y ) \to A ( X )$ the corresponding homomorphism of the coordinate rings. Are the following statements true or false?

(a) $f$ is surjective if and only if $f ^ { * }$ is injective.   
(b) $f$ is injective if and only if $f ^ { * }$ is surjective.   
(c) If $f \colon \mathbb { A } ^ { 1 } \to \mathbb { A } ^ { 1 }$ is an isomorphism then $f$ is affine linear, i. e. of the form $f ( x ) = a x + b$ for some $a , b \in K$ .   
(d) If $f \colon \mathbb { A } ^ { 2 } \to \mathbb { A } ^ { 2 }$ is an isomorphism then $f$ is affine linear, i. e. it is of the form $f ( x ) = A x + b$ for some $A \in \mathbf { M a t } ( 2 \times 2 , K )$ and $b \in K ^ { 2 }$ .

Construction 4.14 (Affine varieties from finitely generated reduced $K$ -algebras). Corollary 4.8 allows us to construct affine varieties in a different way: Let $R$ be a finitely generated $K$ -algebra, and assume that it is reduced, i. e. that it has no nilpotent elements. We can then pick generators $a _ { 1 } , \ldots , a _ { n }$ for $R$ and obtain a surjective $K$ -algebra homomorphism

$$
g \colon K [ x _ { 1 } , \ldots , x _ { n } ] \to R , f \mapsto f ( a _ { 1 } , \ldots , a _ { n } ) .
$$

By the homomorphism theorem we therefore see that $R \cong K [ x _ { 1 } , \ldots , x _ { n } ] / J .$ , where $J$ is the kernel of $g$ . Moreover, $J$ is a radical ideal as we have assumed $R$ to be reduced. Hence $X = V ( J )$ is an affine variety in $\mathbb { A } ^ { n }$ with coordinate ring $A ( X ) \cong R$ .

Note that this construction of $X$ from $R$ depends on the choice of generators of $R$ , and so we can get different affine varieties that way. However, Corollary 4.8 implies that all these affine varieties will be isomorphic since they have isomorphic coordinate rings — they just differ in their embeddings in affine spaces.

This motivates us to make a (very minor) redefinition of the term “affine variety” to allow for objects that are isomorphic to an affine variety in the old sense, but that do not come with an intrinsic description as the zero locus of some polynomials in a fixed affine space.

Definition 4.15 (Slight redefinition of affine varieties). From now on, an affine variety will be a ringed space that is isomorphic to an affine variety in the old sense of Definition 1.2 (b).

Remark 4.16. With this new definition, the result of Construction 4.14 can be reformulated by saying that there is a natural bijection

{affine varieties}/isomorphisms $\stackrel { 1 : 1 } { \longleftrightarrow }$ {finitely generated reduced $K$ -algebras}/isomorphisms that also extends to morphisms, i. e. morphisms of affine varieties correspond exactly to homomorphisms of $K$ -algebras in this picture.

Note that all our concepts and results immediately carry over to an affine variety $X$ in this new sense: For example, all topological concepts are defined as $X$ is still a topological space, regular functions are just sections of the structure sheaf ${ \mathcal { O } } _ { X }$ , the coordinate ring $A ( X )$ can be considered to be ${ \mathcal { O } } _ { X } ( X )$ by Proposition 3.8, and products involving $X$ can be defined using any embedding of $X$ in affine space (yielding a product that is unique up to isomorphisms).

Probably the most important examples of affine varieties in this new sense that do not look like affine varieties a priori are the distinguished open subsets of Definition 3.6:

Proposition 4.17 (Distinguished open subsets are affine varieties). Let $X$ be an affine variety, and let $f \in A ( X )$ . Then the distinguished open subset $D ( f )$ is an affine variety with coordinate ring $A ( D ( f ) ) = A ( X ) _ { f }$ .

Proof. Clearly,

$$
Y : = \{ ( x , t ) \in X \times \mathbb { A } ^ { 1 } : t f ( x ) = 1 \} \quad \subset X \times \mathbb { A } ^ { 1 }
$$

is an affine variety as it is the zero locus of the polynomial $t f ( x ) - 1$ in the affine variety $\boldsymbol { X } \times \mathbb { A } ^ { 1 }$ . It is isomorphic to $D ( f )$ by the map

$$
f \colon Y \to D ( f ) , ( x , t ) \mapsto x \qquad { \mathrm { w i t h ~ i n v e r s e } } \qquad f ^ { - 1 } \colon D ( f ) \to Y , x \mapsto \left( x , { \frac { 1 } { f ( x ) } } \right) .
$$

So $D ( f )$ is an affine variety, and by Proposition 3.8 and Corollary 3.10 we see that its coordinate ring is $A ( D ( f ) ) = \mathcal { O } _ { X } ( D ( f ) ) = A ( X ) _ { f }$ . 

Example 4.18 $( \mathbb { A } ^ { 2 } \backslash \{ 0 \}$ is not an affine variety). As in Example 3.11 let $X = \mathbb { A } ^ { 2 }$ and consider the open subset $U = \mathbb { A } ^ { 2 } \backslash \{ 0 \}$ of $X$ . Then even in the new sense of Definition 4.15 the ringed space $U$ is not an affine variety: Otherwise its coordinate ring would be ${ \mathcal { O } } _ { X } ( U )$ by Proposition 3.8, and thus just the polynomial ring $K [ x , y ]$ by Example 3.11. But this is the same as the coordinate ring of $X = \mathbb { A } ^ { 2 }$ , and hence Corollary 4.8 would imply that $U$ and $X$ are isomorphic, with the isomorphism given by the identity map. This is obviously not true, and hence we conclude that $U$ is not an affine variety.

However, we can cover $U$ by the two (distinguished) open subsets

$$
D ( x _ { 1 } ) = \{ ( x _ { 1 } , x _ { 2 } ) : x _ { 1 } \neq 0 \} \quad { \mathrm { a n d } } \quad D ( x _ { 2 } ) = \{ ( x _ { 1 } , x _ { 2 } ) : x _ { 2 } \neq 0 \}
$$

which are affine by Proposition 4.17. This leads us to the idea that we should also consider ringed spaces that can be patched together from affine varieties. We will do this in the next chapter.

Exercise 4.19. Which of the following ringed spaces are isomorphic over $\mathbb { C } ^ { \epsilon }$ ?

(a) $\begin{array} { r l } & { \mathbb { A } ^ { 1 } \backslash \{ 1 \} } \\ & { V ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } ) \subset \mathbb { A } ^ { 2 } } \\ & { V ( x _ { 2 } - x _ { 1 } ^ { 2 } , x _ { 3 } - x _ { 1 } ^ { 3 } ) \backslash \{ 0 \} \subset \mathbb { A } ^ { 3 } } \end{array}$ (d) $\begin{array} { r l } & { V \big ( x _ { 1 } x _ { 2 } \big ) \subset \mathbb { A } ^ { 2 } } \\ & { V \big ( x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 3 } - x _ { 1 } ^ { 2 } \big ) \subset \mathbb { A } ^ { 2 } } \\ & { V \big ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - 1 \big ) \subset \mathbb { A } ^ { 2 } } \end{array}$ (b) (e) (c) (f)

# 5. Varieties

In this chapter we will now finally introduce the main objects of study in this class, the so-called varieties. As already announced in Example 4.18 they will be spaces that are not necessarily affine varieties themselves, but that can be covered by affine varieties. This idea is completely analogous to the definition of manifolds: Recall that to construct them one first considers open subsets of $\mathbb { R } ^ { n }$ that are supposed to form the patches of your space, and then defines a manifold to be a topological space that looks locally like these patches. In our algebraic case we can say that the affine varieties form the basic patches of the spaces that we want to consider, and that general varieties are then spaces that look locally like affine varieties.

One of the main motivations for this generalization is that in the classical topology affine varieties over $\mathbb { C }$ are never bounded, and hence never compact, unless they are a finite set (see Exercise 2.36 (b)). As compact spaces are usually better-behaved than non-compact ones, it is therefore desirable to have a method to compactify an affine variety by “adding some points at infinity”. Technically, this can be achieved by gluing it to other affine varieties that contain the points at infinity. The complete space can then obviously be covered by affine varieties. We will see this explicitly in Example 5.5 (a), and much more generally when we construct projective varieties in Chapters 6 and 7.

So let us start by defining spaces that can be covered by affine varieties. They are called prevarieties since we will want to impose another condition on them later in Definition 5.17, which will then make them into varieties.

Definition 5.1 (Prevarieties). A prevariety is a ringed space $X$ that has a finite open cover by affine varieties. Morphisms of prevarieties are simply morphisms as ringed spaces. In accordance with Definition 3.1, the elements of ${ \mathcal { O } } _ { X } ( U )$ for an open subset $U \subset X$ will be called regular functions on $U$ .

Remark 5.2. Note that the open cover in Definition 5.1 is not part of the data needed to specify a prevariety — it is just required that such a cover exists. Any open subset of a prevariety that is an affine variety is called an affine open set.

Example 5.3. Of course, any affine variety is a prevariety. More generally, every open subset of an affine variety is a prevariety: It has a finite open cover by distinguished open subsets by Remark 3.7 (b), and these are affine open sets by Proposition 4.17.

The basic way to construct new prevarieties is to glue them together from previously known patches.   
For simplicity, let us start with the case when we only have two spaces to glue.

Construction 5.4 (Gluing two prevarieties). Let $X _ { 1 } , X _ { 2 }$ be two prevarieties (e. g. affine varieties), and let $U _ { 1 , 2 } \subset X _ { 1 }$ and $U _ { 2 , 1 } \subset X _ { 2 }$ be open subsets. Moreover, let $f \colon U _ { 1 , 2 } \to U _ { 2 , 1 }$ be an isomorphism. Then we can define a prevariety $X$ obtained by gluing $X _ { 1 }$ and $X _ { 2 }$ along $f$ , as shown in the picture below.

![](images/1b1ad8c8ccbe77552eab8e1a76f40ef58ed9facdd80b459dedb4398cde71ceff.jpg)

• As a set, the space $X$ is just the disjoint union $X _ { 1 } \cup X _ { 2 }$ modulo the equivalence relation given by $a \sim f ( a )$ and $f ( a ) \sim a$ for all $a \in U _ { 1 , 2 }$ (in addition to $a \sim a$ for all $a \in X _ { 1 } \cup X _ { 2 }$ ). Note that there are then natural embeddings $i _ { 1 } \colon X _ { 1 } \to X$ and $i _ { 2 } \colon X _ { 2 } \to X$ that map a point to its equivalence class in $X _ { 1 } \cup X _ { 2 }$ .

• As a topological space, we call a subset $U \subset X$ open if $i _ { 1 } ^ { - 1 } ( U ) \subset X _ { 1 }$ and $i _ { 2 } ^ { - 1 } ( U ) \subset X _ { 2 }$ are open. In topology, this is usually called the quotient topology of the two maps $i _ { 1 }$ and $i _ { 2 }$ .

• As a ringed space, we define the structure sheaf ${ \mathcal { O } } _ { X }$ by

$$
{ \mathcal { O } } _ { X } ( U ) = \{ \varphi \colon U \to K \colon i _ { 1 } ^ { * } \varphi \in { \mathcal { O } } _ { X _ { 1 } } ( i _ { 1 } ^ { - 1 } ( U ) ) { \mathrm { ~ a n d ~ } } i _ { 2 } ^ { * } \varphi \in { \mathcal { O } } _ { X _ { 2 } } ( i _ { 2 } ^ { - 1 } ( U ) ) \}
$$

for all open subsets $U \subset X$ , where $i _ { 1 } ^ { * }$ and $i _ { 2 } ^ { * }$ denote the pull-backs of Definition 4.3 (a). Intuitively, this means that a function on the glued space is regular if it is regular when restricted to both patches. It is obvious that this defines a sheaf on $X$ .

With this construction it is checked immediately that the images of $i _ { 1 }$ and $i _ { 2 }$ are open subsets of $X$ that are isomorphic to $X _ { 1 }$ and $X _ { 2 }$ . We will often drop the inclusion maps from the notation and say that $X _ { 1 }$ and $X _ { 2 }$ are open subsets of $X$ . Since $X _ { 1 }$ and $X _ { 2 }$ can be covered by affine open subsets, the same is true for $X$ , and thus $X$ is a prevariety.

Example 5.5. As the simplest example of the above gluing construction, let $X _ { 1 } = X _ { 2 } = \mathbb { A } ^ { 1 }$ and $U _ { 1 , 2 } = U _ { 2 , 1 } = \mathbb { A } ^ { 1 } \backslash \{ 0 \}$ in the notation of Construction 5.4. We consider two different choices of gluing isomorphism $f \colon U _ { 1 , 2 } \to U _ { 2 , 1 }$ :

(a) Let $f \colon U _ { 1 , 2 } \to U _ { 2 , 1 }$ , $\textstyle x \mapsto { \frac { 1 } { x } }$ . By construction, the affine line $X _ { 1 } = \mathbb { A } ^ { 1 }$ is an open subset of $X$ . Its complement $X \backslash X _ { 1 } = X _ { 2 } \backslash U _ { 2 , 1 }$ is a single point that corresponds to 0 in $X _ { 2 }$ and therefore to $\mathrm { \Sigma } ^ { \infty } \infty = \frac { 1 } { 0 } \mathrm { \Delta } ^ { \mathrm { , , } }$ in the coordinate of $X _ { 1 }$ . Hence we can think of the glued space $X$ as $\mathbb { A } ^ { 1 } \cup \{ \infty \}$ , and thus as a “compactification” of the affine line. We denote it by $\mathbb { P } ^ { 1 }$ ; it is a special case of the projective spaces that we know already from [G2, Chapter 3] and that we will construct as prevarieties in Chapters 6 and 7 (see Exercise 7.3 (a)).

In the case $K = \mathbb { C }$ the resulting space $X$ is just the Riemann sphere $\mathbb { C } \cup \{ \infty \}$ . Its subset of real points is shown in the picture below (with the dotted arrows indicating the gluing isomorphism), it is homeomorphic to a circle.

![](images/659ab9e6c5886c7d44f6e83d562f9f6a82a9cf2e4578f33531a5f24b5a70ee87.jpg)

As an example of gluing morphisms as in Lemma 4.6, the morphisms

$$
X _ { 1 } \to X _ { 2 } \subset \mathbb { P } ^ { 1 } , \ x \mapsto x \quad { \mathrm { a n d } } \quad X _ { 2 } \to X _ { 1 } \subset \mathbb { P } ^ { 1 } , \ x \mapsto x
$$

(that correspond to a reflection across the horizontal axis in the picture above) glue together to a single morphism $\mathbb { P } ^ { 1 } \to \mathbb { P } ^ { 1 }$ that can be thought of as $\textstyle x \mapsto { \frac { 1 } { x } }$ in the interpretation of $\mathbb { P } ^ { 1 }$ as $\mathbb { A } ^ { 1 } \cup \{ \infty \}$ .

(b) Let $f \colon U _ { 1 , 2 } \to U _ { 2 , 1 }$ be the identity map. Then the space $X$ obtained by gluing $X _ { 1 }$ and $X _ { 2 }$ along $f$ is shown in the picture below, it is “an affine line with two zero points”.

$$
{ \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c } { - 3 } & { - 2 } & { - 1 } & { 0 } & { 1 } & { 2 } & { 3 } & { \qquad } & { \underline { { \operatorname { g l u e } } } } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } \\ { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } & { \vdots } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } \\ { \vdots } & { \vdots } & { \vdots } & { } & { } & { \vdots } & { \vdots } & { \vdots } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } \\ { - 3 } & { - 2 } & { - 1 } & { 0 } & { 1 } & { 2 } & { } & { 3 } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } \end{array} }
$$

Obviously this is a somewhat weird space. Speaking in analytic terms in the case $K = \mathbb { C }$ , a sequence of points tending to zero would have two possible limits in $X$ , namely the two zero points. Also, as in (a) the two morphisms

$$
X _ { 1 } \to X _ { 2 } \subset X , x \mapsto x \quad { \mathrm { a n d } } \quad X _ { 2 } \to X _ { 1 } \subset X , x \mapsto x
$$

glue again to a morphism $g \colon X \to X$ ; this time it exchanges the two zero points and thus leads to the set $\{ x \in X : g ( x ) = x \} = \mathbb { A } ^ { 1 } \backslash \{ 0 \}$ not being closed in $X$ , although it is given by an equality of continuous maps.

Usually we want to exclude such spaces from the objects we consider. In Definition 5.17 we will therefore impose an additional condition on our prevarieties that ensures that the above phenomena do not occur (see e. g. Proposition 5.19 (b)).

Let us now turn to the general construction to glue more than two spaces together. In principle this works in the same way as in Construction 5.4; we just have an additional technical compatibility condition on the gluing isomorphisms.

Construction 5.6 (General gluing construction). For a finite index set $I$ let $X _ { i }$ be a prevariety for all $i \in I$ . Moreover, as in the picture below suppose that for all $i , j \in I$ with $i \neq j$ we are given open subsets $U _ { i , j } \subset X _ { i }$ and isomorphisms $f _ { i , j } \colon U _ { i , j } \to U _ { j , i }$ such that for all distinct $i , j , k \in I$ we have

(a) $f _ { j , i } = f _ { i , j } ^ { - 1 }$ ;   
(b) $U _ { i , j } \cap f _ { i , j } ^ { - 1 } ( U _ { j , k } ) \subset U _ { i , k }$ , and $f _ { j , k } \circ f _ { i , j } = f _ { i , k }$ on $U _ { i , j } \cap f _ { i , j } ^ { - 1 } ( U _ { j , k } )$ . (Note that the initial set-theoretic condition just says that the domain of definition of $f _ { j , k } \circ f _ { i , j }$ is included in the domain of definition of $f _ { i , k }$ , i. e. if we glue a point in $X _ { i }$ via $f _ { i , j }$ and $f _ { j , k }$ to a point in $X _ { k }$ , we also do so directly via $f _ { i , k } )$ .

![](images/4a1ec6c0425afc8d074a89310d7e421d628ee012876c96c270ccac811132ff73.jpg)

In analogy to Construction 5.4 we can then define a set $X$ by taking the disjoint union of all $X _ { i }$ for $i \in I$ , modulo the equivalence relation $a \sim f _ { i , j } ( a )$ for all $a \in U _ { i , j } \subset X _ { i }$ (in addition to $a \sim a$ for all $a$ ). In fact, the conditions (a) and (b) above ensure precisely that this relation is symmetric and transitive, respectively. It is obvious that we can now make $X$ into a prevariety by defining its topology and structure sheaf in the same way as in Construction 5.4. We call it the prevariety obtained by gluing the $X _ { i }$ along the isomorphisms $f _ { i , j }$ .

# Exercise 5.7. Show:

(a) Every morphism $f \colon \mathbb { A } ^ { 1 } \backslash \{ 0 \}  \mathbb { P } ^ { 1 }$ can be extended to a morphism $\mathbb { A } ^ { 1 } \to \mathbb { P } ^ { 1 }$ .   
(b) Not every morphism $f \colon \mathbb { A } ^ { 2 } \backslash \{ 0 \}  \mathbb { P } ^ { 1 }$ can be extended to a morphism $\mathbb { A } ^ { 2 } \to \mathbb { P } ^ { 1 }$ .   
(c) Every morphism $f \colon  { \mathbb { P } } ^ { 1 } \to  { \mathbb { A } } ^ { 1 }$ is constant.

# Exercise 5.8.

(a) Show at every isomorphism $f \colon { \mathbb { P } } ^ { 1 } \to { \mathbb { P } } ^ { 1 }$ is of the form $\textstyle f ( x ) = { \frac { a x + b } { c x + d } }$ for some $a , b , c , d \in K$ $x$ $\mathbb { A } ^ { 1 } \subset \mathbb { P } ^ { 1 }$

(b) Given three distinct points $a _ { 1 } , a _ { 2 } , a _ { 3 } \in \mathbb { P } ^ { 1 }$ and three distinct points $b _ { 1 } , b _ { 2 } , b _ { 3 } \in \mathbb { P } ^ { 1 }$ , show that there is a unique isomorphism $f \colon { \mathbb { P } } ^ { 1 } \to { \mathbb { P } } ^ { 1 }$ such that $f ( a _ { i } ) = b _ { i }$ for $i = 1 , 2 , 3$ .

Exercise 5.9. If $X$ and $Y$ are affine varieties we have seen in Proposition 3.8 and Corollary 4.8 that there is a bijection

$$
\begin{array} { r } { \{ \operatorname { m o r p h i s m s } X  Y \} \stackrel { \cdot \cdot \lambda \cdot } { \longleftrightarrow } \{ K \mathrm { - a l g e b r a \ h o m o m o r p h i s m s } \ O _ { Y } ( Y )  \mathcal O _ { X } ( X ) \} } \\ { f \longmapsto f ^ { * } . } \end{array}
$$

Does this statement still hold (a) if $X$ is an arbitrary prevariety (but $Y$ is still affine); (b) if $Y$ is an arbitrary prevariety (but $X$ is still affine)?

We have just seen how we can construct prevarieties by gluing affine varieties. For the rest of the chapter let us now study some of their basic properties. Of course, all topological concepts (like connectedness, irreducibility, and dimension) carry over immediately to the case of prevarieties. The irreducible decomposition of Proposition 2.14 is also applicable since a prevariety is always Noetherian by Exercise 2.19 (b). As for properties of prevarieties involving the structure as ringed spaces, we should first of all figure out to what extent their subsets, images and inverse images under morphisms, and products are again prevarieties.

Construction 5.10 (Open and closed subprevarieties). Let $X$ be a prevariety.

(a) Let $U \subset X$ be an open subset. Then $U$ is again a prevariety (as usual with the structure sheaf $\mathcal { O } _ { U } = \mathcal { O } _ { X } | _ { U }$ as in Definition 4.1 (c)): As $X$ can be covered by affine varieties, $U$ can be covered by open subsets of affine varieties, which themselves can be covered by affine varieties by Example 5.3. We call $U$ (with this structure as a prevariety) an open subprevariety of $X$ .   
(b) The situation is more complicated for a closed subset $Y \subset X$ : As an open subset $U$ of $Y$ is in general not open in $X$ we cannot define a structure sheaf on $Y$ by simply setting ${ \mathcal { O } } _ { Y } ( U )$ to be ${ \mathcal { O } } _ { X } ( U )$ . Instead, we define ${ \mathcal { O } } _ { Y } ( U )$ to be the $K$ -algebra of functions $U \to K$ that are locally restrictions of functions on $X$ , or formally ${ \mathcal { O } } _ { Y } ( U ) : = \{ \varphi \colon U \to K :$ for all $a \in U$ there are an open neighborhood $V$ of $a$ in $X$ and $\psi \in { \mathcal { O } } _ { X } ( V )$ with $\varphi = \psi$ on $U \cap V  \big \}$ .

By the local nature of this definition it is obvious that ${ \mathcal { O } } _ { Y }$ is a sheaf, thus making $Y$ into a ringed space. In fact, we will check in Exercise 5.11 that $Y$ is a prevariety in this way. We call it a closed subprevariety of $X$ .

Note that for a general subset of $X$ there is no way to make it into a prevariety in a natural way. Even worse, the notions of open and closed subprevarieties do not mix very well: Whereas a finite union of open (resp. closed) subprevarieties is of course again an open (resp. closed) subprevariety, the same statement is not true if we try to combine open with closed spaces. For example, in $X = \mathbb { A } ^ { 2 }$ the union of the open subprevariety $U = \bar { \mathbb { A } } ^ { 1 } \times ( \mathbb { A } ^ { 1 } \backslash \{ 0 \} )$ and the closed subprevariety $Y = \{ 0 \}$ as in the picture on the right does not have a natural structure as a subprevariety of $\mathbb { A } ^ { 2 }$ (since it does not look like an affine variety in a neighborhood of the origin).

![](images/23467cb4d33c9b81f95c0cec70905e362fc813e274d5dfdefef65a5318aa1690.jpg)

Exercise 5.11. Let $Y$ be a closed subset of a prevariety $X$ , considered as a ringed space with the structure sheaf of Construction 5.10 (b). Prove for every affine open subset $U \subset X$ that the ringed space $U \cap Y$ (considered as an open subset of the ringed space $Y$ as in Definition 4.1 (c)) is isomorphic to the affine variety $U \cap Y$ (considered as an affine subvariety of the affine variety $U$ ).

In particular, this shows that Construction 5.10 (b) makes $Y$ into a prevariety, and that this prevariety is isomorphic to the affine variety $Y$ if $X$ is itself affine (and thus $Y$ an affine subvariety of $X$ ).

Remark 5.12 (Properties of closed subprevarieties). By Construction 5.10 (b), a regular function on (an open subset of) a closed subprevariety $Y$ of a prevariety $X$ is locally the restriction of a regular function on $X$ . Hence:

(a) The inclusion map $Y  X$ is a morphism (it is clearly continuous, and regular functions on $X$ are by construction still regular when restricted to Y ).   
(b) If $f \colon Z \to X$ is a morphism from a prevariety $Z$ such that $f ( Z ) \subset Y$ then we can also regard $f$ as a morphism from $Z$ to $Y$ (the pull-back of a regular function on $Y$ by $f$ is locally also a pull-back of a regular function on $X$ , and hence regular as $f \colon Z \to X$ is a morphism).

Remark 5.13 (Images and inverse images of subprevarieties). Let $f \colon X \to Y$ be a morphism of prevarieties.

(a) The image of an open or closed subprevariety of $X$ under $f$ is not necessarily an open or closed subprevariety of Y . For example, for the affine variety $X = V ( x _ { 2 } x _ { 3 } - 1 ) \cup \{ 0 \} \subset \mathbb { A } ^ { 3 }$ and the projection morphism $f \colon X \to \mathbb { A } ^ { 2 }$ onto the first two coordinates the image $f ( X )$ is exactly the space $\mathbb { A } ^ { 1 } \times ( \mathbb { A } ^ { 1 } \backslash \{ 0 \} ) \cup \{ 0 \}$ of Construction 5.10 which is neither an open nor a closed subprevariety of $\mathbb { A } ^ { 2 }$ . As a substitute, one can often consider the graph of $f$ instead of its image, see Proposition 5.19 (a).   
(b) By continuity, the inverse image of an open (resp. closed) subprevariety of $Y$ under $f$ is clearly again an open (resp. closed) subprevariety of $X$ .

As for the product $X \times Y$ of two prevarieties $X$ and $Y$ , the natural idea to construct this space as a prevariety would be to choose finite affine open covers $\{ U _ { i } : i \in I \}$ and $\{ V _ { j } : j \in J \}$ of $X$ and $Y$ , respectively, and then glue the affine product varieties $U _ { i } \times V _ { j }$ using Construction 5.6. If we did this directly however, we would still have to prove that the resulting space does not depend on the chosen affine covers. The best way out of this trouble is to define the product prevariety by a universal property analogous to Proposition 4.10. This will then ensure the uniqueness of the product, so that it suffices to prove its existence by gluing affine patches.

Definition 5.14 (Products of prevarieties). Let $X$ and $Y$ be prevarieties. A product of $X$ and $Y$ is a prevariety $P$ together with morphisms $\pi _ { X } \colon P \to X$ and $\pi _ { Y } \colon P \to Y$ satisfying the following universal property: For any two morphisms $f _ { X } \colon Z \to X$ and $f _ { Y } \colon Z \to Y$ from another prevariety $Z$ there is a unique morphism $f \colon Z \to P$ such that $\pi _ { X } \circ f = f _ { X }$ and $\pi _ { Y } \circ f = f _ { Y }$ .

As in the affine case in Proposition 4.10, this means that giving a morphism to the product $P$ is the same as giving a morphism to each of the factors $X$ and $Y$ .

$$
{ \begin{array} { l } { { \boldsymbol { Z } } } \\ { \displaystyle \qquad et { } { ' } { \left. \right.} \sum _ { { P } \atop { P } } et { } { ' }  _ { \begin{array} { l } { X } \\ { X } \end{array} } } \\ { \qquad \displaystyle \ s \left( { \boldsymbol { \pi } } _ { { X } } ^ { \phantom { * } } \cdot { \boldsymbol { X } } \right) } \\ { \qquad \displaystyle \ s \left( { \boldsymbol { \pi } } _ { { Y } } ^ { \phantom { * } } \cdot { \boldsymbol { X } } \right) } \end{array} }
$$

Proposition 5.15 (Existence and uniqueness of products). Any two prevarieties $X$ and $Y$ have a product. Moreover, this product $P$ with morphisms $\pi _ { X } \colon P \to X$ and $\pi _ { Y } \colon P \to Y$ is unique up to unique isomorphism: If $P ^ { \prime }$ with $\pi _ { X } ^ { \prime } \colon P ^ { \prime } \to X$ and $\pi _ { Y } ^ { \prime } \colon P ^ { \prime } \to Y$ is another product there is a unique isomorphism $f \colon P ^ { \prime } \to P$ such that $\pi _ { X } \circ f = \pi _ { X } ^ { \prime }$ and $\pi _ { Y } \circ f = \pi _ { Y } ^ { \prime }$ .

We will denote this product simply by $X \times Y$

Proof. To show existence we glue the affine products of Proposition 4.10 using Construction 5.6. More precisely, let $X$ and $Y$ be covered by affine varieties $U _ { 1 } , \dots , U _ { n }$ and $V _ { 1 } , \ldots , V _ { m }$ , respectively. We glue the affine products $U _ { i } \times V _ { j }$ for all $i = 1 , \ldots , n$ and $j = 1 , \ldots , m$ , where we glue any two such products $U _ { i } \times V _ { j }$ and $U _ { i ^ { \prime } } \times V _ { j ^ { \prime } }$ along the identity isomorphism of the common open subset $\left( U _ { i } \cap U _ { i ^ { \prime } } \right) \times \left( V _ { j } \cap V _ { j ^ { \prime } } \right)$ . Note that these isomorphisms obviously satisfy the conditions (a) and (b) of the construction, and that the resulting glued space $P$ is set-theoretically just the usual product $X \times Y$ . Moreover, using Lemma 4.6 we can glue the affine projection morphisms $U _ { i } \times V _ { j } \to U _ { i } \subset X$ and $U _ { i } \times V _ { j } \to V _ { j } \subset Y$ to morphisms $\pi _ { X } \colon P \to X$ and $\pi _ { Y } \colon P \to Y$ .

Let us now check the universal property of Definition 5.14 for our construction. If $f _ { X } \colon Z \to X$ and $f _ { Y } \colon Z \to Y$ are any two morphisms from a prevariety $Z$ , the only way to achieve $\pi _ { X } \circ f = f _ { X }$ and $\pi _ { Y } \circ f = f _ { Y }$ is to define $f \colon Z \to P$ as $f ( z ) = ( f _ { X } ( z ) , f _ { Y } ( z ) )$ , where we identify $P$ set-theoretically with $X \times Y$ . By Lemma 4.6, we can check that this is a morphism by restricting it to an affine open cover. If we first cover $Z$ by the open subsets $f _ { X } ^ { - 1 } ( U _ { i } ) \cap f _ { Y } ^ { - 1 } ( V _ { j } )$ for all $i \in I$ and $j \in J$ , and these subsets then by affine open subsets by Construction 5.10 (a), we may assume that every affine open subset in our open cover of $Z$ is mapped to a single (and hence affine) patch $U _ { i } \times V _ { j }$ . But after this restriction to the affine case we know by Proposition 4.10 that $f$ is a morphism.

To show uniqueness, assume that $P ^ { \prime }$ with $\pi _ { X } ^ { \prime } \colon P ^ { \prime } \to X$ and $\pi _ { Y } ^ { \prime } \colon P ^ { \prime } \to Y$ is another product. By the universal property of $P$ applied to the morphisms $\pi _ { X } ^ { \prime } \colon P ^ { \prime } \to X$ and $\pi _ { Y } ^ { \prime } \colon P ^ { \prime } \to Y$ , we see that there is a unique morphism $f \colon P ^ { \prime } \to P$ with $\pi _ { X } \circ f = \pi _ { X } ^ { \prime }$ and $\pi _ { Y } \circ f = \pi _ { Y } ^ { \prime }$ . Reversing the roles of the two products, we get in the same way a unique morphism $g \colon P \to P ^ { \prime }$ with $\pi _ { X } ^ { \prime } \circ g = \pi _ { X }$ and $\pi _ { Y } ^ { \prime } \circ g = \pi _ { Y }$ .

Finally, apply the universal property of $P$ to the two morphisms $\pi _ { X } \colon P \to X$ and $\pi _ { Y } \colon P \to Y$ . Since both

$$
\begin{array} { r } { \begin{array} { c c c c c c } { \pi _ { X } \circ ( f \circ g ) = \pi _ { X } ^ { \prime } \circ g = \pi _ { X } } & & { \mathrm { ~ a n d ~ } } & & { \pi _ { X } \circ \mathrm { i d } _ { P } = \pi _ { X } } \\ { \pi _ { Y } \circ ( f \circ g ) = \pi _ { Y } ^ { \prime } \circ g = \pi _ { Y } } & & { \mathrm { ~ a n d ~ } } & & { \pi _ { Y } \circ \mathrm { i d } _ { P } = \pi _ { Y } } \end{array} } \end{array}
$$

the uniqueness part of the universal property shows that $f \circ g = \operatorname { i d } _ { P }$ . In the same way we see that $g \circ f = \operatorname { i d } _ { P ^ { \prime } }$ , so that $f$ is an isomorphism. 

Remark 5.16. Again, a check might be in order that our constructions were consistent: Let $X$ and $Y$ be prevarieties, and let $X ^ { \prime } \subset X$ and $Y ^ { \prime } \subset Y$ be closed subprevarieties. Then we have defined two structures of prevarieties on the set-theoretic product $X ^ { \prime } \times Y ^ { \prime }$ : The closed subprevariety structure of $X ^ { \prime } \times Y ^ { \prime }$ in $X \times Y$ as in Construction 5.10 (b), and the product prevariety structure of Definition 5.14. As expected, these two structures agree: In fact, by Definition 5.14 together with Remark 5.12 the set-theoretic identity map is a morphism between these two structures in both ways.

Finally, as already announced let us now impose a condition on prevarieties that excludes such unwanted spaces as the affine line with two zero points of Example 5.5 (b). In the theory of manifolds, this is usually done by requiring that the topological space satisfies the so-called Hausdorff property, i. e. that every two distinct points have disjoint open neighborhoods. This is obviously not satisfied in our case, since the two zero points do not have such disjoint open neighborhoods.

However, in the Zariski topology the Hausdorff property does not make too much sense, as nonempty open subsets of an irreducible space can never be disjoint by Remark 2.16 (a). So we need a suitable replacement for this condition that captures our geometric idea of the absence of doubled points also in the Zariski topology.

The solution to this problem is inspired by a proposition in general topology stating that the Hausdorff property of a topological space $X$ is equivalent to the condition that the so-called diagonal $\Delta _ { X } = \{ ( x , x ) : x \in X \}$ is closed in $X \times X$ (with the product topology). The picture below illustrates this in the case when $X$ is the affine line with two zero points $a$ and $^ b$ : The product $X \times X$ then contains four zero points $( a , a ) , ( a , b ) , ( b , a )$ , and $( b , b )$ , but by definition only two of them, namely $( a , a )$ and $( b , b )$ , are in $\Delta _ { X }$ . Hence the diagonal is not closed: The other two zero points are also contained in its closure.

![](images/995f04e8975519d2774ca6d837bb684736e9c4cd3f1283e5f6426bd6cf20dbdd.jpg)

Of course, this equivalence does not really help us directly in algebraic geometry since we do not use the product topology on $X \times X$ . But the geometric idea to detect doubled points shown in the picture above on the right is still valid in the Zariski topology — and so we will just use the diagonal condition to define the property that we want:

# Definition 5.17 (Varieties).

(a) A prevariety $X$ is called a variety (or separated) if the diagonal

$$
\Delta _ { X } : = \{ ( x , x ) : x \in X \}
$$

is closed in $X \times X$ .

(b) Analogously to Definition 2.32 (b), a variety of pure dimension 1 or 2 is called a curve resp. surface. If $X$ is a pure-dimensional variety and $Y$ a pure-dimensional subvariety of $X$ with $\mathrm { d i m } Y = \mathrm { d i m } X - 1$ we say that $Y$ is a hypersurface in $X$ .

So by the argument given above, the affine line with two zero points of Example 5.5 (b) is not a variety. In contrast, the following lemma shows that most prevarieties that we will meet are also varieties. From now on we will almost always assume that our spaces are separated, and thus talk about varieties instead of prevarieties.

# Lemma 5.18.

(a) Affine varieties are varieties.   
(b) Open and closed subprevarieties of varieties are varieties. We will therefore simply call them open and closed subvarieties, respectively.

# Proof.

(a) If $X \subset \mathbb { A } ^ { n }$ then $\Delta _ { X } = V ( x _ { 1 } - y _ { 1 } , \ldots , x _ { n } - y _ { n } ) \subset X \times X$ , where $x _ { 1 } , \ldots , x _ { n }$ and $y _ { 1 } , \ldots , y _ { n }$ are the coordinates on the two factors, respectively. Hence $\Delta _ { X }$ is closed.   
(b) If $Y \subset X$ is open or closed, consider the inclusion morphism $i \colon Y \times Y \to X \times X$ (which exists by the universal property of Definition 5.14). As we have $\Delta _ { Y } = i ^ { - 1 } ( \Delta _ { X } )$ and $\Delta _ { X }$ is closed by assumption, $\Delta _ { Y }$ is closed as well by the continuity of $i$ . 

For varieties, we have the following additional desirable properties in addition to the ones for prevarieties:

Proposition 5.19 (Properties of varieties). Let $f , g \colon X \to Y$ be morphisms of prevarieties, and assume that $Y$ is a variety.

(a) The graph $\Gamma _ { f } : = \{ ( x , f ( x ) ) : x \in X \}$ is closed in $X \times Y$ .   
(b) The set $\{ x \in X : f ( x ) = g ( x ) \}$ is closed in $X$ .

# Proof.

(a) By the universal property of products of prevarieties as in Definition 5.14 there is a morphism $( f , \operatorname { i d } ) \colon X \times Y \to Y \times Y .$ $( x , y ) \mapsto ( f ( x ) , y )$ . As $Y$ is a variety we know that $\Delta _ { Y }$ is closed, and hence so is $\Gamma _ { f } = ( f , \mathrm { i d } ) ^ { - 1 } ( \Delta _ { Y } )$ by continuity.   
(b) Similarly to (a), the given set is the inverse image of the diagonal $\Delta _ { Y }$ under the morphism $X  Y \times Y$ , $x \mapsto ( f ( x ) , g ( x ) )$ . Hence it is closed again since $\Delta _ { Y }$ is closed. 

Exercise 5.20. Show that the space $\mathbb { P } ^ { 1 }$ of Example 5.5 (a) is a variety.

Exercise 5.21. Let $X$ and $Y$ be prevarieties. Show:

(a) If $X$ and $Y$ are varieties then so is $X \times Y$ .   
(b) If $X$ and $Y$ are irreducible then so is $X \times Y$ .

Exercise 5.22. Use diagonals to prove the following statements:

(a) The intersection of any two affine open subsets of a variety is again an affine open subset. (b) If $X , Y \subset \mathbb { A } ^ { n }$ are two pure-dimensional affine varieties then every irreducible component of $X \cap Y$ has dimension at least $\mathrm { d i m } X + \mathrm { d i m } Y - n$ .

Exercise 5.23. In Exercise 2.34 (b) we have seen that the dimension of a dense open subset $U$ of a topological space $X$ need not be the same as that of $X$ .

However, show now that $\mathrm { d i m } U = \mathrm { d i m } X$ holds in this situation if $X$ is a variety.

# 6. Projective Varieties I: Topology

In the last chapter we have studied (pre-)varieties, i. e. topological spaces that are locally isomorphic to affine varieties. In particular, the ability to glue affine varieties together allowed us to construct compact spaces (in the classical topology over the ground field $\mathbb { C }$ ) as e. g. $\mathbb { P } ^ { 1 }$ , whereas affine varieties themselves are never compact unless they consist of only finitely many points (see Exercise 2.36 (b)). Unfortunately, the description of a variety in terms of its affine patches and gluing isomorphisms is quite inconvenient in practice, as we have seen already in some of the calculations in the last chapter. It would therefore be desirable to have a global description of these spaces that does not refer to gluing methods.

We can obtain a large class of such “compact” varieties admitting a global description by considering zero loci of polynomials in projective instead of affine spaces, generalizing projective curves as in [G2, Chapter 3] — recall that the idea of projective spaces is to add “points at infinity” to affine space similarly to how we have obtained $\mathbb { P } ^ { 1 }$ from $\mathbb { A } ^ { 1 }$ in Example 5.5 (a). It turns out that the resulting class of projective varieties is in fact very large — so large that it is actually not easy to construct a variety that is not an open subset of a projective variety. We will certainly not see one in these notes.

Let us quickly review the construction of projective spaces from [G2, Chapter 3], and then transfer the concept of varieties to this new setting. In this chapter we will construct these projective varieties just as topological spaces, leaving their structure as ringed spaces to Chapter 7.

Definition 6.1 (Projective spaces). Let $n \in \mathbb { N }$ . We define projective $n$ -space over $K$ , denoted $\mathbb { P } _ { K } ^ { n }$ or simply $\mathbb P ^ { n }$ , to be the set of all 1-dimensional linear subspaces of the vector space $K ^ { n + 1 }$ .

Notation 6.2 (Homogeneous coordinates). Obviously, a 1-dimensional linear subspace of $K ^ { n + 1 }$ is uniquely determined by a non-zero vector in $K ^ { n + 1 }$ , with two such vectors spanning the same linear subspace if and only if they are scalar multiples of each other. In other words, we have

$$
\mathbb { P } ^ { n } = ( K ^ { n + 1 } \backslash \{ 0 \} ) / \sim
$$

with the equivalence relation

$$
( x _ { 0 } , \ldots , x _ { n } ) \sim ( y _ { 0 } , \ldots , y _ { n } ) \quad : \Leftrightarrow \quad x _ { i } = \lambda y _ { i }
$$

where $K ^ { * } = K \backslash \{ 0 \}$ is the multiplicative group of units of $K$ . This is usually written as $\mathbb P ^ { n } = ( K ^ { n + 1 } \backslash \{ 0 \} ) / K ^ { * }$ , and the equivalence class of $\left( x _ { 0 } , \ldots , x _ { n } \right)$ will be denoted by $\left( x _ { 0 } \colon \dots \colon x _ { n } \right) \in \mathbb { P } ^ { n }$ (the notations $\left[ x _ { 0 }          colon \cdots : x _ { n } \right]$ and $[ x _ { 0 } , \ldots , x _ { n } ]$ are also common in the literature). So in the notation $\left( x _ { 0 } \colon \cdots : x _ { n } \right)$ for a point in $\mathbb { P } ^ { n }$ the numbers $x _ { 0 } , \ldots , x _ { n }$ are not all zero, and they are defined only up to a common scalar multiple. They are called the homogeneous coordinates of the point (the reason for this name will become obvious in the course of this chapter). Note also that we will usually label the homogeneous coordinates of $\mathbb P ^ { n }$ by $x _ { 0 } , \ldots , x _ { n }$ instead of by $x _ { 1 } , \ldots , x _ { n + 1 }$ . This choice is motivated by the following relation between $\mathbb { A } ^ { n }$ and $\mathbb P ^ { n }$ .

Remark 6.3 (Affine coordinates). Consider the map

$$
f \colon { \mathbb { A } } ^ { n } \to { \mathbb { P } } ^ { n } , ( x _ { 1 } , \ldots , x _ { n } ) \mapsto \left( 1 \colon x _ { 1 } \colon \cdot \cdot \colon x _ { n } \right)
$$

which sets $x _ { 0 } = 1$ and makes the coordinates $x _ { 1 } , \ldots , x _ { n }$ of $\mathbb { A } ^ { n }$ into homogeneous coordinates of $\mathbb P ^ { n }$ . Taking into account that the homogeneous coordinates can be rescaled, it is obviously injective with image $U _ { 0 } : = \left\{ \left( x _ { 0 } : \cdot \cdot \cdot : x _ { n } \right) : x _ { 0 } \neq 0 \right\}$ . On this image the inverse of $f$ is given by

$$
f ^ { - 1 } \colon U _ { 0 } \to \mathbb { A } ^ { n } , ( x _ { 0 } \colon \cdots \colon x _ { n } ) \mapsto \left( { \frac { x _ { 1 } } { x _ { 0 } } } , \ldots , { \frac { x _ { n } } { x _ { 0 } } } \right) .
$$

With this embedding, we can thus think of $\mathbb { A } ^ { n }$ as a subset $U _ { 0 }$ of $\mathbb { P } ^ { n }$ . We call it the affine part of $\mathbb P ^ { n }$ ;   
the coordinates $\left( { \frac { x _ { 1 } } { x _ { 0 } } } , \ldots , { \frac { x _ { n } } { x _ { 0 } } } \right)$ of a point $( x _ { 0 } \colon \cdot \cdot \cdot : x _ { n } ) \in U _ { 0 } \subset \mathbb { P } ^ { n }$ are called its affine coordinates.

The remaining points of $\mathbb P ^ { n }$ (where $x _ { 0 } = 0$ ) are of the form $\left( 0 { : } x _ { 1 } : \cdots : x _ { n } \right)$ and can be viewed as points at infinity, since by $( * )$ they would have infinite affine coordinates. By forgetting their first coordinate (which is zero anyway) they form a set that is naturally bijective to $\mathbb { P } ^ { n - 1 }$ . We can thus write

$$
\mathbb { P } ^ { n } = \mathbb { A } ^ { n } \cup \mathbb { P } ^ { n - 1 } ,
$$

where $\mathbb { A } ^ { n }$ is the affine part and $\mathbb { P } ^ { n - 1 }$ parametrizes the points at infinity. Usually, it is more helpful to think of the points in projective space $\mathbb P ^ { n }$ in this way rather than as 1-dimensional linear subspaces as in Definition 6.1. After having given $\mathbb { P } ^ { n }$ the structure of a variety we will see in Proposition 7.2 and Exercise 7.3 (b) that in this decomposition $\mathbb { A } ^ { n }$ and $\mathbb { P } ^ { n - 1 }$ are open and closed subvarieties of $\mathbb { P } ^ { n }$ , respectively.

Remark 6.4 ( $\mathbb { P } _ { \mathbb { C } } ^ { n }$ is compact in the classical topology). In the case $K = \mathbb { C }$ one can give $\mathbb { P } _ { \mathbb { C } } ^ { n }$ a standard (quotient) topology by declaring a subset $U \subset \mathbb { P } ^ { n }$ to be open if its inverse image under the quotient map $\pi \colon \mathbb { C } ^ { n + 1 } \backslash \{ 0 \} \to \mathbb { P } ^ { n }$ is open in the standard topology. Then $\mathbb { P } _ { \mathbb { C } } ^ { n }$ is compact: Let

$$
S = \{ ( x _ { 0 } , \ldots , x _ { n } ) \in \mathbb { C } ^ { n + 1 } : | x _ { 0 } | ^ { 2 } + \cdots + | x _ { n } | ^ { 2 } = 1 \}
$$

be the unit sphere in $\mathbb { C } ^ { n + 1 }$ . This is a compact space as it is closed and bounded. Moreover, as every point in $\mathbb P ^ { n }$ can be represented by a unit vector in $s$ , the restricted map $\pi | _ { S } \colon S \to \mathbb { P } ^ { n }$ is surjective. Hence $\mathbb { P } ^ { n }$ is compact as a continuous image of a compact set.

Remark 6.5 (Homogeneous polynomials). In complete analogy to affine varieties, we now want to define projective varieties to be subsets of $\mathbb P ^ { n }$ that can be given as the zero locus of some polynomials in the homogeneous coordinates. Note however that if $f \in K [ x _ { 0 } , \ldots , x _ { n } ]$ is an arbitrary polynomial, it does not make sense to write down a definition like

$$
V ( f ) = \{ ( x _ { 0 } \colon \cdots \colon x _ { n } ) : f ( x _ { 0 } , \ldots , x _ { n } ) = 0 \} \quad \subset \mathbb { P } ^ { n } ,
$$

because the homogeneous coordinates are only defined up to a common scalar. For example, if $f = x _ { 1 } ^ { 2 } - x _ { 0 } \in K [ x _ { 0 } , x _ { 1 } ]$ then $f ( 1 , 1 ) = 0$ and $f ( - 1 , - 1 ) \neq 0$ , although $\left( 1 : 1 \right) = \left( - 1 : - 1 \right)$ in $\mathbb { P } ^ { 1 }$ . To get rid of this problem we have to require that $f$ is homogeneous, i. e. that all of its monomials have the same (total) degree $d$ : In this case

$$
f ( \lambda x _ { 0 } , \ldots , \lambda x _ { n } ) = \lambda ^ { d } f ( x _ { 0 } , \ldots , x _ { n } ) { \mathrm { ~ f o r ~ a l l ~ } } \lambda \in K ^ { * } ,
$$

and so in particular we see that

$$
f ( \lambda x _ { 0 } , \ldots , \lambda x _ { n } ) = 0 \quad \Leftrightarrow \quad f ( x _ { 0 } , \ldots , x _ { n } ) = 0 ,
$$

so that the zero locus of $f$ is well-defined in $\mathbb P ^ { n }$ . So before we can start with our discussion of projective varieties we have to set up some algebraic language to be able to talk about homogeneous elements in a ring (or $K$ -algebra).

Definition 6.6 (Graded rings and $K$ -algebras).

(a) A graded ring is a ring $R$ together with Abelian subgroups $R _ { d } \subset R$ for all $d \in \mathbb { N }$ , such that:

• We have $R = \oplus _ { d \in \mathbb { N } } R _ { d }$ , i. e. every $f \in R$ has a unique decomposition $\textstyle f = \sum _ { d \in \mathbb { N } } f _ { d }$ such that $f _ { d } \in R _ { d }$ for all $d \in \mathbb { N }$ and only finitely many $f _ { d }$ are non-zero. • For all $d , e \in \mathbb { N }$ and $f \in R _ { d }$ , $g \in R _ { e }$ we have $f g \in R _ { d + e }$ .

For $f \in R \backslash \{ 0 \}$ the biggest number $d \in \mathbb { N }$ with $f _ { d } \neq 0$ in the decomposition $\textstyle f = \sum _ { d \in \mathbb { N } } f _ { d }$ as above is called the degree $\deg f$ of $f$ . The elements of $R _ { d } \backslash \{ 0 \}$ are said to be homogeneous (of degree $d$ ). We call $\textstyle f = \sum _ { d \in \mathbb { N } } f _ { d }$ and $R = \oplus _ { d \in \mathbb { N } } R _ { d }$ as above the homogeneous decomposition of $f$ and $R$ , respectively.

(b) If $R$ is also a $K$ -algebra in addition to (a), we say that it is a graded $K$ -algebra if $\lambda f \in R _ { d }$ for all $\lambda \in K , d \in \mathbb { N }$ , and $f \in R _ { d }$ .

Example 6.7. The polynomial ring $R = K [ x _ { 0 } , \ldots , x _ { n } ]$ is obviously a graded $K$ -algebra with

$$
R _ { d } = \left\{ \sum _ { \tiny { i _ { 0 } , \ldots , i _ { n } \in \mathbb { N } } } { a _ { i _ { 0 } , \ldots , i _ { n } } x _ { 0 } ^ { i _ { 0 } } \cdot \dots \cdot x _ { n } ^ { i _ { n } } } : a _ { i _ { 0 } , \ldots , i _ { n } } \in K \mathrm { f o r } \mathrm { a l l } i _ { 0 } , \ldots , i _ { n } \right\}
$$

for all $d \in \mathbb { N }$ . In the following we will always consider it with this grading.

Exercise 6.8. Let $R \neq 0$ be a graded ring. Show that the multiplicative unit $1 \in R$ is homogeneous of degree 0.

Of course, we will also need ideals in graded rings. Naively, one might expect that we should consider ideals consisting only of homogeneous elements in this case. However, as an ideal has to be closed under multiplication with arbitrary ring elements, it is virtually impossible that all of its elements are homogeneous. Instead, the correct notion of homogeneous ideal is the following.

Definition 6.9 (Homogeneous ideals). An ideal in a graded ring is called homogeneous if it can be generated by homogeneous elements.

Lemma 6.10 (Properties of homogeneous ideals). Let $J , J _ { 1 } , J _ { 2 }$ be ideals in a graded ring R.

(a) The ideal $J$ is homogeneous if and only if for all $f \in J$ with homogeneous decomposition $\textstyle f = \sum _ { d \in \mathbb { N } } f _ { d }$ we also have $f _ { d } \in J$ for all $d$ .   
(b) If $J _ { 1 }$ and $J _ { 2 }$ are homogeneous then so are $J _ { 1 } + J _ { 2 } , J _ { 1 } J _ { 2 } , J _ { 1 } \cap J _ { 2 }$ , and $\sqrt { J _ { 1 } }$ .   
(c) If J is homogeneous then the quotient $R / J$ is a graded ring with homogeneous decomposition $R / J = \bigoplus _ { d \in \mathbb { N } } R _ { d } / ( R _ { d } \cap J )$ .

# Proof.

(a) $\ " \Rightarrow \ "$ : Let $J = \langle h _ { i } : i \in I \rangle$ for homogeneous elements $h _ { i } \in R$ for all $i$ , and let $f \in J$ . Then $\textstyle f = \sum _ { i \in I } g _ { i } h _ { i }$ for some (not necessarily homogeneous) $g _ { i } \in R$ , of which only finitely many are non-zero. If we denote by $\begin{array} { r } { g _ { i } = \sum _ { e \in \mathbb { N } } g _ { i , e } } \end{array}$ the homogeneous decompositions of these elements, the degree- $^ { \cdot d }$ part of $f$ for $d \in \mathbb { N }$ is

$$
f _ { d } = \sum _ { i \in I , e \in \mathbb { N } } g _ { i , e } h _ { i } \quad \in J .
$$

$" \Leftarrow 2 ^ { , 3 }$ : Under the given assumption, we claim that $J = \langle h _ { d } : h \in J , d \in \mathbb { N } \rangle$ , so that $J$ is a homogeneous ideal. In fact, the inclusion “ $\subset '$ follows since $\begin{array} { r } { h = \sum _ { d \in \mathbb { N } } h _ { d } } \end{array}$ for all $h \in J$ , and the inclusion $" \supset '$ holds by our assumption.

(b) If $J _ { 1 }$ and $J _ { 2 }$ are generated by homogeneous elements, then clearly so are $J _ { 1 } + J _ { 2 }$ (which is generated by $J _ { 1 } \cup J _ { 2 } )$ and $J _ { 1 } J _ { 2 }$ . Moreover, $J _ { 1 }$ and $J _ { 2 }$ then satisfy the equivalent condition of (a), and thus so does $J _ { 1 } \cap J _ { 2 }$ .

It remains to be shown that √ $\sqrt { J _ { 1 } }$ is homogeneous. We will check the condition of (a) for any $f \in \sqrt { J _ { 1 } }$ by induction over the degree $d$ of $f$ . Writing $f = f _ { 0 } + \dots + f _ { d }$ in its homogeneous decomposition, we get

$$
f ^ { n } = ( f _ { 0 } + \dots + f _ { d } ) ^ { n } = f _ { d } ^ { n } + ( { \mathrm { t e r m s ~ o f ~ l o w e r ~ d e g r e e } } ) \quad \in J _ { 1 }
$$

for some $n \in \mathbb { N }$ , hence $f _ { d } ^ { n } \in J _ { 1 }$ by (a), and thus $f _ { d } \in \sqrt { J } _ { 1 }$ . But then $f - f _ { d } = f _ { 0 } + \cdot \cdot \cdot + f _ { d - 1 }$ lies in $\sqrt { J _ { 1 } }$ as well, and so by the induction hypothesis we also see that $f _ { 0 } , \dotsc , f _ { d - 1 } \in \sqrt { J _ { 1 } }$ .

(c) It is clear that $R _ { d } / ( R _ { d } \cap J )  R / J .$ , ${ \overline { { f } } } \mapsto { \overline { { f } } }$ is an injective group homomorphism, so that we can consider $R _ { d } / ( R _ { d } \cap J )$ as a subgroup of $R / J$ for all $d$ .

Now let $f \in R$ be arbitrary, with homogeneous decomposition $\textstyle f = \sum _ { d \in \mathbb { N } } f _ { d }$ . Then we have $\textstyle { \overline { { f } } } = \sum _ { d \in \mathbb { N } } { \overline { { f _ { d } } } }$ with $\overline { { f _ { d } } } \in R _ { d } / ( R _ { d } \cap J )$ , so $\overline { { f } }$ also has a homogeneous decomposition. Moreover, this decomposition is unique: If $\textstyle \sum _ { d \in \mathbb { N } } \overline { { f _ { d } } } = \sum _ { d \in \mathbb { N } } \overline { { g _ { d } } }$ are two such decompositions of the same element in $R / J$ then $\Sigma _ { d \in \mathbb { N } } ( f _ { d } - g _ { d } )$ lies in $J$ . Hence, by (a) we have $f _ { d } - g _ { d } \in J$ for all $d$ as well, which means that $\overline { { f _ { d } } } = \overline { { g _ { d } } } \in R _ { d } / ( R _ { d } \cap J )$ . 

With this preparation we can now define projective varieties in the same way as affine ones. For simplicity, for a homogeneous polynomial $f \in K [ x _ { 0 } , \ldots , x _ { n } ]$ and a point $x = ( x _ { 0 } \colon \cdot \cdot \cdot : x _ { n } ) \in \mathbb { P } ^ { n }$ we will write the condition $f ( x _ { 0 } , \ldots , x _ { n } ) = 0$ (which is well-defined by Remark 6.5) also as $f ( x ) = 0$ .

Definition 6.11 (Projective varieties and their ideals). Let $n \in \mathbb { N }$ .

(a) Let $S \subset K [ x _ { 0 } , \ldots , x _ { n } ]$ be a set of homogeneous polynomials. Then the (projective) zero locus of $s$ is defined as

$$
V ( S ) : = \{ x \in \mathbb { P } ^ { n } : f ( x ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } f \in S \} \quad \subset \mathbb { P } ^ { n } .
$$

Subsets of $\mathbb { P } ^ { n }$ that are of this form are called projective varieties. For ${ \cal S } = ( f _ { 1 } , \dots , f _ { k } )$ we will write $V ( S )$ also as $V ( f _ { 1 } , \ldots , f _ { k } )$ .

(b) For a homogeneous ideal $J \triangleleft K [ x _ { 0 } , \ldots , x _ { n } ]$ we set

$$
V ( J ) : = \{ x \in \mathbb { P } ^ { n } : f ( x ) = 0 { \mathrm { ~ f o r ~ a l l ~ h o m o g e n e o u s ~ } } f \in J \} \quad \subset \mathbb { P } ^ { n } .
$$

Clearly, if $J$ is the ideal generated by a set $s$ of homogeneous polynomials then $V ( J ) = V ( S )$

(c) If $X \subset \mathbb { P } ^ { n }$ is any subset we define its ideal to be

$$
I ( X ) : = \langle f \in K [ x _ { 0 } , \ldots , x _ { n } ] \mathrm { ~ h o m o g e n e o u s : ~ } f ( x ) = 0 \mathrm { ~ f o r ~ a l l ~ } x \in X \rangle \quad \exists K [ x _ { 0 } , \ldots , x _ { n } ] .
$$

(Note that the homogeneous polynomials vanishing on $X$ do not form an ideal yet, so that we have to take the ideal generated by them.)

If we want to distinguish these projective constructions from the affine ones in Definitions 1.2 (b) and 1.8 we will denote them by $V _ { \mathfrak { p } } ( S )$ and $I _ { \mathrm { p } } ( X )$ , and the affine ones by $V _ { \mathrm { a } } ( S )$ and $I _ { \mathrm { a } } ( X )$ , respectively.

# Example 6.12.

(a) As in the affine case, the empty set $\varnothing = V _ { \mathrm { p } } ( 1 )$ and the whole space $\mathbb { P } ^ { n } = V _ { \mathrm { p } } ( 0 )$ are projective varieties.   
(b) If $f _ { 1 } , \dots , f _ { r } \in K [ x _ { 0 } , \dots , x _ { n } ]$ are homogeneous linear polynomials then $V _ { \mathfrak { p } } ( f _ { 1 } , \ldots , f _ { r } ) \subset \mathbb { P } ^ { n }$ is a projective variety. Projective varieties that are of this form are called linear subspaces of $\mathbb P ^ { n }$ .

Exercise 6.13. Let $a \in \mathbb { P } ^ { n }$ be a point. Show that the one-point set $\{ a \}$ is a projective variety, and compute explicit generators for the ideal $I _ { \mathfrak { p } } ( \{ a \} ) { \overset { \vartriangle } { \vline } } \leq K [ { \vline } x _ { 0 } , \ldots , { \vline } x _ { n } ]$ .

Example 6.14. Let $f = x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - x _ { 0 } ^ { 2 } \in \mathbb { C } [ x _ { 0 } , x _ { 1 } , x _ { 2 } ]$ . The real part of the affine zero locus $V _ { \mathrm { a } } ( f ) \subset \mathbb { A } ^ { 3 }$ of this homogeneous polynomial is the 2-dimensional cone shown in the picture below on the left. According to Definition 6.11, its projective zero locus $V _ { \mathsf { p } } ( f ) \subset \mathbb { P } ^ { 2 }$ is the set of all 1-dimensional linear subspaces contained in this cone — but we have seen in Remark 6.3 already that we should rather think of $\mathbb { P } ^ { 2 }$ as the affine plane $\mathbb { A } ^ { 2 }$ (embedded in $\mathbb { A } ^ { 3 }$ at $x _ { 0 } = 1$ ) together with some points at infinity. With this interpretation the real part of $V _ { \mathrm { p } } ( f )$ consists of the hyperbola shown below on the right (whose equation $x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - 1 = 0$ can be obtained by setting $x _ { 0 } = 1$ in $f )$ , together with two points $a$ and $^ b$ at infinity. In the 3-dimensional picture on the left, these two points correspond to the two 1-dimensional linear subspaces parallel to the plane at $x _ { 0 } = 1$ , in the 2-dimensional picture of the affine part in $\mathbb { A } ^ { 2 }$ on the right they can be thought of as points at infinity in the corresponding directions. Note that, in the latter interpretation, “opposite” points at infinity are actually the same, since they correspond to the same 1-dimensional linear subspace in $\mathbb { C } ^ { 3 }$ .

![](images/dac267fafc0c3a8c9cda82b7022f6acb079cb6775641afce2648222832b330cc.jpg)

![](images/c19fd67f973af9b2b53aeaef5d20107da319dca6643501eb8f898737d59131d2.jpg)

We see in this example that the affine and projective zero locus of $f$ carry essentially the same geometric information — the difference is just whether we consider the cone as a set of individual points, or as a union of 1-dimensional linear subspaces in $\mathbb { A } ^ { 3 }$ . Let us now formalize and generalize this correspondence.

Definition 6.15 $( \mathrm { C o n e s } ) _ { \bullet } \ \operatorname { L e t } \pi : \mathbb { A } ^ { n + 1 } \backslash \{ 0 \} \to \mathbb { P } ^ { n } , ( x _ { 0 } , \ldots , x _ { n } ) \mapsto ( x _ { 0 } : \cdots : x _ { n } ) .$

(a) An affine variety $X \subset \mathbb { A } ^ { n + 1 }$ is called a cone if $0 \in X$ , and $\lambda x \in X$ for all $\lambda \in K$ and $x \in X$ . In other words, it consists of the origin together with a union of lines through 0.

(b) For a cone $X \subset \mathbb { A } ^ { n + 1 }$ we call

$$
\mathbb { P } ( X ) : = \pi ( X \backslash \{ 0 \} ) = \{ ( x _ { 0 } : \cdots : x _ { n } ) \in \mathbb { P } ^ { n } : ( x _ { 0 } , \ldots , x _ { n } ) \in X \} \quad \subset \mathbb { P } ^ { n }
$$

the projectivization of $X$ .

(c) For a projective variety $X \subset \mathbb { P } ^ { n }$ we call

$$
C ( X ) : = \{ 0 \} \cup \pi ^ { - 1 } ( X ) = \{ 0 \} \cup \{ ( x _ { 0 } , \ldots , x _ { n } ) : ( x _ { 0 } : \cdots : x _ { n } ) \in X \} \quad \subsetneq \mathbb { A } ^ { n + 1 }
$$

the cone over $X$ (note that this is obviously a cone in the sense of (a)).

Remark 6.16 (Cones and homogeneous ideals).

(a) If $S \subset K [ x _ { 0 } , \ldots , x _ { n } ]$ is a set of non-constant homogeneous polynomials then $V _ { \mathrm { a } } ( S )$ is a cone: Clearly, we then have $0 \in V _ { \mathrm { a } } ( S )$ . Moreover, let $\lambda \in K$ and $x \in V _ { \mathrm { a } } ( S )$ . Then $f ( x ) = 0$ for all $f \in S$ , hence $f ( \lambda x ) = \lambda ^ { \deg f } f ( x ) = 0$ , and so $\lambda x \in V _ { \mathrm { a } } ( S )$ as well.

(b) Conversely, the ideal $I ( X )$ of a cone $X \subset \mathbb { A } ^ { n + 1 }$ is homogeneous: Let $f \in I ( X )$ with homogeneous decomposition $\textstyle f = \sum _ { d \in \mathbb { N } } f _ { d }$ . Then for all $x \in X$ we have $f ( x ) = 0$ , and therefore also

$$
0 = f ( \lambda x ) = \sum _ { d \in \mathbb { N } } \lambda ^ { d } f _ { d } ( x )
$$

for all $\lambda \in K$ since $X$ is a cone. This means that we have the zero polynomial in $\lambda$ , i. e. that $f _ { d } ( x ) = 0$ for all $d$ , and thus $f _ { d } \in I ( \boldsymbol { X } )$ . Hence $I ( X )$ is homogeneous by Lemma 6.10 (a).

Lemma 6.17 (Cones projective varieties). There is a bijection

$$
\begin{array} { r c l } { \{ c o n e s i n \mathbb { A } ^ { n + 1 } \} } & { \stackrel { \cdot \cdot \cdot 1 } { \longleftrightarrow } } & { \{ p r o j e c t i \nu e \nu a r i e t i e s i n \mathbb { P } ^ { n } \} } \\ { X } & { \longmapsto } & { \mathbb { P } ( X ) } \\ { C ( X ) } & { \longleftarrow } & { X . } \end{array}
$$

Proof. For a set $S \subset K [ x _ { 0 } , \ldots , x _ { n } ]$ of non-constant homogeneous polynomials we have by construction

$$
\mathbb { P } ( V _ { \mathrm { a } } ( S ) ) = V _ { \mathfrak { p } } ( S ) \qquad { \mathrm { a n d } } \qquad C ( V _ { \mathfrak { p } } ( S ) ) = V _ { \mathrm { a } } ( S ) .
$$

But $V _ { \mathrm { a } } ( S )$ is really a cone by Remark 6.16 (a), and every cone is of this form by Remark 6.16 (b) (namely for a set $s$ of homogeneous generators of its homogeneous ideal). Hence we obtain the bijection as desired. 

In other words, the correspondence between cones and projective varieties works by passing from the affine to the projective zero locus (and vice versa) of the same set of homogeneous polynomials, as in Example 6.14. Note that in this way linear subspaces of $\mathbb { A } ^ { n + 1 }$ correspond exactly to linear subspaces of $\mathbb { P } ^ { n }$ in the sense of Example 6.12 (b).

Of course, we would also expect a projective version of the Nullstellensatz as in Proposition 1.10,√ i. e. that $I _ { \mathrm { p } } ( V _ { \mathrm { p } } ( J ) ) = \sqrt { J }$ for any homogeneous ideal $J$ in $K [ x _ { 0 } , \ldots , x _ { n } ]$ . This is almost true and can in fact be proved by reduction to the affine case — there is one exception however: as the origin in $\mathbb { A } ^ { n + 1 }$ does not correspond to a point in projective space $\mathbb { P } ^ { n }$ , its ideal $\left. x _ { 0 } , \ldots , x _ { n } \right.$ has to be excluded from the correspondence between varieties and ideals.

Definition 6.18 (Irrelevant ideal). The (radical homogeneous) ideal

$$
\begin{array} { r l } { I _ { 0 } : = ( x _ { 0 } , \ldots , x _ { n } ) } & { { } \le K [ x _ { 0 } , \ldots , x _ { n } ] } \end{array}
$$

is called the irrelevant ideal.

# Proposition 6.19 (Projective Nullstellensatz).

(a) For any projective variety $X \subset \mathbb { P } ^ { n }$ we have $V _ { \mathfrak { p } } ( I _ { \mathfrak { p } } ( X ) ) = X$ .

(b) For any homogeneous ideal $J \triangleleft K [ x _ { 0 } , \ldots , x _ { n } ]$ with ${ \sqrt { J } } \neq I _ { 0 }$ we have $I _ { \mathrm { p } } ( V _ { \mathrm { p } } ( J ) ) = \sqrt { J }$ .

In particular, there is an inclusion-reversing bijection

$$
\begin{array} { r l } { \{ p r o j e c t i v e \nu a r i e t i e s i n \mathbb { P } ^ { n } \} } & { \overset { , ! \cdot ! } { \longleftrightarrow } } & { \left\{ \begin{array} { l } { h o m o g e n e o u s \ r a d i c a l \ i d e a l s \ i n \ K [ x _ { 0 } , \dots , x _ { n } ] } \\ { n o t e q u a l \ t o t h e i r r e l e v a n t i d e a l } \end{array} \right\} } \\ { X } & { \longmapsto } & { I _ { \mathrm { P } } ( X ) } \\ { V _ { \mathrm { p } } ( J ) } & { \longleftrightarrow } & { J . } \end{array}
$$

Proof. The equality in (a), the inclusion $\cdot \supset ^ { \prime \prime }$ of (b), and the fact that the operations $V _ { \mathrm { p } } ( \cdot )$ and $I _ { \mathrm { p } } ( \cdot )$ reverse inclusions are easy and follow in exactly the same way as in the affine case in Proposition 1.10.

For the remaining inclusion “ $\subset { } \mathfrak { s }$ of (b) let $J \neq I _ { 0 }$ be a homogeneous ideal in $K [ x _ { 0 } , \ldots , x _ { n } ]$ . Then

$$
\begin{array} { r l } & { I _ { \mathrm { p } } ( V _ { \mathrm { p } } ( J ) ) = \langle f \in K [ x _ { 0 } , \ldots , x _ { n } ] \mathrm { ~ h o m o g e n e o u s : ~ } f ( x ) = 0 \mathrm { ~ f o r ~ a l l ~ } x \in V _ { \mathrm { p } } ( J ) \rangle } \\ & { \phantom { I I } = \langle f \in K [ x _ { 0 } , \ldots , x _ { n } ] \mathrm { ~ h o m o g e n e o u s : ~ } f ( x ) = 0 \mathrm { ~ f o r ~ a l l ~ } x \in V _ { \mathrm { a } } ( J ) \backslash \{ 0 \} \rangle } \end{array}
$$

As the affine zero locus of polynomials is closed, we can rewrite this as

$$
I _ { \mathsf { p } } ( V _ { \mathsf { p } } ( J ) ) = \langle f \in K [ x _ { 0 } , \ldots , x _ { n } ] { \mathrm { ~ h o m o g e n e o u s : ~ } } f ( x ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } x \in { \overline { { V _ { \mathsf { a } } ( J ) \backslash \{ 0 \} } } } \rangle .
$$

But now $V _ { \mathrm { a } } ( J ) \neq \{ 0 \}$ as otherwise ${ \sqrt { J } } = I _ { \mathrm { a } } ( V _ { \mathrm { a } } ( J ) ) = I _ { 0 }$ , which we excluded. So $V _ { \mathrm { a } } ( J )$ is either empty or (by Remark 6.16 (a)) a cone containing at least one line through the origin. In both cases we obviously get $\overline { { V _ { \mathrm { a } } ( J ) \backslash \{ 0 \} } } = V _ { \mathrm { a } } ( J )$ , so that

$$
I _ { \mathsf { P } } ( V _ { \mathsf { P } } ( J ) ) = \langle f \in K [ x _ { 0 } , \ldots , x _ { n } ] { \mathrm { ~ h o m o g e n e o u s : ~ } } f ( x ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } x \in V _ { \mathsf { a } } ( J ) \rangle .
$$

As the ideal of the cone $V _ { \mathrm { a } } ( J )$ is homogeneous by Remark 6.16 (b) this can be rewritten as $I _ { \mathrm { p } } ( V _ { \mathrm { p } } ( J ) ) = I _ { \mathrm { a } } ( V _ { \mathrm { a } } ( J ) )$ , which is equal to $\sqrt { J }$ by the affine Nullstellensatz.

The additional bijection statement now follows from (a) and (b), together with the observation that $I _ { \mathrm { p } } ( X )$ is always radical by (b), and never equal to $I _ { 0 }$ as otherwise we would obtain the contradiction $\bar { I _ { 0 } } = I _ { \mathrm { p } } ( V _ { \mathrm { p } } ( I _ { 0 } ) ) = I _ { \mathrm { p } } ( \emptyset ) = K [ x _ { 0 } , \dots , x _ { n } ]$ . 

Remark 6.20 (Properties of $V _ { \mathrm { p } } ( \cdot )$ and $I _ { \mathrm { p } } ( \cdot ) )$ ). The operations $V _ { \mathrm { p } } ( \cdot )$ and $I _ { \mathrm { p } } ( \cdot )$ satisfy the same properties as their affine counterparts in Lemmas 1.4, 1.7, and 1.12. More precisely, in the same way as in the affine case we obtain:

(a) For any two subsets $S _ { 1 } , S _ { 2 } \subset K [ x _ { 0 } , \dotsc , x _ { n } ]$ we have $V _ { \mathfrak { p } } ( S _ { 1 } ) \cup V _ { \mathfrak { p } } ( S _ { 2 } ) = V _ { \mathfrak { p } } ( S _ { 1 } S _ { 2 } )$ ; for any family $( S _ { i } )$ of subsets of $K [ x _ { 0 } , \ldots , x _ { n } ]$ we have $\cap _ { i } V _ { \mathfrak { p } } ( S _ { i } ) = V _ { \mathfrak { p } } ( \bigcup _ { i } S _ { i } )$ .   
(b) If $J _ { 1 } , J _ { 2 } \triangleleft K [ x _ { 0 } , \ldots , x _ { n } ]$ are homogeneous ideals then $V _ { \mathrm { p } } ( J _ { 1 } ) \cup V _ { \mathrm { p } } ( J _ { 2 } ) = V _ { \mathrm { p } } ( J _ { 1 } J _ { 2 } ) = V _ { \mathrm { p } } ( J _ { 1 } \cap J _ { 2 } ) \quad { \mathrm { a n d } } \quad V _ { \mathrm { p } } ( J _ { 1 } ) \cap V _ { \mathrm { p } } ( J _ { 2 } ) = V _ { \mathrm { p } } ( J _ { 1 } + J _ { 2 } ) .$   
(c) For any two projective varieties $X _ { 1 } , X _ { 2 }$ in $\mathbb P ^ { n }$ we have $I _ { \mathrm { p } } ( X _ { 1 } \cap X _ { 2 } ) = { \sqrt { I _ { \mathrm { p } } ( X _ { 1 } ) + I _ { \mathrm { p } } ( X _ { 2 } ) } }$ unless the latter is the irrelevant ideal (which is only possible if $X _ { 1 }$ and $X _ { 2 }$ are disjoint). Moreover, we have $I _ { \mathrm { p } } ( X _ { 1 } \cup X _ { 2 } ) = I _ { \mathrm { p } } ( X _ { 1 } ) \cap I _ { \mathrm { p } } ( X _ { 2 } )$ .

Next, and also as in the affine case, let us associate a coordinate ring to a projective variety, and consider zero loci and ideals in a relative setting.

Construction 6.21 (Relative version of zero $V _ { \mathrm { p } } ( \cdot )$ and $I _ { \mathrm { p } } ( \cdot ) )$ . Let $Y \subset \mathbb { P } ^ { n }$ be a projective variety. In analogy to Definition 1.15 we call

$$
S ( Y ) : = K [ x _ { 0 } , \ldots , x _ { n } ] / I ( Y )
$$

the homogeneous coordinate ring of Y . By Lemma 6.10 (c) it is a graded ring, so that it makes sense to talk about homogeneous elements of $S ( Y )$ . Moreover, the condition $f ( x ) = 0$ is still well-defined for a homogeneous element $f \in S ( Y )$ and a point $x \in Y$ , and thus we can define as in Definition 6.11

$V ( J ) : = \{ x \in Y : f ( x ) = 0$ for all homogeneous $f \in J \}$ for a homogeneous ideal $J { \le } S ( Y )$

(and similarly for a set of homogeneous polynomials in $S ( { \boldsymbol { Y } } ) _ { } ^ { }$ ), and

$$
I ( X ) : = \langle f \in S ( Y ) { \mathrm { ~ h o m o g e n e o u s : ~ } } f ( x ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } x \in X \rangle \qquad { \mathrm { f o r ~ a ~ s u b s e t ~ } } X \subset Y .
$$

As before, in case of possible confusion we will decorate $V$ and $I$ with the subscript $Y$ and/or p to denote the relative and projective situation, respectively. Subsets of $Y$ that are of the form $V _ { Y } ( J )$ for a homogeneous ideal $J { \le } S ( Y )$ will be called projective subvarieties of $Y$ ; these are obviously exactly the projective varieties contained in $Y$ .

As in the affine case, the Nullstellensatz and the properties of $V ( \cdot )$ and $I ( \cdot )$ can again be transferred to this relative setting in the obvious way.

Remark 6.22. A remark that is sometimes useful is that every projective subvariety $X$ of a projective variety $Y \subset \mathbb { P } ^ { n }$ can be written as the zero locus of finitely many homogeneous polynomials in $S ( Y )$ of the same degree. This follows easily from the fact that $V _ { \mathfrak { p } } ( f ) = V _ { \mathfrak { p } } ( x _ { 0 } ^ { d } f , \dots , x _ { n } ^ { d } f )$ for all homogeneous $f \in S ( Y )$ and every $d \in \mathbb { N }$ . However, it is not true that every homogeneous ideal in $S ( Y )$ can be generated by homogeneous elements of the same degree.

We can now proceed to define a topology on projective varieties. As in the affine setting, it follows by (the relative version of) Remark 6.20 (a) that arbitrary intersections and finite unions of subvarieties of a projective variety $X$ are again subvarieties, and hence we can define the Zariski topology on $X$ in the same way as in the affine case:

Definition 6.23 (Zariski topology). The Zariski topology on a projective variety $X$ is the topology whose closed sets are exactly the projective subvarieties of $X$ , i. e. the subsets of the form $V _ { \mathrm { p } } ( S )$ for some set $S \subset S ( X )$ of homogeneous elements.

Of course, from now on we will always use this topology for projective varieties and their subsets. Note that, in the same way as in Remark 2.3, this is well-defined in the sense that the Zariski topology on a projective variety $X \subset \mathbb { P } ^ { n }$ agrees with the subspace topology of $X$ in $\mathbb { P } ^ { n }$ . Moreover, since we want to consider $\mathbb { A } ^ { n }$ as a subset of $\mathbb { P } ^ { n }$ as in Remark 6.3 we should also check that the Zariski topology on $\mathbb { A } ^ { n }$ is the same as the subspace topology of $\mathbb { A } ^ { n }$ in $\mathbb { P } ^ { n }$ . To do this, we need the following definition.

Construction 6.24 (Homogenization and dehomogenization).

(a) For a homogeneous polynomial $f \in K [ x _ { 0 } , \ldots , x _ { n } ]$ , the dehomogenization of $f$ is defined to be the polynomial $f ^ { \mathrm { i } } : = f ( x _ { 0 } = 1 ) \in K [ x _ { 1 } , \dots , x _ { n } ]$ obtained from $f$ by setting $x _ { 0 } = 1$ . In general, it will be an inhomogeneous polynomial (hence the notation $f ^ { \mathrm { i } }$ ). Note that evaluation at $x _ { 0 } = 1$ is a ring homomorphism, i. e. we have

$$
( f g ) ^ { \mathrm { i } } = f ^ { \mathrm { i } } \quad { \mathrm { a n d } } \quad ( f + g ) ^ { \mathrm { i } } = f ^ { \mathrm { i } } + g ^ { \mathrm { i } }
$$

for all $f , g \in K [ x _ { 0 } , \ldots , x _ { n } ]$ . As it is surjective, we can also apply this construction directly to ideals: For a homogeneous ideal $J \triangleleft K [ x _ { 0 } , \ldots , x _ { n } ]$ , the dehomogenization $J ^ { \mathrm { i } } : = \{ f ^ { \mathrm { i } } : f \in J \}$ is again an ideal in $K [ x _ { 1 } , \ldots , x _ { n } ]$ .

(b) For the opposite direction, let

$$
f = \sum _ { i _ { 1 } , \ldots , i _ { n } \in \mathbb { N } } a _ { i _ { 1 } , \ldots , i _ { n } } x _ { 1 } ^ { i _ { 1 } } \cdot \dots \cdot x _ { n } ^ { i _ { n } } \quad \in K [ x _ { 1 } , \ldots , x _ { n } ]
$$

be a (non-zero) polynomial of degree $d$ . We define its homogenization to be

$$
\begin{array} { r l } { f ^ { \mathrm { h } } : = x _ { 0 } ^ { d } f \Big ( \displaystyle \frac { x _ { 1 } } { x _ { 0 } } , \ldots , \displaystyle \frac { x _ { n } } { x _ { 0 } } \Big ) } & { { } } \\ { = \displaystyle \sum _ { i _ { 1 } , \ldots , i _ { n } \in \mathbb { N } } a _ { i _ { 1 } , \ldots , i _ { n } } x _ { 0 } ^ { d - i _ { 1 } - \cdots - i _ { n } } x _ { 1 } ^ { i _ { 1 } } \cdot \dots \cdot x _ { n } ^ { i _ { n } } } & { { } \in K [ x _ { 0 } , \ldots , x _ { n } ] ; } \end{array}
$$

obviously this is a homogeneous polynomial of degree $d$ . For all $f , g \in K [ x _ { 1 } , \ldots , x _ { n } ]$ of degrees $d$ and $e$ , respectively, we have

$$
( f g ) ^ { \mathrm { h } } = x _ { 0 } ^ { d + e } f { \biggl ( } { \frac { x _ { 1 } } { x _ { 0 } } } , \ldots , { \frac { x _ { n } } { x _ { 0 } } } { \biggr ) } \cdot g { \biggl ( } { \frac { x _ { 1 } } { x _ { 0 } } } , \ldots , { \frac { x _ { n } } { x _ { 0 } } } { \biggr ) } = f ^ { \mathrm { h } } \cdot g ^ { \mathrm { h } } ,
$$

but in contrast to (a) the polynomial $( f + g ) ^ { \mathrm { h } }$ is clearly not equal to $f ^ { \mathrm { h } } + g ^ { \mathrm { h } }$ in general — in fact, $f ^ { \mathrm { h } } + g ^ { \mathrm { h } }$ is usually not even homogeneous. So in order to apply this construction to an ideal $J { \overset { \vartriangle } { \mathop { \vartriangle } } } { \underset { \ v { u } } { K } } [ x _ { 1 } , \dots , x _ { n } ]$ , we have to define the ideal $J ^ { \mathrm { h } } \triangleleft K [ x _ { 0 } , \ldots , x _ { n } ]$ to be the ideal generated by the homogenizations $f ^ { \mathrm { h } }$ of all non-zero $f \in J$ .

Example 6.25. For $f = x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - 1 \in K [ x _ { 1 } , x _ { 2 } ]$ we have $f ^ { \mathrm { h } } = x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - x _ { 0 } ^ { 2 } \in K [ x _ { 0 } , x _ { 1 } , x _ { 2 } ]$ , and then back $( f ^ { \mathrm { h } } ) ^ { \mathrm { i } } = x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - 1 { \stackrel { . } { = } } f$ .

Remark 6.26 ( $\mathbb { A } ^ { n }$ as an open subset of $\mathbb { P } ^ { n }$ ). Recall from Remark 6.3 that we want to identify the subset $U _ { 0 } = \{ ( x _ { 0 } { : } \dots { : } x _ { n } ) \in \mathbb { P } ^ { n } : x _ { 0 } \neq 0 \}$ of $\mathbb { P } ^ { n }$ with $\mathbb { A } ^ { n }$ by the bijective map

$$
F \colon \mathbb { A } ^ { n } \to U _ { 0 } , ( x _ { 1 } , \ldots , x _ { n } ) \mapsto ( 1 { : } x _ { 1 } { : } \cdots { : } x _ { n } ) .
$$

Obviously, $U _ { 0 }$ is an open subset of $\mathbb { P } ^ { n }$ . Moreover, with the above identification the subspace topology of $U _ { 0 } = \mathbb { A } ^ { n } \subset \mathbb { P } ^ { n }$ is the affine Zariski topology:

(a) If $X = V _ { \mathfrak { p } } ( J ) \cap { \mathbb { A } } ^ { n }$ is a closed set in the subspace topology (with $J \triangleleft K [ x _ { 0 } , \ldots , x _ { n } ]$ a homogeneous ideal) then $X = V _ { \mathrm { a } } ( J ^ { \mathrm { i } } )$ is also Zariski-closed.   
(b) If $X = V _ { \mathrm { a } } ( J ) \subset \mathbb { A } ^ { n }$ is Zariski-closed (with $J \triangleleft K [ x _ { 1 } , \ldots , x _ { n } ] )$ then $X = V _ { \mathrm { p } } ( J ^ { \mathrm { h } } ) \cap \mathbb { A } ^ { n }$ is closed in the subspace topology as well.

In other words we can say that the map $F \colon \mathbb { A } ^ { n } \to U _ { 0 }$ above is a homeomorphism. In fact, after having given $\mathbb { P } ^ { n }$ the structure of a variety we will see in Proposition 7.2 that it is even an isomorphism of varieties.

Having defined the Zariski topology on projective varieties (or more generally on subsets of $\mathbb { P } ^ { n }$ ) we can now immediately apply all topological concepts of Chapter 2 to this new situation. In particular, the notions of connectedness, irreducibility, and dimension are well-defined for projective varieties (and have the same geometric interpretation as in the affine case). Let us study some examples using these concepts.

Remark 6.27 $\mathbb { P } ^ { n }$ is irreducible of dimension $n$ ). Of course, by symmetry of the coordinates, it follows from Remark 6.26 that all subsets $U _ { i } = \left\{ \left( x _ { 0 } : \cdots : x _ { n } \right) : x _ { i } \neq 0 \right\}$ of $\mathbb { P } ^ { n }$ for $i = 0 , \ldots , n$ are homeomorphic to $\mathbb { A } ^ { n }$ as well. As these subsets cover $\mathbb { P } ^ { n }$ and have non-empty intersections, we conclude by Exercise 2.21 (b) that $\mathbb { P } ^ { n }$ is irreducible, and by Exercise 2.34 (a) that $\dim \mathbb { P } ^ { n } = n$ .

Exercise 6.28. Let $L _ { 1 }$ , $L _ { 2 } \subset \mathbb { P } ^ { 3 }$ be two disjoint lines (i. e. 1-dimensional linear subspaces in the sense of Example 6.12 (b)), and let $a \in \mathbb { P } ^ { 3 } \backslash ( L _ { 1 } \cup L _ { 2 } )$ . Show that there is a unique line $L \subset \mathbb { P } ^ { 3 }$ through $a$ that intersects both $L _ { 1 }$ and $L _ { 2 }$ .

Is the corresponding statement for lines and points in $\mathbb { A } ^ { 3 }$ true as well?

# Exercise 6.29.

(a) Prove that a graded ring $R$ is an integral domain if and only if for all homogeneous elements $f , g \in R$ with $f g = 0$ we have $f = 0$ or $g = 0$ .   
(b) Show that a projective variety $X$ is irreducible if and only if its homogeneous coordinate ring $S ( X )$ is an integral domain.

Exercise 6.30. In this exercise we want to show that an intersection of projective varieties is never empty unless one would expect it to be empty for dimensional reasons — so e. g. the phenomenon of parallel non-intersecting lines in the plane does not occur in projective space (which we have seen already in Remark 6.3).

So let $X , Y \subset \mathbb { P } ^ { n }$ be non-empty projective varieties. Show:

(a) The dimension of the cone $C ( X ) \subset \mathbb { A } ^ { n + 1 }$ is $\mathrm { d i m } X + 1$ .   
(b) If $\mathrm { d i m } X + \mathrm { d i m } Y \geq n$ then $X \cap Y \neq \emptyset$ .

We have just seen in Remark 6.26 (b) that for an affine variety $X = V ( J ) \subset \mathbb { A } ^ { n }$ the homogenization $J ^ { \mathrm { h } }$ gives an ideal such that the closed set $V _ { \mathfrak { p } } ( J ^ { \mathrm { h } } ) \subset \mathbb { P } ^ { n }$ restricts to $X$ on $\mathbb { A } ^ { n } \subset \mathbb { P } ^ { n }$ . In fact, we will now show that $V _ { \mathrm { p } } ( J ^ { \mathrm { h } } )$ is even the smallest closed set in $\mathbb P ^ { n }$ containing $X$ , i. e. the closure $\overline { { X } }$ of $X$ in $\mathbb P ^ { n }$ . As this will be a “compact” space in the sense of Remarks 6.3 and 6.4 we can think of this closure $\overline { { X } }$ as being obtained by compactifying $X$ by some “points at infinity”. For example, if we start with the affine hyperbola $X = V _ { \mathrm { a } } ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - 1 ) \subset \mathbb { A } ^ { 2 }$ in the picture below on the left, its closure

$$
{ \overline { { X } } } = V _ { \mathsf { p } } \left( ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - 1 ) ^ { \mathrm { h } } \right) = V _ { \mathsf { p } } ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - x _ { 0 } ^ { 2 } ) \subset \mathbb { P } ^ { 2 }
$$

adds the two points $a$ and $^ b$ at infinity as in Example 6.14.

$$
{ \bf \Phi } { \bf \Phi } { \bf \Phi } { \bf \Phi } ) ^   ^ { x _ { 2 } } ( \begin{array} { l l l l } { { \bf \Phi } } & { { \bf \Phi } } & { { \bf \Phi } } & { { \bf \Phi } } \\ { { \bf \Phi } } & { { \bf \Phi } } & { { \bf \Phi } } & { { \bf \Phi } } \\ { { \bf X } } & { { \bf \Phi } } & { { \bf \Phi } } & { { \bf \Phi } } \end{array} ) ^ { x _ { 2 } } ( \begin{array} { l } { { \bf \Phi } } \\ { { \bf \Phi } } \\ { { \bf \Phi } } \\ { { \bf \Phi } } \\ { { \bf \Phi } } \end{array} ) _ { [ \begin{array} { l } { { \bf \Phi } } \\ { { \bf \Phi } } \\ { { \bf \Phi } } \\ { { \bf \Phi } } \\ { { \bf \Phi } } \end{array} ] } ^ { x _ { 1 } }
$$

Proposition 6.31 (Computation of the projective closure). Let $J { \overset { \vartriangle 1 } { \mathop {  } } } K [ x _ { 1 } , \dots , x _ { n } ]$ be an ideal. Consider its affine zero locus $X = V _ { \mathrm { a } } ( J ) \subset \mathbb { A } ^ { n }$ , and its closure $\overline { { X } }$ in $\mathbb { P } ^ { n }$ .

(a) We have $\overline { { { X } } } = V _ { \mathrm { p } } ( J ^ { \mathrm { h } } )$ .   
(b) If $J = \langle f \rangle$ is a non-zero principal ideal then $\overline { { { X } } } = V _ { \mathrm { p } } ( f ^ { \mathrm { h } } )$ .

# Proof.

(a) Clearly, the set $V _ { \mathrm { p } } ( J ^ { \mathrm { h } } )$ is closed and contains $X$ . In order to show that $V _ { \mathrm { p } } ( J ^ { \mathrm { h } } )$ is the smallest closed set containing $X$ let $Y \supset X$ be any closed set; we have to prove that $Y \supset V _ { \mathrm { p } } ( J ^ { \mathrm { h } } )$ . As $Y$ is closed we have $Y = V _ { \mathrm { p } } ( J ^ { \prime } )$ for some homogeneous ideal $J ^ { \prime }$ . Now any homogeneous element of $J ^ { \prime }$ can be written as $x _ { 0 } ^ { d } f ^ { \mathrm { h } }$ for some $d \in \mathbb { N }$ and $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ , and for this element we have

$$
\begin{array} { r l r } & { \quad x _ { 0 } ^ { d } f ^ { \mathrm { h } } \mathrm { i s . z e r o o n } X \subset \mathbb { P } ^ { n } } & { ( X \mathrm { i s ~ a ~ s u b s e t ~ o f } Y ) } \\ & { \Rightarrow \ f \mathrm { i s . z e r o o n } X \subset \mathbb { A } ^ { n } } & { ( x _ { 0 } \neq 0 \mathrm { o n } X \subset \mathbb { A } ^ { n } ) } \\ & { \Rightarrow \ f \in I _ { \mathfrak { a } } ( X ) = I _ { \mathfrak { a } } ( V _ { \mathfrak { a } } ( J ) ) = \sqrt { J } } & { ( \mathrm { P r o p o s i t i o n ~ 1 . 1 0 } ) } \\ & { \Rightarrow f ^ { m } \in J \mathrm { f o r ~ s o m e } m \in \mathbb { N } } \\ & { \Rightarrow ( f ^ { \mathrm { h } } ) ^ { m } = ( f ^ { m } ) ^ { \mathrm { h } } \in J ^ { \mathrm { h } } \mathrm { ~ f o r ~ s o m e } m \in \mathbb { N } } & { ( \mathrm { C o n s t r u c t i o n ~ 6 . 2 4 ~ ( b ) } ) } \\ & { \Rightarrow f ^ { \mathrm { h } } \in \sqrt { J ^ { \mathrm { h } } } } \\ & { \Rightarrow x _ { 0 } ^ { d } f ^ { \mathrm { h } } \in \sqrt { J ^ { \mathrm { h } } } . } \end{array}
$$

We therefore conclude that $J ^ { \prime } \subset \sqrt { J ^ { \mathrm { h } } }$ , and so $Y = V _ { \mathrm { p } } ( J ^ { \prime } ) \supset V _ { \mathrm { p } } ( { \sqrt { J ^ { \mathrm { h } } } } ) = V _ { \mathrm { p } } ( J ^ { \mathrm { h } } )$ as desired.

(b) As $\langle f \rangle = \{ f g : g \in K [ x _ { 1 } , \ldots , x _ { n } ] \}$ , we have

$$
{ \overline { { X } } } = V _ { \mathsf { p } } { \big ( } ( f g ) ^ { \mathrm { h } } : g \in K [ x _ { 1 } , \ldots , x _ { n } ] { \big ) } = V _ { \mathsf { p } } { \big ( } f ^ { \mathrm { h } } g ^ { \mathrm { h } } : g \in K [ x _ { 1 } , \ldots , x _ { n } ] { \big ) } = V _ { \mathsf { p } } { \big ( } f ^ { \mathrm { h } } { \big ) }
$$

by (a) and Construction 6.24 (b).

Remark 6.32 (Ideal of hypersurfaces in $\mathbb { P } ^ { n }$ ). Let $X$ be a hypersurface in $\mathbb P ^ { n }$ , and assume without loss of generality that it does not contain the set of points at infinity $V _ { \mathrm { p } } ( x _ { 0 } )$ as a component. Then $Y : = X \cap \mathbb { A } ^ { n }$ is an affine hypersurface whose closure is again $X$ . By Remark 2.38 we know that its ideal $I ( Y )$ is principal, generated by a polynomial $g \in K [ x _ { 1 } , \ldots , x _ { n } ]$ .

If we now set $f = g ^ { \mathrm { h } } \in K [ x _ { 0 } , \ldots , x _ { n } ]$ then $V _ { \mathfrak { p } } ( f ) = { \overline { { Y } } } = X$ by Proposition 6.31 (b). Moreover, as $g$ has no repeated factors the same is true for $f$ , and hence we even have $I ( X ) = \langle f \rangle$ . In other words, just as in the affine case the ideal of any projective hypersurface is principal, and thus we can transfer our definition of degree to the projective case:

Definition 6.33 (Degree of a projective hypersurface). Let $X$ be a hypersurface in $\mathbb { P } ^ { n }$ , with ideal $I ( X ) = \langle f \rangle$ as in Remark 6.32. As in the affine case in Definition 2.39, the degree of $f$ is then also called the degree of $X$ , again denoted degX. We also use the terms linear, quadric, or cubic for projective hypersurfaces of degrees 1, 2, or 3, respectively.

Example 6.34. In contrast to Proposition 6.31 (b), for general ideals it usually does not suffice to only homogenize a set of generators. As an example, consider the ideal $J = \langle x _ { 1 } , x _ { 2 } - x _ { 1 } ^ { 2 } \rangle \triangleleft K [ x _ { 1 } , x _ { 2 } ]$ with affine zero locus $X = V _ { \mathrm { a } } ( J ) = \{ 0 \} \subset \mathbb { A } ^ { 2 }$ . This one-point set is also closed in $\mathbb { P } ^ { 2 }$ , and thus $\overline { { X } } = \{ ( 1 { : } 0 { : } 0 ) \}$ is just the corresponding point in homogeneous coordinates. But if we homogenize the two given generators of $J$ we obtain the homogeneous ideal $\langle x _ { 1 } , x _ { 0 } x _ { 2 } - x _ { 1 } ^ { 2 } \rangle$ with projective zero locus $\left\{ ( 1 : 0 : 0 ) , ( 0 : 0 : 1 ) \right\} \supseteq \overline { { X } }$ .

For those of you who know some computer algebra: One can show however that it suffices to homogenize a Gröbner basis of $J$ . This makes the problem of finding $\overline { { X } }$ computationally feasible since in contrast to Proposition 6.31 (a) we only have to homogenize finitely many polynomials.

Exercise 6.35. Sketch the set of real points of the complex affine curve $X = V ( x _ { 1 } ^ { 3 } - x _ { 1 } x _ { 2 } ^ { 2 } + 1 ) \subset \mathbb { A } _ { \mathbb { C } } ^ { 2 }$ and compute the points at infinity of its projective closure $\overline { { X } } \subset \mathbb { P } _ { \mathbb { C } } ^ { 2 }$ .

# 7. Projective Varieties II: Ringed Spaces

After having defined projective varieties as topological spaces, we will now give them the structure of ringed spaces to make them into varieties in the sense of Chapter 5. In other words, we have to define a suitable notion of regular functions on (open subsets of) projective varieties.

Of course, as in the affine case in Definition 3.1 the general idea is that a regular function should be a $K$ -valued function that is locally a quotient of two polynomials. However, note that in contrast to the affine situation the elements of the homogeneous coordinate ring $S ( X )$ of a projective variety $X$ are not well-defined functions on $X$ : Even if $f \in S ( X )$ is homogeneous of degree $d$ we only have $f ( \lambda x ) = \lambda ^ { d } f ( x )$ for all $x \in X$ and $\lambda \in K$ . So the only way to obtain well-defined functions is to consider quotients of homogeneous polynomials of the same degree, so that the factor $\lambda ^ { d }$ cancels out:

Definition 7.1 (Regular functions on projective varieties). Let $U$ be an open subset of a projective variety $X$ . A regular function on $U$ is a map $\varphi \colon U \to K$ with the following property: For every $a \in U$ there are $d \in \mathbb { N }$ and $f , g \in S ( X ) _ { d }$ with $f ( x ) \neq 0$ and

$$
\varphi ( x ) = { \frac { g ( x ) } { f ( x ) } }
$$

for all $x$ in an open subset $U _ { a }$ with $a \in U _ { a } \subset U$ .

It is obvious that the sets ${ \mathcal { O } } _ { X } ( U )$ of regular functions on $U$ are subrings of the $K$ -algebras of all functions from $U$ to $K$ , and — by the local nature of the definition — that they form a sheaf ${ \mathcal { O } } _ { X }$ on $X$ .

With this definition, let us check first of all that the open subsets of a projective variety where one of the coordinates is non-zero are affine varieties, so that projective varieties are prevarieties in the sense of Definition 5.1.

Proposition 7.2 (Projective varieties are prevarieties). Let $X \subset \mathbb { P } ^ { n }$ be a projective variety. Then

$$
U _ { i } = \{ ( x _ { 0 } : \cdots : x _ { n } ) \in X : x _ { i } \neq 0 \} \quad \subset X
$$

is an affine variety for all $i = 0 , \ldots , n .$ . In particular, $X$ is a prevariety.

Proof. By symmetry it suffices to prove the statement for $i = 0$ . Let $X = V _ { \mathrm { p } } ( J )$ for some homogeneous ideal $J \triangleleft K [ x _ { 0 } , \ldots , x _ { n } ]$ . If $Y = V _ { \mathrm { a } } ( J ^ { \mathrm { i } } )$ we claim that

$$
F \colon Y \to U _ { 0 } , ( x _ { 1 } , \ldots , x _ { n } ) \mapsto \left( 1 { : } x _ { 1 } { : } \cdots { : } x _ { n } \right)
$$

is an isomorphism with inverse

$$
F ^ { - 1 } \colon U _ { 0 } \to Y , ( x _ { 0 } { \colon } \cdots { \colon } x _ { n } ) \mapsto \left( { \frac { x _ { 1 } } { x _ { 0 } } } , \ldots , { \frac { x _ { n } } { x _ { 0 } } } \right) .
$$

In fact, it is clear by construction that these two maps are well-defined and inverse to each other. Moreover, as in Remark 6.26 they are continuous: The inverse image of a closed set $V _ { \mathrm { p } } ( J ^ { \prime } ) \cap U _ { 0 }$ under $F$ (with $J ^ { \prime } { \overset { \triangledown } { \lrcorner } } K [ x _ { 0 } , \ldots , x _ { n } ]$ homogeneous) is the closed set $V _ { \mathrm { a } } ( J ^ { \prime \mathrm { i } } )$ , and the image of a closed set $V _ { \mathrm { a } } ( J ^ { \prime } ) \subset Y$ under $F$ (with $J ^ { \prime } { \overset { \triangleleft } { \lrcorner } } K [ x _ { 1 } , \ldots , x _ { n } ] )$ is the closed set $V _ { \mathrm { p } } ( J ^ { \prime \mathrm { h } } ) \cap U _ { 0 }$ .

Finally, we have to check that $F$ and $F ^ { - 1 }$ pull back regular functions to regular functions: A regular function on (an open subset of) $U _ { 0 }$ is by Definition 7.1 locally of the form $\frac { g ( x _ { 0 } , . . . , x _ { n } ) } { f ( x _ { 0 } , . . . , x _ { n } ) }$ (with nowhere vanishing denominator) for two homogeneous polynomials $g$ and $f$ of the same degree. Then

$$
F ^ { * } { \frac { g ( x _ { 0 } , \ldots , x _ { n } ) } { f ( x _ { 0 } , \ldots , x _ { n } ) } } = { \frac { g ^ { \mathrm { i } } ( x _ { 1 } , \ldots , x _ { n } ) } { f ^ { \mathrm { i } } ( x _ { 1 } , \ldots , x _ { n } ) } }
$$

is a quotient of polynomials and thus a regular function on $Y$ . Conversely, $F ^ { - 1 }$ pulls back a quotient $\frac { g ( x _ { 1 } , . . . , x _ { n } ) } { f ( x _ { 1 } , . . . , x _ { n } ) }$ of two polynomials to

$$
( F ^ { - 1 } ) ^ { * } { \frac { g ( x _ { 1 } , \ldots , x _ { n } ) } { f ( x _ { 1 } , \ldots , x _ { n } ) } } = { \frac { g { \big ( } { \frac { x _ { 1 } } { x _ { 0 } } } , \ldots , { \frac { x _ { n } } { x _ { 0 } } } { \big ) } } { f { \big ( } { \frac { x _ { 1 } } { x _ { 0 } } } , \ldots , { \frac { x _ { n } } { x _ { 0 } } } { \big ) } } } ,
$$

which is a regular function on $U _ { 0 }$ since it can be rewritten as a quotient of two homogeneous polynomials of the same degree (by multiplying both the numerator and the denominator by $x _ { 0 } ^ { d }$ for $d = \operatorname* { m a x } ( \deg p , \deg q ) )$ . Hence $F$ is an isomorphism by Definition 4.3 (b), and so $U _ { 0 }$ is an affine open subset of $X$ .

In particular, as the open subsets $U _ { i }$ for $i = 0 , \ldots , n$ cover $X$ we conclude that $X$ is a prevariety.

Exercise 7.3. Check that Definition 7.1 (together with Proposition 7.2) is compatible with our earlier constructions in the following cases:

(a) The prevariety $\mathbb { P } ^ { 1 }$ is the same as the one introduced in Example 5.5 (a). (b) If $X \subset \mathbb { P } ^ { n }$ is a projective variety then its structure sheaf as defined above is the same as the closed subprevariety structure of $X$ in $\mathbb { P } ^ { n }$ as in Construction 5.10 (b).

We have already mentioned that the major advantage of (subprevarieties of) projective varieties is that they have a global description with homogeneous coordinates that does not refer to gluing techniques. In fact, the following proposition shows that many morphisms between projective varieties can also be constructed without gluing.

Lemma 7.4 (Morphisms of projective varieties). Let $X \subset \mathbb { P } ^ { n }$ be a projective variety, and let $f _ { 0 } , \ldots , f _ { m } \in S ( X )$ be homogeneous elements of the same degree. Then on the open subset $U : = X \backslash V ( f _ { 0 } , . . . , f _ { m } )$ these elements define a morphism

$$
f \colon U \to \mathbb { P } ^ { m } , x \mapsto ( f _ { 0 } ( x ) \colon \colon \cdot \colon f _ { m } ( x ) ) .
$$

Proof. First of all note that $f$ is well-defined set-theoretically: By definition of $U$ the image point can never be $( 0 \colon \cdots \colon 0 )$ ; and if we rescale the homogeneous coordinates $x _ { 0 } , \ldots , x _ { n }$ of $x \in U$ we get

$$
\begin{array} { r l } & { \bigl ( f _ { 0 } \bigl ( \lambda x _ { 0 } \colon \cdots \colon \lambda x _ { n } \bigr ) \colon \cdots \colon f _ { m } \bigl ( \lambda x _ { 0 } \colon \cdots \colon \lambda x _ { n } \bigr ) \bigr ) } \\ & { \qquad = \bigl ( \lambda ^ { d } f _ { 0 } \bigl ( x _ { 0 } \colon \cdots \colon x _ { n } \bigr ) \colon \cdots \colon \lambda ^ { d } f _ { m } \bigl ( x _ { 0 } \colon \cdots \colon x _ { n } \bigr ) \bigr ) } \\ & { \qquad = \bigl ( f _ { 0 } \bigl ( x _ { 0 } \colon \cdots \colon x _ { n } \bigr ) \colon \cdots \colon f _ { m } \bigl ( x _ { 0 } \colon \cdots \colon x _ { n } \bigr ) \bigr ) , } \end{array}
$$

where $d$ is the common degree of the $f _ { 0 } , \ldots , f _ { m }$ . To check that $f$ is a morphism we want to use the gluing property of Lemma 4.6. So let $\{ V _ { i } : i = 0 , \ldots , m \}$ be the affine open cover of $\mathbb { P } ^ { m }$ with $V _ { i } = \left\{ \left( y _ { 0 } : \cdots : y _ { m } \right) : y _ { i } \neq 0 \right\}$ for all $i$ . Then the open subsets $U _ { i } : = f ^ { - 1 } ( V _ { i } ) = \{ x \in X : f _ { i } ( x ) \neq 0 \}$ cover $U$ , and in the affine coordinates $\frac { y _ { j } } { y _ { i } }$ on $V _ { i }$ the map $f | _ { U _ { i } }$ is given by the quotients of polynomials $\frac { f _ { j } } { f _ { i } }$ for $j = 0 , \ldots , m$ with $j \neq i$ , which are regular functions on $U _ { i }$ by Definition 7.1. Hence $f | _ { U _ { i } }$ is a morphism by Proposition 4.7, and so $f$ is a morphism by Lemma 4.6. 

# Example 7.5.

(a) Let $A \in \mathrm { G L } ( n + 1 , K )$ be an invertible matrix. Then $f \colon  { \mathbb { P } } ^ { n } \to  { \mathbb { P } } ^ { n }$ , $x \mapsto A x$ is a morphism with inverse $f ^ { - 1 } \colon \mathbb { P } ^ { n } \to \mathbb { P } ^ { n }$ , $x \mapsto A ^ { - 1 } x .$ , and hence an isomorphism. We will refer to these maps as projective automorphisms of $\mathbb P ^ { n }$ . In fact, one can show that these are the only isomorphisms of $\mathbb { P } ^ { n }$ .   
(b) Let $a = ( 1 : 0 : \dots : 0 ) \in \mathbb { P } ^ { n }$ and $L = V ( x _ { 0 } ) \cong \mathbb { P } ^ { n - 1 }$ . Then the map $f \colon \mathbb { P } ^ { n } \backslash \left\{ a \right\} \to \mathbb { P } ^ { n - 1 } , ( x _ { 0 } \colon \cdots \colon x _ { n } ) \mapsto \left( x _ { 1 } \colon \cdots \colon x _ { n } \right)$ given by forgetting one of the homogeneous coordinates is a morphism by Lemma 7.4. It can be interpreted as in the picture below on the left: For $x = ( x _ { 0 } ! \cdots : x \cdot x _ { n } ) \in \mathbb { P } ^ { n } \backslash \{ a \}$ the unique line through $a$ and $x$ is given parametrically by

$$
\{ \left( s : t x _ { 1 } : \dots : t x _ { n } \right) : \left( s : t \right) \in \mathbb { P } ^ { 1 } \} ,
$$

and its intersection point with $L$ is $\left( 0 { : } x _ { 1 } : \cdots : x _ { n } \right)$ , i. e. $f ( x )$ with the identification $L \cong \mathbb { P } ^ { n - 1 }$ . We call $f$ the projection from $a$ to the linear subspace $L$ . Note however that the picture below does not show a standard affine open subset $U _ { i } = \left\{ \left( x _ { 0 } : \cdot \cdot \cdot : x _ { n } \right) : x _ { i } \neq 0 \right\}$ , since none of these subsets contains both $a$ and (a non-empty open subset of) $L$ .

Of course, the same construction works for any point $a \in \mathbb { P } ^ { n }$ and any linear subspace $L$ of dimension $n - 1$ not containing $a$ — the corresponding morphism then differs from the special one considered above by a projective automorphism as in (a).

![](images/786d66a2dd685a5b8a0ef5f182b96eff0dd9bb15449667393c3f349e3344d351.jpg)

(c) The projection morphism $f \colon \mathbb { P } ^ { n } \backslash \{ a \}  \mathbb { P } ^ { n - 1 }$ as in (b) cannot be extended to the point $a$ . The intuitive reason for this is that the line through $a$ and $x$ (and thus also the point $f ( x ) )$ does not have a well-defined limit as $x$ approaches $a$ . This changes however if we restrict the projection to a suitable projective variety: For $X = V ( x _ { 0 } x _ { 2 } - x _ { 1 } ^ { 2 } )$ as in the schematic picture above on the right consider the map

$$
f \colon X \to \mathbb { P } ^ { 1 } , ( x _ { 0 } { \colon } x _ { 1 } { \colon } x _ { 2 } ) \mapsto { \{ \begin{array} { l l } { ( x _ { 1 } { \mathrel {  { \vphantom { ( { x } _ { 1 } }  { \kern - delimiterspace } } x _ { 2 } ) } } } & { { \mathrm { i f } } ( x _ { 0 } { \mathrel {  { \vphantom { ( { x } _ { 0 } }  { \kern - delimiterspace } } x _ { 1 } ) } } ) } \neq ( 1 { \mathrel {  { \vphantom { ( { 1 } } 0 { \mathrel {  { \vphantom { ( { x } _ { 0 } }  { \kern - delimiterspace } } x _ { 2 } ) } } ) } } } , } \\ { ( x _ { 0 } { \mathrel {  { \vphantom { ( { x } _ { 0 } }  { \kern - delimiterspace } } x _ { 1 } ) } } } & { { \mathrm { i f } } ( x _ { 0 } { \mathrel {  { \vphantom { ( { x } _ { 0 } }  { \kern - delimiterspace } } x _ { 1 } ) } } ) } \neq ( 0 { \mathrel { \mathop { \mathopen { ( { 0 } } \colon 0 ) } } } 1 ) .  \end{array}  
$$

It is clearly well-defined since the equation $x _ { 0 } x _ { 2 } - x _ { 1 } ^ { 2 } = 0 { \mathrm { ~ i m p l i e s ~ } } ( x _ { 1 } : x _ { 2 } ) = ( x _ { 0 } : x _ { 1 } )$ whenever both these points in $\mathbb { P } ^ { 1 }$ are defined. Moreover, it extends the projection as in (b) to all of $X$ (which includes the point $a$ ), and it is a morphism since it is patched together from two projections as above. Geometrically, the image $f ( a )$ is the intersection of the tangent to $X$ at $a$ with the line $L$ .

This geometric picture also tells us that $f$ is bijective: For every point $y \in L$ the restriction of the polynomial $x _ { 0 } x _ { 2 } - x _ { 1 } ^ { 2 }$ defining $X$ to the line through $a$ and $y$ has degree 2, and thus this line intersects $X$ in two points (counted with multiplicities), of which one is $a$ . The other point is then the unique inverse image $f ^ { - 1 } ( y )$ . In fact, it is easy to check that $f$ is even an isomorphism since its inverse is

$$
f ^ { - 1 } \colon  { \mathbb { P } } ^ { 1 } \to X , ( y _ { 0 } : y _ { 1 } ) \mapsto ( y _ { 0 } ^ { 2 } : y _ { 0 } y _ { 1 } : y _ { 1 } ^ { 2 } ) ,
$$

which is a morphism by Lemma 7.4.

Note that the example of the morphism $f$ above also shows that we cannot expect every morphism between projective varieties to have a global description by homogeneous polynomials as in Lemma 7.4.

(d) Now let $X \subset \mathbb { P } ^ { 2 }$ be any projective conic, i. e. an irreducible quadric curve. Assuming that char $K \neq 2$ , we know by Exercise 4.12 that the affine part $X \cap \mathbb { A } ^ { 2 }$ is isomorphic to $V _ { \mathrm { a } } ( x _ { 2 } - x _ { 1 } ^ { 2 } )$ or $V _ { \mathrm { a } } ( x _ { 1 } x _ { 2 } - 1 )$ by a linear transformation followed by a translation. Extending this map to a projective automorphism of $\mathbb { P } ^ { 2 }$ as in (a), the projective conic $X$ thus becomes isomorphic to $V _ { \mathrm { p } } ( x _ { 0 } x _ { 2 } - x _ { 1 } ^ { 2 } )$ or $V _ { \mathrm { p } } ( x _ { 1 } x _ { 2 } - x _ { 0 } ^ { 2 } )$ by Proposition 6.31 (b). So by (c) we see that every projective conic is isomorphic to $\mathbb { P } ^ { 1 }$ .

Exercise 7.6. Show by example that the homogeneous coordinate ring of a projective variety is not invariant under isomorphisms, i.e. that there are isomorphic projective varieties $X , Y$ such that the rings $S ( X )$ and $S ( Y )$ are not isomorphic.

Exercise 7.7. Let $m , n \in \mathbb { N } _ { > 0 }$ . Prove:

(a) If $f \colon  { \mathbb { P } } ^ { n } \to  { \mathbb { P } } ^ { m }$ is a morphism and $X \subset \mathbb { P } ^ { m }$ a hypersurface then every irreducible component of $f ^ { - 1 } ( X )$ has dimension at least $n - 1$ .   
(b) If $n > m$ then every morphism $f \colon  { \mathbb { P } } ^ { n } \to  { \mathbb { P } } ^ { m }$ is constant.   
(c) $\mathbb { P } ^ { n } \times \mathbb { P } ^ { m }$ is not isomorphic to $\mathbb { P } ^ { n + m }$ .

Let us now verify that projective varieties are separated, i. e. that they are varieties and not just prevarieties. In other words, we have to check that the diagonal $\Delta _ { X }$ of a projective variety $X$ is closed in the product $X \times X$ . By Lemma 5.18 (b) it suffices to show this for $X = \mathbb { P } ^ { n }$ .

For the proof of this statement it is useful to first find a good description of the product of projective spaces — note that by Exercise 7.7 (c) such products are not just again projective spaces. Of course, we could just parametrize these products by two sets of homogeneous coordinates. It turns out however that we can also use a single set of homogeneous coordinates and thus embed products of projective spaces as a projective variety into a bigger projective space.

Construction 7.8 (Segre embedding). Consider $\mathbb P ^ { n }$ with homogeneous coordinates $x _ { 0 } , \ldots , x _ { n }$ and $\mathbb { P } ^ { m }$ with homogeneous coordinates $y _ { 0 } , \ldots , y _ { m }$ . Set $N = ( n + 1 ) ( m + 1 ) - 1$ and let $\mathbb { P } ^ { N }$ be the projective space with homogeneous coordinates labeled $z _ { i , j }$ for $0 \leq i \leq n$ and $0 \le j \le m$ . Then there is an obviously well-defined set-theoretic map

$$
f \colon  { \mathbb { P } } ^ { n } \times  { \mathbb { P } } ^ { m } \to  { \mathbb { P } } ^ { N }
$$

given by $z _ { i , j } = x _ { i } y _ { j }$ for all $i , j$ . It satisfies the following properties:

Proposition 7.9. Let $f \colon  { \mathbb { P } } ^ { n } \times  { \mathbb { P } } ^ { m } \to  { \mathbb { P } } ^ { N }$ be the map of Construction 7.8. Then:

(a) The image $X = f ( \mathbb { P } ^ { n } \times \mathbb { P } ^ { m } )$ is a projective variety given by

$$
X = V _ { p } ( z _ { i , j } z _ { k , l } - z _ { i , l } z _ { k , j } : 0 \leq i , k \leq n , 0 \leq j , l \leq m ) .
$$

(b) The map $f \colon \mathbb { P } ^ { n } \times \mathbb { P } ^ { m } \to X$ is an isomorphism.

In particular, $\mathbb { P } ^ { n } \times \mathbb { P } ^ { m } \cong X$ is a projective variety. The isomorphism $f \colon  { \mathbb { P } } ^ { n } \times  { \mathbb { P } } ^ { m } \to X \subset  { \mathbb { P } } ^ { N }$ is called the Segre embedding; the coordinates $z _ { 0 , 0 } , \ldots , z _ { n , m }$ above will be referred to as Segre coordinates on $\mathbb { P } ^ { n } \times \mathbb { P } ^ { m }$ .

# Proof.

(a) It is obvious that the points of $f ( \mathbb { P } ^ { n } \times \mathbb { P } ^ { m } )$ satisfy the given equations. Conversely, consider a point $z \in \mathbb { P } ^ { N }$ with homogeneous coordinates $z _ { 0 , 0 } , \ldots , z _ { n , m }$ that satisfy the given equations. At least one of these coordinates must be non-zero; we can assume without loss of generality that it is $z _ { 0 , 0 }$ . Let us pass to affine coordinates by setting $z _ { 0 , 0 } = 1$ . Then we have $z _ { i , j } = z _ { i , 0 } z _ { 0 , j }$ for all $i = 0 , \ldots , n$ and $j = 0 , \ldots , m$ . Hence by setting $x _ { i } = z _ { i , 0 }$ and $y _ { j } = z _ { 0 , j }$ (in particular $x _ { 0 } = y _ { 0 } = 1 .$ ) we obtain a point of $\mathbb { P } ^ { n } \times \mathbb { P } ^ { m }$ that is mapped to $z$ by $f$ .   
(b) Continuing the above notation, let $z \in X$ be a point with $z _ { 0 , 0 } = 1$ . If $f ( x , y ) = z $ for some $( x , y ) \in \mathbb { P } ^ { n } \times \mathbb { P } ^ { m }$ , it follows that $x _ { 0 } \neq 0$ and $y _ { 0 } \neq 0$ , so we can pass to affine coordinates here as well and assume that $x _ { 0 } = 1$ and $y _ { 0 } = 1$ . But then it follows that $x _ { i } = z _ { i , 0 }$ and $y _ { j } = z _ { 0 , j }$ for all $i$ and $j$ , i. e. $f$ is injective and thus as a map onto its image also bijective. The same calculation shows that $f$ and $f ^ { - 1 }$ are given (locally in affine coordinates) by polynomial maps. Hence $f$ is an isomorphism. 

Example 7.10 (Segre embedding of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ ). According to Proposition 7.9, the product $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ is (isomorphic to) the quadric surface

$$
\begin{array} { r l } { X = \{ ( z _ { 0 , 0 } : z _ { 0 , 1 } : z _ { 1 , 0 } : z _ { 1 , 1 } ) : z _ { 0 , 0 } z _ { 1 , 1 } = z _ { 1 , 0 } z _ { 0 , 1 } \} } & { { } \subset \mathbb { P } ^ { 3 } } \end{array}
$$

by the isomorphism

$$
f \colon \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } \to X , ( \left( x _ { 0 } \colon x _ { 1 } \right) , ( y _ { 0 } \colon y _ { 1 } ) ) \mapsto ( x _ { 0 } y _ { 0 } \colon x _ { 0 } y _ { 1 } \colon x _ { 1 } y _ { 0 } \colon x _ { 1 } y _ { 1 } ) .
$$

In particular, the “lines” $\{ a \} \times \mathbb { P } ^ { 1 }$ and $\mathbb { P } ^ { 1 } \times \{ a \}$ in $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ where the first or second factor is constant, respectively, are mapped to lines in $X \subset \mathbb { P } ^ { 3 }$ . The following schematic picture shows these two families of lines on the surface $X$ (whose set of real points is a hyperboloid).

![](images/ae38413757eb5980dc318789e4f6c6bf7ee949df2091cf9eee205822f09c490f.jpg)  
Corollary 7.11. Every projective variety is a variety.

Proof. We have already seen in proposition 7.2 that every projective variety is a prevariety. So by Lemma 5.18 (b) it only remains to be shown that $\mathbb P ^ { n }$ is separated, i. e. that the diagonal $\Delta { \mathbb { P } } ^ { n }$ is closed in $\mathbb { P } ^ { n } \times \mathbb { P } ^ { n }$ . We can describe this diagonal as

$$
\Delta _ { \mathbb { P } ^ { n } } = { \big \{ } { \big ( } ( x _ { 0 } : \cdots : x _ { n } ) , ( y _ { 0 } : \cdots : y _ { n } ) { \big ) } : x _ { i } y _ { j } - x _ { j } y _ { i } = 0 { \mathrm { ~ f o r ~ a l l ~ } } i , j { \big \} } ,
$$

because these equations mean exactly that the matrix

$$
\left( \begin{array} { c c c c } { x _ { 0 } } & { x _ { 1 } } & { \cdots } & { x _ { n } } \\ { y _ { 0 } } & { y _ { 1 } } & { \cdots } & { y _ { n } } \end{array} \right)
$$

has rank (at most) 1, i. e. that $( x _ { 0 } \colon \cdot \cdot \cdot : x _ { n } ) = ( y _ { 0 } \colon \cdot \cdot \cdot : y _ { n } )$ . In particular, it follows that $\Delta { \mathbb { P } } ^ { n }$ is closed as the zero locus of the homogeneous linear polynomials $z _ { i , j } - z _ { j , i }$ in the Segre coordinates $z _ { i , j } = x _ { i } y _ { j }$ of $\mathbb { P } ^ { n } \times \mathbb { P } ^ { n }$ . 

Remark 7.12. If $X \subset \mathbb { P } ^ { m }$ and $Y \subset \mathbb { P } ^ { n }$ are projective varieties then $X \times Y$ is a closed subset of $\mathbb { P } ^ { m } \times \mathbb { P } ^ { n }$ . As the latter is a projective variety by the Segre embedding we see that $X \times Y$ is a projective variety as well (namely a projective subvariety of $\mathbb { P } ^ { m } \times \mathbb { P } ^ { n } )$ .

Exercise 7.13. Let $X \subset \mathbb { P } ^ { 2 }$ be a cubic curve. Moreover, let $U \subset X \times X$ be the set of all $( a , b ) \in X \times X$ such that $a \neq b$ and the unique line through the two points $a$ and $^ b$ meets $X$ in exactly three distinct points. Of course, two of these points must then be $a$ and $^ b$ ; we will denote the third one by $f ( a , b ) \in X$ .

$$
\sum \limits _ { X } ^ { \infty } f ( a , b )
$$

Show that $U \subset X \times X$ is open, and that $f \colon U \to X$ is a morphism.

Note that in the “Plane Algebraic Curves” class it was shown that, for a smooth cubic curve $X$ , the morphism $f$ can be extended to a map $X \times X \to X$ that can be used to construct a group structure on $X$ [G2, Chapter 7].

Exercise 7.14. Show by example that not every hypersurface $Y$ in a projective variety $X$ is of the form $V ( f )$ for a homogeneous polynomial $f \in S ( X )$ . (One possibility is to consider the Segre embedding $X$ of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ in $\mathbb { P } ^ { 3 }$ , and $Y = \mathbb { P } ^ { 1 } \times \{ 0 \} \subset \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } .$ .)

The most important property of projective varieties is that they are compact in the classical topology if the ground field is $\mathbb { C }$ . We have seen this already for projective spaces in Remark 6.4, and it then follows for projective varieties as well since they are closed subsets of them. However, Exercise 2.36 (b) shows unfortunately that every prevariety is compact in the Zariski topology (since it is a Noetherian topological space), and so in particular that compactness in the Zariski topology does not capture the same geometric idea as in the classical case. We therefore need an alternative description of the intuitive compactness property that works in our algebraic setting of the Zariski topology.

The key idea to achieve this is that compact sets should be mapped to compact sets again under continuous maps. In our language, this means that images of morphisms between projective varieties should be closed. This property (that we have already seen to be false for general varieties in Remark 5.13 (a)) is what we want to prove now. We start with a special case which contains all the hard work, and from which the general case will then follow easily.

Definition 7.15 (Closed maps). A map $f \colon X \to Y$ between topological spaces is called closed if $f ( A ) \subset Y$ is closed for every closed subset $A \subset X$ .

Proposition 7.16. The projection map $\pi \colon \mathbb { P } ^ { n } \times \mathbb { P } ^ { m }  \mathbb { P } ^ { m }$ is closed.

Proof. Let $Z \subset \mathbb { P } ^ { n } \times \mathbb { P } ^ { m }$ be a closed set. By Remark 6.22 we can write $Z = V ( f _ { 1 } , \dots , f _ { r } )$ for homogeneous polynomials $f _ { 1 } , \ldots , f _ { r }$ of the same degree $d$ in the Segre coordinates of $\mathbb { P } ^ { n } \times \mathbb { P } ^ { m }$ , i. e. for bihomogeneous polynomials of degree $d$ in both the coordinates $x _ { 0 } , \ldots , x _ { n }$ of $\mathbb { P } ^ { n }$ and $y _ { 0 } , \ldots , y _ { m }$ of $\mathbb { P } ^ { m }$ . Now consider a fixed point $a \in \mathbb { P } ^ { m }$ ; we will determine if it is contained in the image $\pi ( Z )$ . To do this, let $g _ { i } = f _ { i } ( \cdot , a ) \in K [ x _ { 0 } , \ldots , x _ { n } ]$ for $i = 1 , \ldots , r$ . Then

$$
{ \begin{array} { r l } & { \Leftrightarrow V _ { \mathrm { p } } ( g _ { 1 } , \ldots , g _ { r } ) = \emptyset } \\ & { \Leftrightarrow { \sqrt { \left. g _ { 1 } , \ldots , g _ { r } \right. } } = \left. 1 \right. { \mathrm { o r } } { \sqrt { \left. g _ { 1 } , \ldots , g _ { r } \right. } } = \left. x _ { 0 } , \ldots , x _ { n } \right. \quad { \mathrm { ( P r o p o s i t i o n ~ } } 6 . 1 { \mathrm { ) } } } \\ & { \Leftrightarrow { \mathrm { t h e r e ~ a r e ~ } } k _ { i } \in { \mathbb { N } } { \mathrm { ~ w i t h ~ } } x _ { i } ^ { k _ { i } } \in \left. g _ { 1 } , \ldots , g _ { r } \right. { \mathrm { f o r ~ a l l ~ } } i } \\ & { \Leftrightarrow K [ x _ { 0 } , \ldots , x _ { n } ] _ { k } \subset \left. g _ { 1 } , \ldots , g _ { r } \right. { \mathrm { f o r ~ s o m e ~ } } k \in \mathbb { N } , } \end{array} }
$$

where as usual $K [ x _ { 0 } , \ldots , x _ { n } ] _ { k }$ denotes the homogeneous degree- $k$ part of the polynomial ring as in Definition 6.6, and the direction $\ " \Rightarrow \ "$ of the last equivalence follows by setting $k = k _ { 0 } + \cdots + k _ { n }$ . The last condition can only be satisfied if $k \geq d$ and is equivalent to $K [ x _ { 0 } , \ldots , x _ { n } ] _ { k } = \langle g _ { 1 } , \ldots , g _ { r } \rangle _ { k }$ . As $\langle g _ { 1 } , \ldots , g _ { r } \rangle = \left\{ h _ { 1 } g _ { 1 } + \cdots + h _ { r } g _ { r } : h _ { 1 } , \ldots , h _ { r } \in K [ x _ { 0 } , \ldots , x _ { n } ] \right\}$ this is the same as saying that the $K$ -linear map

$$
F _ { k } \colon ( K [ x _ { 0 } , \ldots , x _ { n } ] _ { k - d } ) ^ { r } \to K [ x _ { 0 } , \ldots , x _ { n } ] _ { k } , ( h _ { 1 } , \ldots , h _ { r } ) \mapsto h _ { 1 } g _ { 1 } + \cdots h _ { r } g _ { r }
$$

is surjective, i. e. has rank $\begin{array} { r } { \dim _ { K } K [ x _ { 0 } , \ldots , x _ { n } ] _ { k } = { \binom { n + k } { k } } } \end{array}$ for some $k \geq d$ . This in turn is the case if and only if at least one of the minors of size  n+kk  of a matrix for some Fk is non-zero. But these minors are polynomials in the coefficients of $g$ and thus in the coordinates of $a$ , and consequently the non-vanishing of one of these minors is an open condition in the Zariski topology of $\mathbb { P } ^ { m }$ .

Hence the set of all $a \in \mathbb { P } ^ { m }$ with $a \not \in \pi ( Z )$ is open, which means that $\pi ( Z )$ is closed.

Remark 7.17. Let us look at Proposition 7.16 from an algebraic point of view. We start with some equations $f _ { 1 } ( x , y ) = \dots = f _ { r } ( x , y ) = 0$ in two sets of variables $x = ( x _ { 0 } , \ldots , x _ { n } ) $ and $y = ( y _ { 0 } , \ldots , y _ { m } )$ and ask for the image of their common zero locus under the projection map $( x , y ) \mapsto y$ . The equations satisfied on this image are precisely the equations in $y$ alone that can be derived from the given ones $f _ { 1 } ( x , y ) = \dots = f _ { r } ( x , y ) = 0$ in $x$ and $y$ . In other words, we want to eliminate the variables $x$ from the given system of equations. The statement of Proposition 7.16 is therefore sometimes called the main theorem of elimination theory.

Corollary 7.18. The projection map $\pi \colon \mathbb { P } ^ { n } \times Y  Y$ is closed for any variety $Y$

Proof. Let us first show the statement for an affine variety $Y \subset \mathbb { A } ^ { m }$ . Let $Z \subset \mathbb { P } ^ { n } \times Y$ be closed, and let $\overline { Z }$ be its closure in $\mathbb { P } ^ { n } \times \mathbb { P } ^ { m }$ . If $\pi \colon \mathbb { P } ^ { n } \times \mathbb { P } ^ { m }  \mathbb { P } ^ { m }$ is the projection map then $\pi ( { \overline { { Z } } } )$ is closed in $\mathbb { P } ^ { m }$ by Proposition 7.16, and thus

$$
\pi ( Z ) = \pi ( \overline { { { Z } } } \cap ( \mathbb { P } ^ { n } \times Y ) ) = \pi ( \overline { { { Z } } } ) \cap Y
$$

is closed in $Y$

If $Y$ is any variety we can cover it by affine open subsets. As the condition that a subset is closed can be checked by restricting it to the elements of an open cover, the statement follows from the corresponding one for the affine open patches that we have just shown. 

It is in fact this property of Corollary 7.18 that captures the classical idea of compactness. Let us therefore give it a name:

Definition 7.19 (Complete varieties). A variety $X$ is called complete if the projection $\pi \colon X \times Y \to Y$ is closed for any variety $Y$ .

# Example 7.20.

(a) $\mathbb { P } ^ { n }$ is complete by Corollary 7.18.

(b) Any closed subvariety $X ^ { \prime }$ of a complete variety $X$ is complete: If $Z \subset X ^ { \prime } \times Y$ is closed then $Z$ is also closed in $X \times Y$ , and hence its image under the second projection to $Y$ is closed as well. In particular, by (a) this means that every projective variety is complete.

(c) $\mathbb { A } ^ { 1 }$ is not complete: As in the picture below on the left, the image $\pi ( Z )$ of the closed subset $Z = V ( x _ { 1 } x _ { 2 } - 1 ) \subset \mathbb { A } ^ { 1 } \times \mathbb { A } ^ { 1 }$ under the second projection is $\mathbb { A } ^ { 1 } \backslash \{ 0 \}$ , which is not closed.

![](images/16cff830ba96c7a9698f99832355b966bdda6379561dc38dd9a253a5afa68d4c.jpg)

The geometric reason for this is that $\mathbb { A } ^ { 1 }$ is missing a point at infinity: If we replace $\mathbb { A } ^ { 1 }$ by $\mathbb { P } ^ { 1 }$ as in the picture on the right there is an additional point in the closure $\overline { Z }$ of $Z \subset \mathbb { A } ^ { 1 } \times \mathbb { A } ^ { 1 }$ in $\mathbb { P } ^ { 1 } \times \mathbb { A } ^ { 1 }$ ; the image of this point under $\pi$ fills the gap and makes $\pi ( { \overline { { Z } } } )$ a closed set. Intuitively, one can think of the name “complete” as coming from the geometric idea that it contains all the “points at infinity” that are missing in affine varieties.

Remark 7.21. There are complete varieties that are not projective, but this is actually quite hard to show — we will certainly not meet such an example in this course. So for practical purposes you can usually assume that the terms “projective variety” and “complete variety” are synonymous.

In any case, complete varieties now have the property that we were aiming for:

Corollary 7.22. Let $f \colon X \to Y$ be a morphism of varieties. If $X$ is complete then its image $f ( X )$ is closed in Y .

Proof. By Proposition 5.19 (a) the graph $\Gamma _ { f } \subset X \times Y$ is closed. But then $f ( X ) = \pi ( \Gamma _ { f } )$ for the projection map $\pi \colon X \times Y \to Y$ , which is closed again since $X$ is complete. 

Let us conclude this chapter with two applications of this property.

Corollary 7.23. Let X be a connected complete variety. Then ${ \mathcal { O } } _ { X } ( X ) = K$ , i. e. every global regular function on $X$ is constant.

Proof. A global regular function $\varphi \in { \mathcal { O } } _ { X } ( X )$ determines a morphism $\varphi : X \to \mathbb { A } ^ { 1 }$ . By extension of the target we can consider this as a morphism $\varphi \colon X \to \mathbb { P } ^ { 1 } = \mathbb { A } ^ { 1 } \cup \{ \infty \}$ whose image $\varphi ( X ) \subset \mathbb { P } ^ { 1 }$ does not contain the point $\infty$ . But $\varphi ( \boldsymbol X )$ is also closed by Corollary 7.22 since $X$ is complete, and hence it must be a finite set since these are the only closed proper subsets of $\mathbb { P } ^ { 1 }$ . Moreover, Exercise 2.22 (a) implies that $\varphi ( \boldsymbol X )$ is connected since $X$ is. Altogether this means that $\varphi ( \boldsymbol X )$ is a single point, i. e. that $\varphi$ is constant. 

Remark 7.24. Corollary 7.23 is another instance of a result that has a counterpart in complex analysis: A holomorphic function on the compact space $\mathbb { P } _ { \mathbb { C } } ^ { 1 } = \mathbb { C } \cup \{ \infty \}$ is bounded (since it is continuous), and Liouville’s Theorem asserts that every bounded holomorphic function on $\mathbb { C }$ is constant. More generally, it can be shown that every holomorphic function on a connected compact complex manifold is constant.

Construction 7.25 (Veronese embedding). Choose $n , d \in  { \mathbb { N } } _ { > 0 }$ , and let $f _ { 0 } , \dots , f _ { N } \in K [ x _ { 0 } , \dots , x _ { n } ]$ for $N = { \binom { n + d } { n } } - 1$ be the set of all monomials of degree $d$ in the variables $x _ { 0 } , \ldots , x _ { n }$ , in any order. Consider the map

$$
F \colon \mathbb { P } ^ { n } \to \mathbb { P } ^ { N } , x \mapsto { \big ( } f _ { 0 } ( x ) \colon \cdots \colon f _ { N } ( x ) { \big ) } .
$$

By Lemma 7.4 this is a morphism (note that the monomials $x _ { 0 } ^ { d } , \ldots , x _ { n } ^ { d }$ , which cannot be simultaneously zero, are among the $f _ { 0 } , \ldots , f _ { N } )$ . So by Corollary 7.22 the image $X = F ( \mathbb { P } ^ { n } )$ is a projective variety.

We claim that $F \colon \mathbb { P } ^ { n } \to X$ is an isomorphism. All we have to do to prove this is to find an inverse morphism. This is not hard: We can do this on an affine open cover, so let us consider the open subset where $x _ { i } \neq 0$ , i. e. $x _ { i } ^ { d } \neq 0$ for some $i$ . On this set we can pass to affine coordinates and set $x _ { i } = 1$ . The inverse morphism is then given by $\begin{array} { r } { x _ { j } = \frac { x _ { j } x _ { i } ^ { d - 1 } } { x _ { i } ^ { d } } } \end{array}$ for all $j \neq i$ , which is a quotient of two degree- $^ { d }$ monomials.

The morphism $F$ is therefore an isomorphism and thus realizes $\mathbb P ^ { n }$ as a subvariety $X$ of $\mathbb { P } ^ { N }$ . It is usually called the degree- $^ { \cdot d }$ Veronese embedding; the coordinates on $\mathbb { P } ^ { N }$ are called Veronese coordinates of $\mathbb { P } ^ { n } \cong X$ . Of course, this embedding can also be restricted to any projective variety $Y \subset \mathbb { P } ^ { n }$ and then gives an isomorphism by degree- $d$ polynomials between $Y$ and a projective variety in $\mathbb { P } ^ { N }$ .

The importance of the Veronese embedding lies in the fact that degree- $^ { d }$ polynomials in the coordinates of $\mathbb { P } ^ { n }$ are translated into linear polynomials in the Veronese coordinates. An example where this is useful will be given in Corollary 7.28.

# Example 7.26.

(a) For $d = 1$ the Veronese embedding of $\mathbb P ^ { n }$ is just the identity $\mathbb { P } ^ { n } \to \mathbb { P } ^ { n }$ . (b) For $n = 1$ the degree- $^ { \cdot d }$ Veronese embedding of $\mathbb { P } ^ { 1 }$ in $\mathbb { P } ^ { d }$ is $F \colon \mathbb { P } ^ { 1 } \to \mathbb { P } ^ { d } , ( x _ { 0 } \colon x _ { 1 } ) \mapsto ( x _ { 0 } ^ { d } \colon x _ { 0 } ^ { d - 1 } x _ { 1 } \colon \cdot \cdot \colon x _ { 0 } x _ { 1 } ^ { d - 1 } \colon x _ { 1 } ^ { d } ) .$

In the case $d = 2$ we have already seen in Example 7.5 (c) that this is an isomorphism.

# Exercise 7.27.

(a) For any $n , d \in  { \mathbb { N } } _ { > 0 }$ , find explicit equations describing the image of the degree- $d$ Veronese embedding of $\mathbb P ^ { n }$ in $\mathbb { P } ^ { N }$ , where $N = \overset { \vartriangle } { \boldsymbol { \binom { n + d } { n } } } - 1$ .   
(b) Prove that every projective variety is isomorphic to the zero locus of quadratic polynomials in a projective space.

Corollary 7.28. Let $X \subset \mathbb { P } ^ { n }$ be a projective variety, and let $f \in S ( X )$ be homogeneous and nonconstant. Then $X \backslash V ( f )$ is an affine variety.

Proof. If $f = x _ { 0 }$ this is just Proposition 7.2. For a general linear polynomial $f$ the statement follows from this after a projective automorphism as in Example 7.5 (a) that takes $f$ to $x _ { 0 }$ , and if $f$ is of degree $d > 1$ we can reduce the claim to the linear case by first applying the degree- $d$ Veronese embedding of Construction 7.25. 

Exercise 7.29. Recall from Example 7.5 (d) that a conic in $\mathbb { P } ^ { 2 }$ over a field of characteristic not equal to 2 is an irreducible quadric curve.

(a) Considering the coefficients of such polynomials, show that the set of all conics in $\mathbb { P } ^ { 2 }$ can be identified with an open subset $U$ of the projective space $\mathbb { P } ^ { 5 }$ .   
(b) Let $a \in \mathbb { P } ^ { 2 }$ . Show that the subset of $U$ consisting of all conics passing through $a$ is the zero locus of a linear equation in the homogeneous coordinates of $U \subset \mathbb { P } ^ { 5 }$ .   
(c) Given 5 points in $\mathbb { P } ^ { 2 }$ , no three of which lie on a line, show that there is a unique conic in $\mathbb { P } ^ { 5 }$ passing through all these points.

Exercise 7.30. Let $X \subset \mathbb { P } ^ { 3 }$ be the degree-3 Veronese embedding of $\mathbb { P } ^ { 1 }$ , i. e. the image of the morphism

$$
\mathbb { P } ^ { 1 } \to \mathbb { P } ^ { 3 } , ( x _ { 0 } : x _ { 1 } ) \mapsto ( y _ { 0 } : y _ { 1 } : y _ { 2 } : y _ { 3 } ) = ( x _ { 0 } ^ { 3 } : x _ { 0 } ^ { 2 } x _ { 1 } : x _ { 0 } x _ { 1 } ^ { 2 } : x _ { 1 } ^ { 3 } ) .
$$

Moreover, let $a = ( 0 : 0 : 1 : 0 ) \in \mathbb { P } ^ { 3 }$ and $L = V ( y _ { 2 } ) \subset \mathbb { P } ^ { 3 }$ , and consider the projection $f$ from $a$ to $L$ as in Example 7.5 (b).

(a) Show that $f$ is a morphism. (b) Determine an equation of the curve $f ( X )$ in $L \cong \mathbb { P } ^ { 2 }$ . (c) Is $f \colon X \to f ( X )$ an isomorphism onto its image?

# 8. Grassmannians

After having introduced affine and projective varieties, let us now take a break in our discussion of the general theory to construct an interesting and useful class of examples. The idea behind this construction is simple: Since the definition of projective spaces as the sets of 1-dimensional linear subspaces of $K ^ { n }$ turned out to be a very useful concept, let us now generalize this and consider instead the sets of $k$ -dimensional linear subspaces of $K ^ { n }$ for an arbitrary $k = 0 , \ldots , n$ .

Definition 8.1 (Grassmannians). Let $n \in  { \mathbb { N } } _ { > 0 }$ , and let $k \in \mathbb N$ with $0 \leq k \leq n$ . We denote by $G ( k , n )$ the set of all $k$ -dimensional linear subspaces of $K ^ { n }$ . It is called the Grassmannian of $k$ -planes in $K ^ { n }$ .

Remark 8.2. By Example 6.12 (b) and Exercise 6.30 (a), Lemma 6.17 shows that $k$ -dimensional linear subspaces of $K ^ { n }$ for $k > 0$ are in natural bijection with $\left( k - 1 \right)$ -dimensional linear subspaces of $\mathbb { P } ^ { n - 1 }$ . We can therefore consider $G ( k , n )$ alternatively as the set of such projective linear subspaces. As the dimensions $k$ and $n$ are reduced by 1 in this way, our Grassmannian $G ( k , n )$ of Definition 8.1 is sometimes written in the literature as $G ( k - 1 , n - 1 )$ instead.

Of course, as in the case of projective spaces our goal must again be to make the Grassmannian $G ( k , n )$ into a variety. In fact, we will see that it is even a projective variety in a natural way. For this we need the algebraic concept of alternating tensor products, a slight variant of the ordinary tensor products well-known from commutative algebra [G3, Chapter 5]. Let us briefly introduce them now.

Definition 8.3 (Alternating linear maps). Let $V$ be a vector space over $K$ , and let $k \in \mathbb N$ . A $k$ -fold) multilinear map $f \colon V ^ { k } \to W$ to another vector space $W$ is called alternating if $f ( \nu _ { 1 } , \dots , \nu _ { k } ) = 0$ for all $\nu _ { 1 } , . . . , \nu _ { k } \in V$ such that $\nu _ { i } = \nu _ { j }$ for some $i \neq j$ .

Remark 8.4. Let $f \colon V ^ { k } \to W$ be an alternating multilinear map, and let $\nu _ { 1 } , . . . , \nu _ { k } \in V$ . Plugging in $\nu _ { i } + \nu _ { j }$ as the $i$ -th and $j { \cdot }$ -th argument for $f$ we obtain by multilinearity

$$
\begin{array} { r l } & { f \bigl ( \ldots , \nu _ { i } + \nu _ { j } , \ldots , \nu _ { i } + \nu _ { j } , \ldots \bigr ) = f \bigl ( \ldots , \nu _ { i } , \ldots , \nu _ { i } , \ldots \bigr ) + f \bigl ( \ldots , \nu _ { j } , \ldots , \nu _ { j } , \ldots \bigr ) } \\ & { \qquad + f \bigl ( \ldots , \nu _ { i } , \ldots , \nu _ { j } , \ldots \bigr ) + f \bigl ( \ldots , \nu _ { j } , \ldots , \nu _ { i } , \ldots \bigr ) . } \end{array}
$$

But the three terms in the first row are 0 by Definition 8.3, and hence we obtain

$$
f ( \dots , \nu _ { j } , \dots , \nu _ { i } , \dots ) = - f ( \dots , \nu _ { i } , \dots , \nu _ { j } , \dots ) ,
$$

i. e. exchanging two arguments of $f$ multiplies the result by $^ { - 1 }$ . For any permutation $\sigma \in S _ { k }$ of the arguments (which is a composition of such exchanges) we therefore obtain

$$
f ( \nu _ { \sigma ( 1 ) } , \ldots , \nu _ { \sigma ( k ) } ) = \operatorname { s i g n } \sigma \cdot f ( \nu _ { 1 } , \ldots , \nu _ { k } ) .
$$

# Example 8.5.

(a) The determinant det: $\operatorname { M a t } ( n \times n , K ) = ( K ^ { n } ) ^ { n } \to K$ is an alternating $n$ -fold multilinear map to the ground field $K$ .

(b) The cross product

$$
f ( \nu , w ) = ( a _ { 2 } b _ { 3 } - a _ { 3 } b _ { 2 } , a _ { 3 } b _ { 1 } - a _ { 1 } b _ { 3 } , a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } )
$$

of two vectors $\nu = ( a _ { 1 } , a _ { 2 } , a _ { 3 } )$ and $w = ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$ in $K ^ { 3 }$ defines an alternating bilinear map $f \colon K ^ { 3 } \times K ^ { 3 } \to K ^ { 3 }$ .

Definition 8.6 (Alternating tensor products). Again let $V$ be a vector space over $K$ , and let $k \in \mathbb N$ .

A $k$ -fold alternating tensor product of $V$ is a vector space $T$ together with an alternating $k$ -fold multilinear map $\tau \colon V ^ { k } \to T$ satisfying the following universal property: For every $k$ -fold alternating multilinear map $f \colon V ^ { k } \to W$ to another vector space $W$ there is a unique linear map $g \colon T \to W$ with $f = g \circ \tau$ , i. e. such that the diagram on the right commutes.

$$
\sum \limits _ { T } ^ { f } \frac { f } { 2 ^ { s - \frac { s } { g } } } = \frac { 1 } { 2 }
$$

Proposition 8.7 (Existence and uniqueness of alternating tensor products). For any vector space $V$ and any $k \in \mathbb N ,$ , there is a $k$ -fold alternating tensor product $\tau \colon V ^ { k } \to T$ as in Definition 8.6, and it is unique up to unique isomorphism. We will write $T$ as $\Lambda ^ { k } V$ and $\tau ( \nu _ { 1 } , \ldots , \nu _ { k } )$ as $\nu _ { 1 } \wedge \cdot \cdot \cdot \wedge \nu _ { k } \in \Lambda ^ { k } V$ for all $\nu _ { 1 } , \dots , \nu _ { k } \in V$ .

Proof. The proof both of the uniqueness and the existence is entirely analogous to the case of ordinary tensor products [G3, Propositions 5.4 and 5.5]. In fact, assuming the statement for ordinary tensor products, for the existence part we could also take $T = ( V \otimes \cdots \otimes V ) / L$ , where $L$ is the linear subspace generated by all tensors $\nu _ { 1 } \otimes \cdots \otimes \nu _ { k }$ with $\nu _ { 1 } , . . . , \nu _ { k } \in V$ such that $\nu _ { i } = \nu _ { j }$ for some $i \neq j$ , which satisfies the required property by the universal property of the ordinary tensor product together with Definition 8.3. 

Example 8.8. Assume that $V$ is a finite-dimensional vector space with $n : = \dim V$ , and let $e _ { 1 } , \ldots , e _ { n }$ be a basis of $V$ .

(a) In the same way as the tensors $e _ { i _ { 1 } } \otimes \cdots \otimes e _ { i _ { k } }$ for all $i _ { 1 } , \ldots , i _ { k } \in \left\{ 1 , \ldots , n \right\}$ form a basis of the ordinary $k$ -fold tensor product $V \otimes \cdots \otimes V$ [G3, Example 5.10 (a)], the alternating tensors $e _ { i _ { 1 } } \wedge \cdots \wedge e _ { i _ { k } }$ for all strictly increasing indices $i _ { 1 } < \cdots < i _ { k }$ in $\{ 1 , \ldots , n \}$ form a basis of $\Lambda ^ { k } V$ . In particular, we have $\mathrm { d i m } \Lambda ^ { k } V = { \binom { n } { k } }$ .

(b) Clearly, we have $\Lambda ^ { 0 } V = K$ and $\Lambda ^ { 1 } V = V$ . Moreover, by (a) we have $\dim \Lambda ^ { n } K ^ { n } = 1$ ; an isomorphism $\Lambda ^ { n } K ^ { n } \cong K$ is given by the determinant as in Example 8.5 (a).

(c) For $V = K ^ { 3 }$ and two vectors $\nu = a _ { 1 } e _ { 1 } + a _ { 2 } e _ { 2 } + a _ { 3 } e _ { 3 }$ and $w = b _ { 1 } e _ { 1 } + b _ { 2 } e _ { 2 } + b _ { 3 } e _ { 3 }$ in $K ^ { 3 }$ we have

$$
\nu \wedge w = \left( a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } \right) e _ { 1 } \wedge e _ { 2 } + \left( a _ { 1 } b _ { 3 } - a _ { 3 } b _ { 1 } \right) e _ { 1 } \wedge e _ { 3 } + \left( a _ { 2 } b _ { 3 } - a _ { 3 } b _ { 2 } \right) e _ { 2 } \wedge e _ { 3 } \quad \in \Lambda ^ { 2 } K ^ { 3 } .
$$

As $e _ { 1 } \wedge e _ { 2 } , e _ { 1 } \wedge e _ { 3 }$ , and $e _ { 2 } \wedge e _ { 3 }$ form a basis of $\Lambda ^ { 2 } K ^ { 3 } \cong K ^ { 3 }$ by (a), we therefore see that (up to a simple change of basis) $\nu \wedge w$ is just the cross product of $\nu$ and $w$ as in Example 8.5 (b), i. e. the cross product gives a concrete isomorphism $\Lambda ^ { 2 } K ^ { 3 } \cong K ^ { 3 }$ .

In this example, note that the coordinates of $\nu \wedge w$ are just the three $2 \times 2$ minors (i. e. the determinants of all $2 \times 2$ submatrices) of the $2 \times 3$ matrix with rows $\nu$ and $w$ . This is in fact a general phenomenon:

Remark 8.9 (Alternating tensor products and determinants). Let $0 \leq k \leq n$ , and let $\nu _ { 1 } , \ldots , \nu _ { k } \in K ^ { n }$ with basis expansions $\textstyle \nu _ { i } = \sum _ { j } a _ { i , j } e _ { j }$ for $i = 1 , \ldots , k$ with respect to the standard basis. For strictly increasing indices $i _ { 1 } < \cdots < i _ { k }$ let us determine the coefficient of the basis vector $e _ { i _ { 1 } } \wedge \cdots \wedge e _ { i _ { k } }$ of $\Lambda ^ { k } K ^ { n }$ as in Example 8.8 (a) in the tensor product $\nu _ { 1 } \wedge \dots \wedge \nu _ { k }$ . First of all, by multilinearity we have

$$
\nu _ { 1 } \wedge \cdots \wedge \nu _ { k } = \sum _ { j _ { 1 } , \ldots , j _ { k } } a _ { 1 , j _ { 1 } } \cdot \cdot \cdot a _ { k , j _ { k } } \cdot e _ { j _ { 1 } } \wedge \cdot \cdot \cdot \wedge e _ { j _ { k } } .
$$

Note that the indices $j _ { 1 } , \dots , j _ { k }$ in the products $e _ { j _ { 1 } } \wedge \dots \wedge e _ { j _ { k } }$ in the terms of this sum are not necessarily in strictly ascending order. So to figure out the coefficient of $e _ { i _ { 1 } } \wedge \cdots \wedge e _ { i _ { k } }$ in $\nu _ { 1 } \wedge \dots \wedge \nu _ { k }$ we have to sort the indices in each sum first; the resulting coefficient is then by Remark 8.5

$$
\sum \mathrm { s i g n } \sigma \cdot a _ { 1 , i _ { \sigma ( 1 ) } } \cdot \cdot \cdot a _ { k , i _ { \sigma ( k ) } } ,
$$

where the sum is taken over all permutations $\sigma$ . By definition, this is exactly the determinant of the maximal quadratic submatrix of the coefficient matrix $\left( a _ { j , i } \right) _ { j , i }$ obtained by taking only the columns $i _ { 1 } , \dots , i _ { k }$ . In other words, the coordinates of $\nu _ { 1 } \wedge \dots \wedge \nu _ { k }$ in the basis of Example 8.8 (a) are just all the maximal minors of the matrix whose rows are $\nu _ { 1 } , \ldots , \nu _ { k }$ . So the alternating tensor product can be viewed as a convenient way to encode all these minors in a single object.

As a consequence, we will see now that alternating tensor products can be used to encode the linear dependence and linear spans of vectors in a very elegant way.

Lemma 8.10. Let $\nu _ { 1 } , \ldots , \nu _ { k } \in K ^ { n }$ for some $k \leq n$ . Then $\nu _ { 1 } \wedge \dots \wedge \nu _ { k } = 0$ if and only $i f \nu _ { 1 } , \ldots , \nu _ { k }$ are linearly dependent.

Proof. By Remark 8.9, we have $\nu _ { 1 } \wedge \cdot \cdot \cdot \wedge \nu _ { k } = 0$ if and only if all maximal minors of the matrix with rows $\nu _ { 1 } , \ldots , \nu _ { k }$ are zero. But this is the case if and only if this matrix does not have full rank, i. e. if and only if $\nu _ { 1 } , \ldots , \nu _ { k }$ are linearly dependent. 

Lemma 8.11. Let $\nu _ { 1 } , \ldots , \nu _ { k } \in K ^ { n }$ and $w _ { 1 } , \ldots , w _ { k } \in K ^ { n }$ both be linearly independent. Then the alternating tensor products $\nu _ { 1 } \wedge \dots \wedge \nu _ { k }$ and $w _ { 1 } \wedge \dots \wedge w _ { k }$ are linearly dependent in $\Lambda ^ { k } K ^ { n }$ if and only $i f$ $\operatorname { L i n } ( \nu _ { 1 } , \dots , \nu _ { k } ) = \operatorname { L i n } ( w _ { 1 } , \dots , w _ { k } )$ .

Proof. As we have assumed both $\nu _ { 1 } , \ldots , \nu _ { k }$ and $w _ { 1 } , \ldots , w _ { k }$ to be linearly independent, we know by Lemma 8.10 that $\nu _ { 1 } \wedge \dots \wedge \nu _ { k }$ and $w _ { 1 } \wedge \dots \wedge w _ { k }$ are both non-zero.

$\ " \Rightarrow \ '$ Assume that $\nu _ { 1 } \wedge \cdots \wedge \nu _ { k } = \lambda w _ { 1 } \wedge \cdots \wedge w _ { k }$ for some $\lambda \in K$ . Then we have

$$
w _ { i } \wedge \nu _ { 1 } \wedge \dots \wedge \nu _ { k } = \lambda w _ { i } \wedge w _ { 1 } \wedge \dots \wedge w _ { k } = 0
$$

for all $i$ since the vector $w _ { i }$ appears twice in this alternating product. Hence the vectors $w _ { i } , \nu _ { 1 } , \ldots , \nu _ { k }$ are linearly dependent by Lemma 8.10, which means that $w _ { i } \in \operatorname { L i n } ( \nu _ { 1 } , \ldots , \nu _ { k } )$ , and thus $\operatorname { L i n } ( w _ { 1 } , \dots , w _ { k } ) \subset \operatorname { L i n } ( \nu _ { 1 } , \dots , \nu _ { k } )$ . The other inclusion then follows by symmetry.

$" \Leftarrow 2 ^ { , 3 }$ If $\nu _ { 1 } , \ldots , \nu _ { k }$ and $w _ { 1 } , \ldots , w _ { k }$ span the same subspace of $K ^ { n }$ then the basis $w _ { 1 } , \ldots , w _ { k }$ can be obtained from $\nu _ { 1 } , \ldots , \nu _ { k }$ by a finite sequence of basis transformations $\nu _ { i }  \nu _ { i } + \lambda \nu _ { j }$ and $\nu _ { i } \to \lambda \nu _ { i }$ for $\lambda \in K$ and $i \neq j$ . But as

$$
\begin{array} { r l } & { \nu _ { 1 } \wedge \cdots \wedge \nu _ { i - 1 } \wedge \big ( \nu _ { i } + \lambda \nu _ { j } \big ) \wedge \nu _ { i + 1 } \wedge \cdots \wedge \nu _ { n } = \nu _ { 1 } \wedge \cdots \wedge \nu _ { i } \wedge \cdots \wedge \nu _ { n } } \\ { \mathrm { \texttt { n d } } } & { \qquad \nu _ { 1 } \wedge \cdots \wedge \big ( \lambda \nu _ { i } \big ) \wedge \cdots \wedge \nu _ { n } = \lambda \nu _ { 1 } \wedge \cdots \wedge \nu _ { n } , } \end{array}
$$

a

these transformations change the alternating product at most by a multiplicative scalar.

We can now use our results to realize the Grassmannian $G ( k , n )$ as a subset of a projective space.

Construction 8.12 (Plücker embedding). Let $0 \leq k \leq n$ , and consider the map $f \colon G ( k , n ) \to \mathbb { P } ^ { \binom { n } { k } - 1 }$ given by sending a linear subspace $\operatorname { L i n } ( \nu _ { 1 } , \dots , \nu _ { k } ) \in G ( k , n )$ to the class of the alternating tensor v1 ∧ · · · ∧ vk ∈ ΛkKn ∼= K(nk) in P(nk)−1.

Note that this is well-defined: $\nu _ { 1 } \wedge \dots \wedge \nu _ { k }$ is non-zero by Lemma 8.10, and representing the same subspace by a different basis does not change the resulting point in $\mathbb { P } ^ { \binom { n } { k } - 1 }$ by the part $" \langle \Leftarrow "$ o f Lemma 8.11. Moreover, the map $f$ is injective by the part $\ " \Rightarrow \ "$ of Lemma 8.11. We call it the Plücker embedding of $G ( k , n )$ ; for a $k$ -dimensional linear subspace $L \in G ( k , n )$ the (homogeneous) coordinates of $f ( L )$ in $\mathbb { P } ^ { \binom { n } { k } - 1 }$ are called the Plücker coordinates of $L$ . By Remark 8.9, they are just all the maximal minors of the matrix whose rows are $\nu _ { 1 } , \ldots , \nu _ { k }$ .

In the following, we will always consider $G ( k , n )$ as a subset of $\mathbb { P } ^ { \binom { n } { k } - 1 }$ using this Plücker embedding.

# Example 8.13.

(a) The Plücker embedding of $G ( 1 , n )$ simply maps a linear subspace $\operatorname { L i n } ( a _ { 1 } e _ { 1 } + \cdots + a _ { n } e _ { n } )$ to the point $( a _ { 1 } : \cdot \cdot \cdot : a _ { n } ) \in \mathbb { P } ^ { \binom { n } { 1 } - 1 } = \mathbb { P } ^ { n - 1 }$ . Hence $G ( 1 , n ) = \mathbb { P } ^ { n - 1 }$ as expected.

(b) Consider the 2-dimensional subspace $L = \operatorname { L i n } ( e _ { 1 } + e _ { 2 } , e _ { 1 } + e _ { 3 } ) \in G ( 2 , 3 )$ of $K ^ { 3 }$ . As

$$
\left( e _ { 1 } + e _ { 2 } \right) \wedge \left( e _ { 1 } + e _ { 3 } \right) = - e _ { 1 } \wedge e _ { 2 } + e _ { 1 } \wedge e _ { 3 } + e _ { 2 } \wedge e _ { 3 } ,
$$

the coefficients $\left( - 1 : 1 : 1 \right)$ of this vector are the Plücker coordinates of $L$ in $\mathbb { P } ^ { ( _ { 2 } ^ { 3 } ) - 1 } = \mathbb { P } ^ { 2 }$ Alternatively, these are the three maximal minors of the matrix

$$
\left( \begin{array} { c c c } { { 1 } } & { { 1 } } & { { 0 } } \\ { { 1 } } & { { 0 } } & { { 1 } } \end{array} \right)
$$

whose rows are the given spanning vectors $e _ { 1 } + e _ { 2 }$ and $e _ { 1 } + e _ { 3 }$ of $L$ . Note that a change of these spanning vectors will just perform row operations on this matrix, which changes the maximal minors at most by a common constant factor. This shows again in this example that the homogeneous Plücker coordinates of $L$ are well-defined.

So far we have embedded the Grassmannian $G ( k , n )$ into a projective space, but we still have to see that it is a closed subset, i. e. a projective variety. So by Construction 8.12 we have to find suitable equations describing the alternating tensors in $\Lambda ^ { k } K ^ { n }$ that can be written as a so-called pure tensor, i. e. as $\nu _ { 1 } \wedge \dots \wedge \nu _ { k }$ for some $\nu _ { 1 } , \ldots , \nu _ { k } \in K ^ { n }$ — and not just as a linear combination of such expressions. The key lemma to achieve this is the following.

Lemma 8.14. For a fixed non-zero $\omega \in { \Lambda } ^ { k } K ^ { n }$ with $k < n$ consider the $K$ -linear map

$$
f \colon K ^ { n } \to \Lambda ^ { k + 1 } K ^ { n } , \ \nu \mapsto \nu \wedge \omega .
$$

Then rk $f \geq n - k$ , with equality holding if and only if $\omega = \nu _ { 1 } \wedge \cdot \cdot \cdot \wedge \nu _ { k }$ for some $\nu _ { 1 } , \ldots , \nu _ { k } \in K ^ { n }$ .

Example 8.15. Let $k = 2$ and $n = 4$ .

(a) For ${ \pmb { \omega } } = e _ { 1 } \wedge e _ { 2 }$ the map $f$ of Lemma 8.14 is given by

$$
\begin{array} { c } { { f ( a _ { 1 } e _ { 1 } + a _ { 2 } e _ { 2 } + a _ { 3 } e _ { 3 } + a _ { 4 } e _ { 4 } ) = \left( a _ { 1 } e _ { 1 } + a _ { 2 } e _ { 2 } + a _ { 3 } e _ { 3 } + a _ { 4 } e _ { 4 } \right) \wedge e _ { 1 } \wedge e _ { 2 } } } \\ { { { } } } \\ { { = a _ { 3 } e _ { 1 } \wedge e _ { 2 } \wedge e _ { 3 } + a _ { 4 } e _ { 1 } \wedge e _ { 2 } \wedge e _ { 4 } , } } \end{array}
$$

for $a _ { 1 } , a _ { 2 } , a _ { 3 } , a _ { 4 } \in K$ , and thus has rank rk $f = 2 = n - k$ in accordance with the statement of the lemma.

(b) For $\omega = e _ { 1 } \wedge e _ { 2 } + e _ { 3 } \wedge e _ { 4 }$ we get

$$
\begin{array} { r l } & { f \bigl ( a _ { 1 } e _ { 1 } + a _ { 2 } e _ { 2 } + a _ { 3 } e _ { 3 } + a _ { 4 } e _ { 4 } \bigr ) } \\ & { \qquad = \bigl ( a _ { 1 } e _ { 1 } + a _ { 2 } e _ { 2 } + a _ { 3 } e _ { 3 } + a _ { 4 } e _ { 4 } \bigr ) \wedge \bigl ( e _ { 1 } \wedge e _ { 2 } + e _ { 3 } \wedge e _ { 4 } \bigr ) } \\ & { \qquad = a _ { 1 } e _ { 1 } \wedge e _ { 3 } \wedge e _ { 4 } + a _ { 2 } e _ { 2 } \wedge e _ { 3 } \wedge e _ { 4 } + a _ { 3 } e _ { 1 } \wedge e _ { 2 } \wedge e _ { 3 } + a _ { 4 } e _ { 1 } \wedge e _ { 2 } \wedge e _ { 4 } } \end{array}
$$

instead, so that rk $f = 4$ . Hence Lemma 8.14 tells us that there is no way to write $\omega$ as a pure tensor $\nu _ { 1 } \wedge \nu _ { 2 }$ for some vectors $\nu _ { 1 } , \nu _ { 2 } \in K ^ { 4 }$ .

Proof of Lemma 8.14. Let $\nu _ { 1 } , \ldots , \nu _ { r }$ be a basis of $\operatorname { K e r } f$ (with $r = n - \operatorname { r k } f )$ , and extend it to a basis $\nu _ { 1 } , \ldots , \nu _ { n }$ of $K ^ { n }$ . By Example 8.8 (a) the alternating tensors $\nu _ { i _ { 1 } } \wedge \dots \wedge \nu _ { i _ { k } }$ with $i _ { 1 } < \cdots < i _ { k }$ then form a basis of $\Lambda ^ { k } K ^ { n }$ , and so we can write

$$
{ \pmb { \omega } } = \sum _ { i _ { 1 } < \cdots < i _ { k } } a _ { i _ { 1 } , \dots , i _ { k } } \nu _ { i _ { 1 } } \wedge \cdots \wedge \nu _ { i _ { k } }
$$

for suitable coefficients $a _ { i _ { 1 } , \dots , i _ { k } } \in K$ . Now for $i = 1 , \ldots , r$ we know that $\nu _ { i } \in \mathrm { K e r } f$ , and thus

$$
0 = \nu _ { i } \wedge \omega = \sum _ { i _ { 1 } < \cdots < i _ { k } } a _ { i _ { 1 } , \dots , i _ { k } } \nu _ { i } \wedge \nu _ { i _ { 1 } } \wedge \cdots \wedge \nu _ { i _ { k } } .
$$

Note that $\nu _ { i } \wedge \nu _ { i _ { 1 } } \wedge \dots \wedge \nu _ { i _ { k } } = 0$ if $i \in \{ i _ { 1 } , \ldots , i _ { k } \}$ , and in the other cases these products are (up to sign) different basis vectors of $\Lambda ^ { k + 1 } K ^ { n }$ . So the equation $( \ast )$ tells us that we must have $a _ { i _ { 1 } , \dots , i _ { k } } = 0$ whenever $i \not \in \{ i _ { 1 } , \ldots , i _ { k } \}$ . As this holds for all $i = 1 , \ldots , r$ we conclude that the coefficient $a _ { i _ { 1 } , \dots , i _ { k } } = 0$ can only be non-zero if $\{ 1 , \ldots , r \} \subset \{ i _ { 1 } , \ldots , i _ { k } \}$ .

But at least one of these coefficients has to be non-zero since $\omega \neq 0$ by assumption. This obviously requires that $r \leq k$ , i. e. that $\operatorname { r k } f = n - r \geq n - k$ . Moreover, if we have equality then only the coefficient $^ { a _ { 1 , . . . , k } }$ can be non-zero, which means that $\omega$ is a scalar multiple of $\nu _ { 1 } \wedge \dots \wedge \nu _ { k }$ .

Conversely, if $\omega = w _ { 1 } \wedge \cdots \wedge w _ { k }$ for some (necessarily linearly independent) $w _ { 1 } , \ldots , w _ { k } \in K ^ { n }$ then $w _ { 1 } , \dotsc , w _ { k } \in \operatorname { K e r } f$ . Hence in this case $\operatorname { d i m } \mathrm { K e r } f \geq k$ , i. e. rk $f \leq n - k$ , and together with the above result rk $f \geq n - k$ we have equality. 

Corollary 8.16 $( G ( k , n )$ as a projective variety). With the Plücker embedding of Construction 8.12, the Grassmannian $G ( k , n )$ is a closed subset of $\mathbb { P } ^ { \binom { n } { k } - 1 }$ . In particular, it is a projective variety.

Proof. As $G ( n , n )$ is just a single point (and hence clearly a variety) we may assume that $k < n$ . Then by construction a point $\omega \in \mathbb { P } ^ { ( { n } ) - 1 }$ lies in $G ( k , n )$ if and only if it is the class of a pure tensor $\nu _ { 1 } \wedge \dots \wedge \nu _ { k }$ . Lemma 8.14 shows that this is the case if and only if the rank of the linear map $f \colon K ^ { n } \to \Lambda ^ { k + 1 } K ^ { n }$ , $\nu \mapsto \nu \wedge \omega$ is $n - k$ . As we also know that the rank of this map is always at least $n - k$ , this condition can be checked by the vanishing of all $\left( n - k + 1 \right) \times \left( n - k + 1 \right)$ minors of the matrix corresponding to $f$ . But these minors are polynomials in the entries of this matrix, and thus in the coordinates of $\omega$ . Hence we see that the condition for $\omega$ to be in $G ( k , n )$ is closed. 

Example 8.17. By the proof of Corollary 8.16, the Grassmannian $G ( 2 , 4 )$ is given by the vanishing of all sixteen $3 \times 3$ minors of a $4 \times 4$ matrix corresponding to a linear map $K ^ { 4 } \to \Lambda ^ { 3 } K ^ { 4 }$ , i. e. it is a subset of $\mathbb { P } ^ { ( _ { 2 } ^ { 4 } ) - 1 } = \mathbb { P } ^ { 5 }$ given by 16 cubic equations.

As you might expect, this is by no means the simplest set of equations describing $G ( 2 , 4 )$ — in fact, we will see in Exercise 8.22 (a) that a single quadratic equation suffices to cut out $G ( 2 , 4 )$ from $\mathbb { P } ^ { 5 }$ . Our proof of Corollary 8.16 is just the easiest way to show that $G ( k , n )$ is a variety; it is not suitable in practice to find a nice description of $G ( k , n )$ as a zero locus of simple equations.

However, there is another useful description of the Grassmannian in terms of affine patches, as we will see now. This will then also allow us to easily read off the dimension of $G ( k , n )$ — which would be very hard to compute from its equations as in Corollary 8.16.

Construction 8.18 (Affine cover of the Grassmannian). Let $U _ { 0 } \subset G ( k , n ) \subset \mathbb { P } ^ { \binom { n } { k } - 1 }$ be the affine open subset where the $e _ { 1 } \wedge \cdots \wedge e _ { k }$ -coordinate is non-zero. Then by Remark 8.9 a linear subspace $L \in G ( k , n )$ is in $U _ { 0 }$ if and only if it is the row span of a $k \times n$ matrix of the form $\left( A | B \right)$ for an invertible $k \times k$ matrix $A$ and an arbitrary $k \times ( n - k )$ matrix $B$ . Multiplying such a matrix by $A ^ { - 1 }$ from the left, which does not change its row span, yields that $U _ { 0 }$ is the image of the map

$$
f \colon \mathbb { A } ^ { k ( n - k ) } = \mathbf { M } \mathrm { a t } ( k \times ( n - k ) , K ) \to U _ { 0 } ,
$$

$C \mapsto$ the row span of $\left( E _ { k } | C \right)$ ,

where $C = A ^ { - 1 } B$ in the notation above. It is clear that different matrices $C$ lead to different row spans of $\left( E _ { k } | C \right)$ , so $f$ is bijective. Moreover, as the maximal minors of $\left( E _ { k } | C \right)$ are polynomial functions in the entries of $C$ , we see that $f$ is a morphism. Conversely, the $( i , j )$ -entry of $C$ can be reconstructed from $f ( C )$ up to sign as the maximal minor of $\left( E _ { k } | C \right)$ where we take all columns of $E _ { k }$ except the $i \cdot$ -th, together with the $j { \cdot }$ -th column of $C$ . Hence $f ^ { - 1 }$ is a morphism as well, showing that $f$ is in fact an isomorphism.

In other words, we have seen that $U _ { 0 } \cong \mathbb { A } ^ { k ( n - k ) }$ is an affine space (and not just an affine variety, which is already clear from Proposition 7.2). As the same arguments also holds for all other affine patches where one of the Plücker coordinates is non-zero, we conclude that $G ( k , n )$ can be covered by such affine spaces. In particular, it follows:

Corollary 8.19. $G ( k , n )$ is an irreducible variety of dimension $k ( n - k )$ .

Proof. We have just seen in Construction 8.18 that $G ( k , n )$ has an open cover by affine spaces $\mathbb { A } ^ { k ( n - k ) }$ . As any two of these patches have a non-empty intersection (it is in fact easy to write down a $k \times n$ matrix such that any two given maximal minors are non-zero), the result follows from Exercises 2.21 (b) and 2.34 (a). 

Remark 8.20. The argument of Construction 8.18 also shows an alternative description of the Grassmannian: It is the space of all full-rank $k \times n$ matrices modulo row transformations. As we know that every such matrix is equivalent modulo row transformations to a unique matrix in reduced row echelon form, we can also think of $G ( k , n )$ as the set of full-rank $k \times n$ matrices in such a form. For example, in the case $k = 1$ and $n = 2$ (when $G ( 1 , 2 ) = \mathbb { P } ^ { 1 }$ by Example 8.13 (a)) the full-rank $1 \times 2$ matrices in reduced row echelon form are

$$
\begin{array} { r l } { ( 1 } & { * ) \quad \mathrm { c o r r e s p o n d i n g ~ t o ~ A ^ { 1 } \subset \mathbb { P } ^ { 1 } ~ } } \\ { \mathrm { a n d } \quad ( 0 } & { 1 ) \quad \mathrm { c o r r e s p o n d i n g ~ t o ~ \infty \in \mathbb { P } ^ { 1 } ~ } } \end{array}
$$

as in the homogeneous coordinates of $\mathbb { P } ^ { 1 }$ .

The affine cover of Construction 8.18 can also be used to show the following symmetry property of the Grassmannians.

Proposition 8.21. For all $0 \leq k \leq n$ we have $G ( k , n ) \cong G ( n - k , n )$ .

Proof. There is an obvious well-defined set-theoretic bijection $f \colon G ( k , n ) \to G ( n - k , n )$ that sends a $k$ -dimensional linear subspace $L$ of $K ^ { n }$ to its “orthogonal” complement

$$
L ^ { \perp } = \{ x \in K ^ { n } : \langle x , y \rangle = 0 { \mathrm { ~ f o r ~ a l l ~ } } y \in L \} ,
$$

where $\textstyle \left. x , y \right. = \sum _ { i = 1 } ^ { n } x _ { i } y _ { i }$ denotes the standard bilinear form. It remains to be shown that $f$ (and analogously $f ^ { - 1 } )$ is a morphism. By Lemma 4.6, we can do this on the affine coordinates of Construction 8.18. So let $L \in G ( k , n )$ be described as the subspace spanned by the rows of a matrix $\left( E _ { k } | C \right)$ , where the entries of $C \in \operatorname { M a t } ( k \times ( n - k ) , K )$ are the affine coordinates of $L$ . As

$$
\left( E _ { k } | C \right) \cdot \binom { - C } { E _ { n - k } } = 0 ,
$$

we see that $L ^ { \perp }$ is the subspace spanned by the rows of $\left( - C ^ { \mathsf { T } } | E _ { n - k } \right)$ . But the maximal minors of this matrix, i. e. the Plücker coordinates of $L ^ { \perp }$ , are clearly polynomials in the entries of $C$ , and thus we conclude that $f$ is a morphism. 

Exercise 8.22. Let $G ( 2 , 4 ) \subset \mathbb { P } ^ { 5 }$ be the Grassmannian of lines in $\mathbb { P } ^ { 3 }$ (or of 2-dimensional linear subspaces of $K ^ { 4 }$ ). We denote the homogeneous Plücker coordinates of $G ( 2 , 4 )$ in $\mathbb { P } ^ { 5 }$ by $x _ { i , j }$ for $1 \leq i < j \leq 4$ . Show:

(a) $G ( 2 , 4 ) = V ( x _ { 1 , 2 } x _ { 3 , 4 } - x _ { 1 , 3 } x _ { 2 , 4 } + x _ { 1 , 4 } x _ { 2 , 3 } ) .$ (b) Let $L \subset \mathbb { P } ^ { 3 }$ be an arbitrary line. Show that the set of lines in $\mathbb { P } ^ { 3 }$ that intersect $L$ , considered as a subset of $G ( 2 , 4 ) \subset \mathbb { P } ^ { 5 }$ , is the zero locus of a homogeneous linear polynomial.

How many lines in $\mathbb { P } ^ { 3 }$ would you expect to intersect four general given lines?

Exercise 8.23. Show that the following sets are projective varieties:

(a) the incidence correspondence

$\{ ( L , a ) \in G ( k , n ) \times \mathbb { P } ^ { n - 1 } : L \subset \mathbb { P } ^ { n - 1 }$ a $\left( k - 1 \right)$ -dimensional linear subspace and $a \in L \}$

(b) the join of two disjoint varieties $X , Y \subset \mathbb { P } ^ { n }$ , i. e. the union in $\mathbb { P } ^ { n }$ of all lines intersecting both $X$ and $Y$ .

# 9. Birational Maps and Blowing Up

In the course of this class we have already seen many examples of varieties that are “almost the same” in the sense that they contain isomorphic dense open subsets (although the varieties are not isomorphic themselves). Let us quickly recall some of them.

Example 9.1 (Irreducible varieties with isomorphic non-empty open subsets).

(a) The affine space $\mathbb { A } ^ { n }$ and the projective space $\mathbb { P } ^ { n }$ have the common open subset $\mathbb { A } ^ { n }$ by Proposition 7.2. Consequently, $\mathbb { P } ^ { m } \times \mathbb { P } ^ { n }$ and $\mathbb { P } ^ { m + n }$ have the common open subset $\mathbb { A } ^ { m } \times \mathbb { A } ^ { n } = \mathbb { A } ^ { m + n }$ — but they are not isomorphic by Exercise 7.7 (c).   
(b) Similarly, the affine space $\mathbb { A } ^ { k ( n - k ) }$ and the Grassmannian $G ( k , n )$ have the common open subset $\mathbb { A } ^ { k ( n - k ) }$ by Construction 8.18.   
(c) The affine line $\mathbb { A } ^ { 1 }$ and the cubic curve $X = V ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 3 } ) \subset \mathbb { A } ^ { 2 }$ of Example 4.9 have the isomorphic open subsets $\mathbb { A } ^ { 1 } \backslash \{ 0 \}$ resp. $X \backslash \{ 0 \}$ — in fact, the morphism $f$ given there is an isomorphism after removing the origin from both the source and the target curve.

We now want to study this situation in more detail and present a very general construction — the so-called blow-ups — that gives rise to many examples of this type. But first of all we have to set up some notation to deal with morphisms that are defined on dense open subsets. For simplicity, we will do this only for the case of irreducible varieties, in which every non-empty open subset is automatically dense by Remark 2.16.

Definition 9.2 (Rational maps). Let $X$ and $Y$ be irreducible varieties. A rational map $f$ from $X$ to $Y$ , written $f \colon X \to Y$ , is a morphism $f \colon U \to Y$ (denoted by the same letter) from a non-empty open subset $U \subset X$ to Y . We say that two such rational maps $f _ { 1 } , f _ { 2 } \colon X \to Y$ defined on $U _ { 1 }$ resp. $U _ { 2 }$ are the same if $f _ { 1 } = f _ { 2 }$ on a non-empty open subset of $U _ { 1 } \cap U _ { 2 }$ .

# Remark 9.3.

(a) Strictly speaking, Definition 9.2 means that a rational map $f \colon X \to Y$ is an equivalence class of morphisms from non-empty open subsets of $X$ to $Y$ . Note that the given relation is in fact an equivalence relation: Reflexivity and symmetry are obvious, and if $f _ { 1 } \colon U _ { 1 } \to Y$ agrees with $f _ { 2 } \colon U _ { 2 } \to Y$ on a non-empty open subset $U _ { 1 , 2 }$ and $f _ { 2 }$ with $f _ { 3 } \colon U _ { 3 } \to Y$ on a nonempty open subset $U _ { 2 , 3 }$ then $f _ { 1 }$ and $f _ { 3 }$ agree on $U _ { 1 , 2 } \cap U _ { 2 , 3 }$ , which is again non-empty by Remark 2.16 (a) since $X$ is irreducible. For the sake of readability it is customary however not to indicate these equivalence classes in the notation and to denote the rational map $f \colon X \to Y$ and the morphism $f \colon U \to Y$ by the same letter.   
(b) If two rational maps $f _ { 1 } , f _ { 2 } \colon X \to Y$ defined on $U _ { 1 } \subset X$ resp. $U _ { 2 } \subset X$ are the same, i. e. if they agree on a non-empty open subset $U \subset U _ { 1 } \cap U _ { 2 }$ , note that they must already agree on their full common domain of definition $U _ { 1 } \cap U _ { 2 }$ since this is the closure of $U$ in $U _ { 1 } \cap U _ { 2 }$ and the locus where two morphisms agree is closed by Proposition 5.19 (b).

If we now want to consider “rational maps with an inverse”, i. e. rational maps $f \colon X \to Y$ such that there is another rational map $g \colon Y \to - \to X$ with $g \circ f = \operatorname { i d } _ { X }$ and $f \circ g = \operatorname { i d } _ { Y }$ , we run into problems: If e. g. $f$ is a constant map and $g$ is not defined at the point $f ( X )$ then there is no meaningful way to compose it with $f$ . So we need to impose a technical condition first to ensure that compositions are well-defined:

Definition 9.4 (Birational maps). Again let $X$ and $Y$ be irreducible varieties.

(a) A rational map $f \colon X \to Y$ is called dominant if its image contains a non-empty open subset $U$ of $Y$ . In this case, if $g \colon Y \ {  } \ Z$ is another rational map, defined on a non-empty open subset $V$ of $Y$ , we can construct the composition $g \circ f \colon X \to Z$ as a rational map since we have such a composition of ordinary morphisms on the non-empty open subset $f ^ { - 1 } ( U \cap V )$ .   
(b) A rational map $f \colon X \to Y$ is called birational if it is dominant, and if there is another dominant rational map $g \colon Y \to - \to X$ with $g \circ f = \operatorname { i d } _ { X }$ and $f \circ g = \operatorname { i d } _ { Y }$ .   
(c) We say that $X$ and $Y$ are birational if there is a birational map $f \colon X \to Y$ between them.

Remark 9.5. Note that two irreducible varieties are birational if and only if they contain isomorphic non-empty open subsets:

$\ " \Rightarrow \ "$ If $f \colon X \to Y$ is a birational map defined on $U \subset X$ , with inverse $g \colon Y \ {  } \ X$ defined on $V \subset Y$ , the open subsets $U \cap f ^ { - 1 } ( V ) \subset X$ and $V \cap g ^ { - 1 } ( U ) \subset Y$ are isomorphic by $f$ and $g$ .   
$" \Leftarrow 2 ^ { , 3 }$ If $f \colon U \to V$ is an isomorphism between non-empty open subsets $U \subset X$ and $V \subset Y$ , then $f$ is by definition a birational map $f \colon X \to Y$ .

In particular, Exercise 5.23 then implies that birational irreducible varieties have the same dimension.

An important case of rational maps is when the target space is just the ground field, i. e. if we consider regular functions on open subsets.

Construction 9.6 (Rational functions and function fields). Let $X$ be an irreducible variety.

A rational map $\varphi \colon X \to \mathbb { A } ^ { 1 } = K$ is called a rational function on $X$ . In other words, a rational function on $X$ is given by a regular function $\varphi \in { \mathcal { O } } _ { X } ( U )$ on some non-empty open subset $U \subset X$ , with two such regular functions defining the same rational function if and only if they agree on a non-empty open subset. The set of all rational functions on $X$ will be denoted $K ( X )$ .

Note that $K ( X )$ is a field: For $\varphi _ { 1 } \in { \mathcal { O } } _ { X } ( U _ { 1 } )$ and $\varphi _ { 2 } \in { \mathcal { O } } _ { X } ( U _ { 2 } )$ we can define $\varphi _ { 1 } + \varphi _ { 2 }$ and $\varphi _ { 1 } \varphi _ { 2 }$ on $U _ { 1 } \cap U _ { 2 } \neq \emptyset$ , the additive inverse $- \varphi _ { 1 }$ on $U _ { 1 }$ , and for $\varphi _ { 1 } \neq 0$ the multiplicative inverse $\varphi _ { 1 } ^ { - 1 }$ on $U _ { 1 } \backslash V ( \varphi _ { 1 } )$ . We call $K ( X )$ the function field of $X$ .

# Remark 9.7.

(a) If $U \subset X$ is a non-empty open subset of an irreducible variety $X$ then $K ( U ) \cong K ( X )$ : An isomorphism is given by $\begin{array} { r l } { K ( U ) \to K ( X ) } & { \qquad \ K ( X ) \to K ( U ) } \\ { \varphi \in { \mathcal O } _ { U } ( V ) \mapsto \varphi \in { \mathcal O } _ { X } ( V ) } & { \qquad \mathrm { w i t h ~ i n v e r s e } } \qquad & { \varphi \in { \mathcal O } _ { X } ( V ) \mapsto \varphi | _ { V \cap U } \in { \mathcal O } _ { U } ( V \cap U ) . } \end{array}$ In particular, birational irreducible varieties have isomorphic function fields.   
(b) By definition, the function field of an irreducible variety $X$ is exactly the stalk of the structure sheaf ${ \mathcal { O } } _ { X }$ at $X$ in the sense of Exercise 3.23. In particular, if $X$ is affine then this exercise shows that $K ( X )$ is the localization of the coordinate ring $A ( X )$ at the ideal $I ( X ) = \langle 0 \rangle$ , i. e. the quotient field of $A ( X )$ .

Exercise 9.8. Show that any irreducible quadric hypersurface in $\mathbb { P } ^ { n }$ is birational, but in general not isomorphic to the projective space $\mathbb { P } ^ { n - 1 }$ .

The main goal of this chapter is now to describe and study a general procedure to modify an irreducible variety to a birational one. In its original form, this construction depends on given polynomial functions $f _ { 1 } , \ldots , f _ { r }$ on an affine variety $X$ — but we will see in Construction 9.16 that it can also be performed with a given ideal in $A ( X )$ or subvariety of $X$ instead, and that it can be glued in order to work on arbitrary varieties.

Construction 9.9 (Blowing up). Let $X \subset \mathbb { A } ^ { n }$ be an affine variety. For some given polynomial functions $f _ { 1 } , \dots , f _ { r } \in A ( X )$ on $X$ , we set $U = X \backslash V ( f _ { 1 } , \dotsc , f _ { r } )$ . As $f _ { 1 } , \ldots , f _ { r }$ then do not vanish simultaneously at any point of $U$ , there is a well-defined morphism

$$
f \colon U \to \mathbb { P } ^ { r - 1 } , x \mapsto ( f _ { 1 } ( x ) \colon \cdots \colon f _ { r } ( x ) ) .
$$

We consider its graph

$$
\Gamma _ { f } = \{ ( x , f ( x ) ) : x \in U \} \quad \subset U \times \mathbb { P } ^ { r - 1 } .
$$

It is closed in $U \times \mathbb { P } ^ { r - 1 }$ by Proposition 5.19 (a), but in general not in $X \times \mathbb { P } ^ { r - 1 }$ . The closure of $\Gamma _ { f }$ in $X \times \mathbb { P } ^ { r - 1 }$ is called the blow-up of $X$ at $f _ { 1 } , \ldots , f _ { r }$ ; we will usually denote it by $\tilde { X }$ . Note that there is a natural projection morphism $\pi \colon \tilde { X } \to X$ to the first factor. Sometimes we will also say that this morphism $\pi$ is the blow-up of $X$ at $f _ { 1 } , \ldots , f _ { r }$ .

Before we give examples of blow-ups let us introduce some more notation and easy general results that will help us to deal with them.

Remark 9.10 (Exceptional sets). In construction 9.9, the graph $\Gamma _ { f }$ is isomorphic to $U$ , with isomorphism $\pi | _ { \Gamma _ { f } } \colon \Gamma _ { f } \to U$ . By abuse of notation, one often uses this isomorphism to identify $\Gamma _ { f }$ with $U$ , so that $U$ becomes a dense open subset of $\tilde { X }$ . Its complement $\tilde { X } \backslash U = \pi ^ { - 1 } ( V ( f _ { 1 } , \dots , f _ { r } ) )$ , on which $\pi$ is usually not an isomorphism, is called the exceptional set of the blow-up.

If $X$ is irreducible and $f _ { 1 } , \ldots , f _ { r }$ do not vanish simultaneously on all of $X$ , then $U = X \backslash V ( f _ { 1 } , \dotsc , f _ { r } )$ is a non-empty and hence dense open subset of $X$ . So its closure in the blow-up, which is all of $\tilde { X }$ by definition, is also irreducible. We therefore conclude that $X$ and $\tilde { X }$ are birational in this case, with common dense open subset $U$ .

Remark 9.11 (Strict transforms and blow-ups of subvarieties). In the notation of Construction 9.9, let $Y$ be a closed subvariety of $X$ . Then we can blow up $Y$ at $f _ { 1 } , \ldots , f _ { r }$ as well. By construction, the resulting space ${ \tilde { Y } } \subset Y \times \mathbb { P } ^ { r - 1 } \subset X \times \mathbb { P } ^ { r - 1 }$ is then also a closed subvariety of $\tilde { X }$ , in fact it is the closure of $Y \cap U$ in $\tilde { X }$ (using the isomorphism $\Gamma _ { f } \cong U$ of Remark 9.10 to identify $Y \cap U$ with a subset of $\tilde { X }$ ). If we consider $\tilde { Y }$ as a subset of $\tilde { X }$ in this way it is often called the strict transform of $Y$ in the blow-up of $X$ .

In particular, if $X = X _ { 1 } \cup \cdots \cup X _ { m }$ is the irreducible decomposition of $X$ then ${ \tilde { X } } _ { i } \subset { \tilde { X } }$ for $i = 1 , \ldots , m$ . Moreover, since taking closures commutes with finite unions it is immediate from Construction 9.9 that

$$
\tilde { X } = \tilde { X } _ { 1 } \cup \cdots \cup \tilde { X } _ { m } ,
$$

i. e. that for blowing up $X$ we just blow up its irreducible components individually. For many purposes it therefore suffices to consider blow-ups of irreducible varieties.

Example 9.12 (Trivial cases of blow-ups). Let $r = 1$ in the notation of Construction 9.9, i. e. consider the case when we blow up $X$ at only one function $f _ { 1 }$ . Then ${ \tilde { X } } \subset X \times \mathbb { P } ^ { 0 } \cong X$ , and $\Gamma _ { f } \cong U$ . So $\tilde { X }$ is just the closure of $U$ in $X$ under this isomorphism. If we assume for simplicity that $X$ is irreducible we therefore obtain the following two cases:

(a) If $f _ { 1 } \neq 0$ then $U = X \backslash V ( f _ { 1 } )$ is a non-empty open subset of $X$ , and hence ${ \tilde { X } } = X$ by Remark 2.16 (b).   
(b) If $f _ { 1 } = 0$ then $U = \emptyset$ , and hence also $\tilde { X } = \emptyset$ .

So in order to obtain interesting examples of blow-ups we will have to consider cases with $r \geq 2$ .

In order to understand blow-ups better, one of our main tasks has to be to find an explicit description of them that does not refer to taking closures. The following inclusion is a first step in this direction.

Lemma 9.13. The blow-up $\tilde { X }$ of an affine variety $X$ at $f _ { 1 } , \dots , f _ { r } \in A ( X )$ satisfies

$$
\tilde { X } \subset \{ ( x , y ) \in X \times \mathbb { P } ^ { r - 1 } : y _ { i } f _ { j } ( x ) = y _ { j } f _ { i } ( x ) f o r \mathop { a l l } i , j = 1 , \ldots , r \} .
$$

Proof. Let $U = X \backslash V ( f _ { 1 } , \dotsc , f _ { r } )$ . Then any point $( x , y ) \in U \times \mathbb { P } ^ { r - 1 }$ on the graph $\Gamma _ { f }$ of the function $f \colon U \to \mathbb { P } ^ { r - 1 }$ , $x \mapsto ( f _ { 1 } ( x ) \colon \cdot \cdot \cdot : f _ { r } ( x ) )$ satisfies $( y _ { 1 } : \cdot \cdot \cdot : y _ { r } ) = ( f _ { 1 } ( x ) : \cdot \cdot \cdot : f _ { r } ( x ) )$ , which is equivalent to $y _ { i } f _ { j } ( x ) = y _ { j } f _ { i } ( x )$ for all $i , j = 1 , \dots , r$ . As these equations then also have to hold on the closure $\tilde { X }$ of $\Gamma _ { f }$ , the lemma follows. 

Example 9.14 (Blow-up of $\mathbb { A } ^ { n }$ at the coordinate functions). Our first non-trivial (and in fact the most important) case of a blow-up is that of the affine space $\mathbb { A } ^ { n }$ at the coordinate functions $x _ { 1 } , \ldots , x _ { n }$ . This blow-up $\widetilde { \mathbb { A } ^ { n } }$ is then isomorphic to $\mathbb { A } ^ { n }$ on the open subset $U = \mathbb { A } ^ { n } \backslash V ( x _ { 1 } , \dotsc , x _ { n } ) = \mathbb { A } ^ { n } \backslash \{ 0 \}$ , and by Lemma 9.13 we have

$$
\widetilde { \mathbb { A } ^ { n } } \subset \{ ( x , y ) \in \mathbb { A } ^ { n } \times \mathbb { P } ^ { n - 1 } : y _ { i } x _ { j } = y _ { j } x _ { i } { \mathrm { ~ f o r ~ a l l ~ } } i , j = 1 , \ldots , n \} = : Y .
$$

We claim that this inclusion is in fact an equality. To see this, let us consider the open subset $U _ { 1 } = \{ ( x , y ) \in Y : y _ { 1 } \neq 0 \}$ with affine coordinates $x _ { 1 } , \ldots , x _ { n } , y _ { 2 } , \ldots , y _ { n }$ in which we set $y _ { 1 } = 1$ . Note that for given $x _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ the equations (1) for $Y$ then say exactly that $x _ { j } = x _ { 1 } y _ { j }$ for $j = 2 , \dots , n$ (since this implies $y _ { i } x _ { j } = x _ { 1 } y _ { i } y _ { j } = y _ { j } x _ { i }$ for all $i , j )$ . Hence there is an isomorphism

$$
{ \mathbb A } ^ { n } \to U _ { 1 } \subset { \mathbb A } ^ { n } \times { \mathbb P } ^ { n - 1 } , \ ( x _ { 1 } , y _ { 2 } , \ldots , y _ { n } ) \mapsto { \big ( } ( x _ { 1 } , x _ { 1 } y _ { 2 } , \ldots , x _ { 1 } y _ { n } { \big ) } , { \big ( } 1 { \colon } y _ { 2 } { \colon } \cdots { \colon } y _ { n } { \big ) } { \big ) } .
$$

Of course, the same holds for the open subsets $U _ { i }$ of $Y$ where $y _ { i } \neq 0$ for $i = 2 , \ldots , n$ . Hence $Y$ can be covered by $n$ -dimensional affine spaces. As these affine spaces intersect e. g. in the point $( ( 1 , \ldots , 1 ) , ( 1 \colon \cdots \colon 1 ) )$ , this means by Exercises 2.21 (b) and 2.34 (a) that $Y$ is irreducible of dimension $n$ as well. But as $Y$ contains the closed subvariety $\widetilde { \mathbb { A } ^ { n } }$ which is also of dimension $n$ by Remarks 9.5 and 9.10, we conclude that we must already have $Y = { \widetilde { \mathbb { A } } } ^ { n }$ .

In fact, both the description (1) of $\widetilde { \mathbb { A } ^ { n } }$ (with equality, as we have just seen) and the affine coordinates of (2) are very useful in practice for explicit computations on this blow-up.

Let us now also study the blow-up (i. e. projection) morphism $\pi \colon { \widetilde { \mathbb { A } ^ { n } } } \to \mathbb { A } ^ { n }$ of Construction 9.9. We know already that this map is an isomorphism on $U = \mathbb { A } ^ { n } \backslash \{ 0 \}$ . In contrast, the exceptional set $\pi ^ { - 1 } ( 0 )$ is given by setting $x _ { 1 } , \ldots , x _ { n }$ to 0 in the description (1) above. As all defining equations $x _ { i } y _ { j } = x _ { j } y _ { i }$ become trivial in this case, we simply get

$$
\pi ^ { - 1 } ( 0 ) = \{ ( 0 , y ) \in \mathbb { A } ^ { n } \times \mathbb { P } ^ { n - 1 } \} \cong \mathbb { P } ^ { n - 1 } .
$$

In other words, passing from $\mathbb { A } ^ { n }$ to $\widetilde { \mathbb { A } ^ { n } }$ leaves all points except 0 unchanged, whereas the origin is replaced by a projective space $\mathbb { P } ^ { n - 1 }$ . This is the geometric reason why this construction is called blowing up — in fact, we will slightly extend our terminology in Construction 9.16 (a) so that we can then call the example above the blow-up of $\mathbb { A } ^ { n }$ at the origin, instead of at the functions $x _ { 1 } , \ldots , x _ { n }$ .

Because of this behavior of the inverse images of $\pi$ one might be tempted to think of $\widetilde { \mathbb { A } ^ { n } }$ as $\mathbb { A } ^ { n }$ with a projective space $\mathbb { P } ^ { n - 1 }$ attached at the origin, as in the picture below on the left. This is not correct however, as one can see already from the fact that this space would not be irreducible, whereas $\widetilde { \mathbb { A } ^ { n } }$ is.

![](images/42b8e55f7d1f9a15e01eba4541ab8c24d8d105c61b1afcbab4f9d59c1d0c3ddd.jpg)

To get the true geometric picture for $\mathbb { A } ^ { n }$ let us consider the strict transform of a line $L \subset \mathbb { A } ^ { n }$ through the origin, i. e. the blow-up $\tilde { L }$ of $L$ at $x _ { 1 } , \ldots , x _ { n }$ contained in $\widetilde { \mathbb { A } ^ { n } }$ . We will give a general recipe to compute such strict transforms in Exercise 9.21, but in the case at hand this can also be done without much theory: By construction, over the complement of the origin every point $( x , y ) \in \tilde { L } \subset L \times \mathbb { P } ^ { n - 1 }$ must have $y$ being equal to the projective point corresponding to $L \subset K ^ { n }$ . Hence the same holds on the closure $\tilde { L }$ , and thus the strict transform $\tilde { L }$ meets the exceptional set $\pi ^ { - 1 } ( 0 ) \cong \mathbb { P } ^ { n - 1 }$ exactly in the point corresponding to $L$ . In other words, the exceptional set parametrizes the directions in $\mathbb { A } ^ { n }$ at $_ 0$ ; two lines through the origin with distinct directions will become separated after the blow-up. The picture above on the right illustrates this in the case of the plane: We can imagine the blow-up $\widetilde { \mathbb { A } ^ { 2 } }$ as a helix winding around the central line $\pi ^ { - 1 } ( 0 ) \cong \mathbb { P } ^ { 1 }$ (in fact, it winds around this exceptional set once, so that one should think of the top of the helix as being glued to the bottom).

As already mentioned, the geometric interpretation of Example 9.14 suggests that we can think of this construction as the blow-up of $\mathbb { A } ^ { n }$ at the origin instead of at the functions $x _ { 1 } , \ldots , x _ { n }$ . To justify this notation let us now show that the blow-up construction does not actually depend on the chosen functions, but only on the ideal generated by them.

Lemma 9.15. The blow-up of an affine variety $X$ at $f _ { 1 } , \dots , f _ { r } \in A ( X )$ depends only on the ideal $( f _ { 1 } , \ldots , f _ { r } ) \triangleleft A ( X )$ .

More precisely, if $f _ { 1 } ^ { \prime } , \ldots , f _ { s } ^ { \prime } \in A ( X )$ with $\langle f _ { 1 } , \dots , f _ { r } \rangle = \langle f _ { 1 } ^ { \prime } , \dots , f _ { s } ^ { \prime } \rangle \underline { { \triangleleft } } A ( X ) _ { \mathrm { ~ ~ } }$ , and $\pi \colon \tilde { X } \to X$ and $\pi ^ { \prime } \colon \tilde { X } ^ { \prime } \to X$ are the corresponding blow-ups, there is an isomorphism $F \colon \tilde { X }  \tilde { X } ^ { \prime }$ with $\pi ^ { \prime } \circ F = \pi$ . In other words, we get a commutative diagram as in the picture on the right.

![](images/5cd9ab7afb27e2d08ac85e00d93de442c0a5f685edafb6d0fa170a06f50c36db.jpg)

Proof. By assumption we have relations

$$
f _ { i } = \sum _ { j = 1 } ^ { s } g _ { i , j } f _ { j } ^ { \prime } \mathrm { ~ f o r ~ a l l } i = 1 , . . . , r \quad \mathrm { a n d } \quad f _ { j } ^ { \prime } = \sum _ { k = 1 } ^ { r } h _ { j , k } f _ { k } \mathrm { ~ f o r ~ a l l } j = 1 , . . . , s
$$

in $A ( X )$ for suitable $g _ { i , j } , h _ { j , k } \in A ( X )$ . We claim that then

$$
F : \tilde { X } \to \tilde { X } ^ { \prime } , ( x , y ) \mapsto ( x , y ^ { \prime } ) : = \left( x , \Big ( \sum _ { k = 1 } ^ { r } h _ { 1 , k } ( x ) y _ { k } : \cdots : \sum _ { k = 1 } ^ { r } h _ { s , k } ( x ) y _ { k } \Big ) \right)
$$

is an isomorphism between ${ \tilde { X } } \subset X \times \mathbb { P } ^ { r - 1 }$ and ${ \tilde { X } } ^ { \prime } \subset X \times \mathbb { P } ^ { s - 1 }$ as required. This is easy to check:

• The homogeneous coordinates of $y ^ { \prime }$ are not simultaneously 0: Note that by construction we have the relation $( y _ { 1 } : \cdot \cdot \cdot : y _ { r } ) = ( f _ { 1 } : \cdot \cdot \cdot : f _ { r } )$ on $U = X \backslash V ( f _ { 1 } , \dotsc , f _ { r } ) \subset \tilde { X } \subset X \times \mathbb { P } ^ { r - 1 }$ , i. e. these two vectors are linearly dependent (and non-zero) at each point in this set. Hence the linear relations $\begin{array} { r } { f _ { i } = \sum _ { j , k } g _ { i , j } h _ { j , k } f _ { k } } \end{array}$ in $f _ { 1 } , \ldots , f _ { r }$ imply the corresponding relations $\begin{array} { r } { y _ { i } = \sum _ { j , k } g _ { i , j } h _ { j , k } y _ { k } } \end{array}$ in $y _ { 1 } , \ldots , y _ { r }$ on this set, and thus also on its closure $\tilde { X }$ . So if we had $\begin{array} { r } { y _ { j } ^ { \prime } = \sum _ { k } h _ { j , k } y _ { k } = 0 } \end{array}$ for all $j$ then we would also have $\begin{array} { r } { y _ { i } = \sum _ { j } g _ { i , j } y _ { j } ^ { \prime } = 0 } \end{array}$ for all $i$ , which is a contradiction.

• The image of $F$ lies in ${ \tilde { X } } ^ { \prime }$ : By construction we have

$$
F ( x , y ) = \left( x , \left( \sum _ { k = 1 } ^ { r } h _ { 1 , k } ( x ) f _ { k } ( x ) \colon \cdots \colon \sum _ { k = 1 } ^ { r } h _ { s , k } ( x ) f _ { k } ( x ) \right) \right) = \left( x , ( f _ { 1 } ^ { \prime } ( x ) \colon \cdots \colon f _ { s } ^ { \prime } ( x ) ) \right) \quad \in { \tilde { X } } ^ { \prime }
$$

on the open subset $U$ , and hence also on its closure $\tilde { X }$ .

• $F$ is an isomorphism: By symmetry the same construction as above can also be done in the other direction and gives us an inverse morphism $F ^ { - 1 }$ .

• It is obvious that $\pi ^ { \prime } \circ F = \pi$ .

Construction 9.16 (Generalizations of the blow-up construction).

(a) Let $X$ be an affine variety. For an ideal $J { \triangleleft ( X ) }$ we define the blow-up of $X$ at $J$ to be the blow-up of $X$ at any set of generators of $I$ — which is well-defined up to isomorphisms by Lemma 9.15. If $Y \subset X$ is a closed subvariety the blow-up of $X$ at $I ( Y ) \triangleleft A ( X )$ will also be called the blow-up of $X$ at $Y$ . So in this language we can say that Example 9.14 describes the blow-up of $\mathbb { A } ^ { n }$ at the origin.

(b) Now let $X$ be an arbitrary variety, and let $Y \subset X$ be a closed subvariety. For an affine open cover $\{ U _ { i } : i \in I \}$ of $X$ , let $\tilde { U } _ { i }$ be the blow-up of $U _ { i }$ at the closed subvariety $U _ { i } \cap Y$ . It is then easy to check that these blow-ups $\tilde { U } _ { i }$ can be glued together to a variety $\tilde { X }$ . We will call it again the blow-up of $X$ at $Y$ .

In the following, we will probably only need this in the case of the blow-up of a point, where the construction is even easier as it is local around the blown-up point: Let $X$ be a variety, and let $a \in X$ be a point. Choose an affine open neighborhood $U \subset X$ of $a$ , and let $\tilde { U }$ be the blow-up of $U$ at $a$ . Then we obtain $\tilde { X }$ by gluing $X \backslash \{ a \}$ to $\tilde { U }$ along the common open subset $U \backslash \{ a \}$ .

(c) With our current techniques the gluing procedure of (b) only works for blow-ups at subvarieties — for the general construction of blowing up ideals we would need a way to patch ideals. This is in fact possible and leads to the notion of a sheaf of ideals, see Remark 14.10. We will not consider such blow-ups in these notes however.

Note however that blow-ups of a projective variety $X$ can be defined in essentially the same way as for affine varieties: If $f _ { 1 } , \dots , f _ { r } \in S ( X )$ are homogeneous of the same degree the blow-up of $X$ at $f _ { 1 } , \ldots , f _ { r }$ is defined as the closure of the graph

$$
\Gamma = \{ ( x , ( f _ { 1 } ( x ) \colon \dots \colon f _ { r } ( x ) ) : x \in U \} \quad \subset U \times \mathbb { P } ^ { r - 1 }
$$

(for $U = X \backslash V ( f _ { 1 } , . . . , f _ { r } ) )$ in $X \times \mathbb { P } ^ { r - 1 }$ ; by the Segre embedding as in Remark 7.12 it is again a projective variety.

Exercise 9.17. Let $\widetilde { \mathbb { A } ^ { 3 } }$ be the blow-up of $\mathbb { A } ^ { 3 }$ at the line $V ( x _ { 1 } , x _ { 2 } ) \cong \mathbb { A } ^ { 1 }$ . Show that its exceptional set is isomorphic to $\mathbb { A } ^ { 1 } \times \mathbb { P } ^ { 1 }$ . When do the strict transforms of two lines in $\mathbb { A } ^ { 3 }$ through $V ( x _ { 1 } , x _ { 2 } )$ intersect in the blow-up? What is therefore the geometric meaning of the points in the exceptional set (corresponding to Example 9.14 in which the points of the exceptional set correspond to the directions through the blown-up point)?

Exercise 9.18. Let $X \subset \mathbb { A } ^ { n }$ be an affine variety, and let $Y _ { 1 } , Y _ { 2 } \subsetneq X$ be irreducible, closed subsets, no-one contained in the other. Moreover, let $\tilde { X }$ be the blow-up of $X$ at the ideal $I ( Y _ { 1 } ) + I ( Y _ { 2 } )$ .

Show that the strict transforms of $Y _ { 1 }$ and $Y _ { 2 }$ in $\tilde { X }$ are disjoint.

One of the main applications of blow-ups is the local study of varieties. We have seen already in Example 9.14 that the exceptional set of the blow-up of $\mathbb { A } ^ { n }$ at the origin parametrizes the directions of lines at this point. It should therefore not come as a surprise that the exceptional set of the blow-up of a general variety $X$ at a point $a \in X$ parametrizes the tangent directions of $X$ at $a$ .

Construction 9.19 (Tangent cones). Let $a$ be a point on a variety $X$ . Consider the blow-up $\pi \colon \tilde { X } \to X$ of $X$ at $a$ ; its exceptional set $\pi ^ { - 1 } ( a )$ is a projective variety (e. g. by choosing an affine open neighborhood $U \subset \mathbb { A } ^ { n }$ of $a = \left( a _ { 1 } , \ldots , a _ { n } \right)$ in $X$ and blowing up $U$ at $x _ { 1 } - a _ { 1 } , \ldots , x _ { n } - a _ { n }$ ; the exceptional set is then contained in the projective space $\{ a \} \times \mathbb { P } ^ { n - 1 } \subset U \times \mathbb { P } ^ { n - 1 } )$ .

The cone over this exceptional set $\pi ^ { - 1 } ( a )$ (as in Definition 6.15 (c)) is called the tangent cone $C _ { a } X$ of $X$ at $a$ . Note that it is well-defined up to isomorphisms by Lemma 9.15. In the special case (of an affine patch) when $X \subset \mathbb { A } ^ { n }$ and $a \in X$ is the origin, we will also consider $C _ { a } X \subset C ( \mathbb { P } ^ { n - 1 } ) = \mathbb { A } ^ { n }$ as a closed subvariety of the same ambient affine space as for $X$ by blowing up at $x _ { 1 } , \ldots , x _ { n }$ .

Example 9.20. Consider the three complex affine curves $X _ { 1 } , X _ { 2 } , X _ { 3 } \subset \mathbb { A } _ { \mathbb { C } } ^ { 2 }$ with real parts as in the picture below.

![](images/88bbbf8c99cbd35a185e999c9442a9ec992076724efed2812d2d48fb1db54eb6.jpg)

Note that by Remark 9.11 the blow-ups $\tilde { X _ { i } }$ of these curves at the origin (for $i = 1 , 2 , 3$ ) are contained as strict transforms in the blow-up $\widetilde { \mathbb { A } ^ { 2 } }$ of the affine plane at the origin as in Example 9.14. They can thus be obtained geometrically as in the following picture by lifting the curves $X _ { i } \backslash \{ 0 \}$ by the map $\pi \colon \widetilde { \mathbb { A } ^ { 2 } } \to \mathbb { A } ^ { 2 }$ and taking the closure in $\widetilde { \mathbb { A } ^ { 2 } }$ . The additional points in these closures (drawn as dots in the picture below) are the exceptional sets of the blow-ups. By definition, the tangent cones $C _ { 0 } X _ { i }$ then consist of the lines corresponding to these points, as shown in gray below. They can be thought of as the cones, i. e. unions of lines, that approximate $X _ { i }$ best around the origin.

![](images/7a7bc9375566d8fde04c2cacea3fb32dfdcda014a853317167c76f2b526da184.jpg)

Let us now study how these tangent cones can be computed rigorously. For example, for a point $( ( x _ { 1 } , x _ { 2 } ) , ( y _ { 1 } : y _ { 2 } ) ) \in \tilde { X } _ { 2 } \subset \widetilde { \mathbb { A } } ^ { 2 } \subset \overline { { \mathbb { A } } } ^ { 2 } \times \mathbb { P } ^ { 1 }$ we have $x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 2 } - x _ { 1 } ^ { 3 } = 0$ (as the equation of the curve) and $y _ { 1 } x _ { 2 } - y _ { 2 } x _ { 1 } = 0$ by Lemma 9.13. The latter means that the vectors $( x _ { 1 } , x _ { 2 } )$ and $( y _ { 1 } , y _ { 2 } )$ are linearly dependent, i. e. that $y _ { 1 } = \lambda x _ { 1 }$ and $y _ { 2 } = \lambda x _ { 2 }$ away from the origin for some non-zero $\lambda \in K$ . Multiplying the equation of the curve with $\lambda ^ { 2 }$ thus yields

$$
\lambda ^ { 2 } \left( x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 2 } - x _ { 1 } ^ { 3 } \right) = 0 \quad \Rightarrow \quad y _ { 2 } ^ { 2 } - y _ { 1 } ^ { 2 } - y _ { 1 } ^ { 2 } x _ { 1 } = 0
$$

on $\tilde { X } _ { 2 } \backslash \pi ^ { - 1 } ( 0 )$ , and thus also on its closure $\tilde { X } _ { 2 }$ . On $\pi ^ { - 1 } ( 0 )$ , i. e. if $x _ { 1 } = x _ { 2 } = 0$ , this implies

$$
y _ { 2 } ^ { 2 } - y _ { 1 } ^ { 2 } = 0 \quad \Rightarrow \quad ( y _ { 2 } - y _ { 1 } ) ( y _ { 2 } + y _ { 1 } ) = 0 ,
$$

so that the exceptional set consists of the two points with $( y _ { 1 } : y _ { 2 } ) \in \mathbb { P } ^ { 1 }$ equal to $\left( 1 { : } 1 \right)$ or $( 1 \colon - 1 )$ . Consequently, the tangent cone $C _ { 0 } X _ { 2 }$ is the cone in $\mathbb { A } ^ { 2 }$ with the same equation

$$
( x _ { 2 } - x _ { 1 } ) ( x _ { 2 } + x _ { 1 } ) = 0 ,
$$

i. e. the union of the two diagonals in $\mathbb { A } ^ { 2 }$ as in the picture above.

Note that the effect of this computation was exactly to pick out the terms of minimal degree of the defining equation $x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 2 } - x _ { 1 } ^ { 3 } = 0$ — in this case of degree 2 — to obtain the equation ${ \bar { x _ { 2 } ^ { 2 } } } - x _ { 1 } ^ { 2 } = 0$ of the tangent cone at the origin. This obviously yields a homogeneous polynomial (so that its affine zero locus is a cone), and it fits well with the intuitive idea that for small values of $x _ { 1 }$ and $x _ { 2 }$ the higher powers of the coordinates are much smaller, so that we get a good approximation for the curve around the origin when we neglect them.

In fact, the following exercise (which is similar in style to proposition 6.31) shows that taking the terms of smallest degree of the defining equations is the general way to compute tangent cones explicitly after the coordinates have been shifted so that the point under consideration is the origin.

Exercise 9.21 (Computation of tangent cones). Let $J { \overset { \vartriangle 1 } { \mathop {  } } } K [ x _ { 1 } , \ldots , x _ { n } ]$ be an ideal, and assume that the corresponding affine variety $X = V ( J ) \subset \mathbb { A } ^ { n }$ contains the origin. Consider the blow-up $\tilde { X } \subset \widetilde { \mathbb { A } } ^ { n } \subset$ $\mathbb { A } ^ { n } \times \mathbb { P } ^ { n - 1 }$ at $x _ { 1 } , \ldots , x _ { n }$ , and denote the homogeneous coordinates of $\mathbb { P } ^ { n - 1 }$ by $y _ { 1 } , \ldots , y _ { n }$ .

(a) By Example 9.14 we know that $\widetilde { \mathbb { A } ^ { n } }$ can be covered by affine spaces, with one coordinate patch being

$$
\begin{array} { c } { \mathbb { A } ^ { n } \to \widetilde { \mathbb { A } ^ { n } } \subset \mathbb { A } ^ { n } \times \mathbb { P } ^ { n - 1 } , } \\ { ( x _ { 1 } , y _ { 2 } , \dotsc , y _ { n } ) \mapsto ( ( x _ { 1 } , x _ { 1 } y _ { 2 } , \dotsc , x _ { 1 } y _ { n } ) , ( 1 { : } y _ { 2 } { : } \dots { : } y _ { n } ) ) . } \end{array}
$$

Prove that on this coordinate patch the blow-up $\tilde { X }$ is given as the zero locus of the polynomials

$$
\frac { f ( x _ { 1 } , x _ { 1 } y _ { 2 } , \ldots , x _ { 1 } y _ { n } ) } { x _ { 1 } ^ { \mathrm { m i n } \mathrm { d e g } f } }
$$

for all non-zero $f \in J$ , where min $\deg f$ denotes the smallest degree of a monomial in $f$ .

(b) Prove that the exceptional hypersurface of $\tilde { X }$ is

$$
V _ { \mathfrak { p } } ( f ^ { \mathrm { i n } } : f \in J ) \quad \subset \{ 0 \} \times \mathbb { P } ^ { n - 1 } ,
$$

where $f ^ { \mathrm { i n } }$ is the initial term of $f$ , i. e. the sum of all monomials in $f$ of smallest degree. Consequently, the tangent cone of $X$ at the origin is

$$
C _ { 0 } X = V _ { \mathrm { a } } ( f ^ { \mathrm { i n } } : f \in J ) \quad \subset \mathbb { A } ^ { n } .
$$

(c) If $J = \langle f \rangle$ is a principal ideal prove that $C _ { 0 } X = V _ { \mathrm { a } } ( f ^ { \mathrm { i n } } )$ . However, for a general ideal $J$ show that $C _ { 0 } X$ is in general not the zero locus of the initial terms of a set of generators for $J$ .

In Example 9.14 above, blowing up the $n$ -dimensional variety $\mathbb { A } ^ { n }$ at $x _ { 1 } , \ldots , x _ { n }$ has replaced the origin by a variety $\mathbb { P } ^ { n - 1 }$ of codimension 1 in $\widetilde { \mathbb { A } ^ { n } }$ . We will now see that this is in fact a general phenomenon.

Proposition 9.22 (Dimension of the exceptional set). Let $\pi \colon \tilde { X } \to X$ be the blow-up of an irreducible affine variety $X$ at $f _ { 1 } , \ldots , f _ { r } \in A ( X )$ . Then every irreducible component of the exceptional set $\pi ^ { - 1 } ( V ( f _ { 1 } , \dots , f _ { r } ) )$ has codimension $1 \ : i n \tilde { X }$ . It is therefore often called the exceptional hypersurface of the blow-up.

Proof. It is enough to prove the statement on all affine open subsets $U _ { i } \subset \tilde { X } \subset X \times \mathbb { P } ^ { r - 1 }$ where the $i .$ -th projective coordinate $y _ { i }$ is non-zero, since these open subsets cover $\tilde { X }$ . But note that for $a \in U _ { i }$ the condition $f _ { i } ( a ) = 0$ implies $f _ { j } ( a ) = 0$ for all $j$ by Lemma 9.13. So the exceptional set is given by one equation $f _ { i } = 0$ on $U _ { i }$ . Moreover, if $U _ { i }$ is non-empty then this polynomial $f _ { i }$ is not identically zero on $U _ { i }$ : Otherwise $U _ { i }$ , and thus also its closure $\tilde { X }$ , would be contained in the exceptional set — which is a contradiction since this implies $U = \emptyset$ and thus $\tilde { X } = \varnothing$ . The statement of the lemma thus follows from Proposition 2.28 (c). 

Corollary 9.23 (Dimension of tangent cones). Let a be a point on a variety $X$ . Then the dimension $\mathrm { d i m } C _ { a } X$ of the tangent cone of $X$ at a is the local dimension codimX $\{ a \}$ of $X$ at a.

Proof. Note that both $\mathrm { d i m } C _ { a } X$ and codimX $\{ a \}$ are local around the point $a$ . By passing to an open neighborhood of $a$ we can therefore assume that every irreducible component of $X$ meets $a$ , and that $X \subset \mathbb { A } ^ { n }$ is affine. We may also assume that $X$ is not just the one-point set $\{ a \}$ , since otherwise the statement of the corollary is trivial.

Now let $X = X _ { 1 } \cup \cdots \cup X _ { m }$ be the irreducible decomposition of $X$ . Note that $X \neq \{ a \}$ implies that all of these components have dimension at least 1. By Proposition 9.22 every irreducible component of the exceptional set of the blow-up $\tilde { X _ { i } }$ of $X _ { i }$ at $a$ has dimension $\dim X _ { i } - 1$ , and so by Exercise 6.30 (a) every irreducible component of the tangent cone $C _ { a } X _ { i }$ has dimension $\mathrm { d i m } X _ { i }$ . As the maximum of these dimensions is just the local dimension $\operatorname { c o d i m } _ { X } \{ a \}$ (see Exercise 2.35) it therefore suffices to show that all these exceptional sets (and hence also the tangent cones) are non-empty.

Assume the contrary, i. e. that the exceptional set of $\tilde { X } _ { i }$ is empty for some $i$ . Extending this to the projective closure $\mathbb { P } ^ { n }$ of $\mathbb { A } ^ { n }$ we obtain an irreducible variety ${ \overline { { X _ { i } } } } \subset \mathbb { P } ^ { n }$ containing $a$ whose blow-up $\widetilde { \overline { { X _ { i } } } }$ in $\widetilde { \mathbb { P } ^ { n } }$ has an empty exceptional set. This means that $\pi { \Big ( } { \widetilde { X _ { i } } } { \Big ) } = { \overline { { X _ { i } } } } \backslash \{ a \}$ , where $\pi \colon { \widetilde { \mathbb { P } ^ { n } } } \to \mathbb { P } ^ { n }$ is the blow-up map. As $\widetilde { \overline { { X _ { i } } } }$ is a projective (and hence complete) variety by Construction 9.16 (c) this is a contradiction to Corollary 7.22 since $\overline { { X _ { i } } } \backslash \{ a \}$ is not closed (recall that $\overline { { X _ { i } } }$ has dimension at least 1, so that $\overline { { X _ { i } } } \backslash \{ a \} \neq \emptyset )$ . 

# Exercise 9.24.

(a) Show that the blow-up of $\mathbb { A } ^ { 2 }$ at the ideal $\langle x _ { 1 } ^ { 2 } , x _ { 1 } x _ { 2 } , x _ { 2 } ^ { 2 } \rangle$ is isomorphic to the blow-up of $\mathbb { A } ^ { 2 }$ at the ideal $\left. x _ { 1 } , x _ { 2 } \right.$ .   
(b) Let $X$ be an affine variety, and let $J { \triangleleft ( X ) }$ be an ideal. Show by example that the blow-up of $X$ at $J$ is in general not isomorphic to the blow-up of $X$ at $\sqrt { J }$ . (Hint: Tangent cones are invariant under isomorphisms.)

We will now discuss another important application of blow-ups that follows more or less directly from the definitions: They can be used to extend morphisms defined only on an open subset of a variety.

Remark 9.25 (Blowing up to extend morphisms). Let $X$ be an affine variety, and let $f _ { 1 } , \ldots , f _ { r }$ be polynomial functions on $X$ . Note that the morphism $f \colon x \mapsto ( f _ { 1 } ( x ) \colon \cdots \colon f _ { r } ( x ) )$ to $\mathbb { P } ^ { r - 1 }$ is only well-defined on the open subset $U = X \backslash V ( f _ { 1 } , \dotsc , f _ { r } )$ of $X$ . In general, we can not expect that this morphism can be extended to a morphism on all of $X$ . But we can always extend it “after blowing up the ideal $( f _ { 1 } , \ldots , f _ { r } )$ of the indeterminacy locus”: There is an extension $\tilde { f } \colon \tilde { X } \to  { \mathbb { P } } ^ { r - 1 }$ of $f$ (that agrees with $f$ on $U$ ), namely just the projection from ${ \tilde { X } } \subset X \times \mathbb { P } ^ { r - 1 }$ to the second factor $\mathbb { P } ^ { r - 1 }$ . So blowing up is a way to extend morphisms to bigger sets on which they would otherwise be ill-defined. Let us consider a concrete example of this idea in the next lemma and the following remark.

Lemma 9.26. $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ blown up in one point is isomorphic to $\mathbb { P } ^ { 2 }$ blown up in two points.

Proof. We know from Example 7.10 that $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ is isomorphic to the quadric surface

$$
X = \{ ( x _ { 0 } : x _ { 1 } : x _ { 2 } : x _ { 3 } ) : x _ { 0 } x _ { 3 } = x _ { 1 } x _ { 2 } \} \quad \subset \mathbb { P } ^ { 3 } .
$$

Let $\tilde { X }$ be blow-up of $X$ at $a = ( 0 { : } 0 { : } 0 { : } 1 ) \in X$ , which can be realized as in Construction 9.16 (c) as the blow-up $\tilde { X } \subset \mathbb { P } ^ { 3 } \times \mathbb { P } ^ { 2 }$ of $X$ at $x _ { 0 } , x _ { 1 } , x _ { 2 }$ .

On the other hand, let $b = ( 0 { : } 1 { : } 0 ) , c = ( 0 { : } 0 { : } 1 ) \in \mathbb { P } ^ { 2 }$ , and let $\widetilde { \mathbb { P } ^ { 2 } } \subset \mathbb { P } ^ { 2 } \times \mathbb { P } ^ { 3 }$ be the blow-up of $\mathbb { P } ^ { 2 }$ at $y _ { 0 } ^ { 2 } , y _ { 0 } y _ { 1 } , y _ { 0 } y _ { 2 } , y _ { 1 } y _ { 2 }$ as in Construction 9.16 (c). Note that these polynomials do not generate the ideal $I ( \{ b , c \} ) = \langle y _ { 0 } , y _ { 1 } y _ { 2 } \rangle$ , but this does not matter: The blow-up is a local construction, so let us check that we are locally just blowing up $^ b$ , and similarly $c$ . There is an open affine neighborhood around $^ b$ given by $y _ { 1 } \neq 0$ , where we can set $y _ { 1 } = 1$ , and on this neighborhood the given functions $y _ { 0 } ^ { 2 } , y _ { 0 } , y _ { 0 } y _ { 2 } , y _ { 2 }$ generate the ideal $\left. y _ { 0 } , y _ { 2 } \right.$ of $b$ . So $\widetilde { \mathbb { P } ^ { 2 } }$ is actually the blow-up of $\mathbb { P } ^ { 2 }$ at $^ b$ and $c$ . Now we claim that an isomorphism is given by

$$
f \colon { \tilde { X } } \mapsto \widetilde { \mathbb { P } ^ { 2 } } , \ \bigl ( \bigl ( x _ { 0 } \colon x _ { 1 } \colon x _ { 2 } \colon x _ { 3 } \bigr ) , \bigl ( y _ { 0 } \colon y _ { 1 } \colon y _ { 2 } \bigr ) \bigr ) \mapsto \bigl ( \bigl ( y _ { 0 } \colon y _ { 1 } \colon y _ { 2 } \bigr ) , \bigl ( x _ { 0 } \colon x _ { 1 } \colon x _ { 2 } \colon x _ { 3 } \bigr ) \bigr ) .
$$

In fact, this is easy to prove: Obviously, $f$ is an isomorphism from $\mathbb { P } ^ { 3 } \times \mathbb { P } ^ { 2 }$ to $\mathbb { P } ^ { 2 } \times \mathbb { P } ^ { 3 }$ , so we only have to show that $f$ maps $\tilde { X }$ to $\widetilde { \mathbb { P } ^ { 2 } }$ , and that $f ^ { - 1 }$ maps $\widetilde { \mathbb { P } ^ { 2 } }$ to $\tilde { X }$ . Note that it suffices to check this on a dense open subset. But this is easy: On the complement of the exceptional set in $\tilde { X }$ we have $x _ { 0 } x _ { 3 } = x _ { 1 } x _ { 2 }$ and $( y _ { 0 } : y _ { 1 } : y _ { 2 } ) = ( x _ { 0 } : x _ { 1 } : x _ { 2 } )$ , so on the (smaller) complement of $V ( x _ { 0 } )$ we get the correct equations

$$
( x _ { 0 } : x _ { 1 } : x _ { 2 } : x _ { 3 } ) = ( x _ { 0 } ^ { 2 } : x _ { 0 } x _ { 1 } : x _ { 0 } x _ { 2 } : x _ { 0 } x _ { 3 } ) = ( x _ { 0 } ^ { 2 } : x _ { 0 } x _ { 1 } : x _ { 0 } x _ { 2 } : x _ { 1 } x _ { 2 } ) = ( y _ { 0 } ^ { 2 } : y _ { 0 } y _ { 1 } : y _ { 0 } y _ { 2 } : y _ { 1 } y _ { 2 } )
$$

for the image point under $f$ to lie in $\widetilde { \mathbb { P } ^ { 2 } }$ . Conversely, on the complement of the exceptional hypersurface in $\bar { \mathbb { P } ^ { 2 } }$ we have $( x _ { 0 } : x _ { 1 } : x _ { 2 } : x _ { 3 } ) = ( y _ { 0 } ^ { 2 } : y _ { 0 } y _ { 1 } : y _ { 0 } y _ { 2 } : y _ { 1 } y _ { 2 } )$ , so we conclude that $x _ { 0 } x _ { 3 } = x _ { 1 } x _ { 2 }$ and $( y _ { 0 } : y _ { 1 } : y _ { 2 } ) = ( x _ { 0 } : x _ { 1 } : x _ { 2 } )$ where $y _ { 0 } \neq 0$ . 

Remark 9.27. The proof of Lemma 9.26 is short and elegant, but not very insightful. So let us try to understand geometrically what is going on. As in the proof above, we think of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ as the quadric surface

$$
X = \{ ( x _ { 0 } : x _ { 1 } : x _ { 2 } : x _ { 3 } ) : x _ { 0 } x _ { 3 } = x _ { 1 } x _ { 2 } \} \quad \subset \mathbb { P } ^ { 3 } .
$$

Let us project $X$ from $a = ( 0 : 0 : 0 : 1 ) \in X$ to $V _ { \mathrm { p } } ( x _ { 3 } ) \cong \mathbb { P } ^ { 2 }$ . The corresponding morphism $f$ is shown in the picture below; as in Example 7.5 (b) it is given by $f ( x _ { 0 } : x _ { 1 } : x _ { 2 } : x _ { 3 } ) = ( x _ { 0 } : x _ { 1 } : x _ { 2 } )$ and well-defined away from $a$ .

![](images/e500f5c96a8119409ff9b9c95e9713927bd1fdba48c1aecd81ba28e393c14665.jpg)

Recall that, in the corresponding case of the projection of a quadric curve in Example 7.5 (c), the morphism $f$ could be extended to the point $a$ . This is now no longer the case for our quadric surface $X$ : To construct $f ( a )$ we would have to take the limit of the points $f ( x )$ for $x$ approaching $a$ , i. e. consider lines through $a$ and $x$ for $x \to a$ . These lines will then become tangent lines to $X$ at $a$ — but $X$ , being two-dimensional, has a one-parameter family of such tangent lines. This is why $f ( a )$ is ill-defined. But we also see from this discussion that blowing up $a$ on $X$ , i. e. replacing it by the set of all tangent lines through $a$ , will exactly resolve this indeterminacy. Hence $f$ becomes a well-defined morphism from $\tilde { X }$ to $V _ { \mathsf { p } } ( x _ { 3 } ) \cong \mathbb { P } ^ { 2 }$ .

Let us now check if there is an inverse morphism. By construction, it is easy to see what it would have to look like: The points of $X \backslash \{ a \}$ mapped to a point $y \in V _ { \mathrm { p } } ( x _ { 3 } )$ are exactly those on the line $\overline { { a y } }$ through $a$ and $y$ . In general, this line intersects $X$ in two points, one of which is $a$ . So there is then exactly one point on $X$ which maps to $y$ , leading to an inverse morphism $f ^ { - 1 }$ . This reasoning is only false if the whole line $\overline { { a y } }$ lies in $X$ . Then this whole line would be mapped to $y$ , so that we cannot have an inverse $f ^ { - 1 }$ there. But of course we expect again that this problem can be taken care of by blowing up $y$ in $\mathbb { P } ^ { 2 }$ , so that it is replaced by a $\mathbb { P } ^ { 1 }$ that can then be mapped bijectively to $\overline { { a y } }$ .

There are obviously two such lines $\overline { { a b } }$ and $\overline { { a c } }$ , given by $b = ( 0 { : } 1 { : } 0 )$ and $c = ( 0 { : } 0 { : } 1 )$ . If you think of $X$ as $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ again, these lines are precisely the “horizontal” and “vertical” lines passing through $a$ where the coordinate in one of the two factors is constant. So we would expect that $f$ can be made into an isomorphism after blowing up $b$ and $c$ , which is exactly what we have shown in Lemma 9.26.

Exercise 9.28 (Cremona transformation). Let $a = ( 1 { : } 0 { : } 0 )$ , $b = ( 0 { : } 1 { : } 0 )$ , and $c = ( 0 { : } 0 { : } 1 )$ be the three coordinate points of $\mathbb { P } ^ { 2 }$ , and let $U = \mathbb { P } ^ { 2 } \backslash \{ a , b , c \}$ . Consider the morphism

$$
f \colon U \to \mathbb { P } ^ { 2 } , ( x _ { 0 } { \mathrel { : } } x _ { 1 } { \mathrel { : } } x _ { 2 } ) \mapsto \big ( x _ { 1 } x _ { 2 } { \mathrel { : } } x _ { 0 } x _ { 2 } { \mathrel { : } } x _ { 0 } x _ { 1 } \big ) .
$$

(a) Show that there is no morphism $\mathbb { P } ^ { 2 } \to \mathbb { P } ^ { 2 }$ extending $f$ .

(b) Let $\widetilde { \mathbb { P } ^ { 2 } }$ be the blow-up of $\mathbb { P } ^ { 2 }$ at $\{ a , b , c \}$ . Show that $f$ can be extended to an isomorphism $\widetilde { f } \colon \widetilde { \mathbb { P } ^ { 2 } } \to \widetilde { \mathbb { P } ^ { 2 } }$ . This isomorphism is called the Cremona transformation.

# 10. Smooth Varieties

Let $a$ be a point on a variety $X$ . In the last chapter we have introduced the tangent cone $C _ { a } X$ as a way to study $X$ locally around $a$ (see Construction 9.19). By Corollary 9.23, it is a cone whose dimension is the local dimension $\operatorname { c o d i m } _ { X } \left\{ a \right\}$ of $X$ at $a$ (or just $\mathrm { d i m } X$ if $X$ is irreducible), and we can think of it as the cone that best approximates $X$ around $a$ . In an affine open chart where $a$ is the origin, we can compute $C _ { a } X$ by choosing an ideal with zero locus $X$ and replacing each polynomial in this ideal by its initial term (Exercise 9.21 (b)).

However, in practice one often wants to approximate a given variety by a linear space rather than by a cone. We will therefore study now to what extent this is possible, and how the result compares to the tangent cones that we already know. Of course, the idea to construct this is just to take the linear terms instead of the initial terms of the defining polynomials when considering the origin in an affine variety. For simplicity, let us therefore assume for a moment that we have chosen an affine neighborhood of the point $a$ such that $a = 0$ — we will see in Corollary 10.5 that the following construction actually does not depend on this choice.

Definition 10.1 (Tangent spaces). Let $a$ be a point on a variety $X$ . By choosing an affine neighborhood of $a$ we assume that $X \subset \mathbb { A } ^ { n }$ and that $a = 0$ is the origin, so that no polynomial $f \in I ( X )$ has a constant term. Then

$$
T _ { a } X : = V ( f _ { 1 } : f \in I ( X ) ) \quad \subset \mathbb { A } ^ { n }
$$

is called the tangent space of $X$ at $a$ , where $f _ { 1 } \in K [ x _ { 1 } , \ldots , x _ { n } ]$ denotes the linear term of a polynomial $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ as in Definition 6.6 (a).

As in the case of tangent cones, we can consider $T _ { a } X$ either as an abstract variety (leaving its dimension as the only invariant since it is a linear space) or as a subspace of $\mathbb { A } ^ { n }$ .

# Remark 10.2.

(a) In contrast to the case of tangent cones in Exercise 9.21 (c), it always suffices in Definition 10.1 to take the zero locus only of the linear parts of a set $s$ of generators for $I ( X )$ : If $f , g \in S$ are polynomials such that $f _ { 1 }$ and $g _ { 1 }$ vanish at a point $x \in \mathbb { A } ^ { n }$ then

$$
\begin{array} { c } { { ( f + g ) _ { 1 } ( x ) = f _ { 1 } ( x ) + g _ { 1 } ( x ) = 0 } } \\ { { \mathrm { a n d ~ } \quad ( h f ) _ { 1 } ( x ) = h ( 0 ) f _ { 1 } ( x ) + f ( 0 ) h _ { 1 } ( x ) = h ( 0 ) \cdot 0 + 0 \cdot h _ { 1 } ( x ) = 0 } } \end{array}
$$

for an arbitrary polynomial $h \in K [ x _ { 1 } , \ldots , x _ { n } ]$ , and hence $x \in T _ { a } X$ .

(b) However, again in contrast to the case of tangent cones in Exercise 9.21 it is crucial in Definition 10.1 that we take the radical ideal of $X$ and not just any ideal with zero locus $X$ : The ideals $( x )$ and $( x ^ { 2 } )$ in $K [ x ]$ have the same zero locus $\{ 0 \}$ in $\mathbb { A } ^ { 1 }$ , but the zero locus of the linear term of $x$ is the origin again, whereas the zero locus of the linear term of $x ^ { 2 }$ is all of $\mathbb { A } ^ { 1 }$ .

(c) For polynomials vanishing at the origin, a non-vanishing linear term is clearly always initial. Hence by Exercise 9.21 (b) it follows that $C _ { a } X \subset T _ { a } X$ , i. e. that the tangent space always contains the tangent cone. In particular, this means by Corollary 9.23 that $\dim T _ { a } X \geq \operatorname { c o d i m } _ { X } \left\{ a \right\}$ .

Example 10.3. Consider again the three complex curves $X _ { 1 } , X _ { 2 } , X _ { 3 }$ of Example 9.20. By taking the initial resp. linear term of the defining polynomials we can compute the tangent cones and spaces of these curves at the origin:

$$
X _ { 1 } = V ( x _ { 2 } + x _ { 1 } ^ { 2 } ) \colon C _ { 0 } X _ { 1 } = T _ { 0 } X _ { 1 } = V ( x _ { 2 } ) ;
$$

$$
X _ { 3 } = V ( x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 3 } ) \colon C _ { 0 } X _ { 3 } = V ( x _ { 2 } ^ { 2 } ) = V ( x _ { 2 } ) , T _ { 0 } X _ { 3 } = V ( 0 ) = { \mathbb A } ^ { 2 } .
$$

The following picture shows these curves together with their tangent cones and spaces. Note that for the curve $X _ { 1 }$ the tangent cone is already a linear space, and the notions of tangent space and tangent cone agree. In contrast, the tangent cone of $X _ { 2 }$ at the origin is not linear. By Remark 10.2 (c), the tangent space $T _ { 0 } X _ { 2 }$ must be a linear space containing $C _ { 0 } X _ { 2 }$ , and hence it is necessarily all of $\mathbb { A } ^ { 2 }$ . However, the curve $X _ { 3 }$ shows that the tangent space is not always the linear space spanned by the tangent cone.

![](images/f1155090913290bc365c3b6e55db39f72c5678ef877c7196c036e25cadb9211b.jpg)

Before we study the relation between tangent spaces and cones in more detail, let us show first of all that the (dimension of the) tangent space is actually an intrinsic local invariant of a variety around a point, i. e. that it does not depend on a choice of affine open subset or coordinates around the point. We will do this by establishing an alternative description of the tangent space that does not need any such choices. The key observation needed for this is the isomorphism of the following lemma, in which for clarity we denote by ${ \overline { { f } } } \in A ( X ) = K [ x _ { 1 } , \dots , x _ { n } ] / I ( X )$ the class of a polynomial $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ modulo the ideal of an affine variety $X$ .

Lemma 10.4. Let $X \subset \mathbb { A } ^ { n }$ be an affine variety containing the origin $a = 0$ , whose ideal is then $I ( a ) = \left. { \overline { { x _ { 1 } } } } , \ldots , { \overline { { x _ { n } } } } \right. { \underline { { \triangleleft } } } A ( X )$ . Then there is a natural vector space isomorphism

$$
I ( a ) / I ( a ) ^ { 2 } \cong \mathrm { H o m } _ { K } ( T _ { a } X , K ) .
$$

In other words, the tangent space $T _ { a } X$ is naturally the vector space dual to $I ( a ) / I ( a ) ^ { 2 }$

Proof. Consider the $K$ -linear map

$$
\varphi \colon I ( a ) \to \mathrm { H o m } _ { K } ( T _ { a } X , K ) , \ { \overline { { f } } } \mapsto f _ { 1 } | _ { T _ { a } X }
$$

sending the class of a polynomial to its linear term, regarded as a map restricted to the tangent space. By definition of the tangent space, this map is well-defined. Moreover, note that $\varphi$ is surjective since any linear map on $T _ { a } X$ can be extended to a linear map on $\mathbb { A } ^ { n }$ . So by the homomorphism theorem it suffices to prove that $\operatorname { K e r } \varphi = I ( a ) ^ { 2 }$ .

“⊂” Consider the vector subspace $W = \{ g _ { 1 } : g \in I ( X ) \}$ of $K [ x _ { 1 } , \ldots , x _ { n } ]$ , and let $k$ be its dimension. Then its zero locus $T _ { a } X$ has dimension $n - k$ , and hence the space of linear forms vanishing on $T _ { a } X$ has dimension $k$ again. As it clearly contains $W$ , we conclude that $W$ must be equal to the space of linear forms vanishing on $T _ { a } X$ . So if ${ \overline { { f } } } \in \operatorname { K e r } \varphi$ , i. e. the linear term of $f$ vanishes on $T _ { a } X$ , we know that there is a polynomial $g \in I ( X )$ with $g _ { 1 } = f _ { 1 }$ . But then $f - g$ has no constant or linear term, and hence we have ${ \overline { { f } } } = { \overline { { f - g } } } \in I ( a ) ^ { 2 }$ .   
“⊃” If ${ \overline { { f } } } , { \overline { { g } } } \in I ( a )$ then $( f g ) _ { 1 } = f ( 0 ) g _ { 1 } + g ( 0 ) f _ { 1 } = 0 \cdot g _ { 1 } + 0 \cdot f _ { 1 } = 0$ , and hence $\varphi ( { \overline { { f g } } } ) = 0$ . 

In order to make Lemma 10.4 into an intrinsic description of the tangent space we need to transfer it from the affine coordinate ring $A ( X )$ (which for a general variety would require the choice of an affine coordinate chart that sends the given point $a$ to the origin) to the local ring ${ \mathcal { O } } _ { X , a }$ (which is independent of any choices). To do this, recall by Lemma 3.19 that with the notations from above we have ${ \mathcal { O } } _ { X , a } \cong S ^ { - 1 } A ( X )$ , where $S = A ( X ) \backslash I ( a )$ is the multiplicatively closed subset of polynomial functions that are non-zero at the point $a$ . In this ring

$$
S ^ { - 1 } I ( a ) = \left\{ { \frac { g } { f } } : g , f \in A ( X ) { \mathrm { ~ w i t h ~ } } g ( a ) = 0 { \mathrm { ~ a n d ~ } } f ( a ) \neq 0 \right\}
$$

is just the maximal ideal $I _ { a }$ of all local functions vanishing at $a$ . Using these constructions we obtain the following result.

Corollary 10.5. With notations as in Lemma 10.4 and $S = A ( X ) \backslash I ( a )$ we have

$$
I ( a ) / I ( a ) ^ { 2 } \cong ( S ^ { - 1 } I ( a ) ) / ( S ^ { - 1 } I ( a ) ) ^ { 2 } .
$$

In particular, if $a \in X$ is a point on any variety $X$ and $I _ { a }$ is the unique maximal ideal in ${ \mathcal { O } } _ { X , a } ,$ then $T _ { a } X$ is naturally isomorphic to the vector space dual to $I _ { a } / I _ { a } ^ { 2 }$ , and thus independent of any choices.

Proof. For an element $f \in S$ we have $f ( a ) \neq 0$ , so (the class of) $f$ is non-zero and hence invertible in $A ( X ) / I ( a ) \cong K$ . In other words, we have $\textstyle { \frac { 1 } { f } } = c$ in $A ( X ) / I ( a )$ for some $c \in K$ (in fact, for $\begin{array} { r } { c = \frac { 1 } { f ( a ) } ) } \end{array}$ ). But then we have $\begin{array} { r } { \frac { g } { f } = c g \in I ( a ) / I ( a ) ^ { 2 } } \end{array}$ for all $g \in I ( a ) / I ( a ) ^ { 2 }$ , which means that localizing at $s$ does not change $I ( a ) / I ( a ) ^ { 2 }$ since the elements of $s$ are already invertible. We thus see that

$$
I ( a ) / I ( a ) ^ { 2 } \cong S ^ { - 1 } \big ( I ( a ) / I ( a ) ^ { 2 } \big ) \cong S ^ { - 1 } I ( a ) / ( S ^ { - 1 } I ( a ) ) ^ { 2 } ,
$$

where the last isomorphism holds since localization commutes with quotients [G3, Corollary 6.22 (b)].

Exercise 10.6. Let $f \colon X \to Y$ be a morphism of varieties, and let $a \in X$ . Show that $f$ induces a linear map $T _ { a } X  T _ { f ( a ) } Y$ between tangent spaces.

We have now constructed two objects associated to the local structure of a variety $X$ at a point $a \in X$ :

• the tangent cone $C _ { a } X$ , which is a cone of dimension $\operatorname { c o d i m } _ { X } \left\{ a \right\}$ , but in general not a linear space; and   
• the tangent space $T _ { a } X$ , which is a linear space, but whose dimension might be bigger than codimX $\{ a \}$ .

Of course, we should give special attention to the case when these two notions agree, i. e. when $X$ can be approximated around $a$ by a linear space whose dimension is the local dimension of $X$ at $a$ . This defines the co-called notion of smoothness; in fact we will see in Example 10.12 that it agrees with the concept of smoothness for plane curves that we have already introduced in [G2, Definition 2.22].

Definition 10.7 (Smooth and singular varieties). Let $X$ be a variety.

(a) A point $a \in X$ is called smooth, regular, or non-singular if $T _ { a } X = C _ { a } X$ . Otherwise it is called a singular point of $X$ .   
(b) If $X$ has a singular point we say that $X$ is singular. Otherwise $X$ is called smooth, regular, or non-singular.

Example 10.8. Of the three curves of Example 10.3, exactly the first one is smooth at the origin. As in our original motivation for the definition of tangent spaces, this is just the statement that $X _ { 1 }$ can be approximated around the origin by a straight line — in contrast to $X _ { 2 }$ and $X _ { 3 }$ , which have a “multiple point” resp. a “corner” there. A more precise geometric interpretation of smoothness can be obtained by comparing our algebraic situation with the Implicit Function Theorem from analysis, see Remark 10.15.

Lemma 10.9. Let X be a variety, and let $a \in X$ be a point. The following statements are equivalent:

(a) The point a is smooth on $X$ .   
(b) $\dim T _ { a } X = \operatorname { c o d i m } _ { X } \{ a \} .$ .   
(c) $\dim T _ { a } X \leq \operatorname { c o d i m } _ { X } \{ a \} .$ .

Proof. The implication $\mathbf { \rho } ( \mathbf { a } ) \Rightarrow \mathbf { \rho } ( \mathbf { b } )$ follows immediately from Corollary 9.23, and $( { \bf b } ) \Rightarrow ( { \bf c } )$ is trivial. To prove $\mathbf { \rho } ( \mathbf { c } ) \Rightarrow \mathbf { \rho } ( \mathbf { a } )$ , note first that (c) together with Remark 10.2 (c) implies $\dim T _ { a } X = \operatorname { c o d i m } _ { X } \left\{ a \right\}$ . But again by Remark 10.2 (c), the tangent space $T _ { a } X$ contains the tangent cone $C _ { a } X$ , which is of the same dimension by Corollary 9.23. As $T _ { a } X$ is irreducible (since it is a linear space), this is only possible if $T _ { a } X = C _ { a } X$ , i. e. if $a$ is a smooth point of $X$ . 

Remark 10.10 (Smoothness in commutative algebra). Let $a$ be a point on a variety $X$ .

(a) Let $I _ { a } \triangleleft { \mathcal { O } } _ { X , a }$ be the maximal ideal as in Lemma 3.19. Combining Corollary 10.5 with Lemma 10.9 we see that $a$ is a smooth point of $X$ if and only if the vector space dimension of $I _ { a } / I _ { a } ^ { 2 }$ is equal to the local dimension codimX $\{ a \}$ of $X$ at $a$ . This is a property of the local ring ${ \mathcal { O } } _ { X , a }$ alone, and one can therefore study it with methods from commutative algebra. A ring with this property is usually called a regular local ring [G3, Definition 11.38], which is also the reason for the name “regular point” in Definition 10.7 (a).   
(b) It is a result of commutative algebra that a regular local ring as in (a) is always an integral domain [G3, Proposition 11.40]. Translating this into geometry as in Proposition 2.8, this yields the intuitively obvious statement that a variety is locally irreducible at every smooth point $a$ , i. e. that $X$ has only one irreducible component meeting $a$ . Equivalently, any point on a variety at which two irreducible components meet is necessarily a singular point.

The good thing about smoothness is that it is very easy to check using (formal) partial derivatives:

Proposition 10.11 (Affine Jacobi criterion). Let $a \in X$ be a point on an affine variety $X \subset \mathbb { A } ^ { n }$ , and let $I ( X ) = \langle f _ { 1 } , \ldots , f _ { r } \rangle$ . Then $X$ is smooth at a if and only if the rank of the $r \times n$ Jacobian matrix

$$
\left( \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) \right) _ { i , j }
$$

is at least $n - \operatorname { c o d i m } _ { X } \left\{ a \right\}$ , and in this case the rank of this matrix is in fact equal to $n - \operatorname { c o d i m } _ { X } \left\{ a \right\}$

Proof. Let $x = ( x _ { 1 } , \ldots , x _ { n } )$ be the coordinates of $\mathbb { A } ^ { n }$ , and let $y : = x - a$ be the shifted coordinates $a$ $f _ { i }$ $y$ $\textstyle \sum _ { j = 1 } ^ { n } { \frac { \partial f _ { i } } { \partial x _ { j } } } ( a ) \cdot y _ { j }$ $T _ { a } X$   
$\begin{array} { r } { J = \left( \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) \right) _ { i , j } } \end{array}$ $1 0 . 9 \ ^ {  } ( \mathrm { a } ) \Leftrightarrow ( \mathrm { c } ) ^ { \prime }$ $a$ $X$   
if dim Ker $J \leq \mathsf { c o d i m } _ { X } \{ a \}$ , which is equivalent to $\operatorname { \cdot k } J \geq n - \operatorname { c o d i m } _ { X } \{ a \}$ . The part “(a) $\Leftrightarrow ( \boldsymbol { \mathsf { b } } ) ^ { \flat }$   
Lemma 10.9 then shows that we have in fact equality in this case. 

Example 10.12. Let $X \subset \mathbb { A } ^ { 2 }$ be a plane curve with ideal $I ( X ) = \langle f \rangle$ . By Proposition 10.11, the point $a$ is then smooth on $X$ if and only if the rank of the Jacobian matrix $\begin{array} { r l } { \bigg ( \frac { \partial f } { \partial x _ { 1 } } } & { { } \frac { \partial f } { \partial x _ { 2 } } \bigg ) } \end{array}$ at $a$ is (at least) 1, i. e. if and only if at least one of these two derivatives is non-zero at $a$ . This is precisely the criterion from [G2, Proposition 2.26], showing that our new definition agrees with the old one for plane curves.

To check smoothness for a point on a projective variety, we can of course restrict to an affine open subset of the point. However, the following exercise shows that there is also a projective version of the Jacobi criterion that does not need these affine patches and works directly with the homogeneous coordinates instead.

# Exercise 10.13.

(a) Show that

$$
\sum _ { i = 0 } ^ { n } x _ { i } \cdot { \frac { \partial f } { \partial x _ { i } } } = d \cdot f
$$

for any homogeneous polynomial $f \in K [ x _ { 0 } , \ldots , x _ { n } ]$ of degree $d$ .

(b) (Projective Jacobi criterion) Let $X \subset \mathbb { P } ^ { n }$ be a projective variety with homogeneous ideal $I ( X ) = ( f _ { 1 } , \ldots , f _ { r } )$ , and let $a \in X$ . Prove that $X$ is smooth at $a$ if and only if the rank of the $r \times ( n + 1 )$ Jacobian matrix $\begin{array} { r } { \left( \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) \right) _ { i , j } } \end{array}$ is at least $n - \operatorname { c o d i m } _ { X } \left\{ a \right\}$ .

In this criterion, note that the entries $\begin{array} { r } { \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) } \end{array}$ of the Jacobian matrix are not well-defined: Multiplying the coordinates of $a$ by a scalar $\lambda \in K ^ { * }$ will multiply $\begin{array} { r } { \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) } \end{array}$ by $\lambda ^ { d _ { i } - 1 }$ , where $d _ { i }$ is the degree of $f _ { i }$ . However, these are just row transformations of the Jacobian matrix, which do not affect its rank. Hence the condition in the projective Jacobi criterion is well-defined.

Recall that the Jacobi criterion of Proposition 10.11 requires generators for the ideal $I ( X )$ of an affine variety $X$ in order to determine if $X$ is smooth. However, in case one only knows polynomials $f _ { 1 } , \ldots , f _ { r }$ with $V ( f _ { 1 } , \dots , f _ { r } ) = X$ (whose ideal might not be radical) one direction of the Jacobi criterion still holds and gives rise to the following important variants of the proposition. They also hold in the projective setting of Exercise 10.13 (b).

Corollary 10.14 (Variants of the Jacobi criterion). L ${ \mathit { z t } } f _ { 1 } , \ldots , f _ { r } \in K [ x _ { 1 } , \ldots , x _ { n } ]$ be polynomials, and let $a \in X : = V ( f _ { 1 } , \dots , f _ { r } ) \subset \mathbb { A } ^ { n }$ .

(a) $\begin{array} { r } { I f \mathrm { r k } \left( \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) \right) _ { i , j } \geq n - \mathrm { c o d i m } _ { X } \{ a \} } \end{array}$ then $X$ is smooth at a.   
(b) $\begin{array} { r }  I f \mathbf { r } \mathbf { k } \left( \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) \right) _ { i , j } = r \left( \begin{array} { l } { \mathbf { \right. } } \end{array} \end{array}$ (i. e. the Jacobian matrix has maximal row rank) then $X$ is smooth at a of local dimension $n - r$ .

# Proof.

(a) As $f _ { 1 } , \dots , f _ { r } \in I ( X )$ , we can extend these polynomials to a set of generators $f _ { 1 } , \ldots , f _ { s }$ of $I ( X )$ for some $s \geq r$ . Then

$$
\operatorname { r k } \left( \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) \right) _ { 1 \leq i \leq s } \geq \operatorname { r k } \left( \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) \right) _ { 1 \leq i \leq r } \geq n - \operatorname { c o d i m } _ { X } \{ a \} ,
$$

and so the claim follows from Proposition 10.11.

(b) As every irreducible component of $X$ has dimension at least $n - r$ by Proposition 2.28 (c) we know that codimX $\{ a \} \geq n - r$ . Hence by assumption the rank of the Jacobian matrix is $r \geq n - \mathrm { c o d i m } _ { X } \{ a \}$ , and so $X$ is smooth at $a$ by (a). Moreover, its local dimension is then ${ \mathrm { c o d i m } } _ { X } \{ a \} = n - r$ by the equality part of Proposition 10.11. 

Remark 10.15 (Relation to the Implicit Function Theorem). The version of the Jacobi criterion of Corollary 10.14 (b) is closely related to the Implicit Function Theorem from analysis. Given real polynomials $f _ { 1 } , \ldots , f _ { r } \in \mathbb { R } [ x _ { 1 } , \ldots , x _ { n } ]$ (or more generally continuously differentiable functions on an open subset of $\mathbb { R } ^ { n }$ ) and a point $a$ in their common zero locus $X = V ( f _ { 1 } , \dots , f _ { r } )$ such that the Jacobian matrix $\begin{array} { r } { \left( \frac { \partial f _ { i } } { \partial x _ { j } } ( a ) \right) _ { i , j } } \end{array}$ has rank $r$ , this theorem states roughly that $X$ is locally around $a$ the graph of a continuously differentiable function [G1, Proposition 27.9] — so that in particular it does not have any “corners”. It can be shown that the same result holds over the complex numbers as well. So in the case $K = \mathbb { C }$ the statement of Corollary 10.14 (b) that $X$ is smooth at $a$ can also be interpreted in this geometric way.

Note however that there is no algebraic analogue of the Implicit Function Theorem itself: For example, the polynomial equation $f ( x _ { 1 } , x _ { 2 } ) : = x _ { 2 } - x _ { 1 } ^ { 2 } = 0$ cannot be solved for $x _ { 1 }$ by a regular function locally around the point $( 1 , 1 )$ , although $\textstyle { \frac { \partial f } { \partial x _ { 1 } } } ( 1 , 1 ) = - 2 \neq 0$ — it can only be solved by a continuously differentiable function $x _ { 1 } = \sqrt { x _ { 2 } }$ .

Example 10.16. Consider again the curve $X _ { 3 } = V ( x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 3 } ) \subset \mathbb { A } _ { \mathbb { C } } ^ { 2 }$ of Examples 9.20 and 10.3. The Jacobian matrix of the single polynomial $f = x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 3 }$ is

$$
\left( { \frac { \partial f } { \partial x _ { 1 } } } { \frac { \partial f } { \partial x _ { 2 } } } \right) = \left( - 3 x _ { 1 } ^ { 2 } 2 x _ { 2 } \right) ,
$$

so it has rank (at least) $2 - \dim X = 1$ exactly if $( x _ { 1 } , x _ { 2 } ) \in \mathbb { A } ^ { 2 } \backslash \{ 0 \}$ . Hence the Jacobi criterion does not only reprove our observation from Example 10.3 that the origin is a singular point of $X _ { 3 }$ , but also shows simultaneously that all other points of $X _ { 3 }$ are smooth.

In the picture on the right we have also drawn the blow-up ${ \tilde { X } } _ { 3 }$ of $X _ { 3 }$ at its singular point again. We have seen already that its exceptional set consists of only one point $a \in \tilde { X } _ { 3 }$ . Let us now check that this is a smooth point of ${ \tilde { X } } _ { 3 }$ — as we would expect from the picture.

In the coordinates ${ \big ( } ( x _ { 1 } , x _ { 2 } ) , ( y _ { 1 } : y _ { 2 } ) { \big ) }$ of $\tilde { X } _ { 3 } \subset \widetilde { \mathbb { A } ^ { 2 } } \subset \mathbb { A } ^ { 2 } \times \mathbb { P } ^ { 1 }$ , the point $a$ is given as $\left( ( 0 , 0 ) , ( 1 { : } 0 ) \right)$ . So around $a$ we can use the affine open chart $U _ { 1 } = \{ ( ( x _ { 1 } , x _ { 2 } ) , ( y _ { 1 } : y _ { 2 } ) ) : y _ { 1 } \neq 0 \}$ with affine coordinates $x _ { 1 }$ and $y _ { 2 }$ as in Example 9.14. By Exercise 9.21 (a), the blow-up ${ \tilde { X } } _ { 3 }$ is given in these coordinates by

$$
{ \frac { ( x _ { 1 } y _ { 2 } ) ^ { 2 } - x _ { 1 } ^ { 3 } } { x _ { 1 } ^ { 2 } } } = 0 , \quad { \mathrm { i . e . ~ } } g ( x _ { 1 } , y _ { 2 } ) : = y _ { 2 } ^ { 2 } - x _ { 1 } = 0 .
$$

As the Jacobian matrix

$$
\left( { \frac { \partial g } { \partial x _ { 1 } } } { \frac { \partial g } { \partial y _ { 2 } } } \right) = \left( - 1  \begin{array} { l } { 2 y _ { 2 } } \right) \end{array}
$$

![](images/5c5c2b4f82057e4eb415ecfa751064890f169539a7bb45bef06a0c6ebc990f9a.jpg)

of this polynomial has rank 1 at every point, the Jacobi criterion tells us that ${ \tilde { X } } _ { 3 }$ is smooth. In fact, from the defining equation $y _ { 2 } ^ { 2 } - x _ { 1 } = 0$ we see that on the open subset $U _ { 1 }$ the curve ${ \tilde { X } } _ { 3 }$ is just the “standard parabola” tangent to the exceptional set of Af2 (which is given on $U _ { 1 }$ by the equation $x _ { 1 } = 0$ by the proof of Proposition 9.22).

It is actually a general statement that blowing up makes singular points “nicer”, and that successive blow-ups will eventually make all singular points smooth. This process is called resolution of singularities. We will not discuss this here in detail, but the following exercise shows an example of this process.

Exercise 10.17. For $k \in \mathbb N$ let $X _ { k }$ be the complex affine curve $X _ { k } : = V ( x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 2 k + 1 } ) \subset \mathbb { A } _ { \mathbb { C } } ^ { 2 }$ . Show that $X _ { k }$ is not isomorphic to $X _ { l }$ if $k \neq l$ .

(Hint: Consider the blow-up of $X _ { k }$ at the origin.)

Exercise 10.18. Let $X \subset \mathbb { P } ^ { 3 }$ be the degree-3 Veronese embedding of $\mathbb { P } ^ { 1 }$ as in Exercise 7.30. Of course, $X$ must be smooth since it is isomorphic to $\mathbb { P } ^ { 1 }$ . Verify this directly using the projective Jacobi criterion of Exercise 10.13 (b).

Corollary 10.19. The set of smooth points of a variety is open.

Proof. Let $a$ be a smooth point on a variety $X$ ; we have to find a smooth open neighborhood of this point.

By restricting to an affine open set, we may first of all assume that $X$ is affine. Next, by possibly restricting to a smaller affine subset, we may assume by Remark 10.10 (b) that $X$ is irreducible. Then by the Jacobi criterion of Proposition 10.11 we know that the smooth locus of $X$ is exactly the set of points at which the rank of the Jacobian matrix of generators of $I ( X )$ is at least codim $X$ . As this is an open condition (given by the non-vanishing of at least one minor of size codim $X$ ), the result follows. 

Remark 10.20 (Generic smoothness). Corollary 10.19 tells us by a simple application of the Jacobi criterion that the locus of smooth points on a variety is open, but it does not guarantee that it is non-empty. It is much harder to show that the smooth locus is in fact always dense — a statement referred to as “generic smoothness” [H, Theorem I.5.3]. We will prove this here only in the case of a hypersurface $X = V ( f ) \subset \mathbb { A } ^ { n }$ for a non-constant irreducible polynomial $f \in K [ x _ { 1 } , \ldots , x _ { n } ]$ . As $X$ is then irreducible, it suffices to see that the set of smooth points of $X$ is non-empty (since a non-empty open subset in an irreducible space is always dense by Remark 2.16).

Assume the contrary, i. e. that all points of $X$ are singular. Then by Proposition 10.11 the Jacobian matrix of $f$ must have rank 0 at every point, which means that $\begin{array} { r } { \frac { \partial f } { \partial x _ { i } } ( \boldsymbol { a } ) = 0 } \end{array}$ for all $a \in X$ and $i = 1 , \ldots , n$ . Henc e $\begin{array} { r } { \frac { \partial f } { \partial x _ { i } } \in I ( V ( f ) ) = \langle f \rangle } \end{array}$ by the Nullstellensatz. But since $f$ is irreducible and the polynomial $\frac { \partial f } { \partial x _ { i } }$ has smaller degree than f this is only possible if ∂ f∂ x $\begin{array} { r } { { \frac { \partial f } { \partial x _ { i } } } = 0 } \end{array}$ for all $i$ .

In the case char $K = 0$ this is already a contradiction to $f$ being non-constant. If char $K = p$ is positive, then $f$ must be a polynomial in $x _ { 1 } ^ { p } , \ldots , x _ { n } ^ { p }$ , and so

$$
f = \sum _ { i _ { 1 } , \dots , i _ { n } } a _ { i _ { 1 } , \dots , i _ { n } } x _ { 1 } ^ { p i _ { 1 } } \dots \dots \cdot x _ { n } ^ { p i _ { n } } = \left( \sum _ { i _ { 1 } , \dots , i _ { n } } b _ { i _ { 1 } , \dots , i _ { n } } x _ { 1 } ^ { i _ { 1 } } \cdot \dots \cdot x _ { n } ^ { i _ { n } } \right) ^ { p } ,
$$

for $p$ -th roots $b _ { i _ { 1 } , \dots , i _ { n } }$ of $a _ { i _ { 1 } , \dots , i _ { n } }$ . This is a contradiction since $f$ was assumed to be irreducible.

Example 10.21 (Fermat hypersurfaces). For given $n , d \in  { \mathbb { N } } _ { > 0 }$ consider the Fermat hypersurface

$$
X : = V _ { \mathfrak { p } } ( x _ { 0 } ^ { d } + \cdot \cdot \cdot + x _ { n } ^ { d } ) \quad \subset \mathbb { P } ^ { n } .
$$

We want to show that $X$ is smooth for all choices of $n , d .$ , and $K$ . For this we use the Jacobian matrix $( d x _ { 0 } ^ { d - 1 } ~ \cdots ~ d x _ { n } ^ { d - 1 } )$ of the given polynomial:

(a) If char $K \not \rangle d$ the Jacobian matrix has rank 1 at every point, so $X$ is smooth by Exercise 10.13 (b).   
(b) If $p = \operatorname { c h a r } K | d$ we can write $d = k p ^ { r }$ for some $r \in  { \mathbb { N } } _ { > 0 }$ and $p \not \backslash k$ . Since $x _ { 0 } ^ { d } + \dots + x _ { n } ^ { d } = ( x _ { 0 } ^ { k } + \dots + x _ { n } ^ { k } ) ^ { p ^ { r } } ,$

we see again that $X = V _ { \mathfrak { p } } ( x _ { 0 } ^ { k } + \cdots + x _ { n } ^ { k } )$ is smooth by (a).

Exercise 10.22. Let $X$ be a projective variety of dimension $n$ . Prove:

(a) There is an injective morphism $X \to \mathbb { P } ^ { 2 n + 1 }$ .   
(b) There is in general no such morphism that is an isomorphism onto its image.

Exercise 10.23. Let $n \geq 2$ . Prove:

(a) Every smooth hypersurface in $\mathbb P ^ { n }$ is irreducible.   
(b) A general hypersurface in $\mathbb { P } _ { \mathbb { C } } ^ { n }$ is smooth (and thus by (a) irreducible). More precisely, for a given $d \in \mathbb { N } _ { > 0 }$ the vector space $\mathbb { C } [ x _ { 0 } , \ldots , x _ { n } ] _ { d }$ has dimension $\textstyle { \binom { n + d } { n } }$ , and so the space of all homogeneous degree- $^ { \cdot d }$ polynomials in $x _ { 0 } , \ldots , x _ { n }$ modulo scalars can be identified with the projective space $\mathbb { P } _ { \mathbb { C } } ^ { \binom { n + d } { n } - 1 }$ . Show that the subset of this projective space of all (classes of) polynomials $f$ such that $f$ is irreducible and $V _ { \mathrm { p } } ( f )$ is smooth is dense and open.

Exercise 10.24 (Dual curves). Assume that char $K \neq 2$ , and let $f \in K [ x _ { 0 } , x _ { 1 } , x _ { 2 } ]$ be a homogeneous polynomial whose partial derivatives $\frac { \partial f } { \partial x _ { i } }$ for $i = 0 , 1 , 2$ do not vanish simultaneously at any point of $X = V _ { \mathfrak { p } } ( f ) \subset \mathbb { P } ^ { 2 }$ . Then the image of the morphism

$$
F \colon X \to \mathbb { P } ^ { 2 } , a \mapsto \left( { \frac { \partial f } { \partial x _ { 0 } } } ( a )                      { \mathrm { : } } { \frac { \partial f } { \partial x _ { 1 } } } ( a ) { \mathrm { : } } { \frac { \partial f } { \partial x _ { 2 } } } ( a ) \right)
$$

is called the dual curve to $X$ .

(a) Find a geometric description of $F$ . What does it mean geometrically if $F ( a ) = F ( b )$ for two distinct points $a , b \in X ?$   
(b) If $X$ is a conic, prove that its dual $F ( X )$ is also a conic.   
(c) For any five lines in $\mathbb { P } ^ { 2 }$ in general position (what does this mean?) show that there is a unique conic in $\mathbb { P } ^ { 2 }$ that is tangent to all of them.

# 11. The 27 Lines on a Smooth Cubic Surface

As an application of the theory that we have developed so far, we now want to study lines on cubic surfaces in $\mathbb { P } ^ { 3 }$ . In Example 0.1, we have already mentioned that every smooth cubic surface has exactly 27 lines on it. Our goal is now to show this, to study the configuration of these lines, and to prove that every smooth cubic surface is birational (but not isomorphic) to $\mathbb { P } ^ { 2 }$ . All these results are classical, dating back to the 19th century. They can be regarded historically as being among the first non-trivial statements in projective algebraic geometry.

The results of this chapter will not be needed later on. Most proofs will therefore not be given in every detail here, in particular since some of them also use methods from topology and analysis which we have not discussed in this class. The aim of this chapter is rather to give an idea of what can be done with the methods that we have developed so far.

For simplicity, we will restrict ourselves to the case of the ground field $K = \mathbb { C }$ . Let us start with the discussion of a special case of a cubic surface: the Fermat cubic $V ( x _ { 0 } ^ { 3 } + x _ { 1 } ^ { 3 } + x _ { 2 } ^ { 3 } + x _ { 3 } ^ { 3 } ) \subset \mathbb { P } ^ { 3 }$ as in Example 10.21.

Lemma 11.1. The Fermat cubic $X = V ( x _ { 0 } ^ { 3 } + x _ { 1 } ^ { 3 } + x _ { 2 } ^ { 3 } + x _ { 3 } ^ { 3 } ) \subset \mathbb { P } ^ { 3 }$ contains exactly 27 lines.

Proof. To find the lines in $X$ , we may assume after a permutation of the coordinates that their first Plücker coordinate in $G ( 2 , 4 )$ is non-zero, i. e. as in Construction 8.18 that we have lines $L \in G ( 2 , 4 )$ given as the row span of the matrix

$$
\left( { \begin{array} { l l l l } { 1 } & { 0 } & { a _ { 2 } } & { a _ { 3 } } \\ { 0 } & { 1 } & { b _ { 2 } } & { b _ { 3 } } \end{array} } \right) \quad { \mathrm { f o r ~ s o m e ~ } } a _ { 2 } , a _ { 3 } , b _ { 2 } , b _ { 3 } \in \mathbb { C } .
$$

Then

$$
L = \{ ( s : t : a _ { 2 } s + b _ { 2 } t : a _ { 3 } s + b _ { 3 } t ) : ( s : t ) \in \mathbb { P } ^ { 1 } \} ,
$$

and hence $L \subset X$ if and only if the polynomial $s ^ { 3 } + t ^ { 3 } + ( a _ { 2 } s + b _ { 2 } t ) ^ { 3 } + ( a _ { 3 } s + b _ { 3 } t ) ^ { 3 }$ is identically zero in $s$ and $t$ . This means that its coefficients of $s ^ { 3 } , s ^ { 2 } t , s t ^ { 2 }$ , and $t ^ { 3 }$ must be 0, i. e. that

$$
\begin{array} { c } { { a _ { 2 } ^ { 3 } + a _ { 3 } ^ { 3 } = - 1 , } } \\ { { \ a _ { 2 } ^ { 2 } b _ { 2 } = - a _ { 3 } ^ { 2 } b _ { 3 } , } } \\ { { a _ { 2 } b _ { 2 } ^ { 2 } = - a _ { 3 } b _ { 3 } ^ { 2 } , } } \\ { { b _ { 2 } ^ { 3 } + b _ { 3 } ^ { 3 } = - 1 . } } \end{array}
$$

If $a _ { 2 } , a _ { 3 } , b _ { 2 } , b _ { 3 }$ are all non-zero, then $( 2 ) ^ { 2 } / ( 3 )$ gives $a _ { 2 } ^ { 3 } = - a _ { 3 } ^ { 3 }$ , in contradiction to (1). Hence for a line in the cubic at least one of these four numbers must be zero. Again after possibly renumbering the coordinates we may assume that $a _ { 2 } = 0$ . Then $a _ { 3 } ^ { 3 } = - 1$ by (1), $b _ { 3 } = 0$ by (2), and $b _ { 2 } ^ { 3 } = - 1$ by (4). Conversely, for such values of $a _ { 2 } , a _ { 3 } , b _ { 2 } , b _ { 3 }$ the above equations all hold, so that we really obtain a line in the cubic.

We thus obtain 9 lines in $X$ by setting $a _ { 3 } = - \omega ^ { j }$ and $b _ { 2 } = - \omega ^ { k }$ for $0 \leq j , k \leq 2$ and $\begin{array} { r } { \omega = \exp ( \frac { 2 \pi i } { 3 } ) } \end{array}$ a primitive third root of unity. So by finally allowing permutations of the coordinates we find that there are exactly 27 lines on $X$ , given by the row spans of the matrices

$$
\left( \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { - \omega ^ { j } } \\ { 0 } & { 1 } & { - \omega ^ { k } } & { 0 } \end{array} \right) , \quad \left( \begin{array} { c c c c } { 1 } & { 0 } & { - \omega ^ { j } } & { 0 } \\ { 0 } & { 1 } & { 0 } & { - \omega ^ { k } } \end{array} \right) , \quad \mathrm { a n d } \quad \left( \begin{array} { c c c c } { 1 } & { - \omega ^ { j } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - \omega ^ { k } } \end{array} \right)
$$

for $0 \leq j , k \leq 2$ .

Corollary 11.2. Let $X \subset \mathbb { P } ^ { 3 }$ again be the Fermat cubic as in Lemma 11.1.

(a) Given any line $L$ in $X$ , there are exactly 10 other lines in X that intersect L.

(b) Given any two disjoint lines $L _ { 1 } , L _ { 2 }$ in $X$ , there are exactly 5 other lines in X meeting both $L _ { 1 }$ and $L _ { 2 }$ .

Proof. As we know all the lines in $X$ by the proof of Lemma 11.1, this is just simple checking. For example, to prove (a) we may assume by permuting coordinates and multiplying them with suitable third roots of unity that $L$ is the row span of the matrix

$$
\left( { \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { - 1 } & { 0 } \end{array} } \right) ,
$$

i. e. that $L = V ( x _ { 0 } + x _ { 3 } , x _ { 1 } + x _ { 2 } )$ . The other lines meeting $L$ are then exactly the following:

4 lines as the row span of 1 0 0 −ω j0 1 −ωk 0  for ( j, k) = (1, 0), (2, 0), (0, 1), (0, 2), 3 lines as the row span of $\begin{array} { r l } { \left( \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { - \omega ^ { j } } \\ { 0 } & { 1 } & { - \omega ^ { k } } & { 0 } \end{array} \right) } & { \mathrm { f o r } ( j , k ) = ( 1 , 0 ) , ( 2 , 0 ) , ( 0 , 1 ) , ( 0 , 2 ) , } \\ { \left( \begin{array} { c c c c } { 1 } & { 0 } & { - \omega ^ { j } } & { 0 } \\ { 0 } & { 1 } & { 0 } & { - \omega ^ { k } } \end{array} \right) } & { \mathrm { f o r } ( j , k ) = ( 0 , 0 ) , ( 1 , 2 ) , ( 2 , 1 ) , } \\ { \left( \begin{array} { c c c c } { 1 } & { - \omega ^ { j } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - \omega ^ { k } } \end{array} \right) } & { \mathrm { f o r } ( j , k ) = ( 0 , 0 ) , ( 1 , 2 ) , ( 2 , 1 ) . } \end{array}$   
3 lines as the row span of

The proof of part (b) is analogous.

Let us now transfer these results to an arbitrary smooth cubic surface. This is where it gets interesting, since the equations determining the lines lying in the cubic as in the proof of Lemma 11.1 will in general be too complicated to solve them directly. Instead, we will only show that the number of lines in a smooth cubic must be the same for all cubics, so that we can then conclude by Lemma 11.1 that this number must be 27. In other words, we have to consider all smooth cubic surfaces at once.

Construction 11.3 (The incidence correspondence of lines in smooth cubic surfaces). As in Exercise 10.23 (b), let $\mathbb { P } ^ { 1 9 } = \mathbb { P } ^ { ( 3 + 3 ) - 1 }$ be the projective space of all homogeneous degree-3 polynomials in $x _ { 0 } , x _ { 1 } , x _ { 2 } , x _ { 3 }$ modulo scalars, so that the space of smooth cubic surfaces is a dense open subset $U$ of $\mathbb { P } ^ { 1 9 }$ . More precisely, a smooth cubic surface can be given as the zero locus of an irreducible polynomial $\begin{array} { r } { f _ { c } : = \sum _ { \alpha } c _ { \alpha } x ^ { \alpha } = 0 } \end{array}$ in multi-index notation, i. e. $\alpha$ runs over all quadruples of non-negative indices $( \alpha _ { 0 } , \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } )$ with $\textstyle \sum _ { i } { \alpha _ { i } } = 3$ . The corresponding point in $U \subset \mathbb { P } ^ { 1 9 }$ is then the one with homogeneous coordinates $c = ( c _ { \alpha } ) _ { \alpha }$ .

We can now consider the incidence correspondence

$M : = \left\{ \left( X , L \right) : L \right.$ is a line contained in the smooth cubic $\begin{array} { r l } { X \} } & { { } \subset U \times G ( 2 , 4 ) . } \end{array}$

Note that it comes with a natural projection map $\pi \colon M \to U$ sending a pair $( X , L )$ to $X$ , and that the number of lines in a cubic surface is just its number of inverse images under $\pi$ .

To show that this number of inverse images is constant on $U$ , we will pass from the algebraic to the analytic category and prove the following statement.

Lemma 11.4. With notations as in Construction 11.3, the incidence correspondence $M$ is. . .

(a) closed in the Zariski topology of $U \times G ( 2 , 4 )$ ;   
(b) locally in the classical topology the graph of a continuously differentiable function $U  G ( 2 , 4 )$ , as shown in the picture on the right.

![](images/eb093da32acd57d19cb669f60bbc9fc7fe2adfeb97ff9b43a69efd13b83c727c.jpg)

# Proof.

(a) The proof goes along the same lines as that of Lemma 11.1, just with a varying polynomial defining the cubic. More precisely, let $( X , L ) \in M$ . By a linear change of coordinates we may assume that $L = \operatorname { L i n } ( e _ { 1 } , e _ { 2 } )$ . Locally around this point $L \in G ( 2 , 4 )$ in the Zariski topology

we can use the affine coordinates on the Grassmannian as in Construction 8.18, namely $a _ { 2 } , a _ { 3 } , b _ { 2 } , b _ { 3 } \in \mathbb { C }$ corresponding to the line in $\mathbb { P } ^ { 3 }$ given as the row span of the matrix

$$
\left( { \begin{array} { c c c c } { 1 } & { 0 } & { a _ { 2 } } & { a _ { 3 } } \\ { 0 } & { 1 } & { b _ { 2 } } & { b _ { 3 } } \end{array} } \right) ,
$$

with the point $( a _ { 2 } , a _ { 3 } , b _ { 2 } , b _ { 3 } ) = ( 0 , 0 , 0 , 0 )$ corresponding to $L$ . On the space $U$ of smooth cubic surfaces we use the coordinates $( c _ { \alpha } ) _ { \alpha }$ as in Construction 11.3. Taking these together, in the coordinates $( c , a , b ) = ( ( c _ { \alpha } ) , a _ { 2 } , a _ { 3 } , b _ { 2 } , b _ { 3 } )$ on $U \times G ( 2 , 4 )$ the incidence correspondence $M$ is then given by

$$
\begin{array} { r l } { ( c , a , b ) \in M \Leftrightarrow } & { f _ { c } ( s \left( 1 , 0 , a _ { 2 } , a _ { 3 } \right) + t \left( 0 , 1 , b _ { 2 } , b _ { 3 } \right) ) = 0 \mathrm { ~ f o r ~ a l l ~ } s , t } \\ & { \Leftrightarrow \displaystyle \sum _ { \alpha } c _ { \alpha } s ^ { \alpha _ { 0 } } t ^ { \alpha _ { 1 } } ( s a _ { 2 } + t b _ { 2 } ) ^ { \alpha _ { 2 } } ( s a _ { 3 } + t b _ { 3 } ) ^ { \alpha _ { 3 } } = 0 \mathrm { ~ f o r ~ a l l ~ } s , t } \\ & { \Leftrightarrow \colon \displaystyle \sum _ { i } s ^ { i } t ^ { 3 - i } F _ { i } ( c , a , b ) = 0 \mathrm { ~ f o r ~ a l l ~ } s , t } \\ & { \Leftrightarrow F _ { i } ( c , a , b ) = 0 \mathrm { ~ f o r ~ } 0 \leq i \leq 3 . } \end{array}
$$

As these are polynomial equations in $^ { a , b , c }$ , it follows that $M$ is closed.

(b) We will show by (the complex version of) the Implicit Function Theorem [G1, Proposition 27.9] that the four equations $F _ { i } ( c , a , b ) = 0$ for $i = 0 , \ldots , 3$ determine $( a _ { 2 } , a _ { 3 } , b _ { 2 } , b _ { 3 } )$ locally around the origin in the classical topology in terms of $c$ . To prove this we just have to check that the Jacobian matrix $\begin{array} { r } { J : = \frac { \partial ( F _ { 0 } , \bar { F _ { 1 } } , F _ { 2 } , \bar { F _ { 3 } } ) } { \partial ( a _ { 2 } , a _ { 3 } , b _ { 2 } , b _ { 3 } ) } } \end{array}$ is invertible if $a = b = 0$ .

To compute $J$ , note that

$$
\begin{array} { l } { \displaystyle \left. \frac { \partial } { \partial a _ { 2 } } \Big ( \sum _ { i } s ^ { i } t ^ { 3 - i } F _ { i } \Big ) \right. _ { a = b = 0 } = \frac { \partial } { \partial a _ { 2 } } f _ { c } \big ( s , t , s a _ { 2 } + t b _ { 2 } , s a _ { 3 } + t b _ { 3 } \big ) \Big \vert _ { a = b = 0 } } \\ { \displaystyle = s \frac { \partial f _ { c } } { \partial x _ { 2 } } ( s , t , 0 , 0 ) . } \end{array}
$$

The $\scriptstyle ( s , t )$ -coefficients of this polynomial are the first column in the matrix $J$ . Similarly, the other columns are obviously $\begin{array} { r } { s \frac { \partial f _ { c } } { \partial x _ { 3 } } ( s , t , 0 , 0 ) , t \frac { \partial f _ { c } } { \partial x _ { 2 } } ( s , t , 0 , 0 ) } \end{array}$ , and $t \frac { \partial f _ { c } } { \partial x _ { 3 } } ( s , t , 0 , 0 )$ . Hence, if the matrix $J$ was not invertible, there would be a relation

$$
( \lambda _ { 2 } s + \mu _ { 2 } t ) \frac { \partial f _ { c } } { \partial x _ { 2 } } ( s , t , 0 , 0 ) + ( \lambda _ { 3 } s + \mu _ { 3 } t ) \frac { \partial f _ { c } } { \partial x _ { 3 } } ( s , t , 0 , 0 ) = 0
$$

identically in $s , t$ , with $( \lambda _ { 2 } , \mu _ { 2 } , \lambda _ { 3 } , \mu _ { 3 } ) \in \mathbb { C } ^ { 4 } \backslash \{ 0 \}$ . As homogeneous polynomials in two variables always decompose into linear factors, this means that $\frac { \partial f _ { c } } { \partial x _ { 2 } } ( s , t , 0 , 0 )$ and $\frac { \partial f _ { c } } { \partial x _ { 3 } } ( s , t , 0 , 0 )$ must have a common linear factor, i. e. that there is a point $p = ( p _ { 0 } , p _ { 1 } , 0 , 0 ) \in L$ with $\begin{array} { r } { \frac { { \partial { f _ { c } } } } { { \partial { x _ { 2 } } } } ( p ) = \frac { { \partial { f _ { c } } } } { { \partial { x _ { 3 } } } } ( p ) = 0 } \end{array}$ .

But as the line $L$ lies in the cubic $V ( f _ { c } )$ , we also have $f _ { c } ( s , t , 0 , 0 ) = 0$ for all $s , t$ . Differentiating this with respect to $s$ and $t$ gives $\begin{array} { r } { \frac { \partial f _ { c } } { \partial x _ { 0 } } ( p ) = 0 } \end{array}$ and $\begin{array} { r } { \frac { { \partial { f _ { c } } } } { { \partial { x _ { 1 } } } } ( p ) = 0 } \end{array}$ , respectively. Hence all vanish at $p \in L \subset X$ . By the Jacobi criterion of Exercise 10.13 (b) this means that $p$ would be a singular point of $X$ , in contradiction to our assumption. Hence $J$ must be invertible, which proves (b). 

Corollary 11.5. Every smooth cubic surface contains exactly 27 lines.

Proof. In this proof we will work with the classical topology throughout. Let $X \in U$ be a fixed smooth cubic, and let $L \subset \mathbb { P } ^ { 3 }$ be an arbitrary line. We distinguish two cases:

Case 1: If $L$ lies in $X$ , Lemma 11.4 (b) shows that there is an open neighborhood $V _ { L } \times W _ { L }$ of $( X , L )$ in $U \times G ( 2 , 4 )$ in which the incidence correspondence $M$ is the graph of a continuously differentiable function. In particular, every cubic in $V _ { L }$ contains exactly one line in $W _ { L }$ .

Case 2: If $L$ does not lie in $X$ there is an open neighborhood $V _ { L } \times W _ { L }$ of $( X , L )$ such that no cubic in $V _ { L }$ contains any line (since the incidence correspondence is closed by Lemma 11.4 (a)).

Now let $L$ vary. As the Grassmannian $G ( 2 , 4 )$ is projective, and hence compact, there are finitely many $W _ { L }$ that cover $G ( 2 , 4 )$ . Let $V$ be the intersection of the corresponding $V _ { L }$ , which is then again an open neighborhood of $X$ . By construction, in this neighborhood $V$ all cubic surfaces have the same number of lines (namely the number of $W _ { L }$ coming from case 1). As this argument holds for any cubic, we conclude that the number of lines contained in a cubic surface is a locally constant function on $U$ .

To see that this number is also globally constant, it therefore suffices to show that $U$ is connected. But this follows from Exercise 10.23 (b): We know that $U$ is the complement of a proper Zariskiclosed subset in $\mathbb { P } ^ { 1 9 }$ . But as such a closed subset has complex codimension at least 1 and hence real codimension at least 2, taking this subset away from the smooth and connected space $\mathbb { P } ^ { 1 9 }$ leaves us again with a connected space. 

# Remark 11.6.

(a) In topological terms, the argument of the proof of Corollary 11.5 says that the projection map $\pi \colon M \to U$ of Construction 11.3 is a 27-sheeted covering map.   
(b) Applying the methods of Lemma 11.4 and Corollary 11.5 to suitable incidence correspondences involving two resp. three lines in cubic surfaces, one can show similarly that the statements of Corollary 11.2 hold for an arbitrary smooth cubic surface $X$ as well: There are exactly 10 lines in $X$ meeting any given one, and exactly 5 lines in $X$ meeting any two disjoint given ones.

Note that a cubic surface $X$ is clearly not isomorphic to $\mathbb { P } ^ { 2 }$ : By Remark 11.6 (b) there are two disjoint lines on $X$ , whereas in $\mathbb { P } ^ { 2 }$ any two curves intersect by Exercise 6.30 (b). However, we will now see that $X$ is birational to $\mathbb { P } ^ { 2 }$ , and that it is in fact isomorphic to a blow-up of $\mathbb { P } ^ { 2 }$ at six points.

Proposition 11.7. Any smooth cubic surface is birational to $\mathbb { P } ^ { 2 }$ .

Proof. By Remark 11.6 (b) there are two disjoint lines $L _ { 1 }$ , $L _ { 2 } \subset X$ . The following mutually inverse rational maps $X \ { \mathrm { ~ -- } } \times { \cal { L } } _ { 1 } \times { \cal { L } } _ { 2 }$ and $L _ { 1 } \times L _ { 2 } \to \cal { X }$ show that $X$ is birational to $L _ { 1 } \times L _ { 2 } \cong \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ , and hence to $\mathbb { P } ^ { 2 }$ :

$\cdot \cdot X \mathrm { ~ -- }  L _ { 1 } \times { L _ { 2 } } ^ { \cdot \cdot }$ : By Exercise 6.28, for every point $a$ not on $L _ { 1 }$ or $L _ { 2 }$ there is a unique line $L$ in $\mathbb { P } ^ { 3 }$ through $L _ { 1 } , L _ { 2 }$ , and $a$ . Take the rational map from $X$ to $L _ { 1 } \times L _ { 2 }$ sending $a$ to $( a _ { 1 } , a _ { 2 } ) : = ( L _ { 1 } \cap L , L _ { 2 } \cap L )$ , which is obviously well-defined away from $L _ { 1 } \cup L _ { 2 }$ .

![](images/a9afe42ba2fc4296073fffa4fca4f6dce3684b83844d2a0ae2352f851a299a42.jpg)

$\cdot ^ { \cdot } L _ { 1 } \times L _ { 2 }  X ^ { ; \prime }$ : Map any pair of points $( a _ { 1 } , a _ { 2 } ) \in L _ { 1 } \times L _ { 2 }$ to the third intersection point of $X$ with the line $L$ through $a _ { 1 }$ and $a _ { 2 }$ . This is well-defined whenever $L$ is not contained in $X$ . 

Proposition 11.8. Any smooth cubic surface is isomorphic to $\mathbb { P } ^ { 2 }$ blown up in $6$ (suitably chosen) points.

Proof. We will only sketch the proof. Let $X$ be a smooth cubic surface, and consider the rational map $f \colon X \mathrm { ~ -- } \thinspace L _ { 1 } \times L _ { 2 } \cong \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ as in the proof of Proposition 11.7.

First of all we claim that $f$ is actually a morphism. To see this, note that there is a different description for $f$ : If $a \in X \backslash L _ { 1 }$ , let $H$ be the unique plane in $\mathbb { P } ^ { 3 }$ that contains $L _ { 1 }$ and $a$ , and set $f _ { 2 } ( a ) = H \cap L _ { 2 }$ . If one defines $f _ { 1 } ( a )$ analogously, then $f ( a ) = ( f _ { 1 } ( a ) , f _ { 2 } ( a ) )$ . Now if the point $a$ lies on $L _ { 1 }$ , let $H$ be the tangent plane to $X$ at $a$ , and again set $f _ { 2 } ( a ) = H \cap L _ { 2 }$ . Extending $f _ { 1 }$ similarly, one can show that this extends $f = \left( f _ { 1 } , f _ { 2 } \right)$ to a well-defined morphism $X \to \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ on all of $X$ .

Now let us investigate where the inverse map $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } \to \to X$ is not well-defined. As already mentioned in the proof of Proposition 11.7, this is the case if the point $( a _ { 1 } , a _ { 2 } ) \in L _ { 1 } \times L _ { 2 }$ is chosen so that ${ \overline { { a _ { 1 } a _ { 2 } } } } \subset X$ . In this case, the whole line $\overline { { a _ { 1 } a _ { 2 } } }$ will be mapped to $\left( a _ { 1 } , a _ { 2 } \right)$ by $f$ , and it can be checked that $f$ is actually locally the blow-up of this point. By Remark 11.6 (b) there are exactly 5 such lines $\overline { { a _ { 1 } a _ { 2 } } }$ on $X$ . Hence $X$ is the blow-up of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ in 5 points, i. e. by Lemma 9.26 the blow-up of $\mathbb { P } ^ { 2 }$ in 6 suitably chosen points. 

Remark 11.9. It is interesting to see the lines on a cubic surface $X$ in the picture of Proposition 11.8 in which we think of $X$ as a blow-up of $\mathbb { P } ^ { 2 }$ in 6 points. It turns out that the 27 lines correspond to the following curves that we know already (and that are all isomorphic to $\mathbb { P } ^ { 1 }$ ):

• the 6 exceptional hypersurfaces,   
• the strict transforms of the ${ \binom { 6 } { 2 } } = 1 5$ lines through two of the blown-up points,   
• the strict transforms of the ${ \binom { 6 } { 5 } } = 6$ conics through five of the blown-up points (see Exercise 7.29 (c)).

In fact, it is easy to check by the above explicit description of the isomorphism of $X$ with the blow-up of $\mathbb { P } ^ { 2 }$ that these curves on the blow-up actually correspond to lines on the cubic surface.

It is also interesting to see again in this picture that every such “line” meets 10 of the other “lines”, as mentioned in Remark 11.6 (b):

• Every exceptional hypersurface intersects the 5 lines and the 5 conics that pass through this blown-up point.   
• Every line through two of the blown-up points meets – the 2 exceptional hypersurfaces of the blown-up points, – the ${ \binom { 4 } { 2 } } = 6$ lines through two of the four remaining points, – the 2 conics through the four remaining points and one of the blown-up points.

• Every conic through five of the blown-up points meets the 5 exceptional hypersurfaces at these points, as well as the 5 lines through one of these five points and the remaining point.

Exercise 11.10. As in Exercise 10.23 (b) let $U \subset \mathbb { P } ^ { ( ^ { 4 + 5 } ) - 1 } = \mathbb { P } ^ { 1 2 5 }$ be the set of all smooth (3-dimensional) hypersurfaces of degree 5 in $\mathbb { P } ^ { 4 }$ .

(a) Using the Jacobi criterion, show that the incidence correspondence $\{ ( X , L ) \in U \times G ( 2 , 5 ) : L$ is a line contained in $X \}$ is smooth of dimension 125, i. e. of the same dimension as $U$ .   
(b) Although (a) suggests that a smooth hypersurface of degree 5 in $\mathbb { P } ^ { 4 }$ contains only finitely many lines, show that the Fermat hypersurface $V ( x _ { 0 } ^ { 5 } + \cdot \cdot \cdot + x _ { 4 } ^ { 5 } ) \subset \mathbb { P } ^ { 4 }$ contains infinitely many lines. (Hint: Consider lines of the form $L = \{ ( a _ { 0 } s \colon a _ { 1 } s \colon a _ { 2 } t \colon a _ { 3 } t \colon a _ { 4 } t ) : ( s \colon t ) \in \mathbb { P } ^ { 1 } \}$ for suitable $a _ { 0 } , \dots , a _ { 4 } \in \mathbb { C } .$ .)

# 12. Schemes

So far in these notes we have introduced and studied varieties over an algebraically closed ground field $K$ as the main objects of algebraic geometry. Commutative algebra was a very useful tool for this as affine varieties and their morphisms correspond exactly to finitely generated reduced $K$ -algebras and their morphisms by Remark 4.16.

In order to make this correspondence between algebraic geometry and commutative algebra even stronger it is often useful to extend the category of affine varieties to include geometric objects for any ring instead of just for any finitely generated reduced $K$ -algebra. In other words, we will drop the assumptions of an algebraically closed ground field (in fact of any ground field at all) and of any kind of finite generation, and we will allow for nilpotent elements in the coordinate rings. This leads to the notion of affine schemes that we want to introduce in this chapter. Arbitrary schemes will then be objects glued from affine schemes in the same way as general varieties are glued from affine varieties. In many cases, schemes rather than varieties are considered to be the fundamental objects of study in algebraic geometry, in particular if a strong connection to commutative algebra is desired.

Schemes are ringed spaces just like varieties. So the general path of their construction is very similar to our previous work: First we will define affine schemes as sets, then as topological spaces, then as ringed spaces using a suitable structure sheaf, and finally we will consider spaces that are locally isomorphic to such affine schemes. We will therefore not repeat any arguments that are entirely analogous to the case of varieties, but rather stress the few important differences in the transition to schemes.

Let us start by defining affine schemes as sets.

Definition 12.1 (Affine schemes). Let $R$ be a ring. The set of all prime ideals of $R$ is called the spectrum of $R$ or the affine scheme associated to $R$ . We denote it by Spec R.

# Example 12.2.

(a) Clearly the main example of an affine scheme is obtained when $R = A ( X )$ is the coordinate ring of an affine variety $X$ over an algebraically closed ground field $K$ . We will then call Spec $R$ the affine scheme associated to $X$ ; in a sense that we will make precise in Proposition 12.34 it is the scheme-theoretic analogue of the affine variety $X$ . By Remark 2.9, it contains a point $I ( Y )$ for every irreducible subvariety $Y$ of $X$ .   
(b) As a special case of (a), the affine scheme $\operatorname { S p e c } K [ x ]$ associated to $\mathbb { A } _ { K } ^ { 1 }$ for an algebraically closed field $K$ consists of the points $\langle 0 \rangle$ and $\langle x - a \rangle$ for all $a \in K$ . In contrast, Spec $\mathbb { R } [ x ]$ contains additional points that are not of this form, as e. g. $P = \left. x ^ { 2 } + 1 \right.$ . We can think of $P$ geometrically as the pair of complex conjugate points $\{ \mathrm { i } , - \mathrm { i } \}$ in the extension $\mathbb { A } _ { \mathbb { C } } ^ { 1 }$ of $\mathbb { A } _ { \mathbb { R } } ^ { 1 }$ .   
(c) The affine scheme Spec $\mathbb { Z }$ consists of the points $\langle 0 \rangle$ and $\langle p \rangle$ for all prime numbers $p$ .

Remark 12.3. If $R$ is any ring and $J = \sqrt { \langle 0 \rangle }$ its nilradical, then $\operatorname { S p e c } ( R / J ) = \operatorname { S p e c } R$ since every prime ideal of $R$ has to contain $J$ . So the spectrum of a ring as a set cannot detect the presence of nilpotent elements. However, ${ \mathrm { S p e c } } ( R / J )$ and Spec $R$ will in general differ as ringed spaces (see Proposition 12.20).

In order to construct a Zariski topology on an affine scheme Spec R, we first have to define the analogue of polynomial functions on it. Motivated by the case of an affine scheme $\operatorname { S p e c } A ( X )$ associated to an affine variety $X$ , we see that the functions on Spec $R$ should be the elements of $R$ themselves. However, as there is no fixed ground field any more the values of a function at a point $P \in { \mathrm { S p e c } } R$ will lie in fields that depend on both $R$ and $P$ .

Definition 12.4 (Functions on affine schemes). Let $R$ be a ring, and let $P \in { \mathrm { S p e c } } R$ be a point in the corresponding affine scheme, i. e. a prime ideal $P \triangleleft R$ .

(a) We denote by $K ( P )$ the quotient field of the integral domain $R / P$ . It is called the residue field of Spec $R$ at $P$ .   
(b) For any $f \in R$ we define the value of $f$ at $P$ , written as $f ( P )$ , to be the image of $f$ under the composite ring homomorphism $R \to R / P \to K ( P )$ . In particular, we have $f ( P ) = 0$ if and only if $f \in P$ .

# Example 12.5.

(a) Let $R = A ( X )$ be the coordinate ring of an affine variety $X$ over an algebraically closed ground field $K$ , and let $P = I ( a ) \in { \mathrm { S p e c } } R$ be the (maximal) ideal of a point $a \in X$ . Then $R / P \cong K$ by evaluation of a polynomial function at $a$ , and hence Definition 12.4 (b) of $f ( P )$ agrees with the usual value $f ( a ) \in K$ as in Convention 1.1 (c). Similarly, if $P = I ( Y ) \in { \mathrm { S p e c } } R$ is the ideal of an irreducible subvariety $Y \subset X$ then $f ( P )$ is the restriction of $f$ to $Y$ , considered as an element in the function field $K ( Y )$ as in Construction 9.6 (see also Remark 9.7 (b)).   
(b) On Spec $\mathbb { Z }$ , the value of the function $a \in \mathbb { Z }$ at a point $\langle p \rangle \in \mathrm { S p e c } \mathbb { Z }$ for a prime number $p$ is just its class ${ \overline { { a } } } \in \mathbb { Z } _ { p }$ .

Definition 12.6 (Zero loci and ideals in affine schemes). Let $R$ be a ring.

(a) For a subset $S \subset R$ , we define the zero locus of $s$ to be the set

$$
V ( S ) : = \{ P \in { \mathrm { S p e c } } R : f ( P ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } f \in S \} \quad \subset { \mathrm { S p e c } } R .
$$

As usual, if $S = \{ f _ { 1 } , \ldots , f _ { k } \}$ is a finite set, we will write $V ( S )$ also as $V ( f _ { 1 } , \ldots , f _ { k } )$

(b) For a subset $X \subset \operatorname { S p e c } R$ , we define the ideal of $X$ to be

$$
I ( X ) : = \{ f \in R : f ( P ) = 0 { \mathrm { ~ f o r ~ a l l ~ } } P \in { \mathrm { S p e c } } R \} \quad \leq R .
$$

(Note that this is in fact an ideal since evaluation at $P$ is a ring homomorphism by definition.)

Remark 12.7. As $f ( P ) = 0$ if and only if $f \in P$ , we can reformulate Definition 12.6 as

$$
\begin{array} { r l } & { V ( S ) = \left\{ P \in \mathrm { S p e c } R : f \in P \mathrm { ~ f o r ~ a l l ~ } f \in S \right\} = \left\{ P \in \mathrm { S p e c } R : P \supset S \right\} } \\ { \mathrm { a n d ~ } } & { I ( X ) = \displaystyle \bigcap _ { P \in X } P . } \end{array}
$$

Even if our Definition 12.4 (b) of values is probably unexpected, the fact that evaluation at a point of Spec $R$ is still a ring homomorphism and takes values in a field means that most properties of the operations $V ( \cdot )$ and $I ( \cdot )$ together with their proofs carry over immediately from the case of varieties. In particular, both operations reverse inclusions, and we clearly have $V ( S ) = V { \bigl ( } \langle S \rangle { \bigr ) }$ for any $S \subset R$ . Moreover, as in Lemma 1.4 we see that $V ( S _ { 1 } ) \cup V ( S _ { 2 } ) = V ( S _ { 1 } S _ { 2 } )$ and $\begin{array} { r } { \bigcap _ { i \in J } V ( S _ { i } ) = V ( \bigcup _ { i \in J } S _ { i } ) } \end{array}$ for all $S _ { i } \subset R$ and any index set $J$ . As in addition we have $V ( 1 ) = \emptyset$ and $V ( 0 ) = { \mathrm { S p e c } } R$ , the latter means that we can obtain a topology on Spec $R$ in the usual way:

Definition 12.8 (Zariski topology). We define the Zariski topology on an affine scheme Spec $R$ to be the topology whose closed sets are exactly the sets of the form $V ( S ) = \{ P \in { \mathrm { S p e c } } R : P \supset S \}$ for some $S \subset R$ .

In the following, we will always consider an affine scheme as a topological space in this way.

# Remark 12.9.

(a) Of course, Definition 12.8 means that all topological concepts like connectedness, irreducibility, and dimension immediately apply to affine schemes.

(b) Compared to the case of affine varieties, a new feature of the Zariski topology on affine schemes is that points are not necessarily closed. In fact, for a point $P$ in an affine scheme Spec $R$ we have

$$
{ \overline { { \{ P \} } } } = V ( P ) = \{ Q \in { \mathrm { S p e c } } R : Q \supset P \} ,
$$

so that $\{ P \}$ is closed, i. e. we have $\overline { { \{ P \} } } = \{ P \}$ , if and only if $P$ is a maximal ideal.

For an affine scheme $\operatorname { S p e c } A ( X )$ associated to an affine variety $X$ , this means that the closed points of Spec A $( X )$ correspond exactly to the minimal subvarieties of $X$ , i. e. to the points of the variety $X$ in the usual sense. The other non-closed points of $\operatorname { S p e c } A ( X )$ are of the form $I ( Y )$ for a positive-dimensional irreducible affine subvariety $Y$ of $X$ . Such a point $I ( Y ) \in { \mathrm { S p e c } } A ( X )$ is usually called the generic or general point of $Y$ . One motivation for this name is that evaluation at $Y$ takes values in the function field $K ( Y )$ of $Y$ , which encodes rational functions on Y , i. e. regular functions that are not necessarily defined on all of $Y$ , but only at a “general point” of $Y$ .

These additional non-closed points are sometimes important, but in many cases one can actually ignore them. Often one adopts the convention that a point of an affine scheme Spec R is always meant to be a closed point, i. e. a maximal ideal of $R$ , and hence a “usual point of $X ^ { \dag }$ in the case of an affine scheme associated to an affine variety $X$ .

As expected, there is also an analogue of the Nullstellensatz for affine schemes.

Proposition 12.10 (Scheme-theoretic Nullstellensatz). Let R be a ring.

(a) For any closed subset $X \subset \operatorname { S p e c } R$ we have $V ( I ( X ) ) = X$ .   
(b) For any ideal $J \triangleleft R$ we have $I ( V ( J ) ) = \sqrt { J }$ .

In particular, $V ( \cdot )$ and $I ( \cdot )$ induce an inclusion-reversing bijection

$$
\{ c l o s e d s u b s e t s ~ o f { \mathrm { S p e c } } R \} \quad \stackrel { \cdot \cdot \cdot } { \longleftrightarrow } \quad \{ r a d i c a l ~ i d e a l s ~ i n ~ R \} .
$$

Proof. In the same way as for affine varieties, only the “ $\subset$ ” part of (b) is non-trivial. But this is also easy to see: By Remark 12.7 it follows that

$$
I ( V ( J ) ) = \bigcap _ { P \in V ( J ) } P = \bigcap _ { P \in \mathrm { { S p e c } } R } P = { \sqrt { J } } ,
$$

where the last equation is a standard commutative algebra result [G3, Lemma 2.21].

Remark 12.11 (Properties of $V ( \cdot )$ and $I ( \cdot ) )$ . The usual properties of $V ( \cdot )$ and $I ( \cdot )$ as in Lemmas 1.7 and 1.12 follow immediately from their definitions together with the Nullstellensatz, and hence hold for affine schemes as well:

(a) For any two ideals $J _ { 1 } , J _ { 2 }$ in a ring $R$ we have

$$
V ( J _ { 1 } ) \cup V ( J _ { 2 } ) = V ( J _ { 1 } J _ { 2 } ) = V ( J _ { 1 } \cap J _ { 2 } ) \quad { \mathrm { a n d } } \quad V ( J _ { 1 } ) \cap V ( J _ { 2 } ) = V ( J _ { 1 } + J _ { 2 } )
$$

in Spec $R$ .

(b) For any two closed subsets $X _ { 1 } , X _ { 2 }$ of Spec $R$ we have

$$
I ( X _ { 1 } \cup X _ { 2 } ) = I ( X _ { 1 } ) \cap I ( X _ { 2 } ) \quad { \mathrm { a n d } } \quad I ( X _ { 1 } \cap X _ { 2 } ) = { \sqrt { I ( X _ { 1 } ) + I ( X _ { 2 } ) } } .
$$

As in the case of affine varieties in Definition 3.6, there is a notion of distinguished open subsets of an affine scheme that plays an important when studying topological properties.

Definition 12.12 (Distinguished open subsets). For a ring $R$ and an element $f \in R$ , we call

$$
D ( f ) : = { \mathrm { S p e c } } R \backslash V ( f ) = \{ P \in { \mathrm { S p e c } } R : f \notin P \}
$$

the distinguished open subset of $f$ in Spec $R$ .

Remark 12.13. As for affine varieties, the distinguished open subsets form a basis of the topology of an affine scheme Spec $R$ in the sense that every open subset $U \subset \operatorname { S p e c } R$ is a (not necessarily finite) union of distinguished opens: As $U$ has to be of the form $U = { \mathrm { S p e c } } R \backslash V ( S )$ for some $S \subset R$ , we conclude that

$$
U = { \mathrm { S p e c } } R \backslash \bigcap _ { f \in S } V ( f ) = \bigcup _ { f \in S } \left( { \mathrm { S p e c } } R \backslash V ( f ) \right) = \bigcup _ { f \in S } D ( f ) .
$$

Exercise 12.14. Find an example of the following, or prove that it does not exist:

(a) an irreducible affine scheme Spec $R$ such that $R$ is not an integral domain;   
(b) two affine schemes Spec $R$ and Spec $s$ with $R \leq S$ and dimSpec $R >$ dimSpec S;   
(c) a point of $\mathrm { S p e c } \mathbb { R } \big [ x _ { 1 } , x _ { 2 } \big ] / \langle x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + 1 \rangle$ with residue field $\mathbb { R }$ ;   
(d) an affine scheme of dimension 1 with exactly two points.

# Exercise 12.15.

(a) Let $R = A ( X )$ be the coordinate ring of an affine variety $X$ over an algebraically closed field. Show that the set of all closed points is dense in Spec $R$ (which means by definition that every non-empty open subset of Spec $R$ contains a closed point).   
(b) In contrast to (a) however, show by example that on a general affine scheme the set of all closed points need not be dense.

After having studied the topology of affine schemes, we now have to give them the structure of a ringed space by defining regular functions on them. To do this, note that we cannot just copy Definition 3.1 for affine varieties since we no longer have a ground field to which functions can map. Instead, recall by Lemma 3.19 that local regular functions on an affine variety $X$ around a point $a \in X$ are described by the local rings ${ \mathcal { O } } _ { X , a } = A ( X ) _ { I ( a ) }$ . Correspondingly, the idea to define a regular function on an open subset $U$ of an affine scheme Spec $R$ is that we should give a “local function” in the localization $R _ { P }$ for each $P \in U$ — and again as in the case of varieties require that they are locally of the form $\textstyle { \frac { g } { f } }$ for suitable $f , g \in R$ . This leads to the following definition.

Definition 12.16 (Regular functions). Let $R$ be a ring, and let $U$ be an open subset of the affine scheme SpecR. A regular function on $U$ is a family $\varphi = ( \varphi _ { P } ) _ { P \in U }$ with $\varphi _ { P } \in R _ { P }$ for all $P \in U$ , such that the following property holds: For every $P \in U$ there are $f , g \in R$ with $f \not \in Q$ and

$$
\varphi _ { Q } = { \frac { g } { f } } \in R _ { Q }
$$

for all $Q$ in an open subset $U _ { P }$ with $P \in U _ { P } \subset U$ .

The set of all such regular functions on $U$ is clearly a ring; we will denote it by $\mathcal { O } _ { \mathrm { S p e c } R } ( U )$ . Moreover, as the condition imposed on $\varphi$ is local it is obvious that $\mathcal { O } _ { \mathrm { S p e c } R }$ is a sheaf. It is called the structure sheaf of Spec R.

# Remark 12.17.

(a) As in the case of varieties, we will write the condition $\begin{array} { r } { \mathbf { \dot { \varphi } } _ { Q } = \frac { g } { f } \in R _ { Q } } \end{array}$ for all $Q \in U _ { P } { } ^ { \prime }$ simply as “ $\textstyle { \varphi = { \frac { g } { f } } }$ on $U _ { P } { } ^ { \prime }$ .   
(b) For a prime ideal $P$ in a ring $R$ , the quotient $R _ { P } / P _ { P }$ of the local ring $R _ { P }$ by its maximal ideal $P _ { P }$ is just the residue field $K ( P )$ of Definition 12.4 (a). Hence, analogously to Definition 12.4 (b), any regular function $\varphi \in { \mathcal { O } } _ { \operatorname { S p e c } R } ( U )$ has a well-defined value $\varphi ( P ) \in K ( P )$ for all $P \in U$ , namely the class of $\varphi _ { P } \in R _ { P }$ in $K ( P )$ . However, in contrast to the case of affine varieties we will see in 12.21 (a) that a regular function on an affine scheme is not determined by its values.

The motivation for Definition 12.16 was that the local rings $R _ { P }$ for a point $P \in { \mathrm { S p e c } } R$ should describe local functions on SpecR around $P$ . Hence, let us quickly check that in accordance with this idea the germs $\mathcal { O } _ { \operatorname { S p e c } R , P }$ of the structure sheaf at $P$ are in fact isomorphic to these local rings.

Lemma 12.18 (Germs of regular functions). Let R be a ring. Then for any point $P \in \mathfrak { i }$ Spec R the stalk $\mathcal { O } _ { \operatorname { S p e c } R , P }$ of the structure sheaf $\mathcal { O } _ { \mathrm { S p e c } R }$ at $P$ is isomorphic to the localization $R _ { P }$ .

Proof. There is a well-defined ring homomorphism

$$
\mathcal { O } _ { \mathrm { S p e c } R , P }  R _ { P } , \overline { { ( U , \varphi ) } } \mapsto \varphi _ { P }
$$

that maps the class of a family $\varphi = ( \varphi _ { Q } ) _ { Q \in U } \in \mathcal { O } _ { \mathrm { S p e c } R } ( U )$ in the stalk $\mathcal { O } _ { \operatorname { S p e c } R , P }$ to its element at $Q = P$ . We will show that it is a bijection.

It is clearly surjective since any element of $R _ { P }$ is of the form $\textstyle { \frac { g } { f } }$ with $f , g \in R$ and $f \notin P$ , and hence is the image of $\overline { { ( D ( f ) , \frac { g } { f } ) } }$ .

To show injectivity, let $\varphi \in { \mathcal { O } } _ { \operatorname { S p e c } R } ( U )$ for some $U \ni P$ be such that $\varphi _ { P } = 0$ . By shrinking $U$ if necessary we may assume by Definition 12.16 that $\textstyle \varphi = { \frac { g } { f } }$ on $U$ for some $f , g \in R$ . In particular, we have $\textstyle { \frac { g } { f } } = 0 \in R _ { P }$ , which means that $h g = 0$ for some $h \not \in P$ . But then we also have $\textstyle { \frac { g } { f } } = 0 \in R _ { Q }$ for all $Q \in U \cap D ( h )$ . Hence $\varphi = 0$ on the open neighborhood $U \cap D ( h )$ of $P$ , which means that its germ is zero in $\mathcal { O } _ { \operatorname { S p e c } R , P }$ . 

Exercise 12.19 (Stalks at generic points). Let $Y$ be an irreducible subvariety of an affine variety $X$ , and let $P = I ( { \boldsymbol { Y } } )$ the corresponding generic point in the associated affine scheme Spec $R$ with $R = A ( X )$ .

Show that the stalk $\mathcal { O } _ { \operatorname { S p e c } R , P }$ is “the ring of rational functions in a neighborhood of a general point of $Y ^ { \ast }$ , i. e. that it is isomorphic to the ring of equivalence classes of pairs $( U , \varphi )$ , where $U \subset X$ is open with $U \cap Y \neq \emptyset$ and $\varphi \in { \mathcal { O } } _ { X } ( U )$ , and where two such pairs $( U , \varphi )$ and $( U ^ { \prime } , \varphi ^ { \prime } )$ are considered equivalent if there is an open subset $V \subset U \cap U ^ { \prime }$ with $V \cap Y \neq \emptyset$ such that $\varphi | _ { V } = \varphi ^ { \prime } | _ { V }$ .

Of course, Definition 12.16 is not very useful to work with regular functions in practice. The following proposition, which describes regular functions on distinguished open subsets and is entirely analogous to Proposition 3.8, provides a much more convenient description.

Proposition 12.20 (Regular functions on distinguished open subsets). Let $R$ be a ring and $f \in R$ Then $\mathcal { O } _ { \mathrm { S p e c } R } ( D ( f ) )$ is isomorphic to the localization $R _ { f }$ .

In particular, setting $f = 1$ we see that the global regular functions are $\mathcal { O } _ { \mathrm { S p e c } R } \big ( \mathrm { S p e c } R \big ) \cong R$ .

Proof. There is a well-defined ring homomorphism

$$
R _ { f } \mapsto { \mathcal { O } } _ { \operatorname { S p e c } R } ( D ( f ) ) , { \frac { g } { f ^ { r } } } \mapsto { \frac { g } { f ^ { r } } }
$$

that maps $\textstyle { \frac { g } { f r } } \in R _ { f }$ to the family $\varphi = ( \varphi _ { P } ) _ { P \in D ( f ) }$ with $\begin{array} { r } { \varphi _ { P } = { \frac { g } { f ^ { r } } } \in R _ { P } } \end{array}$ for all $P \in D ( f )$ . We have to prove that it is bijective.

To show that it is injective let $g \in R$ and $r \in \mathbb { N }$ such that $\begin{array} { r } { \frac { g } { f r } = 0 } \end{array}$ on $D ( f )$ . For all $P \in D ( f )$ this means that $\textstyle { \frac { g } { f r } } = 0 \in R _ { P }$ , i. e. there is an element $h \not \in P$ with $h g = 0$ , showing that $P \ \mathscr { Z } \ J : = \{ h \in R : h g = 0 \}$ , and consequently $P \notin V ( J )$ by Remark 12.7. In other words, we have $V ( J ) \subset V ( f )$ , and hence $f \in { \sqrt { \langle f \rangle } } \subset { \sqrt { J } }$ by the Nullstellensatz of Proposition 12.10. This means that $f ^ { k } \in J$ for some $k \in \mathbb N$ , i. e. $f ^ { k } g = 0$ by definition of $J$ , and thus $\textstyle { \frac { g } { f r } } = 0 \in R _ { f }$ . Hence, the map $( \ast )$ is injective.

Surjectivity of $( * )$ is harder, but follows closely the proof of the analogous statement of Proposition 3.8 for affine varieties. Let $\varphi \in { \mathcal { O } } _ { \operatorname { S p e c } R } ( D ( f ) )$ . By definition, for each $P \in D ( f )$ there are $f _ { P } , g _ { P } \in R$ such that $\textstyle \varphi = { \frac { g _ { P } } { f _ { P } } } $ on some open neighborhood $U _ { P }$ of $P$ in $D ( f )$ with $U _ { P } \subset D ( f _ { P } )$ . As the distinguished open subsets form a basis for the topology of Spec $R$ , we may assume that $U _ { P } = D ( h _ { P } )$ for some $h _ { P } \in R$ .

We want to show that we can assume $f _ { P } = h _ { P }$ for all $P$ . In fact, as $D ( h _ { P } ) \subset D ( f _ { P } )$ , which means that $V ( f _ { P } ) \subset V ( h _ { P } )$ , we have $h _ { P } \in \sqrt { \langle h _ { P } \rangle } \subset \sqrt { \langle f _ { P } \rangle }$ by Proposition 12.10. Hence $h _ { P } ^ { r } = c f _ { P }$ for some $r \in \mathbb { N }$ and $c \in R$ , so that $\begin{array} { r } { \frac { g _ { P } } { f _ { P } } = \frac { c g _ { P } } { h _ { P } ^ { r } } } \end{array}$ . Replacing $f _ { P }$ by $h _ { P } ^ { r }$ (with $D ( f _ { P } ) = D ( h _ { P } ) )$ and $g _ { P }$ by $c g _ { P }$ we can thus assume that $D ( f )$ is covered by open subsets of the form $D ( f _ { P } )$ , and that $\textstyle \varphi = { \frac { g _ { P } } { f _ { P } } } $ on $D _ { f _ { P } }$ .

Next we prove that $D ( f )$ can actually be covered by finitely many such distinguished opens $D ( f _ { P } )$ . Indeed, $D ( f ) \subset \bigcup _ { P } D ( f _ { P } )$ is equivalent to $\begin{array} { r } { V ( f ) \supset \bigcap _ { P } V ( f _ { P } ) = V \bigl ( \sum _ { P } \langle f _ { P } \rangle \bigr ) } \end{array}$ , so to $\sqrt { \langle f \rangle } \subset \sqrt { \sum _ { P } \langle f _ { P } \rangle }$ by Proposition 12.10, i. e. to $\textstyle f ^ { r } \in \sum _ { P } \left. f _ { P } \right.$ for some $r \in \mathbb { N }$ . But this means that $f ^ { r }$ can be written as a finite sum $\begin{array} { r } { f ^ { r } = \sum _ { P } k _ { P } f _ { P } } \end{array}$ with $k _ { P } \in R$ . Hence we only have to consider finitely many $P$ .

On the distinguished open subset $D ( f _ { P } ) \cap D ( f _ { Q } ) = D ( f _ { P } f _ { Q } )$ for some $P$ and $Q$ , we now have two fractions $\frac { g _ { P } } { f _ { P } }$ and $\frac { g _ { Q } } { f _ { Q } }$ representing $\varphi$ . So by the injectivity proven above it follows that $\begin{array} { r } { \frac { g _ { P } } { f _ { P } } = \frac { g _ { Q } } { f _ { Q } } } \end{array}$ gQ in $R _ { f _ { P } f _ { Q } }$ , i. e. that $( \tilde { f _ { P } f _ { Q } } ) ^ { n } ( g _ { P } f _ { Q } - g _ { Q } f _ { P } ) = 0 \in R$ for some $n$ . As we have only finitely many $P$ and $Q$ to consider, we may pick one $n$ that works for all of them. Now replace $g _ { P }$ by $g _ { P } f _ { P } ^ { n }$ and $f _ { P }$ by $f _ { P } ^ { n + 1 }$ for all $P$ . Then $\varphi$ is still represented by $\frac { g _ { P } } { f _ { P } }$ on $D ( f _ { P } )$ , and moreover $g _ { P } f _ { Q } - g _ { Q } f _ { P } = 0$ for all $P , Q$ .

Finally, write $\begin{array} { r } { f ^ { r } = \sum _ { P } k _ { P } f _ { P } } \end{array}$ as above, and set $\begin{array} { r } { g = \sum _ { P } k _ { P } g _ { P } } \end{array}$ . Then for every $Q$ we have

$$
g f _ { Q } = \sum _ { P } k _ { P } g _ { P } f _ { Q } = \sum _ { P } k _ { P } g _ { Q } f _ { P } = f ^ { r } g _ { Q } ,
$$

$\begin{array} { r } { { \frac { g } { f r } } = { \frac { g _ { Q } } { f _ { Q } } } } \end{array}$ on $D ( f _ { Q } )$ for all $Q$ . Hence $\varphi$ is represented by $\textstyle { \frac { g } { f r } } \in R _ { f }$ on all of $D ( f )$

# Example 12.21.

(a) (Double points) Let $R = K [ x ] / \langle x ^ { 2 } \rangle$ for a field $K$ . Then $x$ is nilpotent in $R$ , and hence on the affine scheme Spec $R$ the ring $\mathcal { O } _ { \mathrm { S p e c } R } \big ( \mathrm { S p e c } R \big ) \overset { 1 2 . 2 0 } { = } R$ of global regular functions has nilpotent elements — which is something that cannot happen for an affine variety $X$ since its coordinate ring $A ( X )$ is always a quotient of a polynomial ring by a radical ideal $I ( X )$ .

More precisely, the global regular functions on Spec R are of the form $\varphi = a + b x$ for $a , b \in K$ Note that Spec $R$ has only one point $P = \langle x \rangle$ , and that $\varphi ( P ) = a \in R / \langle x \rangle = K = K ( P )$ . Hence we can also see from this example that a regular function need not be determined by its values at all points.

Geometrically, one can think of Spec $R$ as “a point that extends infinitesimally in one direction”: As on the affine line $\mathbb { A } _ { K } ^ { 1 }$ , there are polynomial functions in one variable on Spec R, but the space is such an infinitesimally small neighborhood of the origin that we can only see the linearization of the functions on it, and that it does not contain any actual points except 0.

![](images/e2427541ac6b4f1dd1121a4e86ceb586dca6e9d32d30b46266e1e0843c935d81.jpg)

It is usually called a double point or a fat point over $K$ , with the word “double” referring to the vector space dimension of $R$ over $K$ (see also Exercise 12.43).

(b) On the affine scheme Spec $\mathbb { Z }$ consider the open subset

$$
D ( 6 ) = \{ \langle 0 \rangle \} \cup \{ \langle p \rangle : p \neq 2 , 3 { \mathrm { ~ p r i m e } } \} \quad \subset \operatorname { S p e c } \mathbb { Z } .
$$

With the isomorphism of Proposition 12.20 the fraction $\textstyle \varphi = { \frac { 5 } { 6 } }$ in the localization of $\mathbb { Z }$ at the set $\{ 6 ^ { n } : n \in \mathbb { N } \}$ is a well-defined regular function on $D ( 6 )$ , and its values correspond to the ways this fraction can be interpreted in different fields:

• $\varphi ( \langle 0 \rangle )$ is the rational number $\textstyle { \frac { 5 } { 6 } } \in \mathbb { Q } = K { \bigl ( } \langle 0 \rangle { \bigr ) }$ .   
• $\varphi ( \langle p \rangle )$ for $p \neq 2 , 3$ is the element $\overline { { 5 } } . \overline { { 6 } } ^ { - 1 }$ in the field $\mathbb { Z } / p \mathbb { Z } = K ( \langle p \rangle )$ , so e. g. $\varphi$ has a zero at $\langle 5 \rangle$ and $\varphi ( \langle 1 1 \rangle ) = { \overline { { 5 } } } \cdot { \overline { { 2 } } } = { \overline { { 1 0 } } } \in \mathbb { Z } / 1 1 \mathbb { Z }$ .

Exercise 12.22. Let $R$ be a ring. Prove that the affine scheme Spec $R$ is disconnected if and only if $R \cong S \times T$ for two non-zero rings $s$ and $T$ .

With affine schemes defined as ringed spaces, one might hope that we can now go ahead as before and define morphisms of affine schemes just as morphisms of ringed spaces. There is a slight problem with this however, which is due to our simplification in Convention 4.2: We have defined a morphism between two ringed spaces $X$ and $Y$ as a continuous map $f \colon X \to Y$ that pulls back regular functions to regular functions, i. e. such that $f ^ { * } \varphi \in { \mathcal { O } } _ { X } ( f ^ { - 1 } ( U ) )$ for any regular function $\varphi \in { \mathcal { O } } _ { Y } ( U )$ on an open subset $U$ . However, our definition $f ^ { * } \varphi : = \varphi \circ f$ of the pull-back is purely set-theoretic and can only be used to consider values of functions — but we have just seen in Example 12.21 (a) that a regular function on an affine scheme is in general not determined by its values.

The only way around this problem is to include all pull-backs $f ^ { * } \colon { \mathcal { O } } _ { Y } ( U ) \to { \mathcal { O } } _ { X } ( f ^ { - 1 } ( U ) )$ into the data that has to be given to define a morphism. Of course, these a priori arbitrary ring homomorphisms then need to satisfy a certain compatibility condition with the continuous map $f \colon X \to Y$ . To motivate this compatibility condition, let us have a look at the case of (pre-)varieties again.

Remark 12.23. Let $f \colon X \to Y$ be a morphism of (pre-)varieties. For all open subsets $U \subset Y$ the pull-back maps $f ^ { * } \colon { \mathcal { O } } _ { Y } ( U ) \to { \mathcal { O } } _ { X } ( f ^ { - 1 } ( U ) )$ are compatible with restrictions, and hence determine well-defined ring homomorphisms $f _ { a } ^ { * } \colon { \mathcal { O } } _ { Y , f ( a ) } \to { \mathcal { O } } _ { X , a }$ between the stalks for all $a \in X$ . Now recall that these stalks are local rings by Lemma 3.19, with maximal ideals

$$
I _ { a } = \{ \varphi \in { \mathcal O } _ { X , a } : \varphi ( a ) = 0 \} \quad \mathrm { a n d } \quad I _ { f ( a ) } = \{ \varphi \in { \mathcal O } _ { Y , f ( a ) } : \varphi ( f ( a ) ) = 0 \} ,
$$

respectively. Hence we have

$$
( f _ { a } ^ { * } ) ^ { - 1 } ( I _ { a } ) = \{ \varphi \in { \mathcal { O } } _ { Y , f ( a ) } : ( f ^ { * } \varphi ) ( a ) = 0 \} = \{ \varphi \in { \mathcal { O } } _ { Y , f ( a ) } : \varphi ( f ( a ) ) = 0 \} = I _ { f ( a ) } ,
$$

i. e. the local maps $f _ { a } ^ { * } \colon { \mathcal { O } } _ { Y , f ( a ) } \to { \mathcal { O } } _ { X , a }$ have the property that the inverse image of the maximal ideal of ${ \mathcal { O } } _ { X , a }$ is the maximal ideal of $\mathcal { O } _ { Y , f ( a ) }$ . As the stalks of the structure sheaf of an affine scheme are local rings as well by Lemma 12.18, we can use this as compatibility condition between the topological map $f$ and the pull-backs $f ^ { * }$ ; we just have to include this requirement of these stalks being local rings into our definition of ringed spaces.

Definition 12.24 (Locally ringed spaces). A locally ringed space is a ringed space $( X , { \mathcal { O } } _ { X } )$ such that each stalk $\mathcal { O } _ { X , P }$ for $P \in X$ is a local ring.

# Example 12.25.

(a) By Lemma 3.19, every (pre-)variety is a locally ringed space.   
(b) Every open subset of a locally ringed space, together with the restricted structure sheaf as in Definition 3.16, is again a locally ringed space.   
(c) By Lemma 12.18, every affine scheme (and hence by (b) also every open subset of an affine scheme) is a locally ringed space.

Definition 12.26 (Morphisms of locally ringed spaces). A morphism of locally ringed spaces from $( X , { \mathcal { O } } _ { X } )$ to $( Y , { \mathcal { O } } _ { Y } )$ is given by the following data:

• a continuous map $f \colon X \to Y$ ;   
• for every open subset $U \subset Y$ a ring homomorphism $f _ { U } ^ { * } \colon { \mathcal { O } } _ { Y } ( U ) \to { \mathcal { O } } _ { X } ( f ^ { - 1 } ( U ) )$ called pullback on $U$ ;

such that the following two conditions hold:

• The pull-back maps are compatible with restrictions, i. e. we have $f _ { U } ^ { * } ( \pmb { \varphi } | _ { U } ) = \left. \left( f _ { V } ^ { * } \pmb { \varphi } \right) \right| _ { f ^ { - 1 } ( U ) }$ for all $U \subset V \subset Y$ and $\varphi \in { \mathcal { O } } _ { Y } ( V )$ in the notation of Definition 3.13. In particular, this implies that there are induced ring homomorphisms $f _ { P } ^ { * } \colon { \mathcal { O } } _ { Y , f ( P ) } \to { \mathcal { O } } _ { X , P }$ on the stalks for all $P \in X$ .   
• For all $P \in X$ , we have $( f _ { P } ^ { * } ) ^ { - 1 } ( I _ { P } ) = I _ { f ( P ) }$ , where $I _ { P }$ and $I _ { f ( P ) }$ denote the maximal ideals in the local rings ${ \mathcal { O } } _ { X , P }$ and $\mathcal { O } _ { Y , f ( P ) }$ , respectively.

We will often write the pull-back maps $f _ { U } ^ { * }$ and $f _ { P } ^ { * }$ just as $f ^ { * }$ if it is clear from the context on which rings they act.

Example 12.27. By Remark 12.23, every morphism of (pre-)varieties is a morphism of locally ringed spaces.

Let us now check that this is the “correct” definition for affine schemes, i. e. that their morphisms now correspond exactly to homomorphisms of the underlying rings.

Proposition 12.28. For any two rings R and S there is a bijection

$$
\begin{array} { r c l } { { \{ m o r p h i s m s ~ { \mathrm { S p e c } } R  { \mathrm { S p e c } } S \} } } & { { \stackrel { \downarrow : 1 } { \longleftrightarrow } } } & { { \{ r i n g ~ h o m o m o r p h i s m s ~ S  R \} } } \\ { { f } } & { { \longmapsto } } & { { f ^ { * } . } } \end{array}
$$

In particular, this means that there is a natural bijection

$$
\{ a f f i n e \ s c h e m e s \} / i s o m o r p h i s m s \quad \xleftarrow { \cdot } \quad \{ r i n g s \} / i s o m o r p h i s m s .
$$

Proof. If $f$ : Spe $\mathrm { \cdot c } R \to \mathrm { S p e c } S$ is a morphism of affine schemes, this includes by Definition 12.26 the data of a ring homomorphism $f _ { \mathrm { S p e c } S } ^ { * } \colon { \mathcal { O } } _ { \mathrm { S p e c } S } ( \mathrm { S p e c } S ) \to { \mathcal { O } } _ { \mathrm { S p e c } R } ( \mathrm { S p e c } R )$ , which by Proposition 12.20 is just a ring homomorphism $f ^ { * } \colon S \to R$ .

Conversely, if $\varphi \colon S  R$ is a ring homomorphism this first of all defines a set-theoretic map $f$ : Spec $R \to \operatorname { S p e c } S$ , $P \mapsto \varphi ^ { - 1 } ( P )$ as inverse images of prime ideals under ring homomorphisms are again prime. This map is continuous since for any ideal $J \triangleleft S$ we have

$$
f ^ { - 1 } ( V ( J ) ) = \left\{ P \in \operatorname { S p e c } R : f ( P ) = \varphi ^ { - 1 } ( P ) \supset J \right\} = \left\{ P \in \operatorname { S p e c } R : P \supset \varphi ( J ) \right\} = V ( \varphi ( J ) ) ,
$$

so that the inverse image of any closed set under $f$ is closed. Moreover, localizing $\varphi$ at a prime ideal $P \in { \mathrm { S p e c } } R$ gives us an induced homomorphism $\varphi _ { P } \colon S _ { \varphi ^ { - 1 } ( P ) } \to R _ { P }$ . As the sections of the structure sheaves on Spec $R$ and Spec $s$ are by Definition 12.16 made up from elements of these localizations $R _ { P }$ and $S _ { f ( P ) }$ , respectively, this in turn induces componentwise ring homomorphisms $f _ { U } ^ { * } \colon { \mathcal { O } } _ { \operatorname { S p e c } S } ( U ) \to { \mathcal { O } } _ { \operatorname { S p e c } R } ( f ^ { - 1 } ( U ) )$ for all open subsets $U \subset { \mathrm { S p e c } } S$ . They are by construction compatible with restrictions, and their induced maps on the stalks are just $f _ { P } ^ { * } = \varphi _ { P }$ by Lemma 12.18. As these localized homomorphisms satisfy $\varphi _ { P } ^ { - 1 } ( I _ { P } ) = I _ { \varphi ^ { - 1 } ( P ) }$ , the data of $f$ and all $f _ { U } ^ { * }$ indeed determine a morphism of locally ringed spaces.

We leave it as an exercise to check that these two constructions are in fact inverse to each other.

Construction 12.29 (Affine subschemes and their intersections). With the correspondence between affine schemes and rings we can now give a good definition of affine subschemes. Recall that for an affine variety $X \subset \mathbb { A } ^ { n }$ we defined in Construction 1.17 that a subvariety is just a subset of $X$ that is itself an affine variety in $\mathbb { A } ^ { n }$ . But for affine schemes this definition does not make much sense as we have already seen in Remark 12.3 that an affine scheme is not determined by its underlying set alone.

Instead, we define an affine subscheme of an affine scheme Spec $R$ to be a scheme Spec S together with a morphism $i$ : Spec $S \to \operatorname { S p e c } R$ such that the corresponding ring homomorphism $\varphi \colon R \to S$ by Proposition 12.28 is surjective. Note that this implies as expected that the corresponding set-theoretic map $i$ : Spec $S \to \operatorname { S p e c } R$ , $P \mapsto \varphi ^ { - 1 } ( P )$ is injective.

Moreover, this means that up to isomorphism $\varphi$ is just the natural map to a quotient ring $S = R / J$ for an ideal $J \triangleleft R$ . So equivalently, we can say that an affine subscheme of Spec $R$ is an affine scheme of the form ${ \mathrm { S p e c } } R / J$ , together with the natural inclusion map Spec $R / J \to \mathsf { S p e c } R$ . Hence we get a bijection

$$
\{ { \mathrm { a f f i n e ~ s u b s c h e m e s ~ o f ~ } } S { \mathrm { p e c } } R \} \quad \stackrel { \scriptstyle 1 : 1 } { \longleftrightarrow } \quad \left\{ \mathrm { i d e a l s ~ i n ~ } R \right\}
$$

assigning to an ideal $J \triangleleft R$ the affine subscheme $\operatorname { S p e c } R / J$ . In addition, this means that we can define the scheme-theoretic intersection of two affine subschemes Spec $R / J _ { 1 }$ and $\operatorname { S p e c } R / J _ { 2 }$ of Spec $R$ to be the affine subscheme

$$
\operatorname { S p e c } R / J _ { 1 } \cap \operatorname { S p e c } R / J _ { 2 } : = \operatorname { S p e c } R / ( J _ { 1 } + J _ { 2 } ) ,
$$

which corresponds exactly to our result of Lemma 1.12 (b), but without the radical.

For example, let us consider the scheme-theoretic analogue of the example in Remark 1.13, i. e. the two affine subschemes Spec $R / J _ { 1 }$ and $\operatorname { S p e c } R / J _ { 2 }$ of the plane Spec $R$ for $R = K [ x _ { 1 } , x _ { 2 } ]$ , $J _ { 1 } = \left. x _ { 2 } - x _ { 1 } ^ { 2 } \right.$ , and $J _ { 2 } = \left. x _ { 2 } \right.$ . Their scheme-theoretic intersection is

$$
\operatorname { S p e c } R / ( J _ { 1 } + J _ { 2 } ) = \operatorname { S p e c } R / \langle x _ { 2 } - x _ { 1 } ^ { 2 } , x _ { 2 } \rangle = \operatorname { S p e c } R / \langle x _ { 2 } , x _ { 1 } ^ { 2 } \rangle ,
$$

![](images/61be984abcfb02f890442951c86bf2dd395d4833e7659cc4b1ffbd86969bfdca.jpg)

i. e. we obtain exactly the double point of Example 12.21 (a) in $x _ { 1 }$ - direction, encoding the tangency of the two curves.

The following proposition is the scheme-theoretic analogue of Proposition 4.17.

Proposition 12.30 (Distinguished open subsets are affine schemes). Let $R$ be a ring, and let $f \in R$ .   
Then the distinguished open subset $D ( f ) \subset { \mathsf { S p e c } } R$ is isomorphic to the affine scheme Spec $R _ { f }$ .

Proof. Note that both $D ( f )$ and ${ \mathrm { S p e c } } R _ { f }$ have the same underlying set $\{ P \in { \mathrm { S p e c } } R : f \not \in P \}$ . Let us compare their structure sheaves on the common distinguished open subset $U$ of all primes not containing a given element $g \in R$ :

• on $D ( f ) \subset { \mathsf { S p e c } } R$ , this is the open subset $D ( f ) \cap D ( g ) = D ( f g )$ , and hence we have $\mathcal { O } _ { D ( f ) } ( U ) \cong \mathrm { S p e c } R _ { f g }$ by Proposition 12.20; • on Spec $R _ { f }$ , we have ${ \mathcal { O } } _ { \operatorname { S p e c } R _ { f } } ( U ) \cong ( R _ { f } ) _ { g }$ again by Proposition 12.20.

As these two rings are isomorphic, we conclude that ${ \mathcal { O } } _ { D ( f ) } ( U ) \cong { \mathcal { O } } _ { \operatorname { S p e c } R _ { f } } ( U )$ for all distinguished open subsets $U$ . But every open subset is a union of distinguished open subsets by Remark 12.13, so the sheaf gluing axiom implies that the same isomorphism holds in fact for every (common) open subset of $D ( f )$ and Spec $R _ { f }$ . Hence, $D ( f )$ and ${ \mathrm { S p e c } } R _ { f }$ are isomorphic as locally ringed spaces. 

As in the case of (pre-)varieties in Chapter 5, the transition from affine schemes to arbitrary schemes is now simply obtained by gluing — with the only difference that we now also allow to glue infinitely many affine schemes.

Definition 12.31 (Schemes). A scheme is a (locally) ringed space that has an open cover by affine schemes. Morphisms of schemes are just morphisms as locally ringed spaces.

Remark 12.32. From the point of view of prevarieties, it would seem more natural to call the objects defined above preschemes, and then to say that a scheme is a prescheme having the separatedness property analogous to Definition 5.17. In the literature it is common however to adopt the terminology of Definition 12.31, and to talk about separated schemes if they have a closed diagonal in the sense of Construction 12.38.

Construction 12.33 (Open and closed subschemes). Let $X$ be a scheme. We want to define open and closed subschemes analogously to Construction 5.10.

(a) Let $U \subset X$ be an open subset. Then $U$ has an open cover by distinguished open subsets by Remark 12.13, which are affine schemes by Proposition 12.30. Hence, $U$ is also a scheme in a natural way. We call it an open subscheme of $X$ .   
(b) Of course, a closed subscheme should be a “glued version” of an affine subscheme as in Construction 12.29. Hence, in contrast to the case of prevarieties, a closed subscheme is not just determined by a closed subset of $X$ alone. Instead we simply say that a closed subscheme of $X$ is a scheme $Y$ together with a morphism $i \colon Y \to X$ such that $Y$ has an affine open cover $\{ U _ { k } : k \in I \}$ for which each restriction $i | _ { i ^ { - 1 } ( U _ { k } ) } \colon i ^ { - 1 } ( U _ { k } ) \to U _ { k }$ is an affine subscheme in the sense of Construction 12.29. It can be shown that it is equivalent to require that $i | _ { i ^ { - 1 } ( U ) } \colon i ^ { - 1 } ( U ) \to U$ is an affine subscheme for every affine open subset $U \subset X$ .

As the transition from affine schemes to arbitrary schemes is given by the same gluing construction as for prevarieties, we cannot only associate an affine scheme to an affine variety as in Example 12.2 (a), but analogously also a scheme to a prevariety. Let us just give the corresponding statements and their ideas here and leave their precise proofs (which are just simple checking using our definitions, constructions, and results) as an exercise:

Proposition 12.34 (Prevarieties as schemes).

(a) For every prevariety $X$ over an algebraically closed field $K$ , the set $X _ { \mathrm { s c h } }$ of all irreducible closed subsets of $X$ is a scheme in a natural way (namely by covering $X$ with affine varieties $U _ { i }$ and gluing the affine schemes Spec A $( U _ { i } )$ along the same isomorphisms). We call $X _ { \mathrm { s c h } }$ the scheme associated to $X$ .   
(b) The open subsets of $X$ correspond exactly to the open subsets of $X _ { \mathrm { s c h } }$ (they are unions of distinguished opens on various affine open subsets), and we have ${ \mathcal { O } } _ { X } ( U ) = { \mathcal { O } } _ { X _ { \mathrm { s c h } } } ( U )$ for every open subset $U$ with this identification.   
(c) Every morphism $X \to Y$ of prevarieties gives rise to a morphism $X _ { \mathrm { s c h } }  Y _ { \mathrm { s c h } }$ of the associated schemes in a natural way (locally for an affine open subset $U \subset X$ mapping to an affine open subset $V \subset Y$ , the corresponding $K$ -algebra homomorphism $A ( V ) \to A ( U )$ is also a ring homomorphism).

To finish this chapter, we want to identify which schemes actually come from (pre-)varieties in the sense of Proposition 12.34. As gluing works for schemes in the same way as for prevarieties (with the exception that for prevarieties only finitely many affine varieties may be glued together), the main differences between these two categories can already be seen on the level of affine schemes. They stem from the fact that an affine scheme Spec $R$ is defined for an arbitrary ring $R$ , whereas an affine scheme associated to an affine variety $X$ requires $R = A ( X )$ to be a finitely generated reduced $K$ -algebra (with morphisms of affine varieties only corresponding to $K$ -algebra homomorphisms). The following general properties of schemes capture these differences.

Definition 12.35 (Properties of schemes).

(a) Let $Y$ be a scheme. A scheme over $Y$ is a scheme $X$ together with X1 f X2 a morphism $f \colon X \to Y$ . A morphism of schemes $f _ { 1 } \colon X _ { 1 } \to Y$ and / $f _ { 2 } \colon X _ { 2 } \to Y$ over $Y$ is a morphism $f \colon X _ { 1 } \to X _ { 2 }$ of schemes with f f $f _ { 1 } = f _ { 2 } \circ f _ { }$ , i. e. such that the diagram shown on the right commutes. Y A scheme over an affine scheme $Y = { \mathrm { S p e c } } S$ is also called a scheme over S. If $X = { \mathrm { S p e c } } R$ is affine as well, this just means by Proposition 12.28 that we are given a ring homomorphism $S \to R$ , i. e. that $R$ is an $S \mathrm { . }$ -algebra.   
(b) A scheme $f \colon X \to Y$ over $Y$ is said to be of finite type over $Y$ if there is an open cover of $Y$ be affine schemes $V _ { i } = \operatorname { S p e c } S _ { i }$ such that $f ^ { - 1 } ( V _ { i } )$ has a finite open cover by affine schemes $U _ { i , j } = \mathrm { S p e c } R _ { i , j }$ , where each $R _ { i , j }$ is a finitely generated $S _ { i }$ -algebra. In particular, a scheme $X$ over a field $K$ is of finite type over $K$ if it has a finite open cover by affine schemes $U _ { i } = \operatorname { S p e c } R _ { i }$ , where each $R _ { i }$ is a finitely generated $K$ -algebra.   
(c) A scheme $X$ is called reduced if the rings ${ \mathcal { O } } _ { X } ( U )$ have no nilpotent elements for all open subsets $U \subset X$ .

Exercise 12.36. Show that for a scheme $X$ the following are equivalent:

(a) $X$ is reduced, i. e. for every open subset $U \subset X$ the ring ${ \mathcal { O } } _ { X } ( U )$ has no nilpotent elements. (b) There is an open cover of $X$ by affine schemes $U _ { i } = \operatorname { S p e c } R _ { i }$ such that every ring ${ \mathcal { O } } _ { X } ( U _ { i } ) = R _ { i }$ has no nilpotent elements. (c) For every point $P \in X$ the local ring ${ \mathcal { O } } _ { X , P }$ has no nilpotent elements.

Remark 12.37. For a field $K$ , note that $\operatorname { S p e c } K = \{ \langle 0 \rangle \}$ is topologically just a one-pointed space. Hence, for a scheme $X$ over $K$ the set-theoretic map $X \to \operatorname { S p e c } K$ is trivial, and the data of the morphism $f \colon X \to \mathbf { S p e c } K$ just means (since morphisms can be glued) that $X$ can be covered by affine open subsets of the form Spec $R$ for a $K$ -algebra $R$ .

Moreover, saying that $X$ is of finite type over $K$ is by definition equivalent to requiring that there is a finite open cover of this type, and that each $R$ is a finitely generated $K$ -algebra.

Finally, $X$ is reduced by Exercise 12.36 if and only if these $K$ -algebras $R$ are reduced. Hence, by Remark 4.16 the schemes associated to prevarieties as in Proposition 12.34 are exactly the reduced schemes of finite type over an algebraically closed field $K$ . Moreover, morphisms of prevarieties then correspond exactly to morphisms of the associated schemes over $K$ , since this requires that they are locally given by $K$ -algebra homomorphisms (instead of arbitrary ring homomorphisms).

To identify not just prevarieties but also varieties, we finally need to construct a product of schemes so that we can formulate a separatedness condition as in Definition 5.17. This is analogous to Definition 5.14 and Proposition 5.15, with the exception that products of schemes have to be taken over a base scheme as in Definition 12.35 (a). As a byproduct, this construction also allows us to generalize the definition of scheme-theoretic intersection of Construction 12.29 from affine to arbitrary schemes.

Construction 12.38 (Fiber products). Let $f _ { 1 } \colon X _ { 1 } \to Y$ and $f _ { 2 } \colon X _ { 2 } \to Y$ be schemes over Y . A fiber product of $X _ { 1 }$ and $X _ { 2 }$ over $Y$ is a scheme $P$ together with morphisms $\pi _ { 1 } \colon P \to X _ { 1 }$ and $\pi _ { 2 } \colon P  X _ { 2 }$ such that the square in the diagram on the right commutes, and such that the following universal property holds: For any two morphisms $g _ { 1 } \colon Z \to X _ { 1 }$ and $g _ { 2 } \colon Z \to X _ { 2 }$ from another scheme $Z$ that commute with $f _ { 1 }$ and $f _ { 2 }$ , there is a unique morphism $g \colon Z \to P$ that makes the complete diagram on the right commutative.

$$
\begin{array} { c } { { Z \brace { g _ { } ^ { } \ddots \sum _ { \begin{array} { c } { { g _ { 1 } } \\ { { } ^ { \ddots } } \\ { { } ^ { \ddots } } \\ { { } ^ { \ddots } } \end{array} } } } } \\ { { g _ { 2 } \underbrace { \begin{array} { c } { { g _ { } ^ { } \ddots } } \\ { { } } \\ { { \Biggl \{ \begin{array} { c c } { { \pi _ { 2 } } } \\ { { \pi _ { 2 } } } \\ { { \cdots } } \\ { { \chi _ { 2 } } } \end{array} \biggr \} } f _ { 1 } } } \end{array} } } } \end{array}
$$

If $Y = { \mathrm { S p e c } } S$ , $X = { \mathrm { S p e c } } R _ { 1 }$ , and $X = { \mathrm { S p e c } } R _ { 2 }$ are affine schemes, such a fiber product is given by the tensor product $P = { \mathrm { S p e c } } ( R _ { 1 } \otimes _ { S } R _ { 2 } )$ : As morphisms can be glued, we may assume that $Z$ is affine as well, and then the universal property follows by Proposition 12.28 and the universal property of tensor products, which is just given by the same diagram with all arrows reversed [G3, Chapter 5]. By Remark 4.11, for affine schemes associated to affine varieties over $K$ their fiber product over $K$ is exactly the scheme associated to the ordinary product of affine varieties.

For arbitrary schemes, one shows analogously to Proposition 5.15 that a fiber product exists (by gluing the tensor product constructions for affine open subsets of $X _ { 1 } , X _ { 2 }$ , and $Y$ ) and that it is unique up to unique isomorphism over Y . It is denoted by $X _ { 1 } \times _ { Y } X _ { 2 }$ .

# Definition 12.39.

(a) (Scheme-theoretic intersection) Let $i _ { 1 } \colon X _ { 1 } \to X$ and $i _ { 2 } \colon X _ { 2 } \to X$ be two closed subschemes in the sense of Construction 12.33 (b). Then their scheme-theoretic intersection $X _ { 1 } \cap X _ { 2 }$ is defined to be the fiber product $X _ { 1 } \times _ { X } X _ { 2 }$ (together with its induced morphism to $X$ ). Note that on an affine open subset $U = { \mathrm { S p e c } } R \subset X$ this just restricts to the old definition of Construction 12.29: We must then have $i _ { 1 } ^ { - 1 } ( U ) = { \mathrm { S p e c } } R / J _ { 1 }$ and $i _ { 2 } ^ { - 1 } ( U ) = { \mathrm { S p e c } } R / J _ { 2 }$ for ideals $J _ { 1 } , J _ { 2 } \triangleleft R$ , and as in Construction 12.38 their fiber product is given by the tensor product $\operatorname { S p e c } ( R / J _ { 1 } \otimes _ { R } R / J _ { 2 } ) \cong \operatorname { S p e c } R / ( J _ { 1 } + J _ { 2 } )$ .   
(b) (Separated schemes) A scheme $X$ over $Y$ is called separated over $Y$ if the image of the diagonal morphism $X \to X \times _ { Y } X$ (which exists by the universal property) is closed. By definition, a prevariety over $K$ is then separated if and only if its associated scheme is separated over $K$ , and together with Remark 12.37 we obtain:

Proposition 12.40 (Varieties as schemes). For an algebraically closed field $K$ there is a bijection

$$
\begin{array} { r c l } { { \{ \nu a r i e t i e s ~ o v e r ~ K \} } } & { { \stackrel { , ! : 1 } { \longleftrightarrow } } } & { { \{ s e p a r a t e d , ~ r e d u c e d ~ s c h e m e s ~ o f f u n i t e ~ t y p e ~ o v e r ~ K \} } } \\ { { X } } & { { \longmapsto } } & { { X _ { \mathrm { { s c h } } } , } } \end{array}
$$

and morphisms of varieties correspond exactly to morphisms of the associated schemes over K.

Convention 12.41. In the following, we will use Proposition 12.40 to identify varieties with their associated schemes. In this way, we can use the language of schemes, but all our previous results on varieties will remain valid. Hence, let us agree:

From now on, a variety will always be a separated, reduced scheme of finite type over an algebraically closed field $K$ .   
Points of a variety are always meant to be closed points.   
Morphisms of varieties are always morphisms over $K$ .

# Example 12.42.

(a) In the language of Convention 12.41, we have ${ \mathbb A } _ { K } ^ { n } = { \tt S p e c { K } } [ x _ { 1 } , \ldots , x _ { n } ]$ for $n \in \mathbb { N }$ and an algebraically closed field $K$ .   
(b) The complex conjugation map $\varphi \colon \mathbb C [ x _ { 1 } , \ldots , x _ { n } ] \to \mathbb C [ x _ { 1 } , \ldots , x _ { n } ]$ , $f \mapsto { \overline { { f } } }$ is a ring isomorphism, but not a $\mathbb { C }$ -algebra isomorphism. Hence the corresponding map $\mathbb { A } _ { \mathbb { C } } ^ { n } \to \mathbb { A } _ { \mathbb { C } } ^ { n }$ (that maps a prime ideal $P { \overset { \underset { \triangledown } { \triangleleft } } {  } } \mathbb { C } [ x _ { 1 } , \dots , x _ { n } ]$ to its complex conjugate) is an isomorphism of schemes, but not of schemes over $\mathbb { C }$ (and thus not of varieties over $\mathbb { C }$ ).

Exercise 12.43 (Fat points). For $n \in  { \mathbb { N } } _ { > 0 }$ , an $n$ -fold point or fat point over an algebraically closed field $K$ is a scheme over $K$ of the form Spec $R$ that contains only one point, and such that $R$ is a $K$ -algebra of vector space dimension $n$ over $K$ .

(a) Show that every double point over $K$ is isomorphic to Sp $\scriptstyle \mathtt { \backslash c K [ x ] / \langle x ^ { 2 } \rangle }$ . (b) Find two non-isomorphic triple points over $K$ . Can you describe them geometrically?

Exercise 12.44. Let $P$ be a (closed) point on a variety $X$ over an algebraically closed field $K$ , and denote by $D = { \mathrm { S p e c } } K [ x ] / \langle x ^ { 2 } \rangle$ the double point of Example 12.21 (a) and Exercise 12.43 (a). Show that the tangent space $T _ { X , P }$ to $X$ at $P$ can be canonically identified with the set of morphisms $D \to X$ that map the unique point of $D$ to $P$ .

# 13. Sheaves of Modules

After having introduced schemes as the central objects of interest in algebraic geometry, we now have to get a more detailed understanding of sheaves to advance further. Recall from Section 3 that, intuitively speaking, we initially defined a sheaf to be a structure on a topological space $X$ that describes function-like objects that can be glued together from local data. However, the only example of a sheaf that we have studied so far is the sheaf of regular functions on a variety or scheme.

In practice, there are many more important sheaves however that do not just describe “ordinary functions”. One main feature of them occurred already for the structure sheaf on a scheme in Definition 12.16, when we saw that sections of a sheaf are not necessarily just functions to a fixed ground field with some local properties. In fact, the following example shows that even for varieties one should also be interested in “functions to a varying target”:

Example 13.1 (Tangent sheaf). Consider a smooth curve $X$ , as e. g. the complex projective line $X = \mathbb { P } _ { \mathbb { C } } ^ { 1 } = \mathbb { C } \cup \{ \infty \}$ in the picture below on the right, which is topologically a sphere. At each point $P \in X$ we have constructed the tangent space $T _ { P } X$ to $X$ as a 1-dimensional vector space in Chapter 10. So we can try to construct a tangent sheaf $T _ { X }$ on $X$ by setting

$T _ { X } ( U ) = \{ \varphi = ( \varphi _ { P } ) _ { P \in U } : \varphi _ { P } \in T _ { P } X$ “varying nicely with $P ^ { \prime } \}$ for any open subset $U \subset X$ (where of course we will have to make precise what “varying nicely” means; see Chapter 15 for an exact construction of $T _ { X }$ ). In other words, a section $\varphi$ of $T _ { X }$ over $U$ is just given by specifying a tangent vector to $X$ at all points of $P$ . This is also often called a tangent vector field on $U$ . The arrows in the picture represent a global section of $T _ { X }$ . As the tangent spaces $T _ { P } X$ are all 1-dimensional vector spaces, we can think of sections of $T _ { X }$ as “functions to a moving 1- dimensional target”.

![](images/51d12a6bd40ea1715233f06aebafb8122982517086b717edd30c72fe71d2134c.jpg)

Note that there is no canonical way to multiply tangent vectors, and hence $T _ { X }$ will not be a sheaf of rings. There is also no reasonable notion of a “constant vector field”. In fact, we will see in Example 15.12 (a) that every global section of $T _ { \mathbb { P } ^ { 1 } }$ must have two zeros (as e. g. the north and south pole in the picture above).

But what we can do is to multiply a tangent vector field with a regular function (by multiplying the given tangent vector at every point with the value of the function), and hence $T _ { X }$ should be a module over the sheaf ${ \mathcal { O } } _ { X }$ of regular functions in a suitable sense. This leads to the central notion of a sheaf of modules that we will define now.

In the following, we will usually use the language of schemes from Chapter 12. However, in some cases (in particular for examples) we will restrict to varieties, i. e. in the sense of Convention 12.41 to separated and reduced schemes of finite type over an algebraically closed ground field, which we will then continue to denote by $K$ .

Definition 13.2 ((Pre-)sheaves of modules). Let $X$ be a scheme.

(a) A (pre-)sheaf of modules on $X$ , also called a (pre-)sheaf of ${ \mathcal { O } } _ { X }$ -modules, is a (pre-)sheaf $\mathcal { F }$ on $X$ as in Definition 3.13 such that ${ \mathcal { F } } ( U )$ is an ${ \mathcal { O } } _ { X } ( U )$ -module for all open subsets $U \subset X$ , and such that all restriction maps are ${ \mathcal { O } } _ { X }$ -module homomorphisms in the sense that

$$
( \varphi + \psi ) | _ { U } = \varphi | _ { U } + \psi | _ { U } \quad \mathrm { a n d } \quad ( \lambda \varphi ) | _ { U } = \lambda | _ { U } \cdot \varphi | _ { U }
$$

for all open subsets $U \subset V$ of $X$ , $\lambda \in { \mathcal { O } } _ { X } ( V )$ and $\varphi , \psi \in { \mathcal { F } } ( V )$ . (Note that they are not module homomorphisms in the usual sense as ${ \mathcal { F } } ( U )$ and ${ \mathcal { F } } ( V )$ are modules over different rings ${ \mathcal { O } } _ { X } ( U )$ resp. ${ \mathcal { O } } _ { X } ( V )$ , i. e. the scalars have to be restricted as well.)

In what follows, a (pre-)sheaf is always meant to be a (pre-)sheaf of modules unless stated otherwise. A sheaf of modules on $X$ is also often called an ${ \mathcal { O } } _ { X }$ -module.

(b) A morphism $f \colon { \mathcal { F } }  { \mathcal { G } }$ of (pre-)sheaves $\mathcal { F }$ and $\mathcal { G }$ of modules on $X$ is given by the data of ${ \mathcal { O } } _ { X } ( U )$ -module homomorphisms $f _ { U } \colon { \mathcal { F } } ( U ) \to { \mathcal { G } } ( U )$ for all open subsets $U \subset X$ that are compatible with restrictions, i. e. such that $f _ { V } ( \varphi ) | _ { U } = f _ { U } ( \varphi | _ { U } )$ for all open subsets $U \subset V$ and $\varphi \in { \mathcal { F } } ( V )$ .

For simplicity of notation, we will often write the homomorphisms $f _ { U }$ just as $f$

# Example 13.3.

(a) Clearly, ${ \mathcal { O } } _ { X }$ is a sheaf of modules on any scheme $X$ .   
(b) If $\mathcal { F }$ and $\mathcal { G }$ are sheaves of modules on a scheme $X$ , then so is the direct sum $\mathcal { F } \oplus \mathcal { G }$ defined by $( \mathcal { F } \oplus \mathcal { G } ) ( U ) : = \mathcal { F } ( U ) \oplus \mathcal { G } ( U )$ .

Probably the most important example of non-trivial sheaves of modules is given by the following construction that generalizes the sheaves of regular functions on $\mathbb { P } ^ { n }$ . As in Definition 7.1, we still consider quotients of homogeneous polynomials, but not necessarily of the same degree:

Construction 13.4 (Twisting sheaves on $\mathbb { P } ^ { n }$ ). Let $n \in  { \mathbb { N } } _ { > 0 }$ and $d \in \mathbb { Z }$ . For a non-empty open subset $U \subset \mathbb { P } ^ { n }$ we define

$$
\begin{array} { r } { ( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) ( U ) : = \left\{ \frac { g } { f } : f , g \in K [ x _ { 0 } , \ldots , x _ { n } ] \mathrm { ~ h o m o g e n e o u s ~ w i t h ~ d e g ~ } g - \deg f = d \right. } \\ { \left. \qquad \mathrm { ~ a n d ~ } f ( P ) \neq 0 \mathrm { ~ f o r ~ a l l ~ } P \in U \right\} } \end{array}
$$

as a subset of the quotient field of $K [ x _ { 0 } , \ldots , x _ { n } ]$ . Together with setting $( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) ( \pmb { \emptyset } ) : = \{ 0 \}$ we then obtain:

(a) $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ is a sheaf: Note that $K [ x _ { 0 } , \ldots , x _ { n } ]$ is a unique factorization domain, and thus that the representation of its elements as a quotient $\textstyle { \frac { g } { f } }$ with coprime $f$ and $g$ is unique (up to multiplying $f$ and $g$ with a constant in $K ^ { * }$ ). Hence, compatible sections of $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ on open subsets $U _ { i }$ (for $i$ in any index set) trivially glue to a section on $\cup _ { i \in I } U _ { i }$ .   
(b) For $d = 0$ we have $\mathcal { O } _ { \mathbb { P } ^ { n } } ( 0 ) \cong \mathcal { O } _ { \mathbb { P } ^ { n } }$ : The morphism $\mathcal { O } _ { \mathbb { P } ^ { n } } ( 0 ) \to \mathcal { O } _ { \mathbb { P } ^ { n } }$ , $\textstyle { \frac { g } { f } } \mapsto { \frac { g } { f } }$ is well-defined, surjective by the uniqueness statement of (a), and injective since $\textstyle { \frac { g } { f } }$ is zero as a function on a non-empty open subset of $\mathbb { P } ^ { n }$ only if $g = 0$ . In contrast, note that the sections of $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ for $d \neq 0$ are not well-defined functions as rescaling the homogeneous coordinates on $\mathbb P ^ { n }$ would change their value.   
(c) For any $e \in \mathbb { Z }$ there are bilinear maps

$$
( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) ( U ) \times ( \mathcal { O } _ { \mathbb { P } ^ { n } } ( e ) ) ( U ) \to ( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d + e ) ) ( U ) , ( \varphi , \psi ) \mapsto \varphi \psi .
$$

In particular, for $e = 0$ this means by (b) that $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ is an ${ \mathcal { O } } _ { \mathbb { P } ^ { n } }$ -module.

The sheaves $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ are called the twisting sheaves on $\mathbb { P } ^ { n }$ . The name comes from the fact that their sections can in some sense be interpreted as functions to a twisting (i. e. varying) target, see e. g. Exercise 13.6.

Example 13.5. Let $n \in  { \mathbb { N } } _ { > 0 }$ and $d \in \mathbb { Z }$

(a) For a global section $\begin{array} { r } { \frac { g } { f } \in ( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) ( \mathbb { P } ^ { n } ) } \end{array}$ we need $V ( f ) = \emptyset$ . Hence, by the Nullstellensatz $f$ must be a constant, that we can then absorb into the numerator $g$ . It follows that $( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) ( \mathbb { P } ^ { n } ) \cong K [ x _ { 0 } , \ldots , x _ { n } ] _ { d }$ is just the space of all homogeneous polynomials of degree $d$ . In particular, we have $( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) ( \mathbb { P } ^ { n } ) = \{ 0 \}$ for all $d < 0$ .

(b) For the open subset $U _ { 0 } = \{ ( x _ { 0 } : x _ { 1 } ) \in \mathbb { P } ^ { 1 } : x _ { 0 } \neq 0 \}$ of $\mathbb { P } ^ { 1 }$ we have $\begin{array} { r } { \frac { 1 } { x _ { 0 } } \in ( \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 1 ) ) ( U _ { 0 } ) } \end{array}$ (c) For any homogeneous polynomial $f \in K [ x _ { 0 } , \ldots , x _ { n } ]$ of degree $e$ and we have a morphism of sheaves

$$
{ \mathcal { O } } _ { \mathbb { P } ^ { n } } ( d ) \to { \mathcal { O } } _ { \mathbb { P } ^ { n } } ( d + e ) , \varphi \mapsto \varphi f
$$

(i. e. it is given by the maps $( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) ( U ) \to ( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d + e ) ) ( U ) , \varphi \mapsto \varphi f$ for all open subsets $U \subset \mathbb { P } ^ { n } ,$ ).

(d) For $d \neq 0$ , the sheaf $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ and the structure sheaf ${ \mathcal { O } } _ { \mathbb { P } ^ { n } }$ are not isomorphic on $\mathbb { P } ^ { n }$ since their spaces of global sections $( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) ( \mathbb { P } ^ { n } ) = K [ x _ { 0 } , \dots , x _ { n } ] _ { d }$ and ${ \mathcal { O } } _ { \mathbb { P } ^ { n } } ( \mathbb { P } ^ { n } ) = K$ differ by (a). But they become isomorphic when restricted to any open subset $U _ { i } = \left\{ \left( x _ { 0 } : \cdot \cdot \cdot : x _ { n } \right) : x _ { i } \neq 0 \right\}$ for $i = 0 , \ldots , n$ by

$$
f \colon \mathcal { O } _ { \mathbb { P } ^ { n } } | _ { U _ { i } } \to \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) | _ { U _ { i } } , \ \varphi \mapsto \varphi x _ { i } ^ { d } \quad \mathrm { w i t h ~ i n v e r s e } \quad f ^ { - 1 } \colon \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) | _ { U _ { i } } \to \mathcal { O } _ { \mathbb { P } ^ { n } } | _ { U _ { i } } , \ \varphi \mapsto \frac { \varphi } { x _ { i } ^ { d } } .
$$

Exercise 13.6 (The tautological sheaf on $\mathbb P ^ { n }$ ). Recall that $\mathbb P ^ { n }$ is by definition the set of 1-dimensional linear subspaces of $K ^ { n + 1 }$ . Hence we can define the tautological sheaf $\mathcal { F }$ on $\mathbb { P } ^ { n }$ by

${ \mathcal { F } } ( U ) = \{ \varphi \colon U \to K ^ { n + 1 }$ a morphism with $\varphi ( P ) \in P$ for all (closed) points P ∈ U }

for all open subsets $U \subset \mathbb { P } ^ { n }$ . (In other words, the value of $\varphi$ at every point $P \in U \subset \mathbb { P } ^ { n }$ has to lie in the corresponding 1-dimensional linear subspace of $K ^ { n + 1 }$ , so that in particular $\mathcal { F }$ is visibly a sheaf of functions to a 1-dimensional target that varies with the point in the source.)

Prove that $\mathcal { F }$ is isomorphic to the twisting sheaf $\mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 )$ .

Remark 13.7 (Morphisms on stalks). For a sheaf of modules $\mathcal { F }$ on a scheme $X$ , the ${ \mathcal { O } } _ { X }$ -module structure makes each stalk $\mathcal { F } _ { P }$ for $P \in X$ into an $\mathcal { O } _ { X , P }$ -module. As in Definition 12.26, a morphism $f \colon { \mathcal { F } }  { \mathcal { G } }$ of sheaves on $X$ then determines well-defined $\mathcal { O } _ { X , P }$ -module homomorphisms

$$
f _ { P } \colon \mathcal { F } _ { P }  \mathcal { G } _ { P } , \overline { { ( U , \varphi ) } }  \overline { { ( U , f _ { U } ( \varphi ) ) } }
$$

between the stalks.

Exercise 13.8 (Sheaf isomorphisms are local). Show that a morphism $f \colon { \mathcal { F } }  { \mathcal { G } }$ of sheaves on a scheme $X$ is an isomorphism if and only if the induced map $f _ { P } \colon \mathcal { F } _ { P } \to \mathcal { G } _ { P }$ on the stalk as in Remark 13.7 is an isomorphism for all $P \in X$ .

The goal of this chapter is to introduce and study the basic constructions that one can make with sheaves of modules. The simplest one is probably the push-forward of a sheaf along a morphism of schemes.

Definition 13.9 (Push-forward of sheaves). Let $f \colon X \to Y$ be a morphism of schemes, and let $\mathcal { F }$ be a sheaf on $X$ . For all open subsets $U \subset Y$ we set

$$
( f _ { \ast } { \mathcal { F } } ) ( U ) : = { \mathcal { F } } ( f ^ { - 1 } ( U ) ) .
$$

It is checked immediately that this is a sheaf on $Y$ ; in fact it is a sheaf of ${ \mathcal { O } } _ { Y }$ -modules by setting $\lambda \cdot \varphi : = f ^ { * } \lambda \cdot \varphi$ for all $\lambda \in { \mathcal { O } } _ { Y } ( U )$ and $\varphi \in { \mathcal { F } } ( f ^ { - 1 } ( U ) )$ .

Example 13.10. Let $f \colon X \to Y$ be a morphism of schemes.

(a) The data of the pull-back maps $f _ { U } ^ { * } \colon { \mathcal { O } } _ { Y } ( U ) \to { \mathcal { O } } _ { X } ( f ^ { - 1 } ( U ) )$ that come with $f$ as in Definition 12.26 define exactly a morphism of sheaves

$$
f ^ { * } \colon { \mathcal { O } } _ { Y } \to f _ { * } { \mathcal { O } } _ { X } , \varphi \mapsto f ^ { * } \varphi .
$$

In other words, one could simplify Definition 12.26 by saying that the data to define a morphism between locally ringed spaces $X$ and $Y$ is just a continuous map $f \colon X \to Y$ together with a morphism of sheaves $f ^ { * } \colon { \mathcal { O } } _ { Y } \to f _ { * } { \mathcal { O } } _ { X }$ (such that $( f _ { P } ^ { * } ) ^ { - 1 } ( I _ { P } ) = I _ { f ( P ) }$ with $f _ { P } ^ { * }$ as in Remark 13.7).

(b) As a more concrete example, let $P$ be a point on a variety $Y$ , and let $i \colon P \to Y$ be the inclusion map. Then we have $\mathcal { O } _ { P } ( P ) = K$ and $\mathcal { O } _ { P } ( \pmb { \emptyset } ) = \{ 0 \}$ . Hence, the sheaf $i _ { * } \mathcal { O } _ { P }$ is given by

$$
( i _ { * } { \mathcal { O } } _ { P } ) ( U ) = { \mathcal { O } } _ { P } ( i ^ { - 1 } ( U ) ) = { \left\{ K \begin{array} { l l } { K } & { { \mathrm { ~ i f ~ } } P \in U , } \\ { \{ 0 \} } & { { \mathrm { ~ i f ~ } } P \not \in U } \end{array} \right. } \quad { \mathrm { f o r ~ a l l ~ o p e n ~ s u b s e t s ~ } } U \subset Y ,
$$

and the morphism $\mathcal { O } _ { Y } \to i _ { * } \mathcal { O } _ { P }$ , $\varphi \mapsto i ^ { * } \varphi$ is given by evaluating a regular function $\varphi$ on $U \subset Y$ at the point $P$ (if it lies in $U$ ), as shown in the following picture.

![](images/af85b94cfefff10ad4086c47bc3988f2733cc187d0b828b55340b8309f8d2376.jpg)

The sections of $i _ { * } \mathcal { O } _ { P }$ can thus be interpreted as “functions on $Y$ that only have a value at $P ^ { * }$ . The sheaf $i _ { * } \mathcal { O } _ { P }$ is therefore usually denoted $K _ { P }$ (“the field $K$ concentrated at the point $P ^ { \ast }$ ) and called the skyscraper sheaf on $Y$ at $P$ (because of the shape of the shaded region above in which the graph of the function lies).

Next, we would expect that a morphism of sheaves of modules has a kernel and an image sheaf. Whereas the definition of the kernel is very straightforward, it turns out however that the construction of the image is more complicated. So in order to see the difference, let us prove in detail that the kernel sheaf can be obtained as expected.

Construction 13.11 (Kernel sheaf). Let $f \colon { \mathcal { F } }  { \mathcal { G } }$ be a morphism of sheaves on a scheme $X$ . For any open subset $U \subset X$ we set

$$
( \operatorname { K e r } f ) ( U ) : = \operatorname { K e r } ( f _ { U } { \mathrm { : ~ } } { \mathcal { F } } ( U ) \to { \mathcal { G } } ( U ) ) .
$$

It is clear that this defines a presheaf Ker $f$ on $X$ with the obvious restriction maps.

We claim that $\operatorname { K e r } f$ is in fact a sheaf on $X$ , i. e. that it satisfies the gluing property. To show this, let $\{ U _ { i } : i \in I \}$ be an open cover of an open subset $U \subset X$ , and assume that we are given sections $\varphi _ { i } \in \ker f _ { U _ { i } } \subset { \mathcal { F } } ( U _ { i } )$ that agree on the overlaps. As $\mathcal { F }$ is a sheaf, they glue to a unique section $\varphi \in { \mathcal { F } } ( U )$ , and we just have to check that $\varphi \in ( \ker f ) ( U )$ , i. e. that $f _ { U } ( \varphi ) = 0 \in { \mathcal { G } } ( U )$ . But $\mathcal { G }$ is a sheaf as well, so we can check this locally on the given open cover: For all $i \in I$ we have $f _ { U } ( \varphi ) | _ { U _ { i } } = f _ { U _ { i } } ( \varphi | _ { U _ { i } } ) = f _ { U _ { i } } ( \varphi _ { i } ) = 0$ .

Hence $\operatorname { K e r } f$ is a sheaf on $X$ . We call it the kernel sheaf of $f$ .

What the above argument boils down to is simply that the property of being in the kernel, i. e. of being mapped to zero under a morphism, is a local property — a function-like object is zero if it is zero on every subset of an open cover. So the kernel is again a sheaf. In contrast, if we defined the image in the same way, then for a section $\varphi \in { \mathcal { G } } ( U )$ of a sheaf $\mathcal { G }$ on an open set $U$ to be in the image of a morphism $f \colon { \mathcal { F } }  { \mathcal { G } }$ we would need one section of $\mathcal { F }$ on all of $U$ that maps to $\varphi$ under $f$ . This is not a local property, and hence replacing the kernel with the image in Construction 13.11 will only give us a presheaf in general. Let us see this explicitly, and denote this presheaf by $\operatorname { I m } ^ { \prime } f$ as it is just a preliminary construction that will be replaced by the “correct” one in Definition 13.19 (a).

Construction 13.12 (Image presheaf). For a morphism $f \colon { \mathcal { F } }  { \mathcal { G } }$ of sheaves on a scheme $X$ and any open subset $U \subset X$ we set

$$
( \operatorname { I m } ^ { \prime } f ) ( U ) : = \operatorname { I m } ( f _ { U } : { \mathcal { F } } ( U ) \to { \mathcal { G } } ( U ) ) .
$$

As in Construction 13.11, it is immediate that this defines a presheaf $\operatorname { I m } ^ { \prime } f$ on $X$ with the obvious restriction maps.

To see that $\operatorname { I m } ^ { \prime } f$ is in general not a sheaf, consider the inclusion map $i \colon \mathbb { A } ^ { 1 } \to \mathbb { A } ^ { 2 }$ , $x _ { 1 } \mapsto ( x _ { 1 } , 0 )$ and its corresponding morphism of sheaves $f = i ^ { * } \colon { \mathcal { O } } _ { \mathbb { A } ^ { 2 } } \to i _ { * } { \mathcal { O } } _ { \mathbb { A } ^ { 1 } }$ on $\mathbb { A } ^ { 2 }$ as in Example 13.10 (a). For the open cover of $U : = \mathbb { A } ^ { 2 } \backslash \{ ( 0 , 0 ) \}$ by $U _ { k } : = \{ ( x _ { 1 } , x _ { 2 } ) : x _ { k } \neq 0 \}$ for $k \in \{ 1 , 2 \}$ we then have by Corollary 3.10 and Example 3.11:

$$
\begin{array} { r l r l r } { \mathcal { O } _ { \mathbb { A } ^ { 2 } } ( U _ { 1 } ) = K [ x _ { 1 } , x _ { 2 } ] _ { x _ { 1 } } } & { \mathrm { a n d } } & { i _ { * } \mathcal { O } _ { \mathbb { A } ^ { 1 } } ( U _ { 1 } ) = K [ x _ { 1 } ] _ { x _ { 1 } } } & { \Rightarrow } & { ( \mathrm { I m } ^ { \prime } f ) ( U _ { 1 } ) = K [ x _ { 1 } ] _ { x _ { 1 } } , } \\ { \mathcal { O } _ { \mathbb { A } ^ { 2 } } ( U _ { 2 } ) = K [ x _ { 1 } , x _ { 2 } ] _ { x _ { 2 } } } & { \mathrm { a n d } } & { i _ { * } \mathcal { O } _ { \mathbb { A } ^ { 1 } } ( U _ { 2 } ) = \{ 0 \} } & { \Rightarrow } & { ( \mathrm { I m } ^ { \prime } f ) ( U _ { 2 } ) = \{ 0 \} , } \\ { \mathcal { O } _ { \mathbb { A } ^ { 2 } } ( U _ { 1 } \cap U _ { 2 } ) = K [ x _ { 1 } , x _ { 2 } ] _ { x _ { 1 } x _ { 2 } } } & { \mathrm { a n d } } & { i _ { * } \mathcal { O } _ { \mathbb { A } ^ { 1 } } ( U _ { 1 } \cap U _ { 2 } ) = \{ 0 \} } & { \Rightarrow } & { ( \mathrm { I m } ^ { \prime } f ) ( U _ { 1 } \cap U _ { 2 } ) = \{ 0 \} , } \\ { \mathcal { O } _ { \mathbb { A } ^ { 2 } } ( U ) = K [ x _ { 1 } , x _ { 2 } ] } & { \mathrm { a n d } } & { i _ { * } \mathcal { O } _ { \mathbb { A } ^ { 1 } } ( U ) = K [ x _ { 1 } ] _ { x _ { 1 } } } & { \Rightarrow } & { ( \mathrm { I m } ^ { \prime } f ) ( U ) = K [ x _ { 1 } ] . } \end{array}
$$

Hence the sections $\begin{array} { r } { \frac { 1 } { x _ { 1 } } \in ( \mathbf { I m } ^ { \prime } f ) ( U _ { 1 } ) } \end{array}$ and $0 \in ( \operatorname { I m } ^ { \prime } f ) ( U _ { 2 } )$ are (trivially) compatible on the overlap in $( \mathrm { I m } ^ { \prime } f ) ( U _ { 1 } \cap U _ { 2 } ) = \{ 0 \}$ , but they do not glue to a section in $( \operatorname { I m } ^ { \prime } f ) ( U ) = K [ x _ { 1 } ]$ . This means that $\operatorname { I m } ^ { \prime } f$ is not a sheaf. We call $\operatorname { I m } ^ { \prime } f$ the image presheaf of $f$ .

In fact, there are many more natural constructions with sheaves of modules that only yield a presheaf in general. Let us give one more example of this that will be important later.

Construction 13.13 (Tensor presheaf). Let $\mathcal { F }$ and $\mathcal { G }$ be two sheaves on a scheme $X$ . We define the tensor presheaf $\mathcal { F } \otimes ^ { \prime } \mathcal { G }$ on $X$ by

$$
( \mathcal { F } \otimes ^ { \prime } \mathcal { G } ) ( U ) : = \mathcal { F } ( U ) \otimes _ { \mathcal { O } _ { X } ( U ) } \mathcal { G } ( U )
$$

for any open subset $U \subset X$ (as in the previous constructions it is clear that this is a presheaf).

The following example shows that $\mathcal { F } \otimes ^ { \prime } \mathcal { G }$ is in general not a sheaf: On $X = \mathbb { P } ^ { 1 }$ consider the twisting sheaves $\mathcal { F } = \mathcal { O } _ { X } ( 1 )$ and $\mathcal { G } = \mathcal { O } _ { X } ( - 1 )$ , and the open subsets $U _ { i } = \{ ( x _ { 0 } : x _ { 1 } ) : x _ { i } \neq 0 \}$ for $i \in \{ 0 , 1 \}$ that cover $X$ . Then

$$
x _ { 0 } \otimes \frac { 1 } { x _ { 0 } } \in \ L ( \mathcal { F } \otimes ^ { \prime } \mathcal { G } ) ( U _ { 0 } ) \quad \mathrm { a n d } \quad x _ { 1 } \otimes \frac { 1 } { x _ { 1 } } \in ( \mathcal { F } \otimes ^ { \prime } \mathcal { G } ) ( U _ { 1 } ) ,
$$

and these two sections are compatible on $U _ { 0 } \cap U _ { 1 }$ since

$$
\begin{array} { r l } { x _ { 0 } \otimes { \cfrac { 1 } { x _ { 0 } } } = { \cfrac { x _ { 1 } } { x _ { 0 } } } \cdot x _ { 0 } \otimes { \cfrac { x _ { 0 } } { x _ { 1 } } } \cdot { \cfrac { 1 } { x _ { 0 } } } = x _ { 1 } \otimes { \cfrac { 1 } { x _ { 1 } } } } & { { } \in ( { \mathcal { F } } \otimes ^ { \prime } { \mathcal { G } } ) ( U _ { 0 } \cap U _ { 1 } ) } \end{array}
$$

as $\frac { x _ { 1 } } { x _ { 0 } }$ and $\frac { x _ { 0 } } { x _ { 1 } }$ are regular on $U _ { 0 } \cap U _ { 1 }$ . So if $\mathcal { F } \otimes ^ { \prime } \mathcal { G }$ was a sheaf, these sections would have to glue to a global section in

$$
\left( \mathcal { F } \otimes ^ { \prime } \mathcal { G } \right) ( X ) = \mathcal { F } ( X ) \otimes _ { \mathcal { O } _ { X } ( X ) } \mathcal { G } ( X ) \overset { 1 3 . 5 \ : ( \mathrm { a } ) } { = } \mathcal { F } ( X ) \otimes _ { \mathcal { O } _ { X } ( X ) } \{ 0 \} = \{ 0 \} ,
$$

which is of course impossible. Hence $\mathcal { F } \otimes ^ { \prime } \mathcal { G }$ is not a sheaf.

The way out of this trouble is called sheafification: a process that naturally associates to any presheaf ${ \mathcal { F } } ^ { \prime }$ a sheaf $\mathcal { F }$ that describes essentially the same function-like objects, but with the conditions on them made local. We have used this construction implicitly already in the construction of the structure sheaf of an affine variety $X$ or scheme Spec $R$ , when we initially wanted a regular function to be a quotient of elements of $A ( X )$ resp. $R$ , but then defined it to only be locally of this form to obtain a sheaf.

Definition 13.14 (Sheafification). Let ${ \mathcal { F } } ^ { \prime }$ be a presheaf on a scheme $X$ . For an open subset $U \subset X$ we set

where $s _ { Q } \in \mathcal { F } _ { Q } ^ { \prime }$ denotes the germ of $s$ in $Q$ . (As usual, we can write the condition in the last line as $\mathbf { \dot { \varphi } } _ { \varphi } = s$ on $U _ { P } { } ^ { \prime }$ ”.)

It is obvious from the local nature of the definition that $\mathcal { F }$ is a sheaf. It is called the sheafification of ${ \mathcal { F } } ^ { \prime }$ or sheaf associated to ${ \mathcal { F } } ^ { \prime }$ .

# Example 13.15.

(a) Let $X$ be an affine variety. If we had defined the presheaf $\mathcal { O } _ { X } ^ { \prime }$ of functions on $X$ that are (globally) quotients of polynomials, i. e.

$$
{ \mathcal { O } } _ { X } ^ { \prime } ( U ) = \left\{ \varphi : U \to K { \mathrm { ~ s u c h ~ t h a t ~ t h e r e ~ a r e ~ } } f , g \in A ( X ) { \mathrm { ~ w i t h ~ } } \varphi = { \frac { g } { f } } { \mathrm { ~ o n ~ } } U \right\}
$$

for all open subsets $U \subset X$ , then the structure sheaf ${ \mathcal { O } } _ { X }$ would just be the sheafification of $\mathcal { O } _ { X } ^ { \prime }$ . We have seen in Example 3.3 that $\mathcal { O } _ { X } ^ { \prime }$ is in general not a sheaf already and thus differs from ${ \mathcal { O } } _ { X }$ .

(b) As in Construction 13.13, consider again on $X = \mathbb { P } ^ { 1 }$ the two sections $\begin{array} { r } { s _ { i } : = x _ { i } \otimes \frac { 1 } { x _ { i } } } \end{array}$ of $\mathcal { O } _ { X } ( 1 ) \otimes ^ { \prime } \mathcal { O } _ { X } ( - 1 )$ on the open subsets $U _ { i } = \{ ( x _ { 0 } { : } x _ { 1 } ) : x _ { i } \neq 0 \}$ for $i \in \{ 0 , 1 \}$ . Although they are compatible on $U _ { 0 } \cap U _ { 1 }$ , we had seen that they do not glue to a global section of $\mathcal { O } _ { X } ( 1 ) \otimes ^ { \prime } \mathcal { O } _ { X } ( - 1 )$ . As expected, they now do glue however to a global section of the sheafification of $\mathcal { O } _ { X } ( 1 ) \otimes ^ { \prime } \mathcal { O } _ { X } ( - 1 )$ , namely to the family $\varphi = ( \varphi _ { P } ) _ { P \in X }$ with $\varphi _ { P } = { \left( s _ { 0 } \right) } _ { P }$ for all $P \in U _ { 0 }$ and $\varphi _ { P } = { \left( s _ { 1 } \right) } _ { P }$ for all $P \in U _ { 1 }$ .

Remark 13.16. Any presheaf ${ \mathcal { F } } ^ { \prime }$ on a scheme $X$ admits a natural morphism to its sheafification $\mathcal { F }$ defined by

$$
{ \mathcal { F } } ^ { \prime } ( U ) \to { \mathcal { F } } ( U ) , s \mapsto ( s _ { P } ) _ { P \in U }
$$

for all open subsets $U \subset X$ . In fact, there are some more immediate and important properties of sheafification that we should mention. For example, as it does not affect any local properties we would expect that it does not alter the stalks. Moreover, if we start with a sheaf (for which the conditions on the sections are local already) then the sheafification should not change anything. Let us quickly prove these two properties.

Lemma 13.17 (Properties of sheafification). Let ${ \mathcal { F } } ^ { \prime }$ be a presheaf on a scheme $X$ , and let $\mathcal { F }$ be its sheafification.

(a) For all $P \in X$ we have $\mathcal { F } _ { P } \cong \mathcal { F } _ { P } ^ { \prime }$ .   
(b) If ${ \mathcal { F } } ^ { \prime }$ is already a sheaf then $\mathcal { F } \cong \mathcal { F } ^ { \prime }$ .

# Proof.

(a) For all $P \in X$ there is a natural $\mathcal { O } _ { X , P }$ -module homomorphism $\mathcal { F } _ { P }  \mathcal { F } _ { P } ^ { \prime }$ , $\overline { { ( U , \varphi ) } } \mapsto \varphi _ { P }$ that sends the class of a family $\varphi = ( \varphi _ { Q } ) _ { Q \in U } \in { \mathcal { F } } ( U )$ to its element at $P$ . Conversely, the natural morphism $\mathcal { F } ^ { \prime } \to \mathcal { F }$ of Remark 13.16 gives rise to a homomorphism $\mathcal { F } _ { P } ^ { \prime } \to \mathcal { F } _ { P }$ by Remark 13.7. It is obvious that these two maps are inverse to each other, so we have $\mathcal { F } _ { P } \cong \mathcal { F } _ { P } ^ { \prime }$ .

(b) If ${ \mathcal { F } } ^ { \prime }$ is already a sheaf then the natural morphism $\mathcal { F } ^ { \prime } \to \mathcal { F }$ of Remark 13.16 is a morphism of sheaves. As it induces isomorphisms on the stalks by (a), it is itself an isomorphism by Exercise 13.8. 

Exercise 13.18 (Universal property of sheafification). Let ${ \mathcal { F } } ^ { \prime }$ be a presheaf on a scheme $X$ , and denote by $h \colon { \mathcal { F } } ^ { \prime } \to { \mathcal { F } }$ the natural morphism of Remark 13.16.

Prove that any morphism $f ^ { \prime } \colon \mathcal { F } ^ { \prime } \to \mathcal { G }$ to a sheaf $\mathcal { G }$ factors uniquely through $h$ , i. e. there is a unique morphism $f \colon { \mathcal { F } }  { \mathcal { G } }$ with $f ^ { \prime } = f \circ h$ .

Of course, the idea is now to append the process of sheafification to any construction involving sheaves that might just give us a presheaf. Let us list some important examples.

Definition 13.19 (Constructions with sheaves). Let $\mathcal { F }$ and $\mathcal { G }$ be sheaves on a scheme $X$ .

(a) For a morphism $f \colon { \mathcal { F } }  { \mathcal { G } }$ we define the image sheaf $\operatorname { I m } f$ to be the sheafification of the image presheaf $\operatorname { I m } ^ { \prime } f$ of Construction 13.12. Note that it admits a natural morphism to $\mathcal { G }$ by the universal property of Exercise 13.18. We say that $f$ is injective if $\operatorname { K e r } f = \{ 0 \}$ , we say that $f$ is surjective if $\operatorname { I m } f \cong { \mathcal { G } }$ (more precisely, if the natural map $\operatorname { I m } f \to { \mathcal { G } }$ is an isomorphism).

If $f$ is injective then all maps ${ \mathcal { F } } ( U ) \to { \mathcal { G } } ( U )$ for open subsets $U \subset X$ are injective by Construction 13.11, so we can define the quotient sheaf $\mathcal { G } / \mathcal { F }$ to be the sheafification of the presheaf $U \mapsto { \mathcal { G } } ( U ) / { \mathcal { F } } ( U )$ .

A sequence

$$
\cdots { \longrightarrow } { \mathcal { F } } _ { i } \xrightarrow { f _ { i } } { \mathcal { F } } _ { i + 1 } \xrightarrow { f _ { i + 1 } } { \mathcal { F } } _ { i + 2 } \longrightarrow \cdots
$$

of sheaves and morphisms on $X$ is called exact if $\operatorname { I m } f _ { i } \cong \operatorname { K e r } f _ { i + 1 }$ for all $i$ . (More precisely, we require that $f _ { i + 1 } \circ f _ { i }$ is the zero map, which induces morphisms $\operatorname { I m } ^ { \prime } f _ { i } \to \operatorname { K e r } f _ { i + 1 }$ and hence $\operatorname { I m } f _ { i } \to \operatorname { K e r } f _ { i + 1 }$ by Exercise 13.18; we require this to be an isomorphism.)

(b) The tensor sheaf $\mathcal { F } \otimes \mathcal { G }$ is the sheafification of the presheaf $U \mapsto { \mathcal { F } } ( U ) \otimes _ { { \mathcal { O } } _ { X } ( U ) } { \mathcal { G } } ( U )$ of Construction 13.13.

The dual sheaf $\mathcal { F } ^ { \vee }$ is the sheafification of the presheaf $U \mapsto { \mathrm { H o m } } _ { { \mathcal { O } } _ { X } ( U ) } ( { \mathcal { F } } ( U ) , { \mathcal { O } } _ { X } ( U ) ) .$ .

Exercise 13.20. Let $f \colon { \mathcal { F } }  { \mathcal { G } }$ be a morphism of sheaves on a scheme $X$ . Moreover, for a point $P \in X$ let $f _ { P } \colon \mathcal { F } _ { P } \to \mathcal { G } _ { P }$ be the induced map on the stalks as in Remark 13.7. Prove:

(a) $\begin{array} { l } { { ( \mathrm { K e r } f ) _ { P } = \mathrm { K e r } ( f _ { P } ) . } } \\ { { ( \mathrm { I m } f ) _ { P } = \mathrm { I m } ( f _ { P } ) . } } \end{array}$ (b)

In particular, conclude the following generalization of Exercise 13.8: The morphism $f$ is injective (resp. surjective) if and only if $f _ { P }$ is injective (resp. surjective) for all $P \in X$ .

Note that, with the definition of surjectivity and hence exactness involving sheafification, it is in general no longer true that a morphism of sheaves on a scheme $X$ is surjective (resp. a sequence of morphisms of sheaves on $X$ is exact) if and only if it is on sections for all open subsets $U \subset X$ — we will see this explicitly in Example 13.22 (b). However, we will see partial results in this direction in Exercise 13.26, and it is in any case possible to check exactness of a sequence locally in the following sense:

# Lemma 13.21. Let

$$
\cdots \to { \mathcal { F } } _ { i } \to { \mathcal { F } } _ { i + 1 } \to { \mathcal { F } } _ { i + 2 } \to \cdots
$$

be a sequence of sheaves and morphisms on a scheme $X$ . Then the following statements are equivalent:

(a) The sequence $\cdots \to { \mathcal { F } } _ { i } \to { \mathcal { F } } _ { i + 1 } \to { \mathcal { F } } _ { i + 2 } \to \cdots$ is exact.   
(b) The restricted sequence $\cdots \to { \mathcal { F } } _ { i } | _ { U } \to { \mathcal { F } } _ { i + 1 } | _ { U } \to { \mathcal { F } } _ { i + 2 } | _ { U } \to \cdots$ is exact for any open subset $U \subset X$ .   
(c) There is an open cover $\{ U _ { k } : k \in I \}$ of $X$ such that for all $k \in I$ the restricted sequence $\cdots \to { \mathcal { F } } _ { i } | _ { U _ { k } } \to { \mathcal { F } } _ { i + 1 } | _ { U _ { k } } \to { \mathcal { F } } _ { i + 2 } | _ { U _ { k } } \to \cdots$ is exact.   
(d) The induced sequence $\cdots \to ( \mathcal { F } _ { i } ) _ { P } \to ( \mathcal { F } _ { i + 1 } ) _ { P } \to ( \mathcal { F } _ { i + 2 } ) _ { P } \to \cdots$ on the stalks is exact for all $P \in X$ .

Proof. By definition, the given sequence is exact if and only if $\operatorname { I m } f _ { i } \cong \operatorname { K e r } f _ { i + 1 }$ for all $i$ . By Exercise 13.8 this is equivalent to $( \operatorname { I m } f _ { i } ) _ { P } \cong ( \operatorname { K e r } f _ { i + 1 } ) _ { P }$ for all $P \in X$ , and hence by Exercise 13.20 to $\operatorname { I m } ( ( f _ { i } ) _ { P } ) = \operatorname { K e r } ( ( f _ { i + 1 } ) _ { P } )$ for all $P \in X$ . This shows that (a) $\Leftrightarrow ( \mathrm { d } )$ .

The equivalences $( \mathbf { b } ) \Leftrightarrow ( \mathbf { d } )$ and $\left( \mathrm { c } \right) \Leftrightarrow \left( \mathrm { d } \right)$ follow in the same way since for any open subset $U$ containing a point $P$ the stalk $\mathcal { F } _ { P }$ depends only on $\mathcal { F } | _ { U }$ . 

Example 13.22 (Skyscraper sequence).

(a) Let $P = ( 1 { : } 0 ) \in X = \mathbb { P } ^ { 1 }$ , and denote by $i \colon P \to X$ the inclusion morphism. Consider the skyscraper sequence

$$
0 \longrightarrow \mathcal { O } _ { X } ( - 1 ) \stackrel { f } { \longrightarrow } \mathcal { O } _ { X } \stackrel { g } { \longrightarrow } K _ { P } \longrightarrow 0 ,
$$

where $f$ is given by multiplication with $x _ { 1 }$ as in Example 13.5 (c), and $g \colon { \mathcal { O } } _ { X } \to i _ { * } { \mathcal { O } } _ { P }$ is the evaluation at $P$ as in Example 13.10 (b). We claim that this sequence is exact. In fact, in the next chapter we will establish simple ways to check exactness of a sequence like this (see Example 14.9), but for now let us verify this directly:

• The kernel $\operatorname { K e r } f$ consists of all sections $\varphi$ of $\mathcal { O } _ { X } ( - 1 )$ such that $\varphi x _ { 1 } = 0$ (in the quotient field of $K [ x _ { 0 } , x _ { 1 } ] )$ . This obviously requires $\varphi = 0$ , and hence $f$ is injective. • The image presheaf $\operatorname { I m } ^ { \prime } f$ contains all regular functions of the form $\varphi x _ { 1 }$ for a section $\varphi$ of ${ \mathcal { O } } _ { X } ( - 1 )$ . These are exactly the regular functions with value 0 at $P$ . As this is a local condition we see that $\operatorname { I m } ^ { \prime } f$ is already a sheaf, and thus for any open subset $U \subset X$ that $( \operatorname { I m } f ) ( U ) = ( \operatorname { I m } ^ { \prime } f ) ( U ) = \{ \psi \in { \mathcal { O } } _ { X } ( U ) : \psi ( P ) = 0 { \mathrm { ~ i f ~ } } P \in U \} = ( \operatorname { K e r } g ) ( U ) .$ • We clearly have $\mathrm { I m } ^ { \prime } g = K _ { P }$ , as constant functions already map surjectively to $K _ { P }$ . So again, $\operatorname { I m } ^ { \prime } g$ is already a sheaf, and we conclude that $\mathrm { I m } g = K _ { P }$ as well, i. e. that $g$ is surjective.

(b) Now take the additional point $Q = ( 0 { : } 1 ) \in X$ and consider the double skyscraper sequence

$$
0 \longrightarrow \mathcal { O } _ { X } ( - 2 ) \stackrel { \cdot \cdot _ { 0 } x _ { 1 } } { \longrightarrow } \mathcal { O } _ { X } \stackrel { h } { \longrightarrow } K _ { P } \oplus K _ { Q } \longrightarrow 0 ,
$$

where the second non-trivial map $h$ is now the evaluation at $P$ and $Q$ . As this sequence just restricts to the ordinary skyscraper sequence of (a) on $U _ { i } = \{ ( x _ { 0 } : x _ { 1 } ) : x _ { i } \neq 0 \}$ for $i \in \{ 0 , 1 \}$ , we see by Lemma 13.21 that this sequence is still exact.

In particular, the map $h$ is surjective. But note that $h$ is not surjective on global sections as ${ \mathcal { O } } _ { X } ( X ) \cong K$ only contains constant functions by Corollary 7.23, and hence $( \mathrm { I m } ^ { \prime } h ) ( X ) \cong K$ only contains constant functions on $\{ P , Q \}$ — whereas $( K _ { P } \oplus K _ { Q } ) ( X ) = K ^ { 2 }$ . Sheafification will make this condition local, so that $( \mathrm { I m } h ) ( X )$ contains locally constant functions on $\{ P , Q \}$ and we have in fact ${ \mathrm { I m } } h \cong K _ { P } \oplus K _ { Q }$ .

Example 13.23 (Tensor products of twisting sheaves). Let $n \in \mathbb { N } _ { > 0 }$ and $d , e \in \mathbb { Z }$ . By Construction 13.4 (c) there are ${ \mathcal { O } } _ { \mathbb { P } ^ { n } } ( U )$ -module homomorphisms

$$
( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) ( U ) \otimes _ { \mathcal { O } _ { \mathbb { P } ^ { n } } ( U ) } ( \mathcal { O } _ { \mathbb { P } ^ { n } } ( e ) ) ( U ) \to ( \mathcal { O } _ { \mathbb { P } ^ { n } } ( d + e ) ) ( U ) , ( \varphi , \psi ) \mapsto \varphi \psi
$$

for all open subsets $U \subset \mathbb { P } ^ { n }$ . This defines presheaf homomorphisms $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) \otimes ^ { \prime } \mathcal { O } _ { \mathbb { P } ^ { n } } ( e ) \to \mathcal { O } _ { \mathbb { P } ^ { n } } ( d + e )$ , and hence morphisms $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) \otimes \mathcal { O } _ { \mathbb { P } ^ { n } } ( e ) \to \mathcal { O } _ { \mathbb { P } ^ { n } } ( d + e )$ by the universal property of sheafification of Exercise 13.18.

But on the open subsets $U _ { i } = \left\{ \left( x _ { 0 } : \cdots : x _ { n } \right) : x _ { i } \neq 0 \right\}$ this morphism just restricts by Example 13.5 (d) to $\mathcal { O } _ { \mathbb { P } ^ { n } } | _ { U } \otimes \mathcal { O } _ { \mathbb { P } ^ { n } } | _ { U } \to \mathcal { O } _ { \mathbb { P } ^ { n } } | _ { U }$ , which is clearly an isomorphism. Hence we conclude by Lemma 13.21 that

$$
\mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) \otimes \mathcal { O } _ { \mathbb { P } ^ { n } } ( e ) \cong \mathcal { O } _ { \mathbb { P } ^ { n } } ( d + e ) \quad \mathfrak { b } \mathrm { y } \quad \varphi \otimes \psi \mapsto \varphi \psi .
$$

Exercise 13.24. Find $d \in \mathbb { Z }$ and morphisms $f$ and $g$ such that the sequence

$$
0 \longrightarrow \mathcal { O } _ { \mathbb { P } ^ { 1 } } \overset { f } { \longrightarrow } \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 1 ) \oplus \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 1 ) \overset { g } { \longrightarrow } \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( d ) \longrightarrow 0
$$

is exact on $\mathbb { P } ^ { 1 }$

Exercise 13.25. Prove that $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ^ { \vee } \cong \mathcal { O } _ { \mathbb { P } ^ { n } } ( - d )$ for all $n \in  { \mathbb { N } } _ { > 0 }$ and $d \in \mathbb { Z }$

Exercise 13.26. Let $X$ be a scheme.

(a) Prove that a sequence of sheaves $\cdots \to { \mathcal { F } } _ { i } \to { \mathcal { F } } _ { i + 1 } \to { \mathcal { F } } _ { i + 2 } \to \cdots$ on $X$ is exact if the sequence of sections $\cdots \to { \mathcal { F } } _ { i } ( U ) \to { \mathcal { F } } _ { i + 1 } ( U ) \to { \mathcal { F } } _ { i + 2 } ( U ) \to \cdots$ is exact for all open subsets $U \subset X$ .   
(b) Let $f \colon { \mathcal { F } }  { \mathcal { G } }$ be an injective morphism of sheaves on $X$ . Prove that then the image presheaf $\operatorname { I m } ^ { \prime } f$ is already a sheaf. Conclude from this the following partial converse to (a): If $0  \mathcal { F } _ { 1 }  \mathcal { F } _ { 2 }  \mathcal { F } _ { 3 }$ is an exact sequence of sheaves on $X$ then the sequence of sections $0 \to { \mathcal { F } } _ { 1 } ( U ) \to { \mathcal { F } } _ { 2 } ( U ) \to { \mathcal { F } } _ { 3 } ( U )$ is also exact for all open subsets $U \subset X$ .

# 14. Quasi-coherent Sheaves

In the last chapter we have introduced sheaves of modules on schemes as an important tool in algebraic geometry. It turns out however that for many applications these arbitrary sheaves of modules are too general to be useful, and that one wants to restrict instead to a slightly smaller class of sheaves that has a closer relation to commutative algebra.

More precisely, if $X = { \mathrm { S p e c } } R$ is an affine scheme we would expect that a module over $R$ determines a sheaf of modules on $X$ . This is indeed the case, and almost any sheaf of modules on $X$ appearing in practice comes from an $R$ -module in this way. For computations, this means that statements about such a sheaf can finally be reduced to statements about the $R$ -module, and thus to pure commutative algebra. But it does not follow from the definitions that a sheaf on $X$ has to come from an $R$ -module, so we will say that it is quasi-coherent if it does, and in most cases restrict our attention to these quasi-coherent sheaves. For a general scheme, we accordingly require that this property holds on an affine open cover.

Let us start by showing exactly how an $R$ -module $M$ determines a sheaf of modules $\tilde { M }$ on the affine scheme $X = { \mathrm { S p e c } } R$ . Note that the following construction literally reproduces Definition 12.16 of the structure sheaf in the case of the module $M = R$ (so that we obtain $\dot { \tilde { R } } = \mathcal { O } _ { X }$ ).

Definition 14.1 (Sheaf associated to a module). Let $X = { \mathrm { S p e c } } R$ be an affine scheme, and let $M$ be an $R$ -module. For an open subset $U \subset X$ we set

It is clear from the local nature of the definition that $\tilde { M }$ is a sheaf. Moreover, $\tilde { M } ( U )$ is by construction a module over $\tilde { R } ( U ) = \mathcal { O } _ { X } ( U )$ , and hence $\tilde { M }$ is a sheaf of modules on $X$ . We call it the sheaf associated to $M$ .

As sheaves associated to modules are defined in the same way as the structure sheaf, they also share the same important basic properties:

Proposition 14.2. Let $X = { \mathrm { S p e c } } R$ be an affine scheme, and let M be an $R$ -module.

(a) For every $P \in X$ the stalk $\tilde { M } _ { P }$ of $\tilde { M }$ at $P$ is isomorphic to the localization $M _ { P }$ . (b) For every $f \in R$ we have $\tilde { M } ( D ( f ) ) \cong M _ { f }$ . In particular, setting $f = 1$ we obtain ${ \tilde { M } } ( X ) = M$

Proof. In the case $M = R$ , these are exactly the statements of Lemma 12.18 and Proposition 12.20. For an arbitrary module $M$ the proofs can be copied literally since we never had to multiply numerators in the fractions that define the sections of the sheaf. 

The following example shows that, unfortunately, not every sheaf of modules on an affine scheme Spec $R$ is associated to an $R$ -module, so that we have to define this as an additional property. It is a rather strange construction however that will usually not occur in applications.

Example 14.3. For the ring $R = K [ x ] _ { \langle x \rangle }$ , the affine scheme $X = { \mathrm { S p e c } } R$ describes $\mathbb { A } ^ { 1 }$ locally around the origin. It has only two points, namely $\langle x \rangle$ (corresponding to the origin) and $\langle 0 \rangle$ (the generic point of $\mathbb { A } ^ { 1 }$ ). Topologically, the only non-trivial open subset of $X$ is $U : = D ( x ) = \{ \langle 0 \rangle \}$ , with ${ \mathcal { O } } _ { X } ( U ) = R _ { x } = K [ x ] _ { \langle 0 \rangle }$ by Lemma 12.18. Hence we can completely specify a presheaf of modules $\mathcal { F }$ on $X$ by setting

$$
\begin{array} { r } { \mathcal { F } ( X ) = \mathcal { F } ( \emptyset ) = \{ 0 \} \quad \mathrm { a n d } \quad \mathcal { F } ( U ) = K [ x ] _ { \langle 0 \rangle } } \end{array}
$$

with the zero maps as restriction homomorphisms. Note that this is trivially a sheaf — simply because no open subset of $X$ has any non-trivial open cover at all.

But $\mathcal { F }$ cannot be of the form $\tilde { M }$ for an $R$ -module $M$ , since otherwise it would follow from Proposition 14.2 (b) that $M = \mathcal { F } ( X ) = \{ 0 \}$ , and thus that $\mathcal { F } = \tilde { M }$ is the zero sheaf, which is clearly not the case.

Definition 14.4 (Quasi-coherent sheaves). A sheaf of modules $\mathcal { F }$ on a scheme $X$ is called quasicoherent if there is an affine open cover $\{ U _ { i } : i \in I \}$ of $X$ such that on every $U _ { i } = \operatorname { S p e c } R _ { i }$ the restricted sheaf $\mathcal { F } | _ { U _ { i } }$ is isomorphic to the sheaf $\tilde { M _ { i } }$ associated to an $R _ { i }$ -module $M _ { i }$ .

# Remark 14.5.

(a) It can be shown that for a quasi-coherent sheaf $\mathcal { F }$ on a scheme $X$ the restriction to any affine open subset $U = { \mathrm { S p e c } } R \subset X$ is in fact of the form $\mathcal { F } | _ { U } \cong \tilde { M }$ for an $R$ -module $M$ [H, Proposition II.5.4].   
(b) There is also the notion of a coherent sheaf, which is given just as in Definition 14.4 with the additional requirement that $M _ { i }$ is a finitely generated $R _ { i }$ -module for all $i$ . We will not need this stronger condition in these notes, although it is clearly satisfied for almost all sheaves occurring in practice.

# Example 14.6.

(a) Of course, the structure sheaf ${ \mathcal { O } } _ { X }$ is quasi-coherent on any scheme $X$ , since for any open subset $U = { \mathrm { S p e c } } R \subset X$ we have $\mathcal { O } _ { X } | _ { U } \cong \tilde { R }$ .   
(b) Consequently, for any $n \in  { \mathbb { N } } _ { > 0 }$ and $d \in \mathbb { Z }$ the twisting sheaf $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ is quasi-coherent on $\mathbb { P } ^ { n }$ as it is locally isomorphic to the structure sheaf by Example 13.5 (d).

As mentioned already, the following lemma now shows that most statements about quasi-coherent sheaves can be translated immediately into commutative algebra statements about modules, and that almost all constructions that can be performed with quasi-coherent sheaves will again yield quasicoherent sheaves.

Lemma 14.7. Let $X = { \mathrm { S p e c } } R$ be an affine scheme.

(a) For any two $R$ -modules M and $N$ there is a bijection $\{ m o r p h i s m s ~ o f s h e a \nu e s ~ \tilde { M } \to \tilde { N } \} \quad \stackrel { < 1 : 1 } { \longleftrightarrow } \quad \{ R \mathrm { - } m o d u l e ~ h o m o m o r p h i s m s ~ M \to N \} .$   
(b) A sequence of $R$ -modules $0  M _ { 1 }  M _ { 2 }  M _ { 3 }  0$ is exact if and only if the corresponding sequence of associated sheaves $0 \to \tilde { M } _ { 1 } \to \tilde { M } _ { 2 } \to \tilde { M } _ { 3 } \to 0$ is exact on $X$ .   
(c) For any $R$ -modules $M$ , $N$ we have $\tilde { M } \oplus \tilde { N } = ( M \oplus N ) ^ { \sim } , \quad \tilde { M } \otimes \tilde { N } = ( M \otimes N ) ^ { \sim } , \quad a n d \quad \tilde { M } ^ { \vee } = ( M ^ { \vee } ) ^ { \sim } .$

In particular, kernels, images, quotients, direct sums, tensor products, and duals of quasi-coherent sheaves are again quasi-coherent on any scheme $X$ .

# Proof.

(a) Given a morphism $\tilde { M }  \tilde { N }$ , taking global sections gives us an $R$ -module homomorphism $M \to N$ by Proposition 14.2 (b). Conversely, an $R$ -module homomorphism $M \to N$ gives rise by localization to morphisms $M _ { P }  N _ { P }$ for all $P \in X$ , and therefore by definition determines a morphism $\tilde { M }  \tilde { N }$ of the associated sheaves. It is clear from the construction that these two operations are inverse to each other.   
(b) It is known from commutative algebra that a sequence $0  M _ { 1 }  M _ { 2 }  M _ { 3 }  0$ of $R$ -modules is exact if and only if for all $P \in { \mathrm { S p e c } } R$ the sequence of localized modules $0  ( M _ { 1 } ) _ { P }  ( M _ { 2 } ) _ { P }  ( M _ { 3 } ) _ { P }  0$ is exact [G3, Proposition 6.27]. But by Proposition 14.2 (a) this is just the sequence of stalks $0  ( \tilde { M } _ { 1 } ) _ { P }  ( \tilde { M } _ { 2 } ) _ { P }  ( \tilde { M } _ { 3 } ) _ { P }  0$ . So the statement follows immediately since by Lemma 13.21 exactness of a sequence of sheaves can be checked on the stalks.

(c) Similarly to (b), this follows from the commutative algebra fact that direct sums, tensor products, and taking duals commute with localization. More precisely, e. g. in the case of direct sums the natural isomorphisms $M _ { P } \oplus N _ { P } \cong ( M \oplus N ) _ { P }$ [G3, Corollary 6.22] for all $P \in X$ give rise to a morphism of sheaves ${ \tilde { M } } \oplus { \tilde { N } } \to ( M \oplus N ) ^ { \sim }$ , and this is in fact an isomorphism by Exercise 13.8 as it is an isomorphism on the stalks (which are precisely $M _ { P } \oplus N _ { P }$ and $( M \oplus N ) _ { P }$ , respectively). 

There is only one construction with sheaves that we have considered so far and that is not covered by Lemma 14.7: the push-forward of sheaves as in Definition 13.9. In fact, in full generality the push-forward of a quasi-coherent sheaf need not be quasi-coherent, but counterexamples are hard to construct and certainly not of any relevance to us. For simplicity, let us restrict here to the case of the push-forward along an inclusion of a closed subscheme, which is the only case that we will need and for which it is easily shown that it preserves quasi-coherence.

Lemma 14.8 (Ideal sequence). Let $i \colon Y \to X$ be the inclusion of a closed subscheme.

(a) If $\mathcal { F }$ is a quasi-coherent sheaf on $Y$ then $i _ { * } \mathcal { F }$ is quasi-coherent on $X$ . (b) There is an exact sequence

$$
0 \to \mathcal { I } _ { Y / X } \to \mathcal { O } _ { X } \to i _ { * } \mathcal { O } _ { Y } \to 0
$$

of quasi-coherent sheaves on $X$ , where the second non-trivial map is the pull-back of regular functions as in Example 13.10 (a). Its kernel $\mathcal { I } _ { Y / X }$ is called the ideal sheaf of $Y$ in $X$ .

# Proof.

(a) First assume that $X = { \mathrm { S p e c } } R$ is affine. Then $Y$ is an affine subscheme of $X$ by Construction 12.33 (b). It is thus of the form $Y = { \mathrm { S p e c } } R / J$ for an ideal $J \triangleleft R$ , with the inclusion $i \colon Y \to X$ corresponding to the quotient ring homomorphism $R \to R / J$ .

As $\mathcal { F }$ is quasi-coherent on Y , it is of the form $\tilde { M }$ for an $\left( R / J \right)$ -module $M$ . Now by Definition 13.9 the sections of $i _ { * } \mathcal { F }$ are just the same as those of $\mathcal { F }$ (on the inverse image open subset). Hence, $i _ { * } \mathcal { F }$ is again just the sheaf associated to $M$ , just considered as an $R$ -module using the map $R \to R / J$ .

In the general case, we apply this argument to every subset in an affine open cover of $X$ to see that $i _ { * } \mathcal { F }$ is quasi-coherent on $X$ .

(b) We only have to show that the pull-back morphism $\mathcal { O } _ { X } \to i _ { * } \mathcal { O } _ { Y }$ is surjective, as we then obtain an exact sequence as stated with $\mathcal { I } _ { Y / X }$ its kernel sheaf. By Lemma 13.21 this can be checked on an affine open cover, so let us assume that $X = { \mathrm { S p e c } } R$ is affine. But then as in (a) the sheaves ${ \mathcal { O } } _ { X }$ and $i _ { * } \mathcal { O } _ { Y }$ are just the sheaves associated to the $R$ -modules $R$ and $R / J$ for an ideal $J \triangleleft R$ , respectively. As the map $R \to R / J$ is clearly surjective, the statement now follows from Lemma 14.7 (b), and we see that the sequence of the lemma corresponds to the exact sequence of $R$ -modules $0 \to J \to R \to R / J \to 0$ . 

Example 14.9 (The skyscraper sequence revisited). Let $P = ( 1 { : } 0 ) \in X = \mathbb { P } ^ { 1 }$ , with inclusion map $i \colon P \to \mathbb { P } ^ { 1 }$ . Moreover, denote the standard open cover of $\mathbb { P } ^ { 1 }$ by $\{ U _ { 0 } , U _ { 1 } \}$ with $U _ { i } = \{ ( x _ { 0 } : x _ { 1 } ) : x _ { i } \neq 0 \}$ for $i = 0 , 1$ .

As $i _ { * } { \mathcal { O } } _ { P } = K _ { P }$ is the skyscraper sheaf of Example 13.10 (b), the ideal sequence of Lemma 14.8 (b) for the map $i$ is just the skyscraper sequence of Example 13.22. In particular, we see:

(a) The ideal sheaf $\mathcal { I } _ { P / \mathbb { P } ^ { 1 } }$ is isomorphic to $\mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 1 )$ . We will generalize this statement in Exercise 14.12.   
(b) The skyscraper sheaf $K _ { P }$ is quasi-coherent: On $U _ { 0 } = { \mathrm { S p e c } } K [ x _ { 1 } ]$ , the proof of Lemma 14.8 shows that it is the sheaf associated to the $K [ x _ { 1 } ]$ -module $K [ x _ { 1 } ] / \langle x _ { 1 } \rangle \cong K$ , and on $U _ { 1 }$ it is clearly the zero sheaf.

(c) The theory of quasi-coherent sheaves easily reproves the exactness of the original skyscraper sequence

$$
0 \to \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 1 ) \to \mathcal { O } _ { \mathbb { P } ^ { 1 } } \to K _ { P } \to 0
$$

on $\mathbb { P } ^ { 1 }$ : By Lemma 13.21, it suffices to check this after restricting to $U _ { 0 }$ and $U _ { 1 }$ . On $U _ { 0 }$ , the twisting sheaf $\mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 1 )$ is isomorphic to $\mathcal { O } _ { \mathbb { P } ^ { 1 } }$ by Example 13.5 (d), so the sequence corresponds by (b) to the sequence of $K [ x _ { 1 } ]$ -modules

$$
0 \longrightarrow K [ x _ { 1 } ] \stackrel { \cdot \cdot x _ { 1 } } { \longrightarrow } K [ x _ { 1 } ] \longrightarrow K [ x _ { 1 } ] / \langle x _ { 1 } \rangle \longrightarrow 0 ,
$$

which is clearly exact. On $U _ { 1 }$ (which does not contain $P$ ) the skyscraper sheaf is trivial, and hence the exactness of the sequence is just the statement of Example 13.5 (d) that $\mathcal { O } _ { X } ( - 1 ) | _ { U _ { 1 } } \cong \mathcal { O } _ { X } | _ { U _ { 1 } }$ by multiplication with $x _ { 1 }$ .

Remark 14.10 (Ideal sheaves). In general, an ideal sheaf on a scheme $X$ is a “subsheaf of ${ \mathcal { O } } _ { X }$ ”, i. e.   
a sheaf of modules $\mathcal { I }$ on $X$ together with an injective morphism ${ \mathcal { I } } \to { \mathcal { O } } _ { X }$ .   
(a) By Lemma 14.8, every closed subscheme of $X$ determines a quasi-coherent ideal sheaf on $X$ . Conversely, one can check that every quasi-coherent ideal sheaf on $X$ determines a closed subscheme of $X$ : We can cover $X$ by affine open subsets $\operatorname { S p e c } R _ { i } \subset X$ , on which the sheaf is then given by the $R _ { i }$ -modules $R _ { i } / J _ { i }$ for some ideals $J _ { i } \trianglelefteqn { R _ { i } }$ , and glue the affine schemes $\operatorname { S p e c } R _ { i } / J _ { i }$ .   
(b) Similarly, the blow-up construction of Chapter 9 can be generalized to blow up an arbitrary variety $X$ at a quasi-coherent sheaf of ideals (and hence by (a) also at a closed subscheme), as already mentioned in Construction 9.16 (c): On an affine open subvariety $U \subset X$ the sheaf is given by an ideal in $A ( U )$ , so that we can blow up this ideal and glue the resulting varieties when $U$ ranges over an open cover of $X$ .

As we have now seen that almost all our constructions will yield quasi-coherent sheaves, and that quasi-coherent sheaves are very useful for applying commutative algebra techniques, let us agree:

From now on, all sheaves on a scheme will be assumed to be quasi-coherent.

According to Lemma 14.8, push-forwards of sheaves will therefore from now on only be considered along inclusions of closed subschemes.

Exercise 14.11. Let $P = ( 1 : 0 ) \in \mathbb { P } ^ { 1 }$ , and denote as usual by $K _ { P }$ the skyscraper sheaf at $P$ . Determine all morphisms of sheaves of modules

(a) from $\mathcal { O } _ { \mathbb { P } ^ { 1 } }$ to $\mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 1 )$ ;   
(b) from $\mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 1 )$ to $K _ { P }$ ;   
(c) from $K _ { P }$ to $\mathcal { O } _ { \mathbb { P } ^ { 1 } }$ .

Exercise 14.12. Let $X \subset \mathbb { P } ^ { n }$ be an irreducible hypersurface of degree $d$ . Show that the ideal sheaf of $X$ in $\mathbb { P } ^ { n }$ is given by $\mathcal { S } _ { X / \mathbb { P } ^ { n } } \cong \mathcal { O } _ { \mathbb { P } ^ { n } } ( - d )$ .

Exercise 14.13. Find a number $d \in \mathbb { Z }$ and morphisms of sheaves $f$ and $g$ such that the sequence

$$
0 \longrightarrow \mathcal { O } _ { \mathbb { P } ^ { 1 } } \overset { f } { \longrightarrow } \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 1 ) \oplus \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 1 ) \overset { g } { \longrightarrow } \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( d ) \longrightarrow 0
$$

is exact on $\mathbb { P } ^ { 1 }$ .

There is one last fundamental construction of sheaves that we will need in these notes and that is in some sense dual to the push-forward: If $f \colon X \to Y$ is a morphism of schemes and $\mathcal { F }$ a sheaf on $Y$ , there is a notion of a pull-back sheaf $f ^ { * } { \mathcal { F } }$ on $X$ . Note that a priori this clearly looks more natural than the push-forward since sheaves describe function-like objects, and the natural operation for functions is the pull-back. In fact, the pull-back of sheaves that we are going to define now has by far much nicer properties than the push-forward, but surprisingly its construction is more difficult. We will proceed in two steps, first describing the affine situation and then gluing it to a global object on an arbitrary scheme.

Construction 14.14 (Pull-back of sheaves). Let $f \colon X \to Y$ be a morphism of schemes, and let $\mathcal { F }$ be a sheaf on Y .

Then both $M$ and $R$ are $S \mathrm { \Omega }$ -modules, and hence we can form the tensor product $M \otimes s R$ as an $R$ -module. Its associated sheaf $( M \otimes _ { S } R ) ^ { \sim }$ on $X$ is called the pull-back $f ^ { * } { \mathcal { F } }$ of $\mathcal { F }$ along $f$ .

(b) Now let $X$ and $Y$ be arbitrary. To construct a sheaf $f ^ { * } { \mathcal { F } }$ on $X$ , consider first an open subset $U$ of $X$ . Unfortunately, we cannot consider ${ \mathcal { F } } ( f ( U ) )$ as $f ( U )$ is in general not an open subset of $Y$ . The best we can do is to adapt the definition of a stalk (see Construction 3.17) and define a sheaf $f ^ { - 1 } { \mathcal { F } }$ as the sheafification of the presheaf

$U \mapsto \{ ( V , \varphi ) : V \subset Y$ open with $f ( U ) \subset V$ , and $\varphi \in { \mathcal { F } } ( V ) \} / \sim$ where $( V , \varphi ) \sim ( V ^ { \prime } , \varphi ^ { \prime } )$ if there is an open subset $W$ with $f ( U ) \subset W \subset V \cap V ^ { \prime }$ such that $\varphi | _ { W } = \varphi ^ { \prime } | _ { W }$ . Note that the stalk of this presheaf, and hence by Lemma 13.17 (a) also of $f ^ { - 1 } { \mathcal { F } }$ , at a point $P \in X$ is just $\mathcal { F } _ { f ( P ) }$ as expected.

This is not yet the desired sheaf however, as $f ^ { - 1 } { \mathcal { F } }$ is still made up from sections of $\mathcal { F }$ on open subsets of $Y$ , and thus there is no way to multiply them with regular functions on (open subsets of) $X$ . In other words, $f ^ { - 1 } { \mathcal { F } }$ is not an ${ \mathcal { O } } _ { X }$ -module. It is an $f ^ { - 1 } { \mathcal { O } } _ { Y }$ -module however, and so is ${ \mathcal { O } } _ { X }$ by pull-back of functions. Hence we can finally define

$$
f ^ { * } { \mathcal { F } } : = f ^ { - 1 } { \mathcal { F } } \otimes _ { f ^ { - 1 } \mathcal { O } _ { Y } } \mathcal { O } _ { X } ,
$$

where the tensor product again involves sheafification.

Note that in the affine setting this reduces to (a) since for $X = \operatorname { S p e c } R , Y = \operatorname { S p e c } S .$ , and $\mathcal { F } = \tilde { M }$ for an $s$ -module $M$ we have

$$
\begin{array} { r l } & { ( f ^ { * } \mathcal { F } ) _ { P } = ( f ^ { - 1 } \mathcal { F } ) _ { P } \otimes _ { ( f ^ { - 1 } \mathcal { O } _ { Y } ) _ { P } } \mathcal { O } _ { X , P } = \mathcal { F } _ { f ( P ) } \otimes _ { \mathcal { O } _ { Y , f ( P ) } } \mathcal { O } _ { X , P } \overset { ! 4 . 2 } { = } \overset { \Delta } { M } _ { f ( P ) } \otimes _ { S _ { f ( P ) } } R _ { P } } \\ & { \qquad = ( M \otimes _ { S } R ) _ { P } , } \end{array}
$$

and isomorphisms can be checked on the stalks by Exercise 13.8. In fact, for concrete (local) computations involving the pull-back sheaf $f ^ { * } { \mathcal { F } }$ we will almost always use the much simpler description of (a); part (b) is mainly needed to show that there is a globally well-defined sheaf that restricts to (a) in the affine case.

# Remark 14.15.

(a) For any morphism $f \colon X \to Y$ of schemes we have $f ^ { * } { \mathcal { O } } _ { Y } = { \mathcal { O } } _ { X }$ by definition. Moreover, the pull-back construction commutes with direct sums, i. e. we have $f ^ { * } ( { \mathcal { F } } \oplus { \mathcal { G } } ) \cong f ^ { * } { \mathcal { F } } \oplus f ^ { * } { \mathcal { G } }$ for all sheaves $\mathcal { F }$ and $\mathcal { G }$ on $Y$ .   
(b) Let $\mathcal { F }$ be a sheaf on a scheme $X$ . For a closed point $P \in X$ and the inclusion map $i \colon P \to X$ , the sheaf $i ^ { * } { \mathcal { F } }$ on $P$ has only one non-trivial space of sections $i ^ { * } { \mathcal { F } } ( P )$ , which by abuse of notation we will simply write as $i ^ { * } { \mathcal { F } }$ . The geometric meaning of this space is easiest to see in the affine picture of Construction 14.14 (a): If $X = { \mathrm { S p e c } } R$ is affine, so that $P \triangleleft R$ is a prime ideal and $\mathcal { F } = \tilde { M }$ for an $R$ -module $M$ , we have

$$
i ^ { * } \mathcal { F } = M \otimes _ { R } R / P = M / P M
$$

as a vector space over the residue field $K ( P ) = R / P$ (see Definition 12.4 (a)).

This vector space $i ^ { * } { \mathcal { F } }$ over $K ( P )$ is called the fiber of $\mathcal { F }$ at $P$ . Every section $\varphi$ of $\mathcal { F }$ over an open subset containing $P$ determines by Definition 14.1 an element $\varphi _ { P }$ in $\mathcal { F } _ { P } = M _ { P }$ , and hence by taking its quotient modulo $P M$ a value $\varphi ( P )$ in $i ^ { * } { \mathcal { F } }$ . For the structure sheaf $\mathcal { F } = \mathcal { O } _ { X }$ , this just coincides with Definition 12.4 (b) of the value of a regular function. So for an arbitrary sheaf we can still define values of sections at points — they just do not lie in the residue fields any more, but in vector spaces over them. Note however that, just as in the case of regular functions in Example 12.21 (a), these values do not necessarily determine the section.

As we now have defined a push-forward as well as a pull-back of sheaves, let us quickly study to what extent these two operations are inverse to each other. The proof of the following lemma is a good example how statements from commutative algebra can be transferred directly into the language of quasi-coherent sheaves.

Lemma 14.16 (Push-forward and pull-back of sheaves). Let $i \colon Y \to X$ be the inclusion of a closed subscheme. Then for all sheaves $\mathcal { F }$ on $Y$ and $\mathcal { G }$ on $X$ we have:

(a) $i ^ { * } i _ { * } \mathcal { F } \cong \mathcal { F }$ ; (b) (Projection formula) $i _ { * } ( \mathcal { F } \otimes i ^ { * } \mathcal { G } ) \cong ( i _ { * } \mathcal { F } ) \otimes \mathcal { G }$ . In particular, for $\mathcal { F } = \mathcal { O } _ { Y }$ we obtain $i _ { * } i ^ { * } { \mathcal { G } } \cong ( i _ { * } { \mathcal { O } } _ { Y } ) \otimes { \mathcal { G } } .$

Proof. According to Lemma 13.21 we can check these isomorphisms locally, so we may assume that $X = { \mathrm { S p e c } } R$ is affine, and consequently $Y = { \mathrm { S p e c } } R / J$ for an ideal $J \triangleleft R$ . Moreover, we have $\mathcal { F } = \tilde { M }$ for an $R / J$ -module $M$ and $\mathcal { G } = \tilde { N }$ for an $R$ -module $N$ . To prove the stated isomorphisms of quasi-coherent sheaves it then suffices by Lemma 14.7 to show that the corresponding modules are isomorphic. So recall by (the proof of) Lemma 14.8 (a) that the push-forward is given by considering an $R / J$ -module as an $R$ -module, and by Construction 14.14 (a) that the pull-back is given by the tensor product with $R$ over $R / J$ . This means:

(a) The sheaf $i ^ { * } i _ { * } \mathcal { F }$ is associated to the $R / J$ -module $M \otimes _ { R } R / J$ , which by commutative algebra is canonically isomorphic to $M$ .   
(b) We have that $i _ { * } ( \mathcal { F } \otimes i ^ { * } \mathcal { G } )$ is the sheaf associated to the $R$ -module $M \otimes _ { R / J } ( N \otimes _ { R } R / J )$ , and $( i _ { * } \mathcal { F } ) \otimes \mathcal { G }$ is the sheaf associated to the $R$ -module $M \otimes _ { R } N$ , and again it is known from commutative algebra that these two modules are naturally isomorphic. 

To conclude this chapter, let us finally introduce a class of sheaves that are even nicer than the quasi-coherent ones: those that on an affine open cover are associated to free modules.

Definition 14.17 (Locally free sheaves). A sheaf of modules $\mathcal { F }$ on a scheme $X$ is called locally free if there is an affine open cover $\{ U _ { i } : i \in I \}$ of $X$ such that on every $U _ { i } = \operatorname { S p e c } R _ { i }$ the restricted sheaf $\mathcal { F } | _ { U _ { i } }$ is isomorphic to the sheaf $\tilde { M _ { i } }$ associated to a free $R _ { i }$ -module $M _ { i }$ of finite rank (i. e. to a finite direct sum of copies of ${ \mathcal { O } } _ { U _ { i } }$ ). If this rank is the same for all $i \in I$ this number is also called the rank of $\mathcal { F }$ , denoted rk $\mathcal { F }$ .

# Remark 14.18.

(a) For a locally free sheaf $\mathcal { F }$ of rank $r$ on a scheme $X$ the fiber at any point $P \in X$ as in Remark 14.15 (b) is an $r$ -dimensional vector space over the residue field $K ( P )$ . Hence, sections of such a sheaf can be thought of as “functions that take values in a varying $r .$ -dimesional vector space”, as in our original motivation in Example 13.1 where we informally introduced the tangent sheaf in this way. For this reason, a locally free sheaf is also often called a vector bundle, resp. a line bundle if it is of rank 1.   
(b) In contrast to the case of quasi-coherent sheaves in Remark 14.5 (a), for a locally free sheaf $\mathcal { F }$ on a scheme $X$ it is in general not true on every affine open subset $U = { \mathrm { S p e c } } R$ that it is of the form $\mathcal { F } | _ { U } \cong \tilde { M }$ for a free $R$ -module $M$ . A simple example can be obtained if $X$ is the (reducible) 0-dimensional variety consisting of two points $P$ and $Q$ , with coordinate ring $R = K \times K$ by Proposition 2.7. Then the $R$ -module $M = K \times \{ 0 \}$ is clearly not free, but the sheaf $\tilde { M }$ on $X$ is locally free as it is isomorphic to the structure sheaf (resp. the zero sheaf) on the affine open subset $\{ P \}$ (resp. $\{ Q \} ,$ ) of $X$ .

# Example 14.19.

(a) The structure sheaf is a line bundle, i. e. locally free of rank 1, on any scheme $X$ . The twisting sheaves $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ of Construction 13.4 are locally isomorphic to the structure sheaf by Example 13.5 (d), and hence line bundles as well. In contrast, the skyscraper sheaf $K _ { P }$ for a point $P$ on $\mathbb { P } ^ { 1 }$ as in Example 13.10 (b) is not locally free, as its fiber at $P$ is 1-dimensional, whereas all other fibers are 0-dimensional.   
(b) For any construction in commutative algebra that preserves free modules, the corresponding operation on locally free sheaves will again yield locally free sheaves of the corresponding ranks. Hence, for example, if $\mathcal { F }$ and $\mathcal { G }$ are locally free on a scheme $X$ with rk ${ \mathcal { F } } = n$ and rk ${ \mathcal { G } } = m$ then • the direct sum $\mathcal { F } \oplus \mathcal { G }$ is locally free of rank $n + m$ ; • the tensor product $\mathcal { F } \otimes \mathcal { G }$ is locally free of rank nm; • the dual $\mathcal { F } ^ { \vee }$ is locally free of rank $n$ ; and • the pull-back $f ^ { * } { \mathcal { F } }$ for a morphism $f \colon Y \to X$ is locally free of rank $n$ .

(c) In Definition 8.6 and Proposition 8.7, we have constructed the alternating tensor product $\Lambda ^ { k } V$ for a vector space $V$ and a natural number $k \in \mathbb N$ . This construction works in the very same way for modules over a ring, so just as in Construction 13.13 and Definition 13.19 (b) we can define a $k$ -fold alternating tensor product $\Lambda ^ { k } { \mathcal { F } }$ of a sheaf $\mathcal { F }$ on a scheme $X$ as the sheaf associated to the presheaf $U \mapsto \Lambda ^ { k } ( { \mathcal { F } } ( U ) )$ .

As in Example 8.8 (a), the $k$ -fold alternating tensor product of a free module of rank $n$ is again free of rank $\binom { n } { k }$ . Hence, in the same way as in (b) the alternating tensor product $\Lambda ^ { k } { \mathcal { F } }$ of a locally free sheaf $\mathcal { F }$ of rank $n$ is locally free of rank $\binom { n } { k }$ . In particular, the highest non-trivial alternating tensor product $\Lambda ^ { n } { \mathcal { F } }$ is a line bundle.

Clearly, the twisting sheaves on projective spaces are the most important line bundles. Using the pull-back construction we can now extend their definition to arbitrary projective schemes.

Notation 14.20 (Twisting sheaves on projective schemes). Let $X$ be a closed subscheme of a projective space $\mathbb { P } ^ { n }$ (e. g. a projective variety). Then for any $d \in \mathbb { Z }$ we define the twisting sheaf ${ \mathcal { O } } _ { X } ( d )$ on $X$ by

$$
\begin{array} { r } { \mathcal { O } _ { X } ( d ) : = i ^ { * } \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) , } \end{array}
$$

where $i \colon X \to \mathbb { P } ^ { n }$ is the inclusion. By Example 14.19 (b), it is a line bundle on $X$ . Similarly to Construction 13.4, its sections are locally given by quotients $\frac { g } { f }$ with $f , g \in S ( { \cal { X } } )$ homogeneous and $\deg g - \deg f = d$ .

Finally in this chapter, let us transfer two important results from commutative algebra about free modules to the language of locally free sheaves.

Lemma 14.21 (Exact sequences and locally free sheaves). Let $0 \to { \mathcal { F } } _ { 1 } \to { \mathcal { F } } _ { 2 } \to { \mathcal { F } } _ { 3 } \to 0$ be an exact sequence of quasi-coherent sheaves on a scheme $X$ .

(a) For another quasi-coherent sheaf $\mathcal { F }$ on $X$ the sequence

$$
0 \to { \mathcal { F } } _ { 1 } \otimes { \mathcal { F } } \to { \mathcal { F } } _ { 2 } \otimes { \mathcal { F } } \to { \mathcal { F } } _ { 3 } \otimes { \mathcal { F } } \to 0
$$

is also exact on $\textit { X i f } \mathcal { F }$ is locally free or all $\mathcal { F } _ { i }$ are locally free.

(b) For any morphism $f \colon Y \to X$ of schemes the sequence

$$
0 \to f ^ { * } { \mathcal { F } } _ { 1 } \to f ^ { * } { \mathcal { F } } _ { 2 } \to f ^ { * } { \mathcal { F } } _ { 3 } \to 0
$$

is exact on $Y$ if all $\mathcal { F } _ { i }$ are locally free.

# Proof.

(a) Restricting to an open subset of $X$ we may assume that $X = { \mathrm { S p e c } } R$ is affine, $\mathcal { F } _ { i } = \tilde { M } _ { i }$ and $\mathcal { F } = \tilde { M }$ for $R$ -modules $M _ { i }$ and $M$ with $i = 1 , 2 , 3$ , and that $M$ or all $M _ { i }$ are free of finite rank.

But then the statement follows from Lemma 14.7 (b) since in this case it is known from commutative algebra that the original exact sequence $0  M _ { 1 }  M _ { 2 }  M _ { 3 }  0$ remains exact after taking the tensor product with $M$ [G3, Exercise 5.24].

(b) This time we may assume (by restricting to an open subset $U \subset X$ and then to an open subset of $f ^ { - 1 } ( U )$ in $Y$ ) that $X = { \mathrm { S p e c } } R$ and $Y = { \mathrm { S p e c } } S$ are affine, and that $\mathcal { F } _ { i } = \tilde { M } _ { i }$ for free $R$ -modules $M _ { i }$ of finite rank with $i = 1 , 2 , 3$ . As in (a), the tensor product sequence

$$
0  M _ { 1 } \otimes _ { R } S  M _ { 2 } \otimes _ { R } S  M _ { 3 } \otimes _ { R } S  0
$$

is then again exact, and by Construction 14.14 (a) this is precisely the sequence of modules corresponding to the sequence of pull-back sheaves. Hence, the statement follows again from Lemma 14.7 (b). 

Lemma 14.22. Let $0 \to { \mathcal { F } } _ { 1 } \to { \mathcal { F } } _ { 2 } \to { \mathcal { F } } _ { 3 } \to 0$ be an exact sequence of locally free sheaves of ranks n, $n + m$ , and $m$ , respectively. Then there is an isomorphism of line bundles

$$
\Lambda ^ { n } \mathcal { F } _ { 1 } \otimes \Lambda ^ { m } \mathcal { F } _ { 3 } \cong \Lambda ^ { n + m } \mathcal { F } _ { 2 } .
$$

Proof. As in the proof of the previous lemma, it suffices to show the statement for free modules. So let

$$
0 \longrightarrow M _ { 1 } \stackrel { f } { \longrightarrow } M _ { 2 } \stackrel { g } { \longrightarrow } M _ { 3 } \longrightarrow 0
$$

be an exact sequence of free modules of ranks $n , n + m$ , and $m$ , respectively, over a $\operatorname* { r i n g } R$ . We claim that there is then a natural isomorphism

$$
\begin{array} { c } { { \Lambda ^ { n } M _ { 1 } \otimes \Lambda ^ { m } M _ { 3 }  \Lambda ^ { n + m } M _ { 2 } } } \\ { { { } } } \\ { { ( x _ { 1 } \wedge \cdots \wedge x _ { n } ) \otimes ( y _ { 1 } \wedge \cdots \wedge y _ { m } ) \mapsto f ( x _ { 1 } ) \wedge \cdots \wedge f ( x _ { n } ) \wedge g ^ { - 1 } ( y _ { 1 } ) \wedge \cdots \wedge g ^ { - 1 } ( y _ { m } ) , } } \end{array}
$$

where $g ^ { - 1 } ( y _ { i } )$ means to pick any inverse image of $y _ { i }$ under $g$ . In fact, this map is well-defined, as any two inverse images will differ by an element of the form $f ( x )$ for some $x \in M _ { 1 }$ , and the alternating tensor product $f ( x _ { 1 } ) \wedge \cdots \wedge f ( x _ { n } ) \wedge f ( x )$ is zero since $\operatorname { r k } M _ { 1 } = n$ . Moreover, the map $( * )$ is an isomorphism: Both sides are isomorphic to $R$ , and if $x _ { 1 } , \ldots , x _ { n }$ and $y _ { 1 } , \ldots , y _ { m }$ are bases of $M _ { 1 }$ and $M _ { 3 }$ , respectively, then the element on the left and right hand side of $( \ast )$ is a basis of $\Lambda ^ { n } M _ { 1 } \otimes \Lambda ^ { m } M _ { 3 }$ and $\Lambda ^ { n + m } M _ { 2 }$ , respectively. 

# 15. Differentials

We have seen already in Proposition 10.11 that (formal) differentiation of functions is useful to compute the tangent spaces at the (closed) points of a variety $X$ . We now want to introduce this language of differentials in general. The idea behind this is that the various tangent spaces $T _ { P } X$ for $P \in X$ should not just be independent vector spaces at every point, but rather arise as the fibers of one globally defined tangent sheaf on $X$ , as already motivated in Example 13.1.

To construct this tangent sheaf rigorously, we will restrict to the case of varieties as we have defined the notions of tangent spaces and smoothness only in this case. In particular, there will always be a fixed algebraically closed ground field $K$ in this chapter. As the tangent sheaf that we are going to construct will be quasi-coherent, let us first define a suitable module over the coordinate ring $R$ of an affine variety. The following notion of differentials captures the formal properties that we would expect from the differentiation of functions in this case.

Definition 15.1 (Differentials). Let $R$ be a $K$ -algebra. We define $\Omega _ { R }$ to be the free $R$ -module generated by formal symbols $d f$ for all $f \in R$ , modulo the relations

• $d ( f + g ) = d f + d g$ for all $f , g \in R$ ;   
• $d ( f g ) = f d g + g d f$ for all $f , g \in R$ ;   
• $d f = 0$ for all $f \in K$ .

The elements of $\Omega _ { R }$ are called differentials of $R$ .

We can thus consider $d$ as a map that sends an element $f \in R$ to its differential $d f \in \Omega _ { R }$ . Note however that, because of the rule for the differentiation of products, this map $d \colon R  \Omega _ { R }$ is only $K$ -linear but not an $R$ -module homomorphism — although both $R$ and $\Omega _ { R }$ are $R$ -modules.

Remark 15.2 (Differentiation of regular functions on affine varieties). In Definition 15.1, we have constructed differentials in $\Omega _ { R }$ for a $K$ -algebra $R$ so that they satisfy the standard rules for the differentiation of sums, products, and constants. In fact, if we pass to quotients in a localization $R _ { P }$ at a prime ideal $P \in { \mathrm { S p e c } } R$ , the standard rule for the differentiation of quotients holds as well: In $\Omega _ { R _ { P } }$ , we have

$$
0 = d \left( \frac { 1 } { f } \cdot f \right) = \frac { 1 } { f } d f + f d \frac { 1 } { f } , \quad \mathrm { h e n c e } \quad d \left( \frac { 1 } { f } \right) = - \frac { 1 } { f ^ { 2 } } d g , \quad \mathrm { a n d \ t h u s } \quad d \left( \frac { g } { f } \right) = \frac { 1 } { f } d g - \frac { g } { f ^ { 2 } } d f
$$

for all $f \in R \backslash P$ and $g \in R$ .

This computation also shows that the differential of a quotient $\frac { g } { f }$ can be expressed as an $R _ { P }$ -linear combination of the differentials $d f$ and $d g$ of elements of $R$ , and thus that $\Omega _ { R _ { P } } \cong ( \Omega _ { R } ) _ { P }$ . In particular, it follows that on an affine variety Spec $R$ there is also a well-defined notion of differentiation of regular functions (given by elements of $R _ { P }$ for all $P \in { \mathrm { S p e c } } R$ by Definition 12.16) that yields sections of the quasi-coherent sheaf $\tilde { \Omega } _ { R }$ (given by elements of ${ \left( \Omega _ { R } \right) } _ { P }$ by Definition 14.1). Hence we could say that $d$ extends to a map of sheaves $d \colon { \mathcal { O } } _ { \operatorname { S p e c } R } \to { \tilde { \Omega } } _ { R }$ ; but note again that this is not a morphism of sheaves of modules as it does not commute with products.

In the following, we will often also use the differentiation operator $d$ in this extended version without further notice.

# Example 15.3.

(a) Let $R = K [ x _ { 1 } , \ldots , x _ { n } ]$ be the polynomial ring. By the rules of differentiation imposed in Definition 15.1 we have d f = ∑ni=1 ∂ f∂ xi d xi for all f ∈ R, so ΩR is generated by dx1, . . . , dxn as an $R$ -module. Moreover, there are no further relations among these differentials, so

$$
\Omega _ { R } = R d x _ { 1 } \oplus \cdots \oplus R d x _ { n }
$$

is in fact a free $R$ -module of rank $n$ , with basis the differentials of the coordinates.

(b) More generally, consider the coordinate ring $R = A ( X ) = K [ x _ { 1 } , \ldots , x _ { n } ] / I ( X )$ of an affine variety $X \subset \mathbb { A } ^ { n }$ . As in (a), $\Omega _ { R }$ is then still generated by $d x _ { 1 } , \ldots , d x _ { n }$ as an $R$ -module, but in addition for all $f \in I ( X )$ we have $f = 0$ in $R$ , and hence also $d f = 0$ . It suffices to impose these conditions for generators of $I ( X )$ , and thus we obtain

$$
\Omega _ { R } = R d x _ { 1 } \oplus \cdots \oplus R d x _ { n } \Big / \left. \sum _ { j = 1 } ^ { n } \frac { \partial f _ { i } } { \partial x _ { j } } d x _ { j } : i = 1 , \ldots , m \right. \quad \mathrm { f o r } \quad I ( X ) = \langle f _ { 1 } , \ldots , f _ { m } \rangle .
$$

In particular, for a (closed) point $P \in X$ , i. e. a maximal ideal $P \triangleleft R$ (so that $R / P \cong K )$ , we have

$$
\Omega _ { R } \otimes _ { R } R / P = K d x _ { 1 } \oplus \cdots \oplus K d x _ { n } \Big / \Big \langle \sum _ { j = 1 } ^ { n } \frac { \partial f _ { i } } { \partial x _ { j } } ( P ) d x _ { j } \colon i = 1 , \ldots , m \Big \rangle ,
$$

which by (the proof of) the Jacobi criterion in Proposition 10.11 is just the dual $( T _ { P } X ) ^ { \vee }$ of the tangent space $T _ { P } X$ . As motivated in the introduction to this chapter, this means in the language of Remark 14.15 (b) that we have constructed a quasi-coherent sheaf $\tilde { \Omega } _ { R }$ on $X$ whose fiber at every point $P$ is precisely the dual of the tangent space $T _ { P } X$ .

We now have to globalize this construction to a quasi-coherent sheaf on an arbitrary variety. Unfortunately, Definition 15.1 does not glue very well, so we have to give an alternative description of differentials first. Similarly to the definition of the pull-back of sheaves in Construction 14.14 (b), its only purpose for us is to show the existence of a sheaf of differentials in the general case; for actual (local) computations we will always use the module $\Omega _ { R }$ from above.

Lemma 15.4 (Alternative description of $\Omega _ { R }$ ). Let $R$ be a $K$ -algebra. We consider the map

$$
\delta \colon R \otimes _ { K } R \to R , f \otimes g \mapsto f g
$$

and set $J : = \mathrm { K e r } \delta$ . Then $J / J ^ { 2 }$ is an $R$ -module isomorphic to $\Omega _ { R }$

Proof. Note first that $R \otimes _ { K } R$ is an $R$ -algebra in two ways, by multiplication in the left and in the right factor. For both choices, $J ^ { 2 }$ is well-defined as the $R$ -submodule of $J$ generated by all products $f g$ with $f , g \in J$ . But in fact, in the quotient $J / J ^ { 2 }$ both $R$ -module structures coincide, since for all $h \in R$ and $\textstyle \sum _ { i = 1 } ^ { n } f _ { i } \otimes g _ { i } \in J$ we have

$$
\begin{array} { r l } { \displaystyle \sum _ { i = 1 } ^ { n } ( f _ { i } \otimes h g _ { i } - h f _ { i } \otimes g _ { i } ) = \displaystyle \sum _ { i = 1 } ^ { n } ( f _ { i } \otimes g _ { i } ) \cdot \underbrace { ( 1 \otimes h - h \otimes 1 ) } _ { \in J } } & { { } \in J ^ { 2 } . } \end{array}
$$

For this $R$ -module structure of $J / J ^ { 2 }$ it is now straightforward to check that the maps

$$
\begin{array} { r l } { { } } & { { J / J ^ { 2 }  \Omega _ { R } , ~ \displaystyle \sum _ { i = 1 } ^ { n } f _ { i } \otimes g _ { i } \mapsto f _ { i } d g _ { i } } } \\ { { \mathrm { a n d } ~ } } & { { \Omega _ { R }  J / J ^ { 2 } , ~ d f \mapsto 1 \otimes f - f \otimes 1 } } \end{array}
$$

are well-defined $R$ -module homomorphisms and inverse to each other.

Construction 15.5 (Cotangent sheaf). Let $X$ be a variety. By Definition 5.17 (a), the diagonal $\Delta _ { X }$ is then a closed subvariety of $X \times X$ isomorphic to $X$ . We denote by $i \colon X \cong \Delta _ { X } \to X \times X$ the inclusion, and by $\mathcal { I } : = \mathcal { I } _ { X / X \times X }$ its ideal sheaf on $X \times X$ as in Lemma 14.8.

Note that in the affine case $X = { \mathrm { S p e c } } R$ the inclusion $i$ corresponds to the ring homomorphism $\delta$ of Lemma 15.4, the ideal sheaf $\mathcal { I }$ is the sheaf associated to its kernel $J$ , and pulling back $\mathcal { I } / \mathcal { I } ^ { 2 }$ by the map $i$ considers $J / J ^ { 2 }$ as an $R$ -module. Hence, for a general variety $X$ we define the cotangent sheaf of $X$ as

$$
\Omega _ { X } : = i ^ { * } ( { \mathcal { I } } / { \mathcal { I } } ^ { 2 } ) .
$$

By construction, Lemma 15.4 then means that $\Omega _ { X }$ restricts to the sheaf $\tilde { \Omega } _ { R }$ on an affine open subset Spec $R$ of $X$ .

If $X$ is a smooth variety of pure dimension $n$ we know by Lemma 10.9 that all tangent spaces $T _ { P } X$ for $P \in X$ (and hence also all cotangent spaces $( T _ { P } X ) ^ { \vee } )$ have dimension $n$ . Hence, we would expect $\Omega _ { X }$ to be a vector bundle of rank $n$ in this case. Let us prove this now, so that we can then define the tangent bundle as its dual bundle.

Proposition 15.6. Let $X$ be a variety of pure dimension $n$ . Then $\Omega _ { X }$ is locally free of rank n if and only if X is smooth.

# Proof.

$\ " \Rightarrow \ "$ If $\Omega _ { X }$ is a vector bundle of rank $n$ then its fiber at any point $P \in X$ , i. e. by Example 15.3 (b) the cotangent space $( T _ { P } X ) ^ { \vee }$ , has dimension $n$ . By Lemma 10.9 this means that $P$ is a smooth point of $X$ .

$^ { 6 6 } { \Leftarrow }$ ” Now let us assume that $X$ is smooth, and let $P \in X$ . We may assume that $X \subset \mathbb { A } ^ { r }$ is affine, with coordinate ring $R = A ( X ) = K [ x _ { 1 } , \dots , x _ { r } ] / \langle f _ { 1 } , \dots , f _ { m } \rangle$ . As in Example 15.3 (b) we then have

$$
( T _ { P } X ) ^ { \vee } = K d x _ { 1 } \oplus \cdots \oplus K d x _ { r } \Big / \Big \langle \sum _ { j = 1 } ^ { r } \frac { \partial f _ { i } } { \partial x _ { j } } ( P ) d x _ { j } : i = 1 , \ldots , m \Big \rangle .
$$

As this vector space has dimension $n$ by assumption, the Jacobian matrix $\begin{array} { r } { J ( P ) = \big ( \frac { \partial f _ { i } } { \partial x _ { j } } ( P ) \big ) _ { i , j } } \end{array}$ at $P$ has rank $r - n$ . Without loss of generality we may assume that the submatrix of $J ( P )$ given by the last $r - n$ rows and columns has a non-zero determinant. This means that the differentials $d x _ { n + 1 } , \ldots , d x _ { r }$ in $( T _ { P } X ) ^ { \vee }$ can be expressed as a linear combination of $d x _ { 1 } , \ldots , d x _ { n }$ (and that $d x _ { 1 } , \ldots , d x _ { n }$ are a basis of $( T _ { P } X ) ^ { \vee } ,$ ).

Now let $U \subset X$ be the open neighborhood of $P$ consisting of all points $Q$ such that the submatrix of $J ( \boldsymbol { Q } )$ of the last $r - n$ rows and columns has a non-zero determinant. Then, in the same way as above, for all $Q \in U$ the differentials $d x _ { n + 1 } , \ldots , d x _ { r }$ in $( T _ { Q } X ) ^ { \vee }$ are a linear combination of $d x _ { 1 } , \ldots , d x _ { n }$ . Consequently, the differentials $d x _ { 1 } , \ldots , d x _ { n }$ then generate $( T _ { Q } X ) ^ { \vee }$ , i. e. we have $\dim ( T _ { Q } X ) ^ { \vee } \leq n$ . But the opposite inequality always holds by Remark 10.2 (c), so we conclude that the differentials $d x _ { 1 } , \ldots , d x _ { n }$ actually form a basis of the cotangent space at all points $Q \in U$ . Hence

$$
\Omega _ { X } | _ { U } = \mathcal { O } _ { U } d x _ { 1 } \oplus \cdots \oplus \mathcal { O } _ { U } d x _ { n } ,
$$

i. e. $\Omega _ { X }$ is locally free.

Definition 15.7 (Tangent and canonical bundle). Let $X$ be a smooth variety of pure dimension $n$ .

(a) The tangent sheaf or tangent bundle of $X$ is defined to be $T _ { X } : = \Omega _ { X } ^ { \vee }$ ; by Example 14.19 (b) and Proposition 15.6 it is a vector bundle of rank $n$ .

(b) The canonical bundle of $X$ is the line bundle $\omega _ { X } : = \Lambda ^ { n } \Omega _ { X }$ .

The importance of the cotangent, tangent, and canonical bundle stems from the fact that these bundles are canonically defined (hence the name) for any smooth variety. This gives e. g. powerful methods to show that two varieties are not isomorphic: If, for example, we have two varieties whose cotangent bundles have different properties (say their spaces of global sections have different dimensions), then these varieties cannot be isomorphic. We will explore this idea later (see Remark 15.13 and Example 16.16), but first let us see how these bundles can actually be computed in some of the most important cases, namely for projective spaces and their hypersurfaces. In both these cases they are determined by exact sequences in terms of other bundles that we already know.

Proposition 15.8 (Euler sequence). For all $n \in  { \mathbb { N } } _ { > 0 }$ the cotangent bundle of $\mathbb { P } ^ { n }$ is determined by the exact sequence

$$
0  \Omega _ { \mathbb { P } ^ { n } }  \mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 ) ^ { n + 1 }  \mathcal { O } _ { \mathbb { P } ^ { n } }  0 ,
$$

where $\mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 ) ^ { n + 1 }$ stands for the direct sum of $_ { n + 1 }$ copies of the twisting sheaf $\mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 )$

Proof. Let us first construct the two morphisms $f \colon \Omega _ { \mathbb { P } ^ { n } } \to \mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 ) ^ { n + 1 }$ and $g \colon \mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 ) ^ { n + 1 } \to \mathcal { O } _ { \mathbb { P } ^ { n } }$ in the sequence. To motivate the definition of $f$ , consider for $i , j \in \{ 0 , \ldots , n \}$ with $i \neq j$ the regular functions $\frac { x _ { i } } { x _ { j } }$ on $U _ { j } : = \{ x \in \mathbb { P } ^ { n } : x _ { j } \neq 0 \} \subset \mathbb { P } ^ { n }$ . If $x _ { i }$ and $x _ { j }$ were regular functions themselves, we would have by Remark 15.2

$$
d \left( { \frac { x _ { i } } { x _ { j } } } \right) = { \frac { 1 } { x _ { j } } } d x _ { i } - { \frac { x _ { i } } { x _ { j } ^ { 2 } } } d x _ { j } .
$$

But of course $x _ { i }$ and $x _ { j }$ are not well-defined functions, so it seems that this equation does not make sense since $d x _ { i }$ and $d x _ { j }$ do not exist. However, if we denote the $n + 1$ components of $\mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 ) ^ { n + 1 }$ by the formal symbols $d x _ { 0 } , \ldots , d x _ { n }$ we can use the idea of $( * )$ to define the morphism $f$ by

$$
f \colon \Omega _ { \mathbb { P } ^ { n } } \to \mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 ) ^ { n + 1 } , d \biggl ( \frac { x _ { i } } { x _ { j } } \biggr ) \mapsto \biggl ( 0 , \ldots , 0 , \underbrace { \frac { 1 } { x _ { j } } } _ { \mathrm { c o m p o n e n t } i } , 0 , \ldots , 0 , \underbrace { - \frac { x _ { i } } { x _ { j } ^ { 2 } } } _ { \mathrm { c o m p o n e n t } j } , 0 , \ldots , 0 \biggr ) .
$$

In fact, as $\begin{array} { r } { d \big ( \frac { x _ { i } } { x _ { j } } \big ) } \end{array}$ for $i = 0 , \ldots , n$ with $i \neq j$ generate $\Omega _ { X } | _ { U _ { j } }$ by Example 15.3 (a) this completely determines a morphism ofit is well-defined, i. e. that $\begin{array} { r } { d \bigl ( \frac { x _ { i } } { x _ { k } } \bigr ) = d \bigl ( \frac { x _ { i } } { x _ { j } } \cdot \frac { x _ { j } } { x _ { k } } \bigr ) } \end{array}$ s, anand $\begin{array} { r } { \frac { x _ { i } } { x _ { j } } d \bigl ( \frac { x _ { j } } { x _ { k } } \bigr ) + \frac { x _ { j } } { x _ { k } } d \bigl ( \frac { x _ { i } } { x _ { j } } \bigr ) } \end{array}$ of differentiation ensure that map to the same element — which is easily verified directly. Finally, the morphism $g$ is simply defined by

$$
g \colon { \mathcal { O } } _ { \mathbb { P } ^ { n } } ( - 1 ) ^ { n + 1 } \to { \mathcal { O } } _ { \mathbb { P } ^ { n } } , ( \varphi _ { 0 } , \ldots , \varphi _ { n } ) \mapsto \varphi _ { 0 } x _ { 0 } + \cdots + \varphi _ { n } x _ { n } .
$$

It is now just straightforward commutative algebra to check that the sequence of the proposition is exact: By Lemma 13.21 we can do this on each $U _ { j }$ , so without loss of generality on $U _ { 0 }$ , where $x _ { 1 } , \ldots , x _ { n }$ are affine coordinates and $x _ { 0 } = 1$ . By the above definition of the morphisms we have $f ( d x _ { i } ) = d x _ { i } - x _ { i } d x _ { 0 }$ in these coordinates, and hence the matrices over $K [ x _ { 1 } , \ldots , x _ { n } ]$ corresponding by Lemma 14.7 to $f$ and $g$ are

$$
A = \left( \begin{array} { c c c } { { - x _ { 1 } } } & { { \cdots } } & { { - x _ { n } } } \\ { { 1 } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { 1 } } \end{array} \right) \quad \mathrm { a n d } \quad B = \left( 1 \begin{array} { c c c } { { } } & { { x _ { 1 } } } & { { \cdots } } & { { x _ { n } } } \end{array} \right) ,
$$

respectively. But for these matrices it is checked immediately that $\operatorname { K e r } A = \{ 0 \}$ , $\operatorname { I m } A = \operatorname { K e r } B$ , and $\mathrm { I m } { \cal B } = { \cal K } [ x _ { 1 } , \dots , x _ { n } ]$ . 

Remark 15.9. Dualizing the Euler sequence of Proposition 15.8 (and noting by Exercise 13.25 that $\mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 ) ^ { \vee } \cong \mathcal { O } _ { \mathbb { P } ^ { n } } ( 1 ) )$ , we obtain the exact sequence

$$
0 \to \mathcal { O } _ { \mathbb { P } ^ { n } } \to \mathcal { O } _ { \mathbb { P } ^ { n } } ( 1 ) ^ { n + 1 } \to T _ { \mathbb { P } ^ { n } } \to 0
$$

that determines the tangent bundle of $\mathbb { P } ^ { n }$ . The canonical bundle of $\mathbb P ^ { n }$ can also be computed from the Euler sequence: As exact sequences (and hence direct sums) are taken by Lemma 14.22 to tensor products when taking highest alternating powers, we obtain

$$
\omega _ { \mathbb { P } ^ { n } } \cong \Lambda ^ { n + 1 } ( \mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 ) ^ { n + 1 } ) \stackrel { \scriptscriptstyle 1 3 . 2 3 } { \cong } \mathcal { O } _ { \mathbb { P } ^ { n } } ( - n - 1 ) .
$$

Proposition 15.10 (Conormal sequence). Let $X$ be a hypersurface of degree d in $\mathbb P ^ { n }$ over a field of characteristic 0. Then the cotangent sheaf of $X$ is given by the exact sequence

$$
0  \mathcal { O } _ { X } ( - d )  i ^ { * } \Omega _ { \mathbb { P } ^ { n } }  \Omega _ { X }  0
$$

on $X$ , where $\mathcal { O } _ { X } ( - d )$ is as in Notation $I 4 . 2 0$ and $i \colon X \to \mathbb { P } ^ { n }$ denotes the inclusion.

Proof. Let $I ( X ) = \langle f \rangle$ for a homogeneous polynomial $f$ of degree $d$ . The two maps in the sequence are

$$
{ \mathcal O } _ { X } ( - d ) \to i ^ { * } \Omega _ { \mathbb { P } ^ { n } } , \varphi \mapsto d ( f \varphi ) \quad \mathrm { a n d } \quad i ^ { * } \Omega _ { \mathbb { P } ^ { n } } \to \Omega _ { X } , d \varphi \mapsto d ( \varphi | _ { X } ) .
$$

Note that the first map is well-defined as $f \varphi$ is a regular function if $\varphi$ is a section of $\mathcal { O } _ { X } ( - d )$ . We will show on an affine open cover that it is actually a morphism of sheaves of modules, and that the sequence is exact. Without loss of generality, it suffices to check this on $U _ { 0 } = \{ x \in \mathbb { P } ^ { n } : x _ { 0 } \neq 0 \}$ , where we set $x _ { 0 } = 1$ and use $x _ { 1 } , \ldots , x _ { n }$ as affine coordinates.

Note that $X \cap U _ { 0 }$ is just the zero locus of the dehomogenization $f ^ { \mathrm { i } }$ on this open set. We set $R = K [ x _ { 1 } , \ldots , x _ { n } ]$ and $S = R / \langle f ^ { \mathrm { i } } \rangle$ . By the description of the pull-back and the cotangent sheaf in Construction 14.14 and Example 15.3, respectively, the sequence of $S _ { \mathbf { \Omega } }$ -modules corresponding to the given sequence of sheaves on $U _ { 0 }$ is

$$
0  S  ( R d x _ { 1 } \oplus \cdots \oplus R d x _ { n } ) \otimes _ { R } S  ( S d x _ { 1 } \oplus \cdots \oplus S d x _ { n } ) / \langle d f ^ { \mathbf i } \rangle  0 ,
$$

or in other words

$$
0  S  S d x _ { 1 } \oplus \cdots \oplus S d x _ { n }  ( S d x _ { 1 } \oplus \cdots \oplus S d x _ { n } ) / \langle d f ^ { \mathrm { i } } \rangle  0 ,
$$

where the second non-trivial map is just the quotient, and the first is given by

$$
\varphi \mapsto d ( f ^ { \mathrm { i } } \varphi ) = \underbrace { f ^ { \mathrm { i } } } _ { \mathrm { ~ = ~ 0 ~ i n ~ } S } d \varphi + \varphi d f ^ { \mathrm { i } } = \varphi d f ^ { \mathrm { i } } .
$$

Hence, this first map is the $s$ -module homomorphism that is just multiplication with $d f ^ { \mathrm { i } }$ . We therefore just have to prove its injectivity to see that the sequence $( \ast )$ is exact. So assume that we have an element $\varphi \in S$ with

$$
\varphi d f ^ { \mathrm { i } } = \varphi { \frac { \partial f ^ { \mathrm { i } } } { \partial x _ { 1 } } } d x _ { 1 } + \cdots + \varphi { \frac { \partial f ^ { \mathrm { i } } } { \partial x _ { n } } } d x _ { n } { \stackrel { ! } { = } } 0 \quad \in S d x _ { 1 } \oplus \cdots \oplus S d x _ { n } ,
$$

i. e. that $\begin{array} { r } { \varphi \frac { \partial f ^ { \mathrm { i } } } { \partial x _ { k } } \in \langle f ^ { \mathrm { i } } \rangle } \end{array}$ for all $k = 1 , \ldots , n$ . As char $K = 0$ , at least one of these partial derivatives $\frac { \partial f ^ { \mathrm { i } } } { \partial x _ { k } }$ must be non-zero. Moreover, $f ^ { \mathrm { i } }$ generates a radical ideal and hence has no repeated factors, and thus by the rules of differentiation $\frac { \partial f ^ { \mathrm { i } } } { \partial x _ { k } }$ and f i are coprime. Hence, ϕ ∂ f i∂ xk $\begin{array} { r } { \varphi \frac { \partial f ^ { \mathrm { i } } } { \partial x _ { k } } \in \langle f ^ { \mathrm { i } } \rangle } \end{array}$ requires $\varphi \in \langle f ^ { \mathrm { i } } \rangle$ , i. e. $\varphi = 0 \in S$ . This proves the injectivity of the first map in $( * )$ , and thus that this sequence is exact. 

Remark 15.11. If $X$ is a smooth hypersurface in $\mathbb P ^ { n }$ we can dualize the conormal sequence and use Lemma 14.22 to compute the tangent and canonical bundle of $X$ : We have the exact normal sequence

$$
0 \to T _ { X } \to i ^ { * } T _ { \mathbb { P } ^ { n } } \to \mathcal { O } _ { X } ( d ) \to 0 ,
$$

and

$$
\omega _ { X } = i ^ { * } \omega _ { \mathbb { P } ^ { n } } \otimes \mathcal { O } _ { X } ( d ) \overset { \overset { } { \underbrace { 1 5 . 9 } } } { = } \mathcal { O } _ { X } ( d - n - 1 ) .
$$

Note that the normal sequence means that the fibers of the line bundle ${ \mathcal { O } } _ { X } ( d )$ at a point $P \in X$ can be identified with the quotient $T _ { P } \mathbb { P } ^ { n } / T _ { P } X$ , i. e. with the space of normal directions in $\mathbb { P } ^ { n }$ relative to $X$ . This explains the name “normal sequence” resp. “conormal sequence” for the statement of Proposition 15.10; the line bundle $\mathcal { O } _ { X } ( d )$ is also called the normal bundle of $X$ in $\mathbb P ^ { n }$ .

# Example 15.12.

(a) By Remark 15.9, we have

$$
\Omega _ { \mathbb { P } ^ { 1 } } = \omega _ { \mathbb { P } ^ { 1 } } \cong \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 2 ) , \quad \mathrm { a n d ~ h e n c e } \quad T _ { \mathbb { P } ^ { 1 } } = \Omega _ { \mathbb { P } ^ { 1 } } ^ { \vee } \cong \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 2 ) .
$$

In particular, every global section of the tangent bundle has exactly two zeros (counted with multiplicity), as we have already mentioned in Example 13.1. Over the complex numbers one can show that this is in fact a topological property: There is not even a continuous nowhere-zero tangent vector field on the real 2-dimensional unit sphere. This is usually called the “hairy ball theorem” and stated by saying that “one cannot comb a hedgehog (i. e. a ball) without a bald spot”.

(b) For a smooth curve $X$ of degree $d$ in $\mathbb { P } ^ { 2 }$ we have by Remark 15.11

$$
\Omega _ { X } = \omega _ { X } \cong { \mathcal O } _ { X } ( d - 3 ) , \quad \mathrm { a n d \ t h u s } \quad T _ { X } = \Omega _ { X } ^ { \vee } \cong { \mathcal O } _ { X } ( 3 - d ) .
$$

Hence, in this case the zeros of e. g. a global section of the canonical bundle on $X$ are the same as those of a polynomial of degree $d - 3$ . Note that this was exactly our definition of the canonical bundle (resp. divisor) in the “Plane Algebraic Curves” class [G2, Definition 8.11] — so we can see now why this is actually a canonically defined object.

A special case is clearly when $X$ is a plane cubic curve, as we then have $\Omega _ { X } \cong T _ { X } \cong \mathcal { O } _ { X }$ . Hence, on such a cubic there is a nowhere-zero tangent vector field, corresponding to the constant function 1 in ${ \mathcal { O } } _ { X }$ . Over the complex numbers, it is known that a plane cubic curve is topologically a torus [G2, Example 5.17], and this nowhere-zero tangent vector field is easy to visualize as in the picture on the right.

![](images/cb07ca16845a945646d617e4a0bb4e5fd178ebda42a4b5537da727f74cdc43f0.jpg)

Remark 15.13. Note that Example 15.12 also proves that a smooth plane cubic curve $X$ is not isomorphic to $\mathbb { P } ^ { 1 }$ , as the tangent bundles of these two varieties have different properties: $T _ { X }$ has a nowhere-zero global section, whereas this is not the case for $T _ { \mathbb { P } ^ { 1 } }$ . Alternatively, the global sections of $T _ { X } \cong { \mathcal { O } } _ { X }$ form a 1-dimensional vector space over $K$ by Corollary 7.23, whereas this space is 3- dimensional for $T _ { \mathbb { P } ^ { 1 } } \cong \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 2 )$ by Example 13.5 (a). In fact, this is one of the easiest ways to prove that these two curves are not isomorphic, although it already uses rather advanced techniques of algebraic geometry. In the next chapter we will explore in more detail how we can use properties of the (co-)tangent bundle to prove that varieties are not isomorphic.

# 16. Cohomology of Sheaves

In this final chapter of these notes we want to give a short introduction to the important concept of cohomology of sheaves. There are two main motivations for this:

Remark 16.1 (Motivation for sheaf cohomology).

(a) For a short exact sequence $0 \to { \mathcal { F } } _ { 1 } \to { \mathcal { F } } _ { 2 } \to { \mathcal { F } } _ { 3 } \to 0$ of sheaves on a scheme $X$ we have seen already in Exercise 13.26 (b) that taking global sections gives an exact sequence of groups

$$
0 \to { \mathcal { F } } _ { 1 } ( X ) \to { \mathcal { F } } _ { 2 } ( X ) \to { \mathcal { F } } _ { 3 } ( X ) .
$$

However, Example 13.22 (b) showed us that the last map in this sequence is in general not surjective, so that we cannot obtain much information about ${ \mathcal { F } } _ { 3 } ( X )$ from this. Cohomology gives a natural way to extend this sequence to the right: We will construct naturally defined cohomology groups $H ^ { p } ( X , { \mathcal { F } } )$ for any sheaf $\mathcal { F }$ on $X$ and $p \in \mathbb N$ such that there is a long exact sequence

$$
\begin{array} { r l } & { 0 \to { \mathcal { F } } _ { 1 } ( X ) \to { \mathcal { F } } _ { 2 } ( X ) \to { \mathcal { F } } _ { 3 } ( X ) } \\ & { \quad \to H ^ { 1 } ( X , { \mathcal { F } } _ { 1 } ) \to H ^ { 1 } ( X , { \mathcal { F } } _ { 2 } ) \to H ^ { 1 } ( X , { \mathcal { F } } _ { 3 } ) } \\ & { \quad \to H ^ { 2 } ( X , { \mathcal { F } } _ { 1 } ) \to \cdots . } \end{array}
$$

Quite often, there are explicit ways to compute these groups — and in fact they turn out to be zero in many cases, so that this a priori infinitely long exact sequence will usually break up into small and easily tractable pieces.

(b) If $X$ is a variety over $K$ , the cohomology groups $H ^ { p } ( X , { \mathcal { F } } )$ for a sheaf $\mathcal { F }$ on $X$ will actually be $K$ -vector spaces. Hence, applying this to canonically defined sheaves such as ${ \mathcal { O } } _ { X } , \Omega _ { X }$ , $T _ { X }$ , or $\omega _ { X }$ (see Chapter 15), their dimensions are numbers attached intrinsically to $X$ , so that (as in Remark 15.13) they can be used to prove that varieties are not isomorphic.

The cohomology of sheaves is a very general concept. It can not only be defined for sheaves of modules on a scheme, but even for an arbitrary sheaf of Abelian groups on a topological space, and consequently it plays a big role in topology as well. Nevertheless, in order to avoid technicalities we will restrict to the case of quasi-coherent sheaves on varieties in these notes. In this case, the main idea for the construction of cohomology lies in Lemma 14.7 (b): If $X = { \mathrm { S p e c } } R$ is an affine variety and $0 \to { \mathcal { F } } _ { 1 } \to { \mathcal { F } } _ { 2 } \to { \mathcal { F } } _ { 3 } \to 0$ an exact sequence of quasi-coherent sheaves with $\mathcal { F } _ { i } = \tilde { M } _ { i }$ for $R$ - modules $M _ { i }$ for $i \in \{ 1 , 2 , 3 \}$ , this means that the corresponding sequence $0  M _ { 1 }  M _ { 2 }  M _ { 3 }  0$ is exact, which by Proposition 14.2 (b) is just the sequence

$$
0 \to { \mathcal { F } } _ { 1 } ( X ) \to { \mathcal { F } } _ { 2 } ( X ) \to { \mathcal { F } } _ { 3 } ( X ) \to 0
$$

of global sections. Hence, the problem of Remark 16.1 (a) of the sequence of global sections not being exact goes away in the affine case; it just arises from the gluing of affine patches. Consequently, in order to construct the cohomology of sheaves we will consider their sections on an affine open cover and study their gluing behavior. This is formalized by the following definition.

Definition 16.2. Let $\mathcal { F }$ be a sheaf on a variety $X$ , and fix an affine open cover $U _ { 1 } , \dots , U _ { r }$ of $X$

(a) For all $p \in \mathbb N$ we define the $K$ -vector space

$$
C ^ { p } ( \mathcal { F } ) = \bigoplus _ { i _ { 0 } < \cdots < i _ { p } } \mathcal { F } ( U _ { i _ { 0 } } \cap \cdots \cap U _ { i _ { p } } ) .
$$

Hence, an element $\varphi \in C ^ { p } ( { \mathcal { F } } )$ is just a collection of sections $\varphi _ { i _ { 0 } , \dots , i _ { p } } \in { \mathcal { F } } ( U _ { i _ { 0 } } \cap \cdots \cap U _ { i _ { p } } )$ for all intersections of $p + 1$ sets taken from the chosen affine open cover. These sections can be completely unrelated.

(b) For every $p \in \mathbb N$ we define a linear so-called boundary map $d ^ { p } \colon C ^ { p } ( { \mathcal { F } } ) \to C ^ { p + 1 } ( { \mathcal { F } } )$ by

$$
( d ^ { p } \varphi ) _ { i _ { 0 } , . . . , i _ { p + 1 } } = \sum _ { k = 0 } ^ { p + 1 } ( - 1 ) ^ { k } \varphi _ { i _ { 0 } , . . . , i _ { k } , . . . , i _ { p + 1 } } | _ { U _ { i _ { 0 } } \cap \cdots \cap U _ { i _ { p + 1 } } } ,
$$

where the notation $\hat { i _ { k } }$ means that the index $i _ { k }$ is to be left out. Note that this makes sense as $\varphi _ { i _ { 0 } , \dots , i _ { k } , \dots , i _ { p + 1 } }$ is a section of $\mathcal { F }$ on $U _ { i _ { 0 } } \cap \cdots \cap \widehat { U _ { i _ { k } } } \cap \cdots \cap U _ { i _ { p + 1 } }$ , which contains $U _ { i _ { 0 } } \cap \cdots \cap U _ { i _ { p + 1 } }$ as an open subset for all $k$ .

Lemma 16.3. For any sheaf $\mathcal { F }$ on a variety $X$ , the composition $d ^ { p + 1 } \circ d ^ { p } \colon C ^ { p } ( { \mathcal { F } } ) \to C ^ { p + 2 } ( { \mathcal { F } } )$ is the zero map for all $p \in \mathbb N$ .

Proof. This statement holds because of the sign in the definition of the boundary map: Omitting for simplicity the restriction maps in the notation, we have for every $\varphi \in C ^ { p } ( { \mathcal { F } } )$

$$
\begin{array} { l } { { ( d ^ { p + 1 } ( d ^ { p } \varphi ) ) _ { i _ { 0 } , \dots , i _ { p + 2 } } = \displaystyle \sum _ { k = 0 } ^ { p + 2 } ( - 1 ) ^ { k } ( d ^ { p } \varphi ) _ { i _ { 0 } , \dots , i _ { k } , \dots , i _ { p + 2 } } } } \\ { { \mathrm { } \qquad = \displaystyle \sum _ { k = 0 } ^ { p + 2 } \sum _ { l = 0 } ^ { k - 1 } ( - 1 ) ^ { k + l } \varphi _ { i _ { 0 } , \dots , i _ { l } , \dots , i _ { k } , \dots , i _ { p + 2 } } + \sum _ { k = 0 } ^ { p + 2 } \sum _ { l = k + 1 } ^ { p + 2 } ( - 1 ) ^ { k + l - 1 } \varphi _ { i _ { 0 } , \dots , i _ { k } , \dots , i _ { l } , \dots , i _ { p + 2 } } } } \\ { { \mathrm { } = 0 , \qquad } } \end{array}
$$

where the exponent $l - 1$ in the second sum of $( \ast )$ is due to the fact that the index $i _ { l }$ is at position $l - 1$ as $i _ { k }$ has already been left out. Hence, the two sums in $( * )$ cancel each other since the second one is exactly the negative of the first. 

Remark 16.4 (Complexes of vector spaces). Lemma 16.3 means that for any sheaf $\mathcal { F }$ on a variety $X$ we have constructed a sequence of vector spaces and linear maps

$$
C ^ { 0 } ( { \mathcal { F } } ) { \overset { d ^ { 0 } } { \longrightarrow } } C ^ { 1 } ( { \mathcal { F } } ) { \overset { d ^ { 1 } } { \longrightarrow } } C ^ { 2 } ( { \mathcal { F } } ) { \overset { d ^ { 2 } } { \longrightarrow } } \cdots
$$

such that the composition of any two subsequent maps is zero. This is usually called a complex of vector spaces. Note that this sequence is in general not exact, as we only have an inclusion $\mathrm { I m } d ^ { p } \subset \mathrm { K e r } d ^ { p + 1 }$ for all $p$ , which might not be an equality. However, this inclusion allows us to form the quotient spaces $\mathrm { K e r } d ^ { p + 1 } / \mathrm { I m } d ^ { p }$ that measure “by how much the sequence fails to be exact”:

Definition 16.5 (Cohomology). Let $\mathcal { F }$ be a sheaf on a variety $X$ , and let $p \in \mathbb N$ .

(a) With the notations of Definition 16.2, we define the $p$ -th cohomology of $\mathcal { F }$ to be

$$
H ^ { p } ( X , { \mathcal { F } } ) : = \mathrm { K e r } d ^ { p } / \mathrm { I m } d ^ { p - 1 }
$$

(with the convention that $C ^ { - 1 } ( \mathcal { F } )$ and $d ^ { - 1 }$ are zero, so that $H ^ { 0 } ( X , { \mathcal { F } } ) = \operatorname { K e r } d ^ { 0 } )$ .

(b) The dimension of $H ^ { p } ( X , { \mathcal { F } } )$ as a $K$ -vector space is denoted by $h ^ { p } ( X , { \mathcal { F } } )$ .

Remark 16.6 (Independence of the affine cover). As we have constructed it, we had to pick an affine open cover of a variety $X$ in order to define the cohomology of a sheaf $\mathcal { F }$ on $X$ . It is a crucial and non-trivial fact that up to isomorphism the resulting spaces $H ^ { p } ( X , { \mathcal { F } } )$ actually do not depend on this choice — as we have already indicated by the notation.

In fact, it is the main disadvantage of our construction that this independence is not obvious from the definition. There are other approaches to cohomology (e. g. the “derived functor approach” of [H, Chapter III]) that never use affine open covers and therefore do not have this problem, but that on the other hand are essentially useless for actual computations. We will therefore continue to use our construction above, assume the independence of the chosen affine cover for granted, and just refer to [H, Theorem III.4.5] for a proof.

We will start with a few simple cases in which the cohomology of sheaves can be obtained immediately from the definition.

Lemma 16.7 (First properties of cohomology). Let $\mathcal { F }$ be a sheaf on a variety $X$

(a) We have $H ^ { 0 } ( X , { \mathcal { F } } ) \cong { \mathcal { F } } ( X )$ .   
(b) If X is affine then $H ^ { p } ( X , { \mathcal { F } } ) = \{ 0 \}$ for all $p > 0$ .   
(c) If $X$ is projective of dimension n then $H ^ { p } ( X , { \mathcal { F } } ) = \{ 0 \}$ for all $p > n$ .   
(d) I $f i \colon X \to Y$ is the inclusion of $X$ as a closed subvariety in $Y$ then $H ^ { p } ( Y , i _ { * } { \mathcal { F } } ) = H ^ { p } ( X , { \mathcal { F } } )$ for all $p \in \mathbb N$ .

# Proof.

(a) By definition, we have $H ^ { 0 } ( X , { \mathcal { F } } ) = \operatorname { K e r } ( d ^ { 0 } { : } C ^ { 0 } ( { \mathcal { F } } ) \to C ^ { 1 } ( { \mathcal { F } } ) )$ . But an element $\varphi \in C ^ { 0 } ( { \mathcal { F } } )$ is given by sections $\varphi _ { i } \in { \mathcal { F } } ( U _ { i } )$ for every affine open set $U _ { i }$ in the chosen cover, and the map $d ^ { 0 }$ is defined by

$$
( d ^ { 0 } \varphi ) _ { i _ { 0 } , i _ { 1 } } = ( \varphi _ { i _ { 1 } } - \varphi _ { i _ { 0 } } ) | _ { U _ { i _ { 0 } } \cap U _ { i _ { 1 } } }
$$

for all $i _ { 0 } < i _ { 1 }$ . By the sheaf axiom this is zero for all $i _ { 0 }$ and $i _ { 1 }$ if and only if the $\varphi _ { i }$ come from a global section of $\mathcal { F }$ , so we conclude that $H ^ { 0 } ( X , { \mathcal { F } } ) \cong { \mathcal { F } } ( X )$ .

(b) Pick the affine open cover consisting of the single set $X$ . Then $C ^ { p } ( \mathcal { F } ) = \{ 0 \}$ for all $p > 0$ as there is no way to pick $p + 1$ subsets from the cover, and hence $H ^ { p } ( X , { \mathcal { F } } ) = \{ 0 \}$ .

(c) By Proposition 2.28 (c) we can recursively pick non-constant homogeneous polynomials $f _ { 0 } , \ldots , f _ { n }$ such that $\dim ( X \cap V ( f _ { 0 } , . . . , f _ { i } ) ) < n - i$ for all $i = 0 , \ldots , n$ . In particular, this means that $X \cap V ( f _ { 0 } , . . . , f _ { n } ) = \emptyset$ , so that $X$ is covered by the $n + 1$ open complements of $V ( f _ { i } )$ . But these open subsets are affine by Corollary 7.28, so we can choose them as the affine open cover for the construction of cohomology. As this cover has only $n + 1$ subsets, we then have $C ^ { p } ( \mathcal { F } ) = \{ 0 \}$ and hence $H ^ { p } ( X , { \mathcal { F } } ) = \{ 0 \}$ for all $p > n$ .

(d) Let $U _ { 1 } , \dots , U _ { r }$ be an affine open cover of Y . Then $X \cap U _ { 1 } , \ldots , X \cap U _ { r }$ is an affine open cover of $X$ , and with respect to these covers we have

$$
C ^ { p } ( i _ { * } \mathcal { F } ) = \bigoplus _ { i _ { 0 } < \cdots < i _ { p } } i _ { * } \mathcal { F } ( U _ { i _ { 0 } } \cap \cdots \cap U _ { i _ { p } } ) = \bigoplus _ { i _ { 0 } < \cdots < i _ { p } } \mathcal { F } ( X \cap U _ { i _ { 0 } } \cap \cdots \cap U _ { i _ { p } } ) = C ^ { p } ( \mathcal { F } )
$$

for all $p \in \mathbb N$ . As the boundary maps for these two complexes agree as well, we conclude that $H ^ { p } ( Y , i _ { * } { \mathcal { F } } ) = H ^ { p } ( X , { \mathcal { F } } )$ . 

As already mentioned in the introduction to this chapter, the most important tool for both computing and using cohomology is the long exact cohomology sequence arising from a short exact sequence of sheaves. It follows from a basic principle of commutative resp. homological algebra called the Snake Lemma.

Proposition 16.8 (Long exact cohomology sequence). Let $0 \to { \mathcal { F } } _ { 1 } \to { \mathcal { F } } _ { 2 } \to { \mathcal { F } } _ { 3 } \to 0$ be an exact sequence of sheaves on a variety $X$ . Then there is a long exact sequence of vector spaces

$$
{ \begin{array} { r l } & { 0 \to H ^ { 0 } ( X , { \mathcal { F } } _ { 1 } ) \to H ^ { 0 } ( X , { \mathcal { F } } _ { 2 } ) \to H ^ { 0 } ( X , { \mathcal { F } } _ { 3 } ) } \\ & { \quad \to H ^ { 1 } ( X , { \mathcal { F } } _ { 1 } ) \to H ^ { 1 } ( X , { \mathcal { F } } _ { 2 } ) \to H ^ { 1 } ( X , { \mathcal { F } } _ { 3 } ) } \\ & { \quad \to H ^ { 2 } ( X , { \mathcal { F } } _ { 1 } ) \to \cdots . } \end{array} }
$$

Proof. Consider the commutative diagram of linear maps

$$
\begin{array} { c c c c c c c c } { { 0 } } & { { \longrightarrow } } & { { C ^ { p } ( { \mathcal F } _ { 1 } ) } } & { { \longrightarrow } } & { { C ^ { p } ( { \mathcal F } _ { 2 } ) } } & { { \longrightarrow } } & { { C ^ { p } ( { \mathcal F } _ { 3 } ) } } & { { \longrightarrow } } & { { 0 } } \\ { { } } & { { } } & { { } } & { { \Big \downarrow { d } _ { 1 } ^ { p } } } & { { } } & { { \Big \downarrow { d } _ { 2 } ^ { p } } } & { { } } & { { \Big \downarrow { d } _ { 3 } ^ { p } } } & { { } } & { { } } \end{array}
$$

$$
0 \longrightarrow C ^ { p + 1 } ( { \mathcal { F } } _ { 1 } ) \longrightarrow C ^ { p + 1 } ( { \mathcal { F } } _ { 2 } ) \longrightarrow C ^ { p + 1 } ( { \mathcal { F } } _ { 3 } ) \longrightarrow 0 ,
$$

where the horizontal maps are induced by the given morphisms of sheaves. We claim that its rows are exact: By Exercise 5.22 (a), every intersection $U = U _ { i _ { 0 } } \cap \cdots \cap U _ { i _ { p } }$ of affine open subsets from the chosen cover is again an affine variety Spec $R$ . Hence, the three quasi-coherent sheaves $\mathcal { F } _ { i }$ are associated to $R$ -modules $M _ { i }$ for $i = 1 , 2 , 3$ on this intersection, and by Lemma 14.7 (b) the corresponding sequence $0  M _ { 1 }  M _ { 2 }  M _ { 3 }  0$ is exact. But by Proposition 14.2 (b) this is just the sequence of sections $0 \to { \mathcal { F } } _ { 1 } ( U ) \to { \mathcal { F } } _ { 2 } ( U ) \to { \mathcal { F } } _ { 3 } ( U ) \to 0$ . By Definition 16.2 the rows of the above diagram are just direct products of such sequences, and hence also exact.

The Snake Lemma [G3, Lemma 4.7] now implies that there is an induced exact sequence

$$
0  \mathrm { K e r } d _ { 1 } ^ { p }  \mathrm { K e r } d _ { 2 } ^ { p }  \mathrm { K e r } d _ { 3 } ^ { p }  C ^ { p + 1 } ( { \mathcal F } _ { 1 } ) / \mathrm { I m } d _ { 1 } ^ { p }  C ^ { p + 1 } ( { \mathcal F } _ { 2 } ) / \mathrm { I m } d _ { 2 } ^ { p }  C ^ { p + 1 } ( { \mathcal F } _ { 3 } ) / \mathrm { I m } d _ { 3 } ^ { p }  0
$$

made up from the kernels and cokernels of the vertical maps in the above diagram. Using the second half (for $p \to p - 1 .$ ) and first half (for $p  p + 1 \ r ,$ ) of this sequence separately, we can make up a new commutative diagram with exact rows

$$
\begin{array} { r l } & { C ^ { p } ( \mathcal { F } _ { 1 } ) / \mathrm { I m } d _ { 1 } ^ { p - 1 } \longrightarrow C ^ { p } ( \mathcal { F } _ { 2 } ) / \mathrm { I m } d _ { 2 } ^ { p - 1 } \longrightarrow C ^ { p } ( \mathcal { F } _ { 3 } ) / \mathrm { I m } d _ { 3 } ^ { p - 1 } \longrightarrow 0 } \\ { \big \downarrow } & { \big \downarrow } \\ { 0 \longrightarrow \begin{array} { r l r } { \mathrm { K e r } d _ { 1 } ^ { p + 1 } } & { \longrightarrow \quad } & { \mathrm { K e r } d _ { 2 } ^ { p + 1 } } \end{array} } &  \longrightarrow \begin{array} { r l r } { \mathrm { K e r } d _ { 3 } ^ { p + 1 } } & { \longrightarrow 0 } & { \mathrm { K e r } d _ { 3 } ^ { p + 1 } } \\ { \downarrow } & { \longrightarrow \quad } & { \big \downarrow } \\ { \mathrm { K e r } d _ { 1 } ^ { p + 1 } } & { \longrightarrow \quad } & { \mathrm { K e r } d _ { 3 } ^ { p + 1 } } \end{array} \end{array}
$$

where the vertical maps are induced by $d _ { i } ^ { p }$ for $i = 1 , 2 , 3$ . Applying the Snake Lemma again yields an exact sequence

$$
H ^ { p } ( X , { \mathcal { F } } _ { 1 } ) \to H ^ { p } ( X , { \mathcal { F } } _ { 2 } ) \to H ^ { p } ( X , { \mathcal { F } } _ { 3 } ) \to H ^ { p + 1 } ( X , { \mathcal { F } } _ { 1 } ) \to H ^ { p + 1 } ( X , { \mathcal { F } } _ { 2 } ) \to H ^ { p + 1 } ( X , { \mathcal { F } } _ { 3 } )
$$

as the kernels and cokernels of the vertical maps in this new diagram are by definition just the cohomology spaces. The proposition is now obtained by combining these exact sequences for all $p$ . 

The most important examples of sheaves are clearly the twisting sheaves on projective spaces, so let us explicitly compute their cohomology now. Most other sheaves that we have considered so far are related to them by exact sequences, so that their cohomology can then be computed as well by Proposition 16.8.

As the cohomology $H ^ { p } ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) )$ depends on three parameters $p , n$ , and $d$ , let us apply a notational trick to simplify the computations: We will determine the cohomology of the quasi-coherent (but not coherent) sheaf $\mathcal { F } : = \oplus _ { d \in \mathbb { Z } } \mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ on $\mathbb { P } ^ { n }$ , whose sections are of the form $\textstyle { \frac { g } { f } }$ with $f , g \in K [ x _ { 0 } , \ldots , x _ { n } ]$ where $f$ (but not necessarily $g$ ) is homogeneous. Note that $\mathcal { F }$ has a natural grading by $d$ . Correspondingly, the following proposition computes its cohomology as graded vector spaces, so that we can recover from this all cohomology spaces $H ^ { p } ( \mathbb { P } ^ { n } , { \mathcal { O } } _ { \mathbb { P } ^ { n } } ( d ) )$ by taking their $d$ -th graded parts.

Proposition 16.9 (Cohomology of twisting sheaves on $\mathbb P ^ { n }$ ). Let $n \in \mathbb { N } _ { > 0 }$ , and consider the graded sheaf $\mathcal { F } : = \oplus _ { d \in \mathbb { Z } } \mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ on $\mathbb P ^ { n }$ . Then, as graded vector spaces, we have

(a) $H ^ { 0 } ( \mathbb { P } ^ { n } , { \mathcal { F } } ) \cong K [ x _ { 0 } , \dots , x _ { n } ] ,$ ; (b) $\begin{array} { r } { H ^ { n } ( \mathbb { P } ^ { n } , \mathcal { F } ) \cong \frac { 1 } { x _ { 0 } \cdots x _ { n } } K [ x _ { 0 } ^ { - 1 } , \dots , x _ { n } ^ { - 1 } ] ; } \end{array}$ (c) $H ^ { p } ( \mathbb { P } ^ { n } , \mathcal { F } ) = \{ 0 \}$ for all $p \notin \{ 0 , n \}$ .

In particular, this means that

$$
\begin{array} { r l r } { h ^ { 0 } ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) = \binom { n + d } { n } \ f o r d \ge 0 , } & { } & { h ^ { n } ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) = \binom { - d - 1 } { n } \ f o r d \le - n - 1 , } \end{array}
$$

and $h ^ { p } ( \mathbb { P } ^ { n } , { \mathcal { O } } _ { \mathbb { P } ^ { n } } ( d ) ) = 0$ for all other $p$ and $d$ .

# Proof.

(a) As $H ^ { 0 } ( \mathbb { P } ^ { n } , { \mathcal F } )$ is just the space of global sections of $\mathcal { F }$ by Lemma 16.7 (a), this statement follows immediately from Example 13.5 (a). (b) We compute this cohomology directly by definition, using the open cover by the affine spaces Ui = {x ∈ Pn : xi 6= 0} for i = 0, . . . , n. Note that F (Ui0 ∩ · · · ∩ Uip ) = K[x0, . . . , xn]xi · ··· ·xip is the vector space with basis the monomials $x _ { 0 } ^ { k _ { 0 } } \cdot \cdots x _ { n } ^ { k _ { n } }$ where $k _ { i _ { 0 } } , \ldots , k _ { i _ { p } } \in \mathbb { Z }$ and all other exponents are non-negative. The relevant vector spaces for the computation of $H ^ { n } ( \mathbb { P } ^ { n } , { \mathcal { F } } )$ are now

$$
C ^ { n } ( \mathcal { F } ) = \bigoplus _ { i } K [ x _ { 0 } , \ldots , x _ { n } ] _ { x _ { 0 } } . . . . . x _ { i } . . . . x _ { n } \quad { \mathrm { a n d } } \quad C ^ { n + 1 } ( \mathcal { F } ) = K [ x _ { 0 } , \ldots , x _ { n } ] _ { x _ { 0 } } . . . . x _ { n }
$$

(together with $C ^ { n + 2 } ( \mathcal F ) = \{ 0 \} )$ ), and hence we obtain

$$
\begin{array} { r l } & { H ^ { n } ( \mathbb { P } ^ { n } , \mathcal { F } ) = C ^ { n + 1 } / \mathrm { I m } ( d ^ { n } ; C ^ { n } ( \mathcal { F } )  C ^ { n + 1 } ( \mathcal { F } ) ) } \\ & { \qquad = \mathrm { L i n } ( x _ { 0 } ^ { k _ { 0 } } \cdot \dots \cdot x _ { n } ^ { k _ { n } } : \mathrm { a l l } ~ k _ { i } \in \mathbb { Z } ) / \mathrm { L i n } ( x _ { 0 } ^ { k _ { 0 } } \cdot \dots \cdot x _ { n } ^ { k _ { n } } : \mathrm { a t ~ l e a s t ~ o n e } ~ k _ { i } \ge 0 ) } \\ & { \qquad = \mathrm { L i n } ( x _ { 0 } ^ { k _ { 0 } } \cdot \dots \cdot x _ { n } ^ { k _ { n } } : \mathrm { a l l } ~ k _ { i } < 0 ) } \\ & { \qquad = \displaystyle \frac { 1 } { x _ { 0 } \cdot \dots \cdot x _ { n } } K [ x _ { 0 } ^ { - 1 } , \dots , x _ { n } ^ { - 1 } ] . } \end{array}
$$

(c) We prove this statement by induction on $n$ . As $H ^ { p } ( \mathbb { P } ^ { n } , \mathcal { F } ) = \{ 0 \}$ for $p > n$ by Lemma 16.7 (c) there is nothing to show for $n = 1$ . For $n > 1$ we consider the exact ideal sequence of Lemma 14.8 for the inclusion $i \colon \mathbb { P } ^ { n - 1 } \cong V ( x _ { 0 } ) \to \mathbb { P } ^ { n }$ , together with Exercise 14.12:

$$
0 \longrightarrow \mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 ) \stackrel { \cdot \cdot x _ { 0 } } { \longrightarrow } \mathcal { O } _ { \mathbb { P } ^ { n } } \longrightarrow i _ { * } \mathcal { O } _ { \mathbb { P } ^ { n - 1 } } \longrightarrow 0 .
$$

Taking the tensor product with $\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ keeps the sequence exact by Lemma 14.21 (a), as does the direct sum over the resulting sequences for all $d \in \mathbb { Z }$ . Hence we obtain the exact sequence

$$
0 \longrightarrow { \mathcal { F } } { \stackrel { \cdot x _ { 0 } } { \longrightarrow } } { \mathcal { F } } \longrightarrow i _ { * } { \mathcal { F } } \longrightarrow 0 ,
$$

where $\mathcal { F }$ in the last term denotes the corresponding sheaf on $\mathbb { P } ^ { n - 1 }$ . From the associated long exact cohomology sequence of Proposition 16.8 and the induction hypothesis we obtain the following exact sequences (using Lemma 16.7 (d) for the cohomology of $i _ { * } \mathcal { F }$ ):

$$
\begin{array} { r l } & { \begin{array} { r l } & { 0 \to H ^ { 0 } ( \mathbb { P } ^ { n } , \mathcal { F } ) \overset { x _ { 0 } } \to H ^ { 0 } ( \mathbb { P } ^ { n } , \mathcal { F } ) \to H ^ { 0 } ( \mathbb { P } ^ { n - 1 } , \mathcal { F } ) \to H ^ { 1 } ( \mathbb { P } ^ { n } , \mathcal { F } ) \overset { x _ { 0 } } \to H ^ { 1 } ( \mathbb { P } ^ { n } , \mathcal { F } ) \to 0 , } \\ & { \qquad 0 \to H ^ { p } ( \mathbb { P } ^ { n } , \mathcal { F } ) \overset { x _ { 0 } } \to H ^ { p } ( \mathbb { P } ^ { n } , \mathcal { F } ) \to 0 \quad \mathrm { f o r ~ } 1 < p < n - 1 , } \end{array} } \\ & { \begin{array} { r l } & { \qquad \cdot H ^ { n - 1 } ( \mathbb { P } ^ { n } , \mathcal { F } ) \overset { x _ { 0 } } \to H ^ { n - 1 } ( \mathbb { P } ^ { n } , \mathcal { F } ) \to H ^ { n - 1 } ( \mathbb { P } ^ { n - 1 } , \mathcal { F } ) \to H ^ { n } ( \mathbb { P } ^ { n } , \mathcal { F } ) \overset { x _ { 0 } } \to H ^ { n } ( \mathbb { P } ^ { n } , \mathcal { F } ) \to 0 , } \end{array} } \end{array}
$$

The second sequence tells us that multiplication with $x _ { 0 }$ is an isomorphism from $H ^ { p } ( \mathbb { P } ^ { n } , { \mathcal F } )$ to itself for $1 < p < n - 1$ . But the same is true for $p = 1$ as the first sequence starts by (a) with

$$
0 \to K [ x _ { 0 } , \dots , x _ { n } ] { \overset { \cdot \cdot x _ { 0 } } { \to } } K [ x _ { 0 } , \dots , x _ { n } ] \to K [ x _ { 1 } , \dots , x _ { n } ] \to \cdots ,
$$

which is obviously also exact on the right. The same analysis for the third sequence using (b) shows that multiplication with $x _ { 0 }$ is in fact an isomorphism from $H ^ { p } ( \mathbb { P } ^ { n } , { \mathcal F } )$ to itself for all $1 \leq p \leq n - 1$ .

Now on the affine open subset $U _ { 0 }$ we clearly have $H ^ { p } ( U _ { 0 } , \mathcal { F } | _ { U _ { 0 } } ) = \{ 0 \}$ for all $1 \leq p \leq n - 1$ by Lemma 16.7 (b). Algebraically, this corresponds to localization at $x _ { 0 }$ , i. e. we have

$$
H ^ { p } ( \mathbb { P } ^ { n } , { \mathcal F } ) _ { x _ { 0 } } \cong H ^ { p } ( U _ { 0 } , { \mathcal F } | _ { U _ { 0 } } ) = \{ 0 \} .
$$

So for any $\varphi \in H ^ { p } ( \mathbb { P } ^ { n } , { \mathcal { F } } )$ it follows that $x _ { 0 } ^ { k } \cdot \varphi = 0$ for some $k$ . But we have shown above that multiplication with $x _ { 0 }$ in $H ^ { p } ( \mathbb { P } ^ { n } , { \mathcal F } )$ is an isomorphism, hence $\varphi = 0$ . This means that $H ^ { p } ( \mathbb { P } ^ { n } , { \mathcal { F } } ) = 0$ as desired. 

Example 16.10 (The double skyscraper sequence revisited). Recall from Example 13.22 (b) the double skyscraper sequence

$$
0 \longrightarrow \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 2 ) \overset { \cdot \cdot _ { 0 } x _ { 1 } } { \longrightarrow } \mathcal { O } _ { \mathbb { P } ^ { 1 } } \overset { f } { \longrightarrow } K _ { P } \oplus K _ { Q } \longrightarrow 0
$$

on $\mathbb { P } ^ { 1 }$ , where $P = \left( 1 \colon 0 \right)$ and $Q = ( 0 { : } 1 )$ , and $f$ is the evaluation of a regular function at $P$ and $Q$ . We have seen already that this sequence is exact, but that $f$ is not surjective on global sections. As global sections are the same as the 0-th cohomology by Lemma 16.7 (a), Proposition 16.8 now

continues the sequence of global sections to the right, with the first terms of the resulting long exact cohomology sequence being

$$
\begin{array} { r } { 0 \to H ^ { 0 } ( { \mathbb { P } } ^ { 1 } , \mathcal { O } _ { { \mathbb { P } } ^ { 1 } } ( - 2 ) ) \to H ^ { 0 } ( { \mathbb { P } } ^ { 1 } , \mathcal { O } _ { { \mathbb { P } } ^ { 1 } } ) \to H ^ { 0 } ( { \mathbb { P } } ^ { 1 } , K _ { P } \oplus K _ { Q } ) \to H ^ { 1 } ( { \mathbb { P } } ^ { 1 } , \mathcal { O } _ { { \mathbb { P } } ^ { 1 } } ( - 2 ) ) \to H ^ { 1 } ( { \mathbb { P } } ^ { 1 } , \mathcal { O } _ { { \mathbb { P } } ^ { 1 } } ) . } \end{array}
$$

But we know all these terms already: By Proposition 16.9 (a) we have $h ^ { 0 } ( \mathbb { P } ^ { 1 } , \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 2 ) ) = 0$ and $h ^ { 0 } ( \mathbb { P } ^ { 1 } , \mathcal { O } _ { \mathbb { P } ^ { 1 } } ) = 1$ , and by Proposition 16.9 (b) we have $h ^ { 1 } ( { \mathbb P } ^ { 1 } , \mathcal { O } _ { \mathbb P ^ { 1 } } ( - 2 ) ) = 1$ and $h ^ { 1 } ( { \mathbb P } ^ { 1 } , \mathcal { O } _ { \mathbb P ^ { 1 } } ) = 0$ . Moreover, $H ^ { 0 } ( \mathbb { P } ^ { 1 } , K _ { P } \oplus K _ { Q } )$ is isomorphic to $K \oplus K$ given by specifying values at the points $P$ and $Q$ . Hence, skipping the first redundant 0, the above exact cohomology sequence becomes

$$
0 \to K \to K \oplus K \to K \to 0 .
$$

To get a better understanding of this exact sequence, we can actually also identify the morphisms in it:

• The first non-trivial morphism is just

$$
K \cong H ^ { 0 } ( \mathbb { P } ^ { 1 } , \mathcal { O } _ { \mathbb { P } ^ { 1 } } )  H ^ { 0 } ( \mathbb { P } ^ { 1 } , K _ { P } \oplus K _ { Q } ) \cong K \oplus K , a \mapsto ( a , a )
$$

as it is the evaluation of the constant function $a$ on $\mathbb { P } ^ { 1 }$ at the points $P$ and $Q$ .

• The second morphism $K \oplus K \cong H ^ { 0 } ( \mathbb { P } ^ { 1 } , K _ { P } \oplus K _ { Q } ) \to H ^ { 1 } ( \mathbb { P } ^ { 1 } , { \mathcal { O } } _ { \mathbb { P } ^ { 1 } } ( - 2 ) ) \cong K$ is the connecting homomorphism in the Snake Lemma for the diagram

$$
\begin{array} { c c c } { { 0 \longrightarrow C ^ { 0 } ( \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 2 ) ) \longrightarrow C ^ { 0 } ( \mathcal { O } _ { \mathbb { P } ^ { 1 } } ) \longrightarrow C ^ { 0 } ( K _ { P } \oplus K _ { Q } ) \longrightarrow 0 } } \\ { { \Big \downarrow } } & { { \Big \downarrow } } \end{array}
$$

$$
0 \longrightarrow C ^ { 1 } ( { \mathcal { O } } _ { \mathbb { P } ^ { 1 } } ( - 2 ) ) \longrightarrow C ^ { 1 } ( { \mathcal { O } } _ { \mathbb { P } ^ { 1 } } ) \longrightarrow C ^ { 1 } ( K _ { P } \oplus K _ { Q } ) \longrightarrow 0
$$

that we have already considered in the proof of Proposition 16.8. Hence, starting with any element $( a , b ) \in C ^ { 0 } ( K _ { P } \oplus K _ { Q } )$ representing a cohomology class in $H ^ { 0 } ( \mathbb { P } ^ { 1 } , K _ { P } \oplus K _ { Q } )$ we can firstly find an inverse image in $C ^ { 0 } ( \mathcal { O } _ { \mathbb { P } ^ { 1 } } ) = \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( U _ { 0 } ) \oplus \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( U _ { 1 } )$ (with $U _ { i } = \{ x \in \mathbb { P } ^ { 1 } : x _ { i } \neq 0 \} )$ , namely the pair of constant functions $( a , b )$ (as $P \in U _ { 0 }$ and $Q \in U _ { 1 } ,$ ). Going down in the above diagram yields the function $b - a \in C ^ { 1 } ( \mathcal { O } _ { \mathbb { P } ^ { 1 } } ) = \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( U _ { 0 } \cap U _ { 1 } )$ by the definition of the boundary map. Finally, as the morphism from $\mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 2 )$ to $\mathcal { O } _ { \mathbb { P } ^ { 1 } }$ is given by multiplication with $x _ { 0 } x _ { 1 }$ , we find that $\textstyle { \frac { b - a } { x _ { 0 } x _ { 1 } } }$ is the element in $C ^ { 1 } ( \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 2 ) ) = \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 2 ) ( U _ { 0 } \cap U _ { 1 } )$ that we were looking for. Note that $\textstyle { \frac { 1 } { x _ { 0 } x _ { 1 } } }$ is in fact a basis vector of $H ^ { 1 } ( \mathbb { P } ^ { 1 } , \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( - 2 ) )$ by Proposition 16.9 (b).

Hence, in this basis our cohomology sequence reads

$$
\begin{array} { r l r l } { 0 \to K \to K \oplus K \to } & { K } & { \to 0 } \\ { a \mapsto ( a , a ) } \\ { ( a , b ) \mapsto b - a , } \end{array}
$$

which is immediately seen to be exact.

Let us now apply the theory of cohomology of sheaves to the classification of varieties, i. e. to prove that varieties are not isomorphic. As already mentioned in Remark 16.1 (b), the idea is to consider dimensions of cohomology spaces for canonically defined sheaves such as the structure sheaf or the cotangent sheaf, as these numbers would have to be the same for isomorphic varieties. To simplify computations, it is often useful however not to consider these dimensions separately but a certain linear combination of them instead:

Construction 16.11 (Euler characteristic). Let $0 \to { \mathcal { F } } _ { 1 } \to { \mathcal { F } } _ { 2 } \to { \mathcal { F } } _ { 3 } \to 0$ be an exact sequence of sheaves on a projective variety $X$ . We have seen in Proposition 16.8 that there is then a long exact cohomology sequence

$$
{ \begin{array} { r l } & { 0 \to H ^ { 0 } ( X , { \mathcal { F } } _ { 1 } ) \to H ^ { 0 } ( X , { \mathcal { F } } _ { 2 } ) \to H ^ { 0 } ( X , { \mathcal { F } } _ { 3 } ) } \\ & { \quad \to H ^ { 1 } ( X , { \mathcal { F } } _ { 1 } ) \to H ^ { 1 } ( X , { \mathcal { F } } _ { 2 } ) \to H ^ { 1 } ( X , { \mathcal { F } } _ { 3 } ) } \\ & { \quad \to H ^ { 2 } ( X , { \mathcal { F } } _ { 1 } ) \to \cdots . } \end{array} }
$$

As we have assumed $X$ to be projective, note that this is in fact a finite sequence by Lemma 16.7 (c). Moreover, if we knew that all $H ^ { p } ( X , { \mathcal { F } } _ { i } )$ are finite-dimensional vector spaces, it is a standard commutative algebra result [G3, Corollary 4.10] that the exactness of this sequence implies

$$
h ^ { 0 } ( X , \mathcal { F } _ { 1 } ) - h ^ { 0 } ( X , \mathcal { F } _ { 2 } ) + h ^ { 0 } ( X , \mathcal { F } _ { 3 } ) - h ^ { 1 } ( X , \mathcal { F } _ { 1 } ) + h ^ { 1 } ( X , \mathcal { F } _ { 2 } ) - h ^ { 1 } ( X , \mathcal { F } _ { 3 } ) \pm \cdots = 0 .
$$

So if for any sheaf $\mathcal { F }$ on $X$ we set

$$
\chi ( X , { \mathcal { F } } ) : = \sum _ { p = 0 } ^ { \infty } ( - 1 ) ^ { p } h ^ { p } ( X , { \mathcal { F } } )
$$

(which again is actually a finite sum) it follows that

$$
\chi ( X , { \mathcal { F } } _ { 2 } ) = \chi ( X , { \mathcal { F } } _ { 1 } ) + \chi ( X , { \mathcal { F } } _ { 3 } ) .
$$

The number $\chi ( X , { \mathcal { F } } )$ is called the Euler characteristic of $\mathcal { F }$ . The fact that it is “additive on exact sequences” in the sense above makes it usually very easy to compute for a given sheaf, and thus we will see below that it often provides a good way to show that varieties are not isomorphic.

As for the finite-dimensionality of the cohomology, note that an exact sequence $( \ast )$ also implies that all vector spaces $H ^ { p } ( X , { \mathcal { F } } _ { i } )$ of a sheaf $\mathcal { F } _ { i }$ for $i \in \{ 1 , 2 , 3 \}$ are finite-dimensional if this is true for the two others. But all our examples below will be built up from exact sequences in this way starting from the twisting sheaves on projective spaces — for which we have shown their finitedimensionality already in Proposition 16.9. Actually, one can even show that every coherent sheaf on a projective variety has finite-dimensional cohomology [H, Theorem III.5.2], but we will neither need nor prove this here.

Example 16.12 (Euler characteristic of twisting sheaves on $\mathbb { P } ^ { n }$ ). If we define the binomial coefficient

$$
{ \binom { a } { n } } = { \frac { a \cdot ( a - 1 ) \cdot \cdots \cdot ( a - n + 1 ) } { n ! } }
$$

for all $a \in \mathbb { Z }$ and $n \in \mathbb { N }$ we have

$$
\chi ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) = { \binom { n + d } { n } }
$$

for all $n \in  { \mathbb { N } } _ { > 0 }$ and $d \in \mathbb { Z }$ by Proposition 16.9:

• for $d \geq 0$ we have $\begin{array} { r } { \chi ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) = h ^ { 0 } ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) = { \binom { n + d } { n } } ; } \end{array}$   
• for $d \leq - n - 1$ we have $\begin{array} { r } { \colon \chi ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) = ( - 1 ) ^ { n } h ^ { n } ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) = ( - 1 ) ^ { n } \binom { - d - 1 } { n } = \binom { n + d } { n } ; } \end{array}$ • for $- n - 1 < d < 0$ we have $\begin{array} { r } { \chi ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) = 0 = { \binom { n + d } { n } } } \end{array}$ .

Lemma 16.13 (Euler characteristic of twisting sheaves on hypersurfaces). Let $X \subset \mathbb { P } ^ { n }$ be a hypersurface of degree $d$ , and let $e \in \mathbb { Z }$ . Then

$$
\chi ( X , \mathcal { O } _ { X } ( e ) ) = { \binom { n + e } { n } } - { \binom { n + e - d } { n } } .
$$

Proof. By Lemma 14.8 (b) and Exercise 14.12 we have the exact ideal sequence

$$
0  \mathcal { O } _ { \mathbb { P } ^ { n } } ( - d )  \mathcal { O } _ { \mathbb { P } ^ { n } }  i _ { * } \mathcal { O } _ { X }  0
$$

on $\mathbb { P } ^ { n }$ , where $i \colon X \to \mathbb { P } ^ { n }$ denotes the inclusion map. The sequence remains exact by Lemma 14.21 (a) if we take the tensor product with the line bundle $\mathcal { O } _ { \mathbb { P } ^ { n } } ( e )$ . As $i _ { * } { \mathcal { O } } _ { X } \otimes { \mathcal { O } } _ { \mathbb { P } ^ { n } } ( e ) \cong i _ { * } { \mathcal { O } } _ { X } ( e )$ by the projection formula of Lemma 14.16 (b), we thus obtain the new exact sequence

$$
0 \to { \mathcal { O } } _ { \mathbb { P } ^ { n } } ( e - d ) \to { \mathcal { O } } _ { \mathbb { P } ^ { n } } ( e ) \to i _ { * } { \mathcal { O } } _ { X } ( e ) \to 0 .
$$

Using the additivity of the Euler characteristic of Construction 16.11 then yields

$$
\begin{array} { r l } { \chi ( X , \mathcal { O } _ { X } ( e ) ) } & { { } \overset { \mathrm { 1 6 . 7 } \mathrm { ( d ) } } { = } \chi ( { \mathbb P } ^ { n } , i _ { * } \mathcal { O } _ { X } ( e ) ) = \chi ( { \mathbb P } ^ { n } , \mathcal { O } _ { { \mathbb P } ^ { n } } ( e ) ) - \chi ( { \mathbb P } ^ { n } , \mathcal { O } _ { { \mathbb P } ^ { n } } ( e - d ) ) } \\ { \overset { \mathrm { 1 6 . 1 2 } } { = } } & { { } \overset { \mathrm { \rho } } { = } \binom { n + e } { n } - \binom { n + e - d } { n } , } \end{array}
$$

as we have claimed.

# Example 16.14.

(a) (Genus of a plane curve) By Lemma 16.13, the Euler characteristic of the structure sheaf of a plane curve $X \subset \mathbb { P } ^ { 2 }$ of degree $d$ is

$$
h ^ { 0 } ( X , \mathcal { O } _ { X } ) - h ^ { 1 } ( X , \mathcal { O } _ { X } ) = \chi ( X , \mathcal { O } _ { X } ) = 1 - \binom { 2 - d } { 2 } = \frac { - d ^ { 2 } + 3 d } { 2 } .
$$

But $X$ must be connected by Exercise 6.30, so we have $h ^ { 0 } ( X , { \mathcal { O } } _ { X } ) = 1$ , and thus

$$
h ^ { 1 } ( X , { \mathcal { O } } _ { X } ) = { \frac { ( d - 1 ) ( d - 2 ) } { 2 } } .
$$

This number $h ^ { 1 } ( X , { \mathcal { O } } _ { X } )$ (in fact, for any projective curve $X$ ) is called the genus of $X$ ; it is clearly invariant under isomorphisms. Note that this coincides with the definition of genus in the “Plane Algebraic Curves” class [G2, Definition 8.10], where we have also seen that over the ground field $\mathbb { C }$ the genus $g$ can be interpreted topologically as $X$ is then a “sphere with $g$ handles” [G2, Remark 5.12], e. g. a sphere for $g = 0$ as in Example 13.1 and a torus for $g = 1$ as in Example 15.12 (b).

As the genus in $( * )$ is a different number for all $d > 1$ , it follows now that plane curves of different degrees bigger than 1 can never be isomorphic. In contrast, a line (i. e. a plane curve of degree 1) and a conic (irreducible of degree 2) are always isomorphic by Example 7.5 (d), and consequently their genus 0 is the same.

(b) Note that Euler characteristics of twisting sheaves of a plane curve $X$ of degree $d$ such as

$$
\chi ( X , \mathcal { O } _ { X } ( 1 ) ) = { \binom { 3 } { 2 } } - { \binom { 3 - d } { 2 } } = \frac { - d ^ { 2 } + 5 d } { 2 }
$$

are not invariant under isomorphisms since the twisting sheaves depend on the projective embedding (which need not be preserved under isomorphisms). For example, by the above formula $\chi ( X , { \mathcal { O } } _ { X } ( 1 ) )$ is equal to 2 for a line and 3 for a conic although these curves are isomorphic.

(c) For a surface $X \subset \mathbb { P } ^ { 3 }$ of degree $d$ we have by Lemma 16.13

$$
\chi ( X , \mathcal { O } _ { X } ) = 1 - \binom { 3 - d } { 3 } ,
$$

and of course this number is again invariant under isomorphisms. But note that it is equal to 0 for all $d \in \{ 1 , 2 , 3 \}$ although these three cases look very different: For $d = 1$ we obtain $\mathbb { P } ^ { 2 }$ , the Segre embedding of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ in Example 7.10 yields a surface of degree $d = 2$ , and for $d = 3$ cubic surfaces in Chapter 11 had again very different properties. To prove rigorously that surfaces of degrees 1, 2, and 3 indeed cannot be isomorphic we need a different invariant, e. g. one obtained from the cotangent sheaf:

Corollary 16.15 (Euler characteristic of the cotangent sheaf for hypersurfaces). For any hypersurface $X$ of degree d in projective space $\mathbb { P } ^ { n }$ over a field of characteristic 0 we have

$$
\chi ( X , \Omega _ { X } ) = { \binom { n - 2 d } { n } } - ( n + 1 ) { \binom { n - d - 1 } { n } } - 1 .
$$

Proof. The Euler sequence of Proposition 15.8 is a sequence of vector bundles, so by Lemma 14.21 (b) we can pull it back along the inclusion $i \colon X \to \mathbb { P } ^ { n }$ to obtain the exact sequence

$$
0 \to i ^ { * } \Omega _ { \mathbb { P } ^ { n } } \to \mathcal { O } _ { X } ( - 1 ) ^ { n + 1 } \to \mathcal { O } _ { X } \to 0
$$

on $X$ . Moreover, there is the exact conormal sequence of Proposition 15.10

$$
0 \to \mathcal { O } _ { X } ( - d ) \to i ^ { * } \Omega _ { \mathbb { P } ^ { n } } \to \Omega _ { X } \to 0 .
$$

Combining these two sequences, we get by the additivity of the Euler characteristic

$$
\begin{array} { l } { { \chi ( X , \Omega _ { X } ) ~ = ~ \chi ( X , i ^ { * } \Omega _ { \mathbb { P } ^ { n } } ) - \chi ( X , \mathcal { O } _ { X } ( - d ) ) } } \\ { { ~ = ~ ( n + 1 ) \chi ( X , \mathcal { O } _ { X } ( - 1 ) ) - \chi ( X , \mathcal { O } _ { X } ) - \chi ( X , \mathcal { O } _ { X } ( - d ) ) } } \\ { { ~ \overset { \mathrm { 1 6 . 1 3 } } { = } \binom { n - 2 d } { n } - ( n + 1 ) \binom { n - d - 1 } { n } - 1 . } } \end{array}
$$

# Example 16.16.

(a) For a plane curve $X \subset \mathbb { P } ^ { 2 }$ of degree $d$ we have

$$
\chi ( X , \Omega _ { X } ) = \frac { d ^ { 2 } - 3 d } { 2 }
$$

by Corollary 16.15. This is again a number invariant under isomorphisms, but note that it is just the negative of the invariant $\chi ( X , { \mathcal { O } } _ { X } )$ that we have already found in Example 16.14 (a).

In fact, this is not a coincidence: It is a deep result in algebraic geometry called Serre duality that there are natural isomorphisms

$$
H ^ { p } ( X , { \mathcal { F } } ) ^ { \vee } \cong H ^ { n - p } ( X , \omega _ { X } \otimes { \mathcal { F } } ^ { \vee } ) \quad { \mathrm { f o r ~ a l l ~ } } p = 0 , \ldots , n 
$$

for any coherent sheaf $\mathcal { F }$ on an $n$ -dimensional smooth projective variety $X$ [H, Chapter III.7]. Applying this for $\mathcal { F } = \mathcal { O } _ { X }$ on a smooth plane curve we see that

$$
\chi ( X , \Omega _ { X } ) = \chi ( X , \omega _ { X } ) = h ^ { 0 } ( X , \omega _ { X } ) - h ^ { 1 } ( X , \omega _ { X } ) = h ^ { 1 } ( X , \mathcal { O } _ { X } ) - h ^ { 0 } ( X , \mathcal { O } _ { X } ) = - \chi ( X , \mathcal { O } _ { X } ) .
$$

Note that Serre duality is also visible in the cohomology of the twisting sheaves in Proposition 16.9 as $\begin{array} { r } { \omega _ { \mathbb { P } ^ { n } } = \mathcal { O } _ { \mathbb { P } ^ { n } } ( - n - 1 ) } \end{array}$ by Remark 15.9: We have

$$
h ^ { p } ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( d ) ) = h ^ { n - p } ( \mathbb { P } ^ { n } , \mathcal { O } _ { \mathbb { P } ^ { n } } ( - n - 1 - d ) )
$$

for all $p = 0 , \ldots , n$ and $d \in \mathbb { Z }$ .

(b) If $X \subset \mathbb { P } ^ { 3 }$ is a surface of degree $d$ then Corollary 16.15 shows that

$$
\chi ( X , \Omega _ { X } ) = \frac { - 2 d ^ { 3 } + 6 d ^ { 2 } - 7 d } { 3 } .
$$

It is easy to see that these are all different numbers for all $d \in \mathbb { N } _ { > 0 }$ , so we conclude that surfaces in $\mathbb { P } ^ { 3 }$ of different degrees can never be isomorphic.

# References

[AM] M. Atiyah, I. MacDonald, Introduction to Commutative Algebra, Addison Wesley (2004)   
[E] D. Eisenbud, Commutative Algebra with a View towards Algebraic Geometry, Springer (2004)   
[EGA] A. Grothendieck, J. Dieudonné, Éléments de Géométrie Algébrique, Publications Mathématiques IHES (various volumes)   
[EH] D. Eisenbud, J. Harris, The geometry of schemes, Springer Graduate Texts in Mathematics 197 (2000)   
[G1] A. Gathmann, Grundlagen der Mathematik, class notes TU Kaiserslautern (2018/19), https://www.mathematik.uni-kl.de/\~gathmann/gdm.php   
[G2] A. Gathmann, Plane Algebraic Curves, class notes TU Kaiserslautern (2018), https://www.mathematik.uni-kl.de/\~gathmann/curves.php   
[G3] A. Gathmann, Commutative Algebra, class notes TU Kaiserslautern (2014), https://www.mathematik.uni-kl.de/\~gathmann/commalg.php   
[GP] G.-M. Greuel, G. Pfister, A Singular Introduction to Commutative Algebra, Springer (2002)   
[H] R. Hartshorne, Algebraic Geometry, Springer Graduate Texts in Mathematics 52 (1977)   
[Ha] J. Harris, Algebraic Geometry, Springer Graduate Texts in Mathematics 133 (1992)   
[K] F. Kirwan, Complex Algebraic Curves, London Mathematical Society Student Texts 23, Cambridge University Press (1992)   
[M] R. Miranda, Algebraic Curves and Riemann Surfaces, AMS Graduate Studies in Mathematics 5 (1995)   
[M1] D. Mumford, The Red Book of Varieties and Schemes, Springer Lecture Notes in Mathematics 1358 (1988)   
[M2] D. Mumford, Algebraic Geometry I — Complex Projective Varieties, Springer Classics in Mathematics (1976)   
[R] M. Reid, Undergraduate Algebraic Geometry, London Mathematical Society Student Texts 12, Cambridge University Press (1988)   
[S] W. Decker, G.-M. Greuel, G. Pfister, H. Schönemann, SINGULAR — a computer algebra system for polynomial computations, https://www.singular.uni-kl.de   
[S1] I. Shafarevich, Basic Algebraic Geometry I — Varieties in Projective Space, Springer (1994)   
[S2] I. Shafarevich, Basic Algebraic Geometry II — Schemes and Complex Manifolds, Springer (1994)   
[V] R. Vakil, Foundations of Algebraic Geometry, https://math.stanford.edu/\~vakil/216blog/

Note: This is a very extensive list of literature of varying usefulness. Here is a short recommendation which of the references you might want to use for what:

• For motivational aspects, examples, and a generally “fairy-tale” style introduction without much theoretical background, see [Ha], [R], or maybe [S1] and [S2].   
• For questions concerning complex curves, in particular in relation to complex analysis, see [K] or [M].   
• For a general reference on the commutative algebra background, see [AM] or [E].   
• For commutative algebra problems involving computational aspects, see [GP].   
• For a good book that develops the theory thoroughly, but does not contain many motivations and examples, see [H]. You should not try to read the “hard-core” parts of this book without some motivational background.   
• For an easy-reading book on scheme theory containing many motivations and examples, see [EH].   
• For a (very extensive) book that starts right away with schemes instead of with varieties, see [V]. It is very readable and has excellent motivations throughout, but due to the many prerequisites on categories and sheaves developed first you will probably not consider an actual example of a variety on the first 100 pages.   
• For the ultimate reference (“if it is not proven there, it must be wrong”), see [EGA]. Warning: this is unreadable if you do not have a decent background in algebraic geometry yet, and close to unreadable even if you do.

# Index

$\mathbb { A } ^ { n } \in$   
$A ( X )$ 10   
affine conic 32   
affine coordinates 43   
affine curve 19   
affine hypersurface 19   
affine Jacobi criterion 81   
affine open set 35   
affine part 43   
affine scheme 90 associated to an affine variety 9   
affine space 6   
affine subscheme 97   
affine subvariety 10   
affine surface 19   
affine variety 6, 33 product 7, 32   
affine zero locus 6   
algebra 10 graded 44 reduced 33   
algebraic set 6   
alternating linear map 62 tensor product 62, 116   
associated sheaf 106, 110   
automorphism projective 54   
Basis Theorem 7   
birational map 69   
birational varieties 69   
blow-up at a closed subvariety 73 at an ideal 72 at polynomials 70 of a projective variety 73 of a variety 73 of an affine variety 70   
boundary map 125   
bundle canonical 120 line 115 normal 122 tangent 120 vector 115   
$C _ { a } X$ 73   
$C ^ { p } ( { \mathcal { F } } )$ 124   
$C ( { \cal { X } } )$ 47   
canonical bundle 120   
characteristic Euler 130   
closed map 58   
closed subprevariety 38   
closed subscheme 98   
closed subset 12   
closed subvariety 41   
closure 12   
codimX Y 17   
codimension of a prime ideal 17 of a subspace 17   
coherent sheaf 111   
cohomology 125   
complete variety 59   
complex 125   
component connected 16 irreducible 15   
cone 47 over a subset 47 tangent 73   
conic affine 32 projective 55   
connected component 16   
connected space 13   
continuous map 12   
coordinate ring affine 10 homogeneous 49   
coordinates affine 43 homogeneous 43 Plücker 64 Segre 56 Veronese 60   
cotangent sheaf 119   
Cremona transformation 77   
cubic hypersurface 20, 52   
cubic surface 4, 85   
curve 41 affine 19 dual 84   
$D ( f ) ~ 2 4 , 9 2$   
$\Delta \chi \_ 1 1$   
decomposition homogeneous 44 irreducible 15 primary 15   
deg f 44   
degX 20, 52   
degree in a graded ring 44 of a hypersurface 20, 52 of a polynomial 6   
dehomogenization of a polynomial 49 of an ideal 49   
dense 16   
diagonal 41   
differential 118   
dimK V 17   
dimX 17   
dimension Krull 17 local 19 of a ring 17 of a topological space 17 pure 19   
direct sum of sheaves 103   
disconnected space 13   
distinguished open subset 24, 92   
dominant map 69   
double point 95   
dual curve 84   
dual sheaf 108   
elimination theory main theorem 58   
embedding Plücker 64 Segre 56 Veronese 60   
Euler characteristic 130   
Euler sequence 120   
exact sequence 108   
exceptional hypersurface 75   
exceptional set 70

$f _ { * } \mathcal { F }$ 104   
$f ^ { * } { \mathcal { F } }$ 114   
$\mathcal { F } _ { a }$ 27   
$f ^ { \mathrm { h } }$ 50   
$f ^ { \mathrm { i } }$ 49   
$f ^ { \mathrm { i n } } ~ 7 5$   
fat point 95, 101   
Fermat hypersurface 84   
fiber 114   
fiber product 100   
finite type 99   
function   
local 27   
rational 69   
regular 22, 35, 53, 93   
function field 69   
$\Gamma _ { f }$ 41   
$G ( k , n )$ 62   
general point 92   
generic point 92   
generic smoothness 83   
genus 131   
germ 27   
gluing   
of prevarieties 35, 37   
gluing property 26   
graded algebra 44   
graded ring 44   
graph 41   
Grassmannian variety 62   
$h ^ { p } ( X , { \mathcal { F } } )$ 125   
$H ^ { p } ( X , { \mathcal { F } } )$ 125   
Hausdorff space 40

height 17   
Hilbert Basis Theorem 7 Nullstellensatz 8   
homogeneous coordinate ring 49   
homogeneous coordinates 43   
homogeneous decomposition 44   
homogeneous element 44   
homogeneous ideal 45   
homogenization of a polynomial 50 of an ideal 50   
hypersurface 41 affine 19 cubic 20, 52 degree 20, 52 exceptional 75 Fermat 84 linear 20, 52 quadric 20, 52   
$I ( X )$ 8, 10, 46, 49, 91   
$I _ { 0 } \ 4 8$   
$I _ { a } ~ 2 7$   
$I _ { \mathrm { a } } ( X )$ 46   
$I _ { \mathrm { p } } ( X )$ 46, 49   
$I _ { Y } ( X )$ 10, 49   
ideal dehomogenization 49 for schemes 91 homogeneous 45 homogenization 50 irrelevant 48 of a projective variety 46 of a set 8, 10, 46 of an affine variety 8 quotient 16 sequence 112 sheaf 112, 113   
Identity Theorem 23   
image presheaf 106   
image sheaf 107   
Implicit Function Theorem 82   
incidence correspondence 67, 86   
initial term 75   
injective 107   
intersection scheme 97, 100   
irreducible component 15   
irreducible decomposition 15   
irreducible space 13   
irrelevant ideal 48   
isomorphism of ringed spaces 30   
$J ^ { \mathrm { h } } ~ 5 0$   
$\dot { J ^ { 1 } }$ 49   
Jacobi criterion affine 81 projective 82   
Jacobian matrix 81   
join 67

$K ( P )$ 91   
$K _ { P }$ 105

$K ( X )$ 69   
kernel sheaf 105   
Krull dimension 17 Principal Ideal Theorem 18   
$\Lambda ^ { k } { \mathcal { F } }$ 116   
$\Lambda ^ { k } V$ 63   
line bundle 115   
linear hypersurface 20, 52   
linear map alternating 62   
linear subspace of $\mathbb { P } ^ { n }$ 46   
Liouville’s Theorem 59   
local dimension 19   
local function 27   
local ring 27 regular 81   
locally free sheaf 115   
locally irreducible variety 81   
locally ringed space 96 morphism 96   
$\tilde { M }$ 110   
main theorem of elimination theory 58   
map birational 69 closed 58 continuous 12 rational 68   
module over ${ \mathcal { O } } _ { X }$ 103 presheaf 102 sheaf 102   
morphism injective 107 of locally ringed spaces 96 of presheaves 103 of ringed spaces 30 of sheaves 103 surjective 107   
$n$ -fold point 101   
Noetherian space 15   
non-singular point 80   
non-singular variety 80   
normal bundle 122   
normal sequence 122   
Nullstellensatz 8 projective 48 relative 11 scheme-theoretic 92 weak 10   
$\mathcal { O } _ { \mathbb { P } ^ { n } } ( d )$ 103   
${ \mathcal { O } } _ { X } ( U )$ 22, 53, 93   
${ \mathcal { O } } _ { X }$ 26, 29   
${ \mathcal { O } } _ { X , a }$ 27   
${ \mathcal { O } } _ { X }$ -module 103   
$\Omega _ { R }$ 118   
$\Omega _ { X } \ 1 1 9$   
$\omega _ { X } ~ 1 2 0$   
open set distinguished 24, 92   
open subprevariety 38   
open subscheme 98   
open subset 12   
open subvariety 41   
$\mathbb { P } ^ { 1 } 3 6$   
$\mathbb { P } ^ { n } \ 4 3$   
$\mathbb { P } ( X )$ 47   
part affine 43   
Plücker coordinates 64   
Plücker embedding 64   
point double 95 fat 95, 101 general 92 generic 92 $n$ -fold 101 non-singular 80 regular 80 singular 80 smooth 80   
polynomial degree 6 dehomogenization 49 homogenization 50   
polynomial function 10   
presheaf 26 germ 27 image 106 morphism 103 of modules 102 restriction 27 stalk 27 tensor 106   
prevariety 35 gluing 35, 37 product 39 separated 41   
primary decomposition 15   
Principal Ideal Theorem 18   
product of affine varieties 7, 32 of prevarieties 39 of schemes 100 topology 13 universal property 32, 39, 100   
projection 55   
projection formula 115   
projective automorphism 54   
projective conic 55   
projective Jacobi criterion 82   
projective Nullstellensatz 48   
projective space 43   
projective subvariety 49   
projective variety 46   
projective zero locus 46   
projectivization of a cone 47   
pull-back map 96 of a function 30 of sheaves 114

pure dimension 19   
pure tensor 65   
push-forward 104

quadric hypersurface 20, 52   
quasi-coherent sheaf 111   
quotient sheaf 108   
quotient topology 36   
radical 6   
rank of a locally free sheaf 115   
rational function 69   
rational map 68 dominant 69   
reduced algebra 33   
reduced scheme 99   
reducible space 13   
regular function on a prevariety 35 on a projective variety 53 on an affine scheme 93 on an affine variety 22 sheaf 26   
regular local ring 81   
regular point 80   
regular variety 80   
Relative Nullstellensatz 11   
Removable Singularity Theorem 25   
residue field 91   
resolution of singularities 83   
restriction of a presheaf 27   
restriction map 26   
ring graded 44 local 27 reduced 33 regular local 81   
ringed space 29 isomorphism 30 locally 96 morphism 30   
rk F 115   
$S ( X )$ 49   
scheme 98 affine 90 associated to a prevariety 99 associated to a variety 90, 99 fiber product 100 intersection 97, 100 of finite type 99 over Y 99 reduced 99 separated 100   
section of a presheaf 26   
Segre coordinates 56   
Segre embedding 56   
separated prevariety 41   
separated scheme 100   
sequence conormal 121 Euler 120 ideal 112 normal 122 skyscraper 108   
Serre duality 132   
set affine open 35 algebraic 6 dense 16 distinguished open 24, 9 exceptional 70   
sheaf 26 associated 106, 110 coherent 111 cotangent 119 direct sum 103 dual 108 germ 27 ideal 112, 113 image 107 kernel 105 locally free 115 morphism 103 of modules 102 of regular functions 26 pull-back 114 push-forward 104 quasi-coherent 111 quotient 108 restriction 27 skyscraper 105 stalk 27 structure 29, 93 tangent 102, 120 tautological 104 tensor 108 twisting 103, 116   
sheafification 106 universal property 107   
singular point 80 resolution 83   
singular variety 80   
skyscraper sequence 108 double 109, 128   
skyscraper sheaf 105   
smooth point 80   
smooth variety 80 generically 83   
space affine 6 locally ringed 96 projective 43 ringed 29 tangent 78   
spectrum 90   
stalk 27   
strict transform 70   
structure sheaf 29, 93   
subprevariety closed 38 open 38   
subscheme affine 97 closed 98

open 98 subset closed 12 open 12 subspace topology 12 subvariety affine 10 closed 41 open 41 projective 49 sum of sheaves 103 surface 41 affine 19 cubic 4, 85 surjective 107

$T _ { a } X$ 78   
$T _ { X }$ 102, 120   
tangent bundle 120   
tangent cone 73   
tangent sheaf 102, 120   
tangent space 78   
tautological sheaf 104   
tensor pure 65   
tensor presheaf 106   
tensor product alternating 62, 116   
tensor sheaf 108   
topological space connected 13 disconnected 13 Hausdorff 40 irreducible 13 Noetherian 15 reducible 13   
topology 12 product 13 quotient 36 subspace 12 Zariski 12, 49, 91   
transform strict 70   
twisting sheaf 103, 116

unique factorization domain 20 universal property of products 32, 39, 100 of sheafification 107

$V ( S )$ 6, 10, 46, 49, 91   
$V _ { \mathrm { a } } ( S )$ 46   
$V _ { \mathrm { p } } ( S )$ 46, 49   
$V _ { Y } ( S )$ 10, 49   
value 91, 93, 114   
variety 41 affine 6, 33 birational 69 complete 59 Grassmannian 62 non-singular 80 projective 46 regular 80 singular 80 smooth 80   
vector bundle 115   
Veronese coordinates 60   
Veronese embedding 60

Weak Nullstellensatz 10

$X _ { \mathrm { s c h } } \ 9 9 $ $\chi ( X , { \mathcal { F } } )$ 130

Zariski topology 12, 49, 91   
zero locus 10 affine 6 for schemes 91 projective 46