Martin Aigner Günter M. Ziegler

# Proofs from THE BOOK

Third Edition

With 250 Figures Including Illustrations by Karl H. Hofmann

# Preface

Paul Erdôs liked to talk about The Book, in which God maintains the perfect proofs for mathematical theorems, following the dictum of G. H. Hardy that there is no permanent place for ugly mathematics. Erdös also said that you need not believe in God but, as a mathematician, you should believe in The Book. A few years ago, we suggested to him to write up a first (and very modest) approximation to The Book. He was enthusiastic about the idea and, characteristically, went to work immediately, filling page after page with his suggestions. Our book was supposed to appear in March 1998 as a present to Erdôs' 85th birthday. With Paul's unfortunate death in the summer of 1997, he is not listed as a co-author. Instead this book is dedicated to his memory.

We have no definition or characterization of what constitutes a proof from The Book: all we offer here is the examples that we have selected, hoping that our readers will share our enthusiasm about brilliant ideas, clever insights and wonderful observations. We also hope that our readers will enjoy this despite the imperfections of our exposition. The selection is to a great extent influenced by Paul Erdôs himself. A large number of the topics were suggested by him, and many of the proofs trace directly back to him, or were initiated by his supreme insight in asking the right question or in making the right conjecture. So to a large extent this book reflects the views of Paul Erdós as to what should be considered a proof from The Book.

A limiting factor for our selection of topics was that everything in this book is supposed to be accessible to readers whose backgrounds include only a modest amount of technique from undergraduate mathematics. A little linear algebra, some basic analysis and number theory, and a healthy dollop of elementary concepts and reasonings from discrete mathematics should be sufficient to understand and enjoy everything in this book.

We are extremely grateful to the many people who helped and supported us with this project — among them the students of a seminar where we discussed a preliminary version, to Benno Artmann, Stephan Brandt, Stefan Felsner, Eli Goodman, Torsten Heldmann, and Hans Mielke. We thank Margrit Barrett, Christian Bressler, Ewgenij Gawrilow, Elke Pose, and Jörg Rambau for their technical help in composing this book. We are in great debt to Tom Trotter who read the manuscript from first to last page, to Karl H. Hofmann for his wonderful drawings, and most of all to the late great Paul Erdós himself.

![](images/5d65123e864cb03aea812a68a99b8e1f97da3e55693fff6388e05dddbbcf9280.jpg)  
Paul Erdôs

![](images/a722f1c6f08251a2018a9407fe7747b340aec270782682503daaf930b0f30c3b.jpg)  
"The Book"

# Preface to the Second Edition

The first edition of this book got a wonderful reception. Moreover, we received an unusual number of letters containing comments and corrections, some shortcuts, as well as interesting suggestions for alternative proofs and new topics to treat. (While we are trying to record perfect proofs, our exposition isn't.)

The second edition gives us the opportunity to present this new version of our book: It contains three additional chapters, substantial revisions and new proofs in several others, as well as minor amendments and improvements, many of them based on the suggestions we received. It also misses one of the old chapters, about the "problem of the thirteen spheres," whose proof turned out to need details that we couldn't complete in a way that would make it brief and elegant.

Thanks to all the readers who wrote and thus helped us — among them Stephan Brandt, Christian Elsholtz, Jürgen Elstrodt, Daniel Grieser, Roger Heath-Brown, Lee L. Keener, Christian Leboeuf, Hanfried Lenz, Nicolas Puech, John Scholes, Bernulf WeiBbach, and many others. Thanks again for help and support to Ruth Allewelt and Karl-Friedrich Koch at Springer Heidelberg, to Christoph Eyrich and Torsten Heldmann in Berlin, and to Karl H. Hofmann for some superb new drawings.

Berlin, September 2000

# Preface to the Third Edition

We would never have dreamt, when preparing the first edition of this book in 1998, of the great success this project would have, with translations into many languages, enthusiastic responses from so many readers, and so many wonderful suggestions for improvements, additions, and new topics -— that could keep us busy for years.

So, this third edition offers two new chapters (on Euler's partition identities, and on card shuffling), three proofs of Euler's series appear in a separate chapter, and there is a number of other improvements, such as the Calkin-Wilf-Newman treatment of "enumerating the rationals." That's it, for now!

We thank everyone who has supported this project during the last five years, and whose input has made a difference for this new edition. This includes David Bevan, Anders Björner, Dietrich Braess, John Cosgrave, Hubert Kalf, Günter Pickert, Alistair Sinclair, and Herb Wilf.

# Table of Contents

# Number Theory 1

1. Six proofs of the infinity of primes . .   
2. Bertrand's postulate ..   
3.Binomial coefficients are (almost) never powers 13   
4Representing numbers as sums of two squares   
5. Every finite division ring is a field . 23   
6.Some irrational numbers 27   
7. Three times $\pi ^ { 2 } / 6$ 35

# Geometry 43

8. Hilbert's third problem: decomposing polyhedra . . . 45   
9.Lines in the plane and decompositions of graphs 53   
10. The slope problem . 59   
11. Three applications of Euler's formula 65   
12. Cauchy's rigidity theorem 71   
13. Touching simplices .. 75   
14. Every large point sct has an obtuse angle 79   
15. Borsuk's conjecture ... 85

# Analysis _91

16. Sets, functions, and the continuum hypothesis 93   
17. In praise of inequalities 109   
18. A theorem of Pólya on polynomials 117   
19. On a lemma of Littlewood and Offord 123   
20. Cotangent and the Herglotz trick . . 127   
21. Buffon's needle problem .... 133

# Combinatorics _137

22. Pigeon-hole and double counting 139   
23. Three famous theorems on finite sets 151   
24. Shuffling cards . . 157   
25. Lattice paths and determinants 167   
26. Cayley's formula for the number of trees 173   
27. Completing Latin squares 179   
28. The Dinitz problem .. 185   
29. Identities versus bijections . 191

# Graph Theory 197

Five-coloring plane graphs 199   
31. How to guard a museum . 203   
32.Turán's graph theorem .207   
33. Communicating without errors .. 213   
34. Of friends and politicians 223   
35. Probability makes counting (sometimes) easy 227   
About the Illustrations 236   
Index 237

# Six proofsof the infinity of primes

# Chapter 1

It is only natural that we start these notes with probably the oldest Book Proof, usually attributed to Euclid. It shows that the sequence of primes does not end.

Euclid's Proof. For any finite set $\{ p _ { 1 } , \ldots , p _ { r } \}$ of primes, consider the number $n = p _ { 1 } p _ { 2 } \cdots p _ { r } + 1$ This $n$ has a prime divisor $p$ But $p$ is not one of the $p _ { i }$ : otherwise $p$ would be a divisor of $n$ and of the product $p _ { 1 } p _ { 2 } \cdots p _ { r }$ , and thus also of the difference $n - p _ { 1 } p _ { 2 } \ldots p _ { r } = 1$ ,which is impossible. So a finite set $\{ p _ { 1 } , \ldots , p _ { r } \}$ cannot be the collection of all prime numbers. □

Before we continue let us fix some notation. $\mathbb { N } = \{ 1 , 2 , 3 , . . . \}$ is the set of natural numbers, $\mathbb { Z } = \{ \dots , - 2 , - 1 , 0 , 1 , 2 , \dots \}$ the set of integers, and $\mathbb { P } = \{ 2 , 3 , 5 , 7 , \dots \}$ the set of primes.

In the following, we will exhibit various other proofs (out of a much longer list) which we hope the reader will like as much as we do. Although they use different view-points, the following basic idea is common to all of them: The natural numbers grow beyond all bounds, and every natural number $n \geq 2$ has a prime divisor. These two facts taken together force $\mathbb { P }$ to be infinite. The next three proofs are folklore, the fifth proof was proposed by Harry Fürstenberg, while the last proof is due to Paul Erdôs.

The second and the third proof use special well-known number sequences.

Second Proof. Suppose $\mathbb { P }$ is finite and $p$ is the largest prime. We consider the so-called Mersenne number $2 ^ { p } - 1$ and show that any prime factor $q$ of $2 ^ { p } - 1$ is bigger than $p$ , which will yield the desired conclusion. Let $q$ be a prime dividing $2 ^ { p } - 1$ , so we have $2 ^ { p } \equiv 1 ( { \bmod { q } } )$ . Since $p$ is prime, this means that the element 2 has order $p$ in the multiplicative group $\mathbb { Z } _ { q } \backslash \{ 0 \}$ of the field $\mathbb { Z } _ { q }$ This group has $q - 1$ elements. By Lagrange's theorem (see the box) we know that the order of every element divides the size of the group, that is, we have $p \mid q - 1$ , and hence $p < q$ . □

Third Proof. Next let us look at the Fermat numbers $F _ { n } = 2 ^ { 2 ^ { n } } + 1$ for $n = 0 , 1 , 2 , \ldots .$ We will show that any two Fermat numbers are relatively prime; hence there must be infinitely many primes. To this end, we verify the recursion

$$
\prod _ { k = 0 } ^ { n - 1 } F _ { k } \ = \ F _ { n } - 2 \qquad ( n \geq 1 ) ,
$$

# Lagrange's Theorem

IfG is a finite (multplicative) group and $U$ is $a$ subgroup, then $| U |$ divides $| G |$ .

Proof. Consider the binary relation

$$
a \sim b : \iff b a ^ { - 1 } \in U .
$$

It follows from the group axioms that $\sim$ is an equivalence relation. The equivalence class containing an element $a$ is precisely the coset

$$
U a = \{ x a : x \in U \} .
$$

Since clearly $| U a | = | U |$ , we find that $G$ decomposes into equivalence classes, all of size $| U |$ , and hence that $| U |$ divides $| G |$ .

In the special case when $U$ is a cyclic su ugrou $\{ a , a ^ { 2 } , \ldots , a ^ { m } \}$ findd that $m$ (the smallest positive integer such that $\boldsymbol { a } ^ { m } ~ = ~ 1$ , called the order of $a$ )divides the size $| G |$ of the group.

$F _ { 0 } ^ { \ i }$ = 3   
$F _ { 1 }$ = 5   
$F _ { 2 }$ = 17   
$F _ { 3 }$ = 257   
$F _ { 4 }$ = 65537   
$F _ { 5 }$ = 641 ·6700417

The first few Fermat numbers

from which our assertion follows immediately. Indeed, if $m$ is a divisor of, say, $F _ { k }$ and $F _ { n }$ $( k < n )$ , then $m$ divides 2, and hence $m = 1$ or 2. But $m = 2$ is impossible since all Fermat numbers are odd.

To prove the recursion we use induction on $n$ .For $n = 1$ we have $F _ { 0 } = 3$ and $F _ { 1 } - 2 = 3$ With induction we now conclude

$$
\begin{array} { l } { { \displaystyle \prod _ { k = 0 } ^ { n } F _ { k } ~ = \Big ( \prod _ { k = 0 } ^ { n - 1 } F _ { k } \Big ) F _ { n } ~ = ~ ( F _ { n } - 2 ) F _ { n } ~ = } } \\ { { ~ = ( 2 ^ { 2 ^ { n } } - 1 ) ( 2 ^ { 2 ^ { n } } + 1 ) ~ = ~ 2 ^ { 2 ^ { n + 1 } } - 1 ~ = ~ F _ { n + 1 } - 2 . } } \end{array}
$$

Now let us look at a proof that uses elementary calculus.

![](images/b1e723e0bc83ded47902fa07e8364a780ee0c2c2ed7f561d752a75e9671a92fa.jpg)

Steps above the function $\textstyle f ( t ) = { \frac { 1 } { t } }$

Fourth Proof. Let $\pi ( x ) : = \# \{ p \leq x : p \in \mathbb { P } \}$ be the number of primes that are less than or equal to the real number $x$ . We number the primes $\mathbb { P } = \{ p _ { 1 } , p _ { 2 } , p _ { 3 } , . . . \}$ in increasing order. Consider the natural logarithm $\log x$ , defined as $\textstyle \operatorname { l o g } { \dot { x } } = \int _ { 1 } ^ { x } { \frac { 1 } { t } } d t$ .

Now we compare the area below the graph of $\begin{array} { r } { f ( t ) = \frac { 1 } { t } } \end{array}$ with an upper step function. (See also the appendix on page 10 for this method.) Thus for $n \leq x < n + 1$ we have

$$
\begin{array} { l l l } { \log x } & { \leq } & { 1 + { \displaystyle \frac { 1 } { 2 } } + { \displaystyle \frac { 1 } { 3 } } + . . . + \frac { 1 } { n - 1 } + \frac { 1 } { n } } \\ & & { \leq } & { \sum \frac { 1 } { m } , \mathrm { ~ w h e r e ~ t h e ~ s u m ~ e x t e n d s ~ o v e r ~ a l l ~ } n } \\ & & { \mathrm { ~ o n l y ~ p r i m e ~ d i v i s o r s ~ } p \leq x . } \end{array}
$$

Since every such $m$ can be written in a unique way as a product of the form $\prod _ { p \leq x } p ^ { k _ { p } }$ , we see that the last sum is equal to

$$
\prod _ { p \in \mathbb { P } } { \Big ( } \sum _ { k \geq 0 } { \frac { 1 } { p ^ { k } } } { \Big ) } .
$$

The inner sum is a geometric series with ratio $\frac { 1 } { p }$ , hence

$$
\log x \leq \prod _ { \stackrel { p \in \mathbb { P } } { p \leq x } } { \frac { 1 } { 1 - { \frac { 1 } { p } } } } = \prod _ { \stackrel { p \in \mathbb { P } } { p \leq x } } { \frac { p } { p - 1 } } = \prod _ { k = 1 } ^ { \pi ( x ) } { \frac { p _ { k } } { p _ { k } - 1 } } .
$$

Now clearly $p _ { k } \ge k + 1$ , and thus

$$
\frac { \relax _ { p _ { k } } } { \relax _ { p _ { k } - 1 } } = 1 + \frac { 1 } { \mathit { p _ { k } } - 1 } \le 1 + \frac { 1 } { \mathit { k } } = \frac { \mathit { k } + 1 } { \mathit { k } } ,
$$

and therefore

$$
\log x \le \prod _ { k = 1 } ^ { \pi ( x ) } { \frac { k + 1 } { k } } = \pi ( x ) + 1 .
$$

Everybody knows that $\log x$ is not bounded, so we conclude that $\pi ( x )$ is unbounded as well, and so there are infinitely many primes. □

Fifth Proof. After analysis it's topology now! Consider the following curious topology on the set $\mathbb { Z }$ of integers. For $a$ , $b \in \mathbb { Z } , b > 0$ we set

$$
N _ { a , b } = \{ a + n b : n \in \mathbb { Z } \} .
$$

Each set $N _ { a , b }$ is a two-way infinite arithmetic progression. Now call a set $O \subseteq \mathbb { Z }$ open if either $O$ is empty, or if to every $a \in O$ there exists some $b > 0$ with $N _ { a , b } \subseteq O$ .Clearly, the union of open sets is open again. If $O _ { 1 } , O _ { 2 }$ are open, and $a \ \in \ O _ { 1 } \cap O _ { 2 }$ with $N _ { a , b _ { 1 } } \subseteq O _ { 1 }$ and $N _ { a , b _ { 2 } } \subseteq O _ { 2 }$ , then $a \in N _ { a , b _ { 1 } b _ { 2 } } \subseteq O _ { 1 } \cap O _ { 2 }$ .So we conclude that any finite intersection of open sets is again open. So, this family of open sets induces a bona fide topology on $\mathbb { Z }$ .

Let us note two facts:

(A) Any non-empty open set is infinite.   
Any set $N _ { a , b }$ is closed as well.

Indeed, the first fact follows from the definition. For the second we observe

$$
N _ { a , b } ~ = ~ \mathbb { Z } \backslash \bigcup _ { i = 1 } ^ { b - 1 } N _ { a + i , b } ,
$$

which proves that $N _ { a , b }$ is the complement of an open set and hence closed.

So far the primes have not yet entered the picture — but here they come. Since any number $n \neq 1 , - 1$ has a prime divisor $p$ , and hence is contained in $N _ { 0 , p }$ , we conclude

$$
\mathbb { Z } \backslash \{ 1 , - 1 \} \ = \ \bigcup _ { p \in \mathbb { P } } N _ { 0 , p } .
$$

Now if $\mathbb { P }$ were finite, then $\textstyle \bigcup _ { p \in \mathbb { P } } N _ { 0 , p }$ would be a finite union of closed sets (by (B)), and hence closed. Consequently, $\{ 1 , - 1 \}$ would be an open set, in violation of (A). □

Sixth Proof. Our final proof goes a considerable step further and demonstrates not only that there are infinitely many primes, but also that the series ∑p 1 iv.The st pro  ths portant resul as given by Euler (and is interesting in its own right), but our proof, devised by Erdôs, is of compelling beauty.

Let be the sequence of primes in increasing order, and ass me that t pP 1 L ea be a maura er $k$ such that ∑i≥k+1 pi $p _ { 1 } , \ldots , p _ { k }$   
$ p _ { k + 1 } , p _ { k + 2 } , . . .$ the big primes. For an arbitrary natural number $N$ we therefore find

$$
\sum _ { i \geq k + 1 } { \frac { N } { p _ { i } } } < { \frac { N } { 2 } } .
$$

![](images/7f4556e3324d14ed1ecb1e75cabd6b1de791b86a083ef8668c2360a4bc58dfbf.jpg)  
"Pitching flat rocks, infinitely"

Let $N _ { b }$ be the number of positive integers $n \leq N$ which are divisible by at least one big prime, and $N _ { s }$ the number of positive integers $n \leq N$ which have only small prime divisors. We are going to show that for a suitable $N$

$$
N _ { b } + N _ { s } \ < \ N ,
$$

which will be our desired contradiction, since by definition $N _ { b } + N _ { s }$ would have to be equal to $N$ .

To estimate $N _ { b }$ note that $\begin{array} { r } { \lfloor \frac { N } { p _ { i } } \rfloor } \end{array}$ counts the positive integers $n \leq N$ which are multiples of $p _ { i }$ .Hence by (1) we obtain

$$
N _ { b } \leq \sum _ { i \geq k + 1 } \left\lfloor { \frac { N } { p _ { i } } } \right\rfloor < { \frac { N } { 2 } } .
$$

Let us now look at $N _ { s }$ .We write every $n \leq N$ which has only small prime divisors in the form $n = a _ { n } b _ { n } ^ { 2 }$ , where $a _ { n }$ is the square-free part. Every $a _ { n }$ is thus a product of different small primes, and we conclude that there are precisely $2 ^ { k }$ different square-free parts. Furthermore, as $b _ { n } \leq \sqrt { n } \leq \sqrt { N }$ we find that there are at most $\sqrt { N }$ different square parts, and so

$$
N _ { s } \leq 2 ^ { k } { \sqrt { N } } .
$$

Since (2) holds for any $N$ $N$ with $2 ^ { k } { \sqrt { N } } \leq { \frac { N } { 2 } }$ or $2 ^ { k + 1 } \leq \sqrt { N }$ , and for this $N = 2 ^ { 2 k + 2 }$ will do.

# References

[1] P. ERDós: Über die Reihe $\sum { \frac { 1 } { p } }$ , Mathematica, Zutphen B 7 (1938), 1-2.   
[2] L. EULER: Introductio in Analysin Infinitorum, Tomus Primus, Lausanne 1748; Opera Omnia, Ser. 1, Vol. 90.   
[3] H. FÜRSTENBERG: On the infinitude of primes, Amer. Math. Monthly 62 (1955), 353.

# Bertrand's postulate

# Chapter 2

We have seen that the sequence of prime numbers $2 , 3 , 5 , 7 , \ldots$ is infinite. To see that the size of its gaps is not bounded, let $N : = 2 \cdot 3 \cdot 5 \cdot \dots \cdot p$ denote the product of all prime numbers that are smaller than $k + 2$ ,and note that none of the $k$ numbers

$$
N + 2 , N + 3 , N + 4 , . . . . , N + k , N + ( k + 1 )
$$

is prime, since for $2 \leq i \leq k + 1$ we know that $i$ has a prime factor that is smaller than $k + 2$ , and this factor also divides $N$ , and hence also $N + i$ . With this recipe, we find, for example, for $k = 1 0$ that none of the ten numbers

2312, 2313, 2314, . . ., 2321

is prime.

But there are also upper bounds for the gaps in the sequence of prime numbers. A famous bound states that "the gap to the next prime cannot be larger than the number we start our search at." This is known as Bertrand's postulate, since it was conjectured and verified empirically for $n < 3 0 0 0 0 0 0$ by Joseph Bertrand. It was first proved for all $_ n$ by Pafnuty Chebyshev in 1850. A much simplcr proof was given by the Indian genius Ramanujan. Our Book Proof is by Paul Erdôs: it is taken from Erdôs' first published paper, which appeared in 1932, when Erdôs was 19.

# Bertrand's postulate.

For every $n \geq 1$ , there is some prime number $\mathcal { p }$ with $n < p \leq 2 n$

$\binom { 2 n } { n }$ carefully enough to see that if it didn't have any prime factors in the range $n < p \leq 2 n$ , then it would be "too small." Our argument is in five steps.

(1) We first prove Bertrand's postulate for $n < 4 0 0 0$ For this one does not need to check 4000 cases: it suffices (this is "Landau's trick") to check that

$$
2 , 3 , 5 , 7 , 1 3 . 2 3 , 4 3 , 8 3 , 1 6 3 , 3 1 7 , 6 3 1 , 1 2 5 9 , 2 5 0 3 , 4 0 0 1
$$

is a sequence of prime numbers, where each is smaller than twice the previous one. Hence every interval $\{ y : n < y \leq 2 n \}$ , with $n \leq 4 0 0 0$ , contains one of these 14 primcs.

![](images/57be3b458c4d7733468f1df6564a9196feb1eeb243727e1c462933c720854f7f.jpg)  
Joseph Bertrand

# Beweis eines Satzes von Tschebyschef.

# Von P. EaDds in Budapcst.

Fur den 2uerst won Tscheeyscher bewiesenen Satz, laut en s ischen ir natrchn Za nd ther eiachen e  h   Liah Beweise vor. Ais einfachsten kann man obne Zweifel den Beweis n Ra) berichn In s We Voren ber Zahientheorir (Leipaig, 1927), Band 1, S. 66-68 gibt Herr Lanau einen esonders eintachen Bewes fur einen Satz ber di Anzahl zahe ner  een Gc  elce n-Z gac  Pa F blicklichen Zwecken des Herrn Lanau kommt es nicht auf die numerische Bestimmung der i Beweis auftretenden Konstanten u   V des Bewciscs leicht, dad q jedenfalis groder als 2 ausfatt.

In den folgenden Zrilen wride ichk zeigen, daf man durch eine Verscharfung der dem LanaUschen Beweis rugrunde liegenen Iden  einem Bewes des oen crahten Tschescherschen Satzes gelangen kana, der wic mir scheint  an Ein-Iachkeit nicht hinter dem Ramanujaschen Beweis steht. Ciriechische Buchstahn solen  Fodnen duch posii atihe Bucstabn natriche Zan bezeihn; i Bezihung P t fur Primzahien vorbehalten.

1. Der Bnomalkoctizient

πμ<q MMM   
Kernly hon   
Wright m< M m(2==Cm+1

) Next we prove that

$$
\prod _ { p \leq x } p \leq 4 ^ { x - 1 } \qquad { \mathrm { f o r ~ a l l ~ r e a l ~ } } x \geq 2 ,
$$

where our notation — here and in the following — is meant to imply that the product is taken over all prime numbers $p \leq x$ . The proof that we present for this fact uses induction on the number of these primes. It is not from Erdös' original paper, but it is also due to Erds (see the margin), and it is a true Book Proof. First we note that if $\tilde { q }$ is the largest prime with $q \leq x$ , then

$$
\prod _ { p \leq x } p \ = \ \prod _ { p < q } p \qquad { \mathrm { a n d } } \qquad 1 ^ { q - 1 } \ \leq \ 1 ^ { x - 1 } .
$$

Thus it suffices to check (1) for the case where $x = q$ is a prime number. For $q = 2$ we get $^ { \mathfrak { s } \mathfrak { s } } \leq \mathtt { 1 }$ ," so we proceed to consider odd primes $q = 2 m + 1$ . (Here we may assume, by induction, that (1) is valid for all integers $x$ in the set $\{ 2 , 3 , \ldots , 2 m \}$ )For $q = 2 m + 1$ we split the product and compute

$$
\prod _ { p \leq 2 m + 1 } p = \prod _ { p \leq m + 1 } p \cdot \prod _ { m + 1 < p \leq 2 m + 1 } p \leq 4 ^ { m } { \binom { 2 m + 1 } { m } } \leq 4 ^ { m } 2 ^ { 2 m } = 4 ^ { 2 m } .
$$

All the pieces of this "one-line computation" are easy to see. In fact,

$$
\prod _ { p \leq m + 1 } p \leq 4 ^ { m }
$$

holds by induction. The inequality

$$
\prod _ { \scriptstyle m \mid 1 < p \leq 2 m \mid 1 } p \leq { \binom { 2 m + 1 } { m } }
$$

follows from the observation that $\textstyle { \binom { 2 m \mid 1 } { m } } = { \frac { ( 2 m \mid 1 ) ! } { m ! ( m + 1 ) ! } }$ is an integer, where the primes that we consider all are factors of the numerator $( 2 r n + 1 ) !$ , but not of the denominator $m ! ( \mathfrak { m } + { \bf 1 } ) !$ . Finally

# Legendre's theorem

The number n! contains the prime factor $\pmb { p }$ exactly

$$
\sum _ { k \geq 1 } \left\lfloor { \frac { n } { p ^ { k } } } \right\rfloor
$$

times.

Proof. Exactly $\left[ { \frac { n } { p } } \right]$ of the factors of $n ! = 1 \cdot 2 \cdot 3 \cdot \ldots \bar { n }$ are divisible by $p$ , which accounts for $\textstyle \left\lfloor { \frac { n } { \mathfrak { p } } } \right\rfloor p .$ -factors. Next, $\left\lfloor { \frac { \eta } { p ^ { \frac { 3 } { 2 } } } } \right\rfloor$ of the factors of $n !$ are even divisible by $p ^ { 2 }$ , which accounts for the next $\left\lfloor { \frac { \gamma _ { l } } { p ^ { 2 } } } \right\rfloor$ prime factors $\mathfrak { p }$ of $n ! ,$ etc. 0

$$
\binom { 2 m + 1 } { m } \leq 2 ^ { 2 m }
$$

holds since

$$
\binom { 2 m + 1 } { m } \ \mathrm { a n d } \ \binom { 2 m + 1 } { m + 1 }
$$

are two (equal!) summands that appear in

$$
\sum _ { k = 0 } ^ { 2 m \mid 1 } { \binom { 2 m + 1 } { k } } = 2 ^ { 2 m + 1 } .
$$

(3) From Legendre's thcorem (see the box) we get that $\begin{array} { r } { \binom { 2 \pi } { \eta } = \frac { ( 2 \pi ) ! } { \eta ! \eta ! } } \end{array}$ contains the prime factor $p$ exactly

$$
\sum _ { k \geq 1 } \left( \left\lfloor { \frac { 2 n } { p ^ { k } } } \right\rfloor - 2 \left\lfloor { \frac { n } { p ^ { k } } } \right\rfloor \right)
$$

times. Here each summand is at most 1, since it satisfics

$$
\left| \frac { 2 n } { p ^ { k } } \right| - 2 \left\lfloor \frac { n } { p ^ { k } } \right\rfloor \ < \ \frac { 2 n } { p ^ { k } } - 2 \left( \frac { n } { p ^ { k } } - 1 \right) \ = \ 2 ,
$$

and it is an integer. Furthermore the summands vanish whenever $p ^ { \tt A } > 2 \Im \ell$ . Thus $( ^ { 2 \pi i } )$ contains $p$ exactly

$$
\sum _ { k \geq 1 } \left( \left\lfloor { \frac { 2 n } { p ^ { k } } } \right\rfloor - 2 \left\lfloor { \frac { n } { p ^ { k } } } \right\rfloor \right) \leq \operatorname* { m a x } \{ r : p ^ { r } \leq 2 n \}
$$

times. Hence the largest power of $p$ that divides $\binom { 2 \pi i } { \pi i }$ is not larger than $2 \pi$ In particular, primes $p > { \sqrt { 2 n } }$ appear at most once in $\binom { 2 \pi \varepsilon } { n }$ .

Furthermore — and this, according to Erdôs, is the key fact for his proof - primes $p$ that satisfy $\frac { 2 } { 3 } \pi < p \leq n$ do not divide $\binom { 2 n } { n }$ at all! Indeed, $3 p > 2 n$ implies (for $\gamma \} \geq 3$ , and hence $p \geq 3 .$ that $p$ and $2 p$ are the only multiples of $p$ that appcar as factors in the numcrator of $\frac { ( 2 n ) ! } { n ! n ! }$ , while we get two $p$ -factors in the denominator.

() Now e e ay t $( { \bf \small { 2 7 } } , )$ .For $n \geq 3$ , using an estimate from page 12 for the lower bound, we get

$$
{ \frac { 4 ^ { n } } { 2 n } } \leq { \binom { 2 n } { n } } \leq \prod _ { p \leq { \sqrt { 2 n } } } 2 n \quad \cdot \prod _ { { \sqrt { 2 n } } < p \leq { \frac { 2 } { 3 } } n } p \quad \cdot \prod _ { n < p \leq 2 n } p
$$

and thus, since there are not more than $\sqrt { 2 n }$ primes $p \leq \sqrt { 2 n }$

$$
4 ^ { n } \ \leq \ ( 2 n ) ^ { 1 + { \sqrt { 2 n } } } \ \cdot \ \prod _ { { \sqrt { 2 n } } < p \leq { \frac { 2 } { 3 } } n } p \quad \cdot \ \prod _ { n < p \leq 2 n } p \qquad { \mathrm { f o r } } \quad n \geq 3 .
$$

(5) Assume now that there is no prime $p$ with $\gamma _ { \downarrow } < p \le 2 \pi$ , so the second product in (2) is 1. Substituting (1)into (2) we get

$$
4 ^ { r _ { l } } \leq ( 2 n ) ^ { 1 + \sqrt { 2 \pi } } 4 ^ { \frac { 2 } { 3 } n }
$$

or

$$
\begin{array} { l } { { ( _ { 1 3 } ^ { \prime 2 6 } ) = 2 ^ { 3 } \cdot 5 ^ { 2 } \cdot 7 \cdot 1 7 \cdot 1 9 \cdot 2 3 } } \\ { { ( _ { 1 4 } ^ { 2 8 } ) = 2 ^ { 3 } \cdot 3 ^ { 3 } \cdot 5 ^ { 2 } \cdot 1 7 \cdot 1 9 \cdot 2 3 } } \\ { { ( _ { 1 5 } ^ { 3 0 } ) = 2 ^ { 4 } \cdot 3 ^ { 2 } \cdot 5 \cdot 1 7 \cdot 1 9 \cdot 2 3 \cdot 2 9 } } \end{array}
$$

$$
4 ^ { { \frac { 1 } { 3 } } \pi } \leq ( 2 \pi ) ^ { 1 + { \sqrt { 2 \pi } } } ,
$$

which is false for $n$ large enough! In fact, using $a + 1 < 2 ^ { a }$ (which holds for all $a \geq 2$ , by induction) we get

$$
2 \pi = \left( { \sqrt [ 6 ] { 2 n } } \right) ^ { 6 } < \left( \left\lfloor { \sqrt [ 6 ] { 2 n } } \right\rfloor + 1 \right) ^ { 6 } < 2 ^ { 6 }  \left\lfloor { \sqrt [ 6 ] { 2 n } } \right\rfloor \le 2 ^ { 6 } { \sqrt [ 6 ] { 2 n } } ,
$$

Examples such as

illustrate that "very small" prime factors $p < \sqrt { 2 \pi }$ can appear as higher powers in $( \mathbf { \Sigma } _ { n } ^ { 2 \pi z } )$ "smal" primes with $\sqrt { 2 \pi } <$ $p \leq \frac { 2 } { 3 } n$ appear at most once, while factors in the gap with $\frac { 2 } { 3 } \pi < p \leq r 2$ don't appear at all.

and thus for $n \geq 5 0$ (and hence $1 8 < 2 { \sqrt { 2 n } } )$ we obtain from (3) and (4)

$$
2 ^ { 2 n } \leq ( 2 n ) ^ { 3 \left( 1 + { \sqrt { 2 n } } \right) } < 2 ^ { { \sqrt [ 6 ] { 2 n } } \left( 1 8 + 1 8 { \sqrt { 2 n } } \right) } < 2 ^ { 2 0 { \sqrt [ 6 ] { 2 n } } { \sqrt { 2 n } } } = 2 ^ { 2 0 ( 2 n ) ^ { 2 / 3 } } .
$$

This implies $( 2 \gamma _ { L } ) ^ { 1 / 3 } < 2 ( )$ , and thus $\gamma _ { \downarrow } < 4 0 0 0$ .

One can extract even more from this type of estimates: From (2) one can derive with the same methods that

$$
\prod _ { n < \bar { p } \leq 2 n } p \geq 2 \sin ^ { n } \quad \mathrm { f o r } \quad n \geq 4 0 0 0 ,
$$

and thus that there are at least

$$
\log _ { 2 n } ( 2 ^ { \frac { 1 } { 3 0 } \pi L } ) \ = \ { \frac { 1 } { 3 0 } } { \frac { n } { \log _ { 2 } n + 1 } }
$$

![](images/652384b2b7f19ac6a183220235447630f5117f45610c4445f4ff9a7bb3f130ab.jpg)

primes in the range between $\mathfrak { n }$ and $2 \eta$ .

This is not that bad an estimate: the "true" number of primes in this range is roughly $n / \log n$ . This follows from the "prime number theorem," which says that the limit

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { \# \{ p \leq n : p { \mathrm { ~ i s ~ p r i m e } } \} } { n / \log n } }
$$

exists, and equals 1. This famous result was first provcd by Hadamard and de la Vallée-Poussin in 1896; Selberg and Erdös found an elementary proof (without complex analysis tools, but still long and involved) in 1948.

On the prime number theorem itself the final word, it seems, is still not in: for example a proof of the Riemann hypothesis (see page 41), one of the major unsolved open problems in mathematics, would also give a substantial improvement for the estimates of the prime number theorem. But also for Bertrand's postulate, one could expect dramatic improvements. In fact, the following is a famous unsolved problem:

Is there always a prime between $n ^ { 2 }$ and $( \gamma _ { \ell } + 1 ) ^ { 2 } \tilde { . }$

For additional information see [3, p. 19] and [4, pp. 248, 257].

# Appendix: Some estimates

Estimating via integrals

There is a very simple-but-effective method of estimating sums by integrals (as already encountered on page 4). For estimating the harmonic numbers

$$
H _ { n } \ = \ \sum _ { k = 1 } ^ { n } { \frac { \ d H } { \ d k } } \qquad 
$$

we draw the figure in the margin and derive from it

$$
H _ { n } - 1 = \sum _ { k = 2 } ^ { n } { \frac { 1 } { k } } < \int _ { 1 } ^ { n } { \frac { 1 } { \ell } } d t = \log n
$$

by comparing the area below the graph of $\begin{array} { r } { \bar { f } ( t ) = \frac { 1 } { t } \ ( 1 \leq t \leq n ) } \end{array}$ with the area of the dark shaded rectangles, and

$$
H _ { n } - { \frac { 1 } { n } } \ = \ \sum _ { k = 1 } ^ { n - 1 } { \frac { 1 } { k } } \ > \ \int _ { 1 } ^ { n } { \frac { 1 } { t } } d t \ = \ \log n
$$

by comparing with the area of the large rectangles (including the lightly shaded parts). Taken together, this yields

$$
\log n + \frac { 1 } { n } \ < \ H _ { n } \ < \ \log \pi \ + \ 1 .
$$

In particular, lim $H _ { n } \to \infty$ , and the order of growth of $H _ { \pi }$ is given by $\pmb { n } \longrightarrow \infty$ $\operatorname* { l i m } _ { n \to \infty } { \frac { f I _ { n } } { \log n } } = 1$ u  e

$$
H I _ { n } = \log n + \gamma + \frac { 1 } { 2 n } - \frac { 1 } { 1 2 n ^ { 2 } } + \frac { 1 } { 1 2 0 n ^ { 4 } } + O \left( \frac { 1 } { n ^ { 6 } } \right) ,
$$

where $\gamma \approx 0 . 5 7 7 2$ is "Euler's constant."

# Estimating factorials — Stirling's formula

The same method applied to

$$
\log ( n ! ) \ = \ \log 2 + \log 3 + \ldots + \log n \ = \ \sum _ { k = 2 } ^ { n } \log k
$$

yields

$$
\log ( ( n - 1 ) ! ) < \int _ { 1 } ^ { n } \log t d t < \log ( n ! ) ,
$$

where the integral is easily computed:

$$
\int _ { 1 } ^ { n } \log t d t \ = \ \Big [ t \log t - t \Big ] _ { 1 } ^ { n } \ = \ n \log n - n + 1 .
$$

Thus we get a lower estimate on $\hbar$

$$
n ! > e ^ { n \log n - n + 1 } = e { \left( \frac { \pi } { e } \right) } ^ { n }
$$

and at the same time an upper estimate

Here $\textstyle \mathcal { O } \left( \frac { 1 } { \gamma _ { \uparrow } ^ { 6 } } \right)$ denotes a function $f ( n )$ such that $J ( n ) \leq c { \frac { 1 } { \mu ^ { \hat { \kappa } } } }$ holds for some constant $^ { c }$ .

$$
n ! = n ( n - 1 ) ! < n e ^ { n \log n - n + 1 } = \epsilon n { \left( \frac { n } { e } \right) } ^ { n } .
$$

Here a more careful analysis is needed to get the asymptotics of $n !$ , as given by Stirling's formula

$$
n ! \sim { \sqrt { 2 \pi n } } \left( { \frac { \pi } { e } } \right) ^ { n } .
$$

And again there are more precise versions available, such as

$$
n ! = { \sqrt { 2 \pi n } } \left( { \frac { n } { e } } \right) ^ { n } \left( 1 + { \frac { 1 } { 1 2 n } } + { \frac { 1 } { 2 8 8 n ^ { 2 } } } - { \frac { 1 3 9 } { 5 1 4 0 n ^ { 3 } } } + O \left( { \frac { 1 } { n ^ { 4 } } } \right) \right) .
$$

# Estimating binomial coefficients

Just oei e al ceffs $\binom { n } { k }$ as the number of $k$ subsets of an $\hbar$ -set, we know that the sequence ${ \binom { n } { 0 } } , { \binom { n } { 1 } } , \dots , { \binom { n } { n } }$ of binomial coefficients

Here $f ( n ) \sim g ( n )$ means that

$$
\operatorname* { l i m } _ { \varkappa \longrightarrow \infty } \frac { f ( \eta ) } { g ( \eta ) } = 1 .
$$

1   
1 1   
1 2 1   
1 3 -3 1   
1 46 41   
1 5 10 10 5 1   
1 6 15 20 15 6 1   
1 7 21 35 35 21 7 1

Pascal's triangle sums to $\sum _ { k = 0 } ^ { n } { \binom { n } { k } } = 2 ^ { n }$ is symmetric: $\binom { \pi } { k } = \binom { \pi } { \pi - k }$

From the functional equation $\textstyle { \binom { n } { k } } = { \frac { n - k + 1 } { k } } { \binom { n } { k - 1 } }$ one easily finds that for every $\mathscr { n }$ the binomial coefficients $( \pi )$ form a equence that is symeric and unimodal: it incrcases towards the middle, so that the middle binomial coefficients are the largest ones in the sequence:

$$
\begin{array} { r } { 1 = { \binom { n } { 0 } } < { \binom { n } { 1 } } < \ldots < { \binom { n } { \lfloor n / 2 \rfloor } } = { \binom { n } { \lceil n / 2 \rceil } } > \ldots > { \binom { n } { n - 1 } } > { \binom { n } { n } } = 1 . } \end{array}
$$

Here $\lfloor x \rfloor$ resp. $\lceil x \rceil$ denotes the number $\vec { x }$ rounded down resp. rounded up to the nearest integer.

From the asymptotic formulas for the factorials mentioned above one can obtain very precise cstimates for the sizes of binomial coefficients. However, we will only need very weak and simple estimates in this book, such as the following: $( \pi ) \leq 2 ^ { n }$ for all $k$ , while for $n \geq 2$ we have

$$
{ \binom { n } { \lfloor n / 2 \rfloor } } \geq { \frac { 2 ^ { n } } { n } } ,
$$

with cquality only for $n = 2$ In particular, for $\gamma _ { \ell } \geq 1$ ,

$$
{ \binom { 2 \pi } { n } } \geq { \frac { \mathrm { 4 } ^ { n } } { 2 n } } .
$$

This holds since $( \lim \limits _ { x  / 2 } ^ { \pi } )$ , amid nial coeffent, is the larges n in the sequence $\binom { n } { 1 } + \binom { n } { n } , \binom { n } { 1 } , \binom { n } { 2 } , \ldots , \binom { n } { n - 1 }$ , whosesum is $2 ^ { n }$ and whose average is thus $\frac { 2 ^ { n } } { n }$

On thc other hand, we note the upper bound for binomial coefficients

$$
{ \binom { n } { k } } \ = \ { \frac { n ( n - 1 ) \cdot \cdot \cdot ( n - k + 1 ) } { k ! } } \leq { \frac { n ^ { k } } { k ! } } \leq { \frac { n ^ { k } } { 2 ^ { k - 1 } } } ,
$$

which is a reasonably good estimate for the "small" binomial coefficients at the tails of the sequence, when $n$ is large (compared to $k$ ).

# References

[1] P. ErDós: Beweis eines Satzes von Tschebyschef, Acta Sci. Math. (Szeged) 5 (1930-32), 194-198.   
[2] R. L. GRAHAM, D. E. KnUTH & O. PATAsHNIK: Concrete MathematiCs. A Foundation for Computer Science, Addison-Wesley, Rcading MA 1989.   
[3] G. H. HARDY & E. M. WRIGHT: An Introduction to the Theory of Numbers, fifth edition, Oxford University Press 1979.   
[4] P. RiBENBOlM: The New Book of Prime Number Records, Springer-Verlag, New York 1989.

# Binomial coefficients are (almost) never powers

There is an epilogue to Bertrand's postulate which leads to a beautiful result on binomial coefficients. In 1892 Sylvester strengthened Bertrand's postulate in the following way:

If $n \geq 2 k$ , then at least one of the numbers $n , n - 1 , \ldots , n - k + 1$ has a prime divisor p greater than $k$ .

Note that for $n = 2 k$ we obtain precisely Bertrand's postulate. In 1934, Erds gave a short and elementary Book Proof of Sylvester's result, running along the lines of his proof of Bertrand's postulate. There is an equivalent way of stating Sylvester's theorem:

The binomial coefficient

$$
{ \binom { n } { k } } \ = \ { \frac { n ( n - 1 ) \cdot \cdot \cdot ( n - k + 1 ) } { k ! } } \qquad ( n \geq 2 k )
$$

always has a prime factor $p > k$ .

With this observation in mind, we turn to another one of Erdôs' jewels. When is $\binom { n } { k }$ equal to a power $m ^ { \ell } ?$ It is easy to see that there are infinitely many solutions for $k = \ell = 2$ , that is, of the equation ${ \binom { n } { 2 } } = m ^ { 2 }$ . Indeed, if $\binom { n } { 2 }$ is a square, then so is ${ \binom { ( 2 n - 1 ) ^ { 2 } } { 2 } }$ . To see this, set $n ( n - 1 ) = 2 m ^ { 2 }$ . It follows that

$$
( 2 n - 1 ) ^ { 2 } ( ( 2 n - 1 ) ^ { 2 } - 1 ) = ( 2 n - 1 ) ^ { 2 } 4 n ( n - 1 ) = 2 ( 2 m ( 2 n - 1 ) ) ^ { 2 } ,
$$

and hence

$$
{ \binom { ( 2 n - 1 ) ^ { 2 } } { 2 } } \ = \ ( 2 m ( 2 n - 1 ) ) ^ { 2 } .
$$

Beginning with ${ \binom { 9 } { 2 } } = 6 ^ { 2 }$ we thus obtain infinitely many solutions — the next one is (289) exaplei ${ \binom { 2 8 9 } { 2 } } = 2 0 4 ^ { 2 }$ However his does not y For ${ \binom { 5 0 } { 2 } } \ = \ 3 5 ^ { 2 }$ $( \mathbf { \lambda ^ { 1 6 8 2 } } ) \ = \ 1 1 8 9 ^ { 2 }$ $k = 3$ it is known that ${ \binom { n } { 3 } } = m ^ { 2 }$ has the unique solution $n = 5 0$ , $m = 1 4 0$ . But now we are at the end of the line. For $k \geq 4$ and any $\ell \geq 2$ no solutions exist, and this is what Erdôs proved by an ingenious argument.

Theorem. The equation ${ \binom { n } { k } } = m ^ { \ell }$ has no integer solutions with $\ell \geq 2$ and $4 \leq k \leq n - 4$

# Chapter 3

$$
{ \binom { 5 0 } { 3 } } = 1 4 0 ^ { 2 }
$$

is the only solution for $k = 3 , \ell = 2$

of. o  h $n \geq 2 k$ because of $( \mathbf { \Sigma } _ { k } ^ { n } ) = ( \mathbf { \Sigma } _ { n - k } ^ { \pi } )$ Suppe $( \pi ) = \pi z ^ { \ell }$ The proof, by contradiction, proceeds in the following four steps.

(1) By Sylvester's theorem, there is a prime factor $I ^ { \gamma }$ of $( \gamma )$ greater than $k$ , hence $p ^ { \ell }$ divides $n ( r \llcorner - 1 ) \cdots ( r \llcorner - \rrangle _ { \ast } + 1 )$ Clearly, only one of the factors $n - i$ can be a multiple of $p$ (because of $p > k$ ), and we conclude $\vartheta ^ { \ell } \mid \eta , - \dot { \ell } ,$ and therefore

$$
n \geq p ^ { \ell } > k ^ { \ell } \geq k ^ { 2 } .
$$

() Consider any factor $n - j$ of the numerator and write it in the form ${ \mathfrak { n } } - { \mathfrak { j } } = a _ { \mathrm { j } } { \mathfrak { m } } _ { \mathrm { j } } ^ { \mathrm { f } }$ ,where $a _ { j }$ is not divisible by any nontrivial $l$ -th power. We note by (1) that $a _ { j }$ has only prime divisors less than or equal to $k$ We want to show next that a; = aj for i ≠ j. Assume to the contrary that ai = aj for some $i < j$ Then $\uparrow \uparrow \uparrow _ { i } \ge \uparrow r \downarrow _ { j } + 1$ and

$$
\begin{array} { r c l } { k } & { > } & { ( n - i ) - ( n - j ) \ = \ a _ { j } ( m _ { i } ^ { \ell } - m _ { j } ^ { \ell } ) \ > \ a _ { j } ( ( m _ { j } + 1 ) ^ { \ell } - m _ { j } ^ { \ell } ) } \\ & { > } & { a _ { j } \ell r m _ { j } ^ { \ell - 1 } \ \geq \ \ell ( a _ { j } m _ { j } ^ { \ell } ) ^ { 1 / 2 } \ \geq \ \ell ( n - k + 1 ) ^ { 1 / 2 } } \\ & { \geq } & { \ell ( \frac { n } { 2 } + 1 ) ^ { 1 / 2 } \ > \ n ^ { 1 / 2 } , } \end{array}
$$

which contradicts $n > k ^ { 2 }$ from above.

() Next we prove that the $a _ { i } \geq s$ are the integers $1 , 2 , \ldots , k$ in some order. (According to Erds, this is the crux of the proof.) Since we already know that they are all distinct, it suffices to prove that

$$
\boldsymbol { \mathscr { a } } _ { 0 } \boldsymbol { \mathscr { a } } _ { 1 } \cdot \cdot \cdot \cdot \boldsymbol { \mathscr { a } } _ { k - 1 } \quad \mathrm { d i v i d e s } \quad k ! .
$$

Substituting ${ \mathfrak { n } } - j = { \mathfrak { a } } _ { j } { \mathfrak { m } } _ { ; j } ^ { \ell }$ into the equation $( x ) = x x ^ { 2 }$ , we obtain

$$
a _ { 0 } a _ { 1 } \cdot \cdot \cdot a _ { k - 1 } ( r n _ { 0 } m _ { 1 } \cdot \cdot \cdot m _ { k - 1 } ) ^ { \ell } = k ! m ^ { \ell } .
$$

Cancelling the common factors of $\mathfrak { f f l } _ { 0 } \cdots \mathfrak { n } \mathfrak { n } _ { k - 1 }$ and m yields

$$
a _ { 0 } a _ { 1 } \cdot \cdot \cdot a _ { k - 1 } u ^ { \hat { \ell } } = k ! v ^ { \hat { \ell } }
$$

with $\operatorname* { g c d } ( \ i , \ i ) = 1$ .It remains to show that $\tau \stackrel { . . } { - } 1$ .If not, then $\mathcal { V }$ contains a prime divisor $p$ Since $\begin{array} { r } { \mathrm { { g c d } } ( u , v ) = 1 } \end{array}$ , $p$ must be a prime divisor of $a _ { 0 } a _ { 1 } \cdots a _ { k - 1 }$ and hence is less than or cqual to $k$ . By the theorem of Lendre ee pg )  o t $k !$ contains $\mathcal { P }$ to the power $\sum \limits _ { i \geq 1 } \left\lfloor \frac { k } { p ^ { i } } \right\rfloor$ . We now estimale the exponent of $p$ in $n ( n - 1 ) \cdots ( n - k + 1 )$ .Let $i$ be a positive integer, and let $b _ { 1 } < b _ { 2 } < \ldots < b _ { s }$ be the multiples of $p ^ { i }$ among $n , n - 1 , \ldots , n - k + 1$ Then $\ b  \ b  \ b  \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b \ b { \ b { \ b { \ b { \ b \ b { \ b { \ b { \ b \ b { \ b { \ b } { \ b \ b { \ b { \ b \ b { \ b { \ b } \ b { \ b { \ b { \ b \ b { \ b } { \ b \ b { \ b { \ b } \ b { \ b { \ b } \ b { \ b { \ b } \ b { \ b { \ b } \ b { \ b { \ b } \ b { \ b { \ b } \ b { \ b { \ b } \ b { \ b { \ b } \ b { \ b } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } }$ and hence

$$
( s - 1 ) p ^ { i } = b _ { s } - b _ { 1 } \leq n - ( n - k + 1 ) = k - 1 ,
$$

which implies

$$
s \leq \Big \lfloor \frac { k - 1 } { p ^ { i } } \Big \rfloor + 1 \leq \Big \lfloor \frac { k } { p ^ { i } } \Big \rfloor + 1 .
$$

So for each $i$ the number of multiples of $\boldsymbol { y } ^ { i }$ among $r _ { 1 } , \ldots , r _ { l } - k + 1$ , and hence among the $a _ { j } { \bf \ddot { s } }$ , is bounded by $\textstyle { \left\lfloor { \frac { k } { p ^ { i } } } \right\rfloor + 1 }$ This implies that the exponent of $p$ in $i \mathrm { { I } } , _ { 0 } / 1 1 \cdot \cdot \cdot \langle \lambda _ { k - 1 }$ is at most

$$
\sum _ { i = 1 } ^ { \ell - 1 } \Big ( \Big \lfloor \frac { k } { p ^ { i } } \Big \rfloor + 1 \Big )
$$

with the reasoning that we used for Legendre's theorem in Chapter 2. The only difference is that this time the sum stops at $i = \ell  1$ , since the $a _ { j } ^ { \prime } \mathbf { s }$ contain no $\ell .$ -th powers.

Taking both counts together, we find that the exponent of $p$ in $v ^ { \ell }$ is at most

$$
\sum _ { i = 1 } ^ { \ell - 1 } \Big ( \Big \lfloor \frac { k } { p ^ { i } } \Big \rfloor + 1 \Big ) - \sum _ { i \geq 1 } \Big \lfloor \frac { k } { p ^ { i } } \Big \rfloor \ \leq \ \ell - 1 ,
$$

and we have our desired contradiction, since ${ \boldsymbol { \imath } } ; { \boldsymbol { \ell } }$ is an $\ell$ th power.

This suffices already to settle the case $\ell = 2$ .Indeed, since $k \geq 4$ one of the $a _ { i }$ 's must be equal to 4, but the $( \boldsymbol { \lambda } _ { i } ^ { \flat } \boldsymbol { \mathsf { S } }$ contain no squares. So let us now assume that $\ell \geq 3$ .

(4) Since $k \geq 4$ , we must have $a _ { i _ { 1 } } = 1 , a _ { i _ { 2 } } = 2 , a _ { i _ { 3 } } = 4$ for some $i _ { 1 } , i _ { 2 } , i _ { 3 }$ , that is,

$$
n - i _ { 1 } = m _ { 1 } ^ { \ell } , ~ n - i _ { 2 } = 2 m _ { 2 } ^ { \ell } , ~ n - i _ { 3 } = { \it 4 } m _ { 3 } ^ { \ell } .
$$

We claim that $( r \imath - i _ { 2 } ) ^ { 2 } \neq ( n - i _ { 1 } ) ( n - i _ { 3 } )$ If not, put $b = \tau \ i - i _ { 2 }$ and $n _ { \hexagon } - i _ { 1 } = b - x , n _ { \hexagon } - i _ { 3 } = b + y$ , where ${ \mathfrak { l } } < | x | , | y | < k$ Hence

$$
b ^ { 2 } = ( b - x ) ( b + y ) \mathrm { o r } ( y - x ) b = x y ,
$$

where $x  ; y$ is plainly impossible. Now we have by part (1)

$$
| x y | ~ = ~ b | y - x | ~ \geq ~ b ~ > ~ n - k ~ > ~ ( k - 1 ) ^ { 2 } ~ \geq ~ | x y | ,
$$

which is absurd.

So we have $r r _ { 2 } ^ { 2 } \neq m _ { 1 } \eta n _ { 3 }$ , where we assume $m _ { 2 } ^ { 2 } > r r _ { 1 } m _ { 3 }$ (the other case being analogous), and proceed to our last chains of inequalities. We obtain

$$
\begin{array} { l c l c l } { { 2 ( k - 1 ) n } } & { { > } } & { { n ^ { 2 } - ( n - k + 1 ) ^ { 2 } ~ > } } & { { ( n - i _ { 2 } ) ^ { 2 } - ( n - i _ { 1 } ) ( n - i _ { 3 } ) } } \\ { { } } & { { = } } & { { { \cal { A } } [ m _ { 2 } ^ { 2 \ell } \cdot ~ ( m _ { 1 } m _ { 3 } ) ^ { \ell } ] ~ \geq } } & { { { \cal { A } } [ ( m _ { 1 } m _ { 3 } + 1 ) ^ { \ell } - ( m _ { 1 } m _ { 3 } ) ^ { \ell } ] } } \\ { { } } & { { \geq } } & { { { \cal { A } } \ell m _ { 1 } ^ { \ell - 1 } m _ { 3 } ^ { \ell - 1 } , } } \end{array}
$$

Since $\ell \geq 3$ and $n > k ^ { \ell } \geq k ^ { 3 } > 6 k$ , this yields

$$
\begin{array} { r c l } { { 2 ( k - 1 ) n m _ { 1 } m _ { 3 } } } & { { > } } & { { 4 \ell m _ { 1 } ^ { \ell } m _ { 3 } ^ { \ell } \ = \ \ell ( n - i _ { 1 } ) ( n - i _ { 3 } ) } } \\ { { } } & { { > } } & { { \ell ( n - k + 1 ) ^ { 2 } \ > \ 3 ( n - { \displaystyle \frac { n } { 6 } } ) ^ { 2 } \ > \ 2 n ^ { 2 } . } } \end{array}
$$

We see that our analysis so far agrees with ${ \binom { 5 0 } { 3 } } = 1 4 0 ^ { 2 }$ , as

$$
\begin{array} { c } { 5 0 = 2 \cdot 5 ^ { 2 } } \\ { 4 9 = 1 \cdot 7 ^ { 2 } } \\ { 4 8 = 3 \cdot 4 ^ { 2 } } \end{array}
$$

Now since $m _ { i } \le n ^ { 1 / \ell } \le n ^ { 1 / 3 }$ we finally obtain

$$
k n ^ { 2 / 3 } \geq k m _ { 1 } m _ { 3 } > ( k - 1 ) m _ { 1 } m _ { 3 } > n ,
$$

or $k ^ { 3 } > n$ .With this contradiction, the proof is complete.

# References

[1] P. ERDÖs: A theorem of Sylvester and Schur, J. London Math. Soc. 9 (1934),   
282-288. [2] P. ERDôs: On a diophantine equation, J. London Math. Soc. 26 (1951),   
176-178. [3] J. J. SYLVESTER: On arithmetical series, Messenger of Math. 21 (1892), 1-19,   
87-120; Collected Mathematical Papers Vol. 4, 1912, 687-731.

# Representing numbers as sums of two squares

Which numbers can be written as sums of two squares?

This question is as old as number theory, and its solution is a classic in the field. The "hard" part of the solution is to see that every prime number of the form $4 m + 1$ is a sum of two squares. G. H. Hardy writes that this two square theorem of Fermat "is ranked, very justly, as one of the finest in arithmetic." Nevertheless, one of our Book Proofs below is quite recent.

Let's start with some "warm-ups." First, we need to distinguish between the prime $p = 2$ , the primes of the form $p = 4 m + 1$ , and the primes of the form $p = 4 m + 3$ Every prime number belongs to exactly one of these three classes. At this point we may note (using a method $\mathbf { \ddot { a } }$ la Euclid") that there are infinitely many primes of the form $4 m + 3$ In fact, if there were only finitely many, then we could take $p _ { k }$ to be the largest prime of this form. Setting

$$
N _ { k } \ : = \ 2 ^ { 2 } \cdot 3 \cdot 5 \cdot \cdot \cdot p _ { k } - 1
$$

(where $p _ { 1 } = 2 , p _ { 2 } = 3 , p _ { 3 } = 5$ , . . . denotes the sequence of all primes), we find that $N _ { k }$ is congruent to 3 (mod 4), so it must have a prime factor of the form $4 m + 3$ , and this prime factor is larger than $p _ { k }$ — contradiction. At the end of this chapter we will also derive that there are infinitely many primes of the other kind, $p = 4 m + 1$ .

Our first lemma is a special case of the famous "law of reciprocity": It characterizes the primes for which $- 1$ is a square in the field $\mathbb { Z } _ { p }$ (which is reviewed in the box on the next page).

Lemma 1. For primes $p = 4 m + 1$ the equation $s ^ { 2 } \equiv - 1 ( \mathbf { m o d } p )$ has two solutions $s \in \{ 1 , 2 , . . . , p { - } 1 \}$ for $p = 2$ there is one such solution, while for primes of the form $p = 4 m + 3$ there is no solution.

Proof. For $p = 2$ take $s = 1$ .For odd $p$ , we construct the equivalence relation on $\{ 1 , 2 , \dotsc , p - 1 \}$ that is generated by identifying every element with its additive inverse and with its multiplicative inverse in $\mathbb { Z } _ { p }$ Thus the "general" equivalence classes will contain four elements

$$
\{ x , - x , { \overline { { x } } } , - { \overline { { x } } } \}
$$

since such a 4-element set contains both inverses for all its elements. However, there are smaller equivalence classes if some of the four numbers are not distinct:

![](images/aefc92d5b7fd2b9d800168d0c7a12d1a7ed159fad27c868003454ea8d690b826.jpg)

Pierre de Fermat

: $z \equiv - x$ is impossible for odd $p$ .   
• $x \equiv \overline { { x } }$ is equivalent to $x ^ { 2 } \equiv 1$ .This has two solutions, namely $x = 1$ and ${ \mathfrak { x } } = { \mathfrak { p } } - 1$ , leading to the equivalence class $\{ 1 , p - 1 \}$ of size 2.   
• $x \equiv - \overline { { x } }$ is equivalent to $x ^ { 2 } \equiv - 1$ . This equation may have no solution or two distinct solutions $x _ { 0 } , p \gets x _ { 0 }$ : in this case the equivalence class is $\left\{ x _ { 0 } , p - x _ { \mathrm { { 0 } } } \right\}$ .

For ${ \mathfrak { p } } = 1 1$ the partition is $\{ 1 , 1 0 \} , \{ 2 , 9 , 6 , 5 \} , \{ 3 , 8 , 4 , 7 \} \cdots$ . for $p = 1 3$ it is $\{ 1 , 1 2 \} , \{ 2 , 1 1 , 7 , 6 \} , \{ 3 , 1 0 , 9 , 4 \} ,$ $\{ 5 , 8 \}$ : the pair $\{ 5 , 8 \}$ yields the two solutions of $s ^ { 2 } \equiv - 1$ mod 13.

![](images/0002f57b70ceafb00ee1a4bb4967815839a1327214ba585e0f4b39a724d7480e.jpg)

![](images/3f6148deea2d597344c8b0521194ce5e0210a1ece39872cffc962f1f91c66710.jpg)

Addition and multiplication in $\mathbb { Z } _ { 5 }$

The set $\{ 1 , 2 , \dotsc , p - 1 \}$ has ${ \mathfrak { p } } - 1$ elements, and we have partitioned it into quadruples (equivalence classes of size 4), plus one or two pairs (equivalence classes of size 2). For $p - 1 = 4 \eta + 2$ we find that there is only the one pair $\{ 1 , p - 1 \}$ , the rest is quadruples, and thus $s ^ { 2 } \equiv - 1 ( { \bmod { p } } )$ has no solution. For $y \mathbf { \mathbf { \mathbf { ) } } } - 1 = 4 \mathfrak { m }$ there has to be the second pair, and this contains the two solutions of $s ^ { 2 } \equiv - 1$ that we were looking for. □

# Prime fields

If $p$ is a prime, then the set $\mathbb { Z } _ { p } = \{ 0 , 1 , \ldots , p - 1 \}$ with addition and multiplication defined "modulo $p ^ { \prime \prime }$ forms a finite field. We will need the following simple properties:

$\bullet$ For $x \in \mathbb { Z } _ { \mathfrak { p } }$ , $x \neq 0$ , the additive inverse (for which we usually write $- { \mathfrak { x } } )$ is given by $p - x \in \{ 1 , 2 , . . . , p - 1 \}$ . If $p > 2$ , then $\pmb { x }$ and $- x$ are different elements of $\mathbb { Z } _ { p }$ .   
Each $x \in \mathbb { Z } _ { \mathfrak { p } } \backslash \{ 0 \}$ has a unique multiplicative inverse $\overline { { x } } \in \mathbb { Z } _ { p } \backslash \{ 0 \}$ with $\mathbf { \tilde { z } } \mathbf { \overline { { z } } } \equiv 1 \ ( \mathbf { m o d } p )$ . The definition of primes implies that the map $\mathbb { Z } _ { \mathbb { p } }  \mathbb { Z } _ { \mathbb { p } }$ , $z \mapsto x z$ is injective for $x \neq 0$ ,Thus on the finite set $\mathbb { Z } _ { p } \backslash \{ 0 \}$ it must be surjective as well, and hence for each $_ x$ there is a unique $\overline { { x } } \neq 0$ with $x { \overline { { x } } } \equiv 1 ( { \bmod { p } } )$ .   
The squares ${ \mathfrak { 0 } } ^ { 2 } , 1 ^ { 2 } , 2 ^ { 2 } , \ldots , h ^ { 2 }$ define different elements of $\mathbb { Z } _ { \mathbf { \mathcal { P } } }$ , for $h = \lfloor \frac { p } { 2 } \rfloor$ . This is since $x ^ { 2 } \equiv y ^ { 2 }$ , or $( x + y ) ( x - y ) \equiv 0$ implies that $x \equiv y$ or that $x \equiv - y$ .The $1 + \lfloor { \frac { \mathtt { p } } { 2 } } \rfloor$ elements $0 ^ { 2 } , 1 ^ { 2 } , \ldots , h ^ { 2 }$ are called the squares in $\mathbb { Z } _ { \mu }$ .

At this point, let us note "on the fly" that for $a l l$ primes there are solutions for $x ^ { 2 } + y ^ { 2 } \equiv - 1 ( \mathrm { m o d } p )$ . In fact, there are $\lfloor \frac { p } { 2 } \rfloor + 1$ distinct squares $x ^ { 2 }$ in $\mathbb { Z } _ { \mathbf { \mathcal { P } } }$ , and there are $[ \frac { p } { 2 } ] + 1$ distinct numbers of the form $- ( 1 + y ^ { 2 } )$ . These two sets of numbers are too large to be disjoint, since $\mathbb { Z } _ { \mathfrak { p } }$ has only $p$ elements, and thus there must exist $\mathcal { X }$ and $y$ with $x ^ { 2 } \equiv - ( { \bf 1 } + { y } ^ { 2 } )$ (mod p).

Lemma 2. No number ${ \mathfrak { n } } = { \mathfrak { 1 } } { \mathfrak { n } } . + 3$ is $\alpha$ sum of two squares.

Proof. The square of any even number is $( 2 k ) ^ { 2 } = 4 k ^ { 2 } \equiv 0 ( \mathrm { m o d } 4 )$ , while squares of odd numbers yield $( 2 k + 1 ) ^ { 2 } = 4 ( k ^ { 2 } + k ) + 1 \equiv 1 ( \mathrm { m o d } 4 )$ . Thus any sum of two squares is congruent to 0, 1 or 2 (mod 4). □

This is enough evidence for us that the primes $p = 4 \eta _ { \ell } + 3$ are "bad." Thus, we proceed with "good" properties for primes of the form $p = 4 \mathfrak { n } + 1$ . On the way to the main theorem, the following is the key step.

Proposition. Every prime of the form $p = 4 \eta _ { \ell } + 1$ is a sum of two squares, that is, it can be written as ${ \boldsymbol { p } } = { \boldsymbol { x } } ^ { 2 } + { \boldsymbol { y } } ^ { 2 }$ for some natural numbers $x$ , $y \in N$ .

We shall present here two proofs of this result -— both of them elegant and surprising. The first proof features a striking application of the "pigeonhole principle" (which we have already used "on the fy" before Lemma 2; see Chapter 22 for more), as well as a clever move to arguments "modulo p" and back. The idea is due to the Norwegian number theorist Axel Thue.

Proof. Consider the pairs $( x ^ { \prime } , y ^ { \prime } )$ of integers with $0 \leq x ^ { \prime } , y ^ { \prime } \leq \sqrt { p }$ , that is, $x ^ { \prime } , y ^ { \prime } \in \{ 0 , 1 , . . . , \lfloor \sqrt { \mathcal { R } } \rfloor \}$ There are $( \lfloor { \sqrt { p } } \rfloor + 1 ) ^ { \frac { 2 } { 2 } }$ such pairs. Using the estimate $\lfloor x \rfloor + 1 > x$ for $x = \sqrt { p }$ , we see that we have more than $p$ such pairs of integers. Thus for any $s \in \mathbb { Z }$ , it is impossible that all the values $x ^ { \prime } - s y ^ { \prime }$ produced by the pairs $( x ^ { \prime } , y ^ { \prime } )$ are distinct modulo $p$ That is, for every $s$ there are two distinct pairs

$$
( x ^ { \prime } , y ^ { \prime } ) , \ ( x ^ { \prime \prime } , y ^ { \prime \prime } ) \in \{ 0 , 1 , . . . , \lfloor \sqrt { p } \rfloor \} ^ { 2 }
$$

with

$$
x ^ { \prime } - s y ^ { \prime } \equiv x ^ { \prime \prime } - s y ^ { \prime \prime } ( \mathrm { m o d } p ) .
$$

Now we take differences: We have $x ^ { \prime } \sim x ^ { \prime \prime } \equiv s ( y ^ { \prime } - y ^ { \prime \prime } ) ( { \mathrm { m o d } } p )$ Thus if we define

$$
x : = | x ^ { \prime } - x ^ { \prime \prime } | , \quad y : = | y ^ { \prime } - y ^ { \prime \prime } | .
$$

then we get

$$
( x , y ) \in \{ 0 , 1 , \ldots , \lfloor { \sqrt { p } } \rfloor \} ^ { 2 } \quad { \mathrm { w i t h } } \quad x \equiv \pm s y ( { \bmod { p } } ) .
$$

Also we know that not both $x$ and $y$ can be zero, because the pairs $( x ^ { \prime } , y ^ { \prime } )$ and $( x ^ { \prime \prime } , y ^ { \prime \prime } )$ are distinct.

Now let $s$ be a solution of $s ^ { 2 } \ { \stackrel { \ldots } { = } } \ - 1 ( \mathrm { m o d } p )$ , which exists by Lemma 1. Then $x ^ { 2 } \equiv s ^ { 2 } y ^ { 2 } \equiv - y ^ { 2 } ( { \bmod { p } } )$ , and so we have produced

$$
( x , y ) \in \mathbb { Z } ^ { 2 } \quad \mathrm { ~ w i t h ~ } \quad 0 < x ^ { 2 } + y ^ { 2 } < 2 p \quad \mathrm { ~ a n d ~ } \quad x ^ { 2 } + y ^ { 2 } \equiv 0 ( \mathrm { m o d } p ) .
$$

But $p$ is the only number between () and $2 p$ that is divisible by $p$ Thus $\gamma ^ { 2 } + y ^ { 2 } = p$ done!

Our second proof for the proposition — also clearly a Book Proof — was discovered by Roger Heath-Brown in 1971 and appeared in 1984. (A condensed "one-sentence version" was given by Don Zagier.) It is so elementary that we don't even need to use Lemma 1.

Heath-Brown's argument features three linear involutions: a quite obvious one, a hidden one, and a trivial one that gives "the final blow." The second, unexpected, involution corresponds to some hidden structure on the set of integral solutions of the equation $4 x y + z ^ { 2 } = p .$ .

For $p ~ = ~ 1 3$ $\lfloor { \sqrt { p } } \rfloor ~ = ~ 3$ we consider $\mathbf { x } ^ { \prime } , y ^ { \prime } \in \{ 0 , 1 , 2 , 3 \}$ . For $s = 5$ , the sum $\mathbf { x } ^ { \prime } - s y ^ { \prime } \ ( \mathrm { m o d } \ 1 3 )$ assumes the following values:

$$
\begin{array} { c } { { { \ x } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \prime } } } ^ { { \scriptstyle { \prime } } ^ { { \scriptstyle { \prime } } ^ { { \prime } } } } } } } } } } } } } } } } } } } } } } } } } } } \\ { { { { { \begin{array} { c } { { { 1 } } } \\ { { { { 1 } } } \\ { { { { 2 } } } \\ { { { 3 } } } \end{array} } } } } } } \end{array} }  | \begin{array} {array} { l l l l l } { { { \scriptstyle { 1 } } } } & { { { \scriptstyle { 1 } } } } & { { { \scriptstyle { 2 } } } } & { { { \scriptstyle { 3 } } } } \\ { { { \scriptstyle { 3 } } } } & { { { \scriptstyle { 8 } } } } & { { { \scriptstyle { 3 } } } } & { { { \scriptstyle { 1 1 } } } } \\ { { { \scriptstyle { 1 } } } } & { { { \scriptstyle { 9 } } } } & { { { \scriptstyle { 4 } } } } & { { { \scriptstyle { 1 2 } } } } \\ { { { \scriptstyle { 2 } } } } & { { { \scriptstyle { 1 0 } } } } & { { { \scriptstyle { 5 } } } } & { { { \scriptstyle { 0 } } } } \\ { { { \scriptstyle { 3 } } } } &    \end{array}
$$

Proof. We study the set

![](images/8c27cb1b657931b615dfc38e68a8aab62f7a54eaf50ebc97971fd483b6569662.jpg)

$$
S \ : = \ \{ ( x , y , z ) \in \mathbb { Z } ^ { 3 } : 4 x y + z ^ { 2 } = p , \quad x > 0 , \quad y > 0 \} .
$$

This set is finite. Indeed, $x \ge 1$ and $y \geq 1$ implies $y \leq \frac { p } { 4 }$ and $x \leq \frac { p } { 4 }$ . So the  y ney may sse v for $\mathcal { X }$ and $y$ , and given $x$ and $y$ there are at most two values for $z$ .

The first linear involution is given by

$$
f : S \longrightarrow S , \quad ( x , y , z ) \longmapsto ( y , x , - z ) ,
$$

that is, "interchange $x$ and $y$ , and negate $z$ " This clearly maps $S$ to itself, and it is an involution: Applied twice, it yields the identity. Also, $f$ has no fixed points, since $z = 0$ would imply $p = 4 x y$ which is impossible. Furthermore, $f$ maps the solutions in

$$
\textit { T } : = \{ ( x , y , z ) \in S : z > 0 \}
$$

to the solutions in $S \backslash T$ , which satisfy $\smash { z < 0 }$ Also, $f$ reverses the signs of $x - y$ and of $z$ , so it maps the solutions in

$$
U ~ : = ~ \{ ( x , y , z ) \in S : ( x - y ) + z > 0 \}
$$

to the solutions in $S \backslash U$ . For this we have to see that there is no solution with $( x - y ) + z = 0$ , but there is none since this would give $p = 4 x y + z ^ { 2 } =$ $4 x y + ( x - y ) ^ { 2 } = ( x + y ) ^ { 2 }$ .

What do we get from the study of $f ^ { i } !$ The main observation is that since $f$ maps the sets $T$ and $U$ to their complements, it also interchanges the elements in $T \backslash U$ with these in $U \backslash T$ That is, there is the same number of solutions in $U$ that are not in $T$ as there are solutions in $T$ that are not in $U$ — $T$ and $U$ have the same cardinality.

2The second involution that we study is an involution on the set $U$ :

$$
g : U \longrightarrow U , \quad ( x , y , z ) \longmapsto ( x - y + z , y , 2 y - z ) .
$$

First we check that indeed this is a well-defined map: If $( x , y , z ) \in U ^ { \prime }$ , then $x - y + z > 0 , y > 0$ and $4 ( x - y + z ) y + ( 2 y - z ) ^ { 2 } = 4 x y + z ^ { 2 }$ , so $y ( x , y , z ) \in S$ By $( x - y + z ) - y + ( 2 y - z ) = x > 0$ we find that indeed $g ( x , y , z ) \in U$ .

Also $g$ is an involution: $g ( x , y , z ) = ( x - y + z , y , 2 y - z )$ is mapped by $g$ to $\displaystyle ( ( x - y + z ) - y + ( 2 y - z ) , y , 2 y - ( 2 y - z ) ) = ( x , y , z )$ .

And finally: $g$ has exactly one fixed point:

$$
( x , y , z ) ~ = ~ g ( x , y , z ) ~ = ~ ( x - y + z , y , 2 y - z )
$$

7 y U

holds exactly if $y = z$ But then $p = 4 x y + y ^ { 2 } = ( 4 x + y ) y$ , which holds only for y = 1 = z, and x = p−1.

But if $g$ is an involution on $U$ that has exactly one fixed point, then the cardinality of $U$ is odd.

3. The third, trivial, involution that we study is the involution on $T$ that interchanges $x$ and $y$ :

$$
h : T \longrightarrow T , \quad ( x , y , z ) \longmapsto ( y , x , z ) .
$$

This map is clearly well-defined, and an involution. We combine now our knowledge derived from the other two involutions: The cardinality of $T$ is equal to the cardinality of $U$ , which is odd. But if $h$ is an involution on a finite set of odd cardinality, then it has a fixed point: There is a point $( x , y , z ) \in T$ with $x = y$ , that is, a solution of

$$
p = 4 x ^ { 2 } + z ^ { 2 } = ( 2 x ) ^ { 2 } + z ^ { 2 } .
$$

Note that this proof yields more — the number of representations of $p$ in the form $p = x ^ { 2 } + ( 2 y ) ^ { 2 }$ is odd for all primes of the form $p = 4 m + 1$ . (The representation is actually unique, see [3].) Also note that both proofs are not effective: Try to find $x$ and $y$ for a ten digit prime! Efficient ways to find such representations as sums of two squares are discussed in [1] and [7].

The following theorem completely answers the question which started this chapter.

Theorem. A natural number n can be represented as a sum of two squares if and only if every prime factor of the form $p = 4 \eta \eta + 3$ appears with an even exponent in the prime decomposition of $n$ .

Proof. Call a number $\mathscr { n }$ representable if it is a sum of two squares, that is, if $\mathfrak { r } = \mathfrak { x } ^ { 2 } + \mathfrak { y } ^ { 2 }$ for some ${ \mathfrak { x } } , { \mathfrak { y } } \in \mathbb { N } _ { 0 }$ . The theorem is a consequence of the following five facts.

(1) $\mathsf { 1 } = \mathsf { 1 } ^ { \mathsf { 2 } } + \mathsf { 0 } ^ { \mathsf { 2 } }$ and $2 = 1 ^ { 2 } + 1 ^ { 2 }$ are representable. Every prime of the form ${ \mathfrak { p } } = 4 { \mathfrak { m } } + 1$ is representable.   
(The product of any two representable numbers ${ \mathfrak { n } } _ { 1 } = x _ { 1 } ^ { 2 } + y _ { 1 } ^ { 2 }$ and $n _ { 2 } =$ $x _ { 2 } ^ { 2 } + y _ { 2 } ^ { 2 }$ is representable: $n _ { 1 } n _ { 2 } = ( x _ { 1 } x _ { 2 } + y _ { 1 } y _ { 2 } ) ^ { 2 } + ( x _ { 1 } y _ { 2 } - x _ { 2 } y _ { 1 } ) ^ { 2 }$ .   
If $\mathcal { U }$ is representable, $\mathfrak { x } = \mathfrak { x } ^ { 2 } + \mathfrak { y } ^ { 2 }$ , then also $\hbar \tilde { \dot { z } } ^ { 2 }$ is representable, by $n z ^ { 2 } = ( x z ) ^ { 2 } + ( y z ) ^ { 2 }$ .

Facts (1). (2) and (3) together yield the "" part of the theorem.

4If $p = 4 m + 3$ is a prime that divides a representable number $\begin{array} { r l } { \pmb { \mathcal { T } } \pmb { \mathbb { \tilde { \imath } } } } & { { } = } \end{array}$ $x ^ { 2 } + y ^ { 2 }$ , then $p$ divides both $_ x$ and $y$ , and thus $p ^ { 2 }$ divides $n$ In fact, if we had $x \not \equiv 0 ( { \mathrm { m o d } } { p } )$ , then we could find $\overline { { \mathcal { X } } }$ such that $\mathbf { \tilde { \mathbf { \Gamma } } } _ { L } \mathbf { \overline { { \mathbf { \Gamma } } } } \equiv 1 \ ( \mathbf { m o d } \ p )$ multiply the equation $x ^ { 2 } + y ^ { 2 } \equiv 0$ by $\textstyle { { \overline { { x } } } ^ { 2 } }$ , and thus obtain $1 + y ^ { 2 } { \overline { { x } } } ^ { 2 } = { }$ $1 + ( { \overline { { x } } } y ) ^ { 2 } \ \equiv \ 0 ( { \bmod { p } } )$ , which is impossible for $p \ = \ 4 m \cdot 3$ by Lemma 1.

(5If $n$ is representable, and $p = 4 \eta \eta + 3$ divides $n$ , then $p ^ { 2 }$ divides $n$ , and $\eta / p ^ { 2 }$ is representable. This follows from (4), and completes the proof. □

![](images/69ad21493af7b2505197cf67d289c2127c59356c542ae390f8f2e10aa56ac224.jpg)

On a finite set of odd cardinality, every involution has at least one fixed point.

As a corollary, we obtain that there are infinitely many primes of the form $p = 4 \mathfrak { m } + 1$ . For this, we consider

$$
M _ { k } = ( 3 \cdot 5 \cdot 7 \cdot \cdot \cdot p _ { k } ) ^ { 2 } + 2 ^ { 2 } ,
$$

a number that is congruent to $1 \ \{ \bmod { 4 } \}$ . All its prime factors are larger than $p _ { k }$ , and by fact (4) cf the previous proof, it has no prime factors of the form $4 m + 3$ Thus $M _ { k }$ has a prime factor of the form $4 m + 1$ that is larger than Pk.

Two remarks close our discussion:

• If $a$ and $b$ are two natural numbers that are relatively prime, then there are infinitely many primes of the form $a m + b$ $( \gamma ) \in \mathbb { N } )$ — this is a famous (and difficult) theorem of Dirichlet. More precisely, one can show that the number of primes $p \leq x$ of the form $p = a m + b$ is described very accurately for large $\therefore i .$ by the function where (x) denotes the number of $b$ with $1 \leq b < a$ that are relatively prime to $a$ (This is a substantial refinement of the prime number theorem, which we had discussed on page 10.)   
This means that the primes for fixed $a$ and varying $b$ appear essentially at the same rate. Nevertheless, for example for $a = 4$ one can observe a rather subtle, but nevertheless noticable and persistent tendency towards "more" primes of the form $4 \gamma \gamma _ { l } + 3$ : If you look for a large random $x$ , then chances are that there are more primes $p \leq x$ of the form $p = 4 \eta \eta + 3$ than of the form $p = 4 \mathfrak { m } + 1$ .This effect is known as "Chebyshev's bias"; see Riesel [4] and Rubinstein and Sarnak [5].

# References

[I] F. W. CLARKE, W. N. EVERITT, L. L. LITTLEJOHN & S. J. R. VORSTER: H. J. S. Smith and the Fermat Two Squares Theorem, Amer. Math. Monthly 106 (1999), 652-665.   
[2] D. R. HEATH-BROwN: Fermar's two squares theorem, Invariant (1984), 2-5.   
[3] 1. NIVEN & H. S. ZUCKERMAN: An Introduction to the Theory of Numbers, Fifth edition, Wiley, New York 1972.   
[4] H. RIEsEL: Prime Numbers and Computer Methods for Factorization, Second edition, Progress in Mathematics 126, Birkhäuser, Boston MA 1994.   
[5] M. RUBINSTEIN & P. SARNAK: Chebyshev's bias, Experimental Mathematics 3 (1994), 173-197.   
[6] A. THuE: Et par antydninger til en taltheoretisk metode, Kra. Vidensk. Selsk. Forh. 7 (1902), 57-75.   
[7] S. WaGon: Editor's corner: The Euclidean algorithm strikes again, Amcr. Math. Monthly 97 (1990), 125-129.   
|8] D. ZAGIER: A one-sentence proof that every prime $p \equiv 1 { \ : } ( \mathrm { m o d } 4 )$ is a sum of two squares, Amcr. Math. Monthly 97 (1990), 144.

# Every finite division ring is a field

Rings are important structures in modern algebra. If a ring $R$ has a multiplicative unit element 1 and every nonzero element has a multiplicative inverse, then $R$ is called a division ring. So, all that is missing in $R$ from being a field is the commutativity of multiplication. The best-known example of a non-commutative division ring is the ring of quaternions discovered by Hamilton. But, as the chapter title says, every such division ring must of necessity be infinite. If $R$ is finite, then the axioms force the multiplication to be commutative.

This result which is now a classic has caught the imagination of many mathematicians, because, as Herstein writes: "It is so unexpectedly interrelating two seemingly unrelated things, the number of elements in a certain algebraic system and the multiplication of that system."

Theorem. Every finite division ring R is commutative.

This beautiful theorem which is usually attributed to MacLagan Wedderburn has been proved by many people using a variety of different ideas. Wedderburn himself gave three proofs in 1905, and another proof was given by Leonard E. Dickson in the same year. More proofs were later given by Emil Artin, Hans Zassenhaus, Nicolas Bourbaki, and many others. One proof stands out for its simplicity and elegance. It was found by Ernst Witt in 1931 and combines two elementary ideas towards a glorious finish.

Proof. Our first ingredient comes from a blend of linear algebra and basic group theory. For an arbitrary element $s \in R$ , let $C _ { s }$ be the set $\{ x \in R : x s = s x \}$ of elements which commute with $s$ ; $C _ { s }$ is called the centralizer of $s$ Clearly, $C _ { s }$ contains 0 and 1 and is a sub-division ring of $R$ The center $Z$ is the set of elements which commute with all elements of $R$ , thus $\begin{array} { r } { Z = \bigcap _ { s \in R } C _ { s } } \end{array}$ In picular, all elents f $Z$ commute, 0 and 1 are in $Z$ , and so $Z$ is a finite field. Let us set $| Z | = q$ .

We can regard $R$ and $C _ { s }$ as vector spaces over the field $Z$ and deduce that $| R | = q ^ { n }$ , where $_ n$ is the dimension of the vector space $R$ over $Z$ , and similarly $| C _ { s } | = q ^ { n _ { s } }$ for suitable integers $n _ { s } \geq 1$ .

Now let us assume that $R$ is not a field. This means that for some $s \in R$ the centralizer $C _ { s }$ is not all of $R$ , or, what is the same, $n _ { s } < n$ .

On the set $R ^ { * } : = R \backslash \{ 0 \}$ we consider the relation

$$
r ^ { \prime } \sim r \quad : \Longleftrightarrow \quad r ^ { \prime } = x ^ { - 1 } r x \quad { \mathrm { f o r ~ s o m e ~ } } x \in R ^ { * }
$$

![](images/42e6db96aeb35b80ff6f6163b222f9ee3430f972ea82df2281fe190ac00e12ad.jpg)

Ernst Witt

It is easy to check that $\sim$ is an equivalence relation. Let

$$
\mathcal { A } _ { s } ~ : = ~ \{ x ^ { - 1 } s x : x \in \bar { R } ^ { * } \}
$$

be the equivalence class containing s. We note that $| { \mathcal A } _ { s } | = 1$ precisely when s is in the center $\boldsymbol { Z }$ So by our assumption, there are classes $A _ { s }$ with $| \varLambda _ { \mathfrak { s } } | \geq 2$ Consider now for $s \in R ^ { * }$ the map $f _ { s } : x \longmapsto x ^ { \cdot } { } ^ { 1 } s x ^ { \cdot }$ from $R ^ { * }$ onto $A _ { s }$ . For $x , y \in R ^ { * }$ we find

$$
\begin{array} { l l l l } { x ^ { - 1 } s x = y ^ { - 1 } s y } & { \Longleftrightarrow } & { ( y x ^ { - 1 } ) s = s ( y x ^ { - 1 } ) } \\ & { \Longleftrightarrow } & { y x ^ { - 1 } \in C _ { s } ^ { * } \Longleftrightarrow } & { y \in C _ { s } ^ { * } x , } \end{array}
$$

for $C _ { s } ^ { * } : = C _ { s } \backslash \{ 0 \}$ , where $C _ { s } ^ { * } x = \{ z x : z \in C _ { s } ^ { * } \}$ has size $\left| C _ { s } ^ { \star } \right|$ Hence any element ${ x ^ { - 1 } } { \mathfrak { s x } }$ is the image of precisely $| \mathcal { \bar { C } } _ { s } ^ { * } | = \mathrm { q } ^ { \pi _ { s } } - 1$ elements in $R ^ { * }$ under the map $f _ { s }$ , and we deduce $\left| { \cal R } ^ { * } \right| = \left| A _ { s } \right| \left| C _ { s } ^ { * } \right|$ . In particular, we note that

$$
\frac { | R ^ { * } | } { | C _ { s } ^ { * } | } = \frac { q ^ { n } - 1 } { q ^ { n _ { s } } - 1 } = | A _ { s } | \mathrm { i } s \mathrm { a n } i n t e g e r \mathrm { f o r } \mathrm { a l l } s .
$$

We know that the equivalence classes partition $R ^ { * }$ . We now group the central elements $Z ^ { \star }$ together and denote by $\varLambda _ { 1 } , \ldots , \varLambda _ { t }$ the equivalence classes containing more than one element. By our assumption we know $t \geq 1$ Since $\begin{array} { r } { | R ^ { * } | = | Z ^ { * } | + \sum _ { k = 1 } ^ { t } | A _ { k } | } \end{array}$ we have proved the so-called class formula

$$
q ^ { n } - 1 = q - 1 + \sum _ { k = 1 } ^ { t } \frac { q ^ { n } - 1 } { q ^ { n _ { k } } - 1 } ,
$$

where we have $1 < \frac { g ^ { \prime 2 } - 1 } { q ^ { n _ { \cdot k - 1 } } } \in \mathbb { N }$ for all $k$ .

With (1) we have left abstract algebra and are back to the natural numbers. Next we claim that $q ^ { \pi _ { k } } - 1 \mid q ^ { \pi } - 1$ implies $\eta _ { t k } \mid \eta$ Indeed, write $n = a \Re _ { k } + r$ with $0 \leq r < r _ { l _ { k } }$ , then $q ^ { n _ { k } } - 1 | q ^ { a n _ { k } + r } - 1$ implies

$$
q ^ { n _ { k } } - 1 | \left( q ^ { a n _ { k } + r } - 1 \right) - \left( q ^ { n _ { k } } - 1 \right) = q ^ { n _ { k } } ( q ^ { ( a - 1 ) n _ { k } + r } - 1 ) ,
$$

and thus $q ^ { \prime \bar { \imath } _ { k } } - 1 | q ^ { ( \alpha - 1 ) n _ { k } + r } - 1$ , since $q ^ { \pi _ { k } }$ and $q ^ { \pi _ { k } } \sim 1$ are relatively prime. Continuing in this way we find $q ^ { n _ { k } } - 1 \big | q ^ { r } - 1$ with $0 \leq r < n _ { k }$ which is only possible for $r = 0$ , that is, $n _ { k } \vert n _ { l }$ . In summary, we note

$$
r { \boldsymbol { k } } _ { \mathbf { k } } \mid \pi \quad { \mathrm { f o r ~ a l l ~ } } { \boldsymbol { k } } .
$$

Now comes the second ingredient: the complex numbers $\mathbb { C }$ Consider the polynomial $x ^ { \mathfrak { n } } - 1$ . Its roots in $\mathbb { C }$ are called the $7 2 - t h$ roots of unity. Since $\lambda ^ { \pi z } = 1$ , all these roots $\lambda$ have $| \lambda | = 1$ and lie therefore on the unit circle of the complex plane. In fact, they are precisely the numbers $\lambda _ { k } = e ^ { \frac { 2 k \pi i } { \pi } } =$ $\cos ( 2 k \pi / n ) + i \sin ( 2 k \pi / n ) \quad$ , $0 \leq k \leq n - 1$ (see the box on the next page). Some of the roots $\lambda$ satisfy $\lambda ^ { d } = 1$ for $i l < \pi$ ; for example, the root $\lambda = - 1$ satisfies $\lambda ^ { 2 } = 1$ . For a root $\lambda$ , let $d$ be the smallest positive exponent with $\lambda ^ { d } = 1$ , that is, $d$ is the order of $\lambda$ in the group of the roots of unity. Then $d | n$ , by Lagrange's theorem ("the order of every element of a group divides the order of the group" — see the box in Chapter I). Note that there are roots of order $\gamma _ { l }$ , such as $\lambda _ { 1 } = \epsilon ^ { \frac { 2 \pi i } { n } }$

# Roots of unity

Any complex number $z = x + i y$ may be written in the "polar" form

$$
z = r e ^ { i \varphi } = r ( \cos \varphi + i \sin \varphi ) ,
$$

where $r = | z | = { \sqrt { x ^ { 2 } + y ^ { 2 } } }$ is the distance of $\mathfrak { z }$ to the origin, and $\varphi$ is the angle measured from the positive $\mathscr { X }$ axis. The $\mathscr { n } _ { i }$ -th roots of unity are therefore of the form

$$
\begin{array} { r } { \lambda _ { k } = e ^ { \frac { 2 k \pi i } { \pi } } = \cos ( 2 k \pi / n ) + i \sin ( 2 k \pi / n ) , \qquad 0 \le k \le n - 1 , } \end{array}
$$

since for all $k$

$$
\lambda _ { k } ^ { n } = e ^ { 2 k \pi i } = \cos ( 2 k \pi ) + i \sin ( 2 k \pi ) = 1 .
$$

for  i inere $_ { n }$ Thous $\lambda _ { k } = \zeta ^ { k }$ $k$ $\zeta = \mathcal { C } ^ { \frac { 2 \pi i } { n } }$ the $n$ -th roots of unity form a cyclic group $\{ \zeta , \zeta ^ { 2 } , \ldots , \zeta ^ { n - 1 } , \zeta ^ { n } = 1 \}$ of order n.

Now we group all roots of order $d$ together and set

$$
\phi _ { d } ( x ) : = \prod _ { \lambda { \mathrm { ~ o f ~ o r d e r } } d } ( x - \lambda ) .
$$

Note that the definition of $\phi _ { d } ( x )$ is independent of $\mathcal { n }$ Since every root has some order $d .$ , we conclude that

$$
x ^ { \ast 2 } - 1 \ = \ \prod _ { i \mid n } \dot { \varphi } _ { d } ( x ) .
$$

Here is the crucial observation: The coefficients of the polynomials $\phi _ { n } ( x )$ are integers (that is, $\phi _ { \pi } ( x ) \in \mathbb { Z } [ x ]$ for all $\mathscr { n }$ ), where in addition the constant coefficient is either 1 or $- 1$ .

Let us carefully verify this claim. For $n = 1$ we have 1 as the only root, and so $\phi _ { 1 } ( x ) = x$ 1. Now we procecd by induction, where we assume ${ \mathcal { Q } } _ { t } { \big ( } { \boldsymbol { \mathfrak { x } } } { \big ) } \in \mathbb { Z } [ { \boldsymbol { \mathfrak { x } } } ]$ for all $d < n$ , and that the constant coefficient of ${ \bf \Pi } _ { ( i ) _ { d } } ^ { * } ( x )$ is 1 or −1. By (3),

$$
x ^ { n } - 1 = p ( x ) \phi _ { n } ( x )
$$

where $p ( \boldsymbol { \mathscr { x } } ) = \sum _ { j = 0 } ^ { \ell } p _ { j } \boldsymbol { \mathscr { x } } ^ { j }$ . $\phi _ { n } ( x ) = \sum _ { k = 0 } ^ { n - \ell } a _ { k } x ^ { k }$ , with $p _ { 0 } = 1$ or $p _ { \checkmark } = - 1$

Since $- 1 ~ { \stackrel { } { \dots } } ~ \{ p _ { 0 } \alpha _ { 0 } \}$ , we see $a _ { 0 } \in \{ 1 , - 1 \}$ .Suppose we already know that $a _ { \cdot \{ \} } , a _  \cdot \} , \ldots , a _ { k - 1 } \in \mathbb { Z }$ Computing the coefficient of $x ^ { k }$ on both sides of (4)

![](images/49e5f1e20ba5e447b447484925f78399679275a416e99163b4afabb74717366d.jpg)

![](images/2a9a32c6afe3aca23ec2b4844697b8314414c7ec9ba7d3b130ddf54b6a0fab34.jpg)

The roots of unity for $\gamma _ { \downarrow } = 6$

we find

$$
\sum _ { j = 0 } ^ { k } p _ { j } a _ { k - j } \quad \ldots \quad \sum _ { j = 1 } ^ { k } p _ { j } a _ { k - j } + p _ { 0 } a _ { k } \quad \in \mathrm { ~ \mathbb { Z } ~ } .
$$

By assumption, all $a _ { 0 } , \ldots , a _ { k - 1 }$ (and all $\gamma _ { j }$ )are in $\mathbb { Z }$ Thus $p _ { 0 } \Omega k$ and hence $a _ { k }$ must also be integers, since $p _ { 0 }$ is 1 or $- 1$ .

We are ready for the coup de grâce. Let $n _ { k } \mid n$ be one of the numbers appearing in (1). Then

$$
x ^ { n } - 1 = \prod _ { d \mid n } \phi _ { d } ( x ) = ( x ^ { n _ { k } } - 1 ) \phi _ { n } ( x ) \prod _ { d \mid n , d \nmid n , d \neq n } \phi _ { d } ( x ) .
$$

We conclude that in $\mathbb { Z }$ we have the divisibility relations

$$
\phi _ { n } ( q ) \mid q ^ { n } - 1 \qquad \mathrm { a n d } \qquad \phi _ { n } ( q ) \mid \frac { q ^ { n } - 1 } { q ^ { n _ { k } } - 1 } .
$$

Since (5) holds for all $k$ , we deduce from the class formula (1)

![](images/383d1b85bc188ab0069e363b2c7a38c199ae55862af9bf850a51c3a85083464c.jpg)

$$
\phi _ { \tau { 2 } } ( q ) \mid q - 1 ,
$$

$\left| q - \mu \right| > \left| q - 1 \right|$

but this cannot be. Why? We know $\phi _ { n } ( x ) = \prod ( x - \lambda )$ where $\lambda$ runs through all roots of $x ^ { \gamma _ { 2 } } - 1$ of order $n$ . Let $\tilde { \lambda } = a + i b$ be one of those roots. By $n > 1$ (because of $R \neq Z .$ we have $\widetilde { \lambda } \neq 1$ , which implies that the real part $a _ { \mathrm { \ell } }$ is smaller than 1. Now $| \tilde { \lambda } | ^ { 2 } = a ^ { 2 } + b ^ { 2 } = 1$ , and hence

$$
\begin{array} { r c l } { { q - \tilde { \lambda } | ^ { 2 } } } & { { = } } & { { | q - a - i b | ^ { 2 } ~ = ~ ( q - a ) ^ { 2 } + b ^ { 2 } } } \\ { { } } & { { = } } & { { q ^ { 2 } - 2 a q + a ^ { 2 } + b ^ { 2 } ~ = ~ q ^ { 2 } - 2 a q + 1 } } \\ { { } } & { { > } } & { { q ^ { 2 } - 2 q + 1 ~ ( \mathrm { b e c a u s e ~ o f } ~ a < 1 ) } } \\ { { } } & { { = } } & { { ( q - 1 ) ^ { 2 } , } } \end{array}
$$

and so $| q - \tilde { \lambda } | > q - 1$ holds for all roots of order $n$ This implies

$$
| \phi _ { n } ( q ) | = \prod _ { \lambda } | q - \lambda | > q - 1 ,
$$

which means that $\phi _ { n } ( q )$ cannot be a divisor of $q - 1$ , contradiction and end of proof. □

# References

[1] L. E. DicksoN: On finite algebras, Nachrichten der Akad. Wissenschaften Göttingen Math.-Phys. Klasse (1905), 1-36; Collected Mathematical Papers Vol. III, Chelsea Publ. Comp, The Bronx, NY 1975, 539-574.   
[2] J. H. M. WEDDERBURN: A theorem on finite algebras, Trans. Amer. Math. Soc. 6 (1905), 349-352.   
[3] E. WITT: Über die Kommutativität endlicher Schiefkörper, Abh. Math. Sem. Univ. Hamburg 8 (1931), 413.

"π is irrational"

This was already conjectured by Aristotle, when he claimed that diameter and circumference of a circle are not commensurable. The first proof of this fundamental fact was given by Johann Heinrich Lambert in 1766. Our Book Proof is due to Ivan Niven, 1947: an extremely elegant one-page proof that needs only elementary calculus. Its idea is powerful, and quite a bit more can be derived from it, as was shown by Iwamoto and Koksma, respectively:

• $\pi ^ { 2 }$ is irrational and • $e ^ { r }$ is irrational for rational $r \neq 0$ .

![](images/391cb187c4b6ff63c9e5960f7e8663c494fd30dce850510729d79965f77c4e6a.jpg)  
Charles Hermite

Niven's method does, however, have its roots and predecessors: It can be traced back to the classical paper by Charles Hermite from 1873 which first established that $e$ is transcendental, that is, that $^ e$ is not a zero of a polynomial with rational coefficients.

Before we treat $\pi$ we will look at $e$ and its powers, and see that these are irrational. This is much easier, and we thus also follow the historical order in the development of the results.

To start with, it is rather easy to see (as did Fourier in 1815) that $e =$ $\textstyle \sum _ { k \geq 0 } { \frac { 1 } { k ! } }$ n $\begin{array} { r } { e \ = \ \frac { a } { b } } \end{array}$ for integers $a$ and $b > 0$ then we would get

$$
n ! b e \ = \ n ! a
$$

for every $n \geq 0$ .But this cannot be true, because on the right-hand side we have an integer, while the left-hand side with

$$
e ~ = ~ \left( 1 + { \frac { 1 } { 1 ! } } + { \frac { 1 } { 2 ! } } + \ldots + { \frac { 1 } { n ! } } \right) + \left( { \frac { 1 } { ( n + 1 ) ! } } + { \frac { 1 } { ( n + 2 ) ! } } + { \frac { 1 } { ( n + 3 ) ! } } + \ldots \right)
$$

decomposes into an integral part

and a second part

$$
{ \begin{array} { r c l } { e } & { : = } & { 1 + { \frac { 1 } { 1 } } + { \frac { 1 } { 2 } } + { \frac { 1 } { 6 } } + { \frac { 1 } { 2 4 } } + \dots } \\ & { = } & { 2 . 7 1 8 2 8 1 8 2 8 . . . } \end{array} }
$$

$$
b n ! { \Big ( } 1 + { \frac { 1 } { 1 ! } } + { \frac { 1 } { 2 ! } } + \ldots + { \frac { 1 } { n ! } } { \Big ) }
$$

$$
b \Big ( \frac { 1 } { n + 1 } + \frac { 1 } { ( n + 1 ) ( n + 2 ) } + \frac { 1 } { ( n + 1 ) ( n + 2 ) ( n + 3 ) } + \ldots \Big )
$$

# Geometric series

For the infinite geometric series $\begin{array} { r } { Q = \frac { 1 } { q } + \frac { 1 } { q ^ { 2 } } + \frac { 1 } { q ^ { 3 } } + . . . } \end{array}$   
with $q > 1$ we clearly have   
$q Q = 1 + { \textstyle { \frac { 1 } { q } } } + { \textstyle { \frac { 1 } { q ^ { 2 } } } } + . . . = 1 + Q$   
and thus $Q = { \frac { 1 } { \mathfrak { q } - 1 } } .$

# SUR LTRRATIONNALITE DU NOMBRE

PAR J. LIOUVILLE. \*\*\*

On prouve dans les élérents que le nombre e, base des logarithmes nepériens, $\eta ^ { \prime } \kappa$ pas une valer rationnelle. On devrait, ceme semble, ajouter que la méme métbode prouve aossi que e ne peut pas tre rucine d'ume équation du sccoud degre i coeficients rationmels, en sorte que l'on ne peut pas avoir $a \theta + \frac { \partial } { \partial \theta } = c$ a tant on entier pomtit er $t _ { 1 } , r$ des entiers positifs ou negarifs, En effet, si Ton remplace dans cette équation e et $\vdots$ ou $s ^ { - 1 }$ par leurs développements déduits de celui de $e ^ { \prime }$ puis qu'oa mnltiplie les deux membres par r. a.3.. 4, an rouvera aisément

$$
\lim _ { n + 1 } ^ { \circ } ( 1 + \frac { 1 } { n + \frac { 1 } { 2 } } + \cdots ) \pm \frac { 1 } { n + 1 } ( 1 - \frac { 1 } { n + \frac { 1 } { 2 } } + \cdots ) = \infty .
$$

$\pmb { \mu }$ etant un entier. $\mathrm { { \bf O n \ p u t } }$ tujors fie e s que le ftur

$$
\pm { \frac { \delta } { \pm 1 } }
$$

se $b _ { \mathbf { \alpha } } \deg \mathfrak { t } < 0$ er a impair si $\delta \gets \delta \ell$ $> a$ pn  plust and uin que nous vnn d   sd n etant essentiellement positif et tris petit, sera compris entre o el 1, et ne pourra pas atre egal a un eatier $\pmb { \alpha }$ Doue, etc.

which is approximately $\textstyle { \frac { b } { \pi } }$ , so that for large $\mathscr { n }$ it cray an bnl:   
It is larger than $\frac { b } { n + 1 }$ and smaller than b $\frac { b } { n }$   
with a geometric series:

$$
\begin{array} { r c l } { \displaystyle \frac { 1 } { n + 1 } < } & { \displaystyle \frac { 1 } { n + 1 } + \frac { 1 } { ( n + 1 ) ( n + 2 ) } + \frac { 1 } { ( n + 1 ) ( n + 2 ) ( n + 3 ) } + . . . } \\ { < } & { \displaystyle \frac { 1 } { n + 1 } + \frac { 1 } { ( n + 1 ) ^ { 2 } } + \frac { 1 } { ( n + 1 ) ^ { 3 } } + . . . } & { = \displaystyle \frac { 1 } { n } . } \end{array}
$$

Now one might be led to think that this simple multiplyby-pt! trick is not even sufficient to show that $\epsilon ^ { 2 }$ is irrational. This is a stronger statement: $\sqrt { 2 }$ is an example of a number which is irrational, but whose square is not. From John Cosgrave we have learned that with two nice ideas/observations (let's call them "tricks") one can get two steps further nevertheless: Each of the tricks is sufficient to show that ${ \mathfrak { e } } ^ { 2 }$ is irrational, the combination of both of them even yields the same for $\epsilon ^ { \mathcal { \Lambda } }$ . The first trick may be found in a one page paper by J. Liouville from 1840 — and the second one in a two page "addendum" which Liouville published on the next two journal pages.

Why is $\mathcal { C } ^ { 2 }$ irrational? What can we derive from $\begin{array} { r } { e ^ { 2 } = \frac { a } { b } ? } \end{array}$ According to Liouville we should write this as

$$
 b \epsilon = a \epsilon ^ { - 1 } ,
$$

substitute the series

and

$$
\begin{array} { r c l } { { c } } & { { = } } & { { 1 + \displaystyle \frac { 1 } { 1 } + \displaystyle \frac { 1 } { 2 } + \displaystyle \frac { 1 } { 6 } + \displaystyle \frac { 1 } { 2 4 } + \displaystyle \frac { 1 } { 1 2 0 } + \ldots } } \\ { { } } & { { } } & { { } } \\ { { e ^ { - 1 } } } & { { = } } & { { 1 - \displaystyle \frac { 1 } { 1 } + \displaystyle \frac { 1 } { 2 } - \displaystyle \frac { 1 } { 6 } ~ + \displaystyle \frac { 1 } { 2 4 } - \displaystyle \frac { 1 } { 1 2 0 } \pm \ldots , } } \end{array}
$$

and then multiply by $n !$ , for a sufficiently large even $n$ . Then we see that $\eta ! b c \mathrm { . }$ is nearly integral:

Liouville's paper

$$
v { \nmid } b { \biggl ( } 1 + { \frac { 1 } { 1 } } + { \frac { 1 } { 2 } } + { \frac { 1 } { 6 } } + \ldots + { \frac { 1 } { n ! } } { \biggr ) }
$$

is an integer, and the rest

$$
n ! b { \Bigl ( } { \frac { 1 } { ( n { \mathrm { ~ + ~ } } 1 ) ! } } + { \frac { 1 } { ( n { \mathrm { ~ + ~ } } 2 ) ! } } + \ldots { \Bigr ) }
$$

is approximately $\frac { b } { \eta }$ : It is larger than $\frac { b } { n + 1 }$ but smaller than $\frac { b } { n }$ as we have seen above.

At the same time $n ! a e ^ { - 1 }$ is nearly integral as well: Again we get a large integral part, and then a rest

$$
( - 1 ) ^ { n + 1 } n ! a \Big ( \frac { 1 } { ( n + 1 ) ! } - \frac { 1 } { ( n + 2 ) ! } + \frac { 1 } { ( n + 3 ) ! } \mp \cdots \Big ) ,
$$

and this is approximately $( - 1 ) ^ { n + 1 } \frac { a } { n }$ .More preciscly: for even $\gamma _ { \ell }$ the rest is larger than $- \frac { a } { n ! }$ , but smaller than

$$
- a \Bigl ( \frac { 1 } { n + 1 } - \frac { 1 } { ( n + 1 ) ^ { 2 } } - \frac { 1 } { ( n + 1 ) ^ { 3 } } - \ldots \Bigr ) = - \frac { a } { n + 1 } \Bigl ( 1 - \frac { 1 } { n } \Bigr ) < 0 .
$$

But this cannot be true, since for large even $n$ it would imply that $\eta ! a e ^ { - 1 }$ is just a bit smaller than an integer, whilc $n ! b e$ is a bit larger than an integer, ${ \bf s } \_ { 0 } \ n ! a \epsilon ^ { 1 } = n ! b \epsilon .$ cannot hold.

In order to show that $\mathcal { C } ^ { 4 }$ is irrational, we now courageously assume that $\begin{array} { r } { \mathscr { C } ^ { \sharp } = \frac { a } { b } } \end{array}$ were rational, and write this as

$$
b e ^ { 2 } = a e ^ { - 2 } .
$$

We could now try to multiply this by $n$ for some large $n$ , and collect the non-integral summands, but this leads to nothing useful: Thc sum of the , on the right side $( - \cdot 1 ) ^ { n + 1 } a \frac { 2 ^ { n + 1 } } { n }$ , a  ill $n$ gets large.

So one has to examine the situation a bit more carefully, and make two little adjustments to the strategy: First we will not take an arbitrary large $n$ , but a large power of two, $n = 2 ^ { r t }$ ; and secondly we will not multiply by $n !$ , bul by $\displaystyle \frac { n ! } { 2 ^ { n - 1 } }$ T theorem (see page 8): For any $n \geq 1$ the integer $n !$ contains the prime factor 2 at most $n - 1$ times — with equality if (and only if) $n$ is a power of two, $r \} = 2 ^ { r n }$ .

This lemma is not hard to show: $\left\lfloor { \frac { n } { 2 } } \right\rfloor$ of the factors of $n$ are even, $\left\lfloor { \frac { \pi } { 4 } } \right\rfloor$ of them are divisible by 4, and so on. So if $2 ^ { k }$ is the largest power of two which satisfies $2 ^ { k } \leq n$ , then $n !$ contains the prime factor 2 exactly

$$
\left\lfloor { \frac { n } { 2 } } \right\rfloor + \left\lfloor { \frac { n } { 4 } } \right\rfloor + \ldots + \left\lfloor { \frac { n } { 2 ^ { k } } } \right\rfloor \ \leq \ { \frac { n } { 2 } } + { \frac { n } { 4 } } + \ldots + { \frac { n } { 2 ^ { k } } } \ = \ n \left( 1 - { \frac { 1 } { 2 ^ { k } } } \right) \ \leq \ n - 1
$$

times, with equality in both inequalities exactly if $\gamma _ { \mathord { \downarrow } } = 2 ^ { k }$

Let's get back to $b e ^ { 2 } = a e ^ { - 2 }$ We are looking at

$$
b { \frac { n ! } { 2 ^ { n - 1 } } } e ^ { 2 } = a { \frac { n ! } { 2 ^ { n - 1 } } } e ^ { - 2 }
$$

and substitute the series

and

$$
\begin{array} { r c l } { { e ^ { 2 } } } & { { = } } & { { 1 + \displaystyle \frac { 2 } { 1 } + \frac { 4 } { 2 } + \frac { 8 } { 6 } + \ldots + \displaystyle \frac { 2 ^ { r } } { r ! } + \ldots } } \\ { { } } & { { } } & { { } } \\ { { e ^ { - 2 } } } & { { = } } & { { 1 - \displaystyle \frac { 2 } { 1 } + \frac { 4 } { 2 } - \frac { 8 } { 6 } \pm \ldots + ( - 1 ) ^ { r } \displaystyle \frac { 2 ^ { r } } { r ! } + \ldots } } \end{array}
$$

For $r \leq n$ we get integral summands on both sides, namely

$$
b { \frac { n ! } { 2 ^ { n - 1 } } } { \frac { 2 ^ { r } } { r ! } } \mathrm { r e s p . } ( - 1 ) ^ { r } a { \frac { n ! } { 2 ^ { n - 1 } } } { \frac { 2 ^ { r } } { r ! } } ,
$$

where for $r > 0$ the denominator $r !$ contains the prime factor 2 at most $r - 1$ times, while $n !$ contains it exactly $ \eta \ll 1$ times. (So for $r > 0$ the summands are even.)

And since $_ n$ is even (we assume that $\pi = 2 ^ { \pi \mathfrak { L } }$ ), the series that we get for $r \geq n + 1$ are

$$
2 b { \Big ( } { \frac { 2 } { n + 1 } } + { \frac { 4 } { ( n + 1 ) ( n + 2 ) } } + { \frac { 8 } { ( n + 1 ) ( n + 2 ) ( n + 3 ) } } + \ldots { \Big ) }
$$

resp.

$$
2 a { \Big ( } - { \frac { 2 } { n + 1 } } + { \frac { 4 } { ( n + 1 ) ( n + 2 ) } } - { \frac { 8 } { ( n + 1 ) ( n + 2 ) ( n + 3 ) } } \pm \ldots { \Big ) } .
$$

These series will for large $\mathcal { \textbf { n } }$ be roughly $\begin{array} { l } { { \frac { { 4 } { \dot { \mathbf { 0 } } } } { \pi } } \ \mathrm { r e s p . } - { \frac { { 4 } { \dot { \mathbf { a } } } } { \pi } } } \end{array}$ , as one sees again by comparison with geometric series. For large $\pi = 2 ^ { \mathfrak { n } } { } ^ { \mathfrak { n } }$ this means that the left-hand side of (1) is $\pmb { a }$ bit larger than an integer, while the right-hand side is a bit smaller — contradiction! □

So we know that $e ^ { 4 }$ is irrational; to show that $e ^ { 3 }$ , $\epsilon ^ { 5 }$ etc. are irrational as well, we need heavier machinery (that is, a bit of calculus), and a new idea — which essentially goes back to Charles Hermite, and for which the key is hidden in the following simple lemma.

Lemma. For some fixed $n \geq 1$ ,let

$$
f ( x ) ~ = ~ \frac { x ^ { n } ( 1 - x ) ^ { n } } { n ! } .
$$

The function $f ( x )$ is a polynomial of the form $f ( x ) = { \frac { 1 } { n ! } } \sum _ { i = n } ^ { 2 n } c _ { i } x ^ { i } ,$ where the coefficients $c _ { i }$ are integers.

$$
\begin{array} { r } { F o r \mathrm { 0 } < x < \mathrm { 1 } w e \ h a v e \mathrm { 0 } < f ( x ) < \frac { 1 } { n ! } . } \end{array}
$$

The estimate $\begin{array} { r } { n ! > e ( \frac { \pi } { e } ) ^ { n } } \end{array}$ yields an explicit $\boldsymbol { \mathscr { n } }$ that is "large enough."

The derivatives $f ^ { ( k ) } ( 0 )$ and $f ^ { ( k ) } ( 1 )$ are integers for all $k \geq 0$ .

Proof. Parts (i) and (ii) are clear.

For (iii) note that by (i) the $k$ -th derivative $f ^ { ( k ) }$ vanishes at $x = 0$ unless $n \leq k \leq 2 n .$ and in this range $\begin{array} { r } { f ^ { ( k ) } ( 0 ) = \frac { k ! } { n ! } c _ { k } } \end{array}$ is an integer. From $f ( x ) =$ $f ( 1 - x )$ we get $f ^ { ( k ) } ( x ) = ( - 1 ) ^ { k } f ^ { ( k ) } ( 1 - x )$ for all $x$ , and hence $f ^ { ( k ) } ( 1 ) =$ $( - 1 ) ^ { k } f ^ { ( k ) } ( 0 )$ , which is an integer.

Theorem 1. $e ^ { \tau }$ is irrational for every $r \in \mathbb { Q } \backslash \{ 0 \}$ .

Proof. It suffices to show that $e ^ { s }$ cannot be rational for a positive integer $s$ (if $e ^ { \frac { s } { t } }$ were rational, then $\left( \boldsymbol { \mathscr { e } } ^ { \frac { \mathbf { s } } { t } } \right) ^ { t } = \boldsymbol { \mathscr { e } } ^ { s }$ would be rational, too). Assume that $e ^ { s } = { \frac { a } { b } }$ for integers $a , b > 0$ , and let $\textbf { \textit { u } }$ be so large that $n ! > a s ^ { 2 n + 1 }$ . Put

$$
F ( x ) { \mathit { \Psi } } : = { \mathit { \Phi } } s ^ { 2 n } f ( x ) - s ^ { 2 n - 1 } f ^ { \prime } ( x ) + s ^ { 2 n - 2 } f ^ { \prime \prime } ( x ) \mp \ldots + f ^ { ( 2 n ) } ( x ) ,
$$

where ${ \bar { f } } ( x )$ is the function of the lemma.

$F ( x )$ may also be written as an infinite sum

$$
F ( x ) ~ = ~ s ^ { 2 n } f ( x ) - s ^ { 2 n - 1 } f ^ { \prime } ( x ) + s ^ { 2 n - 2 } f ^ { \prime \prime } ( x ) \mp \ldots ,
$$

since the higher derivatives $f ^ { ( k ) } ( x )$ , for $k > 2 \eta$ , vanish. From this we see that the polynomial $F ( x )$ satisfies the identity

$$
F ^ { \prime } ( x ) = - s F ( x ) + s ^ { 2 n + 1 } f ( x ) .
$$

Thus differentiation yields

$$
{ \frac { d } { d x } } \left[ e ^ { s x } F ( x ) \right] = s e ^ { s x } F ( x ) + e ^ { s x } F ^ { \prime } ( x ) = s ^ { 2 n - 1 } e ^ { s x } f ( x )
$$

and hence

$$
N : = b \int _ { 0 } ^ { 1 } s ^ { 2 n + 1 } e ^ { s x } f ( x ) d x = b [ e ^ { s \cdot r } F ( x ) ] _ { 0 } ^ { 1 } = a F ( 1 ) - b F ( 0 ) .
$$

This is an integer, since part (iii) of the lemma implies that $F ( 0 )$ and $F ( 1 )$ are integers. However, part (ii) of the lemma yields estimates for the size of $N$ from below and from above,

$$
0 < N = b \int _ { 0 } ^ { 1 } s ^ { 2 n + 1 } e ^ { s x } f ( x ) d x < b s ^ { 2 n + 1 } \epsilon ^ { s } { \frac { 1 } { n ! } } = { \frac { a . s ^ { 2 n + 1 } } { n ! } } < 1 ,
$$

which shows that $N$ cannot be an integer: contradiction.

Now that this trick was so successful, we use it once more.

Theorem 2. $\pi ^ { 2 }$ is irrational.

Proof. Assume that $\textstyle \pi ^ { 2 } \ = \ { \frac { a } { b } }$ for integers $a , b > 0$ We now use the polynomial

$$
F ( x ) \ : = \ b ^ { n } \Big ( \pi ^ { 2 n } f ( x ) - \pi ^ { 2 n - 2 } f ^ { ( 2 ) } ( x ) + \pi ^ { 2 n - 4 } f ^ { ( 4 ) } ( x ) \mp \ldots \Big ) ,
$$

which satisfies $F ^ { \prime \prime } ( x ) = - \pi ^ { 2 } F ( x ) + b ^ { n } \pi ^ { 2 n + 2 } f ( x ) .$

From part (iii) of the lemma we get that $F ( 0 )$ and $F ( 1 )$ are integers. Elementary differentiation rules yield

$$
{ \begin{array} { l l l } { { \displaystyle { \frac { d } { d x } } \big [ F ^ { \prime } ( x ) \sin \pi x - \pi F ( x ) \cos \pi x \big ] } } & { = } & { \big ( F ^ { \prime \prime } ( x ) + \pi ^ { 2 } F ( x ) \big ) \sin \pi x } \\ & & { = } & { b ^ { n } \pi ^ { 2 n + 2 } f ( x ) \sin \pi x } \\ & { = } & { \pi ^ { 2 } a ^ { n } f ( x ) \sin \pi x , } \end{array} }
$$

and thus we obtain

$$
{ \begin{array} { l l l } { N : = \pi \displaystyle \int _ { 0 } ^ { 1 } a ^ { n } f ( x ) \sin \pi x d x } & { = } & { \displaystyle \left[ { \frac { 1 } { \pi } } F ^ { \prime } ( x ) \sin \pi x - F ( x ) \cos \pi x \right] _ { 0 } ^ { 1 } } \\ & { = } & { F ( 0 ) + F ( 1 ) , } \end{array} }
$$

which is an integer. Furthermore $N$ is positive since it is defined as the

π is not rational, but it does have "good approximations" by rationals - some of these wcre known sincc antiquity:

$$
\begin{array} { r l r } { \frac { 2 2 } { 7 } } & { { } = } & { 3 . 1 4 2 8 5 7 1 4 2 8 5 7 . . . } \\ { \frac { 3 5 5 } { 1 1 3 } } & { { } = } & { 3 . 1 4 1 5 9 2 9 2 0 3 5 3 . . . } \\ { \frac { 1 0 4 3 4 8 } { 3 3 2 1 5 } } & { { } = } & { 3 . 1 4 1 5 9 2 6 5 3 9 2 1 . . . } \\ { \pi } & { { } = } & { 3 . 1 4 1 5 9 2 6 5 3 5 8 9 . . . } \end{array}
$$

integral of a function that is positive (except on the boundary). However, if we choose $n$ so large that $\frac { \overline { { \pi } } a ^ { n } } { n ! } < 1$ , then from part (ii) of the lemma we obtain

$$
0 < N = \pi \int _ { 0 } ^ { 1 } a ^ { n } f ( x ) \sin \pi x d x < { \frac { \pi a ^ { n } } { n ! } } < 1 ,
$$

a contradiction.

Here comes our final irrationality result

Theorem 3. For every odd integer $n \geq 3 ,$ ,the number

$$
A ( n ) : = { \frac { 1 } { \pi } } \operatorname { a r c c o s } \left( { \frac { 1 } { \sqrt { n } } } \right)
$$

![](images/7de55fca394bf50deee179867762d014a816cca2aef251a8612ba12218a14575.jpg)

is irrational.

We will need this result for Hilbert's third problem (see Chapter 8) in the cases $n \ : = \ : 3$ and $n = 9$ .For $n = 2$ and $ \hbar = 4$ we have $\begin{array} { r } { A ( 2 ) \ = \ \frac { 1 } { 4 } } \end{array}$ and $\begin{array} { r } { A ( 1 ) ~ = ~ \frac { 1 } { 3 } } \end{array}$ , so the restriction to odd integers is essential. These values are easily derived by appealing to the diagram in the margin, in which the statement $\mathbf { \Sigma } ^ { \bullet \sharp } \frac { \mathbf { l } } { \pi }$ arccos $( \frac { 1 } { \sqrt { n } } )$ polygonal arc constructed from n, all of whose chords have the same length, never closes into itself.

We leave it as an exercise for the reader to show that $A ( n )$ is rational only for ${ \mathfrak { r } } \mathfrak { z } \ \{ 1 , 2 , 4 \}$ . For that, distinguish the cases when $n = 2 ^ { r }$ , and when $n$ is not a power of 2.

Proof. We use the addition theorem

$$
\textstyle \cos \alpha + \cos \beta = 2 \cos { \frac { \alpha + \beta } { 2 } } \cos { \frac { \alpha - \beta } { 2 } }
$$

from elementary trigonometry, which for ${ \mathfrak { x } } = ( k + 1 ) \varphi$ and $\beta = ( k - 1 ) \varphi$ yields

$$
\cos { \left( k + 1 \right) } \varphi = 2 \cos { \varphi } \cos { k \varphi } - \cos { ( k - 1 ) \varphi } .
$$

For the angle $\begin{array} { r } { \varphi _ { n } = \operatorname { a r c c o s } \left( \frac { 1 } { \sqrt { n } } \right) } \end{array}$ , which is defined by $\cos \varphi _ { \mathrm { \pmb { r } } } = \frac { 1 } { \sqrt { \pi } }$ and $0 \leq \varphi _ { \mathfrak { n } } \leq \pi$ , this yields representations of the form

$$
\cos { k } \varphi _ { n } = \frac { A _ { k } } { \sqrt { \pi } ^ { k } } ,
$$

where $A _ { k }$ is an integer that is not divisible by $n$ , for all $k : \geq 0$ .In fact, we have such a representation for $k = 0 , 1$ with $A _ { 0 } = A _ { \mathrm { 1 } } = 1$ , and by induction on $k$ using (2) we get for $k \geq 1$

$$
\cos { ( k + 1 ) } \varphi _ { n } ~ = ~ 2 \frac { 1 } { \sqrt { n } } \frac { A _ { k } } { \sqrt { n } ^ { k } } - \frac { A _ { k - 1 } } { \sqrt { n } ^ { k - 1 } } ~ = ~ \frac { 2 A _ { k } - n A _ { k - 1 } } { \sqrt { n } ^ { k + 1 } } .
$$

Thus we obtain $\begin{array} { r } { \mathcal { A } _ { k + 1 } \ = \ 2 \mathcal { A } _ { k } - \gamma _ { \hat { \imath } } \mathcal { A } _ { k - 1 } } \end{array}$ . If $\gamma _ { \mathscr { L } } \geq 3$ is odd, and $A _ { k }$ is not divisible by $\gamma _ { \ell }$ , then we find that $A _ { k + 1 }$ cannot be divisible by $\mathcal { n }$ ,either.

Now assume that

$$
A ( n ) = { \frac { 1 } { \pi } } { \hat { \varphi _ { n } } } = { \frac { k } { \ell } }
$$

is rational (with integers $\dot { \boldsymbol { k } } , \boldsymbol { \ell } > \boldsymbol { 0 } ,$ .Then $\hat { \varepsilon } _ { \mathcal { S } _ { 1 2 } } = k \pi$ yields

$$
\pm 1 - \cos k \pi = \frac { A _ { \ell } } { \sqrt { u } ^ { \ell } } .
$$

Thus $\sqrt { n } ^ { \ell } = \ell \boldsymbol { A } _ { \ell }$ is an integer, with $\ell \geq 2$ , and hence $n \mid { \sqrt { n } } ^ { \ell }$ With $\sqrt { \pi } ^ { \ell } \mid A _ { \ell }$ we find that $n$ divides $A _ { \ell }$ , a contradiction.

# References

[1] C. HERMITE: Sur la fonction exponentielle, Comptes rendus de I'Acadérnie des Sciences (Paris) 77 (1873), 18-24; (Euvres de Charles Hermite, Vol. III, Gauthier-Villars, Paris 1912, pp. 150-181.   
[2] Y. IWAMOTO: A proof that $\pi ^ { 2 }$ is irrational, J. Osaka Institute of Science and Technology 1 (1949), 147-148.   
[3] J. F. KOksMA: On Niven's proof that $\pi$ is irrational, Nieuw Archief voor Wiskunde (2) 23 (1949), 39.   
[4] J. LIOUVILLE: Sur l'irrationalité du nombre $e = 2 \AA , 7 1 8 . . .$ , Journal de Mathé- matiques Pures ct Appl. (1) 5 (1840), 192; Addition, 193-194.   
[5] I. NIvEN: A simple proof that $\pi$ is irrational, Bulletin Amer. Math, Soc. 53 (1947), 509.

W kow that eie s $\textstyle \sum _ { n \geq 1 } { \frac { 1 } { n } }$ does not convege Indeed in $\sum _ { p \in \mathbb { P } } \frac { 1 } { p }$ diverges.

However, the sum of the reciprocals of the squares converges (although very slowly, as we will also see), and it produces an interesting value.

H

Euler's series.

$$
\sum _ { n \ge 1 } { \frac { 1 } { n ^ { 2 } } } ~ = ~ { \frac { \pi ^ { 2 } } { 6 } } .
$$

This is a classical, famous and important result by Leonhard Euler from 1734. One of its key interpretations is that it yields the first non-trivial value $\zeta ( 2 )$ of Riemann's zeta function (see the appendix on page 41). This value is irrational, as we have seen in Chapter 6.

But not only the result has a prominent place in mathematics history, there are also a number of extremely elegant and clever proofs that have their history: For some of these the joy of discovery and rediscovery has been shared by many. In this chapter, we present three such proofs.

Proof. The first proof appears as an exercise in William J. LeVeque's number theory textbook from 1956. But he says: "I haven't the slightest idea where that problem came from, but I'm pretty certain that it wasn't original with me."

The proof consists in two different evaluations of the double integral

$$
I : = \int \int \limits _ { 0 } ^ { 1 } \int \int \frac { 1 } { 1 - x y } d x d y .
$$

For the first one, we expand $\frac { 1 } { 1 - x y }$ as a geometric series, decompose the summands as products, and integrate effortlessly:

$$
{ \begin{array} { r c l } { I } & { = } & { \displaystyle \int _ { 0 } ^ { 1 } \displaystyle \int _ { 0 } ^ { 1 } \sum _ { n \geq 0 } ( x y ) ^ { n } d x d y = \sum _ { n \geq 0 } \displaystyle \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } x ^ { n } y ^ { n } d x d y } \\ & & { = } & { \displaystyle \sum _ { n \geq 0 } \left( \int _ { 0 } ^ { 1 } x ^ { n } d x \right) \left( \int y ^ { n } d y \right) = \sum _ { n \geq 0 } { \frac { 1 } { n + 1 } } { \frac { 1 } { n + 1 } } } \\ & & { = \displaystyle \sum _ { n \geq 0 } { \frac { 1 } { ( n + 1 ) ^ { 2 } } } = \sum _ { n \geq 1 } { \frac { 1 } { n ^ { 2 } } } = \zeta ( 2 ) . } \end{array} }
$$

![](images/f7d949052479cb7a2ac40fd0874eb8f7c148f02c20d33f6f4235b099aecc8c73.jpg)

1.000000   
1.250000   
1.361111   
6 1.423611   
6 25 1.463611   
1+ 4 9 6 \$rac25\$ + 36 1.491388   
\$π2}/6 1.644934.

This evaluation also shows that the double integral (over a positive function with a pole at $x = y = 1$ is finite. Note that the computation is also easy and straightforward if we read it backwards - thus the evaluation of $\zeta ( 2 )$ leads one to the double integral $I$ .

![](images/f360fa5e2418ec54584a3d418b4c68fd4333593789e4b97ae06c833f41868ffd.jpg)

The second way to evaluate $\pmb { I }$ comes from a change of coordinates: in the new coordinates given by u := y+ and $\textstyle v : = { \frac { y - x } { 2 } } $ the domain of integration is a square of side length ${ \scriptstyle { \frac { 1 } { 2 } } } \sqrt { 2 }$ , which we get from the old domain by first rotating it by $4 5 ^ { \mathrm { { c } } }$ and then shrinking it by a factor of $\sqrt { 2 }$ Substitution of $x = \varkappa - \sharp$ and $y = u + v$ yields

$$
\frac { 1 } { 1 - x y } = \frac { 1 } { 1 - u ^ { 2 } + v ^ { 2 } } .
$$

To transform the integral, we have to replace $d x d y$ by $2 \ d u \ d v$ , to compensate for the fact that our coordinate transformation reduces areas by a constant factor of 2 (which is the Jacobi determinant of the transformation; see the box on the next page). The new domain of integration, and the function to be integrated, are symmetric with respect to the $u$ -axis, so we just need to compute two times (another factor of 2 arises here!) the integral over the upper half domain, which we split into two parts in the most natural way:

$$
I = 4 \int _ { 0 } ^ { 1 / 2 } \bigg ( \int _ { 0 } ^ { u } \frac { d v } { 1 - u ^ { 2 } + v ^ { 2 } } \bigg ) d u + 4 \int _ { 1 / 2 } ^ { 1 } \bigg ( \int _ { 0 } ^ { 1 - u } \frac { d v } { 1 - u ^ { 2 } + v ^ { 2 } } \bigg ) d u .
$$

Using $\int { \frac { d x } { a ^ { 2 } + x ^ { 2 } } } = { \frac { 1 } { \alpha } } \arctan { \frac { x } { a } } + C$ , this becomes

$$
\begin{array} { r l r } { { \cal I } ~ = } & { { } } & { ~ 4 \displaystyle \int _ { 0 } ^ { 1 / 2 } \displaystyle \frac { 1 } { \sqrt { 1 - u ^ { 2 } } } \arctan \left( \displaystyle \frac { u } { \sqrt { 1 - u ^ { 2 } } } \right) d u } \\ { ~ } & { { } } & { ~ 4 \displaystyle \int _ { 1 / 2 } ^ { 1 } \displaystyle \frac { 1 } { \sqrt { 1 - u ^ { 2 } } } \arctan \left( \displaystyle \frac { 1 - u } { \sqrt { 1 - u ^ { 2 } } } \right) d u . } \end{array}
$$

These integrals can be simplified and finally evaluated by substituting $u =$ sin $\theta$ resp. $u = \cos \theta$ But we proceed more directly, by computing that the derivative of $\begin{array} { r } { g ( u ) : = \arctan \bar { \left( \frac { u } { \sqrt { 1 - u ^ { 2 } } } \right) } } \end{array}$ uz ) isg′(u) = $\begin{array} { r } { g ^ { \prime } ( \varkappa ) = \frac { 1 } { \sqrt { 1 - \varkappa ^ { 2 } } } } \end{array}$ √1−u2, while the derivative of h(u) := arctan $\begin{array} { r } { \left( \frac { 1 - u } { \sqrt { 1 - u ^ { 2 } } } \right) = \arctan \left( \sqrt { \frac { 1 - u } { 1 + u } } \right) } \end{array}$ 1−u) is h′ (u) = − 1 $\begin{array} { r } { \dot { \hbar } i ^ { \prime } ( u ) = - \frac { 1 } { 2 } \frac { 1 } { \sqrt { 1 - u ^ { 2 } } } . } \end{array}$ So we may use $\begin{array} { r } { \int _ { \alpha } ^ { \dot { t } b } f ^ { \prime } ( x ) f ( x ) d x = \left[ \frac { 1 } { 2 } f ( x ) ^ { 2 } \right] _ { \alpha } ^ { \dot { b } } = \frac { 1 } { 2 } f ( b ) ^ { 2 } - \frac { 1 } { 2 } f ( a ) ^ { 2 } } \end{array}$ and get

$$
\begin{array} { l c l } { { I } } & { { = } } & { { \displaystyle { \ ^ { 1 } \int _ { 0 } ^ { 1 / 2 } g ^ { \prime } ( u ) g ( u ) d u \ + \ ^ { 1 } \int _ { 1 / 2 } ^ { 1 } - 2 h ^ { \prime } ( u ) h ( u ) d u } } } \\ { { } } & { { = } } & { { \displaystyle { 2 \left[ g ( u ) ^ { 2 } \right] _ { 0 } ^ { 1 / 2 } \ - \ \left. \ 4 \Big [ h ( u ) ^ { 2 } \right] _ { 1 / 2 } ^ { 1 } } } } \\ { { } } & { { = } } & { { \displaystyle { 2 g ( \frac 1 2 ) ^ { 2 } \ - \ 2 g ( 0 ) ^ { 2 } \ - \ \ 4 h ( 1 ) ^ { 2 } \ + \ 4 h ( \frac 1 2 ) ^ { 2 } } } } \\ { { } } & { { = } } & { { \displaystyle { 2 \left( \frac \pi 6 \right) ^ { 2 } - 0 - 0 + 4 \left( \frac \pi 6 \right) ^ { 2 } \ = \ \ \frac { \pi ^ { 2 } } { 6 } . } } } \end{array}
$$

This proof extracted the value of Euler's series from an integral via a rather simple coordinate transformation. An ingenious proof of this type — with an entirely non-trivial coordinate transformation — was later discovered by Beukers, Calabi and Kolk. The point of departure for that proof is to split the sum $\sum \limits _ { n \geq 1 } \frac { 1 } { n ^ { 2 } }$ te even tr an he  er. eary te terms $\begin{array} { r } { \frac { 1 } { 2 ^ { 2 } } + \frac { \overline { { 1 } } } { 4 ^ { 2 } } + \frac { 1 } { 6 ^ { 2 } } + . . . = \sum _ { k \geq 1 } \frac { 1 } { ( 2 k ) ^ { 2 } } } \end{array}$ (2k sum to ζ(2), so the odd terms $\begin{array} { r l } { \frac { 1 } { 1 ^ { 2 } } } & { { } \uplus \ \frac { 1 } { 1 ^ { 2 } } \ : + \ : \frac { 1 } { 5 ^ { 2 } } \ : + \ : . . . = \sum _ { k \geq 0 } \frac { 1 } { ( 2 k + 1 ) ^ { 2 } } } \end{array}$ makutree quarer  te al sum $\zeta ( 2 )$ . Thus Euler's series is equivalent to

$$
\sum _ { k \geq 0 } { \frac { 1 } { ( 2 k + 1 ) ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 8 } } .
$$

Proof. As above, we may express this as a double integral, namely

$$
J ~ = ~ \int \int \limits _ { 0 } ^ { 1 } { \frac { 1 } { 1 - x ^ { 2 } y ^ { 2 } } } d x d y ~ = ~ \sum _ { k > 0 } { \frac { 1 } { ( 2 k + 1 ) ^ { 2 } } } .
$$

So we have to compute this integral $I$ . And for this Beukers, Calabi and Kolk proposed the new coordinates

$$
u : = \operatorname { a r c c o s } { \sqrt { \frac { 1 - x ^ { 2 } } { 1 - x ^ { 2 } y ^ { 2 } } } } \qquad v : = \operatorname { a r c c o s } { \sqrt { \frac { 1 - y ^ { 2 } } { 1 - x ^ { 2 } y ^ { 2 } } } } .
$$

To compute the double integral, we may ignore the boundary of the domain, and consider $x , y$ in the range $0 < x ^ { \ast } < 1$ and $0 < y < 1$ Then $u , v$ will lie in the triangle $\eta _ { i } > 0 , v > 0 , u + v < \pi / 2$ . The coordinate transformation can be inverted explicitly, which leads one to the substitution

$$
x = { \frac { \sin u } { \cos u } } \qquad { \mathrm { a n d } } \qquad y = { \frac { \sin v } { \cos u } } .
$$

It is easy to check that these formulas define a bijective coordinate transformation between the interior of the unit square $\bar { S } \stackrel { - } { - } \{ ( x , y ) : 0 \leq x , y \leq 1 \}$ and the interior of the triangle $T = \{ ( u , v ) : u , v \geq 0 . \ u + v \leq \pi / 2 \}$ .

Now we have to compute the Jacobi determinant of the coordinate transformation, and magically it turns out to be

$$
\begin{array} { r l r } { \operatorname* { d e t } \left( \begin{array} { c c } { \frac { \cos u } { \cos v } } & { \frac { \sin u \sin v } { \cos ^ { 2 } v } } \\ { \frac { \sin u \sin v } { \cos ^ { 2 } u } } & { \frac { \cos v } { \cos u } } \end{array} \right) } & { = } & { 1 - \frac { \sin ^ { 2 } u \sin ^ { 2 } v } { \cos ^ { 2 } u \cos ^ { 2 } v } } \\ { \frac { \sin u \sin v } { \cos ^ { 2 } v } } & { \frac { \cos v } { \cos u } } \end{array} =  &  1 - x ^ { 2 } y ^ { 2 } .
$$

But this means that the integral that we want to compute is transformed into

$$
J ~ = ~ \int \limits _ { 0 } ^ { \pi / 2 \pi / 2 - u } 1 d u d v ,
$$

which is just the area $\begin{array} { r } { \frac { 1 } { 2 } \{ \frac { \pi } { 2 } \} ^ { 2 } = \frac { \pi ^ { 2 } } { \aleph } } \end{array}$ of the triangle $T$

# The Substitution Formula

To compute a double integral

$$
I = \int _ { \underline { { S } } } f ( x , y ) d x d y ,
$$

we may perform a substitution of variables

$$
x = x ( u , v ) \quad y = y ( u , v ) ,
$$

if the correspondence of $( u , v ) \in T$ to $( x , y ) \in S$ is bijective and continuously differentiable. Then $1$ equals

$$
\int _ { T } f ( x ( u , v ) , y ( u , v ) ) { \Big \lvert } { \frac { d ( x , y ) } { d ( u , v ) } } { \Big \lvert } d u d v ,
$$

where $\frac { d ( x , y ) } { d ( u , v ) }$ is the Jacobi determinant:

$$
\frac { d ( x , y ) } { d ( u , v ) } = \operatorname * { d e t } \left( \begin{array} { c c } { \frac { \mathrm { d } x } { d u } } & { \frac { d x } { d v } } \\ { \frac { d y } { \mathrm { d } u } } & { \frac { d y } { \mathrm { d } v } } \end{array} \right) .
$$

![](images/392db670e86b9bd7ceeef0cb311c3e4bab676979847b3454305fba87fd53e417.jpg)

![](images/ebe4fabb3451f4a45f34331adb78d28f444f92012d0cfd96b41461e897726503.jpg)

For $m \gets 1 , 2 , 3$ this yields $\cot ^ { 2 } { \frac { \pi } { 3 } } = { \frac { 1 } { 3 } }$ $\cot ^ { 2 } { \frac { \pi } { 5 } } + \cot ^ { 2 } { \frac { 2 \pi } { 5 } } = 2$ $\cot ^ { 2 } { \frac { \pi } { 7 } } + \cot ^ { 2 } { \frac { 2 \pi } { 7 } } + \cot ^ { 2 } { \frac { 3 \pi } { 7 } } = 5$

Beautiful — even more so, as the same method of proof extends to the computation of $\zeta ( 2 k )$ in terms of a $2 k$ -dimensional integral, for all $k \geq 1$ . We refer to the original paper of Beuker, Calabi and Kolk [2], and to Chapter 20, where we'll achieve this on a different path, using the Herglotz trick and Euler's original approach.

After these two proofs via coordinate transformation we can't resist the temptation to present another, entirely different and completely elementary proof for $\begin{array} { r } { \sum _ { n \geq 1 } \frac { 1 } { n ^ { 2 } } = \frac { \pi ^ { 2 } } { 6 } } \end{array}$ It appears in a sequence of exercises in the problem book by the twin brothers Akiva and Isaak Yaglom, whose Russian original edition appeared in 1954. Versions of this beautiful proof were rediscovered and presented by F. Holme (1970), I. Papadimitriou (1973), and by Ransford (1982) who attributed it to John Scholes.

Proof. The first step is to establish a remarkable relation between values of the (squared) cotangent function. Namely, for all $m \geq 1$ one has

$$
\begin{array} { r } { \cot ^ { 2 } \left( \frac { \pi } { 2 m - 1 } \right) + \cot ^ { 2 } \left( \frac { 2 \pi } { 2 \pi + 1 } \right) + \ldots + \cot ^ { 2 } \left( \frac { \pi \pi } { 2 m + 1 } \right) = \frac { 2 \pi ( 2 m - 1 ) } { 6 } . } \end{array}
$$

To establish this, we start with the relation

$$
{ \cos \pi } x + i \sin n x = ( \cos x + i \sin x ) ^ { n }
$$

and take its imaginary part, which is

$$
\sin n x \ = \ { \binom { n } { 1 } } \sin x \cos ^ { n - 1 } x - { \binom { n } { 3 } } \sin ^ { 3 } x \cos ^ { n - 3 } x \pm . . .
$$

Now we let $\eta _ { \downarrow } = 2 \gamma \eta + 1$ , while for $\mathcal { X }$ we will consider the m different values x = 2m+1 , for $r = 1 , 2 , \ldots , m$ For each of these values we have $\hbar \mathfrak { L } = \mathfrak { r } \mathfrak { \pi }$ , and thus sin $\smash { \eta _ { l } ( z ) = 0 }$ , while $0 < x < \frac { \pi } { 2 }$ implies that for sin $\boldsymbol { x }$ we get $m$ distinct positive values.

In particular, we can divide (2) by $\mathsf { s i m } ^ { \bar { \boldsymbol { r } } \bar { \boldsymbol { \varepsilon } } } \ \boldsymbol { \varepsilon }$ , which yields

that

$$
\begin{array} { r c l } { { 0 } } & { { = } } & { { \binom n 1 \cot ^ { n - 1 } x - \binom n 3 \cot ^ { n - 3 } x \pm \ldots , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { i s , } } } & { { } } & { { } } \\ { { 0 } } & { { = } } & { { \binom { 2 m - 1 } { 1 } \cot ^ { 2 m } x - \binom { 2 m + 1 } { 3 } \cot ^ { 2 m - 2 } x \pm . . . } } \\ { { } } & { { } } & { { } } \end{array}
$$

for each of the m distinct values of $x$ Thus for the polynomial of degree m

$$
\begin{array} { r l r } { p ( t ) } & { : = } & { \binom { 2 m + 1 } { 1 } t ^ { m } - \binom { 2 m + 1 } { 3 } t ^ { m - 1 } \pm . . . + ( - 1 ) ^ { m } \binom { 2 m + 1 } { 2 m + 1 } } \end{array}
$$

we know in distinct roots

$$
\begin{array} { r l r } { a _ { r } } & { { } = } & { \cot ^ { 2 } ( \frac { r \pi } { 2 m _ { \mathrm { ~ \tiny ~  ~ } } } ) \quad \mathrm { f o r } \quad r = 1 , 2 , \ldots , m . } \end{array}
$$

Hence the polynomial coincides with

$$
\begin{array} { r l r } { p ( t ) } & { = } & { \binom { 2 m - 1 } { 1 } \left( t - \cot ^ { 2 } \left( \frac { \pi } { 2 m + 1 } \right) \right) \cdot \ldots \cdot \left( t - \cot ^ { 2 } \left( \frac { m \pi } { 2 m + 1 } \right) \right) . } \end{array}
$$

Comparison of the coefficients of $t ^ { m - 1 }$ in $p ( t )$ now yields that the sum of the roots is

$$
a _ { 1 } + \ldots + a _ { r } = { \frac { \binom { 2 m + 1 } { 3 } } { \binom { 2 m + 1 } { 1 } } } = { \frac { 2 m ( 2 m - 1 ) } { 6 } } ,
$$

which proves (1).

We also need a sccond identity, of the same type,

$$
\begin{array} { r } { \csc ^ { 2 } \left( \frac { \pi } { 2 m + 1 } \right) + \csc ^ { 2 } \left( \frac { 2 \pi } { 2 m + 1 } \right) + \ldots + \csc ^ { 2 } \left( \frac { m \pi } { 2 m + 1 } \right) = \frac { 2 m ( 2 m + 2 ) } { 6 } , } \end{array}
$$

for the cosecant function csc $\begin{array} { r } { x = \frac { 1 } { \sin x } } \end{array}$ .But

$$
\csc ^ { 2 } x = { \frac { 1 } { \sin ^ { 2 } x } } = { \frac { \cos ^ { 2 } x + \sin ^ { 2 } x } { \sin ^ { 2 } x } } = \cot ^ { 2 } x + 1 ,
$$

so we can derive (3) from (1) by adding m to both sides of the equation. Now the stage is set, and everything falls into place. We use that in the range $\ 0 < y < \frac { \pi } { 2 }$ we have

$$
0 < \sin y < y < \tan y ,
$$

and thus

$$
0 < \cot y < \frac { 1 } { y } < \csc y ,
$$

which implies

$$
\cot ^ { 2 } y < \frac { 1 } { y ^ { 2 } } < \csc ^ { 2 } y .
$$

Now we take this double inequality, apply it to each of the $_ { \pmb { \eta } } { } _ { \pmb { \imath } }$ distinct values of $x$ , and add the results. Using (1) for the left-hand side, and (3) for the right-hand side, we obtain

$$
\begin{array} { r l r } { \frac { 2 m \left( 2 m - 1 \right) } { 6 } } & { < } & { \left( \frac { 2 m + 1 } { \pi } \right) ^ { 2 } + \left( \frac { 2 m + 1 } { 2 \pi } \right) ^ { 2 } + \ldots + \left( \frac { 2 m + 1 } { m \pi } \right) ^ { 2 } < \frac { 2 m \left( 2 m + 2 \right) } { 6 } , } \end{array}
$$

that is,

$$
\begin{array} { r c l c r c l } { { \frac { \pi ^ { 2 } } { 6 } \frac { 2 \pi n } { 2 m + 1 } \frac { 2 \pi n - 1 } { 2 m + 1 } } } & { { < } } & { { \frac { 1 } { 1 ^ { 2 } } + \frac { 1 } { 2 ^ { 2 } } + \ldots + \frac { 1 } { m ^ { 2 } } } } & { { < } } & { { \frac { \pi ^ { 2 } } { 6 } \frac { 2 \pi n } { 2 m + 1 } \frac { 2 \pi n + 2 } { 2 m + 1 } . } } \end{array}
$$

$\frac { \pi ^ { 2 } } { 6 }$ for $m \longrightarrow \infty .$ end of proof.

So how fast does $\sum \frac { 1 } { n ^ { 2 } }$ converge to $\pi ^ { 2 } / 6 ?$ For this we have to estimate the difference

$$
{ \frac { \pi ^ { 2 } } { 6 } } - \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } = \sum _ { n = m + 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } .
$$

Comparison of coefficients: If $p ( t ) = c ( t - a _ { 1 } ) \cdot \cdot \cdot ( t - a _ { m } ) .$ then the coefficient of $t ^ { \tau \mathcal { r } \cdot - 1 }$ is $- c ( a _ { 1 } + \ldots + a _ { \eta \eta } )$ .

$0 < a < b < c$ implies $0 < \frac { 1 } { \mathit { c } } < \frac { 1 } { \mathit { b } } < \frac { 1 } { \mathit { u } }$

![](images/8ae27a075c7639af296b925df065043b702684ebea326ec13df64f6970e02545.jpg)

This is very easy with the technique of "comparing with an integral" that we have reviewed already in the appendix to Chapter 2 (page 10). It yields

$$
\sum _ { n = m + 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } < \int _ { m } ^ { \infty } { \frac { 1 } { t ^ { 2 } } } d t = { \frac { 1 } { m } }
$$

for an upper bound and

$$
\sum _ { n = m + 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } > \int _ { m + 1 } ^ { \infty } { \frac { 1 } { t ^ { 2 } } } d t = - \frac { 1 } { m + 1 }
$$

for a lower bound on the "remaining summands" — or even

$$
\sum _ { n = m + 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } > \int _ { m + { \frac { 1 } { 2 } } } ^ { \infty } { \frac { 1 } { t ^ { 2 } } } d t = { \frac { 1 } { m + { \frac { 1 } { 2 } } } }
$$

if you are willing to do a slightly more carcful estimate, using that the function $\begin{array} { r } { f ( t ) = \frac { 1 } { l ^ { 2 } } } \end{array}$ is convex.

This means that our series does not converge too well; if we sum the first one thousand summands, then we expect an error in the third digit after the decimal point, while for the sum of the first onc million summands, mn = 100000o, we expcct to get an error in the sixth decimal digit, and we do. However, then comes a big surprise: to an accuracy of 45 digits,

π²2 /6 = 1.644934066848226436472415166646025189218949901, Σ 12 = 1.644933066848726436305748499979391855885616544.

So the sixth digit after the comma is wrong (too small by 1), but the next six digits are right! And then one digit is wrong (too large by 5), then again five are correct. This surprising discovery is quite recent, due to Roy D. North from Colorado Springs, 1988. (In 1982, Martin R. Powell, a school teacher from Amersham, Bucks, England, failed to notice the full effect due to the insufficient computing power available at the time.) It is too strange to be purely coincidental . .. A look at the error term, which again to 45 digits reads

reveals that clearly there is a pattern. You might try to rewrite this last number as

$$
\begin{array} { r } { + \ 1 0 ^ { \cdot \ 6 } \ - \ \frac { 1 } { 2 } \ 1 0 ^ { - 1 2 } \ + \ \frac { 1 } { 6 } \ 1 0 ^ { - 1 8 } \ - \ \frac { 1 } { 3 0 } \ 1 0 ^ { \cdot \ 3 0 } \ + \ \frac { 1 } { 4 2 } \ 1 0 ^ { \ 4 2 } \ + \ \dots . } \end{array}
$$

where the coefficients $( 1 , \cdots { \frac { 1 } { 2 } } ; { \frac { 1 } { 6 } } , 0 , - { \frac { 1 } { 3 0 } } , 0 , { \frac { 1 } { 4 2 } } )$ of $1 0 ^ { - 6 i }$ form the beginning of the sequencc of Bernoulli numbers that we'll meet again in Chapter 20. We refer our readers to the article by Borwein, Borwein & Dilcher [3] for more such surprising "coincidences" — and for proofs.

# Appendix: The Riemann zeta function

The Riemann zeta function $\zeta ( s )$ is defined for real $s > 1$ by

$$
\zeta ( s ) : = \sum _ { n \geq 1 } { \frac { 1 } { n ^ { s } } } .
$$

Our estimates for $H _ { \mathfrak { n } }$ (see page 10) imply that the series for $\zeta ( 1 )$ diverges, but for any real $s > 1$ it does converge. The zeta function has a canonical continuation to the entire complex plane (with one simple pole at $s = 1$ }, which can be constructed using power series expansions. The resulting complex function is of utmost importance for the theory of prime numbers. I et us mention three diverse connections:

)The remarkable identity

$$
\zeta ( s ) = \prod _ { p \atop p } { \frac { 1 } { 1 - p ^ { - s } } }
$$

is due to Euler. It encodes the basic fact that every natural number has a unique (!) decomposition into prime factors; using this, Euler's identity is a simple consequence of the geometric series expansion

$$
\frac { 1 } { 1 - p ^ { - s } } = 1 + \frac { 1 } { p ^ { s } } + \frac { 1 } { p ^ { 2 s } } + \frac { 1 } { p ^ { 3 s } } + \ldots
$$

(2) The location of the complex zeros of the zeta function is the subject of the "Riemann hypothesis": one of the most famous and important unresolved conjectures in all of mathematics. It claims that all the non-trivial zeros $s \in \mathbb { C }$ of the zeta function satisfy $R e ( s ) = \frac { 1 } { 2 }$ .(The zeta function vanishes at all the negative even integers, which are referred to as the "trivial zeros.")

Very recently, Jeff Lagarias showed that, surprisingly, the Ricmann hypothesis is equivalent to the following clcmentary statement: For all $n \geq 1$ ,

$$
\sum _ { d \mid n } d ~ \leq ~ H _ { n } ~ + ~ \exp ( H _ { n } ) \log ( H _ { n } ) ,
$$

with equality only for $\mathfrak { n } = 1$ , where $H _ { \pi }$ is again the $n$ -th harmonic number.

(3) It has been known for a long time that $\zeta ( s )$ is a rational multiple of $\pi ^ { s }$ , and hence irrational, if $s$ is an even integer $s \geq 2$ ; see Chapter 20. In contrast, the irrationality of $\zeta ( 3 )$ was proved by Roger Apéry only in 1979. Despite considerable effort the picture is rather incomplete about $\zeta ( s )$ for the other odd integers, $s = 2 t + 1 \geq 5$ Very recently, Keith Ball and Tanguy Rivoal proved that infinitely many of the values $\zeta ( 2 t + 1 )$ are irrational. And indecd, although it is not known for any single odd value $s \geq 5$ that $\zeta ( s )$ is irrational, Wadim Zudilin has proved that at least one of the four values $\zeta ( 5 ) , \zeta ( 7 ) , \zeta ( 9 ) .$ and $\zeta ( 1 1 )$ is irrational. We refer to the beautiful survey by Fischler [4].

# References

[1] K. BALL & T. RIvOAL: Irrationalité d'une infinité de valeurs de la fonction zéta aux enfiers impairs, Inventiones math. 146 (2001), 193-207.   
[2] F. BEUKERS, J. A. C. KOLK & E. CALABI: Sums of generalized harmonic series and volumes, Nieuw Archief voor Wiskunde (4) 11 (1993). 217-224.   
[3] J. M. BORWEIN. P. B. BORWEIN & K. DILCHER: Pi, Euler numbers, and asymptotic expansions, Amer. Math. Monthly 96 (1989), 681-687.   
[4] S. FisCHLER: Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, ... ). Bourbaki Seminar, No. 910, November 2002; to appear in Astérisque; Preprint arXiv:math.NT/0303066, March 2003, 45 pagcs.   
[5] J. C. LAGARIAS: An elemenlary problem equivalent to the Riemann hypothesis, Amer. Math. Monthly 109 (2002), 534-543.   
[6] W. J. LEVEQUE: Topics in Number Theory, Vol. I, Addison-Wesley, Rcading MA 1956.   
[7] A. M. YAGLOM & I. M. YAGLOM: Challenging mathematical problems with elementary solutions, Vol. II, Holden-Day, Inc., San Francisco, CA 1967.   
[8] W. Zupll.IN: Arithmetic of linear forms involving odd zeta values, Preprint, August 2001, 42 pagcs; arXiv:math.NT/0206176.

# Hilbert's third problem: decomposing polyhedra

# Chapter 8

In his legendary address to the International Congress of Mathematicians at Paris in 1900 David Hilbert asked — as the third of his twenty-three problems — to specify

"two tetrahedra of equal bases and equal altitudes which can in no way be split into congruent tetrahedra, and which cannot be combined with congruent tetrahedra to form two polyhedra which themselves could be split up into congruent tetrahedra."

This problem can be traced back to two letters of Carl Friedrich Gauss from 1844 (published in Gauss' collected works in 1900). If tetrahedra of equal volume could be split into congruent pieces, then this would give one an "elementary" proof of Euclid's theorem XII.5 that pyramids with the same base and height have the same volume. It would thus provide an elementary definition of the volume for polyhedra (that would not depend on analysis, and hence on continuity arguments). A similar statement is true in plane geometry: the Bolyai-Gerwien Theorem [1, Sect. 2.7] states that planar polygons are both equidecomposable (can be dissected into congruent triangles) and equicomplementable (can be made congruent by adding congruent triangles) if and only if they have the same area.

![](images/bcb14e4f85b821d85d3023febe6f59956d0ad3fa3f6f40d7316b7bd1d80a6de0.jpg)

![](images/0bc31fe62c07642a5539f2a4e1334eca48eaf46c114c0534cb8e619151eedf27.jpg)

David Hilbert

The cross is equicomplementable with a square of the same area.

In fact, they are even equidecomposable.

Hilbert — as we can see from his wording of the problem — did expect that there is no analogous theorem in dimension $3 ,$ and he was right. In fact, the problem was completely solved by Hilbert's student Max Dehn in two papers: the first one, exhibiting non-equidecomposable tetrahedra of equal base and height, appeared already in 1900, the second one, also covering equicomplementability, appeared in 1902. However, Dehn's papers are not easy to understand, and it takes effort to see whether Dehn did not fall into a subtle trap which ensnared others: a very-elegant-but-unfortunately-wrong proof was found by Bricard (in 1896!), by Meschkowski (1960), and probably by others. Luckily, Dehn's proof was reworked and redone, and after combined efforts of V. F. Kagan (1903/1930), Hugo Hadwiger (1949/54) and Vladimir G. Boltianskii, we now have a Book Proof — as follows. (The appendix to this chapter provides some basics about polyhedra.)

# (1) A little linear algebra

For every finite set of real numbers $M = \{ m _ { 1 } , . . . , m _ { k } \} \subseteq \mathbb { R } _ { }$ we define $V ( M )$ as the set of all linear combinations of numbers in $M$ with rational coefficients, that is,

$$
V ( M ) : = { \Bigl \{ } \sum _ { i = 1 } ^ { k } q _ { i } m _ { i } : q _ { i } \in \mathbb { Q } { \Bigr \} } \subseteq \mathbb { R } .
$$

The first (trivial, but important) observation is that $V ( M )$ is a finite dimensional vector space over the field $\mathbb { Q }$ of rational numbers. In fact, $V ( M )$ is clearly closed under taking sums and under multiplication with rationals, and the field axioms for $\mathbb { R }$ make $V ( M )$ into a vector space. The dimension of $V ( M )$ is the size of any minimal generating set. Since $M$ generates $V ( 1 1 1 )$ by definition, we see that it contains a minimal generating set, and hence

$$
\dim _ { \mathbb { Q } } V ( M ) \leq k = | M | .
$$

In the following, we shall need and use $\textcircled { 1 }$ -linear functions

$$
f : V ( M ) \to \mathbb { Q }
$$

which we interpret as linear maps of $\mathbb { Q }$ vector spaces. The key property is that for every rational linear dependence $\sum _ { i = 1 } ^ { k } q _ { i } \eta _ { i _ { i } } = 0$ with $q _ { i } \in \mathbb { Q }$ ,we must have $\begin{array} { r } { \sum _ { i - 1 } ^ { k } q _ { i } f ( m _ { i } ) = f ( 0 ) = 0 } \end{array}$ H  p things going.

Lemma. For any finite subsets $M \subseteq M ^ { \prime } o f \mathbb { R }$ , the $\nsubseteq$ -vector space $V ( M )$ is a subspace of the $\nsubseteq$ -vector space $V ( M ^ { \prime } )$ Thus if $f : V ( M ) \to \mathbb { Q }$ is $a \textcircled { 2 }$ -linear function, then $f$ can be extended to a $Q$ -linear function $f ^ { \prime }$ . $V ( \{ \mathcal { M } ^ { \prime } \} \to \mathbb { Q }$ so that $f ^ { \prime } ( \mathfrak { m } ) = f ( \mathfrak { m } )$ for all m  M.

Proof. Any $Q$ linear function $V ( M ) \to \mathbb { Q }$ is determined as soon as its values on a $\textcircled { 1 }$ -basis of $V ( M )$ are fixed. Since every basis of $V ( M )$ can be extended to a basis of $V ( M ^ { \prime } )$ , the rest follows. □

# ) Dehn invariants

For a 3-dimensional polyhedron $P$ , let $M p$ denote the set of all angles between adjacent facets (dihedral $a n g l e s )$ , together with the number $\pi$ . Thus for a cube $C$ we get $M _ { C } = \left\{ \frac { \pi } { 2 } , \pi \right\}$ , while for an orthogonal prism $q$ vn ual g $M _ { \it Q } = \left\{ \frac { \pi } { 3 } , \frac { \pi } { 3 } , \pi \right\}$ .

Given any finite set $M : \subseteq \mathbb { R }$ that contains $1 l _ { F }$ , and any $\nsubseteq$ -linear function

$$
f : V ( M ) \longrightarrow \mathbb { Q }
$$

that satisfies $f ( \pi ) = 0$ , we define the Dehn invariant of $P$ (with respect to $f )$ to be the real number

$$
D _ { f } ( P ) : = \sum _ { \epsilon \in P } \ell ( e ) \cdot f ( \alpha ( e ) ) ,
$$

where the sum extends over all edges $\epsilon$ of the polyhedron, $i ( c )$ denotes the length of $e$ , and $a ( p )$ is the angle betwcen the two facets that meet in $\epsilon$ .

We will calculate various Dehn invariants later. For now just note that $f \left( { \frac { \pi } { 2 } } \right) \ = \ { \frac { 1 } { 2 } } f ( \pi ) \ = \ 0$ must hold for any such $Q$ -linear function $f$ ,and thus

$$
D _ { f } ( { \cal { C } } ) = 0 { } _ { ; }
$$

t is, te z $f$ .

# (3) The Dehn-Hadwiger theorem

As above we call two polyhedra $P , Q$ equidecomposable if they can be decomposed into finite sets of polyhedra $P _ { 1 } , \ldots , P _ { n }$ and $( 2 _ { 1 } , \ldots , 2 _ { n }$ such that $P _ { i }$ and $Q _ { i }$ are congruent for all $i$ $( 1 \leq i \leq \pi )$ . Two polyhedra are equicomplementable if there are polyhedra $\boldsymbol { P } _ { 1 } \ldots \ldots \boldsymbol { P } _ { r r }$ and $\mathcal { Q } _ { 1 } , \ldots , \mathcal { Q } _ { m }$ so that the interiors of the $P _ { i }$ are disjoint from each other and from $P$ , and similarly for the $Q _ { i }$ and $i$ , such that $P _ { i }$ is congruent to $Q _ { i }$ for all $i$ , and such that $\smash { \tilde { P } : = P \cup P _ { 1 } \cup P _ { 2 } \cup . . . \cup P _ { m } }$ and $\widetilde { Q } : = \bigcup \cup \bigcup _ { 1 } \cup Q _ { 2 } \cup \ldots \cup Q _ { m }$ are cquidecomposable. A theorem of Gerling from 1 844 implies that it does not matter whether we admit reflections when considering congruences, or not. Clearly equidecomposable polyhedra are equicomplementable, but the converse is far from clear. The following theorem of Hadwiger (in the version of Boltianski) provides our tool to find — as Hilbert proposed— tetrahedra of equal volume that are not cquicomplementable, and thus not equidecomposable.

Theorem. Let $P$ and $Q$ be polyhedra with dihedral angles $( { \mathcal { X } } _ { 1 } , \dotsc , { \mathcal { X } } _ { p } \ \dotsc$ resp. $i 3 _ { 1 } , \ldots , \beta _ { q }$ at their edges, and let $1 1$ be $\alpha$ finite set of real numbers with

$$
\left\{ \alpha _ { 1 } , \ldots , \alpha _ { p } , \beta _ { 1 } , \ldots , \beta _ { q } , \pi \right\} \subseteq M .
$$

$I f f : V ( M ) \longrightarrow \mathbb { Q }$ is any $\textcircled { 1 }$ -linear function with $f ( \pi ) = 0$ such that

$$
\begin{array} { r } { D _ { j } ( P ) \neq D _ { j } ( Q ) , } \end{array}
$$

then $P$ and $q$ are not equicomplementable.

![](images/da1f98945b1e9a22d7769e89f9ee12a4c5e838b9ac0646958b607bf1c1be5a0b.jpg)

$$
M _ { \zeta } = \{ \textstyle { \frac { \pi } { 2 } } , \pi \}
$$

![](images/599975a5b9afed45ca8ca1fafdd197214ed8ffc11abc8d485113d1a4e043edce.jpg)

Proof. The argument comes in two parts.

(1) If a polyhedron $P$ has a decomposition into finitely many polyhedral pieces $P _ { 1 } , \ldots , P _ { n }$ , and if all the dihedral angles of the pieces $P _ { 1 } , \ldots , P _ { n }$ are contained in the set $M$ then for every $\Updownarrow$ -linear $f : V ( M ) \to \mathbb { Q } .$ ,the Dehn invariants add up:

$$
D _ { f } ( P ; \ = \ D _ { f } ( P _ { 1 } ) + \ldots + I ) _ { f } ( P _ { n } ) .
$$

Y

For this, we associate a mass to any part of an edge of a polyhedron: if $R ^ { \prime } \subseteq { \mathcal { S } }$ is a part of an edge $e$ of $P$ , then its mass will be

$$
m _ { f } ( e ^ { \prime } ) : = \ell ( e ^ { \prime } ) f ( \alpha ( e ^ { \prime } ) ) ,
$$

its length times the $f$ value of its dihedral angle.

Now if $P$ is decomposed into $F _ { 1 } , \ldots , P _ { n }$ , consider the union of all the edges of the pieces $P _ { i }$ Along the edges $e ^ { f }$ that are contained in edges of $P$ we see that the dihedral angles of the pieces add up to the dihedral angle of $P$ at $e ^ { i }$ , and hence the masses add up.

At any other edge $e ^ { i \mu }$ of one of the $I _ { i } ^ { 2 }$ 's which is contained in the interior of a face of $P$ or in the interior of $P$ , the angles add up to $\pi$ or to $2 \pi$ ,so the $f$ -values of the angles in the pieces add up to $f ( \pi ) = 0$ resp. to $f ( 2 \pi ) = 0$ . Thus for the sum of the masses we get the same value that we had attached to these edges for $P$ in the first place, namely 0.

() Assuming that $P$ and $i$ are equicomplementable, we can enlarge $M$ to a superset $M ^ { f ^ { f } }$ that also includes all the dihedral angles appearing in any of the pieces involved. $M ^ { \prime }$ is finite, since we only consider finite decompositions. Then our lemma above allows us to extend $f ^ { \prime }$ to $f ^ { \prime } : V ( M ^ { \prime } ) \to \mathbb { Q } .$ ,and hence part (1) yields an equation of the type

$$
D _ { f ^ { \prime } } ( P ) + D _ { f ^ { \prime } } ( P _ { 1 } ) + \ldots + D _ { f ^ { \prime } } ( P _ { m } ) = D _ { f ^ { \prime } } ( Q ) + D _ { f ^ { \prime } } ( Q _ { 1 } ) + \ldots + D _ { f ^ { \prime } } ( Q _ { m } )
$$

where $D _ { f ^ { \prime } } ( P _ { i } ) = I ) _ { f ^ { \prime } } ( Q _ { i } )$ since $P _ { i }$ and $Q _ { i }$ are congruent. Hence we conclude $D _ { f } ( P ) \subset D _ { f } ( Q )$ , a contradiction. □

![](images/2ee90d833bef8d88305989f52c6859126e8a5b58e2e8fad6ab899eda872f848e.jpg)

Example 1. For a regular tetrahedron $T _ { 0 }$ with edge lengths $\ell$ ,we calculate the dihedral angle from the sketch. The midpoint $M$ of the base triangle divides the height $A E$ of the base triangle by 1:2, and since $| A E | = | I ) E |$ , we find cos $\begin{array} { r } { \alpha = \frac { 1 } { \frac { 1 } { 3 } } } \end{array}$ , and thus

$$
\alpha \ = \ \operatorname { a r c c o s } { \frac { 1 } { 3 } } ,
$$

Setting $M : = \{ \alpha , \pi \}$ we note that the ratio

$$
{ \frac { \alpha } { \pi } } ~ = ~ { \frac { 1 } { \pi } } \operatorname { a r c c o s } { \frac { 1 } { 3 } }
$$

is irrational, according to Theorem 3 of Chapter 6 (taking $\eta , = 9 ,$ .Thus the $\textcircled { 1 }$ -vector space $V ( M )$ is 2-dimensional with basis $M$ , and there is a $\textcircled { 1 }$ linear function $f : V ( M ) \to \mathbb { Q }$ with

$$
f ( \alpha ) : = 1 , f ( \pi ) : = 0 .
$$

For this $j$ we have

$$
D _ { f } ( T _ { 0 } ) ~ = ~ 6 \ell f ( \alpha ) ~ = ~ 6 \ell ~ \neq ~ 0 ,
$$

and thus a regular tetrahedron cannot be equidecomposable or equicomplementable with a cuhe, since the Dehn invariant of a cube vanishes for any $f$ .

Example 2. Let $T _ { \mathrm { I } }$ be a tctrahedron spanned by three orthogonal edges $\angle 1 B , \angle 1 C , \angle 1 D$ of length $\mathcal { U }$ This tetrahedron has three dihedral angles that are right angles, and thrce more dihedral angles of equal size $4 .$ ,which we calculate from the sketch as

$$
\cos \varphi = \frac { | A E | } { | D E | } = \frac { \frac { 1 } { 2 } \sqrt { 2 } u } { \frac { 1 } { 2 } \sqrt { 3 } \sqrt { 2 } u } = \frac { 1 } { \sqrt { 3 } } .
$$

It follows that

$$
\varphi = \operatorname { a r c c o s } { \frac { 1 } { \sqrt { 3 } } } .
$$

For $\begin{array} { r } { M : = \left\{ \frac { \pi } { 2 } , \operatorname { a r c c o s } \frac { 1 } { \sqrt { 3 } } , \pi \right\} } \end{array}$ , the $\mathbb { Q }$ vector space $V ( M )$ has dimension 2. In fact, $\pi$ and $\frac { \pi } { 2 }$ are linearly dependent, so $V ( M ) = V \big ( \{ \operatorname { a r c c o s } \frac { 1 } { \sqrt { 3 } } , \pi \} \big )$ , $\textstyle { \frac { 1 } { \sqrt { 3 } } }$ and $\pi$ = equivalently, $\frac { 1 } { \pi } \operatorname { a r c c o s } \frac { 1 } { \sqrt { 3 } }$ is al, as e provin Chaer6 $n = 3$ in Thm. 3). Thus we may construct a $\nsubseteq$ -linear map $f$ by setting

$$
f ( \pi ) : = \varnothing \quad { \mathrm { a n d } } \quad f { \big ( } \operatorname { a r c c o s } { \textstyle \frac { 1 } { \sqrt { 3 } } } { \big ) } : = 1 ,
$$

from which we obtain $f ( \frac { \pi } { 2 } ) = 0$ and hence

$$
D _ { f } ( T _ { 1 } ) = 3 u f \bigl ( { \frac { \pi } { 2 } } \bigr ) + 3 \bigl ( \sqrt { 2 } u \bigr ) f \bigl ( \operatorname { a r c c o s } { \frac { 1 } { \sqrt { 3 } } } \bigr ) = 3 \sqrt { 2 } u \neq 0 .
$$

This proves that $T _ { 1 }$ is not equidecomposable or equicomplementable with a cube $C$ of the same volume, since $D _ { f } ( C ) = \mathbb { 0 }$ holds for any $f$ .

Example 3. Finally, let $T _ { 2 }$ be a tetrahedron with three consecutive edges $A B , B C$ and $C P$ that are mutually orthogonal (an "orthoscheme") and of the same length $u$ .

$\frac \pi 2 , \frac \pi 3$ and $\scriptstyle { \frac { \pi } { 4 } } )$ , but rather argue that - using the midpoints of edges and faces, and the center — a cube of edge length ${ \mathcal { U } }$ can be decomposed into 6 tetrahedra of this type (3 congruent copies, and 3 mirror images).

All these congruent copies and mirror images have the same Dehn invariants, and hence for every suitable functional $f$ we will obtain

$$
D _ { f } ( T _ { 2 } ) = { \frac { 1 } { 6 } } D _ { f } ( G ) = 0
$$

so all Dehn invariants of such a tetrahedron vanish! This solves Hilbert's third problem, since we have before constructed a different tetrahedron, $T _ { 1 }$ , with congruent bases and the same height, and with $D _ { f } ( \mathbf { \dot { \bar { f } } } _ { 1 } ^ { \prime } ) \neq 0$ By the Dehn-Hadwiger theorem $T _ { 1 }$ and $T _ { 2 }$ are not equidecomposable, and not even equicomplementable.

![](images/59a8a72db70febfd201ef0f36087452884196a0931e035d8a1ecb596449e5d89.jpg)

![](images/57713213788438b87b539cb3e1187a9fb178b7ca873356ff47681a66047d50a9.jpg)

![](images/d57ef1aa7eb5d5ea01f6fa512cfa75f8cc8919e07f12e83cd14956c5af7cd7b8.jpg)

![](images/1258f6e1acea8fe62db8226e719eb1fd35395fcf77c78420dc82297550285919.jpg)

![](images/f4107bd6a0dfe0c3326a17441e2b32d397941ca658c2d9d21ec62e41fd3fa6cf.jpg)

Some familiar polytopes: tetrahedron, cube and permutahedron

# Appendix: Polytopes and polyhedra

A convex polytope in $\mathbb { R } ^ { d }$ is tee ul $S = \{ \pmb { s } _ { 1 } , \ldots , \pmb { s } _ { n } \}$ , that is, a set of the form

$$
P = \mathsf { c o n v } ( S ) : = \Big \{ \sum _ { i = 1 } ^ { n } \lambda _ { i } \pmb { s } _ { i } : \lambda _ { i } \ge 0 , \sum _ { i = 1 } ^ { n } \lambda _ { i } = 1 \Big \} .
$$

Polytopes are certainly familiar objects: prime examples are given by convex polygons (2-dimensional convex polytopes) and by convex polyhedra (3-dimensional convex polytopes).

There are several types of polyhedra that generalize to higher dimensions in a natural way. For example, if the set $S$ is affinely independent of cardinality $d + 1$ , then $\mathsf { c o n v } ( S )$ is a $d$ -dimensional simplex (or $d$ simplex). For $d = 2$ this yields a triangle, for $d = 3$ we obtain a tetrahedron. Similarly, squares and cubes are special cases of $d$ -cubes, such as the unit $d$ -cube given by $C _ { d } = [ 0 , 1 ] ^ { d } \subseteq \mathbb { R } ^ { d }$ .

General polytopes are defined as finite unions of convex polytopes. In this book non-convex polyhedra will appear in connection with Cauchy's rigidity theorem in Chapter 12, and non-convex polygons in connection with Pick's theorem in Chapter 11, and again when we discuss the art gallery theorem in Chapter 31.

Convex polytopes can, equivalently, be defined as the bounded solution sets of finite systems of linear inequalities. Thus every convex polytope $P \subseteq \mathbb { R } ^ { d }$ has a representation of the form

$$
P \ = \ \{ \pmb { x } \in \mathbb { R } ^ { d } : A \pmb { x } \leq \pmb { b } \}
$$

for some matrix $A \in \mathbb { R } ^ { m \times d }$ and a vector $\pmb { b } \in \mathbb { R } ^ { m }$ . In other words, $P$ is the solution set of a system of $m$ linear inequalities ${ \pmb a } _ { i } ^ { T } { \pmb x } \leq b _ { i }$ , where $\pmb { a } _ { i } ^ { T }$ is the $i$ -th row of $A$ Conversely, every bounded such solution set is a convex polytope, and can thus be represented as the convex hull of a finite set of points.

For polygons and polyhedra, we have the familiar concepts of vertices, edges, and 2-faces. For higher-dimensional convex polytopes, we can define their faces as follows: a face of $P$ is a subset ${ \textbf { \textit { F } } } \subseteq { \boldsymbol { \textit { P } } }$ of the form $P \cap \left\{ \pmb { x } \in \mathbb { R } ^ { d } : \pmb { a } ^ { T } \pmb { x } = b \right\}$ , where ${ \pmb { a } } ^ { T } { \pmb { x } } \le { \pmb { b } }$ is a linear inequality that is valid for all points ${ \pmb x } \in P$ .

All the faces of a polytope are themselves polytopes. The set $V$ of vertices (0-dimensional faces) of a convex polytope is also the inclusion-minimal set such that co $\mathfrak { n v } ( V ) = P$ Assuming that $P \subseteq \mathbb { R } ^ { d }$ is a $d$ -dimensional convex polytope, the facets (the $( d { - } 1 )$ -dimensional faces) determine a minimal set of hyperplanes and thus of halfspaces that contain $P$ , and whose intersection is $P$ . In particular, this implies the following fact that we will need later: Let $F$ be a facet of $P$ , denote by $H _ { F }$ the hyperplane it determines, and by $H _ { F } ^ { + }$ and $H _ { F } ^ { - }$ the two closed half-spaces bounded by $H _ { F }$ . Then one of these two halfspaces contains $P$ (and the other one doesn't).

The graph $G ( P )$ of the convex polytope $P$ is given by the set $V$ of vertices, and by the edge set $E$ of 1-dimensional faces. If $P$ has dimension 3, then this graph is planar, and gives rise to the famous "Euler polyhedron formula" (see Chapter 11).

Two polytopes $P , P ^ { \prime } \subseteq \mathbb { R } ^ { d }$ are congruent if there is som ngth-preving affine map that takes $P$ to $P ^ { \prime }$ . Such a map may reverse the orientation of space, as does the reflection of $P$ in a hyperplane, which takes $P$ to a mirror image of $P$ . They are combinatorially equivalent if there is a bijection from the faces of $P$ to the faces of $P ^ { \prime }$ that preserves dimension and inclusions between the faces. This notion of combinatorial equivalence is much weaker than congruence: for example, our figure shows a unit cube and a "skew" cube that are combinatorially equivalent (and thus we would call any one of them "a cube"), but they are certainly not congruent.

A polytope (or a more general subset of $\mathbb { R } ^ { d }$ ) is called centrally symmetric if there is some point $\pmb { x } _ { 0 } \in \mathbb { R } ^ { d }$ such that

![](images/31ff4d32d168102c41b5201bb09205aa55ad2532fc93b1c0b461186118a27bb5.jpg)

$$
\pmb { x } _ { 0 } + \pmb { x } \in P \quad \Longleftrightarrow \quad \pmb { x } _ { 0 } - \pmb { x } \in P .
$$

In this situation we call $\scriptstyle { \mathbf { x } } _ { 0 }$ the center of $P$ .

# References

![](images/b694357a8a0f28f68de99c514aadcd5c9bc5f86f8cbb83e0d397a3c49327e140.jpg)  
Combinatorially equivalent polytopes

[1] V. G. BOLTIANSKII: Hilbert's Third Problem, V. H. Winston & Sons (Halsted Press, John Wiley & Sons), Washington DC 1978.   
[2] M. DEHN: Ueber raumgleiche Polyeder, Nachrichten von der Königl. Gesellschaft der Wissenschaften, Mathematisch-physikalische Klasse (1900), 345-354.   
[3] M. DEHN: Ueber den Rauminhalt, Mathematische Annalen 55 (1902), 465-478.   
[4] C. F. GAUss: "Congruenz und Symmetrie": Briefwechsel mit Gerling, pp. 240-249 in: Werke, Band VIII, Königl. Gesellschaft der Wissenschaften zu Göttingen; B. G. Teubner, Leipzig 1900.   
[5] D. HILBERT: Mathematical Problems, Lecture delivered at the International Congress of Mathematicians at Paris in 1900, Bulletin Amer. Math. Soc. 8 (1902), 437-479.   
[6] G. M. ZiEGLER: Lectures on Polytopes, Graduate Texts in Mathematics 152, Springer-Verlag, New York 1995/1998.

# Lines in the plane and decompositions of graphs

Perhaps the best-known problem on configurations of lines was raised by Sylvester in 1893 in a column of mathematical problems.

# QUESTIONS FOR SOLUTION.

1185l. (Professor SyLvesTek.)-Prove that it is not possible to arrange any finite number of rcal'points so that a right line through every two of them shall pass through a third, unless they all lie in the same right line.

Whether Sylvester himself had a proof is in doubt, but a correct proof was given by Tibor Gallai [Grünwald] some 40 years later. Therefore the following theorem is commonly attributed to Sylvester and Gallai. Subsequent to Gallai's proof several others appeared, but the following argument due to L. M. Kelly may be "simply the best."

Theorem 1. In any configuration of n points in the plane, not all on a line, there is a line which contains exactly two of the points.

Proof. Let $\mathcal { P }$ be the given set of points and consider the set $\mathcal { L }$ of all lines which pass through at least two points of $\mathcal { P }$ . Among all pairs $( P , \ell )$ with $P$ not on $\ell$ , choose a pair $( P _ { 0 } , \ell _ { 0 } )$ such that $P _ { 0 }$ has the smallest distance to $\ell _ { 0 }$ , with $Q$ being the point on $\ell _ { 0 }$ closest to $P _ { 0 }$ (that is, on the line through $P _ { 0 }$ vertical to $\ell _ { 0 }$ ).

Claim. This line $\ell _ { 0 }$ does it!

If not, then $\ell _ { 0 }$ contains at least three points of $\mathcal { P }$ , and thus two of them, say $P _ { 1 }$ and $P _ { 2 }$ , lie on the same side of $Q$ . Let us assume that $P _ { 1 }$ lies between $Q$ and $P _ { 2 }$ , where $P _ { 1 }$ possibly coincides with $Q$ . The figure on the right shows the configuration. It follows that the distance of $P _ { 1 }$ to the line $\ell _ { 1 }$ determined by $P _ { 0 }$ and $P _ { 2 }$ is smaller than the distance of $P _ { 0 }$ to $\ell _ { 0 }$ , and this contradicts our choice for $\ell _ { 0 }$ and $P _ { 0 }$

In the proof we have used metric axioms (shortest distance) and order axioms $P _ { 1 }$ lies between $Q$ and $P _ { 2 }$ ) of the real plane. Do we really need these properties beyond the usual incidence axioms of points and lines? Well, some additional condition is required, as the famous Fano plane depicted in the margin demonstrates. Here $\mathcal { P } = \{ 1 , 2 , . . . , 7 \}$ and $\mathcal { L }$ consists of the 7 three-point lines as indicated in the figure, including the "line" $\{ 4 , 5 , 6 \}$ . Any two points determine a unique line, so the incidence axioms are satisfied, but there is no 2-point line. The Sylvester-Gallai theorem therefore shows that the Fano configuration cannot be embedded into the real plane such that the seven collinear triples lie on real lines: there must always be a "crooked" line.

![](images/dcbc42ebeeb89be0831efe602a04924a2fc92bdea38b8447423874c7f91a4156.jpg)  
J. J. Sylvester

![](images/3047ff2e4755f08ef229a91e0d558549ff43edbf8ebe0ad97a6bd43dc9e71887.jpg)

![](images/6f51d1aaa1bece1de4e006ecc0d8bf1f4708acb77c8d2739e779036ffc5d3256.jpg)

However, it was shown by Coxeter that the order axioms will suffice for a proof of the Sylvester-Gallai theorem. Thus one can devise a proof that does not use any metric properties — see also the proof that we will give in Chapter 1 1, using Euler's formula.

The Sylvester-Gallai theorem directly implies another famous result on points and lines in the plane, due to Paul Erdós and Nicolaas G. de Bruijn. But in this case the result holds more generally for arbitrary point-line systems, as was observed already by Erdös and de Bruijn. We will discuss the more general result in a moment.

Theorem 2. Let $p$ be a set of $n \geq 3$ points in the plane, not all on a line. Then the set $L$ of lines passing through at least two points contains at least $n$ lines.

Proof. For $\mathfrak { n } = 3$ there is nothing to show. Now we proceed by induction on $n$ Let $| \mathcal { P } | = \eta + 1$ . By the previous theorem there exists a line $l _ { 0 } \in L$ containing exactly two points $P$ and $Q$ of $p$ .Consider the set ${ \mathcal { P } } ^ { \prime } = { \mathcal { P } } \backslash \{ Q \}$ and the set $L ^ { r }$ of lines determined by $P ^ { \prime }$ . If the points of $P ^ { \prime }$ do not all lie on a single line, then by induction $| \mathcal { L } ^ { \prime } | \geq n$ and hence $| { \mathcal { L } } | \geq \pi + 1$ because of the additional line $\ell _ { 0 }$ in $L$ . If, on the other hand, the points in $p ^ { i }$ are all on a single line, then we have the "pencil" which results in precisely $n + 1$ lines.

Now, as promised, here is the general result, which applies to much more general "incidence geometries."

Theorem 3. Let $X$ be a set of $n \geq 3$ elements, and let $A _ { 1 } , \ldots , A _ { m }$ be proper subsets of $X$ , such that every pair of elements of $X$ is contained in precisely one set $A _ { i }$ . Then $m \geq n$ holds.

Proof. The following proof, variously attributed to Motzkin or Conway, is almost one-line and truly inspired. For $x \in X$ let $r _ { x }$ be the number of sets $A _ { i }$ containing $\mathcal { X }$ . (Note that $2 \leq r _ { x } < r r _ { l }$ by the assumptions.) Now if $x \notin A _ { i }$ , then $r _ { x } \geq | { \cal { A } } _ { i } |$ because the $| \varLambda _ { i } |$ sets containing $\mathcal { X }$ and an element of $A _ { i }$ must be distinct. Suppose m $< n$ , then $m | A _ { i } | ~ < ~ n r _ { \mathrm { { x } } }$ and thus $m ( n - | A _ { i } | ) > n ( m - r _ { x } )$ for $x \notin A _ { i }$ , and we find

$$
1 = \sum _ { x \in X } \frac { 1 } { n } = \sum _ { x \in X } \sum _ { A _ { i } : x \notin A _ { i } } \frac { 1 } { n ( m - r _ { x } ) } > \sum _ { A _ { i } } \sum _ { x : x \notin A _ { i } } \frac { 1 } { m ( n - | A _ { i } | ) } = \sum _ { A _ { i } } \frac { 1 } { m } = 1 ,
$$

which is absurd.

There is another very short proof for this theorem that uses linear algebra. Let $B$ be the incidence matrix of $( X ; A _ { 1 } , \ldots , A _ { m } )$ , that is, the rows in $B$ are indexed by the elements of $X$ , the columns by $A _ { 1 } , \ldots , A _ { \tau \tau 2 }$ , where

$$
B _ { x A } : = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f } } \quad x \in A } \\ { 0 } & { { \mathrm { i f } } \quad x \notin A . } \end{array} \right. }
$$

Consider the product $B B ^ { \prime }$ . For $x \neq x ^ { \prime }$ we have $( B B ^ { T } ) _ { \tt T \cdot x ^ { \prime } } \ : = \ : 1$ , since $x$

and $x ^ { \prime }$ are contained in precisely one set $\varLambda _ { i }$ , hence

$$
B B ^ { \prime \prime } = \left( \begin{array} { c c c c } { { r _ { x _ { 1 } } - 1 } } & { { 0 } } & { { \ldots } } & { { 0 } } \\ { { 0 } } & { { r _ { x _ { 2 } } - 1 } } & { { } } & { { \vdots } } \\ { { \vdots } } & { { } } & { { \ddots } } & { { 0 } } \\ { { 0 } } & { { \ldots } } & { { 0 } } & { { r _ { x _ { n } } - 1 } } \end{array} \right) + \left( \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { \ldots } } & { { 1 } } \\ { { 1 } } & { { 1 } } & { { } } & { { \vdots } } \\ { { \vdots } } & { { } } & { { \ddots } } & { { 1 } } \\ { { 1 } } & { { \ldots } } & { { 1 } } & { { 1 } } \end{array} \right)
$$

where $r _ { x }$ is defined as above. Since the first matrix is positive definite (it has only positive eigenvalues) and the second matrix is positive semi-definite (it has the eigenvalues $n ,$ and 0), we deduce that $B B ^ { T }$ is positive definite and thus, in particular, invertible, implying rank $\langle B B ^ { T } \rangle ~ = ~ \pi$ It follows that the rank of the $( r \iota \times r \iota )$ -matrix $B$ is at least $n$ , and we conclude that indeed $n \leq m$ , since the rank cannot exceed the number of columns.

Let us go a little beyond and turn to graph theory. (We refer to the review of basic graph concepts in the appendix to this chapter.) A moment's thought shows that the following statement is really the same as Theorem 3:

If we decompose a complete graph $K _ { n }$ into m cliques different from $K _ { n }$ , such that every edge is in a unique clique, then $m \geq n$ .

Indeed, let $X$ correspond to the vertex set of $K _ { \pi }$ and the sets $\pmb { A } _ { i }$ to the vertex sets of the cliques, then the statements are identical.

Our next task is to decompose $K _ { \pi }$ into complete bipartite graphs such that again every edge is in exactly one of these graphs. There is an easy way to do this. Number the vertices $\{ 1 , 2 , \ldots , n \}$ First take the complete bipartite graph joining 1 to all other vertices. Thus we obtain the graph $K _ { 1 , n - 1 }$ which is called a star. Next join ${ \textrm { 2 } } 1 0 \ 3 , \ldots , n$ , resulting in a star $K _ { 1 , \pi - 2 }$ . Going on like this, we decompose $K _ { \pi }$ into stars $K _ { 1 , n - 1 } , K _ { 1 , n - 2 } , \ldots , K _ { 1 , 1 }$ . This decomposition uses $\hbar - 1$ complete bipartite graphs. Can we do better, that is, use fewer graphs? $\mathbf { N o }$ , as the following result of Ron Graham and Henry O. Pollak says:

Theorem 4. If $K _ { n }$ is decomposed into complete bipartite subgraphs $H _ { 1 } , \ldots , H _ { m }$ , then $m \geq \pi - 1$ .

The interesting thing is that, in contrast to the Erdós-de Bruijn theorem, no combinatorial proof for this result is known! All of them use linear algebra in one way or another. Of the various more or less equivalent ideas let us look at the proof due to Tverberg, which may be the most transparent.

Proof. Let the vertex set of $K _ { \pi }$ be $\{ 1 , \ldots , n \}$ , and let $L _ { j } , R _ { j }$ be the defining vertex sets of the complete bipartite graph $H _ { j }$ , $j = 1 , \dots , m$ To every vertex $i$ we associate a variable $x _ { i }$ . Since $H _ { 1 } , \ldots , H _ { m }$ decompose $K _ { n }$ , we find

$$
\sum _ { i < j } x _ { i } x _ { j } = \sum _ { k = 1 } ^ { m } ( \sum _ { a , \in I _ { k } } x _ { a } \cdot \sum _ { b \in R _ { k } } x _ { b } ) .
$$

![](images/e6ddfc0f309a4b37e706d3a9c81ea99696d8a73750cc5f89f19e68a34bd072d1.jpg)  
A decomposition of $\bar { k _ { \mathrm { ~ 5 ~ } } }$ into 4 complete bipartite subgraphs

Now suppose the theorem is false, $m < \mathfrak { n } \mathfrak { a } \mathfrak { - 1 }$ Then the system of linear

equations

$$
\begin{array} { r c l } { x _ { 1 } + \ldots + x _ { n } } & { = } & { 0 , } \\ { \displaystyle \sum _ { \mathfrak { a } \in L _ { k } } x _ { a } } & { = } & { 0 \qquad ( k = 1 , \ldots , m ) } \end{array}
$$

has fewer equations than variables, hence there cxists a non-trivial solution ${ \vec { c } } _ { 1 } , \dots , { \vec { c } } _ { \gamma _ { 2 } }$ .From (1) we infer

$$
\sum _ { i < j } c _ { i } c _ { \cdot j } = 0 .
$$

But this implics

$$
0 ~ = ~ ( c _ { 1 } + . . . + c _ { n } ) ^ { 2 } ~ = ~ \sum _ { i = 1 } ^ { n } c _ { i } ^ { 2 } + 2 \sum _ { i < j } c _ { i } c _ { j } ~ = ~ \sum _ { i - 1 } ^ { n } c _ { i } ^ { 2 } ~ > ~ 0 ,
$$

a contradiction, and the proof is complete.

![](images/60d24a2e15cd39c93fafb513018b7fe5e7bdb896790794590a8801a75dc5ac24.jpg)

A graph $G$ with 7 vertices and 11 edges. It has onc loop, onc double edge and onc triple edge.

# Appendix: Basic graph concepts

Graphs are among the most basic of all mathematical structures. Correspondingly, they have many different versions, representations, and incarnations. Abstractly, a graph is a pair $\tilde { G } = \{ V , E \}$ , wherc $V$ is the set of vertices, $E$ is the set of edges, and each edge $\epsilon \in E$ "connects" two vertices $v , u ) \in V$ .We consider only finite graphs, where $V$ and $E$ are finite.

Usually, we deal with simple graphs: Then we do not admit loops, i. e., edges for which both ends coincide, and no multiple edges that have the same set of endvertices. Vertices of a graph are called adjacent or neighbors if they are the endvertices of an edge. A vertex and an edge are called incident if the edge has the vertex as an cndvertex.

Here is a little picture gallery of important (simple) graphs:

The complete graphs $K _ { \eta }$ on $n$ vertices and $\binom { \pi } { 2 }$ edges

K2 K K K5   
K1,1 K 1,2 K1,3 X K2,2 K2,3 K2,4 K3,3

The complete bipartite graphs $K _ { r \eta , \eta ; \eta }$ with $m + n$ vertices and mn cdgcs

BBABA B $C _ { 3 }$ Δ: : 7 $C _ { 4 }$ $C _ { 5 }$ $C _ { 6 }$

Two graphs $G = ( V , E )$ and $G ^ { \prime } = ( \boldsymbol { V } ^ { \prime } , \boldsymbol { E } ^ { \prime } )$ are considered isomorphic if there are bijections $V  V ^ { \prime }$ and $E \to E ^ { \prime }$ that preserve the incidences between edges and their endvertices. (It is a major unsolved problem whether there is an efficient test to decide whether two given graphs are isomorphic.) This notion of isomorphism allows us to talk about the complete graph $K _ { 5 }$ on 5 vertices, etc.

$G ^ { \prime } = ( V ^ { \prime } , E ^ { \prime } )$ is a subgraph of $G = ( V , E )$ if $V ^ { \prime } \subseteq V , E ^ { \prime } \subseteq E$ , and every edge $\textit { e } \in \textit { E } ^ { \prime }$ has the same endvertices in $G ^ { \prime }$ as in $G$ b $G ^ { \prime }$ is an induced subgraph if, additionally, all edges of $G$ that connect vertices of $G ^ { \prime }$ are also edges of $G ^ { \prime }$ .

Many notions about graphs are quite intuitive: for example, a graph $G$ is connected if every two distinct vertices are connected by a path in $G$ , or equivalently, if $G$ cannot be split into two nonempty subgraphs whose vertex sets are disjoint.

We end this survey of basic graph concepts with a few more pieces of terminology: A clique in $G$ is a complete subgraph. An independent set in $G$ is an induced subgraph without edges, that is, a subset of the vertex set such that no two vertices are connected by an edge of $G$ A graph is a forest if it does not contain any cycles. A tree is a connected forest. Finally, a graph $G = ( V , E )$ is bipartite if it is isomorphic to a subgraph of a complete bipartite graph, that is, if its vertex set can be written as a union $V = V _ { 1 } \cup V _ { 2 }$ of two independent sets.

# References

[1] N. G. DE BruIjN & P. ERDóS: On a combinatorial problem, Proc. Kon. Ned. Akad. Wetensch. 51 (1948), 1277-1279.   
[2] H. S. M. CoxETER: A problem of collinear points, Amer. Math. Monthly 55 (1948), 26-28 (contains Kelly's proof).   
[3] P. ERDós: Problem 4065 — Three point collinearity, Amer. Math. Monthly 51 (1944), 169-171 (contains Gallai's proof).   
[4] R. L. GRAHAM & H. O. POLLAK: On the addressing problem for loop switching, Bell System Tech. J. 50 (1971), 2495-2519.   
[5] J. J. SYLVESTER: Mathematical Question 11851, The Educational Times 46 (1893), 156.   
[6] H. TvERBERG: On the decomposition of $K _ { n }$ into complete bipartite graphs, J. Graph Theory 6 (1982), 493-494.

The paths $P _ { n }$ with $^ n$ vertices

The cycles $C _ { n }$ with $_ n$ vertices is a subgraph of

![](images/8b0a244611a173fa2c19e1027aa958e41af6fe26846cfb473336f4152387678d.jpg)

# The slope problem

Try for yourself — before you read much further — to construct configurations of points in the plane that determine "relatively few" slopes. For this we assume, of course, that the $n \geq 3$ points do not all lie on one line. Recall from Chapter 9 on "Lines in the plane" the theorem of Erdôs and de Bruijn: the $_ n$ points will determine at least $n$ different lines. But of course many of these lines may be parallel, and thus determine the same slope.

![](images/9982d8b0875e5305cfd01e3db240af499491d7d95a41b272f88cf56533a2d9c7.jpg)

After some attempts at finding configurations with fewer slopes you might conjecture — as Scott did in 1970 — the following theorem.

Theorem. If $n \geq 3$ points in the plane do not lie on one single line, then they determine at least $n - 1$ different slopes, where equality is possible only if $n$ is odd and $n \geq 5$ .

Our examples above — the drawings represent the first few configurations in two infinite sequences of examples — show that the theorem as stated is best possible: for any odd $n \geq 5$ there is a configuration with $_ n$ points that determines exactly $n - 1$ different slopes, and for any other $n \geq 3$ we have a configuration with exactly $n$ slopes.

A little experimentation for small $_ n$ will probably lead you to a sequence such as the two depicted here.

![](images/356ef95bfaed8f9ef2c41e28e49e8e366a2820f1655c3c875bd4b6382303cdba.jpg)

Three pretty sporadic examples from the Jamison-Hill cataloguc

However, the configurations that we have drawn above are by far not the only ones. For example, Jamison and Hill described four infinite families of configurations, cach of them consisting of configurations with an odd number $\gamma _ { \ell }$ of points that determine only $ \hbar - 1$ slopes ("slope-critical configurations"). Furthermore, they listed 102 "sporadic" examples that do not seem to fit into an infinite family, most of them found by extensive computer searches.

Conventional wisdom might say that extremal problems tend to be very difficult to solve exactly if the extreme configurations are so diverse and irregular. Indeed, there is a lot that can be said about the structure of slopecritical configurations (see [2]), but a classification seems completely out of reach. However, the theorem above has a simple proof, which has two main ingredients: a reduction to an efficient combinatorial model due to Eli Goodman and Ricky Pollack, and a beautiful argument in this model by which Peter Ungar completed the proof in 1982.

![](images/75df9017f03645626ec2283efa86d614bf6371eea671c507efaa8f6e69d66492.jpg)

This configuration of $n = 6$ points determines $t = 6$ different slopes.

4   
! 3 5 6 ?   
0   
1 2 3 4 5 6

Here a vertical starting direction yields $\pi _ { \downarrow \uparrow } = 1 2 3 4 5 6 $ .

Proof. (1) First wc notice that it suffices to show that every "even" set of $\pi = 2 \pi$ points in the plane $( \gamma \gamma 2 )$ determines at least $n$ slopes. This is so since the case $ \textrm { \textrm { r } } = \textrm { \textbar { 3 } }$ is trivial, and for any set of ${ \mathfrak { r } } = { \mathfrak { Z } } { \mathfrak { m } } + 1 \geq 5$ points (not all on a line) we can find a subset of $\pi - 1 = 2 \pi$ points, not all on a line, which already determines $ \pi - 1$ slopes.

Thus for the following we consider a configuration of $\pi = 2 \pi \iota$ points in the plane that determines $t \geq 2$ different slopes.

(2) The combinatorial model is obtained by constructing a periodic sequence of permutations. For this we start with some direction in the plane that is not one of the configuration's slopes, and we number the points $1 , \ldots , n$ in the order in which they appear in the 1-dimensional projection in this direction. Thus the permutation $\pi _ { 0 } = 1 2 3 . . . \pi$ represents the order of the points for our starting direction.

Next let the direction perform a counterclockwise motion, and watch how the projection and its permutation change. Changes in the order of the projected points appcar exactly when the direction passes over one of the configuration's slopes.

But the changes are far from random or arbitrary: By performing a $1 8 0 ^ { \circ }$ rotation of the direction, we obtain a sequence of permutations

$$
\pi _ { 0 } \longrightarrow \pi _ { 1 } \longrightarrow \pi _ { 2 } \longrightarrow \ldots \longrightarrow \pi _ { t - 1 } \longrightarrow \pi _ { t }
$$

which has the following special properties:

The sequence starts with $\pi _ { 0 } = 1 2 3 . . . \pi$ and ends with $\pi _ { i } = \pi . . . 3 2 1$ .   
$\bullet$ The length $t$ of the scquencc is the number of slopes of the point configuration. In the course of the sequence, every pair $i < j$ is switched exactly once. This means that on the way from $\pi _ { 0 } = 1 2 3 . . . \pi$ to $\pi _ { t } = n . . . 3 2 1$ , only increasing substrings are reversed.

Every move consists in the reversal of one or more disjoint increasing substrings (corresponding to the one or more lines that have the direction which we pass at this point).

![](images/9c58f33ae3930d54790a73e98b0eaa37f45a77c4f1d1ba3e44c97be11f3ac7ee.jpg)

By continuing the circular motion around the configuration, one can view the sequence as a part of a two-way infinite, periodic sequence of permutations

$$
\dots \to \pi _ { - 1 } \to \pi _ { 0 } \to \dots \to \pi _ { t } \to \pi _ { t + 1 } \to \dots \to \pi _ { 2 t } \to \dots .
$$

where $\pi _ { i + t }$ is the reverse of $\pi _ { i }$ for all $i$ , and thus $\pi _ { i + 2 t } = \pi _ { i }$ for all $i \in \mathbb Z$ . We will show that every sequence with the above properties (and $t \geq 2$ must have length $t \geq n$

(3) The proof's key is to divide each permutation into a "left half" and a right half" of equal size $\begin{array} { r } { m = { \frac { \pi } { 2 } } } \end{array}$ , and to count the letters that cross the imaginary barrier between the left half and the right half.

Call $\pi _ { i } \implies \pi _ { i + 1 }$ a crossing move if one of the substrings it reverses does involve letters from both sides of the barrier. The crossing move has order $d$ if it moves $2 d$ letters across the barrier, that is, if the crossing string has exactly $d$ letters on one side and at least $d$ letters on the other side. Thus in our example

$$
\pi _ { 2 } = 2 1 3 5 6 4 \longrightarrow 2 \bar { 6 } 5 3 \bar { 1 } 4 = \pi _ { 3 }
$$

is a crossing move of order $d = 2$ (it moves 1, 3, 5, 6 across the barrier, which we mark by "."),

$$
6 5 2 { : } 3 4 1 \longrightarrow 6 5 \overline { { 4 { : } 3 2 } } 1
$$

Getting the sequence of permutations for our small example

![](images/b37df7a7f015189cbf9a4fde38c30ac8619413c9ecadfd7861fce2b9d4208164.jpg)  
A crossing move

is crossing of order $d = 1$ , while for example

$$
\mathrm { 6 2 5 { : } 3 1 4 } \longrightarrow \mathrm { 6 } \overleftrightarrow { 5 2 } { : } 3 \overrightarrow { 4 } \overleftrightarrow { 1 }
$$

is not a crossing move.

In the course of the sequence $\pi _ { 0 } \to \pi _ { 1 } \to \ldots \to \pi _ { t }$ , each of the letters $1 , 2 , \ldots , \ n$ has to cross the barrier at least once. This implies that, if the orders of the $c$ crossing moves are $d _ { \mathrm { i } } , d _ { 2 } , \dots , d _ { c }$ , then we have

$$
\sum _ { i = 1 } ^ { c } 2 d _ { i } = \# \{ { \mathrm { l e t t e r s ~ t h a t ~ c r o s s ~ t h e ~ b a r r i e r } } \} \geq n .
$$

This also implies that we have at least two crossing moves, since a crossing move with $2 d _ { i } = n$ occurs only if all the points are on one line, i. e. for $t = 1$ . Geometrically, a crossing move corresponds to the direction of a line of the configuration that has less than $m$ points on each side.

![](images/b3b7667915b69e64e234384bc046f83dbd3f22d287f2ca66e605c5d296d84474.jpg)

A touching move

![](images/bfc3a27b1b3f412ee991b8a716832b21d4cabca0d21970508b904549a878a2e9.jpg)

An ordinary move

(4) A touching move is a move that reverses some string that is adjacent to the central barrier, but does not cross it. For example,

$$
\pi _ { 4 } ~ = ~ 6 2 5 { : } 3 1 4 \longrightarrow 6 5 2 { : } 3 \overline { { 4 1 } } ~ = ~ \pi _ { 5 }
$$

is a touching move. Geometrically, a touching move corresponds to the slope of a line of the configuration that has exactly m points on one side, and hence at most $\ r \ / r - 2$ points on the other side.

Moves that are neither touching nor crossing will be called ordinary moves. For this

$$
\pi _ { 1 } ~ = ~ 2 1 3 5 4 6 \longrightarrow 2 1 3 5 5 \overline { { { 6 4 } } } ~ = ~ \pi _ { 2 }
$$

is an example. So every move is either crossing, or touching, or ordinary, and we can use the letters $T , C , O$ to denote the types of moves. $\vec { C } ( d )$ will denote a crossing move of order $d$ Thus for our small example we get

$$
\pi _ { 0 } \stackrel { T } { \longrightarrow } \pi _ { 1 } \stackrel { O } { \longrightarrow } \pi _ { 2 } \stackrel { C \{ 2 \} } { \longrightarrow } \pi _ { 3 } \stackrel { O } { \longrightarrow } \pi _ { 4 } \stackrel { T } { \longrightarrow } \pi _ { 5 } \stackrel { C \{ 1 \} } { \longrightarrow } \pi _ { 6 } ,
$$

or even shorter we can record this sequence as $T , O , C ( 2 ) , O , T , C ( 1 )$ .

(5) To complete the proof, we need the following two facts:

Between any two crossing moves, there is at least one touching move.

Between any crossing move of order d and the next touching move, there are at least $d - 1$ ordinary moves.

In fact, after a crossing move of order $d$ the barrier is contained in a symmetric decreasing substring of length $2 d .$ ,with $d$ letters on each side of the barrier. For the next crossing move the central barrier must be brought into an increasing substring of length at least 2. But only touching moves affect whether the barrier is in an increasing substring. This yields the first fact.

For the second fact, note that with each ordinary move (reversing some increasing substrings) the decreasing $2 d .$ -string can get shortened by only one letter on each side. And, as long as the decreasing string has at least 4 letters, a touching move is impossible. This yields the second fact.

If we construct the sequence of permutations starting with the same initial projection but using a clockwise rotation, then we obtain the reversed sequence of permutations. Thus the sequence that we do have recorded must also satisfy the opposite of our second fact, namely

Between a touching move and the next crossing move, of order $d _ { i }$ .   
there are at least $d - 1$ ordinary moves.

() The $T$ -O $C$ -pattern of the infinite sequence of permutations, as derived in (2), is obtained by repeating over and over again the $T – O { \cdot } C$ -pattern of length $t$ of the sequence $\pi _ { 0 } \longrightarrow \ldots \longrightarrow \pi _ { t }$ Thus with the facts of (5) we see that in the infinite sequence of moves, each crossing move of order $d$ is embedded into a $T { \cdot } O { - } C$ pattern of the type

$$
T , \underbrace { O , O , \ldots , O } _ { \geq d - 1 } , C ( d ) , \underbrace { O , O , \ldots , O } _ { \geq d - 1 } ,
$$

of length $1 + ( d - 1 ) + 1 + ( d - 1 ) = 2 d .$

In the infinite sequence, we may consider a finite segment of length $t$ that starts with a touching move. This segment consists of substrings of the type $( \ast )$ , plus possibly extra inserted $T$ 's. This implies that its length $t$ satisfies

$$
t \geq \sum _ { i = 1 } ^ { c } 2 d _ { i } \geq n ,
$$

which completes the proof.

# References

[1] J. E. GoODMAN & R. POLLACK: A combinatorial perspective on some problems in geometry, Congressus Numerantium 32 (1981), 383-394.   
[2] R. E. JAmIsON & D. HILL: A catalogue of slope-critical configurations, Congressus Numerantium 40 (1983), 101-125.   
[3] P. R. ScoTT: On the sets of directions determined by n points, Amer. Math. Monthly 77 (1970), 502-505.   
[4] P. UNGAR: $2 N$ noncollinear points determine at least $2 N$ directions, J. Combinatorial Theory, Ser. A 33 (1982), 343-347.

# Three applications of Euler's formula

# Chapter 11

A graph is planar if it can be drawn in the plane $\mathbb { R } ^ { 2 }$ without crossing edges (or, equivalently, on the 2-dimensional sphere $S ^ { 2 }$ ). Wc talk of a plane graph if such a drawing is already given and fixed. Any such drawing decomposes the plane or spherc into a finite number of connected regions, including the outer (unbounded) region, which are referred to as faces. Euler's formula cxhibits a beautiful relation bctween the number of vertices, edges and faces that is valid for any plane graph. Euler mentioned this result for the first time in a letter to his friend Goldbach in 1750, but he did not have a complete proof at the time. Among the many proofs of Euler's formula, we present a pretty and "self-dual" one that gets by without induction. It can be traced back to von Staudt's book "Geometrie der Lage" from 1847.

Euler's formula. If $G$ is a connected plane graph with $\boldsymbol { n }$ vertices, e edges and $f$ faces, then

$$
n - e + f = 2 .
$$

Proof. Let $T \subseteq E$ be the edge set of a spanning tree for $G$ , that is, of a minimal subgraph that connects all the vertices of $G$ This graph does not contain a cycle because of the minimality assumption.

We now need the dual graph $G ^ { * }$ of $G$ : to construct it, put a vertex into the interior of each face of $G$ , and connect two such vertices of $G ^ { \star }$ by edges that correspond to common boundary edges between the corresponding faces. If there are several common boundary edges, then we draw several connecting edges in the dual graph. (Thus $G ^ { * }$ may have multiple edges even if the original graph $G$ is simple.)

Consider the collection $T ^ { * } \subseteq E ^ { * }$ of edges in the dual graph that corresponds to edges in $E \backslash T$ The edges in $T ^ { * }$ connect all the faces, since $T$ does not have a cycle; but also $T ^ { * }$ does not contain a cycle, since otherwise it would separate some vertices of $G$ inside the cycle from vertices outside (and this cannot be, since $T$ is a spanning subgraph, and the edges of $T$ and of $T ^ { * }$ do not intersect). Thus $T ^ { * }$ is a spanning tree for $G ^ { * }$ .

For every tree the number of vertices is one larger than the number of edges. To see this, choose one vertex as the root, and direct all edges "away from the root": this yields a bijection between the non-root vertices and the edges, by matching each edge with the vertex it points at. Applied to the tree $T$ this yields $n = e _ { T } + 1$ , while for the tree $T ^ { * }$ it yields $f = e _ { T ^ { * } } + 1 .$ Adding both equations we get $n { + } f = ( e _ { T } { + } 1 ) { + } ( e _ { T ^ { * } } { + } 1 ) =$ $e + 2$

![](images/b03093495c373aeb1f1dc93174d1d02ba992d72f9727a4efefd44e02231c2ebf.jpg)  
Leonhard Euler

![](images/b5763109f8ce0322bcbda5c1f17ee9022efdcb9fd21e4062810663b25d46cd30.jpg)

A plane graph $G \colon n = 6 , e = 1 0 , f = 6$

![](images/911d83274b4af9b004fb5d5135fe1e52e46e6908891d9647d071a2f6279bc00b.jpg)

Dual spanning trees in $G$ and in $G ^ { * }$

![](images/9124bc5cb6896f4c1889bf01e73f9080eecffc22731be203a0c6a526e4261899.jpg)

The five platonic solids

![](images/1e059c879983364334c24099cbce6e76e191c92d2f88d5bc6261d6f9e9b6a409.jpg)

Here the degree is written next to each vertex. Counting the vertices of given degree yields ${ n } _ { 2 } = 3$ , ${ { n } _ { 3 } } = 0$ , $n _ { 4 } = 1$ , $\eta _ { \bar { \tau } ; } = 2$ .

Euler's formula thus produces a strong numerical conclusion from a geometric-topological situation: the numbers of vertices, edges, and faces of a finite graph $G$ satisfy $n - e + f = 2$ whenever the graph is or can be drawn in the plane or on a sphere.

Many well-known and classical consequences can be derived from Euler's formula. Among them are the classification of the regular convex polyhedra (the platonic solids), the fact that $K _ { 5 }$ and $K _ { 3 , 3 }$ are not planar (see below), and the five-color theorem that every planar map can be colored with at most five colors such that no two adjacent countries have the same color. But for this we have a much better proof, which does not even need Euler's formula — see Chapter 30.

This chapter collects three other beautiful proofs that have Euler's formula at their core. The first two — a proof of the Sylvester-Gallai theorem, and a theorem on two-colored point configurations — use Euler's formula in clever combination with other arithmetic relationships between basic graph parameters. Let us first look at these parameters.

The degree of a vertex is the number of edges that end in the vertex, where loops count double. Let $n _ { i }$ denote the number of vertices of degree $i$ in $G$ . Counting the vertices according to their degrees, we obtain

$$
n = n _ { 0 } + n _ { 1 } + n _ { 2 } + n _ { 3 } + . . .
$$

On the other hand, every edge has two ends, so it contributes 2 to the sum of all degrees, and we obtain

$$
2 e \ = \ n _ { 1 } + 2 n _ { 2 } + 3 n _ { 3 } + 4 n _ { 1 } + \ldots
$$

You may interpret this identity as counting in two ways the ends of the edges, that is, the edge-vertex incidences. The average degree $\overline { { d } }$ of the vertices is therefore

$$
\overline { { { d } } } \ = \ \frac { 2 \epsilon } { n } .
$$

9 2   
4 K

The number of sides is written into each region. Counting the faces with a given number of sides yields $f _ { \mathrm { { I } } } = 1$ . $f _ { 2 } = 3$ $f _ { 4 } = 1 , f _ { 9 } = 1$ , and $f _ { i } = 0$ otherwise.

Next we count the faces of a plane graph according to their number of sides: a $k$ -face is a face that is bounded by $k$ edges (where an edge that on both sides borders the same region has to be counted twice!). Let $f _ { k }$ be the number of $k$ -faces. Counting all faces we find

$$
f = f _ { 1 } + f _ { 2 } + f _ { 3 } + f _ { 4 } + . . .
$$

Counting the edges according to the faces of which they are sides, we get

$$
2 e = f _ { 1 } + 2 f _ { 2 } + 3 f _ { 3 } + 4 f _ { 4 } + \ldots
$$

As before, we can interpret this as double-counting of edge-face incidences. Note that the average number of sides of faces is given by

$$
{ \overline { { f } } } \ = \ { \frac { 2 \mathcal { e } } { f } } .
$$

Let us deduce from this — together with Euler's formula — quickly that the complete graph $K _ { 5 }$ and the complete bipartite graph $K _ { 3 , 3 }$ are not planar. For a hypothetical plane drawing of $K _ { 5 }$ we calculate $\mathfrak { n } = 5$ . $\mathcal { C } = \binom { 5 } { 2 } \overline { { = } } 1 0$ . thus ${ \mathfrak { f } } = { \mathfrak { e } } + { \mathfrak { 2 } } - { \mathfrak { n } } = { \mathfrak { 7 } }$ and $\begin{array} { r } { \overline { { f } } = \frac { 2 \epsilon } { f } = \frac { 2 0 } { 7 } < 3 } \end{array}$ But if the average number of sides is smaller than 3, then the embedding would have a face with at most two sides, which cannot be.

Similarly for $K _ { 3 , 3 }$ we get $\hbar \tau = 6 , \epsilon = 9 .$ , and $f = e + 2 - \pi = 5$ , and thus $\overline { f } = \frac { 2 \epsilon } { f } = \frac { 1 8 } { 5 } < 4$ which cannot be since $\bar { \kappa } _ { 3 , 3 }$ is simple and bipartite, so all its cycles have length at least 4.

It is no coincidence, of course, that the equations (3) and (4) for the $f _ { i }$ s look so similar to the equations (1) and (2) for the $\boldsymbol { \mathscr { n } _ { i } }$ s. They are transformed into each other by the dual graph construction $G \to G ^ { * }$ explained above.

From the double counting identities, we get the following important "local" consequences of Euler's formula.

Proposition. Let G be any simple plane graph with $n > 2$ vertices. Then

(A) $G$ has a vertex of degree at most 5.   
(B) G has at most 3n - 6 edges.   
(C) If the edges of G are two-colored, then there is a vertex of $G$ with at most two color-changes in the cyclic order of the edges around the vertex.

Proof. For each of the three statements, we may assume that $G$ is connected.

(A) Every face has at least 3 sides (since $G$ is simple), so (3) and (4) yield

$$
\begin{array} { r l r } { f } & { = } & { f _ { 3 } + \ f _ { 4 } \ \dag \ f _ { 5 } \ \dag \ \dots } \\ { 2 e } & { = } & { 3 f _ { 3 } + 4 f _ { 4 } + 5 f _ { 5 } + \dots . } \end{array}
$$

and thus $2 c \mathrm { ~ - ~ } 3 f \ge 0$ .

Now if cach vertex has degree at least 6, then (1) and (2) imply

$$
\begin{array} { r l r } { n } & { = } & { n _ { 6 } + n _ { 7 } + n _ { 8 } + \ldots } \\ { 2 e } & { = } & { 6 n _ { 6 } + 7 n _ { 7 } + 8 n _ { 8 } + \ldots } \end{array}
$$

and thus $2 \epsilon - \delta \pi \geq 0$ .

Taking both inequalities together, we get

$$
6 ( e - n - f ) = ( 2 e - 6 n ) + 2 ( 2 e - 3 f ) \geq 0
$$

and thus $e \geq n + f$ , contradicting Euler's formula.

() As in the first step of part (A), we obtain $2 \epsilon \mathrm { ~ - ~ } 3 f \ge 0$ , and thus

$$
3 \hbar - 6 = 3 \epsilon - 3 f \geq e
$$

from Euler's formula.

$\tilde { K _ { 5 } }$ drawn with one crossing

![](images/4890e2253ab626b2b088f92a959ad19fcfc026f2eb55db5e28dc01effaaa3a5d.jpg)

$K _ { 3 , 3 }$ drawn with one crossing

V \*

Arrows point to the corners with color changes.

A

![](images/8c519095de84dbcf06d780677e54665bd3d906808512cb0adce41a62c50644b1.jpg)

(C) Let $c$ be the number of corners where color changes occur. Suppose the statement is false, then we have $c \geq 4 n$ corners with color changes, since at every vertex there is an even number of changes. Now every face with $2 k$ or $2 k \pi + 1$ sides has at most $2 k$ such corners, so we conclude that

$$
{ \begin{array} { l l l } { 4 n \leq c } & { \leq } & { 2 f _ { 3 } + 4 f _ { 4 } + 4 f _ { 5 } + 6 f _ { 6 } + 6 f _ { 7 } + 8 f _ { 8 } + . . . } \\ & { \leq } & { 2 f _ { 3 } + 4 f _ { 4 } + 6 f _ { 5 } + 8 f _ { 6 } + 1 0 f _ { 7 } + . . . } \\ & { = } & { 2 ( 3 f _ { 3 } + 4 f _ { 4 } + 5 f _ { 5 } + 6 f _ { 6 } + 7 f _ { 7 } + . . . ) } \\ & & { - 4 ( f _ { 3 } + f _ { 4 } + f _ { 5 } + f _ { 6 } + f _ { 7 } + . . . ) } \\ & { = } & { 4 e - 4 f } \end{array} }
$$

using again (3) and (4). So we have $\varepsilon \ge \pi + f$ , again contradicting Euler's formula.

# 1. The Sylvester-Gallai theorem, revisited

It was first noted by Norman Steenrod, it seems, that part (A) of the proposition yields a strikingly simple proof of the Sylvester-Gallai theorem (see Chapter 9).

The Sylvester-Gallai theorem. Given any set of $n \geq 3$ points in the plane, not all on one line, there is always a line that contains exactly two of the points.

Proof. (Sylvester-Gallai via Euler)

If we embed the plane $\mathbb { R } ^ { 2 }$ in $\mathbb { R } ^ { 3 }$ near the unit sphere $S ^ { 2 }$ as indicated in our figure, then every point in $\mathbb { R } ^ { 2 }$ corresponds to a pair of antipodal points on $S ^ { 2 }$ , and the lines in $\mathbb { R } ^ { 2 }$ correspond to great circles on $S ^ { 2 }$ .Thus the Sylvester-Gallai theorem amounts to the following:

Given any set of $n \geq 3$ pairs of antipodal points on the sphere, not all on one great circle, there is always a great circle that contains exactly two of the antipodal pairs.

Now we dualize, replacing each pair of antipodal points by the corresponding great circle on the sphere. That is, instead of points $\pm v \in S ^ { 2 }$ we consider the orthogonal circles given by $C _ { v } : = \{ { \pmb x } \in S ^ { 2 } : \langle { \pmb x } , { \pmb v } \rangle = 0 \}$ . (This $C _ { v }$ is the equator if we consider $\pmb { v }$ as the north pole of the sphere.) Then the Sylvester-Gallai problem asks us to prove:

Given any collection of $n \geq 3$ great circles on $S ^ { 2 }$ , not all of them passing through one point, there is always a point that is on exactly two of the great circles.

But the arrangement of great circles yields a simple plane graph on $S ^ { 2 }$ , whose vertices are the intersection points of two of the great circles, which divide the great circles into edges. All the vertex degrees are even, and they are at least 4 — by construction. Thus part (A) of the proposition yields the existence of a vertex of degree 4. That's it! □

# 2. Monochromatic lines

The following proof of a "colorful" relative of the Sylvester-Gallai theorem is due to Don Chakerian.

Theorem. Given any finite configuration of "black" and "white" points in the plane, not all on one line, there is always a "monochromatic" line: a line that contains at least two points of one color and none of the other.

Proof. As for the Sylvester-Gallai problem, we transfer the problem to the unit sphere and dualize it there. So we must prove:

Given uny finite collection of "black" and "white" great circles on the unit sphere, not all passing through one point, there is always an intersection point that lies either only on white great circles, or only on black great circles.

Now the (positive) answer is clear from part (C) of the proposition, since in every vertex where great circles of different colors intersect, we always have at least 4 corners with sign changes. □

# 3. Pick's theorem

Pick's theorem from 1899 is a beautiful and surprising result in itself, but it is also a "classical" consequence of Euler's formula. For the following, call a convex polygon $P \subseteq \mathbb { R } ^ { 2 }$ elementary if its vertices are integral (that is, they lie in the lattice $\mathbb { Z } ^ { 2 }$ ), but if it does not contain any further lattice points.

Lemma. Every elementary triangle $\Delta = \mathrm { c o n v } \{ p _ { ( \rangle } , p _ { 1 } , p _ { 2 } \} \subseteq \mathbb { R } ^ { 2 }$ has area $A ( \Delta ) = \frac { 1 } { 2 }$

Proof. Both the parallelogram $P$ with corners $p _ { 0 } , p _ { 1 } , p _ { 2 } , p _ { 1 } + p _ { 2 } - p _ { 0 }$ and the lattice $\sum ^ { 2 }$ are symmetric with respect to the map

$$
\sigma : { \pmb x } \longmapsto { \pmb p } _ { 1 } + { \pmb p } _ { 2 } - { \pmb x } ,
$$

which is the reflection with respect to the center of the segment from $\pmb { p } _ { 1 }$ to $p _ { 2 }$ .Thus the parallelogram $P = \Delta \cup \sigma ( \Delta )$ is elementary as well, and its integral translates tile the planc. Hence $\{ p _ { 1 } - p _ { 0 } , p _ { 2 } - p _ { 0 } \}$ is a basis of the lattice $\mathbb { Z } ^ { 2 }$ , it has determinant $\pm 1$ , $P$ is a parallelogram of area 1, and $\Delta$ has area $\frac 1 2$ . (For an explanation of these terms see the box on the next page.) □

Theorem. The area of any (not necessarily convex) polygon $Q \subseteq \mathbb { R } ^ { 2 } w i t h$ integral vertices is given by

$$
A ( Q ) = n _ { i n i } + \frac { 1 } { 2 } \pi _ { b d } - 1 ,
$$

where $u _ { i ; n ; t }$ and $n _ { b d }$ are the numbers of integral points in the interior respectively on the boundary of $C$ .

![](images/c04dac197a621988cd8b21cd28083056245475d6edf9dd59f542f2b1fce827da.jpg)

![](images/b49446ba8e22120465fe2ac4a388bce660c9aaf3d0c7a9e1a4fe931dc6e0ad32.jpg)

# Lattice bases

A basis of $\textstyle \mathbb { Z } ^ { 2 }$ is a pair o linearly independent vectors $e _ { 1 } , e _ { 2 }$ such that

$$
\mathbb { Z } ^ { 2 } = \{ \lambda _ { 1 } e _ { 1 } + \lambda _ { 2 } e _ { 2 } : \lambda _ { 1 } , \lambda _ { 2 } \in \mathbb { Z } \} .
$$

Let $\begin{array} { l l l } { e _ { 1 } } & { = } & { { \binom { \bar { \alpha } } { \bar { \Delta } } } } \end{array}$ and $e _ { 2 } ~ = ~ { \binom { c } { d } }$ , then the area of the parallelogram spanned by $e _ { 1 }$ and $e _ { 2 }$ is given by $A ( e _ { 1 } , e _ { 2 } ) = | \operatorname* { d e t } ( e _ { 1 } , e _ { 2 } ) | =$ $| \dot { \operatorname* { d e t } } \left( { \mathfrak { a } } \ { \mathfrak { c } } \right) |$ .If ${ { f } _ { 1 } } \ = \ { { \binom { r } { s } } }$ and $f _ { 2 } = ( \phi )$ is another basis, then there exis an inverible $\mathbb { Z }$ mattrix $C$ with $( \ * { \begin{array} { l } { r \ t } \\ { s \ u } \end{array} } ) \ = \ ( \ * { \begin{array} { l } { { \mathrm { ~ a ~ c ~ } } } \\ { { \mathfrak { d } } \ d } \end{array} } ) Q$ Siince $\scriptstyle Q Q ^ { - 1 } \ = \ { \binom { 1 \ 0 } { 0 \ 1 } }$ $| \operatorname* { d e t } Q | = 1$ , and hence $| \operatorname* { d e t } ( \pmb { f } _ { 1 } , \pmb { f } _ { 2 } ) | = | \operatorname* { d e t } ( e _ { 1 } , e _ { 2 } ) |$ Therefore all basis parallelograms have the same area 1, since ${ \bf \dot { A } ( \binom { j } { 0 } , \binom { 0 } { 1 } ) = 1 }$ .

![](images/39995a9fc296c1ab7a557fde70b6d36c3f91327c9dba9697e2a47aa097c9bcce.jpg)

Proof. Every such polygon can be triangulated using all the $n _ { i n t }$ lattice points in the interior, and all the $n _ { b d }$ lattice points on the boundary of $Q$ . (This is not quite obvious, in particular if $2$ is not requjred to be convex, but the argument given in Chapter 31 on the art gallery problem proves this.) Now we interpret the triangulation as a plane graph, which subdivides the plane into one unbounded face plus $f \sim 1$ triangles of area $\frac { 1 } { 2 }$ , so

$$
A ( Q ) \ = \ { \frac { 1 } { 2 } } ( f - 1 ) .
$$

Every triangle has three sides, where each of the $\mathbb { C } _ { \cdot } { \mathrm { i } } _ { \mathfrak { n } } { \mathfrak { t } }$ interior edges bounds two triangles, while the $\mathcal { C } \mathcal { b } d .$ boundary edges appear in one single triangle each. So $3 ( f - 1 ) = 2 \epsilon _ { i : i \pm } + \epsilon _ { b d }$ and thus $f = 2 ( \epsilon - f ) - \epsilon _ { b d } + 3$ Also, there is the same number of boundary edges and vertices, $e _ { t ; t } = \pi , \ldots$ These two facts together with Euler's formula yield

$$
\begin{array} { r c l } { { f } } & { { = } } & { { 2 ( \epsilon - f ) - e _ { b d } + 3 } } \\ { { } } & { { = } } & { { 2 ( n - 2 ) - n _ { b d } + 3 = 2 n _ { i n t } + n _ { b d } - 1 , } } \end{array}
$$

and thus

$$
A ( Q ) = \textstyle { \frac { 1 } { 2 } } ( f - 1 ) = n _ { i n t } + \frac { 1 } { 2 } \pi _ { b d } - 1 .
$$

# References

[1] G. D. CHAKERIAN: Sylvester's problem on collinear points and a relative, Amer. Math. Monthly 77 (1970), 164-167.

[2] G. PiCK: Geometrisches zur Zahlenlehre, Sitzungsberichte Lotos (Prag) Natur-med. Verein für Böhmen 19 (1899), 311-319.

[3] K. G. C. voN STAUDT: Geometrie der Lage, Verlag der Fr. Korn'scher Buchhandlung, Nürnberg 1847.

[4] N. E. STEENROD: Solution 4065/Editorial Note, Amer. Math. Monthly 51 (1944), 170-171.

A famous result that depends on Euler's formula (specifically, on part (C) of the proposition in the previous chapter) is Cauchy's rigidity theorem for 3-dimensional polyhedra.

For the notions of congruence and of combinatorial equivalence that are used in the following we refer to the appendix on polytopes and polyhedra in the chapter on Hilbert's third problem, see page 50.

Theorem. If two 3-dimensional convex polyhedra $P$ and $P ^ { \prime }$ are combinatorially equivalent with corresponding facets being congruent, then also the angles between corresponding pairs of adjacent facets are equal (and thus $P$ is congruent to $P ^ { \prime }$ ).

The illustration in the margin shows two 3-dimensional polyhedra that are combinatorially equivalent, such that the corresponding faces are congruent. But they are not congruent, and only one of them is convex. Thus the assumption of convexity is essential for Cauchy's theorem!

Proof. The following is essentially Cauchy's original proof. Assume that two convex polyhedra $P$ and $P ^ { \prime }$ with congruent faces are given. We color the edges of $P$ as follows: an edge is black (or "positive") if the corresponding interior angle between the two adjacent facets is larger in $P ^ { \prime }$ than in $P$ ; it is white (or "negative") if the corresponding angle is smaller in $P ^ { \prime }$ than in $P$ .

The black and the white edges of $P$ together form a 2-colored plane graph on the surface of $P$ , which by radial projection, assuming that the origin is in the interior of $P$ , we may transfer to the surface of the unit sphere. If $P$ and $P ^ { \prime }$ have unequal corresponding facet-angles, then the graph is nonempty. With part (C) of the proposition in the previous chapter we find that there is a vertex $p$ that is adjacent to at least one black or white edge, such that there are at most two changes between black and white edges (in cyclic order).

Now we intersect $P$ with a small sphere $S _ { \varepsilon }$ (of radius $\varepsilon$ ) centered at the vertex $p$ , and we intersect $P ^ { \prime }$ with a sphere $S _ { \varepsilon } ^ { \prime }$ of the same radius $\varepsilon$ centered at the corresponding vertex $p ^ { \prime }$ . In $S _ { \varepsilon }$ and $S _ { \varepsilon } ^ { \prime }$ we find convex spherical polygons $Q$ and $Q ^ { \prime }$ such that corresponding arcs have the same lengths, because of the congruence of the facets of $P$ and $P ^ { \prime }$ , and since we have chosen the same radius $\varepsilon$ .

![](images/dff31d3bc64c3ace143aab8bf21715614642915ce830408234b4f7500a84a949.jpg)  
Augustin Cauchy

![](images/eb626e70b60e2458f4384aae6845495b2ab66c9f6321149beebebf7cadaae222.jpg)

![](images/9c53232f70277d677146f602cf6e5e47f6722afc6a37252b8ddb2df448cf6d6f.jpg)

![](images/1e937667d7cc2e3929938fa1810c74073fd63912c917f8d6d0782b4e1797604e.jpg)

Now we mark by $+$ the angles of $i$ for which the corresponding angle in $Q ^ { i }$ is larger, and by - the angles whose corresponding angle of $C ^ { \prime }$ is smaller. That is, when moving from $Q$ to $2 ^ { r }$ the $+$ angles are "opened," the — angles are "closed," while all side lengths and the unmarked angles stay constant.

From our choice of $p$ we know that some $+$ or -- sign occurs, and that in cyclic order there are at most two $+ 1 -$ changes. If only one type of signs occurs, then the lemma below directly gives a contradiction, saying that one edge must change its length. If both types of signs occur, then (since there are only two sign changes) there is a "separation line" that connects the midpoints of two edges and separates all the $+$ signs from all the — signs. Again we get a contradiction from the lemma below, since the separation line cannot be both longer and shorter in $Q ^ { i }$ than in $Q$ . □

# Cauchy's arm lemma.

If $Q$ and $Q ^ { \prime }$ are convex (planar or spherical) $\gamma _ { \ell }$ -gons, labeled as in the figure,

![](images/1da0f522e17c8037d1a3983d7e1c5abe5bafed7252b434df2c9d71f4e11e049c.jpg)

such that $\overline { { q _ { i } q _ { i - 1 } } } = \overline { { q _ { i } ^ { \prime } q _ { i + 1 } ^ { \prime } } }$ holds for the lengths of corresponding edges for $1 \leq i \leq \pi - 1$ ,and $\alpha _ { i } \leq \alpha _ { i } ^ { \prime }$ holds for the sizes of corresponding angles for $2 < i \leq \pi - 1$ , then the "missing" edge length satisfies

$$
\overline { { { q _ { 1 } q _ { n } } } } \leq \overline { { { q _ { 1 } ^ { \prime } q _ { n } ^ { \prime } } } } ,
$$

with equality if and only if $C { \boldsymbol { \nu } } _ { i } \ { \stackrel { . . . } { = } } \ C _ { i } ^ { \prime }$ holds for all $i$ .

It is interesting that Cauchy's original proof of the lemma was false: a continuous motion that opens angles and keeps side-lengths fixed may destroy convexity — see the figure! On the other hand, both the lemma and its proof given here, from a letter by I. J. Schoenberg to S. K. Zaremba, are valid both for planar and for spherical polygons.

Proof. We use induction on $\gamma _ { \ell }$ . The case $ \hbar =  3$ is easy: If in a triangle we increase the angle $\gamma$ between two sides of fixed lengths $\alpha$ and $l$ , then the length $c$ of the opposite side also increases. Analytically, this follows from the cosine theorem

$$
c ^ { 2 } \ = \ a ^ { 2 } + b ^ { 2 } - 2 a b \cos \gamma
$$

in the planar case, and from the analogous result

$$
\cos c = \cos a \cos b + \sin a \sin b \cos \gamma
$$

in spherical trigonometry. Here the lengths $a , b , c$ are measured on the surface of a sphere of radius 1, and thus have values in the interval $[ 0 , \pi ]$ .

Now let $n \geq 4$ If for any $i \in \{ 2 , \ldots , n - 1 \}$ we have $\alpha _ { i } = \alpha _ { i } ^ { \prime }$ then the corresponding vertex can be cut off by introducing the diagonal from $q _ { i - 1 }$ to ${ \dot { q } } _ { i + 1 }$ resp. from $q _ { i - 1 } ^ { \prime }$ to $q _ { i - 1 } ^ { \prime }$ , with $\overline { { { \mathfrak { q } } _ { i - 1 } { \mathfrak { q } } _ { i + 1 } } } = \overline { { { \mathfrak { q } } _ { i - 1 } ^ { \prime } { \mathfrak { q } } _ { i + 1 } ^ { \prime } } }$ , so we are done by induction. Thus we may assume $( \boldsymbol { \mathbf { \mathit { x } } } _ { i } < \boldsymbol { \mathbf { \mathit { \alpha } } } ( \boldsymbol { \mathbf { \mathit { x } } } _ { i } ^ { \prime }$ for $2 \leq i \leq n - 1$ .

Now we produce a new polygon $Q ^ { \ast }$ from $Q$ by replacing $\alpha _ { \pmb { r } _ { L } - 1 }$ by the largest possible angle $\alpha _ { r _ { 2 } - 1 } ^ { \ l * } \ \leq \ \alpha _ { n - 1 } ^ { \prime }$ that keeps $C ^ { \pi }$ convex. For this we replace $q _ { n }$ by ${ q } _ { n } ^ { * }$ , keeping all the other $q _ { i }$ , edge lengths, and angles from $Q$ .

If indeed we can choose $\alpha _ { \eta _ { 4 } - 1 } ^ { \ast } ~ \stackrel { - } { \sim } ~ \alpha _ { \eta _ { 4 } - 1 } ^ { \prime }$ keeping $Q ^ { \ast }$ convex, then we get $\overline { { q _ { 1 } q _ { n } } } < \overline { { q _ { 1 } q _ { n } ^ { * } } } \leq \overline { { q _ { 1 } ^ { \prime } q _ { n } ^ { \prime } } }$ , using the case $n = 3$ for the first step and induction as above for the second.

Otherwise after a nontrivial move that yields

$$
\overline { { { q _ { 1 } q _ { r 2 } ^ { * } } } } > \overline { { { q _ { 1 } q _ { r 2 } } } }
$$

we "get stuck" in a situation where $\ell _ { 2 } , q _ { 1 }$ and $\tilde { \mathcal { I } } _ { \mathcal { T } } ^ { \dagger }$ are collinear, with

$$
\overline { { { q _ { 2 } q _ { 1 } } } } + \overline { { { q _ { 1 } q _ { n } ^ { * } } } } = \overline { { { q _ { 2 } q _ { n } ^ { * } } } } .
$$

Now we compare this $Q ^ { \ast }$ with $Q ^ { \prime }$ and find

$$
\overline { { q _ { 2 } q _ { n } ^ { * } } } \leq \overline { { q _ { 2 } ^ { \prime } q _ { n } ^ { \prime } } }
$$

by induction on $\gamma _ { l }$ (ignoring the vertex $q _ { 1 }$ resp. $( \boldsymbol { \jmath } _ { 1 } ^ { \prime }$ ). Thus we obtain

$$
\begin{array} { r c c c c c l } { \overline { { q _ { 1 } ^ { \prime } q _ { n } ^ { \prime } } } } & { \stackrel { ( * ) } { \geq } } & { \overline { { q _ { 2 } ^ { \prime } q _ { n } ^ { \prime } } } - \overline { { q _ { 1 } ^ { \prime } q _ { 2 } ^ { \prime } } } } & { \stackrel { ( 3 ) } { \geq } } & { \overline { { q _ { 2 } q _ { n } ^ { * } } } - \overline { { q _ { 1 } q _ { 2 } } } } & { \stackrel { ( 2 ) } { = } } & { \overline { { q _ { 1 } q _ { n } ^ { * } } } } & { \stackrel { ( 1 ) } { > } } & { \overline { { q _ { 1 } q _ { n } } } , } \end{array}
$$

where $( * )$ is just the triangle inequality, and all other rclations have already been derived. □

We have seen an example which shows that Cauchy's theorem is not true for non-convex polyhedra. The special feature of this example is, of course. that a non-continuous "flip" takes one polyhedron to the other, keeping the facets congruent while the dihedral angles "jump." One can ask for more:

Could there be, for some non-convex polyhedron, a continuous deformation that would keep the facets flat and congruent?

It was conjectured that no triangulated surface, convex or not, admits such a motion. So, it was quite a surprise when in 1977 — more than 160 years after Cauchy's work — Robert Connelly presented counterexamples: closed triangulated spheres embedded in $\mathbb { R } ^ { 3 }$ (without self-intersections) that are flexible, with a continuous motion that keeps all the edge lengths constant, and thus keeps the triangular faces congruent.

![](images/e7af8458a51ea222bc13fc7b99ddb7af6601bad0d185d5d1b3ce17a3e7bd8137.jpg)

A beautiful example of a flexible surface constructed by Klaus Steffen: The dashed tincs represent the non-convex edges in this "cut-out" paper model. Fold the normal lines as "mountains" and the dashed lincs as "vallcys." The edges in the model have lengths 5, 10, 11, 12 and 17 units.

![](images/420afd8e567d286c2c66ea9a3859836272c0e3eddd41c8313466dcbb7434206e.jpg)

The rigidity theory of surfaces has even more surprises in store: only very recently Connelly, Sabitov and Walz managed to prove that when any such flexing surface moves, the volume it encloscs must be constant. Their proof is beautiful also in its use of algebraic machinery (outside the scope of this book).

# References

[1] A. CAucHy: Sur les polygones et les polyèdres, seconde mémoire, J. École Polytechnique XVIc Cahier, Tome IX (1813). 87-98; (Euvrcs Complètes, IIc Série, Vol. 1, Paris 1905, 26-38.   
[2] R. CoNNELLY: A counterexample to the rigidity conjecture for polyhedra, Inst. Haut. Etud. Sci., Publ. Math. 47 (1978), 333-338.   
[3] R. CoNNELLY: The rigidity of polyhedral surfaces, Mathemalics Magazinc 52 (1979), 275-283.   
[4] R. CONNELLY, I. SABITOV & A. WALZ: The bellows conjecture, Bciträge zur Algebra und Geometrie/Contributions to Algebra and Geomctry 38 (1997), 1-10.   
[5] J. SCHOENBERG & S.K. ZAREMBA: On Cauchy's lemma concerning convex polygons, Canadian J. Math. 19 (1967), 1062-1071.

How many $d$ -dimensional simplices can be positioned in $\mathbb { R } ^ { d }$ so that they touch pairwise, that is, so that all their pairwise intersections are $( d - 1 )$ -dimensional?

This is an old and very natural question. We shall call $f ( d )$ the answer to this problem, and record $f ( 1 ) = 2$ , which is trivial. For $\alpha = 2$ the configuration of four triangles in the margin shows $f ( 2 ) \geq 4$ There is no similar configuration with five triangles, because from this the dual graph construction, which for our example with four triangles yiclds a planar drawing of $K _ { 4 }$ , would give a planar embedding of $K _ { 5 } ^ { ' }$ , which is impossible (see page 67). Thus we have

$$
f ( 2 ) = 4 ,
$$

In three dimensions, $f ( 3 ) \geq 8$ is quite easy to see. For that we use the configuration of eight triangles depicted on the right. The four shaded triangles are joined to some point $x$ below the "plane of drawing," which yields four tetrahcdra that touch the plane from below. Similarly, the four white triangles are joined to some point $y$ above the plane of drawing. So we obtain a configuration of cight touching tetrahedra in $\mathbb { R } ^ { 3 }$ , that is, $f ( 3 ) \geq 8$ .

In 1965, Baston wrote a book proving $f ( 3 ) \leq 9$ , and in 1991 it took Zaks another book to establish

$$
f ( 3 ) = 8 .
$$

With $f ( 1 ) = 2 , f ( 2 ) = 4$ and $f ( 3 ) = 8$ , it doesn't take much inspiration to arrive at the following conjecture, first posed by Bagemihl in 1956.

Conjecture. The maximal number of pairwise touching $d$ -simplices in $^ { a }$ configuration in $\mathbb { R } ^ { d }$ is

$$
f \{ d \} = 2 ^ { d } .
$$

The lower bound. $f ( i l ) \geq 2 ^ { d }$ , is easy to verify "if we do it right."This amounts to a heavy use of affine coordinate tranformations, and to an induction on the dimension that establishes the following stronger result, due to Joseph Zaks [4].

Theorem 1. For every $d \ge 2 .$ , there is a family of $2 ^ { d . }$ pairwise touching $d$ simplices in $\mathbb { R } ^ { d }$ together with $\alpha$ transversal line that hits the interior of every single one of them.

![](images/d45087ad91b59c8640f5148d44e85e894911071f8daa3d92d6dc6ae5a95cde01.jpg)

S(2) ≥ 4

![](images/de125ad6aa9cf5e48a9a334bad67268e1306bac81c1e880f34015b8730d456ee.jpg)

$$
f ( 3 ) \geq 8
$$

![](images/01572c6484651c80710baee4bbc98719d8cc65f283661149293f1593907b8292.jpg)

"Touching simplices"

![](images/32cab9691bd5da96b36c76aa78e75b652cd7e1c9210c72038cb9a1c96f1f60cb.jpg)

![](images/edcabcc725ad56d4865f61cdd70c1de0263979027655c5f112b3389c94a41e55.jpg)

Proof. For $d = 2$ the family of four triangles that we had considered does have such a transversal line. Now consider any $d$ -dimensional configuration of touching simplices that has a transversal line $\ell$ Any nearby parallel line $\ell ^ { \prime }$ is a transversal line as well. If we choose $\ell ^ { \prime }$ and $\ell$ parallel and close enough, then each of the simplices contains an orthogonal (shortest) connecting interval between the two lines. Only a bounded part of the lines $\ell$ and $\ell ^ { \prime }$ is contained in the simplices of the configuration, and we may add two connecting scgments outside the configuration, such that the rectangle spanned by the two outside connecting lines (that is, their convex hull) contains all the other connecting segments. Thus, we have placed a "ladder" such that each of the simplices of the configuration has one of the ladder's steps in its interior, while the four cnds of the ladder arc outside the configuration.

Now the main step is that we perform an (affine) coordinate transformation that maps $\mathbb { R } ^ { d }$ to $\mathbb { R } ^ { d }$ , and takes the rectangle spanned by the ladder to the rectangle (half-square) as shown in the figure below, given by

$$
\begin{array} { r l r } { R ^ { 1 } } & { = } & { \{ ( x _ { 1 } , x _ { 2 } , 0 , \ldots , 0 ) ^ { T } : - 1 \leq x _ { 1 } \leq 0 ; - 1 \leq x _ { 2 } \leq 1 \} . } \end{array}
$$

Thus the configuration of touching simplices $\Sigma ^ { 1 }$ in $\mathbb { R } ^ { d }$ which we obtain has the $x _ { 1 }$ -axis as a transversal line, and it is placed such that each of the simplices contains a segment

$$
S ^ { 1 } ( \alpha ) ~ = ~ \{ ( \alpha , x _ { 2 } , 0 , \ldots , 0 ) ^ { T } : - 1 \le x _ { 2 } \le 1 \}
$$

![](images/7f1c0e5c3836fa4fce90a71fc4d8113bebdfcd59fab79f20b40d48e916d76ba9.jpg)

in its interior (for some $\alpha$ with $- 1 < \alpha < 0$ ), while the origin 0 is outside all simplices.

Now we produce a second copy $\Sigma ^ { 2 }$ of this configuration by reflecting the first onc in the hyperplane given by $x _ { 1 } = x _ { 2 }$ . This second configuration has the $x _ { 2 }$ -axis as a transversal line, and each simplex contains a segment

$$
S ^ { 2 } ( \beta ) \ = \ \{ ( x _ { 1 } , \beta , 0 , \ldots , 0 ) ^ { T } : - 1 \leq x _ { 1 } \leq 1 \}
$$

in its interior, with $- 1 < \beta < 0$ But each segment $S ^ { 1 } ( \alpha )$ intersects each segment $S ^ { 2 } ( \beta )$ , and thus the interior of each simplex of $\Sigma ^ { 1 }$ intersects each simplex of $\Sigma ^ { 2 }$ in its interior. Thus if we add a new $( d + 1 )$ -st coordinate $x _ { d + 1 }$ , and take $\Sigma$ to be

![](images/96b6359ceb9b9fc5a2dd5c67a8cbd1938c65cb1ac2f2108fd8b5c8e33c74e4b5.jpg)

$$
\{ { \mathrm { c o n v } } ( P _ { i } \cup \{ - e _ { d + 1 } \} ) : P _ { i } \in \Sigma ^ { 1 } \} \ \cup \ \{ { \mathrm { c o n v } } ( P _ { j } \cup \{ e _ { d + 1 } \} ) : P _ { j } \in \Sigma ^ { 2 } \} ,
$$

then we get a configuration of touching $( d + 1 )$ -simplices in $\mathbb { R } ^ { d + 1 }$ . Furthermore, the antidiagonal

$$
A \ = \ \{ ( x , - x , 0 , \dotsc , 0 ) ^ { T } : x \in \mathbb { R } \} \ \subseteq \ \mathbb { R } ^ { d }
$$

intersects all segments $S ^ { 1 } ( \alpha )$ and $S ^ { 2 } ( \beta )$ We can tilit a little, nd a line

$$
L _ { \varepsilon } ~ = ~ \{ ( x , - x , 0 , \ldots , 0 , \varepsilon x ) ^ { T } : x \in \mathbb { R } \} ~ \subseteq ~ \mathbb { R } ^ { d + 1 } ,
$$

which for all small enough $\varepsilon > 0$ intersects all the simplices of $\Sigma$ .This completes our induction step. 0

In contrast to this exponential lower bound, tight upper bounds are harder to get. A naive inductive argument (considering all the facet hyperplanes in a touching configuration separately) yields only

$$
f ( d ) ~ \leq ~ \frac { 2 } { 3 } ( d + 1 ) ! ,
$$

and this is quite far from the lower bound of Theorem 1. However, Micha Perles found the following "magical" proof for a much better bound.

Theorem 2. For all $d \geq 1$ , we have $f ( d ) < 2 ^ { d + 1 }$ .

Proof. Given a configuration of $r$ touching $d$ -simplices $P _ { 1 } , P _ { 2 } , \ldots , P _ { r }$ in $\mathbb { R } ^ { d }$ , first enumerate the different hyperplanes $H _ { 1 } , H _ { 2 } , \dots , H _ { s }$ spanned by facets of the $P _ { i }$ , and for each of them arbitrarily choose a positive side $H _ { i } ^ { + }$ , and call the other side $H _ { i } ^ { - }$ .

For example, for the 2-dimensional configuration of $r = 4$ triangles depicted on the right we find $s = 6$ hyperplanes (which are lines for $d = 2$ .

From these data, we construct the $B$ -matrix, an $( r \times s )$ -matrix with entries in $\{ + 1 , - 1 , 0 \}$ , as follows:

$$
B _ { i j } : = \left\{ \begin{array} { r l } { + 1 } & { \mathrm { i f ~ } P _ { i } \mathrm { ~ h a s ~ a ~ f a c e t ~ i n ~ } H _ { j } \mathrm { , ~ a n d ~ } P _ { i } \subseteq H _ { j } ^ { + } , } \\ { - 1 } & { \mathrm { i f ~ } P _ { i } \mathrm { ~ h a s ~ a ~ f a c e t ~ i n ~ } H _ { j } \mathrm { , ~ a n d ~ } P _ { i } \subseteq H _ { j } ^ { - } , } \\ { 0 } & { \mathrm { i f ~ } P _ { i } \mathrm { ~ d o e s ~ n o t ~ h a v e ~ a ~ f a c e t ~ i n ~ } H _ { j } . } \end{array} \right.
$$

For example, the 2-dimensional configuration in the margin gives rise to the matrix

$$
B = \left( \begin{array} { c c c c c c c } { { 1 } } & { { 0 } } & { { 1 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { - 1 } } & { { - 1 } } & { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { - 1 } } & { { 1 } } & { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - 1 } } & { { - 1 } } & { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) .
$$

Three properties of the $B$ matrix are worth recording. First, since every $d .$ -simplex has $d + 1$ facets, we find that every row of $B$ has exactly $d + 1$ nonzero entries, and thus has exactly $s - ( d + 1 )$ zero entries. Secondly, we are dealing with a configuration of pairwise touching simplices, and thus for every pair of rows we find one column in which one row has a $+ 1$ entry, while the entry in the other row is ${ - 1 }$ . That is, the rows are different even if we disregard their zero entries. Thirdly, the rows of $B$ "represent" the simplices $P _ { i }$ , via

$$
P _ { i } = \bigcap _ { j : B _ { i j } = 1 } H _ { j } ^ { + } \cap \bigcap _ { j : B _ { i j } = - 1 } H _ { j } ^ { - } .
$$

Now we derive from $B$ a new matrix $C$ , in which every row of $B$ is replaced by all the row vectors that one can generate from it by replacing all the zeros by either $+ 1$ or $^ { - 1 }$ Since each row of $B$ has $s - d - 1$ zeros, and $B$ has $r$ rows, the matrix $C$ has $2 ^ { s - d - 1 } r$ rows.

![](images/065e4f596b514a493e015ecf231b42fe144b2d149efd1c4d7b39054826d640d0.jpg)

For our example, this matrix $C$ is a $( 3 2 \times 6 3 )$ -matrix that starts

$$
\begin{array} { r } { \mathcal { C } = \left( \begin{array} { c c c c c c c } { 1 } & { 1 } & { 1 } & { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { 1 } & { 1 } & { 1 } & { - 1 } \\ { 1 } & { 1 } & { 1 } & { - 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { 1 } & { - 1 } & { 1 } & { - 1 } \\ { 1 } & { - 1 } & { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { - 1 } & { 1 } & { 1 } & { 1 } & { - 1 } \\ { 1 } & { - 1 } & { 1 } & { - 1 } & { 1 } & { 1 } \\ { \frac { 1 } { - 1 } } & { - 1 } & { 1 } & { - 1 } & { - 1 } & { 1 } \\ { \frac { 1 } { - 1 } } & { - 1 } & { 1 } & { 1 } & { 1 } & { - 1 } \\ { - 1 } & { - 1 } & { 1 } & { 1 } & { 1 } & { - 1 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \end{array} \right) , } \end{array}
$$

![](images/6b194f14a637a506882aec81994f775ad0d833f0a98756c536e9390ba40b9249.jpg)

The first row of the $i$ -matrix represents the shaded triangle, while the second row corresponds to an empty intersection of the halfspaces. The point $\pmb { x }$ leads to the vector

$$
\left( \begin{array} { l l l l l l l l } { 1 } & { - 1 } & { } & { 1 } & { } & { 1 } & { - 1 } & { } & { 1 } \end{array} \right)
$$

that does not appear in the $C$ -matrix.

where the first eight rows of $C$ are derived from the first row of $B$ , the second eight rows come from the second row of $B$ , etc.

The point now is that all the rows of $C$ are different: If two rows are derived from the same row of $B$ , then they are different since their zeros have been replaced differently; if thcy are derived from different rows of $B$ , then they differ no matter how the zeros have been replaced. But the rows of $C$ are $( \pm 1 )$ -vectors of length $s$ , and there are only $2 ^ { s }$ different such vectors. Thus since the rows of $C$ are distinct, $C$ can have at most $2 ^ { s }$ rows, that is,

$$
2 ^ { s } \ d ^ { \ldots 1 } r \ \leq \ 2 ^ { s } .
$$

However, not all possible $( \pm 1 )$ -vectors appear in $C$ , which yields a strict inequality $2 ^ { s - d - 1 } r < 2 ^ { s }$ , and thus $r < 2 ^ { d + 1 }$ .To see this, we note that every row of $C ^ { \prime }$ represents an intersection of halfspaces — just as for the rows of $B$ before, via the formula $( \ast )$ . This intersection is a subset of the simplex $P _ { i }$ , which was given by the corresponding row of $B$ Let us take a point $\pmb { x } \in \mathbb { R } ^ { d }$ that does not lie on any of the hyperplanes $H _ { j }$ , and not in any of the simplices $P _ { i }$ .From this $\pmb { x }$ we derive a (±1)-vector that records for each $j$ whether $x \in H _ { j } ^ { + }$ or $x \in \mathop { I f } _ { j } ^ { - }$ .This $( \pm 1 )$ -vector docs not occur in $C$ , because its halfspace intersection according to $( \ast )$ contains $\pmb { x }$ and thus is not contained in any simplex $P _ { i }$ .

# References

[1] F. BAGEMIHL: A conjecture concerning neighboring tetrahedra, Amer. Math. Monthly 63 (1956) 328-329.   
[2] V. J. D. BAsToN: Some Properties of Polyhedra in Euclidean Space, Pergamon Press, Oxford 1965.   
[3] . A. PERIES: At most $2 ^ { d + 1 }$ neighborly simplices in $E ^ { t }$ , Annals of Discrete Math. 20 (1984), 253-254.   
[4] J. ZakS: Neighborly families of $2 ^ { d }$ $d$ -simplices in $E ^ { d }$ , Geometriae Dedicata 11 (1981), 279-296.   
[5] J. ZAKs: No Nine Neighborly Tetrahedra Exist, Memoirs Amer. Math. Soc. No. 447, Vol. 91, 1991.

# Every large point set has an obtuse angle

Around 1950 Paul Erdôs conjectured that every set of more than $2 ^ { d }$ points in $\mathbb { R } ^ { d }$ determines at least one obtuse angle, that is, an angle that is strictly greater than $\begin{array} { l } { { \frac { \pi } { 2 } } } \end{array}$ . In other words, any set of points in $\mathbb { R } ^ { d }$ which only has acute angles (including right angles) has size at most $2 ^ { d }$ .This problem was posed as a "prize question" by the Dutch Mathematical Society — but solutions were received only for $d = 2$ and for $d = 3$ .

For $d = 2$ the problem is easy: The five points may determine a convex pentagon, which always has an obtuse angle (in fact, at least one angle of at least $1 0 8 ^ { \circ }$ ). Otherwise we have one point contained in the convex hull of three others that form a triangle. But this point "sees" the three edges of the triangle in three angles that sum to $3 6 0 ^ { \circ }$ , so one of the angles is at least $1 2 0 ^ { \circ }$ . (The second case also includes situations where we have three points on a line, and thus a $1 8 0 ^ { \circ }$ angle.)

Unrelated to this, Victor Klee asked a few years later — and Erdôs spread the question — how large a point set in $\mathbb { R } ^ { d }$ could be and still have the following "antipodality property": For any two points in the set there is a strip (bounded by two parallel hyperplanes) that contains the point set, and that has the two chosen points on different sides on the boundary.

Then, in 1962, Ludwig Danzer and Branko Grünbaum solved both problems in one stroke: They sandwiched both maximal sizes into a chain of inequalities, which starts and ends in $2 ^ { d }$ .Thus the answer is $2 ^ { d }$ both for Erdôs' and for Klee's problem.

In the following, we consider (finite) sets $S \subseteq \mathbb { R } ^ { d }$ of points, their convex hulls $\mathrm { c o n v } ( S )$ , and general convex polytopes $Q \subseteq \mathbb { R } ^ { d }$ (See the appendix on polytopes on page 50 for the basic concepts.) We assume that these sets have the full dimension $d$ , that is, they are not contained in a hyperplane. Two convex sets touch if they have at least one boundary point in common, while their interiors do not intersect. For any set $Q \subseteq \mathbb { R } ^ { d }$ and any vector $\pmb { s } \in \mathbb { R } ^ { d }$ we denote by $Q + \pmb { s }$ the image of $Q$ under the translation that moves 0 to $\pmb { s }$ Similarly, $Q - s$ is the translate obtained by the map that moves $\pmb { s }$ to the origin.

Don't be intimidated: This chapter is an excursion into $d$ -dimensional geometry, but the arguments in the following do not require any "highdimensional intuition," since they all can be followed, visualized (and thus understood) in three dimensions, or even in the plane. Hence, our figures will illustrate the proof for $d = 2$ (where a "hyperplane" is just a line), and you could create your own pictures for $d \ : = \ : 3$ (where a "hyperplane" is a plane).

Theorem 1. For every $\vec { d } ,$ one has the following chain of inequalities:

$\begin{array} { r } { { 2 ^ { d } } \overset { ( 1 ) } { \leq } \operatorname* { m a x } \left\{ \# S \vert S \subseteq \mathbb { R } ^ { d } , \mathfrak { A } ( s _ { i } , s _ { j } , s _ { k } ) \leq \frac { \pi } { 2 } f o r e v e r y \left\{ s _ { i } , s _ { j } , s _ { k } \right\} \subseteq S \right\} } \end{array}$ ≤ max #s s ce d such tany wo poi $\{ \pmb { \mathscr { s } } _ { i } , \pmb { \mathscr { s } } _ { j } \} \subseteq S \}$ $S ( i , j )$ $S$ $\pmb { S } _ { 3 }$ 1 lying in the parallel boundary hyperplanes of $S ( i , j ) ~ ,$ $\stackrel { ( 3 ) } { = } \operatorname* { m a x } \Bigg \{ \# S$ S  Rd such that the translates the connvex hull $P : = \operatorname { c o n v } ( S )$ in $\left. \begin{array} { c } { { P - s _ { i } , s _ { i } \in S , o f } } \\ { { t e r s e c t i n \ : u c o m m o n } } \\ { { } } \end{array} \right\}$ point, but they only touch $\stackrel { ( 4 ) } { \leq } \mathrm { m a x } \left\{ \# S \left| \stackrel { S } { d i m e n s i o } \right. \right.$ such thatt the transt $Q + s _ { i }$ of saimeid d. $Q \subseteq \mathbb { R } ^ { d }$ ${ \stackrel { ( 5 ) } { = } } \operatorname* { m a x } \left\{ \# S \left| { \stackrel { S } { d } } \right. \right.$ Rd such that the translates $Q ^ { \ast } + s _ { i }$ of some $\begin{array} { r l r l } { \lfloor } & { { } } & { \mid Q ^ { * } \subseteq \mathbb { R } ^ { d } } \end{array}$ touch pairwise $\stackrel { ( 6 ) } { \leq } 2 ^ { d }$ .

![](images/021f7207bb82b8192f0fb8542041c51d01beb29756846536a634e46e23826b27.jpg)

Proof. We have six claims (equalitics and inequalities) to verify. Let's get going.

(1) Take ${ \cal { S } } : = \{ 0 , 1 \} ^ { d }$ to be the vertex set of the standard unit cube in $\mathbb { R } ^ { d . }$ , and choose $\mathbf { \mathfrak { s } } _ { i } , \mathbf { \mathcal { s } } _ { j } , \pmb { \mathscr { s } } _ { k } \in S$ . By symmetry wc may assume that $s _ { j } = 0$ is the zero vector. Hence the angle can be computed from

$$
\cos \triangleleft ( s _ { i } , s _ { j } , s _ { k } ) = \frac { \langle s _ { i } , s _ { k } \rangle } { \left| s _ { i } \right| \left| s _ { k } \right| }
$$

which is clearly nonnegative. Thus $S$ is a set with $| S _ { \textrm { i } } ^ { \dagger } = 2 ^ { d }$ that has no obtuse angles.

() If $S$ contains no obtuse angles, then for any $\mathbf { \mathscr { s } } _ { i } , \mathbf { \mathscr { s } } _ { j } \in { \ \bar { \mathbf { \mathscr { s } } } ^ { \prime } }$ we may define $H _ { i , j } + s _ { i }$ and $H _ { i j } + \pmb { s } _ { j }$ to bc thc parallel hyperplanes through $\pmb { s } _ { i }$ resp. ${ \pmb { s } } _ { j }$ that are orthogonal to the edge $[ \pmb { s } _ { i } , \pmb { s } _ { j } ]$ Here $H _ { i j } = \{ \pmb { x } \in \mathbb { R } ^ { d } : \langle \pmb { x } , \pmb { s } _ { i } - \pmb { s } _ { j } \rangle = 0 \}$ is the hyperplanc through the origin that is orthogonal to the line through $\pmb { S } _ { i }$ and $\pmb { s } _ { j }$ , and $H _ { i j } + s _ { j } = \{ { \pmb x } + { \pmb s } _ { j } : { \pmb x } \in H _ { i j } \}$ is the translate of $H _ { i , j }$ that passes through ${ \pmb s } _ { j }$ , etc. Hence the strip between $H _ { i , j } + s _ { i }$ and $H _ { i ; j } + s _ { j }$ consists, besides $\pmb { s } _ { i }$ and $\pmb { s } _ { j }$ , exactly of all the points $\pmb { x } \in \mathbb { R } ^ { d }$ such that the angles $\ P ( s _ { i } , s _ { j } , \pmb { x } )$ and $\triangleleft ( s _ { j } , s _ { i } , \pmb { x } )$ are non-obtuse. Thus the strip contains all of $S$ .

(3) $P$ is contained in the halfspace of $H _ { i j } + s _ { j }$ that contains $\pmb { { \cal B } } _ { i }$ if and only if $P - \mathbf { s } _ { j }$ is contained in the halfspace of $H _ { i j }$ that contains $\mathbf { \Delta } \mathbf { \mathcal { S } } _ { i } - \mathbf { \Delta } \pmb { \mathcal { S } } _ { j }$ : A property "an object is contained in a halfspace" is not destroyed if we translate both the object and the halfspace by the same amount (namely by $- s _ { j } )$ . Similarly, $P$ is containcd in the halfspace of $I I _ { i j } + s _ { i }$ that contains ${ \pmb s } _ { j }$ if and only if $\pmb { \mathscr { P } } - \pmb { \mathscr { s } } _ { i }$ is contained in the halfspace of $H _ { i j }$ that contains ${ \pmb s } _ { j } - { \pmb s } _ { i }$ .

Putting both statements together, we find that the polytope $P$ is contained in the strip between $H _ { i j } + s _ { i }$ and $H _ { i j } + s _ { j }$ if and only if $P - s _ { i }$ and $P - \pmb { s } _ { j }$ lie in different halfspaces with respect to the hyperplane $H _ { i j }$ .

This correspondence is illustrated by the sketch in the margin.

Furthermore, from $s _ { i } \in P = \mathsf { c o n v } ( S )$ we get that the origin O is contained in all the translates $P - \mathbf { \delta } _ { \mathbf { \delta } _ { i } }$ $( s _ { i } \in S )$ .Thus we see that the sets $P - \mathbf { \vec { s } } _ { i }$ all intersect in O, but they only touch: their interiors are pairwise disjoint, since they lie on opposite sides of the corresponding hyperplanes $H _ { i j }$ .

(4) This we get for free: "the translates must touch pairwise" is a weaker condition than "they intersect in a common point, but only touch." Similarly, we can relax the conditions by letting $P$ be an arbitrary convex $\textit { d }$ -polytope in $\mathbb { R } ^ { d }$ .Furthermore, we may replace $S$ by $\ldots S$ .

(5) Here $\because$ is trivial, but that is not the interesting direction for us. We have to start with a configuration $S \subseteq \mathbb { R } ^ { d }$ and an arbitrary $d ,$ polytope $\dot { Q } \subseteq \mathbb { R } ^ { d }$ such that the translates $Q + s _ { i }$ $( s _ { i } \in S )$ touch pairwise. The claim is that in this situation we can use

$$
Q ^ { * } : = \left\{ { \textstyle \frac { 1 } { 2 } } ( { \pmb x } - { \pmb y } ) \in \mathbb { R } ^ { d } : { \pmb x } , { \pmb y } \in Q \right\}
$$

instead of $Q$ .But this is not hard to see: First, $Q ^ { * }$ is $d$ -dimensional, convex, and centrally symmetric. One can check that $Q ^ { * }$ is a polytope (its vertices are of the form $\begin{array} { r } { \frac { 1 } { 2 } ( \pmb q _ { i } - \pmb q _ { j } ) } \end{array}$ , for vertices $\mathbf { \delta } \mathbf { \vec { q } } _ { i } , \mathbf { \vec { q } } _ { j }$ of $\mathcal { Q }$ ), but this is not important for us.

Now we will show that $Q + s _ { i }$ and $Q + { \pmb s } _ { j }$ touch if and only if $Q ^ { * } + { \pmb { \mathscr { s } } } _ { i }$ and $Q ^ { * } + { \mathfrak { s } } _ { j }$ touch. For this we note, in the footsteps of Minkowski, that

$$
\begin{array} { r l } & { ( Q ^ { * } + s _ { i } ) \cap ( Q ^ { * } + s _ { j } ) \neq \emptyset } \\ & { \qquad \iff \exists q _ { i } ^ { \prime } , q _ { i } ^ { \prime \prime } , q _ { j } ^ { \prime } , q _ { j } ^ { \prime \prime } \in Q : \frac { 1 } { 2 } ( q _ { i } ^ { \prime } - q _ { i } ^ { \prime \prime } ) + s _ { i } = \frac { 1 } { 2 } ( q _ { j } ^ { \prime } - q _ { j } ^ { \prime \prime } ) + s _ { j } } \\ & { \qquad \iff \exists q _ { i } ^ { \prime } , q _ { i } ^ { \prime \prime } , q _ { j } ^ { \prime } , q _ { j } ^ { \prime \prime } \in Q : \frac { 1 } { 2 } ( q _ { i } ^ { \prime } + q _ { j } ^ { \prime \prime } ) + s _ { i } = \frac { 1 } { 2 } ( q _ { j } ^ { \prime } + q _ { i } ^ { \prime \prime } ) + s _ { j } } \\ & { \qquad \iff \exists q _ { i } , q _ { j } \in Q : q _ { i } + s _ { i } = q _ { j } + s _ { j } } \\ & { \qquad \iff ( Q + s _ { i } ) \cap ( Q + s _ { j } ) \neq \emptyset , } \end{array}
$$

where in the third (and crucial) equivalence $\stackrel { 6 4 } { \longleftrightarrow } \stackrel { 7 } { \longleftrightarrow }$ we use that every ${ \pmb q } \in Q$ can be written as $\begin{array} { r } { \pmb q = \frac { 1 } { 2 } ( \pmb q + \pmb q ) , } \end{array}$ to get $\therefore \Leftarrow$ , and that $Q$ is convex and thus $\textstyle { \frac { 1 } { 2 } } \bigl ( \mathbf { q } _ { i } ^ { \prime } + \mathbf { q } _ { j } ^ { \prime \prime } \bigr )$ , $\textstyle { \frac { 1 } { 2 } } ( q _ { j } ^ { \prime } + q _ { i } ^ { \prime \prime } ) \in { \mathcal { Q } }$ to see $\ " \Rightarrow \ "$ .

![](images/afab6d9c5d8696bf738f0166697bb284c58bd8b5968f74ce68e16ac524fa781e.jpg)

Thus the passage from $\mathcal { Q }$ to $\mathcal { Q } ^ { \star }$ (known as Minkowski symmetrization) preserves the property that two translates $Q + s _ { i }$ and ${ \mathcal { Q } } + s _ { j }$ intersect. That is, we have shown that for any convex set $Q$ , two translates ${ \dot { Q } } + s _ { i }$ and $\mathcal { Q } + \mathfrak { s } _ { j }$ intersect if and only if the translates $\tilde { Q } ^ { \ast } + s _ { i }$ and ${ \dot { Q } } ^ { * } + { \pmb { \mathscr { s } } } _ { j }$ intersect.

The following characterization shows that Minkowski symmetrization also preserves the property that two translates touch:

${ \dot { Q } } + { \pmb s } _ { i }$ and $Q + s _ { j }$ touch if and only if they intersect, while $Q + s _ { i }$ and $Q + s _ { j } + \varepsilon ( s _ { j } - s _ { i } )$ do not intersect for any $\varepsilon > 0$ .

(6) Assume that $Q ^ { * } + s _ { i }$ and ${ Q ^ { * } + s } _ { j }$ touch. For every intersection point

$$
\mathbf { x } \in ( Q ^ { * } + s _ { i } ) \cap ( Q ^ { * } + s _ { j } )
$$

![](images/c6dfddd618195de7c74b2105c3e8146006ebf39440bae6f576bb6d5e039be9fa.jpg)

![](images/516e0e30340f57b90d975b4228ef0af21f91f96b3f7b1031e289e5197dbbae4c.jpg)

Scaling factor $\textstyle { \frac { 1 } { 2 } }$ , $\begin{array} { r } { \mathsf { v o l } ( P _ { j } ) = \frac { 1 } { \ S } \mathsf { v o l } \big ( P \big ) } \end{array}$

we have

$$
{ \pmb x } - { \pmb s } _ { i } \in Q ^ { * } \quad \mathrm { a n d } \quad { \pmb x } - { \pmb s } _ { j } \in Q ^ { * } ,
$$

thus, since $Q ^ { \ast }$ is centrally symmetric,

$$
\begin{array} { r } { { \pmb { s } } _ { i } - { \pmb x } = - ( { \pmb x } - { \pmb s } _ { i } ) \in { \pmb Q } ^ { * } , } \end{array}
$$

and hence, since $\hat { Q } ^ { \ast }$ is convex,

$$
\begin{array} { r } { \frac { 1 } { 2 } \big ( { \pmb s } _ { i } - { \pmb s } _ { j } \big ) = \frac { 1 } { 2 } \left( \big ( { \pmb x } - { \pmb s } _ { j } \big ) + \big ( { \pmb s } _ { i } - { \pmb x } \big ) \right) \in { \cal Q } ^ { * } . } \end{array}
$$

We conclude that $\frac { 1 } { 2 } ( s _ { i } + s _ { j } )$ is contained in ${ Q } ^ { * } + { \pmb { s } } _ { j }$ for all i. Consequently, for $P : = \mathrm { c o n v } ( S )$ we get

$$
\begin{array} { r } { P _ { j } : = \frac { 1 } { 2 } \big ( P + s _ { j } \big ) = \mathrm { c o n v } \left\{ \frac { 1 } { 2 } \big ( { s } _ { i } + { s } _ { j } \big ) : { s } _ { i } \in S \right\} \subseteq Q ^ { * } + s _ { j } , } \end{array}
$$

which implies that the sets $\begin{array} { r } { \bar { P } _ { j } = \frac { 1 } { 2 } ( P + \pmb { \mathscr { s } } _ { j } ) } \end{array}$ can only touch.

Finally, the sets $P _ { j }$ are contained in $P$ , because all the points $s _ { i } , \ s _ { j }$ and $\frac { 1 } { 2 } ( \pmb { s } _ { i } + \pmb { s } _ { j } )$ are in $P$ , since $P$ is convex. But the $P _ { j }$ are just smaller, scaled, translates of $P$ , contained in $P$ .The scaling factor is $\frac { 1 } { 2 }$ , which implies that

$$
{ \mathrm { v o l } } ( P _ { j } ) = { \frac { 1 } { 2 ^ { d } } } { \mathrm { v o l } } ( P ) ,
$$

since we are dealing with $d$ -dimensional sets. This means that at most $2 ^ { d }$ sets $P _ { j }$ fit into $P$ , and hence $| S | \le 2 ^ { d }$ .

This completes our proof: the chain of inequalities is closed.

... but that's not the end of the story. Danzer and Grünbaum asked the following natural question:

What happens if one requires all angles to be acute rather than just non-obtuse, that is, if right angles are forbidden?

They constructed configurations of $2 d - 1$ points in $\mathbb { R } ^ { d }$ with only acute angles, conjecturing that this may be best possible. Grünbaum proved that this is indced true for $\ d \leq 3$ But twenty-one years later, in 1983, Paul Erdós and Zoltan Füredi showed that the conjecture is false — quite dramatically, if the dimension is high! Their proof is a great example for the power of probabilistic arguments; see Chapter 35 for an introduction to the "probabilistic method." Our version of the proof uscs a slight improvement in the choice of the parameters due to our reader David Bevan.

Theorem 2. For every $\smash { d \geq 2 }$ , there is a set $\begin{array} { r } { S \subseteq \{ 0 , \lfloor \rfloor ^ { d } o f 2 \lfloor \frac { \sqrt { 6 } } { 9 } \Big ( \frac { 2 } { \sqrt { 3 } } \Big ) ^ { d } \rfloor } \end{array}$ points in $\mathbb { R } ^ { d }$ (vertices of the unit $d$ -cube) that determine only acute angles. In particular, in dimension $ d = 3 4$ there is a set of $7 2 > 2 { \cdot } 3 4 \mathrm { ~ - ~ } 1$ points with only acute angles.

Proof. Set $\begin{array} { r } { \pi : = \lfloor \frac { \sqrt { 6 } } { 9 } \left( \frac { 2 } { \sqrt { 3 } } \right) ^ { d } \rfloor } \end{array}$ , and pick 3m vectors

$$
\pmb { x } ( 1 ) , \pmb { x } ( 2 ) , \dots , \pmb { x } ( 3 \pi n ) \ \in \ \{ 0 , \mathbf { 1 } \} ^ { \mathrm { d } }
$$

by choosing all their coordinates independently and randomly, to be cither 0 or 1, with probability $\frac { 1 } { 2 }$ for each alternative. (You may toss a perfect coin 3md times for this; however, if $d$ is large you may get bored by this soon.)

We have seen above that all angles determined by $0 / 1$ -vectors are nonobtuse. Three vectors $\mathbf { { x } } ( i ) , \mathbf { { x } } ( j ) , \mathbf { { x } } ( k )$ determine a right angle with apex $\pmb { x } ( j )$ if and only if the scalar product $\langle \pmb { x } ( i ) - \pmb { x } ( j ) , \pmb { x } ( k ) - \pmb { x } ( j ) \rangle$ vanishes, that is, if we have

$$
x ( i ) _ { \ell } \ - x ( j ) _ { \ell } = 0 \quad \mathsf { o r } \quad x ( k ) _ { \ell } - x ( j ) _ { \ell } = 0
$$

We call $( i , j , k )$ a had triple if this happens. If $\pmb { x } ( i ) = \pmb { x } ( j )$ or $x ( j ) =$ $x ( k )$ , then the angle is not defined, but also then the triple $( i , j , k )$ is certainly bad.)

The probability that one specific triple is bad is exactly $\left( { \frac { 3 } { 4 } } \right) ^ { d }$ : Indeed, it will be good if and only if, for one of the $d$ coordinates $\ell$ , we get

$$
\begin{array} { l l l } { \mathrm { e i t h e r ~ } } & { x ( i ) _ { \ell } = x ( k ) _ { \ell } = 0 , } & { x ( j ) _ { \ell } = 1 , } \\ { \mathrm { o r ~ } } & { x ( i ) _ { \ell } = x ( k ) _ { \ell } = 1 , } & { x ( j ) _ { \ell } = 0 . } \end{array}
$$

This leaves us with six bad options out of eight equally likely ones, and a y $\frac { 3 } { 4 }$ happens for each of the $d$ coordinates.

T $3 \binom { 3 r \iota } { 3 }$ , since there are $\binom { 3 m } { 3 }$ sets of three vectors, and for cach of them there are three choices for the apex. Of course the probabilities that the various triples are bad are not independent: but linearity of expectation (which is what you get by averaging over all possible selections; see the appendix) yields that the expected y $3 { \binom { 3 m } { 3 } } \left( { \frac { 3 } { 4 } } \right) ^ { d }$ This means — and this is the point where the probabilistic method shows its power — that there is some choice of the $3 m$ v ha $3 \Big ( \begin{array} { c } { { 3 r n } } \\ { { 3 } } \end{array} \Big ) \Big ( \frac { \lambda } { 4 } \Big ) ^ { d }$ bad triples, where

$$
\begin{array} { r } { 3 \binom { ^ { 3 m } } { ^ 3 } \left( \frac { 3 } { 4 } \right) ^ { d } < 3 \frac { ( 3 m ) ^ { 3 } } { 6 } \left( \frac { 3 } { 4 } \right) ^ { d } = m ^ { 3 } \big ( \frac { 9 } { \sqrt { 6 } } \big ) ^ { 2 } \left( \frac { 3 } { 4 } \right) ^ { d } \leq m , } \end{array}
$$

by the choice of $_ { r n }$

But if there are not more than $\pi$ bad triples, then we can remove $m$ of the 3m vectors ${ \pmb x } ( i )$ in such a way that the remaining $2 m$ vectors don't contain a bad triple, that is, they determine acute angles only. □

The "\*probabilistic construction" of a large set of $0 / 1$ -points without right angles can be easily implemented, using a random number generator to "flip the coin." David Bevan has thus constructed a set of 31 points in dimension $d - 1 5$ that determines only acute angles.

# Appendix: Three tools from probability

Here we gather three basic tools from discrete probability theory which will come up several times: random variables, linearity of expectation and Markov's inequality.

Let $( \Omega , p )$ be a finite probability space, that is, $\Omega$ is a finite set and ${ \boldsymbol { p } } = \mathbf { P r o b }$ is a map from $\Omega$ into the interval $[ 0 , 1 ]$ with $\begin{array} { r } { \sum _ { \omega \in \Omega } p ( \omega ) = 1 } \end{array}$ A random variable $X$ on $\Omega$ is a mapping $X : \Omega \longrightarrow \mathbb { R }$ We define a probability space on the image set $X ( \Omega )$ by setting $\begin{array} { r } { p ( X = x ) : = \sum _ { X ( \omega ) = x } p ( \omega ) } \end{array}$ A simple example is an unbiased dice (all $\begin{array} { r } { p ( \omega ) = \frac { 1 } { 6 } ) } \end{array}$ with $X = { } ^ { \cdot }$ "the number on top when the dice is thrown."

The expectation $E X$ of $X$ is the avcrage to be expected, that is,

$$
E X ~ = ~ \sum _ { \omega \in \Omega } p ( \omega ) X ( \omega ) .
$$

Now suppose $X$ and $Y$ are two random variables on $\Omega$ , then the sum $X + Y$ is again a random variable, and we obtain

$$
\begin{array} { r c l } { E ( X + Y ) } & { = } & { \displaystyle \sum _ { \omega } p ( \omega ) \big ( X ( \omega ) + Y ( \omega ) \big ) } \\ & { = } & { \displaystyle \sum _ { \omega } p ( \omega ) X ( \omega ) + \sum _ { \omega } p ( \omega ) Y ( \omega ) = E X + E Y . } \end{array}
$$

Clearly, this can be extended to any finite linear combination of random variables — this is what is called the linearity of expectation. Note that it needs no assumption that the random variables have to be "indepcndent" in any sense!

Our third tool concerns random variables $X$ which take only nonnegative values, shortly denoted $X \geq 0$ Let

$$
\operatorname* { P r o b } ( X \geq a ) ~ = ~ \sum _ { \omega : X ( \omega ) \geq a } p ( \omega )
$$

be the probability that $X$ is at least as large as some $a > 0$ Then

$$
E X = \sum _ { \omega : X ( \omega ) \geq a } p ( \omega ) X ( \omega ) \ + \ \sum _ { \omega : X ( \omega ) < a } p ( \omega ) X ( \omega ) \ \geq \ a \sum _ { \omega : X ( \omega ) \geq a } p ( \omega ) ,
$$

and we have proved Markov's inequality

$$
\operatorname { P r o b } ( X \geq a ) \ \leq \ { \frac { E X } { a } } .
$$

# References

[1] L. DANZER & B. GRüNBAUM: Über zwei Probleme bezüglich konvexer Körper von P. Erdös und von V. L. Klee, Math. Zeitschrift 79 (1962), 95-99.   
[2] P. ERDs & Z. FÜREDI: The greatest angle among n points in the d-dimensional Euclidean space, Annals of Discrete Math. 17 (1983), 275-283.   
[3] H. MiNKowsKI: Dichteste gitterförmige Lagerung kongruenter Körper, Nachrichten Ges. Wiss. Göttingen, Math.-Phys. Klasse 1904, 311-355.

Karol Borsuk's paper "Three theorems on the $n$ -dimensional euclidean sphere" from 1933 is famous because it contained an important result (conjectured by Stanislaw Ulam) that is now known as the Borsuk-Ulam theorem:

Every continuous map $f : S ^ { d } \to \mathbb { R } ^ { d }$ maps two antipodal points of the sphere $S ^ { d }$ to the same point in $\mathbb { R } ^ { d }$ .

The same paper is famous also because of a problem posed at its end, which became known as Borsuk's Conjecture:

$^ { \ast }$

Can every set $S ~ \subseteq ~ \mathbb { R } ^ { d }$ of bounded diameter diam $\iota ( S ) \ > \ 0$ be partitioned into at most $d + 1$ sets of smaller diameter?

The bound of $d + 1$ is best possible: if $S$ is a regular $d$ dimensional simplex, or just the set of its $d + 1$ vertices, then no part of a diameter-reducing partition can contain more than one of the simplex vertices. If $f ( d )$ denotes the smallest number such that every bounded set $S \subseteq \mathbb { R } ^ { d }$ has a diameterreducing partition into $f ( d )$ parts, then the example of a regular simplex establishes $f ( d ) \geq d + 1$ .

Borsuk's conjecture was proved for the case when $S$ is a sphere (by Borsuk himself), for smooth bodies $S$ (using the Borsuk-Ulam theorem), for $d \leq$ 3, . . . but the general conjecture remained open. The best available upper bound for $f ( d )$ was established by Oded Schramm, who showed that

$$
f ( d ) \leq ( 1 . 2 3 ) ^ { d }
$$

for all large enough $d$ . This bound looks quite weak compared with the conjecture $\mathbf { \dot { \varphi } } _ { f ( d ) } = d + \mathbf { 1 } ^ { \prime }$ , but it suddenly seemed reasonable when Jeff Kahn and Gil Kalai dramatically disproved Borsuk's conjecture in 1993. Sixty years after Borsuk's paper, Kahn and Kalai proved that $f ( d ) \geq ( 1 . 2 ) ^ { \sqrt { d } }$ holds for large enough $d$ .

A Book version of the Kahn-Kalai proof was provided by A. Nilli: brief and self-contained, it yields an explicit counterexample to Borsuk's conjecture in dimension $d = 9 4 6$ We present here a modification of this proof, due to Andrei M. Raigorodskii and to Bernulf WeiBbach, which reduces the dimension to $d = 5 6 1$ , and even to $d = 5 6 0$ . The current "record" is $d = 2 9 8$ , achieved by Aicke Hinrichs and Christian Richter in 2002.

Karol Borsuk

![](images/beab8e4ab70203fa8a3e72539901f6555c653341d8c023b004dea1cacef752c9.jpg)

![](images/76086d4fb6d8eb6767ae9b60731092657b55347b7cbcd488a85311ea43460a06.jpg)

Any $^ { d }$ -simplex can be split into $d + 1$ pieces, each of smaller diameter.

![](images/7c575fcaa148b1b1115c000d9c6331534ce4db87ba03516244c4bab6adaed1a6.jpg)

A. Nilli

$$
{ \begin{array} { r l } { x } & { = { \left( \begin{array} { l } { 1 } \\ { - 1 } \\ { - 1 } \\ { 1 } \end{array} \right) } \ \Longrightarrow } \\ { x ^ { T } = \ ( \ { \begin{array} { r r r r r r } { 1 } & { - 1 } & { - 1 } & { 1 } & { - 1 } \end{array} } ) } \\ & { x x ^ { T } = { \left( \begin{array} { r r r r r r } { 1 } & { - 1 } & { - 1 } & { 1 } & { - 1 } \\ { - 1 } & { 1 } & { 1 } & { - 1 } & { 1 } \\ { - 1 } & { 1 } & { 1 } & { - 1 } & { 1 } \\ { 1 } & { - 1 } & { - 1 } & { 1 } & { - 1 } \\ { - 1 } & { 1 } & { 1 } & { - 1 } & { 1 } \end{array} \right) } } \end{array} }
$$

Theorem. Let $q = p ^ { m }$ be a prime power, $n : = 4 q - 2$ ,and $d : = { \binom { n } { 2 } } = \quad .$ $( 2 q - 1 ) ( 4 q - 3 )$ Then there is a set $S \subseteq \{ + 1 , - 1 \} ^ { d }$ of $2 ^ { n - 2 }$ points in $\mathbb { R } ^ { d }$ such that every partition of $S$ , whose parts have smaller diameter than $S _ { z }$ . has at least

$$
\frac { 2 ^ { n - 2 } } { \displaystyle \sum _ { i = 0 } ^ { q - 2 } \binom { n - 1 } { i } }
$$

parts. For $q = 9$ this implies that the Borsuk conjecture is false in dimension $d = 5 6 1$ Furthermore, $f ( d ) > ( 1 . 2 ) ^ { \sqrt { d } }$ holds for all large enough d.

roof.The construction of the set $S$ proceeds in four steps.

(1) Let $q$ be a prime power, set $n = 4 q - 2$ , and let

$$
Q ~ : = ~ \left\{ x \in \{ + 1 , - 1 \} ^ { n } : x _ { 1 } = 1 , \# \{ i : x _ { i } = - 1 \} { \mathrm { ~ i s ~ e v e n } } \right\} .
$$

This $Q$ is a set of $2 ^ { n - 2 }$ vectors in $\mathbb { R } ^ { n }$ .We will see that $\langle \pmb { x } , \pmb { y } \rangle \equiv 2 ( \mathrm { m o d } 4 )$ holds for all vectors $\textstyle { \pmb x } , { \pmb y } \in \mathrm { ~ } Q$ We will call $\mathbf { \nabla } _ { \mathbf { x } , \mathbf { y } }$ nearly-orthogonal if $| \langle { \pmb x } , { \pmb y } \rangle | = 2$ We will prove that any subset $Q ^ { \prime } \subseteq Q$ which contains no narly- $\begin{array} { r } { | Q ^ { \prime } | \leq \sum _ { i = 0 } ^ { q - 2 } { \binom { n - 1 } { i } } } \end{array}$

() From $Q$ , we construct the set

$$
R \ : = \ \{ x x ^ { T } : x \in Q \}
$$

of $2 ^ { n - 2 }$ symmetric $( n \times n )$ -matrices of rank 1. We interpret them as vectors with $n ^ { 2 }$ components, $R \subseteq \mathbb { R } ^ { n ^ { 2 } }$ .We will show that there are only acute angles between these vectors: they have positive scalar products, which are at least 4. Furthermore, if $R ^ { \prime } \subseteq R$ contains no two vectors with minimal scalar product 4, then $| R ^ { \prime } |$ is "smal" $\begin{array} { r } { | R ^ { \prime } | \leq \sum _ { i = 0 } ^ { q - 2 } { \binom { n - 1 } { i } } } \end{array}$

# Vectors, matrices, and scalar products

In our notation all vectors $\pmb { x }$ $\mathbf { r } , \pmb { y } , \ldots$ are column vectors; the transposed vectors ${ \pmb x } ^ { T } , { \pmb y } ^ { T } , \dots$ are thus row vectors. The matrix product $\pmb { x x } ^ { T }$ is a matrix of rank 1, with $( { \pmb x } { \pmb x } ^ { T } ) _ { i j } = x _ { i } x _ { j }$ .

If $\mathbf { \mu } _ { \mathbf { x } , \mathbf { y } }$ are column vectors, then their scalar product is

$$
\langle x , y \rangle \ = \ \sum _ { i } x _ { i } y _ { i } \ = \ x ^ { T } y .
$$

We will also need scalar products for matrices $X , Y \in \mathbb { R } ^ { n \times n }$ which can be interpreted as vectors of length $n ^ { 2 }$ , and thus their scalar product is

$$
\langle X , Y \rangle \ : = \ \sum _ { i , j } x _ { i j } y _ { i j } .
$$

(3) From $R$ we he   i $\mathbb { R } ^ { \binom { n } { 2 } }$ whose coordinates are the subdiagonal entries of the corresponding matrices:

$$
S \ : = \ \{ ( { \bf x x } ^ { T } ) _ { i > j } : x x ^ { T } \in R \} .
$$

Again, $s$ consists of $2 ^ { n - 2 }$ points. The maximal distance between these points is precisely obtained for the nearly-orthogonal vectors $\pmb { x } , \pmb { y } \in \mathcal { Q }$ . We ccone $S ^ { \prime } \subseteq S$ of smaler diameter than $S$ must be $\textstyle | { \tilde { S } } ^ { \prime } | \leq \sum _ { i = 0 } ^ { q - 2 } { \binom { n - 1 } { i } }$

(4) Estimates: From (3) we see that one needs at least

$$
g ( q ) : = \frac { 2 ^ { 4 q - 4 } } { \sum _ { i = 0 } ^ { q \ 2 } { \binom { 4 q - 3 } { i } } }
$$

parts in every diameter-reducing partition of $\bar { S }$ Thus

$$
f ( d ) \ \geq \ \operatorname* { m a x } \{ g ( q ) , d + 1 \} \qquad \mathrm { f o r } \ d \ = \ ( 2 q - 1 ) ( 4 q - 3 ) .
$$

Therefore, whenever we have $g ( q ) > ( 2 q - 1 ) ( 4 q - 3 ) + 1$ , then we have a counterexample to Borsuk's conjecture in dimension $d \simeq ( 2 q - 1 ) ( 4 q - 3 )$ . We will calculate below that $g ( 9 ) > 5 6 2$ , which yields the counterexample in dimension $d = 5 6 1$ , and that

$$
g ( q ) > \frac { e } { 6 4 q ^ { 2 } } \left( \frac { 2 7 } { 1 6 } \right) ^ { q } ,
$$

c yie $f ( d ) > ( 1 . 2 ) ^ { \sqrt { d } }$ for $\smash { d }$ large enough.

Details for (1): We start with some harmless divisibility considerations.

Lemma. The function $P ( z ) : = { \binom { z - 2 } { q - 2 } }$ is a polynomial of degree $q - 2$ yields integer values for all integers $z$ The integer $P ( z )$ is divisible by $p$ if and only if $z$ is not congruent to 0 or | modulo $q$ .

Proof. For this we write the binomial coefficient as

$$
P ( z ) = { \binom { z - 2 } { q - 2 } } = { \frac { ( z - 2 ) ( z - 3 ) \cdot \ldots \cdot ( z - q + 1 ) } { ( q - 2 ) ( q - 3 ) \cdot \ldots \cdot \ldots \cdot 2 \cdot 1 } }
$$

and compare the number of $p$ -factors in the denominator and in the numerator. The denominator has the same number of $\pmb { p }$ -factors as $( q - 2 ) !$ , or as $( q - 1 ) !$ , since $q - 1$ is not divisible by $\mathcal { P }$ . Indeed, by the claim in the margin we get an integer with the same number of $\mathbf { \mathcal { J } }$ -factors if we take any product of $q - 1$ integers, one from each non-zero residue class modulo $q$ .

Now if $\ddot { \ddot { \mathbf { \pi } } }$ is congruent to 0 or $\mathbf { 1 } \ ( \mathbf { m o d } q )$ , then the numerator is also of this type: All factors in the product are from different residue classes, and the only classes that do not occur are the zero class (the multiples of $q$ ), and the class either of $- l$ or of $+ 1$ , but neither $+ 1 \ n o r - 1$ is divisible by $p$ Thus denominator and numerator have the same number of $\mathscr { p }$ -factors, and hence the quotient is not divisible by $\mathscr { p }$ .

Claim. If $\texttt { a } \equiv \texttt { b } \not \equiv \texttt { l } ( \mod q )$ , then a and $b$ have the same number of $p .$ factors.

Proof. Wc have $a = \mathfrak { b } + s \mathfrak { p } ^ { m }$ , where $\pmb { \theta }$ is not divisible by $p ^ { \mathfrak { m } } = q$ So every power $p ^ { k }$ that divides $b$ satisfics $k < \gamma \eta$ . and thus it also divides $^ { a }$ The statement is symmetric in $^ { a }$ and $\boldsymbol { b }$ .

On the other hand, if $z \not \equiv 0 , 1 ( { \bf m o d } q )$ , then the numerator of $( \ast )$ contains one factor that is divisible by $q = p ^ { m }$ At the same time, the product has no factors from two adjacent nonzero residue classes: one of them represents numbers that have no $p$ -factors at all, the other one has fewer $p$ -factors than $q = p ^ { m }$ . Hence there are more $p$ -factors in the numerator than in the denominator, and the quotient is divisible by $p$ . □

Now we consider an arbitrary subset $Q ^ { \prime } \subseteq Q$ that does not contain any nearly-orthogonal vectors. We want to establish that $Q ^ { \prime }$ must be "small."

Claim 1. If $\cdot _ { x , y }$ are distinct vectors from $Q$ , then $\begin{array} { r } { \frac { 1 } { 4 } ( \langle \pmb { \mathscr { x } } , \pmb { y } \rangle + 2 ) } \end{array}$ is an integer in the range

$$
- ( q - 2 ) \ \leq \ \frac 1 4 ( \langle x , y \rangle + 2 ) \ \leq \ q - 1 .
$$

Both $_ { \pmb { x } }$ and $\pmb { y }$ have an even number of $( - 1 )$ -components, so the number of components in which $\textbf { \em x }$ and $\pmb { y }$ differ is even, too. Thus

$$
\langle { \pmb x } , { \pmb y } \rangle ~ = ~ ( 4 q - 2 ) ~ - ~ 2 \# \{ i : x _ { i } \neq y _ { i } \} ~ \equiv ~ - 2 ~ ( \mathrm { m o d } 4 )
$$

for all $\pmb { x } , \pmb { y } \in Q$ , that is, $\begin{array} { r } { \frac { 1 } { 4 } ( \langle \pmb { x } , \pmb { y } \rangle + 2 ) } \end{array}$ is an integer.

From $x , y \in \{ + 1 , - 1 \} ^ { 4 q - 2 }$ we see that $- ( 4 q - 2 ) \le \langle { \pmb x } , { \pmb y } \rangle \le 4 q - 2 ,$ that is, $\begin{array} { r } { - ( q - 1 ) \le \frac 1 4 ( \langle { \pmb x } , { \pmb y } \rangle + 2 ) \le q } \end{array}$ The lower bound never holds with equality, since $x _ { 1 } = y _ { 1 } = 1$ implies that $\pmb { x } \neq - \pmb { y }$ The upper bound holds with equality only if $\mathbf { \mu } _ { \mathbf { x } } = \mathbf { \mu } _ { \mathbf { y } }$ .

Claim 2. For any $\pmb { y } \in Q ^ { \prime }$ , the polynomial in n variables $x _ { 1 } , \ldots , x _ { n }$ of degree $q - 2$ given by

$$
F _ { y } ( { \pmb x } ) ~ : = ~ P \big ( { \textstyle { \frac { 1 } { 4 } } } ( \langle { \pmb x } , { \pmb y } \rangle + 2 ) \big ) ~ = ~ \bigg ( \displaystyle { \frac { 1 } { 4 } } \big ( \langle { \pmb x } , { \pmb y } \rangle + 2 \big ) - 2 \bigg )
$$

satisfies that $F _ { \pmb { y } } ( \pmb { x } )$ is divisible by $p$ for every ${ \pmb x } \in Q ^ { \prime } \backslash \{ { \pmb y } \}$ , but not for $\mathbf { \mu } _ { \mathbf { x } } = \mathbf { \mu } _ { \mathbf { y } }$ .

The representation by a binomial coefficient shows that $F _ { \pmb { y } } ( \pmb { x } )$ is an integervalued polynomial. For $\textbf { \em x } = \textbf { \em y }$ , we get $F _ { \pmb { y } } ( \pmb { y } ) = 1$ For $\textit { \textbf { x } } \neq \textit { \textbf { y } }$ , the Lemma yields that $F _ { \pmb { y } } ( \pmb { x } )$ is not divisible by $p$ if and only if $\begin{array} { r } { \frac { 1 } { 4 } ( \left. \pmb { x } , \pmb { y } \right. + 2 ) } \end{array}$ is congruent to 0 or $\lfloor \left( { \bmod { q } } \right)$ . By Claim 1, this happens only if $\scriptstyle { \frac { 1 } { 4 } } ( \langle \pmb { x } , \pmb { y } \rangle + 2 )$ is either 0 or 1, that is, f $\langle \pmb { x } , \pmb { y } \rangle \in \{ - 2 , + 2 \}$ . So $\textbf { \em x }$ and $\pmb { y }$ must be nearlyorthogonal for this, which contradicts the definition of $Q ^ { \prime }$ .

Claim 3. The same is true for the polynomials $\overline { { F } } _ { \pmb { y } } ( \pmb { x } )$ in the $n - 1$ variables $x _ { 2 } , \ldots , x _ { n }$ that are obtained as follows: Expand $F _ { \mathbf { y } } ( \pmb { x } )$ into monomials and remove the variable $x _ { 1 }$ , and reduce all higher powers of other variables, by substituting $x _ { 1 } = 1$ , and $x _ { i } ^ { 2 } = 1$ for $i > 1$ The polynomials $\overline { { F } } _ { \pmb { y } } ( \pmb { x } )$ have degree at most $q - 2$ .

The vectors $\pmb { x } \in Q \subseteq \{ + 1 , - 1 \} ^ { n }$ all satisfy $x _ { 1 } = 1$ and $x _ { i } ^ { 2 } = 1$ .Thus the substitutions do not change the values of the polynomials on the set $Q$ . They also do not increase the degree, so $\overline { { F } } _ { \pmb { y } } ( \pmb { x } )$ has degree at most $q - 2$ .

Claim 4. There is no linear relation (with rational coefficients) between the polynomials $\overline { { F } } _ { y } ( x )$ , that is, the polynomials $\overline { { F } } _ { y } \{ { \pmb x } \}$ $y \in Q ^ { \prime }$ , are linearly independent over $\nsubseteq$ In particular, they are distinct.

Aa  i $\begin{array} { r } { \sum _ { y \in \mathcal { Q } ^ { \prime } } \alpha _ { y } \overline { { F } } _ { y } ( x ) = 0 } \end{array}$ such that not all coefficients $\alpha _ { y }$ are zero, After multiplication with a suitable scalar we may assume that all the coefficients are integers, but not all of them are divisible by $p$ But then for every $y \in Q ^ { \prime }$ the evaluation at $x : = y$ yields that $\alpha _ { y } \sqrt { y } _ { y } ( y )$ is divisible by $p$ , and hence so is $\alpha _ { y }$ , since $\overline { { f } } ( y )$ is not.

Cfadn $| Q ^ { \prime } |$ is varibr of squoref $q - 2$ $n - 1$ $\sum \limits _ { i = 0 } ^ { n - 2 } ( \sum \limits _ { i } ^ { n - 1 } )$

By construction the polynomials $\overline { { F } } _ { y }$ are squarefree: none of their monomials contains a variable with higher degrce than 1. Thus each $\overline { { F } } _ { y } ( { \bf x } )$ is a linear combination of the squarefree monomials of degree at most $q - 2$ in the $ \nwarrow \cdots 1$ variables $x _ { : 2 } , \ldots , x _ { n }$ .Sincc the polynomials $| F _ { y } ( x )$ are lincarly independent, their number (which is $\cdot Q ^ { \prime } |$ ) cannot be larger than the number of monomials in question.

Details for (2): Thc first column of ${ \pmb x } { \pmb x } ^ { T }$ is $\pmb { x }$ Thus for distinct $x \in Q$ we obtain distinct matrices $M ( x ) : = x x ^ { T }$ . We interpret these matrices as vectors of length $\gamma _ { l } \} ^ { 2 }$ with components $x _ { i } x _ { j }$ A simple computation

$$
\begin{array} { l l l l } { \left. M ( { \pmb x } ) , M ( { \pmb y } ) \right. } & { \ \stackrel { } { = } } & { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } ( x _ { i } x _ { j } ) ( y _ { i } y _ { j } ) } \\ & { = } & { \displaystyle \Big ( \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \Big ) \Big ( \sum _ { j = 1 } ^ { n } x _ { j } y _ { j } \Big ) \ = \ \langle { \pmb x } , { \pmb y } \rangle ^ { 2 } \ \geq \ 4 } \end{array}
$$

shows that the scalar product of $M ( x )$ and $M ( y )$ is minimized if and only if $x , y \in Q$ are nearly-orthogonal.

Details for (3): Let $U ^ { \prime } ( \mathbf { x } ) ~ \in ~ \{ + 1 . - 1 \} ^ { d } .$ denote the vector of all subdiagonal entries of $M ( x )$ .Since $M ( { \pmb x } ) = { \pmb x } { \pmb x } ^ { T }$ is symmetric with diagonal values $+ 1$ , we see that $\Im [ \left( { \bf x } \right) \ne \Re \left( { \bf y } \right) ]$ implies $U ( { \pmb x } ) \neq U ( { \pmb y } )$ . Furthermore,

$$
4 ~ \leq ~ \left. M ( { \pmb x } ) , M ( { \pmb y } ) \right. ~ = ~ 2 \langle U ( { \pmb x } ) , U ( { \pmb y } ) \rangle ~ \textrm { i } \ n ,
$$

that is,

$$
\begin{array}{c} \langle U ( { \pmb x } ) , U ( { \pmb y } ) \rangle \ge - \frac { \pi } { 2 } \{ \ { \pmb \Sigma } ^ { } \ { \pmb \Sigma } ^ { } \} _ { } \end{array}
$$

with equality if and only if $\pmb { x }$ and $y$ are nearly-orthogonal. Since all the vectors $U ( x ) \in S$ have the same length $\begin{array} { r } { \sqrt { \langle U ( \mathbf { x } ) , U ( \mathbf { x } ) \rangle } = \sqrt { \binom { \hbar } { 2 } } } \end{array}$ , this means that the maximal distance between points $U ( \mathbf { x } ) , U ( \mathbf { y } ) \in \mathcal { S }$ is achieved exactly when $\pmb { x }$ and $\pmb { y }$ are nearly-orthogonal.

Details for (4): For $q = 0$ wc have $g ( 9 ) \approx 7 5 8 . 3 1$ , which is greatcr than $t ^ { \downarrow } + 1 = { \binom { 3 \cdot 1 } { 2 } } + 1 = \bar { 5 } 6 2$

![](images/803bb7a5957b27c0e1171f65bde2223fb96cce0678ba1a528a61dac47bab94f2.jpg)

To obtain a general bound for large $d ,$ we use monotonicity and unimodality oel cffint an te t $n ! > e ( \frac { \pi } { e } ) ^ { \pi }$ and $n ! < \tan ( \frac { n } { e } ) ^ { \prime \varepsilon }$ (see the appendix to Chapter 2) and derive

$$
\sum _ { i = 0 } ^ { q - 2 } { \binom { 4 q - 3 } { i } } < q { \binom { 4 q } { q } } = q { \frac { ( 4 q ) ! } { q ! ( 3 q ) ! } } < q { \frac { e 4 q \left( { \frac { 4 q } { e } } \right) ^ { 4 q } } { e \left( { \frac { q } { e } } \right) ^ { q } e \left( { \frac { 3 q } { e } } \right) ^ { 3 q } } } = { \frac { 4 q ^ { 2 } } { e } } { \left( { \frac { 2 5 6 } { 2 7 } } \right) } ^ { q } .
$$

Thus we conclude

$$
f ( d ) \geq g ( q ) = \frac { 2 ^ { 4 q - 4 } } { \displaystyle \sum _ { i = 0 } ^ { q - 2 } \binom { 4 q - 3 } { i } } > \frac { e } { 6 4 q ^ { 2 } } \Big ( \frac { 2 7 } { 1 6 } \Big ) ^ { q } .
$$

From this, with

$$
\begin{array} { r l } & { d = ( 2 q - 1 ) ( 4 q - 3 ) = 5 q ^ { 2 } + ( q - 3 ) ( 3 q - 1 ) \geq 5 q ^ { 2 } \quad \mathrm { f o r } q \geq 3 , } \\ & { \qquad q = \frac { 5 } { 8 } + \sqrt { \frac { d } { 8 } + \frac { 1 } { 6 4 } } > \sqrt { \frac { d } { 8 } } , \qquad \mathrm { a n d } \qquad ( \frac { 2 7 } { 1 6 } ) ^ { \sqrt { \frac { 1 } { 8 } } } > 1 . 2 0 3 2 , } \end{array}
$$

we get

$$
f ( d ; ~ > ~ \frac { e } { 1 3 d } ( 1 . 2 0 3 2 ) ^ { \sqrt { d } } ~ > ~ ( 1 . 2 ) ^ { \sqrt { d } } ~ \mathrm { ~ f o r ~ a l l ~ l a r g e ~ e n o u g h } ~ d .
$$

A counterexample of dimension 560 is obtained by noting that for $q = 9$ the quotient $g ( q ) \approx 7 5 8$ is much larger than the dimension $d ( q ) = 5 6 1$ . Thus one gets a counterexample for $d = 5 6 0$ by taking only the "three fourths" of the points in $s$ that satisfy $x _ { 2 1 } + x _ { 3 1 } + x _ { 3 2 } = - 1$ .

Borsuk's conjecture is known to be true for $\ d \ \leq \ 3$ , but it has not been verified for any larger dimension. In contrast to this, it is true up to $1 7 = 8$ if we restrict ourselves to subsets $S \subseteq \{ 1 , - 1 \} ^ { d }$ , as constructed above (see [8]). In either case it is quite possible that counterexamples can be found in reasonably small dimensions.

# References

[1] K. BoRsuk: Drei Sätze über die $\pmb { n }$ -dimensionale euklidische Sphäre, Fundamenta Math. 20 (1933), 177-190.   
[2] A. HinriChs & C. RiChTEr: New sets with large Borsuk numbers, Preprint, February 2002, 10 pages; Discrete Math., to appear.   
[3] J. KAHN & G. KALAI: A counterexample to Borsuk's conjecture, Bulletin Amer. Math. Soc. 29 (1993), 60-62.   
[4] A. NiLLl: On Borsuk's problem, in: "Jerusalem Combinatorics '93" (H. Barcelo and G. Kalai, eds.), Contemporary Mathematics 178, Amer. Math. Soc. 1994, 209-210.   
[5] A. M. RAIGORODsKII: On the dimension in Borsuk's problem, Russian Math. Surveys (6) 52 (1997), 1324-1325.   
[6] O. SCHRAMM: Illuminating sets of constant width, Mathematika 35 (1988), 180-199.   
[7] B. WElssBACH: Sets with large Borsuk number, Beiträge zur Algebra und Geometrie/Contributions to Algebra and Geometry 41 (2000), 417-423.   
[8] G. M. ZIEGLER: Coloring Hamming graphs, optimal binary codes, and the 0/I-Borsuk problem in low dimensions, Lecture Notes in Computer Science 2122, Springer-Verlag 2001, 164-175.

# Sets, functions, and the continuum hypothesis

Set theory, founded by Georg Cantor in the second half of the 19th century, has profoundly transformed mathematics. Modern day mathematics is unthinkable without the concept of a set, or as David Hilbert put it: "Nobody will drive us from the paradise (of set theory) that Cantor has created for us."

One of Cantor's basic concepts was the notion of the size or cardinality of a set $M$ , denoted by $\lvert M \rvert$ . For finite sets, this presents no difficulties: we just count the number of elements and say that $M$ is an $n$ -set or has size $_ n$ , if $M$ contains precisely $n$ elements. Thus two finite sets $M$ and $N$ have equal size, $| M | = | N |$ , if they contain the same number of elements.

To carry this notion of equal size over to infinite sets, we use the following suggestive thought experiment for finite sets. Suppose a number of people board a bus. When will we say that the number of people is the same as the number of available seats? Simple enough, we let all people sit down. If everyone finds a seat, and no seat remains empty, then and only then do the two sets (of the people and of the seats) agree in number. In other words, the two sizes are the same if there is a bijection of one set onto the other.

This is then our definition: Two arbitrary sets $M$ and $N$ (finite or infinite) are said to be of equal size or cardinality, if and only if there exists a bijection from $M$ onto $N$ .Clearly, this notion of equal size is an equivalence relation, and we can thus associate a number, called cardinal number, to every class of equal-sized sets. For example, we obtain for finite sets the cardinal numbers $0 , 1 , 2 , \ldots , n , \ldots$ where $\boldsymbol { n }$ stands for the class of $n$ -sets, and, in particular, O for the empty set $\varnothing$ We further observe the obvious fact that a proper subset of a finite set $M$ invariably has smaller size than $M$ .

The theory becomes very interesting (and highly non-intuitive) when we turn to infinite sets. Consider the set $\mathbb { N } = \{ 1 , 2 , 3 , . . . \}$ of natural numbers. We call a set $M$ countable if it can be put in one-to-one correspondence with $\mathbb { N }$ In other words, $M$ is countable if we can list the elements of $M$ as $m _ { 1 } , m _ { 2 } , m _ { 3 } , . . . .$ But now a strange phenomenon occurs. Suppose we add to $\mathbb { N }$ a new element $x$ Then $\mathbb { N } \cup \{ x \}$ is still countable, and hence has equal size with $\mathbb { N } !$

This fact is delightfully illustrated by "Hilbert's hotel." Suppose a hotel has countably many rooms, numbered $1 , 2 , 3 , \ldots$ with guest $g _ { i }$ occupying room $i$ ; so the hotel is fully booked. Now a new guest $_ x$ arrives asking for a room, whereupon the hotel manager tells him: Sorry, all rooms are taken. No problem, says the new arrival, just move guest $g _ { 1 }$ to room 2, $g _ { 2 }$ to room 3, $g _ { 3 }$ to room 4, and so on, and I will then take room 1. To the

![](images/238cf13c14c313387a9d3f4ee573922642537167dfc50843d7bb6466c4dc204f.jpg)

Georg Cantor

![](images/2be1aab955d7d1cae0be1197390bb29da968c83545ea1b3c923a0e908a9271f4.jpg)

![](images/0a9ceac47324e31545c4650bce7bb31adea2c29b383331eabaf854e61863e553.jpg)

manager's surprise (he is not a mathematician) this works; he can still put up all guests plus the new arrival x!

Now it is clear that he can also put up another guest $y$ , and another one $z$ , and so on. In particular, we note that, in contrast to finite sets, it may well happen that a proper subset of an infinite set $M$ has the same size as $M$ .In fact, as we will see, this is a characterization of infinity: A set is infinite if and only if it has the same size as some proper subset.

Let us leave Hilbert's hotel and look at our familiar number sets. The sct $\mathbb { Z }$ of integers is again countable, since we may enumerate $\mathbb { Z }$ in the form $\mathbb { Z } = \{ 0 , 1 , - 1 , 2 , - 2 , 3 , - 3 , . . . \}$ . It may come more as a surprise that the rationals can be enumerated in a similar way.

Theorem 1. The set $Q$ of rational numbers is countable.

Proof. By listing the set $\mathbb { Q } ^ { + }$ of positive rationals as suggested in the figure in the margin, but leaving out numbers already encountered, we see that $\mathbb { Q } ^ { + }$ is countable, and hence so is $\mathbb { Q }$ by listing 0 at the beginning and $- { \frac { \mathfrak { p } } { \mathfrak { q } } }$ right after $\begin{array} { l } { { \underline { { { \vec { E } } } } } ^ { \gamma } } \\ { { \underline { { { \vec { \boldsymbol { \psi } } } } } } } \end{array}$ With tthis listing

![](images/66b1593375b9c0d5244bca7a365ce448ee41547cc78425642a63fcd26acdc05a.jpg)

$$
\begin{array} { r } { \mathbb { Q } = \{ \ell , 1 , - 1 , 2 , - 2 , \frac { 1 } { 2 } , - \frac { 1 } { 2 } , \frac { 1 } { 3 } , - \frac { 1 } { 3 } , 3 , - 3 , 4 , - 4 , \frac { 3 } { 2 } , - \frac { 3 } { 2 } , \ldots \} . } \end{array}
$$

Another way to interpret the figure is the following statement:

The union of countably many countable sets $M _ { \pi }$ is again countable.

Indeed, set $M _ { n } = \{ a , _ { n 1 } , a , _ { n 2 } , a _ { n 3 } , . . . \}$ and list

$$
\bigcup _ { n = 1 } ^ { \infty } M _ { n } \ = \ \{ a _ { 1 1 } , a _ { 2 1 } , a _ { 1 2 } , a _ { 1 3 } , a _ { 2 2 } , a _ { 3 1 } , a _ { 4 1 } , a _ { 3 2 } , a _ { 2 3 } , a _ { 1 4 } , . . . \ \}
$$

precisely as before.

Let us contemplate Cantor's enumeration of the positive rationals a bit more. Looking at the figure we obtained the sequence

$$
{ \frac { 1 } { 1 } } , \ { \frac { 2 } { 1 } } , \ { \frac { 1 } { 2 } } , \ { \frac { 1 } { 3 } } , \ { \frac { 2 } { 2 } } , \ { \frac { 3 } { 1 } } , \ { \frac { 4 } { 1 } } , \ { \frac { 3 } { 2 } } , \ { \frac { 2 } { 3 } } , \ { \frac { 1 } { 4 } } , \ { \frac { 1 } { 5 } } , \ { \frac { 2 } { 4 } } , \ { \frac { 3 } { 3 } } , \ { \frac { 4 } { 2 } } , \ { \frac { 5 } { 1 } } , \ \ldots .
$$

$\begin{array} { r } { \frac { 2 } { 2 } = \frac { 1 } { 1 } \mathbf { o r } \frac { 2 } { 4 } = \frac { 1 } { 2 } . } \end{array}$

But there is a listing that is even more elegant and systematic, and which contains no duplicates — found only quite recently by Neil Calkin and Herbert Wilf. Their new list starts as follows:

$$
{ \frac { 1 } { 1 } } \colon { \frac { 1 } { 2 } } , \ { \frac { 2 } { 1 } } , \ { \frac { 1 } { 3 } } , \ { \frac { 3 } { 2 } } , \ { \frac { 2 } { 3 } } , \ { \frac { 3 } { 1 } } , \ { \frac { 1 } { 4 } } , \ { \frac { 4 } { 3 } } , \ { \frac { 3 } { 5 } } , \ { \frac { 5 } { 2 } } , \ { \frac { 2 } { 5 } } , \ { \frac { 5 } { 3 } } , \ { \frac { 3 } { 4 } } , \ { \frac { 4 } { 1 } } , \ { \dots } \ .
$$

Here the denominator of the $n$ -th rational number equals the numerator of the $( n + 1 )$ -st number. In other words, the $n$ -th fraction is $\bar { b } ( \bar { n } ) / \bar { b } ( \bar { n } + 1 )$ . where $( b ( n ) ) _ { \cdots ( 1 ) }$ is a sequence that starts with

$$
( 1 , 1 , 2 , 1 , 3 , 2 , 3 , 1 , 4 , 3 , 5 , 2 , 5 , 3 , 4 , 1 , 5 , . . . ) .
$$

This sequence has first been studied by a German mathematician, Moritz Abraham Stern, in a paper from 1858, and is has become known as "Stern's diatomic series."

How do we obtain this sequence, and hence the Calkin-Wilf listing of the positive fractions? Consider the infinite binary tree in the margin. We immediately note its recursive rule:

• $\frac { \downarrow } { \lambda }$ is on top of the tree, and every node $\frac { i } { j }$ has two sons he left on is $\frac { i } { \cdot i + j }$ and he right son is $\textstyle { \frac { i + j } { j } }$ .

We can easily check the following four properties:

(1) All fractions in the tree are reduced, that is, if $\frac { \texttt { T } } { s }$ appears in the tree, then $r$ and $\pmb { S }$ are relatively prime.

This holds for the top $\frac { \mathsf { L } } { \mathsf { l } }$ , and then we use induction downward. If $\gamma$ and $s$ are relatively prime, then so are $r$ and $r + s$ , as well as $s$ and $r + s$ .

Every reduced fraction $\frac { r } { s } > 0$ appears in the tree.

We use induction on the sum $r + s$ The smallest value is $r + s = 2$ , that is $\begin{array} { r } { \frac { r } { s } = \frac { 1 } { 1 } } \end{array}$ , and this appears at the t.I $r > s$ , then $\frac { r - s } { s }$ appears in the tree by induction, and so we get $\frac { r } { s }$ as is right son. Sialy, if $r < s$ , then $\frac { r } { s - r }$ appears, which has $\frac { \tau } { s }$ as its left son.

()Every reduced fraction appears exactly once.

The argument is similar. If $\textstyle { \frac { r } { s } }$ appears more than once, then $r \neq s .$ since any node in the tree except the top is of the form $\textstyle { \frac { i } { i + j } } < 1$ or $\textstyle { \frac { i + j } { j } } > 1$ But if $r > s$ or $r \textless s$ , then we argue by induction as before.

Every positive rational appears therefore exactly once in our tree, and we may write them down listing the numbers level-by-level from left to right. This yields precisely the initial segment shown above.

(4) The denominator of the $n$ -th fraction in our list equals the numerator of the $( \eta + 1 )$ -st.

This is certainly true for $n = 0$ , or when the $\pmb { n }$ -th fraction is a left son. Suppose the $n$ -th number $\frac { \triangledown \mathit { \Pi } _ { \mathit { \Pi } } ^ { \prime } } { s }$ is a right son. If $\frac { r } { s }$ is at the right boundary, then $s = 1$ , and the successor lies at the left boundary and has numerator 1. Finally, if $\boldsymbol { \underline { { \underline { { r } } } } }$ is in the interior, and $\frac { r ^ { \prime } } { s ^ { \prime } }$ is the next fraction in our sequence, then $\frac { \mathbf { r } } { \pmb { \mathscr { s } } }$ is the right son of ${ \frac { \mathfrak { r } - s } { s } } , ~ { \frac { \mathfrak { r ^ { \prime } } } { \mathfrak { s ^ { \prime } } } }$ is the left son of sr, and by induction the denominator of $\frac { \underline { { \boldsymbol { r } } } - \underline { { \boldsymbol { s } } } } { \underline { { \boldsymbol { s } } } }$ is the numerator of s−r1 , so we get s = rl.

Well, this is nice, but there is even more to come. There are two natural questions:

Does the sequence $\left( b ( n ) \right) _ { n \geq 0 }$ have a"eanng?That  d $b ( \eta _ { l } )$ count anything simple?

- Given $\frac { \cdot \mathbf { r } } { s }$ , is there an easy way to determine the successor in the listing?

\$\frac{ { 1 }\$ \$\fac{2\$ A A A A

T= a\$ r' s \$\^r1}\$

For example, $h ( 6 ) = 3$ , with the hyper  
binary representations   
$\begin{array} { l } { 6  4 + 2 } \\ { \{  4 + 1 + 1 }  \\ { 6 = 2 + 2 + 1 + 1 . } \end{array}$

To answer the first question, we work out that the node $b ( n ) / b ( n , + 1 )$ has the two sons $b ( 2 \eta + 1 ) / { b ( 2 \eta + 2 ) }$ and $b ( 2 n + 2 ) / b ( 2 r \} + 3 )$ .By the set-up of the tree we obtain the recursions

$$
b ( 2 n + 1 ) = b ( n ) \quad { \mathrm { a n d } } \quad b ( 2 n + 2 ) = b ( n ) + b ( n + 1 ) .
$$

With $b ( 0 ) = 1$ the sequence $( b ( r _ { i } ) ) _ { r _ { i } \geq 0 }$ is completely determined by (1).

So, is there a "nice" "known" sequence which obeys the same recursion? Yes, there is. We know that any number n can be uniquely written as a sum of distinct powcrs of 2 — this is the usual binary representation of $n$ . A hyper-binary representation of $\mathscr { n }$ is a representation of $\gamma _ { l }$ a sum of powers of 2, where every power $2 ^ { k }$ appears at most twice. Let $h ( \eta )$ be the number of such representations for $n$ . You are invited to check that the sequence $h ( n )$ obeys the rccursion (1), and this gives $\mathfrak { b } ( \gamma _ { \mathfrak { k } } ) = \mathfrak { h } ( \mathfrak { n } )$ for all $n$ .

Incidentally, we have proved a surprising fact: Let $\frac { r } { s }$ be a reduced fraction, there exists precisely one integer $\pmb { \eta } _ { e }$ with $r = h ( r )$ and $s = \hbar ( \eta , + 1 )$ .

Let us look at the second question. We have in our tree

![](images/02b3b5c58b627702b8ed5ab436c01049caf7240fb165fafda06290fb9b964d8c.jpg)

$x : = \frac { r } { s }$

![](images/bf3da37ad572cc52d9df5cccfd670f92ffcfe444048ff55991c70ca87eff9543.jpg)

We now use this to gencrate an even larger infinite binary tree (without a root) as follows:

![](images/35609af428217ea4d77315b68722e0a4f0cdd10194064fad1abd8c0f289dcfc4.jpg)

In this trec all rows are equal, and they all display the Calkin-Wilf listing of the positive rationals (starting with an additional $\frac { \harpoonright } { \mathbf { l } }$ ).

So how does one get from one rational to the next? To answer this, we first record that for every rational $\vec { x }$ its right son is $x + 1$ , the right grand-son is $x + 2$ , so the $k$ -fold right son is $x + k$ Similarly, the left son of $_ x$ is $\frac { x } { 1 + x }$ whose left son is an o The ol $\frac { x } { 1 + k x }$

Now to find how to get from $\frac { \texttt { r } } { s } = \texttt { r }$ to the "next" rational $f ( x )$ in the listing, we have to analyze the situation depicted in the margin. In fact, if we consider any nonnegative rational number $\boldsymbol { \mathscr { x } }$ in our infinite binary tree, then it is the $k$ -fold right son of the left son of some rational $y \geq 0$ (for some $k \geq 0 )$ , while $f ( x )$ is given as the $k$ -fold left son of the right son of the same $y$ Thus with the formulas for $k$ -fold left sons and $k$ -fold right sons, we get

$$
z = { \frac { y } { 1 + y } } + k .
$$

as claimed in the figure in the margin. Here $k = \lfloor x \rfloor$ is the integral part of $x$ while $\frac { y } { 1 + y } = \{ x \}$

$$
f ( x ) = { \frac { y + 1 } { 1 + k ( y + 1 ) } } = { \frac { 1 } { { \frac { 1 } { y + 1 } } + k } } = { \frac { 1 } { k + 1 - { \frac { y } { y + 1 } } } } = { \frac { 1 } { \lfloor x \rfloor + 1 - \{ x \} } } .
$$

Thus we have obtained a beautiful formula for the successor $f ( x )$ of $\boldsymbol { x }$ . found very recently by Moshe Newman:

The function

$$
x \longmapsto f ( x ) = { \frac { 1 } { \lfloor x \rfloor + 1 - \{ x \} } }
$$

generates the Calkin-Wilf sequence

$$
{ \begin{array} { l } { { \frac { 1 } { 1 } } \mapsto { \frac { 1 } { 2 } } \mapsto { \frac { 2 } { 1 } } \mapsto { \frac { 1 } { 3 } } \mapsto { \frac { 3 } { 2 } } \mapsto { \frac { 3 } { 2 } } \mapsto { \frac { 2 } { 3 } } \mapsto { \frac { 3 } { 1 } } \mapsto { \frac { 1 } { 4 } } \mapsto { \frac { 4 } { 3 } } \mapsto { \frac { 4 } { 5 } } \mapsto \cdots . } \end{array} }
$$

which contains every positive rational number exactly once.

The Calkin-Wilf-Newman way to enumerate the positive rationals has a number of additional remarkable properties. For example, one may ask for a fast way to determine the $\mathfrak { N } _ { \ell }$ -th fraction in the sequence, say for $\boldsymbol { \mathscr { n } } = 1 0 ^ { 6 }$ . Here it is:

To find the $\gamma _ { i }$ -th fraction in the Calkin-Wilf sequence, express $\mathcal { n }$ as a binary number ${ \mathfrak { n } } = ( b _ { \mathsf { k } } . b _ { \mathsf { k } - 1 } . . . b _ { 1 } b _ { 0 } ) _ { 2 }$ , and then follow the path in the Calkin-Wilf tree that is determined by its digits, starting at $\begin{array} { r } { \frac { s } { t } = \frac { 0 } { 1 } } \end{array}$ . Here $b _ { i } = 1$ means "take the right son," that is, "add the denominator to the numerator," while $\boldsymbol { \dot { t } } _ { i } = 0$ means "take the left son," that is, "add the numerator to the denominator."

The figure in the margin shows the resulting path for $n = 2 5 = ( 1 1 0 0 1 ) _ { 2 }$ . So the 25th number in the Calkin-Wilf sequence is $\frac { 7 } { 5 }$ The reader could easily work out a similar scheme that computes for a given fraction $\frac { s } { t }$ (the binary representation of) its position $n$ in the Calkin-Wilf sequence.

y y + 1 t 1+y y +k 1k(y+1 \$y}\$

1 m \$\fac { { 2 }\$ -→ \$\frac{{2 }\$ \$\frac { { 2 }\$ of of A 2 A b \$\fr{  }\$

Let us move on to the real numbers R. Are they still countable? No, they are not, and the means by which this is shown — Cantor's diagonalization method — is not only of fundamental importance for all of set theory, but certainly belongs into The Book as a rare stroke of genius.

Theorem 2. The ser R of real numbers is not countable.

Proof. Any subset $N$ of a countable set $M \ - \ \{ \eta \} _ { 1 } , m _ { 2 } , \eta n _ { 3 } , . . . \}$ is at most countable (that is, finite or countable). In fact, just list the elements of $N$ as they appear in $M$ Accordingly, if we can find a subset of $\mathbb { R }$ which is not countable, then a fortiori $\mathbb { R }$ cannot be countable. The subset $M$ of $\mathbb { R }$ we want to look at is the interval $( 0 , 1 ]$ of all positive real numbers $r$ with $0 ~ \leq ~ r ~ \leq ~ 1$ . Suppose, to the contrary, that $M$ is countable, and let $M = \{ r _ { 1 } , r _ { 2 } , r _ { 3 } , . . . \}$ be a listing of $M$ . We write $r _ { \pi }$ as its unique infinite decimal expansion without an infinite sequence of zeros at the end:

$$
r _ { n } = 0 . a _ { \cdot n 1 } a _ { \cdot n 2 } a _ { \cdot n 3 } { \ldots }
$$

where $a _ { n i } \in \{ 0 , 1 , \ldots , 9 \}$ for all $\mathfrak { n }$ and $i$ . For example, $0 . 7 = 0 . 6 9 9 9 . .$ Consider now the doubly infinite array

$$
\begin{array} { r c l } { { r _ { 1 } } } & { { = } } & { { 0 . a _ { 1 1 } a _ { 1 2 } a _ { 1 3 } . . . } } \\ { { } } & { { } } & { { } } \\ { { r _ { 2 } } } & { { = } } & { { 0 . a _ { 2 1 } a _ { 2 2 } a _ { 2 3 } . . . } } \\ { { } } & { { } } & { { } } \\ { { \vdots } } & { { } } & { { \vdots } } \\ { { r _ { n } } } & { { = } } & { { 0 . a _ { n 1 } a _ { n 2 } a _ { n 3 } . . . } } \\ { { } } & { { } } & { { } } \\ { { \vdots } } & { { } } & { { \vdots } } \end{array}
$$

![](images/7683e5d65f14665f39e988eab1a62335854917287faff20f84274efabe621869.jpg)  
A bijective $f : ( 0 , 1 ] \longrightarrow ( 0 , 1 )$

For every $\pmb { \eta } _ { \pmb { \imath } }$ ,choose $\mathfrak { b } _ { n } \in \{ 1 , \ldots , 8 \}$ different from $a _ { \mathfrak { n } \mathfrak { n } }$ ; clearly this can be done. Then $\dot { b } = 0 . b _ { 1 } b _ { 2 } b _ { 3 } . . . b _ { n } . . .$ is a real number in our set $M$ and hence must have an index, say $\boldsymbol { b } = r _ { \boldsymbol { k } }$ . But this cannot be. since $b _ { k }$ is different from $a _ { k k }$ . And this is the whole proof!

Let us stay with the real numbers for a moment. We note that all four types of intervals $( 0 , 1 ) , ( 0 , 1 ] , [ 0 , 1 )$ and [0, 1] have the same size. As an example, we verify that $( 0 , 1 ]$ and $( 0 , 1 )$ have equal cardinality. The map $f : ( 0 , 1 ] \longrightarrow ( 0 , 1 ) , x \longmapsto y$ defined by

$$
y : = \left\{ \begin{array} { c l l } { \frac { 3 } { 2 } - x } & { \mathrm { f o r } } & { \frac { 1 } { 2 } < x \leq 1 , } \\ { \frac { 3 } { 4 } - x } & { \mathrm { f o r } } & { \frac { 1 } { 4 } < x \leq \frac { 1 } { 2 } , } \\ { \frac { 3 } { 8 } - x } & { \mathrm { f o r } } & { \frac { 1 } { 8 } < x \leq \frac { 1 } { 4 } , } \\ { \vdots } \end{array} \right.
$$

does the job. Indeed, the map is bijective, since the range of $y$ in the first line is $\frac { 1 } { 2 } \leq y < 1$ , in the second line $\frac { 1 } { 4 } \leq y < \frac { 1 } { 2 }$ ,in the third line $\frac { 1 } { 8 } \leq y < \frac { 1 } { 4 }$ and so on.

Next we find that any two intervals (of finite length $> 0 1$ have equal size by considering the central projection as in the figure. Even more is true: Every interval (of length $\geq 0$ ) has the same size as the whole real line $\mathbb { R }$ . To see this, look at the bent open interval (0, 1) and project it onto $\mathbb { R }$ from the center $S$ .

So, in conclusion, any open, half-open, closed (finite or infinite) interval of length $> 0$ has the same size, and we denote this size by $c$ ,where $c$ stands for continuum (a name sometimes used for the interval [0, 1 ]).

That finite and infinite intervals have the same size may come expected on second thought, but here is a fact that is downright counter-intuitive.

Theorem 3. The sel $\mathbb { R } ^ { 2 }$ of all ordered pairs of real numbers (that is, the real plane) has the same size as $\mathbb { R }$ .

Proof. To see this, it suffices to prove that the set of all pairs $( x , y )$ $0 < x , y \le 1$ , can be mapped bijectively onto $( 0 , 1 ]$ The proof is again from The Book. Consider the pair $( x , y )$ and write $x , y$ in their unique non-terminating decimal expansion as in the following example:

$$
\begin{array} { r l r } { x } & { { } - } & { 0 . 3 \quad \quad 0 1 \quad \quad 2 \quad \quad 0 0 7 \quad \quad 0 8 \quad \ldots } \\ { y } & { { } = } & { 0 . 0 0 9 \quad \quad 2 \quad \quad 0 5 \quad \quad 1 \quad \quad 0 0 0 8 \quad \ldots } \end{array}
$$

Note that we have separated the digits of $x$ and $y$ into groups by always going to the next nonzero digit, inclusive. Now we associate to $( x , y )$ the number $z \in \ \{ 0 , 1 \}$ by writing down the first $x$ -group, after that the first $1 1$ -group, then the second $x ^ { 2 }$ -group, and so on. Thus, in our example, we obtain

$$
z \ = \ 0 . 3 0 0 9 0 1 2 2 0 5 0 0 7 1 0 8 0 0 0 8 \ldots .
$$

Since neither $x$ nor $y$ exhibits only zeros from a certain point on, we find that the expression for $\mathcal { Z }$ is again a non-terminating decimal expansion. Conversely, from the expansion of $\vec { \mathcal { S } }$ we can immediately read off the preimage $( x , y )$ , and the map is bijective — end of proof.

As $( x , y ) \longmapsto x + i y$ is a bijection from $\mathbb { R } ^ { 2 }$ onto the complex numbers $\mathbb { C }$ . we conclude that $| \mathbb { C } | = | \mathbb { R } | - i$ Why is the result $| \mathbb { R } ^ { 2 } | = | \mathbb { R } |$ so unexpected? Because it goes against our intuition of dimension. It says that the 2-dimensional plane $\mathbb { R } ^ { 2 }$ (and, in general, by induction, the $\gamma _ { \ell }$ -dimensional space $\mathbb { R } ^ { \eta _ { i } }$ ) can be mapped bijectively onto the 1-dimensional line $\mathbb { R }$ .Thus dimension is not generally preserved by bijective maps. If, however, we require the map and its inverse to be continuous, then the dimension is preserved, as was first shown by Luitzen Brouwer.

Let us go a little further. So far, we have the notion of equal size. When will we say that $M$ is at most as large as $N ^ { i }$ Mappings provide again the key. We say that the cardinal number $\mathbf { m }$ is less than or equal to n, if for sets $M$ and $N$ with $| M | = m$ , $| N | = \bar { n }$ , there exists an injection from $M$ into $N$ . Clearly, the relation $\mathfrak { m } \leq \mathfrak { n }$ is independent of the representative sets $1 1 ^ { f }$ and $N$ chosen. For finite sets this corresponds again to our intuitive notion: An m-set is at most as large as an $\gamma _ { i }$ -set if and only if $m \leq n$ .

![](images/97f2b645006f3af7d0f38bc8db8ed408ed50541a958895fbf2f7878d8d78c69f.jpg)  
R

![](images/037afdd468b616ba9feaf9f425aec2b039f075e2b05a82e4adc5882c6359e19e.jpg)

Now we are faced with a basic problem. We would certainly like to have that the usual laws concerning inequalities also hold for cardinal numbers. But is this true for infinite cardinals? In particular, is it true that ${ \mathfrak { m } } \leq { \mathfrak { n } }$ . ${ \mathfrak { n } } \leq { \mathfrak { m } }$ imply $\mathfrak { m } = \mathfrak { n } ?$ This is not at all obvious: We are given infinite sets $1 1$ and $\mathcal { N }$ as well as maps $f : \mathcal { M } \longrightarrow N$ and $g : N \longrightarrow M$ that are injective but not necessarily surjective. This suggests to construct a bijection by relating some elements $m \in M$ to $f ( m ) \in N$ , and some elements $\mu \in N$ to $g ( \pi ) \in M$ , But it is not clear whether the many possible choices can be made to "fit together."

The affirmative answer is provided by the famous Schröder-Bernstein theorem, which Cantor announced in 1883. The first proofs were given by Friedrich Schröder and Felix Bernstein quite some time later. The following proof appears in a litle book by one of the twentieth century giants of sel theory, Paul Cohen, who is famous for resolving the continuum hypothesis (which we will discuss below).

![](images/1116b572e49a7ffaf227e536e46d440615e03d34e6d20619e4fa15c7dfea50ee.jpg)

![](images/ea78543f8461c924ffaa3c647ed8b8e30ad435e09958db4fb199e4e6ba8f7659.jpg)

Theorem 4. If each of two sets $M$ and $N$ can be mapped injectively into the other, then there is a bijection from $M$ to $N$ , that is, $| M | = | N |$ .

Proof. We may certainly assume that $M$ and $N$ are disjoint — if not, then we just replace $N$ by a new copy.

Now $f$ and $g$ map back and forth between the elements of $M$ and those of $N$ . One way to bring this potentially confusing situation into perfect clarity and order is to align $M \cup N$ into chains of elements: Take an arbitrary element $m _ { 0 } \in M$ , say, and from this generate a chain of elements by applying $f$ , then $g$ , then $f$ again, then $g .$ , and so on. The chain may close up (this is Case 1) if we reach $m _ { 0 }$ again in this process, or it may continue with distinct elements indefinitely. (The first "duplicate" in the chain cannot be an element different from $m _ { 0 }$ , by injectivity.)

If the chain continues indefinitely, then we try to follow it backwards: From $m _ { 0 }$ to $g ^ { - 1 } ( \eta _ { \ell | } ) \big )$ if $m _ { 0 }$ is in the image of $g$ , then to $f ^ { - 1 } ( \boldsymbol { y } ^ { - 1 } ( \gamma \boldsymbol { r } _ { i \bar { 0 } } ) )$ if $y ^ { - 1 } ( r r _ { 0 } )$ is in the image of $f$ , and so on. Three more cases may arise here: The process of following the chain backwards may go on indefinilely (Case ), it may stop in an element of $M$ that does not lie in the image of $\boldsymbol { \vartheta }$ (Case 3), or it may stop in an element of $N$ that docs not lie in the image of $f$ (Case 4).

Thus $M \subset N$ splits perfectly into four types of chains, whose elements we may labcl in such a way that a bijection is simply given by putting $F : { \mathit { r n } } _ { i } \longmapsto { \mathit { r n } } _ { i }$ .We verify this in the four cases separately:

Case 1. Finite cycles on $2 k + 2$ distinct elements $( k \geq 0 )$

Case 2. Two-way infinite chains of distinct elements

$$
\therefore  m _ { 0 } \xrightarrow { f } n _ { 0 } \xrightarrow { g } m _ { 1 } \xrightarrow { f } n _ { 1 } \xrightarrow { g } m _ { 2 } \xrightarrow { f } m _ { 2 } \cdots
$$

Case 3. The onc-way infinite chains of distinct elements that start at the elements $m _ { 0 } \in M \backslash g ( N )$

$$
m _ { 0 } \xrightarrow [ \hdots ] { f } n _ { 0 } \xrightarrow [ \hdots ] { g } m _ { 1 } \xrightarrow [ \hdots ] { f } n _ { 1 } \xrightarrow [ \hdots ] { g } m _ { 2 } \xrightarrow [ \hdots ] { f } \quad \dots
$$

Case 4. The one-way infinite chains of distinct elements that start at the elements $r _ { 0 } \in N \backslash f ( M )$

$$
n _ { 1 1 } \stackrel { g } { \longrightarrow } m _ { 0 } \stackrel { f } { \longrightarrow } n _ { 1 } \stackrel { g } { \longrightarrow } m _ { 1 } \stackrel { f } { \longrightarrow }
$$

What about the other relations governing inequalities? As usual, we set ${ \mathfrak { m } } < { \mathfrak { n } }$ if ${ \mathfrak { m } } \leq { \mathfrak { n } }$ , but $\mathfrak { m } \ne \mathfrak { n }$ . We have just seen that for any two cardinals $\mathfrak { m }$ and $\pmb { \nmid }$ at most one of the three possibilities

$$
{ \mathfrak { m } } < { \mathfrak { n } } , { \mathfrak { m } } = { \mathfrak { n } } , { \mathfrak { m } } > { \mathfrak { n } }
$$

holds, and it follows from the theory of cardinal numbers that, in fact, precisely one relation is true. (See the appendix to this chapter, Proposition 2.) Furthermore, the Schröder-Bernstein Theorem tells us that the relation $<$ is transitive, that is, ${ \mathfrak { m } } < { \mathfrak { n } }$ and ${ \textbf { n } } < { \mathfrak { p } }$ imply ${ \mathfrak { m } } < { \mathfrak { p } }$ .Thus the cardinalities are arranged in linear order starting with the finite cardinals $0 , 1 , 2 , 3 , \ldots$ Invoking the usual Zermelo-Fraenkel axiom system (in particular, the axiom of choicc) we easily find that any infinite sct $M$ contains a countable subset. In fact, $\Lambda f$ contains an element, say $m _ { 1 }$ . The set $M \backslash \{ m _ { 1 } \}$ is not empty (since it is infinite) and hence contains an element $m _ { 2 }$ Considering $M \setminus \{ r r _ { 1 } , m _ { 2 } \}$ we infer the existence of $m _ { \mathrm { 4 } }$ , and so on. So, the size of a countable set is the smallest infinite cardinal, usually denoted by $\aleph _ { 0 }$ (pronounced "aleph zero").

![](images/1836321a50cc6edbdd7d33d86b52da3f62c6fba159b57843564bdbb271daa335.jpg)  
"The smallest infinite cardinal"

With this we have also proved a result announced earlier:

Every infinite set has the same size as some proper subset.

As a corollary to $\aleph _ { 0 } \leq m$ for any infinite cardinal m, we can immediately prove "Hilbert's hotel" for any infinite cardinal number $\mathfrak { m }$ , that is, we have $| M \cup \{ x \} \} | = | M \}$ for any infinite set $M$ . Indeed, $M$ contains a subset $N = \{ m _ { 1 } , m _ { 2 } , m _ { 3 } , . . . \}$ Now map $x$ onto $m _ { 1 } , ~ m _ { 1 }$ onto $m _ { 2 }$ , and so on, keeping the elements of $M \backslash N$ fixed. This gives the desired bijection.

As another consequence of the Schröder-Bernstein theorem we may prove that the set ${ \mathcal { P } } \{ \mathbb { N } \}$ of all subsets of $\mathbb { N }$ has cardinality c. As noted above, it suffices to show that $| \mathcal { P } ( \mathbb { N } ) \backslash \{ \emptyset \} | = | ( 0 , 1 ] |$ . An example of an injective map is

$$
f : \mathcal { P } ( \mathbb { N } ) \setminus \{ \emptyset \} \ \longrightarrow \ ( 0 , 1 ] , \qquad A \ \longmapsto \ \sum _ { i \in A } 1 0 ^ { - i } ,
$$

while

$$
\begin{array} { r } { g : ( 0 , 1 ] \longrightarrow \mathcal { P } ( \mathbb { N } ) \setminus \{ \emptyset \} , \qquad 0 . b _ { 1 } b _ { 2 } b _ { 3 } . . . \longmapsto \left\{ b _ { i } 1 0 ^ { i } : i \in \mathbb { N } \right\} } \end{array}
$$

defines an injection in the other direction.

Up to now we know the cardinal numbers $0 , 1 , 2 , \ldots , \aleph _ { 0 }$ , and further that the cardinality $c$ of $\mathbb { R }$ is bigger than $\aleph _ { 0 }$ . The passage from $\mathbb { Q }$ with $| \mathbb { Q } | = \aleph _ { 0 }$ to $\mathbb { R }$ with $| \mathbb { R } | = c$ immediately suggests the next question:

Is $c = | \mathbb { R } |$ the next infinite cardinal number after $\aleph _ { 0 } ?$

Now, of course, we have the problem whether there is a next larger cardinal number, or in other words, whether $\aleph _ { 1 }$ has a meaning at all. It does — the proof for this is outlined in the appendix to this chapter.

The statement $c = \aleph _ { 1 }$ became known as the continuum hypothesis. The question whether the continuum hypothesis is true presented for many decades one of the supreme challenges in all of mathematics. The answer, finally given by Kurt Gödel and Paul Cohen, takes us to the limit of logical thought. They showed that the statement ${ \dot { c } } : \equiv \aleph _ { 1 }$ is independent of the Zermelo-Fraenkel axiom system, in the same way as the parallel axiom is independent of the other axioms of Euclidian geometry. There are models where $c = \aleph _ { 1 }$ holds, and there are other models of set theory where ${ \mathfrak { C } } \neq \aleph _ { 1 }$ holds.

In the light of this fact it is quite interesting to ask whether there are other conditions (from analysis, say) which are equivalent to the continuum hypothesis. Indeed, it is natural to ask for an analysis example, since historically the first substantial applications of Cantor's set theory occurred in analysis, specifically in complex function theory. In the following we want to present one such instance and its extremely elegant and simple solution by Paul Erdós. In 1962, Wetzel asked the following question:

Let $\{ \{ \alpha \}$ be a family of pairwise distinct analytic functions on the complex numbers such that for each $z \in \mathbb { C }$ the set of values $\{ f _ { \alpha } ( z ) \}$ is at most countable (that is, it is either finite or countable); let us call this property $( P _ { 0 } )$ .

Does it then follow that the family itself is at most countable?

Very shortly afterwards Erdôs showed that, surprisingly, the answer depends on the continuum hypothesis.

Theorem 5. $f c > \aleph _ { \ I }$ , then every family $\{ f _ { \alpha } \}$ satisfying $( P _ { 0 } )$ is countable. $I f .$ on the other hand, $c = \aleph _ { 1 }$ , then there exists some family $\{ f _ { \alpha } \}$ with $p r o p e r t y : ( P _ { 0 } )$ which has size c.

For the proof we need some basic facts on cardinal and ordinal numbers. For readers who are unfamiliar with these concepts, this chapter has an appendix where all the necessary results are collected.

Proof of Theorem 5. Assume first $r ; \aleph _ { 1 }$ .We shall show that for any family $\{ f _ { \alpha } \}$ of size $\aleph _ { 1 }$ of analytic functions there exists a complex number $z _ { 0 }$ such that all $\aleph _ { 1 }$ values $f _ { \alpha } ( z _ { 0 } )$ are distinct. Consequently, if a family of functions satisfies $( P _ { 0 } )$ , then it must be countable.

To see this, we make use of our knowledge of ordinal numbers. First, we well-order the family $\{ f _ { \alpha } \}$ according to the initial ordinal number $\omega _ { \mathrm { l } }$ of $\aleph _ { 1 }$ . This means by Proposition I of the appendix that the index set runs through all ordinal numbers $\alpha$ which are smaller than $\omega _ { 1 }$ . Next we show that the set of pairs $( \alpha , \beta )$ , $\alpha < \beta < \omega _ { 1 }$ , has size $\aleph _ { 1 }$ Since any $\beta < \omega _ { 1 }$ is a countable ordinal, the set of pairs $( \alpha , \beta ) , \alpha < \beta$ , is countable for every fixed $\beta$ Taking the union over all $\aleph _ { 1 }$ -many $\beta$ , we find from Proposition 6 of the appendix that the set of all pairs $( \alpha , \beta ) , \alpha < \beta$ , has size $\aleph _ { 1 }$ .

Consider now for any pair $\alpha < \beta$ the set

$$
S ( \alpha , \beta ) = \{ z \in \mathbb { C } : f _ { \alpha } ( z ) = f _ { \beta } ( z ) \} .
$$

We claim that each set $S ( \alpha , \beta )$ is countable. To verify this, consider the disks $C _ { k }$ of radius $k = 1 , 2 , 3 , . . ,$ around the origin in the complex plane. If $f _ { x }$ and $f _ { \beta }$ agree on infinitely many points in some $C _ { k }$ , then $f _ { \alpha }$ and $f _ { j }$ are identical by a well-known result on analytic functions. Hence $f _ { \alpha }$ and $f _ { \beta }$ agrce only in finitely many points in each $C _ { k }$ , and hence in at most countably many points altogether. Now we set $\begin{array} { r } { \bar { S } : = \bigcup _ { \alpha < \beta } \bar { S } ( \alpha , \beta ) } \end{array}$ Again by Proposition 6, we find that $S$ has size $\aleph _ { 1 }$ , as each set $S ( x , \beta )$ is countable. And herc is the punch line: Because, as we know, $\mathbb { C }$ has size $c$ ,and $c$ is larger than $\aleph _ { 1 }$ by assumption, there exists a complex number $z _ { 0 }$ not in $S$ . and for this $z _ { \mathrm { 0 } }$ all $\aleph _ { 1 }$ values $f _ { \alpha } ( z _ { 0 } )$ are distinct.

Next we assume ${ c } = \aleph _ { 1 }$ . Consider the set $D \subseteq \mathbb { C }$ of complex numbers $\gamma + i \gamma _ { l }$ with rational real and imaginary part. Since for each $p$ the set $\{ \chi \} + i q : q \in \mathbb { Q } \}$ is countable, we find that $D$ is countable. Furthermore, $D$ is a dense set in $\mathbb { C }$ : Every open disk in the complex plane contains some point of $D$ . Let $\{ z _ { \alpha } : 0 \leq \alpha < \omega _ { 1 } \}$ be a well-ordering of $\mathbb { C }$ We shall now construct a family $\{ f _ { i ^ { 3 } } : 0 \leq \beta < \omega _ { 1 } \}$ of $\aleph _ { 1 }$ -many distinct analytic functions such that

$$
f _ { \beta } ( z _ { \alpha } ) \in D \mathrm { w h e n e v e r } \alpha < \beta .
$$

Any such family satisfies the condition $( l _ { 0 } )$ . Indeed, each point $z \in \mathbb { C }$ has some index, say $z = z _ { \alpha }$ .Now, for all $\beta > \alpha$ , the values $\{ f _ { \beta } ( z _ { \alpha } ) \}$ lie in the countable set $D$ Since $\alpha$ is a countable ordinal number, the functions $f _ { \beta }$ with $j \le \alpha$ will contribute at most countably further values $f _ { \beta } ( z _ { \alpha } )$ ,so that the set of all values $\{ f _ { \beta } ( z _ { \alpha } ) \}$ is likewise at most countable. Hence, if we can construct a family $\{ f _ { i } \} \}$ satisfying (1), then the second part of the theorem is proved.

The construction of $\{ f _ { i } \}$ is by transfinite induction. For $f _ { \parallel }$ we may take any analytic function, for example $f _ { 0 } =$ constant. Suppose $f _ { \beta }$ has already been constructed for all $\beta < \gamma$ Since $\gamma$ is a countable ordinal, we may reorder $\{ f _ { \beta } : 0 \le \beta < \gamma \}$ into a sequence $g _ { 1 } , \ P _ { 2 } , \ P _ { 3 } , \ldots .$ The same reordering of $\{ z _ { \alpha } : 0 \leq c \kappa < \gamma \}$ yields a sequence $w _ { 1 } , \ i , \ i , \ i , \ i , \dots$ .. We shall now construct a function $f _ { \gamma }$ satisfying for each $\gamma \smash { \ v { j } _ { \perp } }$ the conditions

$$
f _ { \gamma } ( w _ { n } ) \in D \qquad \mathrm { a n d } \qquad f _ { \gamma } ( w _ { n } ) \neq g _ { n } ( w _ { n } ) .
$$

The second condition will ensure that all functions $f _ { \gamma }$ $( 0 \leq \gamma < \omega _ { 1 } )$ are distinct, and the first condition is just (1), implying $( l _ { 0 } ^ { 2 } )$ by our previous argument. Notice that the condition $f _ { \gamma } ( w _ { n } ) \ne g _ { n } ( w _ { n } )$ is once more a diagonalization argument.

To construct $f _ { \gamma }$ , we write

$$
\begin{array} { r l r } { f _ { \gamma } ( z ) } & { : = } & { \varepsilon _ { 0 } + \varepsilon _ { 1 } \big ( z - w _ { 1 } \big ) + \varepsilon _ { 2 } \big ( z - w _ { 1 } \big ) \big ( z - w _ { 2 } \big ) } \\ & { } & { + \varepsilon _ { 3 } \big ( z - w _ { 1 } \big ) \big ( z - w _ { 2 } \big ) \big ( z \cdots w _ { 3 } \big ) + \dots . . . } \end{array}
$$

If $\gamma$ is a finite ordinal, then $f _ { \gamma }$ is a polynomial and hence analytic, and we can certainly choose numbers $\varepsilon _ { i }$ such that (2) is satisfied. Now suppose $\gamma$ is a countable ordinal, then

$$
f _ { \gamma } ( z ) ~ = ~ \sum _ { n = 0 } ^ { \infty } \varepsilon _ { n } ( z - w _ { 1 } ) \cdot \cdot \cdot ( z - w _ { n } ) .
$$

Note that the values of $\varepsilon _ { m }$ $( m \ge n )$ have no influence on the value $\textstyle { \int _ { \gamma } \left( w _ { n } \right) }$ , hence we may choose the $\varepsilon _ { \pi }$ step by step. If the sequence $( \varepsilon _ { \pi } )$ converges to 0 sufficiently fast, then (3) defines an analytic function. Finally, since $D$ is a dense set, we may choose this sequence $( \sum \pi )$ so that $f _ { \gamma }$ meets the requirements of (2), and the proof is complete. □

"A legend talks about St. Augustin who, walking along the seashore and contemplating infinity, saw a child trying to empty the ocean with a small shell...\*

# Appendix: On cardinal and ordinal numbers

Let us first discuss the question whether to each cardinal number there exists a next larger one. As a start we show that to every cardinal number m there always is a cardinal number n larger than m. To do this we employ again a version of Cantor's diagonalization method.

Let $1 1 1$ be a set, then we claim that the set $P ( M )$ of all subsets of $M$ has larger size than $M$ By letting $m \in M$ correspond to $\{ \gamma \} \ U \backslash \Sigma ^ { } \{ \mathcal { M } \} ,$ we see that $M$ can be mapped bijectively onto a subset of $P ( M )$ , which implies $| { \cal M } | \le | { \cal P } ( { \cal M } ) |$ by definition. It remains to show that $P ( M )$ can not be mapped bijectively onto a subset of $M$ Suppose, on the contrary, $\varphi : { \cal N } \longrightarrow { \mathcal { P } } ( M )$ is a bijection of $N \subseteq M$ onto $\mathcal { P } ( M )$ Consider the subset ${ U } _ { \cdot } ^ { \textsf { F } } \subseteq N$ of all elements of $N$ which are not contained in their image under $\varphi$ , that is, $U = \{ m \in N : m \notin \varphi ( m ) \}$ . Since $\varphi$ is a bijection, there exists $u \in N$ with $\varphi ( u ) = U$ Now, either $u \in U$ or $u \notin U$ , but both alternatives are impossible! Indeed, if $u \in U$ , then $u \notin \varphi ( u ) = U$ by the definition of $[ \zeta$ , and if $u \not \in U \not = \varphi ( u )$ , then $u , \in U$ , contradiction.

Most likely, the reader has seen this argument before. It is the old barber riddle: "A barber is the man who shaves all men who do not shave themselves. Does the barber shave himself?"

To get further in the theory we introduce another great concept of Cantor's, ordered sets and ordinal numbers. A set $\lambda \mathcal { I }$ is ordered by $\nless$ if the relation $<$ is transitive, and if for any two distinct elements $a$ and $b$ of $M$ we either have $a < b$ or $\smash { b < a }$ . For example, we can order $\mathbb { N }$ in the usual way according to magnitude, $\mathbb { N } = \{ 1 , 2 , 3 , 4 , \dots \}$ , but, of course, we can also order $\mathbb { N }$ the other way round, $\mathbb { N } = \{ \dots , \dots 4 , 3 , 2 . 1 \}$ , or $\mathbb { N } = \{ 1 , 3 , 5 . . . , 2 , 4 , 6 , . . . \}$ by listing first the odd numbers and then the even numbers.

Ilere is the seminal concept. An ordered set $M f$ is called well-ordered if every nonempty subset of $\Lambda I$ has a first element. Thus the first and third orderings of $\mathbb { N }$ above are well-orderings, but not the second ordering. The fundamental well-ordering theorem, implied by the axioms (including the axiom of choice), now states that every set $M$ admits a well-ordering. From now on, we only consider sets endowed with a well-ordering.

Let us say that two well-ordered sets $\Lambda \prime$ and $N$ are similar (or of the same order-type) if there exists a bijection $\varphi$ from $M$ on $N$ which respects the ordering, that is, $\gamma \gamma _ { \normalfont } < \gamma _ { \normalfont i } , \ r _ { \normalfont i }$ implies $\varphi ( m ) < _ { N } \varphi ( n )$ .Note that any ordered set which is similar to a well-ordered set is itself well-ordered.

Similarity is obviously an equivalence relation, and we can thus speak of an ordinal number $\alpha$ belonging to a class of similar sets. For finite sets, any two orderings are similar well-orderings, and we use again the ordinal number $n$ for the class of $\boldsymbol { n }$ -sets. Note that, by definition, two similar sets have the same cardinality. Hence it makes sense to speak of the cardinality $\left| \alpha \right|$ of an ordinal number $\alpha$ . Note further that any subset of a well-ordered set is also well-ordered under the induced ordering.

As we did for cardinal numbers, we now compare ordinal numbers. Let $\it { \Omega } _ { \it { 1 1 } } \it { \Omega } _ { \it { 1 1 } }$ be a well-ordered set, $\gamma \gamma . \in \Lambda ^ { \prime }$ , then $M _ { m } = \{ x \in M : x < m \}$ is called the (initial) segment of $M$ determined by m; $N$ is a segment of $M$ if $N \mathrm { ~ - ~ } M _ { r \prime k }$ for some $m$ Thus, in particular, $M _ { m }$ is the empty set when $m$ is the first element of $M$ . Now let $\mu$ and $\nu$ be the ordinal numbers of the well-ordered sets $\mathit { 1 1 }$ and $N$ We say that $\mu$ is smaller than $\nu$ , $\mu < \nu$ ,if $M$ is similar to a segment of $N$ . Again, we have the transitive law that $\mu \ll \nu , \nu < \pi$ implies $\mu < \pi$ , since under a similarity mapping a segment is mapped onto a segment.

The well-ordered scts $\mathbb { N } = \{ 1 , 2 , \ 3 , . . . \}$ and $\mathbb { N } = \{ 1 , 3 , 5 , \dots , 2 , 4 , 6 , \dots \}$ are not similar: the first ordering has only onc clement without an immediate predecessor, while the second one has two.

Clearly, for finite sets, $r \nwarrow \ < \ n$ corresponds to the usual meaning. Let us denote by $\omega$ the ordinal number of $\mathbb { N } = \{ 1 , 2 , 3 , 4 , . . . \}$ ordered according to magnitude. By considering the segment $\mathbb { N } _ { \pi + 1 }$ we find $r _ { i } < \omega$ for any finite $n$ Next we see that $w \leq \alpha$ holds for any infinite ordinal

The ordinal number of $\{ 1 , 2 , 3 , \ldots \}$ is smaller than the ordinal number of $\{ 1 , 3 , 5 , \dots , 2 , 4 , 6 , \dots \}$ .

number $\alpha$ . Indeed, if the infinite well-ordered set $M$ has ordinal number $\alpha$ , then $1 1 1$ contains a first element $m _ { 1 }$ , the set $M \backslash \{ r r _ { k 1 } \}$ contains a first element $m _ { 2 }$ , $M \backslash \{ \tau r _ { k 1 } , \tau r _ { k : 2 } \}$ contains a first element $m _ { 3 }$ Continuing in this way, we produce the sequence $m _ { 1 } < m _ { 2 } < m _ { 3 } < \ldots$ in $M$ If $M = \{ r n _ { 1 } , r n _ { 2 } , n _ { 3 } , . . . \}$ , then $M$ is similar to $\mathbb { N }$ , and hence $\alpha = \omega$ .If, on the other hand, $M \backslash \{ m , \eta v _ { 2 } , . . . \}$ is nonempty, then it contains a first element $\gamma _ { l }$ , and we conc!ude that $\mathbb { N }$ is similar to the segment $M _ { m }$ , that is, $u < a$ by definition.

We now state (without the proofs, which are not difficult) three basic results on ordinal numbers. The first says that any ordinal number $\mu$ has a "standard" representative well-ordered set $W _ { \mu }$ .

Proposition 1. $L e t \mu$ be an ordinal number and denote by $W _ { j i }$ the set of ordinal numbers smaller than $\mu$ Then the following holds:

(i) The elements of $W _ { \mu }$ are pairwise comparable.   
(ii) If we order $W _ { \mu }$ according to magnitude, then $W _ { \mu }$ is well-ordered and has ordinal number $\mu$ .

Proposition 2. Any two ordinal numbers $\mu$ and $\nu$ satisfy precisely one of the relations $\mu \leq \nu$ , $\mu = \nu$ , $o r \mu > \nu$ .

Proposition 3. Every set of ordinal numbers (ordered according to magnitude) is well-ordered.

After this excursion to ordinal numbers we come back to cardinal numbers. Let m be a cardinal number, and denote by $\hat { \cal O } _ { \bf m }$ the set of all ordinal numbers $\mu$ with $| { \boldsymbol { \mu } } | = m$ . By Proposition 3 there is a smallest ordinal number $\omega _ { \mathbf { m } }$ in $O _ { m }$ , which we call the initial ordinal number of $\mathbf { m }$ . As an example, $\dot { \omega }$ is the initial ordinal number of $\aleph _ { 0 }$ .

With these preparations we can now prove a basic result for this chapter.

Proposition 4. For every cardinal number m there is a definite next larger cardinal numher.

Proof. We already know that there is some larger cardinal number n. Consider now the set $\kappa$ of all cardinal numbers larger than m and at most as large as n. We associate to each $\pmb { \mathfrak { p } } \in \mathcal { K }$ its initial ordinal number $w _ { p }$ . Among these initial numbers there is a smallest (Proposition 3), and the corresponding cardinal number is then the smallest in $r$ , and thus is the desired next larger cardinal number to m. □

Proposition 5. Let the infinite set $M$ have cardinality $\mathbf { m }$ , and let M be well-ordered according to the initial ordinal number $\omega _ { \mathfrak { m } }$ . Then $M$ has no last element.

Proof. Indeed, if $M$ had a last element $\mathbf { \nabla } ^ { \mathbf { \gamma } } p \mathbf { \gamma } _ { \mathbf { \ell } }$ , then the segment $M _ { \pi \ i }$ would have an ordinal number $\mu < \ w _ { \mm }$ with $| \mu | = m$ , contradicting the definition of $\omega _ { \mathfrak { m } }$ . □

What we finally need is a considerable strenghthening of the result that the union of countably many countable sets is again countable. In the following result we consider arbitrary families of countable sets.

Proposition 6. Suppose $\left\{ A _ { \alpha } \right\}$ is a family of size m of countable sets $A _ { \alpha }$ where m is an infinite cardinal. Then the union $\bigcup _ { \alpha } A _ { \alpha }$ has size at most m.

Proof. We may assume that the sets $A _ { \alpha }$ are pairwise disjoint, since this can only increase the size of the union. Let $M$ with $| M | = \mathfrak { m }$ be the index set, and well-order it according to the initial ordinal number $\omega _ { \mathbf { m } }$ We now replace each $\alpha \in M$ by a countable set $B _ { \alpha } = \left\{ b _ { \alpha 1 } = \alpha , b _ { \alpha 2 } , b _ { \alpha 3 } , . . . \right\}$ , ordered according to $\omega$ , and call the new set $\widetilde { M }$ . Then $\widetilde { M }$ is again wellordered by setting $b _ { \alpha i } < b _ { \beta j }$ for $\alpha < \beta$ and $b _ { \alpha i } < b _ { \alpha j }$ for $i < j$ . Let $\widetilde { \mu }$ be the ordinal number of $\widetilde { M }$ Since $M$ is a subset of $\widetilde { M }$ , we have $\mu \leq \widetilde { \mu }$ by an earlier argument. If $\mu = \widetilde { \mu }$ , then $M$ is similar to $\widetilde { M }$ , and if $\mu < \widetilde { \mu }$ , then $M$ is similar to a segment of $\widetilde { M }$ Now, since the ordering $\omega _ { \mathbf { m } }$ of $M$ has no last element (Proposition 5), we see that $M$ is in both cases similar to the union of countable sets $B _ { \beta }$ , and hence of the same cardinality.

The rest is easy. Let $\varphi : \bigcup B _ { \beta } \longrightarrow M$ be a bijection, and suppose that $\varphi ( B _ { \beta } ) = \{ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } , . . . \}$ . Replace each $\alpha _ { i }$ by $A _ { \alpha _ { i } }$ and consider the union $\bigcup A _ { \alpha _ { i } }$ . Since $\bigcup A _ { \alpha _ { i } }$ is the union of countably many countable sets (and hence countable), we see that $B _ { \beta }$ has the same size as $\bigcup A _ { \alpha _ { i } }$ . In other words, there is a bijection from $B _ { \beta }$ to $\bigcup A _ { \alpha _ { i } }$ for all $\beta$ , and hence a bijection $\psi$ from $\bigcup B _ { \beta }$ to $\bigcup A _ { \alpha }$ . But now $\psi \varphi ^ { - 1 }$ gives the desired bijection from $M$ to $\bigcup A _ { \alpha }$ , and thus $| \bigcup A _ { \alpha } | = \ m$ . □

# References

[1] L. E. J. BROUwER: Beweis der Invarianz der Dimensionszahl, Math. Annalen 70 (1911), 161-165.   
[2] N. CALKIN & H. WILF: Recounting the rationals, Amer. Math. Monthly 107 (2000), 360-363.   
[3] P. COHEN: Set Theory and the Continuum Hypothesis, W. A. Benjamin, New York 1966.   
[4] P. ERDôs: An interpolation problem associated with the continuum hypothesis, Michigan Math. J. 11 (1964), 9-10.   
[5] E. KAMkE: Theory of Sets, Dover Books 1950.   
[6] M. A. STERN: Ueber eine zahlentheoretische Funktion, Journal für die reine und angewandte Mathematik 55 (1858), 193-220.

# In praise of inequalities

Analysis abounds with inequalities, as witnessed for example by the famous book "Incqualities" by Hardy, Littlewood and Pólya. Let us single out two of the most basic inequalities with two applications each, and let us listen in to George Pólya, who was himself a champion of the Book Proof, about what he considers the most appropriate proofs.

Our first inequality is variously attributed to Cauchy, Schwarz and/or to Buniakowski:

Theorem I (Cauchy-Schwarz inequality)

Let $\langle a , b \rangle$ be an inner product on a real vector space $V$ (with the norm ${ \pmb a } | ^ { 2 } : = \langle { \pmb a } , { \pmb a } \rangle _ { , } ^ { * }$ . Then

$$
\begin{array} { r l r } { \langle a , b \rangle ^ { 2 } } & { { } \le } & { { \bf \langle { a } | { \bf { \bar { \Delta } } } | { \bf { b } } | ^ { 2 } } } \end{array}
$$

holds for all vectors $a , b \in V$ , with equality if and only if $\pmb { a }$ and $^ { b }$ are linearly dependent.

Proof. The following (folklore) proof is probably the shortest. Consider the quadratic function

$$
| x a + b | ^ { 2 } = x ^ { 2 } | a | ^ { 2 } + 2 x \langle a , b \rangle + | b | ^ { 2 }
$$

in the variable $x$ We may assume $a \neq 0$ . If $\textbf { \textit { b } } = \lambda \pmb { a }$ , then clearly $\langle { \bf a } , { \pmb b } \rangle ^ { 2 } = \langle { \bf a } | ^ { 2 } | { \pmb b } | ^ { 2 }$ If, on the other hand, $\pmb { a }$ and $^ { b }$ are linearly independent, then $| x \pmb { \delta } | ^ { 2 } > 0$ for all $\boldsymbol { x }$ , and thus the discriminant $\langle a , b \rangle ^ { 2 } - | a | ^ { 2 } | b | ^ { 2 }$ is less than 0. □

Our second cxample is the inequality of the harmonic, geometric and arithmetic mean:

Theorem II (Harmonic, geometric and arithmetic mean) Let $a _ { 1 } , \dots , a _ { n }$ be positive real numbers, then

$$
\frac { n } { \frac { 1 } { a _ { 1 } } + \ldots + \frac { 1 } { a _ { n } } } \ \leq \ \sqrt [ n ] { a _ { 1 } a _ { 2 } \ldots a _ { n } } \ \leq \ \frac { a _ { 1 } + \ldots + a _ { n } } { n }
$$

with equality in both cases if and only if all $\boldsymbol { \Omega } _ { i }$ 's are equal.

Proof. The following beautiful non-standard induction proof is attributed to Cauchy (see [7]). Let $P ( \eta _ { l } )$ be the statement of the sccond inequality, written in the form

$$
a _ { 1 } a _ { 2 } \ldots a _ { n } \leq { \Big ( } { \frac { a _ { 1 } + \ldots + a _ { n } } { n } } { \Big ) } ^ { n } .
$$

For $\pi = 2$ we have $\begin{array} { r } { a _ { 1 } a _ { 2 } \leq ( \frac { a _ { 1 } + a _ { 2 } } { 2 } ) ^ { 2 } \Longleftrightarrow ( a _ { 1 } - a _ { 2 } ) ^ { 2 } \geq 0 , } \end{array}$ which is true. Now we proceed in the following two steps:

(A) $P ( \pi ) \Longrightarrow P ( \pi - 1 )$ (B) $P ( \pi )$ and $P ( 2 ) \Longrightarrow P ( 2 \eta )$

which will clearly imply the full result.

To prove $( \mathbf { A } )$ , set $A : = \sum _ { k = 1 } ^ { n - 1 } { \frac { \mathfrak { a } _ { k } } { n - 1 } }$ na, then

$$
\Big ( \prod _ { k = 1 } ^ { n - 1 } a _ { k } \Big ) A \stackrel { P ( n ) } { \leq } \Bigg ( \frac { \sum _ { k = 1 } ^ { n - 1 } a _ { k } \ : + \ : A } { n } \Bigg ) ^ { n } \ : = \ : \Big ( \frac { ( n - 1 ) A + A } { n } \Big ) ^ { n } \ : = \ : A ^ { n }
$$

$$
\prod _ { k = 1 } ^ { n - 1 } a _ { k } \ \le \ A ^ { n - 1 } \ = \ \left( \frac { \sum _ { k = 1 } ^ { n - 1 } a _ { k } } { n - 1 } \right) ^ { n - 1 } .
$$

For (B), we see

$$
\begin{array} { r c l } { \displaystyle \prod _ { k = 1 } ^ { 2 n } a _ { k } = \Big ( \displaystyle \prod _ { k = 1 } ^ { n } a _ { k } \Big ) \Big ( \displaystyle \prod _ { k = n + 1 } ^ { 2 n } a _ { k } \Big ) } & { \stackrel { P ( n ) } { \leq } } & { \Big ( \displaystyle \sum _ { k = 1 } ^ { n } \frac { a _ { k } } { n } \Big ) ^ { n } \Big ( \displaystyle \sum _ { k = n + 1 } ^ { 2 n } \frac { a _ { k } } { n } \Big ) ^ { n } } \\ & { P ( 2 ) } & { \displaystyle \sum _ { k = 1 } ^ { 2 n } \frac { a _ { k } } { n } \Big ) ^ { 2 n } = \Bigg ( \displaystyle \sum _ { k = 1 } ^ { 2 n } a _ { k } \Bigg ) ^ { 2 n } . } \end{array}
$$

Th  qal uy.

The left-hand inequality, between the harmonic and the geometric mean, follows now by considering $\frac { 1 } { a _ { 1 } } , \ldots , \frac { 1 } { a _ { n } }$

Another Proof. Of the many other proofs of the arithmetic-geometric mean inequality (the monograph [2] lists more than 50), let us single out a particularly striking one by Alzer which is of recent date. As a matter of fact, this proof yields the stronger inequality

$$
a _ { 1 } ^ { p _ { 1 } } a _ { 2 } ^ { p _ { 2 } } \ldots a _ { n } ^ { p _ { n } } \ \leq \ p _ { 1 } a _ { 1 } + p _ { 2 } a _ { 2 } + \ldots + p _ { n } a _ { n }
$$

for any positive numbers $a _ { 1 } , \ldots , a _ { n } , p _ { 1 } , \ldots , p _ { n }$ with $\sum _ { i = 1 } ^ { \lnot \tau \imath } p _ { i } = 1$ Let us denote the expression on the left side by $G$ , and on the right side by $A$ .We may assume $a _ { 1 } \leq \ldots \leq a _ { n }$ . Clearly $a _ { 1 } \leq \tilde { G } \leq a _ { n }$ , so there must exist some $k$ with $a _ { k } \leq G \leq a _ { k + 1 }$ . It follows that

$$
\sum _ { i = 1 } ^ { k } p _ { i } \int \left( { \frac { 1 } { t } } - { \frac { 1 } { G } } \right) d t \ + \sum _ { i = k + 1 } ^ { n } p _ { i } \intop _ { G } ^ { a _ { i } } \left( { \frac { 1 } { G } } - { \frac { 1 } { t } } \right) d t \ \geq \ 0
$$

since all integrands are $\geq 0$ Rewriting (1) we obtain

$$
\sum _ { i = 1 } ^ { n } p _ { i } \int _ { G } ^ { \frac { a _ { i } } { } } { \frac { 1 } { G } } d t \geq \sum _ { i = 1 } ^ { n } p _ { i } \int _ { G } ^ { \frac { a _ { i } } { } } { \frac { 1 } { t } } d t
$$

where the left-hand side equals

$$
\sum _ { i = 1 } ^ { n } p _ { i } \ : \frac { a _ { i } - G } { G } = \frac { A } { G } - 1 ,
$$

while the right-hand side is

$$
\sum _ { i = 1 } ^ { n } p _ { i } ( \log a _ { i } - \log G ) = \log \prod _ { i = 1 } ^ { n } a _ { i } ^ { p _ { i } } - \log G = 0 .
$$

We conclude $\frac { A } { \mathsf { C } } \mathrm { ~ - ~ } \mathbf { 1 } \mathrm { ~ \geq ~ } 0$ which is $A \ \geq \ G$ In the case of equality, all integrals in (1) must be $0$ , which implies $a _ { 1 } = \ldots = a _ { n } = G$ □

Our rs appicatin is  eiul resul f Laguee e [7]) con the location of roots of polynomials,

TheorSupal ot the p $x ^ { n } + a _ { n , - 1 } x ^ { n - 1 } + \cdot \cdot + a _ { 0 }$ are real. Then the roots are contained in the interval with the endpoints

$$
- \frac { a _ { n - 1 } } { r _ { l } } \pm \frac { n - 1 } { n } \sqrt { a _ { n - 1 } ^ { 2 } - \frac { 2 n } { n - 1 } a _ { n - 2 } } \ .
$$

Proof. Let $y$ be one of the roots and $y _ { 1 } , \ldots , y _ { n - 1 }$ the others. Then the polynomial is $( x \cdot y ) ( x - y _ { 1 } ) \cdot \cdot \cdot ( x \cdot - y _ { n - 1 } )$ Thus by comparing coefficients

$$
\begin{array} { r c l } { - \boldsymbol { a } _ { n \cdot \mathrm { ~ \tiny ~ 1 ~ } } } & { = } & { \boldsymbol { y } + \boldsymbol { y } _ { 1 } + \ldots + \boldsymbol { y } _ { n - 1 } , } \\ { \boldsymbol { a } _ { n - 2 } } & { = } & { \boldsymbol { y } \big ( \boldsymbol { y } _ { 1 } + \ldots + \boldsymbol { y } _ { n - 1 } \big ) + \displaystyle \sum _ { i < j } \boldsymbol { y } _ { i } \boldsymbol { y } _ { j } , } \end{array}
$$

and so

$$
a _ { n - 1 } ^ { 2 } - 2 a _ { n } \ { \mathrm { ~ 2 ~ - ~ } } y ^ { 2 } \ = \ \sum _ { i = 1 } ^ { n - 1 } y _ { i } ^ { 2 } .
$$

By Cauchy's inequality applied to $\left( { y _ { 1 } , \dots , y _ { n - 1 } } \right)$ and $( 1 , \ldots , 1 )$ ,

$$
\begin{array} { r c l } { ( a _ { n - 1 } + y ) ^ { 2 } } & { = } & { ( y _ { 1 } + y _ { 2 } + \ldots + y _ { n - 1 } ) ^ { 2 } } \\ & & { \leq } & { ( n - 1 ) \displaystyle \sum _ { i = 1 } ^ { n - 1 } y _ { i } ^ { 2 } = ( n - 1 ) ( a _ { n - 1 } ^ { 2 } - 2 a _ { n - 2 } - y ^ { 2 } ) , } \end{array}
$$

or

$$
y ^ { 2 } + \frac { 2 a _ { n - 1 } } { n } y + \frac { 2 ( n - 1 ) } { n } a _ { n - 2 } - \frac { n - 2 } { n } a _ { n - 1 } ^ { 2 } \leq 0 .
$$

Thus $y$ (and hence all $y _ { i }$ ) lie between the two roots of the quadratic function, and these roots are our bounds.

For our second application we start from a well-known elementary property of a parabola. Consider the parabola described by $f ( x ) = 1 - x ^ { 2 }$ between $x = - 1$ and $x = 1$ . We associate to $f ( x )$ the tangential triangle and the tangential rectangle as in the figure.

![](images/2ec96246b7ae34f25342e808297592e54dbdebbd9c46aefbbddeaf5fde51c84c.jpg)

We find that the shaded re $\begin{array} { r } { A = \int _ { - 1 } ^ { 1 } ( 1 - x ^ { 2 } ) d x } \end{array}$ is equal to $\textstyle { \frac { 4 } { 3 } }$ , and the areas $T$ a $R$ ${ \frac { \mathbf { \vec { x } } } { A } } \ = \ { \frac { \mathbf { \vec { 3 } } } { \mathbf { \vec { 2 } } } }$ $\begin{array} { r } { \frac { R } { A } = \frac { 3 } { 2 } } \end{array}$

In a beautiful paper, Paul Erdós and Tibor Gallai asked what happens when $f ( x )$ is an arbitrary $n$ -th degree real polynomial with $f ( x ) > 0$ for $- 1 < x < 1$ , and $f ( - 1 ) = f ( 1 ) = 0$ The area $A$ is then $\textstyle \int _ { - 1 } ^ { 1 } f ( x ) d x$ Suppose that $f ( x )$ assumes in $( - 1 , 1 )$ its maximum value al $b$ , then $R = 2 f ( b )$ . Computing the tangents at $^ { - 1 }$ and at 1, it is readily seen (see the box) that

$$
{ \cal T } ~ = ~ { \frac { 2 f ^ { \prime } ( 1 ) f ^ { \prime } ( - 1 ) } { f ^ { \prime } ( 1 ) - f ^ { \prime } ( - 1 ) } } ,
$$

respectively $T = 0$ for $f ^ { \prime } ( 1 ) = f ^ { \prime } ( - 1 ) = 0$ .

# The tangential triangle

![](images/253e42347a90aa05f09d28e91db135af6a0ff6eddf9199e296f72c4ef129ef2f.jpg)

The area $\boldsymbol { T }$ of the tangential triangle is precisely $y _ { 0 }$ , where $( x _ { 0 } , y _ { 0 } )$ is the point of intersection of the two tangents. The equation of these tangents are $y = f ^ { \prime } ( - 1 ) ( x + 1 )$ and $y = f ^ { \prime } ( 1 ) ( x - 1 )$ ,hence

$$
x _ { 0 } = { \frac { f ^ { \prime } ( 1 ) + f ^ { \prime } ( - 1 ) } { f ^ { \prime } ( 1 ) - f ^ { \prime } ( - 1 ) } } ,
$$

and thus

$$
y _ { 0 } ~ = ~ f ^ { \prime } ( 1 ) \left( \frac { f ^ { \prime } ( 1 ) + f ^ { \prime } ( - 1 ) } { f ^ { \prime } ( 1 ) - f ^ { \prime } ( - 1 ) } - 1 \right) ~ = ~ 2 \frac { f ^ { \prime } ( 1 ) f ^ { \prime } ( - 1 ) } { f ^ { \prime } ( 1 ) - f ^ { \prime } ( - 1 ) } .
$$

$\textstyle { \frac { T } { A } }$ and $\textstyle { \frac { R } { A } }$ To see this, take $f ( x ) = 1 - x ^ { 2 n }$ b $T = 2 n$ : $\begin{array} { r } { \varLambda = \frac { 4 \eta _ { i } } { 2 \eta _ { i } + 1 } } \end{array}$ 2n+1,\$ and thus $\begin{array} { r } { \frac { T } { A } > n } \end{array}$ Similary, $R = 2$ $\begin{array} { r } { \frac { R } { A } = \frac { 2 n + 1 } { 2 n } } \end{array}$ $\boldsymbol { \mathscr { n } }$

But, as Erdôs and Gallai showed, for polynomials which have only real roots such bounds do indeed exist.

Theorem 2. Let $f ( x )$ be a real polynomial of degree $\eta \geq 2$ with only real roots, such that $f ( x ) > 0 f o r - 1 < x < 1$ and $f ( - 1 ) = f ( 1 ) = 0 ,$ Then

$$
\frac { 2 } { 3 } T \leq {  { \cal A } } \leq \frac { 2 } { 3 } {  { \cal R } } ,
$$

Mathematical Reviews

$$
\frac { \mathrm { F a l . ~ l . ~ N e ~ } } { \sin ( \pi \cdot \pi ) ^ { - 1 } } - \frac { \mathrm { F a ~ N e ~ t r ~ s ~ a n ~ } } { \sin ( \pi \cdot \pi ) } - \frac { \mathrm { F a l . ~ n u } ( \pi ) } { \sin ( \pi \cdot \pi ) } = 0
$$

Erdds, P. and Grünwald, T. Oa polynomiale with only roal ata Ann. of Mach. 40, 537-548 (1939). [MF 93} Es sci $\langle \Upsilon ( x )$ ein Palynom mit nur reellen Wurzeln,

$$
f ( - 1 ) = f ( 1 ) = 0 , \quad 0 < f ( x ) \equiv f ( \mu ) \quad \mathrm { f i r e ~ - 1 } < x < 1 ,
$$

wobei $- 2 < \mu < 2$ so dase $\nvdash$ die Stelle des Maximums von $f ( x )$ im Intervall $( - 1 , 1 )$ bedeutet. Dann int

$$
\ P : \mathop { \longrightarrow } _ { f ^ { \prime } ( \uparrow ) \to f ^ { \prime } ( - \uparrow ) } \mathop { \cong } _ { \operatorname { m a x } } \int _ { - \uparrow } ^ { 1 } f ( x ) d x \mathop { \le } _ { \operatorname { m a x } } \uparrow \cdot 2 f ( \mu ) ,
$$

and equality holds in both cases only for $n = 2$

Erds and Gallai established this result with an intricate induction proof. In the review of their paper, which appeared on the first page of the first issue of the Mathematical Reviews in 1940, George Pólya explained how the first inequality can also be proved by the inequality of the arithmetic and geometric mean — a beautiful example of a conscientious review and a Book Proof at the same time.

Proof of ${ \frac { 2 } { 3 } } T \leq A$ Since $f ( x )$ has only real roots, and none of them in the open interval $( - 1 , 1 )$ , it can be written — apart from a constant positive factor which cancels out in the end — in the form

$$
f ( x ) = ( 1 - x ^ { 2 } ) \prod _ { i } ( x _ { i } - x ) \prod _ { j } ( \beta _ { j } + x )
$$

with $\alpha _ { i } \geq 1 , \beta _ { j } \geq 1$ Hence

$$
A = \int _ { - 1 } ^ { 1 } ( 1 - x ^ { 2 } ) \prod _ { i } ( \alpha _ { i } - x ) \prod _ { j } ( \beta _ { j } + x ) d x .
$$

By making the substitution $x \longmapsto - x$ , we find that also

$$
A = \int _ { - 1 } ^ { 1 } ( 1 - x ^ { 2 } ) \prod _ { i } ( x _ { i } + x ) \prod _ { j } ( \beta _ { j } - x ) d x ,
$$

and hence by the inequality of the arithmetic and the geometric mean (note that all factors are $\geq 0$ )

$$
\begin{array} { r l } { A } & { = \displaystyle \int _ { - 1 } ^ { 1 } \frac { 1 } { 2 } \left[ \left( 1 - \alpha ^ { 2 } \right) \prod _ { i } ( \alpha _ { i } - x ) \prod _ { j } ( i \beta _ { j } - x ) \right] + } \\ & { \qquad \left( 1 - \alpha ^ { 2 } \right) \prod ( \alpha _ { i } + x ) \prod _ { j } ( \beta _ { j } - x ) \ \Bigg ] d x } \\ & { \geq \displaystyle \int _ { - 1 } ^ { 1 } \left( 1 - \alpha ^ { 2 } \right) \left( \prod _ { i } ( \alpha _ { i } ^ { 2 } - x ^ { 2 } ) \prod _ { j } ( \beta _ { j } ^ { 2 } - x ^ { 2 } ) \right) ^ { 1 / 2 } d x } \\ & { \geq \displaystyle \int _ { - 1 } ^ { 1 } \left( 1 - x ^ { 2 } \right) \left( \prod _ { i } ( \alpha _ { i } ^ { 2 } - 1 ) \prod _ { j } ( \beta _ { j } ^ { 2 } - 1 ) \right) ^ { 1 / 2 } d x } \\ & { = \displaystyle \frac { 4 } { 3 } \left( \prod _ { i } ( \alpha _ { i } ^ { 2 } - 1 ) \prod _ { j } ( \beta _ { j } ^ { 2 } - 1 ) \right) ^ { 1 / 2 } . } \end{array}
$$

Let us compute $f ^ { \prime } ( 1 )$ and ${ \hat { f } } ^ { \prime } ( - 1 )$ . (We may assume $f ^ { \prime } ( - 1 ) , f ^ { \prime } ( 1 ) \neq 0 ,$ since otherwise $T = 0$ and the inequality ${ \mathfrak { z } } T \leq A$ becomes trivial.) By (3) we see

$$
f ^ { \prime } ( 1 ) = - 2 \prod _ { i } ( \alpha _ { i } - 1 ) \prod _ { j } ( \beta _ { j } + 1 ) ,
$$

and similarly

$$
f ^ { \prime } ( - 1 ) = 2 \prod _ { i } ( \alpha _ { i } + 1 ) \prod _ { j } ( \beta _ { j } - 1 ) .
$$

Hence we conclude

$$
A \ \geq \ { \frac { 2 } { 3 } } ( - f ^ { \prime } ( 1 ) f ^ { \prime } ( - 1 ) ) ^ { 1 / 2 } .
$$

![](images/83a3f9427b563c5203dc60d5609e5a185d4ea307aaa3d8dd7f3d31d07e2ed255.jpg)

Applying now the inequality of the harmonic and the geometric mean to $- f ^ { \prime } ( 1 )$ and $\int \limits ^ { \prime } ( 1 )$ , we arrive by (2) at the conclusion

$$
A ~ \geq ~ \frac { 2 } { 3 } \frac { 2 } { \frac { 1 } { - f ^ { \prime } ( 1 ) } + \frac { 1 } { f ^ { \prime } ( - 1 ) } } ~ = ~ \frac { 4 } { 3 } \frac { f ^ { \prime } ( 1 ) f ^ { \prime } ( - 1 ) } { f ^ { \prime } ( 1 ) - f ^ { \prime } ( - 1 ) } ~ = ~ \frac { 2 } { 3 } T ,
$$

which is what we wanted to show. By analyzing the case of equality in all our inequalities the reader can easily supply the last statement of the theorem. 0

The reader is invited to search for an equally inspired proof of the second inequality in Theorem 2.

Well, analysis is inequalities after all, but here is an example from graph theory where the use of inequalities comes in quite unexpected. In Chapter 32 we will discuss Turán's theorem. In the simplest case it takes on the following form:

Theorem 3. Suppose $G$ is a graph on n vertices without triangles. Then $G$ has at most n^{ \$ $\begin{array} { r } { \frac { \boldsymbol { n } ^ { 2 } } { 1 } \ i e d g e s , } \end{array}$ ,and equality holds only when $n$ is even and $G$ is the complete bipartite graph $K _ { \pi / 2 , \pi / 2 }$ .

First proof. This proof, using Cauchy's inequality, is due to Mantel. Let $V = \{ 1 , \ldots , n \}$ be the vertex set and $E$ the edge set of $G$ By $d _ { i }$ we denote the degree of $i$ hence $\sum _ { i \in \nu } d _ { i } \ = \ 2 | L ^ { \prime } |$ (see page 143 in the chapter on double counting). Suppose $i j$ is an edge. Since $G$ has no triangles, we find $d _ { i } + d _ { j } \leq \pi$ since no vertex is a neighbor of both $i$ and $j$ .

It follows that

$$
\sum _ { i j \in E } ( d _ { i } + d _ { j } ) \ \leq \ n | E | .
$$

Note that $d _ { i }$ appears exactly $d _ { i }$ times in the sum, so we get

$$
n | E | \ge \sum _ { i j \in E } ( d _ { i } + d _ { j } ) = \sum _ { i \in V } d _ { i } ^ { 2 } ,
$$

and hence with Cauchy's inequality applied to the vectors $( d _ { 1 } , \ldots , d _ { n } )$ and $( 1 , \ldots , 1 )$ ,

$$
n | E | \geq \sum _ { i \in V } d _ { i } ^ { 2 } \geq \frac { ( \sum d _ { i } ) ^ { 2 } } { n } = \frac { 4 | E | ^ { 2 } } { n } ,
$$

and the result follows. In the case of equality we find $d _ { i } ~ = ~ d _ { j }$ for all $i , j$ , and further $d _ { i } = \frac { n } { 2 }$ (since $d _ { i } + d _ { j } = n )$ . Since $G$ is triangle-free, $G = K _ { n / 2 , n / 2 }$ is immediately seen from this.

Second proof. The following proof of Theorem 3, using the inequality of the arithmetic and the geometric mean, is a folklore Book Proof. Let $\alpha$ be the size of a largest independent set $A$ , and set ${ \beta = n - \alpha }$ Since $G$ is triangle-frce, the neighbors of a vertex $i$ form an independent set, and we infer $d _ { i } \leq \alpha$ for all $i$ .

The set $\boldsymbol { B } = \boldsymbol { V } \backslash \boldsymbol { A }$ of size $\beta$ meets every edge of $G$ Counting the edges of $G$ according to their endvertices in $B$ we obtain $\begin{array} { r } { | E | \le \sum _ { i \in B } d _ { i } } \end{array}$ .The inequality of the arithmetic and geometric mean now yields

$$
| E | \le \sum _ { i \in B } d _ { i } \le \alpha \beta \le \Big ( \frac { \alpha + \beta } { 2 } \Big ) ^ { 2 } = \frac { n ^ { 2 } } { 1 } ,
$$

and again the case of equality is easily dealt with.

# References

[1] H. Al.ZER: A proof of the arithmetic mean-geometric mean inequality, Amer. Math. Monthly 103 (1996), 585.   
[2] P. S. BULLEN, D. S. MITRinOvICS & P. M. VASI: Means and their Inequalities, Reidel, Dordrecht 1988.   
[3] P. ERDÖs & T. GRüNwALD: On polynomials with only real roots, Annals Math. 40 (1939), 537-548.   
[4] G. H. HARDY, J. E. LITTLEWOOD & G. POLYA: InequaliTiEs, Cambridge University Press, Cambridge 1952.   
[5] W. MANTEL: Problem 28, Wiskundige Opgaven 10 (1906), 60-61.   
[6] G. PóLYA: Review of [3]. Mathematical Reviews 1 (1940), 1.   
[7] G. PóL.YA & G. SZEGó: Problems and Theorems in Analysis, Vol. I. Springer-Verlag, Berlin Heidelberg New York 1972/78; Reprint 1998.

![](images/6b15d2be533017f70e06b7da243704440ddc61b8197cf11321f691a7a903eb50.jpg)

# A theorem of Pólya on polynomials

Among the many contributions of George Pólya to analysis, the following has always been Erdôs' favorite, both for the surprising result and for the beauty of its proof. Suppose that

$$
f ( z ) = z ^ { n } + b _ { n - 1 } z ^ { n - 1 } + \cdots + b _ { 0 }
$$

is a complex polynomial of degree $n \geq 1$ with leading coefficient 1. Associate with $f ( z )$ the set

$$
{ \mathcal { C } } : = \{ z \in \mathbb { C } : | f ( z ) | \leq 2 \} ,
$$

that is, $\mathcal { C }$ is the set of points which are mapped under $f$ into the circle of radius 2 around the origin in the complex plane. So for $n = 1$ the domain $\mathcal { C }$ is just a circular disk of diameter 4.

By an astoundingly simple argument, Pólya revealed the following beautiful property of this set $\mathcal { C }$ :

Take any line $L$ in the complex plane and consider the orthogonal projection $\mathcal { C } _ { L }$ of the set $\mathcal { C }$ onto $L$ Then the total length of any such projection never exceeds 4.

What do we mean by the total length of the projection $\mathcal { C } _ { L }$ being at most 4? We will see that $\mathcal { C } _ { L }$ is a finite union of disjoint intervals $I _ { 1 } , \ldots , I _ { t }$ , and the condition means that $\ell ( I _ { 1 } ) + \ldots + \ell ( I _ { t } ) \leq 4$ , where $\ell ( I _ { j } )$ is the usual length of an interval.

By rotating the plane we see that it suffices to consider the case when $L$ is the real axis of the complex plane. With these comments in mind, let us state Pólya's result.

Theorem 1. Let $f ( z )$ be $^ { a }$ complex polynomial of degree at least 1 and leading coefficient 1. Set $C = \{ z \in \mathbb { C } : | f ( z ) | \leq 2 \}$ and let $\mathcal { R }$ be the orthogonal projection of $\mathcal { C }$ onto the real axis. Then there are intervals $I _ { 1 } , \ldots , I _ { t }$ on the real line which together cover $\mathcal { R }$ and satisfy

$$
\ell ( I _ { 1 } ) + \ldots + \ell ( I _ { t } ) \leq 4 .
$$

Clearly the bound of 4 in the theorem is attained for $n = 1$ . To get more of a feeling for the problem let us look at the polynomial $f ( z ) = z ^ { 2 } - 2$ which also attains the bound of 4. If $z = x + i y$ is a complex number, then $x$ is its orthogonal projection onto the real line. Hence

$$
{ \mathcal { R } } = \{ x \in \mathbb { R } : x + i y \in C { \mathrm { ~ f o r ~ s o m e ~ } } y \} .
$$

![](images/d3a16c6f95a59c9e6cfbeb165671172b9b5f39fa82faf1805987c8327f8b579d.jpg)  
George Pólya

![](images/fb1caab9e21585e14ec5d69a8bc0e4d79553ccfd0144b6bbce1323aeee63e046.jpg)

![](images/a17a9d56f14bf118dc2ddc50fa204d78723d94a95d43bb731de342b9260310b3.jpg)

![](images/260fdaa0589a26680940e69cdf9a180de018afb53e4872b306a101c4a7c4a27e.jpg)

The reader can easily prove that for $f ( z ) = z ^ { 2 } - 2$ we have $x + i y \in { \mathcal { C } }$ if and only if

$$
( x ^ { 2 } + y ^ { 2 } ) ^ { 2 } \leq 4 ( x ^ { 2 } - y ^ { 2 } ) .
$$

It follows that $x ^ { 4 } \leq ( x ^ { 2 } + y ^ { 2 } ) ^ { 2 } \leq 4 x ^ { 2 }$ , and thus $x ^ { 2 } \leq 4$ , that is, $| x | \le 2$ . On the other hand, any $z = x \in \mathbb { R }$ with $| x | \le 2$ satisfies $| z ^ { 2 } - 2 | \leq 2$ , and we find that $\mathcal { R }$ is precisely the interval $[ - 2 , 2 ]$ of length 4.

As a first step towards the proof write $f ( z ) = \left( z - c _ { 1 } \right) \cdot \cdot \cdot \left( z - c _ { n } \right)$ with $c _ { k } =$ $a _ { k } + i b _ { k }$ , and consider the real polynomial $p ( x ) = ( x - a _ { 1 } ) \cdot \cdot \cdot ( x - a _ { n } )$ . Let $z = x + i y \in \mathcal { C }$ , then by the theorem of Pythagoras

$$
| x - a _ { k } | ^ { 2 } + | y - b _ { k } | ^ { 2 } = | z - c _ { k } | ^ { 2 }
$$

and hence $\left| x - a _ { k } \right| \leq \left| z - c _ { k } \right|$ for all $k$ , that is,

$$
| p ( x ) | = | x - a _ { 1 } | \cdots | x - a _ { n } | \leq | z - c _ { 1 } | \cdots | z - c _ { n } | = | f ( z ) | \leq 2 .
$$

Thus we find that $\mathcal { R }$ is contained in the set $\mathcal { P } = \{ x \in \mathbb { R } : | p ( x ) | \leq 2 \}$ . and if we can show that this latter set is covered by intervals of total length at most 4, then we are done. Accordingly, our main Theorem 1 will be a consequence of the following result.

Theorem 2. Let $p ( x )$ be a real polynomial of degree $n \geq 1$ with leading coefficient 1, and all roots real. Then the set $\mathcal { P } = \{ x \in \mathbb { R } : | p ( x ) | \leq 2 \}$ can be covered by intervals of total length at most 4.

As Pólya shows in his paper [2], Theorem 2 is, in turn, a consequence of the following famous result due to Chebyshev. To make this chapter self-contained, we have included a proof in the appendix (following the beautiful exposition by Pólya and Szegó).

![](images/db3aec1c9953bb420cbc02dadb7b52ace9307518b6c3e26755df33cb8985412c.jpg)

Pavnuty Chebyshev on a Soviet stamp from 1946

# Chebyshev's Theorem.

Let $p ( x )$ be a real polynomial of degree $n \geq 1$ with leading coefficient 1. Then

$$
\operatorname* { m a x } _ { - 1 \leq x \leq 1 } | p ( x ) | \geq { \frac { 1 } { 2 ^ { n - 1 } } } .
$$

Let us first note the following immediate consequence.

Corollary. Let $p ( x )$ be a real polynomial of degree $n \geq 1$ with leading coefficient 1, and suppose that $| p ( x ) | \leq 2$ for all $_ x$ in the interval $[ a , b ]$ . Then $b - a \leq 4$ .

Proof. Consider the substitution $\begin{array} { r } { y = \frac { 2 } { b - a } ( x - a ) - 1 } \end{array}$ This maps the $x$ interval $[ a , b ]$ onto the $y$ interval $[ - 1 , 1 ]$ . The corresponding polynomial

$$
q ( y ) = p ( { \textstyle { \frac { b - a } { 2 } } } ( y + 1 ) + a )
$$

has leading coefficient $( { \frac { b - a } { 2 } } ) ^ { n }$ and satisfies

$$
\operatorname* { m a x } _ { - 1 \leq y \leq 1 } | q ( y ) | \ = \ \operatorname* { m a x } _ { a \leq x \leq b } | p ( x ) | .
$$

By Chebyshev's theorem we deduce

$$
\begin{array} { r } { 2 \geq \underset { { \mathfrak a } \leq x \leq { b } } { \operatorname* { m a x } } | p ( x ) | \geq ( \frac { b - a } { 2 } ) ^ { n } \frac { 1 } { 2 ^ { n - 1 } } = 2 ( \frac { b - a } { 4 } ) ^ { n } , } \end{array}
$$

and thus $\} - a \leq 4$ , as desired.

This corollary brings us already very close to the statement of Theorem 2. If the set $\mathcal { P } = \{ x : | p ( x ) | \ \leq \ 2 \}$ is an interval, then the length of $p$ is at most 4. The set $p$ may, however, not be an interval, as in the example depicted here, where $p$ consists of two intervals.

What can we say about $p 2$ Since $p ( x )$ is a continuous function, we know at any rate that $p$ is the union of disjoint closed intervals $I _ { 1 } , I _ { 2 } , . . . ,$ and that $p ( x )$ assumes the value 2 or $- 2$ at each endpoint of an interval $I _ { j }$ .This implies that there are only finitely many intervals $I _ { 1 } , \ldots , I _ { t }$ , since $p ( x )$ can assume any value only finitely often.

Pólya's wonderful idea was to construct another polynomial $\tilde { p } ( x )$ of degree n. again with leading coefficient 1, such that $\widetilde { \mathcal { P } } = \{ x : | \bar { p } ( x ) | \le 2 \}$ is an interval of length at least $\ell ( I _ { 1 } ) + \ldots + \ell ( I _ { t } )$ . The corollary then proves $\ell ( I _ { 1 } ) + \ldots + \ell ( I _ { t } ) \leq \ell ( \widetilde { \mathcal { P } } ) \leq 4$ , and we are done.

Proof of Theorem 2. Consider $p ( x ) = ( x - u _ { 1 } ) \cdot \cdot \cdot ( x \cdot - a _ { n } )$ with $\mathcal { P } = \{ x \in \mathbb { R } : | p ( x ) | \leq 2 \} = I _ { 1 } \cup . . . \cup I _ { t }$ , where we arrange the intervals $I _ { j }$ such that $I _ { 1 }$ is the leftmost and $I _ { t }$ the rightmost interval. First we claim that any interval $I _ { j }$ contains a root of $p ( x )$ . We know that $p ( x )$ assumes the values 2 or $- 2$ at the endpoints of $I _ { j }$ . If one value is 2 and the other $- 2$ , then there is certainly a root in $I _ { j }$ . So assume $p ( x ) = 2$ at both endpoints (the case $- 2$ being analogous). Suppose $b \in I _ { j }$ is a point where $p ( x )$ assumes its minimum in $I _ { j }$ . Then $p ^ { \prime } ( b ) = 0$ and $p ^ { \prime \prime } ( b ) \geq 0$ If $p ^ { \prime \prime } ( \boldsymbol { b } ) = 0$ , then $b$ is a multiple root of $p ^ { \prime } ( x )$ , and hence a root of $p ( x )$ by Fact 1 from the box on the next page. If, on the other hand, $z ^ { \prime \prime } ( b ) > 0$ , then we deduce $p ( b ) \leq 0$ from Fact 2 from the same box. Hence either $p ( b ) = 0$ , and we have our root, or $p ( b ) < 0$ , and we obtain a root in the interval from $b$ to either endpoint of $I _ { j }$ .

Here is the final idea of the proof. Let $I _ { 1 } , \ldots , I _ { t }$ be the intervals as before, and suppose the rightmost interval $I _ { t }$ contains $\gamma n$ roots of $p ( x )$ , counted with their multiplicities. If $n ! = n$ , then $I _ { t }$ is the only interval (by what we just proved), and we are finished. So assume m $< ~ \pi$ , and let $d$ be the distance between $I _ { t - 1 }$ and $I _ { t }$ as in the figure. Let $b _ { 1 } , \ldots , b _ { m }$ be the roots of $p ( x )$ which lie in $I _ { t }$ and $c _ { 1 } , \ldots , c _ { n - m }$ the remaining roots. We now write $p ( x ) = q ( x ) r ( x )$ where $q ( x ) = ( x - b _ { 1 } ) \cdot \cdot \cdot ( x - b _ { m } )$ and $r ^ { * } ( x ) =$ $( x - c _ { 1 } ) \dotsb ( x - c _ { n - 1 } )$ , and set $p _ { 1 } ( x ) = q ( x + d ) r ( x )$ . The polynomial $p _ { 1 } ( x )$ is again of degree $n$ with leading coefficient 1. For $x \in I _ { 1 } \cup . . . \cup I _ { t - 1 }$ we have $| x + d - b _ { i } \} < | x - b _ { i } |$ for all $i$ , and hence $| q ( x + d ) | < | q ( x ) |$ . It follows that

$$
| p _ { 1 } ( x ) | \ \leq \ | p ( x ) | \ \leq \ 2 \qquad \mathrm { f o r } \ x \in I _ { 1 } \cup . . . \cup I _ { t - 1 } .
$$

If, on the other hand, $x \in l _ { t }$ , then we find $| \gamma ( x - d ) \} \leq | r ( x ) |$ and thus

$$
\begin{array} { r } { | p _ { 1 } ( x - d ) | ~ = ~ | q ( x ) | | r ( x - d ) | ~ \le ~ | p ( x ) | ~ \le ~ 2 , } \end{array}
$$

![](images/e9c10831f1f98fcab62d224a7ea59ec8432402b28b55e3745942018736cd1e8b.jpg)

For the polynomial $y ( x ) = x ^ { 2 } ( x - 3 )$ we get $\mathcal { P } = [ 1 - \sqrt { 3 } , 1 ] \cup [ 1 + \sqrt { 3 } , \approx 3 . 2 ]$ which means that $I _ { t } - d \subseteq { \mathcal { P } } _ { 1 } \mathrel { \mathop { : } } \{ x :  | p _ { 1 } ( x ) | \leq 2 \} .$

![](images/2e2c017a4ffe5ec133c0010727c42f8a450d59bb8183612cb670de97551e5393.jpg)

In summary, we see that ${ \mathcal P } _ { 1 }$ contains $I _ { 1 } \cup . . . \cup I _ { t . }$ . $_ 1 \cup ( I _ { t } - d )$ and hence has total length at least as large as $p$ . Notice now that with the passage from $p ( x )$ to $p _ { 1 } ( x )$ the intervals $I _ { t - 1 }$ and $I _ { t } \ - \ d$ merge into a single interval. We conclude that the intervals $J _ { 1 } , \ldots , J _ { s }$ of ${ \boldsymbol { \gamma } } _ { 1 } ( { \boldsymbol { x } } )$ making up $\mathcal { P } _ { 1 }$ have total length at least $\ell ( I _ { 1 } ) + \ldots + \ell ( I _ { t } )$ , and that the rightmost interval $J _ { s }$ contains more than $m$ roots of ${ \mathfrak { p } } _ { 1 } ( x )$ . Repeating this procedure at most $t - 1$ times, we finally arrive at a polynomial $\tilde { p } ( x )$ with ${ \widetilde { \mathcal { P } } } = \{ x : | { \tilde { p } } ( x ) | \leq 2 \}$ being an interval of length $\ell ( \widetilde { \mathcal { P } } ) \geq \ell ( I _ { 1 } ) + \ldots \ell ( I _ { t } )$ , and the proof is complete. □

# Two facts about polynomials with real roots

Let $p ( x )$ be a non-constant polynomial with only real roots.

Fact 1. If $b$ is a multiple root of $p ^ { \prime } ( x )$ , then $b$ is also a root of $p ( x )$ .

Proof. Let $b _ { 1 } , \ldots , b _ { r }$ be the roots of $p ( x )$ with multiplicities $\begin{array} { r } { s _ { 1 } , \dotsc , s _ { r } , \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc } \end{array}$ From $p ( x ) = ( x - b _ { j } ) ^ { s _ { j } } h ( x )$ we infer that $b _ { j }$ is a root of $\boldsymbol { p ^ { \prime } } ( \boldsymbol { x } )$ if $s _ { j } \geq 2$ , and the multiplicity of $b _ { j }$ in $p ^ { \prime } ( x )$ is $s _ { j } \sim 1$ .Furthermore, there is a root of $p ^ { \prime } ( x )$ between $b _ { 1 }$ and $b _ { 2 }$ , another root between $b _ { 2 }$ and $b _ { 3 } , \ldots$ , and one between $b _ { r - 1 }$ and $b _ { r }$ , $\begin{array} { r } { \sum _ { j = 1 } ^ { r } \big ( s _ { j } - 1 \big ) + \big ( r - 1 \big ) } \end{array}$ counts already up to the degree $n \cdots 1$ of $p ^ { \prime } ( x ) ^ { \prime }$ . Consequently, the multiple roots of $p ^ { \prime } ( x )$ can only occur among the roots of $p ( x )$

Fact 2. We have $p ^ { \prime } ( x ) ^ { 2 } \geq p ( x ) p ^ { \prime \prime } ( x ) \ f o r \ a l l \ x \in \mathbb { R } .$

Proof. If $x = a _ { i }$ is a root of $p ( x )$ , then there is nothing to show. Assume then $_ x$ is not a root. The product rule of differentiation yields

$$
p ^ { \prime } ( x ) = \sum _ { k = 1 } ^ { n } { \frac { p ( x ) } { x - a _ { k } } } , \quad { \mathrm { t h a t ~ i s , } } \quad { \frac { p ^ { \prime } ( x ) } { p ( x ) } } = \sum _ { k = 1 } ^ { n } { \frac { 1 } { x - a _ { k } } } .
$$

Differentiating this again we have

$$
\frac { p ^ { \prime \prime } ( x ) p ( x ) - p ^ { \prime } ( x ) ^ { 2 } } { p ( x ) ^ { 2 } } = - \sum _ { k = 1 } ^ { n } \frac { 1 } { ( x - a _ { k } ) ^ { 2 } } < 0 .
$$

# Appendix: Chebyshev's theorem

Theorem. Let $p ( x )$ be $a$ real polynomial of degree $n \geq 1$ with leading coefficient 1. Then

$$
\operatorname { m a x } _ { - 1 \leq x \leq 1 } | p ( x ) | \geq { \frac { 1 } { 2 ^ { n - 1 } } } .
$$

Before we start, let us look at some examples where we have equality. The margin depicts the graphs of polynomials of degrees 1, 2 and 3, where we have cquality in each case. Indeed, we will see that for every degrce there is precisely onc polynomial with equality in Chebyshev's theorem.

Proof. Consider a real polynomial $p ( x ) = x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \ldots + a _ { 0 }$ with leading coefficient 1. Since we are interested in the range $- 1 \leq x \leq 1$ , we set $x = \cos \vartheta$ and denote by $g ( \vartheta ) : = f ^ { \prime } ( \cos \vartheta )$ the resulting polynomial in cos $\vartheta$ ,

$$
g ( \vartheta ) = ( \cos \vartheta ) ^ { n } + a _ { n - 1 } ( \cos \vartheta ) ^ { n - 1 } + \ldots + a _ { 0 } .
$$

The proof proceeds now in the following two steps which are both classical results and interesting in their own right.

(A) We express $g \{ v ^  \} \}$ as a so-called cosine polynomial, that is, a polynomial of the form

$$
g ( \vartheta ) = b _ { n } \cos n \vartheta + b _ { n - 1 } \cos ( n - 1 ) \vartheta + . . . + b _ { 1 } \cos \vartheta + b _ { 0 }
$$

with $b _ { k } \in \mathbb { R }$ , and show that its leading coefficient is $\textstyle b _ { n } = { \frac { 1 } { 2 ^ { n - 1 } } }$ :

(B) Given any cosine polynomial $h ( v )$ of order $n$ (meaning that $\lambda _ { n }$ is the highest nonvanishing coefficient)

$$
h ( \vartheta ) = \lambda _ { n } \cos n \vartheta + \lambda _ { n - 1 } \cos ( n - 1 ) \vartheta + . . . + \lambda _ { 0 } ,
$$

we show $| \lambda _ { n } | \leq \operatorname* { m a x } | \hbar ( \vartheta ) |$ , which when applied to $g ( \vartheta )$ will then prove the theorem.

Proof of (A). To pass from (1) to thc representation (2), we have to express all powers $( \cos \theta ) ^ { k }$ as cosine polynomials. For example, the addition theorem for the cosine gives

$$
\cos 2 \vartheta = \cos ^ { 2 } \vartheta - \sin ^ { 2 } \vartheta = 2 \cos ^ { 2 } \vartheta - 1 ,
$$

so that $\cos ^ { 2 } \vartheta = \textstyle { \frac { 1 } { 2 } } \cos 2 \vartheta + \textstyle { \frac { 1 } { 2 } }$ To do this for an arbitrary power $( \cos \theta ) ^ { k }$ we go into the complex numbers, via the relation ${ \mathfrak { e } } ^ { i \cdot { \mathbf { x } } } = \cos x + i \sin x$ . The $\boldsymbol { \mathsf { e } } ^ { i x }$ are the complex numbers of absolute value I (see the box on complex unit roots on page 25). In particular, this yields

$$
e ^ { i n \vartheta } = \cos n \vartheta + i \sin n \vartheta .
$$

On the other hand,

$$
e ^ { i n \vartheta } \ = \ ( e ^ { i \vartheta } ) ^ { n } \ = \ ( \cos \vartheta + i \sin \vartheta ) ^ { n } .
$$

![](images/9039b709df02ed5efba2c180fe3cf941dba4c7d6196137269e19eedfc17927cc.jpg)

Thc polynomials $p _ { 1 } ( x ) = x$ , $p _ { 2 } \{ x \} =$ $x ^ { 2 } - { \frac { 1 } { 2 } }$ and $\begin{array} { r } { p _ { 3 } ( x ) = x ^ { 3 } - \frac { 3 } { 4 } x } \end{array}$ achicve equality in Chebyshev's theorcm.

Equating the real parts in (4) and (5) wc obtan by $i ^ { 4 \ell + 2 } = - 1$ . $i ^ { 4 \ell } = 1$ and $\sin ^ { 2 } \theta = 1 - \cos ^ { 2 } \theta$

$$
\begin{array} { r c l } { \cos n \vartheta } & { = } & { \displaystyle \sum _ { \ell \geq 0 } { \binom { n } { 4 \ell } } ( \cos \vartheta ) ^ { n - 4 \ell } ( 1 - \cos ^ { 2 } \vartheta ) ^ { 2 \ell } } \\ & & { \cdot \displaystyle \sum _ { \ell \geq 0 } { \binom { n } { 4 \ell + 2 } } ( \cos \vartheta ) ^ { n - 4 \ell - 2 } ( 1 - \cos ^ { 2 } \vartheta ) ^ { 2 \ell + 1 } . } \end{array}
$$

We conclude that $\cos n \vartheta$ is a polynomial in cos $\vartheta$

$$
\cos n \vartheta \ = \ c _ { n } ( \cos \vartheta ) ^ { n } + c _ { n } \quad _ { 1 } ( \cos \vartheta ) ^ { n - 1 } + \ldots + c _ { 0 } .
$$

From (6) we obtain for the highest coefficient $\begin{array} { l l l } { \sum _ { k > 0 } { \binom { n } { 2 k } } } & { = } & { 2 ^ { r _ { i } - 1 } } \end{array}$ holds for $n > 0$ . Every subset of $\{ 1 , 2 , \ldots , n - 1 \}$ yields an even sized subset of $\{ 1 , 2 , \ldots , n \}$ if we add the element $\mathscr { n }$ "if needed."

$$
\begin{array} { r c l } { \displaystyle \mathfrak { c } _ { \eta } } & { = } & { \displaystyle \sum _ { \ell \ge 0 } \binom { n } { 4 \ell } + \sum _ { \ell \ge 0 } \binom { n } { 4 \ell + 2 } } \end{array} = 2 ^ { n - 1 } .
$$

Now we turn our argument around. Assuming by induction that for $k < n ,$ $( \cos { \vartheta } ) ^ { k }$ can be expressed as a cosine polynomial of order $k$ , we infer from (that $( \cos \vartheta ) ^ { \eta 2 }$ can be written as a cosine polynomial of order $\gamma _ { \downarrow }$ with leading coefficient $\begin{array} { r } { b _ { n } = \frac { 1 } { 2 ^ { n - 1 } } } \end{array}$ .

Proof of $( \mathbf { B } )$ .Let $h ( \vartheta )$ be a cosine polynomial of order $n$ as in (3), and assume without loss of generality $\lambda _ { n } > 0$ Now we set $\begin{array} { r } { m ( \vartheta ) : = \lambda _ { n } \cos \cdot r _ { l } \vartheta } \end{array}$ and find

$$
\begin{array} { r c l } { { m ( \frac { k } { n } \pi ) } } & { { = } } & { { ( - 1 ) ^ { k } \lambda _ { n } \qquad \mathrm { f o r } \ k = 0 , 1 , \dots , n . } } \end{array}
$$

Suppose, for a proof by contradiction, that max $| h ( \vartheta ) | < \lambda _ { n }$ .Then

$$
m ( { \frac { k } { n } } \pi ) \ - h ( { \frac { k } { n } } \pi ) = ( - 1 ) ^ { k } \lambda _ { n } - h ( { \frac { k } { n } } \pi )
$$

is positive for even $k$ and negative for odd $k$ in the range $0 \leq k \leq n$ .We conclude that $m ( \vartheta ) - h ( \vartheta )$ has at least $\mathscr { n }$ roots in the interval $[ 0 , \pi ]$ .But this cannot be since $m ( \vartheta ) - \hbar ( \vartheta )$ is a cosinc polynomial of order $n - 1$ , which can be written in the form (1) and thus has at most $n - 1$ roots.

The proof of $\mathbf { ( B ) }$ and thus of Chebyshev's theorcm is complete.

The reader can now easily complete the analysis, showing that $g _ { n } ( \vartheta ) : =$ $\frac { 1 } { 2 ^ { n - 1 } } \cos \eta , \vartheta$ is the only cosine polynomial of order $n$ with leading coefficn e  al $\begin{array} { r } { | g ( \vartheta ) | = \frac { 1 } { 2 ^ { n - 1 } } } \end{array}$ .

The polynomials $T _ { n } ( x ) = \cos \pi \vartheta$ , $x = \cos \vartheta$ , are called the Chebyshev $\displaystyle { \frac { 1 } { 2 ^ { n - 1 } } T _ { \ u { r } } \left( \ d { } x \right) }$ is the unique monic polynomial of degree $\mathfrak { n }$ where equality holds in Chebyshev's theorem.

# References

[1] P. L. CEBYCEv: (Euvres. Vol. I, Acad. Imperiale des Sciences, St. Petersburg 1899, pp. 387-469.   
[2] G. Pói.YA: Beitrag zur Verallgemeinerung des Verzerrungssatzes auf mehrfach zusammenhüngenden Gebieten, Sitzungsber. Preuss. Akad. Wiss. Bcrlin (1928). 228-232; Collected Papers Vol. I, MIT Press 1974, 347-351.   
[3] G. P6I.YA & G. SZEGO: Problems and Theorems in Analysis, Vol. , Springer-Verlag, Berlin Heidclberg New York 1976; Reprint 1998.

# On a lemma of Littlewood and Offord

In their work on the distribution of roots of algebraic equations, Littlewood and Offord proved in 1943 the following result:

Let $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ be complex numbers with $| a _ { i } | \geq 1$ for all $i$ , and consider the $2 ^ { n }$ linear combinations $\textstyle \sum _ { i = 1 } ^ { n } \varepsilon _ { i } a _ { i }$ with $\varepsilon _ { i } \in \{ 1 , - 1 \}$ . Then the number of sums $\textstyle \sum _ { i = 1 } ^ { n } \varepsilon _ { i } a _ { i }$ which li in ther y circle of radius 1 is not greater than

$$
c { \frac { 2 ^ { n } } { \sqrt { n } } } \log n f o r s o m e c o n s t a n t c > 0 .
$$

A few years later Paul Erdôs improved this bound by removing the $\log n$ term, but what is more interesting, he showed that this is, in fact, a simple consequence of the theorem of Sperner (see page 151).

To get a feeling for his argument, let us look at the case when all $a _ { i }$ are real. We may assume that all $a _ { i }$ are positive (by changing $a _ { i }$ to $- a _ { i }$ and $\varepsilon _ { i }$ to $- \varepsilon _ { i }$ whenever $a _ { i } < 0 \dot s$ . Now suppose that a set of combinations $\sum \varepsilon _ { i } a _ { i }$ lies in the interior of an interval of length 2. Let $N = \{ 1 , 2 , \dots , n \}$ be the index set. For every $\sum \varepsilon _ { i } a _ { i }$ we set $I : = \{ i \in N : \varepsilon _ { i } = 1 \}$ .Now if ${ \mathit { I } } \subsetneq { \mathit { I } } ^ { \prime }$ for two such sets, then we conclude that

$$
\sum \varepsilon _ { i } ^ { \prime } a _ { i } - \sum \varepsilon _ { i } a _ { i } = 2 \sum _ { i \in I ^ { \prime } \backslash I } a _ { i } \geq 2 .
$$

![](images/f07d34600c61a5ee21c980a08daaadd2b28c7fb2f3bd21fc3e5320a1b9195a95.jpg)  
John E. Littlewood

which is a contradiction. Hence the sets $I$ form an antichain, and we $\scriptstyle { { \binom { n } { \lfloor n / 2 \rfloor } } }$ such combinations. By Stirling's formula (see page 1 1) we have

$$
{ \binom { n } { \lfloor n / 2 \rfloor } } \ \leq \ c { \frac { 2 ^ { n } } { \sqrt { n } } } \quad { \mathrm { f o r ~ s o m e ~ } } c > 0 .
$$

For $n$ even and all $a _ { i } = 1$ we obtain $\binom { n } { n / 2 }$ combinations $\textstyle \sum _ { i = 1 } ^ { n } \varepsilon _ { i } a _ { i }$ that sum to 0. Looking at the interval $( - 1 , 1 )$ we thus find that the binomial number gives the exact bound.

$\scriptstyle { \binom { n } { \lfloor n / 2 \rfloor } }$ was the right bound for complex numbers as well (he could only prove $c 2 ^ { n } n ^ { - 1 / 2 }$ for some $c$ and indeed that the same bound is valid for vectors $\pmb { a } _ { 1 } , \ldots , \pmb { a } _ { n }$ with $| { \pmb a } _ { i } | \geq 1$ in a real Hilbert space, when the circle of radius 1 is replaced by an open ball of radius 1.

Sperner's theorem. Any antichain of subsets of an $n$ -set has size at most $\scriptstyle { { \binom { n } { \lfloor n / 2 \rfloor } } }$

Erdös was right, but it took twenty years until Gyula Katona and Daniel Kleitman independently came up with a proof for the complex numbers (or, what is the same, for the plane $\mathbb { R } ^ { 2 }$ ).Their proofs used explicitly the 2-dimensionality of the plane, and it was not at all clear how they could be extended to cover finite dimensional real vector spaces.

But then in 1970 Kleitman proved the full conjecture on Hilbert spaces with an argument of stunning simplicity. In fact, he proved even more. His argument is a prime example of what you can do when you find the right induction hypothesis.

A word of comfort for all readers who are not familiar with the notion of a Hilbert space: We do not really need general Hilbert spaces. Since we only deal with finitely many vectors ${ \pmb a } _ { i }$ , it is enough to consider the real space $\mathbb { R } ^ { d }$ with the usual scalar product. Here is Kleitman's result.

Theorem. Let $a _ { 1 } , \ldots , a _ { r }$ be vectors in $\mathbb { R } ^ { d }$ ,each of length at least 1, and let $R _ { 1 } , \ldots , R _ { k }$ be $k$ open regions of $\mathbb { R } ^ { d }$ ,where $| x - y | < 2$ for any $\boldsymbol { x } , \boldsymbol { y }$ that lie in the same region $R _ { i }$ .

Then the $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \varepsilon _ { i } { \pmb a } _ { i } , \varepsilon _ { i } \in \{ 1 , - 1 \} . } \end{array}$ that can lie in the union $\textstyle \bigcup _ { i } R _ { i }$ of the regions is at most the sum of the $k$ largest binomial coefficients $\binom { n } { j }$ .

In pcular, w  e $\binom { n } { \lfloor n / 2 \rfloor } f o r k = 1 .$

Before turning to the proof note that the bound is exact for

$$
\mathbf { \alpha } _ { \mathbf { a } _ { 1 } } = \mathbf { \alpha } _ { \cdot \cdot \cdot } = \mathbf { \alpha } _ { \mathbf { a } _ { n } } = \mathbf { \alpha } _ { \mathbf { a } } = ( 1 , 0 , \ldots , 0 ) ^ { T } .
$$

Indeed, for even $\boldsymbol { n }$ we obtain $\binom { n } { n / 2 }$ sums equal to 0, $\binom { n } { n / 2 - 1 }$ sums equal to   
$\scriptstyle ( - 2 ) \mathbfcal { a } , \binom { n } { n / 2 + 1 }$ sums cqual to ${ 2 a }$   
around

$$
\begin{array} { r } { - 2 \lceil \frac { k - 1 } { 2 } \rceil { \bf a } , \quad \ldots \quad ( - 2 ) { \bf a } , \quad 0 , \quad 2 { \bf a } , \quad \ldots \quad 2 \lfloor \frac { k - 1 } { 2 } \rfloor { \bf a } , } \end{array}
$$

we obtain

$$
\left( { \binom { n } { \frac { n - k + 1 } { 2 } } } \right) + . . . + \left( { \binom { n } { \frac { n - 2 } { 2 } } } \right) + { \binom { n } { \frac { n } { 2 } } } + { \binom { n } { \frac { n + 2 } { 2 } } } + . . . + \left( { \binom { n } { \frac { n + k - 1 } { 2 } } } \right)
$$

sums lying in these $k$ balls, and this is our promised expression, since the largest binomial coefficients are centered around the middle (see page 12). A similar reasoning works when $n$ is odd.

Proof. We may assume, without loss of generality, that the regions $R _ { i }$ are disjoint, and will do so from now on. The key to the proof is the recursion of the binomial coefficients, which tells us how the largest binomial coefficients of $n$ and $ n - 1$ are related. Set $r = \lfloor \frac { n - k + 1 } { 2 } \rfloor , s ^ { \prime } = \lfloor \frac { n + k - 1 } { 2 } \rfloor .$ then ${ \binom { n } { r } } , { \binom { n } { r + 1 } } , \dots , { \binom { n } { s } }$ aree the $k$ $\mathscr { n }$ The recursion $\binom { n } { i } \ = \ \binom { n - 1 } { i } + \binom { n - 1 } { i - 1 }$ implies

$$
\begin{array} { r c l } { \displaystyle \sum _ { i = r } ^ { s } \binom { n } { i } } & { = } & { \displaystyle \sum _ { i = r } ^ { s } \binom { n - 1 } { i } + \sum _ { i = r } ^ { s } \binom { n - 1 } { i - 1 } } \\ & { = } & { \displaystyle \sum _ { i = r } ^ { s } \binom { n - 1 } { i } + \sum _ { i = r - 1 } ^ { s - 1 } \binom { n - 1 } { i } } \\ & { = } & { \displaystyle \sum _ { i = r - 1 } ^ { s } \binom { n - 1 } { i } + \sum _ { i = r } ^ { s - 1 } \binom { n - 1 } { i } , } \end{array}
$$

and an easy calculation shows that the first sum adds the $k \ \nearrow \ 1$ largest binomial coeffficients $\binom { r \imath - 1 } { \it \Omega _ { i } }$ $k - 1$

Kleitman's proof proceeds by induction on $n$ , the case $\gamma _ { \downarrow } ~ \simeq ~ 1$ being trivial. In the light of (1) we need only show for the induction step that the linear combinations of ${ \pmb a } _ { 1 } , \dots , { \pmb a } _ { \gamma _ { 2 } }$ that lie in $k$ disjoint regions can be mapped bijectively onto combinations of $a _ { 1 } , \ldots , a _ { n } . . . _ { 1 }$ that lie in $k + 1$ or $k - 1$ regions.

Claim. At least one of the translated regions $R _ { j } \ : - \ : \pmb { a } _ { \uparrow \downarrow }$ is disjoint from all the translated regions $R _ { 1 } + { \bf a } _ { n } , . . . , R _ { k } + { \bf a } _ { n }$

To prove this, consider the hyperplane $H = \{ { \bf x } : \langle { \pmb a } _ { n } , { \pmb x } \rangle = c \}$ orthogonal to $\mathbf { a } _ { \mathfrak { u } }$ , which contains all translates $R _ { i } + { a _ { \mathfrak { n } } }$ on the side that is given by $\langle \pmb { a } _ { n } , \pmb { x } \rangle \geq \mathcal { C } .$ , and which touches the closure of some region, say $R _ { j } + { \pmb a } _ { n }$ . Such a hyperplane exists since the regions are bounded. Now $| x - y | < 2$ holds for any $\pmb { x } \in R _ { j }$ and $\pmb { y }$ in the closure of $R _ { j }$ , since $R _ { j }$ is open. We want to show that $R _ { j } - { \pmb a } _ { n }$ lies on the other side of $H$ . Suppose, on the contrary, that $\langle \pmb { a } _ { n } , \pmb { x } - \pmb { a } _ { n } \rangle \geq c$ for some $\pmb { x } \in R _ { j }$ , that is, $\langle a _ { n } , \mathbf { x } \rangle \geq | a _ { n } | ^ { 2 } + \mathfrak { c } .$

Let ${ \pmb y } + { \pmb a } _ { \pmb u }$ be a point where $\boldsymbol { H }$ touches ${ R _ { j } } + { { \mathbf { a } } _ { \harpoonright } }$ , then $\pmb { y }$ is in the closure of $R _ { j }$ , and $\langle { \pmb a } _ { n } , { \pmb y } + { \pmb a } _ { n } \rangle = c$ , that is. $\langle \pmb { a } _ { n } , - \pmb { y } \rangle = | \pmb { a } _ { n } | ^ { 2 } \dotsm { c } .$ Hence

$$
\langle \pmb { a } _ { n } , \pmb { x } - \pmb { y } \rangle \geq 2 | \pmb { a } _ { n } | ^ { 2 } ,
$$

and we infer from the Cauchy-Schwarz inequality

$$
2 | a _ { n } | ^ { 2 } \leq \langle a _ { n } , x - y \rangle \leq | a _ { n } | | x - y | ,
$$

and thus (with $\left| \pmb { a } _ { n } \right| \ge 1 )$ we get $2 \leq 2 | { \pmb a } _ { n } | \leq | { \pmb x } - { \pmb y } |$ , a contradiction.

The rest is easy. We classify the combinations $\sum E _ { i } { \pmb { a } } _ { i }$ which come to lie in $R _ { 1 } \cup \ldots \cup R _ { k }$ $\sum _ { i = 1 } ^ { n } \varepsilon _ { i } \mathbf { a } _ { i }$ wih $\varepsilon _ { \tau { \scriptscriptstyle L } } = - 1$ and all $\sum _ { i = 1 } ^ { n } \varepsilon _ { i } { \pmb { a } } _ { i }$ with $\varepsilon _ { \tau _ { i } } ~ = ~ 1$ lying in $R _ { j }$ , and into Class 2 we throw in the remaining combinations ∑i=1 εi with εn = 1, not in Rj. It follows that the combinations $\sum _ { i = 1 } ^ { n - 1 } \varepsilon _ { i } \pmb { a } _ { i }$ corresponding to Class the $k + 1$ disjoint regions $R _ { 1 } + { \pmb a } _ { n } , \ldots , R _ { k } + { \pmb a } _ { n }$ and $R _ { j } \ : - \ : a _ { \tau \iota }$ , and the combinations $\sum _ { i = 1 } ^ { n - 1 } \varepsilon _ { i } \mathbf { a } _ { i }$ coronding to Class  e $k - 1$ disjoint regions $R _ { 1 } - a _ { n } , . . . , R _ { k } - a _ { n }$ without $R _ { j } - { \pmb a } _ { \tau \imath }$ .By induction, Class 1 contains at most i=r- $\scriptstyle \sum _ { i = r - 1 } ^ { s } { \binom { n - 1 } { i } }$   
$\sum \limits _ { i = r } ^ { s - 1 } ( \sum \limits _ { i } ^ { r _ { i } } 1 )$

![](images/40c41f5f5d4189b4d0a3b67ada41993bf5c6e7d0bc6b10bbd62b3b8362ca2e94.jpg)

# References

[1] P. ErDôs: On a lemma of Littlewood and Offord, Bulletin Amer. Math. Soc. 51 (1945), 898-902.   
[2] G. KAToNA: On a conjecture of Erdós and a stronger form of Sperner's theorem, Studia Sci. Math. Hungar. 1 (1966), 59-63.   
[3] D. KLEITMAN: On a lemma of Littlewood and Offord on the distribution of certain sums, Math. Zeitschrift 90 (1965), 251-259.   
[4] D. KLEITMAN: On a lemma of Littlewood and Offord on the distributions of linear combinations of vectors, Advances Math. 5 (1970), 155-157.   
[5] J. E. LITTLEwOoD & A. C. OfFORD: On the number of real roots of a random algebraic equation III, Mat. USSR Sb. 12 (1943), 277-285.

# Cotangent and the Herglotz trick

What is the most interesting formula involving elementary functions? In his beautiful article [2], whose exposition we closely follow, Jürgen Elstrodt nominates as a first candidate the partial fraction expansion of the cotangent function:

$$
\pi \cot \pi x \ = \ { \frac { 1 } { x } } + \sum _ { n = 1 } ^ { \infty } { \bigl ( } { \frac { 1 } { x + n } } + { \frac { 1 } { x - n } } { \bigr ) } ( x \in \mathbb { R } \backslash \mathbb { Z } ) .
$$

This elegant formula was proved by Euler in $\ S 1 7 8$ of his Introductio in Analysin Infinitorum from 1748 and it certainly counts among his finest achievements. We can also write it even more elegantly as

$$
\pi \cot \pi x = \operatorname* { l i m } _ { N \to \infty } \sum _ { n = - N } ^ { N } { \frac { 1 } { x + n } }
$$

$\textstyle \sum _ { n \in \mathbb { Z } } { \frac { 1 } { x + n } }$ is a bit depends on the "right" order of summation.

We shall derive (1) by an argument of stunning simplicity which is attributed to Gustav Herglotz — the "Herglotz trick." To get started, set

$$
f ( x ) \ : = \ \pi \cot \pi x , \qquad g ( x ) \ : = \ \operatorname* { l i m } _ { N \to \infty } \sum _ { n = - N } ^ { N } { \frac { 1 } { x + n } } .
$$

and let us try to derive enough common properties of these functions to see in the end that they must coincide. ..

The functions $f$ and $g$ are defined for all non-integral values and are continuous there.

For the cotangent function $\begin{array} { r } { f ( x ) = \pi \cot \pi x = \pi \frac { \cos \pi x } { \sin \pi x } } \end{array}$ this is clear (see the figure). For $g ( x )$ , we first use the identity $\begin{array} { r } { { \frac { 1 } { x + n } } + { \frac { 1 } { x - n } } = - { \frac { 2 x } { n ^ { 2 } - x ^ { 2 } } } } \end{array}$ to rewrite Euler's formula as

$$
\pi \cot \pi x = { \frac { 1 } { x } } - \sum _ { n = 1 } ^ { \infty } { \frac { 2 x } { n ^ { 2 } - x ^ { 2 } } } .
$$

Thus for (A) we have to prove that for every $x \not \in \mathbb { Z }$ the series

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } - x ^ { 2 } } }
$$

converges uniformly in a neighborhood of $x$

![](images/2719727a25c5d5065facc0d656e83d288349b6c04849730422c7ddf176094b87.jpg)  
Gustav Herglotz

![](images/133a57e09ad5214d65614f191ce0749ccc30fb8cc157fe51d0deffd7bb00b576.jpg)  
The function $f ( x ) = \pi$ cot πx

For this, we don't get any problem with the first term, for $ \ n = 1$ , or with the terms with $2 n - 1 \leq x ^ { 2 }$ , since there is only a finite number of them. On the other hand, for $n \geq 2$ and $2 n - 1 > x ^ { 2 }$ , that is $n ^ { 2 } - x ^ { 2 } > ( n - 1 ) ^ { 2 } > 0 ,$ . the summands are bounded by

$$
0 < \frac { 1 } { n ^ { 2 } - x ^ { 2 } } < \frac { 1 } { ( n - 1 ) ^ { 2 } } ,
$$

and this bound is not only true for $x$ itself, but also for values in a neighborhood of $x$ Finallythe fact that $\sum \frac { 1 } { ( n - 1 ) ^ { 2 } }$ converges (to $\frac { \pi ^ { 2 } } { 6 }$ sce page 35) provides the uniform convergence needed for the proof of (A).

$\mathbf { ( B ) }$ Both $f$ and $g$ are periodic of period 1, that is, $f ( x + 1 ) = f ( x )$ and $g ( x + 1 ) = g ( x )$ hold for all $x \in \mathbb { R } \backslash \mathbb { Z }$ .

Since the cotangent has period $\pi$ , we find that $f$ has period 1 (sec again the figure above). For $g$ we argue as follows. Let

$$
g _ { _ { N } } ( x ) \ : = \ \sum _ { n = - N } ^ { N } { \frac { 1 } { x + n } } ,
$$

then

$$
\begin{array} { r c l } { { g _ { _ { N } } ( x + 1 ) } } & { { = } } & { { \displaystyle \sum _ { n = - N } ^ { N } \frac { 1 } { x + 1 + n } = \sum _ { n = - N + 1 } ^ { N + 1 } \frac { 1 } { x + n } } } \\ { { } } & { { = } } & { { g _ { _ { N - 1 } } ( x ) + \displaystyle \frac { 1 } { x + N } + \frac { 1 } { x + N + 1 } . } } \end{array}
$$

Hence $g ( x + 1 ) = \operatorname* { l i m } _ { N \to \infty } g _ { N } ( x + 1 ) = \operatorname* { l i m } _ { N \to \infty } g _ { N - 1 } ( x ) = g ( x ) .$

Both $f$ and $g$ are odd functions, that is, we have $f ( - x ) = - f ( x )$ and $g ( - x ) = - g ( x )$ for all $x \in \mathbb { R } \backslash \mathbb { Z }$ .

The function $f$ obviously has this property, and for $g$ we just have to observe that $g _ { N } ( - x ) = - g _ { N } ( x )$ .

The final two facts constitute the Herglotz trick: First we show that $f$ and $g$ satisfy the same functional cquation, and secondly that $h : = f - g$ can be continuously extended to all of $\mathbb { R }$

$\mathbf { ( D ) }$ The two functions $f$ and $g$ satisfy the same functional equation: $\textstyle f ( { \frac { x } { 2 } } ) + f ( { \frac { x + 1 } { 2 } } ) = 2 f ( x )$ and $\begin{array} { r } { g ( \frac { x } { 2 } ) + g ( \frac { x + 1 } { 2 } ) = 2 g ( x ) } \end{array}$ .

# Addition theorems:

$$
{ \begin{array} { r l } & { \sin ( x + y ) = \sin x \cos y + \cos x \sin y } \\ & { \cos ( x + y ) = \cos x \cos y - \sin x \sin y } \\ & { \implies \sin ( x + { \frac { \pi } { 2 } } ) = \quad \cos x } \\ & { \qquad \cos ( x + { \frac { \pi } { 2 } } ) = - \sin x } \\ & { \qquad \sin x = 2 \sin { \frac { x } { 2 } } \cos { \frac { x } { 2 } } } \\ & { \cos x - \cos ^ { 2 } { \frac { x } { 2 } } - \sin ^ { 2 } { \frac { x } { 2 } } . } \end{array} }
$$

For $f ( x )$ this results from the addition theorems for the sine and cosine functions:

$$
\begin{array} { r c l } { { f \big ( \frac { x } { 2 } \big ) + f \big ( \frac { x + 1 } { 2 } \big ) } } & { { \simeq } } & { { \pi \left[ \frac { \cos { \frac { \pi x } { 2 } } } { \sin { \frac { \pi x } { 2 } } } - \frac { \sin { \frac { \pi x } { 2 } } } { \cos { \frac { \pi x } { 2 } } } \right] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 2 \pi \frac { \cos \left( \frac { \pi x } { 2 } + \frac { \pi x } { 2 } \right) } { \sin \left( \frac { \pi x } { 2 } + \frac { \pi x } { 2 } \right) } = 2 f ( x ) . } } \end{array}
$$

The functional equation for $g$ follows from

$$
g _ { _ { N } } ( { \textstyle \frac { x } { 2 } } ) + g _ { _ { N } } ( { \textstyle \frac { x + 1 } { 2 } } ) = 2 g _ { _ { 2 N } } ( x ) + \frac { 2 } { x + 2 N + 1 } .
$$

which in turn follows from

$$
\frac { 1 } { \frac { x } { 2 } + n } + \frac { 1 } { \frac { x + 1 } { 2 } + n } = 2 \Big ( \frac { 1 } { x + 2 n } + \frac { 1 } { x + 2 n + 1 } \Big ) .
$$

Now let us look at

$$
h ( x ) ~ = ~ f ( x ) ~ - ~ g ( x ) ~ = ~ \pi \cot \pi x - \Big ( \frac { 1 } { x } - \sum _ { n = 1 } ^ { \infty } \frac { 2 x } { n ^ { 2 } - x ^ { 2 } } \Big ) .
$$

Wc know by now that $h$ is a continuous function on $\mathbb { R } \backslash \mathbb { Z }$ that satisfies the properties (B), (C), (D). What happens at the integral values? From the sine and cosine series expansions, or by applying de I'Hospital's rule twice, we find

$$
\operatorname * { l i m } _ { x \to 0 } \ \left( \cot x - { \frac { 1 } { x } } \right) \ = \ \operatorname * { l i m } _ { x \to 0 } \ { \frac { x \cos x - \sin x } { x \sin x } } = 0 ,
$$

$$
\begin{array} { r } { \cos x = 1 - \frac { x ^ { 2 } } { 2 ! } + \frac { x ^ { 4 } } { 1 ! } - \frac { x ^ { 6 } } { 6 ! } \pm \dots } \\ { \sin x = x - \frac { x ^ { 3 } } { 3 ! } + \frac { x ^ { 5 } } { 5 ! } - \frac { x ^ { 7 } } { 7 ! } \pm \dots } \end{array}
$$

and hence also

$$
\operatorname* { l i m } _ { x  0 } ~ ( \pi \cot \pi x - { \frac { 1 } { x } } ) ~ = ~ 0 .
$$

Bu since to have in fact $\operatorname* { l i m } _ { x \to 0 } \hbar \langle x \rangle = 0$ , and thus by periodicity

$$
\operatorname* { l i m } _ { \mathbf { x } } \hbar ( x ) = 0 \qquad { \mathrm { f o r ~ a l l ~ } } \pi \in \mathbb { Z } .
$$

In summary, we have shown the following:

(EBy setting $h ( x ) = 0$ for $x \in \ \mathbb { Z }$ , $h$ becomes a continuous function on all of $\mathbb { R }$ that shares the properties given in (B), (C) and (D).

We are ready for the coup de grâce. Since $h$ is a periodic continuous function, it possesses a maximum $7 7 2$ . Let $x _ { 0 }$ be a point in [0, 1] with $h ( x _ { 0 } ) = m$ . It follows from (D) that

$$
\begin{array} { r } { \hbar ( \frac { x _ { 0 } } { 2 } ) + \hbar ( \frac { x _ { 0 } + 1 } { 2 } ) = 2 m , } \end{array}
$$

and hence that $\beta _ { l } ( \frac { x _ { 0 } } { 2 } ) = m$ Iteration gives $h ( \frac { x _ { 0 } } { 2 ^ { n } } ) = n n$ for all $\mathcal { V }$ , and hence $h ( 0 ) = m$ by continuity. But $h ( 0 ) = 0$ , and so $\gamma _ { l } = 0$ , that is, $h ( x ) \leq 0$ for all $x \in \mathbb { R }$ . As $h ( x )$ is an odd function, $h ( x ) < 0$ is impossible, hence $h ( x ) = 0$ for all $z \in \mathbb { R }$ , and Euler's theorem is proved. □

A great many corollarics can be derived from (1), the most famous of which concerns the values of Riemann's zeta function at even positive integers (see the Appendix to Chapter 6),

$$
\zeta ( 2 k ) = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 k } } } \qquad ( k \in \mathbb { N } ) .
$$

So to finish our story let us see how Euler — a few ycars later, in 1755 - treated the series (4). We start with formula (2). Multiplying (2) by $\mathcal { X }$ and setting $y = \pi x$ we find for $| y | < \pi$ .

$$
\begin{array} { l l l } { { y \cot y } } & { { = } } & { { 1 \cdot 2 \displaystyle \sum _ { n = 1 } ^ { \infty } \frac { y ^ { 2 } } { \pi ^ { 2 } n ^ { 2 } - y ^ { 2 } } } } \\ { { } } & { { = } } & { { 1 - 2 \displaystyle \sum _ { n = 1 } ^ { \infty } \frac { y ^ { 2 } } { \pi ^ { 2 } n ^ { 2 } } \displaystyle \frac { 1 } { 1 - \left( \frac { y } { \pi n } \right) ^ { 2 } } . } } \end{array}
$$

The last factor is the sum of a geometric series, hence

$$
\begin{array} { l c l } { { y \cot y } } & { { = } } & { { 1 - 2 \displaystyle \sum _ { n = 1 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } \left( \frac { y } { \pi n } \right) ^ { 2 k } } } \\ { { } } & { { = } } & { { 1 - 2 \displaystyle \sum _ { k = 1 } ^ { \infty } \left( \frac { 1 } { \pi ^ { 2 k } } \sum _ { n = 1 } ^ { \infty } \frac { 1 } { n ^ { 2 k } } \right) y ^ { 2 k } , } } \end{array}
$$

and we have proved the remarkable result:

For all $k \in \mathbb { N }$ the coefficient of $y ^ { 2 k }$ in the   f $y \cot y$

$$
\left[ y ^ { 2 k } \right] y \cot y = - \frac { 2 } { \pi ^ { 2 k } } \sum _ { n = 1 } ^ { \infty } \frac { 1 } { n ^ { 2 k } } = - \frac { 2 } { \pi ^ { 2 k } } \zeta ( 2 k ) .
$$

There is another, perhaps much more "canonical," way to obtain a series expansion of $y$ cot $y$ We know from analysis that $e ^ { i \mathfrak { Y } } = \cos { y } + i \sin { y } .$ ,and thus

$$
\cos y ~ = ~ { \frac { e ^ { i y } + e ^ { - i y } } { 2 } } , \qquad \sin y ~ = ~ { \frac { e ^ { i y } - e ^ { - i y } } { 2 i } } ,
$$

which yields

$$
y \cot y ~ = ~ i y { \frac { e ^ { i y } + \epsilon ^ { - i y } } { e ^ { - i y } } } ~ = ~ i y { \frac { e ^ { 2 i y } + 1 } { e ^ { 2 i y } - 1 } } ~ .
$$

We now substitute $z = 2 i y$ , and get

$$
y \cot y = \frac { z } { 2 } \frac { e ^ { z } + 1 } { e ^ { z } - 1 } = \frac { z } { 2 } + \frac { z } { e ^ { z } - 1 } .
$$

Thus all we need is a power series expansion of the function $\frac { z } { c ^ { i } - 1 }$ that this function is defined and continuous on all of $\mathbb { R }$ (for $z = 0$ use the power series of the exponential function, or alternatively de l'Hospital's rule, which yields the value 1). We write

$$
\frac { z } { e ^ { z } - 1 } = : \ \sum _ { n \ge 0 } B _ { n } \frac { z ^ { n } } { n ! } \ .
$$

The coefficients $B _ { n }$ are known as the Bernoulli numbers. The left-hand side of (6) is an even function (that is, $f ( z ) = f ( - z ) )$ , and thus we see that $B _ { \scriptscriptstyle  { r 2 } } = 0$ for odd $n \geq 3$ , while $\begin{array} { r } { B _ { 1 } = - \frac { 1 } { 2 } } \end{array}$ corresponds to the term of $\textstyle { \frac { z } { 2 } }$ in (6).

From

$$
\biggl ( \sum _ { n \geq 0 } R _ { n } { \frac { z ^ { n } } { n ! } } \biggr ) \left( e ^ { z } - 1 \right) = \biggl ( \sum _ { n \geq 0 } D _ { n } { \frac { z ^ { n } } { n ! } } \biggr ) \biggl ( \sum _ { n \geq 1 } { \frac { z ^ { n } } { n ! } } \biggr ) = z
$$

we obtain by comparing coefficients for $z ^ { \pmb { \imath } , }$ .

$$
\sum _ { k = 0 } ^ { n - 1 } { \frac { B _ { k } } { k ! ( n - k ) ! } } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { f o r } } \ n = 1 , } \\ { 0 } & { { \mathrm { f o r } } \ n \neq 1 . } \end{array} \right. }
$$

We may compute the Bernoulli numbers recursively from (8). The value $n = 1$ gives $B _ { 0 } = { \bf 1 }$ . $n = 2$ yields $\begin{array} { r } { \frac { B _ { \vartheta } } { \mathbf { \tilde { z } } } + B _ { 1 } = 0 } \end{array}$ that is $B _ { \mathrm { 1 } } = \cdots _ { \mathrm { 2 } } ^ { 1 }$ and so on.

Now we are almost done: The combination of (6) and (7) yields

$$
y \cot y \ = \ \sum _ { k = 0 } ^ { \infty } B _ { 2 k } { \frac { ( 2 i y ) ^ { 2 k } } { ( 2 k ) ! } } \ = \ \sum _ { k = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { k } 2 ^ { 2 k } B _ { 2 k } } { ( 2 k ) ! } } y ^ { 2 k } ,
$$

and out comes, with (5), Euler's formula for $\zeta ( 2 k )$ :

$$
\begin{array} { l l l } { \displaystyle \sum _ { n = 1 } ^ { \infty } \frac { 1 } { n ^ { 2 k } } } & { = } & { \displaystyle \frac { ( - 1 ) ^ { k - 1 } 2 ^ { 2 k - 1 } B _ { 2 k } } { ( 2 k ) ! } \pi ^ { 2 k } \qquad ( k \in \mathbb { N } ) . } \end{array}
$$

Looking at our table of the Bernoulli numbers, we thus obtain once again the sum $\begin{array} { r } { \sum \frac { 1 } { n ^ { 2 } } = \frac { \pi ^ { 2 } } { 6 } } \end{array}$ from Chapter 6, and further

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 4 } } } - { \frac { \pi ^ { 4 } } { 9 0 } } , \qquad \sum _ { n ^ { \ldots } 1 } ^ { \infty } { \frac { 1 } { n ^ { 6 } } } = { \frac { \pi ^ { 6 } } { 9 4 5 } } , \qquad \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 8 } } } = { \frac { \pi ^ { 8 } } { 9 4 5 0 } } ,
$$

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 1 0 } } } = { \frac { \pi ^ { 1 0 } } { 9 3 5 5 5 } } , \qquad \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 1 2 } } } = { \frac { 6 9 1 \pi ^ { 1 2 } } { 6 3 8 5 1 2 8 7 5 } } , \quad . . .
$$

The Bernoulli number $\begin{array} { r } { B _ { 1 0 } = \frac { 5 } { \mathrm { f i f } } } \end{array}$ that gets us $\zeta ( 1 0 )$ looks innocuous enough, but the next value $\begin{array} { r } { B _ { 1 2 } = - \frac { 6 9 \ " } { 2 7 3 0 } } \end{array}$ , needed for $\zeta ( 1 2 )$ , contains the large prime factor 691 in the numerator. Euler had first computed some values $\zeta ( 2 k )$ without noticing the connection to the Bernoulli numbers. Only the appcarance of the strange prime 691 put him on the right track.

Incidentally, since $\zeta ( 2 k )$ converges to 1 for $k \longrightarrow \infty$ , equation (9) tells us that the numbers $| \boldsymbol { B } _ { 2 k } |$ grow very fast — something that is not clear from the first few values.

In contrast to all this, one knows very little about the values of the Riemann zeta function at the odd integers $k _ { i } \geq 3$ ; see page 41.

IN DEFINIEND. SUMMIS SERIER. INTINTT. 131 m. Quo aurem vaior harum fummarum clarius perpiciaplures hajumodi Stricrum Summas commadiori modo prelas hic adjiciam.

$$
\begin{array} { r l } & { \quad _ { 1 } + _ { 2 } ^ { \infty } + _ { 3 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 1 } ^ { \infty } + _ { 1 } ^ { \infty } + _ { 3 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 4 } ^ { \infty } \alpha \alpha \alpha \left( \frac { \alpha + 1 } { 3 } \right) ^ { \infty } } \\ & { \quad _ { 1 } + _ { 1 } ^ { \infty } + _ { 2 } ^ { \infty } + _ { 3 } ^ { \infty } + _ { 2 } ^ { \infty } + _ { 1 } ^ { \infty } + _ { 1 } ^ { \infty } + _ { 2 } ^ { \infty } \alpha ^ { 2 } \alpha ^ { 3 } \alpha ^ { 3 } + _ { 1 } ^ { \infty } } \\ & { \quad _ { 2 } + _ { 3 } ^ { \infty } + _ { 3 } ^ { \infty } + _ { 3 } ^ { \infty } + _ { 2 } ^ { \infty } + _ { 1 } ^ { \infty } + _ { 3 } ^ { \infty } + _ { 3 } ^ { \infty } \alpha ^ { 3 } \alpha ^ { 3 } } \\ & { \quad _ { 3 } + _ { 4 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 3 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 4 } ^ { \infty } - _ { 3 } ^ { \infty } \alpha ^ { 3 } \alpha ^ { 3 } } \\ & { \quad _ { 4 } + _ { 5 } ^ { \infty } + _ { 3 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 1 } ^ { \infty } - _ { 3 } ^ { \infty } + _ { 3 } ^ { \infty } } \\ & { \quad _ { 4 } + _ { 5 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 5 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 4 } ^ { \infty } + _ { 6 } ^ { \infty } - _ { 3 } ^ { \infty } + _ { 4 } ^ { \infty } } \\ &  \quad _ { 1 } + _ { 6 } ^  \end{array}
$$

Hocwlque itos Porclatum iplus $\pmb { \imath }$ Exponemtes artificio alibi copomcndo continuare Licuit, quod ideo hic adjunxi, quod R Seiei

Page 131 of Euler's 1748 \*Introductio in Analysin Infinitorum"

# References

[1] S. BoCHNER: Book review of "Gesammelte Schriften" by Gustav Herglotz, Bulletin Amcr, Math. Soc. 1 (1979), 1020-1022.

[2] J. El.sTroDT: Partialbruchzerlegung des Kotangens, Herglotz-Trick und die WeierstruBsche stetige, nirgends differenzierbare Funktion, Math. Semesterberichte 45 (1998), 207-220.

[3] L. EuLER: Introductio in Analysin Infinitorum, Tomus Primus, Lausanne 1748: Opera Omnia, Ser. 1, Vol. 8. In English: Introduction to Analysis of the Infinite, Book I (translatcd by J. D. Blanton), Springer-Verlag, Ncw York 1988.

[4] L. EuLER: Institutiones calculi differentialis cum ejus usu in analysi finitorum ac doctrina serierum, Petersburg 1755; Opera Omnia, Ser. 1, Vol. 10.

A French nobleman, Georges Louis Leclerc, Comte de Buffon, posed the following problem in 1777:

Suppose that you drop a short needle on ruled paper — what is then the probability that the needle comes to lie in a position where it crosses one of the lines?

The probability depends on the distance $d$ between the lines of the ruled paper, and it depends on the length $\ell$ of the needle that we drop — or rather it depends only on the ratio $\frac { \ell } { d }$ A short needle for our purpose is one of length $\ell \leq d$ In other words, a short needle is one that cannot cross two lines at the same time (and will come to touch two lines only with probability zero). The answer to Buffon's problem may come as a surprise: It involves the number $\pi$ .

# Theorem ("Buffon's needle problem")

If a short needle, of length e, is dropped on paper that is ruled with equally spaced lines of distance $d \geq \ell ,$ then the probability that the needle comes to lie in a position where it crosses one of the lines is exactly

$$
p ~ = ~ { \frac { 2 } { \pi } } { \frac { \ell } { d } } .
$$

The result means that from an experiment one can get approximate values for $\pi$ :If you drop a needle $N$ times, and get a positive answer (an intersection) in $P$ cases, then $\textstyle { \frac { P } { N } }$ should be approximately $\frac { 2 } { \pi } \frac { \ell } { d }$ , that is, $\pi$ should be approximated by $\textstyle { \frac { 2 \ell N } { d P } }$ . The most extensive (and exhaustive) test was perhaps done by Lazzarini in 1901, who allegedly even built a machine in order to drop a stick 3408 times (with $\begin{array} { r } { \frac { \ell } { d } ~ = ~ \frac { 5 } { 6 } ) } \end{array}$ . He found that it came to cross a line 1808 times, which yields the approximation $\pi \approx 2 \cdot { \frac { 5 } { 6 } } { \frac { 3 4 0 8 } { 1 8 0 8 } } = 3 . 1 4 1 5 9 2 9 . . . . ,$ which is corect t x $\pi$ and much too good to be true! (The values that Lazzarini chose lead directly $\begin{array} { r } { \pi \approx \frac { 3 5 5 } { 1 1 3 } } \end{array}$ nthe ta ho $\frac { 5 } { 6 }$ where $\textstyle { \frac { 5 } { 6 } } 3 4 0 8$ is a multiple of 355. See [5] for a discussion of Lazzarini's hoax.)

The needle problem can be solved by evaluating an integral. We will do that below, and by this method we will also solve the problem for a long needle. But the Book Proof, presented by E. Barbier in 1860, needs no integrals. It just drops a different needle ...

![](images/06fd00948b4f713869e7efcddfd2b0da9fffc9574de6eda2b69f5f451e74eefe.jpg)

Le Comte de Buffon

$^ d$   
1-11 $\ell$

If you drop any needle, short or long, then the expected number of crossings will be

$$
\begin{array} { r } { E = p _ { 1 } + 2 p _ { 2 } + 3 p _ { 3 } + \ldots , } \end{array}
$$

where $p _ { 1 }$ is the probability that the needle will come to lie with exactly one crossing, $\vartheta \boldsymbol { \cdot } \boldsymbol { \cdot }$ is the probability that we get exactly two crossings, $\{ \beta _ { 3 }$ is the probability for three crossings, etc. The probability that we get at least one crossing, which Buffon's problem asks for, is thus

$$
y = y _ { 1 } + y _ { 2 } + y _ { 3 } + \ldots
$$

(Events where the needle comes to lie exactly on a line, or with an endpoint on one of the lines, have probability zero — so they can be ignored throughout our discussion.)

On the other hand, if the needle is short then the probability of more than one crossing is zero, $p _ { 2 } = p _ { 3 } = \ldots = 0 .$ ,and thus we get $E = p$ The probability that we are looking for is just the expected number of crossings. This reformulation is extremely useful, because now we can use linearity of expectation (cf. page 84). Indeed, let us write $E ( f )$ for the expected number of crossings that will be produced by dropping a straight needle of length $l$ . If this length is $f = x + y$ , and we consider the "front part" of length $\boldsymbol { \mathbf { \mathit { x } } }$ and the "back part" of length $y$ of the needle separately, then we get

$$
{ \cal E } ( x \ t \cdot y ) = { \cal E } ( x ) \ t \cdot { \cal E } ( y ) ,
$$

since the crossings produced are always just those produced by the front part, plus those of the back part.

By induction on n this functional equation" implies that ${ \cal { F } } ( n x ) = n { \cal { E } } ( x )$ for all $n \in \mathbb { N }$ , and then that $\begin{array} { r } { m { E } ( \frac { n } { m } x ) = E \big ( m \frac { n } { m } x ) = E ( n x ) = n E ( x ) } \end{array}$ . so that $E ( \boldsymbol { r } ; \boldsymbol { x } ) = r E ( \boldsymbol { x } )$ holds for all rational $r \in \mathbb { Q }$ Furthermore, $E ( x )$ is clearly monotone in $x \geq 0$ , from which we get that $E ( x ) = { \mathfrak { c x } }$ for all $x \geq 0$ , where $c = E ( 1 )$ is some constant.

But what is the constant?

For that we use needles of different shape. Indeed, let's drop a "polygonal" needle of total length $l$ , which consists of straight pieces. Then the number of crossings it produces is (with probability 1) the sum of the numbers of crossings produced by its straight pieces. Hence, the expected number of crossings is again

$$
E = c _ { } \ell ,
$$

by linearity of expectation. (For that it is not even important whether the straight pieces are joined together in a rigid or in a flcxible way!)

The key to Barbier's solution of Buffon's needle problem is to consider a necdle that is a perfect circle $i$ of diameter $d .$ ,which has length $x = d \pi$ . Such a needle, if dropped onto ruled paper, produces exactly two intersections, always!

The circle can be approximated by polygons. Just imagine that together with the circular needle $C$ we are dropping an inscribed polygon $P _ { n }$ , as well as a circumscribed polygon $\boldsymbol { P ^ { n } }$ . Every line that intersects $P _ { n }$ will also intersect $C$ , and if a line intersects $C$ then it also hits $P ^ { n . }$ . Thus the expected numbers of intersections satisfy

$$
E ( P _ { n } ) ~ \leq ~ E ( C ) ~ \leq ~ E ( P ^ { n } ) .
$$

Now both $P _ { n }$ and $P ^ { n }$ are polygons, so the number of crossings that we may expect is $w _ { C }$ times length" for both of them, while for $C$ it is 2, whence

$$
c \ell ( P _ { n } ) ~ \leq ~ 2 ~ \leq ~ \mathfrak { c } \ell ( P ^ { n } ) .
$$

Both $P _ { r }$ and $P ^ { \prime }$ approximate $C$ for $\pi \longrightarrow \infty$ In particular,

$$
\operatorname * { l i m } _ { n \longrightarrow \infty } \ell ( P _ { n } ) = d \pi = \operatorname * { l i m } _ { n \longrightarrow \infty } \ell ( P ^ { n } ) ,
$$

and thus for $\eta , \longrightarrow \infty$ we infer from (1) that

$$
c d \pi \leq 2 \leq c d \pi ,
$$

which gives $\begin{array} { r } { c = \frac { 2 } { \pi } \frac { 1 } { d } } \end{array}$ .

But we could also have done it by calculus! The trick to obtain an "easy" integral is to first consider the slope of the needle; let's say it drops to lie with an angle of $\alpha$ away from horizontal, where $\alpha$ will be in the range $0 \leq \alpha \leq \frac { \pi } { 2 }$ . (We will ignore the case where the necdle comes to lie with negative slope, since that case is symmetric to the case of positive slope, and produces the same probability.) A needle that lies with angle $\alpha$ has height $\boldsymbol { \acute { f . } \operatorname { s i n } \alpha }$ , and the probability that such a needle crosses one of the horizontal lines of distance $d$ is Thus we get the probability by averaging over the possible angles $\alpha$ , as

$$
{ p \ = \ \begin{array} { l c l } { \displaystyle } & { \displaystyle } & { \displaystyle } \\ { \displaystyle } & { \displaystyle } \end{array} } \frac { \pi / 2 } { \pi } \frac { \ell \sin { \alpha } } { d \ } d \alpha = \frac { 2 } { \pi } \frac { \ell } { d } \big [ - \cos { \alpha } \big ] _ { 0 } ^ { \pi / 2 } = \frac { 2 } { \pi } \frac { \ell } { d } .
$$

For  lon ee  t t  y $\frac { \ell \ : \mathrm { s i n } \ : \alpha } { d }$ as long as $\ell \sin \ell x \leq d .$ that is, in the range $\begin{array} { r } { 0 \leq \alpha \leq \arcsin \frac { d } { \hat { \ell } } } \end{array}$ . However, for larger angles $\alpha$ the needle must cross a line, so the probability is 1. Hence we compute

$$
\begin{array} { r c l } { { p } } & { { = } } & { { \displaystyle \frac { 2 } { \pi } \Big ( \int _ { 0 } ^ { \arcsin ( d / \ell ) } \frac { \ell \sin \alpha } { d } d \alpha + \sum _ { \alpha \in \sin ( d / \ell ) } 1 d \alpha \Big ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \displaystyle \frac { 2 } { \pi } \Big ( \frac { \ell } { d } \Big [ - \cos \alpha \Big ] _ { 0 } ^ { \arcsin ( d / \ell ) } + \Big ( \frac { \pi } { 2 } - \arcsin \frac { d } { \ell } \Big ) \Big ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \displaystyle 1 + \frac { 2 } { \pi } \Big ( \frac { \ell } { d } \Big ( 1 - \sqrt { 1 - \frac { d ^ { 2 } } { \ell ^ { 2 } } } \Big ) - \arcsin \frac { d } { l } \Big ) } } \end{array}
$$

for $f \geq d$

So the answer isn't that pretty for a longer needle, but it provides us with a nice cxercise: Show ("just for safety") that the formula yiclds $\textstyle { \frac { 2 } { \pi } }$ for $\ell = d$ that it is strictly increasing in $l$ , and that it tends to 1 for $t \longrightarrow \infty$ .

![](images/33309bfdaab166dc85ea4caa5a0f81ddcb36f87931b5e7bb3f313786c81f664f.jpg)

![](images/259ef0155e349769ccc55a163ab7ab9bce4e4a88e7005d7c44fee43b5b7351e0.jpg)

![](images/2783add121160e62e627706b461879922d3a1e6a751cc57c9f6da06400d4733b.jpg)

# References

[1] E. BARBIER: Note sur le problème de l'aiguille et le jeu du joint couvert, J. Mathématiques Pures et Appliquées (2) 5 (1860), 273-286.   
[2] L. BERGGREN, J. BORWEIN & P. BORWEIN, EDS.: Pi: A SourCe Book, Springer-Verlag, New York 1997.   
[3] G. L. LECLERC, COMTE DE BUFFON: Essai d'arithmétique morale, Appendix to "Histoire naturelle générale et particulière," Vol. 4, 1777.   
[4] D. A. KLAIN & G.-C. ROTA: Introduction to Geometric Probability, "Lezioni Lincee," Cambridge University Press 1997.   
[5] T. H. O'BEIRNE: Puzzles and Paradoxes, Oxford University Press, London 1965.

![](images/a30bbbbd94c8c9a74333424f16ab6bca1cc0792b83700671637ce33898ea52a1.jpg)

# Pigeon-hole and double counting

Some mathematical principles, such as the two in the title of this chapter, are so obvious that you might think they would only produce equally obvious results. To convince you that "It ain't necessarily so" we illustrate them with examples that were suggested by Paul Erdös to be included in The Book. We will encounter instances of them also in later chapters.

# Pigeon-hole principle.

If n objects are placed in r boxes, where $r < n$ , then at least one of the boxes contains more than one object.

Well, this is indeed obvious, there is nothing to prove. In the language of mappings our principle reads as follows: Let $N$ and $R$ be two finite sets with

$$
| N | = n > r = | R | ,
$$

and let $f : N \longrightarrow R$ be a mapping. Then there cxists some $a \in R$ with $| f ^ { \cdots } | _ { ( a ) } | \geq 2$ We may even state a stronger inequality: There exists some $a \in R$ with

$$
| f ^ { - 1 } ( a ) | \geq \left\lceil { \frac { T L } { p } } \right\rceil .
$$

In fact, otherwisc we would have $| f ^ { - 1 } ( x ) | < \frac { \pi } { r }$ for all $\alpha$ , and hence $n = \sum _ { a \in R } | f ^ { - 1 } ( a ) | < r { \frac { n } { r } } = n$ , which cannot be.

# 1. Numbers

Claim. Consider the numbers 1, 2, 3, . .., 2n, and take any $\pi + 1$ of them. Then there are two among these $\boldsymbol { \mathfrak { n } } + \boldsymbol { \mathsf { I } }$ numbers which are relatively prime.

This is again obvious. There must be two numbers which are only 1 apart, and hence relatively prime.

But let us now turn the condition around.

Claim. Suppose again $A \subseteq \{ 1 , 2 , \dots , 2 n \}$ with $| A | = n ! + 1$ Then there are always two numbers in $A$ such that one divides the other.

![](images/2d46216739cec0eef49173aa3a8e71a4ee03b6a1145c3952b9ebeeff70e9c4bb.jpg)  
"The pigeon-holes from a bird's perspective"

Both results are no longer true if one replaces $\boldsymbol { \ n } { + } 1$ by $\gamma _ { \downarrow }$ : For this consider the sets $\{ 2 , 4 , 6 , \ldots , 2 \pi \}$ , respectively $\{ \eta , + 1 , n + 2 , \dots , 2 n \}$ .

This is not so clear. As Erdós told us, he put this question to young Lajos Posa during dinner, and when the meal was over, Lajos had the answer. It has remained onc of Erds' favorite "initiation" questions to mathematics. The (affirmative) solution is provided by the pigeon-hole principle. Write every number $a \ \in \ A$ in the form $a = 2 ^ { k } \mathfrak { m }$ , where $m$ is an odd number between I and $2 n - 1$ , Since there are $n + 1$ numbers in $A$ , but only $n$ different odd parts, there must be two numbers in $A$ with the same odd part. Hence one is a multiple of the other.

# 2. Sequences

Here is another one of Erdós' favorites, contained in a paper of Erdós and Szekeres on Ramsey problems.

Claim. In any sequence $a _ { 1 } , a _ { 2 } , \dots , a _ { r r { \imath } { \imath } { \imath } } .$ of $m n + 1$ distinct real numbers, there exists an increasing subsequence

$$
a _ { i _ { 1 } } < a _ { i _ { 2 } } < \ldots < a _ { i _ { m + 1 } } \qquad ( i _ { 1 } < i _ { 2 } < \ldots < i _ { m + 1 } )
$$

of length $m + 1$ , or a decreasing subsequence

$$
a _ { j _ { 1 } } > a _ { j _ { 2 } } > . . . > a _ { j _ { n + 1 } } ( j _ { 1 } < j _ { 2 } < . . . < j _ { n + 1 } )
$$

of length $n + 1$ , or both.

This time the application of the pigeon-hole principle is not immediate. Associate to cach $a _ { i }$ the number $t _ { i }$ which is the length of a longest increasing subsequence starting at $a _ { i }$ . If $t _ { i } \ \geq \ r n + 1$ for some $i$ , then we have an increasing subsequence of length $m + 1$ , Suppose then that $t _ { i } \leq m$ for all $i$ The function $f : a _ { i } \longmapsto t _ { i }$ mapping $\{ a _ { 1 } , \dotsc , a _ { m \uparrow \downarrow + 1 } \}$ to $\{ 1 , \ldots , m \}$ tells us by (1) that there is some $s \in \{ 1 , \ldots , m \}$ such that $f ( \boldsymbol { a } _ { i } ) = \mathcal { s }$ for $\textstyle { \frac { m n } { m } } + 1 = n + 1$ numbers $a _ { i }$ Let $a _ { j _ { 1 } } , a _ { j _ { 2 } } , \dotsc , a _ { j _ { n + 1 } } \ ( j _ { 1 } < \dotsc < j _ { n - 1 } )$ be these numbers. Now look at two consccutive numbers $a _ { j _ { i } }$ , $a _ { j _ { i + 1 } }$ . If $a _ { j _ { i } } ~ < ~ a _ { j _ { i + 1 } }$ , then we would obtain an increasing subsequence of length s starting at $a _ { j , + }$ , and consequently an increasing subscquence of length $s + 1$ starting at $a _ { j _ { v } }$ , which cannot be since $f ( a _ { j _ { i } } ) = s$ We thus obtain a decreasing subsequence $a _ { j _ { 1 } } > a _ { j _ { 2 } } > . . , > a _ { j _ { n + 1 } }$ of length $n + 1$ .

The reader may have fun in proving that for mnn numbers the statement remains no longer true in general.

This simple-sounding result on monotone subsequences has a highly nonobvious consequence on the dimension of graphs. We don't need here the notion of dimension for general graphs, but only for complete graphs $K _ { n }$ . It can bc phrased in the following way. Let $N = \{ 1 , \ldots , n \}$ , $n \geq 3$ ,and consider $m$ permutations $\pi _ { 1 } , \ldots , \pi _ { \gamma \eta 2 }$ of $N$ . We say that the permutations $\pi _ { i }$ represent $K _ { n }$ if to every three distinct numbers $i , j , k$ there exists a permutation $\pi$ in which $k$ comes after both $i$ and $j$ The dimension of $K _ { \pi }$ is then the smallest $m$ for which a representation $\pi _ { 1 } , \ldots , \pi _ { \gamma \pi }$ exists.

As an example we have $\dim ( K _ { 3 } ) = 3$ since any one of the three numbers must come last, as in $ \pi _ { 1 } = \{ 1 , 2 , 3 \}$ , $\pi _ { 2 } = ( 2 , 3 , 1 )$ , $\pi _ { 3 } = ( 3 , 1 , 2 )$ .What about $1 5 4 ?$ Note first $\dim ( K _ { n } ) \ \leq \ \dim ( K _ { n + 1 } )$ just delete $n + 1$ in a representation of $K _ { n + 1 }$ . So, $\mathrm { d i m } ( K _ { 4 } ) \ge 3$ , and, in fact, $\dim ( K _ { 4 } ) = 3$ , by taking

$$
\pi _ { 1 } = ( 1 , 2 , 3 , 4 ) , \quad \pi _ { 2 } = ( 2 , 4 , 3 , 1 ) , \quad \pi _ { 3 } = ( 1 , 4 , 3 , 2 ) .
$$

It is not quite so easy to prove $\dim ( K _ { 5 } ) = 4$ , but then, surprisingly, the dimension stays at $^ 4$ up to $ \ n = 1 2$ ,while $\mathrm { d i m } ( \bar { K } _ { 1 3 } ) = \bar { \mathfrak { z } }$ So $\mathrm { d i m } \langle K _ { \tau _ { k } } \rangle$ seems to be a pretty wild function. Well, it is not! With $\mathscr { n }$ going to infinity, $\mathrm { ( i m } ( K _ { \eta _ { 2 } } )$ is, in fact, a very well-behaved functon — and the key for finding a lower bound is the pigeon-hole principle. We claim

$$
\dim ( K _ { n } ) \ \geq \ \log _ { 2 } \log _ { 2 } n .
$$

Since, as we have seen, $\mathrm { d i m } ( K _ { n } )$ is a monotone function in $n$ , it suffices to verify (2) for $n = 2 ^ { 2 ^ { P } } + 1$ , that is, we have to show that

$$
\dim ( K _ { n } ) \ \geq \ p + 1 \qquad { \mathrm { f o r } } \quad n = 2 ^ { 2 ^ { p } } + 1 .
$$

Suppose, on the contrary, $\mathrm { d i m } ( K _ { n } ) \le p$ , and let $\pi _ { 1 } , \ldots , \pi _ { p } ,$ be representing permutations of $N = \{ 1 , 2 , \dots , 2 ^ { 2 ^ { p } } + 1 \}$ . Now we use our result on monotone subsequences $p$ times. In $\pi _ { 1 }$ there cxists a monotone subsequence $A _ { 1 }$ of length $2 ^ { \bar { 2 } ^ { \prime \prime } { } ^ { - 1 } } + 1$ (t ds omate whetecasing r decig). Look at this set $A _ { 1 }$ in $\pi _ { 2 }$ . Using our result again, wc find a monotonc subsequence A2 of A in π2 of length 2 , and $A _ { 2 }$ is, of course, also monotone in $\pi _ { 1 }$ . Continuing, we eventually find a subsequence $A _ { p }$ of size $2 ^ { 2 ^ { 0 } } + 1 = 3$ which is monotone in all permutations $\pi _ { i }$ .Let $A _ { p } = \left( a , b , c \right)$ , then either $a < b < c$ or $a > b > c$ in all $\pi _ { i }$ But this cannot be, since there must be a permutation where $b$ comes after $a$ and $c$ . □

The right asymptotic growth was provided by Joel Spencer (upper bound) and by Erdös, Szemerédi and Trotter (lower bound):

$$
\dim ( K _ { n } ) \ = \ \log _ { 2 } \log _ { 2 } n + ( { \frac { 1 } { 2 } } + o ( 1 ) ) \log _ { 2 } \log _ { 2 } \log _ { 2 } n .
$$

But this is not thc whole story: Very recently, Morris and Hoten found a method which, in principlc, establishes the precise value of $\mathrm { d i m } ( K _ { n } )$ . Using their result and a computer one can obtain the values given in the margin. This is truly astounding! Just consider how many permutations of size 1422564 there are. How does onc dccide whether 7 or 8 of them are required to represent $K _ { 1 4 2 2 5 6 4 } ?$

# 3. Sums

Paul Erdós attributes the following nice application of the pigcon-hole principle to Andrew Vázsonyi and Marta Sved:

Claim. Suppose we are given n integers $a _ { 1 } , \dots , a _ { r } $ which need not be distinct. Then there is always a set of consecutive numbers $a _ { k + 1 } , a _ { k + 2 } , \ldots , a _ { \ell } .$ whose sum $\sum \limits _ { i = k + 1 } ^ { l } a _ { i }$ is a multiple of n.

π1:1 2 3 5 6 7 8 910 11 12 4   
π2: 2 3 4 8 7 6 5 12 11 10 9 1   
π3:3 4 1 11 12 9 10 6 5 8 7 2   
π4:4 1 210 91211 7 8 5 6 3

These four permutations represent $K _ { 1 2 }$

$$
\begin{array} { r l } & { \dim ( K _ { n } ) \leq 4 \iff n \leq 1 2 } \\ & { \dim ( K _ { n } ) \leq 5 \iff n \leq 8 1 } \\ & { \dim ( K _ { n } ) \leq 6 \iff n \leq 2 6 4 6 } \\ & { \dim ( K _ { n } ) \leq 7 \iff n \leq 1 4 2 2 5 6 4 } \end{array}
$$

For the proof we set $N = \{ 0 , 1 , \ldots , n \}$ and $R = \{ 0 , 1 , \ldots , n - 1 \}$ . Consider the map $f : N \to R$ where $f ( m )$ is the remainder of $a _ { 1 } + \ldots + a _ { m }$ upon division by $\pmb { \eta } _ { e }$ . Since $| N | = n + 1 > n = | R | .$ , it follows that there are two sums ${ \mathfrak { a } } _ { 1 } + \ldots + { \mathfrak { a } } _ { k }$ , $a _ { 1 } + \ldots + a _ { \ell } ( k < \ell )$ with the same remainder, where the first sum may be the empty sum denoted by (. It follows that

has remainder 0 - end of proof.

![](images/96b1f4968c0b4ce37030bac5c4626fda56a1fe7a0b3206418bdd6efa7e1bda3e.jpg)

$$
\sum _ { i = k + 1 } ^ { \ell } a _ { i } = \sum _ { i = 1 } ^ { \ell } a _ { i } - \sum _ { i = 1 } ^ { k } a _ { i }
$$

Lct us turn to the scond principle: counting in two ways. By this we mean the following.

# Double counting.

Suppose that we are given two finite sets $R$ and $C$ and $a$ subset $S \subseteq R \times C$ Whenever $( p , q ) \in S$ , then we say $\pmb { \mathscr { p } }$ and $q$ are incident. If $r _ { p }$ denotes the number of elements that are incident to $p \in R ,$ and $c _ { \eta }$ denotes the number of elements that are incident to $q \in C ,$ then

$$
\sum _ { p \in R } r _ { p } = | S | = \sum _ { q \in C } c _ { q } .
$$

Again, there is nothing to prove. The first sum classifies the pairs in $S$ according to the first entry, while the second sum classifies the same pairs according to the second entry.

There is a useful way to picture the set $S$ Consider the matrix $A = ( i \ i _ { p y } )$ the incidence matrix of $S$ , where the rows and columns of $A$ are indexed by the elements of $R$ and $C$ , respectively, with

$$
a _ { p q } = \left\{ \begin{array} { l l } { 1 } & { \mathrm { ~ i f ~ } ( p , q ) \in S } \\ { \mathfrak { h } } & { \mathrm { ~ i f ~ } ( p , q ) \notin S . } \end{array} \right.
$$

With this set-up, $r _ { p }$ is the sum of the $p$ -th row of $A$ and $c _ { q }$ is the sum of the $q$ -th column. Hence the first sum in (3) adds the entries of $A$ (that is, counts the elements in $S$ )by rows, and the second sum by columns.

The following cxample should make this correspondence clear. Let $R =$ $\mathcal { ( ) } = \{ 1 . 2 , \ldots , 8 \}$ , and set $S = \{ ( i , j ) : i$ divides $j \}$ , We then obtain the matrix in the margin, which only displays the I's.

# 4. Numbers again

Look at the table on the left. The number of $\mathbf { l } \ \mathbf { \bar { s } }$ in column $j$ is precisely the number of divisors of $j$ ; let us denote this number by $t ( j )$ . Let us ask how

large this number $i ( j )$ is on the average when $j$ ranges from 1 to $\mathcal { U }$ .Thus, we ask for the quantity

$$
\bar { t } ( n ) = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \ell ( j ) .
$$

How large is $i ( \pi )$ for arbitrary $\hbar \vec { \zeta }$ At first glance, this seems hopeless. For prime numbers $p$ we have $t ( p ) = 2$ , while for $2 ^ { k }$ we obtain a large number $l ( 2 ^ { k } ) = k + 1$ So, $l ( \pi )$ is a wildly jumping function, and we surmise that the same is true for $\bar { t } ( \eta t )$ . Wrong guess, the opposite is true! Counting in two ways provides an unexpected and simple answer.

Consider the matrix $\varLambda$ (as above) for the integers 1 up to n. Counting by columns we get $\sum \limits _ { j = 1 } ^ { \pi } t ( j )$ How many I's are in row $i ?$ Easy enough, the I's correspond to the multiples of $i ; ~ 1 i , 2 i , \ldots$ ,and the last multiple not exceeding $n$ is $\lfloor \frac { n } { i } \rfloor i$ Hence we obtain

$$
{ \overline { { \ell } } } ( n ) = { \frac { 1 } { n } } \sum _ { j = 1 } ^ { n } \ell ( j ) = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } \left\lfloor { \frac { n } { i } } \right\rfloor \leq { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } { \frac { n } { i } } = \sum _ { i = 1 } ^ { n } { \frac { 1 } { i } } ,
$$

where the error in each summand, when passing from $[ \frac { n } { i } ] 1 0 \frac { \pi } { i }$ , is less than 1. Now the last sum is the $n$ -th harmonic number $H _ { n }$ , so we obtain $H _ { n } - 1 < \bar { t } ( n ) < H _ { n s }$ , and together with the estimates of $H _ { n }$ on page 11 this gives

$$
\frac { n | 1 2 3 4 5 6 7 8 } { \overline { { t } } ( n ) | 1 \frac { 3 } { 2 } \frac { 5 } { 3 } 2 2 \frac { 7 } { 3 } \frac { 1 6 } { 7 } \frac { 5 } { 2 } }
$$

The first few values of $\bar { t } ( \gamma _ { t } )$

$$
\log n - 1 < H _ { n } - 1 - \frac { 1 } { n } < \bar { t } ( n ) < H _ { n } < \log n + 1 .
$$

Thus we have proved the remarkable result that, while $t ( \mathfrak { N } )$ is totally erratic, the average $t ( \eta )$ behaves beautifully: It differs from log $\gamma _ { 2 }$ by less than 1.

# 5. Graphs

Let $G$ be a finite simple graph with vertex set $V$ and edge set $E$ . We have defined in Chapter 11 the degree $d ( v )$ of a vertex $v$ as the number of edges which have $\left. \begin{array} { r l } \end{array} \right.$ as an end-vertex. In the example of the figure, the vertices $1 , 2 , \ldots 7$ have degrees 3, 2, 4, 3, 3. 2, 3, respectively.

Almost every book in graph theory starts with the following result (that we have already encountered in Chapters 11 and 17):

$$
\sum _ { \mathfrak { n } ^ { \prime } \in \mathcal { V } } d ( \nu ) \ = \ 2 | E | .
$$

For the proof consider $S \subseteq V \times E$ , where $S$ is the set of pairs $( v , \epsilon )$ such 1hat $v \in V$ is an end-vertex of $\mathcal { E } \in E$ Counting $S$ in two ways gives on the one hand $\sum v \ c \mathcal { V } ^ { \textit { d } ( v ) }$ , since every vertex contribules $d ( v )$ to the count, and on the other hand $2 | E |$ , since every edge has two ends.

As simple as the result (4) appears, it has many important consequences, some of which will be discussed as we go along. We want to single out in

![](images/3d7eeca9b40b9bcb01530695116204fc44893559b7de3f896fd801451e4404bc.jpg)

this section the following beautiful application to an extremal problem on graphs. Here is the problem:

Suppose $\hat { G } ~ = ~ ( V , E )$ has $n$ vertices and contains no cycle of length 4 (denoted by $C _ { 1 }$ ), that is, no subgraph . How many edges can $G$ have at most?

As an example, the graph in the margin on 5 vertices contains no 4-cycle and has 6 edges. The reader may easily show that on 5 vertices the maximal number of edges is 6, and that this graph is indeed the only graph on 5 vertices with 6 edges that has no 4-cycle.

Let us tackle the general problem. Let $G$ be a graph on $n$ vertices without a 4-cycle. As above we denote by $d ( u )$ the degree of $\mathscr { W } .$ Now we count the following set $S$ in two ways: $S$ is the set of pairs $\left( \mathfrak { u } , \{ \mathfrak { v } , \mathfrak { w } \} \right)$ where $u$ is adjacent to $\mathcal { V }$ and to $w$ ,with $v \neq u$ . In other words, we count all occurrences of

W

Summing over $u$ we find $\begin{array} { r } { | S | ~ = ~ \sum _ { u \in V } { \binom { t ! ( u ) } { 2 } } } \end{array}$ On the other hand, every pair $\{ v , w \}$ has at most one common neighbor (by the $C _ { 4 }$ -condition). Hence $| S | \leq { \binom { n } { 2 } }$ , and we conclude

$$
\sum _ { u \in V } { \binom { d ( u ) } { 2 } } \leq { \binom { n } { 2 } }
$$

or

$$
\sum _ { u \in V } d ( u ) ^ { 2 } \leq n ( n - 1 ) + \sum _ { u \in V } d ( u ) .
$$

Next (and this is quite typical for this sort of extremal problems) we apply the Cauchy-Schwarz inequality to the vectors $\big ( d ( u _ { 1 } ) , \ldots , d ( u _ { n } ) \big )$ and $( 1 , 1 , \ldots , 1 )$ , obtaining

$$
\left( \sum _ { u \in V } d ( u ) \right) ^ { 2 } \ \leq \ n \sum _ { u \in V } d ( u ) ^ { 2 } ,
$$

and hence by (5)

$$
\Bigl ( \sum _ { u \subset V } d ( u ) \Bigr ) ^ { 2 } \ \leq \ n ^ { 2 } ( n - 1 ) + n \sum _ { u \in V } d ( u ) .
$$

Invoking (4) we find

$$
4 | E | ^ { 2 } \ \leq \ n ^ { 2 } ( n - 1 ) + 2 n | E |
$$

or

$$
| E | ^ { 2 } - { \frac { \pi } { 2 } } | E | - { \frac { \pi ^ { 2 } ( n - 1 ) } { 1 } } \leq 0 .
$$

Solving the corresponding quadratic equation we thus obtain the following result of Istvan Reiman.

Theorem. If the graph $G$ on n vertices contains no 4-cycles, then

$$
| E | \ \leq \ \left\lfloor { \frac { n } { 4 } } \left( 1 + { \sqrt { 4 n - 3 } } \right) \right\rfloor .
$$

For $ \ n \ = \ 5$ this gives $| E \} \leq 6$ , and the graph above shows that cquality can hold.

Counting in two ways has thus produced in an casy way an upper bound on the number of edges. But how good is the bound (6) in general? The following bcautiful example [2] [3] [6] shows that it is almost sharp. As is often the case in such problems, finite geometry leads the way.

In presenting the example we assume that the reader is familiar with the finite field $\mathbb { Z } _ { \mathfrak { p } }$ of integers modulo a prime $p$ (see page 18). Consider the 3-dimensional vector space $X$ over $\mathbb { Z } _ { \mathfrak { p } }$ . We construct from $X$ the following graph $G _ { p }$ . The vertices of $C _ { p }$ are the one-dimensional subspaces $[ v ] \ : = \ { \mathsf { s p a n } } _ { \mathbb { Z } _ { \mathtt { p } } } \{ v \}$ , $\mathbf { 0 } ~ \neq ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm \pm ~ \pm ~ \pm ~ \pm ~ \pm ~ \pm \pm ~ \pm ~ \pm ~ \pm ~ \pm \pm ~ \pm ~ \pm \pm ~ \pm ~ \pm ~ \pm \pm ~ \pm ~ \pm \pm ~ \pm ~ \pm \pm ~ \pm \pm ~ \pm \pm ~ \pm \pm ~ \pm \pm ~ \pm \pm ~ \pm \pm ~ \pm \pm \pm ~ \pm \pm ~ \pm \pm \pm ~ \pm \pm \pm \pm \pm ~ \pm \pm \pm \pm \pm \pm ~ \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm \pm $ , and we connect two such subspaces $[ v ] , [ w ]$ by an edge if

$$
\langle v , w \rangle = w _ { 1 } w _ { 1 } + v _ { 2 } w _ { 2 } + v _ { 3 } w _ { 3 } = 0 .
$$

Note that it does not matter which vector $\neq 0$ we take from the subspace. In the language of geometry, the vertices are the points of the projective plane over $\mathbb { Z } _ { \mathfrak { p } }$ , and $[ w ]$ is adjacent to $\left[ { \pmb v } \right]$ if w lies on the polar line of $\pmb { v }$ .

As an example, the graph $G _ { 2 }$ has no 4-cycle and contains 9 edges, which almost reaches the bound 10 given by (6). We want to show that this is true for any prime $p$ .

Let us first prove that $G _ { p }$ satisfies the $C _ { 1 }$ -condition. If $[ u ]$ is a common neighbor of $[ v ]$ and $\{ w \}$ , then $\pmb { u }$ is a solution of the linear equations

$$
\begin{array} { r l } { v _ { 1 } x + v _ { 2 } y + v _ { 3 } z } & { = 0 } \\ { w _ { 1 } x + w _ { 2 } y + w _ { 3 } x } & { = 0 . } \end{array}
$$

Since $\pmb { v }$ and $\mathbf { w }$ are linearly independent, we infer that the solution space has dimension 1, and hence that the common neighbor $[ u ]$ is unique.

Next, we ask how many vertices $G _ { \phi }$ has. It's double counting again. The space $X$ contains ${ { \underline { { { \mathfrak { x } } } } } ^ { 3 } } \mathrm { ~ - ~ } 1$ vectors $\neq 0$ . Since every one-dimensional subntns   1 veors = 0, we r hat X has $\frac { p ^ { 3 } - 1 } { p - 1 } = p ^ { 2 } + p + 1$ one-dimensional subspaces, that is, $G _ { p }$ has $n = p ^ { 2 } + p ^ { \cdot } + 1$ vertices. Similarly, any two-dimensional subspace contains $p ^ { 2 } - 1 \mathrm { v e c t o r s } \neq \mathbf { 0 } .$ , and hence $\frac { { \mathfrak { p } } ^ { 2 } - 1 } { { \mathfrak { p } } - 1 } = { \mathfrak { p } } + 1$ one-dimensional subspaces.

It remains to determine the number of edges in $G _ { y }$ , or, what is the same by (4), the degrees. By the construction of $G _ { p }$ , the vertices adjacent to $[ u ]$ are the solutions of the equation

$$
u _ { 1 } x + u _ { 2 } y + u _ { 3 } z = 0 .
$$

The solution space of (7) is a two-dimensional subspace, and hence there are ${ \mathfrak { h } } + 1$ vertices adjacent to $[ { \pmb u } ]$ But beware, it may happen that $\pmb { u }$ itself is a solution of (7). In this case there are only $p$ vertices adjacent to $[ u ]$ .

(0, 0, 1)   
(1,0,1) (0, 1, 1) (1, 1, 1)   
(1,0,0) (1,1,0) (0, 1, 0\$

The graph $G _ { 2 }$ : its vertices are all seven nonzero triples $( x , y , z )$ .

In summary, we obtain the following result: If $\textbf { \em u }$ lies on the conic given by $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 0$ , then $d ( [ u ] ) = p$ , and, if not, then $d ( [ u ] ) = p + 1$ So it remains to find the number of one-dimensional subspaces on the conic

$$
x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 0 .
$$

Let us anticipate the result which we shall prove in a moment.

Claim. There are precisely $p ^ { 2 }$ solutions $( x , y , z )$ of the equation $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 0$ and ence (excetig the ero olutin) preisely ${ \frac { p ^ { 2 } - 1 } { p - 1 } } = p + 1$ vertices in $G _ { p }$ ofdegree $p$

With this, we complete our analysis of $G _ { p }$ There are $p + 1$ vertices of degree $p$ , hence $( p ^ { 2 } + p + 1 ) - ( p + 1 ) \stackrel { } { = } p ^ { 2 }$ vertices of degree $p + 1$ . Using (4), we obtain

$$
\begin{array} { l l l } { \displaystyle | E | } & { = } & { \displaystyle \frac { ( p + 1 ) p } { 2 } + \frac { p ^ { 2 } ( p + 1 ) } { 2 } = \frac { ( p + 1 ) ^ { 2 } p } { 2 } } \\ { \displaystyle } & { = } & { \displaystyle \frac { ( p + 1 ) p } { 4 } ( 1 + ( 2 p + 1 ) ) = \frac { p ^ { 2 } + p } { 4 } ( 1 + \sqrt { 4 p ^ { 2 } + 4 p + 1 } ) . } \end{array}
$$

Setting $n = p ^ { 2 } + p + 1$ , the last equation reads

$$
\left| E \right| = { \frac { n - 1 } { 4 } } ( 1 + { \sqrt { 4 n - 3 } } ) ,
$$

and we see that this almost agrees with (6).

Now to the proof of the claim. The following argument is a beautiful application of linear algebra involving symmetric matrices and their eigenvalues. We will encounter the same method in Chapter 34, which is no coincidence: both proofs are from the same paper by Erdôs, Rényi and Sós.

We represent the one-dimensional subspaces of $X$ as before by vectors $v _ { 1 } , v _ { 2 } , \ldots , v _ { p ^ { 2 } + p + 1 }$ , any two of which are linearly independent. Similarly, we may represent the two-dimensional subspaces by the same set of vectors, where the subspace corresponding to $\pmb { u } = ( u _ { 1 } , u _ { 2 } , u _ { 3 } )$ is the set of solutions of the equation $u _ { 1 } x + u _ { 2 } y + u _ { 3 } z = 0$ as in (7). (Of course, this is just the duality principle of linear algebra.) Hence, by (7), a one-dimensional subspace, represented by ${ \mathbf { } } v _ { i }$ , is contained in the two-dimensional subspace, represented by ${ \pmb v } _ { j }$ , if and only if $\langle { \pmb v } _ { i } , { \pmb v } _ { j } \rangle = 0$ .

$$
A = { \left( \begin{array} { l l l l l l l l } { 0 } & { 1 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 1 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 1 } & { 0 } \end{array} \right) }
$$

The matrix for $G _ { 2 }$

Consider now the matrix $A = \left( a _ { i j } \right)$ of size $( p ^ { 2 } + p + 1 ) \times ( p ^ { 2 } + p + 1 )$ , defined as follows: The rows and columns of A correspond to $\pmb { v } _ { 1 } , \dotsc , \pmb { v } _ { p ^ { 2 } + p + 1 }$ (we use the same numbering for rows and columns) with

$$
a _ { i j } : = \left\{ \begin{array} { l l } { 1 } & { \mathrm { i f } \left. v _ { i } , v _ { j } \right. = 0 , } \\ { 0 } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

$A$ is thus a real symmetric matrix, and we have $a _ { i i } = 1$ if $\langle { \pmb v } _ { i } , { \pmb v } _ { i } \rangle = 0$ , that is, precisely when ${ \pmb v } _ { i }$ lies on the conic $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 0$ Thus, all that remains to show is that

$$
\operatorname { t r a c e } A = p + 1 .
$$

From linear algebra we know that the trace equals the sum of the eigenvalues. And here comes the trick: While $A$ looks complicated, the matrix $A ^ { 2 }$ is easy to analyze. We note two facts:

Any row of $\varLambda$ contains precisely $p + 1$ 1's. This implies that $p + 1$ is an eigenvalue of $A$ , since $A { \bf 1 } = ( p + 1 ) { \bf 1 }$ , where 1 is the vector consisting of 1's.   
For any two distinct rows $v _ { i } , v _ { j }$ there is exactly one column with a 1 in both rows (the column corresponding to the unique subspace spanned by $v _ { i } , v _ { j } )$ .

Using these facts we find

$$
A ^ { 2 } = \left( \begin{array} { l l l l l } { { p + 1 } } & { { 1 } } & { { \cdots } } & { { 1 } } \\ { { 1 } } & { { p + 1 } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { \ddots } } \\ { { \vdots } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { \cdots } } & { { } } & { { p + 1 } } \end{array} \right) ~ = ~ p ~ I ~ + ~ J ,
$$

where $I$ is the identity matrix and $J$ is the all-ones-matrix. Now, $\boldsymbol { J }$ has the eigenvalue $p ^ { 2 } + p + 1$ (of multiplicity 1) and 0 (of multiplicity $p ^ { 2 } + p )$ . Hence $A ^ { 2 }$ has the eigenvalues $p ^ { 2 } + 2 p + 1 = ( p + 1 ) ^ { 2 }$ of multiplicity I and $p$ of multiplicity $\boldsymbol { p } ^ { 2 } + \boldsymbol { p }$ Since $A$ is real and symmetric, hence diagonalizable, we find that $\varLambda$ has the eigenvalue $p + 1$ or $- ( p + 1 )$ and $p ^ { 2 } + p$ eigenvalues $\pm \sqrt { \boldsymbol { p } }$ , From Fact 1 above, the first eigenvalue must be $p + 1$ Suppose that $\sqrt { p }$ has multiplicity $r$ , and $- \sqrt { I } ^ { \rangle }$ multiplicity $s$ ,then

$$
\mathrm { t r a c e } \ : \mathcal { A } = ( p + 1 ) + r \sqrt { p } - s \sqrt { p } .
$$

But now we are home: Since the trace is an integer, we must have $r = s$ so trace $A = p + 1$ . □

# 6. Sperner's Lemma

In 1911, Luitzen Brouwer published his famous fixed point theorem:

Every continuous function $f \colon B ^ { n } \longrightarrow B ^ { n }$ of an $n$ -dimensional ball to itself has a fixed point (a point $\pmb { x } \in B ^ { \pi }$ with ${ \pmb f } ( { \pmb x } ) = { \pmb x } ,$ .

For dimension 1, that is for an interval, this follows easily from the intermediate value theorem, but for higher dimensions Brouwer's proof needed some sophisticated machinery. It was therefore quite a surprise when in 1928 young Emanuel Sperner (he was 23 at the time) produced a simple combinatorial result from which both Brouwer's fixed point theorem and the invariance of the dimension under continuous bijective maps could be deduced. And what's more, Sperner's ingenious lemma is matched by an equally beautiful proof — it is just double counting.

![](images/18dd05b6f8b10a690d5b2b20a1a282599d86d0088abb0082fd48931113e81ae7.jpg)

The triangles with three different colors are shaded

![](images/76eb02c09d9f747e863b4fad6c3740e00d29062255e2c6bc0b931670761b3069.jpg)

We discuss Sperner's lemma, and Brouwer's theorem as a consequence, for the first interesting case, that of dimension $\eta = 2$ The reader should have no difficulty to extend the proofs to higher dimensions (by induction on the dimension).

# Sperner's Lemma.

Suppose that some "big" triangle with vertices $V _ { 1 }$ $, \ V _ { 2 } , \ V _ { 3 }$ is triangulated (that is, decomposed into $\pmb { a }$ finite number of "small" triangles that fit together edge-by-edge).

Assume that the vertices in the triangulation get "colors" from the set $\{ 1 , 2 , 3 \}$ such that $V _ { i }$ receives the color $i$ (for each i), and only the colors $i$ and $j$ are used for vertices along the edge from $V _ { i }$ 10 $V _ { j }$ $( \hat { f o r \ i } \ne j )$ , while the interior vertices are colored arbitrarily with 1, 2 or 3.

Then in the triangulation there must be a small "tricolored" triangle, which has all three different vertex colors.

Proof. We will prove a stronger statement: the number of tricolored triangles is not only nonzero, it is always odd.

Consider the dual graph to the triangulation, but don't take all its edges — only those which cross an edge that has endvertices with the (different) colors 1 and 2. Thus we get a "partial dual graph" which has degree 1 at all vertices that correspond to tricolored triangles, degree 2 for all triangles in which the two colors 1 and 2 appear, and degree 0 for triangles that do not have both colors 1 and 2. Thus only the tricolored triangles correspond to vertices of odd degree (of degree 1).

However, the vertex of the dual graph which corresponds to the outside of the triangulation has odd degree: in fact, along the big edge from $V _ { 1 }$ to $V _ { 2 }$ , there is an odd number of changes between 1 and 2. Thus an odd number of edges of the partial dual graph crosses this big edge, while the other big edges cannot have both 1 and 2 occurring as colors.

Now since the number of odd vertices in any finite graph is even (by equation (4)), we find that the number of small triangles with three different colors (corresponding to odd inside vertices of our dual graph) is odd.

With this lemma, it is easy to derive Brouwer's theorem.

Proof of Brouwer's fixed point theorem $( \operatorname { f o r } n = 2 )$ . Let $\Delta$ be the triangle in $\mathbb { R } ^ { 3 }$ with vertices $e _ { 1 } = \{ 1 , 0 , 0 \}$ $e _ { 2 } = \{ 0 , 1 , 0 \}$ , and $\mathbf { e } _ { 3 } = \{ 0 , 0 , 1 \}$ It suffices to prove that every continuous map $f \colon \Delta \longrightarrow \Delta$ has a fixed point, since $\Delta$ is homeomorphic to the two-dimensional ball $B _ { 2 }$ .

We use $\delta ( T )$ to denote the maximal length of an edge in a triangulation $T$ . One can easily construct an infinite sequence of triangulations $T _ { 1 } , T _ { 2 } , \dots$ of $\Delta$ such that the sequence of maximal diameters $\delta ( T _ { k } )$ converges to (. Such a sequence can be obtained by explicit construction, or inductively, for example by taking $T _ { k + 1 }$ to be the barycentric subdivision of $T _ { k }$ .

For each of these triangulations, we define a 3-coloring of their vertices $\pmb { v }$ by setting $\lambda ( v ) : = \operatorname* { m i n } \{ i : f ( v ) _ { i } < \upsilon _ { i } \}$ , that is, $\lambda ( v )$ is the smallest index $i$ such that the $i$ -th coordinate of $f ( v ) - v$ is negative. Assuming that $f$ has no fixed point, this is well-defined. To see this, note that every $v \in \Delta$ lies in the plane $x _ { 1 } + x _ { 2 } + x _ { 3 } = 1$ , hence $\textstyle \sum _ { i } { \mathfrak { t } } _ { i } = 1$ .So if $f ( v ) \neq v$ , then at least one of the coordinates of ${ f } ( v ) - v$ must be negative (and at least one must be positive).

Let us chcck that this coloring satisfies the assumptions of Sperner's lemma. First, the vertex $e _ { i }$ must receive color $i$ , since the only possible negative component of $f ( e _ { i } ) - e _ { i }$ is the $i$ -th component. Moreover, if $\pmb { \imath } )$ lies on the edge opposite to $e _ { i }$ , then $\iota \iota _ { i } = 0$ , so the $i$ -th component of $f ( v ) - v$ cannot be negative, and hence $\pmb { v }$ does not get the color $i$ .

Sperner's lemma now tells us that in cach triangulation $\tau _ { k }$ there is a tricolored triangle $\{ \boldsymbol { v } ^ { k : 1 } , \boldsymbol { v } ^ { k : 2 } , \boldsymbol { v } ^ { k : 3 } \}$ with $\lambda ( \pmb { v } ^ { k : i } ) ~ \approx ~ i$ The sequence of points $( v ^ { k : 1 } ) _ { k \geq 1 }$ need not converge, but since the simplex $\Delta$ is compact somc subsequence has a limit point. After replacing the sequence of triangulations $\tau _ { k }$ by the corresponding subsequence (which for simplicity wc also denote by $\tau _ { k }$ ) we can assumc that $( \pmb { v } ^ { k : 1 } ) _ { k }$ converges to a point $v \in \Delta$ Now the distance of $\scriptstyle v ^ { k : 2 }$ and $\scriptstyle v ^ { k : 3 }$ from $\scriptstyle v ^ { k : 1 }$ is at most the mesh length $\delta ( T _ { k } )$ , which converges to O. Thus the sequences $( v ^ { k ; 2 } )$ and $( \pmb { v } ^ { k : 3 } )$ converge to the same point $\pmb { v }$ .

But where is $f ( v ) ^ { \prime }$ ? We know that the first coordinate $f ( v ^ { k : 1 } )$ is smaller than that of $v ^ { k : 1 }$ for all $k$ Now since $f$ is continuous, we derive that the first coordinate of $f ( v )$ is smaller or cqual to that of $\pmb { v }$ . The same reasoning works for the second and third coordinates. Thus none of the coordinates of $f ( v ) - v$ is positive -— and we have already seen that this contradicts the assumption $f ( v ) \neq v$ . □

# References

[1] L. E. J. BRoUwER: Über Abbildungen von Mannigfaltigkeiten, Math. Annalen 71 (1912), 97-115.   
[2] W. G. BRown: On graphs that do not contain a Thomsen graph. Canadian Math, Bull. 9 (1966), 281-285.   
[3] P. ERDÖs, A. RÉNYI & V. SÓS: On a problem of graph theory, Studia Sci. Math. Hungar. 1 (1966), 215-235.   
[4] P. ERDÖs & G. SZEKERES: A combinatorial problem in geometry, Compositio Math. (1935). 463-470.   
[5] S. HoTEN & W. D. MoRRIS: The order dimension of the complete graph, Discrete Math. 201 (1999), 133- 139.   
[6] I. REiMAN: Uber ein Problem von K. Zarankiewicz, Acta Math. Acad. Sci. Hungar. 9 (1958), 269-273.   
17| J. SPENCER: Minimal scrambling sers of simple orders, Acta Math. Acad. Sci. Hungar. 22 (1971), 349-353.   
[8] E. SPERNER: Neuer Beweis für die Invarianz der Dimensionszahl und des Gebietes, Abh. Math. Sem. Hamburg 6 (1928), 265-272.   
|9| W. T. TRoTTER: Combinatorics and Partially Ordered Sets: Dimension Theory, John Hopkins University Press, Baltimore and London 1992.

# Three famous theorems on finite sets

# Chapter 23

In this chapter we are concerned with a basic theme of combinatorics: properties and sizes of special families $\mathcal { F }$ of subsets of a finite set $N =$ $\{ 1 , 2 , \ldots , n \}$ . We start with two results which are classics in the field: the theorems of Sperner and of Erdôs-Ko-Rado. These two results have in common that they were reproved many times and that each of them initiated a new field of combinatorial set theory. For both theorems, induction seems to be the natural method, but the arguments we are going to discuss are quite different and truly inspired.

In 1928 Emanuel Sperner asked and answered the following question: Suppose we are given the set $N = \{ 1 , 2 , \dots , n \}$ Call a family $\mathcal { F }$ of subsets of $N$ an antichain if no set of $\mathcal { F }$ contains another set of the family $\mathcal { F }$ What is the size of a largest antichain? Clearly, the family $\mathcal { F } _ { k }$ of all $k$ -sets satisfies the antichain property with $\textstyle | { \mathcal F } _ { k } | = { \binom { n } { k } }$ . Looking at the maximum of the b  sine $\textstyle { \binom { n } { \lfloor n / 2 \rfloor } } = \operatorname* { m a x } _ { k } { \binom { n } { k } }$ no larger ones.

Theorem $n$ set is $\scriptstyle { { \binom { n } { \lfloor n / 2 \rfloor } } }$

Proof. Of the many proofs the following one, due to David Lubell, is probably the shortest and most elegant. Let $\mathcal { F }$ be an arbitrary antichain. Then we have to show |F| ≤ (n/2. The key to the proof is that we consider chains of subsets $\emptyset = { \dot { C } } _ { 0 } { \overset { . . . } { \subset } } C _ { 1 } \subset C _ { 2 } \subset . . . \subset C _ { n } = N .$ , where $| C _ { i } | = i$ for $i = 0 , \ldots , n$ . How many chains are there? Clearly, we obtain a chain by adding one by one the elements of $N$ , so there are just as many chains as there are permutations of $N$ , namely $n !$ Next, for a set $A \in { \mathcal { F } }$ we ask how many of these chains contain $A$ Again this is easy. To get from $\varnothing$ to $A$ we have to add the elements of $A$ one by one, and then to pass from $A$ to $N$ we have to add the remaining elements. Thus if $A$ contains $k$ elements, then by considering all these pairs of chains linked together we see that there are precisely $k ! ( n - k ) !$ such chains. Note that no chain can pass through two different sets $A$ and $B$ of $\mathcal { F }$ , since $\mathcal { F }$ is an antichain.

To complete the proof, let $m _ { k }$ be the number of $k$ -sets in $\mathcal { F }$ Thus $| { \mathcal { F } } | =$ $\scriptstyle \sum _ { k = 0 } ^ { n } m _ { k }$ .Then it follows from our discussion that the number of chains passing through some member of $\mathcal { F }$ is

$$
\sum _ { k = 0 } ^ { n } m _ { k } k ! ( n - k ) ! ,
$$

and this expression cannot exceed the number $n$ of all chains. Hence

![](images/e0340a52a2e2e8e5b6ed160b65ed51d0e1c34a8e126e3435f5cdc54f22ca6025.jpg)  
Emanuel Sperner

we conclude

Check that the family of all $\frac { \mathfrak { r } } { 2 }$ -sets for even $\gamma _ { \ell }$ respectivcly the two families of all $\scriptstyle { \frac { \mathfrak { r } ^ { 1 } - 1 } { \mathfrak { Z } } }$ -sets and of all $\scriptstyle { \frac { n + 1 } { 2 } }$ -sets, when $\mathscr { n }$ is odd, arc indced the only antichains that achieve the maximum size!

$$
\sum _ { k = 0 } ^ { n } m _ { k } \frac { k ! ( n - k ) ! } { n ! } \ \leq \ 1 , \qquad \mathrm { o r } \qquad \sum _ { k = 0 } ^ { n } \frac { m _ { k } } { \binom { n } { k } } \ \leq \ 1 .
$$

Replacing the denominators by the largest binomial coefficient, we therefore obtain

$$
\frac { 1 } { \left( \begin{array} { c } { n } \\ { n / 2 ! } \end{array} \right) } \sum _ { k = 0 } ^ { n } m _ { k } \leq 1 , \qquad \mathrm { i } \hbar \mathrm { a t ~ i s , } \qquad | \mathcal { F } | = \sum _ { k = 0 } ^ { n } m _ { k } \leq \binom { n } { \lfloor n / 2 \rfloor } ,
$$

and the proof is complete.

Our second result is of an entirely different nature. Again we consider the set $N = \{ 1 , \ldots , \pi \}$ . Call a family $\mathcal { F }$ of subsets an intersecting family if ay two sets in $\mathcal { F }$ have at least one element in common. It is almost immediate that the size of a largest intersecting family is $2 ^ { \eta . - 1 }$ . If $A \in { \mathcal { F } }$ ,then the complement $A ^ { c } = N \backslash A$ has empty intersection with $\boldsymbol { \mathscr { A } }$ and accordingly cannot be in $\mathcal { F }$ .Hence we conclude that an intersecting family contains at most half the number $2 ^ { n . }$ of all subsets, that is, $| { \mathcal { F } } _ { 1 } ^ { \prime } \leq 2 ^ { \pi - 1 }$ .On the other hand, if we consider the family of all sets containing a fixed element, say the family $\mathcal { F } _ { 1 }$ of all sets containing 1, then clearly $| { \mathcal { F } } _ { 1 } | = 2 ^ { n - 1 }$ , and the problem is settled.

But now let us ask the following question: How large can an intersecting family $\mathcal { F }$ be if all sets in $\mathcal { F }$ have the same size, say $k$ ? Let us call such families intersecting $k$ -families. To avoid trivialities, we assume $n \geq 2 k$ since otherwise any two $k _ { i }$ -sets intersect, and there is nothing to prove. Taking up the above idea, we certainly obtain such a family ${ \mathcal { F } } _ { 1 }$ by considering all $k \mathrm { . }$ -sets containing a fixed element, say 1. Clearly, we obtain all sets in $F _ { 1 }$ by adding to I all $( k - 1 )$ subss of $\{ 2 , 3 , \ldots , n \}$ hence $| \mathcal { F } _ { 1 } | = \binom { \pi - \textstyle 1 } { k - 1 }$ Can we do better? No — and this is the theorem of Erds-Ko-Rado.

Th hen The larget s  ntersecting $k$ family in an tu-set is $\binom { n - 1 } { k - 1 }$ $n \geq 2 k \mathrm { . }$

Paul Erdós, Chao Ko and Richard Rado found this result in 1938, but it was not published until 23 years later. Since then multitudes of proofs and variants have been given, but the following argument due to Gyula Katona is particularly elegant.

![](images/befd18fee74fcee3ffaa0e8dc6310e01fa08a89621358988aeb9b1054e7bdee6.jpg)

A circle $C$ for $r _ { k } = 6$ The bold edges depict an are of length 3.

Proof. The key to the proof is the following simple lemma, which at first sight seems to be totally unrelated to our problem. Consider a circle $C$ divided by $n$ points into $n$ edges. Let an are of length $k$ consist of $k + 1$ consecutive points and the $k$ edges between them.

Lemma. $\ L e t \ n \geq 2 k$ , and suppose we are given t distinct arcs $A _ { 1 } , \dotsc , A _ { t }$ of length $k$ , such that any two arcs have an edge in common. Then $t \leq k$ .

To prove the lemma, note first that any point of $C$ is the endpoint of at most one arc. Indeed, if $A _ { i } , A _ { j }$ had a common endpoint $\mathcal { V }$ , then they would have to start in different direction (since they are distinct). But then they cannot have an edge in common as $\pi \geq 2 k$ Let us fix $A _ { 1 }$ . Since any $A _ { i }$ $( i \geq 2 )$ has an edge in common with $\boldsymbol { A } _ { 1 }$ , one of the endpoints of $A _ { i }$ is an inner point of $\boldsymbol { \mathcal { A } } _ { \mathbf { \mathcal { I } } }$ . Since these endpoints must be distinct as we have just seen, and since $A _ { 1 }$ contains $k - 1$ inner points, we conclude that there can be at most $k - 1$ further arcs, and thus at most $k$ arcs altogether. □

Now we proceed with the proof of the Erdós-Ko-Rado theorem. Let $\mathcal { F }$ be an intersecting $k$ -family. Consider a circle $C$ with $\boldsymbol { \mathscr { n } }$ points and $n$ edges as above. We take any cyclic permutation $\pi = ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } )$ and write the numbers $i i _ { 1 }$ clockwise next to the edges of $C$ . Let us count the number of sets $A \in \mathcal { F }$ which appear as $k$ consecutive numbers on $C$ . Since $\mathcal { F }$ is an intersecting family we sec by our lemma that we get at most $k$ such sets. Since this holds for any cyclic permutation, and since there are $( \eta , \mathrm { ~ - ~ } 1 ) !$ cyclic permutations, we produce in this way at most

$$
k ( \eta _ { l } \textrm { -- } 1 ) !
$$

sets of $\mathcal { F }$ which appear as consecutive clements of some cyclic permutation. How often do we count a fixed sel $A \in { \mathcal { F } } ?$ Easy enough: $A$ appears in $\pi$ if the $k$ elements of $A$ appear consecutively in some order. Hence we have $k !$ possibilities to write $A$ consecutively, and $( \gamma , - k ) !$ ways to order the remaining elements. So we conclude that a fixed set $A$ appears in preciscly $h ^ { \prime } ( \eta , - k ) !$ cyclic permutations, and hence that

$$
| { \mathcal { F } } | ~ \leq ~ { \frac { k ( n - 1 ) ! } { k ! ( n - k ) ! } } ~ = ~ { \frac { ( n - 1 ) ! } { ( k - 1 ) ! ( n - 1 - ( k - 1 ) ) ! } } ~ = ~ { \binom { n - 1 } { k - 1 } }
$$

Again we may ask whether the families containing a fixed element are the only intersecting $k$ -families. This is certainly not true for $\pi = 2 k$ For example, for $\hbar = 4$ and $k = 2$ the family $\left\{ 1 , 2 \right\} , \left\{ 1 , 3 \right\} , \left\{ 2 , 3 \right\}$ also has size $\bar { \binom { 3 } { 1 } } = 3$ More generally, for $\pi = 2 k$ we get the maximal intersecting $k$ families, of size $\begin{array} { r } { \frac { 1 } { 2 } \binom { \pi \iota } { \hbar } = \binom { \pi \iota - 1 } { \bar { \kappa } - 1 } } \end{array}$ pair of sets formed by a $k$ -set $A$ and its complement But for the spccial families containing a fixed element are indeed the only ones. The reader is invited to try his hand at the proof.

Finally, we turn to the third result which is arguably the most important basic theorem in finite set theory, the "marriage theorem" of Philip Hall proved in 1935. It opened the door to what is today called matching theory, with a wide variety of applications, some of which we shall see as we go along.

Consider a finite set $X$ and a collection $A _ { 1 } , \ldots , A _ { n }$ of subsets of $X$ (which need not be distinct). Let us call a sequence $x \cdot \ldots , x \ldots$ a system of distinct representatives of $\{ A _ { 1 } , . . . , A _ { \uparrow \bar { \imath } } \}$ if the $x _ { i }$ are distinct elements of $X$ , and if $x _ { i } \in A _ { i }$ for all $\dot { \tau }$ .Of coursc, such a system, abbreviated SDR, need not exist, for example when one of the sets $A _ { i }$ is empty. The content of the theorem of Hall is the precise condition under which an SDR exists.

3

An intersecting family for $n = 4 , k = 2$

![](images/9f4261ce6602a8b1e4a7bb15e30e2319f19c10a90c70636f02ea5f9d4db9a6a6.jpg)

"A mass wedding"

Before giving the result let us stale the human interpretation which gave it the folklore name marriage theorem: Consider a set $\{ 1 , \ldots , n \}$ of girls and a set $X$ of boys. Whenever $x \in A _ { i }$ , then girl $i$ and boy $x$ are inclined to get married, thus $A _ { i }$ is just the set of possible matches of girl $i$ An SDR represents then a mass-wedding where every girl marries a boy she likes.

Back to sets, here is the statement of the result.

Theorem 3. Let $A _ { 1 } , \ldots , A _ { r } $ be a collection of subsets of a finite set $X$ . Then there exists a system of distinct representatives if and only if the union of any m sets $A _ { i }$ contains at least mn elements, for $1 \leq m \leq n$ .

The condition is clearly necessary: If m sets $\varXi _ { j }$ contain between them fewer than $m$ elements, then these mn sets can certainly not be represented by distinct elements. The surprising fact (resulting in the universal applicability) is that this obvious condition is also sufficient. Hall's original proof was rather complicated, and subsequently many different proofs were given, of which the following one (due to Easterfield and rediscovered by Halmos and Vaughan) may be the most natural.

Proof. We use induction on p. For $n = 1$ there is nothing to prove. Let $n > 1$ , and suppose $\{ A _ { 1 } , . . . . , A _ { n } \}$ satisfies the condition of the theorem which we abbreviate by (H). Call a collection of $\ell$ sets $A _ { i }$ with $1 \leq \ell < n \mathtt { a }$ critical family if its union has cardinality $\ell$ Now we distinguish two cases.

Case 1: There is no critical family.

Choose any element $x \in A _ { \mathit { r l } }$ .Delete $x$ from $X$ and consider the collection $A _ { 1 } ^ { \prime } , \ldots , A _ { n } ^ { \prime } _ { 1 }$ with $A _ { i } ^ { \prime } = A _ { i } \backslash \{ x \}$ Sin there is no ciicl fmily, we ind that the union of any $m$ sets $A _ { i } ^ { \prime }$ contains at least $m$ elements. Hence by induction on $n$ there exists an SDR $x _ { 1 } , \ldots , x _ { n } \quad 1$ of $\left\{ \mathcal { A } _ { 1 } ^ { \prime } , \dots , \mathcal { A } _ { n - 1 } ^ { \prime } \right\}$ , and together with $x _ { r } , \ l = x$ , this gives an SDR for the original collection.

Case 2: There exists a critical family.

After renumbering the sets we may assume that $\{ A _ { 1 } , \ldots , A _ { \ell } \}$ is a critical family. Then $\textstyle \bigcup _ { i = 1 } ^ { \ell } A _ { i } = { \tilde { X } }$ with $| { \tilde { X } } | = \ell$ Since $\ell < n$ , we infer the existence of an SDR for $A _ { 1 } , \ldots , A _ { \ell }$ by induction, that is, there is a numbering $x _ { 1 } , \ldots , x _ { \ell }$ of $\tilde { X }$ such that $x _ { i } \in { \varLambda } _ { i }$ for all $\dot { \wr } < \ell$ .

![](images/83e1a8e72c8cca3a26a18e1efa58f633d7b2bc9362d0c37fe04ed8c4f586b4c1.jpg)  
$\{ \boldsymbol { B } , \boldsymbol { C } _ { : } ^ { \gamma } , \boldsymbol { D } \}$ is a critical family

Consider now the remaining collection $A _ { \ell + 1 } , \ldots , A _ { n }$ , and take any m of these sets. Since the union of $A _ { 1 } , \ldots , A _ { \ell }$ and these in sets contains at least $\ell + m$ elements by condition (H), we infer that the $m$ sets contain at least $m$ elements outside $\widetilde { X }$ .In other words, condition $\mathrm { ( H ) }$ is satisfied for the family

$$
A _ { \ell + 1 } \backslash \widetilde X , \ldots , A _ { n } \backslash \widetilde X .
$$

Induction now gives an SDR for $A _ { \ell + 1 } , \ldots , A _ { r } $ that avoids $\widetilde { X }$ Combining it with $x _ { 1 } , \ldots , x _ { k }$ we obtain an SDR for all sets $\varLambda _ { i }$ .This completes the proof.

As we mentioned, Hall's theorem was the beginning of the now vast field of matching theory [6]. Of the many variants and ramifications let us state one particularly appealing result which the reader is invited to prove for himself:

Suppose the sets $A _ { 1 } , \ldots , A _ { n }$ all have size $k \geq 1$ and suppose further that no element is contained in more than $k$ sets. Then there exist $k$ SDR's such that for any $i$ the $k$ representatives of $A _ { i }$ are distinct and thus together form the set $A _ { i }$ .

A beautiful result which should open new horizons on marriage possibilities.

# References

[1] T. E. EASTERFIEl.D: A combinatorial algorithm. J. London Math. Soc. 21 (1946), 219-226.   
[2] P. ERDÖs. C. KO & R. RADO: Intersection theorems for systems of finite sets, Quart. J. Math. (Oxford), Ser. (2) 12 (1961), 313-320.   
[3] P. HALL: On representatives of subsets, J. London Math. Soc. 10 (1935), 2630.   
[4] P. R. HALMOS & H. E. VAUGHAN: The marriage problem, Amcr. J. Math. 72 (1950), 214-215.   
[5] G. KAToNA: A simple proof of the Erdós-Ko-Rado theorem, J. Combinatorial Theory, Scr. B 13 (1972), 183-184.   
[6] L. LovÁS7. & M. D. Pl.UMMER: Matching Theory, Akadémiai Kiadó, Budapcst 1986.   
17] D. LUBELL: A short proof of Sperner's theorem, J. Combinatorial Theory 1 (1966), 299.   
[8] E. SPERNER: Ein Satz über Untermengen einer endlichen Menge, Math. Zeitschrift 27 (1928), 544-548.

How often does one have to shuffle a deck of cards until it is random?

The analysis of random processes is a familiar duty in life ("How long does it take to get to the airport during rush-hour?") as well as in mathematics. Of course, getting meaningful answers to such problems heavily depends on formulating meaningful questions. For the card shuffling problem, this means that we have

to specify the size of the deck $\hphantom { 0 } n = 5 2$ cards, say), to say how we shuffle (we'll analyze top-in-at-random shuffles first, and then the more realistic and effective riffle shuffles), and finally to explain what we mean by "is random" or "is close to random."

So our goal in this chapter is an analysis of the riffle shuffle, due to Edgar N. Gilbert and Claude Shannon (1955, unpublished) and Jim Reeds (1981, unpublished), following the statistician David Aldous and the former magician turned mathematician Persi Diaconis according to [1]. We will not reach the final precise result that 7 riffle shuffles are sufficient to get a deck of $n = 5 2$ cards very close to random, while 6 riffle shuffles do not suffice — but we will obtain an upper bound of 12, and we will see some extremely beautiful ideas on the way: the concepts of stopping rules and of "strong uniform time," the lemma that strong uniform time bounds the variation distance, Reeds' inversion lemma, and thus the interpretation of shuffling as "reversed sorting." In the end, everything will be reduced to two very classical combinatorial problems, namely the coupon collector and the birthday paradox. So let's start with these!

# The birthday paradox

Take $n$ random people — the participants of a class or seminar, say. What is the probability that they all have different birthdays? With the usual simplifying assumptions (365 days a year, no seasonal effects, no twins present) the probability is

$$
p ( n ) \ = \ \prod _ { i = 1 } ^ { n - 1 } \Big ( 1 - \frac { i } { 3 6 5 } \Big ) ,
$$

![](images/fc08b6f1ba0695b9c8ef36c8f662fa462ebfadd5f77cdd7986d3504ab33b1783.jpg)

Persi Diaconis' business card as a magician. In a later interview he said: "If you say that you are a professor at Stanford people treat you respectfully. If you say that you invent magic tricks, they don't want to introduce you to their daughter."

which is smaller than $\frac { 1 } { 2 }$ for $n = 2 3$ (this is the "birthday paradox"!), less than 9 percent for $n = 4 2$ , and exactly 0 for $\pi > 3 6 5$ (the "pigeon-hole principle," see Chapter 22). The formula is easy to see — if we take the persons in some fixed order: If the first $i$ persons have distinct birthdays, then the probability that the $( i + 1 ) - s t$ person doesn't spoil the series is $1 - { \frac { i } { 3 6 5 } }$ , since there are $3 6 5 - i$ birthdays left.

Similarly, if $n$ balls are placed independently and randomly into $K$ boxes, then the probability that no box gets more than one ball is

$$
p ( n , K ) = \prod _ { i = 1 } ^ { n - 1 } \Big ( 1 - \frac { i } { K } \Big ) .
$$

$$
\begin{array} { r c l } { { \displaystyle \sum _ { s > 1 } x ^ { s - 1 } ( 1 - x ) s } } & { { = } } & { { } } \\ { { } } & { { = } } & { { \displaystyle \sum _ { s \geq 1 } x ^ { s - 1 } s - \sum _ { s \geq 1 } x ^ { s } s } } \\ { { } } & { { = } } & { { \displaystyle \sum _ { s \geq 0 } x ^ { s } ( s + 1 ) - \sum _ { s \geq 0 } x ^ { s } s } } \\ { { } } & { { = } } & { { \displaystyle \sum _ { s \geq 0 } x ^ { s } = \frac { 1 } { 1 - x } , } } \end{array}
$$

where at the end we sum a geometric series (see page 28).

# The coupon collector

Children buy photos of pop stars (or soccer stars) for their albums, but they buy them in little non-transparent envelopes, so they don't know which photo they will get. If there are $n$ different photos, what is the expected number of pictures a kid has to buy until he or she gets every motif at least once?

Equivalently, if you randomly take balls from a bowl that contains n distinguishable balls, and if you put your ball back each time, and then again mix well, how often do you have to draw on average until you have drawn each ball at least once?

If you already have drawn $k$ distinct balls, then the probability not to get a new one in the next drawing is $\frac { k } { n }$ .So the probability to need exactly $\boldsymbol { s }$ drawings for the next new ball is $\textstyle { \left( { \frac { k } { \hbar } } \right) ^ { s - 1 } ( 1 - { \frac { k } { \hbar 2 } } ) }$ And thus the expected number of drawings for the next new ball is

$$
\sum _ { s > 1 } \left( { \frac { k } { n } } \right) ^ { s - 1 } \left( 1 - { \frac { k } { n } } \right) s = { \frac { 1 } { 1 - { \frac { k } { n } } } } ,
$$

as we get from the series in the margin. So the expected number of drawings until we have drawn each of the $n$ different balls at least once is

$$
\sum _ { k = 0 } ^ { n - 1 } { \frac { 1 } { 1 - { \frac { k } { n } } } } = { \frac { n } { n } } + { \frac { n } { n - 1 } } + \cdots + { \frac { n } { 2 } } + { \frac { n } { 1 } } = n H _ { n } \ \approx \ n \log n ,
$$

with the bounds on the size of harmonic numbers that we had obtained on page 11. So the answer to the coupon collector's problem is that we have to expect that roughly $n ! \log n !$ drawings are necessary.

The estimate that we need in the following is for the probability that you need significantly more than $n \log n$ trials. If $V _ { \mathfrak { r } }$ denotes the number of drawings needed (this is the random variable whose expected value is $E [ V _ { n } ] \approx n \log n )$ , then for $\pi \geq 1$ and $c \geq 0$ , the probability that we need more than $m : = { \bar { \Gamma } } \hbar \log \eta + c \eta \mathbf { \bar { \Pi } }$ drawings is

$$
\operatorname { P r o b } \left[ V _ { n } > m \right] \leq e ^ { - c } .
$$

Indeed, if $A _ { i }$ denotes the event that the ball $i$ is not drawn in the first $m$ drawings, then

$$
\begin{array} { r c l l } { { \mathrm { P r o b } \big [ { \cal V } _ { \mathrm { n } } > m \big ] } } & { { = } } & { { \mathrm { P r o b } \Big [ \bigcup _ { i } { \cal A } _ { i } \Big ] } } & { { \le } } & { { \displaystyle \sum _ { i } \mathrm { P r o b } \big [ { \cal A } _ { i } \big ] } } \\ { { } } & { { = } } & { { \displaystyle n \Big ( 1 - { \frac { 1 } { n } } \Big ) ^ { m } } } & { { < } } & { { n e ^ { - m / n } \leq \epsilon ^ { - c } , } } \end{array}
$$

A little calculus shows that $( 1 - \frac { 1 } { n } ) ^ { n }$ is an increasing function in $\mathscr { n }$ , which converges to $1 / e$ So $( 1 - \frac { 1 } { n } ) ^ { n } < \frac { 1 } { e }$ holds for all $n \geq 1$ .

Now let's grab a deck of $\boldsymbol { \mathscr { n } }$ cards. We number them 1 up to $n$ in the order in which they come — so the card numbered "1" is at the top of the deck, whilc $" \gamma _ { l } ? ^ { \prime \prime }$ is at the bottom. Let us denote from now on by ${ \mathfrak { S } } _ { n }$ the set of all permutations of $1 , \ldots , n$ . Shuffling the deck amounts to the application of certain random permutations to the order of the cards. Ideally, this might mean that we apply an arbitrary permutation $\pi \in { \mathfrak { S } } _ { n }$ to our starting order $( \mathsf { I } , 2 , \ldots , \mathsf { r } )$ y $\textstyle { \frac { \downarrow } { n ! } }$ . Thus, after doing this just once, we would have our deck of cards in order $\pi = ( \pi ( 1 ) , \pi ( 2 ) , \ldots , \pi ( n ) )$ , and this would be a perfect random order. But that's not what happens in real life. Rather, when shuffling only "certain" permutations occur, perhaps not all of them with the same probability, and this is repeated a "certain" number of times. After that, we expect or hope the deck to be at least "close to random."

# Top-in-at-random shuffles

These are performed as follows: you take the top card from the deck, and insert it into the deck at one of the $n$ distinct possible places, each of them with probability $\frac { 1 } { n }$ . Thus one of the permutations

$$
\begin{array} { c } { i } \\ { \downarrow } \\ { \tau _ { i } = ( 2 , 3 , \dots , i , 1 , i + 1 , \dots , n ) } \end{array}
$$

is applied, $1 \leq i \leq \pi$ . After one such shuffle the deck doesn't look random, and indeed we expect to need lots of such shuffles until we reach that goal. A typical run of top-in-at-random shuffles may look as follows (for $n = 5$ :

Top-in-at-random

![](images/b2ace46e4a585db73ce558f4e116c48fbaf111e28bf585d5fe17606d1dada660.jpg)

![](images/22df0a7510db1089e1bbee66c5aaf31aee8c11285f25d22b306d871fd31ca2ca.jpg)

How should we measure "being close to random"? Probabilists have cooked up the "variation distance" as a rather unforgiving measure of randomness: We look at the probability distribution on the $n !$ different orderings of our deck, or equivalently, on the $\hbar !$ different permutations $\sigma \in \mathfrak { S } _ { \mathfrak { z } }$ that yield the orderings.

Two examples are our starting distribution E, which is given by

$$
\begin{array} { l c l } { { { \sf E } ( \mathrm { i d } ) } } & { { = } } & { { 1 , } } \\ { { { \sf E } ( \pi ) } } & { { = } } & { { 0 \quad ( } } \end{array}
$$

and the uniform distribution U given by

$$
{ \mathsf { U } } ( \pi ) = { \frac { 1 } { n ! } } { \mathsf { f o r } } { \mathsf { a l l } } \pi \in { \mathfrak { S } } _ { n } .
$$

The variation distance between two probability distributions $\mathsf Q _ { 1 }$ and $\mathsf { Q } _ { 2 }$ is now defined as

$$
\begin{array} { r l r } { \| \mathsf { Q } _ { 1 } - \mathsf { Q } _ { 2 } \| } & { : = } & { \frac { 1 } { 2 } \displaystyle \sum _ { \pi \in \mathfrak { S } _ { \pi } } | \mathsf { Q } _ { 1 } ( \pi ) - \mathsf { Q } _ { 2 } ( \pi ) | , } \end{array}
$$

By setting $S : = \{ \pi \in \mathfrak { S } _ { n } : \mathsf { Q } _ { 1 } ( \pi ) > \mathsf { Q } _ { 2 } ( \pi ) \}$ and using $\begin{array} { r l } { \sum _ { \pi } \mathsf { Q } _ { \perp } ( \pi ) = } & { { } } \end{array}$ $\begin{array} { r } { \sum _ { \pi } \mathsf Q _ { 2 } ( \pi ) = 1 } \end{array}$ we can rewrite this as

$$
\left\| \mathsf { Q } _ { 1 } - \mathsf { Q } _ { 2 } \right\| = \displaystyle \operatorname* { m a x } _ { S \subseteq \mathfrak { S } _ { \tau } } | \mathsf { Q } _ { 1 } ( S ) - \mathsf { Q } _ { 2 } ( S ) | ,
$$

with $\begin{array} { r } { \mathsf Q _ { i } ( S ) : = \sum _ { \pi \in S } \mathsf Q _ { i } ( \pi ) } \end{array}$ Clearly we have $0 \leq \| \mathsf Q _ { 1 } - \mathsf Q _ { 2 } \| \leq 1$ In the following, "being close to random" will be interprcted as "having small variation distance from the uniform distribution." Here the distance between the starting distribution and the uniform distribution is very close to 1 :

$$
\begin{array} { r } { \| \mathsf { E } - \mathsf { U } \| } \ = \ 1 - \frac { 1 } { n ! } ,  \end{array}
$$

After one top-in-at-random shuffle, this will not be much better:

$$
\begin{array} { r } { \| \mathsf { T o p } - \mathsf { U } \| } { \mathsf { \Omega } } = { \mathsf { \Omega } } 1 - \frac { 1 } { ( n - 1 ) ! } ,  \end{array}
$$

For card players, the question is not "exactly how close to uniform is the deck after a million riffle shuffles?", but "is 7 shuffles enough?"

(Aldous & Diaconis [1])

![](images/dc5110b9694a22e4b89f016776892b6bcf33374fbdf69d2b5cfb41c2fd466f6b.jpg)

The probability distribution on ${ \mathfrak { S } } _ { \mathfrak { n } }$ that we obtain by applying the top-in-atrandom shuffle $k$ times will be denoted by $\boldsymbol { \mathsf { T o p } } ^ { * k }$ . So how does $\| \mathsf { T o p } ^ { * k } - \mathsf { U } \|$ behave if $k$ gets larger, that is, if we repeat the shuffling? And similarly for other types of shuffling? General theory (in particular, Markov chains on finite groups; see e. g. Behrends [3]) implies that for large $k$ the variation distance $\bar { d ( k ) } : = \| \mathsf { T o p } ^ { * k } - \mathsf { U } \|$ goes to zero exponentially fast, but it does not yield the "cut-off" phenomenon that one observes in practice: After a certain number $k _ { 0 }$ of shuffles "suddenly" $d ( k )$ goes to zero rather fast. Our margin displays a schematic sketch of the situation.

# Strong uniform stopping rules

The amazing idea of strong uniform stopping rules by Aldous and Diaconis captures the essential features. Imagine that the casino manager closely watches the shuffling process, analyzes the specific permutations that are applied to the deck in each step, and after a nurber of steps that depends on the permutations that he has seen calls "STOp!". So he has a stopping rule that ends the shuffling process. It depends only on the (random) shuffles that have already been applied. The stopping rule is strong uniform if the following condition holds for all $k \geq 0$ :

If the process is stopped after exactly $k$ steps, then the resulting permutations of the deck have uniform distribution (exactly!).

Let $T$ be the number of steps that are performed until the stopping rule tells the manager to cry "STOP!"; so this is a random variable. Similarly, the ordering of the deck after $k$ shuffles is given by a random variable $X _ { k }$ (with values in ${ \mathfrak { S } } _ { n }$ ). With this, the stopping rule is strong uniform if for all feasible values of $k$ ,

$$
\operatorname { P r o b } \left[ X _ { k } = \pi \mid T = k \right] ~ = ~ { \frac { 1 } { n ! } } \quad { \mathrm { f o r ~ a l l ~ } } \pi \in { \mathfrak { S } } _ { n } .
$$

Three aspects make this interesting, useful, and remarkable:

1. Strong uniform stopping rules exist: For many examples they are quite simple.   
2. Morcover, these can be analyzed: Trying to determine $\mathrm { P r o b } [ T > k ]$ leads often to simple combinatorial problems.   
3. This yields effective upper bounds on the variation distances such as $d ( k ) \stackrel { \cdot } { = } | | \mathsf { T o p } ^ { * k } - \mathsf { U } | |$ .

For example, for the top-in-at-random shuffles a strong uniform stopping rule is

"STOP after the original bottom card (labelled $n _ { e }$ ) is first inserted back into the deck."

Indeed, if we trace the card $n$ during these shuffles,

# Relative probabilities

The relative probability

$$
\mathbf { P r o b } [ A \mid B ]
$$

![](images/1432d93a3aeddc14b57f761b7dd4d9b82a38dfd9155388b2cbb9bd1006b344ed.jpg)

we see that during the whole process the ordering of the cards below this card is completely uniform. So, after the card $\pmb { n }$ rises to the top and then is inserted at random, the deck is uniformly distributed; we just don't know when precisely this happens (but the manager does).

Now let $T _ { i }$ be the random variable which counts the number of shuffles that are performed until for the first time $i ,$ cards lie below card $\boldsymbol { \mathfrak { n } }$ .So we have to determine the distribution of

$$
T \ = \ T _ { 1 } + ( T _ { 2 } - T _ { 1 } ) + \ldots + ( T _ { n - 1 } - T _ { n - 2 } ) + ( T - T _ { n - 1 } ) .
$$

But each summand in this corresponds to a coupon collector's problem: $r _ { i } - T _ { i - 1 }$ is the time until the top card is inserted at one of the $i$ possible places below the card $n$ . So it is also the time that the coupon collector takes from the $( \gamma _ { l } , \textrm { -- } i )$ -th coupon to the $(  \eta - \dot { \imath } + 1 )$ -st coupon. Let $V _ { i }$ be the number of pictures bought until he has $i$ different pictures. Then

$$
V _ { n } ~ = ~ V _ { 1 } + ( V _ { 2 } - V _ { 1 } ) + \ldots + ( V _ { n - 1 } - V _ { n - 2 } ) + ( V _ { n } - V _ { n - 1 } ) ,
$$

denotes the probability of the event $A$ under the condition that $B$ happens. This is just the probability that both events happen, divided by the probability that $B$ is true, that is,

$$
\mathrm { P r o b } [ \varLambda | \ B ] \ = \ \frac { \mathrm { P r o b } [ A \wedge B ] } { \mathrm { P r o b } [ B ] } .
$$

and we have seen that $\mathrm { P r o b } [ { \cal T } _ { i } - { \cal T } _ { i - 1 } = j ] = \mathrm { P r o b } [ V _ { n - i + 1 } - V _ { n - i } = j ]$ for all $i$ and $j$ .Hence the coupon collector and the top-in-at-random shuffler perform equivalent sequences of independent random processes, just in the opposite order (for the coupon collector, it's hard at the end). Thus we know that the strong uniform stopping rule for the top-in-at-random shuffles takes more than $k = \lceil n \log n + \mathfrak { c r } \rceil$ steps with low probability:

$$
\operatorname { P r o b } \left[ { \mathcal { T } } > k \right] \ \leq \ \epsilon ^ { - c } .
$$

And this in turn means that after $\begin{array} { r } { k \ = \ \left\lceil n \log \eta _ { i } + c \eta _ { i } \right\rceil } \end{array}$ top-in-at-random shuffles, our deck is "close to random," with

$$
d ( k ) ~ - ~ \| \mathsf { T o p } ^ { * k } - \mathsf { U } \| ~ \leq ~ \epsilon ^ { - \epsilon } .
$$

due to the following simple but crucial lemma.

Lemma. $\begin{array} { r } { L e t \mathbb { Q } : \mathfrak { S } _ { n } \longrightarrow \mathbb { R } } \end{array}$ be any probability distribution that defines a shuffling process $\mathsf Q ^ { * k }$ with $\pmb { a }$ strong uniform stopping rule whose stopping time is $T .$ Then for all $k \geq 0$ .

$$
\| { \mathsf { Q } } ^ { * k } - { \mathsf { U } } \| ~ \leq ~ { \mathsf { P r o b } } \big [ T > k \big ] .
$$

Proof. If $X$ is a random variable with values in $\mathfrak { S } _ { n }$ , with probability distribution $\mathsf Q$ , then we write $\ Q ( S )$ for the probability that $X$ takes a value in $S \subseteq \mathfrak { S } _ { n }$ . Thus $\mathsf Q ( S ) = \mathsf { P r o b } [ X \in S ]$ , and in the case of the uniform distribution $\ Q = \mathsf { U }$ we get

$$
\mathsf { U } ( S ) \ \subsetneq \ \mathrm { P r o b } \big [ X \in S \big ] \ = \ \frac { | S | } { n ! } .
$$

For every subset $S \subseteq \mathfrak { S } _ { \pi }$ , we get the probability that after $k$ steps our deck is ordered according to a permutation in $S$ as

$$
\begin{array} { r } { \begin{array} { r c l } { \displaystyle \mathbb { Q } ^ { \star k } ( \mathcal { S } ) } & { \displaystyle - \mathrm { \normalfont ~ P r o b } [ X _ { k } \in \mathcal { S } ] } \\ { = } & { \displaystyle \sum _ { j \leq k } \mathrm { \normalfont ~ P r o b } [ X _ { k } \in \mathcal { S } \wedge T = j ] \ + \ \mathrm { \normalfont ~ P r o b } [ X _ { k } \in \mathcal { S } \wedge T > k ] } \\ { = } & { \displaystyle \sum _ { j \leq k } \mathsf { U } ( \mathcal { S } ) \mathrm { \normalfont ~ P r o b } [ T = j ] \ + \mathrm { \normalfont ~ P r o b } [ X _ { k } \in \mathcal { S } \ | T > k ] \cdot \mathrm { \normalfont ~ P r o b } [ T > k ] } \\ { = } & { \displaystyle \mathsf { U } ( \mathcal { S } ) \left( 1 - \mathrm { \normalfont ~ P r o b } [ T > k ] \right) \ + \ \mathrm { \normalfont ~ P r o b } [ X _ { k } \in \mathcal { S } \ | T > k ] \cdot \mathrm { \normalfont ~ P r o b } [ T > k ] } \\ { = } & { \displaystyle \mathsf { U } ( \mathcal { S } ) \ + \ \left( \mathrm { P r o b } [ X _ { k } \in \mathcal { S } \ | T > k ] - \mathsf { U } ( \mathcal { S } ) \right) \cdot \mathrm { \normalfont ~ P r o b } [ T > k ] . } \end{array} } \end{array}
$$

This yields

$$
\lvert \mathrm { Q } ^ { * k } ( S ) - \mathsf { U } ( S ) \rvert \ \leq \ \mathrm { P r o b } [ T > k ]
$$

since

$$
\mathrm { P r o b } [ X _ { k } \in S \mid T > k ] \ - \ \mathsf { U } ( S )
$$

is a difference of two probabilities, so it has absolute value at most I.

This is the point where we have completed our analysis of the top-in-atrandom shuflle: We have proved the following upper bound for the number of shuffles needed to get "close to random."

Theorem 1. Let $c \geq 0$ and $k : = \lceil \tau \rceil \log \eta + \mathfrak { c } \mathfrak { n } \rceil$ . Then after performing k top-in-ut-random shuffles on a deck of n cards, the variation distance from the uniform distribution satisfies

$$
d ( k ) \ : = \| { \mathsf { T o p } } ^ { * k } - { \mathsf { U } } \| \ \leq \ \epsilon ^ { - \alpha } .
$$

One can also verify that the variation distance $d ( k )$ stays large if we do significantly fewer than $n$ log n top-in-at-random shuffles. The reason is that a smaller number of shuffles will not suffice to destroy the relative ordering on the lowest fcw cards in the deck.

Of course, top-in-at-random shuffles are extremely ineffective — with the bounds of our theorem, we need roughly $n \log n \approx 2 0 5$ top-in-at random shuffles until a deck of $n = 5 2$ cards is mixed up well. Thus we now switch our attention to a much more interesting and realistic model of shuffling.

# Riffle shuffles

This is what dealers do at the casino: They take the deck, split it into two parts, and thesc are then interleaved, for example by dropping cards from the bottons of the two half-decks in some irregular pattern.

Again a riffle shuffle performs a certain permutation on the cards in the deck, which we initially assume to be labelled from 1 to $n$ , where 1 is the top card. The riffle shuffles correspond exactly to the permutations $\pi \in { \mathfrak { S } } _ { n }$ such that the sequence

$$
( \pi ( 1 ) . \pi ( 2 ) , \ \dots \ , \pi ( n ) )
$$

consists of two interlaced increasing sequences (only for the identity permutation it is one increasing scquence), and that there are exactly $2 ^ { n } - n$ distinct riffle shuffles on a deck of $n$ cards.

![](images/8f96495788a1d6abb8568a93b7a6068ae0316128a5811845a7d914cd7ede3fbe.jpg)

In fact, if the pack is split such that the top $t ,$ cards are taken into the right hand $( 0 \leq t \leq n )$ and the other $n - t$ cards into the left hand, then there are $( \mathbf { \lambda } _ { t } ^ { \mathsf { \pi } } )$ w v tations — except that for each $t$ there is one possibility to obtain the identity permutation.

Now it's not clear which probability distribution one should put on the riffle shuffles - there is no unique answer since amateurs and professional dealers would shuffle differently. However, the following model, developed first by Edgar N. Gilbert and Claude Shannon in 1955 (at the legendary

![](images/91dd909f525577b06ebd0697998cfd3fe657c010f88f5de777436b7c4203662c.jpg)

A riffle shuffle

Bell Labs "Mathematics of Communication" department at the time), has several virtues:

it is elegant, simple, and seems natural,   
$\bullet$ it models quite well the way an amateur would perform riffle shuffles, $\bullet$ and we have a chance to analyze it.

Here are three descriptions — all of them describe the same probability distribution Rif on $\mathfrak { S } _ { \pi }$ :

1. Rif : $\mathfrak { S } _ { \tau } \longrightarrow \mathbb { R }$ is defined by

$$
\mathsf { R i f } ( \pi ) \ : = \ \left\{ \begin{array} { l l } { \frac { n + 1 } { 2 ^ { \pi } } } & { \mathrm { i f } \ \pi = \mathrm { i d } , } \\ { \frac { 1 } { 2 ^ { n } } } & { \mathrm { i f } \ \pi \mathsf { c o n s i s t s ~ o f ~ t w o ~ i n c r e a s i n g ~ s e q u e n c e s } , } \\ { 0 } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

2. Cut off $t$ cards from the deck with probability ${ \frac { 1 } { 2 ^ { n , } } } { \binom { n } { t } }$ , take them into your right hand, and take the rest of the deck into your left hand. Now when you have $\pmb { r }$ cards in the right hand and $\ell$ in the left, "drop" the bottom card from your right hand with probability $\frac { \because } { r + \ell . }$ , and from your left hand with probability $\frac { \ell } { r + \ell }$ Repeat!

The inversc riffle shuffles correspond to the permutations $\pi = ( \pi ( 1 ) , \ldots , \pi ( r ) )$ that are increasing except for at most one "dcscent." (Only thc identity permutation has no descent.)

3. An inverse shuffle would take a subset of the cards in the deck, remove them from the deck, and place them on top of the remaining cards of the deck — while maintaining the relative order in both parts of the deck. Such a move is determined by the subset of the cards: Take all subsets with cqual probability.

Equivalently, assign a label $\mathbf { \bar { \rho } } ^ { \ast } \mathbf { 0 } ^ { \ast }$ or $" 1 "$ to each card, randomly and independently with probabilities $\textstyle { \frac { 1 } { 2 } }$ , and move the cards labelled $\ " 0 \ "$ to the top.

It is easy so see that these descriptions yield the same probability distributions. For $( 1 ) \Longleftrightarrow ( 3 )$ just observe that we get the identity permutation whenever all the O-cards are on top of all the cards that are assigned a 1.

This defines the model. So how can we analyze it? How many riffle shuffles are needed to get close to random? We won't get the precise best-possible answer, but quite a good one, by combining three components:

1We analyze inverse riffle shuffles instead, (2) we describe a strong uniform stopping rule for these, (3) and show that the key to its analysis is given by the birthday paradox!

Theorem 2. After performing $k$ riffle shuffles on a deck of n cards, the variation distance from a uniform distribution satisfies

$$
\| \mathsf { R i f } ^ { * k } - \mathsf { U } \| ~ \leq ~ 1 - \prod _ { i = 1 } ^ { n - 1 } \left( 1 - \frac { i } { 2 ^ { k } } \right) .
$$

Proof. (1) We may indeed analyze inverse riffle shuffles and try to see how fast they get us from the starting distribution to (close to) uniform. These inverse shuffles correspond to the probability distribution that is given by ${ \overline { { \mathsf { R i f } } } } ( \pi ) : = { \mathsf { R i f } } ( \pi ^ { - 1 } )$ .

Now the fact that every permutation has its unique inverse, and the fact that $\mathsf { U } ( \pi ) = \mathsf { U } ( \pi ^ { - 1 } )$ , yield

$$
\| \mathsf { R i f } ^ { * k } - \mathsf { U } \|  &  = \| \overline { { \mathsf { R i f } } } ^ { * k } - \mathsf { U } \| .
$$

(This is Reeds' inversion lemma!)

(2) In every inverse riffle shuffle, each card gets associated a digit 0 or 1:

![](images/1414feeab495007e2fccb7f5c937e49e9bfa4dbef2ba5cb5a6368d95abb5de83.jpg)

If we remember these digits — say we just write them onto the cards — then after $k$ inverse riffle shuffles, each card has gotten an ordered string of $k$ digits. Our stopping rule is:

STOP as soon as all cards have distinct strings.

When this happens, the cards in the deck are sorted according to the binary numbers $b _ { k } b _ { k - 1 } \dots b _ { 2 } b _ { 1 }$ , where $b _ { i }$ is the bit that the card has picked up in the $i$ -th inverse riffle shuffle. Since these bits are perfectly random and independent, this stopping rule is strong uniform!

In the following example, for $n = 5$ cards, we need $T = 3$ inverse shuffles until we stop:

![](images/43ecec8411c13ff657b300de95e27d9f02c5180aaab08c1839031604c6217517.jpg)

(3) The expected time $T$ taken by this stopping rule is distributed according to the birthday paradox, for $K = 2 ^ { k }$ : We put two cards into the same box if they have the same label $b _ { k } b _ { k - 1 } \ldots b _ { 2 } b _ { 1 } \in \{ 0 , 1 \} ^ { k }$ So there are $K = 2 ^ { k }$ boxes, and the probability that some box gets more than one card ist

$$
\mathrm { P r o b } [ T > k ] = 1 - \prod _ { i = 1 } ^ { n - 1 } \left( 1 - \frac { i } { 2 ^ { k } } \right) ,
$$

and as we have sen this bouds he ri se $\| \mathsf { R i f } ^ { * k } - \mathsf { U } \| =$ $\| \widetilde { \mathsf { R i f } } ^ { * k } - \mathsf { U } \|$ □

![](images/85f3730ead64d61b5ca2980a1f7ffbea728b7c9aec4680a4e39195ed95cc222b.jpg)

The variation distance after $k$ riffle shuffles, according to [2]

![](images/0a5ed587c3e40192bb4dd7c38e65a1686844b27849036bc3e99aa70f7d071207.jpg)

So how often do we have to shuffle? For large $\mathcal { n }$ we will need roughly $k \mathrm { = } 2 \log _ { 2 } ( \uparrow 2 \cdot )$ shuffles. Indeed, setting $k : = 2 \log _ { 2 } ( c \eta _ { \ell } )$ for some $c \geq 1$ we find (with a bit of calculus) that $\begin{array} { r } { P [ T > k ] \approx 1 - \epsilon ^ { * 2 r ^ { 2 } } \approx \frac { 1 } { 2 c ^ { 2 } } } \end{array}$

Explicitly, for $\gamma _ { \ell } = 5 2$ cards the upper bound of Theorem 2 reads $d ( 1 0 ) \leq$ 0.73, $d ( 1 2 ) \ \leq \ 0 . 2 8$ . $d ( 1 4 ) ~ \leq ~ 0 . 0 8 -  s _ { 0 } ~ k ~ = ~ 1 2$ should be "random enough" for all practical purposes. But we don't do 12 shuffles "in practice" — and they are not really necessary, as a more detailed analysis shows (with the results given in the margin). The analysis of riffle shuffles is part of a lively ongoing discussion about the right measure of what is "random enough." Diaconis [4] is a guide to recent developments.

Indeed, does it matter? Yes, it does: Even after three good riffle shuffles a sorted deck of 52 cards looks quite random .. . but it isn't. Martin Gardner [5, Chapter 7] describes a number of striking card tricks that are based on the hidden order in such a deck!

# References

[1] D. AL.DOUS & P. DIACoNIS: Shuffling cards and stopping times, Amer. Math. Monthly 93 (1986), 333-348.   
[2] D. BAYER & P. DIACoNIs: Trailing the dovetail shuffle to its lair, Annals Applied Probability 2 (1992), 294-313.   
[3] E. BEHRENDs: Introduction to Markov Chains, Vieweg, Braunschweig/ Wiesbaden 2000.   
[4] P. DiACoNIS: Mathematical developmenis from the analysis of rifle shuffing, in: "Groups. Combinatorics and Geometry. Durham 2001" (A. A. Ivanov, M. W. Liebeck and J. Saxl, eds.). World Scientific, Singapore 2003, pp. 73-97.   
[5] M. GARDNER: Mathematical Magic Show, Knopf, New York/Allen & Unwin, London 1977.   
[6] E. N. Gl1.BERT: Theory of Shuffling, Technical Memorandum, Bell Laboratorics, Murtay Hill NJ, 1955.

![](images/2ac47ab57a867fbb77d8b682178bc0a8e606da24189172421bfcdb787c18b92e.jpg)

The essence of mathematics is proving theorems — and so, that is what mathematicians do: They prove theorems. But to tell the truth, what thcy really want to prove, once in their lifetime, is a Lemma, like the one by Fatou in analysis, the Lemma of Gauss in number theory, or the Burnside-Frobenius Lemma in combinatorics.

Now what makes a mathematical statement a true Lemma? First, it should be applicable to a wide variety of instances, even seemingly unrelated problems. Secondly, the statement should, once you have seen it, be completely obvious. The reaction of the reader might well be one of faint envy: Why haven't I noticed this before? And thirdly, on an esthetic level, the Lemma — including its proof — should be beautiful!

In this chapter we look at one such marvelous piece of mathematical reasoning, a counting lemma that first appeared in a paper by Bcrnt Lindstrom in 1972. Largely overlooked at the time, the result became an instant classic in 1985, when Ira Gessel and Gerard Viennot rediscovered it and demonstrated in a wonderful paper how the lemma could be successfully applied to a diversity of difficult combinatorial cnumeration problems.

The starting point is the usual permutation representation of the determinant of a matrix. Let $\lambda I = \left( r r _ { i j } \right)$ be a real $n \times n$ -matrix. Then

$$
\operatorname * { d e t } M ~ = ~ \sum _ { \sigma } \mathrm { s i g n } \sigma \mathsf { m } _ { 1 \sigma ( 1 ) } \mathsf { m } _ { 2 \sigma ( 2 ) } \cdot \cdot \cdot \mathsf { m } _ { n \sigma ( n ) } ,
$$

where $\sigma$ runs through all permutations of $\{ 1 , 2 , \ldots , n \}$ , and the sign of $\sigma$ is 1 or $^ { - 1 }$ , depending on whether $\sigma$ is the product of an even or an odd number of transpositions.

Now wc pass to graphs, more precisely to weighted directed bipartite graphs. Let the vertices $A _ { 1 } , \ldots , A _ { r } $ stand for the rows of $\lambda f$ , and $B _ { 1 } , \ldots , B _ { \tau 2 }$ for the columns. For cach pair of $i$ and $j$ draw an arrow from $A _ { i }$ to $B _ { j }$ and give it the weight ${ m } _ { i j }$ , as in the figure.

$\bullet$ The left-hand side is the determinant of the path-matrix $M$ , whose $( i , j )$ -entry is the weight of the (unique) directed path from $A _ { i }$ to $B _ { j }$ .

The right-hand side is the weightcd (signed) sum over all vertex-disjoint path systems from $\boldsymbol { \mathcal { A } } = \{ A _ { 1 } , \ldots , A _ { n } \}$ to $\beta = \{ B _ { 1 } , \ldots , B _ { n } \}$ . Such a system $\mathcal { P } _ { \sigma }$ is given by paths

$$
A _ { 1 } \to B _ { \sigma ( 1 ) } , \dots , A _ { n } \to B _ { \sigma ( n ) } ,
$$

![](images/7b2ae944ed02beecfe489884aee8095108fb47ef6755db0164ba6b7fd8a4b003.jpg)

and the weight of the path system ${ \mathcal P } _ { \sigma }$ is the product of the weights of the individual paths:

$$
w ( \mathcal { P } _ { \sigma } ) = w ( A _ { 1 } \to B _ { \sigma ( 1 ) } ) \cdots w ( A _ { n } \to B _ { \sigma ( n ) } ) .
$$

In this interpretation formula (1) reads

![](images/a9ad864a78e752f7cd48372591cfc90c414473cf44a4bbc1a502d11c565bc779.jpg)

An acyclic directed graph

$$
\operatorname* { d e t } M = \sum _ { \sigma } \mathrm { s i g n } \sigma w ( \mathcal P _ { \sigma } ) .
$$

And what is the result of Gessel and Viennot? It is the natural generalization of (1) from bipartite to arbitrary graphs. It is precisely this step which makes the Lemma so widely applicable — and what's more, the proof is stupendously simple and elegant.

Lct us first collect thc necessary concepts. We are given a finite acyclic directed graph $C _ { i } = ( V , E )$ , where acyclic means that there are no directed cycles in $G$ In particular, there are only finitely many directed paths between any two vertices $A$ and $B$ , where we includc all trivial paths $A \  \ A$ of length O. Every edge $\epsilon$ carries a weight $w ( e )$ .If $P$ is a directed path from $A$ to $B$ , written shortly $P : A  B$ , then we define the weight of $P$ as

$$
\displaystyle { \mathfrak { w } } ( P ) { \quad : } = \prod _ { \mathfrak { c } \in P } { \mathfrak { w } } ( { \mathfrak { e } } ) ,
$$

which is defined to be ${ \mathfrak { w } } ( P ) = 1$ if $P$ is a path of length ().

Now let $\mathcal { A } = \{ A _ { 1 } , . . . , A _ { \tau _ { i } } \}$ and $\boldsymbol { B } \ = \ \{ B _ { 1 } , . . . , B _ { \tau \iota } \}$ be two sets of $\gamma ,$ vertices, where $\mathcal { A }$ and $B$ need not be disjoint. To $\pmb { A }$ and $\beta$ we associate the path matrix $M = ( m _ { i j } )$ with

$$
m _ { i j } : = \sum _ { P : A _ { i }  B _ { j } } w ( P ) .
$$

A path system $p$ from $1 1 0 1 3$ consists of a permutation $\sigma$ together with $\gamma _ { l }$ paths $P _ { i } : A _ { i } \to B _ { \sigma ( i ) }$ , for $i = 1 , \ldots , \pi$ ; we write sign ${ \mathcal { P } } = { \mathrm { s i g n } } \sigma$ . The weight of $p$ is the product of the path weights

$$
w ( \mathcal { P } ) ~ = ~ \prod _ { i = 1 } ^ { n } w ( P _ { i } ) ,
$$

which is the product of the weights of all the edges of the path system.

Finally, we say that the path system $\mathcal { P } = ( P _ { 1 } , \ldots , P _ { n } )$ is vertex-disjoint if the paths of $p$ are pairwise vertex-disjoint.

Lemma. Let $G = \{ V , E \}$ be $a$ finite weighted acyclic directed graph, $\mathcal { A } = \{ A _ { 1 } , . . . , A _ { \tau \iota } \}$ and $\vec { B } = \{ B _ { 1 } , \ldots , B _ { r \imath } \}$ two n-sets of vertices, and M the path matrix from $\mathcal { A } t o B$ Then

$$
\operatorname* { d e t } M = \sum \quad \operatorname { s i g n } \mathcal { P } w ( \mathcal { P } ) .
$$

Proof. A typical summand of det(Af) is signσ m1σ(1) ··mnσ(n), which can be written as

$$
\mathrm { s i g n } \sigma \big ( \sum _ { P _ { 1 } : A _ { 1 } \to B _ { o ( 1 ) } } w ( P _ { 1 } ) \big ) \cdots \big ( \sum _ { P _ { n } : A _ { n } \to B _ { \sigma ( n ) } } w ( P _ { n } ) \big ) .
$$

Summing over $\sigma$ we immediately find from (2) that

$$
\begin{array} { r c l } { \operatorname* { d e t } { \bar { \Lambda } } I } & { = } & { \displaystyle \sum _ { \mathcal P } \mathsf { s i g n } \mathcal P w ( \mathcal P ) , } \end{array}
$$

where $\mathcal { P }$ runs through all path systems from $A$ to $B$ (vertex-disjoint or not). Hence to arrive at (3), all we have to show is

$$
\sum _ { \mathcal { P } \in N } \mathrm { s i g n } \mathcal { P } w ( \mathcal { P } ) \ = \ 0 ,
$$

where $N$ is the sct of all path systems that are not vertex-disjoint. And this is accomplished by an argument of singular beauty. Namely, we exhibit an involution $\pi : N  N$ (without fixed points) such that for $\mathcal { P }$ and $\pi \mathcal { P }$

$$
w ( \pi { \mathcal P } ) = w ( { \mathcal P } ) \mathrm { a n d } \mathrm { s i g n } \pi { \mathcal P } = - \mathrm { s i g n } { \mathcal P } .
$$

Clearly., this will imply (4) and thus the formula (3) of the Lemma.

The involution $\pi$ is defined in the most natural way. Let $\mathcal { P } \in N$ with paths $P _ { i } : { \varLambda } _ { i } \ \to \ B _ { \sigma ( i ) }$ .By definition, some pair of paths will intersect:

Let $i _ { 0 }$ be the minimal index such that $P _ { i _ { 1 } }$ shares some vertex with another path.   
Let $X$ be the first such common vertex on the path ${ { \cal { P } } _ { i _ { 0 } } }$ .   
Let $j _ { 0 }$ be the minimal index $( j _ { 0 } > i _ { 0 } )$ such that $P _ { j _ { i } }$ has the vertex $X$ in common with $P _ { i _ { \{ \cdot \} } }$ .

Now we construct the new system $\pi \mathcal { P } = \big ( P _ { 1 } ^ { \prime } , \dots , P _ { n } ^ { \prime } \big )$ as follows:

Set $I _ { k } ^ { \prime } = P _ { k }$ for all $\vec { k } \neq i _ { 0 } , j _ { 0 }$ .   
The ncw path $P _ { i _ { \uparrow \uparrow } } ^ { \prime }$ gocs from $A _ { \dot { \iota } _ { \mathsf { I } } }$ to $X$ along $P _ { j , y }$ , and then continues   
to $B _ { \sigma ( j _ { 1 } ) } )$ along $P _ { j _ { 0 } }$ Similarly, $P _ { j _ { \mathrm { t } } } ^ { \prime }$ goes from $A _ { j _ { \ell } }$ to $X$ along $P _ { j _ { 0 } }$ and continues to $B _ { \sigma ( i _ { 0 } ) }$ along $P _ { \mathit { i } _ { \mathrm { t } } }$ .

Clearly $\pi ( \pi \mathcal { P } ) = \mathcal { P }$ , since the index $i _ { \updownarrow }$ , the vertex $X$ , and the index $j _ { 0 }$ are the same as before. In other words, applying $\pi$ twice we switch back to the old paths $P _ { i }$ . Next, since $\pi \mathcal { P }$ and $p$ use precisely the same edges, we certainly have $w ( \pi \mathcal { P } ) = w ( \mathcal { P } )$ . And finally, since the new permutation $\sigma ^ { \prime }$ is obtained by multiplying $\sigma$ with the transposition $\left( i _ { 0 } , j _ { \parallel } \right)$ , we find that sign $\pi \mathcal { P } \ \underline { { \mathcal { \cdots } } } \ - \mathfrak { s i g n } \mathcal { P }$ , and that's it. □

The Gessel-Viennot Lemma can be used to derive all basic properties of determinants, just by looking at appropriate graphs. Let us consider one particularly striking example, the formula of Binet-Cauchy. which gives a very uscful generalization of the product rule for determinants.

![](images/5914f7e6c7356604ce0d0387da4476fc176d2667da0aa9dea999d840ebacd9e9.jpg)

![](images/44202874c3a442226fbf0d643eebfd2ce9e73bc690f3b7a75469816a7327eec1.jpg)

20 20 20 2 fac 1 1

Theorem. If $P$ is an $( r \times s )$ -matrix and $Q$ an $( s \times r )$ -matrix, $r \leq s ,$ then where $P z$ is the $( r \times r )$ -submatrix of $P$ with column-set $\mathcal { Z }$ , and $Q z$ the $( r \times r )$ -submatrix of $C$ with the corresponding rows $\mathcal { Z }$ .

$$
\operatorname * { d e t } ( P Q ) = \sum _ { z } ( \operatorname * { d e t } P _ { z } ) ( \operatorname * { d e t } Q { z } ) ,
$$

Proof. Let the bipartite graph on $\mathcal { A }$ and $\beta$ correspond to $I ^  \}$ as before, and similarly the bipartite graph on $B$ and $\mathcal { C }$ to $C$ . Consider now the concatenated graph as indicated in the figure on the left, and observe that the $( i , j )$ - entry $m _ { i j }$ of the path matrix $M$ from $\mathcal { A }$ to $\mathcal { C }$ is precisely $\begin{array} { r } { m _ { i j } = \sum _ { k } p _ { i k } q _ { k j } } \end{array}$ thus $M = P Q$ .

![](images/7ff7cab8e4b40a54c5b359e17e7dbbecebc8e2ae83af4d195d49c8f69e770e21.jpg)

Since the vertex-disjoint path systems from $\mathcal { A }$ to $\mathcal { C }$ in the concatenated graph correspond to pairs of systems from $\mathcal { A }$ to $\mathcal { Z }$ resp. from $\mathcal { Z }$ to $\mathcal { C }$ , the result follows immediately from the Lemma, by noting that sign $\left( \sigma \tau \right) =$ (sign $\sigma$ ) (sign 7).

The Lemma of Gessel-Viennot is also the source of a great number of results that relate determinants to enumerative properties. The recipe is always the same: Interpret the matrix $M$ as a path matrix, and try to compute the right-hand side of (3). As an illustration we will consider the original problem studied by Gessel and Viennot, which led them to their Lemma:

Suppose that $a _ { 1 } < a _ { 2 } < \ldots < a _ { n }$ and $b _ { 1 } < b _ { 2 } < \ldots < b _ { n }$ are two sets of natural numbers. We wish to compute the determinant of the matrix $\mathcal { M } = ( m _ { i j } )$ where ${ m } _ { i j }$ is the binomial coeffcient $\binom { a _ { i } } { b _ { j } }$

In other words, Gessel and Viennot were looking at the determinants of arbitrary square matrices of Pascal's triangle, such as the matrix

$$
\begin{array} { r l r } { \operatorname* { d e t } \left( \begin{array} { c c c } { \langle ^ { 3 } _ { 1 } \rangle } & { \langle ^ { 3 } _ { 3 } \rangle } & { \binom { 3 } { 4 } } \\ { \binom { 4 } { 1 } } & { \binom { 4 } { 3 } } & { \binom { 4 } { 4 } } \\ { \binom { 6 } { 1 } } & { \binom { 6 } { 3 } } & { \binom { 6 } { 4 } } \end{array} \right) } & { = } & { \operatorname* { d e t } \left( \begin{array} { c c c } { 3 } & { 1 } & { 0 } \\ { 4 } & { 4 } & { 1 } \\ { 6 } & { 2 0 } & { 1 5 } \end{array} \right) } \end{array}
$$

given by the bold entries of Pascal's triangle, as displayed in the margin.

As a preliminary step to the solution of the problem we recall a well-known result which connects binomial coefficients to lattice paths. Consider an $a \times b$ -lattice as in the margin. Then the number of paths from the lower left-hand corner to the upper right-hand corner, where the only steps that ${ \binom { a ^ { - } - b } { a } }$

The proof of this is easy: each path consists of an arbitrary sequence of $b$ "east" and $a$ "north" steps, and thus it can be encoded by a sequence of the form NENEEEN, consisting of $a + b$ letters, $a$ N's and $\delta \mathbf { E } ^ { \prime } \mathbf { s }$ The number of such strings is the number of ways to choose $a$ positions of letters $\mathbf { N }$ from a total of $a + b$ positions, which is ${ \binom { a + b } { a } } = { \binom { a + b } { b } }$

Now look at the fgure to the right, where $\varLambda _ { i }$ is placed at the point $\left( \mathbb { 0 } , - { \boldsymbol { n } } _ { i } \right)$ and $B _ { j }$ at $( b _ { j } , - b _ { j } )$ .

The number of paths from $A _ { i }$ to $B _ { j }$ in this grid that use only steps to the $\left( { \begin{array} { c } { b _ { j } + ( a _ { i } - b _ { j } ) } \\ { b _ { j } } \end{array} } \right) \ = \ \left( { \begin{array} { c } { a _ { i } } \\ { b _ { j } } \end{array} } \right) ,$ In  other words, the matrix of binomials $\lambda \mathcal { I }$ is precisely the path matrix from $A$ to $\mathfrak { z }$ in the directed lattice graph for which all edges have weight 1, and all edges are directed to go north or east. Hence to compute det $M$ we may apply the Gessel-Viennot Lemma. A moment's thought shows that every vertexdisjoint path system $\mathcal { P }$ from $\boldsymbol { A }$ to $\boldsymbol { \it { \it B } }$ must consist of paths $P _ { i } : A _ { i }  B _ { i }$ for all $i$ Thus the only possible permutation is the identity, which has sign ${ } = 1$ , and we obtain the beautiful result

In particular, this implies the far from obvious fact that det $M$ is always nonnegative, since the right-hand side of the equality counts something. More precisely, one gets from the Gessel-Viennot Lemma that det $M = 0$ if and only if ${ a _ { i } < b _ { i } }$ for some $i$ .

In our previous small example,

![](images/6c03b70abc1c78005cc0b6bc2c1be42db51704e19e2c495b27ee13d949815ac5.jpg)

![](images/3ccd903f4c86a81d28017b4f0ed4951b8554d4fb8f5061344efbeed3c81f7fe0.jpg)  
"Lattice paths"

![](images/98f2dccd7ff1dd3b7850edd42d236eb66c5f8b8c2c6a3cf9aa135544de730174.jpg)

# References

[1] I. M. GESSEl. & G. VIENNOT: Binomial determinants, paths, and hook length formulae, Advances in Math. 58 (1985), 300-321.

[2] B. LINDSTRöM: On the vector representation of induced matroids, Bulletin London Math. Soc. 5 (1973), 85-90.

# Cayley's formula for the number of trees

One of the most beautiful formulas in enumerative combinatorics concerns the number of labeled trees. Consider the set $N = \{ 1 , 2 , \ldots , n \}$ .How many different trees can we form on this vertex set? Let us denote this number by $T _ { n }$ . Enumeration "by hand" yields $T _ { 1 } = 1 , T _ { 2 } = 1 , T _ { 3 } = 3$ . $T _ { 4 } = 1 6$ , with the trees shown in the following table:

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } { { 3 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { } { } & { { } } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } \end{array}
$$

Note that we consider labeled trees, that is, although there is only one tree of order 3 in the sense of graph isomorphism, there are 3 different labeled trees obtained by marking the inner vertex 1, 2 or 3. For $n = 5$ there are three non-isomorphic trees:

5 A

For the first tree there are clearly 5 different labelings, and for the second and third there are $\frac { 5 ! } { 2 } = 6 0$ labelings, so we obtain $T _ { 5 } = 1 2 5$ This should be enough to conjecture $T _ { n } = n ^ { n - 2 }$ , and that is precisely Cayley's result.

Theorem. There are $n ^ { \mathit { n } - 2 }$ different labeled trees onn vertices.

This beautiful formula yields to equally beautiful proofs, drawing on a variety of combinatorial and algebraic techniques. We will outline three of them before presenting the proof which is to date the most beautiful of them all.

![](images/32576030111c01af57d99508a5bbe8f689d1aa6f2f08abff7d060299eaabe0ff.jpg)

Arthur Cayley

First proof (Bijection). The classical and most direct method is to find a bijection from the set of all trees on $\gamma _ { \ell }$ vertices onto another set whose cardinality is known to be $\hbar ^ { \gamma _ { l } , - 2 }$ Naturally, the set of all ordered sequences $\left( a _ { 1 } , \ldots , a _ { n - 2 } \right)$ with $1 \leq a _ { i } \leq n$ comes into mind. Thus we want to uniquely encode every trec $T$ by a sequence $( a _ { 1 } \ldots , a _ { n } \ldots 2 )$ . Such a code was found by Prüfer and is contained in most books on graph theory.

1 1 1   
2 2 ② 2

The four trees of $\mathcal { T } _ { 2 }$

Here we want to discuss another bijection proof, due to Joyal, which is less known but of equal elegance and simplicity. For this, we consider not just trees $t$ on $N = \{ 1 , \ldots , \pi \}$ but trees together with two distinguished vertices, the left end $\bigcirc$ and the right end $\sqsubset$ ,which may coincide. Let $T _ { n } = \{ ( t ; \bigcirc , \bigcirc ) \}$ be this new set; then, clearly, $| T _ { n } | = n ^ { 2 } T _ { n }$ .

Our goal is thus to prove $| { \mathcal { T } } _ { n } | = n ^ { \gamma _ { l } }$ . Now there is a set whose size is known to bc ${ \boldsymbol { n } } ^ { n }$ , namely the sct $N ^ { N }$ of all mappings from $N$ into $N$ .Thus our formula is proved if we can find a bijection from $N ^ { N }$ onto $\mathcal { T } _ { \mathfrak { n } }$

Let $f : N \longrightarrow N$ be any map. We represent $\boldsymbol { \mathscr { f } }$ as a directed graph $\vec { \tilde { G } _ { f } }$ by drawing arrows from $i$ to $\textstyle \int ( i )$ .

![](images/37fdc7b8921ad97d07be1df089c7b5d915407a7bfbd4091286bf30036c7cda67.jpg)

For example, the map

$$
f = \left( \begin{array} { l l l l l l l l l l l } { 1 } & { 2 } & { 3 } & { 4 } & { 5 } & { 6 } & { 7 } & { 8 } & { 9 } & { 1 0 } \\ { 7 } & { 5 } & { 5 } & { 9 } & { 1 } & { 2 } & { 5 } & { 8 } & { 4 } & { 7 } \end{array} \right)
$$

is represented by the directed graph in the margin.

Look at a component of $\vec { G } _ { f }$ Sinc theres precsely ne  anai from each vertex, thc component contains cqually many vertices and edges, and hence precisely one dirccted cycle. Let $M \subsetneq N$ be the union of the vertex sets of these cycles. A moment's thought shows that $M$ is the unique maximal subset of $N$ such that the restriction of $f$ onto $M$ acts as a bijection on $M$ Write $f | _ { M } = \left( \begin{array} { c c c c } { { a } } & { { b } } & { { \cdots } } & { { z } } \\ { { f \big ( a \big ) } } & { { f \big ( b \big ) } } & { { \cdots } } & { { f \big ( z \big ) } } \end{array} \right)$ such that the numbers $a , b , \ldots , z$ in the first row appear in natural order. This gives us an ordering $f ( a ) , f ( b ) , \ldots , f ( z )$ of $M$ according to the second row. Now $f ( \boldsymbol { a } )$ is our left end and $\textstyle \int ( z )$ is our right end.

The tree $t$ corresponding to the map $f$ is now constructed as follows: Draw $f ( a ) , \ldots , f ( z )$ in this order as a path from $f ( a )$ to $f ( z )$ , and fill in the remaining vertices as in $\vec { G } _ { f }$ (deleting the arrows).

![](images/caf047a71874eda4775f47997df66b8abba4167868a7691073033dea812ea4b5.jpg)

In our example above we obtain $\mathcal { M } = \{ 1 , 4 , 5 , 7 , 8 , 9 \}$

$$
f | _ { M } = \left( \begin{array} { c c c c c c } { { 1 } } & { { 4 } } & { { 5 } } & { { 7 } } & { { 8 } } & { { 9 } } \\ { { 7 } } & { { 9 } } & { { 1 } } & { { 5 } } & { { 8 } } & { { 4 } } \end{array} \right)
$$

and thus the tree $t$ depicted in the margin.

It is immediate how to reverse this correspondence: Given a tree $t$ , we look at the unique path $P$ from the left end to the right end. This gives us the set $M$ and the mapping $f \vert \chi _ { I }$ . The remaining correspondences $i  f ( i )$ are then filled in according to the unique paths from $i$ to $P$ .

Second proof (Linear Algebra). We can think of $T _ { n }$ as the number of spanning trees in the complcte graph $K _ { n }$ . Now let us look at an arbitrary connected simple graph $G$ on $V ~ = ~ \{ 1 , 2 , . . . , n \}$ , denoting by $t ( G )$ the number of spanning trees; thus $T _ { n } ~ = ~ \ell ( K _ { \eta _ { i } } )$ . The following celebrated result is Kirchhoff's matrix-tree theorem (see [1]). Consider the incidence matrix $\beta = ( b _ { i \epsilon } )$ of $G$ , whose rows are labeled by $V$ , the columns by $E$ , where we write $b _ { i , \mathscr { C } } = 1$ or 0 depending on whether $i \in \mathcal { C }$ or $\textit { i } \not \in \textit { e }$ .Note that $| E | \ge \hbar ^ { 2 } - 1$ since $G$ is connected. In every column we replace one of the two I's by $- 1$ in an arbitrary manner (this amounts to an orientation of $G$ ), and call the new matrix $C$ . $\boldsymbol { M } = \boldsymbol { C } \boldsymbol { C } ^ { \prime \prime }$ is then a symmetric $( n \times n )$ -matrix with the degrees $d _ { 1 } , \ldots , d _ { n } ^ { \phantom { \dagger } }$ in the main diagonal.

Proposition. We have $t ( G ) = \operatorname* { d e t } M _ { i i }$ for all $i = 1 , \ldots , n$ , where $\ M _ { i i }$ results from M by deleting the $i$ -th row and the $i$ -th column.

Proof. The key to the proof is the Binet-Cauchy theorem provcd in the previous chapter: When $\boldsymbol { p }$ is an $( r \times s )$ -matrix and $Q$ an $( s \times r )$ -matrix, $r ~ \leq ~ s$ , then $\mathrm { d e t } ( P Q )$ equals the sum of the products of determinants of corresponding $( \boldsymbol r \times \boldsymbol r \boldsymbol \nu )$ -submatrices, where "corresponding" means that we take the same indices for the $\gamma$ columns of $P$ and the $r$ rows of $Q$ .

For $M _ { i i }$ this means that

$$
\mathrm { d e t } M _ { i i } \ = \ \sum _ { N } \mathrm { d e t } N \cdot \mathrm { d e t } N ^ { T } \ = \ \sum _ { N } ( \mathrm { d e t } N ) ^ { 2 } ,
$$

where $\mathcal { N }$ runs through all $( n - 1 ) \times ( n - 1 )$ submatrices of $C \backslash \{ \mathsf { r o w } i \}$ The $ \hbar - 1$ columns of $N$ correspond to a subgraph of $G$ with $n - 1$ edges on $n$ vertices, and it remains to show that

$$
\operatorname* { d e t } N = { \left\{ \begin{array} { l l } { \pm 1 } & { { \mathrm { i f ~ t h e s e ~ e d g e s ~ s p a n ~ a ~ t r e e } } } \\ { \quad 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

Suppose the $n - 1$ edges do not span a tree. Then there exists a component which does not contain $i$ .Since the corresponding rows of this component add to O, we infer that they are linearly dependent, and hence det $N = 0$ .

Assume now that the columns of $N$ span a tree. Then there is a vertex $j _ { 1 } \neq i$ of degree 1; let $\epsilon _ { 1 }$ be the incident edge. Deleting $j _ { 1 } , e _ { 1 }$ we obtain a tree with $n - 2$ edges. Again there is a vertex $j _ { 2 } \neq i$ of degree I with incident edge $\mathcal { C } _ { 2 }$ Continue in this way until $j _ { 1 } \colon j _ { 2 } , \ldots , j _ { n - 1 }$ and $\boldsymbol { \mathscr { e } } _ { 1 } , \boldsymbol { \mathscr { e } } _ { : 2 } , \dots , \boldsymbol { \mathscr { e } } _ { \cdot n - 1 }$ with $j _ { i } \in \boldsymbol { \epsilon } _ { i }$ are determined. Now permute the rows and columns to bring $j _ { k }$ into the $k$ -th row and $e _ { k }$ into the $k$ -th column. Since by construction $j _ { k } \notin \epsilon _ { \ell }$ for $k < \ell .$ , we see that the new matrix $N ^ { \prime }$ is lower triangular with all clements on the main diagonal equal to $\pm 1$ Thus det $N = \pm \mathsf { d e t } N ^ { \prime } = \pm 1$ , and we are done.

For the special case $\vec { G } = \vec { K _ { n } }$ we clearly obtain

$$
M _ { i i } = \left( \begin{array} { c c c c } { { n - 1 } } & { { - 1 } } & { { \ldots } } & { { - 1 } } \\ { { - 1 } } & { { n - 1 } } & { { } } & { { - 1 } } \\ { { \vdots } } & { { } } & { { \ddots } } & { { \vdots } } \\ { { - 1 } } & { { - 1 } } & { { \ldots } } & { { n - 1 } } \end{array} \right)
$$

and an easy computation shows det $\lambda \mathbf { \cdot } f _ { i ; i } = n ^ { \mathbf { \cdot } n }$ 2.

![](images/49c027dbf04c14518dbec4a023dce3af0d653dbc4ab24e24c43aebfd9ef37347.jpg)

"A nonstandard method of counting trees: Put a cat into each tree, walk your dog, and count how often he barks."

For example, $T _ { \cdot 1 , 2 } = 8$ for $A = \left. 1 , 2 \right.$

![](images/1fa93209660c990b34dd11ae16a9137bd96a0410d152f262713bd5f9fb8a42d1.jpg)

Third proof (Recursion). Another classical mcthod in enumerative combinatorics is to establish a recurrence relation and to solve it by induction. The following idea is essentially due to Riordan and Rényi. To find the proper recursion, we consider a more gencral problem (which already appears in Cayley's papcr). Let $A$ be an arbitrary $k$ -set of the vertices. By $T _ { n , k }$ we denote the number of (labeled) forests on $\{ \boldsymbol { 1 } , \ldots , \boldsymbol { n } \}$ consisting of $k$ trees where the vertices of $A$ appear in different trees. Clearly, the set A does not matter, only the size k. Note that Tn, i = Tn.

$$
\ ! \times \{ \begin{array} { c c c c c c c c c c c } { { 3 } } & { { 2 } } & { { 1 } } & { { 2 } } & { { 1 } } & { { 2 } } & { { 1 } } & { { 2 } } & { { 1 } } & { { 2 } } & { { 1 } } & { { 2 } } & { { 1 } } & { { 2 } } & { { 1 } } & { { 2 } } & { { 1 } } & { { 2 } } & { { 1 } } \\ { { 3 } } & { { 4 } } & { { 3 } } & { { 4 } } & { { 3 } } & { { 4 } } & { { 3 } } & { { 4 } } & { { 3 } } & { { 4 } } & { { 3 } } & { { 4 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 2 } } & { { 1 } } & { { 2 } } & { { 4 } } \end{array} \}
$$

Consider such a forest F with A = {1, 2, . . . , k}, and suppose 1 is adjacent to $i$ vertices, as indicated in the margin. Deleting 1, the $i$ neighbors together with $2 , \ldots , k$ yield one vertex each in the components of a forest that consists of k - 1 + i trees. As we can (re)construct F by first fixing i, then choosing the $i$ neighbors of 1 and then the forest $F ^ { \prime } \backslash \{ 1$ , this yields

$$
T _ { n , k } \ = \ \sum _ { i = 0 } ^ { n - k } { \binom { n - k } { i } } T _ { n - 1 , k - 1 + i } ^ { \ }
$$

for all $r \geq k \geq 1$ , where we set $\mathcal { T } _ { 0 , 0 } = 1 , \mathcal { T } _ { n , 0 } = 0$ for $n > 0$ Note that $T _ { 0 , 0 } = 1$ is necessary to ensure $T _ { n , \tau \bar { \imath } } \ : \approx 1$ .

Proposition. We have and thus, in particular,

$$
{ \cal T } _ { \pi , k } ^ { \mathrm { ~ ~ } } = k \pi ^ { \mathrm { ~ } \mathrm { { r a } - k - 1 } }
$$

$$
T _ { n , 1 } = T _ { n } = n ^ { n - 2 } .
$$

Proof. By (1), and using induction, we find

$$
\begin{array} { r l } { T _ { n , k } ^ { - } } & { = \frac { n ^ { - \frac { k } { 2 } } } { \underset { k = 0 } { \overset { n } { \sum } } } ( \begin{array} { l } { n - k } \\ { i } \end{array} ) ( k - 1 + i ) ( n - 1 ) ^ { n - 1 + k - i } \quad \quad ( i \quad \cdot \cdot \ n  } \\ & { =   \sum _ { i = 1 } ^ { n } ( \begin{array} { l } { n } \\ { i } \end{array} ) ( n \quad , \quad i ) ( n - 1 ) ^ { i } ) ^ { - 1 } } \\ & { =  \frac { n ^ { - \frac { k } { 2 } } } { \underset { k = 0 } { \overset { n } { \sum } } } ( \begin{array} { l } { n - k } \\ { i } \end{array} ) ( n - 1 ) ^ { i } -  \sum _ { i = 1 } ^ { \infty } ( \begin{array} { l } { n - k } \\ { i } \end{array} ) ^ { i ( n - 1 ) } i ( n - 1 ) ^ { i - 1 }  } \\ & { =  \frac { n ^ { - \frac { k } { 2 } } } { \underset { k = 0 } { \overset { n } { \sum } } } ( \begin{array} { l } { n - k } \\ { i } \end{array} )  \underset { k = 1 } { \overset { n } { \sum } } ( \begin{array} { l } { n - 1 - k } \\ { i - 1 } \end{array} ) ( n - 1 ) ^ { i - 1 } } \\ & { =  n ^ { n - k } \quad \cdot ( n - k ) ) \underset { k = 0 } { \overset { n - 1 - k } { \sum } } ( \begin{array} { l } { n - 1 - k } \\ { i } \end{array} ) ( n - 1 ) ^ { \frac { k } { 2 } }  } \\ &  =  \frac { n ^ { - \frac { k } { 2 } } } { \underset { k = 0 } { \overset { n } { \sum } } } ( \begin{array} { l } { n - 1 - k } \\ { i } \end{array} )  \underset { k = 1 } { \overset { n } { \sum } } ( \begin{array} { l } { n - 1 - k } \\  1  \end{array} \end{array}
$$

Fourth proof (Double Counting). The following marvelous idea due to Jim Pitman gives Cayley's formula and its generalization (2) without induction or bijection — it is just clever counting in two ways.

A rooted forest on $\{ 1 , \ldots , n \}$ is a forest together with a choice of a root in each component tree. Let $\mathcal { F } _ { n , k }$ be the set of all rooted forests that consist of $k$ rooted trees. Thus $\mathcal { F } _ { n , 1 }$ is the set of all rooted trees.

Note that $| \mathcal { F } _ { n , 1 } | = n T _ { n }$ , since in every tree there are $n$ choices for the root. We now regard $F _ { n , k } \in \mathcal { F } _ { n , k }$ as a directed graph with all edges directed away from the roots. Say that a forest $F$ contains another forest $F ^ { \prime }$ if $F$ contains $F ^ { \prime }$ as directed graph. Clearly, if $F$ properly contains $F ^ { \prime }$ , then $F$ has fewer components than $F ^ { \prime }$ . The figure shows two such forests with the roots on top.

Here is the crucial idea. Call a sequence $F _ { 1 } , \ldots , F _ { k }$ of forests a refining sequence if $F _ { i } \in \mathcal { F } _ { n , i }$ and $F _ { i }$ contains $F _ { i + 1 }$ , for all $i$ .

Now let $F _ { k }$ be a fixed forest in $\mathcal { F } _ { n , k }$ and denote $\bullet$ by $N ( F _ { k } )$ the number of rooted trees containing $\vec { F } _ { k }$ , and $\bullet$ by $N ^ { * } ( F _ { k } )$ the number of refining sequences ending in $F _ { k }$ .

We count $N ^ { * } ( F _ { k } )$ in two ways, first by starting at a tree and secondly by starting at $F _ { k }$ . Suppose $F _ { 1 } ~ \in ~ \mathcal { F } _ { n , 1 }$ contains $F _ { k }$ . Since we may delete the $k - 1$ edges of $F _ { 1 } \backslash F _ { k }$ in any possible order to get a refining sequence from $F _ { 1 }$ to $F _ { k }$ , we find

F2 3   
2

$F _ { 2 }$ contains $F _ { 3 }$

3 20 4 R   
5 9   
1   
$F _ { 3 }$ 6   
10

$$
N ^ { * } ( F _ { k } ) = N ( F _ { k } ) ( k - 1 ) ! .
$$

Let us now start at the other end. To produce from $F _ { k }$ an $F _ { k - 1 }$ we have to add a directed edge, from any vertex $a$ , to any of the $k - 1$ roots of the trees that do not contain $a$ (see the figure on the right, where we pass from $F _ { 3 }$ to $F _ { 2 }$ by adding the edge $3 \bullet \substack { \longrightarrow } \bullet \ s \ 7 )$ Thus we have $n ( k - 1 )$ choices. Similarly, for $F _ { k - 1 }$ we may produce a directed edge from any vertex $b$ to any of the $k - 2$ roots of the trees not containing $b$ For this we have $n ( k { - } 2 )$ choices. Continuing this way, we arrive at

$$
N ^ { * } ( F _ { k } ) \ = \ n ^ { k - 1 } ( k - 1 ) ! ,
$$

and out comes, with (3), the unexpectedly simple relation

$$
N ( F _ { k } ) = n ^ { k - 1 } \qquad { \mathrm { f o r ~ } } a n y ~ F _ { k } \in { \mathcal { F } } _ { n , k } .
$$

For $k = n$ , $F _ { n }$ consists just of $n$ isolated vertices. Hence $N ( F _ { n } )$ counts the number  all ro trees, and webt $| { \mathcal { F } } _ { n , 1 } | = n ^ { n - 1 }$ , and thus Cayley's formula. □

But we get even more out of this proof. Formula (4) yields for $k = n$ :

$$
{ \# } \big \{ \mathrm { r e f i n i n g ~ s e q u e n c e s } ( F _ { 1 } , F _ { 2 } , \ldots , F _ { n } ) \big \} \ = \ n ^ { n - 1 } ( n - 1 ) ! .
$$

For $F _ { k } { \in } { \mathcal { F } } _ { n , k }$ , let $N ^ { * * } ( F _ { k } )$ denote the number of those refining sequences $F _ { 1 } , \ldots , F _ { n }$ whose $k$ -th term is $F _ { k }$ Clearly this is $N ^ { * } ( F _ { k } )$ times the number

![](images/edb150543c3337500dcef7df05903672950eb6c6283bd3c65a72c114cc96b9a3.jpg)

of ways to choose $( H _ { k + 1 } , \ldots , F _ { n } )$ But this latter number is $( n - k ) !$ since we may delete the $n . . . k$ edges of $F _ { k }$ in any possible way, and so

$$
N ^ { * * } ( F _ { k } ) ~ = ~ N ^ { * } ( F _ { k } ) ( n - k ) ! ~ = ~ n ^ { k - 1 } ( k - 1 ) ! ( n - k ) ! .
$$

Since this number does not depend on the choice of $F _ { k }$ , dividing (5) by (6) yields the number of rooted forests with $k$ trees:

$$
| { \mathcal F } _ { n , k } | ~ = ~ \frac { n ^ { n - 1 } ( n - 1 ) ! } { n ^ { k - 1 } ( k - 1 ) ! ( n - k ) ! } ~ = ~ \binom { n } { k } k n ^ { n - 1 - k } .
$$

As we may choose the $k$ roots in $\binom { n } { k }$ possible ways, we have reproved the formula $T _ { n , k } = k n ^ { n - k - 1 }$ witout recurse to ducion.

Let us end with a historical note. Cayley's paper from 1889 was anticipated by Carl W. Borchardt (1860), and this fact was acknowledged by Cayley himself. An equivalent result appeared even earlier in a paper of James J. Sylvester (1857), see [2, Chapter 3]. The novelty in Cayley's paper was the use of graph theory terms, and the theorem has been associated with his name ever since.

# References

[1] M. AIGNER: Combinatorial Theory, Springer-Verlag, Berlin Heidelberg New York 1979; Reprint 1997.   
[2] N. L. BIGGs, E. K. LLOYD & R. J. WILSON: Graph Theory 1736-1936, Clarendon Press, Oxford 1976.   
[3] A. CAYLEY: A theorem on trees, Quart. J. Purc Appl. Math. 23 (1889), 376-378; Collected Mathematical Papers Vol. 13, Cambridge University Press 1897, 26-28.   
[4] A. JoYAL: Une théorie combinatoire des séries formelles, Advances in Math. 42 (1981), 1-82.   
[5] J. PrrMAn: Coalescent random forests, J. Combinatorial Theory, Ser. A 85 (1999), 165-193.   
[6] H. PRC1;ER: Neuer Beweis eines Satzes über Permutationen, Archiv der Math. u. Physik (3) 27 (1918), 142-144.   
[7] A. RÉNYI: Some remarks on the theory of trees. MTA Mat. Kut. Inst. Kozl. (Publ. math. Inst. Hungar. Acad. Sci.) 4 (1959), 73-85; Selected Papers Vol. 2, Akadémiai Kiad6, Budapest 1976, 363-374.   
[8] J. RioRDAN: Forests of labeled trees, J. Combinatorial Theory 5 (1968), 90-103.

Some of the oldest combinatorial objects, whosc study apparently goes back to ancient times, are the Latin squares. To obtain a Latin square, one has to fill the $\pi ^ { 2 }$ cells of an $( n \times n )$ -square array with the numbers $1 , 2 , \ldots , n \ s 0$ that that every number appears exactly once in every row and in every column. In other words, the rows and columns cach represent permutations of the set $\{ 1 , \ldots , n \}$ . Let us call $n$ the order of the Latin square. Here is the problem we want to discuss. Suppose someone started filling the cells with the numbers $\{ 1 , 2 , \ldots , n \}$ . At some point he stops and asks us to fill in the remaining cells so that we get a Latin square. When is this possible? In order to have a chance at all we must, of course, assume that at the start of our task any element appears at most once in cvery row and in every column. Let us give this situation a name. We speak of a partial Latin square of order $\mathfrak { n }$ if some cells of an $( n \times n )$ -array are filled with numbers from the set $\{ 1 , \ldots , n \}$ such that every number appears at most once in every row and column. So the problem is:

# When can a partial Latin square be completed to a Latin square of the same order?

Let us look at a few examples. Suppose the first $n - 1$ rows are filled and the last row is empty. Then we can casily fill in the last row. Just note that every element appears $n - 1$ times in the partial Latin square and hence is missing from exactly one column. Hence by writing cach element below the column where it is missing we have completed the square correctly.

Going to the other end, suppose only the first row is filled. Then it is again easy to complete the square by cyclically rotating the elements one step in each of the following rows.

So, while in our first example the completion is forced, we have lots of possibilities in the second example. In general, the fewer cells are prefilled, the morc freedom we should have in completing the square.

However, the margin displays an example of a partial square with only $\gamma _ { \downarrow }$ cells filled which clearly cannot be completed, since there is no way to fill the upper right-hand corner without violating the row or column condition.

If fewer than n cells are filled in an $( \gamma _ { l } \times \gamma _ { l } )$ -array, can one then always complete it to obtain a Latin square?

![](images/cbce0aaecf193b763e733e2f30a18881b61bd7a5373e5509a3ee53d23756bc53.jpg)

A Latin square of order 4

A cyclic Latin square   
![](images/bc8add7008928f139ce5161d1a0494f7ca478b971421786c6b0d61285daf1f94.jpg)

![](images/e5c6902bfa55c20ca99e2d887425e0d8a1d1febe22a3c81fcc7ebc1c239fd766.jpg)

A partial Latin squarc that cannot be completed

This question was raised by Trevor Evans in 1960, and the assertion that a completion is always possible quickly became known as the Evans conjecture. Of course, one would try induction, and this is what finally led to success. But Bohdan Smetaniuk's proof from 1981, which answered the question, is a beautiful example of just how subtle an induction proof may be needed in order to do such a job. And, what's more, the proof is constructive, it allows us to complete the Latin square explicitly from any initial partial configuration.

R: 1 1 1 2 2 2 3 3 3   
C:123123123   
E: 1 3 2 2 1 3 3 2 1

![](images/1c1480cd8eb58e4704f19c03301b8203469da631b4211fdce16334adc717fbc3.jpg)

If we permute the lines of the above example cyclically,   
$R \longrightarrow C \longrightarrow E \longrightarrow R ,$ then we oblain the following line array and Latin square:

![](images/07f4693acac76c2f8168ef69efe87b700bc94a617cf714859104e8adebc50626.jpg)

$\begin{array} { r } { R : \textbf { \ i } 3 2 \textbf { \ i } 3 3 2 \textbf { \ i } } \\ { C : \textbf { \ i } \mid \textbf { \ i } 1 \ge 2 \textbf { \ i } 3 3 \textbf { \ i } } \\ { E : \textbf { \ i } 2 \textbf { \ i } 2 \textbf { \ i } 2 \textbf { \ i } 3 } \end{array}$

Before proceeding to the proof let us take a closer look at Latin squares in general. We can alternatively view a Latin square as a $( 3 \times n ^ { 2 } )$ -array, called the line array of the Latin square. The figure to the left shows a Latin square of order 3 and its associated line array, where $R , C$ and $E$ stand for rows, columns and elements.

The condition on the Latin square is equivalent to saying that in any two lines of the line array all $\eta ^ { 2 }$ ordered pairs appear (and therefore each pair appears exactly once). Clearly, we may permute the symbols in each line arbitrarily (corresponding to permutations of rows, columns or elements) and still obtain a Latin square. But the condition on the $( 3 \times n ^ { 2 } )$ -array tells us more: There is no special role for the elements. We may also permute the lines of the array (as a whole) and still preserve the conditions on the line array and hence obtain a Latin square.

Latin squares that are connected by any such permutation are called conjugates. Here is the observation which will make thc proof transparent: A partial Latin square obviously corresponds to a partial line array (every pair appears at most once in any two lines), and any conjugate of a partial Latin square is again a partial Latin square. In particular, a partial Latin square can be completed if and only if any conjugate can be completed (just complete the conjugate and then reverse the permutation of the three lines).

We will need two results, due to Herbert J. Ryser and to Charles C. Lindner, that were known prior to Smetaniuk's theorem. If a partial Latin square is of the form that the first $r$ rows are completely filled and the remaining cells are empty, then we speak of an $( r \times n )$ -Latin rectangle.

Lemma 1. Any $( r \times n )$ -Latin rectangle, $r ^ { \nu } < \ n _ { \tau }$ can be extended to an $( ( r + 1 ) \times n )$ -Latin rectangle and hence can be completed to a Latin square.

Proof. We apply Hall's theorem (see Chapter 23). Let $A _ { j }$ be the set of numbers that do not appear in column $j$ An admissible $( \gamma + 1 )$ -st row corresponds then precisely to a system of distinct representatives for the collection $A _ { 1 } , \ldots , A _ { r k }$ . To prove the lemma we therefore have to verify Hall's condition (H). Every set $A _ { j }$ has size $n - r$ , and every element is in precisely $n - r$ sets $A _ { j }$ (since it appears $\mathbf { \nabla } ^ { \mathbf { \cdot } \mathbf { \nabla } ^ { \mathbf { \cdot } } }$ times in the rectangle). Any m of the sets $A _ { j }$ contain together $m ( \eta , - \mathbf { \nabla } \mathbf { r } )$ elements and therefore at least m different ones, which is just condition (H). □

Lemma 2. Let $P$ be a partial Latin square of order n with at most $n - 1$ cells filled and at most $\frac { \pi } { 2 }$ distinct elements, then $P$ can be completed to a Latin square of order $\mathscr { n }$ .

Proof. We first transform the problem into a more convenient form. By the conjugacy principle discussed above, we may replace the condition "at most $\frac { \pi } { 2 }$ distinct elements" by the condition that the entries appear in at most $\frac { r { \imath } } { 2 }$ rows, and we may further assume that these rows are the top rows. So let the rows with filled cells be the rows $1 , 2 , \ldots , r$ , with $f _ { i }$ filled cels in row $i$ where $r \leq \frac { \pi } { 2 }$ and $\textstyle \sum _ { i = 1 } ^ { r } f _ { i } \leq \eta _ { \bar { \imath } } - 1$ By perimuting the rows, we may assume that $f _ { 1 } \geq f _ { 2 } \geq \ldots \geq f _ { \tau } .$ . Now we complete the rows $1 \ldots \ldots , r$ step by step until we reach an $( T \times n )$ -rectangle which can then be extended to a Latin square by Lemma 1.

Suppose we have already filled rows $1 , 2 , \ldots , \ell - 1$ .In row $\ell$ there are $\int E$ filled cells which we may assume to be at the end. The current situation is depicted in the figure, where the shaded part indicates the filled cells.

The completion of row $\ell$ is performed by another application of Hall's theorem, but this time it is quite subtle. Let $X$ be the set of clements that do not appear in row $l$ thus $| X | = \pi - \int \ell$ ,and for $j = 1 , \ldots , n - f _ { \ell }$ let $\varLambda _ { j }$ denote the set of those elements in $X$ which do not appcar in column $j$ (neither above nor below row $\ell$ ). Hence in order to complete row $f$ we must verify condition $( \mathrm { H } )$ for the collection $A _ { 1 } , \ldots , A _ { n - f _ { \ell } }$ .

First we claim

$$
n - f _ { \ell } - \ell + 1 > \ell - 1 + f _ { \ell + 1 } + \dots + f _ { r } .
$$

The case $\ell = 1$ is clear. Otherwise $\begin{array} { r } { \sum _ { i = 1 } ^ { r } f _ { i } < n , f _ { 1 } \geq . . . \geq f _ { r } } \end{array}$ and $1 < \ell \leq r$ together imply

$$
n ~ > ~ \sum _ { i = 1 } ^ { r } f _ { i } ~ \geq ~ ( \ell - 1 ) f _ { \ell - 1 } + f _ { \ell } + . . . + f _ { r } .
$$

Now either $f _ { \ell - 1 } > 2$ (in which case (1) holds) or $f _ { \hat { \ell } - 1 } ^ { \ast } = 1$ . In the latter case, (1) reduces to $n > 2 ( \ell - 1 ) + r - \ell + 1 = r + \ell - 1$ , which is true because of $f \leq r \leq \frac { \pi } { 2 }$ .

Let us now take $m$ sets $A _ { j } , 1 \leq m \leq n - f _ { \ell }$ , and let $B$ be their union. We must show $| B | \geq m$ . Consider the number $\bar { \mathbf { \Omega } }$ of cells in the $m$ columns corresponding to the $A _ { j }$ 's which contain elements of $X$ . There are at most $( \ell - 1 ) \eta \eta$ such cells above row $\ell$ and at most $f _ { \ell + 1 } + \ldots + f _ { r }$ below row $i$ . and thus

$$
c \leq ( \ell - 1 ) m + f _ { \ell + 1 } + \ldots + f _ { r } .
$$

On the other hand, each element $x \in X \backslash B$ appears in each of the $m$ columns, hence $c \geq m ( | X | - | B | )$ , and therefore (with $| X \} = \pi - \ f _ { \ell } \}$

$$
\begin{array} { r l r } { | B | } & { \geq } & { | X | - \frac { 1 } { m } c ~ \geq ~ n - f _ { \ell } - \left( \ell - 1 \right) - \frac { 1 } { m } \{ f _ { \ell + 1 } + \cdot \cdot \cdot + f _ { r } \} . } \end{array}
$$

It follows that $| B | \geq \gamma \pi$ if

$$
\begin{array} { r } { n - f _ { \ell } \cdot \mathrm { ~ ( ~ \ell ~ - ~ 1 ~ ) ~ } - \frac { 1 } { m } ( f _ { \ell + 1 } + \ldots + f _ { r } ) \ > \ m - 1 , } \end{array}
$$

that is, if

$$
m ( n - f _ { \ell } - \ell + 2 - m ) > f _ { \ell + 1 } + \ldots + f _ { r } .
$$

![](images/1c3ba5eaf9ec4391d2f70c64eb98cd7082ddf293fda97d5527b8971fadbe246f.jpg)

A situation for $n = 8$ ,with $\ell = 3$ ${ f } _ { 1 } =$ $f _ { 2 } = f _ { 3 } = 2$ . $f _ { 4 } = 1$ .The dark squares represent the pre-filled cells, the lighter ones show the cells that have been filled in the completion process.

Inequality (2) is true for $m = 1$ and for $m = \eta _ { l } - f _ { \ell } - \ell + 1$ by (1), and hence for all values $m$ between 1 and $n - f _ { \ell } - \ell + 1$ , since the left-hand side is a quadratic function in m with leading coefficient $- 1$ . The remaining case is $m > n - f _ { \ell } - \ell + 1$ . Since any element $x$ of $X$ is contained in at most $\ell - 1 + f _ { \ell + 1 } + \ldots + f _ { r }$ rows, it can also appear in at most that many columns. Invoking (1) once more, we find that $_ { x }$ is in one of the sets $A _ { j }$ , so in this case $B = X , | B | = r _ { l } - f _ { \ell } \geq m _ { l }$ , and the proof is complete. □

![](images/23d3ed325ffd13dba0bf8181ce5c7d67e7a54b563bfdb86c238cbe5a7614e5fe.jpg)

![](images/8688c98cd5be1d8d7e751f1a5f3c20f06d7a9b17270402c6cb8a02b58e4d0a16.jpg)

Let us finally prove Smetaniuk's theorem.

Theorem. Any partial Latin square of order nt with at most $n - 1$ filled cells can be completed to a Latin square of the same order.

Proof. We use induction on $\mathscr { n }$ , the cases $n \leq 2$ being trivial. Thus we now study a partial Latin square of order $\pi \geq 3$ with at most $n - 1$ filled cells. With the notation used above these cells lie in $r \leq n - 1$ different rows numbered $s _ { 1 } , \ldots , s _ { r }$ , which contain $f _ { 1 } , \ldots , f _ { r } > 0$ filled cells, with $\textstyle \sum _ { i = 1 } ^ { r } f _ { i } \leq r _ { i } - 1$   
$\frac { n } { 2 }$   
renumbering and permutation of rows (if necessary) we may assume that the element $\mathscr { n }$ occurs only once, and this is in row $s _ { 1 }$ .

In the next step we want to permute the rows and columns of the partial Latin square such that after the permutations all the filled cells lie below the diagonal — except for the cell filled with $n$ , which will end up on the diagonal. (The diagonal consists of the cells $( k , k )$ with $1 \leq k \leq n .$ We achieve this as follows: First we permute row $s _ { 1 }$ into the position $f _ { 1 }$ . By permutation of columns we move all the filled cells to the left, so that $\gamma _ { l } ,$ occurs as the last element in its row, on the diagonal. Next we move row $s _ { 2 }$ into position $1 + f _ { 1 } + f _ { 2 }$ , and again the filled cells as far to the left as possible. In general, for $1 < i \leq r$ we move the row $s _ { i }$ into position $1 + f _ { 1 } + f _ { 2 } + \ldots + f _ { i }$ and the filled cells as far left as possible. This clearly gives the desired set-up. The drawing to the left shows an example, with $n = 7$ the rows $s _ { \mathrm { ~ l ~ } } = ~ 2$ , $s _ { 2 } = 3$ , $s _ { 3 } = 5$ and $s _ { 4 } = 7$ with $f _ { 1 } = f _ { 2 } = 2$ and $f _ { 3 } = f _ { 4 } = 1$ are moved into the rows numbered 2, 5, 6 and 7, and the columns are permuted "to the left" so that in the end all entries except for the single 7 come to lie below the diagonal, which is marked by s.

In order to be able to apply induction wc now rcmove the entry $\hbar$ from the diagonal and ignore the first row and the last column (which do not not contain any filled cells): thus we are looking at a partial Latin square of order $n - 1$ with at most $\pi \cdots 2$ filled cells, which by induction can be completed to a Latin square of order $n - 1$ The margin shows one (of many) completions of the partial Latin square that arises in our example. In the figure, the original entries are printed bold. They are already final, as are all the elements in shaded cells; some of the other entries will be changed in the following, in order to complete the Latin square of order $\gamma 2 .$ . In the next step we want to move the diagonal elements of the square to the last column and put entrics ri onto the diagonal in their place. However, in general we cannot do this, since the diagonal elements need not be distinct. Thus we proceed more carefully and perform successivcly, for $\ v { k } : = 2 , 3 , \dotsc , \ v { n } - 1$ (in this order), the following operation:

Put the value n into the cell $( k , n )$ This yields a correct partial Latin square. Now exchange the value $x _ { k }$ in the diagonal cell $( k , k )$ with the value n in the cell $( k , n )$ in the last column.

If the value $x _ { k }$ did not already occur in the last column, then our job for the current $k$ is complcted. After this, the current elements in the $k$ -th column will not be changed any more.

In our example this works without problems for $k = 2$ , 3 and 4, and the corresponding diagonal elements 3, 1 and 6 move to the last column. The following thrcc figures show the corresponding operations.

![](images/a74f01920e2bb13e6ef14bf89a109c8b6d9203d6ea438f8e5dca3fe5579b7b62.jpg)

Now we have to treat thc case in which there is already an element $x _ { k }$ in the last column. In this case we proceed as follows:

If there is already an element $x _ { k }$ in $^ a$ cell $( j , n )$ with $2 \leq j < k _ { : }$ ,then we exchange in row $j$ the element $x _ { k }$ in the $n$ -th column with the element $\boldsymbol { x } _ { k } ^ { \prime }$ in the $k$ -th column. If the element $ { \boldsymbol { { x } } } _ { k } ^ { \prime }$ also occurs in a cell $( j ^ { \prime } , n )$ , then we also exchange the elements in the $j ^ { \prime }$ -th row that occur in the $\scriptstyle { \boldsymbol { \mathscr { n } } }$ -th and in the $k$ -th columns, and so on.

![](images/1ce85f6946fca43dd079ad0341796688b0067a773dd1bd69c00cca01a8f6329b.jpg)

If we proceed like this there will never be two equal entries in a row. Our exchange process ensures that there also will never be two equal elements in a column. So we only have to verify that the cxchange process bctween the $k$ -th and the $\boldsymbol { \mathscr { n } }$ -th column does not lead to an infinite loop. This can be seen from the following bipartite graph $G _ { k }$ : Its vertices correspond to the cells $( i , k )$ and $( j , n )$ with $2 \leq i , j \leq k$ whose elements might be exchanged. There is an edge between $( i , k )$ and $( j , \pi )$ if these two cells lie in the same row (that is, for $i = j ,$ , or if the cells before the exchange process contain the same element (which implies $i \neq j ,$ . In our sketch the edges for $i \stackrel { \cdot \cdot } { - } j$ are dotted, the others are not. All vertices in $G _ { k }$ have degree 1 or 2. The cell $\{ k , \pi \}$ corresponds to a vertex of degree 1; this vertex is the beginning of a path which leads to column $k$ on a horizontal edge, then possibly on a sloped edge back to column $\gamma \}$ , then horizontally back to column $k$ and so on. It ends in column $k$ at a value that does not occur in column $\mathscr { n }$ Thus the exchange operations will end at some point with a step where we move a new elcment into the last column. Then the work on column $k$ is completed, and the elements in the cells $( i , k )$ for $i \geq 2$ are fixed for good.

![](images/27f6b553022495a56eda52e605a1e5f1ccec02b0e3897d690b03710b7f2710c5.jpg)

![](images/1d24d7fad72feb0795e9962b91d7aa8a10e67e005e38ece2959902caf9846818.jpg)

In our example the "exchange case" happens for $k = 5$ : the element $z _ { 5 } = 3$ does already occur in the last column, so that entry has to be moved back to column $k = 5$ But the exchange element $x _ { 5 } ^ { \prime } = 6$ is not new either, it is exchanged by $x _ { 5 } ^ { \prime \prime } = 5$ , and this one is new.

![](images/4a4d8ba5e980a98407e2873d8a992c92b2575331e80fe4e0171724c6a8d7744a.jpg)

![](images/c9ead563581b2d5843383dabfc22fa41408d6ab4133d1976f35a7ad153e6d6ae.jpg)

Finally, the exchange for $k = 6 = \eta , - 1$ poses no problem, and after that the completion of the Latin square is unique:

![](images/c18be99689f5f7b0b1b79ec481df116998f1ebb921a692cce6156b8cedc6c1bf.jpg)

![](images/5f415460a0672cb79b31754ea506f3e8e693f1cea655415157e3f3f029b312c7.jpg)

![](images/c6dd68b3b7c20f3f4bc39ab69f9b8f4f9357413050d0b0f5be5fdd7fc4a3b99c.jpg)

... and the same occurs in general: We put an element $n$ into the cell $( n , n )$ , and after that the first row can be completed by the missing elements of the respective columns (see Lemma I), and this completes the proof. In order to get explicitly a completion of the original partial Latin square of order $n$ we only have to reverse the clement, row and column permutations of the first two steps of the proof. □

# References

[1] T. EvANs: Embedding incomplete Latin squares, Amer. Math. Monthly 67 (1960), 958-961.   
[2] C. C. LINDNER: On completing Latin rectangles, Canadian Math. Bulletin 13 (1970), 65-68.   
[3] H. J. RYSER: A combinatorial theorem with an application to Latin rectangles, Proc. Amer. Math. Soc. 2 (1951), 550-552.   
[4] B. SmETANIuK: A new construction on Latin squares I: A proof of the Evans conjecture, Ars Combinatoria 11 (1981 ), 155-172.

The four-color problem was a main driving force for the development of graph theory as we know it today, and coloring is still a topic that many graph theorists like best. Here is a simple-sounding coloring problem, raised by Jeff Dinitz in 1978, which defied all attacks until its astonishingly simple solution by Fred Galvin fifteen years later.

Consider $n ^ { 2 }$ cells arranged in an $( n \times n )$ -square, and let $( i , j )$ denote the cell in row i and column $j$ Suppose that for every cell $( i , j )$ we are given a set $C ( i , j )$ of n colors.

Is it then always possible to color the whole array by picking for each cell $( i , j )$ a color from its set $C ( i , j )$ such that the colors in each row and each column are distinct?

Since this is so easy, why should it be so much harder in the general case when the set $\textstyle C : = \bigcup _ { i , j } C ( i , j )$ contains even more than $n$ colors? The difficulty derives from the fact that not every color of $C$ is available at each cell. For example, whereas in the Latin square case we can clearly choose an arbitrary permutation of the colors for the first row, this is not so anymore in the general problem. Already the case $n = 2$ illustrates this difficulty.

Suppose we are given the color sets that are indicated in the figure. If we choose the colors 1 and 2 for the first row, then we are in trouble since we would then have to pick color 3 for both cells in the second row.

As a start consider the case when all color sets $C ( i , j )$ are the same, say $\{ 1 , 2 , \ldots , n \}$ . Then the Dinitz problem reduces to the following task: Fill the $( n \times n )$ -square with the numbers $1 , 2 , \ldots , n$ in such a way that the numbers in any row and column are distinct. In other words, any such coloring corresponds to a Latin square, as discussed in the previous chapter. So, in this case, the answer to our question is "yes."

Before we tackle the Dinitz problem, let us rephrase the situation in the language of graph theory. As usual we only consider graphs $G = \left( V , E \right)$ without loops and multiple edges. Let $\chi ( G )$ denote the chromatic number of the graph, that is, the smallest number of colors that one can assign to the vertices such that adjacent vertices receive different colors.

ln other words, a coloring calls for a partition of $V$ into classes (colored with the same color) such that there are no edges within a class. Calling a set $A \subseteq V$ independent if there are no edges within $A$ , we infer that the chromatic number is the smallest number of independent sets which partition the vertex set $V .$ .

![](images/d7aec08a4755bec30083987af34c5d7d323108dcceef6ea37383355c28bf7616.jpg)

{1, 2} {2, 3} {1, 3} {2, 3}

In 1976 Vizing, and three years later Erdós, Rubin, and Taylor, studied the following coloring variant which leads us straight to the Dinitz problem. Suppose in the graph $G = \left( V , E \right)$ we are given a set $C ( v )$ of colors for each vertex $\mathcal { V }$ .A list coloring is a coloring $c : V \longrightarrow \bigcup _ { v \in V } C ( v )$ where $c ( v ) \in C ( v )$ for each $\nu \in V$ . The definition of the list chromatic number $\chi _ { \ell } ^ { \mathrm { ~ ~ } } ( G )$ should now be clear: It is the smallest number $k$ such for any list of color sets $( \vec { \cdot } ( y )$ with $| { \hat { C } } _ { i } ^ { \dagger } ( i ) | = k$ for all $\smash { \ell : \ell \in V }$ there always exists a list coloring. Of course, we have $\chi _ { \_ i } ( G ) \leq | V |$ (we never run out of colors). Since ordinary coloring is just the special case of list coloring when all sets $C ( v )$ are equal, we obtain for any graph $G$

The graph $S _ { 3 }$

$$
\chi ( G ) ~ \leq ~ \chi _ { \ell } ( G ) .
$$

To get back to the Dinitz problem, consider the graph $S _ { \pi }$ which has as vertex set the $n ^ { 2 }$ cells of our $( n \times \pi )$ -array with two cells adjacent if and only if they are in the same row or column.

Since any $\pmb { \eta }$ cells in a row are pairwise adjacent we need at least n colors. Furthermore, any coloring with $n$ colors corresponds to a Latin square, with the cells occupied by the same number forming a color class. Since Latin squares, as we have seen, exist, we infer $\chi ( S _ { \mathfrak { n } } ) = \mathfrak { n }$ , and the Dinitz problem can now be succinctly stated as

$$
X _ { i } ( S _ { n } ) = n !
$$

{1,3}   
{1,2} {1,4} {2,3}   
{3.4} {2,4}

One might think that perhaps $\chi ( G ) = \chi _ { \ell } ( G )$ holds for any graph $G$ but this is a long shot from the truth. Consider the graph $G = K _ { 2 , 4 }$ . The chromatic number is 2 since we may use one color for the two left vertices and the second color for the vertices on the right. But now suppose that we are given the color sets indicated in the figure.

To color the left vertices we have the four possibilities $1 | 3 , 1 | 4 , 2 | 3$ and $2 | 4 ,$ but any one of these pairs appears as a color set on the right-hand side, so a list coloring is not possible. Hence $\chi _ { \ell } \left( G \right) \geq 3$ , and the reader may find it fun to prove $\chi _ { \ell } ( G ) = 3$ (there is no need to try out all possibilities!). Generalizing this example, it is not hard to find graphs $G$ where $\chi ( G ) = 2 ,$ but $\chi _ { \ell } \left( G \right)$ is arbitrarily large! So the list coloring problem is not as easy as it looks at first glance.

Back to the Dinitz problem. A significant step towards the solution was made by Jeanette Janssen in 1992 when she proved $x _ { \ell } ( S _ { \pi } ) \leq \pi + 1$ and the coup de gráce was delivered by Fred Galvin by ingeniously combining two results, both of which had long been known. We are going to discuss these two results and show then how they imply $\chi _ { \ell } ( \boldsymbol { S } _ { \boldsymbol { \mathfrak { n } } } ) = \boldsymbol { \mathfrak { n } }$ .

First we fix some notation. Suppose v is a vertex of the graph $G$ ,then we denote as before by $d ( \imath ) )$ the degree of $\mathcal { V }$ . In our square graph $S _ { \pi }$ every vertex has degree $2 \pi - 2$ , accounting for the $n - 1$ other vertices in the same row and in the same column. For a subset $\varLambda \subseteq V$ we denote by $G _ { 1 }$ the subgraph which has $A$ as vertex set and which contains all edges of $G$ between vertices of $A$ We call $G _ { 1 }$ the subgraph induced by $\varLambda$ , and say that $H$ is an induced subgraph of $G$ if $H = G _ { A }$ for some $A$ .

To state our first result we need directed graphs $\vec { G } = ( V , E )$ , that is, graphs where cvery edge $\mathcal { C }$ has an orientation. The notation $\vec { \mathcal { F } } = \left( \vec { \tau } , \vec { v } \right)$ means that there is an arc $\mathcal { C }$ , also denoted by $u \longrightarrow \{ \}$ , whose initial vertex is $u$ and whose terminal vertex is $v$ . It then makes sensc to speak of the outdegree $\alpha ^ { + } ( \imath )$ resp. the indegree $d ^ { - } ( v )$ , where $d ^ { + } ( v )$ counts the number of edges with $v$ as initial vertex, and similarly for $d ^ { - } ( v )$ ; furthermore, $d ^ { + } ( v ) + d \ O \left( v \right) = d ( v )$ . When we wrile $G$ , we mean the graph $\vec { G }$ without the orientations.

The following concept originated in the analysis of games and will play a crucial role in our discussion.

Definition 1. Let $\vec { C } ^ { \vec { \tau } } = ( V , E )$ be a directed graph. A kernel $K \subseteq V$ is a subsct of the vertices such that

(i) $K$ is independent in $G$ ,and ii) for every $u \notin K$ there exists a vertex $v \in K$ with an edge $u \longrightarrow v$ .

Lct us look at thc example in the figure. The set $\{ b , c , f \}$ constitutes a kernel, but the subgraph induced by $\{ a , c , c \}$ does not have a kernel since the three edges cycle through the vertices.

With all these preparations we are ready to state the first result.

Lemma 1. Let $\vec { \tilde { G } } = ( V , E )$ be a directed graph, and suppose that for each vertex $v \in V$ we have a color set $C ( \iota )$ that is larger than the outdegree, $| C ( v ) | \geq d ^ { + } ( v ) + 1$ . If every induced subgraph of $\vec { G }$ possesses a kernel, then there exists a list coloring of $G$ with a color from $C ( \upsilon )$ for each $v$ .

![](images/7dfa52f03a7dfd27b9649079b0f3f4c2a2d526ed6f6a824ffa88dca411e204e8.jpg)

Proof. We proceed by induction on $| V |$ For $| V | = 1$ there is nothing to prove. Choose a color $\begin{array} { r } { c \in C = \bigcup _ { v \in V } C ( v ) } \end{array}$ and set

$$
A ( c ) : = \{ \upsilon \in V : c \in C ( \upsilon ) \} .
$$

By hypothesis, the induced subgraph ${ { G } _ { A \left( c \right) } }$ possesses a kernel $K ( c )$ . Now we color all $v \in K ( c )$ with the color $c$ (this is possible since $K ( c )$ is independent), and delete $K ( c )$ from $G$ and $c$ from $C$ .Let $G ^ { \prime \prime }$ be the induced subgraph of $G$ on $V \backslash K ( c )$ with $C ^ { \prime } ( v ) = C ( v ) \backslash \mathfrak { c }$ as the new list of color sets. Notice that for cach $v \in A ( c ) \backslash K ( c )$ , the outdegree $\alpha ^ { + } \left( v \right)$ is decreased by at least 1 (due to condition (ii) of a kernel). So $d ^ { + } ( v ) + 1 \leq | C ^ { \prime } ( v ) |$ still holds in $\vec { G } ^ { \prime }$ . The same condition also holds for the vertices outside $\varLambda ( c )$ , since in this case the color sets $C ( v )$ remain unchanged. The new graph $G ^ { \prime \prime }$ contains fewer vertices than $G$ , and we are done by induction. □

The method of attack for the Dinitz problem is now obvious: We have to find an orientation of the graph $S _ { \pi }$ with outdegrees $d ^ { + } ( \imath ) \leq \hbar - 1$ for all $\mathcal { V }$ and which ensures the existence of a kernel for all induced subgraphs. This is accomplished by our second result.

Again wc need a few preparations. Recall (from Chapter 9) that a bipartite graph $G = ( X \cup Y , E )$ is a graph with the following property: The vertex set $V$ is split into two parts $X$ and $Y$ such that every edge has onc endvertex in $X$ and the other in $Y$ . In other words, the bipartite graphs are precisely those which can be colored with two colors (one for $X$ and one for $Y$ ).

![](images/1bf9209c7cdd8b6c0190c28883618de1bd938afc1c1b35f80555561e11ed4865.jpg)

Now we come to an important concept, "stable matchings," with a downto-earth interpretation. A maiching $M$ in a bipartite graph $G = ( X \cup Y , E )$ is a set of edges such that no two edges in $\smash { \lambda \mathcal { H } }$ have a common endvertex. In the displayed graph the edges drawn in bold lines constitute a matching.

A bipartite graph with a matching

The bold edges constitute a stable matching. In each priority list, the choice leading to a stable matching is printed bold.

Consider $X$ to be a set of men and $Y$ a set of women and interpret $u v \in E$ to mean that $u$ and $\mathcal { V }$ might marry. A matching is then a mass-wedding with no person committing bigamy. For our purposes we need a more refined (and more realistic?) version of a matching, suggested by David Gale and Lloyd S. Shapley. Clearly, in real life every person has preferences, and this is what we add to the set-up. In $\vec { G } = ( X \cup Y , E )$ we assume that for every $v \in X \cup Y$ there is a ranking of the set $\mathcal { N } ( v )$ of vertices adjacent to $v$ , $N ( v ) = \{ z _ { 1 } > z _ { 2 } > . . . > z _ { d ( v ) } \}$ Thus $z _ { 1 }$ is the top choice for $\mathcal { V }$ , followed by $z _ { 2 }$ , and so on.

Definition 2. A matching $M$ of $\hat { \boldsymbol { \mathfrak { x } } } = ( \boldsymbol { X } \cup \boldsymbol { Y } , \boldsymbol { E } )$ is called stable if the following condition holds: Whenever $u v \in E \backslash M , u \in X , v \in Y$ , then either $u y \in M$ with $y > r$ in $N ( u )$ or $x _ { 1 } , \in \mathbb { N }$ with $x > u$ in $N ( v )$ or both.

In our real life interpretation a set of marriages is stable if it never happens that $u$ and $\gamma$ are not married but $u$ prefers $\mathcal { V }$ to his partner (if he has one at all) and $\mathcal { V }$ prefers $u$ to her mate (if she has one at all), which would clearly be an unstable situation.

Before proving our second result let us take a look at the following example:

$$
\begin{array} { c c l } { { \{ A > C \} } } & { { { \imath } } } & { { \nonumber } } \\ { { \{ C > D > B \} } } & { { { \nonumber \nu } } } & { { \nonumber { \bf \mathscr { K } _ { \delta } ^ { \mu } } } } \\ { { \{ A > D \} } } & { { { \subset } } } & { { \nonumber \mathscr { C } } } \\ { { \{ A \} } } & { { d } } & { { \nonumber { \bf \mathscr { L } _ { \delta } } } } \end{array} \{array \begin{array} { c c l }  { A > d > a \} } \\ { { { \nu } _ { \delta } } } & { { { \{ b \} } } } \\ { { { c \nonumber \nu } } } & { { { \{ a > b \} } } } \end{array}
$$

Notice that in this example there is a unique largest matching $M$ with four edges, $M = \{ a C ; b B ; c D , d A \}$ , but $M$ is not stable (consider ${ \hat { c . A } } { \dagger }$ .

Lemma 2. A stable matching always exists.

Proof. Consider the following algorithm. In the first stage all men $u \in X$ propose to their top choice. If a girl receives more than one proposal she picks the one she likes best and keeps him on a string, and if she receives just one proposal she keeps that one on a string. The remaining men are rejected and form the reservoir $R$ , In the second stage all men in $R$ propose to their next choice. The women compare the proposals (together with the one on the string, if there is one), pick their favorite and put him on the string. The rest is rejected and forms the new set $R$ Now the men in $R$ propose to their next choice, and so on. A man who has proposed to his last choice and is again rejected drops out from further consideration (as well as from the reservoir). Clearly, after some time the reservoir $R$ is empty, and at this point the algorithm stops.

Claim. When the algorithm stops, then the men on the strings together with the corresponding girls form a stable matching.

Notice first that the men on the string of a particular girl move there in increasing preference (of the girl) since at each stage the girl compares the new proposals with the present mate and then picks the new favorite. Hence if $u v \in E$ but $u v \notin \mathcal { M }$ , then either $u$ never proposed to $v$ in which case he found a better mate before he even got around to $v$ ,implying $u y \in M$ with $y > v$ in $N ( u )$ , or $u$ proposed to $v$ but was rejected, implying $x v \in M$ with $x > u$ in $N ( v )$ . But this is exactly the condition of a stable matching. □

Putting Lemmas 1 and 2 together, we now get Galvin's solution of the Dinitz problem.

Theorem. We have $\chi _ { \ell } ( S _ { n } ) = n$ for all $n$ .

Proof. As before we denote the vertices of $S _ { n }$ by $( i , j ) , 1 \leq i , j \leq n$ . Thus $( i , j )$ and $( r , s )$ are adjacent if and only if $i \ = \ r$ or $j = s$ Take any Latin square $L$ with letters from $\{ 1 , 2 , \ldots , n \}$ and denote by $L ( i , j )$ the entry in cell $( i , j )$ . Next make $S _ { n }$ into a directed graph $\vec { S } _ { n }$ by orienting the horizontal edges $( i , j ) \longrightarrow ( i , j ^ { \prime } )$ if $L ( i , j ) < L ( i , j ^ { \prime } )$ and the vertical edges $( i , j ) \longrightarrow ( i ^ { \prime } , j )$ if $L ( i , j ) > L ( i ^ { \prime } , j )$ .Thus, horizontally we orient from the smaller to the larger element, and vertically the other way around. (In the margin we have an example for $n \simeq 3 .$ )

Notice that we obtain $d ^ { + } ( i , j ) = n - 1$ for all $( i , j )$ . In fact, if $L ( i , j ) = k$ , then $n - k$ cells in row $i$ contain an entry larger than $k$ , and $k - 1$ cells in column $j$ have an entry smaller than $k$ .

By Lemma 1 it remains to show that every induced subgraph of ${ \vec { S } } _ { n }$ possesses a kernel. Consider a subset $A \subseteq V$ , and let $X$ be the set of rows of $L$ , and $Y$ the set of its columns. Associate to $A$ the bipartite graph $G = ( X \cup Y , A )$ , where every $( i , j ) \in A$ is represented by the edge $i j$ with $i \in X , j \in Y$ .In the example in the margin the cells of $A$ are shaded.

The orientation on $S _ { n }$ naturally induces a ranking on the neighborhoods in $G = ( X \cup Y , A )$ by setting $j ^ { \prime } > j$ in $N ( i )$ if $( i , j ) \longrightarrow ( i , j ^ { \prime } )$ in $\vec { S } _ { n }$ respectively $i ^ { \prime } > i$ in $N ( j )$ if $( i , j ) \longrightarrow ( i ^ { \prime } , j )$ . By Lemma 2, $G = ( X \cup Y , A )$ possesses a stable matching $M$ .This $M$ , viewed as a subset of $A$ , is our desired kernel! To see why, note first that $M$ is independent in $A$ since as edges in $G = ( X \cup Y , A )$ they do not share an endvertex $i$ or $j$ Secondly, if $( i , j ) \in A \backslash M$ , then by the definition of a stable matching there either exists $( i , j ^ { \prime } ) \in M$ with $j ^ { \prime } > j$ or $( i ^ { \prime } , j ) \in M$ with $i ^ { \prime } > i$ , which for $\vec { S } _ { n }$ means $( i , j ) \longrightarrow ( i , j ^ { \prime } ) \in { \cal M }$ or $( i , j ) \longrightarrow ( i ^ { \prime } , j ) \in { \cal M }$ , and the proof is complete.

To end the story let us go a little beyond. The reader may have noticed that the graph $S _ { n }$ arises from a bipartite graph by a simple construction. Take the complete bipartite graph, denoted by $K _ { n , n }$ ,with $| X | = | Y | = n$ , and all edges between $X$ and $Y$ . If we consider the edges of $K _ { n , n }$ as vertices

![](images/a82a2c571806648cf6002d309b81e398351d5c042cdba83af1230b81ff84509c.jpg)

![](images/7b9fd88384806bdf75a8e48a213b6e42dc3a4a461dc453ab952426d1a65df78a.jpg)

![](images/fe16a2316d3132ae2f956dd66b841411e4d327aee9dc17666bb2ab96f4d2304f.jpg)

![](images/339570e82e94b104ca7c9b8263da8b5fa6befc4cbb3df475897e7b2ea5b5b557.jpg)

Construction of a line graph

of a ne graph, jog to suc veri  ndnly  s e in $K _ { n , n }$ they have a common endvertex, then we clearly obtain the square graph $S _ { \mathfrak { z } }$ . Let us say that $S _ { \mathfrak { z } }$ is the line graph of $K _ { n , n }$ . Now this same construction can be performed on any graph $G$ with the resulting graph called the line graph $L ( G )$ of $G$ .

In general, call $H$ a line graph if $H = I ( G )$ for some graph $G$ Of course, not every graph is a line graph, an example being the graph $K _ { 2 , 4 }$ that we considered earlier, and for this graph we have seen $\chi ( K _ { 2 , 4 } ) < \chi _ { \ell } ( K _ { 2 , 4 } )$ . But what if $H$ is a line graph? By adapting the proof of our theorem it can easily be shown that $\chi ( H ) = \chi _ { \ell } ( H )$ holds whenever $H$ is the line graph of a bipartite graph, and the method may well go some way in verifying the supreme conjecture in this field:

Does $\chi ( H ) = \chi _ { \ell } ( H )$ hold for every line graph H?

Very little is known about this conjecture, and things look hard — but after all, so did the Dinitz problem twenty years ago.

# References

[1] P. ERDÖS, A. L. RUBIN & H. TAYLOR: Choosability in graphs, Proc. West Coast Confercnce on Combinatorics, Graph Thcory and Computing, Congressus Numerantium 26 (1979), 125-157.   
[2] D. GALE & L. S. SHAPLEY: College admissions and the stability of marriage, Amer. Math. Monthly 69 (1962), 9-15.   
[3] F. GALvIN: The list chromatic index of a bipartite multigraph, J. Combinatorial Theory, Ser. B 63 (1995), 153-158.   
[4] J. C. M. JaNssEN: The Dinitz problem solved for rectangles, Bulletin Amer. Math. Soc. 29 (1993), 243-249.   
[5] V. G. VizING: Coloring the vertices of a graph in prescrihed colours (in Russian), Metody Diskret. Analiz. 101 (1976), 3-10.

Consider the infinite product $( 1 + x ) ( 1 + x ^ { 2 } ) ( 1 + x ^ { 3 } ) ( 1 + x ^ { 4 } ) \cdot \cdot \cdot$ and expand it in theusual way into ass $\textstyle \sum _ { n \geq 0 } a _ { n } x ^ { n }$ by grouping together those products that yield the same power $x ^ { n }$ By inspection we find for the first terms

$$
\prod _ { k \geq 1 } ( 1 + x ^ { k } ) = 1 + x + x ^ { 2 } + 2 x ^ { 3 } + 2 x ^ { 4 } + 3 x ^ { 5 } + 4 x ^ { 6 } + 5 x ^ { 7 } + \cdot \cdot \cdot \cdot
$$

So we have e. g. $a _ { 6 } = 4$ , $a _ { 7 } = 5$ , a w uly $a _ { n }$ goes to infinity with $n \longrightarrow \infty$ .

Looking at the equally simple product $( 1 - x ) ( 1 - x ^ { 2 } ) ( 1 - x ^ { 3 } ) ( 1 - x ^ { 4 } ) \cdot \cdot \cdot$ something unexpected happens. Expanding this product we obtain

$$
\prod _ { k \geq 1 } ( 1 - x ^ { k } ) = 1 - x - x ^ { 2 } + x ^ { 5 } + x ^ { 7 } - x ^ { 1 2 } - x ^ { 1 5 } + x ^ { 2 2 } + x ^ { 2 6 } - \cdot \cdot \cdot \cdot
$$

It seems that all coefficients are equal to 1, $- 1$ or O. But is this true? And if so, what is the pattern?

Infinite sums and products and their convergence have played a central role in analysis since the invention of the calculus, and contributions to the subject have been made by some of the greatest names in the field, from Leonhard Euler to Srinivasa Ramanujan.

In explaining identities such as (1) and (2), however, we disregard convergence questions — we simply manipulate the coefficients. In the language of the trade we deal with "formal" power series and products. In this framework we are going to show how combinatorial arguments lead to elegant proofs of seemingly difficult identities.

Our basic notion is that of a partition of a natural number. We call any sum

$$
\lambda : ~ n = \lambda _ { 1 } + \lambda _ { 2 } + . . . + \lambda _ { t } ~ \mathrm { w i t h } ~ \lambda _ { 1 } \geq \lambda _ { 2 } \geq . . . \geq \lambda _ { t } \geq 1
$$

a partition of $n$ . $P ( n )$ shall be the set of all partitions of $n$ , with $p ( n ) : =$ $| P ( n ) |$ , where we set $p ( 0 ) = 1$ .

What have partitions got to do with our problem? Well, consider the following product of infinitely many series:

$$
( 1 + x + x ^ { 2 } + x ^ { 3 } + \dots ) ( 1 + x ^ { 2 } + x ^ { 4 } + x ^ { 6 } + \dots ) ( 1 + x ^ { 3 } + x ^ { 6 } + x ^ { 9 } + \dots ) \cdot \cdot \cdot
$$

where the $k$ -th factor is $( 1 + x ^ { k } + x ^ { 2 k } + x ^ { 3 k } + . ~ . ~ . ~ )$ . What is the coefficient of $x ^ { n }$ w w    i $\textstyle \sum _ { n \geq 0 } a _ { n } x ^ { n } ?$ A moment's

$$
\begin{array} { l } { 5 = 5 } \\ { 5 = 4 + 1 } \\ { 5 = 3 + 2 } \\ { 5 = 3 + 1 + 1 } \\ { 5 = 2 + 2 + 1 } \\ { 5 = 2 + 1 + 1 + 1 } \\ { 5 = 1 + 1 + 1 + 1 + 1 . } \end{array}
$$

The partitions counted by $p ( 5 ) = 7$

$$
\begin{array} { l } { 6 = 5 + 1 } \\ { 6 = 3 + 3 } \\ { 6 = 3 + 1 + 1 + 1 } \\ { 6 = 1 + 1 + 1 + 1 + 1 + 1 } \end{array}
$$

Partitions of 6 into odd parts: $p _ { \mathscr { p } } ( \bar { \mathscr { \mathbf { \sigma } } } ) = 4$

$$
\begin{array} { l } { 7 = 7 } \\ { 7 = 5 + 1 + 1 } \\ { 7 = 3 + 3 + 1 } \\ { 7 = 3 + 1 + 1 + 1 + 1 } \\ { 7 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 } \\ { 7 = 7 } \\ { 7 = 6 + 1 } \\ { 7 = 5 + 2 } \\ { 7 = 4 + 3 } \\ { 7 = 4 + 2 + 1 . } \end{array}
$$

The partitions of 7 into odd resp. distinct parts: $p _ { o } ( 7 ) = p _ { d } ( 7 ) = 5$ .

thought should convince you that this is just the number of ways to write $n$ as a sum

$$
\begin{array} { l c l } { { n } } & { { = } } & { { n _ { 1 } \cdot 1 + n _ { 2 } \cdot 2 + n _ { 3 } \cdot 3 + \ldots } } \\ { { } } & { { = } } & { { \underbrace { 1 + \ldots + 1 } _ { n _ { 1 } } + \underbrace { 2 + \ldots + 2 } _ { n _ { 2 } } + \underbrace { 3 + \ldots + 3 } _ { n _ { 3 } } + \ldots . } } \end{array}
$$

So the coefficient is nothing else but the number $\gamma ) ( n )$ of partitions of $n$ Since the geometric series $1 + x ^ { \star } + x ^ { 2 k } + ,$ .. equals $\frac { 1 } { 1 - x ^ { k } }$ , we have proved our first identity:

$$
\prod _ { k \geq 1 } { \frac { 1 } { 1 - x ^ { k } } } = \sum _ { n \geq 0 } p ( n ) x ^ { n } .
$$

What's more, we see from our analysis that the factor 1−xk accounts for the contribution of $k$ to a partition of $n$ .Thus, if we leave out $\scriptstyle { \frac { 1 } { 1 - x ^ { k } } }$ from the product on the left side of (4), then $k$ does not appear in any partition on the right side. As an example we immediately obtain

$$
\prod _ { i \geq 1 } { \frac { 1 } { 1 - x ^ { 2 i - 1 } } } = \sum _ { n \geq 0 } p _ { o } ( n ) x ^ { n } ,
$$

where $p _ { 0 } ( \mathfrak { n } )$ is the number of partitions of $\gamma _ { \ell }$ all of whose summands are odd, and the analogous statement holds when all summands are even.

By now it should be clear what the $n$ -th coefficient in the infinite product $\textstyle \prod _ { \ k \geq 1 } ( 1 + \underline { { x } } ^ { \ k } )$ will be. Since we take from any factor in (3) either 1 or $x ^ { k }$ , this means that we consider only those partitions where any summand $k$ appears at most once. In other words, our original product (1) is expanded into

$$
\prod _ { k \geq 1 } ( 1 + x ^ { k } ) \ = \ \sum _ { n \geq 0 } \mathcal { p } _ { d } ( n ) x ^ { n } ,
$$

where $p _ { d } ( n )$ is the number of partitions of $\gamma _ { \ell }$ into distinct summands.

Now the method of formal series displays its full power. Since $1 - x ^ { 2 } =$ $( 1 - x ) ( 1 + x )$ we may write

$$
\prod _ { k \geq 1 } ( 1 + x ^ { k } ) = \prod _ { k \geq 1 } { \frac { 1 - x ^ { 2 k } } { 1 - x ^ { k } } } = \prod _ { k \geq 1 } { \frac { 1 } { 1 - x ^ { 2 k - 1 } } }
$$

since all factors $1 - \mathfrak { X } ^ { 2 i }$ with even exponent cancel out. So, the infinite products in (5) and (6) are the same, and hence also the series, and we obtain the beautiful result

$$
p _ { \circ } ( n ) \ = \ p _ { d } ( n ) \qquad { \mathrm { f o r ~ a l l ~ } } n \geq 0 .
$$

Such a striking equality demands a simple proof by bijection — at least that is the point of view of any combinatorialist.

Problem. Let $P _ { o } ( r _ { i } )$ and $P _ { d } ( \pi )$ be the partitions of $\hbar$ into odd and into distinct summands, respectively: Find $a$ bijection from $P _ { o } ( r )$ onto $P _ { d } ( \pi ) !$

Several bijections are known, but the following one due to J. W. L. Glaisher (1907) is perhaps the ncatest. Let $\lambda$ bc a partition of $\gamma _ { \ell }$ into odd parts. We collect cqual summands and have

$$
\begin{array} { l c l } { n } & { = } & { \underbrace { \lambda _ { 1 } + \ldots + \lambda _ { 1 } } _ { n _ { 1 } } + \underbrace { \lambda _ { 2 } + \ldots + \lambda _ { 2 } } _ { n _ { 2 } } + \ldots + \underbrace { \lambda _ { \ell } + \ldots + \lambda _ { \ell } } _ { n _ { t } } } \\ & { = } & { n _ { 1 } \cdot \lambda _ { 1 } + n _ { 2 } \cdot \lambda _ { 2 } + \ldots + n _ { \ell } \cdot \lambda _ { \ell } . } \end{array}
$$

Now we write $n _ { 1 } = 2 ^ { m _ { 1 } } + 2 ^ { m _ { 2 } } + \ldots + 2 ^ { m _ { 1 } }$ in its binary representation and similarly for the other $\gamma _ { i }$ . The new partition $\lambda ^ { \prime }$ of $n$ is then

$$
\lambda ^ { \prime } : \ n = 2 ^ { m _ { 1 } } \lambda _ { 1 } + 2 ^ { m _ { 2 } } \lambda _ { 1 } + \ldots + 2 ^ { m _ { r } } \lambda _ { 1 } + 2 ^ { k _ { 1 } } \lambda _ { 2 } + \ldots .
$$

We have to check that $\lambda ^ { \prime }$ is in $P _ { d } ( \uparrow \downarrow )$ , and that ${ \dot { \phi } } : \lambda \longmapsto \lambda ^ { \prime }$ is indeed a bijection. Both claims are easy to verify: If $2 ^ { a } \lambda _ { i } = 2 ^ { i } \lambda _ { j }$ then $2 ^ { a } = 2 ^ { b }$ since $\lambda _ { i }$ and $\lambda _ { j }$ are odd, and so $\lambda _ { i } = \lambda _ { j }$ . Hence $\lambda ^ { \prime }$ is in $P _ { i l } ( n )$ .Conversely, when $n = \mu _ { 1 } + \mu _ { 2 } + . . . + \mu . .$ is a partition into distinct summands, then wc revcrse the bijection by collecting all $\mu _ { i }$ with the same highest power of 2, and write down the odd parts with the proper multiplicity. The margin displays an example.

Manipulating formal products has thus led to the equality ${ \mathfrak { p } } _ { \circ } ( n ) = { \mathfrak { p } } _ { d } ( n )$ for partitions which we then verified via a bijection. Now we turn this around, givc a bijection proof for partitions and deduce an identity. This time our goal is to identify the pattern in the expansion (2).

Look at

$$
1 - x \ - x ^ { 2 } + x ^ { 5 } + x ^ { 7 } - x ^ { 1 2 } - x ^ { 1 5 } + x ^ { 2 2 } + x ^ { 2 6 } - x ^ { 3 5 } - x ^ { 4 0 } + \dots .
$$

The exponents (apart from O) seem to come in pairs, and taking the exponents of the first power in each pair gives the sequence

well-known to Euler. These arc the pentagonal numbers $f ( j )$ , whose name is suggested by the figure in the margin.

We easily compute $f ( j ) = \frac { 3 j ^ { 2 } - j } { 2 }$ and ${ \bar { f } } ( j ) = { \frac { 3 j ^ { 2 } + j } { 2 } }$ for the other number of each pair. In summary, we conjecture, as Euler has done, that the following formula should hold.

# Theorem.

Pentagonal numbers

For example,

$$
\lambda : 2 5 = 5 + 5 + 5 + 3 \div 3 + 1 + 1 + 1
$$

is mapped by $\phi ^ { \downarrow }$ to

$$
\begin{array} { c } { { \lambda ^ { \prime } : 2 5 = ( 2 + 1 ) ^ { 5 } + ( 2 ) ^ { 3 } + ( { \bf 4 } ) 1 } } \\ { { = 1 0 + 5 + 6 + 1 } } \\ { { = 1 0 + 6 ^ { 3 } + 5 + 1 . } } \end{array}
$$

We write

$$
\begin{array} { c } { { \lambda ^ { \prime } : 3 0 = 1 2 + 6 + 5 + 4 + 3 } } \\ { { \mathrm { a s } \quad 3 0 = 4 ( 3 + 1 ) + 2 ( 3 ) + 1 ( 5 + 3 ) } } \\ { { = ( 1 ) 5 + ( 4 + 2 + 1 ) 3 + ( 4 ) 1 } } \end{array}
$$

and obtain as $( \phi ^ { - 1 } ( \lambda ^ { r } )$ the partition   
$\lambda : 3 0 = 5 + 3 + 3 + 3 + 3 + 3 + 3 +$ $ + 1 + 1 + 1 + 1$   
into odd summands.

![](images/70e9f36dbb0a0d1c43482a1946aa0a306140dcf747dee3299f874b4624e8b1b6.jpg)

$$
\prod _ { k \geq 1 } ( 1 - x ^ { k } ) = 1 + \sum _ { j \geq 1 } ( - 1 ) ^ { j } { \Big ( } x ^ { \frac { 3 j ^ { 2 } - j } { 2 } } + x ^ { \frac { 3 j ^ { 2 } + j } { 2 } } { \Big ) } .
$$

Euler proved this remarkable theorem by calculations with formal series, but we give a bijection proof from The Book. First of all, we notice by (4) that the product $\scriptstyle \prod _ { k \geq 1 } ( 1 - x ^ { k } )$ is precisely the inverse of our partition series $\sum _ { \tau , \geq 0 } \gamma \{ \gamma _ { \ell } \} _ { : \mathcal { X } } ^ { \tau _ { \ell } }$ Hence setting $\begin{array} { r } { \prod _ { k \geq 1 } ( 1 - x ^ { k } ) = : \sum _ { n \geq 0 } c ( n ) x ^ { n } } \end{array}$ , we find

$$
\big ( \sum _ { n \geq 0 } c ( n ) x ^ { n } \big ) \ \cdot \ \big ( \sum _ { n \geq 0 } p ( n ) x ^ { n } \big ) \ = \ 1 .
$$

Comparing coefficients this means that $c ( \gamma )$ is the unique sequence with $r ( 0 ) = 1$ and

$$
\sum _ { k = 0 } ^ { n } c ( k ) p ( n - k ) = 0 \qquad { \mathrm { f o r ~ a l l ~ } } n \geq 1 .
$$

Writing the right-hand of (8) as $\sum _ { \mathbf { \lambda } = - \infty } ^ { \infty } ( - 1 ) ^ { j } x ^ { \frac { 3 - j ^ { 2 } + j } { 2 } }$ , we have to show that

$$
\begin{array} { r l r } { c ( k ) } & { = } & { \left\{ \begin{array} { l l } { 1 } & { \mathrm { f o r } k = \frac { 3 j ^ { 2 } + j } { 2 } , \mathrm { w h e n } j \in \mathbb { Z } \mathrm { i s } \mathrm { e v e n } , } \\ { - 1 } & { \mathrm { f o r } k = \frac { 3 j ^ { 2 } + j } { 2 } , \mathrm { w h e n } j \in \mathbb { Z } \mathrm { i s } \mathrm { o d d } , } \\ { 0 } & { \mathrm { o t h e r w i s e } } \end{array} \right. } \end{array}
$$

$b ( j ) = { \frac { 3 j ^ { 2 } + j } { 2 } }$ for $j \in \mathbb Z$ and substituting these values into (9), our conjecture takes on the simple form

$$
\sum _ { j \ { \mathfrak { c v e n } } } p ( n - \mathfrak { b } ( j ) ) \ = \ \sum _ { j \ { \mathfrak { c o d d } } } p ( n - \mathfrak { b } ( j ) ) \qquad \mathrm { f o r ~ a l l } \ n ,
$$

where of course we only consider $j$ with $b ( j ) \leq \pi$ So the stage is set: We have to find a bijection

$$
\phi : \bigcup _ { j \mathrm { ~ e v e n } } P ( n - b ( j ) ) \longrightarrow \bigcup _ { j \mathrm { ~ o d d } } P ( n - b ( j ) ) ,
$$

As an cxample consider $n = 1 5 , j = 2$ . $\mathfrak { s o } \left\{ \mathfrak { h } \right\} \mathrm { = 7 }$ The partition $3 + 2 + 2 + 1$ in $P ( 1 5 - t ) ( 2 ) ) = t ^ { x } ( 8 )$ is mapped to $\Theta + 2 + 1 + 1$ , which is in $P ( 1 5 - b ( 1 ) ) =$ $P ( \mathrm { { 1 3 } } )$ .

Again several bijections have been suggested, but the following construction by David Bressoud and Doron Zeilberger is astonishingly simple. We just give the definition of $( \phi )$ (which is, in fact, an involution), and invite the reader to verify the easy details.

For $\lambda : \lambda _ { 1 } + . . . + \lambda _ { i } \in P ( \eta - b ( j ) )$ set

$$
\begin{array} { r l } { \phi ( \lambda ) } & { : = \left\{ \begin{array} { l l } { ( t + 3 j \mathrm { ~ - ~ } 1 ) + ( \lambda _ { 1 } - 1 ) \mathrm { ~ i ~ . ~ . ~ . ~ } \mathrm { ~ i ~ } ( \lambda _ { t } - 1 ) } & { \mathrm { i f ~ } t + 3 j \ge \lambda _ { 1 } , } \\ { \qquad \quad ( \lambda _ { 2 } + 1 ) + . . . + ( \lambda _ { t } \mathrm { ~ t ~ } 1 ) + \underbrace { 1 + . . . + 1 } _ { \lambda _ { 1 } - t - 3 j - 1 } } & { \mathrm { i f ~ } t + 3 j < \lambda _ { 1 } , } \end{array} \right. } \end{array}
$$

where we leave out possible $0 \cdot s$ One finds that in the first case $\phi ( \lambda )$ is in $P ( \mathfrak { r } - \mathfrak { b } ( j - 1 ) )$ , and in the second case in $P ( \gamma _ { i } - \mathfrak { h } ( j + \mathbf { 1 } ) )$ .

This was beautiful, and we can get even more out of it. We already know that

$$
\prod _ { k \geq 1 } ( 1 + x ^ { k } ) \ = \ \sum _ { n \geq 0 } p _ { d } ( n ) x ^ { n } .
$$

As experienced formal series manipulators we notice that the introduction of the new variable $y$ yields

$$
\prod _ { k \geq 1 } ( 1 + y x ^ { k } ) \ = \ \sum _ { n \geq 0 } p _ { d , m } ( n ) x ^ { n } y ^ { m } ,
$$

where $p _ { d , m } ( n )$ counts the partitions of $n$ into precisely $m$ distinct summands. With $y = - 1$ this yields

$$
\prod _ { k \ge 1 } ( 1 - x ^ { k } ) \ = \ \sum _ { n \ge 0 } ( E _ { d } ( n ) - { \cal O } _ { d } ( n ) ) x ^ { n } ,
$$

where $E _ { d } ( n )$ is the number of partitions of $_ n$ into an even number of distinct parts, and $O _ { d } ( n )$ is the number of partitions into an odd number. And here is the punchline. Comparing (10) to Euler's expansion in (8) we infer the beautiful result

$$
\begin{array} { r l r } { E _ { d } ( n ) - O _ { d } ( n ) } & { = } & { \left\{ \begin{array} { l l } { ~ 1 } & { \mathrm { f o r } n = \frac { 3 \eta ^ { 2 } \pm \chi } { 2 } \mathrm { w h e n } j \ge 0 \mathrm { i s ~ e v e n } , } \\ { - 1 } & { \mathrm { f o r } n = \frac { 3 \eta ^ { 2 } \pm \chi } { 2 } \mathrm { w h e n } j \ge 1 \mathrm { i s ~ o d d } , } \\ { ~ 0 } & { \mathrm { o t h e r w i s e } . } \end{array} \right. } \end{array}
$$

This is, of course, just the beginning of a longer and still ongoing story. The theory of infinite products is replete with unexpected indentities, and with their bijective counterparts. The most famous examples are the so-called Rogers-Ramanujan identities, named after Leonard Rogers and Srinivasa Ramanujan, in which the number 5 plays a mysterious role:

$$
\begin{array} { r c l } { { \displaystyle \prod _ { k \geq 1 } \frac { 1 } { ( 1 - x ^ { 5 k - 4 } ) ( 1 - x ^ { 5 k - 1 } ) } } } & { { = } } & { { \displaystyle \sum _ { n \geq 0 } \frac { x ^ { n ^ { 2 } } } { ( 1 - x ) ( 1 - x ^ { 2 } ) \cdot \cdot \cdot ( 1 - x ^ { n } ) } , } } \\ { { \displaystyle \prod _ { k \geq 1 } \frac { 1 } { ( 1 - x ^ { 5 k - 3 } ) ( 1 - x ^ { 5 k - 2 } ) } } } & { { - } } & { { \displaystyle \sum _ { n \geq 0 } \frac { x ^ { n ^ { 2 } + n } } { ( 1 - x ) ( 1 - x ^ { 2 } ) \cdot \cdot \cdot ( 1 - x ^ { n } ) } . } } \end{array}
$$

The reader is invited to translate them into the following partition identities first noted by Percy MacMahon:

Let $f ( n )$ be the number of partitions of $n$ all of whose summands are of the form $5 k + 1$ or $5 k + 4 .$ and $g ( n )$ the number of partitions whose summands differ by at least 2. Then $f ( n ) = g ( n )$ . Let $r ( n )$ be the number of partitions of $n$ all of whose summands are of the form $5 k + 2$ or $5 k + 3$ , and $s ( n )$ the number of partitions whose parts differ by at least 2 and which do not contain 1. Then $r ( n ) = s ( n )$ .

All known formal series proofs of the Rogers-Ramanujan identities are quite involved, and for a long time bijection proofs of $f ( n ) = g ( n )$ and of $r ( n ) = s ( n )$ seemed elusive. Such proofs were eventually given 1981 by Adriano Garsia and Stephen Milne. Their bijections are, however, very complicated — Book proofs are not yet in sight.

An example for $n = 1 0$ : $\begin{array} { l } { 1 0 = 9 + 1 } \\ { 1 0 = 8 + 2 } \\ { 1 0 = 7 + 3 } \\ { 1 0 = 6 + 4 } \\ { 1 0 = 4 + 3 + 2 + 1 } \end{array}$ and $\begin{array} { l } { 1 0 = 1 0 } \\ { 1 0 = 7 + 2 + 1 } \\ { 1 0 = 6 + 3 + 1 } \\ { 1 0 = 5 + 4 + 1 } \\ { 1 0 = 5 + 3 + 2 . } \end{array}$ so $E _ { d } ( 1 0 ) = O _ { d } ( 1 0 ) = 5 .$

![](images/4adde2be68a49489fd536245db80d7aedd2ab5e2fc70f9a5b5f1e17e3154acb6.jpg)

Srinivasa Ramanujan

# References

[1] G. E. ANDREws: The Theory of Partitions, Encyclopedia of Mathematics and its Applications, Vol. 2, Addison-Wesley, Reading MA 1976.   
[2] D. BREssOUD & D. ZEILBERGER: Bijecting Euler's partitions-recurrence, Amer. Math. Monthly 92 (1985), 54-55.   
[3] A. GARSIA & S. MILNE: A Rogers-Ramanujan bijection, J. Combinatorial Theory. Scr. A 31 (1981), 289-339.   
[4] S. RAMANUJAN: Proof of certain identities in combinatory analysis, Proc. Cambridge Phil. Soc. 19 (1919), 214-216.   
[5] L. J. RoGERs: Second memoir on the expansion of certain infinite products, Proc. Iondon Math. Soc. 25 (1894), 318-343.

# Five-coloring plane graphs

Plane graphs and their colorings have been the subject of intensive research since the beginnings of graph theory because of their connection to the fourcolor problem. As stated originally the four-color problem asked whether it is always possible to color the regions of a plane map with four colors such that regions which share a common boundary (and not just a point) receive different colors. The figure on the right shows that coloring the regions of a map is really the same task as coloring the vertices of a plane graph. As in Chapter 1 1 (page 65) place a vertex in the interior of each region (including the outer region) and connect two such vertices belonging to neighboring regions by an edge through the common boundary.

The resulting graph $G$ , the dual graph of the map $M$ , is then a plane graph, and coloring the vertices of $G$ in the usual sense is the same as coloring the regions of $M$ . So we may as well concentrate on vertex-coloring plane graphs and will do so from now on. Note that we may assume that $G$ has no loops or multiple edges, since these are irrelcvant for coloring.

![](images/29ca244c58a323f2575f3376b08131e4ccd5e706354c2ed7e19f26ef85de540d.jpg)

The dual graph of a map

In the long and arduous history of attacks to prove the four-color theorem many attempts came close, but what finally succeeded in the Appel-Haken proof of 1976 and also in the recent proof of Robertson, Sanders, Seymour and Thomas 1997 was a combination of very old ideas (dating back to the 19th century) and the very new calculating powers of modern-day computers. Twenty-five years after the original proof, the situation is still basically the same, no proof from The Book is in sight.

So let us be more modest and ask whether there is a neat proof that every plane graph can be 5-colored. A proof of this five-color theorem had already becn given by Hcawood at the turn of the century. The basic tool for his proof (and indeed also for the four-color theorem) was Euler's formula (see Chapter 1 1). Clearly, when coloring a graph $G$ we may assumc that $G$ is connected since we may color the connected pieces separatcly. A plane graph divides the plane into a set $R$ of regions (including the exterior region). Euler's formula states that for plane connected graphs $G \ : \simeq \ : ( V , E )$ we always have

$$
| V | - | E | + | R | \ = ~ 2 .
$$

As a warm-up, let us see how Euler's formula may be applied to prove that cvery plane graph $G$ is 6-colorable. We proceed by induction on the number $n$ of vertices. For small values of $n$ (in particular, for $n \leq 6 )$ this is obvious.

13 edges and 7 regions.

From part (A) of the proposition on page 67 we know that $G$ has a vertex $v$ of degree at most 5. Delete $\begin{array}{c} \left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. \left. \begin{array}  { r l } \end{array} \end{array} \right.$ and all edges incident with $v$ The resulting graph $\vec { G } ^ { \prime } = G \backslash v$ is a plane graph on $n - 1$ vertices. By induction, it can be 6-colored. Since $v$ has at most 5 neighbors in $G$ , at most 5 colors are used for these neighbors in the coloring of $G ^ { \prime }$ . So we can extend any 6-coloring of $G ^ { t }$ to a 6-coloring of $G$ by assigning a color to $v$ which is not used for any of its neighbors in the coloring of $G ^ { \dagger }$ Thus $G$ is indeed 6-colorable.

Now let us look at the list chromatic number of plane graphs, as discussed in the previous chapter on the Dinitz problem. Clearly, our 6-coloring method works for lists of colors as well (again we never run out of colors), so $\chi _ { \ell } \{ G \} \le 6$ holds for any plane graph $G$ Erdös, Rubin and Taylor conjectured in 1979 that every plane graph has list chromatic number at most 5, and further that there are plane graphs $G$ with $\chi _ { \scriptscriptstyle \hat { \ell } } \left( G \right) > 4$ They were right on both counts. Margit Voigt was the first to construct an example of a plane graph $G$ with $\chi _ { \ell } \{ G \} = 5$ (her example had 238 vertices) and around the same time Carsten Thomassen gave a truly stunning proof of the 5-list coloring conjecture. His proof is a telling example of what you can do when you find the right induction hypothesis. It does not use Euler's formula at all!

Theorem. All planar graphs $G$ can be 5-list colored:

$$
\chi _ { \hat { \ell } } \{ G \} \leq 5 .
$$

Proof. First note that adding edges can only increase the chromatic number. In other words, when $H$ is a subgraph of $G$ ,then $\chi _ { \ell } \left( { \cal { I } } { \bar { q } } \right) \leq \chi _ { \ell ^ { \prime } } ( G )$ certainly holds. Hence we may assume that $G$ is connected and that all the bounded faccs of an embedding have triangles as boundaries. Let us call such a graph near-triangulated. The validity of the theorem for neartriangulated graphs will establish the statement for all plane graphs.

![](images/d4d5333c02ec66e062c86946ca399d8c7ae6e30ecf32d6a3ca424adf39b1e1aa.jpg)

The trick of the proof is to show the following stronger statement (which allows us to use induction):

A ncar-triangulated plane graph

Let $G = ( V , E )$ be a near-triangulated graph, and let B be the cycle bounding the outer region. We make the following assumptions on the color sets $C ( v )$ . $v \in V$

1)Two adjacent vertices $x , y$ of $B$ are already colored with (different) colors $\alpha$ and $\beta$ .   
(2) $| C ( \mathfrak { r } ) | > 3$ for all other vertices v of $B$ .   
(3) $| C ( ? ) \} | \geq 5$ for all vertices v in the interior.

Then the coloring of $\mathcal { X }$ , y can be extended to a proper coloring of $G$ by choosing colors from the lists. In particular, $x _ { i } ( G ) \leq 5$ .

For $| V | = 3$ this is obvious, since for the only uncolored vertex $\mathcal { V }$ we have $| C ( v ) | \ge 3$ , so there is a color available. Now we procced by induction.

Case 1: Suppose $B$ has a chord, that is, an edge not in $B$ that joins two vertices $u , v \in B$ The subgraph $G _ { 1 }$ which is bounded by ${ \cal B } _ { \mathrm { l } } \cup \{ u v \}$ and contains $x , y , u$ and $v$ is near-triangulated and therefore has a 5-list coloring by induction. Suppose in this coloring the vertices $_ u$ and $v$ receive the colors $\gamma$ and $\delta$ Now we look at the bottom part $G _ { 2 }$ bounded by $B _ { 2 }$ and uv. Regarding $u , v$ as pre-colored, we see that the induction hypotheses are also satisfied for $G _ { 2 }$ . Hence $G _ { 2 }$ can be 5-list colored with the available colors, and thus the same is true for $G$ .

Case 2: Suppose $B$ has no chord. Let $v _ { 0 }$ be the vertex on the other side of the $\alpha$ -colored vertex $x$ on $B$ , and lect $x , v _ { 1 } , \dotsc , v _ { t } , w$ be the ncighbors of $v _ { 0 }$ . Since $G$ is near-triangulated we have the situation shown in the figure.

Construct the near-triangulated graph $G ^ { \prime } = G \backslash \boldsymbol { v } _ { 0 }$ by deleting from $G$ the vertex $v _ { 0 }$ and all edges emanating from $v _ { 0 }$ .This $G ^ { \prime }$ has as outer boundary $B ^ { \prime } = ( B \backslash v _ { 0 } ) \cup \left\{ v _ { 1 } , . . . , v _ { t } \right\}$ .Since $| C ( v _ { 0 } ) | \ge 3$ by assumption (2) there exist two colors $\gamma , \delta$ in $C \{ v _ { 0 } \}$ different from $\alpha$ .Now we replace every color set $C ( v _ { i } )$ by $C ( v _ { i } ) \backslash \{ \gamma , \delta \}$ , keeping the original color sets for all other vertices in $G ^ { \prime }$ .Then $G ^ { \prime }$ clearly satisfies all assumptions and is thus 5-list colorable by induction. Choosing $\gamma$ or $\delta$ for $v _ { 0 }$ , different from the color of $w$ , we can extend the list coloring of $G ^ { t }$ to all of $G$ .

So, the 5-list color thcorem is proved, but the story is not quite over. A stronger conjecture claimed that the list-chromatic number of a planc graph $C$ is at most 1 more than the ordinary chromatic number:

Is $\chi _ { \ell } ( G ) \leq \chi ( G ) + 1$ for every plane graph $G$ ?

Since $\chi \langle G \rangle \leq 4$ by the four-color theorem, we have three cases:

Case II: Case I: $\begin{array} { l } { { \chi ( G ) = 2 \implies \chi _ { \ell } ( G ) \leq 3 } } \\ { { \chi ( G ) = 3 \implies \chi _ { \ell } ( G ) \leq 4 } } \\ { { \chi ( G ) = 4 \implies \chi _ { \ell } ( G ) \leq 5 . } } \end{array}$ Case II:

Thomassen's result settles Case III, and Case I was proved by an ingenious (and much more sophisticated) argument by Alon and Tarsi. Furthermore, there are plane graphs $G$ with $\chi ( G ) = 2$ and $\chi _ { \ell } \{ G \} = 3$ , for example the graph $K _ { 2 , 4 }$ that we considered in the preceding chapter on the Dinitz problem.

But what about Case II? Here the conjecture fails: this was first shown by Margit Voigt for a graph that was earlier constructed by Shai Gutner. His graph on 130 vertices can be obtained as follows. First we look at the "double octahedron" (sce the figure), which is clearly 3-colorable, Let ${ \mathfrak { \alpha } } \in \{ 5 , 6 , 7 , 8 \}$ and $\beta \in \{ 9 , 1 0 , 1 1 , 1 2 \}$ , and consider the lists that are given in the figure. You are invited to check that with these lists a coloring is not possible. Now take 16 copics of this graph, and identify all top vertices and all bottom vertices. This yields a graph on $1 6 \cdot 8 + 2 = 1 3 0$ vertices which

![](images/aa5fa37202d3ddd76e88b48723f3163861b2f209201da80acc08aede606a71ee.jpg)

![](images/648c5ba5f08e80121670f500780e78f6c2132e8eb41ba3d901bc7aad345120f5.jpg)

$\alpha$ {α, 1, 3, 4}} {α, 2, 3, 4} {α, β, 1, 2}\$ {1,2, 3,4}{α, β,1, 2} {1,2,3,4} {β,2, 3,4} {β, 1, 3, 4} β

is still plane and 3-colorable. We assign $\left. 5 , 6 , 7 , 8 \right.$ to the top vertex and $\{ 9 , 1 0 , 1 1 , 1 2 \}$ to the bottom vertex, with the inner lists corresponding to the 16 pairs $( \alpha , \beta )$ . $\alpha \in \{ 5 , 6 , 7 , 8 \}$ , $\beta \in \{ 9 , 1 0 , 1 1 , 1 2 \}$ . For every choice of $\alpha$ and $\beta$ we thus obtain a subgraph as in the figure, and so a list coloring of the big graph is not possible.

By modifying another one of Gutner's examples, Voigl and Wirth came up with an even smaller plane graph with 75 vertices and $\chi = 3 , \chi _ { \ell } = 5 .$ ,which in addition uses only the minimal number of 5 colors in the combined lists. The current record is 63 vertices.

# References

[1] N. ALON & M. TARSI: Colorings and orientations of graphs, Combinatorica 12 (1992), 125-134.   
[2] P. ErDÖs. A. L. RuBIN & H. TAyLOR: Choosability in graphs, Proc. West Coast Conference on Combinatorics, Graph Theory and Computing, Congressus Numcrantium 26 (1979). 125-157.   
[3] S. GuTNER: The complexity of planar graph choosability, Discrete Math. 159 (1996), 119-130.   
[4] N. ROBERTSON, D. P. SANDERS, P. SEYMOUR & R. THOMAS: The fourcolour theorem, J. Combinatorial Theory, Ser. B 70 (1997), 2-44.   
[5] C. TnomAssEN: Every planar graph is 5-choosable. J. Combinatorial Theory, Scr. B 62 (1994), 180-181.   
[6] M. VoIGT: List colorings of plamar graphs, Discrete Math. 120 (1993), 215-219.   
[7] M. VOIGT & B. WIRTH: On 3-colorable non-4-choosable planar graphs, J. Graph Theory 24 (1997), 233-235.

Here is an appealing problem which was raised by Victor Klee in 1973. Suppose the manager of a museum wants to make sure that at all times every point of the museum is watched by a guard. The guards are stationed at fixed posts, but they are able to turn around. How many guards are needed?

We picture the walls of the museum as a polygon consisting of $n$ sides. Of course, if the polygon is convex, then one guard is enough. In fact, the guard may be stationed at any point of the museum. But, in general, the walls of the museum may have the shape of any closed polygon.

Consider a comb-shaped museum with $n = 3 m$ walls, as depicted on the right. It is easy to see that this requires at least $\begin{array} { r } { m = { \frac { n } { 3 } } } \end{array}$ guards. In fact, there are $_ n$ walls. Now notice that the point 1 can only be observed by a guard stationed in the shaded triangle containing 1, and similarly for the other points $2 , 3 , \ldots , m$ . Since all these triangles are disjoint we conclude that at least $m$ guards are needed. But $m$ guards are also enough, since they can be placed at the top lines of the triangles. By cutting off one or two walls at the end, we conclude that for any $n$ there is an $_ n$ -walled museum which requires $\left\lfloor { \frac { n } { 3 } } \right\rfloor$ guards.

![](images/f560d32f1f00221b14037d0c63bfc96b4124b660fa420973cf68be26a99b0c3b.jpg)

![](images/8d5db8955595b305a986aacd87eeb6020bec156064d74f49faa6883ceea13db3.jpg)  
A convex exhibition hall

V √ 2 3 m

![](images/85408451f31ef6fb685384c600d28a41a1b12fb6f402f6a6243596c87d23fc91.jpg)  
A real life art gallery..

![](images/c9acc34fb4b581e679133dd2265c5a4d28879ca8eda688abd3b701fcb0929e89.jpg)

A muscum with $n = 1 2$ walls

![](images/f689a73932a6587f9c9708ffcc1d8b6ea3f45044ffb439f9e227ff4bd65ebf40.jpg)

A triangulation of the museum

![](images/51bf1e5b09f75801e09cf116baecbf48faf98c59779b92a353b0a8c2d0ad2943.jpg)

Schönhardt's polyhedron: The interior dihedral angles at the edges $A B ^ { \prime }$ , $B C ^ { \prime }$ and $C A ^ { \prime }$ are greater than $\ I \tilde { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } ( \mathbf { \bar { \mathbf { \Lambda } } } ) ^ { \zeta \mathbf { \hat { \mathbf { \mathbf { \Lambda } } } } }$ .

The following result states that this is the worst case.

Theorem. For any museum with $\pmb { n }$ walls, $\lfloor { \frac { n } { 3 } } \rfloor$ guards suffice.

This "art gallery theorem" was first proved by Vaek Chvátal by a clever argument, but here is a proof due to Steve Fisk that is truly beautiful.

Proof. First of all, let us draw $n - 3$ non-crossing diagonals between corners of the walls until the interior is triangulated. For example, we can draw 9 diagonals in the museum depicted in the margin to produce a triangulation. It does not matter which triangulation we choose, any one will do. Now think of the new figure as a plane graph with the corners as vertices and the walls and diagonals as edges.

Claim. This graph is 3-colorable.

For $ \ n = 3$ there is nothing to prove. Now for $\pi > 3$ pick any two vertices $u$ and $\mathcal { V }$ which are connected by a diagonal. This diagonal will split the graph into two smaller triangulated graphs both containing the edge uv. By induction we may color each part with 3 colors where we may choose color 1 for $u$ and color 2 for $\mathcal { V }$ in each coloring. Pasting the colorings together yields a 3-coloring of the whole graph.

The rest is easy. Since there are $\pmb { n }$ vertices, at least one of the color classes, say the vertices colored 1, contains at most $\left\lfloor { \frac { \pi } { 3 } } \right\rfloor$ vertices, and this is where we place the guards. Since every triangle contains a vertex of color I we infer that every triangle is guarded, and hence so is the whole museum.

The astute reader may have noticed a subtle point in our reasoning. Does a triangulation always exist? Probably everybody's first reaction is: Obviously, yes! Well, it does exist, but this is not completely obvious, and, in fact, the natural generalization to three dimensions (partitioning into tetrahedra) is false! This may be seen from Schönhardt's polyhedron, depicted on the left. It is obtained from a triangular prism by rotating the top triangle, so that each of the quadrilateral faces breaks into two triangles with a non-convex edge. Try to triangulate this polyhedron! You will notice that any tetrahedron that contains the bottom triangle must contain one of the three top vertices: but the resulting tetrahedron will not be contained in Schönhardt's polyhedron. So there is no triangulation without an additional vertex.

To prove that a triangulation exists in the case of a planar non-convex polygon, we proceed by induction on the number $\mathscr { n }$ of vertices. For $n = 3$ the polygon is a triangle, and there is nothing to prove. Let $\mathfrak { n } \geq \mathrm { ~ 4 ~ }$ .To use induction, all we have to produce is one diagonal which will split the polygon $P$ into two smaller parts, such that a triangulation of the polygon can be pasted together from triangulations of the parts.

Call a vertex $A$ convex if the interior angle at the vcrtex is less than $1 8 0 ^ { \circ }$ . Since the sum of the interior angles of $P$ is $( \Im \mathrm { { \ : 2 \ : - \ : 2 } } ) \Im \mathrm { { \ : 8 0 } } ^ { \circ }$ , there must be a convex vertex $A$ , In fact, there must be at least three of them: In essence this is an application of the pigeonhole principle! Or you may consider the convex hull of the polygon, and note that all its vertices are convex also for the original polygon.

Now look at the two neighboring vertices $B$ and $C$ of $A$ . If the segment $B C$ lies entirely in $P$ , then this is our diagonal. If not, the triangle $A B C$ contains other vertices. Slide $B C$ towards $A$ until it hits the last vertex $Z$ in $A B C$ Now $A Z$ is within $P$ , and we have a diagonal.

There are many variants to the art gallery theorem. For example, we may only want to guard the walls (which is, after all, where the paintings hang), or the guards are all stationed at vertices. A particularly nice (unsolved) variant goes as follows:

Suppose each guard may patrol one wall of the museum, so he walks along his wall and sees anything that can be seen from any point along this wall.

How many "wall guards" do we then need to keep control?

Godfried Toussaint constructed the example of a museum displayed here which shows that $\lfloor { \frac { n } { 4 } } \rfloor$ guards may be necessary.

This polygon has 28 sides (and, in general, 4m sides), and thc reader is invited to check that m wall-guards are needed. It is conjectured that, except for some small values of $\boldsymbol { n }$ , this number is also sufficient, but a proof, lct alone a Book Proof, is still missing.

![](images/5184ab4b9e389e0a759c858481fb52a245dca302778afeaf5e61e5a912fc058d.jpg)

# References

![](images/d40d1237fa8f4a40c0e5a0fe06cc64f615d9884596aaf08048f1c9b596deb293.jpg)

[1] V. CHVÁTAL: A combinatorial theorem in plane geometry, J. Combinatorial Theory, Ser. B 18 (1975), 39-41.   
[2] S. FisK: A short proof of Chvátal's watchman theorem, J. Combinatorial Theory, Ser. B 24 (1978), 374.   
[3] J. O'RouRKE: Art Gallery Theorems and Algorithms, Oxford University Press 1987.   
[4] E. SCHöNHARDT: Über die Zerlegung von Dreieckspolyedern in Tetraeder, Math. Annalen 98 (1928), 309-312.

![](images/68cf556395072a61e7106ca80d992482dbc3b706001b91151d01a05e58e55350.jpg)

One of the fundamental results in graph theory is the theorem of Turán from 1941, which initiated extremal graph theory. Turán's theorem was rediscovered many times with various different proofs. We will discuss five of them and let the reader decide which one belongs in The Book.

Let us fix some notation. We consider simple graphs $G$ on the vertex set $V = \{ v _ { 1 } , \ldots , v _ { n } \}$ and edge set $E$ .If $v _ { i }$ and $v _ { j }$ are neighbors, then we write $v _ { i } v _ { j } \in E$ A $p$ -clique in $G$ is a complete subgraph of $G$ on $p$ vertices, denoted by $K _ { p }$ . Paul Turán posed the following question:

Suppose $G$ is a simple graph that does not contain a $p$ -clique. What is the largest number of edges that $G$ can have?

We readily obtain examples of such graphs by dividing $V$ into $p { - } 1$ pairwise disjoint subsets $V = V _ { 1 } \cup \dotsc \cup V _ { p - 1 }$ , $| V _ { i } | = n _ { i }$ , $n = n _ { 1 } + . . . + n _ { p - 1 }$ , joining two vertices if and only if they lie in distinct sets $V _ { i } , V _ { j }$ We denote the resulting graph by $K _ { n _ { 1 } , \ldots , n _ { p - 1 } }$ ; it has $\textstyle \sum _ { i < j } n _ { i } n _ { j }$ edges. We obtain a maximal number of edges among such graphs with given $n$ if we divide the numbers $n _ { i }$ as evenly as possible, that is, if $| n _ { i } - n _ { j } | \leq 1$ for all $i , j$ . Indeed, suppose $n _ { 1 } \geq n _ { 2 } + 2$ By shifting one vertex from $V _ { 1 }$ to $V _ { 2 }$ , we obtain $K _ { n _ { 1 } - 1 , n _ { 2 } + 1 , \dots , n _ { p - 1 } }$ which contains $( n _ { 1 } \mathrm { ~ - ~ } 1 ) ( n _ { 2 } \mathrm { ~ + ~ } 1 ) \mathrm { ~ - ~ } n _ { 1 } n _ { 2 } \mathrm { ~ = ~ }$ $n _ { 1 } - n _ { 2 } - 1 \ge 1$ more edges than $K _ { n _ { 1 } , n _ { 2 } , \ldots , n _ { p - 1 } } .$ Let us call the graphs $K _ { n _ { 1 } , \ldots , n _ { p - 1 } }$ with $| n _ { i } - n _ { j } | \leq 1$ the Turán graphs. In particular, $p - 1$ divides $n$ , then we may choose $\begin{array} { r } { n _ { i } = \frac { n } { p - 1 } } \end{array}$ for all $i$ , obtaining

$$
{ \binom { p - 1 } { 2 } } { \Big ( } { \frac { n } { p - 1 } } { \Big ) } ^ { 2 } = { \Big ( } 1 - { \frac { 1 } { p - 1 } } { \Big ) } { \frac { n ^ { 2 } } { 2 } }
$$

edges. Turán's theorem now states that this number is an upper bound for the edge-number of any graph on $n$ vertices without a $p$ -clique.

Theorem. If a graph $G = ( V , E )$ on $n$ vertices has no $p$ -clique, $p \geq 2$ then

$$
| E | \leq { \Big ( } 1 - { \frac { 1 } { p - 1 } } { \Big ) } { \frac { n ^ { 2 } } { 2 } } .
$$

For $p = 2$ this is trivial. In the first interesting case $p = 3$ the theorem states that a triangle-free graph on $n$ vertices contains at most $\textstyle { \frac { n ^ { 2 } } { 4 } }$ edges. Proofs of this special case were known prior to Turán's result. Two elegant proofs using inequalities are contained in Chapter 17.

![](images/ffef44f376a5357559b69fe448870028b42e08c10d6d618ee9a81e6d5dc4c413.jpg)  
Paul Turán

![](images/495a9b949115945c46143a5c13923202ae93f8f2bebd7c3310ef0bc18cc8009a.jpg)

The graph $K _ { 2 , 2 , 3 }$

![](images/73c51c2e0dd25ed29d93d9507e9c053e0f3ba36f86eae54e30a20a3a3d3a927f.jpg)

Let us turn to the general case. The first two proofs use induction and are due to Turán and to Erds, respectively.

First proof. We use induction on $\boldsymbol { \mathscr { n } }$ One easily computes that (1) is true for $ { \mathcal { n } } <  { \mathcal { p } }$ .Let $G$ be a graph on $V = \{ v _ { 1 } , \ldots , v _ { n } \}$ without $p$ -cliques with a maximal number of edges, where $ { \mathcal { n } } \geq  { \mathcal { p } }$ . $G$ certainly contains $( p - 1 )$ . cliques, since otherwise we could add edges. Let $A$ be a $( p - 1 )$ -clique, and set $B : = V \backslash A$ .

$A$ contains $\binom { p - 1 } { 2 }$ edges, and we now estimate the edge-number $\boldsymbol { \epsilon } _ { B }$ in $B$ and the edge-number $e _ { A , B }$ between $A$ and $B$ By induction, we have $c _ { 1 3 } \leq$ $\begin{array} { r } { \frac { 1 } { \mathbf { \widehat { z } } } \big ( 1 - \frac { 1 } { \mathcal { P } ^ { - } } \big ) \big ( \pi - p + 1 \big ) ^ { 2 } } \end{array}$ Since $G$ has no $p$ -clique, every $u _ { j } \in B$ is adjacent to at most $p - 2$ vertices in $A$ , and we obtain $\begin{array} { r } { e _ { A , B } \leq ( p - 2 ) ( n - p + 1 ) } \end{array}$ . Altogether, this yields

$$
| E | \leq { \binom { p - 1 } { 2 } } + { \frac { 1 } { 2 } } { \Big ( } 1 - { \frac { 1 } { p - 1 } } { \Big ) } ( n - p + 1 ) ^ { 2 } + ( p - 2 ) ( n - p + 1 ) ,
$$

which is precisely $\begin{array} { r } { ( 1 - \frac { 1 } { r - 1 } ) \frac { n ^ { 2 } } { 2 } } \end{array}$

![](images/ae2654e30e1342c08816b47badd5a344a6f1f9b094114213a55a79e686ff5eed.jpg)

Second proof. This proof makes use of the structure of the Turán graphs. Let $v _ { m } \in V$ be a vertex of maximal degree $d _ { m } = \operatorname { m a x } _ { 1 \leq j \leq n } d _ { j }$ Denote by $S$ the set of neighbors of $v _ { m }$ , $| S | = d _ { m }$ , and set $T : = V \backslash S$ As $G$ contains no $p$ -clique, and $v _ { m }$ is adjacent to all vertices of $S$ , we note that $S$ contains no $( p - 1 )$ -clique.

We now construct the following graph $H$ on $V$ (see the figure). $I I$ corresponds to $G$ on $S$ and contains all edges between $S$ and $T$ , but no edges within $\mathcal { T }$ In other words, $T$ is an independent set in $H$ , and we conclude that $H$ has again no $p$ cliques. Let $\vec { d } _ { j } ^ { \prime }$ be the degree of $v _ { j }$ in $H$ . If ${ \mathfrak { U } } _ { j } \in S$ , then we certainly have $d _ { j } ^ { \prime } \geq d _ { j }$ by the construction of $H$ , and for ${ v } _ { j } \in \mathcal { T }$ , we see $d _ { j } ^ { \prime } = | S | = d _ { m } ^ { \prime } \geq d _ { j }$ by the choice of $v _ { \mathsf { r } \mathsf { r } \mathsf { L } }$ . We infer $| E ( H ) | \geq | E |$ , and find that among all graphs with a maximal number of edges, there must be one of the form of $H$ By induction, the graph induced by S has al most as many edges as a suitable graph Kn1,.,np 2 on $S$ So $| E | \le | E ( H ) | \le E ( K _ { n _ { 1 } , \ldots , n _ { n - 1 } } )$ with ${ \mathfrak { r } } _ { p - 1 } = | T |$ which implies (1). □

The next two proofs are of a totally different nature, using a maximizing argument and ideas from probability theory. They are due to Motzkin and Straus and to Alon and Spencer, respectively.

Third proof. Consider a probability distribution $w = ( \pi , \ldots , \pi _ { n } )$ on the vertices, that is, an assignment of values $w _ { i } \geq 0$ to the vertices with $\textstyle \sum _ { i = 1 } ^ { n } { \mathcal { W } } _ { i } = 1$

$$
f ( \boldsymbol { w } ) = \sum _ { v _ { i } v _ { j } \subset E } w _ { i } w _ { j } .
$$

Suppose $\mathbf { w }$ is any distribution, and let ${ \vec { v } } _ { i }$ and $v _ { j }$ be a pair of non-adjacent vertices with positive weights $w _ { i } , \operatorname { \ d } { i i } _ { j }$ . Let $s _ { i }$ be the sum of the weights of all vertices adjacent to $v _ { y }$ , and define $s _ { j }$ similarly for $v _ { j }$ , where we may assume that $s _ { i } \geq s _ { j }$ . Now we move the weight from $v _ { j }$ to $v _ { i }$ , that is, the new weight of $v _ { i }$ is $w _ { i } + w _ { j }$ , while the weight of $v _ { j }$ drops to O). For the new new distribution $w ^ { \prime }$ we find

$$
f ( w ^ { \prime } ) ~ { \stackrel { - } { \cdots } } ~ f ( w ) + w _ { j } s _ { i } - w _ { j } s _ { j } ~ \geq ~ f ( w ) .
$$

We repeat this (reducing the number of vertices with a positive weight by one in each step) until there are no non-adjacent vertices of positive weight anymore. Thus we conclude that there is an optimal distribution whose nonzero weights are concentrated on a clique, say on a $k$ -clique. Now if, say, $w _ { 1 } > w _ { 2 } > 0$ , then choose $\varepsilon$ with $0 < \varepsilon < w _ { 1 } - w _ { 2 }$ and change $w _ { 1 }$ to $w _ { 1 } - \varepsilon$ and $u / 2$ to $\mathfrak { t } \mathfrak { i } _ { 2 } + \varepsilon$ The new distribution $w ^ { \prime }$ satisfies $f ^ { 2 } ( w ^ { \prime } ) =$ $f ( w ) + \varepsilon ( w _ { 1 } - w _ { 2 } ) - \varepsilon ^ { 2 } > f ( w ) .$ , and we infer that the maximal value of $f ( w )$ is attained for $u _ { i } = \frac { 1 } { k }$ on a $k$ -clique and $\imath \imath _ { i } = 0$ otherwise. Since a $k$ -clique contains $\frac { k ( k - 1 ) } { 2 }$ edges, we obtain

$$
f ( w ) = \frac { k \big ( k - 1 \big ) } { 2 } \frac { 1 } { k ^ { 2 } } = \frac { 1 } { 2 } \Big ( 1 - \frac { 1 } { k } \Big ) .
$$

Since this expression is increasing in $k$ , the best we can do is to set $k = p \mathrm { - - } 1$ (since $G$ has no $p$ -cliques). So we conclude

$$
f ( w ) \leq \frac { 1 } { 2 } \Big ( 1 - \frac { 1 } { p - 1 } \Big )
$$

for any distribution $\pmb { w }$ . In particular, this inequality holds for the uniform distribution given by $\begin{array} { r } { w _ { i } = \frac { 1 } { \pi } } \end{array}$ for all $i$ Thus we find

$$
{ \frac { | E | } { n ^ { 2 } } } \ = \ f { \Big ( } w _ { i } = { \frac { 1 } { n } } { \Big ) } \ \leq \ { \frac { 1 } { 2 } } { \Big ( } 1 - { \frac { 1 } { p \ - \ 1 } } { \Big ) } ,
$$

which is precisely (1).

Fourth proof. This time we use some concepts from probability theory. Let $G$ be an arbitrary graph on the vertex set $V = \{ v _ { 1 } , \ldots , v _ { r \imath } \}$ Denote the degree of $\Im , _ { i }$ by $d _ { i }$ , and write $\omega ( G )$ for the number of vertices in a largest clique, called the clique number of $G$ .

$$
C l a i m . \ W e \ h a \nu e \ \omega ( G ) \ \geq \ \sum _ { i = 1 } ^ { n } { \frac { 1 } { n - d _ { i } } } .
$$

We choose a random permutation $\pi ~ = ~ v _ { 1 } v _ { 2 } \ldots v _ { n }$ of the vertex set $V$ , where cach permutation is supposed to appear with the same probability and then consider the following set We put v into   andnly if $\mathcal { V } _ { \mathcal { I } }$ is adjacent to all $v _ { j }$ $r _ { j } ( j < i )$ preceding $n _ { i }$ . By definition, $C _ { \pi }$ is a clique in $G$ Let $X = | C _ { \pi } |$ be the corresponding random variable. We have $\textstyle X = \sum _ { i = 1 } ^ { n } X _ { i }$ where $X _ { i }$ $v _ { i }$ that is, $X _ { i } = 1$ or $X _ { i } = 0$ depending on whether $v _ { i } \in C _ { \pi } \mathrm { o r } v _ { i } \not \in C _ { \pi }$ Note that $l _ { \cdot \ i } ^ { \dagger }$ belongs to $C _ { \pi }$ with respect to the permutation $\vartheta _ { 1 } \vartheta _ { 2 } \ldots \vartheta _ { \eta }$ if and only if $1 . 2$ appears before all $ \ n - 1 - d _ { 1 }$ vertices which are not adjacent to $i i _ { i }$ , or in other words, if $\mathcal { V } _ { \dot { \mathcal { Z } } }$ is the first among $\mathcal { V } _ { \widehat { \mathcal { V } } }$ and its ${ \mathfrak { n } } . - 1 - d _ { i }$ non-neighbors. $\frac { 1 } { \pi - d _ { i } }$ , hence $\begin{array} { r } { E X _ { i } = \frac { 1 } { n } } \end{array}$

![](images/b70017da2207f022210c0d3783d1c4eb37f74a0f84c5d6d04e8fa5e6b9a8680a.jpg)

"Moving weights"

Thus by linearity of expectation (see page 84) we obtain

$$
E ( { \sf \{ C _ { \pi } \} } ) = E X = \sum _ { i = 1 } ^ { n } E X _ { i } = \sum _ { i = 1 } ^ { n } \frac { 1 } { n - d _ { i } } .
$$

Consequently, there must be a clique of at least that size, and this was our claim. To deduce Turán's theorem from the claim we use the Cauchy-Schwarz inequality from Chapter 17,

$$
\Bigl ( \sum _ { i = 1 } ^ { n } a _ { i } b _ { i } \Bigr ) ^ { 2 } \ \leq \ \Bigl ( \sum _ { i = 1 } ^ { n } a _ { i } ^ { 2 } \Bigr ) \Bigl ( \sum _ { n = 1 } ^ { n } b _ { i } ^ { 2 } \Bigr ) .
$$

$\begin{array} { r } { a _ { i } = \sqrt { n - d _ { i } } , b _ { i } = \frac { 1 } { \sqrt { \pi - d _ { i } } } } \end{array}$ , then $a _ { i } b _ { i } = 1$ , and so

$$
n ^ { 2 } \ \leq \ ( \sum _ { i : - 1 } ^ { n } ( n - d _ { i } ) ) ( \sum _ { i - 1 } ^ { n } { \frac { 1 } { n - d _ { i } } } ) \ \leq \ \omega ( G ) \sum _ { i = 1 } ^ { n } ( n - d _ { i } ) .
$$

At this point we apply the hypothesis $\omega \{ G \} \subseteq { \mathfrak { p } } - 1$ of Turán's theorem. Using also $\textstyle \sum _ { i = 1 } ^ { n } d _ { i } = 2 | E |$ ity (2) leads to

$$
n ^ { 2 } \ \leq \ ( p - 1 ) ( \eta ^ { 2 } - 2 \vert E \vert ) ,
$$

and this is equivalent to Turan's inequaliy.

Now we are ready for the last proof, which may be the most beautiful of them all. Its origin is not clear; we got it from Stephan Brandt, who heard it in Oberwolfach. It may be "folklore" graph theory. It yields in one stroke that the Turán graph is in fact the unique example with a maximal number of edges. It may be noted that both proofs 1 and 2 also imply this stronger result.

Fifth proof. Let $G$ be a graph on 7 vertices without a p-clique and with a maximal number of edges.

Claim. $G$ does not contain three vertices u, u, w such that $v / l ^ { \prime } \in E$ .   
$b u t \ u v \notin E , u w \notin E .$ .

Suppose otherwise, and consider the following cases.

Case 1: $d ( u ) < d ( \mathfrak { z } )$ or $d ( u ) < d ( w )$

We may suppose that $d [ \{ t \} ] < d [ \{ \} ]$ .Then we duplicate $\mathcal { V }$ , that is, we create a new vertex $v ^ { \prime }$ which has exactly the same neighbors as $\ v { v }$ (but $v v ^ { t }$ is not an edge), delete $u$ , and keep the rest unchanged.

The new graph $G ^ { \prime }$ has again no $p$ -clique, and for the number of edges we find

$$
| E ( G ^ { \prime } ) | ~ = ~ | E ( G ) | + d ( v ) - d ( u ) ~ > ~ | E ( G ) | ,
$$

![](images/cb298a97b75f579ff9c44a98eb0d8d84994abf60d2c8f1af84f77c44655edd53.jpg)

a contradiction.

Case 2: $d ( u ) \geq d ( \ i ) )$ and $d ( w ) \geq d ( w )$ .

Duplicate $u$ twice and delete $\smash { \ell ^ { \prime } }$ and $2 1 7$ (as illustrated in thc margin). Again, the new graph $G ^ { \prime \prime }$ has no $p$ -clique, and we compute (the $- 1$ results from the edge $\mathbb { Q } \mathbb { Q } \mathbb { 2 }$ ):

$$
| { \cal E } ( G ^ { \prime } ) | ~ = ~ | { \cal E } ( G ) | + 2 d ( u ) - ( d ( v ) + d ( w ) - 1 ) ~ > ~ | { \cal E } ( G ) | .
$$

So we have a contradiction once more.

A moment's thought shows that the claim we have proved is equivalent to the statement that

$$
u \sim v \iff { \mathfrak { u } } . v \not \in E ( G )
$$

defines an equivalence relation. Thus $G$ is a complete multipartite graph, $G = K _ { \pi _ { 1 } , \dots , \pi _ { \mathtt { p } - 1 } }$ , and we are finished.

# References

[1] M. AIGNER: Turán's graph theorem, Amer. Math. Monthly 102 (1995), 808-816.   
[2] N. ALON & J. SpENCER: The Probabilistic Method, Wiley Intcrscicncc 1992.   
[3] P. ERDós: On the graph theorem of Turán (in Hungurian), Math. Fiz. Lapok 21 (1970), 249-251.   
[4] T. S. MoT7.KIN & E. G. STRAUS: Maxima for graphs and a new proof of a theorem of Turán, Canad. J. Math. 17 (1965), 533-540.   
[5] P. TuRÁN: On an extremal problem in graph theory, Math. Fiz. Lapok 48 (1941), 436-452.

![](images/bf8402b4f95be6bfbd412180475242bb74569f6d76f49c7f21c9326b9f0bcc33.jpg)

![](images/ca826bb020037fbb6fe7a6fb943b31d3af1a9ad8c027e4f3e315a1455eac5caf.jpg)

# Communicating without errors

# Chapter 33

In 1956, Claude Shannon, the founder of information theory, posed the following very interesting question:

Suppose we want to transmit messages across a channel (where some symbols may be distorted) to a receiver. What is the maximum rate of transmission such that the receiver may recover the original message without errors?

Let us see what Shannon meant by "channel" and "rate of transmission." We are given a set $V$ of symbols, and a message is just a string of symbols from $V .$ We model the channel as a graph $G = ( V , E )$ , where $V$ is the set of symbols, and $E$ the set of edges between unreliable pairs of symbols, that is, symbols which may be confused during transmission. For example, communicating over a phone in everyday language, we connnect the symbols $B$ and $P$ by an edge since the receiver may not be able to distinguish them. Let us call $G$ the confusion graph.

The 5-cycle $C _ { 5 }$ will play a prominent role in our discussion. In this example, 1 and 2 may be confused, but not 1 and 3, etc. Ideally we would like to use all 5 symbols for transmission, but since we want to communicate error-free we can -- if we only send single symbols — use only one letter from each pair that might be confused. Thus for the 5-cycle we can use only two different letters (any two that are not connected by an edge). In the language of information theory, this means that for the 5-cycle we achieve an information rate of $\log _ { 2 } 2 = 1$ (instead of the maximal $\log _ { 2 } 5 \approx 2 . 3 2 \AA$ . It is clear that in this model, for an arbitrary graph $G = ( V , E )$ , the best we can do is to transmit symbols from a largest independent set. Thus the information rate, when sending single symbols, is $\log _ { 2 } \alpha ( G )$ , where $\alpha ( G )$ is the independence number of $G$ .

Let us see whether we can increase the information rate by using larger strings in place of single symbols. Suppose we want to transmit strings of length 2. The strings $u _ { 1 } u _ { 2 }$ and $v _ { 1 } v _ { 2 }$ can only be confused if one of the following three cases holds:

• $u _ { 1 } = v _ { 1 }$ and $u _ { 2 }$ can be confused with $v _ { 2 }$ , : $u _ { 2 } = v _ { 2 }$ and $u _ { 1 }$ can be confused with $v _ { 1 }$ , or $u _ { 1 } \neq v _ { 1 }$ can be confused and $u _ { 2 } \neq v _ { 2 }$ can be confused.

In graph-theoretic terms this amounts to considering the product $G _ { 1 } \times G _ { 2 }$ of two graphs $G _ { 1 } = ( V _ { 1 } , E _ { 1 } )$ and $G _ { 2 } = ( V _ { 2 } , E _ { 2 } )$ . $G _ { 1 } \times G _ { 2 }$ has the vertex

![](images/29326b0383cf1fde90ced2ed9c71a4d3379b58102aae47724c9017ba7b17ef2f.jpg)  
Claude Shannon

![](images/972be56648bf570c5ab5e9fff4c725224d77cc0b3f6e22c2106afb996d8ed395.jpg)

![](images/0f74385663b8c749c94541dcae21723dcffe886436005d5a669f355ae35889e0.jpg)

The graph $C _ { 5 } \times C _ { 5 }$

set $V _ { 1 } \times V _ { 2 } = \{ ( u _ { 1 } , u _ { 2 } ) : u _ { 1 } \in V _ { 1 } , u _ { 2 } \in V _ { 2 } \}$ , with $( u _ { 1 } , u _ { 2 } ) \neq ( v _ { 1 } , v _ { 2 } )$ connected by an edge if and only if $u _ { i } = v _ { i }$ or $u _ { i } v _ { i } \in E$ for $i = 1 , 2$ The confusion graph for strings of length 2 is thus $G ^ { 2 } \xrightarrow [ ] { } G \times G$ , the product of the confusion graph $G$ for single symbols with itself. The information rate of strings of length 2 per symbol is then given by

$$
{ \frac { \log _ { 2 } \alpha ( G ^ { 2 } ) } { 2 } } ~ = ~ \log _ { 2 } { \sqrt { \alpha ( G ^ { 2 } ) } } .
$$

Now, of course, we may use strings of any length $n$ The $n$ -th confusion graph $G ^ { n } = G \times G \times \ldots \times G$ has vertex set $V ^ { n } = \{ ( u _ { 1 } , \ldots , u _ { n } ) : u _ { i } \in V \}$ with $\left( u _ { 1 } , \ldots ; u _ { n } \right) , \neq \left( v _ { 1 } , \ldots v _ { n } \right)$ being connected by an edge if ${ \mathfrak { U } } _ { i } = { \mathfrak { v } } _ { i }$ or $u _ { i } v _ { i } \in \textit { E }$ for all $i$ The rate of information per symbol determined by strings of length $n$ is

$$
{ \frac { \log _ { 2 } \alpha ( G ^ { n } ) } { \pi } } ~ = ~ \log _ { 2 } ~ \sqrt [ n ] { \alpha ( G ^ { n } ) } .
$$

What can we say about $\alpha ( G ^ { n } ) ?$ Here is a first observation. Let $U \subseteq V$ be a largest independent set in $G$ ${ \vec { z } } , | U | = \alpha$ .The $\alpha ^ { \mathfrak { n } }$ vertices in $G ^ { \eta _ { 2 } }$ of the form $\left( \mathfrak { u } _ { 1 } , \dots , \mathfrak { u } _ { n } \right)$ , $u _ { i } \in U$ for all $i$ , clearly form an independent set in $G ^ { n }$ . Hence

and therefore

$$
\begin{array} { r c l } { { \alpha ( G ^ { n } ) } } & { { \geq } } & { { \alpha ( G ) ^ { n } } } \\ { { } } & { { } } & { { } } \\ { { \ } } & { { } } & { { } } \\ { { \sqrt [ n ] { \alpha ( G ^ { n } ) } } } & { { \geq } } & { { \alpha ( G ) , } } \end{array}
$$

meaning that we never decrease the information rate by using longer strings insted of single symbols. This, by the way, is a basic idea of coding thery: By encoding symbols into longer strings we can make error-free communication more efficient.

Disregarding the logarithm we thus arrive at Shannon's fundamental definition: The zero-error capacity of a graph $G$ is given by

$$
\Theta ( G ) : = \operatorname* { s u p } _ { n \geq 1 } \sqrt [ n ] { \alpha ( G ^ { n } ) } ,
$$

and Shannon's problem was to compute $\Theta ( G )$ , and in particular $\Theta ( \vec { C } _ { 5 } )$ .

Let us look at $C _ { 5 }$ . So far we know $\alpha ( { \bar { C } } _ { 5 } ) = 2 \leq \Theta ( { \bar { C } } _ { 5 } )$ . Looking at the 5-cycle as dcpicted earlier, or at the product $C _ { 5 } \times C _ { 5 }$ as drawn on the left, we see that the set $\{ ( 1 , 1 ) , ( 2 , 3 ) , ( 3 , 5 ) , ( 1 , 2 ) , ( 5 , 1 ) \}$ is independent in $\bar { C } _ { \bar { \mathrm { 5 } } } ^ { 2 }$ Thus we have $\alpha ( \vec { C } _ { 5 } ^ { 2 } ) \geq 5$ Since an independent set can contain only two vertices from any two consecutive rows we see that $\alpha ( \bar { C } _ { \bar { 3 } } { } ^ { 2 } ) = 5$ . Hence, by using strings of length 2 we have increased the lower bound for the capacity to $\Theta ( C _ { \bar { 3 } } ) \ge \sqrt { 5 }$ .

So far we have no upper bounds for the capacity. To obtain such bounds we again follow Shannon's original ideas. First we need the dual definition of an independent set. We recall that a subset $C \subseteq V$ is a clique if any two vertices of $C$ are joined by an edge. Thus the vertices form trivial cliques of size 1, the edges are the cliques of size 2, the triangles are cliques of size 3, and so on. Let $\vec { C }$ be the set of cliques in $G$ Consider an arbitrary probability distribution $x ~ = ~ ( x _ { v } ~ : ~ v ~ \in ~ V )$ on the set of vertices, that is, $x _ { v } \geq 0$ and $\textstyle \sum _ { { \mathfrak { V } } \in V } x _ { \mathfrak { V } } = 1$ . To every distribution $_ { x }$ we associate the "maximal value of a clique"

$$
\lambda ( \pmb { x } ) = \operatorname* { m a x } _ { \mathcal { C } \in \mathcal { C } } \sum _ { \prime , \in \mathcal { C } ^ { \prime } } x _ { v } ,
$$

and finally we set

$$
\lambda ( G ) = \operatorname* { m i n } _ { \mathfrak { X } } \lambda ( \pmb { x } ) = \operatorname* { m i n } _ { \pmb { x } } \operatorname* { m a x } _ { \mathcal { C } ^ { \prime } \in \mathcal { C } } \sum _ { \mathfrak { v } \in \mathcal { C } ^ { \prime } } x _ { \mathfrak { v } } .
$$

To be precise we should use inf instead of min, but the minimum exists because $\lambda ( { \pmb x } )$ is continuous on the compact set of all distributions.

Consider now an independent set $U \subseteq V$ of maximal size $\alpha ( G ) ~ = ~ \alpha$ . Associated to $U$ we define the distribution ${ \pmb x } _ { l { \prime } } = ( x _ { v } : v \in V )$ by setting $\begin{array} { r } { { \mathfrak { Q } } _ { : \ell } = { \frac { 1 } { \alpha } } } \end{array}$ if $\upsilon \in U$ and ${ { x } _ { v } } = 0$ otherwise. Since any clique contains at most one vertex from $U$ , we infer $\begin{array} { r } { \lambda ( \pmb { x } _ { l ^ { \prime } } ) = \frac { 1 } { \alpha } } \end{array}$ , and thus by the definition of $\lambda ( G )$

$$
\lambda ( G ) \leq { \frac { 1 } { \alpha ( G ) } } \qquad { \mathrm { o r } } \qquad \alpha ( G ) \leq \lambda ( G ) ^ { - 1 } .
$$

What Shannon observed is that $\lambda ( G ) ^ { - 1 }$ is, in fact, an upper bound for all $\sqrt [ n ] { \alpha ( G ^ { r } ) }$ , and hence also for $\Theta ( G )$ . In order to prove this it suffices to show that for graphs $G , H$

$$
\lambda ( G \times I I ) ~ = ~ \lambda ( G ) \lambda ( H )
$$

holds, since this will imply $\lambda ( G ^ { n } ) = \lambda ( G ) ^ { n }$ and hence

$$
\begin{array} { r c l } { { \alpha ( G ^ { n } ) } } & { { \leq } } & { { \lambda ( G ^ { n } ) ^ { 1 } = \lambda ( G ) ^ { - n } } } \\ { { \sqrt [ n ] { \alpha ( G ^ { n } ) } } } & { { \leq } } & { { \lambda ( G ) ^ { - 1 } . } } \end{array}
$$

To prove (1) we make use of the duality theorem of linear programming (see|1]) and get

$$
\lambda ( G ) \ = \ \operatorname* { m i n } _ { \bf x \in \mathcal { C } \in \mathcal { C } } \sum _ { v \in \cal C } x _ { v } \ = \ \operatorname* { m a x } _ { y } \operatorname* { m i n } _ { v \in V } \sum _ { \cal C ^ { \prime } \ni v } y _ { \cal C } ,
$$

where the right-hand side runs through all probability distributions ${ \textbf { \em y } } =$ $( y _ { C } : \mathcal { C } \in \mathcal { C } )$ on $\mathcal { C }$ .

Consider $G \times H$ , and let $\pmb { x }$ and $\pmb { x } ^ { \prime }$ be distributions which achieve the minima, $\lambda ( \pmb { x } ) = \lambda ( G \pmb { \cdot } ) , \lambda ( \pmb { x } ^ { \prime } ) = \lambda ( H )$ . In the vertex set of $G \times H$ we assign the value $z _ { ( u , v ) } = x _ { u } x _ { v } ^ { \prime }$ to the vertex $( \boldsymbol { \ i } , \boldsymbol { \ v { v } } )$ .Since $\sum _ { \mathcal { Q } ( u , v ) } \mathcal { Z } _ { \{ \mathfrak { u } , \mathfrak { v } \} } \ \stackrel {  } { = }$ $\begin{array} { r } { \sum _ { u } x _ { u } \sum _ { v } x _ { v } ^ { \prime } = 1 } \end{array}$ , we obtain a distribution. Next we observe that the maximal cliques in $G \times I I$ are of the form $C \times D = \{ ( u , v ) : u \in C , v \in D \}$ where $C$ and $D$ are cliques in $G$ and $H$ , respectively. Hence we obtain

$$
\begin{array} { l c l } { { \lambda ( G \times H ) \ \leq \ \lambda ( z ) } } & { { = } } & { { \displaystyle \operatorname* { m a x } _ { C \times D } \displaystyle \sum _ { ( u , v ) \in C \times D } z _ { ( u , v ) } } } \\ { { } } & { { } } & { { \displaystyle - \ \operatorname* { m a x } _ { C \times D } \displaystyle \sum _ { u \in C } x _ { u } \displaystyle \sum _ { v \in D } x _ { v } ^ { \prime } \ = \ \lambda ( G ) \lambda ( H ) } } \end{array}
$$

![](images/823e5ddee8aafbd2e22a29915e9c238c9543616ac7cdc04fc7f073f8ff3f66be.jpg)

The Lovász umbrella

by the definition of $\lambda ( G \times H )$ . In the same way the converse inequality $\lambda ( G \times H ) \geq \lambda ( G ) \lambda ( H )$ is shown by using the dual expression for $\lambda ( G )$ in (2). In summary we can state:

$$
\Theta ( { \cal G } ) \ \leq \ \lambda ( { \cal G } ) ^ { - 1 } ,
$$

for any graph $G$

Let us apply our findings to the 5-cycle and, more generally, to the $m$ $C _ { m }$ obBiy ifomn is blion $\textstyle { \left( { \frac { 1 } { r r } } , \ldots , { \frac { 1 } { r } } \right) }$ on the vertices, we obtain $\lambda ( C _ { m } ) \leq \frac { 2 } { m }$   
vertices. Smilarly, choosing $\begin{array} { l } { \frac { \downarrow } { m } } \end{array}$ t n s $\begin{array} { r } { \lambda ( C _ { m } ) \ge \frac { 2 } { m } } \end{array}$ by the dual expression in (2). We conclude that $\begin{array} { r } { \lambda ( C _ { m } ) = \frac { 2 } { m } } \end{array}$ and therefore

$$
\Theta ( C _ { m } ) \ \leq \ \frac { m } { 2 }
$$

for all $m$ .Now, if $^ { \prime \prime }$ is even, then clearly $\begin{array} { r } { \alpha ( C _ { \gamma \gamma _ { 2 } } ) ~ = ~ \frac { \eta _ { 2 } } { 2 } } \end{array}$ and thus also $\begin{array} { r } { \Theta ( { C _ { \prime n } } ) = \frac { \pi } { 2 } } \end{array}$ . For odd $m$ , however, we have $\begin{array} { r } { \alpha ( C _ { m } ) = \frac { \eta - 1 } { 2 } } \end{array}$ For $m = 3$ , $C _ { 3 }$ is a clique, and so is every product $C _ { 3 } ^ { \eta _ { 2 } }$ , implying $\alpha ( C _ { 3 } \bar { ) } = \Theta ( C _ { 3 } ) = 1$ . So, the first interesting case is the 5-cycle, where we know up to now

$$
{ \sqrt { 5 } } ~ \leq ~ \Theta ( C _ { 5 } ) ~ \leq ~ { \frac { 5 } { 2 } } .
$$

Using his linear programming approach (and some other ideas) Shannon was able to compute the capacity of many graphs and, in particular, of all graphs with five or fewer vertices — with the single exception of $C _ { 5 }$ , where he could not go beyond the bounds in (3). This is where things stood for more than 20 years until Lászl6 Lovász showed by an astonishingly simple argument that indeed $\Theta ( C _ { 5 } ) \simeq \sqrt { 5 }$ A seemingly very difficult combinatorial problem was provided with an unexpected and elegant solution.

Lovász' main new idea was to represent the vertices $\wr$ of the graph by real vectors of length 1 such that any two vectors which belong to nonadjacent vertices in $G$ are orthogonal. Let us call such a set of vectors an orthonormal representation of $\bar { G }$ Clearly, such a representation always exists: just take the unit vectors $( 1 , 0 , \ldots , 0 ) ^ { T }$ $( 0 , 1 , 0 , \ldots , 0 ) ^ { T }$ , .…, $( 0 , \mathbf { 0 } , \dots , 1 ) ^ { T }$ of dimension $m = | V |$ .

For the graph $C _ { 5 }$ we may obtain an orthonormal representation in $\mathbb { R } ^ { 3 }$ by considering an "umbrella" with five ribs $\pmb { v } _ { 1 } , \ldots , \pmb { v } _ { 5 }$ of unit length. Now open the umbrella (with tip at the origin) to the point where the angles between alternate ribs are $9 0 ^ { \mathrm { c } }$ .

Lovász then went on to show that the height $h$ of the umbrella, that is, the distance between O and $S$ , provides the bound

$$
\Theta ( C _ { 5 } ) \leq \frac { 1 } { h ^ { 2 } } .
$$

A simple calculation yields $\textstyle h ^ { 2 } = { \frac { 1 } { \sqrt { 5 } } }$ ; sce the box on the next page. From this $\Theta ( \vec { C } _ { 5 } ) \le \sqrt { 5 }$ follows, and therefore $\Theta ( \vec { C } _ { 5 } ) = \sqrt { 5 }$ .

Let us see how Lovász proceeded to prove the inequality (4). (His results were, in fact, much more general.) Consider the usual inner product

$$
\langle \pmb { x } , \pmb { y } \rangle = { \pmb { x } } _ { 1 } { y } _ { 1 } + \ldots + { \pmb { x } } _ { s } { y } _ { s }
$$

of two vectors $\mathbf { x } = ( { x } _ { 1 } , \dots , { x } _ { s } )$ , $\pmb { y } = ( y _ { 1 } , \dots , y _ { s } )$ in $\mathbb { R } ^ { s }$ .Then $| \pmb { x } | ^ { 2 } =$ $\langle \pmb { x } , \pmb { x } \rangle = \pmb { x } _ { 1 } ^ { 2 } + \dots + \pmb { x } _ { s } ^ { 2 }$ is the square of the length $| { \pmb x } |$ of $\pmb { x }$ , and the angle $\gamma$ between $\pmb { x }$ and $y$ is given by

$$
\cos \gamma ~ { \stackrel { } { \dots } } ~ { \frac { \langle { \pmb x } , { \pmb y } \rangle } { | { \pmb x } | | { \pmb y } \rangle } } .
$$

Thus $\langle \pmb { x } , \pmb { y } \rangle = 0$ if and only if $\pmb { x }$ and $y$ are orthogonal.

# Pentagons and the golden section

Tradition has it that a rectangle was considered aesthetically pleasing if, after cutting off a square of length $\mathcal { Q }$ , the remaining rectangle had the same shape as the original one. The side lengths $a , b$ of such a rectangle must satisfy $\frac { b } { a } = \frac { a } { b - a }$ .Setting $r : = \frac { b } { a }$ for the ratio, we obtain $\begin{array} { r } { \tau = \frac { 1 } { \tau - 1 } } \end{array}$ or $\tau ^ { 2 } - \tau - 1 = 0$ Solving the quadratic equation yields the golden section $\begin{array} { r } { \tau = \frac { 1 + \sqrt { 5 } } { 2 } \approx 1 . 6 1 8 0 } \end{array}$ .

Consider now a regular pentagon of side length $a$ , and let $d$ be the length of its diagonals. It was already known to Euclid (Book XIII,8) that $\frac { d } { d t } = T$ , and that the intersection point of two diagonals divides the diagonals in the golden section.

Here is Euclid's Book Proof. Since the total angle sum of the pentaon   is $3 \pi$ $\frac { 3 \pi } { 5 }$ It fo lows that $\begin{array} { r } { \triangleleft A B E = { \frac { \pi } { 5 } } } \end{array}$ , since $A B E$ is an isosceles triangle.This, in turn, implies $\begin{array} { r } { \mathtt { q } A \overset { \vee } { M } B = \frac { 3 \pi } { 5 } } \end{array}$ $A B C$ and $A M B$ are similar. The quadrilateral $C M E D$ is a rhombus since opposing sides are parallel (look at the angles), and so $| M C | = \alpha$ and thus $| A M | = d - \alpha .$ By the similarity of $A B C$ and $A M B$ we conclude

$$
{ \frac { d } { a } } = { \frac { | A C | } { | A B | } } = { \frac { | A B | } { | A M | } } = { \frac { a } { d - a } } = { \frac { | M C | } { | M A | } } = \tau .
$$

There is more to come. For the distance $\pmb { S }$ of a vertex to the center of (note that $B S$ cuts the diagonal $A C$ at a right angle and halves it).

To finish our excursion into geometry, consider now the umbrella with the regular pentagon on top. Since alternate ribs (of length 1) form a right angle, the theorem of Pythagoras gives us $d = { \sqrt { 2 } } ,$ and hence $\textstyle s ^ { 2 } = { \frac { 2 } { \tau + 2 } } = { \frac { 4 } { \sqrt { 5 } + 5 } }$ So, with Pythagoras again, we find for the height $h = | O S |$ our promised result

$$
h ^ { 2 } = 1 - s ^ { 2 } = { \frac { 1 + { \sqrt { 5 } } } { \sqrt { 5 } + 5 } } = { \frac { 1 } { \sqrt { 5 } } } .
$$

![](images/23cc377b2547c9a497fa0ef50da3fe4f62f72a6dfa480d3e07afc73bafff7eb1.jpg)

$b - a$

![](images/21bfa2b5a218db5fc98275ee6ed31e5c9690e189f63c6444a3c34f453c1d5ea4.jpg)

Now we head for an upper bound ${ } ^ { * } \Theta ( G ) \leq \sigma _ { T } ^ { - 1 } { } ^ { * }$ for the Shannon capacity of any graph $G$ that has an especially "nice" orthonormal representation. For this let $\begin{array} { r c l } { T } & { = } & { \{ \mathbf { { v } } ^ { ( 1 ) } ; \dots , \mathbf { \bar { v } } ^ { ( m ) } \} } \end{array}$ be an orthonormal representation of $G$ in $\mathbb { R } ^ { s }$ where $\dot { v } ^ { ( i ) }$ corresponds to the vertex ${ \boldsymbol { v } } _ { i }$ . We assume in addition that all the vectors ${ \pmb v } ^ { ( i ) }$ have the same angle $( \neq 9 0 ^ { \circ } )$ with the vector $\begin{array} { r } { \pmb { \mathscr { u } } : = \frac { 1 } { \eta \imath } ( \pmb { \mathscr { v } } ^ { ( 1 ) } + . . . + \pmb { \mathscr { v } } ^ { ( m ) } ) } \end{array}$ , or eqivalentl that the ine pouct

$$
\langle { { \bf { v } } ^ { ( i ) } , { \bf { u } } } \rangle = \sigma _ { T }
$$

has the same value $\sigma _ { T } \neq 0$ for all $i$ Let us call this value $\sigma _ { \boldsymbol { T } }$ the constant of the representation $T$ . For the Lovász umbrella that represents $C _ { 5 }$ the condition $\langle { \pmb v } ^ { ( i ) } , { \pmb u } \rangle = \sigma _ { T }$ certainly holds, for $\pmb { u } = \vec { O S }$ .

Now we proceed in the following three steps.

(A) Consider a probability distribution $\pmb { x } = ( x _ { 1 } , \dots , x _ { m } )$ on $V$ and set

$$
\begin{array} { r } { \begin{array} { l l l } { \mu ( \pmb { x } ) } & { : = } & { | x _ { 1 } \pmb { v } ^ { ( 1 ) } + \dots + x _ { m } \pmb { v } ^ { ( m ) } | ^ { 2 } , } \end{array} } \end{array}
$$

and

$$
\mu _ { \dot { \cdot } \dot { \cdot } } ( { \cal G } ) : = \operatorname * { i n f } _ { \bf x } \mu ( { \bf x } ) .
$$

Let $U$ be a largest independent set in $\bar { G }$ with $| U | = \alpha$ , and define ${ \pmb x } _ { U } =$ $\left( x _ { 1 } , \dots , x _ { m } \right)$ with $\begin{array} { r } { x _ { i } ~ = ~ \frac { 1 } { \alpha } } \end{array}$ if $\mathfrak { v } _ { i } ~ \in ~ U$ and $x _ { i } ~ = ~ 0$ otherwise. Since all vectors $\pmb { v } ^ { ( i ) }$ have unit length and $\langle { \pmb v } ^ { ( i ) } , { \pmb v } ^ { ( j ) } \rangle = 0$ for any two non-adjacent vertices, we infer

$$
\mu _ { r _ { \smash } } ( G ) \ \leq \ \mu ( { \pmb x } _ { U } ) \ = \ \Big | \sum _ { i = 1 } ^ { m } x _ { i } { \pmb v } ^ { ( i ) } \Big | ^ { 2 } \ = \ \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } = \alpha \frac { 1 } { \alpha ^ { 2 } } = \frac { 1 } { \alpha } .
$$

Thus we have $\mu , _ { f } . ( G ) \leq \alpha ^ { - 1 }$ , and therefore

$$
\alpha ( G ) \ \leq \ \frac { 1 } { \mu _ { T } ( G ) } .
$$

(B) Next we compute $\mu _ { \gamma } \mathopen { } \mathclose \bgroup \left( G \aftergroup \egroup \right)$ .We need the Cauchy-Schwarz inequality

$$
\langle a , b \rangle ^ { 2 } \ \leq \ | a | ^ { 2 } | b | ^ { 2 }
$$

for vectors $a , b \in \mathbb { R } ^ { s }$ .Applied to $\pmb { a } = x _ { \mathrm { { i } } } \pmb { v } ^ { ( 1 ) } + . . . + x _ { m } \pmb { v } ^ { ( m ) }$ and $\ b _ { b } = \ b { u }$ the inequality yields

$$
\langle x _ { 1 } { \pmb v } ^ { ( 1 ) } + \ldots + x _ { m } { \pmb v } ^ { ( m ) } , { \pmb u } \rangle ^ { 2 } \ \leq \ \mu ( { \pmb x } ) | { \pmb u } | ^ { 2 } .
$$

By our assumption that $\langle { \pmb v } ^ { ( i ) } , { \pmb u } \rangle = \sigma _ { T }$ for all $i$ , we have

$$
\langle x _ { 1 } { \pmb v } ^ { ( 1 ) } + . . . + x _ { m } { \pmb v } ^ { ( m ) } , { \pmb u } \rangle = \left( x _ { 1 } + . . . + x _ { m } \right) \sigma _ { T } = \sigma _ { T }
$$

for any distribution $\pmb { x }$ . Thus, in particular, this has to hold for the uniform distribution $\textstyle { \bigl ( } { \frac { 1 } { \pi \cdot } } , \ldots , { \frac { 1 } { \gamma \gamma _ { 2 } } } { \bigr ) }$ whic implies $| \boldsymbol { u } | ^ { 2 } = \sigma _ { \gamma }$ Hence (5) reduces to

$$
\sigma _ { T } ^ { 2 } \ \leq \ \mu ( \mathbf { x } ) \sigma _ { T } \qquad \mathrm { o r } \qquad \mu _ { T } ( G ) \geq \ \sigma _ { T } .
$$

On the other hand, for $\pmb { x } = ( \frac { 1 } { m } , \dots , \frac { 1 } { m } )$ we obtain

$$
\begin{array} { r } { \mu _ { T } ( G ) \le \mu ( \pmb { x } ) = | \frac { \perp } { m } ( \pmb { v } ^ { ( 1 ) } + . . . + \pmb { v } ^ { ( m ) } ) | ^ { 2 } = | \pmb { u } | ^ { 2 } = \sigma _ { \prime \prime } , } \end{array}
$$

and so we have proved

$$
\mu _ { _ { T } } ( G ) = \sigma _ { _ { T } } .
$$

In summary, we have established the inequality

$$
\alpha \big ( \tilde { G } \big ) \ \leq \ \frac { 1 } { \sigma _ { T } }
$$

for any orthnormal respentation $T$ with constant $\sigma _ { T }$ .

(C) To extend this incquality to $\Theta ( { \vec { G } } )$ , we proceed as before. Consider again the product $G \times H$ of two graphs. Let $G$ and $H$ have orthonormal represntations $R$ and $S$ in $\mathbb { R } ^ { r }$ and $\mathbb { R } ^ { s }$ epeively, th constants $\sigma _ { R }$ and $\sigma _ { S }$ . Let $\pmb { v } = \left( v _ { 1 } , \dots , v _ { r } \right)$ be a vector in $R$ and $\pmb { w } = ( w _ { 1 } , \dots , w _ { s } )$ be a vector in $S$ To the vertex in $G \times H$ corresponding to the pair $( v , w )$ we associate the vector

$$
\begin{array} { r } { \pmb { v } \pmb { w } ^ { T } : = \left( v _ { 1 } w _ { 1 } , \ldots , v _ { 1 } w _ { s } , v _ { 2 } w _ { 1 } , \ldots , v _ { 2 } w _ { s } , \ldots , v _ { r } w _ { 1 } , \ldots , v _ { r } w _ { s } \right) \in \mathbb { R } ^ { r \times } . } \end{array}
$$

It is immediately checked that $R \times S : = \{ { \pmb v } { \pmb w } ^ { T } : { \pmb v } \in \bar { R } , { \pmb w } \in S \}$ is an orthonormal representation of $G \times H$ with constant $\sigma _ { R } \sigma _ { S }$ . Hence by (6) we obtain

$$
\begin{array} { r } { \mu _ { R \times S } ( G \times H ) = \mu _ { R } ( G ) \mu _ { S } ( H ) . } \end{array}
$$

For $G ^ { n } = G \times \ldots \times G$ and the representation $T$ with constant $\sigma _ { T }$ this means

$$
\mu _ { T ^ { n } } ( G ^ { n } ) ~ = ~ \mu _ { T } ( G ) ^ { n } ~ = ~ \sigma _ { T } ^ { n }
$$

and by (7) we obtain

$$
\alpha ( G ^ { n } ) \ \leq \ \sigma _ { T } ^ { - n } , \qquad { \sqrt [ n ] { \alpha ( G ^ { n } ) } } \ \leq \ \sigma _ { T } ^ { - 1 } .
$$

Taking all things together we have thus completed Lovász' argument:

Theorem. Whenever $T ~ = ~ \{ v ^ { ( 1 ) } , \ldots , v ^ { ( m ) } \}$ is an orthonormal representation of $G$ with constant $\sigma _ { T }$ , then

$$
\Theta ( G ) \ \leq \ \frac { 1 } { \sigma _ { _ T } } .
$$

Looking at the Lovász umbrella, we have $\mathbf { \boldsymbol { u } } = ( 0 , 0 , \hbar { = } \frac { 1 } { \sqrt [ 4 ] { 5 } } ) ^ { T }$ and hence $\textstyle \sigma = \langle { \pmb v } ^ { ( i ) } , { \pmb u } \rangle = h ^ { 2 } = { \frac { 1 } { \sqrt { 5 } } }$ which yields θ(C) ≤ 5.Thus Shannon's problem is solved.

![](images/c2010f3bcb0a0fe93d8551a57242d21a4a26843a0ecfeb2a93640e4215961a55.jpg)  
Umbrellas with five ribs"

$$
\begin{array} { r } { A = \left( \begin{array} { l l l l l } { 0 } & { 1 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } & { 1 } & { 0 } \end{array} \right) } \end{array}
$$

The adjacency matrix for the 5-cycle $C . 5$

$\sigma _ { T }$ is for a representation of $G$ , the better a bound for $\Theta ( \vec { \pi } )$ we will get. Here is a method that gives us an orthonormal representation for any graph $G$ . To $G = ( V , E )$ we associate the adjacency matrix $A = ( a _ { i j } )$ , which is defined as follows: Let $V ^ { ' } = \{ v _ { 1 } , \ldots , v _ { r r i } \}$ , then we set

$$
a _ { i , j } : = \left\{ { \begin{array} { l l } { 1 } & { { \mathrm { i f } } v _ { i } v _ { j } \in E } \\ { 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} } \right.
$$

$A$ is a real symmetric matrix with $( ) ^ { * } s$ in the main diagonal.

Now we need two facts from linear algebra. First, as a symmetric matrix, $A$ has m real cigenvalues $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \ldots \geq \lambda _ { \tau \tau }$ (some of which may be equal), and the sum of the eigenvalues equals the sum of the diagonal entries of $A$ , that is, O. Hence the smallest eigenvalue must bc ncgative (except in the trivial case when $G$ has no edges). Lct $p = | \lambda _ { r n } | = - \lambda _ { m }$ be the absolute value of the smallest eigenvalue, and consider the matrix

$$
M \ : = \ I \ + \ { \frac { 1 } { p } } \ A ,
$$

where $I$ denotes the $( \gamma \gamma ) \times \gamma \gamma \hat { \imath } \rangle$ identity matrix. This $M$ has the eigenvalues $\begin{array} { r } { 1 + \frac { \lambda _ { 1 } } { p } \geq 1 + \frac { \lambda _ { 2 } } { p } \geq . . . \geq 1 + \frac { \lambda _ { \pi } } { p } = 0 } \end{array}$ Now we quote the scond result principal axis theorem of linear algebra): If $M = ( m _ { i j } )$ is a real symmetric matrix with all eigenvalues $\geq 0$ , then there are vectors (1 $\mathbf { \bar { v } } ^ { ( \bar { \ n } \bar { \mathfrak { z } } ) } \in \mathbb { R } ^ { s }$ for $s = \mathrm { r a n k } ( \mathbb { M } )$ , such that

$$
m _ { i j } ~ = ~ \langle { \pmb v } ^ { ( i ) } , { \pmb v } ^ { ( j ) } \rangle ~ ( 1 \leq i , j \leq m ) .
$$

In particular, for $M - I + { \textstyle { \frac { 1 } { p } } } A$ we obtain

$$
\langle { \pmb v } ^ { ( i ) } , { \pmb v } ^ { ( i ) } \rangle = m _ { i i } = { \bf 1 } \qquad \mathrm { f o r ~ a l l ~ } i
$$

and

$$
\langle { \pmb v } ^ { ( i ) } , { \pmb v } ^ { ( j ) } \rangle = \frac { 1 } { p } a _ { i , j } \qquad \mathrm { f o r } i \ne j .
$$

Since ${ a _ { i j } } = 0$ whenever $v _ { i } v _ { j } \not \equiv E$ ,we see that the vectors $\pmb { v } ^ { ( 1 ) } , \dots , \pmb { v } ^ { ( \pi z ) }$ form indeed an orthonormal representation of $G$ .

Let us, finally, apply this construction to the m-cycles $C _ { n 2 }$ for odd $m \geq 5$ . Here one easily computes $\begin{array} { r } { p \ = \ | \lambda _ { \mathrm { m i n } } | \ = \ 2 \cos { \frac { \pi } { \pi } } } \end{array}$ (see the box). Every row of the adjacency matrix contains two $| \mathit { \Pi } _ { \mathbf { \hat { s } } } ^ { \ }$ ,implying that every row of the matrix $M$ sums to $1 \ + \ { \frac { 2 } { p } }$ For the representation $\{ \hat { \pmb { v } } ^ { ( 1 ) } , \dots , \hat { \pmb { v } } ^ { ( m ) } \}$ this means

$$
\langle { \pmb v } ^ { ( i ) } , { \pmb v } ^ { ( 1 ) } \ + \ . \ . . \ { \pmb v } ^ { ( m ) } \rangle \ = \ 1 \ + \ \frac { 2 } { p } \ = \ 1 \ + \ \frac { 1 } { \cos \frac { \pi } { m } }
$$

and hence

$$
\langle { \pmb v } ^ { ( i ) } , { \pmb u } \rangle = \frac { 1 } { m } ( 1 + ( \cos \frac { \pi } { m } ) ^ { - 1 } ) = \sigma
$$

for all $i$ We can therefore apply our main result (8) and conclude

$$
\Theta ( C _ { m } ) \ \leq \ { \frac { m } { 1 + ( \cos { \frac { \pi } { m } } ) ^ { - 1 } } } \qquad ( { \mathrm { f o r ~ } } m \geq 5 \ { \mathrm { o d d } } ) .
$$

Notice that because of $\begin{array} { r } { z _ { 0 \mathrm { s } } \frac { \pi } { \eta _ { \mathrm { s } } } < 1 } \end{array}$ the bound (9) is better than the bound $\begin{array} { r } { \Theta ( { \cal C } _ { m } ) \le \frac { m } { 2 } } \end{array}$ we found before. Note further cos $\begin{array} { r } { \frac { \pi } { 5 } = \frac { \tau } { 2 } } \end{array}$ , whcrc $\begin{array} { r } { \tau = \frac { \sqrt { 5 } + 1 } { 2 } } \end{array}$ is the golden section. Hence for $\hbar \boldsymbol { n } = 5$ we again obtain

$$
\Theta ( C _ { 5 } ) \le { \frac { 5 } { 1 + { \frac { 4 } { \sqrt { 5 } + 1 } } } } = { \frac { \breve { \mathfrak { z } } ( \sqrt { \breve { \mathfrak { z } } } \ + 1 ) } { 5 + \sqrt { 5 } } } = \sqrt { \breve { \mathfrak { z } } } .
$$

The orthonormal representation given by this construction is, of course, precisely the "Lovász umbrella."

And what about $C _ { 7 } , C _ { 9 }$ , and thc other odd cycles? By considering $\phantom { } ( \chi \bigl ( C _ { m } ^ { 2 } \bigr )$ , $\alpha \big ( C _ { \tau \tau \iota } ^ { 3 } \big )$ and other small powers the lower bound $\frac { m - 1 } { 2 } \leq \Theta ( C _ { m } )$ can certainly be increased, but for no odd $r n \geq 7$ do the best known lower bounds agree with the upper bound given in (8). So, twenty years after Lovász' marvelous proof of $\Theta ( C _ { 5 } ) \ = \ \sqrt { 5 }$ , these problems remain open and are considered very difficult — but after all we had this situation before.

For example, for $m = 7$ all we know is $\sqrt [ 5 ] { 3 4 3 } \leq \Theta ( C \tau ) \leq \frac { 7 } { 1 + ( \cos \frac { \pi } { 7 } ) ^ { - 1 } } ,$ which is $3 . 2 1 4 1 \leq \Theta ( C _ { 7 } ) \leq 3 . 3 1 7 7 .$

# The eigenvalues of $C _ { m }$

Look at the adjacency matrix $A$ of the cycle $C _ { m }$ . To find the eigenvalues (and eigenvectors) we use the $^ { m }$ -th roots of unity. These are gven by $1 , \zeta , \bar { \zeta } ^ { 2 } , \ldots , \zeta ^ { \prime \prime \prime - 1 }$ for $\zeta = e ^ { \frac { 2 \pi i } { m } }$ — see the box on page 25. Let $\begin{array} { r l r } { \lambda } & { { } = } & { \zeta ^ { k } } \end{array}$ be any of these roots, then we claim that $( 1 , \lambda , \lambda ^ { 2 } , \dots , \lambda ^ { m - 1 } ) ^ { T }$ is an eigenvector of $A$ to the eigenvaluc $\lambda +$ $\lambda ^ { - 1 }$ . In fact, by the set-up of $A$ we find

$$
A \left( \begin{array} { l } { 1 } \\ { \lambda } \\ { \lambda ^ { 2 } } \\ { \vdots } \\ { \lambda ^ { m - 1 } } \end{array} \right) = \left( \begin{array} { l l l } { \lambda } & { + } & { \lambda ^ { m - 1 } } \\ { \lambda ^ { 2 } } & { + } & { 1 } \\ { \lambda ^ { 3 } } & { + } & { \lambda } \\ & { \vdots } \\ { 1 } & { + } & { \lambda ^ { m - 2 } } \end{array} \right) = ( \lambda + \lambda ^ { - 1 } ) \left( \begin{array} { l } { 1 } \\ { \lambda } \\ { \lambda ^ { 2 } } \\ { \vdots } \\ { \lambda ^ { m - 1 } } \end{array} \right) .
$$

Since the vectors $( 1 , \lambda , \dots , \lambda ^ { \prime \prime \lambda - 1 } )$ are independent (they form a socalled Vandermonde matrix) we conclude that for odd $_ { m }$

$$
\begin{array} { l l l } { { \zeta ^ { k } + \zeta ^ { - k } } } & { { = } } & { { \left[ ( \cos ( 2 k \pi / m ) + i \sin ( 2 k \pi / m ) \right] } } \\ { { } } & { { } } & { { + \left\{ \cos ( 2 k \pi / m ) - i \sin ( 2 k \pi / m ) \right\} } } \\ { { } } & { { = } } & { { 2 \cos ( 2 k \pi / m ) \qquad ( 0 \le k \le { \frac { m - 1 } { 2 } } ) } } \end{array}
$$

are all the eigenvalues of $A$ Now the cosine is a decreasing function, and so

$$
2 \cos \left( { \frac { ( m - 1 ) \pi } { m } } \right) ~ = ~ - 2 \cos { \frac { \pi } { m } }
$$

is the smallest eigenvalue of $A$ .

# References

[1] V. CHVÁTAL: Linear Programming, Freeman, New York 1983.   
[2] W. HAEMERs: Eigenvalue methods, in: "Packing and Covering in Combinatorics" (A. Schrijver, cd.), Math. Centrc Tracts 106 (1979), 15-38.   
[3] L. LovÁsz: On the Shannon capacity of a graph, IEEE Trans. Information Theory 25 (1979), 1-7.   
[4] C. E. SHANNON: The zero-error capacity of a noisy channel, IRE Trans. Information Theory 3 (1956), 3-15.

It is not known who first raised the following problem or who gave it its human touch. Here it is:

Suppose in a group of people we have the situation that any pair of persons have precisely one common friend. Then there is always a person (the "politician") who is everyhody's friend.

In the mathematical jargon this is called the friendship theorem.

Before tackling the proof let us rephrase the problem in graph-theoretic terms. We interpret the people as the set of vertices $V$ and join two vertices by an edge if the corresponding people are friends. We tacitly assume that friendship is always two-ways, that is, if $u$ is a friend of v, then $\mathcal { V }$ is also a friend of $u$ , and further that nobody is his or her own friend. Thus the theorem takes on the following form:

Theorem. Suppose that $G$ is a finite graph in which any two vertices have precisely one common neighbor. Then there is a vertex which is adjacent to all other vertices.

Note that there are finite graphs with this property; see the figure, where u is the politician. However, these "windmill graphs" also turn out to be the only graphs with the desired property. Indeed, it is not hard to verify that in the presence of a politician only the windmill graphs are possible.

Surprisingly, the friendship theorem does not hold for infinite graphs! Indeed, for an inductive construction of a counterexample one may start for example with a 5-cycle, and repeatedly add common neighbors for all pairs of vertices in the graph that don't have one, yet. This leads to a (countably) infinite friendship graph without a politician.

Several proofs of the friendship theorem exist, but the first proof, given by Paul Erdôs, Alfred Rényi and Vera Sós, is still the most accomplished.

Proof. Suppose the assertion is false, and $G$ is a counterexample, that is, no vertex of $G$ is adjacent to all other vertices. To derive a contradiction we proceed in two steps. The first part is combinatorics, and the second part is linear algebra.

(1) We claim that $G$ is a regular graph, that is, $\mathbb { d } ( \{ u \} = \mathbb { d } \{ \eta \}$ for any $u , v \in V ,$ Note first that the condition of the theorem implies that there are no cycles of length 4 in $G$ Let us call this the $C _ { 1 }$ -condition.

![](images/5e8eed37cb358bbed6840914366b5388550af39c18e15e2715f9369d16b87037.jpg)

"A politician's smile"

![](images/956e61c723994ddef20825b87a1a925e5930ac0fd144f9719f7e3eacc95e79f7.jpg)  
A windmill graph

![](images/95f12f089dc58cf05c33e225aaa8c218af097770f61cf47d9d22ad162e418749.jpg)

![](images/a1c3c51e72bf3a970d515e555ae68c3f692fd00e359b35df5154b72fa8c974e8.jpg)

We first prove that any two non-adjacent vertices $u$ and $v$ have equal degree $d ( u ) = d ( v )$ . Suppose $d ( u ) = k$ , where $w _ { 1 } , \ldots , w _ { k }$ are the neighbors of $u$ . Exactly one of the $w _ { i }$ , say $w _ { 2 }$ , is adjacent to $v$ , and $w _ { 2 }$ adjacent to exactly one of the other $w _ { i }$ 's, say $w _ { 1 }$ , so that we have the situation of the figure to the left. The vertex $v$ has with $w _ { 1 }$ the common neighbor $w _ { 2 }$ , and with $w _ { i }$ $( i \geq 2 )$ a common neighbor $z _ { i }$ $\left( i \geq 2 \right)$ . By the $C _ { 4 }$ -condition, all these $z _ { i }$ must be distinct. We conclude $d ( v ) \geq k = d ( u )$ , and thus $d ( u ) = d ( v ) = k$ by symmetry.

To finish the proof of (1), observe that any vertex different from $w _ { 2 }$ is not adjacent to either $u$ or $v$ , and hence has degree $k$ , by what we already proved. But since $w _ { 2 }$ also has a non-neighbor, it has degree $k$ as well, and thus $G$ is $k$ -regular.

Summing over the degrees of the $k$ neighbors of $u$ we get $k ^ { 2 }$ . Since every vertex (except $u$ ) has exactly one common neighbor with $u$ , we have counted every vertex once, except for $u$ , which was counted $k$ times. So the total number of vertices of $G$ is

$$
n \ = \ k ^ { 2 } - k + 1 .
$$

(2) The rest of the proof is a beautiful application of some standard results of linear algebra. Note first that $k$ must be greater than 2, since for $k \leq 2$ only $G = K _ { 1 }$ and $G = K _ { 3 }$ are possible by (1), both of which are trivial windmill graphs. Consider the adjacency matrix $A = \left( a _ { i j } \right)$ , as defined on page 220. By part (1), any row has exactly $k$ 1's, and by the condition of the theorem, for any two rows there is exactly one column where they both have a 1. Note further that the main diagonal consists of $0 ^ { \prime } s$ Hence we have

$$
\begin{array} { r c l } { { A ^ { 2 } } } & { { = } } & { { \left( \begin{array} { l l l l } { { k } } & { { 1 } } & { { \dots } } & { { 1 } } \\ { { 1 } } & { { k } } & { { } } & { { 1 } } \\ { { \vdots } } & { { } } & { { \ddots } } & { { \vdots } } \\ { { 1 } } & { { \dots } } & { { 1 } } & { { k } } \end{array} \right) } } \end{array} = ( k - 1 ) I + J ,
$$

where $I$ is the identity matrix, and $J$ the matrix of all 1's. It is immediately checked that $J$ has the eigenvalues $n$ (of multiplicity 1) and 0 (of multiplicity $n - 1 \mathrm { \Delta }$ It follows that $A ^ { 2 }$ has the eigenvalues $k - 1 + n = k ^ { 2 }$ (of multiplicity 1) and $k - 1$ (of multiplicity $n - 1 ,$ .

Since $A$ is symmetric and hence diagonalizable, we conclude that $A$ has the eigenvalues $k$ of multiplicity 1) and $\pm \sqrt { k - 1 }$ Suppose $r$ of the eigenvalues are equal to $\sqrt { k - 1 }$ and $s$ of them are equal to $- { \sqrt { k - 1 } }$ , with $r + s = n - 1$ .Now we are almost home. Since the sum of the eigenvalues of $A$ equals the trace (which is 0), we find

$$
k + r { \sqrt { k - 1 } } - s { \sqrt { k - 1 } } = 0 ,
$$

and, in particular, $r \neq s$ , and

$$
{ \sqrt { k - 1 } } \ = \ { \frac { k } { s - r } } .
$$

Now if the square root $\sqrt { \gamma \mu }$ of a natural number mn is rational, then it is an integer! An elegant proof for this was presented by Dedekind in 1858: Let $n _ { 0 }$ be the smallest natural number with $\mathfrak { r } _ { 1 0 } \sqrt { \mathfrak { n } \mathfrak { r } } \in \mathbb { N }$ .If $\sqrt { \pi x } \notin \mathbb { N }$ , then there exists $\ell \in \mathbb { N }$ with $0 < \sqrt  \gamma \eta \} - \ell < 1$ Setting $n _ { 1 } : = n _ { 0 } ( \sqrt { \pi } - \ell )$ , we find $\textstyle n _ { 1 } \in \mathbb { N }$ and $n _ { 1 } \sqrt { m } = n _ { 0 } ( \sqrt { m } \cdot \ell ) \sqrt { m } = n _ { 0 } m - \ell ( n _ { 0 } \sqrt { m } ) \in \mathbb { N }$ With $n _ { 1 } < n _ { ! }$ this yields a contradiction to the choice of $n _ { 0 }$ .

Returning to our equation, let us set $h = \sqrt { k - 1 } \in \mathbb { S } .$ ,then

$$
h ( s - r ) ~ = ~ k ~ = ~ h ^ { 2 } + 1 .
$$

Since $H _ { l }$ divides $h ^ { 2 } + 1$ and $\hslash ^ { 2 }$ , we find that $h$ must be equal to 1, and thus $k = 2$ , which we have already excluded. So we have arrived at a contradiction, and the proof is complete.

However, the story is not quite over. Iet us rephrase our theorem in the following way: Suppose $G$ is a graph with the property that between any two vertices there is exactly one path of length 2. Clearly, this is an cquivalent formulation of the friendship condition. Our theorem then says that the only such graphs are the windmill graphs. But what if we consider paths of length more than 2? A conjecture of Anton Kotzig asserts that the analogous situation is impossible.

Kotzig's Conjecture. Let $\ell > 2$ . Then there are no finite graphs with the property that between any two vertices there is precisely one path of length k.

Kotzig himself verified his conjecture for $\ell \ \leq \ 8$ . In [3] his conjecture is proved up to $\ell = 2 0$ , and A. Kostochka has told us recently that it is now verified for all $\ell \leq 3 3$ . A gencral proof, however, seems to be out of reach ...

# References

[1] P. ERDÖs, A. RÉNYI & V. SóS: On a problem of graph theory, Studia Sci. Math. 1 (1966), 215-235.   
[2] A. KOTZIG: Regularly $k$ -path conmected graphs, Congressus Numerantium 40 (1983), 137-141.   
[3] A. KosTocHk A: The nonexistence of certain generalized friendship graphs, in: "Combinatorics" (Eger, 1987), Colloq. Math. Soc. János Bolyai 52, North-Holland, Amsterdam 1988, 341-356.

# Probability makes counting (sometimes) easy

# Chapter 35

Just as we started this book with the first papers of Paul Erdós in number theory, we close it by discussing what will possibly be considered his most lasting legacy — the introduction, together with Alfred Rényi, of the probabilistic method. Stated in the simplest way it says:

If, in a given set of objects, the probability that an object does not have a certain property is less than 1, then there must exist an object with this property.

Thus we have an existence result. It may be (and often is) very difficult to find this object, but we know that it exists. We present here thrce examples (of increasing sophistication) of this probabilistic method duc to Erdôs, and end with a particularly elcgant recent application.

As a warm-up, consider a family $\mathcal { F }$ of subsets $A _ { i }$ , all of size $d , \geq 2$ , of a finite ground-set $X$ . We say that $\mathcal { F }$ is 2-colorable if therc exists a coloring of $X$ with two colors such that in every set $A _ { i }$ both colors appear. It is immediate that not every family can be colored in this way. As an example, take all subsets of size $\textit { d }$ of a $( 2 d . - 1 )$ -set $X$ . Then no matter how we 2-color $X$ , there must be $d$ elements which are colored alike. On the other hand, it is equally clear that every subfamily of a 2-colorable family of $d .$ -sets is itself 2-colorable. Hence we are intcrcsted in the smallest number $m = m , ( d )$ for which a family with rn sets exists which is not 2-colorable. Phrased differently, $m ( d )$ is the largest number which guarantees that every family with less than $m ( d )$ sets is 2-colorable.

Theorem 1. Every family of at most $2 ^ { d - 1 }$ $\ c { d } _ { \prime }$ sets is 2-colorable, that is \$m{(d)}>2d-1

Proof. Suppose $\mathcal { F }$ is a family of $d$ -sets with at most $2 ^ { d - 1 }$ sets. Color $X$ randomly with two colors, all colorings being equally likely. For cach set $A \in { \mathcal { F } }$ let $E _ { \varLambda }$ be the event that all elements of $A$ are colored alike. Since there are preciscly two such colorings, we have

$$
\mathrm { P r o b } ( E _ { A } ) = \left( \frac { 1 } { 2 } \right) ^ { d - 1 } ,
$$

and hence with $m = | \mathcal { F } | \leq 2 ^ { d - 1 }$ (note that the events $E _ { \varLambda }$ are not disjoint)

$$
\mathrm { P r o b } ( \bigcup _ { A \in { \mathcal F } } E _ { A } ) < \sum _ { A \in { \mathcal F } } \mathrm { P r o b } ( E _ { A } ) = m \left( \frac { 1 } { 2 } \right) ^ { d - 1 } \ \le \ 1 .
$$

We conclude that there exists some 2-coloring of $X$ without a unicolored $d$ -set from $F$ , and this is just our condition of 2-colorability.

![](images/729c08297430db206ad7e97fc23400ccef46e8f1ab1b6c4cc476c34f7ffb954d.jpg)

![](images/3ffbed3ce98991f654a5c1081a7bf59fe385f0aa3e452ae9958ce62379a0de21.jpg)

An upper bound for $m ( d )$ , roughly equal to $d ^ { 2 }$ , was also established by Erdôs, again using the probabilistic method, this time taking random sets and a fixed coloring. As for exact values, only the first two $m ( 2 ) = 3 .$ . $m ( 3 ) = 7$ are known. Of course, $m ( 2 ) = 3$ is rcalized by the graph $K _ { 3 }$ while the Fano configuration yields $m ( 3 ) \leq 7$ Here $\mathcal { F }$ consists of the seven 3-sets of the figure (including the circle set $\{ 4 , 5 , 6 \} )$ . The rcader may find it fun to show that $\mathcal { F }$ needs 3 colors. To prove that all families of six 3-sets are 2-colorable, and hence $m ( 3 ) = 7$ , requires a little more care.

Our next example is the classic in the field  Ramsey numbers. Consider the complete graph $K _ { N }$ on $N$ vertices. We say that $\bar { k _ { N } }$ has property $( r r , n )$ if, no matter how we color the edges of $\tilde { k _ { N } }$ red and blue, there is always a complete subgraph on  vertices with all edges colored red or a complete subgraph on $n$ vertices with all edges colored blue. It is clear that if $k _ { N }$ has property $( m , n )$ , then so does every $K _ { s }$ with $s \geq N$ . So, as in the first example, wc ask for the smallest number $N$ ( it xists) with this property — and this is the Ramsey number $R ( \mathfrak { n } , \mathfrak { n } )$ .

As a start, we certainly have $R ( m , 2 ) = m$ because either all of the edges of $K _ { m }$ are red or there is a blue edge, resulting in a blue $K _ { 2 }$ . By symmetry, we have ${ \cal R } ( 2 , n . ) = n .$ Now, suppose $R ( m - 1 , n )$ and $R ( m , n - 1 )$ exist. We then prove that $R ( r r , n )$ exists and that

$$
\begin{array} { r } { R ( \tau n , n ) { \bf \Sigma } \le { \cal R } ( m - 1 , n ) { \bf \Sigma } + { \cal R } ( m , n - 1 ) . } \end{array}
$$

Suppose $N = R ( m - 1 , n ) + R ( m , n - 1 )$ , and consider an arbitrary redblue coloring of $k _ { N } ^ { \prime }$ For a vertex $\mathcal { V }$ , let $A$ be the set of vertices joined to $v$ by a red edge, and $B$ the vertices joined by a blue edge.

Since $| A | + | B | = N - 1$ , we find that either $| A | \geq R ( r n - 1 , n )$ or $| B | \ \stackrel { > } { _ - } \ { \cal R } ( \pi , n - 1 )$ . Suppose $| A | \geq R ( m - 1 , n )$ , the other case being analogous. Then by the definition of $R ( r n , - 1 , r \ i )$ , there either exists in $A$ a subset $A _ { R }$ of size $m - 1$ all of whose edges are colored red which together with $\ i$ yields a red $K _ { m }$ , or there is a subset $A _ { B }$ of size $^ { \mathrm { ~ ~ } } n$ with all edges colored blue. We infer that $K _ { N }$ satisfies the $( \gamma \gamma , \eta , )$ -property and Claim (1) follows.

Combining (1) with the starting values $R ( m , 2 ) = m$ and $R ( 2 , \eta ) = \pi$ , we obtain from the familiar recursion for binomial cocfficients

$$
R ( m , n ) ~ \leq ~ { \binom { m + n - 2 } { m - 1 } } ,
$$

and, in particular

$$
R ( k , k ) ~ \leq ~ { \binom { 2 k - 2 } { k - 1 } } ~ = ~ { \binom { 2 k - 3 } { k - 1 } } ~ + ~ { \binom { 2 k - 3 } { k - 2 } } ~ \leq ~ 2 ^ { 2 k - 3 } .
$$

Now what we are really interested in is a lower bound for $R ( k , k )$ .This amounts to proving for an as-large-as-possible $N ~ < ~ R ( k , k )$ that there exists a coloring of the edges such that no red or blue $K _ { k }$ results. And this is where the probabilistic method comes into play.

Theorem 2. For all $k \geq 2$ , the following lower bound holds for the Ramsey numbers:

$$
R ( k , k ) \geq 2 ^ { \frac { k } { 2 } } .
$$

Proof. We have $R ( 2 , 2 ) = 2$ From (2) we know $R ( 3 , 3 ) \leq 6$ , and the pentagon colored as in the figure shows $R ( 3 , 3 ) = 6$ .

Now let us assume $k \geq 4$ Suppose $N < 2 ^ { \frac { k } { 2 } }$ , and consider all red-blue colorings, where we color each edge independently red or blue with probability $\frac { 1 } { 2 }$ Thus all colorings are equally likely with probability $2 ^ { - ( \mathbf { \Sigma } _ { 2 } ^ { N } ) }$ .Let $A$ be a set of vertices of size $k$ The probability of the event $A _ { R }$ that the edges in $A$ are all colored red is then $2 ^ { - \binom { k } { 2 } }$ Hny $p _ { \boldsymbol { \mathscr { k } } }$ for some $k$ -set to be colored all red is bounded by

$$
p _ { R } ~ = ~ \mathsf { P r o b } \bigl ( \bigcup _ { | A | = k } A _ { R } \bigr ) ~ \le ~ \sum _ { | A | = k } \mathsf { P r o b } ( A _ { R } ) ~ = ~ \binom { N } { k } 2 ^ { - \binom { k } { 2 } } .
$$

Now with $N < 2 ^ { \frac { k } { 2 } }$ and $k \geq 4 .$ using $\begin{array} { r } { \binom { N } { k } \leq \frac { N ^ { k } } { 2 ^ { k - 1 } } } \end{array}$ for $k \geq 2$ (scc page 12), we have

$$
{ \binom { N } { k } } 2 ^ { - { \binom { k } { 2 } } } \ \leq \ { \frac { N ^ { k } } { 2 ^ { k - 1 } } } 2 ^ { - { \binom { k } { 2 } } } \ < \ 2 ^ { { \frac { k ^ { 2 } } { 2 } } - { \binom { k } { 2 } } - k + 1 } \ = \ 2 ^ { - { \frac { k } { 2 } } + 1 } \leq { \frac { 1 } { 2 } } .
$$

Hcnce $\ l { j } _ { R } \ < \ \frac { \ l _ { 1 } } { 2 }$ , and by symmetry $p _ { B } ~ < ~ \frac { 1 } { 2 }$ for the probability of some $k$ vertices with all edges between them colored bluc. We conclude that $p _ { R } + p _ { B } < 1$ for $N ^ { ^ { - } } < 2 ^ { \frac { k } { 2 } }$ , so there must be a coloring with no red or blc $K _ { k }$ , which mcans that $K _ { N }$ does not have property $( k , k )$ . □

Of course, there is quite a gap between the lower and the upper bound for $R ( k , k )$ . Still, as simple as this Book Proof is, no lower bound with a better exponent has been found for general $k$ in the more than 50 years since Erds' result. In fact, no one has been able to prove a lower bound of the form $R ( k , k ) > 2 ^ { ( \frac { 1 } { 2 } + \varepsilon ) k }$ nor an upper bound of the form $R ( k , k ) < 2 ^ { ( 2 - \varepsilon ) k }$ for a fixed $\varepsilon > 0$ .

Our third result is another beautiful illustration of the probabilistic method. Consider a graph $G$ on $n$ verticcs and its chromatic number $\chi ( G )$ .If $\chi ( G )$ is high, that is, if we need many colors, then we might suspect that $\vec { G }$ contains a large complete subgraph. However, this is far from the truth. Already in the fourties Blanche Descartes constructed graphs with arbitrarily high chromatic number and no triangles, that is, with every cycle having length at least 4, and so did several others (see the box on the next page).

However, in these examples there were many cycles of length 4. Can we do even better? Can we stipulate that there are no cycles of small length and still have arbitrarily high chromatic number? Yes we can! To make matters precise, let us call the length of a shortest cycle in $G$ the girth $\gamma ( G )$ of $G$ then we have the following theorem, first proved by Paul Erdós.

![](images/12c9dc55ba1e706b8f034817f382f46905ff3ad23ed8ffa92e733f03a1a180ab.jpg)

![](images/0809724baddca07cb2d34b38338a494ab69f08ea9b37d9b80fb51c72e9938e69.jpg)

Constructing the Myciclski graph

# Triangle-free graphs with high chromatic number

Here is a sequence of triangle-free graphs $( \vec { \cal { z } } _ { 3 } , \vec { \cal { G } } _ { 4 } , \dots$ with

$$
\chi ( G _ { \pi } ) = \pi .
$$

Start with $\bar { G } _ { 3 } = C _ { 5 }$ , the 5-cycle; thus $\chi ( G _ { 3 } ) = 3$ Suppose we have already constructed $G _ { n }$ on the vertex set $V$ . The new graph $G _ { n + 1 }$ has the vertex set $V \cup V ^ { \prime } \cup \{ z \}$ , where the vertices $v ^ { \prime } \in V ^ { \prime }$ correspond bijectively to $\because \in V$ , and $z$ is a single other vertex. The edges of $G _ { \pi + 1 }$ fall into 3 classes: First, we take all edges of $G _ { \mathfrak { n } }$ ; secondly every vertex $v ^ { \prime }$ is joined to precisely the neighbors of $\mathcal { V }$ in $G _ { \pi }$ ; thirdly $z$ is joined to all $\chi ^ { \prime } \in V ^ { \prime }$ .Hence from $G _ { 3 } = C _ { 5 }$ we obtain as $G _ { 4 }$ the so-called Mycielski graph.

Clearly, $G _ { n + 1 }$ is again triangle-free. To prove $\chi ( G _ { n + 1 } ) = n + 1$ we use induction on $\hbar$ Take any $n$ -coloring of $G _ { \pi }$ and consider a color class $C$ There must exist a vertex $\nu \in C$ which is adjacent to at least one vertex of every other color class; otherwise we could distribute the vertices of $C$ onto the $n - 1$ other color classes, resulting in $\chi ( G _ { n } ) \leq n - 1$ But now it is clear that $v ^ { \prime }$ (the vertex in $V ^ { r }$ corresponding to $v$ ) must receive the same color as $\textit { \textbf { 2 } }$ in this $n$ -coloring. So, all $n$ colors appear in $V ^ { r }$ , and we need a new color for $z$ .

Theorem 3. For every $k \geq 2$ there exists $a$ graph $G$ with chromatic number $\chi ( G ) > k$ and girth $\gamma ( G ) > k$ .

The strategy is similar to that of the previous proofs: We consider a certain probability space on graphs and go on to show that the probability for $\chi ( G ) \leq k$ is smaller than $\frac 1 2$ , and similarly the probability for $\gamma ( G ) \leq k$ is smaller than $\frac { 1 } { 2 }$ . Consequently, there must exist a graph with the desired properties.

Proof. Let $V = \{ v _ { 1 } , v _ { 2 } , . . . , v _ { n } \}$ be the vertex set, and $p$ a fixed number between 0 and 1, to be carefully chosen later. Our probability space $\vec { \mathcal { G } } ( n , \mu )$ consists of all graphs on $V$ where the individual edges appear with probability $p$ , independently of each other. In other words, we are talking about a Bernoulli experiment where we throw in each edge with probability $p$ As an example, the probability $\operatorname { P r o b } ( K _ { \mathfrak { n } } )$ for the complete graph is $\operatorname { P r o b } ( K _ { n } ) = p ^ { ( \frac { n } { 2 } ) }$ . In general, we have $\operatorname { P r o b } ( H ) = p ^ { m } ( 1 - p ) { \binom { n } { 2 } } - r n$ if the graph $H$ on $V$ has precisely m edges.

Let us first look at the chromatic number $\chi ( G )$ . By $x = x ( G )$ we denote the independence number, that is, the size of a largest independent set in $G$ . Since in a coloring with $\chi = \chi ( \vec { G } )$ colors all color classes are independent (and hence of size $\leq \alpha$ , we infer $\chi \alpha \geq n$ . Therefore if $\alpha$ is small as compared to $n$ , then $\chi$ must be large, which is what we want.

Suppose $2 \leq r \leq n$ The probability that a fixed $\gamma .$ set in $V$ is independent is $( 1 - p ) ^ { ( r ) }$

$$
\begin{array} { r l } { \mathrm { P r o b } ( \alpha \geq r ) ~ \leq ~ \binom { n } { r } \big ( 1 - p \big ) ^ { \binom { r } { 2 } } } \\ { ~ \leq ~ n ^ { r } ( 1 - p ) ^ { \binom { r } { 2 } } ~ = ~ ( n ( 1 - p ) ^ { ~ \frac { r - 1 } { 2 } } ) ^ { r } ~ \leq ~ ( n e ^ { - p ( r - 1 ) / 2 } ) ^ { r } , } \end{array}
$$

since $1 - p \leq e ^ { - p }$ for all $p$

Given any fixed $k > 0$ we now choose $p : = n ^ { - \frac { k } { k + 1 } }$ , and proceed to show that for $n$ large enough,

$$
\mathrm { P r o b } \Big ( \alpha \geq \frac { n } { 2 k } \Big ) < \frac { 1 } { 2 } .
$$

Indeed, since ${ \boldsymbol { \eta } } { \boldsymbol { \cdot } } { \frac { 1 } { k { \mathrm { ~ } } } } { \boldsymbol { \cdot } } { \mathrm { ~ } } { \mathrm { ~ i ~ } }$ grows faster than $\log n$ ,we have $r _ { 2 } \frac { 1 } { k + 1 } \geq 6 k \log \pi$ for large enough $n$ and thus $p \geq 6 k \frac { \log n } { n }$ For $\begin{array} { r l r } { r } & { { } : = } & { \left\lceil \frac { n } { 2 k } \right\rceil } \end{array}$ this gives $m r \geq 3 \log n ,$ , and thus

$$
n \epsilon ^ { - p ( r \cdot 1 ) / 2 } = n e ^ { - \frac { p r } { 2 } } e ^ { \frac { p } { 2 } } \leq n e ^ { - \frac { 3 } { 2 } \log n } e ^ { \frac { 1 } { 2 } } = n ^ { \frac { 1 } { 2 } } e ^ { \frac { 1 } { 2 } } = \left( \frac { \epsilon } { n } \right) ^ { \frac { 1 } { 2 } } ,
$$

which converges to 0 as $n$ goes to infinity. Hence (3) holds for all $n \geq n _ { 1 }$ . Now we look at the second parameter, $\gamma ( G )$ . For the given $k$ we want to show that there are not too many cycles of length $\leq k$ .Let $i$ be between 3 and $k$ , and $A \subseteq V$ a fixed $i$ -set. The number of possible $i$ -cycles on $A$ is clearly the number of cyclic permutations of $A$ divided by 2 (since we may $\textstyle { \frac { ( i - 1 ) ! } { 2 } }$ .The total number of possible $i$ ccles is therefore ${ \binom { n } { i } } { \frac { ( i - 1 ) ! } { 2 } }$ , and every such cycle $C$ appears with probability $p ^ { i }$ .Let $X$ be the random variable which counts the number of cycles of length $\leq k$ . In order to estimate $X$ we use two simple but beautiful tools. The first is linearity of expectation, and the second is Markov's inequality for nonnegative random variables, which says

$$
\operatorname { P r o b } ( X \geq a ) \leq { \frac { E X } { a } } ,
$$

where $E X$ is the expected value of $X$ . See the appendix to Chapter 14 for both tools.

Let $X _ { \zeta } ,$ be the indicator random variable of the cycle $C ^ { \dagger }$ of, say, length $i$ . That is, we set $X _ { C } = 1$ or 0 depending on whether $C$ appears in the graph or not; hence $E X _ { C } \cong p ^ { i }$ .Since $X$ counts the number of all cycles of length $\leq k$ we have $\textstyle X = \sum X _ { \zeta } $ , and hence by linearity

$$
E X = \sum _ { i = 3 } ^ { k } { \binom { n } { i } } { \frac { ( i - 1 ) ! } { 2 } } p ^ { i } = { \frac { 1 } { 2 } } \sum _ { i = 3 } ^ { k } n ^ { i } p ^ { i } \leq { \frac { 1 } { 2 } } ( k - 2 ) n ^ { k } p ^ { k }
$$

where the ast iequalityholds b $n p = n ^ { \frac { 1 } { k - 1 } } \geq 1$ Applying now Markov's inequaliry with $\begin{array} { r } { a = \frac { \pi } { 2 } } \end{array}$ we obtain

$$
\operatorname { P r o b } ( X \geq { \frac { n } { 2 } } ) ~ \leq ~ { \frac { E X } { n / 2 } } ~ \leq ~ ( k - 2 ) { \frac { ( n p ) ^ { k } } { n } } ~ = ~ ( k - 2 ) n ^ { - { \frac { 1 } { k + 1 } } } .
$$

Since the right-hand side goes to 0 with $\boldsymbol { n }$ going to infinity, we infer that $p ( X \geq { \frac { \pi } { 2 } } ) < { \frac { 1 } { 2 } }$ for $r _ { i } \geq r _ { i - 2 }$ .

Now we are almost home. Our analysis tells us that for $\pi \geq \operatorname { I I } \mathrm { a x } \left( \pi _ { 1 } , \pi _ { 2 } \right)$ there exists a graph $H$ on $n _ { e }$ vertices with $\alpha ( H ) < \frac { \pi } { 2 k }$ and fewer than $\frac { \pi } { 2 }$ cycles of length $\leq k$ . Delete one vertex from each of these cycles, and let $G$ be the resulting graph. Then $\gamma ( G ) > k$ holds at any rate. Since $G$ contains more than $\frac { n . } { 2 }$ vertices and satisfies $\begin{array} { r } { \alpha ( G ) \leq \alpha ( H ) < \frac { n } { 2 k } } \end{array}$ , we find

$$
\chi ( G ) ~ \geq ~ { \frac { n / 2 } { \alpha ( G ) } } ~ \geq ~ { \frac { n } { 2 \alpha ( H ) } } ~ > ~ { \frac { n } { n / k } } ~ = ~ k ,
$$

and the proof is finished.

Explicit constructions of graphs with high girth and chromatic number (of hugc sizc) are known. (In contrast, one does not know how to construct red/blue colorings with no large monochromatic cliques, whose existence is given by Theorem 2.) What remains striking about the Erdôs proof is that it proves the existence of relatively small graphs with high chromatic number and girth.

To end our excursion into the probabilistic world let us discuss an important result in geometric graph theory (which again goes back to Paul Erdós) whose stunning Book Proof is of very recent vintage.

Consider a simple graph $\tilde { G } = \tilde { G } ( V , E )$ with $\gamma _ { \ell }$ vertices and m edges. We want to embed $G$ into the plane just as we did for planar graphs. Now, we know from Chapter 11 - as a consequence of Euler's formula — that a simple planar graph $G$ has at most $3 n - 6$ edges. Hence if m is greater than $3 n - 6$ , there must be crossings of edges. The crossing number $\operatorname { c r } ( G )$ is then naturally defined: It is the smallest number of crossings among all drawings of $G$ , where crossings of more than two edges in one point are not allowed. Thus ${ \bf \ddot { r } } ( G ) = 0$ if and only if $G$ is planar.

In such a minimal drawing the following three situations are ruled out:

No edge can cross itself.   
$\bullet$ Edges with a common endvertex cannot cross.   
No two edges cross twice.

X

This is because in either of these cases, we can construct a different drawing of the same graph with fewer crossings, using the operations that are indicated in our figurc. So, from now on wc assume that any drawing observes these rules.

Suppose that $G$ is drawn in the plane with $c r ( G )$ crossings. We can immediately derive a lower bound on the number of crossings. Consider thc following graph $H$ : The vertices of $H$ are those of $G$ together with all crossing points, and the edges are all pieces of the original edges as we go along from crossing point to crossing point.

The new graph $H$ is now plane and simple (this follows from our three assumptions!). The number of vertices in $H$ is $n + \operatorname { c r } ( G )$ and the number of edges is $\mathtt { r r } \iota + \mathsf { 2 c r } ( \vec { \tau } )$ , since every new vertex has degree 4. Invoking the bound on the number of edges for plane graphs we thus find

$$
m + 2 \operatorname { c r } ( G ) ~ \leq ~ 3 ( n + \operatorname { c r } ( G ) ) ~ - ~ 6 ,
$$

that is,

$$
\begin{array} { r } { \mathrm { c r } ( G ) \geq m - 3 n + 6 . } \end{array}
$$

As an example, for the complete graph $K _ { 6 }$ we compute

$$
\mathsf { c r } ( K _ { 6 } ) \geq 1 5 - 1 8 + 6 = 3
$$

and int   w s c.

The bound (4) is good enough when ${ \mathbf { \nabla } } m .$ is linear in $n$ , but when $m$ is larger compared to $n$ , then the picture changes, and this is our theorem.

Theorem 4. Let $G$ be a simple graph with n vertices and m edges, where $m \geq \varOmega$ Then

$$
\operatorname { c r } ( G ) \geq { \frac { 1 } { 6 4 } } { \frac { m ^ { 3 } } { n ^ { 2 } } } .
$$

The history of this result, called the crossing lemma, is quite interesting. It was conjectured by Erds and Guy in 1973 (with $\frac { 1 } { 6 4 }$ replaced by some constant $^ { c }$ ). The first proofs were given by Leighton in 1982 (with $\scriptstyle { \frac { 1 } { | { \boldsymbol { 0 } } | | } }$ instead of $\frac { 1 } { 6 4 }$ ) and independently by Ajtai, Chvátal, Newborn and Szemerédi. The crossing lemma was hardly known (in fact, many people thought of it as a conjecture long after the original proofs), until László Székely demonstrated its usefulness in a beautiful paper, applying it to a variety of hitherto hard geometric extremal problems. The proof which we now present arose from e-mail conversations between Bernard Chazelle, Micha Sharir and Emo Welzl, and it belongs without doubt in The Book.

Proof. Consider a minimal drawing of $\vec { G }$ , and let $p$ be a number between () and 1 (to be chosen later). Now we generate a subgraph of $G$ , by selecting the vertices of $G$ to lie in the subgraph with probability $p$ ,independently from each other. The induced subgraph that we obtain that way will be called $G _ { p }$ .

Let $\gamma _ { l , \eta } , m _ { \bar { \mu } } , X _ { \bar { r } }$ be the random variables counting the number of vertices, of edges, and of crossings in $G _ { \mu }$ Since $\mathbf { c r } ( G ) - m + 3 n \geq 0$ holds by (4) for any graph, we certainly have

$$
E ( X _ { p } - m _ { p } + 3 \eta _ { l p } ) ~ \geq ~ 0 .
$$

Now we proceed to compute the individual expectations $E ( n _ { p } ) , E ( m _ { p } )$ and $E ( X _ { \mathfrak { p } } )$ .Clearly, $E ( \mathfrak { n } _ { \mathfrak { p } } ) = p \mathfrak { n } \mathfrak { z }$ and $E ( \eta \eta _ { \mathfrak { p } } ) = p ^ { 2 } \eta \eta$ , since an edge appears in $G _ { I ^ { \jmath } }$ if and only if both its endvertices do. And finally, ${ \cal E } ( X _ { \bar { t } } ) = p ^ { 4 } \mathrm { c r } ( G )$ since a crossing is present in $G _ { \mu }$ if and only if all four (distinct!) vertices involved are there.

By linearity of expectation we thus find

$$
0 ~ \leq ~ E ( X _ { p } ) ~ - ~ E ( m _ { p } ) ~ + ~ 3 E ( n _ { p } ) ~ = ~ p ^ { 4 } { \mathrm { c r } } ( G ) ~ - ~ p ^ { 2 } m ~ + ~ 3 p n ,
$$

which is

$$
\operatorname { c r } ( G ) ~ \geq ~ { \frac { p ^ { 2 } m - 3 p n } { p ^ { 4 } } } ~ = ~ { \frac { m } { p ^ { 2 } } } - { \frac { 3 n } { p ^ { 3 } } } .
$$

Here comes the punch line: Se $\begin{array} { r } { p : = { \frac { 1 \pi } { \pi } } } \end{array}$ c     - tion), then (5) becomes

$$
\mathsf { c r } ( G ) ~ \geq ~ \frac { 1 } { 6 4 } \left[ \frac { 4 m } { ( n / m ) ^ { 2 } } - \frac { 3 n } { ( n / m ) ^ { 3 } } \right] ~ = ~ \frac { 1 } { 6 4 } \frac { m ^ { 3 } } { n ^ { 2 } } ,
$$

and this is it.

Paul Erdôs would have loved to see this proof.

# References

[1] M. AJTAI, V. CHVÁTAL, M. NEWBORN & E. SZEMERÉDI: CrosSiNg-free subgraphs, Annals of Discrete Math. 12 (1982), 9-12.   
[2] N. ALON & J. SPENCER: The Probabilistic Method, Second edition, Wiley-Interscience 2000.   
[3] P. ErDôs: Some remarks on the theory of graphs, Bulletin Amer. Math. Soc. 53 (1947), 292-294.   
[4] P. ERDós: Graph theory and probability, Canadian J. Math. 11 (1959), 34-38.   
[5] P. ERDÖs: On a combinatorial problem 1, Nordisk Math. Tidskrift 11 (1963), 5-10.   
[6] P. ERDós & R. K. GuY: Crossing number problems, Amer. Math. Monthly 80 (1973), 52-58.   
|7] P. ERDÖs & A. RÉNYI: On the evolution of random graphs, Magyar Tud. Akad. Mat. Kut. Int. Közl. 5 (1960), 17-61.   
|8] T. LEIGHTON: Complexity Issues in VLSI, MIT Press, Cambridge MA 1983.   
[9] L. A. SzÉkELY: Crossing numbers and hard Erdös problems in discrete geometry, Combinatorics, Probability, and Computing 6 (1997), 353-358.