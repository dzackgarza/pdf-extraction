# A First Course in Wvelets with Fourier Analysis

$$
\begin{array} { r } { \begin{array} { c l l } { \Delta \textsf { L B E R T } } & { \Delta \textsf { O G G E S } } \\ { \textsf { R A N C I S } } & { \Delta \textsf { N A R C O W I C } } \end{array} } \end{array}
$$

# A First Course in Wavelets with Fouricr Analysis

# Contents

Preface xi

Acknowledgments xix

# 0 Inner Product Spaces 1

0.1 Motivation 1   
0.2 Definition of Inner Product 1   
0.3 The Spaces $L ^ { 2 }$ and $\scriptstyle { l ^ { 2 } }$ 0.3.1 Definitions 0.3.2 Convergence in $L ^ { 2 }$ versus Uniform Convergence   
0.4 Schwarz and Triangle Inequalities . 10   
0.5 Orthogonality. 12 0.5.1 Definitions and Examples 12 0.5.2 Orthogonal Projections 14 0.5.3 Gram-Schmidt Orthogonalization 19   
0.6 Linear Operators and Their Adjoints . 20 0.6.1 Linear Operators . 20 0.6.2 Adjoints . . 21   
0.7 Least Squares and Linear Predictive Coding 23 0.7.1 Best Fit Line for Data 23 0.7.2 General Least Squares Algorithm . 0.7.3 Linear Predictive Coding 29   
0.8 Exercises 32

# 1 Fourier Series 37

# 1.1 Introduction... 37

1.1.1 Historical Perspective 30 a6   
1.1.2 Signal Analysis .   
1.1.3 Partial Differential Equations . .

# 1.2 Computation of Fourier Series . . . . . . 41

1.2.1 On the Interval $- \pi \leq x \leq \pi$ . . . . 41   
1.2.2 Other Intervals. 43   
1.2.3 Cosine and Sine Expansions . . 45   
1.2.4 Examples .. 49   
1.2.5 The Complex Form of Fourier Series . 57

# 1.3 Convergence Theorems for Fourier Series . . . . . 61

1.3.1 The Riemann-Lebesgue Lemma . . . . 61   
1.3.2 Convergence at a Point of Continuity 63   
1.3.3 Convergence at a Point of Discontinuity 67   
1.3.4 Uniform Convergence 72   
1.3.5 Convergence in the Mean . . 75

1.4 Exercises 82

# 2 The Fourier Transform 91

2.1 Informal Development of the Fourier Transform . . . . . 91

2.1.1 The Fourier Inversion Theorem 91   
2.1.2 Examples . . . 94

2.2 Properties of the Fourier Transform . . . 98

2.2.1 Basic Properties 98   
2.2.2 Fourier Transform of a Convolution . 104   
2.2.3 Adjoint of the Fourier Transform . 107   
2.2.4 Plancherel Formula . .. 107   
2.3.1 Time Invariant Filters .108   
2.3.2 Causality and the Design of Filters . . . .113

2.4 The Sampling Theorem . . 117

2.5 The Uncertainty Principle . . . . 120

2.6 Exercises 125

# 3 Discrete Fourier Analysis . 131

# 3.1 The Discrete Fourier Transform . . . . . 131

3.1.1 Definition of Discrete Fourier Transform . . . . . . .. . 133   
3.1.2 Properties of the Discrete Fourier Transform : . . 134   
3.1.3 The Fast Fourier Transform . .. 136   
3.1.4 The FFT Approximation to the Fourier Transform . . . . 142   
3.1.5 Application—Parameter Identification . 143   
3.1.6 Application—Discretizations of Ordinary   
Differential Equations . . 144

3.2 Discrete Signals . . . . . 145

3.2.1 Time Invariant, Discrete Linear Filters . . . . . . . . . . . 145

3.2.2 $\pmb { z }$ -Transform and Transfer Functions . . . . . . . . . . . . 147

3.3 Exercises . • ..151

# 4 Haar Wavelet Analysis 155

# 4.1 Why Wavelets? 155

4.2 Haar Wavelets 156

4.2.1 The Haar Scaling Function 156   
4.2.2 Basic Properties of the Haar Scaling Function . .. 157   
4.2.3 Basic Properties of the Haar Scaling Function . 161   
4.2.4 The Haar Wavelet .. 162

4.3 Haar Decomposition and Reconstruction Algorithms . . . . . . . 166

4.3.1 Decomposition . 166   
4.3.2 Reconstruction 170   
4.3.3 Filters and Diagrams . .. 177

4.4 Summary 178

4.5 Exercises 180

# 5 Multiresolution Analysis 183

# 5.1 The Multiresolution Framework . . . . . 183

5.1.1 Definition . 183   
5.1.2 The Scaling Relation 187   
5.1.3 The Associated Wavelet and Wavelet Spaces 190   
5.1.4 Decomposition and Reconstruction Formulas:   
A Tale of Two Bases 193   
5.1.5 Summary 195

5.2 Implementing Decomposition and Reconstruction . . . . . . . . . 196

5.2.1 The Decomposition Algorithm 197   
5.2.2 The Reconstruction Algorithm 201   
5.2.3 Processing a Signal . . . 205   
5.3.1 The Scaling Function 208   
5.3.2 Orthogonality via the Fourier Transform. 210   
5.3.3 The Scaling Equation via the Fourier Transform 213   
5.3.4 Iterative Procedure for Constructing the   
Scaling Function. 217

5.4 Exercises 221

# 6 The Daubechies Wavelets 227

6.1 Daubechies's Construction . 227   
6.2 Classification, Moments, and Smoothness 231   
6.3 Computational Issues 235   
6.4 The Scaling Function at Dyadic Points 236   
6.5 Exercises 239

# 7 Other Wavelet Topics 243

7.1 Computational Complexity . . 243

7.1.1 Wavelet Algorithm . . . 243   
7.1.2 Wavelet Packets 244

7.2 Wavelets in Higher Dimensions . . . . .245

7.3 Relating Decomposition and Reconstruction . . . . . . . . . .. . 247

7.3.1 Transfer Function Interpretation . . . ..251 .4 Wavelet Transform . . . . 253

7.4.1 Definition of the Wavelet Transform .254   
7.4.2 Inversion Formula for the Wavelet Transform . . . . . . . 255

Appendix A Technical Matters 261

A.1 Proof of the Fourier Inversion Formula . ... 261

A.2 Rigorous Proof of Theorem 5.17 . . . . 264

A.2.1 Proof of Theorem 5.10 . . 268   
A.2.2 Proof of the Convergence Part of Theorem 5.23 . . . . . . 270

Appendix B Matlab Routines 273

B.1 General Compression Routine . 273   
B.2 Use of MATLAB's FFT Routine for Filtering and Compression . 273   
B.3 Sample Routines Using MATLAB's Wavelet Toolbox 275   
B.4 MATLAB Code for the Algorithms in Section 5.2 276

# Bibliography

# 279

# Index

# Preface

Fourier series and the Fourier transform have been around since the nineteenth century and many research articles and books (at both the graduate and undergraduate levels) have been written about these topics. By contrast, the development of wavelets has been much more recent. While its origins go back many decades, the subject of wavelets has become a popular tool in signal analysis and other areas of applications only within the last two decades or so partly as a result of Ingrid Daubechies's celebrated work on the construction of compactly supported, orthonormal wavelets. Consequently, most of the articles and reference materials on wavelets require a sophisticated mathematical background (a good first-year real analysis course at the graduate level). Our goal with this book is to present many of the essential ideas behind Fourier analysis and wavelets, along with some of their applications to signal analysis, to an audience of advanced undergraduate science, engineering, and mathematics majors. The only prerequisites are a good calculus background and some exposure to linear algebra (a course that covers matrices, vector spaces, linear independence, linear maps, and inner product spaces should suffice). The applications to signal processing are kept elementary, without much use of the technical jargon of the subject, in order for this material to be accessible to a wide audience.

# Fourier Analysis

The basic goal of Fourier series is to take a signal, which will be considered as a function of the time variable $\pmb { t } _ { i }$ , and decompose it into its various frequency components. The basic building blocks are the sine and cosine functions:

$$
\sin ( n t ) \qquad \cos ( n t ) ,
$$

which vibrate at a frequency of $\pmb { n }$ times per $\pmb { 2 \pi }$ interval. As an example, consider the following function:

$$
\begin{array} { r } { f ( t ) = \sin ( t ) + 2 \cos ( 3 t ) + 0 . 3 \sin ( 5 0 t ) . } \end{array}
$$

This function has three components that vibrate at frequency 1 (the sint part), at frequency 3 [the $\mathbf { 2 } \cos ( 3 t )$ part], and at frequency 50 [the $\mathbf { 0 . 3 \ s i n ( 5 0 t ) }$ part]. The graph of $\pmb { f }$ is given in Figure 1.

![](images/d3d9ad422a4f9d09fa40f2be4890f06319b3f26d7cc3f273136d7cd8b4180b80.jpg)  
Figure 1 Plot of $\pmb { f } ( t ) = \sin ( t ) + 2 \cos ( 3 t ) + 0 . 3 \sin ( 5 0 t )$

A common problem in signal analysis is to filter out unwanted noise. The background hiss on a cassette tape is an example of high-frequency (audio) noise that various devices (Dolby filters) try to filter out. In the preceding example, the component, $\mathbf { 0 . 3 \sin ( 5 0 t ) }$ , contributes the high-frequency wiggles to the graph of $\pmb { f }$ in Figure 1. By setting the coefficient 0.3 equal to zero, the resulting function is

$$
\tilde { f } ( t ) = \sin ( t ) + 2 \cos ( 3 t )
$$

whose graph (given in Figure 2) is the same as the one for $\pmb { f }$ but without the high-frequency wiggles.

The preceding example shows that one approach to the problem of filtering out unwanted noise is to express a given signal, ${ f ( t ) }$ ,in terms of sines and cosines:

$$
f ( t ) = \sum _ { n } a _ { n } \cos ( n t ) + b _ { n } \sin ( n t )
$$

and then to eliminate (i.e., set equal to zero) the coefficients (the $a _ { n }$ and $b _ { n }$ ) that correspond to the unwanted frequencies. In the case of the signal $\pmb { f }$ just presented, this process is easy since the signal is already presented as a sum of sines and cosines. Most signals, however, are not presented in this manner. The subject of Fourier series, in part, is the study of how to efficiently decompose a function into a sum of cosine and sine components so that various types of filtering can be accomplished easily.

Another related problem in signal analysis is that of data compression. Imagine that the graph of the signal $\pmb { f } ( t )$ in Figure 1 represents a telephone conversation. The horizontal axis is time, perhaps measured in milliseconds, and the vertical axis represents the electric voltage of a sound signal generated by someone's voice. Suppose this signal is to be digitized and sent via satellite overseas from America to Europe. One naive approach is to sample the signal every millisecond or so and send these data bits across the Atlantic. However, this would result in thousands of data bits per second for just one phone conversation. Since there will be many such conversations between the two continents, the phone company would like to compress this signal into as few digital bits as possible without significantly distorting the signal. A more efficient approach is to express the signal into its Fourier series: $\begin{array} { r } { f ( t ) = \sum _ { n } a _ { n } \cos ( n t ) + b _ { n } \sin ( n t ) } \end{array}$ and then discard those coefficients, $a _ { n }$ and $b _ { n }$ , that are smaller than some tolerance for error. Only those coefficients that are above this tolerance need to be sent across the Atlantic, where the signal can then be reconstructed. For most signals, the number of significant coefficients in its Fourier series is relatively small.

![](images/d5fcce50e9df084432e929f06ad4453ec2c1ff89d041a4bb2e9b471d66e93c7c.jpg)  
Figure 2 Plot of $f ( t ) = \sin ( t ) + 2 \cos ( 3 t )$

# Wavelets

One disadvantage of Fourier series is that its building blocks, sines and cosines, are periodic waves that continue forever. While this approach may be appropriate for filtering or compressing signals that have time-independent wavelike features (as in Figure 1), other signals may have more localized features for which sines and cosines do not model very well. As an example, consider the graph given in Figure 3. This may represent a sound signal with two isolated noisy pops that need to be filtered out. Since these pops are isolated, sines and cosines do not model this signal very well. A different set of building blocks, called wavelets, is designed to model these types of signals. In a rough sense, a wavelet looks like a wave that travels for one or more periods and is nonzero only over a finite interval instead of propagating forever the way sines and cosines do [see Figure 4 for the graph of the Daubechies ( $N = 2 !$ wavelet]. A wavelet can be translated forward or backward in time. It also can be stretched or compressed by scaling to obtain low- and high-frequency wavelets (see Figure 5). Once a wavelet function is constructed, it can be used to filter or compress signals in much the same manner as Fourier series. A given signal is first expressed as a sum of translations and scalings of the wavelet. Then the coefficients corresponding to the unwanted terms are removed or modified.

![](images/e337636e5e7abb452d9b445365bd185bbee09de4e108fb46285468d295134097.jpg)  
Figure 3 Graph of a signal with isolated noise

![](images/78fdd7fd1f4146ff64735351243f9633938a0065bf1bfcb5fc593d4c0d416907.jpg)  
Figure 4 Graph of Daubechies wavelet

![](images/5b0dc35632773714b4da970bf2ca849c7e13589233020407dd301b60eb0d547d.jpg)  
Figure 5 High-frequency Daubechies wavelet

In order to implement efficient algorithms for decomposing a signal into an expansion (either Fourier or wavelet based), the building blocks (sines, cosines or wavelets) should satisfy various properties. One convenient property is orthogonality, which for the sine function states

$$
{ \frac { 1 } { \pi } } \int _ { 0 } ^ { 2 \pi } \sin ( n t ) \sin ( m t ) d t = { \left\{ \begin{array} { l l } { 0 } & { { \mathrm { i f ~ } } n \neq m } \\ { 1 } & { { \mathrm { i f ~ } } n = m . } \end{array} \right. }
$$

The analogous properties hold for the cosine function as well. In addition, $\begin{array} { r } { \int _ { 0 } ^ { 2 \pi } \sin ( n t ) \cos ( m t ) \dot { d t } = 0 } \end{array}$ for all $\textbf { \em n }$ and $_ { \pmb { m } }$ Wehal e that these rhogliy properties result in simple formulas for the Fourier coefficients (the ${ \pmb a } _ { \pmb n }$ and $b _ { n }$ and efficient algorithms (fast Fourier transform) for their computation.

One of the difficult tasks in the construction of a wavelet is to make sure that its translates and rescalings satisfy analogous orthogonality relationships, so that efficient algorithms for the computation of the wavelet coefficients of a given signal can be found. This is why we cannot construct a wavelet simply by truncating a sine or cosine wave by declaring it to be zero outside of one or more of its periods. Such a function, while satisfying the desired support feature of a wavelet, would not satisfy any reasonable orthogonality relationship with its translates and rescales and thus would not be as useful for signal analysis.

# Outline

This text has eight chapters and two appendices. Chapter 0, on inner product spaces, contains the necessary prerequisites for Chapters 1 through 7. The primary inner product space of interest is the space of square integrable functions, which is presented in simplified form without the use of the Lebesgue integral. Depending on the audience, this chapter can be covered at the beginning of a course or can be folded into the course as the need arises. Chapter 1 contains the basics of Fourier series. Several convergence theorems are presented with simplifying hypothesis so that their proofs are manageable. The Fourier transform is presented in Chapter 2. Besides being of interest in its own right, much of this material is used in later chapters on wavelets. An informal proof of the Fourier inversion formula is presented in order to keep the exposition at an elementary level. A formal proof is given in the Appendix A. The discrete Fourier transform and fast Fourier transform are discussed in Chapter 3. This chapter also contains applications to signal analysis and to the identification of the natural vibrating frequency (or sway) of a building.

Wavelets are discussed in Chapters 4 through 7. Our presentation on wavelets starts with the case of the Haar wavelets in Chapter 4. The basic ideas behind a multiresolution analysis and the desired features of wavelets, such as orthogonality, are easy to describe with the explicitly defined Haar wavelets. However, the Haar wavelets are discontinuous and so they are of limited use in signal analysis. The concept of a multiresolution analysis in a general context is presented in Chapter 5. This gives a general framework that generalizes the structure of the wavelet spaces generated by the Haar wavelet. Chapter 6 contains the construction of the Daubechies wavelet, which is continuous and orthogonal. Prescriptions for smoother wavelets are also given. Chapter 7 contains more advanced topics, such as wavelets in higher dimensions and the wavelet transform.

The proofs of most theorems are given in the text. Some of the more technical theorems are discussed in a heuristic manner with complete proofs given in Appendix A. Some of these proofs require more advanced mathematics, such as some exposure to the Lebesgue integral.

MATLAB code that was used to generate figures or to illustrate concepts is found in Appendix B.

This text is not a treatise. The focus of the latter half of the book is on the construction of orthonormal wavelets. Little mention is made of bi-orthogonal wavelets using splines and other tools. There are ample references for these other types of wavelets (see, for example, [5]) and we want to keep the amount of material in this text manageable for a one-semester undergraduate course.

The basics of Fourier analysis and wavelets can be covered in a one semester undergraduate course using the following outline:

Chapter 0, Sections 0.1 through 0.5 (Sections 0.6 and 0.7 on adjoints, least squares, and linear predictive coding are more topical in nature). This material can either be covered first or covered as needed throughout the rest of the course.

# Preface

Chapter 1 (Fourier Series), all sections.   
Chapter 2 (Fourier Transform), all sections except the ones on the adjoint of the Fourier transform, and the proof of the uncertainty principle, which are more topical in nature.   
Chapter 3 (Discrete Fourier Analysis), all sections except the $\pmb { z }$ -transform, which is more topical in nature.   
Chapter 4 (Haar Wavelet Analysis), all sections.   
Chapter 5 (Multiresolution Analysis), all sections.   
Chapter 6 (Daubechies Wavelets), all sections.

# Acknowledgments

This book arose from lecture notes used by both authors for the Fourier Analysis and Wavelets course taught at Texas A&M. The authors would like to thank the many students in these classes that gave critical comments on the manuscript. We would especially like to thank Svenja Lowitzsch and Beng Ong who read the manuscript carefully and corrected many of our mistakes. The authors would also like to thank the editorial staff; in particular, George Lobell, for the kind encouragement during the development of this book. the following reviewers did an excellent job of making suggestions and pointing out errors, William Beckner, University of Texas; Joe Lakey, New Mexico State University; Edward A. Newburg, Rochester Institute of Technology; Oscar Rothaus, Cornell University; and David Weinberg, Texas Tech university. Of course, any mistakes remaining in the book are solely the fault of the authors. We also thank Steven S. Pawlowski and the rest of the staff at Prentice Hall for their professional production of the book. On a personal note, Fran Narcowich would also like to thank his wife Linda for support and encouragement.

# Chapter 0

# Inner Product Spaces

# 0.1 Motivation

For two vectors $\pmb { X } = ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ , $Y = ( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ in $\scriptstyle { \pmb { R } } ^ { 3 }$ , the standard (Euclidean) inner product of $\pmb { X }$ and $\pmb { Y }$ is defined as

$$
\langle X , Y \rangle = x _ { 1 } y _ { 1 } + x _ { 2 } y _ { 2 } + x _ { 3 } y _ { 3 } .
$$

This definition is partly motivated by the desire to measure the length of a vector, which is given by the Pythagorean theorem:

$$
\operatorname { L e n g t h \ o f } X = { \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } } } = { \sqrt { \langle X , X \rangle } } .
$$

The goal of this chapter is to define the concept of an inner product in a more general setting that includes a wide variety of vector spaces. We are especially interested in the inner product defined on vector spaces whose elements are signals (i.e., functions of time).

# 0.2 Definition of Inner Product

The definition of an inner product in $\scriptstyle { \pmb R } ^ { 3 }$ naturally generalizes to $\pmb { R } ^ { n }$ for any dimension $\pmb { n }$ For two vectors $\pmb { X } = ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } )$ ; $Y = ( y _ { 1 } , y _ { 2 } , \cdots , y _ { n } )$ in $\scriptstyle { \pmb { R } } ^ { n }$ , the Euclidean inner product is

$$
\langle X , Y \rangle = \sum _ { j = 1 } ^ { n } x _ { j } y _ { j } .
$$

When we study Fourier series and the Fourier transform, we will use heavily the complex exponential. Thus, we must consider complex vector spaces as well as real ones. The preceding definition of the inner product for $\scriptstyle { { \pmb R } ^ { n } }$ can be modified for vectors in $C ^ { n }$ by conjugating the second factor. Recall that the conjugate of a complex number $z = x + i y$ is defined as ${ \overline { { z } } } = { x } - i { y }$ Note that $z { \overline { { z } } } = x ^ { 2 } + y ^ { 2 }$ , which by definition is $| z | ^ { 2 }$ [the square of the length of $z = x + i y$ regarded as vector in the plane from $( \mathbf { 0 } , \mathbf { 0 } )$ to $( x , y ) ]$ .

If $Z = ( z _ { 1 } , z _ { 2 } , \cdots , z _ { n } ) , W = ( w _ { 1 } , w _ { 2 } , \cdots , w _ { n } )$ are vectors in $c ^ { n }$ , then

$$
\langle Z , W \rangle = \sum _ { j = 1 } ^ { n } z _ { j } { \overline { { w _ { j } } } } .
$$

The purpose of the conjugate is to ensure that the length of a vector in $C ^ { n }$ is real and nonnegative:

$$
\operatorname { L e n g t h } \operatorname { o f } Z = { \sqrt { \langle Z , Z \rangle } } = { \sqrt { \sum _ { j = 1 } ^ { n } z _ { j } { \overline { { z _ { j } } } } } } = { \sqrt { \sum _ { j = 1 } ^ { n } | z _ { j } | ^ { 2 } } } .
$$

The inner products just defined share certain properties. For example, the inner product is bilinear, which implies

$$
\langle X + Y , Z \rangle = \langle X , Z \rangle + \langle Y , Z \rangle \quad { \mathrm { a n d } } \quad \langle X , Y + Z \rangle = \langle X , Y \rangle + \langle X , Z \rangle .
$$

The rest of the properties satisfied by the aforementioned inner products are set down as axioms in the following definition. We shall leave the verification of these axioms for the inner products for $\pmb { R } ^ { n }$ and $C ^ { n }$ as exercises.

DEFINITion 0.1 An inner product on a complex vector space $\pmb { V }$ is a function $\langle \cdot , \cdot \rangle : V \times V  C$ that satisfies the following properties.

Positivity: $\langle v , v \rangle > 0$ for each nonzero $v \in V$ .   
Conjugate symmetry: $\overline { { \langle v , w \rangle } } = \langle w , v \rangle$ for all vectors $\pmb { v }$ and w in $\pmb { V }$ .   
Homogeneity: $\langle c v , w \rangle = c \langle v , w \rangle$ for all vectors $\pmb { v }$ and w in $V$ and scalars $c \in C$ .   
Additivity: $\langle u + v , w \rangle = \langle u , w \rangle + \langle v , w \rangle \ f o r \ a l l \ u , \ v , \ w \in V .$ .

A vector space with an inner product is called an inner product space.

To emphasize the underlying space $V$ , we shall sometimes denote the inner product on $V$ by

$$
\langle \ , \rangle _ { V } .
$$

The preceding definition also serves to define a real inner product on a real vector space except that the scalar $^ { c }$ in the homogeneity property is real and there is no conjugate in the statement of conjugate symmetry.

Note that the second and fourth properties imply bilinearity in the second factor: $\langle u , v + w \rangle = \langle u , v \rangle + \langle u , w \rangle$ .The second and third properties imply that scalars factor out of the second factor with a conjugate:

$$
\langle v , c \dot { w } \rangle = \overline { { \langle c w , v \rangle } } = \overline { { c } } \overline { { \langle w , v \rangle } } = \overline { { c } } \langle v , w \rangle .
$$

The positivity condition means that we can assign the nonzero number, $\| v \| =$ $\sqrt { \langle v , v \rangle }$ , as the length or norm of the vector $\pmb { v }$ The notion of length gives meaning to the distance between two vectors in $V$ , by declaring

$$
{ \mathrm { D i s t a n c e ~ b e t w e e n ~ } } \{ v , w \} = \| v - w \| .
$$

Note that the positivity property of the inner product implies that the only way $\| \pmb { v } - \pmb { w } \| = \pmb { 0 }$ is when $v = w$ This notion of distance also gives meaning to the idea of a convergent sequence $\{ v _ { k } ; k = 1 , 2 , \ldots \}$ namely, we say that

$$
v _ { k } \to v \quad { \mathrm { i f } } \quad \| v _ { k } - v \| \to 0 .
$$

n words, ${ \boldsymbol { v } } _ { \pmb { k } }  { \boldsymbol { v } }$ if the distance between ${ \pmb v } _ { { \pmb k } }$ and $\pmb { v }$ gets small as $\pmb { k }$ gets large.

Here are some further examples of inner products.

# EXAMPLe 0.2

Let $V$ be the space of polynomials $p = a _ { n } x ^ { n } + \cdots + a _ { 1 } x + a _ { 0 } ,$ ,with ${ \pmb a } _ { j } \in C$ . An inner product on $V$ is given as follows: if $p = a _ { 0 } + a _ { 1 } x + \cdots + a _ { n } x ^ { n }$ and $q = b _ { 0 } + b _ { 1 } x + \cdots + b _ { n } x ^ { n }$ , then

$$
\langle p , q \rangle = \sum _ { j = 0 } ^ { n } a _ { j } { \overline { { b _ { j } } } } .
$$

Note that this inner product space looks very much like $C ^ { n + 1 }$ , where we identify a point $( a _ { 0 } , \ldots , a _ { n } ) \in C ^ { n + 1 }$ with $a _ { 0 } + a _ { 1 } x + \cdots + a _ { n } x ^ { n }$ .

# EXaMPle 0.3

Different inner products can be imposed on the same vector space. This example defines an inner product on $C ^ { 2 }$ that is different from the standard Euclidean inner product. Suppose $\boldsymbol { v } = ( v _ { 1 } , v _ { 2 } )$ and $\pmb { w } = ( w _ { 1 } , w _ { 2 } )$ are vectors in $C ^ { 2 }$ .Define

$$
\langle v , w \rangle = ( \overline { { { w _ { 1 } } } } , \overline { { { w _ { 2 } } } } ) \left( \begin{array} { c c } { { 2 } } & { { - i } } \\ { { i } } & { { 3 } } \end{array} \right) \left( \begin{array} { c } { { v _ { 1 } } } \\ { { v _ { 2 } } } \end{array} \right)
$$

There is nothing special about the particular choice of matrix. We can replace the matrix in the preceding equation with any matrix $\pmb { A }$ as long as it is Hermitian symmetric (i.e. $\begin{array} { r } { \overline { { A } } ^ { T } = A ) } \end{array}$ an positive definite (all eigenvalues are positive). These conditions imply that $\pmb { A }$ is invertible. Verification of these properties will be left as exercises.

# 0.3 The Spaces $L ^ { 2 }$ and $l ^ { 2 }$

# 0.3.1 Definitions

The examples in the last section are all finite dimensional (i.e., they contain only a finite number of linearly independent vectors). In this section, we discuss a class of infinite dimensional vector spaces that is particularly useful for analyzing signals. A signal (for example, a sound signal) can be viewed as a function, $f ( t )$ , that indicates the intensity of the signal at time t. Here t varies in an interval $\alpha \leq t \leq b$ that represents the time duration of the signal. Here, $\pmb { a }$ could be $- \infty$ or b could be $+ \infty$ .

We will need to impose a growth restriction on the functions defined on the interval $\alpha \leq t \leq b$ This leads to the following definition.

DefInITioN 0.4 For an interval $a \leq t \leq b$ , the space $L ^ { 2 } ( [ a , b ] )$ is the set of all square integrable functions defined on $\alpha \leq t \leq b$ In other words,

$$
L ^ { 2 } ( [ a , b ] ) = \{ f : [ a , b ]  C ; \int _ { a } ^ { b } | f ( t ) | ^ { 2 } d t < \infty \} .
$$

Functions that are discontinuous are allowed as members of this space. All the examples considered in this book are either continuous or discontinuous at a finite set of points. In this context, the preceding integral can be interpreted in the elementary Riemann sense (the one introduced in freshmen calculus courses). The definition of $L ^ { 2 }$ allows functions whose set of discontinuities is quite large, in which case the Lebesgue integral must be used. The condition $\begin{array} { r } { \int _ { a } ^ { b } | f ( t ) | ^ { 2 } d t < } \end{array}$ $\infty$ physically means that the total energy of the signal is finite (which is a reasonable class of signals to consider).

The space $L ^ { 2 } [ a , b ]$ is infinite dimensional. For example, if ${ \pmb a } = { \pmb 0 }$ and $\pmb { b = 1 }$ , then the set of functions $\{ 1 , \ t , \ t ^ { 2 } , \ t ^ { 3 } \ldots \}$ is linearly independent and belongs to $\pmb { L ^ { 2 } } [ \pmb { 0 } , 1 ]$ The function $f ( t ) = 1 / t$ is an example of a function that does not belong to $\scriptstyle { \cal L } ^ { 2 } [ 0 , 1 ]$ since $\textstyle \int _ { 0 } ^ { 1 } ( 1 / t ) ^ { 2 } d t = \infty$

$L ^ { 2 }$ Inner Product. We now turn our attention to constructing an appropriate inner product on $L ^ { 2 } [ a , b ]$ To motivate the $L ^ { 2 }$ inner product, we discretize the interval $[ a , b ]$ To simplify matters, let ${ \pmb a } = { \bf 0 }$ and $\pmb { b = 1 }$ .Let $\pmb { N }$ be a large positive integer and let $t _ { j } = j / N$ for $1 \leq j \leq N$ If $\pmb { f }$ is continuous, then the values of $\pmb { f }$ on the interval $[ t _ { j } , t _ { j + 1 } )$ can be approximated by $f ( t _ { j } )$ Therefore, $\pmb { f }$ can be approximated by the following vector:

$$
f _ { N } = ( f ( t _ { 1 } ) , f ( t _ { 2 } ) , \ldots , f ( t _ { N } ) ) \in R ^ { N }
$$

as illustrated in Figure 1. As $\pmb { N }$ gets larger, $\pmb { f } _ { N }$ becomes a better approximation to $\pmb { f }$

If $\pmb { f }$ and $\pmb { \mathscr { s } }$ are two signals in $L ^ { 2 } [ 0 , 1 ]$ , then both signals can be discretized as $\pmb { f } _ { N }$ and $\pmb { g } _ { N }$ One possible definition of $\langle f , g \rangle _ { L ^ { 2 } }$ is to examine the ordinary $R ^ { N }$

![](images/7472510f023982de17238f9549af3942b1c24db223ed19a5a234d86448299cde.jpg)  
Figure 1 Approximating a continuous function by discretization

inner product of $\pmb { f } _ { N }$ and $\pmb { g } _ { \pmb { N } }$ as $\pmb { N }$ gets large:

$$
\langle f _ { N } , g _ { N } \rangle _ { R ^ { N } } = \sum _ { j = 1 } ^ { N } f ( t _ { j } ) \overline { { { g ( t _ { j } ) } } } = \sum _ { j = 1 } ^ { N } f ( j / N ) \overline { { { g ( j / N ) } } } .
$$

The trouble with this approach is that as $\pmb { N }$ gets large, the sum on the right typically gets large. A better choice is to consider the averaged inner product:

$$
{ \frac { 1 } { N } } \langle f _ { N } , g _ { N } \rangle _ { R ^ { N } } = \sum _ { j = 1 } ^ { N } f ( j / N ) { \overline { { g ( j / N ) } } } { \frac { 1 } { N } } .
$$

Since $\pmb { f } _ { N }$ and $\pmb { \mathscr { g } } \pmb { N }$ approach $\pmb { f }$ and $\pmb { g }$ as $\pmb { N }$ gets large, a reasonable definition of $\langle f , g \rangle _ { L ^ { 2 } }$ is to take the limit of this averaged inner product as $N \to \infty$ .

The preceding equation can be written as

$$
\frac { 1 } { N } \langle f _ { N } , g _ { N } \rangle _ { R ^ { N } } = \sum _ { j = 1 } ^ { N } f ( t _ { j } ) \overline { { g ( t _ { j } ) } } \Delta t \quad \mathrm { w i t h } \ \Delta t = 1 / N .
$$

The sum on the right is a Riemann sum approximation to $\textstyle \int _ { 0 } ^ { 1 } f ( t ) { \overline { { g ( t ) } } } d t$ over the partition $[ 0 , t _ { 1 } , t _ { 2 } , \ldots , t _ { N } = 1 ]$ of [0, 1]. This approximation gets better as $\pmb { N }$ gets larger. Thus, a reasonable definition of an inner product on $\scriptstyle { L ^ { 2 } [ 0 , 1 ] }$ is $\begin{array} { r } { \langle f , g \rangle = \int _ { 0 } ^ { 1 } f ( t ) \overline { { g ( t ) } } d t } \end{array}$ . This motivation provides the basis for the following definition.

DEFINITIoN 0.5 The $L ^ { 2 }$ inner product on $\scriptstyle { \pmb { L } } ^ { 2 } ( [ a , b ] )$ is defined as

$$
\langle f , g \rangle _ { L ^ { 2 } } = \int _ { a } ^ { b } { \widehat { f ( t ) g ( t ) } } d t \quad f o r \ f , \ g \in L ^ { 2 } ( [ a , b ] ) .
$$

The conjugate symmetry, homogeneity, and bilinearity properties are all easily established for this inner product and we leave them as exercises.

For the positivity condition, i $\textstyle { 0 = \langle f , f \rangle = \int _ { a } ^ { b } | f ( t ) | ^ { 2 } d t }$ and if $\pmb { f }$ is continuous, then $\pmb { f } ( t ) = \pmb { 0 }$ for all t (see Exercise 4). If $\pmb { f } ( t )$ is allowed to be discontinuous at a finite number of points, then we can only conclude that $\pmb { f } ( t ) = \pmb { 0 }$ at all but a finite number of $\pmb { t }$ values. For example, the function

$$
f ( t ) = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } t = 0 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

is not the zero function yet $\begin{array} { r } { \int _ { - 1 } ^ { 1 } | f ( t ) | ^ { 2 } d t = 0 } \end{array}$ However, we stipulate that two elements $\pmb { f }$ and $\pmb { \mathscr { g } }$ in $L ^ { 2 } ( [ a , b ] )$ are equal if $f ( t ) = g ( t )$ for all values $\pmb { t }$ except for a finite number of $\pmb { t }$ -values (or, more generally, a set of measure zero if the Lebesgue integral is used). This is a reasonable definition for the purposes of integration, since $\textstyle \int _ { a } ^ { b } f ( t ) d t = \int _ { a } ^ { b } g ( t ) d t$ for such functions. With this convention. the positivity condition holds.

This notion of equivalence is reasonable from the point of view of signal analysis. The behavior of a signal at one instant in time (say $\pmb { t } = \pmb { 0 }$ is rarelv important. The behavior of a signal over a time interval of positive length is important. Although measure theory and the Lebesgue integral are not used in this text, we digress to discuss this topic just long enough to put the notion of equivalence discussed in the previous paragraph in a broader context. The concept of measure of a set generalizes the congept of length of an interval. The measure of an interval $a < t < b$ is ${ \pmb b - \pmb a }$ The measure of a disjoint union of intervals is the sum of their lengths. So the measure of a finite (or countably infinite) set of points is zero. The measure of a more complicated set can be determined by decomposing it into a limit of sets that are disjoint unions of intervals. Since intervals of length zero have no effect on integration, it is reasonable to expect that if a function $\pmb { f }$ is zero on $\alpha \leq t \leq b$ except on a set of measure zero, then $\textstyle \int _ { a } ^ { b } f ( t ) d t = 0$ The converse is also true: If

$$
0 = \| f \| _ { L ^ { 2 } [ a , b ] } ^ { 2 } = \int _ { a } ^ { b } f ( t ) ^ { 2 } d t ,
$$

then $\pmb { f } ( t ) = \pmb { 0 }$ on $\alpha \leq t \leq b$ except possibly on a set of measure zero. For this reason, it is reasonable to declare that two functions, $\pmb { f }$ and $\pmb { \mathscr { g } }$ , are equivalent on $[ a , b ]$ if $\pmb { f } ( t ) = \pmb { g } ( t )$ for all $\pmb { t }$ in $[ a , b ]$ except possibly for a set of measure zero. This general notion of equivalence includes the definition stated in the previous paragraph (that two functions are equivalent if they agree except at a finite number of points).

The Space $\scriptstyle { l ^ { 2 } }$ . For many applications, the signal is already discrete. For example, the signal from a compact disc player can be represented by a discrete set of numbers that represent the intensity of its sound signal at regular (small) time intervals. In such cases, we represent the signal as a sequence

$X = \dots , x _ { - 1 } , x _ { 0 } , x _ { 1 } , \dots ,$ where each $\pmb { x _ { j } }$ is the numerical value of the signal at the jth time interval $[ t _ { j } , t _ { j + 1 } ]$ . Theoreticallv, the sequence could continue indefinitely (either as $j \to \infty$ or as $j \to - \infty$ or both). In reality, the signal usually stops after some point, which mathematically can be represented by $\pmb { x } _ { j } = \mathbf { 0 }$ for $| j | > N$ for some integer $\pmb { N }$ .

The following definition describes a discrete analogue of $L ^ { 2 }$ .

… DEFINITioN 0.6 The space ${ x _ { i } \in C }$ with $\begin{array} { r } { \sum _ { - \infty } ^ { \infty } | x _ { n } | ^ { 2 } < \infty } \end{array}$ $\imath ^ { 2 }$ is the set of all sequences Thned $X = \dots , x _ { - 1 } , x _ { 0 } , x _ { 1 } ,$ . as

$$
\langle X , Y \rangle _ { l ^ { 2 } } = \sum _ { n = - \infty } ^ { \infty } x _ { n } { \overline { { y _ { n } } } }
$$

for $X = \dots , x _ { - 1 } , x _ { 0 } , x _ { 1 } , \dots ,$ and $Y = \dots , y _ { - 1 } , y _ { 0 } , y _ { 1 } , \dots .$

Verifying that $\langle \cdot , \cdot \rangle$ is an inner product for $\scriptstyle { \pmb { l } } ^ { 2 }$ is relatively easy and will be left to the exercises.

Relative Error. For two signals, $\pmb { f }$ and $\pmb { \mathscr { s } }$ ,the ${ \pmb L } ^ { 2 } .$ norm of their difference, $\| f - g \| _ { L ^ { 2 } }$ , provides one way of measuring how $\pmb { f }$ differs from $\pmb { g }$ However, often the relative error is more meaningful:

$$
{ \mathrm { R e l a t i v e ~ e r r o r } } = { \frac { \| f - g \| _ { L ^ { 2 } } } { \| f \| _ { L ^ { 2 } } } }
$$

(the denominator could also be $\| g \| _ { L ^ { 2 } } )$ . The relative error measures the ${ \pmb L } ^ { 2 }$ -norm of the difference between $\pmb { f }$ and $\pmb { g }$ in relation to the size of $\| f \| _ { L ^ { 2 } }$ . For discrete signals, the $\pmb { l ^ { 2 } }$ -norm is used.

# 0.3.2 Convergence in $L ^ { 2 }$ versus Uniform Convergence

As defined in Section 0.2, a sequence of vectors $\{ v _ { n } ; n = 1 , 2 , \ldots \}$ in an inner product space $\pmb { V }$ is said to converge to the vector ${ \pmb { v } } \in { \pmb { V } }$ provided that ${ \boldsymbol { v } } _ { \pmb { n } }$ is close to $\pmb { v }$ when $\scriptstyle { \pmb { n } }$ is large. Closeness here means that $\| v _ { n } - v \|$ is small. To be more mathematically precise, ${ \pmb v _ { \pmb n } }$ converges to $\pmb { v }$ if $\| v _ { n } - v \| \to 0$ as $\pmb { n }  \infty$ .

In this text, we will often deal with the inner product space $L ^ { 2 } [ \alpha , b ]$ ,and therefore we shall discuss convergence in this space in more detail.

DEfINITION 0.7 A sequence $\pmb { f _ { n } }$ converges to $\pmb { f }$ in $L ^ { 2 } [ a , b ]$ if $\| f _ { n } - f \| _ { L ^ { 2 } } \to 0$ as $\textstyle n \to \infty$ . More precisely, given any tolerance $\epsilon > 0$ , there exists a postive integer $\pmb { N }$ such that if $\pmb { \mathscr { n } } \geq N$ , then $\| f - f _ { n } \| _ { L ^ { 2 } } < \epsilon$ .

Convergence in $L ^ { 2 }$ is sometimes called convergence in the mean. There are two other types of convergence often used with functions.

# DefinitioN 0.8

1. A sequence $\scriptstyle f _ { n }$ converges to $\pmb { f }$ pointwise on the interval $\alpha \leq t \leq b$ if for each $t \in \{ a , b \}$ and each small tolerance $\epsilon > 0$ , there is a positive integer $\pmb { N }$ such that if $\pmb { n } \geq N$ , then $| f _ { n } ( t ) - f ( t ) | < \epsilon$ .

2. A sequence $f _ { n }$ converges to $\pmb { f }$ uniformly on the interval $\alpha \leq t \leq b$ if for each small tolerance $\epsilon > 0$ , there is a positive integer $\pmb { N }$ such that if $\pmb { n } \geq N$ , then $| f _ { n } ( t ) - f ( t ) | < \epsilon$ for all $\alpha \leq t \leq b$ .

For uniform convergence, the $N$ only depends on the size of the tolerance € and not on the point $\pmb { t }$ ,whereas for pointwise convergence, the $N$ is also allowed to depend on the point $\pmb { t }$ .

How do these three types of convergence compare? If ${ f _ { n } }$ uniformly converges to $\pmb { f }$ on $[ a , b ]$ , then the values of $f _ { n }$ are close to the values of $\pmb { f }$ over the entire interval $[ a , b ]$ .For example, Figure 2 illustrates the graphs of two functions that are uniformly close to each other. By contrast, if $f _ { n }$ converges to $\pmb { f }$ pointwise, then for each fixed $\scriptstyle { \mathbf { \pmb { t } } } .$ b $f _ { n } ( t )$ is close to $f ( t )$ for large $\pmb { n }$ However, the rate at which $f _ { n } ( t )$ approaches $\pmb { f } ( t )$ may depend on the point $\pmb { t }$ Thus, a sequence that converges uniformly also must converge pointwise, but not conversely.

![](images/110d3726a387eef024e0ed8fc01bc07bbe06d1fcbccd1114265bbf569b231a9e.jpg)  
Figure 2 Graphs of two functions that are uniformly close

If $f _ { n }$ converges to $\pmb { f }$ in $L ^ { 2 } [ a , b ]$ then on average, ${ f _ { n } }$ is close to $\pmb { f }$ , but for some values $f _ { n } ( t )$ may be far away from $f ( t )$ For example, Figure 3 illustrates two functions that are close in $L ^ { 2 }$ even though some of their function values are not close.

![](images/252c80accf54eca9f8ac0550e0c036333ae3932e94fb72fb2f50c1c4f020b434.jpg)  
Figure 3 Two graphs that are close in ${ \pmb { L } } ^ { 2 }$ but not uniformly close

# EXaMPle 0.9

The sequence of functions $f _ { n } ( t ) = t ^ { n }$ , $n = 1 , 2 , 3 \dots$ converges pointwise to $\pmb { f } ( t ) = \mathbf { 0 }$ on the interval $0 \leq t < 1$ because for any number $0 \leq t < 1$ , $t ^ { n } \to 0$ as $\pmb { n }  \infty$ However, the convergence is not uniform. The rate at which $t ^ { n }$ approaches zero becomes slower as $\pmb { t }$ approaches 1. For example, if $\scriptstyle t = 1 / 2$ and $\epsilon = 0 . 0 0 1$ , then $| t ^ { n } | < \epsilon$ provided that $\pmb { \mathscr { n } } \geq 1 0$ However, if $\pmb { t = 0 . 9 }$ , then $| t ^ { n } |$ is not less than e until $n \geq 6 6$ .

For any fixed number $\tau < 1$ ,then $f _ { n }$ converges uniformly to $\pmb { f } = \pmb { 0 }$ on the interval $[ 0 , r ]$ Indeed, if $0 \leq t \leq r$ , then $| t ^ { n } | \leq r ^ { n }$ .Therefore, as long as $r ^ { n }$ is less than e, $| f _ { n } ( t ) |$ will be less than e for all $\mathbf { 0 } \leq t \leq r$ . In other words, the rate at which $f _ { n }$ approaches zero for all points on the interval $[ 0 , r ]$ is no worse than the rate at which $\pmb { r } ^ { \pmb { n } }$ approaches zero.

We also note that ${ f _ { n } } \to 0$ in $\scriptstyle { L ^ { 2 } [ 0 , 1 ] }$ because

$$
\begin{array}{c} \begin{array} { l l l } { \displaystyle \| f _ { n } \| _ { L ^ { 2 } } ^ { 2 } = \int _ { 0 } ^ { 1 } ( t ^ { n } ) ^ { 2 } d t } \\ { \displaystyle } \\ { \displaystyle } \\ { \displaystyle } \end{array} \qquad = \frac { t ^ { 2 n + 1 } } { 2 n + 1 } \bigg \vert _ { 0 } ^ { 1 }  \\ { \displaystyle } \\ { \displaystyle } \end{array} \qquad = \qquad \begin{array} { r l } { \displaystyle 1 } & { \displaystyle } \\ { \displaystyle } \end{array}
$$

As the following theorem shows, uniform convergence on a finite interval $[ a , b ]$ is a stronger type of convergence than $L ^ { 2 }$ convergence.

THEOrEM 0.10 If a sequence $f _ { n }$ converges uniformly to $\pmb { f }$ as $\textstyle n \to \infty$ on a finite interval $\ a \leq t \leq b$ , then this sequence also converges to $\pmb { f }$ in $L ^ { 2 } [ a , b ]$ . The converse of this statement is not true.

Proof Using the definition of uniform convergence, we can choose, for a given tolerance $\epsilon > 0$ , an integer $\pmb { N }$ such that

$$
| f _ { n } ( t ) - f ( t ) | < \epsilon \quad \mathrm { f o r } \quad n \geq N \quad \mathrm { a n d } \quad a \leq t \leq b .
$$

This inequality implies

$$
\begin{array} { r l } { \displaystyle \| f _ { n } - f \| _ { L ^ { 2 } } ^ { 2 } = \int _ { a } ^ { b } | f _ { n } ( t ) - f ( t ) | ^ { 2 } d t } & { } \\ { \displaystyle \leq \int _ { a } ^ { b } \epsilon ^ { 2 } d t ~ \mathrm { f o r } ~ n \geq N } & { } \\ { \displaystyle } & { = \epsilon ^ { 2 } ( b - a ) . } \end{array}
$$

Therefore, if $\pmb { \mathscr { n } } \geq N$ ,we have $\| f _ { n } - f \| _ { L ^ { 2 } } \leq \epsilon \sqrt { b - a }$ Since $\epsilon$ can be chosen as small as desired, this inequality implies that $f _ { n }$ converges to $\pmb { f }$ in $L ^ { 2 }$ .

To show that the converse is false, consider the following sequence of functions on $\mathbf { 0 } \leq t \leq 1$ :

$$
f _ { n } ( t ) = { \left\{ \begin{array} { l l } { 1 } & { 0 < t \leq 1 / n } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

We leave it to the reader (see Exercise 6) to show that this sequence converges to the zero function in $L ^ { 2 } [ 0 , 1 ]$ but does not converge to zero uniformly on $\mathbf { 0 } \leq t \leq 1$ . $\bullet$

In general, a sequence that converges pointwise does not necessarily converge in $L ^ { 2 }$ However, if the sequence is uniformly bounded by a fixed function in $L ^ { 2 }$ , then pointwise convergence is enough to guarantee convergence in $L ^ { 2 }$ (this is the Lebesgue dominated convergence theorem; see [17]). Further examples illustrating the relationships between these three types of convergence are developed in the Exercises.

# 0.4 Schwarz and Triangle Inequalities

The two most important properties of inner products are the Schwarz and triangle inequalities. The Schwarz inequality states that $| \langle X , Y \rangle | \leq \| X \| \| Y \|$ .In $\pmb { R } ^ { 3 }$ , this inequality follows from the law of cosines:

$$
| \langle X , Y \rangle | = \| X \| \| Y \| | \cos ( \theta ) | \leq \| X \| \| Y \|
$$

where $\pmb \theta$ is the angle between $x$ and $\mathbf { \Delta } _ { \mathbf { Y } }$ . The triangle inequality states that $\| X + Y \| \leq \| X \| + \| Y \|$ .In $\scriptstyle { { \cal R } } ^ { 3 }$ , this inequality follows from Figure 4 which expresses the fact that the shortest distance between two points is a straight line.

![](images/241befa37e196056a653bf1c5c8f1da7ee9fd4de1936f2d66815429fbd944bb2.jpg)  
Figure 4 Triangle inequality

The following theorem states that the Schwarz and triangle inequalities hold for general inner product spaces.

THeOreM 0.11 Suppose $V , \langle \cdot , \cdot \rangle$ is an inner product space (either real or complex). Then for all $X , Y \in V$ ,

Schwarz inequality: $| \langle X , Y \rangle | \leq \| X \| \| Y \|$ . Equality holds if and only if $x$ · and $\pmb { Y }$ are linearly dependent. Moreover, $\langle X , Y \rangle = \| X \| \| Y \|$ if and only if $X$ or $\pmb { Y }$ is a nonnegative multiple of the other. ..

Triangle inequality: $\| X + Y \| \leq \| X \| + \| Y \|$ Equality holds if and only if $X$ or $\pmb { Y }$ is a nonnegative multiple of the other.

# Proof for Real Inner Product Spaces

Assume that one of the vectors, say $\pmb { Y }$ , is nonzero, for otherwise there is nothing to show. Let $\pmb { t }$ be a real variable and consider the following inequality:

$$
\begin{array} { c } { 0 \leq \| X - t Y \| ^ { 2 } = \langle X - t Y , X - t Y \rangle } \\ { = \| X \| ^ { 2 } - 2 t \langle X , Y \rangle + t ^ { 2 } \| Y \| ^ { 2 } . } \end{array}
$$

The right side is a nonnegative quadratic polynomial in $\pmb { t }$ , and so it cannot have two distinct real roots. Therefore, its discriminant (from the quadratic formula) must be nonpositive. In our case, this means

$$
\operatorname { D i s c r i m i n a n t } = 4 | \langle X , Y \rangle | ^ { 2 } - 4 \| X \| ^ { 2 } \| Y \| ^ { 2 } \leq 0 .
$$

Schwarz's inequality follows by rearranging this inequality.

If $\langle X , Y \rangle = \| X \| \| Y \|$ , then the preceding discriminant is zero, which means that the equation $\| \ b { X } - \ b { t Y } \| ^ { 2 } = 0$ has a double real root, $\hat { \pmb { t } } .$ In particular, $X - { \hat { t } } Y = 0$ or $\pmb { X } = \hat { \pmb { t } } \pmb { Y }$ , which implies that $\langle X , Y \rangle = { \hat { t } } \| Y \| ^ { 2 }$ .On the other hand, $\langle X , Y \rangle = \| X \| \| Y \|$ is nonnegative and therefore $\hat { t } \geq 0$ Thus $\pmb { X } = \hat { \pmb { t } } \pmb { Y }$ is a nonnegative multiple of $\pmb { Y }$ , as claimed. The converse (i.e., if $\pmb { X }$ is a nonnegative multiple of $\pmb { Y }$ , then $\langle X , Y \rangle = \| X \| \| Y \| )$ is easy and left to the reader.

# Proof for a Complex Inner Product Space

If $V$ is a complex inner product space, the proof is similar. We let $\phi$ be an argument of $\langle X , Y \rangle$ , which means

$$
\begin{array} { r l } { \cdot } & { { } \langle X , Y \rangle = | \langle X , Y \rangle | e ^ { i \phi } . } \end{array}
$$

Then we consider the following inequality:

$$
\begin{array} { r l } & { 0 \leq \| e ^ { - i \phi } X - t Y \| ^ { 2 } = \langle e ^ { - i \phi } X - t Y , e ^ { - i \phi } X - t Y \rangle } \\ & { \qquad = \| X \| ^ { 2 } - t \left( \langle e ^ { - i \phi } X , Y \rangle + \langle Y , e ^ { - i \phi } X \rangle \right) + t ^ { 2 } \| Y \| ^ { 2 } } \\ & { \qquad = \| X \| ^ { 2 } - t \left( \langle e ^ { - i \phi } X , Y \rangle + \overline { { \langle e ^ { - i \phi } X , Y \rangle } } \right) + t ^ { 2 } \| Y \| ^ { 2 } } \\ & { \qquad = \| X \| ^ { 2 } - 2 \operatorname { R e } \{ t e ^ { - i \phi } \langle X , Y \rangle \} + t ^ { 2 } \| Y \| ^ { 2 } } \end{array}
$$

where ${ \mathfrak { a } } _ { \mathbf { R } \mathbf { e } ^ { \mathfrak { n } } }$ stands for "the real part"; that is, if ${ \boldsymbol { z } } = { \boldsymbol { x } } + i \cdot$ ,then

$$
\mathrm { R e } \ z = x = { \frac { z + { \overline { { z } } } } { 2 } } .
$$

In view of the choice of $\phi$ , the middle term is just $- 2 t | \langle X , Y \rangle |$ and so the term on the right equals the expression on the right side of (0.2). The rest of the argument is now the same as the argument given for the case of a real inner product space.

# Proof of the Triangle Inequality

The proof of the triangle inequality now follows from the Schwarz inequality:

$$
\begin{array} { r l } & { \| X + Y \| ^ { 2 } = \langle X + Y , X + Y \rangle } \\ & { \qquad = \| X \| ^ { 2 } + 2 \mathrm { { R e } } \left\{ \langle X , Y \rangle \right\} + \| Y \| ^ { 2 } } \\ & { \qquad \leq \| X \| ^ { 2 } + 2 \| X \| \| Y \| + \| Y \| ^ { 2 } \quad \mathrm { { b y } ~ S c h w a r z } } \\ & { \qquad = \left( \| X \| + \| Y \| \right) ^ { 2 } . } \end{array}
$$

Taking square roots of both sides of this inequality establishes the triangle inequality.

If the preceding inequality becomes an equality, then $\langle X , Y \rangle = \| X \| \| Y \|$ and the first part of the theorem implies that either $x$ or $\pmb { Y }$ is a nonnegative multiple of the other, as claimed. $\bullet$

# 0.5 Orthogonality

# 0.5.1 Definitions and Examples

For the standard inner product in $\scriptstyle { \pmb { R } } ^ { 3 }$ , the law of cosines is

$$
\langle X , Y \rangle = \| X \| \| Y \| \cos ( \theta ) , \quad \theta = \mathrm { a n g l e } \mathrm { \bf ~ k }
$$

which implies that $\pmb { X }$ and $\pmb { Y }$ are orthogonal (perpendicular) if and only if $\langle X , Y \rangle = \mathbf { 0 }$ We shall make this equation the definition of orthogonality in general.

DEFINITiION 0.12 Suppose $V$ is an inner product space.

The vectors $\pmb { X }$ and $\pmb { Y }$ in $V$ are said to be orthogonal if $\langle X , Y \rangle = 0$ . The collection of vectors $e _ { i }$ , ${ \dot { \mathfrak { z } } } = 1 , \dots , N$ , is said to be orthonormal if each $e _ { i }$ has unit length, $\| e _ { i } \| = 1$ , and $e _ { i }$ and $e _ { j }$ are orthogonal for $i \neq j$ . Two subspaces $V _ { 1 }$ and $V _ { 2 }$ of $\pmb { V }$ are said to be orthogonal if each vector in $V _ { 1 }$ is orthogonal to every vector in $V _ { 2 }$ .

An orthonormal basis or orthonormal system for $\boldsymbol { V }$ is a basis of vectors for $\boldsymbol { v }$ that is orthonormal.

# EXAMPLe 0.13

The line ${ \boldsymbol { y } } = { \boldsymbol { x } }$ generated by the vector $( 1 , 1 )$ is orthogonal to the line $\pmb { y } = - \pmb { x }$ generated by $( \mathbf { 1 } , - \mathbf { 1 } )$ .

# EXAMPLE 0.14

The line $x / 2 = - y = z / 3$ in $\scriptstyle { \pmb { R } } ^ { 3 }$ , which points in the direction of the vector .. $( 2 , - 1 , 3 )$ , is orthogonal to the plane $2 x - y + 3 z = 0$ . :

# EXAMPLe 0.15

For the space $L ^ { 2 } ( [ 0 , 1 ] )$ , any two functions where the first function is zero on the set where the second is nonzero will be orthogonal. For example, if $f ( t )$ is nonzero only on the interval $0 \leq t < 1 / 2$ and $\pmb { g } ( t )$ is nonzero only on the interval $1 / 2 \leq t < 1$ , then $f ( t ) \overline { { g ( t ) } }$ is always zero. Therefore, $\begin{array} { r } { \langle f , g \rangle = \int _ { 0 } ^ { 1 } f ( t ) \overline { { g ( t ) } } d t = 0 , } \end{array}$ .

# EXAMPLE 0.16

Let

$$
\phi ( t ) = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f ~ } 0 \leq t < 1 } \\ { 0 , } & { \mathrm { o t h e r w i s e } } \end{array} \right. \quad \quad \psi ( t ) = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f ~ } 0 \leq t < 1 / 2 } \\ { - 1 , } & { \mathrm { i f ~ } 1 / 2 \leq t < 1 } \\ { 0 , } & { \mathrm { o t h e r w i s e . } } \end{array} \right.
$$

Then $\phi$ and $\psi$ are orthogonal in $\scriptstyle { L ^ { 2 } [ 0 , 1 ] }$ because

$$
\langle \phi , \psi \rangle = \int _ { 0 } ^ { 1 / 2 } 1 d t - \int _ { 1 / 2 } ^ { 1 } 1 d t = 0 .
$$

In contrast to the previous example, note that $\phi$ and $\psi$ are orthogonal and yet $\phi$ and $\psi$ are nonzero on the same set, namely the interval $0 \leq t \leq 1$ The function $\phi$ is called the scaling function and the function $\psi$ is called the wavelet function for the Haar system. We shall revisit these functions in the later chapters on wavelets.

# EXAMPLE 0.17

The function $f ( t ) = \sin { t }$ and $g ( t ) = \cos t$ are orthogonal in $L ^ { 2 } ( [ - \pi , \pi ] )$ , because

$$
\begin{array} { l } { \displaystyle { \langle f , g \rangle = \int _ { - \pi } ^ { \pi } \sin ( t ) \cos ( t ) d t } } \\ { \displaystyle { \quad = \frac { 1 } { 2 } \int _ { - \pi } ^ { \pi } \sin ( 2 t ) d t } } \\ { \displaystyle { \quad = \frac { - 1 } { 4 } \cos ( 2 t ) \Big | _ { - \pi } ^ { \pi } } } \\ { \displaystyle { \quad = 0 . } } \end{array}
$$

Since $\begin{array} { r } { \int _ { - \pi } ^ { \pi } \sin ^ { 2 } ( t ) d t = \int _ { - \pi } ^ { \pi } \cos ^ { 2 } ( t ) d t = \pi , } \end{array}$ ,the functions $\frac { \sin ( t ) } { \sqrt { \pi } }$ and $\frac { \cos ( t ) } { \sqrt { \pi } }$ are orthonormal in $L ^ { 2 } ( [ - \pi , \pi ] )$ . More generally, we shall show in Chapter 1 that the functions

$$
{ \frac { \cos n t } { \sqrt { \pi } } } , { \frac { \sin ( n t ) } { \sqrt { \pi } } } , n = 1 , 2 , \ldots
$$

are orthonormal. This fact will be very important in our development of Fourier series.

Vectors can be expanded easily in terms of an orthonormal basis, as the following theorem shows.

THEOREM 0.18 Suppose $V _ { 0 }$ is a subspace of an inner product space $V$ .Suppose $\{ e _ { 1 } , . . . e _ { N } \}$ is an orthonormal basis for $V _ { 0 }$ .If $\boldsymbol { v } \in V _ { 0 }$ , then

$$
\boldsymbol { v } = \sum _ { j = 1 } ^ { N } \langle \boldsymbol { v } , \mathcal { C } _ { j } \rangle \boldsymbol { e } _ { j } .
$$

Proof Since $\{ e _ { 1 } , \ldots , e _ { N } \}$ is a basis for $V _ { 0 }$ , any vector $v \in V _ { 0 }$ can be uniquely expressed as a linear combination o the $e _ { j }$ .

$$
v = \sum _ { j = 1 } ^ { N } \alpha _ { j } e _ { j } . \qquad .
$$

To evaluate the constant $\alpha _ { k }$ , take the inner product of both sides with $\scriptstyle e _ { k }$ :

$$
\langle v , e _ { k } \rangle = \sum _ { j = 1 } ^ { N } \langle \alpha _ { j } e _ { j } , e _ { k } \rangle .
$$

The only nonzero term on the right occurs when ${ \dot { \pmb { \jmath } } } = { \pmb { k } }$ since the $\boldsymbol { e } _ { j }$ are orthonormal. Therefore,

$$
\langle v , e _ { k } \rangle = \alpha _ { k } \langle e _ { k } , e _ { k } \rangle = \alpha _ { k } .
$$

Thus, $\alpha _ { k } = \langle v , e _ { k } \rangle$ , as desired.

# 0.5.2 Orthogonal Projections

Suppose $\{ e _ { 1 } , . . . e _ { N } \}$ is an orthonormal collection of vectors in an inner product space $\pmb { V }$ .If $_ v$ lies in the span of $\{ e _ { 1 } , . . . e _ { N } \}$ , then, as Theorem 0.18 demonstrates, the equation

$$
\pmb { v } = \sum _ { j = 1 } ^ { N } \alpha _ { j } \pmb { e } _ { j }
$$

is satisfied with $\alpha _ { i } = \langle v , e _ { j } \rangle$ . If $\pmb { v }$ does not lie in the linear span of $\{ e _ { 1 } , . . . e _ { N } \}$ then solving (0.3) for $\pmb { \alpha } _ { j }$ is impossible. In this case, the best we can do is to determine the vector ${ \pmb v } _ { \mathbf { 0 } }$ belonging to the linear span of $\{ e _ { 1 } , . . . e _ { N } \}$ that comes as close as possible to $\pmb { v }$ More generally, suppose $V _ { 0 }$ is a subspace of the inner product space $\boldsymbol { v }$ and suppose ${ \boldsymbol { v } } \in \cdot { \boldsymbol { V } }$ is a vector that is not in $V _ { 0 }$ (see Figure 5). How can we determine the vector $v _ { 0 } \in V _ { 0 }$ that is closest to ${ \pmb v } \pmb { \ ? }$ This vector $( v _ { 0 } )$ has a special name in the following definition.

DEFINITIoN 0.19 Suppose $V _ { 0 }$ is a finite dimensional subspace of an inner product space $V$ .For any vector $v \in V$ , the orthogonal projection of $\pmb { v }$ onto $V _ { 0 }$ is the unique vector $v _ { 0 } \in V _ { 0 }$ that is closest to $\pmb { v }$ ; that is,

$$
\| v - v _ { 0 } \| = \operatorname* { m i n } _ { w \in V _ { 0 } } \| v - w \| .
$$

![](images/730a3e31c38603c9d710cad61f7832feeca5e6b1cbf7730817c58ab0c912d426.jpg)  
Figure 5 Orthogonal projection of $\pmb { v }$ onto $V _ { 0 }$

As Figure 5 indicates, the vector ${ \pmb v } _ { \pmb 0 }$ , which is closest to $\pmb { v }$ , must be chosen so that $\pmb { v } - \pmb { v _ { 0 } }$ (the vector from ${ \pmb v _ { 0 } }$ to $\pmb { v }$ ) is orthogonal to $V _ { 0 }$ .Of course, figures are easily drawn when the underlying vector space is $R ^ { 2 }$ or $\pmb { R } ^ { 3 }$ In a more complicated inner product space, such as ${ \pmb L } ^ { 2 }$ , figures are an abstraction, which may or may not be accurate (e.g., an element in $L ^ { 2 }$ is not really an a point in the plane as in Figure 5). The following theorem states that our intuition in $\scriptstyle { \mathcal { R } } ^ { 2 }$ . regarding orthogonality is accurate in a general inner product space.

TheOreM 0.20 Suppose $V _ { 0 }$ is a finite dimensional subspace of an inner product space $\boldsymbol { v }$ , Let v be any element in $\pmb { V }$ .Then its orthogonal projection, ${ \boldsymbol { v } } _ { 0 }$ , has the following property: $\boldsymbol { v } - \boldsymbol { v _ { 0 } }$ is orthogonal to every vector in $V _ { 0 }$ .

Proof We first show that if ${ \mathfrak { v } } _ { 0 }$ is the closest vector to ${ \pmb v } .$ ,then $\boldsymbol { v } - \boldsymbol { v _ { 0 } }$ is orthogonal to every vector $w \in V _ { 0 }$ Consider the function

$$
f ( t ) = \| v _ { 0 } + t w - v \| ^ { 2 } \quad t \in R ,
$$

which describes the square of the distance between $v _ { 0 } + t w \in V _ { 0 }$ and ${ \pmb v }$ If ${ \pmb v _ { 0 } }$ is the closest element of $V _ { 0 }$ to ${ \pmb v }$ , then $\pmb { f }$ is minimized when $\pmb { t = 0 }$ For simplicity, we will consider the case where the underlying inner product space $\pmb { V }$ is real. Expanding $\pmb { f }$ , we have

$$
\begin{array} { c } { f ( t ) = \langle \left( \upsilon _ { 0 } - \upsilon \right) + t \upsilon , \left( \upsilon _ { 0 } - \upsilon \right) + t \upsilon \rangle } \\ { = \| \upsilon _ { 0 } - \upsilon \| ^ { 2 } + 2 t \langle \upsilon _ { 0 } - \upsilon , \upsilon \rangle + t ^ { 2 } \| \upsilon \| ^ { 2 } . } \end{array}
$$

Since $\pmb { f }$ is minimized when $\pmb { t = 0 }$ , its derivative at $\pmb { t = 0 }$ must be zero. We have

$$
f ^ { \prime } ( t ) = 2 \langle v _ { 0 } - v , w \rangle + 2 t \| w \| ^ { 2 } .
$$

So

$$
0 = f ^ { \prime } ( 0 ) = 2 \langle v _ { 0 } - v , w \rangle
$$

and we conclude that ${ \boldsymbol { v } } _ { 0 } - { \boldsymbol { v } }$ is orthogonal to $\pmb { w }$ .

The converse also holds: If ${ \boldsymbol { v } } _ { 0 } - { \boldsymbol { v } }$ is orthogonal to $\pmb { w }$ ,then from (0.4), ${ f ^ { \prime } } ( 0 ) = 0$ Since $\pmb { f } ( t )$ is a nonnegative quadratic polynomial in $\pmb { t }$ this critical point ${ \pmb t = 0 }$ must correspond to a minimum. Therefore, $\| v _ { 0 } + t w - v \| ^ { 2 }$ is minimized when $\pmb { t = 0 }$ Since $\pmb { w }$ is an arbitrarily chosen vector in $V _ { 0 }$ , we conclude that ${ \pmb v _ { 0 } }$ is the closest vector in $V _ { 0 }$ to $\pmb { v }$ . $\bullet$

In terms of an orthonormal basis for $V _ { 0 }$ , the projection of a vector $\pmb { v }$ onto $V _ { 0 }$ is easy to compute, as the following theorem states.

THeOREM 0.21 Suppose $V$ is an inner product space and $V _ { 0 }$ is an $\pmb { N }$ -dimensional subspace with orthonormal basis $\{ e _ { 1 } , e _ { 2 } , \dots e _ { N } \}$ . The orthogonal projection of a vector $v \in V$ onto $V _ { 0 }$ is given by

$$
v _ { 0 } = \sum _ { j = 1 } ^ { N } \alpha _ { j } e _ { j } \quad \mathrm { w i t h } \quad \alpha _ { j } = \langle v , e _ { j } \rangle .
$$

Note. In the special case that $\pmb { v }$ belongs to $V _ { 0 }$ , then $\pmb { v }$ equals its orthogonal projection, ${ \boldsymbol { v } } _ { \mathbf { 0 } }$ In this case, the preceding formula for ${ \boldsymbol { v } } _ { 0 } = { \boldsymbol { v } }$ is the same as the one given in Theorem 0.18.

Proof Let $\begin{array} { r } { v _ { 0 } = \sum _ { j = 1 } ^ { N } \alpha _ { j } e _ { j } } \end{array}$ with $\alpha _ { j } = \langle v , e _ { j } \rangle$ In view of Theorem 0.20 we must show that $\pmb { v } - \pmb { v _ { 0 } }$ is orthogonal to any vector $w \in V _ { 0 }$ Since $e _ { 1 } , \ldots e _ { N }$ is a basis for $V _ { 0 }$ , it suffices to show that $v - v _ { 0 }$ is orthogonal to each $\scriptstyle { e _ { k } }$ , ${ \pmb k } = 1 , \ldots , { \pmb N }$ . We have

$$
\langle v - v _ { 0 } , e _ { k } \rangle = \langle v - \sum _ { j = 1 } ^ { N } \alpha _ { j } e _ { j } , e _ { k } \rangle .
$$

Since $e _ { 1 } , \ldots , e _ { N }$ are orthonormal, the only contributing term to the sum is when ${ \dot { \pmb { \jmath } } } = { \pmb { k } }$

$$
\begin{array} { r l } & { \langle v - v _ { 0 } , e _ { k } \rangle = \langle v , e _ { k } \rangle - \alpha _ { k } \langle e _ { k } , e _ { k } \rangle } \\ & { \qquad = \langle v , e _ { k } \rangle - \alpha _ { k } \quad \mathrm { s i n c e } \ \| e _ { k } \| = 1 } \\ & { \qquad = 0 \quad \mathrm { s i n c e } \ \alpha _ { k } = \langle v , e _ { k } \rangle . } \end{array}
$$

Thus. $\boldsymbol { v } - \boldsymbol { v } _ { 0 }$ is orthogonal to each $\scriptstyle \mathbf { e } _ { k }$ and hence to all of $V _ { 0 }$ , as desired.

# EXAMPLE 0.22

Let $V _ { 0 }$ be the space spanned by $\cos x$ and $\sin x$ in $L ^ { 2 } ( [ - \pi , \pi ] )$ .As computed in Example 0.17, the functions

$$
e _ { 1 } = { \frac { \cos x } { \sqrt { \pi } } } \quad { \mathrm { a n d } } \quad e _ { 2 } = { \frac { \sin x } { \sqrt { \pi } } } \quad
$$

are orthonormal in $L ^ { 2 } ( [ - \pi , \pi ] )$ .Let $\pmb { f } ( \pmb { x } ) = \pmb { x }$ The projection of $\pmb { f }$ onto $V _ { 0 }$ is given by

$$
f _ { 0 } = \langle f , e _ { 1 } \rangle e _ { 1 } + \langle f , e _ { 2 } \rangle e _ { 2 } .
$$

Now, $f ( x ) \cos ( x ) = x \cos ( x )$ is odd and so $\begin{array} { r } { \langle f , e _ { 1 } \rangle = \frac { 1 } { \sqrt { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \cos ( x ) d x = 0 . } \end{array}$ For the other term,

$$
\begin{array} { l l l } { \displaystyle \langle f , e _ { 2 } \rangle = \frac { 1 } { \sqrt { \pi } } \int _ { - \pi } ^ { \pi } x \sin ( x ) d x } \\ { \displaystyle = 2 \sqrt { \pi } \quad [ \mathrm { i n t e g r a t e ~ b y ~ p a r t s . } ] } \end{array}
$$

Therefore, the projection of $\pmb { f } ( \pmb { x } ) = \pmb { x }$ onto $V _ { 0 }$ is given by

$$
f _ { 0 } = \langle f , e _ { 2 } \rangle e _ { 2 } = 2 { \sqrt { \pi } } { \frac { \sin x } { \sqrt { \pi } } } = 2 \sin ( x ) .
$$

# EXAMPLE 0.23

Consider the space $V _ { 1 }$ that is spanned by $\phi ( { \pmb x } ) = { \bf 1 }$ on $\mathbf { 0 } \leq x < 1$ and

$$
\psi ( x ) = \left\{ { \begin{array} { l l } { 1 , } & { 0 \leq x < 1 / 2 } \\ { - 1 , } & { 1 / 2 \leq x < 1 . } \end{array} } \right. .
$$

The functions $\phi$ and $\psi$ are the Haar scaling function and wavelet function mentioned earlier. These two functions are orthonormal in $L ^ { 2 } ( [ 0 , 1 ] )$ . Let $\pmb { f } ( \pmb { x } ) = \pmb { x }$ . As you can check,

$$
\langle f , \phi \rangle = \int _ { 0 } ^ { 1 } x d x = 1 / 2
$$

and

$$
\langle f , \psi \rangle = \int _ { 0 } ^ { 1 / 2 } x d x - \int _ { 1 / 2 } ^ { 1 } x d x = - 1 / 4 .
$$

So the orthogonal projection of the function $\pmb { f }$ onto $V _ { 1 }$ is given by

$$
f _ { 0 } = \langle f , \phi \rangle \dot { \phi } + \langle \dot { f } , \psi \rangle \psi = \phi / 2 - \psi / 4 = \left\{ 1 / 4 , \ : \ : 0 \leq x < 1 / 2 \right.
$$

The set of vectors that are orthogonal to a given subspace has a special name.

DEFInITIoN 0.24 Suppose $V _ { 0 }$ is a subspace of an inner product space $\pmb { V }$ .The orthogonal complement of $V _ { \mathbf { 0 } }$ , denoted $\pmb { V _ { \alpha } ^ { \perp } }$ , is the set of all vectors in $V$ that are orthogonal to $V _ { 0 }$ ; that is,

$$
V _ { 0 } ^ { \perp } = \{ v \in V ; ~ \langle v , w \rangle = 0 ~ f o r ~ e v e r y ~ w \in V _ { 0 } \} .
$$

![](images/d627961fab62c2a8b3d74006d3c5599e6069b979aacea7ccaf58c305f07760cc.jpg)  
Figure 6 $V = V _ { 0 } \oplus V _ { 0 } ^ { \perp }$ ${ \pmb v } = { \pmb v } _ { 0 } + { \pmb v } _ { 1 }$ with ${ \boldsymbol { v _ { 0 } } } \in V _ { 0 }$ $v _ { 1 } \in V _ { 0 } ^ { \bot }$

As Figure 6 indicates, each vector can be written as a sum of a vector in $V _ { 0 }$ and a vector in $V _ { 0 } ^ { \perp }$ .The intuition from this Euclidean figure is accurate for more general inner product spaces, as the following theorem demonstrates.

THEOREM 0.25 Suppose $V _ { 0 }$ is a finite dimensional subspace of an inner product space $\boldsymbol { v }$ Each vector $v \in V$ can be written uniquely as $\pmb { v } = \pmb { v _ { 0 } } + \pmb { v _ { 1 } }$ ,where ${ \boldsymbol { v } } _ { \mathbf { 0 } }$ belongs to $V _ { 0 }$ and ${ \pmb v } _ { \mathbf { 1 } }$ belongs to $V _ { 0 } ^ { \perp }$ ; that is,

$$
V = V _ { 0 } \oplus V _ { 0 } ^ { \perp } .
$$

Proof Suppose $\pmb { v }$ belongs to $\pmb { V }$ and let ${ \pmb v _ { 0 } }$ be its orthogonal projection onto $V _ { 0 }$ .Let $v _ { 1 } = v - v _ { 0 }$ ;then

$$
\begin{array} { r } { v = v _ { 0 } + ( v - v _ { 0 } ) = v _ { 0 } + v _ { 1 } . } \end{array}
$$

By Theorem 0.20, ${ \pmb v } _ { 1 }$ is orthogonal to every vector in $V _ { 0 }$ Therefore, ${ \pmb v } _ { 1 }$ belongs to $V _ { 0 } ^ { \perp }$ . $\bullet$

# EXaMpLe 0.26

Consider the plane $V _ { 0 } = \{ 2 x - y + 3 z = 0 \}$ .The set of vectors

$$
\left\{ e _ { 1 } = \frac { 1 } { \sqrt { 2 1 } } ( 1 , - 4 , - 2 ) \quad \mathrm { a n d } \quad e _ { 2 } = \frac { 1 } { \sqrt { 6 } } ( 2 , 1 , - 1 ) \right\}
$$

forms an orthonormal basis for $V _ { 0 }$ .So given ${ \pmb v } = ( { \pmb x } , y , z ) \in R ^ { 3 }$ , the vector

$$
\begin{array} { l } { { v _ { 0 } = \langle v , e _ { 1 } \rangle e _ { 1 } + \langle v , e _ { 2 } \rangle e _ { 2 } } } \\ { { \ = \left( \frac { x - 4 y - 2 z } { 2 1 } \right) ( 1 , - 4 , - 2 ) + \left( \frac { 2 x + y - z } { 6 } \right) ( 2 , 1 , - 1 ) } } \end{array}
$$

is the orthogonal projection of $^ { v }$ onto the plane $V _ { 0 }$ .

The vector $e _ { 3 } = ( 2 , - 1 , 3 ) / \sqrt { 1 4 }$ is a unit vector that is perpendicular to this plane. So

$$
v _ { 1 } = \langle v , e _ { 3 } \rangle e _ { 3 } = \frac { ( 2 x - y + 3 z ) } { 1 4 } ( 2 , - 1 , 3 )
$$

is the orthogonal projection of ${ \pmb v } = ( { \pmb x } , { \pmb y } , z )$ onto $V _ { 0 } ^ { \perp }$ .

The theorems in this section are valid for certain infinite dimensional subspaces, but a discussion of infinite dimensions involves more advanced ideas from functional analysis (see [18]).

# 0.5.3 Gram-Schmidt Orthogonalization

Theorems 0.18 and 0.21 indicate the importance of finding an orthonormal basis. Without an orthonormal basis, the computation of an orthogonal projection onto a subspace is much more difficult. If an orthonormal basis is not readily available, then the Gram-Schmidt orthogonalization procedure describes a way to construct one for a given subspace.

THEOREM 0.27 Suppose $V _ { 0 }$ is a subspace of dimension $\dot { N }$ of an inner product space $\pmb { V }$ .Let ${ \boldsymbol { v } } _ { j }$ , ${ \mathfrak { j } } = 1 , \ldots , N$ be a basis for $V _ { 0 }$ . Then there is an orthonormal basis $\{ e _ { 1 } , . . . , e _ { N } \}$ for $V _ { 0 }$ such that each $\boldsymbol { e } _ { j }$ is a linear combination of $v _ { 1 } , \dotsc , v _ { j }$ .

Proof We first define $\boldsymbol { e } _ { 1 } = v _ { 1 } / \| v _ { 1 } \|$ Clearly, ${ e _ { 1 } }$ has unit length. Let ${ \pmb v _ { 0 } }$ be the orthogonal projection of $v _ { 2 }$ onto the line spanned by ${ e \mathbf { 1 } }$ From Theorem 0.21,

$$
v _ { 0 } = \langle v _ { 2 } , e _ { 1 } \rangle e _ { 1 } .
$$

Figure 7 suggests that the vector from ${ \boldsymbol { v } } _ { \mathbf { 0 } }$ to $v _ { 2 }$ is orthogonal to ${ \pmb e _ { 1 } }$ .The vector $\scriptstyle { E _ { 2 } }$ is

$$
\begin{array} { c } { { E _ { 2 } = v _ { 2 } - v _ { 0 } \quad \mathrm { ( t h e ~ v e c t o r ~ f r o m ~ } v _ { 0 } \mathrm { ~ t o ~ } v _ { 2 } \mathrm { ) } } } \\ { { \phantom { E _ { 2 } = v _ { 2 } - v _ { 0 } \quad } = v _ { 2 } - \langle v _ { 2 } , e _ { 1 } \rangle e _ { 1 } } } \end{array}
$$

and

$$
\langle E _ { 2 } , e _ { 1 } \rangle = \langle v _ { 2 } - \langle v _ { 2 } , e _ { 1 } \rangle e _ { 1 } , e _ { 1 } \rangle = \langle v _ { 2 } , e _ { 1 } \rangle - \langle v _ { 2 } , e _ { 1 } \rangle \langle e _ { 1 } , e _ { 1 } \rangle = 0 ,
$$

which confirms our intuition from Figure 7.

Note that $\pmb { { \cal E } } _ { 2 }$ cannot equal zero for otherwise $v _ { 2 }$ and ${ \pmb e } _ { \mathbf { 1 } }$ (and hence $v _ { 2 }$ and $v _ { 1 } )$ would be linearly dependent. To get a vector of unit length, we define $e _ { 2 } = \cdot E _ { 2 } / \| E _ { 2 } \|$ . Both ${ \pmb e _ { 1 } }$ and $\scriptstyle { e _ { 2 } }$ are orthogonial to each other, and since $e _ { 1 }$ is a multiple of ${ \pmb v } _ { 1 }$ , the vector $\scriptstyle { e _ { 2 } }$ is a linear combination of ${ \pmb v } _ { \mathbf { 1 } }$ and $v _ { 2 }$ .

If $N > 2$ , then we continue the process. We consider the orthogonal projection of $\pmb { v _ { 3 } }$ onto the space spanned by ${ \pmb e _ { 1 } }$ and $\scriptstyle { e _ { 2 } }$ :

$$
\mathrm { O r t h o g o n a l ~ p r o j e c t i o n } = v _ { 0 } = \langle v _ { 3 } , e _ { 1 } \rangle e _ { 1 } + \langle v _ { 3 } , e _ { 2 } \rangle e _ { 2 } .
$$

Then let

$$
E _ { 3 } = v _ { 3 } - v _ { 0 } = v _ { 3 } - ( \langle v _ { 3 } , e _ { 1 } \rangle e _ { 1 } + \langle v _ { 3 } , e _ { 2 } \rangle e _ { 2 } )
$$

![](images/81889e2c585de89203c6e09cdb220232a80aed69d7ed531456aa1f9df112ce20.jpg)  
Figure 7 Gram-Schmidt orthogonalization

and set $\boldsymbol { e } _ { 3 } \approx \boldsymbol { E } _ { 3 } / \| \boldsymbol { E } _ { 3 } \|$ . The same argument as before (for $\scriptstyle { E _ { 2 } }$ shows that $\pmb { { \cal E } } _ { 3 }$ is orthogonal to both ${ \pmb e _ { 1 } }$ and $_ { e _ { 2 } }$ Thus, $\{ e _ { 1 } , e _ { 2 } , e _ { 3 } \}$ is an orthonormal set of vectors that span the same space as $v _ { 1 } , v _ { 2 }$ and $\pmb { v _ { 3 } }$ The pattern is now clear. $\bullet$

# 0.6 Linear Operators and Their Adjoints

# 0.6.1 Linear Operators

First, werecal the definition  a linar map.

DEFINITIoN 0.28 A linear operator (or map) between a vector space $\pmb { V }$ and a vector space $\pmb { W }$ is a function $T : V \to W$ which satisfies

$$
T ( \alpha v + \beta w ) = \alpha T ( v ) + \beta T ( w ) \quad f o r v , w \in V \quad \alpha , \beta \in C .
$$

If $\boldsymbol { v }$ and $W$ are finite dimensional, then $\pmb { T }$ is often identified with its matrix representation with respect to a given choice of bases, say $\{ v _ { 1 } , \ldots , v _ { n } \}$ for $\boldsymbol { V }$ and $\{ w _ { 1 } \ldots w _ { m } \}$ for $\boldsymbol { \mathbf { \mathit { W } } }$ For each $1 \leq j \leq n , T v _ { j }$ belongs to $W$ and therefore it can be expanded in terms of $w _ { 1 } , \ldots , w _ { m }$ .

$$
T ( v _ { j } ) = \sum _ { i = 1 } ^ { m } a _ { i j } w _ { i }
$$

where $\pmb { a } _ { i j }$ are complex numbers. The value of $\scriptstyle { \pmb { T } } ( { \boldsymbol { v } } )$ for any vector $\begin{array} { r } { \boldsymbol { v } = \sum _ { j } x _ { j } \boldsymbol { v } _ { j } \in } \end{array}$ $\pmb { V }$ (with ${ \bf \Phi } _ { x _ { j } \in C }$ can be computed by

$$
\begin{array} { l } { { \displaystyle { \cal T } ( v ) = { \cal T } \left( \sum _ { j = 1 } ^ { n } x _ { j } v _ { j } \right) = \sum _ { j = 1 } ^ { n } x _ { j } { \cal T } ( v _ { j } ) = \sum _ { i = 1 } ^ { m } \sum _ { j = 1 } ^ { n } ( a _ { i j } x _ { j } ) w _ { i } \quad \mathrm { f r o m ~ ( ~ ` ~ ` ~ ` ~ ) } } } \\ { { \displaystyle ~ = \sum _ { i = 1 } ^ { m } c _ { i } w _ { i } . } } \end{array}
$$

The coefficient of ${ \pmb w } _ { \pmb { i } }$ is $\begin{array} { r } { c _ { i } = \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } } \end{array}$ wc entry in the following matrix product:

$$
\left( \begin{array} { c c c } { a _ { 1 1 } } & { \cdots } & { a _ { 1 n } } \\ { \vdots } & { \ddots } & { \vdots } \\ { a _ { m 1 } } & { \cdots } & { a _ { m n } } \end{array} \right) \left( \begin{array} { c } { x _ { 1 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right) .
$$

Thus, the matrix $( a _ { i j } )$ is determined by how the basis vectors $v _ { j } \in V$ are mapped into the basis vectors ${ \pmb w } _ { \pmb { i } }$ of $\pmb { W }$ [see Equation (0.5)]. The matrix then determines how an arbitrary vector $\pmb { v }$ maps into $\pmb { W }$ .

In words, a linear operator $T : V \to W$ is said to be bounded if it maps the unit ball in $V$ to a bounded set in $W$ .This means that there is a number $0 \leq M < \infty$ such that

$$
\{ T v ; v \in V \ \mathrm { w i t h } \ \| v \| \leq 1 \ \} \subset \{ w \in W ; \ \| w \| \leq M \} .
$$

In this case, the norm of $_ { \pmb { T } }$ is defined to be the smallest such $\pmb { M }$ .All linear maps between finite dimensional inner product spaces are bounded. As another example, the orthogonal projection map from any inner product space to any of its subspaces (finite or infinite dimensions) is a bounded linear operator.

# 0.6.2 Adjoints

If $\boldsymbol { V }$ and $\pmb { W }$ are inner product spaces, then we will sometimes need to compute $\langle T ( v ) , w \rangle _ { W }$ by shifting the operator $\pmb { T }$ to the other side of the inner product. In other words, we want to write

$$
\langle T ( v ) , w \rangle _ { \mathcal { W } } = \langle v , T ^ { * } ( w ) \rangle _ { V }
$$

for some operator $T ^ { * } : W \to V$ .We formalize the definition of such a map as follows.

DEFINITION 0.29 If $T : V \to W$ is a linear operator between two inner product spaces, the adjoint of $\pmb { T }$ is the linear operator $T ^ { * } { : } W \to V$ that satisfies

$$
\langle T ( v ) , w \rangle _ { W } = \langle v , T ^ { * } ( w ) \rangle _ { V } .
$$

Every bounded linear operator between two inner product spaces always has an adjoint. Here are two examples of adjoints of linear operators.

# EXAMPLE 0.30

Let $V = C ^ { n }$ and $W = C ^ { m }$ with the standard inner products. Suppose $T : C ^ { n } \to$ ${ \pmb { C } } ^ { m }$ is a linear operator with matrix ${ a _ { i j } \in C }$ with respect to the standard basis

If $X = ( x _ { 1 } , \ldots , x _ { n } ) \in C ^ { n }$ and $Y = ( y _ { 1 } , \dots , y _ { m } ) \in C ^ { m }$ , then

$$
\begin{array} { r l } { \langle T ( X ) , Y \rangle = \displaystyle \sum _ { i = 1 } ^ { m } \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } \overline { { y _ { i } } } } & { } \\ { = \displaystyle \sum _ { j = 1 } ^ { n } x _ { j } \left( \sum _ { i = 1 } ^ { m } \overline { { a _ { i j } } } y _ { i } \right) } & { \mathrm { ( s w i t c h ~ o r d e r ~ o f ~ s u m m a t i o n ) } } \\ { = \displaystyle \sum _ { j = 1 } ^ { n } x _ { j } \left( \sum _ { i = 1 } ^ { m } a _ { j i } ^ { * } y _ { i } \right) } & { } \end{array}
$$

where $a _ { j i } ^ { * } = \overline { { a _ { i j } } }$ (the conjugate of the transpose). The right side is $\langle X , T ^ { * } ( Y ) \rangle$ , where the jth component of ${ \pmb T } ^ { * } ( { \pmb Y } )$ is $\scriptstyle \sum _ { i = 1 } ^ { m } a _ { j i } ^ { * } y _ { i }$ Thus the matrix for the adjoint of $\pmb { T }$ is the conjugate of the transpose of the matrix for $\pmb { T }$ .

# EXAMPle 0.31

Suppose $\pmb { \mathscr { g } }$ is a bounded function on the interval $\alpha \leq x \leq b$ Let $T _ { g } : L ^ { 2 } ( [ a , b ] ) $ $L ^ { 2 } ( \{ a , b \} )$ be defined by

$$
T _ { g } ( f ) ( x ) = g ( x ) f ( x ) .
$$

The adjoint of $\pmb { T _ { g } }$ is just

$$
T _ { g } ^ { * } ( h ) ( x ) = \overline { { g ( x ) } } h ( x )
$$

because

$$
\langle T _ { g } ( f ) , h \rangle = \int _ { a } ^ { b } g ( x ) f ( x ) { \overline { { h ( x ) } } } d x = \int _ { a } ^ { b } f ( x ) { \overline { { g ( x ) } } } h ( x ) d x = \langle f , { \overline { { g } } } h \rangle .
$$

The next theorem computes the adjoint of the composition of two operators.

THEOREM 0.32 Suppose $T _ { 1 } : V \to W$ and $T _ { 2 } : W \to U$ are bounded linear operators between inner product spaces. Then $( T _ { 2 } \circ T _ { 1 } ) ^ { * } = T _ { 1 } ^ { * } \circ T _ { 2 } ^ { * }$ .

Proof For ${ \boldsymbol { v } } \in V$ and ${ \pmb u } \in { \pmb U }$ , we have

$$
\langle T _ { 2 } ( T _ { 1 } ( v ) ) , u \rangle = \langle T _ { 1 } ( v ) , T _ { 2 } ^ { * } ( u ) \rangle = \langle v , T _ { 1 } ^ { * } ( T _ { 2 } ^ { * } ( u ) ) \rangle .
$$

On the other hand, the definition of adjoint implies

$$
\langle T _ { 2 } ( T _ { 1 } ( v ) ) , u \rangle = \langle v , ( T _ { 2 } \circ T _ { 1 } ) ^ { * } u \rangle .
$$

Therefore,

$$
\langle v , ( T _ { 2 } \circ T _ { 1 } ) ^ { \bullet } u \rangle = \langle v , T _ { 1 } ^ { \bullet } ( T _ { 2 } ^ { \bullet } ( u ) ) \rangle
$$

for all ${ \boldsymbol { v } } \in V$ By Exercise 17, if $\pmb { u } _ { \mathbf { 0 } }$ and ${ \pmb u } _ { \mathbf { 1 } }$ are vectors in $V$ with $\langle v , u _ { 0 } \rangle = \langle v , u _ { 1 } \rangle$ for all ${ \boldsymbol { v } } \in V$ , then $\pmb { u } _ { 0 } = \pmb { u } _ { 1 }$ .Therefore, from (0.6), we conclude

$$
( T _ { 2 } \circ T _ { 1 } ) ^ { * } u = T _ { 1 } ^ { * } ( T _ { 2 } ^ { * } ( u ) )
$$

as desired.

In the next theorem, we compute the adjoint of an orthogonal projection.

THEOREM 0.33 Suppose $V _ { 0 }$ is a subspace of an inner product space $\pmb { V }$ . Let $\pi : V \to V _ { 0 }$ be the map that assigns to each $v \in V$ its orthogonal projection onto $V _ { 0 }$ Then the adjoint of $\pmb { \pi }$ is the inclusion map $\iota : V _ { 0 } \to V$ , where for ${ \boldsymbol { v } } _ { 0 } \in V _ { 0 }$ $\iota ( v _ { 0 } ) = v _ { 0 }$ thought of as an element of $\pmb { V }$ .

Proof From Theorem 0.25, each vector $v \in V$ can be written as $\boldsymbol { v } = \boldsymbol { v } _ { 0 } + \boldsymbol { v } _ { 1 }$ where ${ \pmb v _ { 0 } \in \pmb V _ { 0 } }$ and ${ \pmb v } _ { \mathbf { 1 } }$ is orthogonal to $V _ { 0 }$ Note that $\pi ( v ) = v _ { 0 }$ Therefore, for $u _ { 0 } \in V _ { 0 }$ ,

$$
\langle \pi ( v ) , u _ { 0 } \rangle _ { V _ { 0 } } = \langle v _ { 0 } , u _ { 0 } \rangle _ { V _ { 0 } } .
$$

Now the subspace $V _ { 0 }$ inherits its inner product from $\pmb { V }$ .Thus

$$
\begin{array} { r l } & { \langle \pi ( v ) , u _ { 0 } \rangle _ { V _ { 0 } } = \langle v _ { 0 } , u _ { 0 } \rangle _ { V } } \\ & { \qquad = \langle v _ { 0 } + v _ { 1 } , u _ { 0 } \rangle _ { V } \quad \mathrm { s i n c e } v _ { 1 } \in V _ { 0 } ^ { \perp } , \mathrm { a n d } u _ { 0 } \in V _ { 0 } } \\ & { \qquad = \langle v , u _ { 0 } \rangle _ { V } . } \end{array}
$$

So

$$
\langle \pi ( \upsilon ) , u _ { 0 } \rangle _ { V _ { 0 } } = \langle \upsilon , u _ { 0 } \rangle _ { V } .
$$

In addition,

$$
\langle \pi ( v ) , u _ { 0 } \rangle _ { V _ { 0 } } = \langle v , \pi ^ { * } ( u _ { 0 } ) \rangle _ { V }
$$

by the definition of adjoint. By comparing the two expressions for $\langle \pi ( \boldsymbol { v } ) , \boldsymbol { u } _ { 0 } \rangle _ { V _ { 0 } }$ , we conclude

$$
\langle v , u _ { 0 } \rangle _ { V } = \langle v , \pi ^ { * } ( u _ { 0 } ) \rangle _ { V }
$$

for all ${ \boldsymbol { v } } \in V$ By Exercise 17, $\pi ^ { * } ( u _ { 0 } ) = u _ { 0 }$ ,as claimed.

# 0.7 Least Squares and Linear Predictive Coding

In this section, we apply some of the basic facts about linear algebra and inner product spaces to the topic of least squares analysis. As motivation, we first describe how to find the best fit line to a collection of data. Then we present the general idea behind the least squares algorithm. As a further application of least squares, we present the ideas behind linear predictive coding, which is a data compression algorithm. In the next chapter, we use least squares to develop a procedure for approximating signals (or functions) by trigonometric polynomials.

# 0.7.1 Best Fit Line for Data

Consider the following problem. Suppose data points $\pmb { x _ { i } }$ and ${ \pmb y } _ { \pmb { i } }$ for $i = 1 , \dots N$ are given with $x _ { i } \neq x _ { j }$ for ${ \dot { \pmb { \mathscr { i } } } } \neq { \dot { \pmb { \mathscr { j } } } }$ We wish to find the equation of the line $\pmb { y } = m \pmb { x } + \pmb { b }$ that comes closest to fitting all the data. Figure 8 gives an example of four data points (indicated by the small circles) as well as the graph of the line that comes closest to passing through these four points.

![](images/6f9d9158ab0db9e90c37a6a5a1757a055f73d9cfadd3278367ea5a15454aa3c9.jpg)  
Figure 8 Least squares approximation

The word closest here means that the sum of the squares of the errors (between the data and the line) is smaller than the corresponding error with any other line. Suppose the line we seek is $y = m x + b$ As Figure 9 demonstrates, the error between this line at $\pmb { x } = \pmb { x } _ { i }$ and the data point $( x _ { i } , y _ { i } )$ is $\left| y _ { i } - ( m x _ { i } + b ) \right|$ .

![](images/1fb3c6fa6413f304aecf8ca0ec78435a4d886c1966ead294ff9e405b33f05d28.jpg)  
Figure 9 Error at $\pmb { x _ { i } }$ is $\left| y _ { i } - \left( m x _ { i } + b \right) \right|$ (length of dashed line)

Therefore, we seek numbers $_ { \pmb { m } }$ and $\pmb { b }$ that minimize the quantity

$$
{ \pmb E } = \sum _ { i = 1 } ^ { N } | y _ { i } - ( m x _ { i } + \delta ) | ^ { 2 } .
$$

The quantity $\pmb { \cal E }$ can be viewed as the square of the distance (in $\mathcal { R } ^ { N }$ ) from the vector

$$
\begin{array} { r } { Y = \left( \begin{array} { c } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { N } } \end{array} \right) } \end{array}
$$

and the vector $m X + b U$ ,where

$$
X = { \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { N } } \end{array} \right) } \quad { \mathrm { ~ a n d ~ } } \quad U = { \left( \begin{array} { l } { 1 } \\ { 1 } \\ { \vdots } \\ { 1 } \end{array} \right) } .
$$

As $\pmb { m }$ and $\pmb { b }$ vary over all possible real numbers, the expression $m X + b U$ sweeps out a two-dimensional plane, $\pmb { M }$ in $R ^ { N }$ Thus our problem of least squares has the following geometric interpretation: Find the point $P = m X + b U$ on $\pmb { M }$ that is closest to the point $\pmb { Y }$ (see Figure 10).

![](images/0e2a72a56f2f44ebad8edfb24bfce63713b6c32eca510748ca7e74af93cb55fa.jpg)  
Figure 10 $\pmb { P }$ is the closest point on the plane $\pmb { M }$ to the point $\pmb { Y }$

The point $\pmb { P }$ must be the orthogonal projection of $\pmb { Y }$ onto $\pmb { M }$ In particular, $\pmb { Y } - \pmb { P }$ must be orthogonal to $\pmb { M }$ Since $\dot { M }$ is generated by the vectors $\pmb { X }$ and . ${ \pmb U } , { \pmb Y } - { \pmb P }$ must be orthogonal to both $\pmb { X }$ and $\pmb { U }$ .Therefore, we seek the point . $P = m X + b U$ that satisfies the following two equations:

$$
\begin{array} { c } { 0 = \langle ( Y - P ) , X \rangle = \langle ( Y - ( m X + b U ) ) , X \rangle } \\ { 0 = \langle ( Y - P ) , U \rangle = \langle ( Y - ( m X + b U ) ) , U \rangle } \end{array}
$$

or

$$
\begin{array} { r } { \langle X , Y \rangle = m \langle X , X \rangle + b \langle X , U \rangle } \\ { \langle U , Y \rangle = m \langle X , U \rangle + b \langle U , U \rangle . } \end{array}
$$

These equations can be rewritten in matrix form as

$$
\left( \begin{array} { c c c } { x _ { 1 } } & { \cdots } & { x _ { N } } \\ { 1 } & { \cdots } & { 1 } \end{array} \right) \left( \begin{array} { c } { y _ { 1 } } \\ { \vdots } \\ { y _ { N } } \end{array} \right) = \left( \begin{array} { c c c } { x _ { 1 } } & { \cdots } & { x _ { N } } \\ { 1 } & { \cdots } & { 1 } \end{array} \right) \left( \begin{array} { c c c } { x _ { 1 } } & { 1 } \\ { \vdots } & { \vdots } \\ { x _ { N } } & { 1 } \end{array} \right) \left( \begin{array} { c } { m } \\ { b } \end{array} \right) .
$$

Keep in mind that the $\pmb { x _ { i } }$ and ${ \pmb y } _ { i }$ are the known data points. The solution to our least squares problem is obtained by solving the preceding linear system for the unknowns $_ { \pmb { m } }$ and $\pmb { b }$ . This discussion is summarized in the following theorem.

THEOREM 0.34 Suppose $X = \{ x _ { 1 } , x _ { 2 } , \ldots , x _ { N } \}$ and $Y = \{ y _ { 1 } , y _ { 2 } , \dots , y _ { N } \}$ are two sets of data points. The equation of the line ${ \pmb y } = m { \pmb x } + { \pmb b }$ that most closely approximates the data $( \pmb { x } _ { 1 } , \pmb { y } _ { 1 } ) , \dots , ( \pmb { x } _ { N } , \pmb { y } _ { N } )$ in the sense of least squares is obtained by solving the linear equation

$$
\begin{array} { r } { z ^ { T } Y = \bar { z } ^ { T } { Z } \left( \begin{array} { c } { m } \\ { b } \end{array} \right) } \end{array}
$$

for m and $\pmb { b }$ , where

$$
\pmb { Z } = \left( \begin{array} { c c } { { x _ { 1 } } } & { { 1 } } \\ { { \vdots } } & { { \vdots } } \\ { { x _ { N } } } & { { 1 } } \end{array} \right) .
$$

If the $\pmb { x _ { i } }$ are distinct, then this system of equations has the following unique solution for m and $\pmb { b }$ .

$$
m = { \frac { \langle Y , X \rangle - N { \overline { { x } } } { \overline { { y } } } } { \sigma _ { x } } } \quad a n d \quad b = { \frac { { \overline { { y } } } ( \sum _ { i } x _ { i } ^ { 2 } ) - { \overline { { x } } } \langle X , Y \rangle } { \sigma _ { x } } }
$$

where $\begin{array} { r } { \sigma _ { x } = \sum _ { i } ( x _ { i } - \overline { { x } } ) ^ { 2 } } \end{array}$ , $\overline { { \mathfrak { x } } } = ( \sum _ { i } x _ { i } ) / N$ and $\textstyle { \overline { { y } } } = ( \sum _ { i } y _ { i } ) / N$ .

Proof We leave the computation of the formulas for $_ m$ and $\pmb { b }$ as an exercise (see Exercise 24). The statement regarding the unique solution for $_ { \pmb { m } }$ and $\pmb { b }$ will follow once we show that the matrix $z ^ { \pmb { { \tau } } } z$ is nonsingular (i.e., invertible). To this end, suppose the $\pmb { x _ { i } }$ are not all the same; then the vectors $\pmb { X }$ and $\pmb { U }$ are linearly independent and so the matrix $z$ has rank 2. In addition, for any $V \in R ^ { 2 }$

$$
\begin{array} { r l } & { \langle ( Z ^ { T } Z ) V , V \rangle = \langle ( Z ) V , ( Z ) V \rangle \quad ( \mathrm { s e e ~ E x a m p l e ~ } 0 . 3 0 ) } \\ & { \qquad = | ( Z ) V | ^ { 2 } } \\ & { \qquad \geq 0 . } \end{array}
$$

Since $z$ is a matrix of maximal rank (i.e., rank 2), the only way $( z ) V$ can be zero is if $\boldsymbol { V }$ is zero. Therefore, $\langle ( Z ^ { T } Z ) V , V \rangle > 0$ for all nonzero $V$ which means that $z ^ { T } z$ is positive definite. In addition, the matrix $z ^ { T } z$ is symmetric because its transpose, $( z ^ { T } { \boldsymbol { Z } } ) ^ { T }$ , equals itself. Using a standard fact from linear algebra, this positive definite symmetric matrix must be nonsingular. Thus, the equation

$$
( Z ^ { T } Z ) \left( { m \atop b } \right) = Z ^ { T } ( Y )
$$

has a unique solution for $_ m$ and $\pmb { b }$ .

# 0.7.2 General Least Squares Algorithm

Suppose $\pmb { z }$ is a $N \times \mathbf q$ matrix (with possibly complex entries) and let $\pmb { Y }$ be a vector in $R ^ { N }$ (or $C ^ { N }$ Linear algebra is, in part, the study of the equation $z V = Y$ , which when written out in detail is

$$
\left( \begin{array} { c c c } { { z _ { 1 1 } } } & { { \ldots } } & { { z _ { 1 q } } } \\ { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { z _ { N 1 } } } & { { \ldots } } & { { z _ { N q } } } \end{array} \right) \left( \begin{array} { c } { { v _ { 1 } } } \\ { { \vdots } } \\ { { v _ { q } } } \end{array} \right) = \left( \begin{array} { c } { { y _ { 1 } } } \\ { { \vdots } } \\ { { y _ { N } } } \end{array} \right) .
$$

If $N > q$ , then the equation $z V = Y$ does not usually have a solution for $V \in C ^ { q }$ because there are more equations $( N )$ than there are unknowns $( v _ { 1 } , \ldots , v _ { q } )$ . If there is no solution, the problem of least squares asks for the next best quantity: Find the vector $V \in C ^ { q }$ such that $z v$ is as close as possible to $\pmb { Y }$ .

In the case of finding the best fit line to a set of data points $( x _ { i } , y _ { i } ) , \ i =$ $\mathbf { 1 } \ldots . . \mathbf { N }$ , the matrix $z$ is

$$
\pmb { Z } = \left( \begin{array} { c c } { x _ { 1 } } & { 1 } \\ { \vdots } & { \vdots } \\ { x _ { N } } & { 1 } \end{array} \right)
$$

and the vectors $\pmb { Y }$ and $\boldsymbol { V }$ are

$$
Y = \left( \begin{array} { c } { { y _ { 1 } } } \\ { { \vdots } } \\ { { y _ { N } } } \end{array} \right) \quad \mathrm { a n d } \quad V = \left( \begin{array} { c } { { m } } \\ { { b } } \end{array} \right) .
$$

In this case, the matrix product ZV is

$$
{ \left( \begin{array} { l l } { x _ { 1 } } & { 1 } \\ { \vdots } & { \vdots } \\ { x _ { N } } & { 1 } \end{array} \right) } \left( { \begin{array} { l } { m } \\ { b } \end{array} } \right) = { \left( \begin{array} { l } { m x _ { 1 } + b } \\ { \vdots } \\ { m x _ { N } + b } \end{array} \right) } = m X + b U
$$

where $\pmb { X }$ and $\pmb { U }$ are the vectors given in (0.7). Thus, finding the $V = \langle m , b \rangle$ so that $z V$ is closest to $\pmb { Y }$ is equivalent to finding the slope and ${ \pmb y }$ intercept of the best fit line to the data $( x _ { i } , y _ { i } ) , \ i = 1 \dots N ,$ as in the last section.

The solution to the general least squares problem is given in the following theorem.

![](images/f43f4da3d46d0f2b55d600f93d6e9a0410ba6da34beedf67a33efb4759a0a6dc.jpg)

THEOREM 0.35 Suppose $\pmb { z }$ is a $N \times q$ matrix (with possibly complex entries) of maximal rank and with $N \geq q$ Let $\pmb { Y }$ be a vector in $R ^ { N }$ (or $C ^ { N } .$ ).There is a unique vector $V \in C ^ { q }$ such that ZV is closest to $\pmb { Y }$ . Moreover, the vector $V$ is the unique solution to the matrix equation

$$
Z ^ { * } Y = Z ^ { * } Z V .
$$

If $z$ is a matrix with real entries, then the preceding equation becomes

$$
\begin{array} { r } { Z ^ { T } Y = Z ^ { T } Z V . } \end{array}
$$

Note that in the case of the best fit line, the matrix $\pmb { z }$ in (0.8) and the equation $Z ^ { T } Y = Z ^ { T } Z V$ are the same as those given in Theorem 0.34.

![](images/be8fbeab8c36c1bb5f2a8a90a154d53409b85ad36b8c6cd97d70c766013a4486.jpg)  
Figure 11 $\mathbf { Y } - \mathbf { z } V$ must be orthogonal to $M = \operatorname { s p a n } \{ Z _ { 1 } , \dots Z _ { q } \}$

Proof The proof of this theorem is similar to the proof given in the construction of the best fit line. We let $\mathbf { Z _ { 1 } , \dots , Z _ { q } }$ be the columns of the matrix $z$ Then $Z V = v _ { 1 } Z _ { 1 } + \cdots + v _ { q } Z _ { q }$ is a point that lies in the subspace $M \subset C ^ { N }$ generated by $\mathbf { Z } _ { 1 } , \ldots , \mathbf { Z } _ { q }$ We wish to find the point $z V$ that is closest to $\pmb { Y }$ As in Figure 11, $\pmb { Y } - \pmb { z } \pmb { V }$ must be orthogonal to $M$ ,or, equivalently, $Y - z V$ must be orthogonal to $\mathbf { \delta Z _ { 1 } , \dots , Z _ { q } }$ that generate $M$ Thus

$$
\left. Y - Z V , Z _ { i } \right. = 0 \quad 1 \leq i \leq q .
$$

These equations can be written succinctly as

$$
\cdot \ z ^ { * } ( Y - Z V ) = 0
$$

because the ith component of this (vector) equation is the inner product of $Y - z V$ with $\pmb { Z _ { i } }$ .This equation can be rearranged to read

$$
Z ^ { * } Y = Z ^ { * } Z V
$$

as claimed in the theorem.

The matrix $z ^ { \ast } z$ has dimension $\mathbf { \nabla } \pmb { q } \times \mathbf { \nabla } \pmb { q }$ and by the same arguments used in the proof of Theorem 0.34, you can show that this matrix is nonsingular (using the fact that $\pmb { z }$ has maximal rank). Therefore, the equation

$$
Z ^ { * } Y = z ^ { * } Z V
$$

has a unique solution $V \in C ^ { q }$ as claimed.

# EXAMPLE 0.36

Suppose a set of data points $\{ ( x _ { i } , y _ { i } ) , \ i = 1 , . . . N \}$ behaves in a quadratic rather than a linear fashion. Then a best fit quadratic equation of the form $y = a x ^ { 2 } + b x + c$ can be found. In this case, we seek $a , b ,$ ,and $\pmb { c }$ that minimize the quantity

$$
E = \sum _ { i = 1 } ^ { N } | y _ { i } - ( a x _ { i } ^ { 2 } + b x _ { i } + c ) | ^ { 2 } .
$$

We can apply Theorem 0.35 with

$$
\pmb { Z } = \left( \begin{array} { l l l } { x _ { 1 } ^ { 2 } } & { x _ { 1 } } & { 1 } \\ { \vdots } & { \vdots } & { \vdots } \\ { x _ { N } ^ { 2 } } & { x _ { N } } & { 1 } \end{array} \right) \quad V = \left( \begin{array} { l } { a } \\ { b } \\ { c } \end{array} \right) \quad \mathrm { a n d } \quad Y = \left( \begin{array} { l } { y _ { 1 } } \\ { \vdots } \\ { y _ { N } } \end{array} \right) .
$$

From Theorem 0.35, the solution $V = ( a , b , c )$ to this least squares problem is the solution to $\begin{array} { r } { z ^ { T } z V = z ^ { T } Y } \end{array}$ Exercise 28 asks you to solve this system with specific numerical data. •

# 0.7.3 Linear Predictive Coding

Here, we will apply the least squares analysis procedure to the problem of efficiently transmitting a signal. As mentioned earlier, computers can process millions, and in some cases billions, of instructions per second. However, if the output must be transmitted from one location to another (say a picture downloaded from the Web), the signal must often be sent over telephone lines or some other medium that can only transmit thousands of bytes per second (in the case of telephone lines, this rate is currently about 60 kilobytes per second). Therefore, instead of transmitting all the data points of a signal, some sort of coding algorithm (data compression) is applied so that only the essential parts of the signal are transmitted.

Let us suppose we are transmitting a signal, which after some discretization process can be thought of as a long string of numbers

$$
x _ { 1 } , x _ { 2 } , x _ { 3 } , \ldots
$$

(zeros and ones, perhaps). For simplicity, we will assume that each $\pmb { x _ { i } }$ is real. Often, there is a repetition of some pattern of the signal (redundancy). If the repetition is perfect, say 1,1,0, 1,1,0, 1,1,0, etc., then there would be no need to send all the digits. We would only need to transmit the pattern 1,1,0 and the number of times this pattern is repeated. Usually, however, there is not a perfect repetition of a pattern, but there may be some pattern that is nearly repetitive. For example, the rhythm of a beating heart is nearly, but not exactly, repetitive (if it is a healthy heart). If there is a near repetition of some pattern, then the following linear predictive coding procedure can achieve significant compression of data.

Main Idea. The idea behind linear predictive coding is to divide up the data into blocks of length $N$ ,where $\pmb { N }$ is a large number.

$$
\{ x _ { 1 } \ldots x _ { N } \} , \{ x _ { N + 1 } \ldots x _ { 2 N } \} , \{ x _ { 2 N + 1 } \ldots x _ { 3 N } \} \ldots
$$

Let's consider the first block of data $\pmb { x } _ { 1 } , \ldots , \pmb { x } _ { N }$ .We choose a number $\pmb { p }$ that should be small compared with $\pmb { N }$ .The linear predictive coding scheme will provide the best results (best compression) if $\pmb { p }$ is chosen close to the number of digits in the near repetitive pattern of this block of data. Next, we try to find numbers $a _ { 1 } , a _ { 2 } , \dotsc , a _ { p }$ that minimize the terms

$$
e ( n ) = x _ { n } - \sum _ { k = 1 } ^ { p } a _ { k } x _ { n - k } \quad { \mathrm { f o r ~ } } p + 1 \leq n \leq N .
$$

in the sense of least squares. Once this is done (the details of which will be presented later), then the idea is to transmit $x _ { 1 } \ldots x _ { p }$ as well as $a _ { 1 } , \ldots , a _ { p }$ . Instead of transmitting $x _ { p + 1 } , x _ { p + 2 } , \ldots$ , we use the following scheme starting with ${ \pmb n } = { \pmb p } + { \pmb 1 }$ If $e ( p + 1 )$ is smaller than some specified tolerance, then we can treat $e ( p + 1 )$ as zero. By letting ${ \pmb n } = { \pmb p } + { \pmb 1 }$ and $e ( p + 1 ) = 0$ in (0.9), we have

$$
x _ { p + 1 } = \sum _ { k = 1 } ^ { p } a _ { k } x _ { p + 1 - k } = a _ { 1 } x _ { p } + a _ { 2 } x _ { p - 1 } + a _ { 3 } x _ { p - 2 } + \cdots + a _ { p } x _ { 1 } .
$$

There is no need to transmit $x _ { p + 1 }$ because the data $\pmb { x _ { 1 } } \ldots \pmb { x _ { p } }$ as well as $a _ { 1 } \ldots a _ { p }$ have already been transmitted and so the receiver can reconstruct $x _ { p + 1 }$ according to the preceding formula. If $e ( p + 1 )$ is larger than the specified tolerance, then $x _ { p + 1 }$ [or, equivalently, $e ( p + 1 ) ]$ needs to be transmitted.

Once the receiver has reconstructed (or received) $x _ { p + 1 }$ , $\pmb { n }$ can be incremented to ${ \pmb { p } } + { \pmb { 2 } }$ in (0.9). If $e _ { p + 2 }$ is smaller than the tolerance, then $x _ { p + 2 }$ does not need to be transmitted and the receiver can reconstruct $x _ { p + 2 }$ by setting $e ( p + 2 ) = 0$ in (0.9) giving

$$
x _ { p + 2 } = a _ { 1 } x _ { p + 1 } + \cdots + a _ { p } x _ { 2 } .
$$

The rest of the $\pmb { x } _ { p + 3 } , \ldots , { \pmb { x } } _ { N }$ can be reconstructed by the receiver in a similar fashion.

The hope is that if the $\mathbf { \alpha } _ { a _ { i } }$ have been chosen to minimize $\{ e ( p { + } 1 ) , \ldots , e ( N ) \}$ in the sense of least squares, then most of the $| e ( n ) |$ will be less than the specified tolerance and therefore most of the $x _ { n }$ can be reconstructed by the receiver and not actually transmitted. The result is that instead of transmitting $N$ pieces of data (i.e., $\boldsymbol { x } _ { 1 } , \ldots , \boldsymbol { x } _ { N } )$ , we only need to transmit $\mathbf { 2 } p$ pieces of data (i.e., $a _ { 1 } , \ldots , a _ { p }$ and $x _ { 1 } , \ldots , x _ { p } )$ and those (hopefully few) values of ${ \pmb x _ { n } }$ where $| e ( n ) |$ is larger than the tolerance. Since $\mathbf { 2 } p$ is typically much less than $N$ ,significant data compression can be achieved. The other blocks of data can be handled similarly, with possibly different values of $\pmb { p }$ .

Role of Least Squares. To find the coefficients $a _ { 1 } , \ldots , a _ { p }$ ,we use Theorem 0.35. We start by putting equation (0.9), for $\pmb { n } = \pmb { p } + 1 , \ldots N$ , in matrix form:

$$
\pmb { { \cal E } } = \pmb { { \cal Y } } - \pmb { { \cal Z } } \pmb { { \cal V } }
$$

where

$$
E = \left( \begin{array} { c } { e ( p + 1 ) } \\ { \vdots } \\ { e ( N ) } \end{array} \right) \quad Y = \left( \begin{array} { c } { x _ { p + 1 } } \\ { \vdots } \\ { x _ { N } } \end{array} \right) \quad Z = \left( \begin{array} { c c c c } { x _ { p } } & { x _ { p - 1 } } & { \ldots } & { x _ { 1 } } \\ { x _ { p + 1 } } & { x _ { p } } & { \ldots } & { x _ { 2 } } \\ { \vdots } & { \ddots } & { \vdots } \\ { x _ { N - 1 } } & { x _ { N - 2 } } & { \ldots } & { x _ { N - p } } \end{array} \right)
$$

and

$$
V = \left( { \begin{array} { c } { a _ { 1 } } \\ { \vdots } \\ { a _ { p } } \end{array} } \right) .
$$

We want to choose $V = ( a _ { 1 } , \ldots , a _ { p } ) ^ { T }$ so that $\| \pmb { E } \|$ is as small as possible, or, in other words, so that $z V$ is as close as possible to $\pmb { Y }$ From Theorem 0.35, $V = ( a _ { 1 } , \ldots , a _ { p } ) ^ { T }$ is found by solving the following (real) matrix equation:

$$
\begin{array} { r } { z ^ { T } Y = z ^ { T } Z V . } \end{array}
$$

Written out in detail, this equation is

$$
\binom { \langle Z _ { p } , Y \rangle } { \vdots } = \left( \begin{array} { c } { { \cdots Z _ { p } ^ { T } \cdots } } \\ { { \vdots } } \\ { { \cdots Z _ { 1 } ^ { T } \cdots } } \end{array} \right) \left( \begin{array} { c c c } { { \vdots } } & { { } } & { { \vdots } } \\ { { Z _ { p } } } & { { \cdots } } & { { Z _ { 1 } } } \\ { { \vdots } } & { { } } & { { \vdots } } \end{array} \right) \left( \begin{array} { c } { { a _ { 1 } } } \\ { { \vdots } } \\ { { a _ { p } } } \end{array} \right)
$$

where we have labeled the columns of the matrix of $\pmb { z }$ by $\pmb { Z _ { p } } , \ldots , \pmb { Z _ { 1 } }$ (reverse order). The horizontal dots on either side of the $\pmb { Z _ { i } ^ { T } }$ indicate that these entries are row vectors. Likewise, the vertical dots above and below the $\mathbf { \delta } _ { Z _ { i } }$ indicate that these entries are column vectors.

Equation (0.10) is a $\pmb { p } \times \pmb { p }$ system of equations for the $a _ { 1 } , \ldots , a _ { p }$ that can be solved in terms of the $\pmb { z }$ vectors (i.e., the original signal points, $\pmb { x }$ )via Gaussian elimination.

# Summary of Linear Predictive Coding

Linear predictive coding involves the following procedure.

1.Sender cuts the data into blocks

$$
\{ x _ { 1 } \dots x _ { N } \} , \{ x _ { N + 1 } \dots x _ { 2 N } \} , \{ x _ { 2 N + 1 } \dots x _ { 3 N } \} \dots x . . .
$$

where each block has some near repetitive pattern. Then choose $\pmb { p }$ close to the length of the repetitive pattern for the first block. t

2. For $1 \leq i \leq p$ , form the vectors

$$
Z _ { i } = \left( \begin{array} { c } { { x _ { i } } } \\ { { \vdots } } \\ { { x _ { N + i - p - 1 } } } \end{array} \right) .
$$

$a _ { 1 } , \ldots , a _ { p }$ and transmits to the receiver both $a _ { 1 } , \ldots , a _ { p }$ and $x _ { 1 } , \ldots , x _ { p }$

The receiver then reconstructs $x _ { p + 1 } , \ldots , x _ { N }$ in this order) via the equation

$$
x _ { n } = a _ { 1 } x _ { n - 1 } + \cdots + a _ { p } x _ { n - p } \quad ( p + 1 \leq n \leq N )
$$

for those ${ \pmb x } _ { \pmb n }$ where the corresponding least squares errors, $e ( n )$ , are smaller than some specified tolerance. If $e ( n )$ is larger than the tolerance, then the sender must transmit ${ \pmb x } _ { \pmb n }$ .

Certainly, some work is required for the sender to solve the preceding equations for the $a _ { 1 } , \dotsc , a _ { p }$ and for the receiver to reconstruct the ${ \pmb x } _ { \pmb n }$ You may wonder whether this work is more than the energy required to transmit all the $\pmb { x _ { i } }$ .However, keep in mind that the work required to solve for the $\pmb { a _ { i } }$ and reconstruct the ${ \pmb x } _ { \pmb n }$ is done by the sender and receiver with computers that can do millions or billions of operations per second, whereas the transmission lines may only handle thousands of data bits per second. So the goal is to shift, as much as possible, the burden from the relatively slow process of transmitting the data to the much faster process of performing computations by the computers located at either the sender or the receiver.

# 0.8 Exercises

1. Verify that the function

$$
\langle Z , W \rangle = \sum _ { j = 1 } ^ { n } Z _ { j } { \widehat { W _ { j } } }
$$

for $\pmb { Z } = ( Z _ { 1 } , \ldots , Z _ { n } )$ , $W = ( W _ { 1 } , \dots , W _ { n } ) \in C ^ { n }$ defines an inner product on $C ^ { n }$ (i.e., satisfies Definition 0.1).

Verify that the functions $\langle , \rangle$ defined in Examples 0.2 and 0.3, arc inncr products.

3. Define $\langle V , W \rangle$ for $V = ( v _ { 1 } , v _ { 2 } )$ and $W = ( w _ { 1 } , w _ { 2 } ) \in C ^ { 2 }$ as

$$
\langle V , W \rangle = ( { \overline { { w _ { 1 } } } } , { \overline { { w _ { 2 } } } } ) \left( \begin{array} { l l } { 1 } & { 2 } \\ { 2 } & { 4 } \end{array} \right) \left( \begin{array} { l } { \upsilon _ { 1 } } \\ { \upsilon _ { 2 } } \end{array} \right) .
$$

Show that $\langle V , V \rangle = 0$ for all vectors $V = \langle v _ { 1 } , v _ { 2 } \rangle$ with $v _ { 1 } + 2 v _ { 2 } = 0$ .Does $\langle , \rangle$ define an inner product?

4. Show that the $L ^ { 2 } [ a , b ]$ inner product satisfies the following propertics.

The $L ^ { 2 }$ inner product is conjugate symmetric (i.e., $\langle f , g \rangle = { \overline { { \langle g , f \rangle } } }$ , homogeneous, and bilinear (these properties are listed in Definition 0.1).

Show that the $L ^ { 2 }$ inner product satisfies positivity on the space of continuous functions on $[ a , b ]$ by using the following outline.

) We want to show that if $\begin{array} { r } { \int _ { a } ^ { b } | f ( t ) | ^ { 2 } d t = 0 } \end{array}$ , then $\pmb { f } ( t ) = \mathbf { 0 }$ for all · $a \leq t \leq b$ .

(b) Suppose, by contradiction, that $| f ( t _ { 0 } ) | > 0$ then use the definition of continuity to show that $| f ( t ) | > | f ( t _ { 0 } ) | / 2$ on an interval of the form $[ t _ { 0 } - \delta , t _ { 0 } + \delta ]$ .

(c) Then show

$$
\int _ { a } ^ { b } | f ( t ) | ^ { 2 } d t \geq { \frac { | f ( t _ { 0 } ) | ^ { 2 } } { 4 } } [ 2 \delta ] > 0 ,
$$

hic cicpt $\begin{array} { r } { \int _ { a } ^ { b } | f ( t ) | ^ { 2 } d t = 0 , } \end{array}$

.Show that $\begin{array} { r } { \langle x , y \rangle = \sum _ { n = 0 } ^ { \infty } x _ { n } \overline { { y _ { n } } } } \end{array}$ defines an inner product on $\scriptstyle { l ^ { 2 } }$ .

6. For $\pmb { n } > \mathbf { 0 }$ , let

$$
f _ { n } ( t ) = { \left\{ \begin{array} { l l } { 1 , } & { 0 \leq t \leq 1 / n } \\ { 0 , } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

Show that ${ f _ { n } } \to 0$ in $\scriptstyle { L ^ { 2 } [ 0 , 1 ] }$ . Show that $f _ { n }$ does not converge to zero uniformly on [0, 1].

7. For $\pmb { n } > \mathbf { 0 }$ , let

$$
f _ { n } ( t ) = { \left\{ \begin{array} { l l } { { \sqrt { n } } } & { 0 \leq t \leq 1 / n ^ { 2 } } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

Show that $f _ { n } \to 0$ in $L ^ { 2 } [ 0 , 1 ] .$ but that $f _ { n } ( 0 ) \to \infty$ as $\pmb { n }  \infty$

8. Is Theorem 0.10 true on an infinite interval such as $[ 0 , \infty ) ^ { \prime }$ ?

9. Compute the orthogonal complement of the space in $R ^ { 3 }$ spanned by the vector $( 1 , - 2 , 1 )$ .

10. Let $f ( t ) = 1$ on $0 \leq t \leq 1$ .Show that the orthogonal complement of $\pmb { f }$ in $\scriptstyle { L ^ { 2 } [ 0 , 1 ] }$ is the set of all functions whose average value is zero.

Show that  differentiable uncion, $\pmb { f }$ is orthogonal to $\cos ( t )$ on $L ^ { 2 } [ 0 , \pi ]$ . then $\pmb { f ^ { \prime } }$ is orthogonal to $\sin ( t )$ in $L ^ { 2 } [ 0 , \pi ]$ .Hint: Integrate by parts.

12. By using Gram-Schmidt, find an orthonormal basis for the subspace of $L ^ { 2 } [ 0 , 1 ]$ spanned by $^ { 1 , x , x ^ { 2 } , x ^ { 3 } }$ .

13. Find the $\scriptstyle { L ^ { 2 } [ 0 , 1 ] }$ projection of the function cos $\pmb { x }$ onto the space spanned by $\mathbf { 1 } , x , x ^ { 2 } , x ^ { 3 }$ .

14. Find the $L ^ { 2 } [ - \pi , \pi ]$ orthogonal projection of the function $f ( x ) = x ^ { 2 }$ onto the space $V _ { n } \subset L ^ { 2 } [ - \pi , \pi ]$ spanned by

$$
\left\{ 1 , { \frac { \sin ( j x ) } { \sqrt { \pi } } } , { \frac { \cos ( j x ) } { \sqrt { \pi } } } ; j = 1 , \ldots , n \right\}
$$

for $\pmb { n = 1 }$ , Repeat this exercise for $\scriptstyle { \mathfrak { n } } = { \mathfrak { 2 } }$ and $\mathbf { \mathscr { n } } = \mathbf { 3 } .$ Plot these projections along with $\pmb { f }$ using a computer algebra system. Repeat for $\pmb { g } ( \pmb { x } ) = \pmb { x } ^ { 3 }$ .

15. Project the function $\pmb { f } ( \pmb { x } ) = \pmb { x }$ onto the space spanned by $\phi ( x ) , \psi ( x ) , \psi ( 2 x )$ $\psi ( 2 x - 1 ) \in L ^ { 2 } [ 0 , 1 ]$ where

$$
\phi ( x ) = \left\{ { \begin{array} { l l } { 1 , } & { 0 \leq x < 1 } \\ { 0 , } & { { \mathrm { o t h e r w i s e } } } \end{array} } \right. \quad \psi ( x ) = \left\{ { \begin{array} { l l } { 1 , } & { 0 \leq x < 1 / 2 } \\ { - 1 , } & { 1 / 2 \leq x < 1 } \\ { 0 , } & { { \mathrm { o t h e r w i s e } } . } \end{array} } \right.
$$

16. Let $D = \{ ( x , y ) \in R ^ { 2 }$ ; $x ^ { 2 } + y ^ { 2 } \leq 1 \}$ . Let

$$
L ^ { 2 } ( D ) = \left\{ f : D \to C ; \iint _ { D } | f ( x , y ) | ^ { 2 } d x d y < \infty \right\} .
$$

Define an inner product on $L ^ { 2 } ( D )$ by

$$
\langle f , g \rangle = \iint _ { D } f ( x , y ) { \overline { { g ( x , y ) } } } d x d y .
$$

Let $\phi _ { n } ( x , y ) \ : = \ : ( x + i y ) ^ { n }$ $\pmb { n = 0 , 1 , 2 , \dots }$ Show that this collection of functions is orthogonal in $L ^ { 2 } ( D )$ and compute $\| \phi _ { n } \|$ Hint: Use polar coordinates.

17. Suppose $\pmb { u } _ { 0 }$ and ${ \pmb u } _ { \mathbf { 1 } }$ are vectors in the inner product space $V$ with $\left. { { u } _ { 0 } } , { \boldsymbol { v } } \right. =$ . $\scriptstyle \left. u _ { 1 } , v \right.$ for all $v \in V$ Show that $\pmb { u } _ { 0 } = \pmb { u } _ { 1 }$ Hint: Let $\pmb { \nu } = \pmb { u } _ { 0 } - \pmb { u } _ { 1 }$ .

18. Suppose $\pmb { A }$ is an $\mathbf { \nabla } _ { n } \times n$ matrix with complex entries. Show that the following are equivalent.

The rows of $\pmb { A }$ form an orthonormal basis in $C ^ { n }$ .

(b) $A A ^ { * } = I$ (the identity matrix).   
(c) $\| A x \| = \| x \|$ for all vectors ${ \pmb x } \in C ^ { n }$ .

19. Suppose $\pmb { K } ( \pmb { x } , \pmb { y } )$ is a continuous function that vanishes outside a bounded set in $\scriptstyle R \times R$ Define $T : L ^ { 2 } ( R )  L ^ { 2 } ( R )$ by

$$
T ( f ) ( x ) = \int _ { y \in R } f ( y ) K ( x , y ) d y .
$$

Show $\begin{array} { r } { T ^ { * } g ( x ) = \int _ { y \in R } \overline { { K ( y , x ) } } g ( y ) d y } \end{array}$ Note the parallel with the adjoint o a matrix $( A _ { i j } ^ { * } = \overline { { A } } _ { j i } )$ .

20. Suppose $A : V  W$ is a linear map between two inner product spaces. Show that $\mathbf { K e r } ( A ^ { * } ) = ( \mathbf { R a n g e } A ) ^ { \perp }$ .Note: Ker stands for Kernel; $\kappa \mathrm { e r } ( A ^ { * } )$ is the set of all vectors in $\pmb { W }$ that are mapped to zero by $A ^ { * }$ .

21. Prove the following theorem (Fredholm's alternative): Suppose $A : V \to W$ is a linear map between two inner product spaces. Let $\pmb { b }$ be any element in W. Then either

• $\pmb { A x } = \pmb { b }$ has a solution for some $\pmb { x } \in \pmb { V }$ , or There is a vector $\pmb { w } \in \pmb { W }$ with $A ^ { * } w = 0$ and $\langle b , w \rangle _ { W } \neq 0$ .

22. Suppose $V _ { 0 }$ is a finite dimensional subspace of an inner product space, $\pmb { V }$ Show that $V _ { 0 } = ( ( V _ { 0 } ) ^ { \perp } ) ^ { \perp }$ Hint: The inclusion $\subset$ is easy; for the reverse inclusion, take any element $w \in ( ( V _ { 0 } ) ^ { \bot } ) ^ { \bot }$ and then use Theorem 0.25 to decompose $\pmb { w }$ into its components in $V _ { 0 }$ and $V _ { 0 } ^ { \perp }$ Show that its $V _ { 0 } ^ { \perp }$ -component is zero.

3.Show that a set of orthonormal vectors is linearly independent.

24. Verify the formulas for $_ { \pmb { m } }$ and $\pmb { b }$ given in Theorem 0.34.

25. Prove the uniqueness part of Theorem 0.35; Hint: See the proof of the uniqueness part of Theorem 0.34.

26Obtain an alternative proof (using calculus) of Theorem 0.34 by using the following outline.

(a) Show that the least squares problem is equivalent to finding $_ m$ and $\pmb { b }$ to minimize the error quantity

$$
E ( m , b ) = \sum _ { i = 1 } ^ { N } | m x _ { i } + b - y _ { i } | ^ { 2 } .
$$

() From calculus, show that this minimum occurs when

$$
\frac { \partial E } { \partial m } = \frac { \partial E } { \partial b } = 0 .
$$

cSolve these two equations for $_ { \pmb { m } }$ and $\pmb { b }$ .

$\frac { x \mid 0 \mid 1 3 4 } { y \mid 0 8 8 8 2 0 } .$

28. Repeat the previous problem with the best fit least squares parabola.

29. This exercise is best done with MATLAB. The goal of this exercise is to use linear predictive coding to compress strings of numbers. Choose $x =$ $( \pmb { x } _ { 1 } , \dots , \pmb { x } _ { N } )$ , where $\pmb { x } _ { j }$ a is periodic sequence of period $\pmb { p }$ and length $N$ For example, $\pmb { x } _ { j } = \sin ( j \pi / 3 )$ for $1 \leq j \leq N = 6 0$ is a periodic sequence of length · ${ \pmb { \mathscr { p } } } = { \pmb { \mathscr { 6 } } }$ Apply the linear predictive coding scheme to compute $a _ { 1 } , \ldots , a _ { p }$ . Compute the residual $\pmb { { \cal E } } = \pmb { { \cal Y } } - \pmb { Z } \pmb { V }$ .If done correctly, this residual should be theoretically zero (although the use of a computer will introduce a small round-off error). Now perturb $\pmb { X }$ by a small randomly generated sequence [in MATLAB, add rand(1,60) to $\boldsymbol { x } \boldsymbol { ] }$ Then reapply linear predictive coding and see how many terms in the residual $\pmb { \cal E }$ are small (say less than 0.1). Repeat with other sequences $\pmb { X }$ on your own.

# Chapter 1 Fourier Series

# 1.1 Introduction

In this chapter, we examine the trigonometric expansion of a function $\pmb { f } ( \pmb { x } )$ defined on an interval such as $- \pi \leq x \leq \pi$ A trigonometric expansion is a sum of the form

$$
a _ { 0 } + \sum _ { k } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) \qquad ,
$$

where the sum could be finite or infinite.Why should we care about expressing a function in such a way? As the following sections show, the answer varies depending on the application we have in mind.

# 1.1.1 Historical Perspective

Trigonometric expansions arose in the 1700s, in connection with the study of vibrating strings and other similar physical phenomena; they became part of a controversy over what constituted a general solution to such problems, but they were not investigated in any systematic way. In 1808, Fourier wrote the first version of his celebrated memoir on the theory of heat Théorie Analytique de la Chaleur, which was not published until 1822. In it, he made a detailed study of trigonometric series, which he used to solve a variety of heat conduction problems.

Fourier's work was controversial at the time, partly because he did make unsubstantiated claims and overstate the scope of his results, but mostly because his point of view was new and strange to mathematicians of the day. For instance, in the early nineteenth century, a function was considered to be any expression involving known terms, such as powers of $\pmb { x }$ , exponential functions, and trigonometric functions. The more abstract definition of a function (i.e., as a rule that assigns numbers from one set, called the domain, to another set, called the range) did not come until later. Nineteenth-century mathematicians tried to answer the following question: Can a curve in the plane, which has the property that each vertical line intersects the curve at most once, be described as the graph of a function that can be expressed using powers of $\pmb { x }$ ,exponentials, and trigonometric functions? In fact, they showed that for most curves, only trigonometric sums of the type given in (1.1) are needed (powers of $\pmb { x }$ , exponentials, and other types of mathematical expressions are unnecessary). We shall prove this result in Theorem 1.22.

The Riemann integral and the Lebesgue integral arose in the study of Fourier series. Applications of Fourier series (and the related Fourier transform) include probability and statistics, signal processing, and quantum mechanics. Nearly two centuries after Fourier's work, the series that bears his name is still important, practically and theoretically, and still a topic of current research. For a fine historical summary and further references, see John J. Benedetto's book [1].

# 1.1.2 Signal Analysis

There are many practical reasons for expanding a function as a trigonometric sum. If $\pmb { f } ( t )$ is a signal, (for example, a time-dependent electrical voltage or the sound coming from a musical instrument), then a decomposition of $\pmb { f }$ into a trigonometric sum gives a description of its component frequencies. Here, we let $\pmb { t }$ be the independent variable (representing time) instead of $\pmb { x }$ A sine wave, such as $\sin ( k t )$ , has a period of ${ 2 \pi } / { k }$ and a frequency of $\pmb { k }$ (i.e., vibrates $\pmb { k }$ times in the interval $0 \leq t \leq 2 \pi$ . A signal such as

$$
2 \sin ( t ) - 5 0 \sin ( 3 t ) + 1 0 \sin ( 2 0 0 t )
$$

contains frequency components that vibrate at 1, 3, and 200 times per $2 \pi \cdot$ - interval length. In view of the size of the coefficients, the component vibrating at a frequency of 3 dominates over the other frequency components.

A common task in signal analysis is the elimination of high-frequency noise. One approach is to express $\pmb { f }$ as a trigonometric sum

$$
f ( t ) = a _ { 0 } + \sum _ { k } a _ { k } \cos ( k t ) + b _ { k } \sin ( k t )
$$

and then set the high-frequency coefficients (the ${ \pmb { a } } _ { { \pmb k } }$ and $\pmb { b _ { k } }$ for large $\pmb { k }$ ) equal to zero.

Another common task in signal analysis is data compression. The goal here is to send a signal in a way that requires minimal data transmission. One approach is to express the signal, $\pmb { f }$ , in terms of a trigonometric expansion, as previously, and then send only those coefficients, $\scriptstyle a _ { k }$ and $\boldsymbol { b } _ { \boldsymbol { k } }$ , that are larger (in absolute value) than some specified tolerance. The coefficients that are small and do not contribute substantially to $\pmb { f }$ can be thrown away. There is no danger that an infinite number of coefficients stay large, because we will show (see the Riemann-Lebesgue lemma, Theorem 1.21) that ${ \pmb a } _ { { \pmb k } }$ and $\scriptstyle b _ { k }$ converge to zero as $k \to \infty$

# 1.1.3 Partial Differential Equations

Trigonometric sums also arise in the study of partial differential equations. Although the subject of partial differential equations is not the main focus of this book, we digress to give a simple yet important example. Consider the heat equation

$$
\begin{array} { r l r l } & { u _ { t } ( x , t ) = u _ { x x } ( x , t ) } & & { t > 0 , 0 \le x \le \pi } \\ & { u ( x , 0 ) = f ( x ) } & & { 0 \le x \le \pi } \\ & { u ( 0 , t ) = A } & & { u ( \pi , t ) = B . } \end{array}
$$

The solution, ${ \pmb u } ( { \pmb x } , t )$ , to this differential equation represents the temperature of a rod of length $\pmb { \pi }$ at position $\pmb { x }$ and at time t with initial temperature (at $\pmb { t = 0 }$ given by ${ f } ( x )$ and where the temperatures at the ends of the rod, $\pmb { x } = \pmb { 0 }$ and ${ \pmb x } = { \pmb \pi }$ , are kept at $\pmb { A }$ and $\pmb { B }$ , respectively. We shall compute the solution to this differential equation in the special case where $\pmb { A } = \pmb { 0 }$ and $\pmb { B } = \mathbf { 0 }$ . The expansion of $\pmb { f }$ into a trigonometric series will play a crucial role in the derivation of the solution.

Separation of Variables. To solve the heat equation, we use the technique of separation of variables, which assumes that the solution is of the form

$$
u ( x , t ) = X ( x ) T ( t )
$$

where $\pmb { T } ( t )$ is a function of ${ \pmb t } \geq { \bf 0 }$ and $\pmb { X } ( \pmb { x } )$ is a function of $\pmb { x }$ , $0 \leq x \leq \pi$ . Inserting this expression for $\pmb { u }$ into the differential equation $u _ { t } = u _ { x x }$ yields

$$
X ( x ) T ^ { \prime } ( t ) = X ^ { \prime \prime } ( x ) T ( t ) \quad { \mathrm { o r } } \quad { \frac { T ^ { \prime } ( t ) } { T ( t ) } } = { \frac { X ^ { \prime \prime } ( x ) } { X ( x ) } } .
$$

The left side depends only on $\pmb { t }$ and the right side depends only on $\pmb { x }$ The only way these two functions can equal each other for all values of $\pmb { x }$ and $\pmb { t }$ is if both functions are constant (since $\pmb { x }$ and $\pmb { t }$ are independent variables). So we obtain the following two equations:

$$
{ \frac { T ^ { \prime } ( t ) } { T ( t ) } } = c \qquad { \frac { X ^ { \prime \prime } ( x ) } { X ( x ) } } = c
$$

where $^ { c }$ is a constant. From the equation ${ \pmb T } ^ { \prime } = { \pmb c T }$ , we obtain $T ( t ) = C e ^ { \alpha t }$ , for some constant $^ { c }$ From physical considerations, the constant c must be negative [otherwise $| T ( t ) |$ and hence the temperature $| { \boldsymbol u } ( { \boldsymbol x } , t ) |$ would increase to

infinity as $t \to \infty ]$ .So we write $c = - \lambda ^ { 2 } < 0$ and we have $T ( t ) = C e ^ { - \lambda ^ { 2 } t }$ .The differential equation for $\pmb { X }$ becomes

$$
X ^ { \prime \prime } ( x ) + \lambda ^ { 2 } X ( x ) = 0 , \ 0 \leq x \leq \pi , \qquad X ( 0 ) = 0 , \ X ( \pi ) = 0 .
$$

The boundary conditions $X ( 0 ) = 0 = X ( \pi ) \quad$ arise because the temperature $u ( x , t ) = X ( x ) T ( t )$ is assumed to be zero at ${ \pmb x } = { \bf 0 } , \ { \pmb \pi }$ The solution to this differential equation is

$$
\begin{array} { r } { X ( x ) = a \cos ( \lambda x ) + b \sin ( \lambda x ) . } \end{array}
$$

The boundary condition $\mathbf { \boldsymbol { X } } ( 0 ) = \mathbf { 0 }$ implies that the constant $\pmb { a }$ must be zero. The boundary condition $0 = X ( \pi ) = b \sin ( \lambda \pi )$ implies that $\lambda$ must be an integer, which we label $\pmb { k }$ .Note that we do not want to set $\pmb { b }$ equal to zero, for if both $\pmb { a }$ and b were zero, the function $\pmb { X }$ would be zero and hence the temperature $\pmb { u }$ . would be zero. This would only make sense if the initial temperature of the rod, $\pmb { f } ( \pmb { x } )$ , is zero.

To summarize, we have shown that the only allowable value of $\lambda$ is an integer $\pmb { k }$ with corresponding solutions $X _ { k } ( x ) = b _ { k } \sin ( k x )$ and $T _ { k } ( t ) = e ^ { - k ^ { 2 } t }$ Each function

$$
u _ { k } ( x , t ) = X _ { k } ( x ) T _ { k } ( t ) = b _ { k } e ^ { - k ^ { 2 } t } \sin ( k x )
$$

is a solution to the heat equation and satisfies the boundary condition $u ( 0 , t ) =$ $u ( \pi , t ) = 0$ The only missing requirement is the initial condition ${ \pmb u } ( { \pmb x } , { \bf 0 } ) = { \pmb f } ( { \pmb x } )$ , which we can arrange by considering the sum of the ${ \pmb u } _ { { \pmb k } }$ :

$$
\begin{array} { l } { { \displaystyle u ( x , t ) = \sum _ { k = 1 } ^ { \infty } u _ { k } ( x , t ) } } \\ { { \displaystyle \qquad = \sum _ { k = 1 } ^ { \infty } b _ { k } e ^ { - k ^ { 2 } t } \sin ( k x ) . } } \end{array}
$$

Setting ${ \pmb u } ( { \pmb x } , { \pmb t } = { \pmb 0 } )$ equal to $\pmb { f } ( \pmb { x } )$ , we obtain the equation

$$
f ( x ) = \sum _ { k = 1 } ^ { \infty } b _ { k } \sin ( k x ) .
$$

Equation (1.4) is called a Fourier sine expansion of $\pmb { f }$ In the coming sections, we describe how to find such expansions (i.e., how to find the $\scriptstyle b _ { k }$ ). Once found, the Fourier coefficients (the $\pmb { b _ { k } }$ )can be substituted into (1.3) to give the complete solution to the heat equation.

Thus, the problem of expanding a function in terms of sines and cosines is an important one, not only from a historical perspective but also for practical problems in signal analysis and partial differential equations.

# 1.2 Computation of Fourier Series

# 1.2.1 On the Interval $- \pi \leq x \leq \pi$

In this section, we compute the Fourier coefficients, ${ \pmb a } _ { \pmb k }$ and $\scriptstyle b _ { k }$ , in the Fourier series

$$
f ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) .
$$

We need the following result on the orthogonality of the trigonometric functions.

THEOREM 1.1 The following integral relations hold:

$$
{ \begin{array} { r l } & { { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } \cos ( n x ) \cos ( k x ) d x = { \Biggl \{ } { \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } n = k \geq 1 } \\ { 2 } & { { \mathrm { i f ~ } } n = k = 0 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} } } \\ & { { \Biggr . } { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } \sin ( n x ) \sin ( k x ) d x = { \Biggl \{ } { \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } n = k \geq 1 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} } } \\ & { { \Biggr \} } \\ & { { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } \cos ( n x ) \sin ( k x ) d x = 0 \quad { \mathrm { f o r ~ a l l ~ i n t e g e r s ~ } } n , } \end{array} } }
$$

An equivalent way of stating this theorem is that the collection

$$
\left\{ \ldots , { \frac { \cos ( 2 x ) } { \sqrt { \pi } } } , { \frac { \cos ( x ) } { \sqrt { \pi } } } , { \frac { 1 } { \sqrt { 2 \pi } } } , { \frac { \sin ( x ) } { \sqrt { \pi } } } , { \frac { \sin ( 2 x ) } { \sqrt { \pi } } } , \ldots \right\}
$$

is an orthonormal set of functions in $L ^ { 2 } ( [ - \pi , \pi ] )$ .

Proof The erivations of the first two equalities use the following identtis:

$$
\begin{array} { r } { \cos ( ( n + k ) x ) = \cos n x \cos k x - \sin n x \sin k x } \\ { \cos ( ( n - k ) x ) = \cos n x \cos k x + \sin n x \sin k x . } \end{array}
$$

Adding these two identities and integrating gives

$$
\int _ { - \pi } ^ { \pi } \cos { n x } \cos { k x } d x = { \frac { 1 } { 2 } } \int _ { - \pi } ^ { \pi } \left( \cos ( ( n + k ) x + \cos ( ( n - k ) x ) ) \ d x . \right.
$$

The right side can be easily integrated. If $\pmb { n } \neq \pmb { k }$ , then

$$
\int _ { - \pi } ^ { \pi } \cos { n x } \cos { k x } d x = { \frac { 1 } { 2 } } \left. \left[ { \frac { \sin ( n + k ) x } { n + k } } + { \frac { \sin ( n - k ) x } { n - k } } \right] \right| _ { - \pi } ^ { \pi } = 0 .
$$

If $\pmb { n } = \pmb { k } \geq \pmb { 1 }$ , then

$$
\int _ { - \pi } ^ { \pi } \cos ^ { 2 } n x d x = \int _ { - \pi } ^ { \pi } ( 1 / 2 ) ( 1 + \cos 2 n x ) d x = \pi .
$$

If $\pmb { n } = \pmb { k } = \pmb { 0 }$ , then (1.5) reduces to $\textstyle ( 1 / \pi ) \int _ { - \pi } ^ { \pi } 1 d x = 2$ This completes the proof of (1.5).

Equation (1.6) follows by subtracting the equations (1.9) and (1.10) and then integrating as before. Equation (1.7) follows from the fact that $\cos ( n x ) \sin ( k x )$ is odd for $\pmb { k } > \mathbf { 0 }$ (see Lemma 1.7). $\bullet$

Now we use the orthogonality relations given in (1.5) through (1.7) to compute the Fourier coefficients. We start with the equation

$$
\cdot f ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) .
$$

To find $a _ { n }$ , we multiply both sides by $( \cos n x ) / \pi$ and integrate:

$$
{ \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \mathrm { c o s } n x d x = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } \left( a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \mathrm { c o s } ( k x ) + b _ { k } \mathrm { s i n } ( k x ) \right) \mathrm { c o s } n x d x .
$$

From equations (1.5) through (1.7), only the cosine terms with $\scriptstyle n = k$ contribute to the right side, and we obtain

$$
{ \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \cos { n x } d x = a _ { n } \quad n \geq 1 .
$$

Similarly, by multiplying equation (1.11) by sinnx and integrating, we obtain

$$
{ \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \sin { n x } d x = b _ { n } n \geq 1 .
$$

As a special case, we compute ${ \pmb a } _ { \mathbf { 0 } }$ by integrating equation (1.11) to give

$$
{ \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( x ) d x = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } \left( a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) \right) d x .
$$

Each sin and cos term integrates to zero and therefore

$$
{ \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( x ) d x = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } a _ { 0 } d x = a _ { 0 } .
$$

We summarize this discussion in the following theorem.

THEOREM 1.2 I $\begin{array} { r } { { } ^ { \textsf { \textsf { f } } } f ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) , } \end{array}$ ,then

$$
\begin{array} { l } { \displaystyle a _ { 0 } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( x ) d x } \\ { \displaystyle a _ { n } = \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } f ( x ) \cos ( n x ) d x } \\ { \displaystyle b _ { n } = \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } f ( x ) \sin ( n x ) d x . } \end{array}
$$

The $\mathbf { a } _ { n }$ and $b _ { n }$ are called the Fourier coefficients of the function $\pmb { f }$ .

Remark. The crux of the proof of Theorem 1.2 is that the collection in (1.8) is orthonormal. Thus, Theorem 0.21 guarantees that the Fourier coefficients ${ a _ { n } }$ and $b _ { n }$ are obtained by orthogonally projecting $\pmb { f }$ onto the space spanned by cosnx and sinnx, respectively. In fact, note that ${ a _ { n } }$ and $\pmb { b _ { n } }$ are (up to a factor of $1 / \pi )$ the $L ^ { 2 }$ inner products of $\pmb { f } ( \pmb { x } )$ with $\cos n x$ and $\sin n x$ respectively, as provided by Theorem 0.21. Thus, the preceding proof is a repeat of the proof of Theorem 0.21 for the special case of the $L ^ { 2 }$ inner product and where the orthonormal collection (the $e _ { j }$ )is given in (1.8).

Keep in mind that we have only shown that if $\pmb { f }$ can be expressed as a trigonometric sum, then the coefficients, $a _ { n }$ and $b _ { n }$ , are given by the preceding formulas. We will show (Theorem 1.22) that most functions on the interval $[ - \pi , \pi ]$ can be expressed as trigonometric sums. Note that Theorem 1.2 implies that the Fourier coefficients for a given function are unique.

# 1.2.2 Other Intervals

Intervals of Length $2 \pi$ In Theorem 1.2, the interval of interest is $[ - \pi , \pi ]$ . As we show in this section, Theorem 1.2 also holds for any interval of length $\mathbf { 2 \pi } \pi$ We need the following lemma.

LEMMA 1.3 Suppose $\pmb { F }$ is any $\scriptstyle 2 \pi$ -periodic function and c is any real number; then

$$
\int _ { - \pi + c } ^ { \pi + c } F ( x ) d x = \int _ { - \pi } ^ { \pi } F ( x ) d x .
$$

Proof A simple proof of this lemma is described graphically by Figure 1. If ${ \pmb F } \geq { \bf 0 }$ ,the left side of (1.15) represents the area under the graph of $\pmb { F }$ from $x = - \pi + c$ to $x = \pi + c$ whereas the right side of (1.15) represents the area under the graph of $\pmb { F }$ from $\pmb { x } = - \pmb { \pi }$ to ${ \pmb x } = { \pmb \pi }$ Since $\pmb { F }$ is $2 \pi$ -periodic, the shaded regions in Figure 1 are the same. The process of transferring the left shaded region to the right shaded region transforms the integral on the right side of (1.15) to the left.

An analytical proof of this lemma is outlined in Exercise 21.

Using this lemma with $F ( x ) = f ( x ) \cos n x$ or $f ( x ) \sin n x$ , we see that the integration formulas in Theorem 1.2 hold for any interval of the form $[ - \pi + c , \pi + c ]$

Intervals of General Length. We can also consider intervals of the form $- a \leq x \leq a ;$ ,of length $\mathbf { 2 } \mathbf { a }$ The basic building blocks are $\cos ( n \pi x / a )$ and $\sin ( n \pi x / a )$ , which have period $\mathbf { 2 } \pmb { a }$ . Note that when ${ \pmb { a } } = { \pmb { \pi } }$ ,these functions reduce to cosnx and $\sin n x$ ,which form the basis for Fourier series on the interval $[ - \pi , \pi ]$ considered in Theorem 1.2.

The following scaling argument can be used to transform the integral formulas for the Fourier coefficients on the interval $[ - \pi , \pi ]$ to the interval $[ - a , a ]$

![](images/185dc0308f5b437279317fb403c4d6284014a559e222d09fb6afcb5b4495f056.jpg)  
Figure 1 Region between $- \pi$ and $- \pi + c$ has same area as between $\pmb { \pi }$ and $\pi + c$ .

Suppose ${ \pmb F }$ is a function defined on the interval $- \pi \leq x \leq \pi$ The substitution $x = t \pi / a , d x = \pi d t / a$ leads to the following change of variables formula:

$$
{ \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } F ( x ) d x = { \frac { 1 } { a } } \int _ { - a } ^ { a } F ( { \frac { \pi t } { a } } ) d t .
$$

By using this change of variables, the following theorem can be derived from Theorem 1.2. (See Exercise 13.)

TheOreM 1.4 If $\begin{array} { r } { f ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k \pi x / a ) + b _ { k } \sin ( k \pi x / a ) } \end{array}$ on the interval $- a \leq x \leq a$ , then

$$
\begin{array} { l } { \displaystyle a _ { 0 } = \frac { 1 } { 2 a } \int _ { - a } ^ { a } f ( t ) d t } \\ { \displaystyle a _ { n } = \frac { 1 } { a } \int _ { - a } ^ { a } f ( t ) \cos ( n \pi t / a ) d t } \\ { \displaystyle b _ { n } = \frac { 1 } { a } \int _ { - a } ^ { a } f ( t ) \sin ( n \pi t / a ) d t . } \end{array}
$$

# EXAMPLE 1.5

Let

$$
f ( x ) = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } 0 \leq x \leq 1 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

We will compute the formal Fourier series for $\pmb { f }$ valid on the interval $- 2 \leq x \leq 2$ . With ${ \pmb a } = { \pmb 2 }$ in Theorem 1.4, the Fourier cosine coefficients are

$$
a _ { 0 } = { \frac { 1 } { 4 } } \int _ { - 2 } ^ { 2 } f ( t ) d t = { \frac { 1 } { 4 } } \int _ { 0 } ^ { 1 } 1 d t = { \frac { 1 } { 4 } }
$$

and for $\pmb { n } \geq \pmb { 1 }$

$$
a _ { n } = \frac { 1 } { 2 } \int _ { - 2 } ^ { 2 } f ( t ) \cos \pi \pi t / 2 d t = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \cos \pi \pi t / 2 d t = \frac { \sin ( n \pi / 2 ) } { n \pi } .
$$

When $\pmb { n }$ is even, these coefficients are zero. When $n = 2 k + 1$ is odd, then $\sin ( n \pi / 2 ) = ( - 1 ) ^ { k }$ Therefore,

$$
a _ { n } = \frac { ( - 1 ) ^ { k } } { ( 2 k + 1 ) \pi } , \quad ( n = 2 k + 1 ) .
$$

Similarly,

$$
b _ { n } = \frac { 1 } { 2 } \int _ { - 2 } ^ { 2 } f ( t ) \sin n \pi t / 2 d t = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \sin n \pi t / 2 d t = \frac { - 1 } { n \pi } \left( \cos n \pi / 2 - 1 \right)
$$

$$
\left\{ \begin{array} { l l } { { \mathrm { w h e n } ~ n = 4 j , b _ { n } = 0 } } \\ { { } } \\ { { \mathrm { w h e n } ~ n = 4 j + 1 , b _ { n } = \displaystyle { \frac { 1 } { ( 4 j + 1 ) \pi } } } } \\ { { } } \\ { { \mathrm { w h e n } ~ n = 4 j + 2 , b _ { n } = \displaystyle { \frac { 1 } { ( 2 j + 1 ) \pi } } } } \\ { { } } \\ { { \mathrm { w h e n } ~ n = 4 j + 3 \mathrm { g e t } ~ \displaystyle { \frac { 1 } { ( 4 j + 3 ) \pi } } . } } \end{array} \right.
$$

Thus, the Fourier series for $\pmb { f }$ is

$$
F ( x ) = a _ { 0 } + \sum _ { n = 1 } ^ { \infty } a _ { n } \cos ( n \pi x / 2 ) + b _ { n } \sin ( n \pi x / 2 )
$$

with $a _ { n } , b _ { n }$ given as above.

In later sections, we take up the question of whether or not the Fourier series $\pmb { F } ( \pmb { x } )$ for $\pmb { f }$ equals $\pmb { f } ( \pmb { x } )$ itself.

# 1.2.3 Cosine and Sine Expansions

Even and Odd Functions

DEFInITIoN 1.6 Let $\pmb { f } : \pmb { R }  \pmb { R }$ be a function; $\pmb { f }$ is even if $f ( - x ) = f ( x ) ; f$ is odd if $f ( - x ) = - f ( x )$

![](images/b84892d86e7ff81589bfd09c374f0d7d72b01e89bb9baf3f95692cfa73c9d1dc.jpg)  
Figure 2 Even function: $f ( - x ) = f ( x )$

![](images/a0efd7b752b98a7686fb1fa554f26b416df68ac3b790169f88f4cc849fc4b550.jpg)  
Figure 3 Odd function: $f ( - x ) = - f ( x )$

The graph of an even function is symmetric about the $\pmb { y }$ -axis, as illustrated in Figure 2. Examples include $f ( x ) = x ^ { 2 }$ (or any even power) and $\pmb { f } ( \pmb { x } ) = \cos \pmb { x }$ . The graph of an odd function is symmetric about the origin, as illustrated in Figure 3. Examples include $f ( x ) = x ^ { 3 }$ (or any odd power) and $f ( x ) = \sin x$ .

The following properties follow from the definition.

$$
{ \begin{array} { r l } & { \mathbf { E v e n } \times \mathbf { E v e n } = \mathbf { E v e n } } \\ & { \mathbf { E v e n } \times \mathbf { O d d } = \mathbf { O d d } } \\ & { \mathbf { O d d } \times \mathbf { O d d } = \mathbf { E v e n } . } \end{array} }
$$

For example, if $\pmb { f }$ is even and $\pmb { \mathscr { g } }$ is odd, then $g ( - x ) f ( - x ) = - g ( x ) f ( x )$ and so $\pmb { f } \pmb { g }$ is odd.

Another important property of even and odd functions is given in the next lemma.

# LEMMA 1.7

If $\pmb { F }$ is an even function, then

$$
\int _ { - a } ^ { a } F ( x ) d x = 2 \int _ { 0 } ^ { a } F ( x ) d x .
$$

•If $\pmb { F }$ is an odd function, then

$$
\int _ { - a } ^ { a } F ( x ) d x = 0 .
$$

This lemma follows easily from Figures 2 and 3. If $\pmb { F }$ is even, then the integral over the left half interval $[ - a , 0 ]$ is the same as the integral over the right half interval $[ 0 , a ]$ Thus, the integral over $[ - a , a ]$ is twice the integral over $[ 0 , a ]$ .If $\pmb { F }$ is odd, then the integral over the left half interval $[ - a , 0 ]$ cancels with the integral over the right half interval $[ 0 , a ]$ In this case, the integral over $[ - a , a ]$ is zero. $\bullet$

If the Fourier series of a function only involves the cosine terms, then it must be an even function (since cosine is even). Likewise, a Fourier series that only involves sines must be odd. The converse of this fact is also true, which is the content of the next theorem.

# THEOREM 1.8

If $\pmb { f } ( \pmb { x } )$ is an even function, then its Fourier series on the interval $[ - a , a ]$ $\begin{array} { r } { f ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k \pi x / a ) } \end{array}$ with

$$
\begin{array} { l } { { a _ { 0 } = \displaystyle \frac { 1 } { a } \int _ { 0 } ^ { a } f ( x ) d x } } \\ { { \displaystyle a _ { k } = \displaystyle \frac { 2 } { a } \int _ { 0 } ^ { a } f ( x ) \cos ( k \pi x / a ) d x . } } \end{array}
$$

If $\pmb { f } ( \pmb { x } )$ is an odd function, then its Fourier series will only involve sines. That is, $\begin{array} { r } { f ( x ) = \sum _ { k = 1 } ^ { \infty } b _ { k } \sin ( k \pi x / a ) } \end{array}$ with

$$
b _ { k } = { \frac { 2 } { a } } \int _ { 0 } ^ { a } f ( x ) \mathrm { s i n } ( k \pi x / a ) d x .
$$

Proof This theorem follows from Lemma 1.7 and Theorem 1.2. If $\pmb { f }$ is even, then $f ( x ) \cos n \pi x / a$ is even and so its integral over $[ - a , a ]$ equals twice the integral over $[ 0 , a ]$ .In addition, $f ( x ) \sin { n \pi x } / a$ is odd and so its integral over $[ - a , a ]$ is zero. The second part follows similarly. $\bullet$

Fourier Cosine and Sine Series on a Half-Interval. Suppose $\pmb { f }$ is defined on the interval $[ 0 , a ]$ By considering even or odd extensions of $f ,$ we can expand $\pmb { f }$ as a cosine or sine series. To express $\pmb { f }$ as a cosine series, we consider the even extension of $\pmb { f }$

$$
f _ { e } ( x ) = { \left\{ \begin{array} { l l } { f ( x ) } & { { \mathrm { i f ~ } } 0 \leq x \leq a } \\ { f ( - x ) } & { { \mathrm { i f ~ } } - a \leq x < 0 . } \end{array} \right. }
$$

The function $f _ { e }$ is an even function defined on $[ - a , a ]$ Therefore, only cosine terms appear in its Fourier expansion:

$$
f _ { e } ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos k \pi x / a \quad - a \leq x \leq a
$$

where $\pmb { a } _ { k }$ is given in Theorem 1.8. Since $f _ { e } ( x ) = f ( x )$ for ${ \mathfrak { o } } \leq x \leq { \mathfrak { a } }$ ,the integral formulas in Theorem 1.8 only involve $\pmb { f } ( \pmb { x } )$ rather than ${ f _ { e } } ( x )$ and so (1.16) becomes

$$
f ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos k \pi x / a \quad 0 \leq x \leq a
$$

with

$$
\begin{array} { l } { { a _ { 0 } = \displaystyle \frac { 1 } { a } \int _ { 0 } ^ { a } f ( x ) d x } } \\ { { \displaystyle a _ { k } = \frac { 2 } { a } \int _ { 0 } ^ { a } f ( x ) \cos ( k \pi x / a ) d x . } } \end{array}
$$

Likewise, to express $\pmb { f }$ as a sine series, then we consider the odd extension of $\pmb { f }$ :

$$
f _ { o } ( x ) = \left\{ { \begin{array} { l l } { f ( x ) } & { { \mathrm { i f ~ } } 0 \leq x \leq a } \\ { - f ( - x ) } & { { \mathrm { i f ~ } } - a \leq x < 0 . } \end{array} } \right.
$$

The odd function, $f _ { \circ }$ , has only sine terms in its Fourier expansion.Since $\pmb { f _ { 0 } } ( \pmb { x } ) =$ $\pmb { f } ( \pmb { x } )$ for $\mathbf { 0 } \leq x \leq a$ , we obtain the following sine expansion for $\pmb { f }$ :

$$
f ( x ) = \sum _ { k = 1 } ^ { \infty } b _ { k } \sin k \pi x / a \quad 0 < x \leq a
$$

where $\scriptstyle b _ { k }$ is given in Theorem 1.8:

$$
b _ { k } = { \frac { 2 } { a } } \int _ { 0 } ^ { a } f ( x ) \sin ( k \pi x / a ) d x .
$$

The examples in the next section will clarify these ideas.

# 1.2.4 Examples

Let $\pmb { f }$ be a function and let ${ \pmb F } ( { \pmb x } )$ be its Fourier series on $[ - \pi , \pi ]$ :

$$
\begin{array} { c } { { F ( x ) = a _ { 0 } + \displaystyle \sum _ { n = 1 } ^ { \infty } a _ { n } \cos n x + b _ { n } \sin n x } } \\ { { = a _ { 0 } + \displaystyle \operatorname* { l i m } _ { N  \infty } \displaystyle \sum _ { n = 1 } ^ { N } a _ { n } \cos n x + b _ { n } \sin n x } } \end{array}
$$

where ${ a _ { n } }$ and $\pmb { b _ { n } }$ are the Fourier coefficients of $\pmb { f }$ We say that the Fourier series converges if the preceding limit exists (as $N \to \infty$ ).Theorems 1.2 and 1.4 only compute the Fourier series of a given function. We have not yet shown that a given Fourier series converges (or what it converges to). In Theorems 1.22 and 1.28, we show that under a mild hypothesis on the differentiability of $\pmb { f }$ ,the following principle holds:

Let $\pmb { f }$ be a $2 \pi$ -periodic function.

If $\pmb { f }$ is continuous at a point $\pmb { x }$ , then its Fourier series, ${ \pmb F } ( { \pmb x } )$ , converges and $F ( x ) = f ( x )$

• If $\pmb { f }$ is not continuous at a point $\pmb { x }$ , then ${ \pmb F } ( { \pmb x } )$ converges to the average of the left and right limits of $\pmb { f }$ at $\pmb { x }$ ;that is,

$$
F ( x ) = { \frac { 1 } { 2 } } \left( \operatorname* { l i m } _ { t \to x ^ { - } } f ( t ) + \operatorname* { l i m } _ { t \to x ^ { + } } f ( t ) \right) .
$$

The second statement includes the first because if $\pmb { f }$ is continuous at $\pmb { x }$ , then the left and right limits of $\pmb { f }$ are both equal to $\pmb { f } ( \pmb { x } )$ and so in this case, $F ( x ) = f ( x )$ .

Rigorous statements and proofs of Theorems 1.22 and 1.28 are given in the following sections. In this section, we present several examples to gain insight into the computation of Fourier series and the rate at which Fourier series converge.

# EXaMPLe 1.9

Consider the function $\pmb { f } ( \pmb { x } ) = \pmb { x }$ on $- \pi \leq x < \pi$ This function is odd and so only the sine coefficients are nonzero. Its Fourier coefficients are

$$
{ \begin{array} { r l } & { b _ { k } = { \frac { 1 } { \pi } } \displaystyle \int _ { - \pi } ^ { \pi } x \sin ( k x ) d x } \\ & { \quad = { \frac { 2 ( - 1 ) ^ { k + 1 } } { k } } \quad \quad { \mathrm { ( u s i n g ~ i n t e g r a t i o n ~ b y ~ p a r t s ) } } } \end{array} }
$$

and so its Fourier series for the interval $[ - \pi , \pi ]$ is

$$
F ( x ) = \sum _ { k = 1 } ^ { \infty } { \frac { 2 ( - 1 ) ^ { k + 1 } } { k } } \sin ( k x ) .
$$

The function $\pmb { f } ( \pmb { x } ) = \pmb { x }$ is not $2 \pi$ -periodic. Its periodic extension, $\tilde { f } _ { i }$ is given in Figure 4. According to the preceding principle, ${ \pmb F } ( { \pmb x } )$ converges to $\tilde { f } ( x )$ ,at points where $\tilde { \pmb f }$ is continuous. At points of discontinuity of $\tilde { f }$ b $( x = \cdots - \pi , \pi , \ldots ) ,$ $\pmb { F } ( \pmb { x } )$ will converge to the average of the left and right limits of $\tilde { f } ( \boldsymbol x )$ For example, $\pmb { F } ( \pmb { \pi } ) = \mathbf { 0 }$ (since s $\mathbf { i n } k \pi = 0 $ , which is the average of the left and right limit of $\tilde { \pmb f }$ at ${ \pmb x } = { \pmb \pi }$ .

![](images/f5cb438dc42f4279290fae220755fb4b318b0641bc39163c6d20fd391173e590.jpg)  
Figure 4 The $2 \pi$ -periodic extension of $\pmb { f } ( \pmb { x } ) = \pmb { x }$

To see how fast the partial sums of this Fourier series converges to $\tilde { f } ( \boldsymbol { x } )$ ,we graph the partial sum

$$
S _ { N } ( x ) = \sum _ { k = 1 } ^ { N } { \frac { 2 ( - 1 ) ^ { k + 1 } } { k } } \sin ( k x )
$$

for various values of $\pmb { N }$ .The graph of

$$
S _ { 1 0 } ( x ) = \sum _ { k = 1 } ^ { 1 0 } { \frac { 2 ( - 1 ) ^ { k + 1 } } { k } } \sin ( k x )
$$

is given in Figure 5 together with the graph of $\tilde { f } ( x )$ (the squiggly curve is the graph of $\scriptstyle S _ { 1 0 }$

First, notice that the accuracy of the approximation of $\tilde { f } ( x )$ by $S _ { 1 0 } ( x )$ gets worse the closer $\pmb { x }$ is to a point of discontinuity. For example, near ${ \pmb x } = { \pmb \pi }$ , the graph of $S _ { 1 0 } ( x )$ must travel from about ${ \pmb y } = { \pmb \pi }$ to $\pmb { y } = - \pmb { \pi }$ in a very short interval, resulting in a slow rate of convergence near ${ \pmb x } = { \pmb \pi }$ .

Second, notice the blips in the graph of the Fourier series just before and just after the points of discontinuity of $\pmb { f } ( \pmb { x } )$ (near ${ \pmb x } = { \pmb \pi }$ , for example). This effect is called the Gibbs phenomenon. An interesting fact about the Gibbs phenomenon is that the height of the blip is approximately the same no matter how many terms are considered in the partial sum. However, the width of the blip gets smaller as the number of terms increase. Figure 6 illustrates the Gibbs phenomenon for $\pmb { S _ { 5 0 } }$ (the first 50 terms of the Fourier expansion) for $\tilde { \pmb f }$ Exercise 28 explains the Gibbs effect in more detail.

![](images/91c9f9c77a3cb2700976a22a26c5a4fe3418dc91d84adb0694a76a48cc2f6677.jpg)  
Figure 5 Gibbs phenomenon for $\pmb { S _ { 1 0 } }$

![](images/70265f474b1fbb8801ee0f93dcc03612322c910f1ab824e93c33e8077da8fbde.jpg)  
Figure 6 Gibbs phenomenon for $\pmb { S _ { 5 0 } }$ in Example 1.9

# EXAMPLe 1.10

Consider the sawtooth wave illustrated in Figure 7. The formula for $\pmb { f }$ on the interval $\mathbf { 0 } \leq x \leq \pi$ given by

$$
f ( t ) = \left\{ { \begin{array} { l l } { x } & { { \mathrm { i f ~ } } 0 \leq x \leq \pi / 2 } \\ { \pi - x } & { { \mathrm { i f ~ } } \pi / 2 \leq x \leq \pi } \end{array} } \right.
$$

and extends to the interval $- \pi \leq x \leq 0$ as an even function (see Figure 7). Since $\pmb { f }$ is an even function, only the cosine terms are nonzero. Using Theorem 1.8, their coefficients are

$$
a _ { 0 } = { \frac { 1 } { \pi } } \int _ { 0 } ^ { \pi } f ( x ) d x = { \frac { \pi } { 4 } } \qquad { \mathrm { ( n o ~ i n t e g r a t i o n ~ i s ~ n e e d e d ) } }
$$

For ${ \dot { \pmb { j } } } > { \pmb { 0 } }$

$$
\begin{array} { l } { { a _ { j } = \displaystyle \frac { 2 } { \pi } \int _ { 0 } ^ { \pi } f ( x ) \mathrm { c o s } ( j x ) d x } } \\ { { \displaystyle = \frac { 2 } { \pi } \int _ { 0 } ^ { \frac { \pi } { 2 } } x \mathrm { c o s } ( j x ) d x + \frac { 2 } { \pi } \int _ { \frac { \pi } { 2 } } ^ { \pi } ( \pi - x ) \mathrm { c o s } ( j x ) d x . } } \end{array}
$$

After performing the necessary integrals, we have

$$
a _ { j } = \frac { 4 \cos ( j \pi / 2 ) - 2 \cos ( j \pi ) - 2 } { \pi j ^ { 2 } } \quad \mathrm { f o r ~ } j > 0 .
$$

![](images/3c3e81430b32d12ba07b220159613c9f15f23d2a201b7ff049bd54651b94bd29.jpg)  
Figure 7 Sawtooth wave

Only the $\pmb { a } _ { 4 k + 2 }$ are nonzero. These coefficients simplify to

$$
a _ { 4 k + 2 } = { \frac { - 2 } { \pi ( 2 k + 1 ) ^ { 2 } } } .
$$

So the Fourier series for the sawtooth wave is

$$
F ( x ) = { \frac { \pi } { 4 } } - { \frac { 2 } { \pi } } \sum _ { k = 0 } ^ { \infty } { \frac { 1 } { ( 2 k + 1 ) ^ { 2 } } } \cos ( ( 4 k + 2 ) x ) .
$$

The sawtooth wave is already periodic and it is continuous. Thus its Fourier series ${ \pmb F } ( { \pmb x } )$ equals the sawtooth wave, $\pmb { f } ( \pmb { x } )$ , for every $\pmb { x }$ by the principle stated at the beginning of this section. In addition, the rate of convergence is much faster than for the Fourier series in Example 1.9. To illustrate the rate of convergence, we plot the sum of the first two terms of its Fourier series

$$
S _ { 2 } ( x ) = \frac { \pi } { 4 } - \frac { 2 \cos ( 2 x ) } { \pi }
$$

in Figure 8.

The sum of just two terms of this Fourier series gives a more accurate approximation of the sawtooth wave than 10 or 50 or even 1000 terms of the Fourier series in the previous (discontinuous) example. Indeed, the graph of the first 10 terms of this Fourier series (given in Figure 9) is almost indistinguishable from the original function.

![](images/49ce4547590bb6ef0abd76e5fc7f8b2c31792594c0471e5961b71b123d024cca.jpg)  
Figure 8 Sum of first two terms of the Fourier series of the sawtooth

![](images/e07ee44504ec1c9a7b52d764b4f7d299f64675cbd6de9f97e556e7854561e949.jpg)  
Figure 9 Ten terms of the Fourier series of the sawtooth

# EXAMPLe 1.11

Let $f ( x ) = \sin ( 3 x ) + \cos ( 4 x )$ Since $\pmb { f }$ is already expanded in terms of sines and cosines, no work is needed to compute the Fourier series of $\pmb { f }$ [i.e., the Fourier series of $\pmb { f }$ is just $\sin ( 3 x ) + \cos ( 4 x ) ]$ . This example illustrates an important point. The Fourier coefficients are unique (Theorem 1.2 specifies exactly what the $\pmb { a } _ { \pmb { k } }$ and $\boldsymbol { b } _ { k }$ must be). Thus by inspection, ${ \pmb b _ { 3 } } = { \pmb 1 } .$ . $\alpha _ { 4 } = 1$ , and all other ${ \pmb a } _ { { \pmb k } }$ and $b _ { k }$ are zero. By uniqueness, these are the same values as would have been obtained by computing the integrals in Theorem 1.2 for the ${ \pmb { a } } _ { \pmb { k } }$ and $\boldsymbol { b } _ { \boldsymbol { k } }$ (but with much less work). •

# EXAMPLE 1.12

Let $f ( x ) = \sin ^ { 2 } ( x )$ ,In this example, $f$ is not written as a linear combination of sines and cosines, so there is some work to do. However, instead of computing the integrals in Theorem 1.2 for the ${ \pmb a } _ { { \pmb k } }$ and $\scriptstyle b _ { k }$ , we use a trigonometric identity

$$
\sin ^ { 2 } ( x ) = { \frac { 1 } { 2 } } ( 1 - \cos ( 2 x ) ) .
$$

The right side is the desired Fourier series for $\pmb { f }$ since it is a linear combination of $\cos ( k x )$ (here, $\scriptstyle { a _ { 0 } } = 1 / 2$ $a _ { 2 } = - 1 / 2$ and all other ${ \pmb a } _ { \pmb k }$ and $\boldsymbol { b } _ { \boldsymbol { k } }$ are zero).

# EXaMPle 1.13

To find the Fourier sine series for the function $f ( x ) = x ^ { 2 } + 1$ valid on the interval $\mathbf { 0 } \leq x \leq \mathbf { 1 }$ , we first extend $\pmb { f }$ as an odd function:

$$
f _ { o } ( x ) = { \left\{ \begin{array} { l l } { f ( x ) = x ^ { 2 } + 1 } & { { \mathrm { f o r ~ } } 0 \leq x \leq 1 } \\ { - f ( - x ) = - x ^ { 2 } - 1 } & { { \mathrm { f o r ~ } } - 1 \leq x \leq 0 . } \end{array} \right. }
$$

Then we use Theorem 1.8 to compute the Fourier coeficients for $f _ { o }$ .

$$
b _ { n } = 2 \int _ { 0 } ^ { 1 } f ( x ) \mathrm { s i n } ( n \pi x ) d x = 2 \int _ { 0 } ^ { 1 } ( x ^ { 2 } + 1 ) \mathrm { s i n } ( n \pi x ) d x .
$$

Note that the formula of the odd extension of $\pmb { f }$ to the interval $- 1 \leq x \leq 0$ is not needed for the computation of ${ \pmb b _ { n } }$ .Integration by parts (twice) gives

$$
b _ { n } = - 2 \frac { 2 n ^ { 2 } \pi ^ { 2 } ( - 1 ) ^ { n } - 2 ( - 1 ) ^ { n } + 2 - n ^ { 2 } \pi ^ { 2 } } { \pi ^ { 3 } n ^ { 3 } } .
$$

When $\scriptstyle n = 2 k$ is even, this simplifies to

$$
b _ { 2 k } = - \frac { 1 } { k \pi }
$$

and when $\pmb { n } = 2 k - 1$ is odd

$$
b _ { 2 k - 1 } = 2 \frac { 1 2 k ^ { 2 } \pi ^ { 2 } - 1 2 \pi ^ { 2 } k + 3 \pi ^ { 2 } - 4 } { \pi ^ { 3 } ( 2 k - 1 ) ^ { 3 } } .
$$

Thus the Fourier sine series for ${ \pmb x } ^ { 2 } + 1$ on the interval [0, 1] is

$$
F ( x ) = \sum _ { k = 1 } ^ { \infty } - \left( { \frac { 1 } { k \pi } } \right) \sin 2 k \pi x + 2 \left( { \frac { 1 2 k ^ { 2 } \pi ^ { 2 } - 1 2 \pi ^ { 2 } k + 3 \pi ^ { 2 } - 4 } { \pi ^ { 3 } ( 2 k - 1 ) ^ { 3 } } } \right) \sin ( 2 k - 1 ) \pi x .
$$

Now $f _ { o }$ is defined on the interval $\left[ - 1 , 1 \right]$ . Its periodic extension, $\tilde { f } _ { o }$ , is graphed on the interval $[ - 2 , 2 ]$ in in Figure 10. Its Fourier series, $\pmb { F } ( \pmb { x } )$ ,will converge to $\tilde { f } _ { o } ( x )$ at each point of continuity of $\tilde { f } _ { o }$ At each integer, $\tilde { f } _ { o }$ is discontinuous. By the principle stated at the beginning of this section, ${ \pmb F } ( { \pmb x } )$ will converge to zero at each integer value (the average of the left and right limits of $\tilde { f } _ { o }$ .This agrees with the value of ${ \pmb F }$ computed by using (1.17) [since sin $2 k \pi$ and $\sin ( 2 k - 1 ) \pi$ are zero for each integer $\pmb { k } ]$ A graph of $\pmb { F } ( \pmb { x } )$ is given in Figure 11. Note that since $\tilde { f } _ { o } ( x ) = f ( x )$ for $0 < x < \mathrm { \hat { 1 } }$ , the Fourier sine series ${ \pmb F } ( { \pmb x } )$ agrees with $f ( x ) = x ^ { 2 } + 1$ on the interval $0 < x < 1$ A partial sum of the first 30 terms of $\pmb { F } ( \pmb { x } )$ is given in Figure 12. •

![](images/722a9b2d675f7fd90d364711b72bd0c94fb09ec1b00727bdbe97b3ad55c06d02.jpg)  
Figure 10 Periodic odd extension of $f ( x ) = x ^ { 2 } + 1$

![](images/e08f0438c3bb0f991603263d43c1ba7df4e1af7ef2b9cf5ca2e82dd6d3171832.jpg)  
Figure 11 Graph of $\pmb { F }$ , the Fourier sine series of $f ( x ) = x ^ { 2 } + 1$

![](images/ae8d419c09983ed75240c817a53663c02a0e03c79f2b745d484db4fa8f01dde8.jpg)  
Figure 12 Graph of sum of first 30 terms of ${ \pmb F } ( { \pmb x } )$ .

# EXaMPLe 1.14

Solve the heat equation

$$
\begin{array} { r l r l } & { u _ { t } ( x , t ) = u _ { x x } ( x , t ) } & & { t > 0 , 0 \le x \le \pi } \\ & { u ( x , 0 ) = f ( x ) } & & { 0 \le x \le \pi } \\ & { u ( 0 , t ) = 0 } & & { u ( \pi , t ) = 0 . } \end{array}
$$

where $\pmb { f } ( \pmb { x } )$ is the sawtooth wave in Example 1.10; that is,

$$
f ( x ) = \left\{ { x \atop \pi - x } \right. \mathrm { i f } \ : 0 \leq x \leq \pi / 2
$$

From the discussion in Section 1.1.3, the solution to this problem is

$$
u ( x , t ) = \sum _ { k = 1 } ^ { \infty } b _ { k } e ^ { - k ^ { 2 } t } \sin ( k x ) .
$$

Setting $\pmb { t = 0 }$ in (1.18) and using ${ \pmb u } ( { \pmb x } , { \pmb 0 } ) = { \pmb f } ( { \pmb x } )$ we obtain

$$
f ( x ) = u ( x , 0 ) = \sum _ { k = 1 } ^ { \infty } b _ { k } \sin ( k x ) .
$$

Therefore, the $\scriptstyle b _ { k }$ must be chosen as the Fourier sine coefficients of ${ f ( x ) }$ ,which by Theorem 1.8 are

$$
b _ { k } = { \frac { 2 } { \pi } } \int _ { 0 } ^ { \pi } f ( t ) \sin ( k t ) d t .
$$

Inserting the formula for $\pmb { f }$ and computing the integral, we can show $b _ { k } = 0$ when $\pmb { k }$ is even. When $\pmb { k } = 2 j + 1$ is odd, then

$$
b _ { 2 j + 1 } = \frac { 4 ( - 1 ) ^ { j } } { \pi ( 2 j + 1 ) ^ { 2 } } .
$$

Substituting $\boldsymbol { b } _ { \boldsymbol { k } }$ into (1.18), the final solution is

$$
u ( x , t ) = \sum _ { j = 0 } ^ { \infty } { \frac { 4 ( - 1 ) ^ { j } } { \pi ( 2 j + 1 ) ^ { 2 } } } \sin ( ( 2 j + 1 ) x ) e ^ { - ( 2 j + 1 ) ^ { 2 } t } .
$$

# 1.2.5 The Complex Form of Fourier Series

Often, it is more convenient to express Fourier series in complex form using the complex exponentials, $e ^ { i n x }$ , $\boldsymbol { \mathscr { n } } \in \boldsymbol { \mathscr { Z } }$ , due to the simple computational properties of these functions. The complex exponential has the following definition.

DEFINItIoN 1.15 For any real number $\pmb { t }$ , the complex exponential is

$$
e ^ { i t } = \cos ( t ) + i \sin ( t )
$$

where $\scriptstyle { i = { \sqrt { - 1 } } }$ .

This definition is motivated by substituting $\mathbf { \hat { \mu } } _ { \mathbf { \hat { x } } } = \mathbf { \dot { \mu } } _ { \mathbf { \hat { x } } } \mathbf { \hat { t } }$ into the usual Taylor series for $e ^ { \pi }$ :

$$
\begin{array} { l } { { \displaystyle e ^ { x } = 1 + x + \frac { x ^ { 2 } } { 2 ! } + \frac { x ^ { 3 } } { 3 ! } + \frac { x ^ { 4 } } { 4 ! } + \cdots } } \\ { { \mathrm { ~ } } } \\ { { \mathrm { w i t h ~ } x = i t : \quad e ^ { i t } = 1 + ( i t ) + \frac { ( i t ) ^ { 2 } } { 2 ! } + \frac { ( i t ) ^ { 3 } } { 3 ! } + \frac { ( i t ) ^ { 4 } } { 4 ! } + \cdots } } \end{array}
$$

Collecting the real and imaginary parts, we obtain

$$
\begin{array} { l } { { e ^ { i t } = \displaystyle \left( 1 - \frac { t ^ { 2 } } { 2 ! } + \frac { t ^ { 4 } } { 4 ! } + \dots \right) + i \left( t - \frac { t ^ { 3 } } { 3 ! } + \frac { t ^ { 5 } } { 5 ! } - \dots \right) } } \\ { { = \displaystyle \cos ( t ) + i \sin ( t ) \qquad \mathrm { u s i n g ~ t h e ~ T a y l o r ~ e x p a n s i o n } } } \end{array}
$$

The next lemma shows that the familiar properties of the real exponential also hold for the complex exponential. These properties follow from the definition together with basic trigonometric identities and will be left to the exercises (see Exercise 14).

LEMMA 1.16 For all t, $\mathsf { \pmb { s } } \in \pmb { R }$ $\begin{array} { r l } & { \bullet \ e ^ { i ( t + 2 \pi ) } = e ^ { i t } } \\ & { \bullet \ | e ^ { i t } | = 1 } \\ & { \bullet \ \overline { { e ^ { i t } } } = e ^ { - i t } } \\ & { \bullet \ e ^ { i t } e ^ { i s } = e ^ { i ( t + s ) } } \\ & { \bullet \ e ^ { i t } / e ^ { i s } = e ^ { i ( t - s ) } } \\ & { \bullet \ \frac { d } { d t } \left\{ e ^ { i t } \right\} = i e ^ { i t } } \end{array}$

The next theorem shows that the complex exponentials are orthonormal in $L ^ { 2 } ( [ \pi , \pi ] )$

THeOreM 1.17 The set of functions

$$
\left\{ \frac { e ^ { i n t } } { \sqrt { 2 \pi } } , n = \ldots , - 2 , - 1 , 0 , 1 , 2 , \ldots \right\}
$$

is orthonormal in $L ^ { 2 } ( [ - \pi , \pi ] )$ .

Proof We must show

$$
\langle e ^ { i n t } , e ^ { i m t } \rangle _ { L ^ { 2 } } = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } e ^ { i n t } { \overline { { e ^ { i m t } } } } d t = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } n = m } \\ { 0 } & { { \mathrm { i f ~ } } n \neq m . } \end{array} \right. }
$$

Using the third, fourth, and sixth properties in Lemma 1.16, we have

$$
\begin{array} { r l } { \displaystyle \int _ { - \pi } ^ { \pi } e ^ { i n t } \overline { { e ^ { i m t } } } d t = \int _ { - \pi } ^ { \pi } e ^ { i n t } e ^ { - i m t } d t } \\ { \displaystyle } \\ { \displaystyle } \\ { \qquad = \int _ { - \pi } ^ { \pi } e ^ { i ( n - m ) t } d t } \\ { \displaystyle } \\ { \qquad = \left. \frac { e ^ { i ( n - m ) t } } { i ( n - m ) } \right| _ { - \pi } ^ { \pi } \quad } & { \mathrm { i f ~ } n \ne m } \\ { \displaystyle } \\ { \qquad = 0 . } \end{array}
$$

If $\mathscr { n } = \mathscr { m }$ , then $e ^ { i n t } e ^ { - i n t } = 1$ and so $\langle e ^ { i n t } , e ^ { i n t } \rangle = 2 \pi$ This completes the proof.

Combining this theorem with Theorem 0.21, we obtain the following complex version of Fourier series.

TheoreM 1.18 If $\begin{array} { r } { f ( t ) = \sum _ { n = - \infty } ^ { \infty } \alpha _ { n } e ^ { i n t } } \end{array}$ on the interval $- \pi \leq t \leq \pi$ , then

$$
\alpha _ { n } = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( t ) e ^ { - i n t } d t .
$$

# EXAMPLE 1.19

Consider the function

$$
f ( t ) = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } 0 \leq t < \pi } \\ { - 1 } & { { \mathrm { i f ~ } } - \pi \leq t < 0 . } \end{array} \right. }
$$

The nth complex Fourier coefficient is

$$
\begin{array} { l l l } { \displaystyle \alpha _ { n } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( t ) e ^ { - i n t } d t } \\ { \displaystyle } & { = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { \pi } e ^ { - i n t } d t - \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { 0 } e ^ { - i n t } d t } \\ { \displaystyle } & { = - \frac { i ( 1 - \cos ( n \pi ) ) } { n \pi } } \\ { \displaystyle } & { = \left\{ \begin{array} { l l } { \displaystyle \frac { - 2 i } { n \pi } } & { \mathrm { i f ~ } n \mathrm { i s ~ o d d } } \\ { \displaystyle 0 } & { \mathrm { i f ~ } n \mathrm { i s ~ e v e n . } } \end{array} \right. } \end{array}
$$

So the complex Fourier series of $\pmb { f }$ is

$$
\sum _ { n = - \infty } ^ { \infty } \alpha _ { n } e ^ { i n t } = \sum _ { k = - \infty } ^ { \infty } \frac { - 2 i } { ( 2 k + 1 ) \pi } e ^ { i ( 2 k + 1 ) t } .
$$

The complex form of Fourier series can be formulated on other intervals as well.

THEOreM 1.20 The set of functions

$$
\left\{ \frac { 1 } { \sqrt { 2 a } } e ^ { i n \pi t / a } , n = \cdots - 2 , - 1 , 0 , 1 , 2 , \ldots \right\}
$$

is an orthonormal basis for $L ^ { 2 } [ - a , a ]$ .If $\begin{array} { r } { f ( t ) = \sum _ { n = - \infty } ^ { \infty } \alpha _ { \mathrm { n } } e ^ { i n \pi t / a } } \end{array}$ then

$$
\alpha _ { n } = { \frac { 1 } { 2 a } } \int _ { - a } ^ { a } f ( t ) e ^ { - i n \pi t / a } d t .
$$

Relation between the Real and Complex Fourier Series. If $\pmb { f }$ is a real-valued function, the real form of its Fourier series can be derived from its complex form and vice versa. For simplicity, we discuss this derivation on the interval $- \pi \leq t \leq \pi$ ,but this discussion also holds for other intervals as well. We first decompose the complex form of the Fourier series of $\pmb { f }$ into positive and negative terms:

$$
f ( t ) = \sum _ { n = - \infty } ^ { - 1 } \alpha _ { n } e ^ { i n t } + \alpha _ { 0 } + \sum _ { n = 1 } ^ { \infty } \alpha _ { n } e ^ { i n t }
$$

where

$$
\alpha _ { n } = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( t ) e ^ { - i n t } d t .
$$

If $\pmb { f }$ is real valued, then $\alpha _ { - n } \doteq \overline { { \alpha _ { n } } }$ because

$$
\alpha _ { - n } = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( t ) e ^ { i n t } d t = { \frac { 1 } { 2 \pi } } { \overline { { \int _ { - \pi } ^ { \pi } f ( t ) e ^ { - i n t } d t } } } = { \overline { { \alpha _ { n } } } } .
$$

Therefore, (1.19) becomes

$$
f ( t ) = \alpha _ { 0 } + \left( \sum _ { n = 1 } ^ { \infty } \alpha _ { n } e ^ { i n t } \right) + \left( \sum _ { n = 1 } ^ { \infty } \alpha _ { n } e ^ { i n t } \right) .
$$

Since $\boldsymbol { z } + \overline { { \boldsymbol { z } } } = 2 \mathbf { R e } ( \boldsymbol { z } )$ for any complex number $\pmb { z }$ , this equation can be written as

$$
f ( t ) = \alpha _ { 0 } + 2 \mathrm { R e } \left( \sum _ { n = 1 } ^ { \infty } \alpha _ { n } e ^ { i n t } \right) .
$$

Now note the following relations between $\alpha _ { n }$ and the real Fourier coefficients, ${ \pmb a } _ { \pmb n }$ and $b _ { n }$ , given in Theorem 1.2:

$$
\begin{array} { l } { \displaystyle \alpha _ { 0 } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( t ) d t = a _ { 0 } } \\ { \displaystyle \alpha _ { n } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( t ) e ^ { - i n t } ~ \mathrm { f o r } ~ n \ge 1 } \\ { \displaystyle \quad = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( t ) ( \cos n t - i \sin n t ) d t } \\ { \displaystyle \quad = \frac { 1 } { 2 } ( a _ { n } - i b _ { n } ) . } \end{array}
$$

Using equation (1.20), we obtain

$$
{ \begin{array} { r l } & { f ( t ) = \alpha _ { 0 } + 2 \operatorname { R e } \left( \displaystyle \sum _ { n = 1 } ^ { \infty } \alpha _ { n } e ^ { i n t } \right) } \\ & { \qquad = a _ { 0 } + \operatorname { R e } \left( \displaystyle \sum _ { n = 1 } ^ { \infty } ( a _ { n } - i b _ { n } ) ( \cos n t + i \sin n t ) \right) } \\ & { \qquad = a _ { 0 } + \displaystyle \sum _ { n = 1 } ^ { \infty } a _ { n } \cos n t + b _ { n } \sin n t , } \end{array} }
$$

which is the real form of the Fourier series of $\pmb { f }$ These equations can also be stated in reverse order so that the complex form of its Fourier series can be derived from its real Fourier series.

# 1.3 Convergence Theorems for Fourier Series

In this section, we prove the convergence of Fourier series under mild assumptions on the original function $\pmb { f }$ The mathematics underlying convergence is somewhat involved. We start with the Riemann-Lebesgue lemma, which is important in its own right.

# 1.3.1 The Riemann-Lebesgue Lemma

In the examples in Section 1.2.4, the Fourier coefficients ${ \pmb a } _ { { \pmb k } }$ and $\boldsymbol { b } _ { \boldsymbol { k } }$ converge to zero as $\pmb { k }$ gets large. This is not a coincidence, as the following theorem shows.

THEOREM 1.21 Riemann-Lebesgue Lemma. Suppose $\pmb { f }$ is a piecewise continuous function on the interval $\ a \leq x \leq b$ . Then

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { a } ^ { b } f ( x ) \mathrm { c o s } ( k x ) d x = \operatorname* { l i m } _ { k \to \infty } \int _ { a } ^ { b } f ( x ) \mathrm { s i n } ( k x ) d x = 0 .
$$

By definition, a piecewise continuous function has only a finite number of discontinuities. This hypothesis can be weakened considerably.

Qne important consequence of Theorem 1.21 is that only a finite number of Fourier coefficients are larger (in absolute value) than any given positive number. This fact is the basic idea underlying the process of data compression. One way to compress a signal is first to express it as a Fourier series; then discard all the small Fourier coefficients and retain (or transmit) only the finite number of Fourier coefficients that are larger than some given threshold. (See Exercise 31 for an illustration of this process.) We encounter data compression again in future sections on the discrete Fourier transform and wavelets.

Proof The intuitive idea behind the proof is that as $\pmb { k }$ gets large, $\sin ( k x )$ and $\cos ( k x )$ oscillate much more rapidly than does $\pmb { f }$ (see Figure 13). If $\pmb { k }$ is large, $\pmb { f } ( \pmb { x } )$ is nearly constant on two adjacent periods of sin $\pmb { k x }$ or $\cos k x$ .The graph of the product of ${ \pmb f } ( { \pmb x } )$ with $\sin ( k x )$ is given in Figure 14. The integral over each period is almost zero, since the areas above and below the $\pmb { x } .$ -axis almost cancel.

![](images/323d9e3622a2552575284f9146696f1e8f57f0a08c511c5372749d6f6ca96925.jpg)  
Figure 13 Plot of both $\pmb { y } = \pmb { f } ( \pmb { x } )$ and ${ \mathfrak { y } } = \sin { k x }$

![](images/1d57598712b68ad6f207653624141cc5f1675eec321e4375cf603c69b71cc97a.jpg)  
Figure 14 Plot of ${ \pmb y } = { \pmb f } ( { \pmb x } ) \sin { \pmb k } { \pmb x }$

We give the following analytical proof of the theorem in the cäse of a differentiable function $\pmb { f }$ Consider the term

$$
\int _ { a } ^ { b } f ( x ) \cos ( k x ) d x .
$$

We integrate by parts with $\pmb { u } = \pmb { f }$ and $d v = \cos { k x }$ to obtain

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } f ( x ) \cos ( k x ) d x = \frac { \sin ( k x ) } { k } f ( x ) \Big \vert _ { a } ^ { b } - \displaystyle \int _ { a } ^ { b } \frac { \sin ( k x ) } { k } f ^ { \prime } ( x ) d x } \\ { \displaystyle \qquad = \frac { \sin ( k b ) f ( b ) - \sin ( k a ) f ( a ) } { k } - \displaystyle \int _ { a } ^ { b } \frac { \sin ( k x ) } { k } f ^ { \prime } ( x ) d x . } \end{array}
$$

As $\pmb { k }$ gets large in the denominator, the expression on the right converges to zero, and this completes the proof. $\bullet$

# 1.3.2 Convergence at a Point of Continuity

The sum appearing in a Fourier expansion generally contains an infinite number of terms (the Fourier expansions of Examples 1.11 and 1.12 are an exception). An infinite sum is, by definition, a limit of partial sums; that is,

$$
\sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) = \operatorname* { l i m } _ { N \to \infty } \sum _ { k = 1 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x )
$$

provided that the limit exists. Therefore, we say that the Fourier series of $\pmb { f }$ converges to $\pmb { f }$ at the point $\pmb { x }$ if

$$
f ( x ) = a _ { 0 } + \operatorname* { l i m } _ { N \to \infty } \sum _ { k = 1 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) .
$$

With this in mind, we state and prove our first theorem on the convergence of Fourier series.

THEOREM 1.22 Suppose $\pmb { f }$ is a continuous and $2 \pi$ -periodic function. Then for each point $\pmb { x }$ , where the derivative of $\pmb { f }$ is defined, the Fourier series of $\pmb { f }$ at $\pmb { x }$ converges to ${ f } ( x )$ .

Proof For a positive integer $\pmb { N }$ , let

$$
S _ { N } ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x )
$$

where ${ \pmb a } _ { \pmb k }$ and $b _ { k }$ are the Fourier coefficients of the given function $\pmb { f }$ Our ultimate goal is to show $S _ { N } ( x )  f ( x )$ as $N \to \infty$ , Before this can be done, we need to rewrite $s _ { N }$ into a different form. This process requires several steps.

Step 1. Substituting the Fourier Coefficients. After substituting the formulas for the $\scriptstyle a _ { k }$ and $\scriptstyle b _ { k }$ , (1.12) through (1.14), of Theorem 1.2, we obtain

$$
\begin{array} { l } { \displaystyle S _ { N } ( \boldsymbol { x } ) = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( t ) d t } \\ { \displaystyle \phantom { \frac { 1 } { \pi } \sum _ { k = 1 } ^ { N } \left( \int _ { - \pi } ^ { \pi } f ( t ) \cos ( k t ) \cos ( k x ) d t + \int _ { - \pi } ^ { \pi } f ( t ) \sin ( k t ) \sin ( k x ) d t \right) } } \\ { \displaystyle \phantom { \frac { 1 } { \pi } \sum _ { k = 1 } ^ { N } \int _ { - \pi } ^ { \pi } f ( t ) \left( \frac { 1 } { 2 } + \sum _ { k = 1 } ^ { N } \cos ( k t ) \cos ( k x ) + \sin ( k t ) \sin ( k x ) \right) d t . } } \end{array}
$$

Using the addition formula for the cosine function, $\cos ( A - B ) = \cos ( A ) \cos ( B ) +$ $\sin ( A ) \sin ( B )$ , we obtain

$$
S _ { N } ( x ) = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( t ) \left( { \frac { 1 } { 2 } } + \sum _ { k = 1 } ^ { N } \cos ( k ( t - x ) ) \right) d t .
$$

To evaluate the sum on the right side, we need the following lemma.

# Step 2. Evaluating the Fourier Kernel.

LEMMA 1.23 For.any number $\pmb { u }$ , $- \pi \leq u \leq \pi$ ,

$$
{ \frac { 1 } { 2 } } + \cos ( u ) + \cos ( 2 u ) + \cdots + \cos ( N u ) = { \left\{ \begin{array} { l l } { \displaystyle \frac { \sin ( ( N + 1 / 2 ) u ) } { 2 \sin ( u / 2 ) } } & { u \neq 0 } \\ { N + 1 / 2 } & { u = 0 . } \end{array} \right. }
$$

Proof of Lemma 1.23 Recall that the complex exponential is defined as $e ^ { i u } = \cos ( u ) + i \sin ( u )$ Note that

$$
( e ^ { i u } ) ^ { n } = e ^ { i n u } = \cos ( n u ) + i \sin ( n u ) .
$$

So cos $n u = \mathbb { R } \mathrm { e } \{ ( e ^ { i u } ) ^ { n } \}$ . We have

$$
\begin{array} { c } { { \displaystyle \frac { 1 } { 2 } + \cos ( u ) + \cos ( 2 u ) + \cdots + \cos ( N u ) } } \\ { { = \displaystyle \frac { - 1 } { 2 } + ( 1 + \cos ( u ) + \cos ( 2 u ) + \cdots + \cos ( N u ) ) } } \end{array}
$$

and so

$$
\frac { 1 } { 2 } + \sum _ { k = 1 } ^ { N } \cos k u = \frac { - 1 } { 2 } + \mathrm { R e } \left\{ \sum _ { k = 0 } ^ { N } ( e ^ { i u } ) ^ { k } \right\} .
$$

The suhe  i $\textstyle \sum _ { k = 0 } ^ { N } z ^ { k }$ , where $z = e ^ { i u }$ .

For any number $\pmb { z }$ , we have

$$
\sum _ { k = 0 } ^ { N } z ^ { k } = \frac { 1 - z ^ { N + 1 } } { 1 - z } .
$$

This formula is established as follows: Let

$$
s _ { N } = \sum _ { k = 0 } ^ { N } z ^ { k } .
$$

Then

$$
\begin{array} { l } { ( 1 - z ) s _ { N } = ( 1 - z ) ( 1 + z + z ^ { 2 } + \cdots + z ^ { N } ) } \\ { \qquad = ( 1 + z + \cdots + z ^ { N } ) - ( z + z ^ { 2 } + \cdots + z ^ { N + 1 } ) } \\ { \qquad = 1 - z ^ { N + 1 } . } \end{array}
$$

Dividing both sides by $( 1 - z )$ yields (1.23).

Applying (1.23) with $z = e ^ { i u }$ to (1.22), we obtain

$$
{ \frac { 1 } { 2 } } + \cos ( u ) + \cos ( 2 u ) + \cdots + \cos ( N u ) = { \frac { - 1 } { 2 } } + \operatorname { R e } \left\{ { \frac { 1 - e ^ { i ( N + 1 ) u } } { 1 - e ^ { i u } } } \right\} .
$$

To compute the expression on the right, we multiply the numerator and denominator by $e ^ { - i u / 2 }$ :

$$
\mathrm { R e } \left\{ \frac { 1 - e ^ { i ( N + 1 ) u } } { 1 - e ^ { i u } } \right\} = \mathrm { R e } \left\{ \frac { e ^ { - i u / 2 } - e ^ { i ( N + 1 / 2 ) u } } { e ^ { - i u / 2 } - e ^ { i u / 2 } } \right\} .
$$

The denominator on the right is $- 2 i \sin ( u / 2 )$ , so

$$
\mathrm { R e } \left\{ \frac { 1 - e ^ { i ( N + 1 ) u } } { 1 - e ^ { i u } } \right\} = \frac { \sin ( u / 2 ) + \sin ( ( N + 1 / 2 ) u ) } { 2 \sin ( u / 2 ) } .
$$

Inserting this equation into the right side of (1.24) gives

$$
{ \begin{array} { r l } & { { \frac { 1 } { 2 } } + \cos ( u ) + \cos ( 2 u ) + \cdots + \cos ( N u ) = { \frac { - 1 } { 2 } } + { \frac { \sin ( u / 2 ) + \sin ( ( N + 1 / 2 ) u ) } { 2 \sin ( u / 2 ) } } } \\ & { \qquad = { \frac { \sin ( ( N + 1 / 2 ) u ) } { 2 \sin ( u / 2 ) } } . } \end{array} }
$$

This completes the proof of Lemma 1.23.

Step 3. Evaluation of the Partial Sum of Fourier Series. Using Lemma 1.23 with $\pmb { u } = \pmb { t } - \pmb { x }$ , (1.21) becomes

$$
\begin{array} { l } { { S _ { N } ( x ) = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } f ( t ) \left( \frac { 1 } { 2 } + \sum _ { k = 1 } ^ { N } \cos ( k ( t - x ) ) \right) d t } } \\ { { \mathrm { ~ } = \displaystyle \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( t ) \left( \frac { \sin ( ( N + 1 / 2 ) ( t - x ) ) } { \sin ( ( t - x ) / 2 ) } \right) d t } } \\ { { \mathrm { ~ } = \displaystyle \int _ { - \pi } ^ { \pi } f ( t ) P _ { N } ( t - x ) d t } } \end{array}
$$

where we have let

$$
P _ { N } ( u ) = \frac { 1 } { 2 \pi } \frac { \sin ( ( N + 1 / 2 ) u ) } { \sin ( u / 2 ) } .
$$

Now use the change of variables $\pmb { u } = \pmb { t } - \pmb { x }$ in the preceding integral to obtain

$$
S _ { N } ( x ) = \int _ { - \pi - x } ^ { \pi - x } f ( u + x ) P _ { N } ( u ) d u .
$$

Since both $\pmb { f }$ and $P _ { N }$ are periodic with period $\mathbf { 2 \pi } \pi$ , the limits of integration can be shifted by $\pmb { x }$ without changing the value of the integral (see Lemma 1.3). Therefore,

$$
S _ { N } ( x ) = \int _ { - \pi } ^ { \pi } f ( u + x ) P _ { N } ( u ) d u .
$$

Next, we need the following lemma.

Step 4. Integrating the Fourier Kernel.

# LEMMA 1.24

$$
\int _ { - \pi } ^ { \pi } P _ { N } ( u ) d u = 1
$$

Proof of Lemma 1.24 We use Lemma 1.23 to write

$$
\begin{array} { l } { { \displaystyle P _ { N } ( u ) = \frac { 1 } { \pi } \frac { \sin ( ( N + 1 / 2 ) u ) } { 2 \sin ( u / 2 ) } } } \\ { { \displaystyle \phantom { \frac { 1 } { \pi } \frac { \sin ( ( N + 1 / 2 ) u ) } { 2 \sin ( u / 2 ) } } } } \\ { { \displaystyle \phantom { \frac { 1 } { \pi } \frac { \sin ( u ) } { 2 \sin ( u / 2 ) } } = \frac { 1 } { \pi } \left( \frac { 1 } { 2 } + \cos ( u ) + \cos ( 2 u ) + \cdots + \cos ( N u ) \right) . } } \end{array}
$$

Integrating this equation gives

$$
\int _ { - \pi } ^ { \pi } P _ { N } ( u ) d u = \int _ { - \pi } ^ { \pi } { \frac { 1 } { 2 \pi } } d u + { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } \cos ( u ) + \cos ( 2 u ) + \cdots + \cos ( N u ) d u .
$$

The second integral on the right is zero (since the antiderivatives involve sin which vanishes at multiples of $\pmb { \pi }$ ).The first integral on the right is one and the proof of the lemma is complete.

Step 5. The End of the Proof of Theorem 1.22. As indicated at the beginning of the proof, we must show that $S _ { N } ( x )  f ( x )$ as $N \to \infty$ Inserting the expression for $S _ { N } ( x )$ given in (1.26), we must show

$$
\int _ { - \pi } ^ { \pi } f ( u + x ) P _ { N } ( u ) d u \to f ( x ) .
$$

In view of Lemma 1.24, $\begin{array} { r } { f ( x ) = \int _ { - \pi } ^ { \pi } f ( x ) P _ { N } ( u ) d u } \end{array}$ and so we are reduced to showing

$$
\int _ { - \pi } ^ { \pi } ( f ( u + x ) - f ( x ) ) P _ { N } ( u ) d u \to 0 \quad \mathrm { a s } \quad N \to \infty .
$$

Using (1.25), the preceding limit becomes

$$
{ \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } \left( { \frac { f ( u + x ) - f ( x ) } { \sin ( u / 2 ) } } \right) \sin ( ( N + 1 / 2 ) u ) d u \to 0 .
$$

We can use the Riemann-Lebesgue lemma (see Theorem 1.21) to establish (1.28) provided that we show that the function

$$
g ( u ) = \frac { f ( u + x ) - f ( x ) } { \sin ( u / 2 ) }
$$

is continuous (as required by the Riemann-Lebesgue lemma). Here, $\pmb { x }$ is a fixed point and $\textbf { \em u }$ is the variable. The only possible value of $u \in [ - \pi , \pi ]$ where $\pmb { g } ( \pmb { u } )$ could be discontinuous is ${ \pmb u } = { \bf 0 }$ However, since $\begin{array} { r } { f ^ { \prime } ( x ) = \operatorname* { l i m } _ { u \to 0 } \frac { f ( u + x ) - f ( x ) } { u } } \end{array}$ exists by hypothesis, we have

$$
\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { u \to 0 } g ( u ) = \operatorname* { l i m } _ { u \to 0 } \frac { f ( u + x ) - f ( x ) } { \sin ( u / 2 ) } \qquad } \\ { \displaystyle \qquad = \operatorname* { l i m } _ { u \to 0 } \frac { f ( u + x ) - f ( x ) } { u } \frac { u / 2 } { \sin ( u / 2 ) } \cdot 2 \qquad } \\ { \displaystyle \qquad = f ^ { \prime } ( x ) \cdot 1 \cdot 2 \quad ( \mathrm { b e c a u s e ~ } \operatorname* { l i m } _ { t \to 0 } \frac { t } { \sin t } = 1 ) \qquad } \\ { \displaystyle \qquad = 2 f ^ { \prime } ( x ) . } \end{array}
$$

Thus $\pmb { g } ( \pmb { u } )$ extends across ${ \pmb u } = { \pmb 0 }$ as a continuous function by defining ${ \pmb g } ( { \pmb 0 } ) =$ ${ \bf 2 } f ^ { \prime } ( x )$ We conclude that (1.28) holds by the Riemann-Lebesgue lemma. This finishes the proof of Theorem 1.22. $\bullet$

# 1.3.3 Convergence at a Point of Discontinuity

Now we discuss some variations of Theorem 1.22. Note that the hypothesis of this theorem requires the function $\pmb { f }$ to be continuous and periodic. However, there are many functions of interest that are neither continuous or periodic. For example, the function in Example 1.9, $f ( x ) = x .$ , is not periodic. Moreover, the periodic extension of $\pmb { f }$ (graphed in Figure 15) is not continuous.

Before we state the theorem on convergence near a discontinuity, we need the following definition.

![](images/e58514db9542186178e5f7ef2d28dd8f24ff6984f93eceb23c7b267390a19ab1.jpg)  
Figure 15 $2 \pi$ -periodic extension of $\pmb { f } ( \pmb { x } ) = \pmb { x }$

# DEFInItioN 1.25

The left and right limits of $\pmb { f }$ at a point $\pmb { x }$ are defined as follows.

$$
\begin{array} { l l } { { L e f t L i m i t : } } & { { f ( x - 0 ) = \displaystyle \operatorname* { l i m } _ { h \to 0 ^ { + } } f ( x - h ) } } \\ { {  } } & { {  } } \\ { { R i g h t L i m i t : } } & { { f ( x + 0 ) = \displaystyle \operatorname* { l i m } _ { h \to 0 ^ { + } } f ( x + h ) } } \end{array}
$$

The function $\pmb { f }$ is said to be left differentiable at $\pmb { x }$ if the following limit exists:

$$
f ^ { \prime } ( x - 0 ) = \operatorname* { l i m } _ { h \to 0 ^ { - } } { \frac { f ( x + h ) - f ( x ) } { h } } .
$$

• The function $\pmb { f }$ is said to be right differentiable at $\pmb { x }$ if the following limit exists:

$$
f ^ { \prime } ( x + 0 ) = \operatorname* { l i m } _ { h \to 0 ^ { + } } { \frac { f ( x + h ) - f ( x ) } { h } } .
$$

Intuitively, ${ f ^ { \prime } } ( x - 0 )$ represents the slope of the tangent line to $\pmb { f }$ at $\pmb { x }$ considering only the part of the graph of ${ \boldsymbol { y } } = { \boldsymbol { f } } ( t )$ that lies to the left of $\pmb { t } = \pmb { x }$ The value $f ^ { \prime } ( x + 0 )$ is the slope of the tangent line of ${ \boldsymbol { y } } = { \boldsymbol { f } } ( t )$ at $\pmb { x }$ considering only the graph of the function that lies to the right of ${ \pmb t = \pmb x }$ (see Figure 16).

![](images/15b6dfa0a13801b34e5ee12701a1ff078399a77a2203536f230a35c98d87689d.jpg)  
Figure 16 Left and right derivatives

# EXAMPLE 1.26

Let $\pmb { f } ( \pmb { x } )$ be the periodic extension of ${ \pmb y } = { \pmb x }$ , $- \pi \leq x < \pi$ (see Figure 15). Then $\pmb { f } ( \pmb { x } )$ is discontinuous at $x = \ldots , - \pi , \pi , \ldots$ The left and right limits of $\pmb { f }$ at ${ \pmb x } = { \pmb \pi }$ are

$$
f ( \pi - 0 ) = \pi \qquad f ( \pi + 0 ) = - \pi .
$$

The left and right derivatives at ${ \pmb x } = { \pmb \pi }$ are

$$
f ^ { \prime } ( \pi - 0 ) = 1 \quad \mathrm { a n d } \quad f ^ { \prime } ( \pi + 0 ) = 1 .
$$

# EXAMPLe 1.27

Let

$$
f ( x ) = \left\{ { \begin{array} { l l } { x } & { { \mathrm { i f ~ } } 0 \leq x \leq \pi / 2 } \\ { \pi - x } & { { \mathrm { i f ~ } } \pi / 2 \leq x \leq \pi . } \end{array} } \right.
$$

The graph of $\pmb { f }$ is the sawtooth wave illustrated in Figure 7. This function is continuous but not differentiable at $x = \pi / 2$ The left and right derivatives at $x = \pi / 2$ are

$$
f ^ { \prime } ( \pi / 2 - 0 ) = 1 \quad { \mathrm { a n d } } \quad f ^ { \prime } ( \pi / 2 + 0 ) = - 1 .
$$

Now we are ready to state the convergence theorem for Fourier series at a point where $\pmb { f }$ is not necessarily continuous.

THEOREM 1.28 Suppose $\pmb { f } ( \pmb { x } )$ is periodic and piecewise continuous. Suppose $\pmb { x }$ is a point where $\pmb { f }$ is left and right differentiable (but not necessarily continuous). Then the Fourier series of $\pmb { f }$ at $\pmb { x }$ converges to

$$
\frac { f ( x + 0 ) + f ( x - 0 ) } { 2 } .
$$

This theorem states that at a point of discontinuity of $\pmb { f }$ , the Fourier series of $\pmb { f }$ converges to the average of the left and right limits of $\pmb { f }$ , At a point of continuity, the left and right limits are the same, and so in this case Theorem 1.28 reduces to Theorem 1.22.

# EXaMPle 1.29

Let $\pmb { f } ( \pmb { x } )$ be the periodic extension of ${ \pmb y } = { \pmb x }$ $- \pi \leq x < \pi$ As mentioned in Example 1.26, $\pmb { f }$ is not continuous but left and right differentiable at ${ \pmb x } = { \pmb \pi }$ . Theorem 1.28 states that its Fourier series, ${ \pmb F } ( { \pmb x } )$ , converges to the average of the left and right limits of $\pmb { f }$ at ${ \pmb x } = { \pmb \pi }$ Since $f ( \pi - 0 ) = \pi$ and $f ( \pi + 0 ) = - \pi ,$ Theorem 1.28 implies $F ( { \boldsymbol { \pi } } ) = \mathbf { 0 }$ This value agrees with the formula for the Fourier series computed in Example 1.9:

$$
F ( x ) = \sum _ { k = 1 } ^ { \infty } { \frac { 2 ( - 1 ) ^ { k + 1 } } { k } } \sin ( k x )
$$

whose value is zero at ${ \pmb x } = { \pmb \pi }$ The graph of the $\pmb { F }$ is given in Figure 17. Note that the value of ${ \pmb F }$ at $\pmb { x } \simeq \pmb { \pm \pmb { \mathrm { \pi } } }$ and $x = \pm 3 \pi$ (indicated by the solid dots) is equal to the average of the left and right limits at $\pmb { x } = \pmb { \pm \mathrm { \pi } } \pmb { \pi }$ and $\pm 3 \pi$ .

Proof of Theorem 1.28 The proof of this theorem is very similar to the proof of Theorem 1.22. We summarize the modifications.

Steps 1 through 3 go through without change. Step 4 needs to be modified as follows

Step 4'.

$$
\int _ { 0 } ^ { \pi } P _ { N } ( u ) d u = \int _ { - \pi } ^ { 0 } P _ { N } ( u ) d u = \frac { 1 } { 2 }
$$

where

$$
P _ { N } ( u ) = \frac { 1 } { 2 \pi } \frac { \sin ( N + 1 / 2 ) u } { \sin u / 2 } .
$$

In fact, these equalities follow from Lemma 1.24, and by using the fact that $P _ { N } ( u )$ is even (so the left- and right-half integrals are equal and sum to 1).

Step 5 is now replaced by the following.

![](images/45069115fab7bbfa8e797b1c9e76cf3822cce9bb00c18a0c6324e52d67948701.jpg)  
Figure 17 Graph of the Fourier series for Example 1.29

Step $\mathbf { 5 ^ { \prime } }$ . To show Theorem 1.28, we need to establish

$$
\int _ { - \pi } ^ { \pi } f ( u + x ) P _ { N } ( u ) d u \quad  \quad { \frac { f ( x + 0 ) + f ( x - 0 ) } { 2 } }
$$

as $N \to \infty$

We show (1.29) by establishing the following two limits:

$$
\begin{array} { l l l } { { \displaystyle \int _ { 0 } ^ { \pi } f ( u + x ) P _ { N } ( u ) d u } } & { { \to } } & { { \displaystyle \frac { f ( x + 0 ) } { 2 } } } \\ { { \displaystyle \int _ { - \pi } ^ { 0 } f ( u + x ) P _ { N } ( u ) d u } } & { { \to } } & { { \displaystyle \frac { f ( x - 0 ) } { 2 } . } } \end{array}
$$

Using Step $\pmb { 4 } ^ { \prime }$ , these limits are equivalent to the following two limits:

$$
\begin{array} { r l r } { \displaystyle \int _ { 0 } ^ { \pi } ( f ( u + x ) - f ( x + 0 ) ) P _ { N } ( u ) d u } & { \to } & { 0 } \\ { \displaystyle \int _ { - \pi } ^ { 0 } ( f ( u + x ) - f ( x - 0 ) ) P _ { N } ( u ) d u } & { \to } & { 0 . } \end{array}
$$

Using the definition of $P _ { N } ( u )$ , equation (1.30) is equivalent to showing

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { \pi } ( { \frac { f ( x + u ) - f ( x + 0 ) } { \sin ( u / 2 ) } } ) \sin ( ( N + 1 / 2 ) u ) d u \quad  \quad 0 .
$$

This limit follows from the Riemann-Lebesgue lemma exactly as in Step 5. Since $\mathbf { \boldsymbol { \mathbf { \mathit { u } } } }$ is positive in the preceding integral, we only need to know that the expression

in parentheses is continuous from the right (i.e., has a right limit as $u \to 0 ^ { + }$ ). Since $\pmb { f }$ is assumed to be right differentiable, the same limit argument from Step 5 can be repeated here (with $\overset { \triangledown } { \boldsymbol { u } } > \dot { \boldsymbol { 0 } }$ ).

Similar arguments can be used to establish (1.31). This completes the proof of Theorem 1.28. $\bullet$

# 1.3.4 Uniform Convergence

Now we discuss uniform convergence of Fourier series. As stated in Definition 0.8, a sequence of functions $F _ { n } ( x )$ converges uniformly to ${ \pmb F } ( { \pmb x } )$ if the rate of convergence is independent of the point $\pmb { x }$ . In other words, given any small tolerance, $\epsilon > 0$ (such as $\epsilon = . 0 1$ ), there exists a number $\pmb { N }$ that is independent of $\pmb { x }$ , such that $| F _ { n } ( x ) - F ( x ) | < \epsilon$ for all $\pmb { x }$ and all $n \geq N$ If the ${ \pmb { F _ { n } } }$ did not converge uniformly, then we might have to choose different values of $\pmb { N }$ for different $\pmb { x }$ values to achieve the same degree of accuracy.

We say that the Fourier series of $\pmb { f } ( \pmb { x } )$ converges to $\pmb { f } ( \pmb { x } )$ uniformly if the sequence of partial sums

$$
S _ { N } ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x )
$$

converges to $\pmb { f } ( \pmb { x } )$ uñiformly as $N \to \infty$ , where the ${ \pmb a } _ { { \pmb k } }$ and $\boldsymbol { b } _ { k }$ are the Fourier coefficients of $\pmb { f }$ .

From Figures 8 and 9, it appears that the Fourier series in Example 1.10 converges uniformly. By contrast, the Fourier series in Example 1.9 does not appear to converge uniformly to ${ f } ( x )$ . As the point $\pmb { x }$ gets closer to a point of discontinuity of $\pmb { f }$ , the rate of convergence gets slower. In view of Example 1.9, the number of terms, $\pmb { N }$ , that must be used in the partial sum of the Fourier series to achieve a certain degree of accuracy must increase as $\pmb { x }$ approaches a point of discontinuity.

In order to state the following theorem on uniform convergence, one more definition is needed. A function is said to be piecewise smooth if it is continuous and its derivative is defined everywhere except possibly for a discrete set of points. For example, the sawtooth function in Example 1.10 is piecewise smooth since the derivative of $\pmb { f }$ exists at all points except at multiples of $\pi / 2$ (which is a discrete set of points).

We now state the theorem for uniform convergence of Fourier series for the interval $[ - \pi , \pi ]$ This theorem also holds with $\pmb { \pi }$ replaced by any number $\pmb { a }$ .

THEOreM 1.30 The Fourier series of a piecewise smooth, $\mathbf { 2 \pi }$ -periodic function ${ f } ( x )$ converges uniformly to $f ( x )$ on $\lceil - \pi , \pi \rceil$ .

# EXAMPLe 1.31

Consider the sawtooth wave in Example 1.10. The graph of its periodic extension is piecewise smooth, as is clear from Figure 7. Therefore, Theorem 1.30 guarantees that its Fourier series converges uniformly. •

# EXAMPLE 1.32

Consider the Fourier series for the function $\pmb { f } ( \pmb { x } ) = \mathbf { \dot { x } }$ on the interval $[ - \pi , \pi ]$ considered in Example 1.9. Since $\pmb { f } ( \pmb { x } ) = \pmb { x }$ is not periodic, we need to consider its periodic extension, which is graphed in Figure 4. Note that its periodic extension is not continuous and therefore not piecewise smooth [even though $\pmb { f } ( \pmb { x } ) = \pmb { x }$ is everywhere smooth]. Therefore, Theorem 1.30 does not apply. In fact, due to the Gibbs effect in this example (see Figures 5 and 6), the Fourier series for this example does not converge uniformly.

Proof of Theorem 1.30 We prove this theorem under the simplifying assumption that $\pmb { f }$ is everywhere twice differentiable.

As a first step, we prove the following relationship between the Fourier co efficients of $\pmb { f }$ and the corresponding Fourier coefficients of $f ^ { \prime \prime }$ : If

$$
f ( x ) = \sum _ { n } a _ { n } \cos ( n x ) + b _ { n } \sin ( n x ) \quad { \mathrm { a n d } } \quad f ^ { \prime \prime } ( x ) = \sum _ { n } a _ { n } ^ { \prime \prime } \cos ( n x ) + b _ { n } ^ { \prime \prime } \sin ( n x )
$$

then

$$
\begin{array} { c } { { a _ { n } = \displaystyle \frac { - a _ { n } ^ { \prime \prime } } { n ^ { 2 } } } } \\ { { b _ { n } = \displaystyle \frac { - b _ { n } ^ { \prime \prime } } { n ^ { 2 } } . } } \end{array}
$$

To establish the first relation, we use integration by parts on the integral formula for ${ a } _ { n }$ (Theorem 1.2) to obtain

$$
\begin{array} { l } { { a _ { n } = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } f ( x ) \mathrm { c o s } ( n x ) d x } } \\ { { \displaystyle ~ = f ( x ) \frac { \sin ( n x ) } { n } \Big \vert _ { - \pi } ^ { \pi } - \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } f ^ { \prime } ( x ) \frac { \sin ( n x ) } { n } d x . } } \end{array}
$$

The first term on the right is zero since sin $n \pi = \sin ( - n \pi ) = 0 .$ The second term on the right is $- b _ { n } ^ { \prime } / n$ ,where $\pmb { b } _ { \pmb { n } } ^ { \prime }$ is the Fourier sine coefficient of $\pmb { f ^ { \prime } }$ Repeating the same process [this time with $d v = ( \sin n x ) / n$ and $\pmb { u } = \pmb { f ^ { \prime } } ]$ gives

$$
a _ { n } = { \frac { - 1 } { \pi n ^ { 2 } } } \int _ { - \pi } ^ { \pi } f ^ { \prime \prime } ( x ) \cos ( n x ) d x .
$$

The right side is $- a _ { n } ^ { \prime \prime } / n ^ { 2 }$ , as claimed in (1.32). Equation (1.33) for $b _ { n }$ is proved in a similar manner.

If $\pmb { f ^ { \prime \prime } }$ is continuous, then both the ${ \pmb { a } } _ { n } ^ { \prime \prime }$ and ${ b } _ { n } ^ { \prime \prime }$ stay bounded by some number $M$ (in fact, by the Riemann Lebesgue lemma, ${ \pmb a } _ { \pmb { n } } ^ { \prime \prime }$ and ${ \pmb { b } } _ { n } ^ { \prime \prime }$ converge to zero as $\textstyle n \to \infty$ .Therefore, using (1.32) and (1.33),

$$
\sum _ { n = 1 } ^ { \infty } | a _ { n } | + | b _ { n } | = \sum _ { n = 1 } ^ { \infty } { \frac { | a _ { n } ^ { \prime \prime } | + | b _ { n } ^ { \prime \prime } | } { n ^ { 2 } } } \leq \sum _ { n = 1 } ^ { \infty } { \frac { M + M } { n ^ { 2 } } } .
$$

This er  ite henal $\scriptstyle \sum _ { n = 1 } ^ { \infty } 1 / n ^ { 2 }$ is finite since $\textstyle \int _ { 1 } ^ { \infty } d x / x ^ { 2 }$ is finite). The proof of the theorem will therefore follow from the following lemma.

# LEMMA 1.33 Suppose

$$
f ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x )
$$

with

$$
\sum _ { k = 1 } ^ { \infty } \left| a _ { k } \right| + \left| b _ { k } \right| < \infty .
$$

Then the Fourier series converges uniformly and absolutely to the functic

Proof We start with the estimate

$$
| a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) | \leq | a _ { k } | + | b _ { k } |
$$

(valid since $| \cos t | , | \sin t | \le 1 )$ .Thus the rate of convergence of the Fourier series of $\pmb { f }$ at any point $\pmb { x }$ is governed by the rate of convergence of $\sum _ { k } | a _ { k } | + | b _ { k } |$ More precisely, let

$$
S _ { N } ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) .
$$

Then

$$
\begin{array} { c } { { f ( x ) - S _ { N } ( x ) = a _ { 0 } + \displaystyle \sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) } } \\ { { - \displaystyle \left( a _ { 0 } + \sum _ { k = 1 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) \right) . } } \end{array}
$$

The $\scriptstyle { a _ { 0 } }$ and the terms up through $\pmb { k } = \pmb { N }$ cancel. Thus

$$
f ( x ) - S _ { N } ( x ) = \sum _ { k = N + 1 } ^ { \infty } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) .
$$

By (1.34)

$$
\vert f ( x ) - S _ { N } ( x ) \vert \leq \sum _ { k = N + 1 } ^ { \infty } \vert a _ { k } \vert + \vert b _ { k } \vert
$$

uniformly for all $\pmb { x }$ Since the series $\begin{array} { r } { \sum _ { k = 1 } ^ { \infty } \left| a _ { k } \right| + \left| b _ { k } \right| } \end{array}$ converges by hypothesis, the tail end of this series can be made as small as desired by choosing $\pmb { N }$ large enough. So, given $\epsilon > 0$ , there is an integer $N _ { 0 } > 0$ so that if $N > N _ { 0 }$ , then $\begin{array} { r } { \sum _ { k = N + 1 } ^ { \infty } \left| a _ { k } \right| + \left| b _ { k } \right| < \epsilon } \end{array}$ From (1.35)

$$
| f ( x ) - S _ { N } ( x ) | < \epsilon \quad \mathrm { f o r } \quad N > N _ { 0 }
$$

for all $\pmb { x }$ . $\pmb { N }$ does not depend on ${ \pmb x } ; { \pmb N }$ depends only on the rate of convergence of $\textstyle \sum _ { k = 1 } ^ { \infty } \left| a _ { k } \right| + \left| b _ { k } \right|$ ${ \pmb S } _ { N } ( { \pmb x } )$ is uniform. This completes the proof of Lemma 1.33 and of Theorem 1.30.

# 1.3.5 Convergence in the Mean

As pointed out in the previous section, if $\pmb { f }$ is not continuous, then its Fourier series does not converge to ${ \pmb f } ( { \pmb x } )$ at points where $\pmb { f } ( \pmb { x } )$ is discontinuous (it converges to the average of its left and right limits instead). In cases where a Fourier series does not converge uniformly or pointwise. it may converge in a weaker sense, such as in $L ^ { 2 }$ (in the mean). We investigate $L ^ { 2 }$ convergence of Fourier series in this section. Again, we state and prove the results in this section for $2 \pi$ -periodic functions. However, the results remain true for other intervals as well (by replacing $\pmb { \pi }$ by any number $\pmb { a }$ and by using the appropriate form of the Fourier series for the interval $[ - a , a ] )$ .

First, we recall some concepts from Chapter 0 on inner product spaces. We will be working with the space $V = L ^ { 2 } ( [ - \pi , \pi ] )$ consisting of all square integrable functions (i.e., $\pmb { f }$ with $\textstyle \int _ { - \pi } ^ { \pi } | f ( x ) | ^ { 2 } d x < \infty )$ . $\pmb { V }$ is an inner product space with the following inner product:

$$
\langle f , g \rangle = \int _ { - \pi } ^ { \pi } f ( x ) { \overline { { g ( x ) } } } d x .
$$

The norm $\| f \|$ in this space is therefore defined by

$$
\| f \| ^ { 2 } = \int _ { - \pi } ^ { \pi } | f ( x ) | ^ { 2 } d x .
$$

We remind you of the two most important inequalities of an inner product space:

$$
\langle f , g \rangle _ { V } \leq \| f \| \| g \| \qquad \mathrm { a n d } \qquad \| f + g \| \leq \| f \| + \| g \| .
$$

The first of these is the Schwarz inequality and the second is the triangle inequality.

Let

$V _ { N } =$ the space spanned by $\{ 1 , \cos ( k x ) , \sin ( k x ) , k = 1 , \ldots , N \}$ .

An element in $V _ { N }$ is a sum of the form

$$
c _ { 0 } + \sum _ { k = 1 } ^ { N } c _ { k } \cos ( k x ) + d _ { k } \sin ( k x )
$$

where $\pmb { c _ { k } }$ and $d _ { k }$ are any complex numbers. Suppose $\pmb { f }$ belongs to $L ^ { 2 } [ - \pi , \pi ]$ . Let

$$
f _ { N } ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) \in V _ { N }
$$

be its partial Fourier series, where the $\pmb { a } _ { \pmb { k } }$ and $\scriptstyle b _ { k }$ are the Fourier coefficients given in Theorem 1.2. The key point in the proof of Theorem 1.2 is that $\pmb { a } _ { \pmb { k } }$ and $6 _ { k }$ are obtained by orthogonally projecting $\pmb { f }$ onto the space spanned by $\cos ( k x )$ and $\sin ( k x )$ (see the remark at the end of the proof). Thus, $\pmb { f } _ { N }$ is the orthogonal projection of $\pmb { f }$ onto the space $V _ { N }$ In particular, $\scriptstyle f _ { N }$ is the element in $V _ { N }$ that is closest to $\pmb { f }$ in the $L ^ { 2 }$ sense. We summarize this discussion in the following lemma.

LEMMA 1.34 Suppose $\pmb { f }$ is an element of $V = L ^ { 2 } ( [ - \pi , \pi ] )$ . Let $V _ { N }$ be the linear span of $\{ 1 , \cos ( k x ) , \sin ( k x ) , 1 \leq k \leq N \}$ . Let

$$
f _ { N } ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x )
$$

where ${ \pmb a } _ { { \pmb k } }$ and $\scriptstyle b _ { k }$ are the Fourier coefficients of $\pmb { f }$ Then $\scriptstyle f _ { N }$ is the element in $V _ { N }$ which is the closest to $\pmb { f }$ in the $L ^ { 2 }$ -norm; that is,

$$
\| f - f _ { N } \| _ { L ^ { 2 } } = \operatorname* { m i n } _ { g \in V _ { N } } \| f - g \| _ { L ^ { 2 } } .
$$

The main result of this section is contained in the next theorem.

THEOREM 1.35 Suppose $\pmb { f }$ is an element of $L ^ { 2 } ( [ - \pi , \pi ] )$ . Let

$$
f _ { N } ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) \quad .
$$

where ${ \pmb a } _ { { \pmb k } }$ and $\boldsymbol { b } _ { \boldsymbol { k } }$ are the Fourier coefficients of $\pmb { f }$ . Then $\scriptstyle f _ { N }$ converges to $\pmb { f }$ in $L ^ { 2 } ( [ - \pi , \pi ] )$ ;that is, $\| f _ { N } - f \| _ { L ^ { 2 } } \to 0$ as $N \to \infty$ .

Theorem 1.35 also holds for the complex form of Fourier series.

THeOREM 1.36 Suppose $\pmb { f }$ is an element of $L ^ { 2 } ( [ - \pi , \pi ] )$ with (complex) Fourier coefficients given by

$$
\alpha _ { n } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( t ) e ^ { - i n t } d t f o r n \in Z .
$$

Then the partial sum

$$
f _ { N } ( t ) = \sum _ { k = - N } ^ { N } \alpha _ { k } e ^ { i k t }
$$

converges to $\pmb { f }$ in the $L ^ { 2 } ( [ - \pi , \pi ] )$ norm as $N \to \infty$ .

# EXAMPLE 1.37

All the examples considered in this chapter arise from functions that are in $L ^ { 2 }$ (over the appropriate interval under consideration for each example). Therefore, the Fourier series of each example in this chapter converges in the mean.

Proof The proofs of both theorems are very similar. We give the proof of Theorem 1.35.

The proof involves two key steps. The first step (the next lemma) states that any function in $L ^ { 2 } ( [ - \pi , \pi ] )$ can be approximated in the $L ^ { 2 } .$ -norm by a piecewise smooth periodic function $\pmb { \mathscr { s } }$ The second step (Theorem 1.30) is to approximate $\pmb { \mathscr { g } }$ uniformly (and therefore in $L ^ { 2 }$ )by its Fourier series. We start with the following lemma.

LEMMA 1.38 A function in $L ^ { 2 } ( [ - \pi , \pi ] )$ can be approximated arbitrarily closely by a smooth, $2 \pi$ -periodic function.

A rigorous proof of this lemma is beyond the scope of this book. However, we can give an intuitive idea as to why this lemma holds. A typical element $\pmb { f } \in$ $L ^ { 2 } [ - \pi , \pi ]$ is not continuous. Even if it were continuous, its periodic extension is often not continuous. The idea is to connect the continuous components of $\pmb { f }$ with the graph of a smooth function $\pmb { \mathscr { g } }$ This is illustrated in Figures 18 through 20. In Figure 18, the graph of a typical $f \in L ^ { 2 } [ - \pi , \pi ]$ is given. The graph of its periodic extension is given in Figure 19. In Figure 20, the graph of a continuous $\pmb { \mathscr { g } }$ that connects the continuous components of $\pmb { f }$ is superimposed on the graph of $\pmb { f }$ Rounding the corners of the connecting segments then molds $\pmb { \mathscr { g } }$ into a smooth function. Since the extended $\pmb { f }$ is periodic, we can arrange that $\pmb { \mathscr { g } }$ is periodic as well.

The graph of $\pmb { \mathscr { s } }$ agrees with the graph of $\pmb { f }$ everywhere except on the connecting segments that connect the continuous components of $\pmb { f }$ Since the horizontal width of each of these segments can be made very small (by increasing the slopes of these connecting segments), $\pmb { \mathscr { g } }$ can be chosen very close to $\pmb { f }$ in the ${ \pmb L } ^ { 2 }$ -norm. These ideas are explored in more detail in Exercise 27.

![](images/bcded2cf19eb05c490aab7f8fdd957bebe26fe9806a6572d77cf6cc24cf9c272.jpg)  
Figure 18 Typical $\pmb { f }$ in $L ^ { 2 }$

![](images/354fe2fed100affb9c34034e2e9d2f3b0e53459a08dce594a690fe95cfcbf2ef.jpg)  
Figure 19 Periodic extension of $\pmb { f }$

Now we can complete the proof of Theorem 1.35. Using Lemma 1.38 and Theorem 0.10, we can (for any $\epsilon > 0$ co differentiable, periicuion, $\pmb { \mathscr { g } }$ , with

$$
\| \ b { f } - \ b { g } \| _ { L ^ { 2 } } < \epsilon .
$$

![](images/2e76069d04bf402a4d9dd3b45fe0de054144edc83327ed13bb3b7b99c2c21d39.jpg)  
Figure 20 Approximation of $\pmb { f }$ by a continuous $\pmb { \mathscr { g } }$

Let

$$
g _ { N } ( x ) = c _ { 0 } + \sum _ { k = 1 } ^ { N } c _ { k } \cos ( k x ) + d _ { k } \sin ( k x )
$$

where $\pmb { c } _ { \pmb { k } }$ and $d _ { k }$ are the Fourier cosine and sine coefficients for $\pmb { \mathscr { g } }$ Since $\pmb { \mathscr { g } }$ is differentiable and periodic, we can uniformly approximate $\mathfrak { s }$ by $\mathfrak { s r }$ (using Theorem 1.30). By choosing $N _ { 0 }$ large enough, we can arrange $| g ( x ) - g _ { N } ( x ) | < \epsilon$ for all $x \in [ - \pi , \pi ]$ and for $N > N _ { 0 }$ Therefore,

$$
\begin{array} { l } { \displaystyle \| g - g _ { N } \| ^ { 2 } = \int _ { - \pi } ^ { \pi } | g ( x ) - g _ { N } ( x ) | ^ { 2 } d x \leq \int _ { - \pi } ^ { \pi } \epsilon ^ { 2 } d x \quad \mathrm { i f } \ N > N _ { 0 } } \\ { = 2 \pi \epsilon ^ { 2 } . } \end{array}
$$

By taking square roots,

$$
\| g - g _ { N } \| < { \sqrt { 2 \pi } } \epsilon .
$$

Combining this estimate with (1.36), we obtain

$$
\begin{array} { r l } & { \left\| f - g _ { N } \right\| = \left\| f - g + g - g _ { N } \right\| } \\ & { \qquad \leq \left\| f - g \right\| + \left\| g - g _ { N } \right\| \qquad \mathrm { ( t r i a n g l e ~ i n e q u a l i t y ) } } \\ & { \qquad < \epsilon + \sqrt { 2 \pi } \epsilon \quad \mathrm { f o r } ~ N > N _ { 0 } . } \end{array}
$$

Now $\pmb { g } _ { N }$ is a linear combination of $\sin ( k x )$ and $\cos ( k x )$ for $k \leq N$ and therefore $\pmb { g } _ { N }$ belongs to $V _ { N }$ We have already shown that $f _ { N }$ is the closest element from $\mathbf { V } _ { N }$ to $\pmb { f }$ in the $L ^ { 2 }$ -norm (see Lemma 1.34). Therefore, we conclude that

$$
\| f - f _ { N } \| \le \| f - g _ { N } \| < ( 1 + \sqrt { 2 \pi } ) \epsilon \quad \mathrm { f o r ~ } N > N _ { 0 } .
$$

Since the tolerance, e, can be chosen as small as desired, the proof of Theorem 1.35 is complete. $\bullet$

One consequence of Theorems 1.35 and 1.36 is the following theorem which is known as Parseval's equation. We state both the real and complex versions.

THEOREM 1.39 Parseval's Equation—Real Version. Suppose

$$
f ( x ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x ) \ \in \ L ^ { 2 } [ - \pi , \pi ] .
$$

Then

$$
{ \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } | f ( x ) | ^ { 2 } d x = 2 | a _ { 0 } | ^ { 2 } + \sum _ { k = 1 } ^ { \infty } | a _ { k } | ^ { 2 } + | b _ { k } | ^ { 2 } .
$$

THEOreM 1.40 Parseval's Equation—Complex Version. Suppose

$$
f ( x ) = \sum _ { k = - \infty } ^ { \infty } \alpha _ { k } e ^ { i k x } \ \in \ L ^ { 2 } [ - \pi , \pi ] .
$$

Then

$$
{ \frac { 1 } { 2 \pi } } \| f \| ^ { 2 } = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } | f ( x ) | ^ { 2 } d x = \sum _ { k = - \infty } ^ { \infty } | \alpha _ { k } | ^ { 2 } .
$$

Moreover, for $\pmb { f }$ and $\pmb { \mathscr { g } }$ in $L ^ { 2 } [ - \pi , \pi ]$

$$
{ \frac { 1 } { 2 \pi } } \langle f , g \rangle = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( t ) { \overline { { g ( t ) } } } d t = \sum _ { n = - \infty } ^ { \infty } \alpha _ { n } { \overline { { \beta _ { n } } } } .
$$

Remark. The $L ^ { 2 }$ -norm of a signal is often interpreted as its energy. With this physical interpretation, the squares of the Fourier coefficients of a signal measure the energy of the corresponding frequency components. Therefore, a physical interpretation of Parseval's equation is that the energy of a signal is simply the sum of the energies from each of its frequency components. (See Example 1.41.)

Proof We prove the complex version of Parseval's equation. The proof of the real version is similar.

We prove equation (1.39). Equation (1.38) then follows from equation (1.39) by setting $\pmb { f } = \pmb { g }$

Let

$$
\begin{array} { l } { f _ { N } ( x ) = \displaystyle \sum _ { k = - N } ^ { N } \alpha _ { k } e ^ { i k x } } \\ { g _ { N } ( x ) = \displaystyle \sum _ { k = - N } ^ { N } \beta _ { k } e ^ { i k x } } \end{array}
$$

be the partial sum of the Fourier series of $\pmb { f }$ and $\pmb { \mathscr { s } }$ , respectively. By Theorem 1.36 , $f _ { N } \to f$ and ${ \pmb g } _ { N }  { \pmb g }$ in $L ^ { 2 } [ - \pi , \pi ]$ as $N \to \infty$ We have

$$
\langle f _ { N } , g _ { N } \rangle = \langle \sum _ { k = - N } ^ { N } \alpha _ { k } e ^ { i k x } , \sum _ { n = - N } ^ { N } \beta _ { n } e ^ { i n x } \rangle = \sum _ { k = - N } ^ { N } \sum _ { n = - N } ^ { N } \alpha _ { k } \overline { { { \beta _ { n } } } } \langle e ^ { i k x } , e ^ { i n x } \rangle .
$$

Since $\{ e ^ { i k x } / \sqrt { 2 \pi } , k = \dots , - 1 , 0 , 1 , \dots \}$ is orthonormal, $\langle e ^ { i k x } , e ^ { i n x } \rangle$ is 0 if $k \neq n$ and $\mathbf { 2 \pi } \pi$ if $\pmb { k } = \pmb { n }$ Therefore,

$$
\langle f _ { N } , g _ { N } \rangle = \sum _ { n = - N } ^ { N } \alpha _ { n } \overline { { { \beta _ { n } } } } \langle e ^ { i n x } , e ^ { i n x } \rangle = 2 \pi \sum _ { n = - N } ^ { N } \alpha _ { n } \overline { { { \beta _ { n } } } } .
$$

Equation (1.39) follows by letting $N \to \infty$ provided that we show

$$
\left. f _ { N } , g _ { N } \right. \to \left. f , g \right. \quad \mathrm { a s } ~ N \to \infty .
$$

To show (1.40), we write

$$
\begin{array} { r l } & { | \langle f , g , \rangle - \langle f _ { N } , g _ { N } \rangle | = | \left( \langle f , g , \rangle - \langle f , g _ { N } \rangle \right) + \left( \langle f , g _ { N } \rangle - \langle f _ { N } , g _ { N } \rangle \right) | } \\ & { \qquad \leq | \langle f , g - g _ { N } \rangle | + | \langle f - f _ { N } , g _ { N } \rangle | } \\ & { \qquad \leq \| f \| \| g - g _ { N } \| + \| f - f _ { N } \| \| g _ { N } \| } \end{array}
$$

where the last step follows by Schwarz's inequality. Since $\| f _ { N } - f \| \to 0$ and $\| g - g _ { N } \| \to 0$ in $L ^ { 2 }$ (Theorem 1.36), the right side converges to zero as $N \to \infty$ and (1.40) follows. $\bullet$

Note. If the series on the right side of (1.38) is truncated at some finite value $\pmb { N }$ ,then the right side can only get smaller, resulting in the following inequality:

$$
\sum _ { k = - N } ^ { N } | \alpha _ { k } | ^ { 2 } \leq \frac { 1 } { 2 \pi } \| f \| ^ { 2 } .
$$

This in known as Bessel's inequality.

# EXAMPLE 1.41

As we noted earlier, one interpretation of Parseval's theorem is that the energy in a signal is the sum of the energies associated with its Fourier components. In Example 1.9, we found that the Fourier coefficients for $\pmb { f } ( \pmb { x } ) = \pmb { x }$ $- \pi \leq x < \pi$ . are $\pmb { a _ { n } = 0 }$ and $b _ { n } = 2 ( - 1 ) ^ { n + 1 } / n$ By equation (1.37), we have

$$
{ \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } x ^ { 2 } d x = \sum _ { n = 1 } ^ { \infty } { \frac { 4 } { n ^ { 2 } } } .
$$

Evaluating the integral on the left and dividing both sides by 4, we see that

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 6 } } .
$$

This sum is computed another way in Exercise 18.

# 1.4 Exercises

1. Expand the function $f ( x ) = x ^ { 2 }$ in a Fourier series valid on the interval $- \pi \leq x \leq \pi$ Plot both $\pmb { f }$ and the partial sums of its Fourier series

$$
S _ { N } ( x ) = \sum _ { k = 0 } ^ { N } a _ { k } \cos ( k x ) + b _ { k } \sin ( k x )
$$

for $N = 1 , 2 , 5 , 7 .$ Observe how the graphs of the partial sums $S _ { N } ( x )$ approximate the graph of $\pmb { f }$ Plot the same graphs over the interval $- 2 \pi \leq$ $x \leq 2 \pi$ .

2.Repeat the previous exercise for the interval $- 1 \leq x \leq 1$ That is, expand the function $f ( x ) = x ^ { 2 }$ in a Fourier series valid on the interval $- 1 \leq x \leq 1$ . Plot both $\pmb { f }$ and the partial Fourier series

$$
\sum _ { k = 0 } ^ { N } a _ { k } \cos ( \pi k x ) + b _ { k } \sin ( \pi k x )
$$

for $N = 1 , 2 , 5 , 7$ over the interval $- 1 \leq x \leq 1$ and $- 2 \leq x \leq 2$ .

3. Expand the function $f ( x ) \stackrel { . } { = } x ^ { 2 }$ in a Fourier cosine series on the interval $\mathbf { 0 } \leq x \leq \pi$

4. Expand the function $f ( x ) = x ^ { 2 }$ in a Fourier sine series on the interval $\mathbf { 0 } \leq x \leq \mathbf { 1 }$ .

5. Expand the function $f ( x ) = x ^ { 3 }$ in a Fourier cosine series on the interval $0 \leq x \leq \pi$ b

6. Expand the function $f ( x ) = x ^ { 3 }$ in a Fourier sine series on the interval $0 \leq x \leq 1$ .

7. Expand the function $f ( x ) = | \sin x |$ in a Fourier series valid on the interval $- \pi \leq x \leq \pi$ b

8. Expand the following function:

$$
f ( x ) = \left\{ \begin{array} { l l } { 1 } & { - 1 / 2 < x \le 1 / 2 } \\ { 0 } & { - 1 < x \le - 1 / 2 \mathrm { o r } 1 / 2 < x \le 1 } \end{array} \right.
$$

in a Fourier series valid on the interval $- 1 \leq x \leq 1$ Plot the various partial Fourier series along with the graph of $\pmb { f }$ as in problem 1 for ${ \pmb { N } } = { \bf 5 }$ ,10, 20, and 40 terms. Notice how much slower the series converges to $\pmb { f }$ in this example than in Exercise 1. What accounts for the slow rate of convergence in this example?

9. Expand the function $f ( x ) = e ^ { r x }$ in a Fourier series valid for $- \pi \leq x \leq \pi$ . For the case $r = 1 / 2$ plot the partial Fourier series along with the graph of $\pmb { f }$ as in problem 1 for $N = 1 0 , 2 0$ and 30 terms. Plot these functions over the interval $- \pi \leq x \leq \pi$ and also $- 2 \pi \leq x \leq 2 \pi$ .

10. Use the previous problem to compute the Fourier coefficients for the function $f ( x ) = \sinh x = ( e ^ { x } - e ^ { - x } ) / 2$ and $f ( x ) = \cosh ( x ) = ( e ^ { x } + e ^ { - x } ) / 2$ over the interval $- \pi \leq x \leq \pi$ .

11. Expand the function $f ( x ) = \cos x$ in a Fourier sine series on the interval $0 \leq x \leq \pi$ .

12. Show that

$$
\int _ { 0 } ^ { 1 } \cos ( 2 n \pi x ) \sin ( 2 k \pi x ) d x = 0 .
$$

13.Show that

$$
\{ \ldots , { \frac { 1 } { \sqrt { a } } } \cos ( { \frac { 2 \pi t } { a } } ) , { \frac { 1 } { \sqrt { a } } } \cos ( { \frac { \pi t } { a } } ) , { \frac { 1 } { \sqrt { 2 a } } } , { \frac { 1 } { \sqrt { a } } } \sin ( { \frac { \pi t } { a } } ) , { \frac { 1 } { \sqrt { a } } } \sin ( { \frac { 2 \pi t } { a } } ) , \ldots \}
$$

is an orthonormal set of functions on $L ^ { 2 } ( [ - \alpha , \alpha ] )$ . Establish the proof of Theorem 1.4.

14. Prove Lemma 1.16 and Theorem 1.20.

15. Let ${ \pmb F } ( { \pmb x } )$ be the Fourier series for the function

$$
f ( x ) = \left\{ { \begin{array} { l l } { 1 } & { - 1 / 2 < x \leq 1 / 2 } \\ { 0 } & { - 1 < x \leq - 1 / 2 { \mathrm { ~ o r ~ } } 1 / 2 < x \leq 1 . } \end{array} } \right.
$$

State the precise value of ${ \pmb F } ( { \pmb x } )$ for each $\pmb { x }$ in the interval $- 1 \leq x \leq 1$

16. If $\pmb { f } ( \pmb { x } )$ is continuous on the interval $0 \leq x \leq a ,$ ,show that its even periodic extension is continuous everywhere. Does this statement hold for the odd periodic extension? What additional condition(s) is (are) necessary to ensure that the odd periodic extension is everywhere continuous?

17. Consider the sawtooth function and the Fourier series derived for it Example 1.10.

(aUse the convergence theorems in this chapter to explain why the Fourier series for the sawtooth function converges pointwise to that function.

Use this fact to show that

$$
\sum _ { k = 0 } ^ { \infty } { \frac { 1 } { ( 2 k + 1 ) ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 8 } } .
$$

18. In Exercise 1, you found the Fourier series for the function $f ( x ) = x ^ { 2 }$ , $- \pi \leq x \leq \pi$ Explain why this series converges uniformly to $\scriptstyle x ^ { 2 }$ on $[ - \pi , \pi ]$ . Use this to show that $\scriptstyle \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 6 } }$ Hint: What happens at ${ \pmb x } = \pi ?$

19. Sketch two periods of the pointwise limit of the Fourier series for each of the following functions. State whether or not each function's Fourier series converges uniformly. (You do not need to compute the Fourier coefficients.)

$$
\begin{array} { r l } & { f ( x ) = \left\{ \begin{array} { l l } { 1 } & { - 1 / 2 < x \leq 1 / 2 } \\ { 0 } & { - 1 < x \leq - 1 / 2 \ \mathrm { o r } \ 1 / 2 < x \leq 1 } \end{array} \right. } \\ & { f ( x ) = x - x ^ { 2 } , - 1 < x \leq 1 } \\ & { f ( x ) = 1 - x ^ { 2 } , - 1 < x \leq 1 } \\ & { f ( x ) = \cos x + | \cos x | , - \pi < x \leq \pi } \\ & { f ( x ) = \left\{ \begin{array} { l l } { \frac { \sin x } { x } } & { - \pi < x \leq \pi , \ x \neq 0 } \\ { 1 } & { x = 0 } \end{array} \right. } \end{array}
$$

20. For each of the functions in Exercise 19, state whether or not its Fourier sine and cosine series (for the corresponding half-interval) converge uniformly on the entire real line, $- \infty < x < \infty$ .

21. If $\pmb { F }$ is $2 \pi$ -periodic and $\pmb { c }$ is any real number, then show that

$$
\int _ { - \pi } ^ { - \pi + c } F ( x ) d x = \int _ { \pi } ^ { \pi + c } F ( x ) d x .
$$

Hint: Use the change of variables $x = t - 2 \pi$ .Then use this equation to prove Lemma 1.3.

22. If $\pmb { f }$ is a real-valued even function on the interval $[ - \pi , \pi ]$ , show that the complex Fourier coefficients are real. If $\pmb { f }$ is a real-valued odd function on the interval $[ - \pi , \pi ]$ , show that the complex Fourier coefficients are purely imaginary (i.e., their real parts are zero).

23. Suppose $\pmb { f }$ is continuously differentiable [i.e., $f ^ { \prime } ( x )$ is continuous for all x] and $\mathbf { 2 } \pi \cdot$ -periodic. Without quoting Theorem 1.35, show that the Fourier series of $\pmb { f }$ converges in the mean. Hint: Use the relationship between the Fourier coefficients of $\pmb { f }$ and those of $f ^ { \prime }$ given in the proof of Theorem 1.30.

24. From Theorem 1.8, the Fourier series of an odd function consists only of sine terms. What additional symmetry conditions on $\pmb { f }$ will imply that the sine coefficients with even indices will be zero? Give an example of a function satisfying this additional condition.

25. Suppose that there is a sequence of nonnegative numbers $\{ M _ { n } \}$ such that $\textstyle \sum _ { n } M _ { n }$ is convergent. Suppose $\scriptstyle { a _ { n } }$ and $\pmb { b _ { n } }$ are given with

$$
\vert a _ { n } \vert , \vert b _ { n } \vert \leq M _ { n } \quad { \mathrm { f o r ~ a l l } } \quad n \geq 0 .
$$

Show that the following series is uniformly convergent on $- \infty < x < \infty$

$$
a _ { 0 } + \sum _ { n = 1 } ^ { \infty } a _ { n } \cos n x + b _ { n } \sin n x
$$

26. Prove the following version of the Riemann-Lebesgue lemma for infinite intervals: Suppose $\pmb { f }$ is a continuous function on $a \leq t < \infty$ with $\textstyle \int _ { a } ^ { \infty } | f ( t ) | d t <$ $\infty$ ;show that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { a } ^ { \infty } f ( t ) \cos n t d t = \operatorname* { l i m } _ { n \to \infty } \int _ { a } ^ { \infty } f ( t ) \sin n t d t = 0 .
$$

Hint: Break up the interval $a \leq t < \infty$ into two intervals, $a \leq t \leq M$ and $M \leq t < \infty$ , where $M$ is chosen so large that $\textstyle { \int _ { M } ^ { \infty } | f ( t ) | d t }$ is less than $\epsilon / 2 ;$ apply the usual Riemann-Lebesgue lemma to the first interval.

27. This exercise explores the ideas in the proof of Lemma 1.38 with a specific function. Let

$$
f ( t ) = \left\{ { \begin{array} { l l } { 0 } & { 0 \leq t \leq 1 / 2 } \\ { 1 } & { 1 / 2 < t \leq 1 . } \end{array} } \right.
$$

For $0 < \delta < 1 / 2$ , let

$$
g _ { \delta } ( t ) = \left\{ \begin{array} { l l } { 0 } & { 0 \leq t \leq 1 / 2 - \delta } \\ { \frac { t } { 2 \delta } - \frac { 1 } { 4 \delta } + \frac { 1 } { 2 } } & { 1 / 2 - \delta < t \leq 1 / 2 + \delta } \\ { 1 } & { 1 / 2 + \delta < t \leq 1 . } \end{array} \right.
$$

Graph both $\pmb { f }$ and $\pmb { 9 \delta }$ for $\pmb { \delta } = \mathbf { 0 . 1 }$ Show that as $\delta \mapsto 0$ $| | f - g _ { \delta } | | _ { L ^ { 2 } [ 0 , 1 ] } \mapsto 0 .$ . Note that $\pmb { 9 6 }$ is continuous but not differentiable. Can you modify the formula for $\pmb { \mathscr { s } } _ { \pmb { \delta } }$ so that $\pmb { \mathscr { g } } _ { \pmb { \delta } }$ is $C ^ { 1 }$ (one continuous derivative) and still satisfy $\operatorname* { l i m } _ { \delta \mapsto 0 } | | f - g _ { \delta } | | _ { L ^ { 2 } [ 0 , 1 ] } = 0 ?$ b

28. This exercise explains the Gibbs phenomenon, which is evident in the convergence of Fourier series near a point of discontinuity. We examine the Gibbs phenomenon for the Fourier series of the function

$$
f ( t ) = { \left\{ \begin{array} { l l } { \pi - t } & { 0 \leq t \leq \pi } \\ { - \pi - t } & { - \pi \leq t < 0 } \end{array} \right. }
$$

on the interval $- \pi \leq t \leq \pi$ (see Figure 21 for the graph of $\pmb { f }$ and its partial Fourier series). Complete the following outline.

![](images/9aaf378fc9621b044bb4421ac5d08a9829abf733c5a3a1de93df7242716b6976.jpg)  
Figure 21 Gibbs phenomenon

a)Show that the Fourier series for $\pmb { f }$ is

$$
2 \sum _ { n = 1 } ^ { \infty } { \frac { \sin n x } { n } } .
$$

(b) Let

$$
g _ { N } ( x ) = 2 \sum _ { n = 1 } ^ { N } \frac { \sin n x } { n } - ( \pi - x ) \nonumber .
$$

where $\pmb { \mathscr { g } } \pmb { N }$ represents the difference between the $f ( x )$ and the Nth partial sum of the Fourier series of $\pmb { f }$ .In the remaining parts of this exercise, you will show that the maximum value of $\pmb { \mathscr { g } } _ { \pmb { N } }$ is greater than 0.5 when $\pmb { N }$ is large and thus represents the Gibbs effect.

Show that $g _ { N } ^ { \prime } ( x ) = 2 \pi P _ { N } ( x )$ , where

$$
{ \begin{array} { r l } & { P _ { N } ( x ) = { \cfrac { 1 } { \pi } } \left( { \cfrac { 1 } { 2 } } + \cos x \cdots + \cos N x \right) } \\ & { \qquad = { \cfrac { 1 } { 2 \pi } } { \cfrac { \sin ( N + 1 / 2 ) x } { \sin ( x / 2 ) } } \quad { \mathrm { b y ~ L e m m a ~ 1 . 2 3 } } . } \end{array} }
$$

Show that $\theta _ { N } = \pi / ( N + 1 / 2 )$ is the first critical point of $\pmb { g } _ { N }$ to the right of $\pmb { x } = \pmb { 0 }$ .

Use the fundamental theorem of calculus and part (c) to show

$$
g _ { N } ( \theta _ { N } ) = \int _ { 0 } ^ { \theta _ { N } } { \frac { \sin ( N + 1 / 2 ) x } { \sin ( x / 2 ) } } d x - \pi .
$$

) Show

$$
\operatorname* { l i m } _ { N \to \infty } g _ { N } \langle \theta _ { N } \rangle = 2 \int _ { 0 } ^ { \pi } { \frac { \sin { x } } { x } } d x - \pi .
$$

Hint: Make a change of variables $\phi = ( N + 1 / 2 ) x$ and use the fact that $\sin t / t \to 1$ as $\mathbf { \Delta } \mathbf { \pmb { t } }  \mathbf { 0 }$ .

g) Show that

$$
2 \int _ { 0 } ^ { \pi } { \frac { \sin { x } } { x } } d x - \pi \approx 0 . 5 6 2
$$

by evaluating this integral numerically. Thus the Gibbs effect or the amount that the Nth partial sum overshoots the function $\pmb { f }$ is about 0.562 when $\pmb { N }$ is large.

29. Use Parseval's theorem and the series from Exercise 1 to find the sum of the series $\scriptstyle \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 4 } } }$

The next two exercises require a computer algebra system (e.g., Maple or MAT-LAB) to compute Fourier coefficients.

30. Consider the function

$$
f ( x ) = e ^ { - x ^ { 2 } / 1 0 } \left( \cos 2 x + 2 \sin 4 x + 0 . 4 \cos 2 x \cos 4 0 x \right) .
$$

For what values of $\scriptstyle { \pmb { n } }$ would you expect the Fourier coefficients ${ \pmb { a } } ( { \pmb { n } } )$ and ${ \pmb b } ( { \pmb n } )$ to be significant (say bigger than 0.01 in absolute value)? Why? Compute the ${ \pmb a } ( { \pmb n } )$ and ${ \pmb b } ( { \pmb n } )$ through $\pmb { n } = 5 0$ and see if you are right. Plot the partial Fourier series through $\pmb { n } = \pmb { 6 }$ and compare with the plot of the original $\pmb { f } ( \pmb { x } )$ .

31. Consider the function

$$
g ( x ) = e ^ { - x ^ { 2 } / 8 } \left( \cos 2 x + 2 \sin 4 x + 0 . 4 \cos 2 x \cos 1 0 x \right) .
$$

Compute the partial Fourier series through $N = 2 5$ Throw away any coefficients that are smaller than 0.01 in absolute value. Plot the resulting series and compare with the original function $\pmb { g } ( \pmb { x } )$ Try experimenting with different tolerances (other than 0.01).

The remaining exercises pertain to Fourier series as a tool for solving partial differential equations, as indicated at the beginning of this chapter.

32. Solve the following heat equation problem:

$$
\begin{array} { c } { { u _ { t } = u _ { x x } \quad \mathrm { f o r ~ } t > 0 , 0 \leq x \leq 1 } } \\ { { u ( 0 , x ) = x - x ^ { 2 } \quad \mathrm { f o r ~ } 0 \leq x \leq 1 } } \\ { { u ( 0 , t ) = u ( 1 , t ) = 0 . } } \end{array}
$$

If the boundary conditions $u ( 0 , t ) = A$ and $u ( 1 , t ) = B$ are not homogeneous (i.e., $\pmb { A }$ and $\pmb { B }$ are not necessarily zero), then the procedure given in Example 1.14 must be modified in order to solve the following heat equation:

$$
\begin{array} { c } { { u _ { t } = u _ { x x } \quad \mathrm { f o r ~ } t > 0 , 0 \leq x \leq 1 } } \\ { { u ( x , t ) = f ( x ) \quad \mathrm { f o r ~ } 0 \leq x \leq 1 } } \\ { { u ( 0 , t ) = A \quad u ( 1 , t ) = B . } } \end{array}
$$

Let $\pmb { L } ( \pmb { x } )$ be the linear function with ${ \pmb { \mathscr { L } } } ( { \bf 0 } ) = { \pmb { \mathscr { A } } }$ and ${ \cal L } ( 1 ) = B$ and let $\hat { \ b u } ( \ b x , t ) = \ b u ( \ b x , t ) - \ b L ( \ b x )$ Show that $\hat { \pmb u }$ solves the following problem:

$$
\begin{array} { c } { { \hat { u } _ { t } = \hat { u } _ { x x } \quad \mathrm { f o r ~ } t > 0 , 0 \leq x \leq 1 } } \\ { { \hat { u } ( x , t ) = f ( x ) - L ( x ) \quad \mathrm { f o r ~ } 0 \leq x \leq 1 } } \\ { { \hat { u } ( 0 , t ) = 0 , \quad \hat { u } ( 1 , t ) = 0 . } } \end{array}
$$

This heat equation can be solved for $\hat { \pmb { u } }$ using the techniques given in Example 1.14. The solution, $\mathbf { \Delta } _ { \mathbf { \mathcal { U } } }$ , to the original heat equation problem can then be found by the equation $u ( x , t ) = \hat { u } ( x , t ) + { \cal L } ( x )$

34.Use the procedure outlined in the previous exercise to solve the following heat equation:

$$
\begin{array} { c } { { u _ { t } = u _ { x x } \quad \mathrm { f o r ~ } t > 0 , 0 \leq x \leq 1 } } \\ { { u ( 0 , x ) = 2 - x ^ { 2 } \quad \mathrm { f o r ~ } 0 \leq x \leq 1 } } \\ { { u ( 0 , t ) = 2 , \quad u ( 1 , t ) = 1 . } } \end{array}
$$

35. Another important version of the heat equation is the following Neumann boundary value problem:

$$
\begin{array} { r l } & { u _ { t } = u _ { x x } \quad \mathrm { f o r ~ } t > 0 , 0 \leq x \leq 1 } \\ & { u ( 0 , x ) = f ( x ) \quad \mathrm { g i v e n ~ f o r ~ } 0 \leq x \leq 1 } \\ & { u _ { x } ( 0 , t ) = 0 , \quad u _ { x } ( 1 , t ) = 0 . } \end{array}
$$

This problem represents the standard heat equation, where ${ \pmb u } ( { \pmb x } , t )$ is the temperature of a rod of unit length at position $\pmb { x }$ and at time $\scriptstyle t _ { i }$ $\pmb { f } ( \pmb { x } )$ is the initial (at time $\pmb { t } = \pmb { 0 }$ )temperature at position $\pmb { x }$ The boundary conditions ${ \pmb u } _ { { \pmb x } } = { \pmb 0 }$ at $\pmb { x } = \pmb { 0 }$ and $\pmb { x } = \pmb { 1 }$ physically mean that no heat is escaping from the rod at its endpoints (i.e.; the rod is insulated at its endpoints). Use the procedure outlined at the beginning of this chapter to show that the general solution to this problem is given by

$$
\sum _ { k = 0 } ^ { \infty } a _ { k } e ^ { - ( k \pi ) ^ { 2 } t } \cos ( k \pi x )
$$

where ${ \pmb a } _ { { \pmb k } }$ are the coefficients of a Fourier cosine series of $\pmb { f }$ over the interval $0 \leq x \leq 1$ . Use this formula to obtain the solution in the case where $f ( x ) = x ^ { 2 } - x$ for ${ \boldsymbol { 0 } } \leq x \leq 1$ .

36. The goal of this problem is to prove Poisson's formula, which states that if $\pmb { f } ( t )$ is a piecewise smooth function on $- \pi \leq t \leq \pi$ ,then

$$
u ( r , \phi ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) \frac { 1 - r ^ { 2 } d t } { 1 - 2 \cos ( \phi - t ) + r ^ { 2 } } ,
$$

for $0 \leq r \leq 1$ , $0 \leq \phi \leq 2 \pi$ solves Laplaces equation

$$
\Delta u = u _ { x x } + u _ { y y } = 0
$$

in the unit disc $x ^ { 2 } + y ^ { 2 } = 1$ (in polar coordinates: $\{ r < 1 \}$ with boundary values $u ( r = 1 , \phi ) = f ( \phi ) , - \pi \leq \phi \leq \pi$ Follow the outline given to establish this formula:

Show that the function $u ( x , y ) = ( x + i y ) ^ { n }$ solves Laplaces equation for each value of $\mathfrak { n } = 0 , 1 , 2 , \ldots$ Using complex notation $z = x + i y$ , this solution can be written as $u ( z ) = z ^ { n }$ :   
S $\scriptstyle \sum _ { n = - N } ^ { N } A _ { n } z ^ { n }$ ,ovve $| N |  \infty )$ converges uniformly and absolutely for $| z | = 1$ , then the infinite series $\scriptstyle \sum _ { n = - \infty } ^ { \infty } A _ { n } z ^ { n }$ solve aplae' qutio $\{ | z | < 1 \}$ Write this function in polar coordinates with $z = r e ^ { i \phi }$ .   
c)In order to solve Laplace's equation, we must hunt for a solution of th he form $\begin{array} { r } { u ( r , \phi ) = \sum _ { n = - \infty } ^ { \infty } A _ { n } r ^ { | n | } e ^ { i n \phi } } \end{array}$ with boundary condition ${ \pmb u } ( { \pmb r } =$ $1 , \phi ) = f ( \phi )$ .Show that the boundary condition is satisfied if $A _ { n }$ is set to the Fourier coefficients of $\pmb { f }$ in complex form.   
(d) Using the formula for the complex Fourier coefficients, show that if $\pmb { f }$ is real valued, then $A _ { - n } = \overline { { A _ { n } } }$ Use this fact to rewrite the solution in the previous step as

$$
u ( r , \phi ) = \frac { 1 } { 2 \pi } \mathrm { R e } \left\{ \int _ { - \pi } ^ { \pi } f ( t ) \left[ 2 ( \sum _ { n = 0 } ^ { \infty } r ^ { n } e ^ { i n ( \phi - t ) } ) - 1 \right] \right\} .
$$

(e) Now use the geometric series formula to rewrite the solution in the previous step as

$$
u ( r , \phi ) = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( t ) P ( r , \phi - t ) d t
$$

where

$$
P ( r , u ) = { \mathrm { R e } } \{ \frac { 2 } { 1 - r e ^ { i u } } - 1 \} .
$$

Rewrite $\pmb { P }$ as

$$
P ( r , u ) = \frac { 1 - r ^ { 2 } } { 1 - 2 r \cos u + r ^ { 2 } } .
$$

Use this formula together with the previous integral formula for $\pmb { u }$ to establish (1.41).

# Chapter 2

# The Fourier Transform

In this chapter, we develop the Fourier transform and its inverse. The Fourier transform can be thought of as a continuous form of Fourier series. A Fourier series decomposes a signal on $[ - \pi , \pi ]$ into components that vibrate at integer frequencies. By contrast, the Fourier transform decomposes a signal defined on an infinite time interval into a $\lambda$ -frequency component, where $\pmb { \lambda }$ can be any real (or even complex) number. Besides being of interest in their own right, the topics in this chapter will be important in the construction of wavelets in later chapters.

# 2.1 Informal Development of the Fourier Transform

# 2.1.1 The Fourier Inversion Theorem

In this section, we give an informal development of the Fourier transform and its inverse. Precise arguments are given in Appendix A.

To obtain the Fourier transform, we consider the Fourier series of a function defined on the interval $- l \leq x \leq l$ and then let $\iota$ go to infinity. Recall from Theorem 1.20 (with $a = 4$ that a function defined on $- l \leq x \leq l$ can be expressed as

$$
f ( x ) = \sum _ { n = - \infty } ^ { \infty } \alpha _ { n } e ^ { i n \pi x / \ell }
$$

where

$$
\alpha _ { n } = \frac { 1 } { 2 l } \int _ { - l } ^ { l } f ( t ) e ^ { - i n \pi t / l } d t .
$$

If $\pmb { f }$ is defined on the entire real line, then it is tempting to let $l _ { \mathbf { \delta g } \mathbf { o } }$ to infinity and see how the preceding formulas are affected. Substituting the expression for $\alpha _ { n }$ into the previous sum, we obtain

$$
\begin{array} { l } { f ( x ) = \displaystyle \operatorname* { l i m } _ { l \to \infty } \left[ \sum _ { n = - \infty } ^ { \infty } \left( \frac { 1 } { 2 l } \int _ { - l } ^ { l } f ( t ) e ^ { - i n \pi t / l } d t \right) e ^ { i n \pi x / l } \right] } \\ { \displaystyle = \operatorname* { l i m } _ { l \to \infty } \left[ \sum _ { n = - \infty } ^ { \infty } \frac { 1 } { 2 l } \int _ { - l } ^ { l } f ( t ) e ^ { i n \pi ( x - t ) / l } d t \right] . } \end{array}
$$

Our goal is to recognize the sum on the right as the Riemann sum formulation of an integral. To this end, let $\begin{array} { r } { \lambda _ { n } = \frac { n \pi } { k } } \end{array}$ and $\Delta \lambda = \lambda _ { n + 1 } - \lambda _ { n } = \frac { \pi } { t }$ We obtain

$$
f ( x ) = \operatorname* { l i m } _ { l  \infty } \sum _ { n = - \infty } ^ { \infty } [ { \frac { 1 } { 2 \pi } } \int _ { - l } ^ { l } f ( t ) e ^ { \lambda _ { n } i ( x - t ) } d t ] \Delta \lambda
$$

Let

$$
F _ { l } ( \lambda ) = { \frac { 1 } { 2 \pi } } \int _ { - l } ^ { l } f ( t ) e ^ { \lambda i ( x - t ) } d t .
$$

The sum in (2.1) is now

$$
\sum _ { n = - \infty } ^ { \infty } F _ { l } ( \lambda _ { n } ) \Delta \lambda .
$$

This term resembles the Riemann sum definition of the integral $\begin{array} { r } { \int _ { - \infty } ^ { \infty } F _ { l } ( \lambda ) d \lambda } \end{array}$ . As $\iota$ converges to $\tilde { \infty }$ the quantity $\Delta \dot { \lambda }$ converges to O and so $\pmb { \triangle } \lambda$ becomes the $\pmb { d \lambda }$ in the integral $\textstyle { \int _ { - \infty } ^ { \infty } F _ { l } ( \lambda ) d \lambda }$ So (2.1) becomes

$$
f ( x ) = \operatorname* { l i m } _ { l \mapsto \infty } \int _ { - \infty } ^ { \infty } F _ { l } ( \lambda ) d \lambda .
$$

As $l \mapsto \infty , F _ { l } ( \lambda )$ formally becomes the integral ${ \begin{array} { l } { { \frac { 1 } { 2 \pi } } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { i \lambda ( x - t ) } d t } \end{array} }$ Therefore,

$$
f ( x ) = { \frac { 1 } { 2 \pi } } \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { i \lambda ( x - t ) } d t d \lambda
$$

or

$$
f ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } \left( { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i \lambda t } d t \right) e ^ { i \lambda x } d x .
$$

We let $\widehat { f } ( \lambda )$

$$
{ \widehat { f } } ( \lambda ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i \lambda t } d t .
$$

The function $\widehat { f } ( \lambda )$ is called the (complex form of the) Fourier transform of $\pmb { f }$ . Equation (2.2) becomes

$$
f ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } { \widehat { f } } ( \lambda ) e ^ { i \lambda x } d \lambda ,
$$

which is often referred to as the Fourier inversion formula since it describes $\pmb { f } ( \pmb { x } )$ as an integral involving the Fourier transform of $\pmb { f }$ .

We summarize this discussion in the following theorem.

THEOREM 2.1 If $\pmb { f }$ is acontinuously differentiablefunctionwh $\textstyle \int _ { - \infty } ^ { \infty } | f ( t ) | d t <$ $\infty$ , then

$$
f ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } { \widehat { f } } ( ( \not \nabla ) e ^ { i \theta / { \cal R } \not \varepsilon } d \lambda
$$

where $\widehat { f } ( \lambda )$ (the Fourier transform of $f _ { \ast }$ ) is given by

$$
{ \widehat { f } } ( \lambda ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i \lambda t } d t .
$$

The preceding argument is not rigorous since we have not justified several steps, including the convergence of the improper integral $\int _ { - \infty } ^ { \infty } { \tilde { F _ { l } } } ( \lambda ) d \lambda$ As with the development of Fourier series (see Theorem 1.28), if the function $\pmb { f } ( \pmb { x } )$ has points of discontinuity, such as a step function, then the preceding formula holds with $\pmb { f } ( \pmb { x } )$ replaced by the average of the left- and right-hand limits [i.e., $( f ( x + 0 ) + f ( x - 0 ) ) / 2 ]$ .Rigorous proofs of these results are given in Appendix A.

The assumption $\int _ { - \infty } ^ { \infty } | f ( t ) | d t < \infty$ in Theorem 2.1 is needed in order to make sense out of the improper integral defining ${ \widehat { f } } ;$ that is,

$$
\begin{array} { r l r } {  { | \widehat { f } ( \lambda ) | \leq \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } | f ( t ) e ^ { - \mathrm { i } \lambda t } | d t } } \\ & { } & \\ & { } & { = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } | f ( t ) | d t \quad \mathrm { s i n c e } \ | e ^ { - \mathrm { i } \lambda t } | = 1 } \\ & { } & \\ & { } & { < \infty . } \end{array}
$$

Comparison with Fourier Series. The complex form of the Fourier transform of $\pmb { f }$ and the corresponding inversion formula are analogons to the complex form of the Fourier series of $\pmb { f }$ over the interval $- l \leq x \leq l$

$$
f ( x ) = \sum _ { n = - \infty } ^ { \infty } \widehat { f } _ { n } e ^ { \# \widehat { p } \widehat { \mathcal { M } } x }
$$

where

$$
\widehat { f } _ { n } = \frac { 1 } { 2 l } \int _ { - l } ^ { l } f ( t ) e ^ { \frac { - i n \pi } { l } t } d t .
$$

The variable_ λ in the Fourier inversion formula, (2.3), plays the role of $\textstyle { \frac { n \pi } { k } }$ in (2.4). The sum over $\pmb { n }$ from $- \infty$ to $\infty$ in (2.4) is replaced by an integral with respect to $\lambda$ from $- \infty$ to $\infty$ defining (2.3). The formulas for $\widehat { f } _ { n }$ and $\widehat { f } ( \lambda )$ are also analogous. The integral over $[ - l , \ l ]$ in the formula for $\widehat { f } _ { n }$ is analogous to the integral over $( - \infty , \infty )$ in $\hat { f } ( \lambda )$ .In the case of Fourier series, $\hat { f } _ { n }$ measures the component of $\pmb { f }$ that oscillates at frequency $\pmb { \mathscr { n } }$ Likewise, $\hat { f } ( \lambda )$ measures the frequency component of $\pmb { f }$ that oscillates with frequency $\lambda .$ If $\pmb { f }$ is defined on a finite interval, then its Fourier series is a decomposition of $\pmb { \mathscr { f } }$ into a discrete set of oscillating frequencies (i.e., $\hat { f } _ { n }$ , one for ea¢h integer. $\pmb { n }$ ). For a function on an infinite interval, there is a continuum of frequencies since the frequency component, $\hat { f } ( \lambda )$ , is defined for each real number $\lambda$ These ideas are illustrated in the following examples.

# 2.1.2 Examples

# EXAMPLE 2.2

In our first example, we will compute the Fourier transform of the rectangular wave (see Figure 1):

$$
f ( t ) = \left\{ { \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } - \pi \leq t \leq \pi } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} } \right.
$$

Now we have $f ( t ) e ^ { - i \lambda t } = f ( t ) ( \cos \lambda t - i \sin \lambda t )$ .Since $\pmb { f }$ is an even. function, $f ( t ) \sin ( \lambda t )$ is an odd function and its integral over the real line is.zero. Therefore, the Fourier transform of $\pmb { f }$ is reduced to

$$
{ \begin{array} { r l } & { { \widehat { f } } ( \lambda ) = { \frac { 1 } { \sqrt { 2 \pi } } } \displaystyle \int _ { - \infty } ^ { \infty } f ( t ) \cos ( \lambda t ) d t } \\ & { \qquad = { \frac { 1 } { \sqrt { 2 \pi } } } \displaystyle \int _ { - \pi } ^ { \pi } \cos ( \lambda t ) d t } \\ & { \qquad = { \frac { { \sqrt { 2 } } \sin ( \lambda \pi ) } { \sqrt { \pi } \lambda } } . } \end{array} }
$$

A graph of $\widehat { \pmb f }$ is given in Figure 2.

As already mentioned, the Fourier transform, $\widehat { f } ( \lambda )$ , measures the frequency component of $\pmb { f }$ that vibrates with frequency $\lambda$ In this example, $\pmb { f }$ is a piecewise constant function. Since a constant vibrates with zero frequency, we should expect that the largest values of $\widehat { f } ( \lambda )$ occur when $\lambda$ is near zero. The graph of $\widehat { \pmb f }$ clearly illustrates this feature.

![](images/39b0775a2170b4673b84a95add64f84587b3132473848f41621d0390b98a34f4.jpg)  
Figure 1 Rectangular wave

![](images/ae79e0fd5958f1f4fb9f49235b0cdb9c78a2ae03f305a7b660b85cdbc01931da.jpg)  
Figure 2 Fourier transform of a rectangular wave

Let

$$
f ( t ) = { \left\{ \begin{array} { l l } { c o s \ 3 \ell } & { i \ell - \pi \leq \ell \leq \pi } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

(see Figure 3).

Since f is an even function, only the cosine part of the transform contributes:

$$
{ \widehat { f } } ( \lambda ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } f ( t ) \cos ( \lambda t ) d t = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \pi } ^ { \pi } \cos ( 3 t ) \cos ( \lambda t ) d t .
$$

The preceding integral is le as an exercise [u the ientites

$$
\begin{array} { r } { \cos ( u + v ) = \cos u \cos v - \sin u \sin v } \\ { \cos ( u - v ) = \cos u \cos v + \sin u \sin v } \end{array}
$$

with $\scriptstyle { \boldsymbol { \mathscr { u } } } = 3 t$ and ${ \pmb v } = \lambda t$ and then integrate]. The result is

$$
{ \widehat { f } } ( \lambda ) = { \frac { { \sqrt { 2 } } \lambda \sin ( \lambda \pi ) } { { \sqrt { \pi } } ( 9 - \lambda ^ { 2 } ) } } .
$$

The graph of $\widehat { \pmb f }$ is given in Figure 4.

Note that the Fourier transform peaks at $\lambda = 3$ and $^ { - 3 }$ This behavior should be expected since $f ( t ) = \cos ( 3 t )$ vibrates with frequency 3 on the interval $- \pi \leq t \leq \pi$ .

![](images/13f0dcfa3381883aab0458bcc981daa8a6c887278404ef8e95e8e3d9a57ec5d5.jpg)  
Figure 3 Plot of $\cos ( 3 t )$

![](images/30103d38c19cfdaa93ac733df37bf1fe0711e0e101b9d5f955bdf11706539bb3.jpg)  
Figure 4 Fourier transform of $\cos ( 3 t )$

# EXAMPLe 2.4

Let

$$
f ( t ) = { \left\{ \begin{array} { l l } { \sin 3 t } & { { \mathrm { i f ~ } } - \pi \leq t \leq \pi } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

Since $\pmb { f }$ is an odd function, only the sine part of the transform contributes (which is purely imaginary). The transform is

$$
{ \begin{array} { r l } & { { \widehat { f } } ( \lambda ) = { \frac { - i } { \sqrt { 2 \pi } } } \displaystyle \int _ { - \infty } ^ { \infty } f ( t ) \sin ( \lambda t ) d t } \\ & { \qquad = { \frac { - i } { \sqrt { 2 \pi } } } \displaystyle \int _ { - \pi } ^ { \pi } \sin ( 3 t ) \sin ( \lambda t ) d t } \\ & { \qquad = { \frac { - 3 { \sqrt { 2 } } i \sin ( \lambda \pi ) } { \sqrt { \pi } ( 9 - \lambda ^ { 2 } ) } } . } \end{array} }
$$

# EXaMPLe 2.5

The next example is a triangular wave whose graph is given in Figure 5. The analytical formula for this graph is given by

$$
f ( t ) = { \left\{ \begin{array} { l l } { t + \pi } & { { \mathrm { i f ~ } } - \pi \leq t \leq 0 } \\ { \pi - t } & { { \mathrm { i f ~ } } 0 < t \leq \pi } \\ { 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

![](images/bf6ac8437211bdb1ff1ae610fa33bc889cd04f2b8bad07f230558444d9f50a0d.jpg)  
Figure 5 Triangular wave

This function is eveh and $\approx$ its Fourier transform is given by

$$
{ \widehat { f } } ( \lambda ) = { \frac { 2 } { \sqrt { 2 \pi } } } \int _ { 0 } ^ { \infty } f ( t ) \cos ( \lambda t ) d t = { \frac { 2 } { \sqrt { 2 \pi } } } \int _ { 0 } ^ { \pi } ( \pi - t ) \cos ( \lambda t ) d t .
$$

This integral can be computed using integration by parts:

$$
{ \widehat { f } } ( \lambda ) = { \sqrt { \frac { 2 } { \pi } } } { \frac { ( 1 - \cos ( \lambda \pi ) ) } { \lambda ^ { 2 } } } .
$$

The graph of $\widehat { \pmb f }$ is given in Figure 6.

Note that the Fourier transforms in Examples 2.4 and 2.5 decay at the rate $1 / \lambda ^ { 2 }$ -as $\lambda \mapsto \infty$ ,which is faster than the decay rate of $1 / \lambda$ exhibited by the Fourier transforms in Examples 2.2 and 2.3. The faster decay in Examples 2.4 and 2.5 results from the continuity of the functions in these examples. Note the parallel with the examples in Chapter 2. The Fourier coefficients, ${ a _ { n } }$ and $b _ { n }$ , for the discontinuous function in Example 1.9 decay like $y _ { a }$ whereas the Fourier coefficients for the continuous function in Example 1.10 decav like $1 / \pi ^ { 2 }$ : •

# 2.2 Properties of the Fourier Transform

# 2.2.1 Basic Properties

In this section, we set down most of the basic properties of the Fourier transform. First, we introduce the alternative notation

$$
{ \mathcal { F } } [ f ] ( \lambda ) = { \widehat { f } } ( \lambda )
$$

![](images/f55f3b266e46a8c137541f70d532dc7d0d98ecb1979ae39073f8553ae7977571.jpg)  
Figure 6 Fourier transform of the triangular wave

for the Fourier transform of $\pmb { f }$ . This notation has advantages when discussing some of the operator theoretic properties of the Fourier transform. The Fourier operator $\pmb { \mathcal { F } }$ should be thought of as a mapping whose domain and range are the space of complex-valued functions defined on the real line. The input of $\pmb { \mathcal { F } }$ is a function, say $\pmb { f }$ , and returns another function, ${ \mathcal { F } } [ f ] = { \widehat { \boldsymbol { f } } }$ , as its output.

In a similar fashion, we define the inverse Fourier transform operator as

$$
{ \mathcal { F } } ^ { - 1 } \{ f \} ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } f ( \lambda ) e ^ { i \lambda x } d \lambda .
$$

Theorem 2.1 implies that $\mathcal { F } ^ { - 1 }$ really is the inverse of $\mathcal { F }$ .

$$
\mathcal { F } ^ { - 1 } [ \mathcal { F } [ f ] ] = f
$$

because

$$
\begin{array} { l } { { \displaystyle { \mathcal { F } } ^ { - 1 } [ { \mathcal { F } } [ f ] ] ( x ) = { \mathcal { F } } ^ { - 1 } [ \widehat f ] ( x ) \qquad \mathrm { b y ~ d e f n i t i o n ~ o f } } \ ~ } \\ { { \displaystyle ~ = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \widehat f ( \lambda ) e ^ { i \lambda x } d \lambda \qquad \mathrm { b y ~ d e f n i t i o n ~ o f ~ } { \mathcal { F } } ^ { - 1 } [ \widehat f ] } \ ~ } \\ { { \displaystyle ~ = f ( x ) \qquad \mathrm { b y ~ T h e o r e n ~ } 2 . 1 } . } \end{array}
$$

Some properties of the Fourier transform and its inverse are given in the following theorem. Other basic properties are given in the exercises.

THEOREM 2.6 Let $\pmb { f }$ and $\pmb { \mathscr { g } }$ be differentiable functions defined on the real line with $\pmb { f } ( t ) = \pmb { 0 }$ for large $\left| t \right|$ The following properties hold.

1The Fourier transform and its inverse are linear operators. That is, for any constant $\pmb { c }$ .

$$
\begin{array} { r } { \mathcal { F } [ f + g ] = \mathcal { F } [ f ] + \mathcal { F } [ g ] \quad \mathit { a n d } \quad \mathcal { F } [ c f ] = c \mathcal { F } [ f ] . } \\ { \mathcal { F } ^ { - 1 } [ f + g ] = \mathcal { F } ^ { - 1 } [ f ] + \mathcal { F } ^ { - 1 } [ g ] \quad \mathit { a n d } \quad \mathcal { F } ^ { - 1 } [ c f ] = c \mathcal { F } ^ { - 1 } [ f ] . } \end{array}
$$

2.The Fourier transform of a product of $\pmb { f }$ with $t ^ { n }$ is given by

$$
{ \mathcal { F } } [ t ^ { n } f ( t ) ] ( \lambda ) = ( i ^ { n } ) { \frac { d ^ { n } } { d \lambda ^ { n } } } \{ { \mathcal { F } } [ f ] ( \lambda ) \} .
$$

3The inverse Fourier transform of a product of $\pmb { f }$ with $\lambda ^ { n }$ is given by

$$
{ \mathcal { F } } ^ { - 1 } [ \lambda ^ { n } f ( \lambda ) ] ( t ) = ~ . . . ~ i ) \mathbb { Y } { \frac { d ^ { n } } { d t ^ { n } } } \{ { \mathcal { F } } ^ { - 1 } [ f ] ( t ) \} .
$$

4The Fourier transform of an nth derivative is given by

$$
{ \mathcal { F } } [ f ^ { ( n ) } ] ( \lambda ) = ( i \lambda ) ^ { n } { \mathcal { F } } [ f ] ( \lambda )
$$

[here $f ^ { ( n ) }$ stands for the h rivati $_ { f l }$

5.The inverse Fourier transform of an nth derivative is given by

$$
\mathcal { F } ^ { - 1 } [ f ^ { ( n ) } ] ( t ) = ( - i t ) ^ { n } \mathcal { F } ^ { - 1 } [ f ] ( t ) .
$$

6.The Fourier transform of a translation is given by

$$
\mathcal { F } [ f ( t - a ) ] ( \lambda ) = e ^ { - i \lambda a } \mathcal { F } [ f ] ( \lambda ) .
$$

7The Fourier transform of a rescaling is given by

$$
\mathcal { F } [ f ( b t ) ] ( \lambda ) = \frac { 1 } { b } \mathcal { F } [ f ] ( \frac { \lambda } { b } ) .
$$

8. If $\pmb { f } ( t ) = \pmb { 0 }$ for ${ \pmb t } < { \pmb 0 }$ , then

$$
{ \mathcal { F } } [ f ] ( \lambda ) = { \frac { 1 } { \sqrt { 2 \pi } } } { \mathcal { L } } [ f ] ( i \lambda )
$$

where $\pmb { \iota } ( f ] ) i s$ the Laplace transform of $\pmb { f }$ defined by

$$
{ \mathcal { L } } [ f ] ( s ) = \int _ { 0 } ^ { \infty } f ( t ) e ^ { - t s } d t .
$$

Proof We prove each part separately.

1. The linearity of the Fourier transform follows from the linearity of the integral, as we demonstrate in the following:

$$
\begin{array} { l } { \displaystyle \mathcal { F } [ f + g ] ( \lambda ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } [ f ( t ) + g ( t ) ] e ^ { - i \lambda t } d t } \\ { \displaystyle \qquad = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i \lambda t } d t + \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } g ( t ) e ^ { - i \lambda t } d t } \\ { \displaystyle \qquad = \mathcal { F } [ f ] ( \lambda ) + \mathcal { F } [ g ] ( \lambda ) . } \end{array}
$$

The proof for ${ \mathcal { F } } [ c f ] = c { \mathcal { F } } [ f ]$ is similar, as are the proofs for the corresponding facts for the inverse Fourier transform.

23. For the Fourier transform of a product of $\pmb { f }$ with $t ^ { n }$ , we have

$$
{ \mathcal { F } } [ t ^ { n } f ( t ) ] ( \lambda ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } t ^ { n } f ( t ) e ^ { - i \lambda t } d t .
$$

Using the equation

$$
t ^ { n } f ( t ) e ^ { - i \lambda t } = ( i ) ^ { n } { \frac { d ^ { n } } { d \lambda ^ { n } } } \{ f ( t ) e ^ { - i \lambda t } \} ,
$$

we obtain

$$
\begin{array} { c } { { \mathcal { F } [ t ^ { n } f ( t ) ] ( \lambda ) = ( i ) ^ { n } \displaystyle \frac { d ^ { n } } { d \lambda ^ { n } } \left\{ \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i \lambda t } d t \right\} } } \\ { { = ( i ) ^ { n } \displaystyle \frac { d ^ { n } } { d \lambda ^ { n } } \{ \mathcal { F } [ f ] ( \lambda ) \} . } } \end{array}
$$

The corresponding property for the inverse Fourier transform is proved similarly.

45. For the Fourier transform of the nth derivative of $\pmb { f }$ , we have

$$
\mathcal { F } [ f ^ { ( n ) } ( t ) ] ( \lambda ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ^ { ( n ) } ( t ) e ^ { - i \lambda t } d t .
$$

We now integrate by parts; that is,

$$
\int _ { - \infty } ^ { \infty } u d v = u v \Big | _ { - \infty } ^ { \infty } - \int _ { - \infty } ^ { \infty } v d u
$$

with $d v = f ^ { ( n ) }$ and $u = e ^ { - i \lambda t }$ As we will see, this process has the effect of transferring the derivatives from $f ^ { ( n ) }$ to $e ^ { - i \lambda t }$ .Since $\pmb { f }$ vanishes at $+ \infty$

and $- \infty$ by hypothesis, there are no boundary terms. So we have

$$
\begin{array} { c } { { \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ^ { ( n ) } ( t ) e ^ { - i \lambda t } d t = - \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ^ { ( n - 1 ) } ( t ) \displaystyle \frac { d } { d t } \{ e ^ { - i \lambda t } \} d t ~ \ ( \mathrm { b y ~ p a r t s } ) } } \\ { { = ( i \lambda ) \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ^ { ( n - 1 ) } ( t ) e ^ { - i \lambda t } d t . } } \end{array}
$$

Note that integration by parts has reduced the number of derivatives on $\pmb { f }$ by one $[ f ^ { ( n ) }$ becomes $f ^ { ( n - 1 ) } ]$ We have also gained one factor f $_ { i \lambda }$ By repeating this process $\pmb { n } - \pmb { 1 }$ additional times, we obtain

$$
{ \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } f ^ { ( n ) } ( t ) e ^ { - i \lambda t } d t = ( i \lambda ) ^ { n } { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i \lambda t } d t
$$

as desired. The proof for the corresponding fact for the inverse Fourier transform is similar.

6-7. The translation and rescaling properties can be combined into the following statement:

$$
\mathcal { F } [ f ( b t - a ) ] ( \lambda ) = \frac { 1 } { b } e ^ { - i \lambda a / b } \mathcal { F } [ f ] ( \lambda / b ) .
$$

This equation can be established by the following change-of-variables argument:

$$
\begin{array} { r } { \mathcal { F } [ f ( b t - a ) ] ( \lambda ) = \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ( b t - a ) e ^ { - i \lambda t } d t } \\ { = \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ( s ) e ^ { - i \lambda ( \frac { s + a } { b } ) } \frac { d s } { b } } \end{array}
$$

where the second equality follows from the change of variables $\pmb { s } = \pmb { b } t - \pmb { a }$ {and so $\pmb { t } = ( \pmb { s } + \pmb { a } ) / b$ and $\begin{array} { r } { d t = \frac { d s } { b } ] } \end{array}$ . Rewriting the exponential on the right as

$$
e ^ { - i \lambda ( \frac { s + a } { b } ) } = e ^ { \frac { - i \lambda a } { b } } e ^ { - i \frac { \lambda } { b } s } .
$$

we obtain

$$
\begin{array} { c l c r } { { \mathcal { F } [ f ( b t - a ) ] ( \lambda ) = e ^ { \frac { - i \lambda a } { b } } \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ( s ) e ^ { - i \frac { \lambda } { b } s } \displaystyle \frac { d s } { \star } } } \\ { { = e ^ { \frac { - i \lambda a } { b } } \displaystyle \frac { 1 } { b } \mathcal { F } [ f ] ( \frac { \lambda } { b } ) . } } \end{array}
$$

8. The final part of the theorem, regarding the relationship of the Fourier and Laplace transforms, follows from their definitions and is left to the exercises. This completes the proof. $\bullet$

# EXAMPLe 2.7

We illustrate the fourth property of Theorem 2.6 with the function in Example 2.4:

$$
f ( t ) = { \left\{ \begin{array} { l l } { \sin 3 t } & { { \mathrm { i f ~ } } - \pi \leq t \leq \pi } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

whose Fourier transform is

$$
{ \widehat { f } } ( \lambda ) = { \frac { - 3 { \sqrt { 2 } } i \sin ( \lambda \pi ) } { \sqrt { \pi } ( 9 - \lambda ^ { 2 } ) } } .
$$

The derivative of $\pmb { f }$ is $\scriptstyle 3 \cos 3 t$ on $- \pi \leq t \leq \pi$ , which is just a multiple of 3 times the function given in Example 2.3. Therefore, from Example 2.3,

$$
{ \widehat { f ^ { \prime } } } ( \lambda ) = { \frac { 3 { \sqrt { 2 } } \lambda \sin ( \lambda \pi ) } { \sqrt { \pi } ( 9 - \lambda ^ { 2 } ) } } .
$$

The fourth property of Theorem 2.6 (with $\pmb { n } = \pmb { 1 }$ states

$$
\widehat { f } ^ { \prime } ( \lambda ) = i \lambda \widehat { f } ( \lambda ) = - i \lambda \frac { 3 \sqrt { 2 } i \sin ( \lambda \pi ) } { \sqrt { \pi } ( 9 - \lambda ^ { 2 } ) } .
$$

This expression for ${ \hat { f } } ^ { \prime } ( \lambda )$ agrees with (2.7).

# EXaMPle 2.8

In this example, we illustrate the scaling property:

$$
\mathcal { F } [ f ( b t ) ] ( \lambda ) = \frac { 1 } { b } \mathcal { F } [ f ] ( \frac { \lambda } { b } ) .
$$

If $b > 1$ , then the graph of $f ( b t )$ is a compressed version of the graph of $\pmb { f }$ The dominant frequencies of $f ( b t )$ are larger than those of $\pmb { f }$ by a factor of $b$ This behavior is illustrated nicely by the function in Example 2.4:

$$
f ( t ) = { \left\{ \begin{array} { l l } { \sin 3 t } & { { \mathrm { i f ~ } } - \pi \leq t \leq \pi } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

whose graph is given in Figure 7. The graph of $f ( 2 t )$ is given in Figure 9. Note that the frequency $f ( 2 t )$ is double that of $\pmb { f }$ .

Increasing the frequency of a signal has the effect of stretching the graph of its Fourier transform. In the preceding example, the dominant frequency of $\pmb { f } ( t )$ . is 3 whereas the dominant frequency of $f ( 2 t )$ is 6. Thus the maximum value of $\vert \widehat { f } ( \lambda ) \vert$ occurs at $\lambda = 3$ (see Figure 8) whereas the maximum value of the Fourier transform of $f ( 2 t )$ occurs at $\lambda = 6$ (see Figure 10). Thus the latter graph is obtained by stretching the former graph by a factor of 2. Note also that the graph of $\widehat { f ( \lambda / 2 ) }$ is obtained by stretching the graph of $\widehat { f ( \lambda ) }$ by a factor of 2.

![](images/70a3c8326d3c6a6adbee5cd4095d8b9a4ad43151058bcf73f0db531bd75a5406.jpg)  
Figure 7 Plot of $\sin ( 3 t ) , - \pi \leq t \leq \pi$

![](images/e4d963f088e365788739aa8153a70659a2dda73ce161f58771f0a5a10089aa5b.jpg)  
Figure 8 Plot of Fourier transform of $\sin ( 3 t )$

This discussion illustrates the following geometrical interpretation of equation (2.8) in the case where $\smash { b > 1 }$ Compressing the graph of $\pmb { f }$ speeds up the frequency and therefore stretches the graph of $\widehat { f } ( \lambda )$ . If $0 < b < 1$ ,then the graph of $f ( b t )$ is stretched, which slows the frequency and therefore compresses the graph of $\widehat { f } ( \lambda )$ .

# 2.2.2 Fourier Transform of a Convolution

Now we examine how the Fourier transform behaves under convolutions. First, we give the definition of the convolution of two functions.

![](images/be14b41746e85a2770a05bfa80f028d0bcf7330bec24a6a71726fb8f860add45.jpg)  
Figure 9 Plot of $\sin ( 6 t ) - \pi / 2 \leq t \leq \pi / 2$

![](images/f321c9ad6c825f3b2a31dd318ab4bee25184aeae61c684a918328d28589822f6.jpg)  
Figure 10 Plot of Fourier transform of sin(6t)

DEfINITIoN 2.9 Suppose $\pmb { f }$ and $\pmb { \mathscr { g } }$ are two square-integrable functions. The convolution of $\pmb { f }$ and $\pmb { \mathscr { g } }$ , denoted $f * g$ , is defined by

$$
( f * g ) ( t ) = \int _ { - \infty } ^ { \infty } f ( t - x ) g ( x ) d x .
$$

The preceding definition is equivalent to

$$
( f * g ) ( t ) = \int _ { - \infty } ^ { \infty } f ( x ) g ( t - x ) d x
$$

(perform the change of variables $\pmb { y } = \pmb { t } - \pmb { x }$ and then relabel the variable $\pmb { y }$ back to $\pmb { x }$ .

We have the following theorem on the Fourier transform of a convolution of two functions.

THEOreM 2.10 Suppose $\pmb { f }$ and $\pmb { \mathscr { g } }$ are two integrable functions. Then

$$
\begin{array} { c } { { \mathcal { F } [ f * g ] = \sqrt { 2 \pi } \widehat { f } \cdot \widehat { g } } } \\ { { \mathcal { F } ^ { - 1 } [ \widehat { f } \cdot \widehat { g } ] = \displaystyle \frac { 1 } { \sqrt { 2 \pi } } f * g . } } \end{array}
$$

Proof To derive the first equation, we use the definitions of the Fourier transform and convolution:

$$
\begin{array} { l } { \displaystyle \mathcal { F } [ f * g ] ( \lambda ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } ( f * g ) ( t ) e ^ { - i \lambda t } d t } \\ { \displaystyle = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } f ( t - x ) g ( x ) d x e ^ { - i \lambda t } d t . } \end{array}
$$

We write $e ^ { - i \lambda t } = e ^ { - i \lambda ( t - x ) } e ^ { - i \lambda x }$ Ai at obtain

$$
\mathcal { F } [ f * g ] ( \lambda ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } f ( t - x ) e ^ { - i \lambda ( t - x ) } g ( x ) d t e ^ { - i \lambda x } d x .
$$

Letting $\begin{array} { r } { \pmb { s } = \pmb { t } - \pmb { x } , } \end{array}$ , we obtain

$$
\mathcal { F } [ f * g ] ( \lambda ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } f ( s ) e ^ { - i \lambda s } d s g ( x ) e ^ { - i \lambda x } d x .
$$

The right side can be rewritten as

$$
 \sqrt { 2 \pi } \left( \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } f ( s ) e ^ { - i \lambda s } d s \right) \left( \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } g ( x ) e ^ { - i \lambda x } d x \right) ,
$$

which is ${ \sqrt { 2 \pi } } { \widehat { f } } ( \lambda ) { \widehat { g } } ( \lambda )$ , as desired.

Equation (2.10) follows from equation (2.9) and the inverse formula for the Fourier transform as follows:

$$
\begin{array} { r } { \sqrt { 2 \pi } \mathcal { F } ^ { - 1 } [ \widehat { f } \widehat { g } ] = \mathcal { F } ^ { - 1 } [ \mathcal { F } ( f \ast g ) ] \qquad \mathrm { f r o m ~ } ( 2 . 9 ) } \\ { = f \ast g \qquad \mathrm { f r o m ~ T h e o r e m ~ } 2 . 1 . } \end{array}
$$

This completes the proof of the theorem.

# 2.2.3 Adjoint of the Fourier Transform

Recall from Section O.6.2 that the adjoint of a linear operator $T : V \mapsto W$ between two inner product spaces is an operator $T ^ { * } : W \mapsto V$ such that

$$
\langle v , T ^ { * } ( w ) \rangle _ { V } = \langle T ( v ) , w \rangle _ { W } .
$$

In the next theorem, we show that the adjoint of the Fourier transform is the inverse of the Fourier transform.

THEOREM 2.11 Suppose $\pmb { f }$ and $\pmb { \mathscr { g } }$ are square integrable. Then

$$
\langle { \mathcal { F } } [ f ] , g \rangle _ { L ^ { 2 } } = \langle f , { \mathcal { F } } ^ { - 1 } [ g ] \rangle _ { L ^ { 2 } } .
$$

Proof We have

$$
\begin{array} { l } { { \displaystyle \langle \mathcal F [ f ] , g \rangle _ { L ^ { 2 } } = \int _ { - \infty } ^ { \infty } \widehat f ( \lambda ) \overline { { { g ( \lambda ) } } } d \lambda } } \\ { { \displaystyle \qquad = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i \lambda t } d t \overline { { { g ( \lambda ) } } } d \lambda \quad \mathrm { b y ~ d e f i n i t i o n ~ o f ~ } \widehat f } } \\ { { \displaystyle \qquad = \int _ { - \infty } ^ { \infty } f ( t ) \left( \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \left( \overline { { { g ( \lambda ) e ^ { i \lambda t } } } } d \lambda \right) d \lambda \right) d t } } \end{array} \quad .
$$

(by switching the order of integration). The second integral (involving $\pmb { \mathscr { s } }$ is $\frac { 2 } { \mathcal { F } ^ { - 1 } [ g ] ( t ) }$ therefore,

$$
\langle { \mathcal { F } } [ f ] , g \rangle _ { L ^ { 2 } } = \int _ { - \infty } ^ { \infty } f ( t ) { \overline { { { \mathcal { F } } ^ { - 1 } [ g ] ( t ) } } } d t = \langle f , { \mathcal { F } } ^ { - 1 } [ g ] \rangle _ { L ^ { 2 } }
$$

as desired.

# 2.2.4 Plancherel Formula

The Plancherel formula states that the Fourier transform preserves the $L ^ { 2 }$ inner product.

THEOREM 2.12 Suppose $\pmb { f }$ and $\pmb { \mathscr { s } }$ are square integrable. Then

$$
\begin{array} { r } { \langle \mathcal { F } [ f ] , \mathcal { F } [ g ] \rangle _ { L ^ { 2 } } = \langle f , g \rangle _ { L ^ { 2 } } } \\ { \langle \mathcal { F } ^ { - 1 } [ f ] , \mathcal { F } ^ { - 1 } [ g ] \rangle _ { L ^ { 2 } } = \langle f , g \rangle _ { L ^ { 2 } } . } \end{array}
$$

In particular,

$$
\| { \mathcal { F } } [ f ] \| _ { L ^ { 2 } } = \| f \| _ { L ^ { 2 } } .
$$

Proof Equation (2.11) follows from Theorems 2.11 and 2.1 as follows:

$$
\begin{array} { r l } & { \langle \mathcal { F } [ f ] , \mathcal { F } [ g ] \rangle _ { L ^ { 2 } } = \langle f , \mathcal { F } ^ { - 1 } \mathcal { F } [ g ] \rangle _ { L ^ { 2 } } \qquad \mathrm { ( T h e o r e m ~ 2 . 1 1 ) } } \\ & { \qquad = \langle f , g \rangle _ { L ^ { 2 } } \qquad \mathrm { ( T h e o r e m ~ 2 . 1 ) } } \end{array}
$$

as desired. Equation (2.12) can be established in a similar manner. Equation (2.13) follows from (2.11) with $\pmb { f } = \pmb { g }$ $\bullet$

Remark. The equation $\| { \mathcal { F } } ( f ) \| = \| f \|$ is analogous to equation (1.38) in Theorem 1.40 and is also referred to as Parseval's equation. This equation has the following interpretations. For a function, $\pmb { f }$ ,defined on $\scriptstyle { \left[ - \pi , \pi \right] }$ ,let $\mathcal { F } ( f ) ( n )$ . be its nth Fourier coefficient (except with the factor $1 / { \sqrt { 2 \pi } }$ instead of $1 / 2 \pi$ :

$$
{ \mathcal { F } } ( f ) ( n ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \pi } ^ { \pi } f ( t ) e ^ { - i n t } d t .
$$

Equation (1.38) can be restated as

$$
\| \mathcal { F } ( f ) \| _ { l ^ { 2 } } ^ { 2 } = \| f \| _ { L ^ { 2 } [ - \pi , \pi ] } ^ { 2 }
$$

which is analogous to (2.13) for the Fourier transform with $\imath ^ { 2 }$ and $L ^ { 2 } [ - \pi , \pi ]$ replaced by the $L ^ { 2 }$ norm on the entire real line. As in the case with Fourier series, Plancherel's formula states that the energy of a signal in the time domain, $\| f \| _ { L ^ { 2 } } ^ { 2 }$ , is the same as the energy in the frequency domain $\| \widehat { f } \| _ { L ^ { 2 } } ^ { 2 }$ .

# 2.3 Linear Filters

# 2.3.1 Time Invariant Filters

The Fourier transform plays a central role in the design of filters. A filter can be thought of as a "black box" that takes an input signal, processes it, and then returns an output signal that in some way modifies the input. One example of a filter is a device that removes noise from a signal.

From a mathematical point of view, a signal is a function $\scriptstyle f : R \mapsto C$ that is usually piecewise continuous. A filter is a transformation $\pmb { L }$ that maps a signal, $\pmb { f } ,$ ,into another signal $\tilde { \pmb f }$ This transformation must satisfy the following two properties in order to be a linear filter :

Additivity: $L \{ f + g \} = L [ f ] + L [ g ]$ Homogeneity: $L [ c f ] = c L [ f ]$ , where $\pmb { c }$ is a constant

There is another property common to most filters. If we play an old, scratchy record starting at 3 p.M. today and put the signal through a noise-reducing filter, we will hear the cleaned-up output, at roughly the same time as we play the record. If we play the same record at $\bf { 1 0 A . M }$ . tomorrow morning, and use the same filter, we should hear the identical output, again at roughly the same time. This property is called time invariance. To formulate this concept, we introduce the following notation: For a function $f ( t )$ and a real number $\pmb { a }$ , let $f _ { a } ( t ) = f ( t - a )$ .Thus $\pmb { f _ { a } }$ is a time shift, by $\pmb { a }$ units, of the signal $\pmb { f }$ .

DefInition 2.13 A transformation $\pmb { L }$ (mapping signals to signals) is said to be time invariant if for any signal $\pmb { f }$ and any real number $\pmb { a }$ , $L [ f _ { a } ] ( t ) = ( L f ) ( t - a )$ for all t (or $L [ f _ { a } ] = ( L f ) _ { a } )$ . In words, $\pmb { L }$ is time invariant if the time-shifted input signal $f ( t - a )$ is transformed by $\pmb { L }$ into the time-shifted output signal $( L f ) ( t - a )$ . (See Figure 11.)

![](images/ded2bcbec4da9b7b32d019f046e515b97993da7ec1d47c3da60a39580d5a42b2.jpg)  
Figure 11 L is time invariant if the upper and lower outputs are the same

# EXaMple 2.14

Let $ { \boldsymbol { l } } ( t )$ be a function that has finite support [i.e., $ { \boldsymbol { l } } ( t )$ is zero outside of a finite $\pmb { t }$ -interval]. For a signal $\pmb { f }$ , let

$$
( L f ) ( t ) = ( l * f ) ( t ) = \int _ { - \infty } ^ { \infty } l ( t - x ) f ( x ) d x \quad { \mathrm { f o r ~ e a c h ~ } } t .
$$

This linear operator is time invariant because for any ${ \pmb a } \in \pmb R$

$$
\begin{array} { l } { { ( L f ) ( t - a ) = \displaystyle \int _ { - \infty } ^ { \infty } l ( t - a - x ) f ( x ) d x } } \\ { { } } \\ { { = \displaystyle \int _ { - \infty } ^ { \infty } l ( t - y ) f ( y - a ) d y ~ \mathrm { ( b y ~ l e t t i n g ~ } y = a + x ) } } \\ { { } } \\ { { = \displaystyle \int _ { - \infty } ^ { \infty } l ( t - y ) f _ { a } ( y ) d y } } \\ { { } } \\ { { = L [ f _ { a } ] ( t ) . } } \end{array}
$$

Thus, $( L f ) ( t - a ) = L [ f _ { a } ] ( t )$ and so $\pmb { L }$ is time invariant.

Not every linear transformation has this property, as the following example shows.

$$
( L f ) ( t ) = \int _ { 0 } ^ { t } f ( \tau ) d \tau .
$$

Let

On one hand, we have

$$
\begin{array} { l } { { \displaystyle { \cal L } [ f _ { a } ] ( t ) ) = \int _ { 0 } ^ { t } f ( \tau - a ) d \tau } } \\ { { \displaystyle ~ = \int _ { - a } ^ { t - a } f ( \hat { \tau } ) d \hat { \tau } ~ \ b y ~ \mathrm { l e t t i n g } ~ \hat { \tau } = \tau - a . } } \end{array}
$$

On the other hand,

$$
( L f ) ( t - a ) = \int _ { 0 } ^ { t - a } f ( \tau ) d \tau .
$$

Since ${ \cal L } [ f _ { \alpha } ] ( t )$ and $( L f ) ( t - a )$ are not the same (for ${ \pmb a } \neq { \pmb 0 }$ , $\pmb { L }$ is not time invariant.

The next lemma and theorem show that the convolution in Example 2.14 is typical of time invariant linear filters. We start by computing $L ( e ^ { i \lambda t } )$ .

LEMMA 2.16 Let $\pmb { L }$ be a linear, time-invariant transformation and let $\lambda$ be any fixed real number. Then there is a function $^ h$ with

$$
L ( e ^ { i \lambda t } ) = { \sqrt { 2 \pi } } { \hat { h } } ( \lambda ) e ^ { i \lambda t } \qquad ( t { \ i s \ t h e \ v a r i a b l e } ) .
$$

Remark. Note that the input signal $e ^ { i \lambda t }$ is a (complex-valued) sinusoidal signal with frequency $\lambda$ This lemma states that the output signal from a time invariant filter of a sinusoidal input signal is also sinusoidal with the same frequency.

Proof Our proof is somewhat informal in order to explain clearly the essential idea. Let $h ^ { \lambda } ( t ) = L ( e ^ { i \lambda t } )$ Since $\pmb { L }$ is time invariant, we have

$$
L [ e ^ { i \lambda ( t - a ) } ] = h ^ { \lambda } ( t - a )
$$

for each real number $\pmb { a }$ Since $\pmb { L }$ is linear, we also have

$$
\begin{array} { r l } { L [ e ^ { i \lambda ( t - a ) } ] = L [ e ^ { - i \lambda a } e ^ { i \lambda t } ] } & { } \\ { = e ^ { - i \lambda a } L [ e ^ { i \lambda t } ] } & { ( L \mathrm { ~ i s ~ l i n e a r } ) . } \end{array}
$$

Thus

$$
{ \cal L } [ e ^ { i \lambda ( t - a ) } ] = e ^ { - i \lambda a } h ^ { \lambda } ( t ) .
$$

Comparing (2.14) and (2.15), we find

$$
h ^ { \lambda } ( t - a ) = e ^ { - i \lambda a } h ^ { \lambda } ( t ) .
$$

Since $\pmb { a }$ is arbitrary, we may set ${ \pmb a } = { \pmb t }$ , yielding $h ^ { \lambda } ( 0 ) = e ^ { - i \lambda t } h ^ { \lambda } ( t ) ;$ solving for $h ^ { \lambda } ( t )$ , we obtain

$$
L [ e ^ { i \lambda t } ] = h ^ { \lambda } ( t ) = h ^ { \lambda } ( 0 ) e ^ { i \lambda t } .
$$

Letting $\hat { h } ( \lambda ) = h ^ { \lambda } ( 0 ) / \sqrt { 2 \pi }$ completes the proof.

The function $\hat { h } ( \lambda )$ determines $\pmb { L }$ To see this we first use the Fourir inversion theorem (Theorem 2.1):

$$
f ( t ) = \mathcal { F } ^ { - 1 } [ \hat { f } ] = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \hat { f } ( \lambda ) e ^ { i \lambda t } d \lambda .
$$

Then we apply $\pmb { L }$ to both sides:

$$
( L f ) ( t ) = L \left[ \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \hat { f } ( \lambda ) e ^ { i \lambda t } d \lambda \right] .
$$

The integral on the right can be approximated by a Riemann sum:

$$
{ \cal L } \left[ \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \hat { f } ( \lambda ) e ^ { i \lambda t } d \lambda \right] \approx { \cal L } \left[ \frac { 1 } { \sqrt { 2 \pi } } \sum _ { j } \hat { f } ( \lambda _ { j } ) e ^ { i \lambda _ { j } t } \Delta \lambda \right] .
$$

Since $\pmb { L }$ is linear, we can distribute $\pmb { L }$ across the sum:

$$
L \left[ { \frac { 1 } { \sqrt { 2 \pi } } } \sum _ { j } { \hat { f } } ( \lambda _ { j } ) e ^ { i \lambda _ { j } t } \Delta \lambda \right] = { \frac { 1 } { \sqrt { 2 \pi } } } \sum _ { j } { \hat { f } } ( \lambda _ { j } ) L \left[ e ^ { i \lambda _ { j } t } \right] \Delta \lambda .
$$

As the partition gets finer, the Riemann sum on the right becomes an integral, and so from (2.16), (2.17), and (2.18), we obtain

$$
\begin{array} { l l } { { ( L f ) ( t ) = \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \hat { f } ( \lambda ) L [ e ^ { \mathrm { i } \lambda t } ] ( t ) d \lambda ~ } } \\ { { { } } } \\ { { = \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \hat { f } ( \lambda ) \left( \sqrt { 2 \pi } \hat { h } ( \lambda ) \right) e ^ { \mathrm { i } \lambda t } d \lambda ~ \mathrm { b y ~ L e m m a 2 . 1 6 } } } \\ { { { } } } \\ { { { } = \sqrt { 2 \pi } \mathcal { F } ^ { - 1 } [ \hat { f } ( \lambda ) \hat { h } ( \lambda ) ] ( t ) ~ \mathrm { b y ~ d e f i n i t i o n ~ o f ~ i n v e r s e ~ F o u r i e r ~ t r a n s f o r r } } } \\ { { { } } } \\ { { { } = \displaystyle ( f * h ) ( t ) ~ \mathrm { b y ~ T h e o r e m ~ 2 . 1 0 } . } } \end{array}
$$

Even though the preceding argument is not totally rigorous, the result is true with very few restrictions on either $\pmb { L }$ or the space of signals being considered (see the text on Fourier analysis by Stein and Weiss [19] for more details). We summarize this discussion in the following theorem.

THEOREM 2.17 Let $\pmb { L }$ be a linear, time invariant transformation on the space of signals that are piecewise continuous functions. Then there exists an integrable function, h, such that

$$
L ( f ) = f * h
$$

for all signals $\pmb { f }$

Physical Interpretation. Both $h ( t )$ and $\hat { h } ( \lambda )$ have physical interpretations. Assume that $h ( t )$ is continuous and that $\delta$ is a small positive number. We apply $\pmb { L }$ to the following impulse signal:

$$
f _ { \delta } ( t ) = { \left\{ \begin{array} { l l } { 1 / ( 2 \delta ) } & { { \mathrm { i f ~ } } - \delta \leq t \leq \delta } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

whose graph is given in Figure 12. If $\delta > 0$ is small, then $f _ { \delta }$ represents a signal that is very strong but only lasts a short period of time (such as the sound signal generated by a hammer blow). Note that $\textstyle \int _ { - \delta } ^ { \delta } f _ { \delta } ( t ) d t = 1$ Applying $\pmb { L }$ to $f _ { \delta }$ ,we obtain

$$
\begin{array} { r l } { ( L f _ { \delta } ) ( t ) = f _ { \delta } * h ( t ) } \\ { \displaystyle } \\ { \displaystyle } \\ { \qquad = \int _ { - \infty } ^ { \infty } f _ { \delta } ( \tau ) h ( t - \tau ) d \tau } \\ { \displaystyle } \\ { \displaystyle } \\ { \qquad = \int _ { - \delta } ^ { \delta } f _ { \delta } ( \tau ) h ( t - \tau ) d \tau } & { \mathrm { ( s i n c e ~ } f _ { \delta } ( \tau ) = 0 \mathrm { ~ f o r ~ } | \tau | \geq \delta ) } \end{array}
$$

![](images/756d75f45a9293f3a49d741b82bffb4cf69548728402ca84f1f59cb28037f2ce.jpg)  
Figure 12 Graph of $f _ { \delta }$

Since $\pmb { h }$ is continuous, $h ( t - \tau )$ is approximately equal to $h ( t )$ for $| \tau | \leq \delta$ . Therefore,

$$
( L f _ { \delta } ) ( t ) \approx h ( t ) \underbrace { \int _ { - \delta } ^ { \delta } f _ { \delta } ( \tau ) d \tau } _ { 1 } = h ( t ) .
$$

Thus $h ( t )$ is the approximate response from applying $\pmb { L }$ to an input signal that is an impulse. For that reason $h ( t )$ is called the impulse response function.

We have already seen that $L [ e ^ { i \lambda t } ] = { \sqrt { 2 \pi } } { \hat { h } } ( \lambda ) e ^ { i \lambda t }$ .Thus up to a constant factor, $\hat { h } ( \lambda )$ is the amplitude of the response to a "pure frequency" signal $e ^ { i \lambda t }$ ; $\hat { h }$ is called the system function.

# 2.3.2 Causality and the Design of Filters

Designing a time invariant filter is equivalent to constructing the impulse function, $\scriptstyle h$ , since any such filter can be written as

$$
L f = f * h
$$

by Theorem 2.17. The construction of $\pmb { h }$ depends on what the filter is designed to do. In this section, we consider filters that reduce high frequencies. Such filters are called low-pass filters.

Taking the Fourier transform of both sides of $L f = f * h$ and using Theorem 2.10 yields

$$
\widehat { L [ f ] } ( \lambda ) = \sqrt { 2 \pi } \widehat { f } ( \lambda ) \widehat { h } ( \lambda ) .
$$

A Faulty Filter. Suppose we wish to remove all frequency components from the signal $\pmb { f }$ that lie beyond some cutoff frequency $\lambda _ { c }$ As a natural first attempt, we choose an $\pmb { h }$ whose Fourier transform is zero outside of the interval $- \lambda _ { c } \leq \lambda \leq \lambda _ { c }$ :

$$
\hat { h } _ { \lambda _ { c } } ( \lambda ) : = \left\{ \begin{array} { l l } { 1 / \sqrt { 2 \pi } } & { \mathrm { i f } \ | \lambda | \leq \lambda _ { c } } \\ { 0 } & { \mathrm { i f } \ | \lambda | > \lambda _ { c } } \end{array} \right.
$$

(the choice of constant $1 / { \sqrt { 2 \pi } }$ is for convenience in later calculations). Since ${ \widehat { L f ( \lambda ) } } = { \sqrt { 2 \pi } } { \widehat { f ( \lambda ) } } { \widehat { h ( \lambda ) } }$ is zero for $\vert \lambda \vert > \lambda _ { c }$ , this filter appears to remove the unwanted frequencies (above $\lambda _ { c . }$ from the signal $\pmb { f }$ However, we will see that this filter is flawed in other respects.

The impulse response function corresponding to the system function $\hat { h } _ { \lambda _ { c } }$ is easy to calculate:

$$
\begin{array} { l } { { \displaystyle h _ { \lambda _ { \star } } ( t ) = { \mathcal F } ^ { - 1 } [ \hat { h } _ { \boldsymbol { \lambda } _ { \star } } ] \quad \mathrm { ( b y ~ T h e o r e m ~ 2 . 1 ) } } } \\ { { \displaystyle \quad = \boldsymbol { \left( 1 / \sqrt { 2 \pi } \right) } \int _ { - \infty } ^ { \infty } \hat { h } _ { \boldsymbol { \lambda } _ { \star } } ( \lambda ) e ^ { i \boldsymbol { \lambda } t } d \boldsymbol { \lambda } } } \\ { { \displaystyle \quad = \frac { 1 } { 2 \pi } \int _ { - \lambda _ { \star } } ^ { \lambda _ { \star } } e ^ { i \lambda t } d \boldsymbol { \lambda } \quad \mathrm { f r o m ~ } ( 2 . 1 9 ) } } \\ { { \displaystyle \quad = \left[ \frac { e ^ { i \boldsymbol { \lambda } t } } { 2 i \pi } \right] _ { \lambda = - \lambda _ { \star } } ^ { \lambda \lambda _ { \star } } } } \\ { { \displaystyle \quad = \frac { e ^ { i \lambda _ { \star } t } - e ^ { - i \lambda _ { \star } t } } { 2 i \pi } } . } \end{array}
$$

Therefore,

$$
h _ { \lambda _ { c } } ( t ) = \frac { \sin ( \lambda _ { c } t ) } { \pi t } .
$$

Now we filter the following simple input function:

$$
f _ { t _ { c } } ( t ) : = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } 0 \leq t \leq t _ { c } } \\ { 0 } & { { \mathrm { i f ~ } } t < 0 { \mathrm { ~ o r ~ } } t > t _ { c } . } \end{array} \right. }
$$

Think of $\mathbf { \widehat { f } } _ { t _ { c } }$ as a signal that is on for $\pmb { t }$ between 0 and $\scriptstyle t _ { c }$ and off at other times. The effect of this filter on the signal $\scriptstyle f _ { t _ { c } }$ is

$$
\begin{array} { r l } { ( L f _ { t _ { c } } ) ( t ) = ( f _ { t _ { c } } * h _ { \lambda _ { c } } ) ( t ) } \\ { = \int _ { - \infty } ^ { \infty } f _ { t _ { c } } ( \tau ) h _ { \lambda _ { c } } ( t - \tau ) d \tau } \\ { ~ } \\ & { = \int _ { 0 } ^ { t _ { c } } \frac { \sin \left( \lambda _ { c } ( t - \tau ) \right) } { \pi ( t - \tau ) } d \tau ~ \mathrm { [ f r o m ~ ( 2 . 2 0 ) ] } } \\ { ~ } \\ & { = \frac { 1 } { \pi } \int _ { \lambda _ { c } ( t - t _ { c } ) } ^ { \lambda _ { c } t } \frac { \sin ~ u } { u } d u ~ \mathrm { [ w i t h ~ } u = \lambda _ { c } ( t - \tau ) ] } \\ { ~ } \\ & { = \frac { 1 } { \pi } \left\{ \mathrm { S i } ( \lambda _ { c } t ) - \mathrm { S i } ( \lambda _ { c } ( t - t _ { c } ) ) \right\} } \end{array}
$$

where $\begin{array} { r } { \mathbf { S i } ( z ) = \int _ { 0 } ^ { z } \frac { \sin u } { u } d u } \end{array}$ A plot of $\begin{array} { r } { ( L _ { \lambda _ { c } } f _ { t _ { c } } ) ( t ) = \frac { 1 } { \pi } \left\{ \mathrm { S i } ( \lambda _ { c } t ) - \mathrm { S i } ( \lambda _ { c } ( t - t _ { c } ) ) \right\} } \end{array}$ with $\scriptstyle t _ { c }$ and $\lambda _ { c }$ both 1 is given in Figure 13. Note that the graph of the output signal is nonzero for $\smash { \pmb { t } < \mathbb { 0 } }$ whereas the input signal, ${ f } _ { t _ { c } } ( t )$ , is zero for $t < 0$ . This indicates that the output signal occurs before the input signal has arrived!

Clearly, a filter cannot be physically constructed to produce an output signal before receiving an input signal. Thus, our first attempt at constructing a filter by using the function $h _ { \lambda _ { c } }$ is not practical. The following definition and theorem characterize a more realistic class of filters.

![](images/46bd69d701e599a5484541a101ff459e7b712d7ac94c29d604b38a5acd888c1e.jpg)  
Figure 13 Graph of $\scriptstyle { \frac { 1 } { \pi } } \left\{ \mathbf { S i } ( t ) - \mathbf { S i } ( t - 1 ) \right\}$

Causal Filters

DefinItioN 2.18 A causal filter is one for which the output signal begins after the input signal has started to arrive.

The following result tells us which filters are causal.

TheoreM 2.19 Let L be a time invariant filter with response function h (i.e., $L f = f * h )$ . $\pmb { L }$ is a causal filter if and only if $h ( t ) = 0$ for all ${ \pmb t } < { \bf 0 }$ .

Proof We prove that if $h ( t ) = 0$ for all $\pmb { t } < \mathbf { 0 }$ , then the corresponding filter is causal. We leave the converse as an exercise (see Exercise 8). We first show that if $\pmb { f } ( t ) = \pmb { 0 }$ for $\pmb { t } < \mathbf { 0 }$ ,then $( L f ) ( t ) = 0$ for $\pmb { t } < \mathbf { 0 }$ We have

$$
( L f ) ( t ) = ( f * h ) ( t ) = \int _ { 0 } ^ { \infty } f ( \tau ) h ( t - \tau ) d \tau ,
$$

where the lower limit in the integral is 0 because $f ( \tau ) = 0$ when $\tau < 0$ If ${ \pmb t } < { \bf 0 }$ and ${ \boldsymbol { \tau } } \geq \mathbf { 0 }$ , then $t - \tau < 0$ and so $h ( t - \tau ) = 0$ ,by hypothesis. Therefore, $( L f ) ( t ) = 0$ for $\mathbf { \delta t } < \mathbf { 0 }$ We have therefore shown that if $\pmb { f } ( t ) = \mathbf { 0 }$ for $\pm < 0$ then $( L f ) ( t ) = 0$ for ${ \pmb t } < { \bf 0 }$ In other words, if the input signal does not arrive until $\pmb { t = 0 }$ , the output of the filter also does not begin until $\pmb { t = 0 }$ .

Suppose, more generally, that the input signal $\pmb { f }$ does not arrive until $\pmb { t } = \pmb { a }$ . To show that $\pmb { L }$ is causal, we must show that $\pmb { L f }$ does not begin until $\pmb { t } = \pmb { a }$ . Let $g ( t ) = f ( t + a )$ Note that the signal $\pmb { g } ( t )$ begins at $\pmb { t = 0 }$ From the previous paragraph, $( { \pmb { L } } { \pmb { g } } ) ( { \pmb { t } } )$ does not begin until ${ \pmb t = 0 }$ Since $f ( t ) = g ( t - a ) = g _ { a } ( t )$ ,we have

$$
\begin{array} { r l } { ( L f ) ( t ) = ( L g _ { a } ) ( t ) } & { } \\ { = ( L g ) ( t - a ) } & { \mathrm { b y ~ t h e ~ t i m e ~ i n v a r i a n c e ~ o f ~ } L . } \end{array}
$$

Since $( L g ) ( \tau )$ does not begin until ${ \boldsymbol { \tau } } = \mathbf { 0 }$ , we see that $( L g ) ( t - a )$ does not begin until $\pmb { t = a }$ Thus $( L f ) ( t ) = ( L g ) ( t - a )$ does not begin until $\pmb { t = a }$ ,as desired. $\bullet$

Theorem 2.19 applies to the response function, but it also gives us important information about the system function, $\hat { h } ( \lambda )$ .By the definition of the Fourier transform,

$$
\hat { h } ( \lambda ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } h ( t ) e ^ { - i \lambda t } d t .
$$

If the filter associated to $\pmb { h }$ is causal, Theorem 2.19 implies $h ( t ) = 0$ for ${ \pmb t } < { \bf 0 }$ and so

$$
\begin{array}{c} \begin{array} { l } { { \displaystyle \hat { h } ( \lambda ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { 0 } ^ { \infty } h ( t ) e ^ { - i \lambda t } d t } } \\ { { \displaystyle ~ = \angle [ h ( t ) / \sqrt { 2 \pi } ] ( i \lambda ) ~ } } \end{array} \mathrm { ( w h e r e ~ } { \cal { L } } \mathrm { = L a p l a c e ~ t r a n s f o r m ) } .  \end{array}
$$

We summarize this discussion in the following theorem.

THeOREM 2.20 Suppose $\pmb { L }$ is a causal filter with response function h. Then the system function associated with $\pmb { L }$ is

$$
{ \widehat { h } } ( \lambda ) = { \frac { { \mathcal { L } } [ h ] ( i \lambda ) } { \sqrt { 2 \pi } } }
$$

where $\pmb { \mathscr { L } }$ is the Laplace transform.

# EXaMPle 2.21

One of the older causal, noise-reducing filters is the Butterworth filter [14]. It is constructed using the previous theorem with

$$
h ( t ) = { \left\{ \begin{array} { l l } { A e ^ { - \alpha t } } & { { \mathrm { i f ~ } } t \geq 0 } \\ { 0 } & { { \mathrm { i f ~ } } t < 0 } \end{array} \right. }
$$

where $\pmb { A }$ and $\pmb { \alpha }$ are parameters. Its Fourier transform is given by

$$
\hat { h } ( \lambda ) = \frac { 1 } { \sqrt { 2 \pi } } ( \mathcal { L } h ) ( i \lambda ) = \frac { A } { \sqrt { 2 \pi } ( \alpha + i \lambda ) }
$$

(see Exercise 10). Note that $\hat { h } ( \lambda )$ decays as $\lambda \mapsto \infty$ , thus diminishing the high-frequency components of the filtered signal $( { \widehat { L f } } ) ( \lambda ) = { \hat { h } } ( \lambda ) { \hat { f } } ( \lambda )$ .

![](images/de661147128cf415bce65660175f2128baaaad5c5c010c3f9c2ff295f1739eb7.jpg)  
Figure 14 Graph of $e ^ { - t / 3 }$ (sin 2 +2sin 4t +0.4sin 2t sin 40)

Consider the signal given by

$$
f ( t ) = e ^ { - t / 3 } \left( \sin 2 t + 2 \sin 4 t + 0 . 4 \sin 2 t \sin 4 0 t \right) \quad 0 \leq t \leq \pi
$$

whose graph is given in Figure 14. We wish to filter the noise that vibrates with frequency approximately 40. At the same time, we do not want to disturb the basic shape of this signal, which vibrates in the frequency range of 2 to 4. By choosing $A = \alpha = 1 0$ $\widehat { h } ( \lambda )$ is close to $\widehat { h } ( 0 ) = 1 / \sqrt { 2 \pi }$ for $| \lambda | \leq 4 ;$ but $| \widehat { h } ( \lambda ) |$ . is small (less than 0.1) when $\lambda \geq 4 0$ Thus filtering by $\pmb { h }$ with this choice of parameters $\pmb { A }$ and $\pmb { \alpha }$ should preserve the low frequencies (frequency $\leq 4$ while damping the high frequencies $( \geq 4 0 )$ A plot of the filtered signal $( f * h ) ( t )$ . for $0 \leq t \leq \pi$ is given in Figure 15. Most of the high-frequency noise has been filtered. Most of the low-frequency components of this signal have been preserved.

# 2.4 The Sampling Theorem

In this section, we examine a class of signals (i.e., functions) whose Fourier transform is zero outside a finite interval $[ - \Omega , \Omega ] ;$ these are (frequency) band-limited functions. For instance, the human ear can only hear sounds with frequencies less than $\bf { 2 0 } ~ \bf { k H z }$ $\mathbf { 1 \ k H z } = \mathbf { 1 0 0 0 }$ cycles per second). Thus, even though we make sounds with higher frequencies, anything above $\bf { 2 0 ~ k H z }$ can't be heard. Telephone conversations are thus effectively band-limited signals. We will show below that a band-limited signal can be reconstructed from its values (or samples) at regularly spaced times. This result is basic in continuous-to-digital signal processing.

![](images/e97b796e05d70eb14a6e991de786582b35a8387565258c369ee4096df47c5c6c.jpg)  
Figure 15 Graph of the filtered signal from Figure 14

Definition 2.22 A function $\pmb { f }$ is said to be frequency band-limited if there exists a constant $\Omega > 0$ such that

$$
{ \hat { f } } ( \lambda ) = 0 \quad { \mathrm { f o r ~ } } | \lambda | > \Omega .
$$

When $\mathbf { \sigma } _ { \Omega }$ is the smallest frequency for which the preceding equation is true, the natural frequency $\textstyle \nu : = { \frac { \Omega } { 2 \pi } }$ $\begin{array} { r } { 2 \nu = \frac { \Omega } { \pi } } \end{array}$ is the Nyquist rate.

THEOREM 2.23 (Shannon-Whittaker Sampling Theorem) Suppose that $\hat { f } ( \lambda )$ is piecewise smooth, continuous, and that ${ \widehat { f } } ( \lambda ) = 0$ for $\left. \lambda \right. > \Omega$ ,where $\pmb { \Omega }$ . is some fixed, positive frequency. Then $\pmb { f } = \pmb { \mathcal { F } } ^ { - 1 } [ \hat { \pmb { f } } ]$ is completely determined by its values at the points $\mathbf { \Delta } t _ { j } = j \pi / \Omega$ , $j = 0 , \pm 1 , \pm 2 , \ldots$ More precisely, $\pmb { f }$ has the following series expansion:

$$
f ( t ) = \sum _ { j = - \infty } ^ { \infty } f ( j \pi / \Omega ) \frac { \sin ( \Omega t - j \pi ) } { \Omega t - j \pi }
$$

where the series on the right converges uniformly.

This is a remarkable theorem! Let's look at how we might use it to transmit several phone conversations simultaneously on a single wire (or channel). The maximum possible (natural) frequency that we can hear is about $\bf { 2 0 ~ k H z }$ , so a phone conversation is effectively a band-limited signal. In fact, the dominant frequencies in most phone conversations are below $\mathbf { 1 } \ \mathbf { k H z }$ which we will take as our Nyquist frequency. The Nyquist rate $\begin{array} { r } { \nu = \frac { \Omega } { \pi } } \end{array}$ is then double this, or 2 $\mathbf { k H z }$ ;so we need to sample the signal every $\scriptstyle { \frac { 1 } { 2 } }$ millisecond. How many phone conversations can we send in this manner? Transmission lines typically send about 56 thousand bits of information per second. If each sample of information can be represented by 7 bits, then we can transmit 8 thousand samples per second, or 8 every millisecond, or 4 every half-millisecond. By tagging and interlacing signals, we can transmit the samples from four conversations. At the receiving end, we can use the series in equation (2.21) to reconstruct the signal, with the samples being $f ( \textstyle { \frac { 1 } { 2 } } j )$ for $\dot { \pmb { \mathscr { I } } }$ an integer and time in milliseconds (only a finite number of these occur during the life of a phone conversation— unless perhaps a teenager is on the line). Here is the proof of the theorem.

Proof Using Theorem 1.20 (with ${ \pmb a } = { \pmb \Omega }$ and $t = \lambda$ ), we expand $\hat { f } ( \lambda )$ in a Fourier series on the interval $[ - \Omega , \Omega ]$ :

$$
\hat { f } ( \lambda ) = \sum _ { k = - \infty } ^ { \infty } c _ { k } e ^ { i \pi k \lambda / \Omega } , \quad c _ { k } = \frac { 1 } { 2 \Omega } \int _ { - \Omega } ^ { \Omega } \hat { f } ( \lambda ) e ^ { - i \pi k \lambda / \Omega } d \lambda .
$$

Since ${ \hat { f } } ( \lambda ) = 0$ for $| \lambda | \geq \Omega$ ,the limits in theintegrals defg $\pmb { c } _ { \pmb { k } }$ can be changed to-∞...∞:

$$
c _ { k } = \frac { \sqrt { 2 \pi } } { 2 \Omega } \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \hat { f } ( \lambda ) e ^ { - i \pi k \lambda / \Omega } d \lambda .
$$

By Theorem 2.1,

$$
c _ { k } = \frac { \sqrt { 2 \pi } } { 2 \Omega } f ( - k \pi / \Omega ) .
$$

If we use this expression for $\pmb { c _ { k } }$ in the preceding series, and if at the same time we change the summation index from $\pmb { k }$ to $\begin{array} { r } { \dot { \boldsymbol { \jmath } } = - \boldsymbol { k } , } \end{array}$ we obtain

$$
\hat { f } ( \lambda ) = \sum _ { j = - \infty } ^ { \infty } \frac { \sqrt { 2 \pi } } { 2 \Omega } f ( j \pi / \Omega ) e ^ { - i \pi j \lambda / \Omega } .
$$

Since $\hat { \pmb f }$ is a continuous, piecewise smooth function, the series (2.22) converges uniformly by Theorem 1.30. Using Theorem 2.1,

$$
\begin{array} { l } { f ( t ) = \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \hat { f } ( \lambda ) e ^ { i \lambda t } d \lambda } \\ { \displaystyle = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \Omega } ^ { \Omega } \hat { f } ( \lambda ) e ^ { i \lambda t } d \lambda \quad \mathrm { s i n c e } ~ \hat { f } ( \lambda ) = 0 , \vert \lambda \vert \geq \Omega . } \end{array}
$$

Using (2.22) for $\widehat { \pmb f }$ and interchanging the order of integration and summation, we obtain

$$
f ( t ) = \sum _ { j = - \infty } ^ { \infty } \frac { \sqrt { 2 \pi } } { 2 \Omega } f ( j \pi / \Omega ) \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \Omega } ^ { \Omega } e ^ { - i \pi j \lambda / \Omega + i \lambda t } d \lambda .
$$

The integral in (2.23) is

$$
\int _ { - \Omega } ^ { \Omega } e ^ { - i \pi j \lambda / \Omega + i \lambda t } d \lambda = 2 { \frac { \Omega \sin ( t \Omega - j \pi ) } { t \Omega - j \pi } } .
$$

After simplifying (2.23), we obtain (2.21), which completes the proof.

The convergence rate in (2.21) is rather slow since the coefficients (in absolute value) decay like $1 / j$ The convergence rate can be increased so that the terms behave like $1 / j ^ { 2 }$ or better, by a technique called oversampling, which is discussed in Exercise 14. At the opposite extreme, if a signal is sampled below the Nyquist rate, then the signal reconstructed via equation (2.21) will not only be missing high frequency components, but it will also have the energy in those components transferred to low frequencies that may not have been in the signal at all. This is a phenomenon called aliasing.

# EXaMPLe 2.24

Consider the function $\pmb { f }$ defined by

$$
{ \widehat { f } } ( \lambda ) : = { \left\{ \begin{array} { l l } { { \sqrt { 2 \pi } } ( 1 - \lambda ^ { 2 } ) } & { { \mathrm { i f ~ } } | \lambda | \leq 1 } \\ { 0 } & { { \mathrm { i f ~ } } | \lambda | > 1 . } \end{array} \right. }
$$

We can calculate $f ( t ) = \mathcal { F } ^ { - 1 } [ \hat { f } ]$ by computing

$$
\begin{array} { l } { { \displaystyle f ( t ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \widehat { f } ( \lambda ) e ^ { i \lambda t } d \lambda } } \\ { ~ } \\ { { \displaystyle ~ = \int _ { - 1 } ^ { 1 } ( 1 - \lambda ^ { 2 } ) e ^ { i \lambda t } d \lambda } } \\ { { \displaystyle ~ = \frac { 4 \sin ( t ) - 4 \cos ( t ) t } { t ^ { 3 } } . } } \end{array}
$$

The last equality can be obtained by integration by parts (or by using your favorite computer algebra system). The plot of $\pmb { f }$ is given in Figure 16.

Since ${ \widehat { f } } ( \lambda ) = 0$ for $| \lambda | > 1$ , the frequency $\pmb { \Omega }$ from the sampling theorem can be chosen to be any number that is greater than or equal to 1. With $\pmb { \Omega } = \pmb { 1 }$ , we graph the partial sum of the first 30 terms in the series given in the sampling theorem in Figure 17; note that the two graphs are nearly identical.

# 2.5 The Uncertainty Principle

In this section, we present the uncertainty principle, which in words states that a function cannot simultaneously have restricted support in time as well as in frequency. To explain these ideas, we need a definition.

![](images/18c10aa7848224ef28560c3047f8f914fa4562461ef8488e827865263af2616a.jpg)  
Figure 16 Graph of $\pmb { f }$ for Example 2.24

![](images/d15c4a8cf54a66b67a5fcbc979605455aef0341939db99eba0fd9d83bb275e33.jpg)  
Figure 17 Graph of partial series in sampling theorem with $\pmb { \Omega } = \pmb { 1 }$

DEFINItIoN 2.25 Suppose $\pmb { f }$ is a function in $L ^ { 2 } ( R )$ .The dispersion of $\pmb { f }$ about the point $a \in R$ is the quantity

$$
\Delta _ { a } f = \frac { \int _ { - \infty } ^ { \infty } ( t - a ) ^ { 2 } | f ( t ) | ^ { 2 } d t } { \int _ { - \infty } ^ { \infty } | f ( t ) | ^ { 2 } d t } .
$$

![](images/7331aa857a7c035af7af841dc8df333a8678674747ad5bde5eda6082fee6d229.jpg)  
Figure 18 Small dispersion of ${ f } _ { 5 }$ .

The dispersion of $\pmb { f }$ about a point a measures the deviation or spread of its graph from ${ \pmb t = \pmb a }$ .This dispersion will be small if the graph of $\pmb { f }$ is concentrated near ${ \pmb t = \pmb a }$ , as in Figure 18 (with ${ \pmb a } = { \bf 0 }$ . The dispersion will be larger if the graph of $\pmb { f }$ spreads out away from $\pmb { t } = \pmb { a }$ as in Figure 19 (with ${ \pmb { a } } = { \pmb { 0 } }$ .

![](images/96b97019593f40ecdcfb8ba08f37b64e92aedbb313552d7d123f1cddb343d08b.jpg)  
Figure 19 Larger dispersion of $f _ { 1 }$

Another description of the dispersion is related to statistics. Think of the function $\frac { | f ( t ) | ^ { 2 } } { | f | ^ { 2 } }$ as a probability density function (this nonnegative function has integral equal to one, which is the primary requirement for a probability density function). If $\pmb { a }$ is the mean of this density, then $\Delta _ { a } f$ is just the variance.

Applying the preceding definition of dispersion to the Fourier transform of $\pmb { f }$ gives

$$
\Delta _ { \alpha } { \widehat { f } } = { \frac { \int _ { - \infty } ^ { \infty } ( \lambda - \alpha ) ^ { 2 } | { \widehat { f } } ( \lambda ) | ^ { 2 } d \lambda } { \int _ { - \infty } ^ { \infty } | { \widehat { f } } ( \lambda ) | ^ { 2 } d \lambda } } .
$$

By the Plancherel formula (Theorem 2.12), the denominators in the dispersions of $\pmb { f }$ and $\widehat { \pmb f }$ are the same.

If the dispersion of $\widehat { \pmb f }$ about $\lambda = \alpha$ is small, then the frequency range of $\pmb { f }$ is concentrated near $\lambda = \alpha$

Now we are ready to state the uncertainty principle.

THEOREM 2.26 (Uncertainty Principle) Suppose $\pmb { f }$ is a function in $L ^ { 2 } ( R )$ that vanishes at $+ \infty$ and $- \infty$ .Then

$$
\Delta _ { a } f \cdot \Delta _ { \alpha } \widehat { f } \geq \frac { 1 } { 4 }
$$

for all points ${ \pmb { \alpha } } \in \pmb { { \cal R } }$ and $\alpha \in R$ .

One consequence of the uncertainty principle is that the dispersion of $\pmb { f }$ about any $\pmb { a }$ (i.e., $\Delta _ { a } f$ and the dispersion of the Fourier transform of $\pmb { f }$ about any frequency $\pmb { \alpha }$ (i.e., $\Delta _ { \alpha } \widehat { f }$ )cannot simultaneously be small. The graph in Figure 18 offers an intuitive explanation. This graph is concentrated near $\pmb { t = 0 }$ ,and therefore its dispersion about $\pmb { t = 0 }$ is small. However, this function changes rapidly, and therefore it will have large-frequency components in its Fourier transform. Thus, the dispersion of $\widehat { \pmb f }$ about any frequency value will be large. This is illustrated by the wide spread of the graph of its Fourier transform, given in Figure 20.

For a more quantitative viewpoint, suppose

$$
f _ { s } ( x ) = { \sqrt { s } } e ^ { - s x ^ { 2 } } .
$$

The graphs of $\pmb { f _ { s } }$ for $\pmb { \mathscr { s } } = \pmb { 5 }$ and ${ \pmb s } = { \bf 1 }$ are given in Figures 18 and 19 respectively. Note that as $\pmb { \mathscr { s } }$ increases, the exponent becomes more negative and therefore the dispersion of $\pmb { f _ { s } }$ decreases (i.e., the graph of $f _ { s }$ becomes more concentrated near the origin).

The Fourier transform of $f _ { s }$ is

$$
\widehat { f } _ { s } ( \lambda ) = \frac { 1 } { \sqrt { 2 } } e ^ { \frac { - \lambda ^ { 2 } } { 4 \sigma } }
$$

(see Exercise 6). Except for the constant in front, the Fourier transform of $\pmb { f _ { s } }$ has the same general negative exponential form as does $\pmb { f _ { s } }$ .Thus the graph of $\widehat { f } _ { s }$ has the same general shape as does the graph of $\pmb { f _ { s } }$ .There is one notable difference: The factor s appears in the denominator of the exponent in $\widehat { f } _ { s }$ instead of the numerator of the exponent (as is the case for $\pmb { f _ { s } }$ .Therefore, as s increases, the dispersion of $\widehat { f } _ { s }$ also increases (instead of decreasing as it does for $\pmb { f _ { s , } }$ .In particular, it is not possible to choose a value of $\pmb { \mathscr { s } }$ that makes the dispersions of both $\pmb { f _ { s } }$ and $\widehat { f } _ { s }$ simultaneously small.

![](images/881f9b562e566034a6c786c414fd761daec595b93dc6c82229527a47838b81da.jpg)  
Figure 20 Large-frequency dispersion of $\hat { f } _ { 5 }$

Proof of Uncertainty Principle We first claim that the following identity holds:

$$
\left\{ ( { \frac { d } { d t } } - i \alpha ) ( t - a ) \right\} f - \left\{ ( t - a ) ( { \frac { d } { d t } } - i \alpha ) \right\} f = f .
$$

Here, $\pmb { \alpha }$ and $\pmb { a }$ are real constants. Written out in detail, the left side is

$$
\frac { d } { d t } \left\{ ( t - a ) f \right\} - i \alpha ( t - a ) f - ( t - a ) ( f ^ { \prime } - i \alpha f ) .
$$

After using the product rule for the first term and then simplifying, the result is $\pmb { f }$ , which establishes (2.25).

Note that (2.25) remains valid after dividing both sides by the constant $\| f \| = \| f \| _ { L ^ { 2 } }$ .Since the $L ^ { 2 }$ -norm of $f / \| f \|$ is 1, we may as well assume from the start that $\| f \| = 1$ (just by relabeling $\pmb { f } / \| \pmb { f } \|$ as $\pmb { f }$ .

Now take the $L ^ { 2 }$ inner product of both sides of (2.25) with $\pmb { f }$ The result is

$$
\left. { ( \frac { d } { d t } - i \alpha ) \{ ( t - a ) f ( t ) \} , f ( t ) } \right. - \left. { ( t - a ) ( \frac { d } { d t } - i \alpha ) f ( t ) , f ( t ) } \right. = \| f \| ^ { 2 } = 1 .
$$

Both terms on the left involve integrals (from $- \infty$ to $\infty$ ). We use integration by parts on the first integral on the left and use the assumption that $f ( - \infty ) =$ $f ( \infty ) = 0$ The result is

$$
\left. ( t - a ) f ( t ) , ( - \frac { d } { d t } + i \alpha ) f ( t ) \right. - \left. ( \frac { d } { d t } - i \alpha ) f ( t ) , ( t - a ) f ( t ) \right. = 1
$$

(the details of which we ask you to carry out in Exercise 9).

From (2.27) and the triangle inequality, we obtain

$$
1 \leq \left| \left. ( t - a ) f ( t ) , ( - { \frac { d } { d t } } + i \alpha ) f ( t ) \right. \right| + \left| \left. ( { \frac { d } { d t } } - i \alpha ) f ( t ) , ( t - a ) f ( t ) \right. \right| .
$$

Now apply Schwarz's inequality (see Theorem 0.11) to the preceding two inner products:

$$
1 \leq 2 \| ( { \frac { d } { d t } } - i \alpha ) f ( t ) \| \| ( t - a ) f ( t ) \| .
$$

Nex weapply he Planceel orul Theo .1nd the ourt proy listed in Theorem 2.6 to obtain

$$
\| ( \frac { d } { d t } - i \alpha ) f ( t ) \| = \| ( \lambda - \alpha ) \hat { f } ( \lambda ) \| .
$$

Combining this equation with the previous inequality, we get

$$
\| ( \lambda - \alpha ) \hat { f } ( \lambda ) \| \| ( t - \alpha ) f ( t ) \| \geq \frac { 1 } { 2 } .
$$

Since $\| f \| _ { L ^ { 2 } } = 1 = \| \widehat { f } \| _ { L ^ { 2 } }$

$$
\Delta _ { a } ( f ) = \| ( t - a ) f \| _ { L ^ { 2 } } ^ { 2 } \mathrm { a n d } \Delta _ { \alpha } \widehat { f } = \| ( \lambda - \alpha ) \widehat { f } \| _ { L ^ { 2 } } ^ { 2 } .
$$

Therefore, squaring both sides of this inequality yields

$$
\Delta _ { \alpha } \widehat { f } \Delta _ { \alpha } f \geq \frac { 1 } { 4 } ,
$$

which completes the proof of the uncertainty principle.1

# 2.6 Exercises

1. Let

$$
f ( t ) = { \left\{ \begin{array} { l l } { \cos ( 3 t ) } & { { \mathrm { f o r ~ } } - \pi \leq t \leq \pi } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

Show that

$$
\int _ { - \pi } ^ { \pi } \cos ( m t ) \mathrm { c o s } ( \lambda t ) d t = - 2 { \frac { ( - 1 ) ^ { m } \lambda \sin ( \pi \lambda ) } { m ^ { 2 } - \lambda ^ { 2 } } }
$$

where $_ { \pmb { m } }$ is an integer and $\lambda \neq m$ .Hint: Sum the identities

$$
\begin{array} { r } { \cos ( u + v ) = \cos u \cos v - \sin u \sin v , } \\ { \cos ( u - v ) = \cos u \cos v + \sin u \sin v . } \end{array}
$$

Use this integral to show that

$$
\widehat { f } ( \lambda ) = \frac { - \sqrt { 2 } \lambda \sin ( \lambda \pi ) } { \sqrt { \pi } ( \lambda ^ { 2 } - 9 ) }
$$

as indicated in Example 2.3.

2. Let

$$
f ( t ) = { \left\{ \begin{array} { l l } { \sin ( 3 t ) } & { { \mathrm { f o r ~ } } - \pi \leq t \leq \pi } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

Compute $\widehat { f } ( \lambda )$ ( etaiEx..

3. (Note: A computer algebra system would help for this problem). Let

$$
f ( t ) = \left\{ \begin{array} { l l } { t ^ { 2 } + 4 t + 4 } & { \mathrm { f o r } - 2 \leq t \leq - 1 } \\ { 2 - t ^ { 2 } } & { \mathrm { f o r } - 1 \leq t \leq 1 } \\ { t ^ { 2 } - 4 t + 4 } & { \mathrm { f o r } ~ 1 \leq t \leq 2 } \\ { 0 } & { \mathrm { o t h e r w i s e . } } \end{array} \right.
$$

Show that $\pmb { f }$ and $\pmb { f ^ { \prime } }$ are continuous everywhere (pay particular attention to what happens at $t = - 2 , - 1 , 1 .$ and 2). Draw a careful graph of $\pmb { f }$ . Compute its Fourier transform and show that

$$
\widehat { f } ( \lambda ) = \left( \frac { 8 \sin ( \lambda ) ( 1 - \cos ( \lambda ) ) } { \sqrt { 2 \pi } \lambda ^ { 3 } } \right) .
$$

Plot the Fourier transform over the interval $- 1 0 \leq \lambda \leq 1 0$ Note that the Fourier transform decays like $\frac { 1 } { \lambda ^ { 3 } }$ as $\lambda \mapsto \infty$ Also note that in Exercise 1, the given function is discontinuous and $\widehat { f } ( \lambda )$ decays like $\textstyle { \frac { 1 } { \lambda } }$ as $\lambda \mapsto \infty ;$ in Exercise 2, $\pmb { f }$ is continuous but not differentiable and $\widehat { f } ( \lambda )$ decays like $1 / \lambda ^ { 2 }$ . Do you see a pattern?

4.Suppose $f \in L ^ { 2 } ( - \infty , \infty )$ is a real-valued, even function; show that $\widehat { \pmb f }$ is real valued. Suppose $f \in L ^ { 2 } ( - \infty , \infty )$ is a real-valued, odd function; show that $\widehat { f } ( \lambda )$ is purely imaginary (its real part is zero) for each $\lambda$ .

5. Let

$$
\phi ( x ) = \left\{ { \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } 0 \leq x < 1 } \\ { 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} } \right.
$$

Show that

$$
( \phi * \phi ) ( x ) = { \left\{ \begin{array} { l l } { 1 - | x - 1 | } & { { \mathrm { i f ~ } } 0 \leq x < 2 } \\ { 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

6. Let $f _ { s } ( x ) = \sqrt { s } e ^ { - s x ^ { 2 } }$ .Show that

$$
\hat { f } _ { s } ( \lambda ) = \frac { 1 } { \sqrt { 2 } } e ^ { \frac { - \lambda ^ { 2 } } { 4 \nu } } .
$$

Hint: After writing out the definition of the Fourier transform, complete the square in the exponent; then perform a change of variables in the resulting $\textstyle \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x =$ $\sqrt { \pi }$ .

7.Establish the parts of Theorem 2.6 that deal with the inverse Fourier transform. Establish the relationship between the Fourier transform and the Laplace transform given in the last part of this theorem.

8. Suppose $\pmb { L }$ is a time-invariant filter with response function $\pmb { h }$ (see Theorem 2.19). Show that if $\pmb { L }$ is causal, then $h ( t ) = 0$ for $t < 0$ Hint: Prove by contradiction-assume $h ( t _ { 0 } ) \neq 0$ for some $t _ { 0 } < 0 ;$ show that by choosing an appropriate $\pmb { f }$ that is nonzero only on $[ 0 , \delta ]$ for some very small ${ \pmb \delta } > { \bf 0 }$ $L ( f ) ( t ) \neq 0$ for some $t \ : < \ : 0$ even though $\pmb { f } ( \pmb { t } ) = \mathbf { \dot { 0 } }$ for all $\smash { t < 0 }$ (thus contradicting causality).

Using integration by parts, show that (2.27) follows from (2.26).

10. Let

$$
h ( t ) = { \left\{ \begin{array} { l l } { A e ^ { - \alpha t } } & { { \mathrm { i f ~ } } t \geq 0 } \\ { 0 } & { { \mathrm { i f ~ } } t < 0 } \end{array} \right. }
$$

where $\pmb { A }$ and $\pmb { \alpha }$ are parameters as in Example 2.21. Show that

$$
\hat { h } ( \lambda ) = \frac { 1 } { \sqrt { 2 \pi } } ( \mathcal { L } h ) ( i \lambda ) = \frac { A } { \sqrt { 2 \pi } ( \alpha + i \lambda ) } .
$$

1 Consider the signal

$$
f ( t ) = e ^ { - t } \left( \sin 5 t + \sin 3 t + \sin t + \sin 4 0 t \right) \quad 0 \leq t \leq \pi .
$$

Filter this signal with the Butterworth filter [i.e., compute $( f * h ) ( t ) )$ for $0 \leq t \leq \pi ]$ Try various values of $\pmb { A } = \pmb { a }$ (starting with $\pmb { A } = \pmb { a } = \pmb { 1 0 }$ ). Compare the filtered signal with the original signal.

Consider the filter given by $f \mapsto f * h$ , where

$$
h ( s ) : = { \left\{ \begin{array} { l l } { 1 / d } & { 0 \leq t \leq d } \\ { 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

Compute and graph $\widehat { h } ( \lambda )$ for $0 \leq \lambda \leq 2 0$ for various values of $\pmb { d } .$ Suppose you wish to use this filter to remove signal noise with frequency larger than 30 and retain frequencies in the range of 0 to 5 (cycles per $2 \pi \cdot$ interval). What values of $\pmb { d }$ would you use? Filter the signal

$$
f ( t ) = e ^ { - t } \left( \sin 5 t + \sin 3 t + \sin t + \sin 4 0 t \right) \quad 0 \leq t \leq \pi
$$

with your chosen values of $\pmb { d }$ and compare the graph of the filtered signal with the graph of $\pmb { f }$ .

13. The sampling theorem (Theorem 2.23) states that if the Fourier transform of a signal $\pmb { f }$ is band limited to the interval $[ - \Omega , \Omega ]$ ,then the signal can be recovered by sampling the signal at a grid of time nodes separated by a time interval of $\pi / \Omega$ Now suppose that the Fourier transform of a signal, $\pmb { f }$ , vanishes outside the interval $[ \omega _ { 1 } \leq \lambda \leq \omega _ { 2 } ]$ ; develop a formula analogous to (2.21) where the time interval of separation is $2 \pi / ( \omega _ { 1 } + \omega _ { 2 } )$ Hint: Show that the Fourier transform of the signal

$$
g ( t ) = e ^ { - i t \left( \frac { \omega _ { 1 } + \omega _ { 2 } } { 2 } \right) } f ( t )
$$

is band lmited to the inteval $[ - \Omega , \Omega ]$ with $\Omega = ( \omega _ { 2 } - \omega _ { 1 } ) / 2$ and then apply Theorem 2.23 to the signal $\pmb { \mathscr { g } }$

14. (Oversampling) This exercise develops a version of the sampling theorem which converges faster than the version given in Theorem 2.23. Complete the following outline.

Suppose $\pmb { f }$ is a band-limited signal with ${ \widehat { f } } ( \lambda ) = 0$ for $| \lambda | \geq \Omega$ Fix a number ${ \pmb a } > 1$ Repeat the proof of Theorem 2.23 to show that

$$
\widehat { f } ( \lambda ) = \sum _ { n = - \infty } ^ { \infty } c _ { - n } e ^ { - i n \pi \lambda / a \Omega } \quad \mathrm { w i t h ~ } c _ { - n } = \frac { \pi } { \sqrt { 2 \pi } a \Omega } f ( \frac { n \pi } { a \Omega } ) .
$$

(b) Let $\widehat { \pmb { g _ { a } } } ( \lambda )$ be the function whose graph is given by Figure 21. Show that

$$
g _ { a } ( t ) = \frac { \sqrt { 2 } ( \cos ( \Omega t ) - \cos ( a \Omega t ) ) } { \sqrt { \pi } ( a - 1 ) \Omega t ^ { 2 } } .
$$

Since ${ \widehat { f } } ( \lambda ) = 0$ for $| \lambda | \geq \Omega$ . ${ \widehat f } ( \lambda ) = { \widehat f } ( \lambda ) { \widehat g } _ { a } ( \lambda )$ Use Theorem 2.1, Theorem 2.6, and the expressions for $\widehat { \pmb f }$ and $\pmb { \mathscr { g } _ { \pmb { a } } }$ in parts (a) and (b) to show that

$$
f ( t ) = \sum _ { n = - \infty } ^ { \infty } \frac { \pi } { \sqrt { 2 \pi } a \Omega } f \left( \frac { n \pi } { a \Omega } \right) g _ { a } \left( t - \frac { n \pi } { a \Omega } \right) .
$$

![](images/bdd6dea382d7122908734213ad094944b36b01bc13fcb9e779b45d278dc9cdf4.jpg)  
Figure 21 Graph of $\widehat { \pmb { g } } _ { \pmb { a } }$

Since ${ \pmb g } _ { \pmb { a } } ( t )$ has a factor of $\scriptstyle { \pmb { t } } ^ { 2 }$ in the denominator, this expression for ${ f ( t ) }$ converges faster than the expression for $\pmb { f }$ given in Theorem 2.23 (the nth term behaves like $1 / n ^ { 2 }$ instead of $1 / n$ The disadvantage of (2.28) is that the function is sampled on a grid of $n \pi / ( a \Omega )$ , which is a more frequent rate of sampling than the grid $n \pi / \Omega$ (since ${ \pmb a } > { \pmb 1 }$ used in Theorem 2.23. Thus there is a trade-off between the sample rate and the rate of convergence.

# Chapter 3 Discrete Fourier Analysis

The Fourier transform and Fourier series techniques are useful for analyzing continuous signals such as the graph in Figure 1. However, for many applications, the signal is a discrete data set (see Figure 2), such as the signal coming from a compact disc player. A discrete version of the Fourier transform is needed to analyze discrete signals.

# 3.1 The Discrete Fourier Transform

To motivate the idea behind the discrete Fourier transform, we numerically approximate the coefficients of a Fourier series for a continuous function $f ( t )$ . The u e $\begin{array} { r } { ( 2 \pi ) ^ { - 1 } \int _ { 0 } ^ { 2 \pi } F ( t ) d t } \end{array}$ with step size $h = 2 \pi / n$ is

$$
( 2 \pi ) ^ { - 1 } \int _ { 0 } ^ { 2 \pi } F ( t ) d t \approx { \frac { 1 } { 2 \pi } } { \frac { 2 \pi } { n } } \left[ { \frac { Y _ { 0 } } { 2 } } + Y _ { 1 } + \cdot \cdot \cdot + Y _ { n - 1 } + { \frac { Y _ { n } } { 2 } } \right]
$$

where $Y _ { j } : = F ( h j ) = F ( 2 \pi j / n )$ , ${ \mathfrak { j } } = 0 \ldots n$ If $F ( t )$ is $2 \pi$ periodic, then $Y _ { 0 } = Y _ { n }$ and the preceding formula becomes

$$
( 2 \pi ) ^ { - 1 } \int _ { 0 } ^ { 2 \pi } F ( t ) d t \approx \frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } Y _ { j } .
$$

Applying this formula to the computation of the kth complex Fourier coefficient gives

$$
\alpha _ { k } = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) \mathrm { e x p } ( - i k t ) d t \approx \frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } f ( 2 \pi j / n ) \mathrm { e x p } ( - 2 \pi i j k / n ) .
$$

![](images/126182bfd17b588cd0a51e4f662ade0041449999568c151a31866051af7281da.jpg)  
Figure 1 Continuous signal

![](images/f15db0d6c635d2cd0081758a9b8ef91ea110b4cafa106b5ad098aa1d02b23bf4.jpg)  
Figure 2 Discrete signal

Therefore,

$$
\alpha _ { k } \approx \frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } y _ { j } \overline { { w } } ^ { j k } ,
$$

where

$$
y _ { j } = f ( 2 \pi j / n ) \quad { \mathrm { a n d } } \quad w = \exp ( 2 \pi i / n ) .
$$

The sum on the right side of equation (3.1) involves $y _ { j }$ , which is the value of $\pmb { f }$ at $t = 2 \pi j / n$ The values of $f$ at the other $\pmb { t }$ -values are not needed. This sum will be used in the next section as the definition of the Fourier transform of a discrete signal, whose values may only be known at a discrete set of time nodes $t = 2 \pi j / n$ for $j = 0 , \ldots , n - 1$ .

The right side of equation (3.1) is unchanged if $k$ is replaced by $k + n$ since $\overline { { w } } ^ { n } = e ^ { - 2 \pi i } = 1$ T e   .im $\alpha _ { k }$ for $k \geq n ,$ because the $\alpha _ { k }$ are not $_ { \pmb { n } } .$ -periodic. In fact, this expression only approximates $\alpha _ { k }$ for $\pmb { k }$ that are relatively small compared with $^ { \circ }$ because the trapezoidal rule algorithm only provides accurate numerical approximations if the step size, $\hbar = 2 \pi / n ,$ is small relative to the frequency $\boldsymbol { k }$ .

# 3.1.1 Definition of Discrete Fourier Transform

Let $S _ { n }$ be the set of $\scriptstyle { \pmb { n } }$ -periodic sequences of complex numbers. Each clement, $y = \{ y _ { j } \} _ { j = - \infty } ^ { \infty }$ in $S _ { n }$ , can be thought of as a periodic discrete signal where $\boldsymbol { y } _ { j }$ . is the value of the signal at a time node $t = t _ { j }$ . The sequence ${ \boldsymbol { y } } _ { j }$ is $_ { \pmb { n } }$ -periodic if $y _ { k + n } = y _ { k }$ for any integer $\boldsymbol { k }$ , The set $S _ { n }$ forms a complex vector space under the operations of entry-by-entry addition and entry-by-entry multiplication by a scalar. If $x = \{ x _ { j } \} _ { j = \cdots \times \mathsf { C } } ^ { \infty } \in S _ { n }$ and $y = \{ y _ { j } \} _ { j = - x } ^ { \infty } \in S _ { n }$ then the $j$ th component of $\{ x + y \}$ is $x _ { j } + y _ { j }$ and the $j$ th component of $c \{ x \}$ is $\boldsymbol { c } \boldsymbol { x } _ { j }$ Here, $\scriptstyle { \pmb { n } }$ should be thought of as the number of time nodes corresponding to the discrete signal of interest.

Definition 3.1 Let $y = \{ y _ { j } \} _ { j = - x } ^ { x } \in S _ { n }$ . The discrete Fourier trunsform of $_ y$ is the sequence $( \mathcal { F } _ { n } \{ y \} ) _ { k } = \widehat { y } _ { k }$ , where

$$
\widehat { y } _ { k } = \sum _ { j = 0 } ^ { n - 1 } y _ { j } \overline { { w } } ^ { j k } \quad w i t h \quad w = \exp ( 2 \pi i / n ) .
$$

In detail, the discrete Fourier transform is the scquence

$$
\widetilde { \mathcal { Y } } _ { k } = \sum _ { j = 0 } ^ { n - 1 } y _ { j } \exp ( - 2 \pi i k j / n ) .
$$

The formula for the discrete Fourier transform is analogous to the formula for the kth Fourier coefficient with the sum over $\pmb { j }$ taking the place of the integral over $t$ (see Theorem 1.18). As stated in the previous section, if the ${ \bf \mathcal { Y } } _ { \mathcal { I } }$ arise as values from a continuous signal, $f$ , defined on the interval $[ 0 , 2 \pi ]$ , then the kth Fourier coefficient of $f ( \alpha _ { k } )$ is approximated by

$$
\alpha _ { k } \approx \frac { 1 } { n } \widehat { y _ { k } }
$$

for $k$ small relative to $_ { \mathscr { n } }$ -

The computation of the discrete Fourier transform is equivalent to the following matrix computation:

$$
{ \mathcal { F } } _ { n } \{ y \} = { \widehat { y } } = ( { \widehat { F } } _ { n } ) \cdot ( y )
$$

where $y = ( y _ { 0 } , \ldots , y _ { n - 1 } ) ^ { T }$ and $\widehat { \boldsymbol { y } } = ( \widehat { \boldsymbol { y } } _ { 0 } , \dots , \widehat { \boldsymbol { y } } _ { n - 1 } ) ^ { T }$ and where

$$
\begin{array} { r } { F _ { n } = \left( \begin{array} { c c c c c } { 1 } & { 1 } & { 1 } & { \ldots } & { 1 } \\ { 1 } & { w } & { w ^ { 2 } } & { \ldots } & { w ^ { n - 1 } } \\ { 1 } & { w ^ { 2 } } & { w ^ { 4 } } & { \ldots } & { w ^ { 2 ( n - 1 ) } } \\ { \vdots } & { \ddots } & { } & { \vdots } \\ { 1 } & { w ^ { n - 1 } } & { w ^ { 2 ( n - 1 ) } } & { \ldots } & { w ^ { ( n - 1 ) ^ { 2 } } } \end{array} \right) . } \end{array}
$$

# 3.1.2 Properties of the Discrete Fourier Transform

The discrete Fourier transform of a signal in $S _ { n }$ produces a discrete signal that also belongs to $S _ { n }$ , as the following lemma shows.

LEMMA 3.2 ${ \mathcal { F } } _ { n }$ is a linear operator from $s _ { n }$ to $S _ { n }$ .

Proof To show that $\mathcal { F } _ { n } \{ y \}$ belongs to $S _ { n }$ we must show that $\mathcal { F } _ { n } \{ y \} _ { k }$ is $_ { \pmb { \mathscr { n } } }$ periodic. We have

$$
\begin{array} { l } { { \displaystyle { \widehat { y } } _ { k + n } = \sum _ { j = 0 } ^ { n - 1 } y _ { j } { \overline { { w } } } ^ { j ( k + n ) } } } \\ { ~ } \\ { { \displaystyle ~ - \sum _ { j = 0 } ^ { n - 1 } y _ { j } { \overline { { w } } } ^ { j k } { \overline { { w } } } ^ { n } } } \\ { { \displaystyle ~ - \sum _ { j = 0 } ^ { n - 1 } y _ { j } { \overline { { w } } } ^ { j k } ~ \mathrm { [ b e c a u s e ~ } { \overline { { w } } } ^ { n } = e ^ { - ( 2 \pi i / n ) n } = 1 ] } } \\ { { \displaystyle ~ - { \widehat { y } } _ { k } } . } \end{array}
$$

Therefore, $\widehat { y } _ { k + n } = \widehat { y } _ { k }$ and so this sequence is $\pmb { n }$ -periodic. Finally, since matrix multiplication is a linear process, $\mathcal { F } _ { n }$ is $\mathbf { a } _ { \mathrm { ~ } }$ linear operator.

Our next task is to compute the inverse of the discrete Fourier transform. We have already computed the inverse Fourier transform since Theorem 2.1 tells us how to recover the function $\pmb { f }$ from its Fourier transform. The inverse discrete Fourier transform is analogous; it allows us to recover the original discrete signal, $\textbf {  { y } }$ , from its discrete Fourier transform, $\widehat { y } = \overrightarrow { F } _ { n } ( y )$ . Computing the inverse discrete Fourier transform is equivalent to computing the inverse of the matrix ${ \overline { { F } } } _ { n }$ The following theorem gives an easy formula for the inverse of this matrix.

THEOREM 3.3 Suppose $y = \{ y _ { k } \}$ is an element of $S _ { n }$ . Let $\mathcal { F } _ { n } ( y ) = \widehat { y } ,$ that is,

$$
\widehat { \pmb { y } } _ { k } = \sum _ { j = 0 } ^ { n - 1 } y _ { j } \overline { { w } } ^ { j k }
$$

where $w = \exp ( 2 \pi i / n )$ . Then $\boldsymbol { y } = \mathcal { F } _ { n } ^ { - 1 } ( \widehat { \boldsymbol { y } } )$ is given by

$$
y _ { j } = \frac { 1 } { n } \sum _ { k = 0 } ^ { n - 1 } \widehat { y } _ { k } w ^ { j k } .
$$

Remark. Using matrix terminology, Theorem 3.3 asserts that the inverse discrete Fourier transform is given by matrix multiplication with the matrix $\frac { 1 } { n } F _ { n } \left\{ F _ { n } \right.$ is defined in (3.2)]; that is,

$$
y = { \mathcal { F } } _ { n } ^ { - 1 } { \widehat { y } } = { \frac { 1 } { n } } { \left( F _ { n } \right) } \cdot { \left( { \widehat { y } } \right) } .
$$

Since $\widehat { y } = ( \overline { { F } } _ { n } ) ( y )$ , the equation $\begin{array} { r } { y = \frac { 1 } { n } F _ { n } ( \widehat { \mathcal { Y } } ) } \end{array}$ is equivalent to

$$
I _ { n } = \left( { \frac { F _ { n } } { \sqrt { n } } } \right) \left( { \frac { \overrightarrow { F } _ { n } } { \sqrt { n } } } \right) \quad { \mathrm { w h e r e ~ } } I _ { n } = n \times n { \mathrm { ~ i d e n t i t y ~ m a t r i x } } .
$$

Since ${ \cal { F } } _ { n }$ is symmetric, this equation means that the matrix $F _ { n } / { \sqrt { n } }$ is unitary (its inverse equals the conjugate of its transpose).

Proof To establish equation (3.3), we must show that

$$
{ \frac { 1 } { n } } \sum _ { k = 0 } ^ { n - 1 } w ^ { \ell k } { \overline { { w } } } ^ { k j } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } j = \ell } \\ { 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

Since $w = e ^ { 2 \pi i / n }$ , clearly $\overline { { w } } = w ^ { - 1 }$ and so

$$
w ^ { \ell k } { \overline { { w } } } ^ { k j } = w ^ { k ( \ell - j ) } .
$$

To sum this expression over $k = 0 , \ldots , n - 1$ , we use the following identity {see equation (1.23) in the proof of Lemma 1.23]

$$
\sum _ { k = 0 } ^ { n - 1 } z ^ { k } = { \left\{ \begin{array} { l l } { n } & { { \mathrm { i f ~ } } z = 1 } \\ { 1 - z ^ { n } } & { } \\ { 1 - z } & { { \mathrm { i f ~ } } z \neq 1 . } \end{array} \right. }
$$

Set $z = w ^ { \ell - j }$ ; note that $z ^ { n } = 1$ because $w ^ { n } = 1$ .Also note that $\boldsymbol { w } ^ { \ell - \ j } \ne 1$ unless $\dot { \mathcal { I } } = \ell$ for $0 \leq j , \ell \leq n - 1$ . The previous equation becomes

$$
{ \frac { 1 } { n } } \sum _ { k = 0 } ^ { n - 1 } w ^ { ( \ell - j ) k } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } j = \ell } \\ { 0 } & { { \mathrm { i f ~ } } j \neq \ell . } \end{array} \right. }
$$

Thus

$$
{ \frac { 1 } { n } } \sum _ { k = 0 } ^ { n - 1 } w ^ { \ell k } \overline { { w } } ^ { k j } = { \frac { 1 } { n } } \sum _ { k = 0 } ^ { n - 1 } w ^ { ( \ell - j ) k } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } j = \ell } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

as desired.

Both ${ \mathcal { F } } _ { n }$ and $\mathcal { F } _ { n } ^ { - 1 }$ are linear transformations from $s _ { n }$ to itself. Here are some additional properties that are analogous to the corresponding properties for the Fourier transform given in Theorems 2.6 and 2.10. The derivations of these properties will be left as exercises.

TheoreM 3.4 The following properties hold for the discrete Fourier transform.

Shifts or translations. If $y \in S _ { n }$ and $z _ { k } = y _ { k + 1 }$ , then $\mathcal { F } [ z ] _ { j } = w ^ { j } \mathcal { F } [ y ] _ { j }$ , where $w = e ^ { 2 \pi i / n }$ .

Convolutions. If $y \in S _ { n }$ and $z \in S _ { n }$ , then the sequence defined by

$$
[ y * z ] _ { k } : = \sum _ { j = 0 } ^ { n - 1 } y _ { j } z _ { k - j }
$$

is also in $S _ { n }$ . The sequence ${ \pmb y } \ast { \pmb z }$ is called the convolution of the sequences ${ \pmb y }$ and $z$ .

The Convolution theorem: $\mathcal { F } [ y * z ] _ { k } = \mathcal { F } [ y ] _ { k } \mathcal { F } [ z ] _ { k }$ .

If $y \in S _ { n }$ is a sequence of real numbers, then

$$
\begin{array} { r } { \mathcal { F } [ y ] _ { n - k } = \overline { { \mathcal { F } [ y ] } } _ { k } \quad \mathrm { ~ f ~ o ~ r ~ } 0 \leq k \leq n } \\ { o r \qquad \widehat { y } _ { n - k } = \overline { { \widehat { y } } } _ { k } . } \end{array}
$$

Since $\widehat { y } _ { n - k } = \overline { { \widehat { y } } } _ { k }$ , only the $\widehat { y } _ { 0 } , \ldots , \widehat { y } _ { n / 2 - 1 }$ need to be calculated (assuming $_ { \textit { \textbf { n } } }$ is even). Further savings in calculations are possible by using the fast Fourier transform algorithm, which we discuss in the next section.

At the end of Section 3.1, we indicated that if $y _ { k } = f ( k / 2 \pi n )$ for a continuous function, $\pmb { f } .$ then $\widehat { y } _ { k }$ is an accurate approximation of the kth Fourier coefficient of $f , \alpha _ { k }$ when $\pmb { k }$ is small relative to $\pmb { \mathscr { n } }$ The equation $\widehat { y } _ { n - k } = \overline { { \widehat { y } } } _ { k }$ further emphasizes this point. For example, if $_ { \pmb { n } }$ is large and $k = 1$ , then ${ \overline { { \widehat { y } } } _ { n - 1 } } = { \widehat { y } _ { 1 } }$ , which approximates $\alpha _ { 1 } { \mathrm { - } } \mathrm { a }$ low-frequency coefficient. Therefore, $\widehat { y } _ { n - 1 }$ has no resemblance to $\alpha _ { n - 1 }$ -a high-frequency coefficient.

# 3.1.3 The Fast Fourier Transform

Since the discrete Fourier transform is such a valuable tool in signal analysis, an efficient algorithm for computing the discrete Fourier and inverse Fourier transforms is very desirable. The computation of the discrete Fourier transform is equivalent to multiplying the sequence $_ y$ (written as an $n \times 1$ column vector) by the $\pi \times n$ matrix ${ \widetilde { F } } _ { n }$ —an operation that requires $n ^ { 2 }$ multiplications. However, the fast Fourier transform (FFT) is an algorithm that takes advantage of the special form of the matrix $F _ { n }$ to reduce the number of multiplications to roughly $5 n \log _ { 2 } n$ If $n = 1 0 0 0$ , then this simplification reduces the number of multiplications from a million to about 50,000. The relative savings increase as $\pmb { \mathscr { n } }$ gets larger.

The fast Fourier transform algorithm will require an even number of nodes $n = 2 N$ We consider a sequence ${ \mathfrak { y } } = ( y _ { 0 } , \dotsc , y _ { 2 N - 1 } )$ (extended periodically, with period $n = 2 N$ ). The $\hat { y } _ { k }$ are calculated via

$$
\widehat { y } _ { k } = \sum _ { j = 0 } ^ { 2 N - 1 } y _ { j } \overline { { w } } ^ { j k } .
$$

Splitting the preceding sum into even and odd indices yields

$$
\widehat { y } _ { k } = \sum _ { j = 0 } ^ { N - 1 } y _ { 2 j } \overline { { w } } ^ { 2 j k } + \sum _ { j = 0 } ^ { N - 1 } y _ { 2 j + 1 } \overline { { w } } ^ { ( 2 j + 1 ) k } .
$$

Recall that $w = e ^ { 2 \pi i / n }$ and $n = 2 N$ Let $W = \exp ( 2 \pi i / N ) = w ^ { 2 }$ We obtain

$$
\widehat { y } _ { k } = \sum _ { j = 0 } ^ { N - 1 } y _ { 2 j } \bar { W } ^ { j k } + \overline { { w } } ^ { k } \left( \sum _ { j = 0 } ^ { N - 1 } y _ { 2 j + 1 } \bar { W } ^ { j k } \right) .
$$

The preceding equation expresses $\widehat { y } _ { k }$ in terms of two discrete Fourier transforms with $_ { \textit { \textbf { n } } }$ replaced by $N$ :

$$
\widehat { y } _ { k } = \mathcal { F } _ { N } [ \left\{ y _ { 0 } , y _ { 2 } , \cdots , y _ { 2 N - 2 } \right\} ] _ { k } + \widetilde { w } ^ { k } \mathcal { F } _ { N } [ \left\{ y _ { 1 } , y _ { 3 } , \cdots , y _ { 2 N - 1 } \right\} ] _ { k }
$$

for $0 \leq k \leq 2 N - 1$ Further savings are possible. In the last equation, replace $\boldsymbol { k }$ by $k + N$ and use the following facts:

• $\mathcal { F } _ { N } [ y _ { \mathrm { e v e n } } ]$ and $\mathcal { F } _ { N } [ y _ { \mathrm { o d d } } ]$ both have period $N$ .   
• $\overline { { { w } } } ^ { k + N } = \overline { { { w } } } ^ { k } \exp ( - \pi i ) = - \overline { { { w } } } ^ { k }$ .

The result is that for $0 \leq k \leq N - 1$ we have

$$
\begin{array} { r } { \widehat { y } _ { k } = \mathcal { F } _ { N } [ \big \{ y _ { 0 } , y _ { 2 } , \dotsc , y _ { 2 N - 2 } \big \} ] _ { k } + \overline { { w } } ^ { k } \mathcal { F } _ { N } [ \big \{ y _ { 1 } , y _ { 3 } , \dotsc , y _ { 2 N - 1 } \big \} ] _ { k } } \\ { \widehat { y } _ { k + N } = \mathcal { F } _ { N } [ \big \{ y _ { 0 } , y _ { 2 } , \dotsc , y _ { 2 N - 2 } \big \} ] _ { k } - \overline { { w } } ^ { k } \mathcal { F } _ { N } [ \big \{ y _ { 1 } , y _ { 3 } , \dotsc , y _ { 2 N - 1 } \big \} ] _ { k } . } \end{array}
$$

Thus we have described $\left( \mathcal { F } _ { 2 N } y \right) _ { k } ~ = ~ \widehat { y } _ { k }$ for $0 \leq k \leq 2 N - 1$ in terms of $\mathcal { F } _ { N } [ \left\{ y _ { 0 } , y _ { 2 } , \dots , y _ { 2 N - 2 } \right\} ] _ { k }$ and $\mathcal { F } _ { N } [ \left\{ y _ { 1 } , y _ { 3 } , \dotsc , y _ { 2 N - 1 } \right\} ] _ { k }$ for $0 \leq k \leq N - 1$ Similar formulas can be derived for the inverse discrete Fourier transform; they are

$$
\begin{array} { r } { y _ { k } = \displaystyle \frac { 1 } { 2 } \left\{ \mathcal { F } _ { N } ^ { - 1 } \big [ \big \{ \hat { y } _ { 0 } , \hat { y } _ { 2 } , \dotsc , \hat { y } _ { 2 N - 2 } \big \} \big ] _ { k } + w ^ { k } \mathcal { F } _ { N } ^ { - 1 } \big [ \big \{ \hat { y } _ { 1 } , \hat { y } _ { 3 } , \dotsc , \hat { y } _ { 2 N - 1 } \big \} \big ] _ { k } \right\} } \\ { y _ { k + N } = \displaystyle \frac { 1 } { 2 } \left\{ \mathcal { F } _ { N } ^ { - 1 } \big [ \big \{ \hat { y } _ { 0 } , \hat { y } _ { 2 } , \dotsc , \hat { y } _ { 2 N - 2 } \big \} \big ] _ { k } - w ^ { k } \mathcal { F } _ { N } ^ { - 1 } \big [ \big \{ \hat { y } _ { 1 } , \hat { y } _ { 3 } , \dotsc , \hat { y } _ { 2 N - 1 } \big \} \big ] _ { k } \right\} } \end{array}
$$

for $0 \leq k \leq N - 1$ (the factor of $\scriptstyle { \frac { 1 } { 2 } }$ appears because the inversion formula contains a factor of $1 / n$

In matrix terms the computation of the discrete Fourier transform is given by

$$
\mathcal { F } _ { 2 N } y = ( \overrightarrow { F } _ { 2 N } ) ( y ) = \left( \begin{array} { c c } { I _ { N } } & { \overline { { D } } _ { N } } \\ { I _ { N } } & { - \overline { { D } } _ { N } } \end{array} \right) \left( \begin{array} { c c } { \overline { { F } } _ { N } } & { 0 } \\ { 0 } & { \overline { { F } } _ { N } } \end{array} \right) \left( \begin{array} { c } { y _ { \mathrm { e v e n } } } \\ { y _ { \mathrm { o d d } } } \end{array} \right)
$$

where $F _ { N }$ is the matrix defined in (3.2), $\scriptstyle { \pmb { I } } _ { N }$ is the $N \times N$ identity matrix, and $D _ { N }$ is the diagonal matrix with the entries $1 , w , w ^ { 2 } , \ldots , w ^ { N - 1 }$ on the diagonal.

The number of multiplications required to compute the discrete Fourier transform from its definition is about $n ^ { 2 } = 4 N ^ { 2 }$ [since the discrete Fourier transform requires multiplication by the $n \times n$ matrix $F _ { n }$ given in (3.2)]. The number of operations required to compute $\hat { y } _ { k }$ and $\hat { y } _ { k + N }$ in equations (3.4) and (3.5) is $2 N ^ { 2 } + N + 1$ (since $\mathcal { F } _ { N } [ \left\{ y _ { 0 } , y _ { 2 } , \dots , y _ { 2 N - 2 } \right\} ] _ { k }$ and $\mathcal { F } _ { N } [ \left\{ y _ { 1 } , y _ { 3 } , \dotsc , y _ { 2 N - 1 } \right\} ] _ { k }$ both require $N ^ { 2 }$ multiplications). Therefore, the number of multiplications has almost been cut in half (provided $N$ is large). If $N$ is a multiple of 2, then the process can be repeated by writing $\mathcal { F } _ { N }$ as a product involving $\mathcal { F } _ { N / 2 }$ .This would cut the number of multiplications by almost another factor of $\scriptstyle { \frac { 1 } { 2 } }$ or almost one-quarter of the original number.

To keep going, we assume the original value of $_ { \pmb { n } }$ is a power of 2, say $n = 2 ^ { L }$ . Then we can iterate the preceding procedure $\pmb { L }$ times. The Lth iteration involves multiplication by the $\mathbf { \lambda } _ { 1 \times 1 }$ matrix $\overline { { F } } _ { 1 }$ , which is just the scalar 1. How many multiplications are involved with the full implementation of this algorithm? The answer is found as follows. Let $\kappa _ { L }$ be the number of real multiplications required to compute $\mathcal { F } [ \boldsymbol { y } ]$ by the preceding method for $\scriptstyle n \ = \ 2 ^ { L }$ (and so $N = 2 ^ { L - 1 }$ ). From the formulas derived previously, we see that to compute $\mathcal { F } [ y ]$ , we need to compute $\mathcal { F } [ \boldsymbol { y } _ { \mathrm { e v e n } } ]$ and $\mathcal { F } [ \boldsymbol { y } _ { \mathrm { o d d } } ]$ . The number of multiplications required is proportional to $2 K _ { L - 1 } + N = 2 K _ { L - 1 } + 2 ^ { L - 1 }$ Thus, $K _ { L }$ is related to $K _ { L - 1 }$ via

$$
K _ { L } \approx 2 K _ { L - 1 } + 2 ^ { L - 1 } .
$$

When $\scriptstyle { L = 0 }$ , $n = 2 ^ { 0 } = 1$ and no multiplications are required; thus, ${ \pmb K } _ { 0 } = 0$ Inserting $\scriptstyle L = 1$ in the last equation, we find that $K _ { 1 } \approx 1$ Similarly, setting $\scriptstyle { \pmb { \mathscr { L } } } = { \pmb { 2 } }$ then yields $K _ { 2 } \approx 2 \times 2 ^ { 1 }$ .Similarly, $K _ { 3 } \approx 3 \times 2 ^ { 2 }$ , $K _ { 4 } \approx 4 \times 2 ^ { 3 }$ , and so on.The general formula is $K _ { L } \approx L \times 2 ^ { L - 1 }$ .Setting $n = 2 ^ { L }$ and noting that $L = \log _ { 2 } n$ , we see that the number of multiplications required is proportional to $n \log _ { 2 } n$ The actual proportionality constant is about 5.

Similar algorithms can be obtained when $n = N _ { 1 } N _ { 2 } \dots N _ { m }$ , although the fastest one is obtained in the case discussed previously. For a discussion of this and related topics, consult the references.

# EXample 3.5

A plot of the absolute value of the discrete Fourier coefficients for the function $f ( t ) = t + t ^ { 2 }$ is given in Figure 3 (this graph was produced by MATLAB's fft routine). The horizontal axis is $k = 0 , 1 , 2 , \ldots , n$ ,with $n = 6 4$ , and the dots represent $( k , \{ \widehat { y } \kappa \} )$ . Since the Fourier coefficients decay with frequency (by the Riemann-Lebesgue lemma), the $| \widehat { y } _ { k } |$ decrease with $k$ until $k = n / 2$ The graph of the $| \widehat { y } _ { k } |$ is symmetric about the line $k = n / 2 = 3 2$ since $| { \widehat { y } } _ { n - k } | = | { \widehat { y } } _ { k } |$ (so the values of $| \widehat { y } _ { n / 2 + 1 } | , \dots | \widehat { y } _ { n - 1 } |$ are the same as $| \widehat { y } _ { n / 2 - 1 } | , \ldots , | \widehat { y } _ { 1 } | )$ . •

![](images/534697c451dc35b6f0245d1d09661a5cd124e47b3155c55b8081e3c3bcde2531.jpg)  
Figure 3 Plot of fast Fourier transform coefficients for $f = t + t ^ { 2 }$

# EXaMPLe 3.6

We consider the signal in Figure 4, which is generated by the function

$$
y ( t ) = e ^ { - ( \cos t ) ^ { 2 } } ( \sin 2 t + 2 \cos 4 t + 0 . 4 \sin t \sin 5 0 t )
$$

over the interval $0 \leq t \leq 2 \pi$ .We wish to fiter the high-frequency noise from this signal. The signal is first discretized by evaluating it at $2 ^ { 8 } = 2 5 6$ equally spaced points on the interval $0 \leq t \leq 2 \pi$ . Then the fast Fourier transform is used to generate the discrete Fourier coefficients $\widehat { y } _ { k }$ , $k = 0 , \ldots , 2 5 5$ .Judging from Figure 4, the noise has a frequency that is larger than 5 (cycles per $2 \pi$ interval). Thus we keep only $\widehat { y } _ { k }$ for $0 \leq k \leq 5$ and set $\widehat { y } _ { k } = 0$ for $6 \leq k \leq 1 2 8$ . By Theorem 3.4, $\widehat { y } _ { k } = 0$ for $1 2 8 \leq k \leq 2 5 0$ Applying the inverse fast Fourier transform to the filtered $\widehat { y } _ { k }$ , we assemble the filtered signal whose graph is given in Figure 5.

# EXampLe 3.7

We consider the signal given in Figure $\mathbf { 6 } ,$ which is generated by the function

$$
y ( t ) = e ^ { - t ^ { 2 } / 1 0 } ( \sin 2 t + 2 \cos 4 t + 0 . 4 \sin t \sin 1 0 t )
$$

over the interval $0 \leq t \leq 2 \pi$ . We wish to compress this signal by taking its fast Fourier transform and ignoring the small Fourier coefficients. As in the previous example, we sample the signal at $2 ^ { 8 } = 2 5 6$ equally spaced nodes. We apply the fast Fourier transform to generate $\widehat { y } _ { k }$ and set $8 0 \%$ of the $\widehat { y } _ { k }$ equal to zero (the smallest $8 0 \%$ ). Taking the inverse fast Fourier transform of the new $\widehat { y } _ { k }$ , we assemble the compressed signal that is graphed in Figure 7. Notice the Gibbs effect since the partial Fourier series is periodic, and so its values at 0 and $2 \pi$ are the same.

![](images/9f51e700ba68f0934e5764b4930bdc2f9dde1f87b0b9ed137841f3c3599888dd.jpg)  
Figure 4 Unfiltered signal

![](images/cfaa1ebb1f36c46f39297554ba96238f507e66c35c0e031db6dc3fe41179c714.jpg)  
Figure 5 Filtered signal with FFT, keeping only $\widehat { f } _ { k }$ , $k = 0 , \ldots , 5$

![](images/e91560e43c8b6ae6aeba6f4d61e861485062cb4cc41fb94e8ae33e72ef0acad9.jpg)  
Figure 6 Uncompressed signal

![](images/9f84ac476f3a9fe61b1395c794aa30e56ffd3eabe48b55ebaa3613a81237047c.jpg)  
Figure 7 Eighty percent compressed signal with FFT

The relative error between the original signal $_ y$ and the compressed signal yc can be computed to be

$$
{ \mathrm { R e l a t i v e ~ e r r o r } } = { \frac { \| y - y c \| _ { l ^ { 2 } } } { \| y \| _ { l _ { 2 } } } } = 0 . 1 0 1 8
$$

(see Appendix B on MATLAB code to learn how to compute the relative error using MATLAB).

# 3.1.4 The FFT Approximation to the Fourier Transform

A very important application of the FFT is the computation of a numerical approximation to the Fourier transform of a function $\pmb { f }$ defined on an interval $\alpha \leq t \leq b$ from samples taken at $\pmb { n }$ nodes, spaced a constant interval $T$ units apart [i.e., at a $\begin{array} { r } { , a + T , a + 2 T , \ldots , a + ( n - 1 ) T = b - T , } \end{array}$ where $T = ( b - a ) / n ]$ . We assume that the function $f$ is zero outside of the interval $[ a , b ]$ ,continuous on $a \leq t < b$ , and that it satisfies $f ( b ) = f ( c )$ . Since most signals are not periodic, this last assumption will usually result in a discontinuity in the signal at $\pmb { t } = \pmb { b }$ , thus causing a Gibbs phenomenon when the function is reconstructed from the Fourier transform of the data.

The Fourier transform of $f$ is given by

$$
{ \hat { f } } ( \omega ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { a } ^ { b } f ( t ) e ^ { - i \omega t } d t .
$$

We want to change variables so that the time interval runs from 0 to $2 \pi$ rather than $\pmb { a }$ to $^ { b }$ Letting $\theta = 2 \pi \frac { t - a } { b - a }$ (or $t = a + ( b - a ) \theta / 2 \pi )$ , $\hat { f }$ is then given by

$$
\begin{array} { r l r } & { } & { \hat { f } ( \omega ) = \frac { b - a } { ( 2 \pi ) ^ { 3 / 2 } } \int _ { 0 } ^ { 2 \pi } f ( a + ( b - a ) \theta / ( 2 \pi ) ) e ^ { - i \omega ( a + ( b - a ) \theta / ( 2 \pi ) ) } d \theta } \\ & { } & \\ & { } & { = \frac { b - a } { ( 2 \pi ) ^ { 3 / 2 } } e ^ { - i \omega a } \int _ { 0 } ^ { 2 \pi } f ( a + ( b - a ) \theta / ( 2 \pi ) ) e ^ { - i \frac { ( b - a ) \omega } { 2 \pi } \theta } d \theta . } \end{array}
$$

Note that if we define the function $g$ and the frequency $\omega _ { k }$ via

$$
g ( \theta ) : = f ( a + ( b - a ) \theta / ( 2 \pi ) ) \quad { \mathrm { a n d } } \quad \omega _ { k } = { \frac { 2 \pi } { b - a } } k ,
$$

then $\hat { f } ( \omega _ { k } )$ has the form

$$
\hat { f } ( \omega _ { k } ) = \frac { b - a } { \sqrt { 2 \pi } } e ^ { - i \omega _ { k } a } \left\{ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } g ( \theta ) e ^ { - i k \theta } d \theta \right\} = \frac { b - a } { \sqrt { 2 \pi } } e ^ { - i \omega _ { k } a } \hat { g } _ { k }
$$

where $\hat { g } _ { \pmb { k } }$ is the kth Fourier series coefficient for $\pmb { g }$ .

The relationship between the discrete Fourier transform (DFT) and Fourier series coefficients is one that we have dealt with before. First, let

$$
y _ { j } : = g { \Bigl ( } j \underbrace { { \frac { 2 \pi } { n } } } _ { h } { \Bigr ) } = f { \Bigl ( } a + j \underbrace { { \frac { b - a } { n } } } _ { T } { \Bigr ) } , \quad j = 0 , \ldots , n - 1 .
$$

Thus the $y _ { j }$ 's are the samples of $\pmb { f }$ taken at times $a + j T$ .The DFT approximation to $\hat { \pmb g } _ { k }$ is $\hat { y } _ { k } / n$ This implies that the DFT for the $\pmb { \mathcal { Y } } _ { j }$ 's is related to $\hat { f }$ via

$$
\hat { f } ( \omega _ { k } ) \approx \frac { b - a } { n \sqrt { 2 \pi } } e ^ { - i \omega _ { k } a } \hat { y } _ { k } = \frac { T } { \sqrt { 2 \pi } } e ^ { - i \omega _ { k } a } \hat { y } _ { k } .
$$

Formula (3.6) accomplishes our goal of approximating the Fourier transform of $\pmb { f }$ at the frequencies $\omega _ { k }$ by the values of $f$ at $_ { \textit { \textbf { n } } }$ equally spaced nodes on $\alpha \leq t \leq b$ .

# 3.1.5 Application—Parameter Identification

As an application of the discrete Fourier transform, we consider the problem of predicting the sway of a building resulting from wind or other external forces. Buildings, especially very tall ones, sway and vibrate in the wind. This is common and hard to avoid. Too much sway and vibration can cause structural damage. How do we find out how a structure behaves in a strong wind? A rough model for the horizontal displacement $\mathbf { \Delta } _ { \mathbf { \mathcal { U } } }$ due to a wind exerting a force $f$ is

$$
a u ^ { \prime \prime } + b u ^ { \prime } + c u = f ( t )
$$

where $a , b ,$ and $^ c$ are positive constants, with $b ^ { 2 } - 4 a c < 0$ .This is a standard problem in ordinary differential equations. The twist here is that we don't know what $a , b$ ,and $^ { c }$ are. Instead, we have to identify them experimentally.

One way to do this is to hit a wall with a jackhammer and record the response. The impulse force exerted by the jackhammer is modeled by $f ( t ) =$ $f _ { 0 } \delta ( t )$ ,where $\delta ( t )$ is Dirac's $\delta$ function, and $f _ { 0 }$ is the strength of the impulse. Think of the $\delta \cdot$ -function as a signal, with total strength equal to one and that lasts for a very short time. Technically speaking, the $\delta \cdot$ -function is the limit as $h \mapsto 0$ of $f _ { h }$ whose graph is given in Figure 8. The corresponding impulse response $\textbf { \em u }$ has the form (see [3, §6.4])

$$
\begin{array} { r } { \mathbf { \boldsymbol { u } } ( t ) = \left\{ \begin{array} { l l } { 0 } & { t < 0 } \\ { \frac { \boldsymbol { f } _ { 0 } } { \omega a } \sin ( \omega t ) e ^ { - \mu t } } & { t \ge 0 } \end{array} \right. } \end{array}
$$

where $\omega = { \frac { \sqrt { 4 a c - b ^ { 2 } } } { 2 a } }$ and $\mu = { \frac { b } { 2 a } }$ .

The idea now is to take measurements of the the displacements (or sway) at various intervals after the building is hit by the jackhammer. This will give a (discretized) graph of the function $\textbf { \em u }$ In theory, the frequency $\omega$ can be determined from this graph along with decay constant $\mu$ and the amplitude $f _ { 0 } / ( \omega a )$ . Since $f _ { 0 }$ is known (the strength of the jackhammer), the parameter $\pmb { a }$ can be determined from the amplitude $f _ { 0 } / \{ \omega a \}$ and $\omega$ The parameters $^ { b }$ and c can then be determined by the equations $\omega = { \frac { \sqrt { 4 a c - b ^ { 2 } } } { 2 a } }$ and μ = $\mu = { \frac { b } { 2 a } }$ (two equations and two unknowns).

![](images/b24041bf869f4e5a646d10f426571bd21782a951b50f7c2a806938f5e06556a0.jpg)  
Figure 8 Graph of $f _ { h }$

The trouble with this approach is that the actual data (the measurements of the displacements) will look somewhat different from the theoretical response $\mathbf { \Delta } _ { \mathbf { \mathcal { U } } }$ in (3.8). The measured data will contain noise that adds high frequencies to the response. The linear differential equation and the $\delta$ -function used in the preceding model are only rough approximations to the corresponding physical system and actual applied force of the jackhammer. Small nonlinearities in the system and an impulse lasting a finite amount of time will add oscillations to the response. Thus, the frequency $\omega$ may be difficult to infer directly from the graph of the data.

In spite of all of the additional factors mentioned previously, an approximate value of $\boldsymbol { \omega }$ can still be found. This is where the discrete Fourier transform plays a key role. The frequency $\omega$ will be the largest-frequency component present in the data, and this largest frequency can be found easily by computing the discrete Fourier transform of the data. An approximate value for the decay constant $\pmb { \mu }$ can also be determined by analyzing the amplitude of the data. Then approximate values for the parameters $a , b ,$ and c can be determined as indicated previously. These ideas are further investigated in Exercises 3-6.

# 3.1.6 Application—Discretizations of Ordinary Differential Equations

As another application of the DFT, we consider the differential equation in equation (3.7) and take $\pmb { f }$ to be a continuous, $2 \pi$ -periodic function of t. There is a well-known analytical method for finding the unique periodic solution to this equation (cf. [3, 3.7.2]), provided that $f$ is known for all t. On the other hand, if we only know $\pmb { f }$ at the points $t _ { j } = 2 \pi j / n$ , for some integer $\pmb { n } \geq \pmb { 1 }$ , this method is no longer applicable.

Instead of trying to work directly with the differential equation itself, we work with a discretized version of it. There a many ways of discretizing. With $h = 2 \pi / n ,$ ,the one that we use here involves the following approximations:

$$
\begin{array} { l } { { \displaystyle u ^ { \prime } ( t ) \approx \frac { u ( t ) - u ( t - h ) } { h } , } } \\ { { \displaystyle u ^ { \prime \prime } ( t ) \approx \frac { u ( t + h ) + u ( t - h ) - 2 u ( t ) } { h ^ { 2 } } . } } \end{array}
$$

We let $t _ { k } = 2 \pi k / n$ and $u _ { k } = u ( t _ { k } )$ for $0 \leq k \leq n$ Since $\textit { \textbf { u } }$ is periodic, $u _ { n } = u _ { 0 }$

At $t = t _ { k }$ , the preceding difference formulas become

$$
\begin{array} { l } { { u ^ { \prime } ( t _ { k } ) \approx \displaystyle \frac { u _ { k } - u _ { k - 1 } } { h } , } } \\ { { \ } } \\ { { u ^ { \prime \prime } ( t _ { k } ) \approx \displaystyle \frac { u _ { k + 1 } + u _ { k - 1 } - 2 u _ { k } } { h ^ { 2 } } . } } \end{array}
$$

for $1 \leq k \leq n - 1$ Substituting these values into the differential equation (3.7) and collecting terms yields the following difference equation (see Exercise 10):

$$
a u _ { k + 1 } + \beta u _ { k } + \gamma u _ { k - 1 } = h ^ { 2 } f _ { k } , \quad 1 \leq k \leq n - 1
$$

where $f _ { k } = f ( 2 \pi k / n )$ $\beta = c h ^ { 2 } + b h - 2 a$ , and $\gamma = a - b h$ .

Suppose that $u \in S _ { n }$ is a solution to the difference equation (3.11). Let $\hat { u } = \mathcal { F } [ u ]$ and $\hat { f } = \mathcal { F } [ f ]$ and ${ \pmb w } = \mathrm { e x p } ( 2 \pi i / n )$ . By taking the DFT of both sides and using the first part of Theorem 3.4, we can show that (Exercise 11)

$$
\hat { u } _ { j } = h ^ { 2 } ( a w ^ { j } + \beta + \gamma \overline { { w } } ^ { j } ) ^ { - 1 } \hat { f } _ { j } ,
$$

provided that $a w ^ { j } + \beta + \gamma \overline { { w } } ^ { j }$ is never 0 (see Exercise 12). This gives us $\hat { \boldsymbol { u } }$ We get $\textit { \textbf { u } }$ by applying the inverse DFT to $\hat { \boldsymbol { u } }$ .

Of course, there are also direct methods for finding the ${ \mathbf { } } _ { { \mathbf { } } _ { u _ { k } } }$ [by solving the linear equations in (3.11) for the $\scriptstyle { \boldsymbol { u } } _ { k _ { \mathrm { } } }$ . However, often information on the frequency components of the solution is desired. In this case, equation (3.12) provides the discrete Fourier transform of the solution directly.

# 3.2 Discrete Signals

Sampling invariably produces digitized signals, not continuous ones. The signal becomes a sequence, $\boldsymbol { x } = ( \dots , x _ { - 2 } , x _ { - 1 } , x _ { 0 } , x _ { 1 } , \dots )$ , and the index $k$ in ${ \pmb x } _ { \pmb k }$ corresponds to the discrete time. The graph of a discrete signal is called a time series. In this section, we discuss discrete versions of many of the Fourier analysis topics discussed in Chapter 2.

# 3.2.1 Time Invariant, Discrete Linear Filters

This section should be considered as the discrete analog of Section 2.3.1, where continuous time invariant filters were discussed. We first define the time translation operator $\mathcal { T } _ { p }$ on a sequence $_ x$ by

$$
[ T _ { p } ( x ) ] _ { k } = x _ { k - p } .
$$

In words, $T _ { p }$ takes a sequence $_ { x }$ and shifts it $\pmb { p }$ units to the right. For example, if $x _ { k } = ( 1 + k ^ { 2 } ) ^ { - 1 }$ , then $y = T _ { p } ( x )$ has entries $y _ { k } = ( 1 + ( k - p ) ^ { 2 } ) ^ { - 1 }$ .Note that . $T _ { p }$ is a linear operator.

To avoid questions concerning convergence of infinite series, we temporarily assume that our sequences are finite; that is, we consider a sequence $_ { x }$ such that $x _ { k } = 0$ for all $| k | > K$ , where $\kappa$ is some positive number.

DefInItion 3.8 A linear operator $F : x  y$ that takes a sequence $\textbf { \em x }$ into another sequence $_ y$ is time invariant if $F \left( T _ { p } ( x ) \right) = T _ { p } \left( F ( x ) \right)$ .

This condition is simply the discretized version of the time invariance condition associated with continuous-time filters (Definition 2.13).

Any linear operator $\pmb { F }$ that takes sequences to sequences is completely determined by what it does to the unit sequences, $e ^ { n }$ , where

$$
e _ { k } ^ { n } = { \left\{ \begin{array} { l l } { 0 } & { k \neq n } \\ { 1 } & { k = n . } \end{array} \right. }
$$

Why? A sequence $_ { \pmb { x } }$ can be written as the sum $\begin{array} { r } { x = \sum _ { n \in Z } x _ { n } \epsilon ^ { n } } \end{array}$ , because its kth component is the sum $\textstyle \sum _ { n \in Z } x _ { n } e _ { k } ^ { n } = x _ { k }$ The linearity of $\boldsymbol { F }$ then implies

$$
F ( x ) = \sum _ { n \in Z } F ( x _ { n } e ^ { n } ) = \sum _ { n \in Z } x _ { n } F ( e ^ { n } ) .
$$

So knowing the values of $\boldsymbol { F }$ on $e ^ { n }$ completely determines $\boldsymbol { F }$ .

Let $f ^ { n } = F ( e ^ { n } )$ be the sequence that $e ^ { n }$ is transformed into by $\pmb { F }$ . If $F$ is time invariant, then

$$
\begin{array} { r l } & { T _ { p } ( f ^ { n } ) = T _ { p } \left( F ( e ^ { n } ) \right) } \\ & { \qquad = F \left( T _ { p } ( e ^ { n } ) \right) \quad \mathrm { b y ~ t i m e ~ i n v a r i a n c e } } \\ & { \qquad = F ( e ^ { n + p } ) \quad \mathrm { ( s e e ~ E x e r c i s e ~ 1 ) } . } \end{array}
$$

Therefore,

$$
T _ { p } ( f ^ { n } ) = f ^ { n + p } .
$$

We also have $( T _ { p } ( f ^ { n } ) ) _ { k } = f _ { k - p } ^ { n }$ from the definition of $T _ { p }$ Therefore, (3.14) $f _ { k } ^ { n + \mathcal { P } } = f _ { k - \mathcal { P } } ^ { n }$ Iwe set $\scriptstyle n = 0$ then $f _ { k } ^ { p } = f _ { k - p } ^ { 0 }$ eplacing $\pmb { p }$ by $\pmb { \mathscr { n } }$ then

$$
f _ { k } ^ { n } = f _ { k - n } ^ { 0 } .
$$

On the other hand, from (3.13),

$$
F ( x ) _ { k } = \sum _ { n \in Z } x _ { n } \underbrace { F ( e ^ { n } ) _ { k } } _ { f _ { k } ^ { n } } .
$$

$f _ { k } ^ { n } = f _ { k - n } ^ { 0 }$ we have

$$
F ( x ) _ { k } = \sum _ { n \in Z } x _ { n } f _ { k - n } , \quad { \mathrm { w h e r e ~ } } f : = f ^ { 0 } .
$$

Compare this formula to that in Theorem 2.17 for time invariant operators in the continuous case. There, the operator had the form of a convolution of two continuous functions (see Definition 2.9). If we replace the integral in the continuous convolutions with a sum, we obtain the preceding formula. Let us therefore define the discrete version of the convolution of two sequences.

DEfINitioN 3.9 (Discrete Convolution) Given the sequences $\pmb { x }$ and $_ y$ , the convolution $x * y$ is defined to be

$$
( x + y ) _ { k } = \sum _ { n \in Z } x _ { k - n } y _ { n } ,
$$

provided that the series involved are absolutely convergent.

Our analysis in this section can be summarized as follows.

THeOreM 3.10 If $\pmb { F }$ is a time invariant linear operator acting on sequences, it has the form of a convolution; namely, there is a sequence $f$ such that

$$
F ( x ) = f * x ,
$$

provided that the series involved are absolutely convergent. Conversely, if $F ( x ) =$ $\boldsymbol { f } * \boldsymbol { x }$ , then $\pmb { F }$ is a discrete, time invariant linear operator.

We again call such convolution operators discrete filters. The sequence $\pmb { f }$ which satisfies $F ( e ^ { 0 } ) = f$ and is thus a response to an "impulse" at discrete time 0, is called the impulse response $\mathrm { ( I R ) }$ . (Refer to the discussion following Theorem 2.17.) If $f$ has an infinite number of nonvanishing terms, it is called an infinite impulse response (IIR); if it has only a finite number of nonzero terms, it is a finite impulse response (FIR).

# 3.2.2 $\pmb { z }$ -Transform and Transfer Functions

In this section, we generalize the discrete Fourier transformn to infinite sequences in $\ell ^ { 2 }$ . The resulting transform is called the $z$ -transform. There is a close relationship between the $Z$ -transform and the complex form of Fourier series. We will encounter the $z .$ -transform again in Chapter 7.

Recall that $l ^ { 2 }$ is the space of all (complex-valued) sequences having finite energy; that is, all sequences $x = ( \ldots , x _ { - 1 } , x _ { 0 } , x _ { 1 } , \ldots )$ with $\begin{array} { r } { \sum _ { n } | x _ { n } | ^ { 2 } < \infty } \end{array}$ . The inner product of two sequences $\boldsymbol { \mathscr { x } }$ and $_ y$ in $\ell ^ { 2 }$ is given by $\textstyle \langle x , y \rangle = \sum _ { n } x _ { n } { \overline { { y _ { n } } } }$ .

DEfInITion 3.11 The $z$ -transform of a sequence $x = ( \ldots , x _ { - 1 } , x _ { 0 } , x _ { 1 } , \ldots ) \in$ $\scriptstyle { l ^ { 2 } }$ is the function ${ \widehat { \pmb { x } } } : [ - \pi , \pi ] \to C$ :

$$
\widehat { x } ( \phi ) = \sum _ { j = - \infty } ^ { \infty } x _ { j } e ^ { - i j \phi } .
$$

Often; $z = e ^ { i \phi }$ is used in the equation defining $\widehat { \mathbf { x } } ( \cdot )$ , so that $\widehat { \pmb { x } }$ becomes

$$
\widehat { x } ( z ) = \sum \limits _ { j = - x } ^ { \infty } x _ { j } z ^ { - j } .
$$

This is the origin of the $z$ in the transform's name.

The $z$ -transform generalizes the definition of the discrete Fourier transform for finite sequences. To see this, suppose $x = x _ { 0 } , x _ { 1 } , . . . , x _ { n - 1 }$ is a finite sequence (so $\scriptstyle { \pmb x } _ { 3 } \ = \ { \pmb 0 }$ for $j < 0$ and $j \geq n !$ .Inserting the angle $\phi = { \frac { 2 \pi k } { n } }$ into the $z$ -transform gives

$$
{ \widehat { x } } ( { \frac { 2 \pi k } { n } } ) = \sum _ { j = 0 } ^ { n - 1 } x _ { j } e ^ { - { \frac { - \imath _ { j } k 2 \pi } { n } } } = \sum _ { j = 0 } ^ { n - 1 } x _ { j } { \widehat { w } } ^ { j k }
$$

where $w = e ^ { \frac { 2 r \tau } { n } }$ The right side is the defiition of $\widehat { x } _ { k }$ -the kth coefficient of the discrete Fourier transform of $\textbf { x }$ .

Connection with Fourier Series. There is an important relation between the $z$ -transform and Fourier series. For a given $f \in L ^ { 2 } [ - \pi , \pi ]$ , its Fourier series is

$$
f ( \phi ) = \sum _ { n = - \infty } ^ { \infty } x _ { n } e ^ { \imath n \phi }
$$

where $x _ { n }$ is the nth Fourier coefficient of $f$ :

$$
x _ { n } = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( \phi ) e ^ { - i n \phi } d \phi .
$$

From the definition of $\hat { \boldsymbol { x } }$ ,

$$
{ \widehat { x } } ( \phi ) = \sum _ { n = - \infty } ^ { \infty } x _ { n } e ^ { - i n \phi } = f ( - \phi ) .
$$

Thus, a Fourier series expansion is a process that converts a function $_ { f \in }$ $L ^ { 2 } \{ - \pi , \pi \}$ into a sequence, $\{ x _ { n } \} \in l ^ { 2 }$ ;and the $z$ -transform takes the sequence $\{ x _ { n } \}$ back to the function $f$ The following diagram illustrates this relationship.

$$
{ \begin{array} { r l r l } { f \in L ^ { 2 } [ - \pi , \pi ] } & { \qquad } & & { \mathrm { F o u r i e r ~ S e r i e s } } & & { \{ x _ { n } \} \in l ^ { 2 } } \\ & { } & \\ { f ( - \phi ) = { \widehat { x } } ( \phi ) \in L ^ { 2 } [ - \pi , \pi ] } & & { \qquad } & & { \{ x _ { n } \} \in l ^ { 2 } } \end{array} }
$$

Isometry between $L ^ { 2 }$ and $\ell ^ { 2 }$ A further connection to Fourier series is given by Parseval's theorem [see equation (1.39)]. If $x _ { n }$ and $_ { y _ { n } }$ are the Fourier coefficients of $f$ and $g \in L ^ { 2 } [ - \pi , \pi ]$ , then

$$
\begin{array} { r l r } {  { \sum _ { n = - \infty } ^ { \infty } x _ { n } \widetilde { y _ { n } } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( \phi ) \overline { { g ( \phi ) } } d \phi \quad \mathrm { f r o m } \ ( 1 . 3 9 ) } } \\ & { } & { = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \widehat { x } ( - \phi ) \overline { { \widehat { y } ( - \phi ) } } d \phi \quad \mathrm { f r o m } \ ( 3 . 1 6 ) . } \end{array}
$$

With the change of variables $\phi  - \phi$ , we obtain

$$
\frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \widehat { x } ( \phi ) \overline { { \widehat { y } ( \phi ) } } d \phi = \sum _ { n = - \infty } ^ { \infty } x _ { n } \overline { { y _ { n } } }
$$

or, in other words,

$$
{ \frac { 1 } { 2 \pi } } \langle \widehat { x } , \widehat { y } \rangle _ { L ^ { 2 } [ - \pi , \pi ] } = \langle x , y \rangle _ { L ^ { 2 } }
$$

where $\pmb { x } = ( \dots , \pmb { x } _ { - 1 } , \pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \dots )$ and $\pmb { y } = ( \dots , y _ { - 1 } , y _ { 0 } , y _ { 1 } , \dots , )$ . We summarize this discussion in the following theorem.

THEOREM 3.12 The $z$ -transform is an isometry between $\scriptstyle { l ^ { 2 } }$ and $L ^ { 2 } [ - \pi , \pi ]$ (preserves the inner products up to a scalar factor of $1 / 2 \pi )$ . In particular, if $\pmb { x } = ( \dots , \pmb { x } _ { - 1 } , \pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \dots )$ and $\pmb { y } = ( \dots , y _ { - 1 } , y _ { 0 } , y _ { 1 } , \dots )$ are sequences in $\scriptstyle { l ^ { 2 } }$ , then

$$
\frac { 1 } { 2 \pi } \langle \widehat { x } , \widehat { y } \rangle _ { L ^ { 2 } ( - \pi , \pi ] } = \langle x , y \rangle _ { l ^ { 2 } } .
$$

Convolutions. Now we discuss the relationship between convolution operators and the $z$ -transform. We have already mentioned that convolution operators resemble their continuous counterparts. The following theorem carries this analogy one step further (compare with Theorem 2.10).

THeOreM 3.13 Suppose $f = \{ f _ { n } \}$ and $x = \{ x _ { n } \}$ are sequences in $\scriptstyle { l ^ { 2 } }$ . Then

$$
\widehat { \left( f * x \right) } ( \phi ) = \widehat { f } ( \phi ) \widehat { x } ( \phi ) .
$$

The function ${ \widehat { f } } ( \phi )$ is the $z$ -transform of the sequence $\pmb { f }$ and is also called the transfer function associated to the operator $\pmb { F }$ , where $F ( x ) = f * x$ .Often, we identify the convolution operator $\boldsymbol { F }$ with its associated sequence $\pmb { f }$ , and therefore we also identify their transfer functions $( \mathrm { i } . \mathbf { e } . , \hat { F }$ with $\widehat { f }$ .

Proof Using the definition of the $z$ -transform , we have

$$
\widehat { ( f * x ) } ( \phi ) = \sum _ { n = - \infty } ^ { \infty } ( f * x ) ( n ) e ^ { - i n \phi } = \sum _ { n , \ldots \infty } ^ { \infty } \left( \sum _ { k = - \infty } ^ { \infty } f _ { k } x _ { n - k } \right) e ^ { - i n \phi } .
$$

Writing $e ^ { - i n \phi } = e ^ { - i k \phi } e ^ { - i ( n - k ) \phi }$ , we obtain

$$
\begin{array} { c } { { \displaystyle \widehat { ( f * x ) } ( \phi ) = \sum _ { n = - \infty } ^ { \infty } \sum _ { k = - \infty } ^ { \infty } f _ { k } e ^ { - i k \phi } x _ { n - k } e ^ { - i ( n - k ) \phi } } } \\ { { = \displaystyle \sum _ { k = - \infty } ^ { \infty } f _ { k } e ^ { - i k \phi } \sum _ { n = - \infty } ^ { \infty } x _ { n - k } e ^ { - i ( n - k ) \phi } } } \end{array}
$$

where we have switched the order of summation. By replacing ${ \boldsymbol { \pi } } - { \boldsymbol { k } }$ by the index $_ { m }$ in the second sum, this equation becomes

$$
\widehat { ( f * x ) } ( \phi ) = \left( \sum _ { k = - \infty } ^ { \infty } f _ { k } e ^ { - i k \phi } \right) \left( \sum _ { m = - \infty } ^ { \infty } x _ { m } e ^ { - i m \phi } \right) = \widehat { f } ( \phi ) \widehat { x } ( \phi )
$$

as desired.

Adjoint of Convolution Operators. Recall that the adjoint of an operator $F : l ^ { 2 }  l ^ { 2 }$ is the operator $F ^ { * } : l ^ { 2 } \to l ^ { 2 }$ , which is defined by (see Definition 0.29):

$$
\langle F ( x ) , y \rangle = \langle x , F ^ { * } ( y ) \rangle \quad { \mathrm { f o r ~ } } x , y \in l ^ { 2 } .
$$

The next theorem calculates a formula for the sequence associated to the adjoint of a convolution operator. This theorem will be needed in Chapter 7.

THeOrEM 3.14 Suppose $\pmb { F }$ is the convolution operator associated with the sequence $f _ { n }$ . Then ${ \pmb F } ^ { * }$ is the convolution operator associated to the sequence $f _ { n } ^ { * } = { \overline { { f } } } _ { - n }$ . The trunsfer function for $F ^ { * }$ is $\widehat { F } ( \phi )$ .

Proof From the definition of convolution and $\scriptstyle { l ^ { 2 } }$ , we have

$$
\begin{array} { r l } { \langle F ( x ) , y \rangle _ { l ^ { 2 } } = \langle f * x , y \rangle _ { l ^ { 2 } } } & { } \\ & { = \displaystyle \sum _ { n = - \infty } ^ { \infty } ( f * x ) _ { n } \overline { { y } } _ { n } } \\ & { = \displaystyle \sum _ { n = - \infty } ^ { \infty } \sum _ { k = - \infty } ^ { \infty } \sum _ { f _ { n - k } x _ { k } \overline { { y _ { n } } } } ^ { \infty } } \\ & { = \displaystyle \sum _ { k = - \infty } ^ { \infty } x _ { k } \sum _ { n = - \infty } ^ { \infty } \overline { { f _ { - ( k - n ) } y _ { n } } } . } \end{array}
$$

The last sum on the right (under the big conjugation) is $( f ^ { * } * y ) ( k )$ , where $f ^ { * } ( m ) = { \overline { { f } } } _ { - m }$ .Therefore, we obtain

$$
\langle F ( x ) , y \rangle _ { l ^ { 2 } } = \sum _ { k = - \infty } ^ { \infty } x _ { k } { \overline { { { ( f ^ { * } * y ) ( k ) } } } } = \langle x , ( f ^ { * } * y ) \rangle _ { l ^ { 2 } } .
$$

Since $\langle F ( x ) , y \rangle = \langle x , F ^ { * } ( y ) \rangle$ , by definition, we conclude that $F ^ { * } ( y ) = ( f ^ { * } * y ) ,$ where $f _ { m } ^ { * } \simeq \overline { { f } } _ { - m }$ , as desired.

The second part of this theorem follows from the first because

$$
\begin{array} { l } { { \displaystyle \widehat { F } ^ { * } ( \phi ) = \sum _ { n = - \infty } ^ { \infty } \int _ { T _ { n } } ^ { \tau _ { e } } e ^ { - i n \phi } ~ ( \mathrm { b y ~ d e f i n i t i o n ~ o i \setminus \mit \mit \Gamma } ) } } \\ { { \displaystyle \qquad = \sum _ { \mathrm { \scriptsize { u s - \infty } } } ^ { \mathrm { \scriptsize { S C } } } \overline { { { T _ { n } } } } e ^ { - i n \phi } ~ ( \mathrm { b y ~ t h e ~ f i n s t ~ p a r t ~ o f ~ t h e ~ t h e o r e m } ) } } \\ { { \displaystyle \qquad = \sum _ { \mathrm { \scriptsize { u s - \infty } } } ^ { \mathrm { \scriptsize { S e } } } \int _ { - \mathrm { \scriptsize { n } } } e ^ { i n \phi } } } \\ { { \displaystyle \qquad = \sum _ { \mathrm { \scriptsize { u s - \infty } } } ^ { \mathrm { \scriptsize { S e } } } \int _ { - \mathrm { \scriptsize { n } } } e ^ { - i n \phi } } } \\ { { \displaystyle \qquad = \sum _ { \mathrm { \scriptsize { m a x - \infty } } } ^ { \mathrm { \scriptsize { S e } } } f _ { m e } e ^ { - i n \phi } ~ ( \mathrm { b y ~ l e t i n g ~ m = - \mit \pi \mit  \mit \Gamma } ) } } \\ { { \displaystyle \qquad = \sum _ { \mathrm { \scriptsize { m a x - \infty } } } ^ { \mathrm { \scriptsize { S e } } } e ^ { - i n \phi } ~ ( \mathrm { b y ~ t e t i n g ~ m = - \mit \pi  \mit \mathrm { \Lambda } } ) } } \\ { { \displaystyle \qquad = \sum _ { \mathrm { \scriptsize { i n } } } e ^ { i \phi } } } \end{array}
$$

as desired.

# 3.3 Exercises

Some of the following problems require the fast Fourier transform (e.g., Maple or MATLAB's FFT routine).

1. Show that $T _ { p } ( e ^ { n } ) = e ^ { n + p }$ , where $T _ { p }$ and $e ^ { n }$ are defined in Section 3.2.

2. Prove Theorem 3.4.

3.Derive equation (3.8) (see [3, §6.4]).

4.Plot the solution $\mathbf { \Delta } \mathbf { u }$ in (3.8), given $\alpha = 1$ , $\ b = 2$ $c = 3 7$ , and $f _ { 0 } = 1$ .

5. In the previous exercise, use MaTLAB or some similar program to take 256 samples of $_ { \textrm { \tiny a } }$ on the interval [0, 4]. Plot the absolute value of the FFT of $\mathbf { \boldsymbol { u } }$ . Locate the largest natural frequency $\omega / 2 \pi$ Compare with the result from the previous exercise.

6. The FFT locates the frequency reasonably well. Find a way to estimate the damping constant, $\mu$ , from FFT data.

7. Filtering. Let

$$
f ( t ) = e ^ { - t ^ { 2 } / 1 0 } ( \sin ( 2 t ) + 2 \cos ( 4 t ) + 0 . 4 \sin ( t ) \sin ( 5 0 t ) ) .
$$

Discretize $f$ by setting $y _ { k } ~ = ~ f ( 2 k \pi / 2 5 6 )$ $k = 1 , \ldots , 2 5 6$ Use the fast Fourier transform to compute $\widehat { y } _ { k }$ for $0 \leq k \leq 2 5 6$ Recall from Theorem 3.4 that $y _ { n - k } = \overline { y } _ { k }$ . Thus, the low-frequency coefficients are $\widehat { y } _ { 0 } , \ldots , \widehat { y } _ { m }$ and $\widehat { y } _ { 2 5 6 - m } , \ldots , \widehat { y } _ { 2 5 6 }$ for some low value of $_ m$ Filter out the high-frequency terms by setting $\widehat { y } _ { k } = 0$ for $m \leq k \leq 2 5 5 - m$ with $m = 6$ ; then apply the inverse fast Fourier transform to this new set of $\widehat { y } _ { k }$ to compute the $_ { y _ { k } }$ (now filtered); plot the new values of $_ { y _ { k } }$ and compare with the original function. Experiment with other values of $_ { \pmb { m } }$ .

8. Compression. Let $t o l = 1 . 0$ In Exercise 7, if $| \widehat { y } _ { k } | < t o l$ then set $\widehat { y } _ { k }$ equal to zero. Apply the inverse fast Fourier transform to this new set of $\widehat { y } _ { k }$ to compute the $_ { y _ { k } }$ ; plot the new values of $_ { y _ { k } }$ and compare with the original function. Experiment with other values of tol. Keep track of the percentage of Fourier coefficients that have been filtered out. MATLAB's sort command is useful for finding a value for tol in order to filter out a specified percentage of coefficients (see the compression routine in Appendix B on MATLAB code). Compute the relative $\ell ^ { 2 }$ -error of the compressed signal as compared with the original signal (again, see Appendix B on MATLAB code).

9 Repeat the previous two exercises over the interval $0 \leq x \leq 1$ with the function

$$
f ( x ) = - 5 2 x ^ { 4 } + 1 0 0 x ^ { 3 } - 4 9 x ^ { 2 } + 2 + N ( 1 0 0 ( x - 1 / 3 ) ) + N ( 2 0 0 ( x - 2 / 3 ) )
$$

where

$$
N ( t ) = t e ^ { - t ^ { 2 } } .
$$

This time, $y _ { k } = f ( k / 2 5 6 )$ -

erive euatin (3.1 by nserting 3.9and (3.10)into (3. t $t = t _ { k } =$ ${ 2 \pi k / n }$ .

11. Derive equation (3.12), assuming that $a w ^ { j } + \beta + \gamma w ^ { j }$ is never 0.

12. Let $a , b , c ,$ and $4 a c - b ^ { 2 }$ be positive. As in (3.11), set $\beta = c h ^ { 2 } + b h - 2 a$ and $\gamma = a - b h$ Show that if $b h < 2 a$ , $a w ^ { j } + \beta + \gamma \overline { { w } } ^ { j }$ is never O. (Hint: Show that the quadratic equation $a z ^ { 2 } + \beta z + \gamma = 0$ has no solutions for which $| z | = 1 .$ )

. Find the exact, $\pi / 3$ -periodic solution to $u ^ { \prime \prime } + 2 u ^ { \prime } + 2 u = 3 \cos ( 6 t )$ .Compare it with the discrete approximation obtained for these values of $\textit { \textbf { \em a } }$ : $n = 1 6$ , $\begin{array} { r } { n = 6 4 } \end{array}$ ,and $n = 2 5 6$ , You will need to use MATLAB or similar software to compute the FFT and inverse FFT involved.

14. Recall that the complex exponentials $u = \exp ( i n t )$ are $2 \pi$ periodic eigenfunctions of the operator $D ^ { 2 } [ u ] = u ^ { \prime \prime }$ (this means that $D ^ { 2 } [ u ] = - n ^ { 2 } u )$ .A discretized version of this operator acts on the periodic sequences in $S _ { n }$ .If $\boldsymbol { \mathscr { u } } _ { k }$ is $_ { \pmb { n } }$ -periodic, then define $L \{ u \}$ via

$$
L [ u ] _ { k } = u _ { k + 1 } + u _ { k - 1 } - 2 u _ { k } .
$$

Show that $\scriptstyle { \pmb { L } }$ maps $S _ { n }$ into itself.

(b) For $n = 4$ , show the the matrix $M _ { 4 }$ that represents $\scriptstyle I$ is

$$
M _ { 4 } = \left( \begin{array} { c c c c } { { - 2 } } & { { 1 } } & { { 0 } } & { { 1 } } \\ { { 1 } } & { { - 2 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { - 2 } } & { { 1 } } \\ { { 1 } } & { { 0 } } & { { 1 } } & { { - 2 } } \end{array} \right) .
$$

(c) Observe that $M _ { 4 }$ is self-adjoint and thus diagonalizable. Find its eigenvalues and corresponding eigenvectors. How are these related to the matrix columns for the matrix $F _ { 4 }$ in (3.2)? Could you have diagonalized this matrix via an FFT? Explain.   
Generalize this result for all $_ { \textit { \textbf { n } } }$ (Hint: Use the DFT on $L [ u ] _ { k }$ -recall that the FFT is really a fast DFT.)

15. (Circulants and the DFT.) An $\textit { n } \times \textit { n }$ matrix $A$ is called a circulant if all of its diagonals (main, super, and sub) are constant and the indices are interpreted "modulo $^ { \mathfrak { n } }$ " For example, this $4 \times 4$ matrix is a circulant:

$$
\left( { \begin{array} { l l l l } { 9 } & { 2 } & { 1 } & { 7 } \\ { 7 } & { 9 } & { 2 } & { 1 } \\ { 1 } & { 7 } & { 9 } & { 2 } \\ { 2 } & { 1 } & { 7 } & { 9 } \end{array} } \right) .
$$

Look at the $_ { \pmb { n } }$ -periodic sequence $^ { a }$ , where $\alpha _ { \ell } = A _ { \ell + 1 , 1 }$ , $\ell = 0 \ldots n - 1$ . Write the entries of $A$ in terms of the sequence $^ a$ .   
(b) Let $X$ be an $n \times 1$ column vector. Show that $Y = A X$ is equivalent to . $y = \alpha * x$ if $x , y$ are $_ { \pmb { \mathscr { n } } }$ periodic sequences for which $x _ { \ell } = X _ { \ell + 1 , 1 }$ and similarly for $\boldsymbol { y } _ { \ell } = Y _ { \ell + 1 , 1 }$ $\ell = 0 , \ldots , n - 1 .$ .   
(c)Prove that the DFT diagonalizes all circulant matirices; that is, that $n ^ { - 1 } F _ { n } ^ { T } A \bar { F } _ { n } = D$ , where $D$ is diagonal. What are the diagonal entries of $D ?$ (i.e., what are the eigenvalues of $A$ )?

16. Find the $z$ -transform for the sequence

$$
\mathbf { \Sigma } = { \left( \begin{array} { l l l l l l l l l l } { ~ \cdots } & { ~ 0 } & { ~ 0 } & { ~ 1 } & { ~ { \frac { 1 } { 2 } } } & { ~ { \frac { 1 } { 4 } } } & { ~ \cdots } & { ~ { \frac { 1 } { 2 ^ { n } } } } & { ~ \cdots } \end{array} \right) } .
$$

# Chapter 4

# Haar Wavelet Analysis

# 4.1 Why Wavelets?

Wavelets were first applied in geophysics to analyze data from seismic surveys, which are used in oil and mineral exploration to get "pictures" of layering in subsurface rock. In fact, geophysicists rediscovered them; mathematicians had developed them to solve abstract problems some twenty years earlier but had not anticipated their applications in signal processing.1

Seismic surveys are made up of many two-dimensional pictures or slices, which are sewn together to give a three-dimensional image of the structure of rock below the surface. Each slice is obtained by placing geophones—seismic "microphones"—at equally spaced intervals along a line, the seismic line. Dynamite is set off at one end of the line to create a seismic wave in the ground. Every geophone along the line records the movement of the earth due to the blast, from start to finish; this record is its seismic trace (see Figure 1).

The first wave recorded by the geophones is the direct wave, which travels along the surface. This is usually not important. Subsequent waves are reflected off rock layers below ground. These are the important ones. Knowledge of the time that the wave hits a geophone gives information about where the layer that reflected it is located. The "wiggles" that the wave produces tell something about the fine details of the layer. The traces from the all the geophones on a line can be combined to give the slice for the ground directly beneath the line.

The key to an accurate seismic survey is a proper analysis of each trace. The Fourier transform is not a good tool here. It can only provide frequency information (the oscillations that comprise the signal). It gives no direct information about when an oscillation occurred. Another tool, the short-time Fourier transform, is better. The full-time interval is divided into a number of small, equal-time intervals; these are individually analyzed using the Fourier transform. The result contains time and frequency information. However, there is a problem with this approach. The equal-time intervals are not adjustable; the times when very-short-duration, high-frequency bursts occur are hard to detect.

![](images/06d0cfdbf0ceb61786fe40acdb67338c6c81d079508ca396b8bc5cfb800da15d.jpg)  
Figure 1 A typical seismic trace. Displacement is plotted versus time. Both the oscillations and the time they occur are important.

Enter wavelets. Wavelets can keep track of time and frequency information. They can be used to "zoom in" on the short bursts mentioned previously, or to "zoom out" to detect long, slow oscillations.

# 4.2 Haar Wavelets

# 4.2.1 The Haar Scaling Function

There are two functions that play a primary role in wavelet analysis, the scaling function $\phi$ and the wavelet $\psi$ These two functions generate a family of functions that can be used to break up or reconstruct a signal. To emphasize the "marriage" involved in building this "family," $\phi$ is sometimes called the "father wavelet" and $\psi$ , the "mother wavelet."

The simplest wavelet analysis is based on the Haar scaling function , whose graph is given in Figure 4. The building blocks are translations and dilations (both in height and width) of this basic graph.

We want to illustrate the basic ideas involved in such an analysis. Consider the signal shown in Figure 2. We may think of this as a measurement of some physical quantity—perhaps line voltage over a single cycle—as a function of time. The two sharp spikes in the graph might represent noise coming from a loose connection in the volt meter, and we want to filter out this undesirable noise. The graph in Figure 3 shows one possible approximation to the signal using Haar building blocks. The high-frequency noise shows up as tall, thin blocks. An algorithm that deletes the thin blocks will eliminate the noise and not disturb the rest of the signal.

![](images/5b123f5ce181795ac51a97549c2ceeb326a20dd4fe4b1a843613dc638858b2d5.jpg)  
Figure 2 Voltage from a faulty meter

The building blocks generated by the Haar scaling function are particularly simple and illustrate the general ideas underlying a multiresolution analysis, which we will discuss in detail. The disadvantage of the Haar wavelets is that they are discontinuous and therefore do not approximate continuous signals very well (Figure 3 does not really approximate Figure 2 too well). In later sections, we introduce other wavelets, due to Daubechies, that are continuous but still retain the localized behavior exhibited by the Haar wavelets.

# 4.2.2 Basic Properties of the Haar Scaling Function

DeFIniTioN 4.1 The Haar scaling function is defined as

$$
\phi ( x ) = \left\{ \begin{array} { l l } { 1 , \quad i f 0 \leq x < 1 } \\ { 0 , \quad e l s e w h e r e . } \end{array} \right.
$$

The graph of the Haar scaling function is given in Figure 4.

![](images/3e8fcec3243ec8a0a49fbfbd7bd4837bc2448d15ed3f94fd96d3b866bf769fdb.jpg)  
Figure 3 Approximation of voltage signal by Haar functions

![](images/0b41ecb4dae7c65b4df639c1c2987e7bf937e51fea0cba244e5baaab3b3e558f.jpg)  
Figure 4 Graph of the Haar scaling function

The function $\phi ( { \pmb x } - { \pmb k } )$ has the same graph as $\phi$ but translated to the right by $\pmb { k }$ units (assuming $\pmb { k }$ is positive). Let $V _ { 0 }$ be the space of all functions of the form

$$
\sum _ { k \in Z } a _ { k } \phi ( x - k ) \quad a _ { k } \in R
$$

where $\pmb { k }$ can range over any finite set of positive or negative integers. Since $\phi ( { \pmb x } - { \pmb k } )$ is discontinuous at ${ \pmb x } = { \pmb k }$ and ${ \pmb x } = { \pmb k } + { \pmb 1 }$ , an alternative description of $V _ { 0 }$ is that it consists of all piecewise constant functions whose discontinuities are contained in the set of integers. Since $\pmb { k }$ ranges over a finite set, each element of $V _ { 0 }$ is zero outside a bounded set. Such a function is said to have finite or compact support. The graph of a typical element of $V _ { 0 }$ is given in Figure 5.

![](images/ef6e6b9806c154e4ee3a7983047740c703dd043deed320aee5a174804b689faf.jpg)  
Figure 5 Graph of typical element in $V _ { 0 }$

Note that a function in $V _ { 0 }$ may not have discontinuities at all the integers (for example, if ${ \pmb a } _ { 1 } = { \pmb a } _ { 2 }$ , then the preceding sum is continuous at ${ \pmb x } = { \pmb 2 }$

# EXample 4.2

The graph of the function

$$
f ( x ) = 2 \phi ( x ) + 3 \phi ( x - 1 ) + 3 \phi ( x - 2 ) - \phi ( x - 3 ) \in V _ { 0 }
$$

is given in Figure 6. This function has discontinuities at ${ \pmb x } = { \pmb 0 } , { \pmb 1 } , { \pmb 3 } .$ and 4.

![](images/6ea3868e22ec5715e925c63d0ac8d093ed86658ebc3c6857a6ec16780d6456d1.jpg)  
Figure 6 Plot of $\pmb { f }$ in Example 4.2

We need blocks that are thinner to analyze signals of high frequency. The building block whose width is half that of the graph of $\phi$ is given by the graph of $\phi ( 2 x )$ shown in Figure 7.

![](images/b2b0753e8a56edd1109e0c95e1e27f817dca7d2938acd18d75fa223cfce798ec.jpg)  
Figure 7 Graph of $\phi ( 2 x )$ .

The function $\phi ( 2 x - k ) = \phi ( 2 ( x - k / 2 ) )$ is the same as the graph of the function of $\phi ( 2 x )$ but shifted to the right by $k / 2$ units. Let $V _ { 1 }$ be the space of functions of the form

$$
\sum _ { k \in Z } a _ { k } \phi ( 2 x - k ) \quad a _ { k } \in R .
$$

Geometrically, $V _ { 1 }$ is the space of piecewise constant functions of finite support with possible discontinuities at the half-integers $\{ 0 , \pm 1 / 2 , \pm 1 , \pm 3 / 2 , \ldots \}$ .

# EXaMPLe 4.3

The graph of the function

$$
f ( x ) = 4 \phi ( 2 x ) + 2 \phi ( 2 x - 1 ) + 2 \phi ( 2 x - 2 ) - \phi ( 2 x - 3 ) \in V _ { 0 }
$$

is given in Figure 8. This function has discontinuities at $\pmb { x } = 0 , 1 / 2 , 3 / 2$ , and 2.

![](images/2450a55351a9a29b4b7895396cca4ff20d46c008532bdadba8bad9a1439350ad.jpg)  
Figure 8 Plot of $\pmb { f }$ in Example 4.3

We make the following more general definition.

DEfinitioN 4.4 Suppose $j$ is any nonnegative integer. The space of step functions at level $\dot { \jmath }$ , denoted by $V _ { j }$ , is defined to be be the space spanned by the set

$$
\{ \ldots , \phi ( 2 ^ { j } x + 1 ) , \phi ( 2 ^ { j } x ) , \phi ( 2 ^ { j } x - 1 ) , \phi ( 2 ^ { j } x - 2 ) , \ldots \}
$$

over the real numbers. $V _ { j }$ is the space of piecewise constant functions of finite support whose discontinuities are contained in the set

$$
\{ \ldots , - 1 / 2 ^ { j } , 0 , 1 / 2 ^ { j } , 2 / 2 ^ { j } , 3 / 2 ^ { j } , \ldots \} .
$$

A function in $V _ { 0 }$ is a piecewise constant function with discontinuities contained in the set of integers. Any function in $V _ { 0 }$ is also contained in $V _ { 1 }$ , which consists of piecewise constant functions whose discontinuities are contained in the set of half-integers $\{ \dots , - 1 / 2 , 0 , 1 / 2 , 1 , 3 / 2 , \dots \}$ The same applies for $V _ { 1 } \subset V _ { 2 }$ and so forth:

$$
V _ { 0 } \subset V _ { 1 } \subset \cdots . . . V _ { j - 1 } \subset V _ { j } \subset V _ { j + 1 } \cdots .
$$

This containment is strict. For example, the function $\phi ( 2 x )$ belongs to $V _ { 1 }$ but does not belong to $V _ { 0 }$ [since $\phi ( 2 x )$ is discontinuous at $\pmb { x } = \pmb { 1 } / 2 ]$ .

$V _ { j }$ contains all relevant information up to a resolution scale of order ${ \pmb { 2 } } ^ { - j }$ . As $\pmb { j }$ gets larger, the resolution gets finer. The fact that $V _ { j } \subset V _ { j + 1 }$ means that no information is lost as the resolution gets finer. This containment relation is also the reason why $V _ { j }$ is defined in terms of $\phi ( 2 ^ { j } x )$ instead of $\phi ( a x )$ for some other factor $\pmb { a }$ If, for example, we had defined $V _ { 2 }$ using $\phi ( 3 x - j )$ instead of $\phi ( 4 x - j )$ , then $V _ { 2 }$ would not contain $V _ { 1 }$ (since the set of multiples of $_ { 1 / 2 }$ is not contained in the set of multiples of $1 / 3$ .

# 4.2.3 Basic Properties of the Haar Scaling Function

The following theorem is an easy consequence of the definitions.

# TheoreM 4.5

A function $\pmb { f } ( \pmb { x } )$ belongs to $V _ { 0 }$ if and only if $f ( 2 ^ { j } x )$ belongs to $V _ { j }$ .   
•A function $\pmb { f } ( \pmb { x } )$ belongs to $V _ { j }$ if and only if $f ( 2 ^ { - j } x )$ belongs to $V _ { 0 }$ .

Proof To prove the first statement, if a function $\pmb { f }$ belongs to $V _ { 0 }$ , then $\pmb { f } ( \pmb { x } )$ is a linear combination of $\{ \phi ( x - k ) , k \in Z \}$ .Therefore, $f ( 2 ^ { j } x )$ is a linear combination of $\{ \phi ( 2 ^ { j } x - k ) , k \in Z \}$ , which means that $f ( 2 ^ { j } x )$ is a member of $V _ { j }$ The proofs of the converse and the second statement are similar. $\bullet$

The graph of the function $\phi ( 2 ^ { j } x )$ is a spike of width $1 / 2 ^ { j }$ .When $\dot { \pmb { \mathscr { I } } }$ is large, the graph of $\phi ( \pmb { 2 } ^ { j } \pmb { x } )$ (appropriately translated) is similar to one of the spikes of a signal that we may wish to filter out. Thus it is desirable to have an efficient algorithm to decompose a signal into its $V _ { j }$ -components. One way to perform this decomposition efciently is to construct an orthonormal bass for $V _ { j }$ (using the $L ^ { 2 }$ inner product).

Let's start with $V _ { 0 }$ . This space is generated by $\phi$ and its translates. The functions $\phi ( { \pmb x } - { \pmb k } )$ each have unit norm in ${ { \pmb { L } } ^ { 2 } }$ ;that is,

$$
\| \phi ( x - k ) \| _ { L ^ { 2 } } ^ { 2 } = \int _ { - \infty } ^ { \infty } \phi ( x - k ) ^ { 2 } d x = \int _ { k } ^ { k + 1 } 1 d x = 1 .
$$

If $\pmb { j }$ is different from $\pmb { k }$ , then $\phi ( { \pmb x } - j )$ and $\phi ( { \boldsymbol { x } } - { \boldsymbol { k } } )$ have disjoint supports (see Figure 9). Therefore,

$$
\langle \phi ( x - j ) , \phi ( x - k ) \rangle _ { L ^ { 2 } } = \int _ { - \infty } ^ { \infty } \phi ( x - j ) \phi ( x - k ) d x = 0 \quad j \neq k
$$

and so the set $\{ \phi ( x - k ) , k \in Z \}$ is an orthonormal basis for $V _ { 0 }$ -

![](images/e4ea20dbd710285c3a3da5eb44900f1b50cd2f18abf58b08d7fce57bb5d7d893.jpg)  
Figure 9 $\phi ( { \pmb x } - j )$ and $\phi ( { \pmb x } - { \pmb k } )$ have disjoint support

The same argument establishes the following more general result.

THeOreM 4.6 The set of functions $\{ 2 ^ { j / 2 } \phi ( 2 ^ { j } x - k ) ; k \in Z \}$ is an orthonormal basis of $V _ { j }$ .

[The factor $\scriptstyle 2 ^ { j / 2 }$ is present since $\begin{array} { r } { \int _ { - \infty } ^ { \infty } ( \phi ( 2 ^ { j } x ) ) ^ { 2 } d x = 1 / 2 ^ { j } . } \end{array}$ ]

# 4.2.4 The Haar Wavelet

Having an orthonormal basis of $V _ { j }$ is only half of the picture. In order to solve our noise-filtering problem, we need to have a way of isolating the "spikes" that belong to $V _ { j }$ but that are not members of $V _ { j - 1 }$ .This is where the wavelet $\psi$ enters the picture.

The idea is to decompose $V _ { j }$ as an orthogonal sum of $V _ { j - 1 }$ and its complement. Again, let's start with $j = 1$ and identify the orthogonal complement of $V _ { 0 }$ in $V _ { 1 }$ .Since $V _ { 0 }$ is generated by $\phi$ and its translates, it is reasonable to expect that the orthogonal complement of $V _ { 0 }$ is generated by the translates of some function $\psi$ .Two key facts are needed to construct $\psi$ :

1. $\psi$ is a member of $V _ { 1 }$ and so $\psi$ can be expressed as $\begin{array} { r } { \psi ( x ) = \sum _ { l } a _ { l } \phi ( 2 x - l ) } \end{array}$ . for some choice of ${ \pmb a } _ { l } \in \pmb R$ (and only a finite number of the ${ \pmb a } _ { l }$ are nonzero). 2. $\psi$ is orthogonal to $V _ { 0 }$ This is equivalent to $\begin{array} { r } { \int { \psi ( x ) \phi ( x - k ) d x } = 0 } \end{array}$ for all integers $\pmb { k }$ .

The first requirement means that $\psi$ is built from blocks of width $_ { 1 / 2 }$ (i.e., scalar multiples of Figure 7 and its translates). The second requirement with $\pmb { k } = \pmb { 0 }$ implies $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \psi ( x ) \phi ( x ) d x = 0 } \end{array}$ The simplest $\psi$ satisfying both of these requirements is the function whose graph appears in Figure 10. This graph consists of two blocks of width one-half and can be written as

$$
\psi ( x ) = \phi ( 2 x ) - \phi ( 2 ( x - 1 / 2 ) ) = \phi ( 2 x ) - \phi ( 2 x - 1 )
$$

thus satisfying the first requirement. In addition,

$$
\begin{array} { l } { \displaystyle \int _ { - \infty } ^ { \infty } \phi ( x ) \psi ( x ) d x = \int _ { 0 } ^ { 1 / 2 } 1 d x - \int _ { 1 / 2 } ^ { 1 } 1 d x } \\ { = 1 / 2 - 1 / 2 } \\ { = 0 . } \end{array}
$$

Thus, $\psi$ is orthogonal to $\phi$ If $\pmb { k } \neq 0$ , then the support of $\psi ( x )$ and the support of $\phi ( { \pmb x } - { \pmb k } )$ do not overlap and so $\begin{array} { r } { \int { \psi ( x ) \phi ( x - k ) d x } = 0 , } \end{array}$ Therefore, $\psi$ belongs to $V _ { 1 }$ and is orthogonal to $V _ { 0 } ; \psi$ is called the Haar wavelet.

DEFINITIoN 4.7 The Haar wavelet is the function

$$
\psi ( x ) = \phi ( 2 x ) - \phi ( 2 x - 1 ) .
$$

Its graph is given in Figure 10.

You can show (see Exercise 4) that any function

$$
f _ { 1 } = \sum _ { k } a _ { k } \phi ( 2 x - k ) \in V _ { 1 }
$$

is orthogonal to $V _ { 0 }$ —that is, orthogonal to each $\phi ( { \boldsymbol { \mathbf { \mathit { x } } } } - { \boldsymbol { \mathbf { \mathit { l } } } } ) , { \boldsymbol { \imath } } \in { \boldsymbol { \mathbf { \mathit { Z } } } } )$ if and only if

$$
a _ { 1 } = - a _ { 0 } , \quad a _ { 3 } = - a _ { 2 } , \ldots .
$$

In this case,

$$
f _ { 1 } = \sum _ { k \in \cal Z } a _ { 2 k } \left( \phi ( 2 x - 2 k ) - \phi ( 2 x - 2 k - 1 ) \right) = \sum _ { k \in \cal Z } a _ { 2 k } \psi ( x - k ) .
$$

![](images/370ef0362f98abb7a6c5cfdeb5f3dfd97e85a9dc7b2ac770a03ea432c1c2af18.jpg)  
Figure 10 The Haar wavelet $\psi ( { \pmb x } )$

In other words, a function in $V _ { 1 }$ is orthogonal to $V _ { 0 }$ if and only if it is of the form $\begin{array} { r } { \sum _ { k } a _ { k } \psi ( { \pmb x } - { \pmb k } ) } \end{array}$ (relabeling $a _ { 2 k }$ by ${ \pmb a } _ { { \pmb k } }$ ).

Let $W _ { 0 }$ be the space of all functions of the form

$$
\sum _ { k \in \mathcal { Z } } a _ { k } \psi ( x - k ) \quad a _ { k } \in R
$$

where, again, we assume that only a finite number of the $\pmb { a } _ { \pmb { k } }$ are nonzero. What we have just shown is that $W _ { 0 }$ is the orthogonal complement of $V _ { 0 }$ in $V _ { 1 }$ or, in other words, $V _ { 1 } = V _ { 0 } \oplus W _ { 0 }$ (recall from Chapter 0 that $\oplus$ means that $V _ { 0 }$ and $W _ { 0 }$ are orthogonal to each other).

In a similar manner, the following more general result can be established.

THEOrEM 4.8 Let $W _ { j }$ be the space of functions of the form

$$
\sum _ { k \in Z } a _ { k } \psi ( 2 ^ { j } x - k ) \quad a _ { k } \in R
$$

where we assume that only a finite number of ${ \pmb a } _ { { \pmb k } }$ are nonzero. $W _ { j }$ is the orthogonal complement of $V _ { j }$ in $V _ { j + 1 }$ and

$$
V _ { j + 1 } = V _ { j } \oplus W _ { j } .
$$

Proof To establish this theorem, we must show two facts:

1. Each function in $W _ { j }$ is orthogonal to every function in $V _ { j }$ .   
2. Any function in $V _ { j + 1 }$ that is orthogonal to $V _ { j }$ must belong to $W _ { j }$ .

For the first requirement, suppose that $\begin{array} { r } { { \pmb g } = \sum _ { k \in { \pmb Z } } a _ { k } \psi ( 2 ^ { j } { \pmb x } - { \pmb k } ) } \end{array}$ belongs to $W _ { j }$ and suppose that $\pmb { f }$ belongs to $V _ { j }$ .We must show

$$
\langle g , f \rangle _ { L ^ { 2 } } = \int _ { - \infty } ^ { \infty } g ( x ) { \overline { { f ( x ) } } } d x = 0 .
$$

Since $\pmb { f } ( \pmb { x } )$ belongs to $V _ { j }$ , the function $f ( 2 ^ { - j } x )$ belongs to $V _ { 0 }$ .So

$$
{ \begin{array} { r l r } & { 0 = \displaystyle \int _ { - \infty } ^ { \infty } \displaystyle \sum _ { k \in Z } a _ { k } \psi ( x - k ) { \overline { { f ( 2 ^ { - } j \cdot x ) } } } d x } & { { \mathrm { ( b e c a u s e ~ } } \psi { \mathrm { ~ i s ~ o r t h o g o r } } } \\ & { } & \\ & { = 2 ^ { j } \displaystyle \int _ { - \infty } ^ { \infty } \displaystyle \sum _ { k \in Z } a _ { k } \psi ( 2 ^ { j } y - k ) { \overline { { f ( y ) } } } d y } & { { \mathrm { ( b y ~ l e t t i n g ~ } } y = 2 ^ { - } j _ { x } { \mathrm { ) } } } \\ & { } & \\ & { = 2 ^ { j } \displaystyle \int _ { - \infty } ^ { \infty } g ( y ) { \overline { { f ( y ) } } } d y . } \end{array} }
$$

Therefore, $\pmb { \mathscr { g } }$ is orthogonal to any $f \in V _ { j }$ and the first requirement has been established.

The discussion leading to equation (4.1) establishes the second requirement when ${ \dot { \pmb { \jmath } } } = { \bf 0 }$ since we showed that any function in $V _ { 1 }$ that is orthogonal to $V _ { 0 }$ must be a linear combination of $\{ \psi ( x - k ) , \ k \in Z \}$ .The argument for general $\pmb { j }$ is very similar to the case when ${ \dot { \pmb { \jmath } } } = { \bf 0 }$ . $\bullet$

By successively decomposing $V _ { j }$ , $V _ { j - 1 }$ and so on, we have

$$
\begin{array} { r l } & { V _ { j } = W _ { j - 1 } \oplus V _ { j - 1 } } \\ & { \quad = W _ { j - 1 } \oplus W _ { j - 2 } \oplus V _ { j - 2 } } \\ & { \qquad \quad \cdots } \\ & { \quad = W _ { j - 1 } \oplus W _ { j - 2 } \oplus \cdots \oplus W _ { 0 } \oplus V _ { 0 } . } \end{array}
$$

So each $\pmb { f }$ in $V _ { j }$ can be decomposed uniquely as a sum

$$
\ b { f } = w _ { j - 1 } + w _ { j - 2 } + \dots + w _ { 0 } + \ b { f _ { 0 } }
$$

where each $_ { w _ { l } }$ belongs to $W _ { l }$ , $0 \leq l \leq j - 1$ and $\pmb { f _ { 0 } }$ belongs to $V _ { 0 }$ Intuitively, ${ \pmb w } _ { \pmb { l } }$ represents the "spikes" of $\pmb { f }$ of width $1 / 2 ^ { l + 1 }$ that cannot be represented as linear combinations of spikes of other widths.

What happens when $\pmb { j }$ goes to infinity? The answer is provided in the following theorem.

THEOREM 4.9 The space $L ^ { 2 } ( R )$ can be decomposed as an infinite orthogonal direct sum

$$
L ^ { 2 } ( R ) = V _ { 0 } \oplus W _ { 0 } \oplus W _ { 1 } \oplus \cdots .
$$

In particular, each $f \in L ^ { 2 } ( R )$ can be written uniquely as

$$
f = f _ { 0 } + \sum _ { j = 0 } ^ { \infty } w _ { j }
$$

where $\pmb { f _ { 0 } }$ belongs to $V _ { 0 }$ and ${ \pmb w } _ { j }$ belongs to $W _ { j }$ .

The infinite sum should be thought of as a limit of finite sums. In other words,

$$
f = f _ { 0 } + \operatorname* { l i m } _ { N  \infty } \sum _ { j = 0 } ^ { N } w _ { j }
$$

where the limit is taken in the sense of $L ^ { 2 }$ Although the proof of this result is beyond the scope of this text, some intuition can be given. There are two key ideas. The first is that any function in $L ^ { 2 } ( R )$ can be approximated by continuous functions (for an intuitive explanation of this idea, see Lemma 1.38). The second is that any continuous function can be approximated as closely as desired by a step function whose discontinuities are multiples of $2 ^ { - j }$ for suitably large $\boldsymbol { j }$ (see Figure 11). Such a step function, by definition, belongs to $V _ { j }$ The theorem is then established by putting both ideas together.

![](images/541a4c8beafaed69bfa6b591e30916bd850a39e324e736c98c9bb5b646698658.jpg)  
Figure 11 Approximating by step functions

# 4.3 Haar Decomposition and Reconstruction Algorithms

# 4.3.1 Decomposition

Now that $V _ { j }$ has been decomposed as a direct sum of $V _ { 0 }$ and $W _ { l }$ for $0 \leq l <$ $j$ ,the solution to our noise-fltering problem is theoretically easy. First, we approximate $\pmb { f }$ by a step function $f _ { j } \in V _ { j }$ (for $\pmb { j }$ suitably large) using Theorem 4.9. Then we decompose $f _ { j }$ into its components

$$
f _ { j } = f _ { 0 } + w _ { 1 } + \cdots + w _ { j - 1 } , \quad w _ { l } \in W _ { l } .
$$

The component ${ \pmb w } _ { \pmb { l } }$ represents the spikes $1 / 2 ^ { l + 1 }$ .For l sufficiently large, these spikes are thin enough to represent noise. For example, suppose that spikes of width less than 0.01 represent noise. Since $2 ^ { - 6 } < 0 . 0 1 < 2 ^ { - 7 }$ , any $w _ { j }$ with $j \geq 6$ represents noise. To filter out this noise, these components can be set equal to zero. The rest of the sum represents a signal that is still relatively close to $\pmb { f }$ and that is noise free.

In order to implement this theoretical algorithm, an efficient way of performing the decomposition given in Theorem 4.9 is needed. The first step is to approximate the original signal $\pmb { f }$ by a step function of the form

$$
f _ { j } ( x ) = \sum _ { l \in Z } a _ { l } \phi ( 2 ^ { j } x - l ) .
$$

The procedure is to sample the signal at $\pmb { x } = . ~ . . , - 1 / 2 ^ { j } , 0 , 1 / 2 ^ { j } , . . . ,$ which leads to $a _ { l } = f ( l / 2 ^ { j } )$ for $\iota \in Z$ An illustration of this procedure is given in Figure 11, where $\pmb { f }$ is the continuous signal and $\pmb { f _ { j } }$ is the step function. Here, $\pmb { j }$ is chosen so that the mesh size ${ \mathfrak { z } } ^ { - j }$ is small enough so that $f _ { j } ( x )$ captures the essential features of the signal. The range of $\iota$ depends on the domain of the signal. If the signal is defined on ${ \mathfrak { d } } \leq x \leq 1$ ,then the range of $\iota$ is $0 \leq l \leq 2 ^ { j } - 1$ .In general, we will not specify the range of $\iota$ unless a specific example is discussed.

Now the task is to decompose $\phi ( 2 ^ { j } x - l )$ into its $W _ { t }$ -components for $\iota < j$ The following relations between $\phi$ and $\psi$ are needed:

$$
\begin{array} { r } { \phi ( 2 x ) = ( \psi ( x ) + \phi ( x ) ) / 2 } \\ { \phi ( 2 x - 1 ) = ( \phi ( x ) - \psi ( x ) ) / 2 , } \end{array}
$$

which follow easily by looking at their graphs (see Figures 4 and 10). More generally, we have the following lemma.

LEMMA 4.10 The following relations hold for al ${ \pmb x } \in { \pmb R }$ :

$$
\begin{array} { r l r } { \phi ( 2 ^ { j } x ) } & { = } & { ( \psi ( 2 ^ { j - 1 } x ) + \phi ( 2 ^ { j - 1 } x ) ) / 2 } \\ { \phi ( 2 ^ { j } x - 1 ) } & { = } & { ( \phi ( 2 ^ { j - 1 } x ) - \psi ( 2 ^ { j - 1 } x ) ) / 2 . } \end{array}
$$

This lemma follows by replacing $\pmb { x }$ by ${ \mathfrak { z } } ^ { j - 1 } { \mathfrak { x } }$ in equations (4.4) and (4.5).

This lemma can be used to decompose $\phi ( 2 ^ { j } x - l )$ into its $W _ { t }$ -components for $\iota < j$ An example helps illustrate the process.

# EXAMPLE 4.11

Let $\pmb { f }$ be given by the graph in Figure 12. Notice that the mesh size needed to capture all the features of $\pmb { f }$ is $2 ^ { - 2 }$ A description of $\pmb { f }$ in terms of $\phi ( 2 ^ { 2 } x - l )$ is given by

$$
f ( x ) = 2 \ \phi ( 4 x ) + 2 \phi ( 4 x - 1 ) + \phi ( 4 x - 2 ) - \phi ( 4 x - 3 ) .
$$

We wish to decompose $\pmb { f }$ into its $W _ { 1 } , W _ { 0 }$ ,and $V _ { 0 }$ components. The following equations follow from (4.6)and (4.7)with ${ \dot { \mathcal { I } } } = 2$

$$
\begin{array} { r l } & { \phi ( 4 x ) = ( \psi ( 2 x ) + \phi ( 2 x ) ) / 2 } \\ & { \phi ( 4 x - 1 ) = ( \phi ( 2 x ) - \psi ( 2 x ) ) / 2 } \\ & { \phi ( 4 x - 2 ) = \phi ( 4 ( x - 1 / 2 ) ) = ( \psi ( 2 ( x - 1 / 2 ) ) + \phi ( 2 ( x - 1 / 2 ) ) ) / 2 } \\ & { \phi ( 4 x - 3 ) = \phi ( 4 ( x - 1 / 2 ) - 1 ) = ( \phi ( 2 ( x - 1 / 2 ) - \psi ( 2 ( x - 1 / 2 ) ) ) / 2 . } \end{array}
$$

![](images/83c89b000c128e66352bf6c56a971c9ed3fa9720f820710ab0303d6cfae15c4e.jpg)  
Figure 12 Figure for Example 4.11

Using these equations together with (4.8) and collecting terms yields

$$
\begin{array} { r l } & { f ( x ) = [ \psi ( 2 x ) + \phi ( 2 x ) ] + [ \phi ( 2 x ) - \psi ( 2 x ) ] } \\ & { \qquad + [ \psi ( 2 x - 1 ) + \phi ( 2 x - 1 ) ] / 2 - [ \phi ( 2 x - 1 ) - \psi ( 2 x - 1 ) ] / 2 } \\ & { \qquad = \psi ( 2 x - 1 ) + 2 \phi ( 2 x ) . } \end{array}
$$

The $W _ { 1 }$ -component of $\pmb { f } ( \pmb { x } )$ is $\psi ( 2 x - 1 )$ , since $W _ { 1 }$ is the linear span of . $\{ \psi ( 2 x - k ) ; k \in Z \}$ The $V _ { 1 }$ -component of $\pmb { f } ( \pmb { x } )$ is given by $2 \phi ( 2 x )$ .This component can be further decomposed into a $V _ { 0 }$ -component and a $W _ { \mathbf { 0 } } .$ -component by using the equation $\phi ( 2 x ) = ( \phi ( x ) + \psi ( x ) ) / 2$ The result is

$$
f ( x ) = \psi ( 2 x - 1 ) + \psi ( x ) + \phi ( x ) .
$$

This equation can also be verified geometrically by examining the graphs of the functions involved. The terms in the expression at right are the components of $\pmb { f }$ in $W _ { 1 } , W _ { 0 }$ ,and $V _ { 0 }$ , respectively.

Using this example as a guide, we can proceed with the general decomposition scheme as follows. First divide the sum $\begin{array} { r } { f _ { j } ( x ) = \sum _ { k } a _ { k } \phi ( 2 ^ { j } x - k ) } \end{array}$ into even and odd terms:

$$
f _ { j } ( x ) = \sum _ { k \in Z } a _ { 2 k } \phi ( 2 ^ { j } x - 2 k ) + \sum _ { k \in Z } a _ { 2 k + 1 } \phi ( 2 ^ { j } x - 2 k - 1 ) .
$$

Next, we use (4.6)and 4.7with $\pmb { x }$ replaced by $x - k 2 ^ { 1 - j }$ :

$$
\begin{array} { r } { \phi ( 2 ^ { j } x - 2 k ) = ( \psi ( 2 ^ { j - 1 } x - k ) + \phi ( 2 ^ { j - 1 } x - k ) ) / 2 } \\ { \phi ( 2 ^ { j } x - 2 k - 1 ) = ( \phi ( 2 ^ { j - 1 } x - k ) - \psi ( 2 ^ { j - 1 } x - k ) ) / 2 . } \end{array}
$$

Substituting these expressions into (4.9) yields

$$
\begin{array} { l } { f _ { j } ( x ) = \displaystyle \sum _ { k \in Z } a _ { 2 k } \left( \psi ( 2 ^ { j - 1 } x - k ) + \phi ( 2 ^ { j - 1 } x - k ) \right) / 2 } \\ { \displaystyle \qquad + \sum _ { k \in Z } a _ { 2 k + 1 } \left( \phi ( 2 ^ { j - 1 } x - k ) - \psi ( 2 ^ { j - 1 } x - k ) \right) / 2 } \\ { \displaystyle = \sum _ { k \in Z } \left( \frac { a _ { 2 k } - a _ { 2 k + 1 } } { 2 } \right) \psi ( 2 ^ { j - 1 } x - k ) + \left( \frac { a _ { 2 k } + a _ { 2 k + 1 } } { 2 } \right) \phi ( 2 ^ { j - 1 } x - k ) } \\ { \displaystyle = w _ { j - 1 } + f _ { j - 1 } . } \end{array}
$$

The first term on the right, ${ \pmb w } _ { j - 1 }$ , represents the $W _ { j - 1 }$ -component of $\pmb { f _ { j } }$ since $W _ { j - 1 }$ is, by definition, the linear span of $\{ \psi ( 2 ^ { j - 1 } x - k ) ,$ $k \in Z \}$ .Likewise, the second term on the right, $f _ { j - 1 }$ , represents the $V _ { j - 1 }$ -component of $\pmb { f _ { j } }$ .We summarize the preceding decomposition algorithm in the following theorem.

THEOREM 4.12 (Haar Decomposition) Suppose

$$
f _ { j } ( x ) = \sum _ { k \in Z } a _ { k } ^ { j } \phi ( 2 ^ { j } x - k ) \ \in V _ { j } .
$$

Then $\pmb { f _ { j } }$ can be decomposed as

$$
f _ { j } = w _ { j - 1 } + f _ { j - 1 }
$$

where

$$
\begin{array} { l } { { \displaystyle w _ { j - 1 } = \sum _ { k \in Z } b _ { k } ^ { j - 1 } \psi ( 2 ^ { j - 1 } x - k ) \in W _ { j - 1 } } } \\ { { \mathrm { ~ } } } \\ { { \displaystyle f _ { j - 1 } = \sum _ { k \in Z } a _ { k } ^ { j - 1 } \phi ( 2 ^ { j - 1 } x - k ) \in V _ { j - 1 } } } \end{array}
$$

with

$$
b _ { k } ^ { j - 1 } = \frac { a _ { 2 k } ^ { j } - a _ { 2 k + 1 } ^ { j } } { 2 } \qquad a _ { k } ^ { j - 1 } = \frac { a _ { 2 k } ^ { j } + a _ { 2 k + 1 } ^ { j } } { 2 } .
$$

The preceding process can now be repeated with $\pmb { j }$ replaced by $j - 1$ to decompose $f _ { j - 1 }$ as $w _ { j - 2 } + f _ { j - 2 }$ Continuing in this way, we achieve the decomposition

$$
f _ { j } = w _ { j - 1 } + w _ { j - 2 } + \cdots + w _ { 0 } + f _ { 0 } .
$$

To summarize the decomposition process, a signal is first discretized that produces an approximate signal $f _ { j } \in V _ { j }$ as in Theorem 4.9. Then the decomposition algorithm in Theorem 4.12 produces a decomposition of $\pmb { f _ { j } }$ into its various frequency components: $f _ { j } = w _ { j - 1 } + w _ { j - 2 } + \cdots + w _ { 0 } + f _ { 0 }$ .

![](images/bc9463202427cf966e4617303fce52279782882cda0d6b480a7633543c73e67a.jpg)  
Figure 13 Sample signal

# EXAMPLe 4.13

Consider the signal $\pmb { f }$ defined on the unit interval $\mathbf { 0 } \leq x \leq 1$ given in Figure 13. We discretize this signal over $2 ^ { 8 }$ nodes [so $a _ { k } ^ { 8 } = f ( k / 2 ^ { 8 } )$ , $0 \leq k \leq 2 ^ { 8 } - 1 ]$ since a mesh size of width $1 / 2 ^ { 8 }$ seems to capture the essential features of this signal. Thus

$$
f _ { 8 } ( x ) = \sum _ { k = 0 } ^ { 2 ^ { 8 } - 1 } f ( k / 2 ^ { 8 } ) \phi ( 2 ^ { 8 } x - k )
$$

approximates $\pmb { f }$ well enough for our purposes. Using Theorem 4.12, we decompose $\pmb { f _ { 8 } }$ into its components in $V _ { j }$ , for $j = 8 , 7 , \dots , 0$ Plots of the components in $f _ { 8 } \in V _ { 8 }$ , $f _ { 7 } \in V _ { 7 }$ , $f _ { 6 } \in V _ { 6 }$ ,and $f _ { 4 } \in V _ { 4 }$ are given in Figures 14, 16, 17, and 18 on the following three pages. A plot of the $W _ { 7 }$ -coefficients is given in Figure 15. The $W _ { 7 }$ -coefficients are small except where the original signal contains a sharp spike of width $\approx 2 ^ { - 8 }$ (at $\pmb { x } \approx \mathbf { 0 . 3 }$ and $\begin{array} { r } { x \approx 0 . 6 5 \} } \end{array}$ . •

# 4.3.2 Reconstruction

Having decomposed $\pmb { f }$ into its $V _ { 0 } \mathrm { - }$ and $W _ { j ^ { \prime } }$ -components for $0 \leq j ^ { \prime } < j$ ,then what? The answer depends on the goal. If the goal is to filter out noise, then the $W _ { j ^ { \prime } }$ -components of $\pmb { f }$ corresponding to the unwanted frequencies can be thrown out and the resulting signal will have much less noise. If the goal is data compression, the $W _ { j ^ { \prime } }$ -components that are small can be thrown out without appreciably changing the signal. Only the significant $W _ { j ^ { \prime } }$ -components (the larger $\pmb { b } _ { \pmb { k } } ^ { j ^ { \prime } }$ ) need to be transmitted, and significant data compression can be achieved. Of course, what constitutes "small" depends on the tolerance for error for a particular application.

![](images/f4e6229d8f88542ade1bf05d0dc240be31cbcb4084663ddf2b57e0a7c972c9a8.jpg)  
Figure 14 $V _ { 8 }$ -component

![](images/4415d23de39793ce73dc0dd31193d336d3356e4f8d75412b18f566c7b0e066f2.jpg)  
Figure 15 $W _ { 7 }$ -coefficients

In either case, since the $\boldsymbol { b } _ { \boldsymbol { k } } ^ { j ^ { \prime } }$ have been modified, we need a reconstruction algorithm (for the receiving end of the signal perhaps) so that the compressed or filtered signal can be rebuilt in terms of the basis elements $\phi ( 2 ^ { j } x - l )$ of $V _ { j }$ ;

![](images/87286d047236de7297409f83953a4a73445ed1f7b0a8176ba0b87254f69b91da.jpg)  
Figure 16 $V _ { 7 }$ -component

![](images/69b100a8832c2df3337a00aec92f95870f1e601373546f18f8ec94b9ccb96356.jpg)  
Figure 17 $V _ { 6 }$ -component

that is,

$$
f ( x ) = \sum _ { l \in Z } a _ { l } ^ { j } \phi ( 2 ^ { j } x - l ) .
$$

Once this is done, the graph of the signal $\pmb { f }$ is a step function of height $\pmb { a } _ { l } ^ { j }$ over the interval $l / 2 ^ { j } \le x \le ( l + 1 ) / 2 ^ { j }$ .

![](images/d59357ad69a374411322187c68055259aa8d057c6949764e9f8a299194cd14cd.jpg)  
Figure 18 $V _ { 4 }$ -component

We start with a signal of the form

$$
f ( x ) = f _ { 0 } ( x ) + w _ { 0 } ( x ) + \cdots + w _ { j - 1 } ( x ) \quad w _ { l } \in W _ { l }
$$

where

$$
f _ { 0 } ( x ) = \sum _ { k \in Z } a _ { k } ^ { 0 } \phi ( x - k ) \in V _ { 0 } \quad \mathrm { a n d } \quad w _ { l } = \sum _ { k } b _ { k } ^ { l } \psi ( 2 ^ { l } x - k ) \in W _ { l }
$$

for $0 \leq l \leq j - 1$ Our goal is to rewrite $\pmb { f }$ as $\begin{array} { r } { f ( x ) = \sum _ { l } a _ { l } ^ { j } \phi ( 2 ^ { j } x - l ) } \end{array}$ and find an algorithm for the computation of the constants $\pmb { \alpha } _ { l } ^ { j }$ We use the equations

$$
\begin{array} { c } { { \phi ( x ) = \phi ( 2 x ) + \phi ( 2 x - 1 ) \nonumber } } \\ { { \psi ( x ) = \phi ( 2 x ) - \phi ( 2 x - 1 ) , } } \end{array}
$$

which follow from the definitions of $\phi$ and $\psi$ Replacing $\pmb { x }$ by ${ \mathfrak { z } } ^ { j - 1 } { \mathfrak { x } }$ yields

$$
\begin{array} { c } { { \phi ( 2 ^ { j - 1 } x ) = \phi ( 2 ^ { j } x ) + \phi ( 2 ^ { j } x - 1 ) } } \\ { { \psi ( 2 ^ { j - 1 } x ) = \phi ( 2 ^ { j } x ) - \phi ( 2 ^ { j } x - 1 ) . } } \end{array}
$$

Using equation (4.12) with $\pmb { x }$ replaced by ${ \pmb x } - { \pmb k }$ , we have

$$
\begin{array} { l } { { f _ { 0 } ( x ) = \displaystyle \sum _ { k \in Z } a _ { k } ^ { 0 } \phi ( x - k ) \quad \mathrm { ( t h e ~ d e f i n i t i o n ~ o f ~ } f _ { 0 } ) } } \\ { { \displaystyle \qquad = \sum _ { k \in Z } a _ { k } ^ { 0 } \phi ( 2 x - 2 k ) + a _ { k } ^ { 0 } \phi ( 2 x - 2 k - 1 ) \quad \mathrm { f r o m ~ } ( 4 . 1 2 ) . } } \end{array}
$$

So

$$
f _ { 0 } ( x ) = \sum _ { k \in \mathcal { Z } } \hat { a } _ { l } ^ { 1 } \phi ( 2 x - l )
$$

where

$$
\hat { a } _ { l } ^ { 1 } = \left\{ \begin{array} { l l } { a _ { k } ^ { 0 } } & { \mathrm { i f } l = 2 k \mathrm { ~ i s ~ e v e n } } \\ { a _ { k } ^ { 0 } } & { \mathrm { i f } l = 2 k + 1 \mathrm { ~ i s ~ o d d } . } \end{array} \right.
$$

Similarly, $\begin{array} { r } { w _ { 0 } = \sum _ { k } b _ { k } ^ { 0 } \psi ( x - k ) } \end{array}$ can be written [using equation (4.1) r $\psi ( { \pmb x } - { \pmb k } ) ]$ as

$$
w _ { 0 } ( x ) = \sum _ { l \in \mathcal { Z } } \hat { b } _ { l } ^ { 1 } \phi ( 2 x - l )
$$

where

$$
\hat { b } _ { l } ^ { 1 } = \left\{ \begin{array} { l l } { { b _ { k } ^ { 0 } , } } & { { \mathrm { i f ~ } l = 2 k \mathrm { ~ i s ~ e v e n } } } \\ { { - b _ { k } ^ { 0 } , } } & { { \mathrm { i f ~ } l = 2 k + 1 \mathrm { ~ i s ~ o d d } } } \end{array} \right.
$$

Combining (4.16) and (4.17) yields

$$
f _ { 0 } ( x ) + w _ { 0 } ( x ) = \sum _ { l \in Z } a _ { l } ^ { 1 } \phi ( 2 x - l )
$$

where

$$
a _ { l } ^ { 1 } = \hat { a } _ { l } ^ { 1 } + \hat { b } _ { l } ^ { 1 } = \left\{ \begin{array} { l l } { a _ { k } ^ { 0 } + b _ { k } ^ { 0 } , } & { \mathrm { i f } \ l = 2 k } \\ { a _ { k } ^ { 0 } - b _ { k } ^ { 0 } , } & { \mathrm { i f } \ l = 2 k + 1 . } \end{array} \right.
$$

Next, $\begin{array} { r } { w _ { 1 } = \sum _ { k } b _ { k } ^ { 1 } \psi ( 2 x - k ) } \end{array}$ is added to this sum in the same manner [using 4.12) and (4.13) with $\pmb { x }$ replaced by $2 x - k ]$ :

$$
f _ { 0 } ( x ) + w _ { 0 } ( x ) + w _ { 1 } ( x ) = \sum _ { l \in Z } a _ { l } ^ { 2 } \phi ( 2 ^ { 2 } x - l )
$$

where

$$
a _ { l } ^ { 2 } = { \left\{ \begin{array} { l l } { a _ { k } ^ { 1 } + b _ { k } ^ { 1 } , } & { { \mathrm { i f ~ } } l = 2 k } \\ { a _ { k } ^ { 1 } - b _ { k } ^ { 1 } , } & { { \mathrm { i f ~ } } l = 2 k + 1 . } \end{array} \right. }
$$

Note that the $\pmb { a } _ { l } ^ { 0 } .$ and $b _ { l } ^ { 0 }$ -coefficients determine the $\pmb { a } _ { l } ^ { 1 }$ -coefficients. Then the $a _ { l } ^ { 1 } -$ and $b _ { l } ^ { 1 }$ -coefficients determine the $\pmb { a } _ { l } ^ { 2 }$ -coefficients, and so on in a recursive manner.

The preceding reconstruction algorithm is summarized in the following theorem.

THEOREM 4.14 (Haar Reconstruction) Suppose

$$
f = f _ { 0 } + w _ { 0 } + w _ { 1 } + w _ { 2 } + \cdots + w _ { j - 1 }
$$

with

$$
f _ { 0 } ( x ) = \sum _ { k \in Z } a _ { k } ^ { 0 } \phi ( x - k ) \in V _ { 0 } \quad a n d \quad w _ { j ^ { \prime } } ( x ) = \sum _ { k \in Z } b _ { k } ^ { j ^ { \prime } } \psi ( 2 ^ { j ^ { \prime } } x - k ) \in W _ { j ^ { \prime } }
$$

for $\mathbf { 0 } \leq j ^ { \prime } < j$ Then

$$
f ( x ) = \sum _ { l \in Z } a _ { l } ^ { j } \phi ( 2 ^ { j } x - l ) \in V _ { j }
$$

where the $\pmb { a } _ { l } ^ { j ^ { \prime } }$ are determined recursively for ${ \dot { \mathcal { I } } } ^ { \prime } = 1$ , then ${ \dot { \pmb { \jmath } } } ^ { \prime } = { \bf 2 }$ , and so on until ${ \dot { \pmb { \jmath } } } ^ { \prime } = { \dot { \pmb { \jmath } } }$ , by the algorithm

$$
a _ { l } ^ { j ^ { \prime } } = \left\{ \begin{array} { l l } { { a _ { k } ^ { j ^ { \prime } - 1 } + b _ { k } ^ { j ^ { \prime } - 1 } , } } & { { i f l = 2 k \ i s \ e v e n } } \\ { { } } & { { } } \\ { { a _ { k } ^ { j ^ { \prime } - 1 } - b _ { k } ^ { j ^ { \prime } - 1 } , } } & { { i f l = 2 k + 1 \ i s \ o d d . } } \end{array} \right.
$$

# EXAMPLE 4.15

We apply the decomposition and reconstruction algorithms to compress the signal $\pmb { f }$ that is shown in Figure 19; $\pmb { f }$ is defined on the unit interval. (This is the same signal used in Example 4.13.)

We discretize this signal over $2 ^ { 8 }$ nodes [so $\alpha _ { k } ^ { 8 } = f ( k / 2 ^ { 8 } ) ]$ and then decompose this signal (as in Theorem 4.12) to obtain $f = f _ { 0 } + w _ { 0 } + w _ { 1 } + w _ { 2 } + \cdots + w _ { 7 }$ with

$$
f _ { 0 } ( x ) = a _ { 0 } ^ { 0 } \phi ( x ) \in V _ { 0 } \mathrm { a n d } w _ { j ^ { \prime } } ( \dot { x } ) = \sum _ { k \in Z } b _ { k } ^ { j ^ { \prime } } \psi ( 2 ^ { j ^ { \prime } } x - k ) \in W _ { j ^ { \prime } }
$$

![](images/b362e28af57e58e4367f2f1e6868f4d18d2dcf5dc88df54cf91ff3a8503fecfb.jpg)  
Figure 19 Sample signal

for $0 \leq j ^ { \prime } \leq 7$ Note that there is only one basis term $\phi ( { \pmb x } )$ in $V _ { 0 }$ since the interval of consideration is ${ \mathbf 0 } \le x \le { \mathbf 1 }$ We first use $8 5 \%$ compression on this decomposed signal, which means that after ordering the $| \pmb { \theta } _ { \pmb { k } } ^ { j } |$ by size, we set the smallest $8 0 \%$ equal to zero (retaining the largest $2 0 \%$ .Then we reconstruct the signal as in Theorem 4.14. The result is graphed in Figure 20. Figure 21 illustrates the same process with $9 0 \%$ compression. The relative $L ^ { 2 }$ -error is 0.0895 for $80 \%$ compression and 0.1838 for $9 0 \%$ compression. -

![](images/217a9fa153baeddb2717ae3975fd380a054f15c5f8318782131a168acd5c109d.jpg)  
Figure 20 Eighty percent compression

![](images/228d1d3d161d453bfdc6292e3a40043fb667ffdd695a36cbe1340a82c242b917.jpg)  
Figure 21 Ninety percent compression

# 4.3.3 Filters and Diagrams

The decomposition and reconstruction algorithms can be put in the language of discrete filters and simple operators acting on a sequence of coefficients. The algorithms can then be visualized in terms of block diagrams.

We do the decomposition algorithm first. Define two discrete filters (convolution operators) $\pmb { H }$ and $\pmb { L }$ via their impulse responses, which are the sequences $\pmb { h }$ and $\ell$

$$
h = ( \cdots 0 \cdots \underbrace { { \frac { 1 } { 2 } } \quad { \frac { 1 } { 2 } } } _ { k = - 1 , 0 } \cdots 0 \cdots ) , \qquad \ell = ( \cdots 0 \cdots \underbrace { { \frac { 1 } { 2 } } \quad { \frac { 1 } { 2 } } } _ { k = - 1 , 0 } \cdots 0 \cdots ) .
$$

If $\{ x _ { k } \} \in \ell ^ { 2 }$ , then $H ( x ) : = h * x$ and $L ( x ) : = \ell * x$ The resulting sequences are thus

$$
H ( x ) _ { k } = ( h * x ) _ { k } = \frac 1 2 x _ { k } - \frac 1 2 x _ { k + 1 } \qquad L ( x ) _ { k } = ( \ell * x ) _ { k } = \frac 1 2 x _ { k } + \frac 1 2 x _ { k + 1 } .
$$

If we keep only even subscripts, then $\begin{array} { r } { H ( x ) _ { 2 k } = ( h * x ) _ { 2 k } = \frac 1 2 x _ { 2 k } - \frac 1 2 x _ { 2 k + 1 } } \end{array}$ and $L ( x ) _ { 2 k } = ( \ell * x ) _ { 2 k } = { \textstyle { \frac { 1 } { 2 } } } x _ { 2 k } + { \textstyle { \frac { 1 } { 2 } } } x _ { 2 k + 1 }$ .This operation of discarding the odd coefficients in a sequence is called downsampling; we denote the corresponding operator by $\pmb { D }$ .

We now apply these ideas to go from level $\pmb { j }$ scaling coefficients $a _ { k } ^ { j }$ to get the level ${ \dot { \jmath } } - 1$ scaling and wavelet coefficients. Using Theorem 4.12 and replacing $\pmb { x }$ by $a _ { k } ^ { j }$ ,

$$
b _ { k } ^ { j - 1 } = D H ( a ^ { j } ) _ { k } \quad \mathrm { a n d } \quad a _ { k } ^ { j - 1 } = D L ( a ^ { j } ) _ { k } .
$$

Figure 22 illustrates the decomposition algorithm. The downsampling operator $D$ is replaced by the more suggestive symbol, $( 2 )$ ."

![](images/730dbd41e6c4bbd8dbfde4b769498c61781eb0276a5e949c1f4614bae73e1ab1.jpg)  
Figure 22 Haar decomposition diagram

The reconstruction algorithm also requires defining two discrete filters $\widetilde { H }$ and $\widetilde { L }$ via their corresponding impulse responses,

$$
\widetilde { h } = ( \cdots \cdot 0 \cdots \underbrace { 1 - 1 } _ { k = 0 , 1 } \cdots \cdot 0 \cdots ) \qquad \widetilde { \ell } = ( \cdots \cdot 0 \cdots \underbrace { 1 } _ { k = 0 , 1 } \cdots \cdot 0 \cdots ) .
$$

For a sequence $\{ \pmb { x } _ { k } \}$ ,we have $( \widetilde { h } * x ) _ { k } = x _ { k } - x _ { k - 1 }$ and $( \widetilde { \ell } * x ) _ { k } = x _ { k } + x _ { k - 1 }$ . Here is an important observation. If $\pmb { x }$ and $\pmb { y }$ are sequences in which the odd entries are all 0, then

$$
( \widetilde { h } * x ) _ { l } = \left\{ \begin{array} { l l } { x _ { 2 k } } & { l = 2 k \mathrm { ~ i s ~ e v e n } , } \\ { - x _ { 2 k } } & { l = 2 k + 1 \mathrm { ~ i s ~ o d d } , } \end{array} \right. \quad ( \widetilde { \ell } * y ) _ { l } = \left\{ \begin{array} { l l } { y _ { 2 k } } & { l = 2 k \mathrm { ~ i s ~ e v e n } , } \\ { y _ { 2 k } } & { l = 2 k + 1 \mathrm { ~ i s ~ o d d } } \end{array} \right.
$$

Adding the two sequences $\widetilde { h } * x$ and $\widetilde { \ell } * y$ then gives us

$$
( \widetilde { h } * x ) _ { l } + ( \widetilde { \ell } * y ) _ { l } = \left\{ \begin{array} { l l } { x _ { 2 k } + y _ { 2 k } } & { l = 2 k \mathrm { ~ i s ~ e v e n } , } \\ { y _ { 2 k } - x _ { 2 k } } & { l = 2 k + 1 \mathrm { ~ i s ~ o d d } . } \end{array} \right.
$$

This is almost the pattern for the reconstruction formula given in Theorem 4.14. Although we have assumed that the $x _ { 2 k + 1 } \cdot \mathbf { s }$ and ${ \bf { y } } _ { 2 k + 1 }$ 's are 0, the $\pmb { x _ { 2 k } } ^ { \prime } \mathbf { s }$ and $y _ { 2 k } \mathbf { ^ { \prime } s }$ a ours to coose, so $x _ { 2 k } = b _ { k } ^ { j - 1 }$ and $y _ { 2 k } = a _ { k } ^ { j - 1 }$ ;that is,

$$
x = ( \cdots 0 b _ { - 1 } ^ { j - 1 } 0 \underbrace { b _ { 0 } ^ { j - 1 } } _ { k = 0 } 0 b _ { 1 } ^ { j - 1 } 0 b _ { 2 } ^ { j - 1 } 0 \cdots )
$$

and similarly for $\pmb { y }$ . The sequences $\pmb { x }$ and $\pmb { y }$ are called upsamples of the sequences $\pmb { b ^ { j - 1 } }$ and ${ \pmb { a } } ^ { j - 1 }$ We use the $\pmb { U }$ to denote the upsampling operator, so ${ \pmb x } = { \pmb U } { \pmb b } ^ { j - 1 }$ . and $\begin{array} { r } { { \pmb y } = U { \pmb a } ^ { j - 1 } } \end{array}$ . The reconstruction formula in Theorem 4.14 then takes the compact form

$$
a ^ { j } = \widetilde { L } U a ^ { j - 1 } + \widetilde { H } U b ^ { j - 1 } .
$$

We illustrate the reconstruction step in Figure 23. The upsampling operator is replaced by the symbol $2 \uparrow$ .

![](images/2014986414d8b80d572c3f07e074b0548f103433bf41c81e004b4cac56b07b8f.jpg)  
Figure 23 Haar reconstruction diagram

# 4.4 Summary

In this section, we present a summary of the ideas of this chapter. The format is a step-by-step procedure used to process (compress or denoise) given signal ${ \boldsymbol { y } } = { \boldsymbol { f } } ( t )$ .We will let $\phi$ and $\psi$ be the Haar scaling function and wavelet.

Step 1. Sample. If the signal is continuous (analog), $y = f ( t )$ , where $\pmb { t }$ represents time, choose the top level ${ \dot { \pmb { \jmath } } } = { \pmb { J } }$ so that $2 ^ { J }$ is larger than the Nyquist rate for the signal (see the discussion just before the Theorem 2.23). Let

$$
\begin{array} { r } { \alpha _ { \pmb { k } } ^ { J } = f ( \pmb { k } / 2 ^ { J } ) . } \end{array}
$$

In practice, the range of $\pmb { k }$ is a finite interval determined by the duration of the signal. For example, if the duration of the signal is $0 \leq t \leq 1$ ,then the range for $\pmb { k }$ is $0 \leq k \leq 2 ^ { J } - 1$ (or perhaps $1 \leq l \leq 2 ^ { J }$ ).If the signal is discrete to start with (i.e., a sequence of numbers), then this step is unnecessary. The top level $\pmb { a } _ { \pmb { k } } ^ { J }$ is set equal to the kth term in the sampled signal, and $2 ^ { J }$ is taken to be the sampling rate. In any case, we have the highest-level approximation to $\pmb { f }$ given by

$$
f _ { J } ( x ) = \sum _ { k \in Z } a _ { k } ^ { J } \phi ( 2 ^ { J } x - k )
$$

Step 2. Decomposition. The decomposition algorithm decomposes $\pmb { f } _ { J }$ into

$$
f _ { J } = w _ { J - 1 } + \cdots + w _ { j - 1 } + f _ { j - 1 } + \cdots + w _ { 0 } + f _ { 0 } ,
$$

where

$$
\begin{array} { l } { { \displaystyle w _ { j - 1 } = \sum _ { l \in Z } b _ { l } ^ { j - 1 } \psi ( 2 ^ { j - 1 } x - l ) } } \\ { { \displaystyle f _ { j - 1 } = \sum _ { l \in Z } a _ { l } ^ { j - 1 } \phi ( 2 ^ { j - 1 } x - l ) . } } \end{array}
$$

The coefficients $\boldsymbol { b } _ { l } ^ { j - 1 }$ and $\pmb { a } _ { l } ^ { j - 1 }$ are determined from the $\pmb { a } ^ { j }$ recursively by the algorithm

$$
\begin{array} { r } { a _ { l } ^ { j - 1 } = D L ( a ^ { j } ) _ { k } } \\ { b _ { l } ^ { j - 1 } = D H ( a ^ { j } ) _ { k } } \end{array}
$$

where $\pmb { H }$ and $\pmb { L }$ are the high- and low-pass filters from Section 4.3.3. When j = J, a1}\$ and $b _ { k } ^ { J - 1 }$ are determined by $\pmb { a } _ { \pmb { k } } ^ { J }$ which are the sampled signal values from Step 1. Then $\pmb { j }$ becomes ${ \pmb J } - { \pmb 1 }$ and $a _ { k } ^ { J - 2 }$ and $b _ { k } ^ { J - 2 }$ are determined frome $a _ { k } ^ { J - 1 }$ Then $\pmb { j }$ bcomes ${ \pmb J } - { \pmb 2 }$ satisfactory for some purpose or there are too few coefficients to continue. Unless otherwise stated, the decomposition algorithm will continue until the ${ \dot { \pmb { \jmath } } } = { \bf 0 }$ level is reached.

Step 3. Processing. After decomposition, the signal is in the form

$$
\begin{array} { l } { { \displaystyle f _ { J } ( x ) = \sum _ { j = 0 } ^ { J - 1 } w _ { j } + f _ { 0 } } } \\ { { \displaystyle \quad = \sum _ { j = 0 } ^ { J - 1 } \left( \sum _ { k \in Z } b _ { l } ^ { j } \psi ( 2 ^ { j } x - k ) \right) + \sum _ { k \in Z } a _ { k } ^ { 0 } \phi ( x - k ) . } } \end{array}
$$

The signal can now be filtered by modifying the wavelet coefficients $\boldsymbol { b } _ { \boldsymbol { k } } ^ { j }$ How this is to be done depends on the problem at hand. To filter out all high frequencies, all the $\pmb { b } _ { \pmb { k } } ^ { j }$ would be set to zero for $j$ above a certain value. Perhaps only a certain segment of the signal corresponding to particular values of $\pmb { k }$ is to be filtered. If data compression is the goal, then the $\boldsymbol { b } _ { \boldsymbol { k } } ^ { j }$ that are below a certain threshold (in absolute value) would be set to zero. Whatever the goal, the process modifies the $\pmb { b } _ { \pmb { k } } ^ { j }$

Step 4. Reconstruction. Now the goal is to take the modified signal, $\scriptstyle f _ { J }$ , in the form (4.21) (with the modified $\mathcal { V } _ { \pmb { k } } ^ { j }$ ) and reconstruct it as

$$
f _ { J } = \sum _ { k \in \cal Z } a _ { k } ^ { J } \phi ( 2 ^ { J } x - k ) .
$$

This is accomplished by the reconstruction algorithm discussed in Section 4.3.3:

$$
a ^ { j } = \widetilde { L } U a ^ { j - 1 } + \widetilde { H } U b ^ { j - 1 }
$$

for ${ \mathfrak { j } } = 1 , \ldots J$ When $j = 1$ , the $a _ { k } ^ { 1 }$ are computed from the $\pmb { a } _ { k } ^ { 0 }$ and $b _ { \pmb { k } } ^ { 0 }$ When $j = 2$ the $a _ { k } ^ { 2 }$ are computed from the $\pmb { a } _ { \pmb { k } } ^ { 1 }$ and $b _ { k } ^ { 1 }$ and so forth. The range of $\pmb { k }$ is determined by the time duration of the signal. When $j = J$ (the top level), $a _ { k } ^ { J }$ represents the approximate value of the processed signal at time $\scriptstyle x = k / 2 ^ { J }$ . Of course, these $\pmb { a } _ { \pmb { k } } ^ { J }$ are different from the original $\pmb { a } _ { \pmb { k } } ^ { J }$ due the modification of coefficients in Step 3.

# 4.5 Exercises

1. Let $\phi$ and $\psi$ be the Haar scaling and wavelet functions, respectively. Let $V _ { j }$ and $W _ { j }$ be the spaces generated by $\phi ( 2 ^ { j } x - k )$ , $\pmb { k } \in \pmb { Z }$ and $\psi ( 2 ^ { j } x - k )$ $\pmb { k } \in \pmb { Z }$ , respectively. Consider the function defined on $\mathbf { 0 } \leq x < 1$ given by

$$
f ( x ) = \left\{ \begin{array} { l l } { - 1 } & { 0 \leq x < 1 / 4 } \\ { 4 } & { 1 / 4 \leq x < 1 / 2 } \\ { 2 } & { 1 / 2 \leq x < 3 / 4 } \\ { - 3 } & { 3 / 4 \leq x < 1 . } \end{array} \right.
$$

Express $\pmb { f }$ first in terms of the basis for $V _ { 2 }$ and then decompose $\pmb { f }$ into its component parts in $W _ { 1 } , W _ { 0 }$ , and $V _ { 0 }$ In other words, find the Haar wavelet decomposition for $\pmb { f }$ Sketch each of these.

2. Repeat Exercise 1 for the function

$$
f ( x ) = \left\{ \begin{array} { l l } { 2 } & { 0 \leq x < 1 / 4 } \\ { - 3 } & { 1 / 4 \leq x < 1 / 2 } \\ { 1 } & { 1 / 2 \leq x < 3 / 4 } \\ { 3 } & { 3 / 4 \leq x < 1 . } \end{array} \right.
$$

3. If $\pmb { A }$ and $\pmb { B }$ are finite-dimensional, orthogonal subspaces of an inner product space $\pmb { V }$ , then show

$$
\dim ( A \oplus B ) = \dim A + \dim B .
$$

If $\pmb { A }$ and $\pmb { B }$ are not necessarily orthogonal, then what is the relationship between $\dim ( A + B )$ , dim A and dim $\pmb { B ? }$

4.(a) Let $V _ { n }$ be the spaces generated by $\phi ( 2 ^ { n } x - k )$ $\textbf { \em k } \in \textbf { \em Z }$ ,where $\phi$ is the Haar scaling function. On the interval $0 \leq x < 1$ ,what are the dimensions of the spaces $V _ { n }$ and $W _ { n }$ for $\pmb { n } \geq \mathbf { 0 }$ (just count the number of basis elements)?

Using the result of Exercise 3, count the dimension of the space on the right side of the equality

$$
V _ { n } = W _ { n - 1 } \oplus W _ { n - 2 } \oplus \cdots \oplus W _ { 0 } \oplus V _ { 0 } .
$$

Is your answer the same as the one you computed for $\dim V _ { n }$ in part (a)?

5. Let $\phi$ and $\psi$ be the Haar scaling and wavelet functions, respectively. Let $V _ { j }$ and $W _ { j }$ be the spaces generated by $\phi ( 2 ^ { j } x - k )$ , $\pmb { k } \in \pmb { Z }$ and $\psi ( 2 ^ { j } x - k )$ , $\pmb { k } \in \pmb { Z }$ , respectively. Suppose $\begin{array} { r } { f ( x ) = \sum _ { k } a _ { k } \phi ( 2 x - k ) \left( a _ { k } \in R \right) } \end{array}$ belongs to $V _ { 1 }$ .Show explicitly that if $\pmb { f }$ is orthogonal to each basis element $\phi ( { \boldsymbol { x } } - { \boldsymbol { l } } ) \in V _ { 0 }$ for all integers $\iota$ , then $a _ { 2 1 + 1 } = - a _ { 2 1 }$ for all integers $\iota$ and hence show that

$$
f ( x ) = \sum _ { l \in Z } a _ { 2 l } \psi ( x - l ) \in W _ { 0 } .
$$

6.Reconstruct $\pmb { \mathscr { g } } \in V _ { 3 }$ given these coefficients in its Haar wavelet decomposition:

$$
a ^ { 2 } = [ 1 / 2 , 2 , 5 / 2 , - 3 / 2 ] \quad b ^ { 2 } = [ - 3 / 2 , - 1 , 1 / 2 , - 1 / 2 ] .
$$

The first entry in each list corresponds to $\pmb { k } = \mathbf { 0 }$ Sketch $\pmb { \mathscr { g } }$ .

7.Reconstruct $h \in V _ { 3 }$ given these coefficients in its Haar wavelet decomposition:

$$
a ^ { 1 } = [ 3 / 2 , - 1 ] \quad b ^ { 1 } = [ - 1 , - 3 / 2 ] \quad b ^ { 2 } = [ - 3 / 2 , - 3 / 2 , - 1 / 2 , - 1 / 2 ] .
$$

The first entry in each list corresponds to $\pmb { k } = \mathbf { 0 }$ Sketch $\pmb { h }$ .

The remaining problems require some programming in a language such as MATLAB, Maple, or $c$ , The code in Appendix $\pmb { B }$ entitled 'Matlab Code' should be useful.

8. (Haar wavelets on [0, 1].) Let $\pmb { n }$ be an integer, and let $\pmb { f }$ be a function continuous on [0, 1]. Let $h _ { k } ( t ) = \sqrt { n } \phi ( n t - k )$ , where $\phi ( t )$ is the Haar scaling

function, which is 1 for $\pmb { t }$ in [0, 1) and 0 otherwise, form the projection of $\pmb { f }$ onto the span of the $h _ { k } { } ^ { \prime } { \mathbf { s } } ,$

$$
f _ { n } = \langle f , h _ { 0 } \rangle h _ { 0 } + \cdots + \langle f , h _ { n - 1 } \rangle h _ { n - 1 } .
$$

Show that $f _ { n }$ converges uniformly to $\pmb { f }$ on [0, 1]. For $f ( t ) = 1 - t ^ { 2 }$ ,use MATLAB or Maple to find the Haar wavelet decomposition (on [0, 1]) for $n = 4 , 8 ,$ ,and 16. Plot the results.

9. Let

$$
f ( t ) = e ^ { - t ^ { 2 } / 1 0 } \left( \sin ( 2 t ) + 2 \cos ( 4 t ) + 0 . 4 \sin ( t ) \sin ( 5 0 t ) \right) .
$$

Discretize the function $\pmb { f }$ over the interval $0 \leq t \leq 1$ as described in Step 1 of Section 4.4. Use $\pmb { n } = \pmb { 8 }$ as the top level (so there are $2 ^ { 8 }$ nodes in the discretization). Implement the decomposition algorithm described in Step 2 of Section 4.4 using the Haar wavelets. Plot the resulting levels, $f _ { j - 1 } \in V _ { j - 1 }$ for $j = 8 \dots 1$ , and compare with the original signal.

10. (Continuation of Exercise 9). Filter the wavelet coefficients computed in Exercise 9 by setting to zero any wavelet coefficient whose absolute value is less than $t o l = 0 . 1$ . Then reconstruct the signal as described in Section 4.4. Plot the reconstructed $f _ { 8 }$ and compare with the original signal. Compute the relative $\ell ^ { 2 }$ -difference between the original signal and the compressed signal. Experimnent with various tolerances. Keep track of the percentage of wavelet coefficients that have been filtered out.

11. Haar wavelets can be used to detect a discontinuity in a signal. Let $\pmb { g } ( t )$ be defined on $\mathbf { 0 } \leq t < 1$ via

$$
g ( t ) = \left\{ \begin{array} { l l } { { 0 } } & { { 0 \leq t < 7 / 1 7 \mathrm { ~ \small ~ \alpha ~ } } } \\ { { 1 - t ^ { 2 } } } & { { 7 / 1 7 \leq t < 1 . } } \end{array} \right. \ .
$$

Discretize the functions $\pmb { \mathscr { s } }$ over the interval $0 \leq t \leq 1$ as described in Step 1 of Section 4.4. Use $\pmb { n } = \pmb { 7 }$ as the top level (so there are $\mathbf { 2 7 }$ nodes in the discretization). Implement a one-level decomposition. Plot the magnitudes of the level 6 wavelet coefficients. Which wavelet has the largest coefficient? What t corresponds to this wavelet? Try the method again with $7 / 1 7$ relaced by $8 / 9$ ,and then by $\mathbf { 2 / 7 }$ Why do you think the method works?

# Chapter 5

# Multiresolution Analysis

In the previous chapter, we described a procedure for decomposing a signal into its Haar wavelet components of varying frequencies (see Theorem 4.12). The Haar wavelet scheme relied on two functions: the Haar scaling function $\phi$ and the Haar wavelet $\psi$ .Both are simple to describe and lead to an easy decomposition algorithm. The drawback with the Haar decomposition algorithm is that both of these functions are discontinuous $\cdot \phi$ at ${ \pmb x } = { \pmb 0 }$ ,1 and $\psi$ at $\pmb { x } = 0 , 1 / 2 , 1$ . As a result, the Haar decomposition algorithm provides only crude approximations to a continuously varying signal (as already mentioned, Figure 3 in Chapter 4 does not approximate Figure 2 in Chapter 4 very well). What is needed is a theory similar to what has been described in the past sections but with continuous versions of our building blocks, $\phi$ and $\psi$ In this chapter, we present a framework for creating more general $\phi$ and $\psi$ The resulting theory, due to Stéphane Mallat [10, 11], is called a multiresolution analysis. In the sections that follow, this theory will be used together with a continuous $\phi$ and $\psi$ (to be constructed later) that will improve the performance of the signal decomposition algorithm with the Haar wavelets described in the past section.

# 5.1 The Multiresolution Framework

# 5.1.1 Definition

Before we define the notion of a multiresolution analysis, we need to provide some background. Recall that the sampling theorem (Theorem 2.23) approximately reconstructs a signal $\pmb { f }$ from samples taken uniformly at intervals of length $_ { \pmb { T } }$ If the signal is band limited and its Nyquist frequency is less than ${ \mathbf { 1 } } / { T }$ , then the reconstruction is perfect; otherwise it's an approximation. The smaller $_ { \pmb { T } }$ is, the better we can approximate or resolve the signal; the size of $_ { \pmb { T } }$ measures our resolution of the signal $\pmb { f }$ A typical FFT analysis of the samples taken from $\pmb { f }$ works at one resolution. $\pmb { T }$ .

If the signal has bursts where it varies rapidly, interspersed with periods where it is slowly varying, this "single" resolution analysis does not work well— for all the reasons that we outlined earlier in Section 4.1. To treat such signals, Mallat had the idea to do these two things. First, replace the space of bandlimited functions from the sampling theorem with one tailored to the signal. Second, analyze the signal using the scaled versions of the same space, but geared to resolutions $\scriptstyle { T / 2 , T / 2 ^ { 2 } }$ , and so on (hence the term multiresolution analysis). This framework is ideal for not only analyzing certain signals, but also for actually creating wavelets.

We start with the general definition of a multiresolution analysis.

DEfinitioN 5.1 Let $V _ { j }$ $\mathit { \Psi } _ { j } ^ { \prime } , \mathit { \Pi } , j = . . . , - 2 , - 1 , 0 , 1 , 2 , . . .$ be a sequence of subspaces of functions in $L ^ { 2 } ( R )$ . The collection of spaces $\{ V _ { j } , j \in Z \}$ is called $\pmb { a }$ multiresolution analysis with scaling function $\phi$ if the following conditions hold:

1. (nested) $V _ { j } \subset V _ { j + 1 }$

2. (density) $\overline { { \sqcup V _ { j } } } = L ^ { 2 } ( R )$

3. (separation) $\cap V _ { j } = \{ 0 \}$

4.(scaling) The function $\pmb { f } ( \pmb { x } )$ belongs to $V _ { j }$ if and only if the functon $f ( 2 ^ { - j } x )$ belongs to $V _ { 0 }$ .

5. (orthonormal basis) The function $\phi$ belongs to $V _ { 0 }$ and the set $\{ { \phi } ( { \pmb x } - { \pmb k } ) , { \pmb k } \in \}$ $z \}$ is an orthonormal basis (using the $L ^ { 2 }$ inner product) for $V _ { 0 }$ .

The $V _ { j }$ 's are call approximation spaces. There may be several choices of $\phi$ corresponding to a system of approximation spaces. Different choices for $\phi$ may yield different multiresolution analyses. Although we required the translates of $\phi ( x )$ to be orthonormal, we don't have to. All that is needed is a $\phi$ for which the set $\{ \phi ( x - k ) , k \in Z \}$ is a basis. We can then use $\phi$ to obtain a new scaling function $\tilde { \phi }$ for which $\{ \tilde { \phi } ( x - k ) , k \in Z \}$ is orthonormal. We discuss this in Section 5.3.

Probably the most useful class of scaling functions are those that have compact or finite support. As defined in the previous chapter, a function has compact support if it is identically 0 outside of a finite interval. The Haar scaling function is a good example of a compactly supported function. The scaling functions associated with Daubechies's wavelets are not only compactly supported, but also continuous. Having both properties in a scaling function is especially desirable, because the associated decomposition and reconstruction algorithms are computationally faster and do a better job of analyzing and reconstructing signals.

# EXAMPle 5.2

The Haar scaling function (Definition 4.1) generates the subspaces, $V _ { j }$ ,consisting of the space of piecewise constant functions of finite support (i.e., step functions) whose discontinuities are contained in the set of integer multiples of $2 ^ { - j }$ (see Definition 4.4). We now verify that this collection $\{ V _ { j } , j \geq 0 \}$ together with the Haar scaling function, $\phi ,$ ,satisfies the definition of a multiresolution analysis.

As mentioned just after Definition 4.4, the nested property follows since the set of multiples of $2 ^ { - j }$ is contained in the set of multiples of $2 ^ { - ( j + 1 ) }$ (the former set consists of every other member of the latter set). Intuitively, an approximation of a signal by a function in $V _ { j }$ is capable of capturing details of the signal down to a resolution of $2 ^ { - j }$ The nested property indicates that as $\dot { \boldsymbol { \mathscr { I } } }$ gets larger, more information is revealed by an approximation of a signal by a function in $V _ { j }$ .

The density condition for the Haar system is the content of Theorem 4.9. This condition means that an approximation of a signal by a function in $V _ { j }$ eventually captures all details of the signal as $\dot { \jmath }$ gets larger (i.e., as $j \to \infty$ . This approximation is illustrated in Figure 11.

To discuss the separation condition, first note that $\dot { \pmb { \mathscr { I } } }$ can be negative as well as positive in the definition of $V _ { j }$ .If $\pmb { f }$ belongs to $V _ { - j }$ , for ${ \dot { \mathbf { \eta } } } _ { 3 } > \mathbf { 0 }$ , then $\pmb { f }$ must be a finite linear combination of $\{ \phi ( x / 2 ^ { j } - k ) , k \in Z \}$ whose elements are constant on the intervals $\cdots , [ - 2 ^ { j } , 0 )$ ,[0,2),.... As $\pmb { j }$ gets larger, these intervals get larger. On the other hand, the support of $\pmb { f }$ (i.e., the set where $\pmb { f }$ is nonzero) must stay finite. So if $\pmb { f }$ belongs to all the $V _ { - j }$ as $j \to \infty$ , then these constant values of $\pmb { f }$ must be zero.

Finally, the scaling condition for the Haar system follows from Theorem 4.5 and the orthonormal condition follows from Theorem 4.6. Therefore, the Haar system of $\{ V _ { j } \}$ satisfies all the properties of a multiresolution analysis. •

# EXAMPLE 5.3

Linear Spline Multiresolution Analysis Linear splines are continuous, piecewise linear functions; the jagged function in Figure 1 is an example of one.

We can construct a multiresolution analysis for linear splines. Let $V _ { j }$ be the space of all finite energy signals $\pmb { f }$ that are continuous and piecewise linear, with

![](images/3f10127619320a54acfab396bc000553b1eca0103982fda81676618bbf75b406.jpg)  
Figure 1 A linear spline

possible corners occurring only at the dyadic points $k / 2 ^ { j }$ , $\pmb { k } \in \pmb { Z }$ These approximation spaces satisfy the conditions 1-4 in the definition of a multiresolution analysis (see Exercise 9). The scaling function $\varphi$ is the "tent function,"

$$
\varphi ( x ) = { \left\{ \begin{array} { l l } { x + 1 , } & { - 1 \leq x \leq 0 , } \\ { 1 - x , } & { 0 < x \leq 1 , } \\ { 0 , } & { | x | > 1 . } \end{array} \right. }
$$

and the set $\{ \varphi ( x - k ) \} _ { k \in Z }$ is a nonorthogonal one. Using the methods in Section 5.3, we can construct a new scaling function $\phi$ that does generate an orthonormal basis for $V _ { 0 }$ .

# EXample 5.4

Shannon Multiresolution Analysis For $j \in Z$ , let $V _ { j }$ be the space of all finite energy signals $\pmb { f }$ for which the Fourier transform $\widehat { f } = 0$ outside of the interval $[ - 2 ^ { j } \pi , 2 ^ { j } \pi ]$ —that is, all $f \in L ^ { 2 } ( R )$ that are band limited and have $\mathbf { s u p p } ( \widehat { f } ) \subseteq [ - 2 ^ { j } \pi , 2 ^ { j } \pi ]$ The scaling function is $\phi ( x ) = \operatorname { s i n c } ( x )$ , where

$$
\operatorname { s i n c } ( x ) : = { \left\{ \begin{array} { l l } { 1 } & { x = 0 } \\ { \displaystyle { \frac { \sin ( \pi x ) } { \pi x } } } & { x \neq 0 . } \end{array} \right. }
$$

See Exercise 8 for further details.

We turn to a discussion of properties common to every multiresolution analysis. For a given function ${ \dot { \pmb g } } : { \pmb R }  { \pmb R } ,$ let

$$
g _ { j k } ( x ) = 2 ^ { j / 2 } g ( 2 ^ { j } x - k ) .
$$

The function $g _ { j k } ( x ) = 2 ^ { j / 2 } g ( 2 ^ { j } ( x - k / 2 ^ { j } ) )$ is a translation $( \log \ k / 2 ^ { j }$ and a rescaling (by a factor of $2 ^ { j / 2 }$ of the original function $\pmb { \mathscr { g } }$ (See Exercise 1.) The factor of $2 ^ { j / 2 }$ is present to preserve its $L ^ { 2 }$ norm; that is,

$$
\| g _ { j k } \| _ { L ^ { 2 } } ^ { 2 } = \| g \| _ { L ^ { 2 } } ^ { 2 } \quad \mathrm { f o r ~ a l l } ~ j , k .
$$

We use this notation both for the scaling function $\phi$ and, later, for the wavelet.   
Our first result is that $\{ \phi _ { j k } \} _ { k \in Z }$ is an orthonormal basis for $V _ { j }$ .

THeOrEM 5.5 Suppose $\{ V _ { j } ; j \in Z \}$ is a multiresolution analysis with scaling function $\phi$ .Then for any $j \in \mathbf { Z }$ , the set of functions

$$
\{ \phi _ { j k } ( x ) = 2 ^ { j / 2 } \phi ( 2 ^ { j } x - k ) ; \ k \in Z \}
$$

is an orthonormal basis for $V _ { j }$ .

Proof To prove that $\{ \phi _ { j k } , k \in Z \}$ spans $V _ { j }$ , we must show that any $\pmb { f } ( \pmb { x } ) \in$ $V _ { j }$ can be written as a linear combination $\{ \phi ( 2 ^ { j } x - k ) ; k \in Z \}$ Using the scaling property (Definition 5.1, condition 4), the function $f ( 2 ^ { - j } x )$ belongs to $V _ { 0 }$ and therefore $f ( 2 ^ { - j } x )$ is a linear combination of $\{ \phi ( x - k ) , k \in Z \}$ By replacing $\pmb { x }$ by $\pmb { 2 ^ { j } } _ { \pmb { x } }$ , we see that $\pmb { f } ( \pmb { x } )$ is a linear combination of $\{ \phi ( 2 ^ { j } x - k ) , k \in Z \}$ .

To show that $\{ \phi _ { j k } , k \in Z \}$ is orthonormal, we must show

$$
\begin{array} { c } { { \displaystyle { \langle \phi _ { j k } , \phi _ { j l } \rangle _ { L ^ { 2 } } = \delta _ { j k } = \left\{ \begin{array} { l l } { { 0 } } & { { \mathrm { i f } j \neq k } } \\ { { 1 } } & { { \mathrm { i f } j = k } } \end{array} \right. } } } \\ { { \mathrm { o r } \qquad 2 ^ { j } \displaystyle { \int _ { - \infty } ^ { \infty } { \phi ( 2 ^ { j } x - k ) } \frac { \ } { \phi ( 2 ^ { j } x - l ) } d x } = \delta _ { k l } . } } \end{array}
$$

To establish this equation, make the change of variables $\pmb { y } = 2 ^ { j } \pmb { x }$ (and so $d y =$ $2 ^ { j } d x )$ . We obtain

$$
2 ^ { j } \int _ { - \infty } ^ { \infty } \phi ( 2 ^ { j } x - k ) { \overline { { \phi ( 2 ^ { j } x - l ) } } } d x = \int _ { - \infty } ^ { \infty } \phi ( y - k ) { \overline { { \phi ( y - l ) } } } d y ,
$$

which equals $\delta _ { k l }$ in view of the orthonormal basis property given in Definition 5.1, condition 5. $\bullet$

# 5.1.2 The Scaling Relation

We are now ready to state and prove the central equation in multiresolution analysis, the scaling relation.

THeOrEM 5.6 Suppose $\{ V _ { j } ; j \in Z \}$ is a multiresolution analysis with scaling function $\phi$ . Then the following scaling relation holds:

$$
\phi ( x ) = \sum _ { k \in Z } p _ { k } \phi ( 2 x - k ) \quad { \mathrm { w h e r e } } \quad p _ { k } = 2 \int _ { - \infty } ^ { \infty } \phi ( x ) { \overline { { \phi ( 2 x - k ) } } } d x .
$$

Moreover, we also have

$$
\phi ( 2 ^ { j - 1 } x - l ) = \sum _ { k \in Z } p _ { k - 2 l } \phi ( 2 ^ { j } x - k )
$$

or, equivalently,

$$
\phi _ { j - 1 , l } = 2 ^ { - 1 / 2 } \sum _ { k } p _ { k - 2 l } \phi _ { j k }
$$

where $\phi _ { j k } ( x ) = 2 ^ { j / 2 } \phi ( 2 ^ { j } x - k )$ .

Remark. The preceding equation, which relates $\phi ( { \pmb x } )$ and the translates of $\phi ( 2 x )$ , is called the scaling relation or two-scale relation. When the support of $\phi$ is compact, only a finite number of the $\pmb { p _ { k } }$ are nonzero, because when $| k |$ is large enough, the support of $\phi ( 2 x - k )$ will be outside of the support for $\phi ( { \pmb x } )$ . Therefore, the sum occurring in Theorem 5.6 is finite. Usually, $\phi$ is real valued in which case the ${ \pmb p } _ { \pmb k }$ are real.

Proof To prove this theorem, note that $\begin{array} { r } { \phi ( \boldsymbol { x } ) = \sum \tilde { p } _ { k } \phi _ { 1 k } ( \boldsymbol { x } ) } \end{array}$ must hold for some choice of $\tilde { p } _ { k }$ because ${ \phi } ( x )$ belongs to $V _ { 0 } \subset V _ { 1 }$ , which is the linear span of $\{ \phi _ { 1 k } , k \in Z \}$ .Since $\{ \phi _ { 1 k } , k \in Z \}$ is an orthonormal basis of $V _ { 1 }$ , the $\tilde { \pmb { p } } _ { \pmb { k } }$ can be determined by using Theorem 0.21:

$$
\tilde { p } _ { k } = \langle \phi , \phi _ { 1 k } \rangle _ { L ^ { 2 } } = 2 ^ { 1 / 2 } \int _ { - \infty } ^ { \infty } \phi ( x ) \overline { { { \phi ( 2 x - k ) } } } d x .
$$

Therefore ,

$$
\phi ( x ) = \sum _ { k \in Z } \tilde { p } _ { k } \phi _ { 1 k } ( x ) = \sum _ { k \in Z } \tilde { p } _ { k } 2 ^ { 1 / 2 } \phi ( 2 x - k ) .
$$

Let $\begin{array} { r } { p _ { k } = 2 ^ { 1 / 2 } \tilde { p } _ { k } = 2 \int _ { - \infty } ^ { \infty } \phi ( x ) \overline { { \phi ( 2 x - k ) } } d x } \end{array}$ and we have

$$
\phi ( x ) = \sum _ { k \in Z } p _ { k } \phi ( 2 x - k )
$$

as claimed. To get the second equation, replace $\pmb { x }$ by $2 ^ { j - 1 } x - l$ in $\phi$ , and then adjust the index of summation in the resulting series. The third follows from the second by multiplying by $2 ^ { ( j - 1 ) / 2 }$ and then simplifying. $\bullet$

# EXAMPLE 5.7

The values of the ${ \pmb p } _ { \pmb k }$ for the Haar system are

$$
p _ { 0 } = p _ { 1 } = 1
$$

[see (4.12)] and all other ${ \pmb p } _ { \pmb { k } }$ are zero.

# EXAMPLe 5.8

As mentioned earlier, the Haar scaling function and Haar wavelet are discontinuous. There is a more intricate construction, due to Daubechies, that we will present in Chapter 6 that leads to a continuous scaling function and wavelet (see Figures 2 and 3 in Chapter 6 for their graphs). The associated values of the ${ \pmb p } _ { \pmb k }$ will be computed in Section 6.1 to be

$$
p _ { 0 } = { \frac { 1 + { \sqrt { 3 } } } { 4 } } \quad p _ { 1 } = { \frac { 3 + { \sqrt { 3 } } } { 4 } } \quad p _ { 2 } = { \frac { 3 - { \sqrt { 3 } } } { 4 } } \quad p _ { 3 } = { \frac { 1 - { \sqrt { 3 } } } { 4 } } .
$$

The following result contains identities for the ${ \pmb p } _ { \pmb k }$ that will be important later.

THEOREM 5.9 Suppose $\{ V _ { j } ; j \in Z \}$ is a multiresolution analysis with scaling function $\phi$ Then the following equalities hold:

$$
1 . \sum _ { k \in Z } p _ { k - 2 l } \overline { { p _ { k } } } = 2 \delta _ { l 0 }
$$

2.

$$
\begin{array} { l } { \displaystyle \sum _ { k \in Z } | p _ { k } | ^ { 2 } = 2 } \\ { \displaystyle \sum _ { k \in Z } p _ { k } = 2 } \end{array}
$$

3.

$$
\sum _ { k \in Z } p _ { 2 k } = 1 a n d \sum _ { k \in Z } p _ { 2 k + 1 } = 1
$$

Proof The first equation follows from the two-scale relation (Theorem 5.6) and the fact that $\{ \phi ( x - k ) , k \in Z \}$ is orthonormal. We leave the details to Exercise 4a. By setting $\pmb { l } = \pmb { 0 }$ in the first equation, we get the second equation.

The proof of the third equation uses Theorem 5.6 as follows:

$$
\int _ { - \infty } ^ { \infty } \phi ( x ) d x = \sum _ { k \in Z } p _ { k } \int _ { - \infty } ^ { \infty } \phi ( 2 x - k ) d x .
$$

By letting $t = 2 x - k$ and $d x = d t / 2$ , we obtain

$$
\int _ { - \infty } ^ { \infty } \phi ( x ) d x = 1 / 2 \sum _ { k \in Z } p _ { k } \int _ { - \infty } ^ { \infty } \phi ( t ) d t .
$$

Now $\textstyle \int \phi ( t )$ dt cannot equal zero (see Exercise 6), for otherwise we could never approximate functions $f \in L ^ { 2 } ( R )$ with $\textstyle \int f ( t ) d t \neq 0$ by functions in $V _ { j }$ Therefore, the factor of $\textstyle \int \phi ( t ) d t$ on the right can be canceled with $\textstyle \int \phi ( x ) d x$ on the left. The third equation now follows.

To prove the fourth equation, we take the first equation, $\begin{array} { r } { \sum _ { k } \mathcal { P } _ { k - 2 l } \overline { { \mathcal { P } } } _ { k } = 2 \delta _ { l 0 } } \end{array}$ and replace $\iota$ by $^ { - l }$ and then sum over $\imath$ We obtain

$$
\sum _ { l \in Z } \sum _ { k \in Z } p _ { k + 2 l } \overline { { p } } _ { k } = 2 \sum _ { l \in Z } \delta _ { l 0 } = 2 .
$$

Now divide the sum over $\pmb { k }$ into even and odd terms:

$$
\begin{array} { r l } & { 2 = \displaystyle \sum _ { l \in Z } \left( \displaystyle \sum _ { k \in Z } p _ { 2 k + 2 l } \overline { { p } } _ { 2 k } + \displaystyle \sum _ { k \in Z } p _ { 2 k + 1 + 2 l } \overline { { p } } _ { 2 k + 1 } \right) } \\ & { ~ = \displaystyle \sum _ { k \in Z } \left( \displaystyle \sum _ { l \in Z } p _ { 2 k + 2 l } \right) \overline { { p } } _ { 2 k } + \displaystyle \sum _ { k \in Z } \left( \displaystyle \sum _ { l \in Z } p _ { 2 k + 1 + 2 l } \right) \overline { { p } } _ { 2 k + 1 } . } \end{array}
$$

For the two inner l-sums on the right, replace $\iota$ by $\pmb { l } - \pmb { k }$ These inner $\imath$ -sums become $\sum \scriptstyle p _ { 2 l }$ and $\sum \eta _ { 2 } \eta _ { + 1 }$ , respectively. Therefore,

$$
\begin{array} { l } { \displaystyle 2 = \sum _ { k \in Z } \overline { { p } } _ { 2 k } \sum _ { l \in Z } p _ { 2 l } + \sum _ { k \in Z } \overline { { p } } _ { 2 k + 1 } \sum _ { l \in Z } p _ { 2 l + 1 } } \\ { \displaystyle \ = \vert \sum _ { k \in Z } \overline { { p } } _ { 2 k } \vert ^ { 2 } + \vert \sum _ { k \in Z } \overline { { p } } _ { 2 k + 1 } \vert ^ { 2 } . } \end{array}
$$

Let $\begin{array} { r } { E = \sum _ { k \in Z } p _ { 2 k } } \end{array}$ and $\begin{array} { r } { O = \sum _ { k \in Z } p _ { 2 k + 1 } } \end{array}$ This last equation can be restated as $| E | ^ { 2 } + | O | ^ { 2 } = 2$ From the first property, $\begin{array} { r } { \sum _ { k } p _ { k } = 2 } \end{array}$ Dividing this sum into even and odd indices gives $\pmb { { \cal E } } + \pmb { { \cal O } } = 2$ These two equations for $\pmb { \cal E }$ and $o$ have only one solution: $\pmb { { \cal E } } = \pmb { { \cal O } } = \mathbf { 1 }$ , as illustrated in Figure 2 for the case when all the ${ \pmb p } _ { \pmb k }$ are real numbers. For the general case, see Exercise 7. $\bullet$

![](images/e6c9743b44811b06619ef9ba9b6adde3ff3f14e22653d2c768ba37d60d191066.jpg)  
Figure 2 The circle $E ^ { 2 } + O ^ { 2 } = 2$ and the line $\pmb { { \cal E } } + \pmb { { \cal O } } = 2$

# 5.1.3 The Associated Wavelet and Wavelet Spaces

Recall that $V _ { j }$ is a subset of $V _ { j + 1 }$ .In order to carry out the decomposition algorithm in the general case, we need to decompose $V _ { j + 1 }$ into an orthogonal direct sum of $V _ { j }$ and its orthogonal complement, which we denote by $W _ { j }$ (as we did in the case of the Haar system). In addition, we need to construct a function $\psi$ whose translates generate the space $W _ { j }$ (also as we did in the Haar system). Once $\phi$ is specified, the scaling relation can be used to construct the associated function $\psi$ that generates $W _ { j }$ .We do this now.

THeOREM 5.10 Suppose $\{ V _ { j } ; j \in Z \}$ is a multiresolution analysis with scaling function

$$
\phi ( x ) = \sum _ { k } p _ { k } \phi ( 2 x - k )
$$

. $( p _ { k }$ are the coefficients in Theorem 5.6). Let $W _ { j }$ be the span of $\{ \psi ( 2 ^ { j } x - k ) ; k \in$ $z \}$ , where

$$
\psi ( x ) = \sum _ { k \in Z } ( - 1 ) ^ { k } { \overline { { p _ { 1 - k } } } } \phi ( 2 x - k ) .
$$

Then $W _ { j } \subset V _ { j + 1 }$ is the orthogonal complement of $V _ { j }$ in $V _ { j + 1 }$ .Furthermore, $\{ \psi _ { j k } ( x ) : = 2 ^ { j / 2 } \psi ( 2 ^ { j } x - k ) , k \in Z \}$ is an orthonormal basis for the $W _ { j }$ .

For the Haar scaling function, the coefficients $\pmb { p _ { 0 } }$ and ${ \pmb { \mathscr { P } } } { \pmb { 1 } }$ are both 1. Theorem 5.10 then states that the Haar wavelet is $\psi ( x ) = \phi ( 2 x ) - \phi ( 2 x - 1 )$ , which agrees with the definition of $\psi$ in Definition 4.7.

Proof of Theorem 5.10 Once we establish this theorem for the case ${ \dot { \pmb { \jmath } } } = { \bf 0 }$ , the case for ${ \dot { \mathbf { \eta } } } _ { { \dot { \mathbf { \eta } } } } ^ { } > \mathbf { 0 }$ will follow by using the scaling condition (Definition 5.1, condition 4).

To establish the result for the case ${ \dot { \pmb { \jmath } } } = { \bf 0 }$ , we must verify the following three statements:

1. The set $\{ \psi _ { 0 k } ( x ) = \psi ( x - k ) , k \in Z \}$ is orthonormal.   
2. $\psi _ { 0 k } ( x ) = \psi ( x ^ { : } - m )$ is orthogonal to $V _ { 0 }$ for all $\pmb { m } \in \pmb { Z }$ Equivalently, ${ \cal { W } } _ { 0 }$ is contained in the orthogonal complement of $V _ { 0 }$ in $V _ { 1 }$ .   
3. Any function in $V _ { 1 }$ that is orthogonal to $V _ { 0 }$ can be written as a linear combination of $\psi ( { \pmb x } - { \pmb k } )$ .Equivalently, $W _ { 0 }$ contains the orthogonal complement of $V _ { 0 }$ in $V _ { 1 }$ .

We shall establish the first two statements and postpone the proof of third (which is more technical) until Appendix A. The second and third together imply that $W _ { 0 }$ is the orthogonal complement of $V _ { 0 }$ in $V _ { 1 }$ .

To establish the first statement we have from Exercise 4b that

$$
\left. \psi _ { 0 m } , \psi _ { 0 l } \right. = \frac { 1 } { 2 } \sum _ { k \in \cal Z } \overline { { p _ { 1 - k + 2 m } } } p _ { 1 - k + 2 l } .
$$

Making the change of index $k ^ { \prime } = 1 - k + 2 m$ in this series and using the first part of Theorem 5.9, we have

$$
\left. { \psi _ { 0 m } , \psi _ { 0 l } } \right. = \frac { 1 } { 2 } \sum _ { k ^ { \prime } \in { \cal Z } } { \overline { { { p _ { k ^ { \prime } } } } } p _ { k ^ { \prime } + 2 l - 2 m } } = \delta _ { m - l , 0 } = \delta _ { m , l } ,
$$

so $\psi _ { 0 , m }$ is orthonormal.

To establish the second statement, it is sufficient to show that $\psi ( { \boldsymbol { x } } - m )$ is orthogonal to $\phi ( { \pmb x } - { \pmb l } )$ for each $\boldsymbol { i } \in \boldsymbol { z }$ because $V _ { 0 }$ is spanned by $\{ \phi ( x - l ) , l \in Z \}$ . From Exercise 4c, we have that

$$
\langle \phi _ { 0 l } , \psi _ { 0 m } \rangle = { \frac { 1 } { 2 } } \sum _ { k \in \mathbb { Z } } ( - 1 ) ^ { k } p _ { 1 - k + 2 m } ~ p _ { k - 2 l } .
$$

The sum on the right is zero. To see this, let us first examine the case when $l = m = 0$ , in order to see the pattern of cancellation. In this case, this sum is

$$
\sum _ { k \in Z } ( - 1 ) ^ { k } p _ { 1 - k } p _ { k } = \cdots - p _ { 2 } p _ { - 1 } + p _ { 1 } p _ { 0 } - p _ { 0 } p _ { 1 } + p _ { - 1 } p _ { 2 } + \cdots .
$$

The inner pair of terms cancel and then the outer pair of terms cancel, and so on. To see the general case, first note that the term with $k = l + m - j$ for ${ \dot { \pmb { \jmath } } } \geq { \bf 0 }$ is

$$
( - 1 ) ^ { l + m - j } p _ { 1 - l + m + j } p _ { m - l - j } ,
$$

which cancels with the term with $k = l + m + j + 1$ (again with ${ \dot { \pmb { \jmath } } } \geq { \pmb { 0 } }$ ), which is

$$
( - 1 ) ^ { l + m + j + 1 } p _ { m - l - j } p _ { m + j + 1 - l } = - ( - 1 ) ^ { l + m - j } p _ { m - l - j } p _ { m + j + 1 - l } .
$$

This completes the proof of the second statement. As we noted earlier, the third statement will be proved in Appendix A. $\bullet$

For future reference, we note that $\psi _ { j l } ( x ) = 2 ^ { j / 2 } \psi ( 2 ^ { j } x - l )$ has the expansion

$$
\psi _ { j l } = 2 ^ { - 1 / 2 } \sum _ { k \in \cal Z } ( - 1 ) ^ { k } \overline { { p _ { 1 - k + 2 l } } } \phi _ { j + 1 , k } .
$$

This follows from the definition of $\psi$ given in Theorem 5.10: Substitute $2 ^ { j } x - l$ for $\pmb { x }$ , multiply both both sides by $\scriptstyle 2 ^ { j / 2 }$ , and adjust the summation index.

From Theorem 5.10, the set $\{ \psi _ { j - 1 , k } \} _ { k \in Z }$ is an orthonormal basis for the space $W _ { j - 1 }$ , which is the orthogonal complement of $V _ { j - 1 }$ in $V _ { j }$ (so $V _ { j } = W _ { j - 1 } \oplus$ $V _ { j - 1 } )$ . By successive orthogonal decompositions,

$$
\begin{array} { l } { { V _ { j } = W _ { j - 1 } \oplus V _ { j - 1 } } } \\ { { \quad = W _ { j - 1 } \oplus W _ { j - 2 } \oplus V _ { j - 2 } } } \\ { { \quad \quad \cdots } } \\ { { \quad = W _ { j - 1 } \oplus W _ { j - 2 } \oplus \cdots \oplus W _ { 0 } \oplus V _ { 0 } . } } \end{array}
$$

Since we have defined $V _ { j }$ for ${ \dot { \mathbf { \zeta } } } _ { j } < \mathbf { 0 }$ ,we can keep going:

$$
\begin{array} { c } { { V _ { j } = W _ { j - 1 } \oplus W _ { j - 2 } \oplus \cdots \oplus W _ { 0 } \oplus W _ { - 1 } \oplus V _ { - 1 } } } \\ { { \ldots } } \\ { { = W _ { j - 1 } \oplus W _ { j - 2 } \oplus \cdots \oplus W _ { - 1 } \oplus W _ { - 2 } \cdots . } } \end{array}
$$

The $V _ { j }$ are nested and the union of all the $V _ { j }$ is the space $L ^ { 2 } ( R )$ Therefore, we can let $j \to \infty$ and obtain the following theorem.

TheOreM 5.11 Let $\{ V _ { j } , j \in Z \}$ be a multiresolution analysis with scaling function $\phi$ Let $W _ { j }$ be the orthogonal complement of $V _ { j }$ in $V _ { j + 1 }$ . Then

$$
L ^ { 2 } ( R ) = \cdots \oplus W _ { - 1 } \oplus W _ { 0 } \oplus W _ { 1 } \oplus \cdots .
$$

In particular each $f \in L ^ { 2 } ( R )$ $\scriptstyle \sum _ { k = - \infty } ^ { \infty } w _ { k }$ with $w _ { k } \in W _ { k }$ and where the ${ \pmb w } _ { \pmb k }$ 's are mutually orthogonal. Equivalently, the set of all wavelets, $\{ \psi _ { j k } \} _ { j , k \in Z }$ , is an orthonormal basis for $L ^ { 2 } ( R )$ .

The infinite sum appearing in this theorem should be thought of as an approximation by finite sums. In other words, each $f \in L ^ { 2 } ( R )$ can be approximated arbitrarily closely in the ${ \pmb L } ^ { 2 }$ -norm by finite sums of the form ${ w _ { - j } } + w _ { 1 - j } +$ $\cdots + w _ { j - 1 } + w _ { j }$ for suitably large $\dot { \pmb { \mathscr { I } } }$ .

For large $\begin{array} { r } { \dot { \pmb { \jmath } } _ { 2 } } \end{array}$ , the $W _ { j }$ -components of a signal represent its high-frequency components because $W _ { j }$ is generated by translates of the function $\psi ( 2 ^ { j } x )$ that vibrate at high frequency. For example, compare the picture in Figure 3, which is the graph of a function, $\psi ( x )$ , to that in Figure 4, which is the graph of $\psi ( 2 ^ { 2 } x )$ (the same function $\psi$ is used to generate both graphs).

![](images/1627bb19f1404c3a51b8e9297251c7ec9a3ad3ad71e7c89ca2c079569a67f461.jpg)  
Figure 3 Graph of $\boldsymbol { \psi }$

![](images/1898a3a4e02b4de8f3612497051f72a40fe6edb546358af16d7fa8b0e87c4418.jpg)  
Figure 4 Graph of $\psi ( 2 ^ { 2 } x )$

# 5.1.4 Decomposition and Reconstruction Formulas: A Tale of Two Bases

Suppose that we are dealing with a signal $\pmb { f }$ that is already in one of the approximation space, such as $V _ { j }$ . There are two primary orthonormal bases that can be used for representing $\pmb { f }$ The first is the natural scaling function basis

for $V _ { j }$ , $\{ \phi _ { j k } \} _ { k \in Z }$ as defined in Theorem 5.5. In terms of this basis, we have

$$
f = \sum _ { k \in \mathcal { Z } } \langle f , \phi _ { j k } \rangle \phi _ { j k } .
$$

Of course, since we have the orthogonal direct sum decomposition $V _ { j } = V _ { j - 1 } \oplus$ $W _ { j - 1 }$ , we can also use the concatenation of the bases for $V _ { j - 1 }$ and $W _ { j - 1 }$ ;that is, we use $\{ \phi _ { j - 1 , k } \} _ { k \in \mathcal { Z } } \cup \{ \psi _ { j - 1 , k } \} _ { k \in \mathcal { Z } }$ , where $\psi _ { j k }$ is defined in Theorem 5.10. Relative to this orthonormal basis (see Theorem 0.21), $\pmb { f }$ has the form

$$
f = \underbrace { \sum _ { k \in Z } \langle f , \phi _ { j - 1 , k } \rangle \phi _ { j - 1 , k } } _ { f _ { j - 1 } } + \underbrace { \sum _ { k \in Z } \langle f , \psi _ { j - 1 , k } \rangle \psi _ { j - 1 , k } } _ { w _ { j - 1 } } .
$$

The decomposition formula starts with the coefficients relative to the first basis [in (5.7)] and uses them to calculate the coefficients relative to the second basis [in (5.8)]. The reconstruction formula does the reverse. Here is the decomposition formula:

$$
\mathrm { i o n : } \quad \left\{ \begin{array} { l l } { \langle f , \phi _ { j - 1 , l } \rangle = 2 ^ { - 1 / 2 } \sum _ { k \in \mathcal { Z } } \overline { { p _ { k - 2 l } } } \langle f , \phi _ { j k } \rangle } \\ { \langle f , \psi _ { j - 1 , l } \rangle = 2 ^ { - 1 / 2 } \sum _ { k \in \mathcal { Z } } ( - 1 ) ^ { k } p _ { 1 - k + 2 l } \langle f , \phi _ { j k } \rangle . } \end{array} \right.
$$

The two parts of this formula are obtained by using Parseval's equation $( E x -$ ercise 3) in conjunction with appropriate expansions. To obtain the first part, we use the expansion (5.7) for $\pmb { f }$ and the scaling relation in equation (5.3). The second part also requires (5.7), but uses equation (5.6) for the wavelets $\psi _ { j k }$ with $\dot { \pmb { \mathscr { I } } }$ replaced by ${ \dot { \jmath } } - 1$ .

One important application of the decomposition formula is to express $\phi _ { j k }$ . in terms of the second basis. From the decomposition formula (5.9) together with the orthonormality of the $\phi _ { j k }$ 's, we have that $\langle \phi _ { j k } , \phi _ { j - 1 , l } \rangle = 2 ^ { - 1 / 2 } \overline { { p _ { k - 2 l } } }$ and $\langle \phi _ { j k } , \psi _ { j - 1 , l } \rangle = 2 ^ { - 1 / 2 } ( - 1 ) ^ { k } { p _ { 1 - k + 2 l } }$ Being careful about which index we are summing over $\{ l$ in this case), we obtain the expansion

$$
\phi _ { j k } = \sum _ { l \in \cal Z } 2 ^ { - 1 / 2 } \overline { { { p _ { k - 2 l } } } } \phi _ { j - 1 , l } + \sum _ { l \in \cal Z } 2 ^ { - 1 / 2 } ( - 1 ) ^ { k } p _ { 1 - k + 2 l } \psi _ { j - 1 , l } ,
$$

which is literally the "inverse" of the scaling relation.

If we apply Parseval's equation (Exercise 3) to equations (5.10) and (5.8), we obtain the reconstruction formula:

$$
\left\{ \begin{array} { l } { \langle f , \phi _ { j k } \rangle = 2 ^ { - 1 / 2 } \sum _ { l \in Z } p _ { k - 2 l } \langle f , \phi _ { j - 1 , l } \rangle } \\ { \qquad + \ 2 ^ { - 1 / 2 } \sum _ { l \in Z } ( - 1 ) ^ { k } \frac { 1 } { p _ { 1 - k + 2 l } } \langle f , \psi _ { j - 1 , l } \rangle . } \end{array} \right.
$$

The preceding formulas all involve orthonormal bases. For various reasons it might be more convenient to use the orthogonal versions— $\{ \phi ( 2 ^ { j } x - k ) \} _ { k \in Z } -$ rather than $\{ \phi _ { j k } ( x ) = 2 ^ { j / 2 } \phi ( 2 ^ { j } x - k ) \} _ { k \in { \cal Z } }$ , and $\{ \psi ( 2 ^ { j } x - k ) \} _ { k \in { \cal Z } }$ rather than

$\{ \psi _ { j k } ( x ) = 2 ^ { j / 2 } \psi ( 2 ^ { j } x - k ) \} _ { k \in { \cal Z } } .$ For instance, the expansion for $f \in V _ { j }$ in equation (5.7) can be rewritten this way:

$$
\begin{array} { l } { f ( x ) = \displaystyle \sum _ { k \in Z } \underbrace { 2 ^ { j / 2 } \langle f , \phi _ { j k } \rangle } _ { a _ { k } ^ { j } } \underbrace { 2 ^ { - j / 2 } \phi _ { j k } } _ { \phi ( 2 ^ { j } x - k ) } } \\ { = \displaystyle \sum _ { k \in Z } a _ { k } ^ { j } \phi ( 2 ^ { j } x - k ) . } \end{array}
$$

Similarly, equation (5.8) can be rewritten as

$$
f = \sum _ { k \in Z } a _ { k } ^ { j - 1 } \phi ( 2 ^ { j - 1 } x - k ) + \sum _ { k \in Z } b _ { k } ^ { j - 1 } \psi ( 2 ^ { j - 1 } x - k )
$$

where $a _ { k } ^ { j - 1 } = 2 ^ { ( j - 1 ) / 2 } \langle f , \phi _ { j - 1 , k } \rangle$ and $b _ { k } ^ { j - 1 } = 2 ^ { ( j - 1 ) / 2 } \langle f , \psi _ { j - 1 , k } \rangle$ .The $a _ { k } ^ { j }$ 's are called the approximation coefficients and the $\pmb { b } _ { \pmb { k } } ^ { j }$ 's are called the detail coefficients. The decomposition and reconstruction formulas can be restated in terms of these coefficients.

$$
\begin{array} { r l } { \mathrm { m p o s i t i o n : } \quad } & { \left\{ \begin{array} { l l } { a _ { l } ^ { j - 1 } = 2 ^ { - 1 } \sum _ { k \in \cal Z } \overline { { p _ { k - 2 l } } } a _ { k } ^ { j } } \\ { b _ { l } ^ { j - 1 } = 2 ^ { - 1 } \sum _ { k \in \cal Z } ( - 1 ) ^ { k } p _ { 1 - k + 2 l } a _ { k } ^ { j } } \end{array} \right. } \\ { \mathrm { n s t r u c t i o n : } \quad a _ { k } ^ { j } = \displaystyle \sum _ { l \in \cal Z } p _ { k - 2 l } a _ { l } ^ { j - 1 } + \displaystyle \sum _ { l \in \cal Z } ( - 1 ) ^ { k } \overline { { p _ { 1 - k + 2 l } } } b _ { l } ^ { j - 1 } } \end{array}
$$

Thus ends our Tale of Two Bases." We use the basis $\{ \phi _ { j k } \} _ { k \in Z }$ to view the signal as a whole, and we use the basis $\{ \phi _ { j - 1 , k } \} _ { k \in \mathbb { Z } } \cup \{ \psi _ { j - 1 , k } \} _ { k \in \mathbb { Z } }$ to view the smoothed and oscillatory parts of the signal.

# 5.1.5 Summary

Let us sumarize hema results concrningmultresolutin aalys $\{ V _ { j } \} _ { j \in Z }$ with scaling function $\phi$ .

# Scaling Function

$$
\mathrm { B a s i s ~ f o r } ~ V _ { j } ; ~ \{ \phi _ { j k } = 2 ^ { j / 2 } \phi ( 2 ^ { j } x - k ) \} _ { k \in { \cal Z } }
$$

$$
\begin{array} { r l } { \mathrm { S c a l i n g ~ R e l a t i o n : } } & { \left\{ \begin{array} { r l } { \phi ( x ) = \sum _ { k \in Z } p _ { k } \phi ( 2 x - k ) } \\ { \phi ( 2 ^ { j - 1 } x - l ) = \sum _ { k \in Z } p _ { k - 2 l } \phi ( 2 ^ { j } x - k ) } \\ { \phi _ { j - 1 , l } = 2 ^ { - 1 / 2 } \sum _ { k \in Z } p _ { k - 2 l } \phi _ { j k } } \end{array} \right. } \end{array}
$$

# Wavelet Spaces

$$
\begin{array} { r l } & { W _ { j } \perp V _ { j } \quad \mathrm { a n d } \quad V _ { j + 1 } = V _ { j } \oplus W _ { j } } \\ & { \qquad V _ { j + 1 } = \cdots W _ { j - 2 } \oplus W _ { j - 1 } \oplus W _ { j } } \\ & { \qquad L ^ { 2 } ( R ) = \cdots W _ { j - 2 } \oplus W _ { j - 1 } \oplus W _ { j } \oplus W _ { j + 1 } \cdots } \end{array}
$$

# Wavelet

$$
\left\{ \begin{array} { c } { \psi ( x ) = \sum _ { k \in Z } ( - 1 ) ^ { k } \overline { { p _ { 1 - k } } } \phi ( 2 x - k ) } \\ { \psi ( 2 ^ { j - 1 } x - l ) = \sum _ { k \in Z } ( - 1 ) ^ { k } \overline { { p _ { 1 - k + 2 l } } } \phi ( 2 ^ { j } x - k ) } \\ { \psi _ { j l } = 2 ^ { - 1 / 2 } \sum _ { k \in Z } ( - 1 ) ^ { k } \overline { { p _ { 1 - k + 2 l } } } \phi _ { j + 1 , k } } \end{array} \right.
$$

# Orthonormal Bases

$$
\frac { W _ { j } }  \{ \psi _ { j - 1 , k } \} _ { k \in \cal Z } \left\{ \begin{array} { l l } { { \{ \phi _ { j - 1 , k } \} _ { k \in \cal Z } \cup \left\{ \psi _ { j - 1 , k } \right\} _ { k \in \cal Z } } } \\ { { \left\{ \phi _ { j + 1 , k } \right\} _ { k \in \cal Z } \cup \left\{ \psi _ { j - 1 , k } \right\} _ { k \in \cal Z } } } \end{array} \right. \left\{ \begin{array} { l l } { { L ^ { 2 } ( R ) } } \\ { { \{ \psi _ { j , k } \} _ { j , k \in \cal Z } \cup \left\{ \psi _ { j - 1 , k } \right\} _ { k \in \cal Z } } } \\ { { \{ \phi _ { j k } \} _ { k \in \cal Z } } } \end{array} \right.
$$

# Decomposition Formulas

$$
\begin{array} { r l } { \mathrm { O r t h o n o r m a l ~ F o r m } } & { \left\{ \begin{array} { l l } { \langle f , \phi _ { j - 1 , l } \rangle = 2 ^ { - 1 / 2 } \sum _ { k \in \mathcal { Z } } \overline { { p _ { k - 2 l } } } \langle f , \phi _ { j k } \rangle } \\ { \langle f , \psi _ { j - 1 , l } \rangle = 2 ^ { - 1 / 2 } \sum _ { k \in \mathcal { Z } } ( - 1 ) ^ { k } p _ { 1 - k + 2 l } \langle f , \phi _ { j k } \rangle } \end{array} \right. } \\ { \mathrm { O r t h o g o n a l ~ F o r m } } & { \left\{ \begin{array} { l l } { \alpha _ { l } ^ { j - 1 } = 2 ^ { - 1 } \sum _ { k \in \mathcal { Z } } \overline { { p _ { k - 2 l } } } a _ { k } ^ { j } } \\ { b _ { l } ^ { j - 1 } = 2 ^ { - 1 } \sum _ { k \in \mathcal { Z } } ( - 1 ) ^ { k } p _ { 1 - k + 2 l } a _ { k } ^ { j } } \end{array} \right. } \end{array}
$$

where

$$
f = \sum _ { k \in Z } a _ { k } ^ { j } \phi ( 2 ^ { j } x - k ) = \sum _ { k \in Z } a _ { k } ^ { j - 1 } \phi ( 2 ^ { j - 1 } x - k ) + b _ { k } ^ { j - 1 } \psi ( 2 ^ { j - 1 } x - k )
$$

# Reconstruction Formulas

$$
\begin{array}{c} \begin{array} { r l } & { \mathrm { O r t h o n o r m a l ~ F o r m } \smallint _ { } \{ \{ f , \phi _ { j k } \} = 2 ^ { - 1 / 2 } \sum _ { l \in Z } p _ { k - 2 l } \langle f , \phi _ { j - 1 , l } \rangle } \\ & { \smallskip \mathrm { O r t h o n o r m a l ~ F o r m } \smallskip } \end{array} \left\{ \begin{array} { r l } { \langle f , \phi _ { j k } \rangle = 2 ^ { - 1 / 2 } \sum _ { l \in Z } p _ { k - 2 l } \langle f , \phi _ { j - 1 , l } \rangle } \\ { + 2 ^ { - 1 / 2 } \sum _ { l \in Z } ( - 1 ) ^ { k } \frac { 1 } { p _ { 1 - k + 2 l } } \langle f , \psi _ { j - 1 , l } \rangle } \\ { + \sum _ { l \in Z } p _ { k - 2 l } a _ { l } ^ { j - 1 } + \sum _ { l \in Z } ( - 1 ) ^ { k } \frac { 1 } { p _ { 1 - k + 2 l } } b _ { l } ^ { j - 1 } } \end{array} \right.  \end{array}
$$

# 5.2 Implementing Decomposition and Reconstruction

In this section, we describe decomposition and reconstruction algorithms associated with a multiresolution analysis. These algorithms are analogous to those presented in the section on Haar wavelets. In later sections, the algorithms developed here will be used in conjunction with a multiresolution analysis involving a continuous scaling function and a continuous wavelet to provide accurate decomposition and reconstruction of signals.

# 5.2.1 The Decomposition Algorithm

In order to do signal processing, such as filtering or data compression, an efficient algorithm is needed to decompose a signal into parts that contain information about the signal's oscillatory behavior. If we use a multiresolution analysis for this purpose, we need to develop an algorithm for breaking up a signal into its wavelet-space $( W _ { j } )$ components, because these components have the information that we want.

There are three major steps in decomposing a signal $\pmb { f }$ : initialization, iteration, and termination.

Initialization This step involves two parts. First, we have to decide on the approximation space $V _ { j }$ that best fits the information available on $\pmb { f }$ The sampling rate and our choice of multiresolution analysis determine which $V _ { j }$ to use. Second, we need to choose $f _ { j } \in V _ { j }$ to best fit $\pmb { f }$ itself.

The best approximation to $\pmb { f }$ from $V _ { j }$ , in the sense of energy, is $P _ { j } f$ , the orthogonal projection of $\pmb { f }$ onto $V _ { j }$ (see Definition 0.19); since $2 ^ { j / 2 } \phi ( 2 ^ { j } x - k )$ is orthonormal, Theorem 0.21 implies

$$
P _ { j } f ( x ) = \sum _ { k \in \cal Z } a _ { k } ^ { j } \phi ( 2 ^ { j } x - k ) \mathrm { , ~ w h e r e ~ } a _ { k } ^ { j } = 2 ^ { j } \int _ { - \infty } ^ { \infty } f ( x ) \overline { { { \phi ( 2 ^ { j } x - k ) } } } d x .
$$

The information from the sampled signal is usually not enough to determine the coefficients $a _ { k } ^ { j }$ exactly, and so we have to approximate them using the quadrature rule given in the next theorem.

THEOREM 5.12 Let $\{ V _ { j } , j \in Z \}$ be a given multiresolution analysis with a scaling function $\phi$ that is compactly supported. If $f \in L ^ { 2 } ( R )$ is continuous, then, for $\dot { \pmb { \mathscr { I } } }$ sufficiently large,

$$
a _ { k } ^ { j } = 2 ^ { j } \int _ { - \infty } ^ { \infty } f ( x ) { \overline { { \phi ( 2 ^ { j } x - k ) } } } d x \approx m f ( k / 2 ^ { j } ) ,
$$

where $\begin{array} { r } { m = \int \overline { { \phi ( x ) } } d x } \end{array}$

Proof Since $\phi$ has compact support, the set where $\phi$ is nonzero is contained in an interval of the form $\{ | t | \leq M \}$ . (In many cases, $\pmb { M }$ is not large; in fact in the case of the Haar function, $M = 1$ , and for the simpler Daubechies wavelets, $M$ is on the order of 5.) Thus, the interval of integration for $\pmb { a } _ { \pmb { k } } ^ { j }$ in (5.14) is $\{ x ; | 2 ^ { j } x - k | \le M \}$ By changing variables with $\pmb { t } = 2 ^ { j } \pmb { x } - \pmb { k }$ ,we obtain

$$
a _ { k } ^ { j } = \int _ { - M } ^ { M } f ( 2 ^ { - j } t + 2 ^ { - j } k ) { \overline { { \phi ( t ) } } } d t .
$$

When $\dot { \pmb { \mathscr { I } } }$ is large, $2 ^ { - j } t + 2 ^ { - j } k \approx 2 ^ { - j } k$ for $t \in [ - M , M ]$ Therefore, $f ( 2 ^ { - j } t +$ $2 ^ { - j } k ) \approx f ( 2 ^ { - j } k )$ for all $t \in [ - M , M ]$ because $\pmb { f }$ is uniformly continuous on any

![](images/3ed99e51ea97302cda81eb96abc76feea5941100144e0f4c72f2fa2be64af73b.jpg)  
Figure 5 A continuous function is almost constant on a small interval

finite interval (this is illustrated in Figure 5.) In particular, we can approximate the integral on the right by replacing $f ( 2 ^ { - j } t + 2 ^ { - j } k )$ by $f ( 2 ^ { - j } k )$ to obtain

$$
a _ { k } ^ { j } \approx f ( k / 2 ^ { j } ) \int _ { - M } ^ { M } \overline { { \phi ( t ) } } d t .
$$

Recalling that $\phi$ is 0 outside of the interval $[ - M , M ]$ , we have that

$$
\int _ { - M } ^ { M } { \overline { { \phi ( t ) } } } d t = \int _ { - \infty } ^ { \infty } { \overline { { \phi ( t ) } } } d t = m ,
$$

so $\alpha _ { k } ^ { j } \approx m f ( k / 2 ^ { j } )$

The accuracy of this approximation increases with increasing $\pmb { j }$ In Exercise 12, an estimate is given on how large $\dot { \jmath }$ must be in order to get an approximation to within a given tolerance. The accuracy may depend on both indicies $\pmb { j }$ and $\pmb { k }$ as well as the smoothness of $\pmb { f }$ Since in practice only finitely many coefficients are dealt with, care should be taken to pick $\dot { \pmb { \mathscr { I } } }$ large enough so that all of the coeficients are accurately calculated. In addition, the proof of the theorem can be modified to apply to the case of a piecewise continuous signal (see Exercise 15) and to the case where $\phi$ is well localized but not compactly supported. As mentioned in the proof of Theorem 5.9, $\textstyle \int \phi \neq 0$ (Exercise 6). Often, $\phi$ is constructed so that $\textstyle \int \phi = 1$ (e.g., Haar and Daubechies), in which case $\alpha _ { k } ^ { j } = f ( k / 2 ^ { j } )$ . Using the quadrature formula $\alpha _ { k } ^ { j } \doteq m f ( k / 2 ^ { j } )$ , we are also approximating the projection $P _ { j } f$ by the expansion

$$
P _ { j } f ( x ) \approx f _ { j } ( x ) = m \sum _ { k \in \cal Z } f ( k / 2 ^ { j } ) \phi ( 2 ^ { j } x - k ) .
$$

Note the similarity to the expansions associated with the sampling theorem.

The initialization step discussed here is often simply assumed and used without comment. Strang and Nguyen [20] point this out, and call it the "wavelet crime"!

Iteration Wavelets shine here! After the initialization step, we have $f \approx$ $f _ { j } \in V _ { j }$ From Theorem 5.11, we can start with $\pmb { f _ { j } }$ and decompose it into a sum of a lower level approximation part, $f _ { j - 1 } \in V _ { j - 1 }$ and a wavelet part, ${ w _ { j - 1 } \in W _ { j - 1 } }$ ; that is, $f _ { j } = f _ { j - 1 } + w _ { j - 1 }$ We then repeat the process with $f _ { j - 1 }$ then with $f _ { j - 2 }$ ,and so on. This is illustrated in the following diagram, where we have stopped the decomposition at level 0.

$$
f \approx f _ { j } \underbrace { \longrightarrow f _ { j - 1 } } _ { w _ { j - 1 } } \underbrace { \longrightarrow f _ { j - 2 } } _ { w _ { j - 2 } } \underbrace { - \dots } _ { \begin{array} { l } { \dots } \\ { \dots } \end{array} } \underbrace { f _ { 1 } } _ { w _ { 1 } } \underbrace { \dots + f _ { 0 } } _ { w _ { 0 } }
$$

To carry out the decomposition, we work with the approximation and wavelet coefficients, the a's and $\pmb { b } \mathbf { \dot { s } }$ that we discussed at the end of Section 5.1.4. As we did for the Haar wavelets, we want to put the decomposition equation (5.12) language of discrete filters and simple operators acting on coefficients.

Recall that the convolution of two sequences $\boldsymbol { x } = ( \dots x _ { - 1 } , x _ { 0 } , x _ { 1 } , \dots )$ and $\pmb { y } = ( \dots . y _ { - 1 } , y _ { 0 } , y _ { 1 } , \dots )$ is defined (see Definition 3.9) by

$$
( x * y ) _ { l } = \sum _ { k \in Z } x _ { k } y _ { l - k } .
$$

Let $\pmb { h }$ and $\pmb { \ell }$ be the sequences

$$
\begin{array} { l } { { h _ { k } : = \displaystyle \frac { 1 } { 2 } ( - 1 ) ^ { k } p _ { k + 1 } } } \\ { { \ell _ { k } : = \displaystyle \frac { 1 } { 2 } \overline { { { p - k } } } . } } \end{array}
$$

Define the two discrete filters (convolution operators) $\pmb { H }$ and $\pmb { L }$ via $H ( x ) = h * x$ and $L ( x ) = \ell * x$ Take $\textbf { \em x } = \textbf { \em a } ^ { j }$ and note that $\begin{array} { r } { L ( a ^ { j } ) _ { l } ~ = ~ \frac { 1 } { 2 } \sum _ { k \in \mathbb { Z } } \overline { { p _ { k - l } } } a _ { k } ^ { j } } \end{array}$ . Comparing this with equation (5.12), we see that $a _ { \iota } ^ { j - 1 } = L ( a ^ { j } ) _ { 2 \iota }$ Similarly, $\ b _ { l } ^ { j - 1 } = H ( a ^ { j } ) _ { 2 l }$ .In discussing the Haar decomposition algorithm, we encountered this operation of discarding the odd coefficients in a sequence and called it downsampling. A downsampled signal is a sampling of the signal at every other node and thus corresponds to sampling a signal on a grid that is twice as coarse as the original one. We define the downsampling operator $\pmb { D }$ as follows.

DEFInITIoN 5.13 If $\pmb { x } = ( \dots , \pmb { x } _ { - 2 } , \pmb { x } _ { - 1 } , \pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \dots )$ then its downsample is the sequence .

$$
D x = ( \dots , x _ { - 2 } , x _ { 0 } , x _ { 2 } , \dots )
$$

or $( D x ) _ { l } = x _ { 2 l }$ for all $l \in { \mathbf { Z } }$

We can now formulate the iterative step in the algorithm using discrete filters (convolution operators). The two filters that we use, $\pmb { h }$ and l, are called the decomposition high-pass and decomposition low-pass filters, respectively.

$$
\left. \begin{array} { l l } { { \mathrm { r m } ; } } & { { a ^ { j - 1 } = D ( \ell * a ^ { j } ) \quad \mathrm { a n d } \quad b ^ { j - 1 } = D ( h * a ^ { j } ) \Big \} } } \\ { { \mathrm { r m } ; } } & { { a ^ { j - 1 } = D L a ^ { j } \quad \mathrm { a n d } \quad b ^ { j - 1 } = D H a ^ { j } } } \end{array} \right\}
$$

In Figure 6, we illustrate the iterative step in the decomposition algorithm. We represent the downsampling operator pictorially by 2↓.

![](images/31e4bbe446fb06dc219b57b42adf373b290550bdcf74a1c4ffc33b165b5cfacc.jpg)  
Figure 6 Decomposition diagram for a general multiresolution analysis

It is important to note that the discrete filters and downsampling operator do not depend on the level $j$ Thus storage is minimal and, because convolution is inexpensive computationally, the whole iterative process is fast and efficient.

Termination. There are several criteria for finishing the decomposition. The simplest is that we decompose until we exhaust the finite number of samples we have taken. On the other hand, this may not be necessary. Singularity detection may only require one or two levels. In general, the choice of stopping point greatly depends on what we wish to accomplish.

The end result of the entire decomposition procedure—stopped at ${ \dot { \pmb { \jmath } } } = { \bf 0 } ,$ . say—is a set of coefficients that includes the approximation coefficients for level 0, (i.e., $\{ a _ { k } ^ { 0 } \}$ )and the detail (wavelet) coefficients $\{ b _ { \pmb { k } } ^ { j ^ { \prime } } \}$ for $j ^ { \prime } = 0 , \ldots , j - 1$ .

# EXAMPLE 5.14

We consider the signal, $\pmb { f }$ , defined on the unit interval $0 \leq x \leq 1$ given in Figure 7 (the same one used in Example 4.13). As before, we discretize this signal over $2 ^ { 8 }$ nodes [so $a _ { l } ^ { 8 } = f ( l / 2 ^ { 8 } ) ]$ We now use the decomposition algorithm given in equation (5.17) with the Daubechies wavelets whose $\pmb { p }$ -values are given in (5.4). Plots of the components in $V _ { 8 }$ , $V _ { 7 }$ , $V _ { 6 }$ and $V _ { 4 }$ are given in Figures 8 through 11. Compare these with the corresponding figures for the Haar wavelets (Figures 14, 16, 17, and 18 in Chapter 4). Since the Daubechies wavelets are continuous, they offer better approximations to the original signal than do the Haar wavelets.

![](images/4a147bf3c4e031571cc56e2ded3b6438e859e1022b78fd2a8b544045c7b9dcd2.jpg)  
Figure 7 Sample signal

![](images/6271552bcb55aa2c7eb0712c378fca10befca8dc690a52bad48f113837316532.jpg)  
Figure 8 $V _ { 8 } .$ -component with Daubechies

# 5.2.2 The Reconstruction Algorithm

As mentioned in the section on Haar wavelets, once the signal has been decomposed, some of its $W _ { j ^ { \prime } }$ -components may be modified. If the goal is to filter out noise, then the $W _ { j ^ { \prime } }$ -components of $\pmb { f }$ corresponding to the unwanted frequencies can be thrown out and the resulting signal will have significantly less noise. If the goal is data compression, the $W _ { j ^ { \prime } }$ -components that are small can be thrown out, without appreciably changing the signal. Only the significant $W _ { j ^ { \prime } }$ -components (the larger $\boldsymbol { b } _ { \boldsymbol { k } } ^ { j ^ { \prime } }$ ) need to be transmitted and significant data compression can be achieved. In either case, since the $W _ { j ^ { \prime } }$ -components have been modified, we need a reconstruction algorithm to reassemble the compressed or filtered signal in terms of the basis elements, $\phi ( 2 ^ { j } x - l )$ , of $V _ { j }$ The idea is to reconstruct $f _ { j } \approx f$ by using $f _ { j ^ { \prime } } = f _ { j ^ { \prime } - 1 } + w _ { j ^ { \prime } - 1 }$ , starting at ${ \dot { \mathcal { I } } } ^ { \prime } = 1$ The scheme is illustrated in the following diagram.

![](images/c3aa615faab5100cbb60cf5d4f1113122773a6dfc0a4db23c0341c1f142fbe17.jpg)  
Figure 9 $V _ { 7 }$ -component with Daubechies

![](images/bc08979f48dc8530bc5c56dd96e9ac487faef99bdbe283bed4edbf6eb76d2673.jpg)  
Figure 10 $V _ { 6 }$ -component with Daubechies

![](images/4d6786aeaeb222666301a671a6861be6a07cc3fd0943f34725f20c6138489db0.jpg)  
Figure 11 $V _ { 4 }$ -component with Daubechies

$$
m _ { 0 } \mathop { \blacktriangleright } _ { \boldsymbol { w } _ { 0 } } f _ { 1 } \mathop { \longrightarrow } _ { \boldsymbol { w } _ { 1 } } f _ { 2 } \mathop { \longrightarrow } _ { \boldsymbol { w } _ { 2 } } \ h _ { \mu _ { 0 } } \ h _ { \mu _ { 0 } } ^ { \mu _ { 1 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 2 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 1 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 2 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 2 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 1 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 2 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 2 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 2 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 2 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 1 } } \ h _ { \mu _ { 1 } } ^ { \mu _ { 2 } }
$$

We again break up the algorithm into three major steps: initialization, iteration, and termination.

Initialization What we have available is a set of possibly modified coefficients-starting at level 0, say—that includes the approximation coefficients for level 0, $\{ a _ { k } ^ { 0 } \}$ ,and the detail (wavelet) coefficients $\{ b _ { \pmb { k } } ^ { j ^ { \prime } } \}$ for $j ^ { \prime } = 0 , \dotsc , j$ . These coefficients appear in the expansions

$$
\begin{array} { l } { { \displaystyle f _ { 0 } ( x ) = \sum _ { k \in \cal Z } a _ { k } ^ { 0 } \phi ( x - k ) \in V _ { 0 } } } \\ { { \displaystyle w _ { j ^ { \prime } } ( x ) = \sum _ { k \in \cal Z } b _ { k } ^ { j ^ { \prime } } \psi ( 2 ^ { j ^ { \prime } } x - k ) \in W _ { j ^ { \prime } } \quad \mathrm { f o r ~ } 0 \leq j ^ { \prime } < j . } } \end{array}
$$

Iteration We again formulate this step in terms of discrete filters. Let $\widetilde { h }$ and $\widetilde { \ell }$ be the sequences

$$
\begin{array} { r l } & { \widetilde { h } _ { k } : = \overline { { p _ { 1 - k } } } ( - 1 ) ^ { k } } \\ & { \widetilde { \ell } _ { k } : = p _ { k } . } \end{array}
$$

Define the two discrete filters (convolution operators) $\widetilde { H }$ and $\widetilde { L }$ via $\widetilde { H } ( x ) = \widetilde { h } * x$ and $\widetilde { L } ( x ) = \widetilde { \ell } * x$ The reconstruction formula equation (5.13) gives $\pmb { a } _ { \pmb { k } } ^ { j }$ as a sum of two terms, $\scriptstyle \sum _ { l \in \mathcal { Z } } p _ { k - 2 l } a _ { l } ^ { j - 1 }$ and $\begin{array} { r l } { } & { { } \sum _ { l \in \mathbb { Z } } ( - 1 ) ^ { k } \overline { { p _ { 1 - k + 2 l } } } b _ { l } ^ { j - 1 } } \end{array}$ Using the filter sequences we have just introduced, we can rewrite (5.13) as

$$
a _ { k } ^ { j } = \displaystyle \sum _ { l \in \cal Z } { \widetilde { \ell } } _ { k - 2 l } a _ { l } ^ { j - 1 } + \displaystyle \sum _ { l \in \cal Z } { \widetilde { h } } _ { k - 2 l } b _ { l } ^ { j - 1 }
$$

This is almost a sum of two convolutions; the only difference is that the index for a convolution is $\pmb { k } - \pmb { l }$ instead of $\pmb { k } - \pmb { 2 } l$ In other words, (5.22) is a convolution with the odd terms missing (i.e., $\tilde { \ell } _ { k - ( 2 l + 1 ) } )$ . They can be inserted back by simplify multiplying them by zero. We illustrate this procedure by explicitly writing out the first few terms:

$$
\begin{array} { r l } & { a _ { k } ^ { j } = \cdots + \widetilde \ell _ { k + 4 } a _ { - 2 } ^ { j - 1 } + \widetilde \ell _ { k + 3 } \cdot 0 + \widetilde \ell _ { k + 2 } a _ { - 1 } ^ { j - 1 } + \widetilde \ell _ { k + 1 } \cdot 0 + \widetilde \ell _ { k } a _ { 0 } ^ { j - 1 } + \widetilde \ell _ { k - 1 } \cdot 0 } \\ & { \qquad + \cdots + \mathrm { s i m i l a r ~ } \widetilde h \mathrm { ~ t e r m s } . } \end{array}
$$

In order to put this sum into convolution form, we alter the input sequence $\pmb { a } _ { l } ^ { j - 1 }$ by interspersing zeros between its components, making a new sequence that has zeros at all odd entries. Each of the original nonzero terms is given a new, even index by doubling its old index. For example, $\pmb { a } _ { - 1 } ^ { j - 1 }$ now has index $- 2$ This procedure is called upsampling and is precisely formulated as follows:

DEFINITION 5.15 Let $\pmb { x } = ( \dots x _ { - 2 } , x _ { - 1 } , x _ { 0 } , x _ { 1 } , x _ { 2 } , \dots )$ be a sequence. We define the upsampling operator $\pmb { U }$ via

$$
U x = ( \dots x _ { - 2 } , 0 , x _ { - 1 } , 0 , x _ { 0 } , 0 , x _ { 1 } , 0 , x _ { 2 } , 0 , \dots )
$$

or

$$
( U x ) _ { k } = { \left\{ \begin{array} { l l } { 0 } & { i f k i s o d d } \\ { x _ { k / 2 } i f k i s e v e n . } \end{array} \right. }
$$

The iterative step (5.2) in the reconstruction algorithm can now be simply formulated in terms of discrete filters (convolution operators).

$$
\left. \begin{array} { r l } { { \mathrm { C o n v o l u t i o n ~ f o r m : } } } & { { } { { a } ^ { j } = \widetilde { \ell } * ( U a ^ { j - 1 } ) + \widetilde { h } * ( U b ^ { j - 1 } ) } } \\ { { \mathrm { O p e r a t o r ~ f o r m : } } } & { { } { { a } ^ { j } = \widetilde { L } U a ^ { j - 1 } + \widetilde { H } U b ^ { j - 1 } } } \end{array} \right\}
$$

We remark that $\widetilde { h }$ and $\widetilde { \ell }$ are called the reconstruction high-pass and low-pass filters, respectively. As was the case in the decomposition algorithm, neither of the filters depends on the level. This makes the iteration in the reconstruction step quick and efficient. In Figure 12, we illustrate the iterative step in the reconstruction algorithm. We represent the upsampling operator pictorially by $2 \uparrow$

In the case of the Haar wavelets, $p _ { 0 } = p _ { 1 } = 1$ This algorithm reduces to the Haar reconstruction algorithm given in Theorem 4.14.

![](images/a40871515f62a68e0cf1690c82e71e03b00a761e765c50452611cb32a0401e5e.jpg)  
Figure 12 Reconstruction diagram for a general multiresolution analysis

Termination The decomposition and reconstruction algorithms use the scaling coefficients, ${ \pmb p } _ { \pmb { k } }$ , but not the actual formulas for ${ \phi } ( { \pmb x } )$ or $\psi ( { \pmb x } )$ To plot the reconstructed signal $\begin{array} { r } { f ( x ) = \sum _ { l } a _ { l } ^ { j } \phi ( 2 ^ { j } x - l ) } \end{array}$ , we can approximate the value of $\pmb { f }$ at $\pmb { x } = l / 2 ^ { j }$ by $\pmb { a } _ { l } ^ { j }$ in view of Theorem 5.12 (provided $\scriptstyle \int \phi = 1 )$ . So the formulas for $\phi$ and $\psi$ do not even enter into the plot of the reconstructed signal. This is fortunate since the computation of $\phi$ and $\psi$ for Daubechies example is rather complicated (see Sections 5.3.4 and 6.4). However, $\phi$ and $\psi$ play important background roles since the orthogonality properties of $\phi$ and $\psi$ are crucial to the success of the decomposition and reconstruction algorithms.

# 5.2.3 Processing a Signal

The steps in processing a signal are essentially the same as the ones discussed in connection with the Haar system in the previous chapter.

1.Sample. This is really a preprocessing step. If the signal is continuous,1 then it must be sampled at a rate sufficient to capture its essential details. The sampling rate varies, depending on a variety of factors. For instance, to sample with full fidelity a performance of Beethoven's Ninth Symphony, we have to capture frequencies up to the audible limit of human hearing, roughly $\bf { 2 0 ~ k H z }$ This is the Nyquist frequency. A good rule of thumb frequently used in sampling signals is to use a rate that is double the Nyquist frequency, or $\mathbf { 4 0 ~ k H z }$ in this case.   
2. Decompose. Once the signal has been sampled, then we use Theorem 5.12 to approximate the highest-level approximation coefficients. We then iterate equation (5.17) until an appropriate level is reached (such as ${ \dot { \pmb { j } } } = { \bf 0 }$ ) The output of this step is all levels of wavelet coefficients (details) and the lowest-level approximation coefficients. This set of coefficients is the one that will be worked with in the next step.   
3. Process the signal. At this stage, the signal can be compressed by discarding insignificant coefficients, or it can be filtered or denoised in other

ways. The output may be stored or immediately reconstructed to recover the processed version of the signal. In some cases, such as singularity detection, the signal is of no further interest and is discarded.

4.Reconstruct. The reconstruction algorithm (5.22) is invoked here. The output of that algorithm is really the set of top-level approximation coefficients. Theorem 5.12 is then invoked to conclude that the processed signal is approximately equal to the top-level reconstructed coefficients.

# EXaMPLe 5.16

We apply the decomposition and reconstruction algorithms with Daubechies wavelets to the signal, $\pmb { f } ,$ , over the unit interval given in Figure 13 (this is the same signal used in Example 4.15).

![](images/31cc157f492495003ffcdaff855cb48d6c149a17d03b204a7a89247e7f5f8d26.jpg)  
Figure 13 Sample signal

As before, we discretize this signal over $2 ^ { 8 }$ nodes (so $\alpha _ { k } ^ { 8 } = f ( k / 2 ^ { 8 } )$ for ${ \mathfrak { o } } \leq$ . $k \leq 2 ^ { 8 } - 1 )$ and then decompose this signal with (5.17) to obtain

$$
f = f _ { 0 } + w _ { 0 } + w _ { 1 } + w _ { 2 } + \cdots + w _ { 7 }
$$

with

$$
f _ { 0 } ( x ) = a _ { 0 } ^ { 0 } \phi ( x ) \in V _ { 0 } \quad \mathrm { a n d } \quad w _ { j ^ { \prime } } ( x ) = \sum _ { k \in Z } b _ { k } ^ { j ^ { \prime } } \psi ( 2 ^ { j ^ { \prime } } x - k ) \in W _ { j ^ { \prime } }
$$

where $\phi$ and $\psi$ are the Daubechies scaling function and wavelet (which we will construct shortly). We then compress and reconstruct the signal using (5.22), and we replot the new $a _ { k } ^ { 8 }$ as the approximate value of the reconstructed signal at $x = k / 2 ^ { 8 }$ .Figures 14 and 15 illustrate $8 0 \%$ and $9 0 \%$ compressions using Daubechies wavelets (by setting the smaller $80 \%$ and $9 0 \%$ of the $| b _ { \pmb { k } } ^ { j ^ { \prime } } |$ coefficients equal to zero, respectively). Compare these compressed signals with Figures 20 and 21 in Chapter 4, which illustrate $8 0 \%$ and $9 0 \%$ compression with the Haar wavelets. The relative errors for $80 \%$ and $9 0 \%$ compression are

![](images/e9ec593ba45ea6db86262d0f65ddb1b163dd79ffabb860ee6ad17857998cc2ee.jpg)  
Figure 14 Eighty percent compression with Daubechies

![](images/25f5531e907f81873cc4bbaf617e4b2d3ce37eff9f2136697fcb85177457fc4e.jpg)  
Figure 15 Ninety percent compression with Daubechies

0.0553 and 0.1794, respectively. For comparison, the relative errors for the same compression rates with Haar wavelets are 0.0895 and 0.1838, respectively (see Example 4.15). Using the FFT, for the same compression rates, the relative errors are 0.1228 and 0.1885, respectively.

Do not get the impression from this example that wavelets are better than the FFT for data compression. The signal in this example has two isolated spikes, which wavelets are designed to handle better than the FFT. Signals without spikes or rapid changes or that have an almost periodic nature can be handled quite well with the FFT (perhaps even better than wavelets). •

# 5.3 Fourier Transform Criteria

The examples of multiresolution analyses discussed in the previous sections— Haar, linear splines, and Shannon—all are constructed by starting with a given set of sampling spaces. All of these have limitations. For example, as mentioned earlier, the decomposition algorithm based on the Haar scaling function does not provide an accurate approximation to most smooth signals, because the Haar scaling function and associated wavelet are discontinuous. The Shannon multiresolution analysis is smooth enough, but the high- and low-pass filters used in decomposition and reconstruction have infinite length impulse responses (i.e., an infinite number of scaling coefficients). Moreover, these responses are sequences that have slow decay for large index n. The linear splines are better in this regard. Even so, the impulse responses involved are still infinite. In Chapter 6, we construct a multiresolution analysis that has a continuous scaling function; finite impulse responses for the high- and low-pass filters are used in its decomposition and reconstruction algorithms. Instead of starting with the sampling spaces, we construct the scaling function directly using Fourier transform methods. In this section, we state and derive the properties that must be satisfied by a scaling function, and then translate these properties into language involving the Fourier transform.

# 5.3.1 The Scaling Function

Recall that a multiresolution analysis is, by definition, a collection of subspaces $\{ V _ { j } , j \in Z \}$ of $L ^ { 2 } ( R )$ , where each $V _ { j }$ is the span of $\{ \phi ( 2 ^ { j } x - k ) , k \in Z \}$ , where $\phi$ must be constructed so that the collection $\{ V _ { j } , j \in Z \}$ satisfies the properties listed in Definition 5.1. The following theorem provides an equivalent formulation of these properties in terms of the function $\phi$ .

THEOREM 5.17 Suppose $\phi$ is a continuous function with compact support satisfying the orthonormality condition: $\begin{array} { r } { \int \phi ( x - k ) \phi ( x - l ) d x = \delta _ { k l } } \end{array}$ .Let $V _ { j }$ be the span of $\{ \phi ( 2 ^ { j } x - k ) ; k \in Z \}$ Then the following hold.

The spaces $V _ { j }$ satisfy the separation condition (i.e. $\cap V _ { j } = \{ 0 \} )$ . If the following additional conditions are satisfied by $\phi$

1. Normalization: $\textstyle \int \phi ( x ) d x = 1$

2. Scaling: $\begin{array} { r } { \phi ( x ) = \sum _ { k } p _ { k } \phi ( 2 x - k ) } \end{array}$ for some finite number of constants . ${ \pmb p } _ { \pmb k }$

then the associated $V _ { j }$ satisfy the density condition: $\cup V _ { j } = L ^ { 2 } ( R )$ ,or, in other words, any function in $L ^ { 2 } ( R )$ can be approximated by functions in $V _ { j }$ for large enough $\dot { \jmath }$

In particular, if the function $\phi$ is continuous with compact support and satisfies the normalization, scaling, and orthonormality conditions just listed, then the collection of spaces $\{ V _ { j } , j \in Z \}$ forms a multiresolution analysis.

Proof Here, we give a nontechnical explanation of the central ideas of the first part of the theorem. Rigorous proofs of the first and second parts are contained in Appendix A.

By definition, a signal, $\pmb { f }$ , belonging to $V _ { - j }$ is a linear combination of

$$
\{ \phi ( x / 2 ^ { j } - k ) , \quad k = \cdots - 2 , - 1 , 0 , 1 , 2 \cdots \} .
$$

As $j > 0$ gets large, the set where $\phi ( x / 2 ^ { j } - k )$ is nonzero gets larger. For example, if Figure 16 represents the graph of $\phi _ { i }$ ,then the graph of $\phi ( x / 2 ^ { 2 } )$ is given in Figure 17.

![](images/20a716eed297ddaa664baf954a844bb02c57d5d2a51cc24c3f932fe9bc569104.jpg)  
Figure 16 Graph of $\phi$

On the other hand, as a member of $L ^ { 2 } ( R )$ , $\pmb { f }$ has finite energy-that is, $\textstyle \int | f ( t ) | ^ { 2 } d t$ is finite. As the graphs in Figures 16 and 17 show, the energy of a signal increases $\begin{array} { r } { ( \int | f ( t ) | ^ { 2 } d t \to \infty ) } \end{array}$ as the size of the set where the signal is nonzero grows large. Therefore, a nonzero signal that belongs to all the $V _ { - j }$ ,as $j \to \infty$ , must have infinite energy. We conclude that the only signal belonging to all the $V _ { j }$ must be identically zero.

![](images/d2fc31c137500bfb3de7d3fb0a3dca3078c816f5c2eb2568bc83600a1460bc7a.jpg)  
Figure 17 Graph of $\phi ( x / 4 )$

# 5.3.2 Orthogonality via the Fourier Transform

How is a scaling function $\phi$ constructed? To construct a scaling function, we must first find coefficients ${ \pmb p } _ { \pmb k }$ that satisfy Theorem 5.9. A direct construction of the ${ \pmb p } _ { \pmb k }$ is difficult. Instead, we use the Fourier transform, which will more clearly motivate some of the steps in the construction of the ${ \pmb p } _ { \pmb k }$ and hence of $\phi$ At first, we assume that a continuous scaling function exists and see what properties must be satisfied by the associated scaling coefficients ${ \pmb p } _ { \pmb k }$ Then we reverse the process and show that if ${ \pmb p } _ { \pmb k }$ satisfies these properties, then an associated scaling function can be constructed. In the next section, an example of a set of coefficients, ${ \pmb p } _ { \pmb k }$ , is constructed that satisfies these properties, and this will lead to the construction of a particular continuous scaling function (due to Daubechies).

Recall that the definition of the Fourier transform of a function $\pmb { f }$ is given by

$$
{ \hat { f } } ( \xi ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } f ( x ) e ^ { - i x \xi } d x .
$$

Since $\begin{array} { r } { \hat { \phi } ( 0 ) = \frac { 1 } { \sqrt { 2 \pi } } \int \phi ( x ) d x , } \end{array}$ the normalization condition $( \int \phi = 1 )$ becomes

$$
\hat { \phi } ( 0 ) = \frac { 1 } { \sqrt { 2 \pi } } .
$$

The translations of the orthonormality conditions on $\phi$ and $\psi$ into the language of the Fourier transform are given in the next theorem.

TheoreM 5.18 A function $\phi$ satisfies the orthonormality condition if and only if

$$
2 \pi \sum _ { k \in \cal Z } | \hat { \phi } ( \xi + 2 \pi k ) | ^ { 2 } = 1 \quad f o r \ a l l \ \xi \in \cal R .
$$

In addition, a function $\psi ( x )$ is orthogonal to $\phi ( { \pmb x } - { \pmb l } )$ for all $\iota \in z$ if and only if

$$
\sum _ { k \in Z } \hat { \phi } ( \xi + 2 \pi k ) \overline { { \hat { \psi } ( \xi + 2 \pi k ) } } = 0 f o r a l l \xi \in R .
$$

Proof We will prove the first part. The proof of the second part is similar. The orthonormality condition can be stated as

$$
\int \phi ( x - k ) { \overline { { \phi ( x - l ) } } } d x = \delta _ { k l } = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } k = l } \\ { 0 , } & { { \mathrm { i f ~ } } k \neq l . } \end{array} \right. }
$$

By replacing $\pmb { x } - \pmb { k }$ by $\pmb { x }$ in the preceding integral and relabeling $\begin{array} { r } { n = l - k , } \end{array}$ , the orthonormality condition can be restated as

$$
. \qquad \int \phi ( x ) \overline { { \phi ( x - n ) } } d x = \delta _ { 0 n } .
$$

Recall that Plancherel's identity for the Fourier transform (Theorem 2.12) states

$$
\int _ { - \infty } ^ { \infty } f ( x ) { \overline { { g ( x ) } } } d x = \int _ { - \infty } ^ { \infty } { \widehat { f ( \xi ) } } { \overline { { \widehat { g ( \xi ) } } } } d \xi \quad { \mathrm { f o r ~ } } f , g \in L ^ { 2 } .
$$

We apply this identity with $f ( x ) = \phi ( x )$ and $g ( x ) = \phi ( x - n )$ .By the sixth part of Theorem 2.6 (with ${ \pmb a } = { \pmb n }$ and $\lambda = \xi$ , ${ \widehat { \phi ( x - n ) } } ( \xi ) = { \widehat { \phi } } ( \xi ) e ^ { - i n \xi }$ .So the orthonormality condition (5.24) can be restated as

$$
\int _ { - \infty } ^ { \infty } \widehat { \phi } ( \xi ) \overline { { \widehat { \phi } ( \xi ) e ^ { - i n \xi } } } d \xi = \delta _ { 0 n } \quad \mathrm { o r } \quad \int _ { - \infty } ^ { \infty } | \widehat { \phi } ( \xi ) | ^ { 2 } e ^ { i n \xi } d \xi = \delta _ { 0 n } .
$$

By dividing the real line into the intervals $I _ { j } = [ 2 \pi j , 2 \pi ( j + 1 ) ]$ for $j \in  { \mathbf { Z } }$ , this equation can be written as

$$
\sum _ { j \in Z } \int _ { 2 \pi j } ^ { 2 \pi ( j + 1 ) } | \hat { \phi } ( \xi ) | ^ { 2 } e ^ { i n \xi } d \xi = \delta _ { 0 n } .
$$

Now replace $\pmb { \xi }$ by $\xi + 2 \pi j$ The limits of integration change to 0 and $2 \pi$ .

$$
\int _ { 0 } ^ { 2 \pi } \sum _ { j \in \cal Z } | \hat { \phi } ( \xi + 2 \pi j ) | ^ { 2 } e ^ { i n ( \xi + 2 \pi j ) } d \xi = \delta _ { 0 n } .
$$

Since $e ^ { 2 \pi i j } = 1$ , for $j \in \mathbf { Z }$ , this equation becomes

$$
\int _ { 0 } ^ { 2 \pi } \sum _ { j \in Z } | \hat { \phi } ( \xi + 2 \pi j ) | ^ { 2 } e ^ { i n ( \xi ) } d \xi = \delta _ { 0 n } .
$$

Let

$$
F ( \xi ) = 2 \pi \sum _ { j \in \cal Z } | \hat { \phi } ( \xi + 2 \pi j ) | ^ { 2 } .
$$

The orthonormality condition (5.25) becomes

$$
( 1 / 2 \pi ) \int _ { 0 } ^ { 2 \pi } F ( \xi ) e ^ { i n \xi } d \xi = \delta _ { 0 n } .
$$

The function $\pmb { F }$ is $\pmb { 2 \pi } .$ periodic because

$$
\begin{array} { r l } { { } } & { { \displaystyle F ( \xi + 2 \pi ) = 2 \pi \sum _ { j \in Z } \vert \hat { \phi } ( \xi + 2 \pi ( j + 1 ) ) \vert ^ { 2 } } } \\ { { } } & { { ~ = 2 \pi \displaystyle \sum _ { j ^ { \prime } } \vert \hat { \phi } ( \xi + 2 \pi j ^ { \prime } ) \vert ^ { 2 } ~ ( \mathrm { r e p l a c e } ~ j + 1 ~ \mathrm { b y } ~ j ^ { \prime } ~ ) } } \\ { { } } & { { ~ = F ( \xi ) . } } \end{array}
$$

Since $\pmb { F }$ is periodic, it has a Fourier series, $\sum \alpha _ { n } e ^ { i n x }$ , where the Fourier coefficients are given by $\begin{array} { r } { \alpha _ { n } = ( 1 / 2 \pi ) \int _ { 0 } ^ { 2 \pi } F ( \xi ) e ^ { - i n \xi } d \xi } \end{array}$ Thus, the orthonormality condition, (5.26), is equivalent to $\alpha _ { - n } = \delta _ { n 0 }$ , which in turn is equivalent to the statement $F ( \xi ) = 1$ This completes the proof. $\bullet$

An Interesting Identity. As an application, there is an interesting and useful formula that we can derive using this theorem. Recall that the Haar scaling function $\phi$ equals 1 on the unit interval and zero everywhere else, and so its Fourier transform is

$$
\begin{array} { c } { { \hat { \phi } ( \xi ) = \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \int _ { 0 } ^ { 1 } e ^ { - i x \xi } d x } } \\ { { = \displaystyle \frac { e ^ { - i \xi } - 1 } { - \sqrt { 2 \pi } i \xi } . } } \end{array}
$$

With a little algebra, we obtain

$$
| \hat { \phi } ( \xi ) | ^ { 2 } = \frac { 1 - \cos \xi } { \pi \xi ^ { 2 } } = \frac { 1 } { 2 \pi } \left( \frac { \sin ( \xi / 2 ) } { \xi / 2 } \right) ^ { 2 } .
$$

Since $\{ \phi ( x - k ) , k \in Z \}$ is an orthonormal set of functions, Theorem 5.18 implies

$$
\sum _ { k \in Z } { \frac { \sin ^ { 2 } \left( { \frac { \xi } { 2 } } + \pi k \right) } { \left( { \frac { \xi } { 2 } } + \pi k \right) ^ { 2 } } } = 1 .
$$

Sinice $\sin ^ { 2 } x$ is $\pmb { \pi }$ $\sin ^ { 2 } \frac { \xi } { 2 }$ Dividing by this and simplifying results in the formula

$$
\csc ^ { 2 } { \frac { \xi } { 2 } } = \sum _ { k \in Z } { \frac { 4 } { \left( \xi + 2 \pi k \right) ^ { 2 } } } .
$$

This formula is well known, and it is usually derived via techniqucs from complex analysis. We will apply it in Exercise 10 to get a second scaling function for the linear spline multiresolution analysis.

# 5.3.3 The Scaling Equation via the Fourier Transform

The scaling condition, $\begin{array} { r } { \phi ( x ) = \sum _ { k } p _ { k } \phi ( 2 x - k ) } \end{array}$ can also be recast in terms of the Fourier transform.

THeOReM 5.19 The scaling condition $\begin{array} { r } { \phi ( { \boldsymbol x } ) = \sum _ { \boldsymbol k } p _ { \boldsymbol k } \phi ( 2 { \boldsymbol x } - { \boldsymbol k } ) } \end{array}$ is equivalent to

$$
\hat { \phi } ( \xi ) = \hat { \phi } ( \xi / 2 ) P ( e ^ { - i \xi / 2 } )
$$

where the polynomial $P$ is given by

$$
P ( z ) = { \frac { 1 } { 2 } } \sum _ { k \in z } p _ { k } z ^ { k } .
$$

Proof We take the Fourier transform of both sides of the equation $\phi ( { \pmb x } ) =$ $\begin{array} { r l } { \sum _ { k } p _ { k } \phi ( 2 x - k ) } \end{array}$ and then use Theorem 2.6 to obtain

$$
\hat { \phi } ( \xi ) = \frac 1 2 \sum _ { k \in \cal Z } \hat { \phi } ( \xi / 2 ) p _ { k } e ^ { - i k ( \xi / 2 ) } = \widehat { \phi } ( \xi / 2 ) P ( e ^ { - i \xi / 2 } )
$$

where $\begin{array} { r } { P ( z ) = ( 1 / 2 ) \sum _ { k } p _ { k } z ^ { k } } \end{array}$ , as claimed.

Suppose $\phi$ satisfies the scaling condition. Using Theorem 5.19 in an iterative fashion, we obtain the following

$$
\begin{array} { c } { { \hat { \phi } ( \xi ) = P ( e ^ { - i \xi / 2 } ) \dot { \phi } ( \xi / 2 ) } } \\ { { \dot { \phi } ( \xi / 2 ) = P ( e ^ { - i \xi / 2 ^ { 2 } } ) \dot { \phi } ( \xi / 2 ^ { 2 } ) } } \end{array}
$$

and so

$$
\hat { \phi } ( \xi ) = P ( e ^ { - i \xi / 2 } ) P ( e ^ { - i \xi / 2 ^ { 2 } } ) \dot { \phi } ( \xi / 2 ^ { 2 } ) .
$$

Continuing in this manner, we obtain

$$
\begin{array} { l } { { \displaystyle { \dot { \phi } } ( \xi ) = P ( e ^ { - i \xi / 2 } ) \cdot \cdot \cdot P ( e ^ { - i \xi / 2 ^ { n } } ) { \hat { \phi } } ( \xi / 2 ^ { n } ) } } \\ { { \displaystyle ~ = \left( \prod _ { j = 1 } ^ { n } P ( e ^ { - i \xi / 2 ^ { j } } ) \right) { \hat { \phi } } ( \xi / 2 ^ { n } ) . } } \end{array}
$$

For a given scaling function $\phi$ , the preceding equation holds for each value of $\pmb { n }$ . In the limit, as $\textstyle n \to \infty$ , this equation becomes

$$
\hat { \phi } ( \xi ) = \prod _ { j = 1 } ^ { \infty } P ( e ^ { - i \xi / 2 ^ { j } } , \quad \hat { \phi } ( 0 ) .
$$

If $\phi$ satisfies the normalization condition $\begin{array} { r l } { \int \phi ( x ) d x = } & { { } \operatorname { t h e n } \hat { \phi } ( 0 ) = 1 / \sqrt { 2 \pi } } \end{array}$ and so

$$
\hat { \phi } ( \xi ) = \frac { 1 } { \sqrt { 2 \pi } } \prod _ { j = 1 } ^ { \infty } P ( e ^ { - i \xi / 2 ^ { j } } ) .
$$

This provides a formula for the Fourier transform of the scaling function $\phi$ in terms of the scaling polynomial $P$ This formula is of limited practical use for the construction of $\dot { \phi }$ since infinite products are difficult to compute. In addition, the inverse Fourier transform would have to be used to recover $\phi$ from its Fourier transform. Nevertheless, it is useful theoretically, as we see later.

Given a multiresolution analysis generated by a function $\phi$ satisfying the scaling condition $\begin{array} { r } { \phi ( x ) = \sum _ { k } p _ { k } \phi ( 2 x - k ) } \end{array}$ , the associated wavelet, $\psi$ , satisfies the following equation (see Theorem 5.10):

$$
\psi ( x ) = \sum _ { k \in Z } ( - 1 ) ^ { k } { \overline { { p } } } _ { 1 - k } \phi ( 2 x - k ) .
$$

$$
Q ( z ) = - z { \overline { { P ( - z ) } } } .
$$

For $| z | = 1$ $\begin{array} { r } { { \bf \Pi } = 1 , Q ( z ) = ( 1 / 2 ) \sum _ { k } ( - 1 ) ^ { k } \overline { { p } } _ { 1 - k } z ^ { k } } \end{array}$ (see Exercise 13). The same arguments given in the proof of Theorem 5.19 show that

$$
\hat { \psi } ( \xi ) = \hat { \phi } ( \xi / 2 ) Q ( e ^ { - i \xi / 2 } ) .
$$

The previous two theorems can be combined to give the following necessary condition on the polynomial $P ( z )$ for the existence of a multiresolution analysis.

THEoREM 5.20 Suppose the function $\phi$ satisfies the orthonormality condition, $\begin{array} { r } { \int \phi ( x - k ) \phi ( x - l ) d x = \delta _ { k l } } \end{array}$ , and the scaling condition, $\begin{array} { r } { \phi ( x ) = \sum _ { k } p _ { k } \phi ( 2 x - } \end{array}$ $\boldsymbol { k } )$ .Then the polynomial $\begin{array} { r } { P ( z ) = \sum _ { k } p _ { k } z ^ { k } } \end{array}$ satisfies the following equation:

$$
| P ( z ) | ^ { 2 } + | P ( - z ) | ^ { 2 } = 1 \quad f o r z \in C \ w i t h \ | z | = 1
$$

or, equivalently,

$$
\begin{array} { r } { | P ( e ^ { - i t } ) | ^ { 2 } + | P ( e ^ { - i ( t + \pi ) } ) | ^ { 2 } = 1 \quad f o r 0 < t < 2 \pi . } \end{array}
$$

Proof In view of Theorem 5.18 $\phi$ satisfies the orthonormality condition then

$$
\sum _ { k \in Z } | { \hat { \phi } } ( \xi + 2 \pi k ) | ^ { 2 } = 1 / 2 \pi \quad { \mathrm { f o r ~ a l l ~ } } \xi \in R .
$$

If $\phi$ satisfies the scaling condition, then (Theorem 5.19)

$$
\hat { \phi } ( \xi ) = \hat { \phi } ( \xi / 2 ) P ( e ^ { - i \xi / 2 } ) .
$$

Dividing the sum in (5.31) into even and odd indices and using (5.32), we have

$$
\begin{array} { r l } { \iota _ { \tau } ^ { - } } & { = \displaystyle \sum _ { k \in \mathcal { L } } | \dot { \phi } ( \xi + 2 \pi k ) | ^ { 2 } } \\ & { \underset { k \in \mathcal { Z } } { \sum } | \dot { \phi } ( \xi + ( 2 \eta ) 2 \pi ) | ^ { 2 } + \displaystyle \sum _ { k \in \mathcal { Z } } | \dot { \phi } ( \xi + ( 2 t + 1 ) 2 \pi ) | ^ { 2 } } \\ & { \underset { k \in \mathcal { Z } } { \sum } \left( | P ( e ^ { - i ( \xi / 2 + 2 \pi k ) } ) | ^ { 2 } | \dot { \phi } ( \xi / 2 + ( 2 \pi ) \pi ) | ^ { 2 } + \right. } \\ & { \left. | P ( e ^ { - i ( \xi / 2 + ( 4 t + 1 ) \pi ) ) } ) | ^ { 2 } | \dot { \phi } ( \xi / 2 + \pi ( 2 t + 1 ) ) | ^ { 2 } \right) } \\ & { = | P ( e ^ { - i ( \xi / 2 ) } ) | ^ { 2 } \underset { k \in \mathcal { Z } } { \sum } | \dot { \phi } ( \xi / 2 + 2 \pi \tau ) | ^ { 2 } + } \\ & { | P ( - e ^ { - i ( \xi / 2 ) } ) | _ { \mathcal { F } _ { \epsilon \epsilon \mathcal { Z } } } ^ { 2 } | \dot { \phi } ( \xi / 2 + \pi ) + 2 \pi | ) | ^ { 2 } . } \end{array}
$$

where the last equation uses $e ^ { - 2 l \pi i } = 1$ and $e ^ { - \pi i } = - 1$ The two sums appearing on the right are both $1 / 2 \pi$ (using Theorem 5.18 with $\pmb { \xi }$ relaced by $\pmb { \xi } / 2$ and $\pmb { \xi } / 2 + \pmb { \pi } )$ . Therefore, the previous equations reduce to

$$
1 = | P ( e ^ { - i \xi / 2 } ) | ^ { 2 } + | P ( - e ^ { - i \xi / 2 } ) | ^ { 2 } .
$$

Since this equation holds for all $\xi \in R$ , we conclude that $| P ( z ) | ^ { 2 } + | P ( - z ) | ^ { 2 } = 1$ for all complex numbers $\pmb { z }$ with $| z | = 1$ , as desired. . $\bullet$

The following theorem is the analogue of Theorem 5.20 for the function $\psi$ and its associated scaling polynomial $\pmb { Q }$ . Its proof is similar to the proof of the previous theorem and will be left to the reader (see Exercise 14).

THEOREM 5.21 Suppose the function $\phi$ satisfies the orthonormality condition, $\begin{array} { r } { \int \phi ( { \boldsymbol { x } } - { \boldsymbol { k } } ) \phi ( { \boldsymbol { x } } - { \boldsymbol { l } } ) d { \boldsymbol { x } } = \delta _ { { \boldsymbol { k } } { \boldsymbol { l } } } } \end{array}$ , and the scaling condition, $\begin{array} { r } { \phi ( x ) = \sum _ { k } p _ { k } \phi ( 2 x - } \end{array}$ $\boldsymbol { k } )$ . Suppose $\begin{array} { r } { \psi ( { \boldsymbol { x } } ) = \sum _ { { \boldsymbol { k } } } q _ { \boldsymbol { k } } \phi ( 2 { \boldsymbol { x } } - { \boldsymbol { k } } ) } \end{array}$ . Let $\begin{array} { r } { Q ( z ) = \sum _ { k } q _ { k } z ^ { k } } \end{array}$ . Then the following two statements are equivalent:

$$
\begin{array} { r } { \int { \psi ( x - k ) \phi ( x - l ) d x } = 0 f o r \ a l l \ k , l \in Z \ } \end{array}
$$

Another way to state Theorems 5.20 and 5.21 is that the matrix

$$
{ \cal M } = \left( \begin{array} { l l } { { P ( z ) } } & { { P ( - z ) } } \\ { { Q ( z ) } } & { { Q ( - z ) } } \end{array} \right)
$$

associated to an orthonormal scaling function and orthonormal wavelet must be unitary (that is, $M M ^ { * } = I )$ .

# EXAMPLE 5.22

Here, we examine the special case of the Haar scaling function that is one on the unit interval and zero everywhere else. For this example, $p _ { 0 } = p _ { 1 } = 1$ (all other $\pmb { p _ { k } = 0 }$ and so

$$
P ( z ) = ( 1 + z ) / 2 .
$$

We check the statements of Theorems 5.19 and 5.20 for this example. Using the formula for the Fourier transform of the Haar scaling function given in equation (5.27), we obtain

$$
P ( e ^ { - i \xi / 2 } ) \hat { \phi } ( \xi / 2 ) = \frac { 1 } { 2 } ( 1 + e ^ { - i \xi / 2 } ) \left( \frac { e ^ { - i \xi / 2 } - 1 } { - i \sqrt { 2 \pi } \xi / 2 } \right) = \frac { e ^ { - i \xi } - 1 } { - \sqrt { 2 \pi } i \xi }
$$

So $\hat { \phi } ( \xi ) = P ( e ^ { - i \xi / 2 } ) \hat { \phi } ( \xi / 2 )$ , as stated in Theorem 5.19.

Also note that

$$
{ \begin{array} { r l } & { | P ( z ) | ^ { 3 } + | P ( - z ) | ^ { 2 } = { \frac { | 1 + z | ^ { 3 } } { 4 } } + { \frac { | 1 - z | ^ { 2 } } { 4 } } } \\ & { \qquad = { \frac { 1 + 2 \operatorname { R e } \{ z \} + | z | ^ { 2 } } { 4 } } + { \frac { 1 - 2 \operatorname { R e } \{ z \} + | z | ^ { 2 } } { 4 } } } \\ & { \qquad = 1 \quad { \mathrm { f o r ~ } } z \in \operatorname { C } { \mathrm { ~ w i t h ~ } } | z | ^ { - } = 7 } \end{array} }
$$

in agreement with Theorem 5.20.

In a similar manner, the Fourier transform of the Haar wavelet is

$$
\hat { \psi } ( \xi ) = \frac { ( e ^ { - i \xi / 2 } - 1 ) ^ { 2 } } { i \sqrt { 2 \pi } \xi }
$$

Its scaling polynomial is $Q ( z ) = ( 1 - z ) / 2$ and so

$$
\hat { \phi } ( \xi / 2 ) Q ( e ^ { - i \xi / 2 } ) = \frac { ( e ^ { - i \xi / 2 } - 1 ) } { - i \sqrt { 2 \pi } \xi / 2 } \frac { ( 1 - e ^ { - i \xi / 2 } ) } { 2 } = \hat { \psi } ( \xi )
$$

in agreement with equation (5.30)

# 5.3.4 Iterative Procedure for Constructing the Scaling Function

The previous theorem states that if $\phi$ exists, its scaling polynomial $P$ mnust satisfy the equation $| P ( z ) | ^ { 2 } + | P ( - z ) | ^ { 2 } = 1$ for $| z | = 1$ So one strategy for constructing a scaling function $\phi$ is to construct a polynomial $P$ that satisfics this equation and then construct a function $\phi$ so that it satisfies the scaling equation $\begin{array} { r } { \phi ( x ) = \sum _ { k } p _ { k } \phi ( 2 x - k ) } \end{array}$ .

Let us assume that $P$ has been constructed to satisfy Theorem 5.20 and that $P ( 1 ) = 1$ . An example of such a $\pmb { P }$ will be given in the next section. The strategy for constructing the scaling function $\phi$ associated with $_ { r }$ is given by the following iterative process. Let the Haar scaling function be denoted by

$$
\phi _ { 0 } ( x ) = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } 0 \leq x < 1 } \\ { 0 , } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

The Haar scaling function already satisfies the orthonormality property. Then define

$$
\phi _ { 1 } ( x ) = \sum _ { k \in Z } p _ { k } \phi _ { 0 } ( 2 x - k ) .
$$

In general, define $\phi _ { n }$ in terms of $\phi _ { n - 1 }$ by

$$
\phi _ { n } ( x ) = \sum _ { k \in Z } p _ { k } \phi _ { n - 1 } ( 2 x - k ) .
$$

In the next theorem, we show that the $\phi _ { n }$ converge, as $\textstyle n \to \infty$ , to a function denoted by $\phi$ . By taking limits of the preceding equation as $\pmb { n }  \infty$ , we obtain

$$
\phi ( x ) = \sum _ { k \in Z } p _ { k } \phi ( 2 x - k )
$$

and so $\phi$ satisfies the desired scaling condition. Since $\phi _ { 0 }$ satisfies the orthonormality condition, there is some hope that $\phi _ { 1 }$ and $\phi _ { 2 } , \phi _ { 3 } \ldots$ and eventually $\phi$ will also satisfy the orthonormality condition. This procedure turns out to work, under certain additional assumptions on $\pmb { P }$ .

THEOREM 5.23 Suppose $\begin{array} { r } { P ( z ) = ( 1 / 2 ) \sum _ { k } p _ { k } z ^ { k } } \end{array}$ is a polynomial that satisfies the following conditions:

$$
\begin{array} { l r } { \bullet P ( 1 ) = 1 } \\ { \bullet | P ( z ) | ^ { 2 } + | P ( - z ) | ^ { 2 } = 1 f o r | z | = 1 } \\ { \bullet | P ( e ^ { i t } ) | > 0 f o r | t | \leq \pi / 2 } \end{array}
$$

Let $\phi _ { 0 } ( { \pmb x } )$ be the Haar scaling function and let $\begin{array} { r } { \phi _ { n } ( x ) = \sum _ { k } p _ { k } \phi _ { n - 1 } ( 2 x - k ) } \end{array}$ for $\pmb { n } \geq 1$ . Then the sequence $\phi _ { n }$ converges pointwise and in $L ^ { 2 }$ to a function $\phi$ , which satisfies the orthonormality condition

$$
\int _ { - \infty } ^ { \infty } \phi ( x - n ) \phi ( x - m ) d x = \delta _ { n m }
$$

and which satisfies the scaling equation, $\begin{array} { r } { \phi ( { \boldsymbol { x } } ) = \sum _ { \boldsymbol { k } } p _ { \boldsymbol { k } } \phi ( 2 { \boldsymbol { x } } - { \boldsymbol { k } } ) } \end{array}$ .

Proof A formal proof of the convergence part of the theorem is technical and is contained in Appendix A. Once convergence has been established, $\phi$ automatically satisfies the scaling condition, as already mentioned. Here, we give an explanation of why $\phi$ satisfies the normalization and orthonormality conditions. We first start with $\phi _ { 1 }$ , which by (5.33) is

$$
\phi _ { 1 } ( x ) = \sum _ { k \in Z } p _ { k } \phi _ { 0 } ( 2 x - k ) .
$$

This is equivalent to the following Fourier transform equation:

$$
\hat { \phi _ { 1 } } ( \xi ) = P ( e ^ { - i \xi / 2 } ) \hat { \phi _ { 0 } } ( \xi / 2 )
$$

by the same argument as in the proof of Theorem 5.19. Since $\begin{array} { r } { \hat { \phi } _ { 0 } ( 0 ) = \frac { 1 } { \sqrt { 2 \pi } } } \end{array}$ and $P ( 1 ) = 1 ,$ clearly $\begin{array} { r } { \hat { \phi } _ { 1 } ( 0 ) = \frac { 1 } { \sqrt { 2 \pi } } } \end{array}$ and so $\phi _ { 1 }$ satisies th orlization coo.

By (5.35), we have

$$
\sum _ { k \in Z } | \hat { \phi } _ { 1 } ( \xi + 2 \pi k ) | ^ { 2 } = \sum _ { k \in Z } | P ( e ^ { - i \xi / 2 + \pi k i } ) | ^ { 2 } | \hat { \phi } _ { 0 } ( \xi / 2 + \pi k ) | ^ { 2 } .
$$

Dividing the sum on the right into even and odd indices and using the same argument as in the proof of Theorem 5.20, we obtain

$$
\begin{array} { l } { { \displaystyle \sum _ { k \in { \cal Z } } | \hat { \phi } _ { 1 } ( \xi + 2 \pi k ) | ^ { 2 } = \sum _ { l \in { \cal Z } } | P ( \mathrm { e } ^ { - i \xi / 2 + 2 \pi i \bar { i } } ) | ^ { 2 } | \hat { \phi } _ { 0 } ( \xi / 2 + 2 \pi l ) | ^ { 2 } } } \\ { { \displaystyle \qquad + \sum _ { l \in { \cal Z } } | P ( \mathrm { e } ^ { - i \xi / 2 + \pi ( 2 t + 1 ) \bar { i } } ) | ^ { 2 } | \hat { \phi } _ { 0 } ( \xi / 2 + \pi ( 2 l + 1 ) ) | ^ { 2 } } } \\ { { \displaystyle \qquad = | P ( e ^ { - i \xi / 2 } ) | ^ { 2 } \sum _ { l \in { \cal Z } } | \hat { \phi } _ { 0 } ( \xi / 2 + 2 \pi l ) | ^ { 2 } } } \\ { { \displaystyle \qquad + \ | P ( - e ^ { - i \xi / 2 } ) | ^ { 2 } \sum _ { l \in { \cal Z } } | \hat { \phi } _ { 0 } ( \xi / 2 + \pi + 2 \pi l ) | ^ { 2 } . } } \end{array}
$$

Since $\phi _ { 0 }$ satisfies the orthonormality condition, both sums on the right side equal $1 / 2 \pi$ (by Theorem 5.18). Therefore,

$$
\begin{array} { r l r } { \displaystyle \sum _ { k \in Z } \vert \hat { \phi } _ { 1 } ( \xi + 2 \pi k ) \vert ^ { 2 } = \frac { 1 } { 2 \pi } \left( \vert P ( e ^ { - i \xi / 2 } ) \vert ^ { 2 } + \vert P ( - e ^ { - i \xi / 2 } ) \vert ^ { 2 } \right) } & { } & \\ { = \displaystyle \frac { 1 } { 2 \pi } \mathrm { \quad } \mathrm { b y ~ t h e ~ a s s u m p t i o n ~ o n ~ } P . } \end{array}
$$

By Theorem 5.18, $\phi _ { 1 }$ satisfies the orthonormality condition. The same argument as before shows that if $\phi _ { \mathfrak { n } - \mathfrak { L } }$ satisfies the normalization and orthonormality conditions, then so does $\phi _ { n }$ .By induction, all the $\phi _ { n }$ satisfy these conditions. After taking limits, we conclude that $\phi$ satisfies these conditions as well. $\bullet$

# EXAMPLE 5.24

In the case of Haar, $p _ { 0 } = p _ { 1 } = 1$ and all other $\pmb { p _ { k } } = \pmb { 0 }$ In this case, $P ( z ) =$ $( 1 + z ) / 2$ Clearly $P ( 1 ) = 1$ , and in Example 5.22 we showed that $| P ( z ) | ^ { 2 } +$ $| P ( - z ) | ^ { 2 } = 1$ for $| z | = 1$ Also, $| P ( e ^ { i t } ) = ( 1 + e ^ { i t } ) / 2 | > 0$ for all $| t | < \pi$ . So all the conditions of Theorem 5.23 are satisfied. The iterative algorithm in this theorem starts with the Haar scaling function for $\phi _ { 0 }$ For the Haar scaling coefficients, $\scriptstyle p _ { 0 } = p _ { 1 } = 1$ , all the $\phi _ { k }$ equal $\phi _ { 0 }$ . For example, from (5.33),

$$
\begin{array} { c l c r } { { \phi _ { 1 } ( x ) = p _ { 0 } \phi _ { 0 } ( 2 x ) + p _ { 1 } \phi _ { 0 } ( 2 x - 1 ) } } \\ { { \ } } \\ { { \qquad = \phi _ { 0 } ( 2 x ) + \phi _ { 0 } ( 2 x - 1 ) } } \\ { { \ } } & { { \qquad = \phi _ { 0 } ( x ) \quad \mathrm { f r o m \ ( 4 . 1 2 ) . } } } \end{array}
$$

Likewise, $\phi _ { 2 } = \phi _ { 1 } = \phi _ { 0 }$ , and so forth. This is not surprising since the iterative algorithm uses the scaling equation to produce $\phi _ { k }$ from $\phi _ { k - 1 }$ . If the Haar scaling equation is used, with the Haar scaling function as $\phi _ { 0 }$ , then the iterative algorithm will keep reproducing $\phi _ { 0 }$ .

![](images/db5749a6073f3aa273e902b9468642739abb38169e53ac33fc534d9146093d3f.jpg)  
Figure 18 Plot of $\phi _ { 0 }$

# EXAMPLE 5.25

Daubechies Example Let $P ( z ) = ( 1 / 2 ) \sum _ { k } p _ { k } z ^ { k }$ , where

$$
p _ { 0 } = { \frac { 1 + { \sqrt { 3 } } } { 4 } } p _ { 1 } = { \frac { 3 + { \sqrt { 3 } } } { 4 } } p _ { 2 } = { \frac { 3 - { \sqrt { 3 } } } { 4 } } p _ { 3 } = { \frac { 1 - { \sqrt { 3 } } } { 4 } } .
$$

As established in Exercise 11, $P ( z )$ satisfies the conditions in Theorem 5.23. Therefore, the iterative scheme stated in Theorem 5.23 converges to a scaling

![](images/b4ece2e275c303d2c81bc6b9e28c157b8f84fa7e889a6cae5b64f86d7bb3e7c3.jpg)  
Figure 19 Plot of $\phi _ { 1 }$ for Daubechies

![](images/270c8e118030b98ae688a9ce6567e0e2d0022620e84d13a5d304dd1b809df14d.jpg)  
Figure 20 Plot of $\phi _ { 2 }$ for Daubechies

function $\phi$ whose construction is due to Daubechies. Plots of the first four iterations, $\phi _ { 0 }$ $\phi _ { 1 }$ , $\phi _ { 2 }$ and $\phi _ { 4 }$ , of this process are given in Figures 18 through 21.

In the next chapter, we motivate the calculation of this choif ${ \pmb p _ { 0 } }$ , $\pmb { p _ { 3 } }$ and other similar choices of $\pmb { x } _ { \pmb { k } }$ .

![](images/19b5810d9fee79a5bba4cca4f83853969700ed58b72bcf1e5e4a63b3826f7234.jpg)  
Figure 21 Plot of $\phi _ { 4 }$ for Daubechies

# 5.4 Exercises

1. For each function $\pmb { \mathscr { s } }$ plot $g ( x ) , g ( x + 1 ) , 2 ^ { 1 / 2 } g ( 2 x - 3 )$ ,and $\frac { 1 } { 2 } g ( \frac { 1 } { 4 } x - 1 )$

a)g(x)=e-x^{2\$   
(b) $\begin{array} { r } { g ( x ) = \frac { 1 } { 1 + x ^ { 2 } } } \end{array}$   
(c) $g ( x ) = \left\{ { \begin{array} { l l } { ( 1 - x ^ { 2 } ) ^ { 2 } } & { | x | < 1 } \\ { 0 } & { | x | \geq 1 } \end{array} } \right.$   
(d) $g ( x ) = { \frac { \sin ( \pi x ) } { \pi x } }$

2The support of a complex-valued function $\pmb { f }$ is the smallest closed set that contains the set where $f \neq 0$ We denote the support of $\pmb { f }$ by supp $( f )$ . We say that $\pmb { f }$ is compactly supported or has compact support if $\mathbf { s u p p } ( f )$ is contained in a bounded set. Find the support of the following functions. Which are compactly supported?

(a) $f ( x ) : = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } k < x < k + 1 { \mathrm { ~ f o r ~ } } k { \mathrm { ~ o d d } } } \\ { 0 } & { { \mathrm { i f ~ } } k \leq x \leq k + 1 { \mathrm { ~ f o r ~ } } k { \mathrm { ~ e v e n } } } \end{array} \right. }$ (b) $g ( x ) : = { \left\{ \begin{array} { l l } { x ( 1 - x ) } & { { \mathrm { i f ~ } } 0 \leq x \leq 3 } \\ { 1 } & { { \mathrm { i f ~ } } x > 3 } \\ { - 1 } & { { \mathrm { i f ~ } } - 5 < x < 0 } \\ { 0 } & { { \mathrm { i f ~ } } x \leq - 5 } \end{array} \right. }$

$$
h ( r , \theta ) : = { \left\{ \begin{array} { l l } { r ^ { 2 } ( 1 - r ^ { 2 } ) } & { { \mathrm { i f ~ } } 0 \leq r < 1 { \mathrm { ~ a n d ~ } } 0 \leq \theta < 2 \pi } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

3. Parseval's equation came up in connection with Fourier series, in Theorem 1.40. It holds under much more general circumstances, however. Let $V$ be a complex inner product space with an orthonormal basis $\{ u _ { k } \} _ { k = 1 } ^ { \infty }$ . Show that if $f \in V$ and $\pmb { \mathscr { s } } \in V$ have the expansions

$$
f = \sum _ { k = 1 } ^ { \infty } a _ { k } u _ { k } \quad { \mathrm { a n d } } \quad g = \sum _ { k = 1 } ^ { \infty } b _ { k } u _ { k } ,
$$

then

$$
\langle f , g \rangle = \sum _ { k = 1 } ^ { \infty } a _ { k } { \bar { b } } _ { k } .
$$

This is called Parseval's equation. The indexing $\pmb { k } = \pmb { 1 } , \pmb { 2 } , \dots$ is unimportant. Any index set (including double indexing) can be used just long as the index set is countable.

4.Use Parseval's equation from Exercise 3 to establish the following equations.

(a) Equation 1 in Theorem 5.9. (b) Show that

$$
\langle \psi _ { 0 m } , \psi _ { 0 l } \rangle = \frac { 1 } { 2 } \sum _ { k \in \cal Z } \overline { { p _ { 1 - k + 2 m } } } p _ { 1 - k + 2 l } ,
$$

where $\psi$ is defined in equation (5.5). Hint: Change summation indices in equation (5.5) and use the fact that $\{ 2 ^ { 1 / 2 } \phi ( 2 x - k ) \} _ { k \in Z }$ is orthonormal.

Show that

$$
\langle \phi _ { 0 l } , \psi _ { 0 m } \rangle = { \frac { 1 } { 2 } } \sum _ { k \in Z } ( - 1 ) ^ { k } p _ { 1 - k + 2 m } p _ { k - 2 l }
$$

where $\psi$ is defined in equation (5.5). Hint: Change summation indices in equation (5.5) and use the fact that $\{ 2 ^ { 1 / 2 } \phi ( 2 x - k ) \} _ { k \in Z }$ is orthonormal.

5. We defined the support of a function in Exercise 2. Show that if the scaling function $\phi$ in a multiresolution analysis has compact support, then there is only a finite number of nonzero coefficients in the scaling relation from Theorem 5.6.

6. Suppose that $\{ V _ { j } : j \in Z \}$ is a multiresolution analysis with scaling function $\phi$ and that $\phi$ is continuous and compactly supported.

Find $\mathbf { \lambda } _ { \mathbf { \lambda } } \mathbf { \lambda } _ { \mathbf { \lambda } } \mathbf { \lambda } _ { \mathbf { \lambda } } \mathbf { \lambda } _ { \mathbf { \lambda } } \mathbf { \lambda } _ { \mathbf { \lambda } } \mathbf { \lambda } _ { \mathbf { \lambda } } \mathbf { \lambda } _ { \mathbf { \lambda } } \mathbf { \lambda } _ { \mathbf { \lambda } } \mathbf { \lambda } _ { \mathbf { \lambda } } \mathbf { \lambda } _ { \lambda } \mathrm { ~ \textbf ~ { ~  ~ } ~ } \mathbf { \lambda } _ { \mathbf { \lambda } } \mathrm { ~ \textbf ~ { ~  ~ } ~ } \mathrm { ~ \bf ~ \lambda } _ { \mathrm { ~ \lambda ~ } }$ , the orthogonal projection onto $V _ { j }$ , of the step function

$$
u ( x ) = \left\{ { \begin{array} { l l } { 1 } & { 0 \leq x \leq 1 } \\ { 0 } & { x < 0 { \mathrm { ~ o r ~ } } x > 1 . } \end{array} } \right.
$$

(b) If $\textstyle \int _ { - \infty } ^ { \infty } \phi ( x ) d x = 0$ , show that for all $j$ sufficiently large, $\begin{array} { r } { \| u - u _ { j } \| \geq \frac { 1 } { 2 } } \end{array}$ (c)Explain why the preceding result implies that $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \phi ( x ) d x \neq 0 . } \end{array}$ .

7. In case the ${ \pmb p } _ { { \pmb k } } ^ { \prime } { \bf s }$ are complex, the quantities $\pmb { \cal E }$ and $o$ , which are defined in connection with the proof of equation (4) in Theorem 5.9, may be complex. Show that even if we allow for this, the equations $| E | ^ { 2 } + | O | ^ { 2 } = 2$ and $\pmb { { \cal E } } + \pmb { { \cal O } } = 2$ have $\scriptstyle { E = O = 1 }$ as their only solution.

8. (Shannon Multiresolution Analysis). For $j \in Z$ ,let $V _ { j }$ be the space of all finite energy signals $\pmb { f }$ for which the Fourier transform $\widehat { f } = 0$ outside of the interval $[ - 2 ^ { j } \pi , 2 ^ { j } \pi ]$ -that is, all $f \in L ^ { 2 } ( R )$ that are band limited and have . $\operatorname { s u p p } ( \widehat { f } ) \subseteq [ - 2 ^ { j } \pi , 2 ^ { j } \pi ]$ .

(a) Show that $\{ V _ { j } \} _ { j \in \mathbb { Z } }$ satisfies properties 1-4 in the definition of a multiresolution analysis, Definition 5.1.

Show that $\phi ( x ) : = \operatorname { s i n c } ( x )$ , where sinc is defined in equation (5.1), satisfies property 5 of Definition 5.1, and so it is a scaling function for .the $V _ { j }$ 's.(Hint: Use the sampling theorem 2.23 to show that $\{ \phi ( { \pmb x } - { \pmb k } ) \}$ is an orthonormal basis for $V _ { 0 }$ )

(c) Show that $\phi$ satisfies the scaling relation

$$
\phi ( x ) = \phi ( 2 x ) + \sum _ { k \in Z } \frac { 2 ( - 1 ) ^ { k } } { ( 2 k + 1 ) \pi } \phi \big ( 2 x - 2 k - 1 \big )
$$

() Find an expansion for the wavelet $\psi$ associated with $\phi$ .   
Find the high- and low-pass decomposition filters, $\pmb { h }$ and l.   
Find the high- and low-pass reconstruction filters, $\widetilde { h }$ and .

9. (Linear Spline Multiresolution Analysis). For $j \in Z$ , let $V _ { j }$ be the space of all finite energy signals $\pmb { f }$ that are continuous and piecewise linear, with possible corners occurring only at the dyadic points $k / 2 ^ { j }$ , $\pmb { k } \in \pmb { Z }$

Show that $\{ V _ { j } \} _ { j \in Z }$ satisfies properties 1-4 in the definition of a multiresolution analysis, Definition 5.1.   
(b) Let $\varphi ( { \pmb x } )$ be the "tent function,"

$$
\begin{array} { l l l } { \varphi ( x ) = } & { x + 1 , } & { - 1 \leq x \leq 0 , } \\ { \varphi ( x ) = } & { 1 - x , } & { 0 < x \leq 1 , } \\ & { 0 , } & { | x | > 1 . } \end{array}
$$

Show that $\{ \varphi ( { \pmb x } - { \pmb k } ) \} _ { { \pmb k } \in { \pmb Z } }$ is a (nonorthogonal) basis for $V _ { 0 }$ .Find the scaling relation for for $\varphi$ .

10. Let $\omega ( x )$ be the tent function from Exercise 9.

Show that

$$
{ \widehat \varphi } ( \xi ) = 2 { \sqrt { \frac { 2 } { \pi } } } { \frac { \sin ^ { 2 } ( \xi / 2 ) } { \xi ^ { 2 } } }
$$

(b) " Show that

$$
\sum _ { k \in Z } \frac { \mathtt { r } } { ( \xi + 2 \pi k ) ^ { 4 } } = \frac { 3 - 2 \sin ^ { 2 } ( \xi / 2 ) } { 4 8 \sin ^ { 4 } ( \xi / 2 ) }
$$

Hint: Differentiate both sides of equation (5.28) twice and simplify.

Verify that the function $\phi$ defined via its Fourier transform,

$$
{ \hat { \phi } } ( \xi ) : = 2 { \sqrt { \frac { 2 } { \pi } } } { \frac { \sin ^ { 2 } ( \xi / 2 ) } { \xi ^ { 2 } { \sqrt { 1 - { \frac { 2 } { 3 } } \sin ^ { 2 } { \frac { \xi } { 2 } } } } } }
$$

is such that $\{ \phi ( { \pmb x } - { \pmb k } ) \} _ { { \pmb k } \in { \pmb Z } }$ is an orthonormal set. [Hint: Use (b) to show that $\begin{array} { r } { \sum _ { k \in \mathcal { Z } } \left| \widehat { \phi } ( \xi + 2 \pi k ) \right| ^ { 2 } = \frac { 1 } { 2 \pi } } \end{array}$ a then pply Theorm5.

11. Let $\begin{array} { r } { P ( z ) = ( 1 / 2 ) \sum _ { k = 0 } ^ { 3 } { p _ { k } z ^ { k } } } \end{array}$ , where

$$
p _ { 0 } = { \frac { 1 + { \sqrt { 3 } } } { 4 } } \quad p _ { 1 } = { \frac { 3 + { \sqrt { 3 } } } { 4 } } \quad p _ { 2 } = { \frac { 3 - { \sqrt { 3 } } } { 4 } } \quad p _ { 3 } = { \frac { 1 - { \sqrt { 3 } } } { 4 } } .
$$

Explicitly show that $P ( z )$ satisfies the conditions in Theorem 5.23. Use a computer algebra system, such as Maple, to establish the equation $| P ( z ) | ^ { 2 } +$ $| P ( - z ) | ^ { 2 } = 1$ for $| z | = 1$ Show by a graph of $\pmb { y } = | P ( e ^ { i t } ) |$ that $| P ( e ^ { i t } ) | > 0$ . for $| t | \leq \pi / 2$ b

12. Suppose $\pmb { f }$ is a continuously differentiable function with $| f ^ { \prime } ( x ) | \leq M$ for $0 \leq x < 1$ Use the following outline to approximate $\pmb { f }$ uniformly to within some specified tolerance, e, by a step function in $V _ { n }$ , the space generated by $\phi ( 2 ^ { n } x - k )$ , $\pmb { k } \in \pmb { Z }$ ,where $\phi$ is the Haar scaling function.

) For $1 \leq j \leq 2 ^ { n }$ , let $a _ { j } = f ( j / 2 ^ { n } )$ and form the step function

$$
f _ { n } ( x ) = \sum _ { j \in Z } a _ { j } \phi ( 2 ^ { n } x - j ) .
$$

Show that $| f ( x ) - f _ { n } ( x ) | \leq \epsilon$ provided that $\pmb { n }$ is greater than $\log _ { 2 } ( M / \epsilon )$

13. Let $\begin{array} { r } { P ( z ) = \sum _ { k } p _ { k } z ^ { k } } \end{array}$ and define

$$
Q ( z ) = - z { \overline { { P ( - z ) } } } .
$$

For $| z | = 1$ ,show that $\begin{array} { r } { Q ( z ) = ( 1 / 2 ) \sum _ { k } ( - 1 ) ^ { k } \overline { { p } } _ { 1 - k } z ^ { k } } \end{array}$ This exercise establishes a formula for the scaling polynomial for the wavelet, $\psi$ from the scaling polynomial, $\pmb { P }$ , for the scaling function.

14. Prove Theorem 5.21 using the ideas in the proof of Theorem 5.20.

15. Prove Theorem 5.12 in the case where the signal $\pmb { f }$ is only piecewise continuous by dividing the support of $\pmb { f }$ into subintervals where $\pmb { f }$ is continuous. Care must be used for the nodes $\scriptstyle { l / 2 ^ { j } }$ that lie near the discontinuities, for then the approximation $f ( x ) \approx f ( l / 2 ^ { j } )$ does not necessarily hold. However, these troublesome nodes are fixed in number and the support of $\phi ( 2 ^ { j } x - l )$ becomes small as $\dot { \pmb { \mathscr { I } } }$ becomes large. So the ${ \pmb { L } } ^ { 2 }$ contribution of the terms . $\alpha _ { l } \phi ( 2 ^ { j } x - l )$ corresponding to the troublesome nodes can be shown to be small as $\pmb { j }$ gets large.

16.Prove the second part of Theorem 5.18 using the proof of the first part as a guide.

17. In Exercise 5, we showed that if $\phi$ has compact support, then only a finite number of ${ \pmb p } _ { { \pmb k } } \mathbf { ^ { \prime } s }$ are nonzero. Use the iterative construction of $\phi$ in equation (5.34) to show that if only a finite number of ${ \pmb p } _ { { \pmb k } } \mathbf { ^ \circ s }$ are nonzero, then $\phi$ has compact support.

18. (Filter Length and Support.) Show that if the ${ \pmb p } _ { { \pmb k } } \mathbf { ^ \prime s }$ in the scaling relation are all zero for $k > N$ and $\pmb { k } < \mathbf { 0 }$ , and if the iterates $\phi _ { n }$ converge to $\phi$ , then $\phi$ has compact support. Find the support of $\phi$ in terms of $\pmb { N }$ .

# Chapter 6

# The Daubechies Wavelets

The wavelets that we have looked at so far—Haar, Shannon, and linear spline wavelets-all have major drawbacks. Haar wavelets have compact support but are discontinuous. Shannon wavelets are very smooth but extend throughout the whole real line, and they decay at infinity very slowly. Linear spline wavelets are continuous, but the orthogonal scaling function and associated wavelet, like the Shannon wavelets, have infinite support; they do, however, decay rapidly at infinity.

These wavelets, together with a few others having similar properties, were the only ones available before Ingrid Daubechies discovered the hierarchy of wavelets that are named after her. The simplest of these is just the Haar wavelet, which is the only discontinuous one. The other wavelets in the hierarchy are compactly supported and continuous. Better still, by going up the hierarchy, they become increasingly smooth; that is, they can have have a prescribed number of continuous derivatives. The wavelet's smoothness can be chosen to satisfy conditions in a particular application. We now turn to Daubechies's construction of the first wavelet past Haar, $\psi _ { 2 }$ .

# 6.1 Daubechies's Construction

Theorem 5.23 lists the three sufficient conditions on the polynomial $\pmb { P }$ that ensures that the iteration scheme just described produces a scaling function. For a given polynomial $P ( z )$ , let

$$
p ( \xi ) = P ( e ^ { - i \xi } ) .
$$

In terms of the of the function $\pmb { p }$ , the three conditions in the hypothesis of Theorem 5.23 can be stated as

$$
\begin{array} { c } { p ( 0 ) = 1 } \\ { \vert p ( \xi ) \vert ^ { 2 } + \vert p ( \xi + \pi ) \vert ^ { 2 } = 1 } \\ { \vert p ( \xi ) \vert > 0 \quad \mathrm { f o r } - \pi / 2 \leq \xi \leq \pi / 2 . } \end{array}
$$

In this section, we describe one polynomial, due to Daubechies, that satisfies (6.1) through (6.3).

From Example 5.22, the polynomial associated with the Haar scaling function is

$$
p _ { 0 } ( \xi ) = P ( e ^ { - i \xi } ) = \frac { 1 + e ^ { - i \xi } } { 2 } = e ^ { - i \xi / 2 } \cos ( \xi / 2 ) .
$$

This choice of ${ \pmb p } _ { \pmb 0 }$ satisfies (6.1) through (6.3). However, the Haar scaling function is discontinuous. One way to generate a continuous scaling function is to take convolution powers. In fact, the convolution of the Haar scaling function with itself can be shown to equal the following continuous linear spline (see Exercise 5 in Chapter 2):

$$
\phi _ { 0 } * \phi _ { 0 } ( x ) = \left\{ \begin{array} { c l } { { 1 - | x - 1 | } } & { { \mathrm { f o r ~ } 0 \leq x \leq 2 } } \\ { { 0 } } & { { \mathrm { o t h e r w i s e } } } \end{array} \right.
$$

(see Figure 1). Now the Fourier transform of a convolution equals the product of the Fourier transforms. In particular, the Fourier transform of $\phi * \phi * \cdots * \phi ($ n times) is $( 2 \pi ) ^ { n / 2 } ( \hat { \phi } ) ^ { n }$ .In view of equation (5.29) for the Fourier transform of the scaling function, we may be first led to ty $p ( \xi ) = p _ { 0 } ( \xi ) ^ { n } = e ^ { - i n \xi / 2 } ( \cos \xi / 2 ) ^ { n }$ for some suitable power of $\pmb { n }$ as the function that generates a continuous scaling function. However, property (6.2) no longer holds (unless $\scriptstyle n \ = 1 ^ { . }$ --the Haar case) and so this first attempt fails.

![](images/3d5afe7b9a2761f1fa5b9664d8c3e276363441a7a257579c8aeb3bdb1658975c.jpg)  
Figure 1 Graph of $\phi _ { 0 } * \phi _ { 0 }$

Instead of simply raising $\pmb { p _ { 0 } }$ to the nth power, we raise both sides of the identity $\cos ^ { 2 } ( \xi / 2 ) + \sin ^ { 2 } ( \xi / 2 ) = 1$ to the nth power. With $\scriptstyle \pmb { n } = \pmb { 3 }$ , we obtain

$$
1 = \left( \cos ^ { 2 } ( \xi / 2 ) + \sin ^ { 2 } ( \xi / 2 ) \right) ^ { 3 }
$$

or

$$
1 = \cos ^ { 6 } ( \xi / 2 ) + 3 \cos ^ { 4 } ( \xi / 2 ) \sin ^ { 2 } ( \xi / 2 ) + 3 \cos ^ { 2 } ( \xi / 2 ) \sin ^ { 4 } ( \xi / 2 ) + \sin ^ { 6 } ( \xi / 2 ) .
$$

Using the identities $\cos ( u ) = \sin ( u + \pi / 2 )$ and $\sin ( u ) = - \cos ( u + \pi / 2 )$ for the last two terms on the right, we have

$$
\begin{array} { r l } & { 1 = \cos ^ { 6 } ( \xi / 2 ) + 3 \cos ^ { 4 } ( \xi / 2 ) \sin ^ { 2 } ( \xi / 2 ) + 3 \sin ^ { 2 } ( ( \xi + \pi ) / 2 ) \cos ^ { 4 } ( ( \xi + \pi ) / 2 ) } \\ & { \phantom { = } + \cos ^ { 6 } ( ( \xi + \pi ) / 2 ) . } \end{array}
$$

If we take

$$
| p ( \xi ) | ^ { 2 } = \cos ^ { 6 } ( \xi / 2 ) + 3 \cos ^ { 4 } ( \xi / 2 ) \sin ^ { 2 } ( \xi / 2 ) ,
$$

then the previous equation becomes

$$
1 = | p ( \xi ) | ^ { 2 } + | p ( \xi + \pi ) | ^ { 2 }
$$

and property (6.) is satisfied. Property (6.3)is also satisfied since $\cos ( \xi / 2 ) \geq$ $1 / { \sqrt { 2 } }$ for $| \xi | \leq \pi / 2$ Also note that $| { \pmb p } ( 0 ) | = 1$ So all that is left is to identify $\pmb { p }$ itself (we have only defined $| p |$ ).First, we rewrite the defining equation for $| { \pmb p } |$ as

$$
\begin{array} { c } { { \vert p ( \xi ) \vert ^ { 2 } = \cos ^ { 4 } ( \xi / 2 ) \left( \cos ^ { 2 } ( \xi / 2 ) + 3 \sin ^ { 2 } ( \xi / 2 ) \right) } } \\ { { = \cos ^ { 4 } ( \xi / 2 ) \vert \cos ( \xi / 2 ) + \sqrt { 3 } i \sin ( \xi / 2 ) \vert ^ { 2 } . } } \end{array}
$$

By taking square roots of this equation, we choose

$$
\begin{array} { r } { p ( \xi ) = \cos ^ { 2 } ( \xi / 2 ) \left( \cos ( \xi / 2 ) + \sqrt { 3 } i \sin ( \xi / 2 ) \right) \alpha ( \xi ) } \end{array}
$$

where ${ \pmb { \alpha } } ( \pmb { \xi } )$ is a complex-valued expression with $| \alpha ( \xi ) | = 1$ that will be chosen later.

To identify the polynomial $\pmb { P }$ [with $p ( \xi ) = P ( e ^ { - i \xi } ) ]$ , we use the identities

$$
\cos ( \xi / 2 ) = { \frac { e ^ { i \xi / 2 } + e ^ { - i \xi / 2 } } { 2 } } \qquad \sin ( \xi / 2 ) = { \frac { e ^ { i \xi / 2 } - e ^ { - i \xi / 2 } } { 2 i } }
$$

to obtain

$$
p ( \xi ) = \frac { 1 } { 8 } ( e ^ { i \xi } + 2 + e ^ { - i \xi } ) \left( e ^ { i \xi / 2 } + e ^ { - i \xi / 2 } + \sqrt { 3 } e ^ { i \xi / 2 } - \sqrt { 3 } e ^ { - i \xi / 2 } \right) \alpha ( \xi ) .
$$

We choose $\alpha ( \xi ) = e ^ { - 3 i \xi / 2 }$ in order to clear all positive and fractional powers in the exponent. Expanding out and collecting terms, we obtain

$$
p ( \xi ) = \left( \frac { 1 + \sqrt { 3 } } { 8 } \right) + e ^ { - i \xi } \left( \frac { 3 + \sqrt { 3 } } { 8 } \right) + e ^ { - 2 i \xi } \left( \frac { 3 - \sqrt { 3 } } { 8 } \right) + e ^ { - 3 i \xi } \left( \frac { 1 - \sqrt { 3 } } { 8 } \right) .
$$

The equation $p ( \xi ) = P ( e ^ { - i \xi } )$ is therefore satisfied by the polynomial

$$
P ( z ) = \left( { \frac { 1 + { \sqrt { 3 } } } { 8 } } \right) + \left( { \frac { 3 + { \sqrt { 3 } } } { 8 } } \right) z + \left( { \frac { 3 - { \sqrt { 3 } } } { 8 } } \right) z ^ { 2 } + \left( { \frac { 1 - { \sqrt { 3 } } } { 8 } } \right) z ^ { 3 } .
$$

Since $\pmb { p }$ satisfies (6.1) through (6.3), $\pmb { P }$ satisfies the hypothesis of Theorem 5.23. Recall that $\begin{array} { r } { P ( z ) = ( 1 / 2 ) \sum _ { k } p _ { k } z ^ { k } } \end{array}$ Therefore, for Daubechies's example,

$$
p _ { 0 } = { \frac { 1 + { \sqrt { 3 } } } { 4 } } \quad p _ { 1 } = { \frac { 3 + { \sqrt { 3 } } } { 4 } } \quad p _ { 2 } = { \frac { 3 - { \sqrt { 3 } } } { 4 } } \quad p _ { 3 } = { \frac { 1 - { \sqrt { 3 } } } { 4 } } .
$$

The Daubechies scaling function, $\phi$ , is found by applying the iterative procedure described in Theorem 5.23. Figures 19 through 21 in Chapter 5 illustrate the first four iterations of this procedure. Figure 2 shows the (approximate) graph of $\phi$ that results from iterating this procedure many times.

![](images/6feab0d4c5a4e9f49d115012c8a046de5c3faaafb9fc0ec82aa74d0cc31128b8.jpg)  
Figure 2 Daubechies scaling function

What about the wavelet $\psi$ that is associated with the Daubechies scaling function $\phi ?$ As shown in Theorem 5.10, once the coefficients, ${ \pmb p } _ { \pmb k }$ ,have been identified and $\phi$ has been constructed, then the associated wavelet is given by the formula

$$
\psi ( x ) = \sum _ { k \in Z } ( - 1 ) ^ { k } p _ { 1 - k } \phi ( 2 x - k ) .
$$

![](images/f3f5fb62363b96b76a1bae9a8fc8d6dac7227af9f0be90659d3ff9d39a1dd916.jpg)  
Figure 3 Daubechies wavelet function

Figure 3 shows the (approximate) graph of the associated wavelct function. Unlike the Haar scaling and wavelet functions, these Daubechies scaling and wavelet functions are continuous. However, they are not differentiable.

# 6.2 Classification, Moments, and Smoothness

Other smoother scaling functions and wavelets can be obtained by choosing a higher power than $\scriptstyle \pmb { \mathscr { n } } = 3$ in equation (6.4). Any odd power, $\begin{array} { r } { n = 2 N - 1 , } \end{array}$ can be used there. In fact, Daubechies showed that for every $N$ there will be $2 N$ nonzero, real scaling coefficients $p _ { 0 } , \ldots , p _ { 2 N - 1 } ,$ resulting in a scaling function and wavelet that are supported on the interval $0 \leq t \leq 2 N - 1$ They are chosen that the crresponding gree ${ \bf 2 } N - { \bf 1 }$ polynomial $\begin{array} { r } { P _ { N } ( z ) : = \frac { 1 } { 2 } \sum _ { k = 0 } ^ { 2 N - 1 } p _ { k } z ^ { k } } \end{array}$ has the factorization

$$
P _ { N } ( z ) = ( z + 1 ) ^ { N } \tilde { P } _ { N } ( z )
$$

where the degree of $\widetilde { P } _ { N }$ is ${ N } - { \bf 1 }$ and $\tilde { P } _ { N } ( - 1 ) \neq 0$ This guarantees that the associated wavelets will have precisely $N$ vanishing moments." We discuss what this means and why it is important later.

Apart from a reversal of the coefficients in $P _ { N }$ (cf. Exercise 1), these coefficients are unique. In the two cases that we have dealt with, $N = 1$ (Haar) and $N = 2$ (Daubechies), the polynomials are $\begin{array} { r } { P _ { 1 } ( z ) = \frac { 1 } { 2 } ( 1 + z ) ^ { 1 } } \end{array}$ and $\begin{array} { r } { P _ { 2 } ( z ) = \left( \frac { 1 + \sqrt { 3 } } { 8 } + \frac { 1 - \sqrt { 3 } } { 8 } z \right) ( 1 + z ) ^ { 2 } } \end{array}$ in (6.6), with $\begin{array} { r } { \widetilde { P } _ { 1 } ( x ) = \frac { 1 } { 2 } } \end{array}$ and $\begin{array} { r } { \widetilde { P } _ { 2 } ( x ) = \frac { 1 + \sqrt { 3 } } { 5 } + \frac { 1 - \sqrt { 3 } } { 5 } z . } \end{array}$ .

The scaling function $\phi _ { N }$ and wavelet $\psi _ { N }$ generated by $P _ { N }$ have Fourier transforms given in terms of infinite products. Because the coefficients of $P _ { N }$ are real, $\overline { { P _ { N } ( - z ) } } = P _ { N } ( - { \bar { z } } )$ Thus from equations (5.29) and (5.30), we have that

$$
\begin{array} { l } { { \hat { \phi } _ { N } ( \xi ) = \displaystyle \frac { 1 } { \sqrt { 2 \pi } } \prod _ { j = 1 } ^ { \infty } P _ { N } ( e ^ { - i \xi / 2 ^ { j } } ) } } \\ { { \hat { \psi } _ { N } ( \xi ) = - e ^ { - i \xi / 2 } P _ { N } ( - e ^ { i \xi / 2 } ) \hat { \phi } _ { N } ( \xi / 2 ) . } } \end{array}
$$

Note that $\hat { \psi } _ { N } ( 0 ) = 0$ ,because $P _ { N } ( - 1 ) = 0$ I $N > 1$ ,we also have $\hat { \psi } _ { N } ^ { \prime } ( 0 ) = 0 ,$ because $P _ { N } ^ { \prime } ( - 1 ) = 0$ In general, by Exercise 2, we have that

$$
\hat { \psi } _ { N } ^ { ( k ) } ( 0 ) = \left\{ \begin{array} { c c } { 0 , } & { k = 0 , \ldots , N - 1 , } \\ { - N ! ( - i / 2 ) ^ { N } \widetilde { P } _ { N } ( - 1 ) / \sqrt { 2 \pi } \neq 0 , } & { k = N . } \end{array} \right.
$$

This gives the following result.

PRoPosITIoN 6.1 For the Daubechies wavelet $\psi _ { N }$ , we have

$$
\int _ { - \infty } ^ { \infty } x ^ { k } \psi _ { N } ( x ) d x = \left\{ \begin{array} { c c } { 0 , } & { k = 0 , \ldots , N - 1 , } \\ { - \left( 2 ^ { - N } N ! / \sqrt { 2 \pi } \right) \widetilde { P } _ { N } ( - 1 ) , } & { k = N . } \end{array} \right.
$$

Proof The proposition follows from equation (6.9) and the Fourier transform property (Theorem 2.6, property 2):

$$
{ \mathcal { F } } [ t ^ { n } f ( t ) ] ( \lambda ) = i ^ { n } { \frac { d ^ { n } } { d \lambda ^ { n } } } { \mathcal { F } } [ f ( t ) ] ( \lambda ) .
$$

Just set ${ \pmb f } = \psi _ { N }$ , $\scriptstyle n = k$ ,and $\lambda = 0$ .

In mechanics, integrals of the form $\textstyle \int _ { - \infty } ^ { \infty } x ^ { k } \rho ( x ) d x$ are called the moments of a mass distribution $\pmb { \rho }$ The term moment carries over to an integral of any function against $x ^ { k }$ We can thus rephrase the proposition by saying that $\psi _ { N }$ has its first $\pmb { N }$ moments vanish. This is usually shortened to saying that $\psi _ { N }$ has $N$ vanishing moments; that they are the first $\pmb { N }$ is understood.

Daubechies wavelets are classified according to the number of vanishing moments they have. The smoothness of the scaling function and wavelet increase with the number of vanishing moments. The $N = 1$ case is the same as the Haar case; both scaling function and wavelet are discontinuous. The $N = 2$ Daubechies scaling function and wavelet are continuous but certainly do not have smooth derivatives. In the $N = 3$ case, both are continuously differentiable. When $\pmb { N }$ is large, the number of continuous derivatives that $\phi _ { N }$ and $\psi _ { N }$ have is roughly $\frac { N } { 5 }$ So, to get 10 derivatives, we need to take $N \approx 5 0$ In the following table, we list approximate scaling coefficients for the Daubechies wavelets, with $N$ going from 1 to 4. Of course, the scaling coefficients given for ${ \pmb { N } } = { \pmb { 2 } }$ are just the decimal approximations for those found in (6.5).

![](images/e0c83476089b3546e96e5174908002e24d34201b9043f218df9dd9a934e9eaf9.jpg)

Why is it useful to have vanishing moments? The short answer is that vanishing moments are a key factor in many wavelet applications—compression, noise removal, singularity detection, for example.

To understand this better, let's look closely at the $N = 2$ case. According to equation (6.10) with $N _ { \cdot } = 2 ,$ the first two moments $( k = 0 , 1$ vanish. The $\scriptstyle { k = 2 }$ moment is $- \left( 2 ^ { - 1 } / \sqrt { 2 \pi } \right) \widetilde { P } _ { 2 } ( - 1 )$ From our earlier discussion, we see that $\begin{array} { r } { \widetilde { P } _ { 2 } ( - 1 ) = \frac { 1 + \sqrt { 3 } } { 8 } - \frac { 1 - \sqrt { 3 } } { 8 } = \frac { \sqrt { 3 } } { 4 } } \end{array}$ Thus, for the third $( k = 2 )$ moment, we have

$$
\int _ { - \infty } ^ { \infty } x ^ { 2 } \psi _ { 2 } ( x ) d x = - \frac { 1 } { 8 } \sqrt { \frac { 3 } { 2 \pi } } .
$$

We want to use these moments to approximate the wavelet coefficients for smooth signals and show that these coefficients will be small when the level $\dot { \jmath }$ is high. If $\pmb { f }$ is a smooth, twice continuously differentiable signal, then its ${ \dot { \jmath } } , k$ -wavelet coefficient is

$$
\begin{array} { c } { { b _ { k } ^ { j } = \displaystyle \int _ { - \infty } ^ { \infty } f ( x ) 2 ^ { j / 2 } \psi _ { 2 } ( 2 ^ { j } x - k ) d x } } \\ { { \ } } \\ { { = \displaystyle \int _ { 0 } ^ { 3 \cdot 2 ^ { - j } } f ( x + 2 ^ { - j } k ) 2 ^ { j / 2 } \psi _ { 2 } ( 2 ^ { j } x ) d x . } } \end{array}
$$

If $\boldsymbol { j }$ is large enough, the interval over which we are integrating will be small, and we may then replace $f ( x + 2 ^ { - j } k )$ by its quadratic Taylor polynomial in $x , f ( x + 2 ^ { - j } k ) \approx f ( 2 ^ { - j } k ) + x f ^ { \prime } ( 2 ^ { - j } k ) + { \textstyle \frac { 1 } { 2 } } x ^ { 2 } f ^ { \prime \prime } ( 2 ^ { - j } k )$ .Doing this, we get the following approximation for $\boldsymbol { b } _ { \boldsymbol { k } } ^ { j }$ :

$$
b _ { k } ^ { j } \approx \int _ { 0 } ^ { 3 \cdot 2 ^ { - j } } \left( f ( 2 ^ { - j } k ) + x f ^ { \prime } ( 2 ^ { - j } k ) + \frac { 1 } { 2 } x ^ { 2 } f ^ { \prime \prime } ( 2 ^ { - j } k ) \right) 2 ^ { j / 2 } \psi _ { 2 } ( 2 ^ { j } x ) d x .
$$

The integral on the right can be reduced to doing the integrals for the first three moments of $\psi _ { 2 }$ Since the first two moments vanish and the third is given in (6.11), we can evaluate the integral. (See Exercise 3.) Our final result is that the ${ \dot { \jmath } } , k$ -wavelet coefficient is approximately

$$
b _ { \mathbf { k } } ^ { j } \approx - { \frac { 1 } { 1 6 } } { \sqrt { \frac { 3 } { 2 \pi } } } 2 ^ { - 5 j / 2 } f ^ { \prime \prime } ( 2 ^ { - j } k ) .
$$

Singularity Detection. As an application of the formula in (6.13), we find a point where an otherwise smooth function has a discontinuity in its derivative. This application is called singularity detection, and this process can be used, among other things, to detect cracks in material.

![](images/3cf96e0e2764fe0ca201a9e0563f1463cccf501962325112e310fad6bc5e702b.jpg)  
Figure 4 The original signal is piecewise linear on the interval $\left\{ - 1 , 4 \right\}$ , with a break at ${ \pmb x } = 2 . 8$ The wavelet part comes from a first-order decomposition using the $N = 2$ wavelet; it is essentially 0, except for the interval near ${ \pmb x } = { \pmb 2 } . { \pmb 8 }$ .

As an example, we will determine where the piecewise linear function shown in Figure 4 changes slope. Keep in mind that the formula (6.13) is exact in any region where a signal $\pmb { f }$ is constant, linear, or quadratic in $\pmb { x }$ ,because the quadratic Taylor polynomial for $\pmb { f }$ is $\pmb { f }$ in these cases. Since ${ \pmb f } ^ { \prime \prime } = { \bf 0 }$ where $\pmb { f }$ is linear, (6.13) implies that the only nonzero wavelet coefficients will come from a small region near the corner point where the slope changes. The signal itself has the form

$$
f ( x ) : = \left\{ \begin{array} { l l } { 0 . 3 7 x + 1 . 3 7 , } & { - 1 \leq x \leq 2 . 8 } \\ { 1 . 5 8 x - 2 . 0 3 , } & { 2 . 8 \leq x \leq 4 . } \end{array} \right.
$$

After sampling the signal at 256 equally spaced points, we decomposed it using the $N = 2$ Daubechies wavelet. Thus, our starting level was $j = 8$ the level down from this is $j = 7$ The only appreciable wavelet coefficient was $b _ { 9 7 } ^ { 7 } \approx$ $\mathbf { - 0 . 0 1 }$ .The rest were on the order of ${ \bf l 0 ^ { - 1 4 } }$ .The index $\pmb { k } = \pmb { 9 7 }$ corresponds to a wavelet supported on the $\pmb { x }$ -interval [2.79, 2.83]; consequently, the singularity is located in this interval.

# 6.3 Computational Issues

Consider the following problem. We want to use $N = 2$ Daubechics wavelets to decompose a signal that we have $\mathbf { \pmb { n } }$ samples for, $s _ { 0 } \ldots , s _ { n - 1 }$ .These samples will be regarded as part of our top-level approximation coefficient sequence, $\pmb { a } ^ { j }$ . We will filter these numbers using the high- and low-pass filters for the Daubechies wavelets. These are $\pmb { H }$ and $\scriptstyle { L , }$ , and they have impulse responses given by the sequences $\scriptstyle h$ and $\pmb { \ell }$ ,where

$$
\begin{array} { l } { { \ell = \displaystyle \frac { 1 } { 2 } \left( \cdots 0 \underbrace { p _ { 3 } \quad p _ { 2 } \quad p _ { 1 } \quad p _ { 0 } \quad 0 \quad 0 \cdots  \quad \ell _ { k } = \displaystyle \frac { 1 } { 2 } \overline { { { p } } } _ { - k } } } } \\ \right){ { h = \displaystyle \frac { 1 } { 2 } \left( \cdots 0 \quad 0 \quad 0 \quad 0 \underbrace { - p _ { 0 } \quad p _ { 1 } \quad - p _ { 2 } \quad p _ { 3 } \quad \cdots  \quad h _ { k } = \displaystyle \frac { 1 } { 2 } ( - 1 ) ^ { k } p _ { k + 1 } } . } } \en\right)d{array} \end{array}
$$

We convolve $\pmb \ell$ and $\pmb { h }$ with $\pmb { a } ^ { j }$ and downsample. Thus, for any ${ \pmb a } ^ { \pmb { j } }$ -not just our signal with eight samples-we have :

$$
\begin{array} { l } { { a _ { k } ^ { j - 1 } = D ( \ell * a ^ { j } ) _ { k } = \displaystyle \frac { 1 } { 2 } \left( p _ { 0 } a _ { 2 k } ^ { j } + p _ { 1 } a _ { 2 k + 1 } ^ { j } + p _ { 2 } a _ { 2 k + 2 } ^ { j } + p _ { 3 } a _ { 2 k + 3 } ^ { j } \right) , } } \\ { { \displaystyle b _ { k + 1 } ^ { j - 1 } = D ( h * a ^ { j } ) _ { k } = \displaystyle \frac { 1 } { 2 } \left( p _ { 3 } a _ { 2 k } ^ { j } - p _ { 2 } a _ { 2 k + 1 } ^ { j } + p _ { 1 } a _ { 2 k + 2 } ^ { j } - p _ { 0 } a _ { 2 k + 3 } ^ { j } \right) . } } \end{array}
$$

To compute each level $_ { j - 1 }$ coefficient, we need four consecutive samples, always starting at an even number. For example, if we have $\pmb { n = 8 }$ samples; $s _ { 0 } , \ldots , s _ { 7 }$ then to compute the $a _ { 2 } ^ { 2 }$ coefficients, we need $\pmb { s _ { 4 } }$ through $\bullet \mathbf { 7 }$ To compute ${ \pmb a } _ { 3 } ^ { 2 }$ we need $\bullet _ { 6 }$ through ${ \pmb s } _ { 9 }$ . But we do not have $\mathbf { \sigma } _ { s } \mathbf { \sigma } _ { \mathbf { \{ \sigma } }  ^ { \mathbf { \{ \sigma } } $ It's no surprise that at some point we will run out of coefficients to filter. The surprise is that we are only able to compute $\pmb { k } = \mathbf { 0 }$ ,1, 2. This means that from eight samples, we only get three decomposition coefficients, not the four that we would expect. This is the overspill problem. The filters $\pmb { H }$ and $\pmb { L }$ spill over to samples we don't have.

What to do? First, the overspill problem comes about because we don't know what the signal was before or after our set of samples. Thus we need to extend the signal in some fashion beyond our initial set of samples. Here are a few of the standard choices. In the accompanying illustrations, the filled circles represent the original signal, and the open circles are points in the signal's extension. :

Zero padding. Extend the signal by adding zeros at the two ends. This is appropriate if the signal is very long, and the ends of the signal do not matter, or if the signal really is abruptly started and stopped. This amounts to setting $\pmb { s _ { k } } = \mathbf { 0 }$ if $\pmb { k } < \mathbf { 0 }$ or $k > n - 1$ .

![](images/46e546cd9da53b3d016c48283a8d707831262da43c01064ff504e19e9a795905.jpg)

Periodic extension. Another approach is to reuse the sampled data by making the signal periodic, so that $\boldsymbol { s } _ { k + n } = \boldsymbol { s } _ { k }$ For example, with eight samples, $s _ { 0 } , \ldots , s _ { 7 }$ , we would let $\begin{array} { r } { s _ { 8 } = s _ { 0 } } \end{array}$ , $\pmb { s _ { 9 } } = \pmb { s _ { 1 } }$ , and so on.

![](images/f12597916f6541fe1f856069d32caf7f6b4d3c66c6545986d3362925b2b48c4d.jpg)

Smooth padding. Extend the signal by linearly extrapolating the data near the two ends. This is appropriate if signal isn't too noisy, at least near the ends.

![](images/c838db0daab26af6a20de53fb4c8e1a23fe6ff6bdd075f2ff38a31cf5a2f4b3e.jpg)

Symmetric extensions. The signal is evenly extended at the endpoints by reflection. There are two ways to do this. The signal can be reflected about a line through an endpoint, or about a line midway between an endpoint and the next point on the grid. The first type is illustrated at the left endpoint, and the second at the right one.

![](images/6869083f4f984de1409a366f825feb12b94fd162fcd447ff2d3b7ab7e4cff1b3.jpg)

# 6.4 The Scaling Function at Dyadic Points

Although the values of the scaling function $\phi$ do not enter into the decomposition and reconstruction algorithms, it is useful to be able to compute approximate values of $\phi$ in order to verify some of its properties (like continuity). An iterative method for computing $\phi$ is given in Theorem 5.23. However, this algorithm is somewhat cumbersome from a computational point of view. A more computationally efficient method for computing the scaling function $\phi$ is to use the scaling equation to compute the value of $\phi$ at all dyadic values, $x = l / 2 ^ { n }$ , where $\imath$ and $\pmb { n }$ are integers. We illustrate this process in the following steps. To simplify the exposition, we concentrate on the Daubechies case $\left[ N = 2 \right]$ with four nonzero $\pmb { p }$ -coefficients as constructed in Section 6.1, but the procedure easily generalizes.

Step 1. Compute $\phi$ at all the integer values.

Let $\phi _ { l } = \phi ( l )$ for $\iota \in Z$ The Daubechies $( N = 2 )$ scaling function is nonzero only on the interval $\mathbf { 0 < { \mathfrak { x } } < 3 }$ and so $\phi _ { 0 } = \phi ( 0 ) = 0 = \phi ( 3 ) = \phi _ { 3 }$ (see Figure 2). In particular, $\phi _ { 1 }$ and $\phi _ { 2 }$ are the only nonzero unknown values of $\phi$ at integer points. In order to arrange the normalization $\textstyle \int \phi = 1$ , we require $\textstyle \sum _ { l } \phi _ { l } = 1$ or, in our specific case,

$$
\phi _ { 1 } + \phi _ { 2 } = 1 .
$$

Now we use the scaling equation $\begin{array} { r } { \phi ( x ) = \sum _ { k } p _ { k } \phi ( 2 x - k ) } \end{array}$ For $\pmb { x } = \pmb { 1 }$ , this equation becomes

$$
\phi _ { 1 } = \sum _ { k = 0 } ^ { 3 } p _ { k } \phi ( 2 - k ) = p _ { 0 } \phi _ { 2 } + p _ { 1 } \phi _ { 1 } \quad ( \mathrm { b e c a u s e } \ \phi _ { 0 } = \phi _ { 3 } = 0 ) .
$$

At ${ \pmb x } = { \pmb 2 }$ , the scaling equation becomes

$$
\phi _ { 2 } = \sum _ { k \in \cal Z } p _ { k } \phi ( 4 - k ) = p _ { 2 } \phi _ { 2 } + p _ { 3 } \phi _ { 1 } .
$$

These two equations can be written in matrix form as

$$
\left( \begin{array} { c } { { \phi _ { 1 } } } \\ { { \phi _ { 2 } } } \end{array} \right) = \left( \begin{array} { c c } { { p _ { 1 } } } & { { p _ { 0 } } } \\ { { p _ { 3 } } } & { { p _ { 2 } } } \end{array} \right) \left( \begin{array} { c } { { \phi _ { 1 } } } \\ { { \phi _ { 2 } } } \end{array} \right) .
$$

Here, the $\pmb { p }$ -values are known [see (6.5)] and we are solving for the unknowns $\phi _ { 1 }$ and $\phi _ { 2 }$ . In order for this matrix equation to have a nonzero solution, the matrix must have an eigenvalue equal to 1. Then $( \phi _ { 1 } , \phi _ { 2 } )$ would be the corresponding eigenvector with $\phi _ { 1 } + \phi _ { 2 } = 1$ .To find this eigenvector, we rewrite the matrix equation as

$$
\left( \begin{array} { c c } { { p _ { 1 } - 1 } } & { { p _ { 0 } } } \\ { { p _ { 3 } } } & { { p _ { 2 } - 1 } } \end{array} \right) \left( \begin{array} { c } { { \phi _ { 1 } } } \\ { { \phi _ { 2 } } } \end{array} \right) = \left( \begin{array} { c } { { 0 } } \\ { { 0 } } \end{array} \right) .
$$

A nonzero solution to this matrix equation exists if the first row is a multiple of the second. From Theorem 5.9, $\begin{array} { r } { \sum p _ { \mathrm { o d d } } = \sum p _ { \mathrm { e v e n } } = 1 } \end{array}$ Therefore the first row is the negative of the second. The equation corresponding to the first row is

$$
( p _ { 1 } - 1 ) \phi _ { 1 } + p _ { 0 } \phi _ { 2 } = 0 .
$$

We restate the normalization equation (6.16):

$$
\phi _ { 1 } + \phi _ { 2 } = 1 .
$$

These two equations can be solved simultaneously. In the case of Daubechies, the solution is

$$
\phi _ { 1 } = { \frac { 1 + \sqrt { 3 } } { 2 } } \approx 1 . 3 6 6 \quad \quad \phi _ { 2 } = { \frac { 1 - \sqrt { 3 } } { 2 } } \approx - 0 . 3 6 6 .
$$

The $\phi$ values at all other integer points are zero.Therefore, all the $\phi _ { l } = \phi ( l )$ , $\iota \in Z$ have now been determined.

Step 2. The values of $\phi$ at the half-integers.

To compute $\phi ( l / 2 )$ , we use the scaling equation

$$
\phi ( x ) = \sum _ { k \in Z } p _ { k } \phi ( 2 x - k )
$$

at $\boldsymbol { x } = \boldsymbol { l } / 2$ to obtain

$$
\phi ( l / 2 ) = \sum _ { k = 0 } ^ { 3 } p _ { k } \phi ( l - k ) .
$$

Since $\phi ( l - k )$ is known from Step 1, $\phi ( l / 2 )$ can be computed. We need only compute $\phi ( l / 2 )$ for $\iota = 1$ 2,3,4, and 5 since ${ \phi } ( { \pmb x } ) = { \bf 0 }$ for ${ \pmb x } \leq { \bf 0 }$ and $\pmb { x } \geq \mathbf { 3 }$ . When $\pmb { l = 2 }$ or $4 , l / 2$ is an integer and the values of $\phi$ at these points are known from Step 1. Thus we need only compute $\phi ( l / 2 )$ for $\pmb { l } = \pmb { 1 }$ , 3, and 5. Equation (6.18)for $\pmb { l } = \pmb { 1 }$ ,3, 5 becomes

$$
\begin{array} { l } { \displaystyle \phi ( 1 / 2 ) = p _ { 0 } \phi _ { 1 } = \frac { ( 1 + \sqrt { 3 } ) ^ { 2 } } { 8 } \approx . 9 3 3 ~ ( l = 1 ) } \\ { \displaystyle \phi ( 3 / 2 ) = p _ { 1 } \phi _ { 2 } + p _ { 2 } \phi _ { 1 } = 0 ~ ( l = 3 ) } \\ { \displaystyle \phi ( 5 / 2 ) = p _ { 3 } \phi _ { 2 } = \frac { ( - 1 + \sqrt { 3 } ) ^ { 2 } } { 8 } \approx . 0 6 7 ~ ( l = 5 ) . } \end{array}
$$

The condition $\begin{array} { r } { \sum _ { l } \phi ( l ) = 1 } \end{array}$ (from Step 1) implies $\Sigma _ { l } \phi ( l / 2 ) = 2$ Indeed, equation (6.17) gives

$$
\sum _ { l \in Z } \phi ( l / 2 ) = \sum _ { l \in Z } \sum _ { k = 0 } ^ { 3 } p _ { k } \phi ( l - k ) = \sum _ { k = 0 } ^ { 3 } p _ { k } \sum _ { l \in Z } \phi ( l - k ) .
$$

By the change of index, the inner sum is $\begin{array} { r } { \sum _ { l } \phi ( l - k ) = \sum _ { l } \phi ( l ) } \end{array}$ This sum equals 1 from Step 1. By Theorem 5.9, $\begin{array} { r } { \sum _ { k } p _ { k } = 2 } \end{array}$ Therefore,

$$
\sum _ { l \in 2 } \phi ( l / 2 ) = 2
$$

as claimed.

Step 3. Iterate.

The values of $\phi$ at the quarter-integers, $\iota / 4$ , can be computed from the values of $\phi$ at the half-integers by letting $\pmb { x } = l / 4$ in the scaling equation $\phi ( { \pmb x } ) =$ $\begin{array} { r } { \sum _ { k } p _ { k } \phi ( 2 x - k ) } \end{array}$ In general, once $\phi$ has been computed at the values $x = l / 2 ^ { n - 1 }$ , then we can compute the value of $\phi$ at the values $x = l / 2 ^ { n }$ by inserting $x = l / 2 ^ { n }$ into the scaling equation (6.17):

$$
\phi ( l / 2 ^ { n } ) = \sum _ { k \in \cal Z } p _ { k } \phi ( l / 2 ^ { n - 1 } - k ) = \sum _ { k \in \cal Z } p _ { k } \phi \left( \frac { l - 2 ^ { n - 1 } k } { 2 ^ { n - 1 } } \right) .
$$

The right side involves values of $\phi$ at $x = l ^ { \prime } / 2 ^ { n - 1 }$ that have been computed from the previous step.

We claim

$$
\sum _ { l \in Z } \phi ( l / 2 ^ { n } ) = 2 ^ { n } .
$$

We have already shown this equation for $\pmb { n = 0 }$ (Step 1) and $\pmb { n } = \pmb { 1 }$ (Step 2). Suppose by induction that we assume this equation is true for $\pmb { n } - \pmb { 1 }$ We now show it to be true for $\pmb { n }$ We have

$$
\begin{array} { r l } { \displaystyle \sum _ { l \in Z } \phi ( l / 2 ^ { n } ) = \sum _ { l \in Z } \sum _ { k \in Z } p _ { k } \phi ( l / 2 ^ { n - 1 } - k ) } & { \mathrm { f r o m ~ ( 6 . 1 7 ) } } \\ { = \displaystyle \sum _ { k \in Z } p _ { k } \sum _ { l \in Z } \phi ( l / 2 ^ { n - 1 } - k ) } & { \mathrm { ( s w i t c h ~ o r d e r ~ o f ~ s u m m a t i o n ) } } \\ { = \displaystyle \sum _ { k \in Z } p _ { k } \sum _ { l \in Z } \phi \left( \frac { l - 2 ^ { n - 1 } k } { 2 ^ { n - 1 } } \right) } \\ { = \displaystyle \sum _ { k \in Z } p _ { k } \sum _ { l \in Z } \phi ( l ^ { \prime } / 2 ^ { n - 1 } ) } & { \mathrm { ( w i t h ~ } l ^ { \prime } = l - 2 ^ { n - 1 } k ) . } \end{array}
$$

By the induction hypothesis, the inner sum is $2 ^ { n - 1 }$ [equation (6.19), with $\scriptstyle { \pmb { n } }$ replaced by $\pmb { n } - 1 ]$ Therefore,

$$
\sum _ { l \in \mathbb { Z } } \phi ( l / 2 ^ { n } ) = \sum _ { k \in \mathbb { Z } } p _ { k } 2 ^ { n - 1 } .
$$

Since $\begin{array} { r } { \sum _ { k } p _ { k } = 2 } \end{array}$ (Theorem 5.9), the right side equals $2 ^ { n }$ , as desired.

As $\pmb { n }$ gets larger, the set of dyadic points $\lbrace l / 2 ^ { n } , l \in Z \rbrace$ gets denser. Since any real number is a limit of dyadic points and since the Daubechies scaling function is continuous, the value of $\phi$ at any value $\pmb { x }$ can be obtained as a limit of $\phi$ -values at Dyadic points.

The scaling function, $\phi _ { i }$ , that is constructed in this manner satisfies the normalization condition $\textstyle \int \phi = 1$ To see this, we regard $\int \phi d x$ as a limit as $n \to \infty$ of a Riemann sum over a partition given by $\{ x _ { l } = l / 2 ^ { n }$ ; $l = \ldots , - 1 , 0 , 1 , 2 , \ldots \}$ . The width of this partition is $\Delta x = 1 / 2 ^ { n }$ .So we have

$$
\begin{array}{c} \int _ { - \infty } ^ { \infty } \phi ( x ) d x = \operatorname* { l i m } _ { n \to \infty } \sum _ { l \in { \cal Z } } \phi ( x _ { l } ) \Delta x = \operatorname* { l i m } _ { n \to \infty } \sum _ { l \in { \cal Z } } \phi ( l / 2 ^ { n } ) \left( 1 / 2 ^ { n } \right) .  \end{array}
$$

Since $\textstyle \sum _ { l } \phi ( l / 2 ^ { n } ) = 2 ^ { n }$ , the right side is 1, as claimed.

# 6.5 Exercises

1. Show that $\widetilde { \phi } ( x ) : = \phi _ { 2 } ( \textstyle { \frac { 3 } { 2 } } - x )$ satisfies the ${ \pmb { N } } = { \pmb { 2 } }$ Daubechies scaling relation, but with the coefficients reversed; that is,

$$
\widetilde { \phi } ( x ) = p _ { 3 } \widetilde { \phi } ( 2 x ) + p _ { 2 } \widetilde { \phi } ( 2 x - 1 ) + p _ { 1 } \widetilde { \phi } ( 2 x - 2 ) + p _ { 0 } \widetilde { \phi } ( 2 x - 3 ) .
$$

What is the corresponding equation for $\widetilde { \psi } ( x ) : = \psi _ { 2 } ( \frac { 3 } { 2 } - x ) :$ Sketch both $\widetilde { \phi }$ and $\widetilde { \psi }$

Show that equation (6.9) holds.

3. Use the first three moments of $\psi _ { 2 }$ to evaluate integral in (6.12) and thus obtain the approximation to $\pmb { b } _ { \pmb { k } } ^ { j }$ given in (6.13).

Repeat Exercises 9 and 10 in Chapter 4 using Daubechies $\left. N = 2 \right.$ wavelets.

5. Repeat Exercise 4 for the signal

$$
g ( t ) = - 5 2 t ^ { 4 } + 1 0 0 t ^ { 3 } - 4 9 t ^ { 2 } + 2 + N ( 1 0 0 ( t - 1 / 3 ) ) + N ( 2 0 0 ( t - 2 / 3 ) )
$$

where

$$
N ( t ) = t e ^ { - t ^ { 2 } } .
$$

Compare your results with that of Daubechies wavelets with those of Exercise 9 in Chapter 3.

6. Let $f ( t )$ be defined via

$$
f ( t ) = \left\{ { \begin{array} { c l } { 0 } & { t < 0 , t > 1 } \\ { t ( 1 - t ) } & { 0 \leq t \leq 1 . } \end{array} } \right.
$$

Sample $\pmb { f }$ at the dyadic points $k \times 2 ^ { - 8 }$ , $k = - 2 5 6 , \ldots , 5 1 2$ Thus, ${ \dot { \mathbf { \zeta } } } _ { 1 } = \mathbf { \zeta } \mathbf { 7 }$ is the top level. Using the Daubechies $N = 2$ $\psi _ { 2 }$ wavelet, implement a 1-level decomposition. Plot the magnitudes of the level 7 wavelet coefficients. Which wavelet has the largest coefficient? What $\pmb { t }$ corresponds to this wavelet? Explain.

7. Let $\pmb { \mathscr { g } }$ be defined by

$$
g ( t ) = \left\{ \begin{array} { c c } { 0 } & { t < 0 , t > 1 } \\ { t ^ { 2 } ( 1 - t ) ^ { 2 } } & { 0 \leq t \leq 1 . } \end{array} \right.
$$

Sample $\pmb { g }$ at the dyadic points $k \times 2 ^ { - 8 }$ , $k = - 2 5 6 , \ldots , 5 1 2 \ ( j = 7$ is the top level). Using the Daubechies $N = 2$ $\psi _ { 2 }$ wavelets, implement a 1-level decomposition. Plot the magnitudes of the level 7 wavelet coefficients for each, and determine which wavelet coefficient is greatest. Repeat with the $\psi _ { 3 }$ b $\left[ N = 3 \right]$ wavelet. Give an explanation of why the greatest coefficients occur where they do.

8. (Polynomial Suppression.) Frequently signals have a "bias," which is a polynomial part (usually linear or quadratic) added to a bounded, rapidly oscillating part— $\begin{array} { r } { \mathbf { \nabla } \cdot \mathbf { \vec { f } } ( t ) = 2 + 5 t + t ^ { 2 } + \frac { 1 } { 5 0 } \sin ( 6 4 \pi t ) \cos ( 6 \pi t ) , } \end{array}$ for example. Suppose that we have taken 1024 samples of $\pmb { f }$ on the interval [-1, 1]. Come up with a strategy for separating the two signals via a Daubechies wavelet analysis. Use MATLAB to carry it out. (Hint: What is the smallest value of $\pmb { N }$ needed to reproduce quadratics exactly? Also, smooth padding works best for these examples.)

9.(Noise Removal.) Wavelets can be used to remove noise from a signal. Let $\begin{array} { r } { \pmb { f } ( t ) = \sin ( 8 \pi t ) \cos ( 3 \pi t ) + n ( t ) , } \end{array}$ ,with ${ \pmb n } ( t )$ being the noise. Numerically, we can model ${ \pmb n } ( t )$ by using a random number generator, such as MATLAB's rand. Take 1500 samples on $[ - 2 , 3 ]$ of $\pmb { f }$ and do an analysis with $N = 2$ 3, and 6 Daubechies wavelets. Experiment with different levels. Which wavelet does the best job?

# Chapter 7 Other Wavelet Topics

This chapter contains a variety of topics of a more advanced nature that relate to wavelets. Since these topics are more advanced, an overview is presented with details left to the various references.

# 7.1 Computational Complexity

# 7.1.1 Wavelet Algorithm

In this section, we briefly discuss the number of operations required to compute the wavelet decomposition of a signal (the computational complexity of the wavelet decomposition algorithm).

To take a concrete setting, suppose $\pmb { f }$ is a continuous signal defined on the unit interval $\mathbf { 0 } \leq t \leq 1$ Let

$$
a _ { l } ^ { n } = f ( l / 2 ^ { n } ) l = 0 , \ldots , 2 ^ { n } - 1
$$

be a discrete sampling of $\pmb { f }$ .We wish to count the number of multiplications number $N = 2 ^ { n }$ .

The decomposition algorithm stated in equation (5.12) or equation (5.17) computes the ${ \pmb { a } } ^ { j - 1 }$ and $\pmb { b } ^ { j - 1 }$ , ${ \pmb j = n , \dots , 1 }$ using the formulas

$$
\begin{array} { l } { { a _ { l } ^ { j - 1 } = ( 1 / 2 ) \displaystyle \sum _ { k } \overline { { { p } } } _ { k - 2 l } a _ { k } ^ { j } } } \\ { { \displaystyle b _ { l } ^ { j - 1 } = ( 1 / 2 ) \displaystyle \sum _ { k } ( - 1 ) ^ { k } p _ { 1 - k + 2 l } a _ { k } ^ { j } . } } \end{array}
$$

Note that there are half as many ${ \pmb { a } } ^ { j - 1 }$ coefficients as there are ${ \pmb { a } } ^ { j }$ coefficients. So the index l on the left runs from 0 to $\pmb { 2 ^ { j - 1 } } - \pmb { 1 }$ Let $\pmb { L }$ be the number of nonzero values of ${ \pmb p } _ { \pmb k }$ For Haar, $\mathbf { L } = \mathbf { 2 } $ , and for the Daubechies system constructed in the previous chapter, ${ \pmb { L } } = { \pmb { 4 } }$ Thus, there are $2 ^ { j - 1 }$ coefficients at level $j - 1$ (for $a _ { \imath } ^ { j - 1 } )$ to be computed, each of which requires ${ \pmb { L } } + { \pmb { 1 } }$ multiplications (including the multiplication by $1 / 2$ ). The same number of computations are required for $\pmb { b } _ { l } ^ { j - 1 }$ .As $\pmb { j }$ runs from $\pmb { n }$ to 1, the total number of multiplications required for decomposition is

$$
{ \begin{array} { r l } { { 2 } ( L + 1 ) 2 ^ { n - 1 } + \cdots + 2 ( L + 1 ) 2 ^ { 0 } = 2 ( L + 1 ) \displaystyle \sum _ { j = 0 } ^ { n - 1 } 2 ^ { j } } & { } \\ { = 2 ( L + 1 ) ( 2 ^ { n } - 1 ) } & { { \mathrm { u s i n g ~ e q u a t i o n ~ ( } } } \\ { \approx 2 ( L + 1 ) N . } & { } \end{array} }
$$

This result is often summarized by stating that the wavelet decomposition algorithm requires $O ( N )$ multiplication operations, where $\pmb { N }$ is the number of data at the top level. Here, $O ( N )$ stands for a number that is proportional to $\pmb { N }$ . The proportionality constant in this case is $2 ( L + 1 )$ (which is 6 in the case of Haar or 10 in the case of Daubechies).

By comparison, the number of multiplicative operations for the fast Fourier transform is $O ( N \log N )$ (see Section 3.1.3). However, this comparison is unfair since the fast Fourier transform decomposes a signal into all its frequency components between 0 and $N / 2$ By contrast, the wavelet decomposition algorithm decomposes a signal into its frequency components that lie in ranges bounded by powers of 2. For example,

$$
w _ { j - 1 } ( x ) = \sum b _ { l } ^ { j - 1 } \psi ( 2 ^ { j - 1 } x - l )
$$

is the decomposition of $\pmb { f }$ given in Theorem 5.11. This should be regarded as the component of $\pmb { f }$ that involves frequencies in the range $2 ^ { j - 1 }$ to $\bullet ^ { j }$ Therefore, the wavelet decomposition algorithm does not decompose the signal into the more detailed range of frequencies that are offered by the discrete Fourier transform.

# 7.1.2 Wavelet Packets

Wavelets can be used to obtain a decomposition of a signal into a finer gradation of frequency components using wavelet packets. We briefly describe the technique for doing this, which requires $O ( N \log N )$ operations; therefore, it is no more efficient than the fast Fourier transform. A more complete discussion may be found in [13, Chapter 7].

We illustrate the idea of wavelet packets in the specific when $\pmb { n } = \pmb { 3 }$ A signal $f _ { 3 } \in V _ { 3 }$ can be decomposed via Theorem 5.11 as

$$
f _ { 3 } = w _ { 2 } + w _ { 1 } + w _ { 0 } + f _ { 0 } \in W _ { 2 } \oplus W _ { 1 } \oplus W _ { 0 } \oplus V _ { 0 } .
$$

We can put this decomposition into a more hierarchical structure.

$$
f _ { 3 } \underbrace { L } _ { \begin{array} { l } { H } \\ { \left( u _ { } \right) } \end{array} } f _ { 2 } \underbrace { L } _ { \begin{array} { l } { H } \\ { w _ { 2 } } \end{array} } \underbrace { f _ { 1 } } _ { \begin{array} { l } { H } \\ { w _ { 1 } } \end{array} } \underbrace { L } _ { \begin{array} { l } { H } \\ { w _ { 0 } } \end{array} } f _ { 0 }
$$

The arrows marked $\pmb { H }$ are the projection operators onto the wavelet components. The arrows marked $\pmb { L }$ stand for the projection to the next lower level (e.g., the projection from $V _ { 2 }$ to $V _ { 1 }$ )The $\pmb { H }$ stands for "high-pass filter" since the wavelet part of a particular level represents the component with higher frequency (e.g., the $W _ { 1 }$ component of $V _ { 2 } = W _ { 1 } \oplus V _ { 1 }$ represents higher-frequency components than the $V _ { 1 }$ component). Likewise, the $\pmb { L }$ stands for "low-pass filter" since it projects to the next lower level.

The ${ f } _ { 3 }$ contains frequency components from 1 to 8. The $\mathbf { \Delta } \mathbf { w } _ { 2 }$ component contains frequency components from 5 to 8. The analogous frequency ranges for the ${ \pmb w } _ { \mathbf 1 }$ , ${ \pmb w } _ { \mathbf { 0 } }$ and ${ f } _ { 0 }$ components are 3 to 4, 2, and 1, respectively. The idea behind wavelet packets is to apply the high-pass and low-pass filters to each of $\mathbf { \Delta } \mathbf { w } _ { 2 }$ , ${ \pmb w } _ { 1 }$ , and ${ \pmb w } _ { \mathbf 0 }$ The high-pass filter and low-pass filters applied to $\mathbf { \Delta } w _ { 2 }$ create new components ${ \boldsymbol { w } } _ { 2 1 }$ and ${ \pmb w } _ { { \bf 2 0 } }$ ,respectively, which are orthogonal to one another. The process is iterated until a complete decomposition into all frequencies is obtained.

In the case of $\pmb { f _ { 3 } }$ , a complete decomposition into all components is illustrated in the following diagram.

fH LH w2 L H f2 Lw21 W20 w1H/ H/ / HW10 wo

To count the number of operations required, imagine this diagram were extended to handle $\textbf { \em n }$ levels $\mathbf { \lambda } _ { n = 3 }$ is illustrated). Each component in the kth level of the diagram requires ${ \cal O } ( 2 ^ { N - k } )$ computations. Since there are $2 ^ { k }$ components in the kth level, the total number of computations for this level is $O ( 2 ^ { n } )$ (independent of $\pmb { k }$ ).Since there are $\pmb { n }$ levels (not counting the first, which only contains the original signal), the total number of operations is $O ( n 2 ^ { n } )$ or $N \log _ { 2 } N$ ,where $N = 2 ^ { n }$ .This is the same number of operations required by the fast Fourier transform.

# 7.2 Wavelets in Higher Dimensions

Signal processing with wavelets of video images requires a generalization of wavelets to several dimensions (two are required for a static pictorial image). Wavelets in higher dimensions are obtained by taking the tensor product of

one-dimensional wavelets. We briefly explain this concept in the case of two dimensions, which we think of as $R ^ { 2 }$ with coordinates $( { \pmb x } , { \pmb y } )$ .

Suppose $\phi$ and $\psi$ are the scaling function and wavelet for a multiresolution analysis (for example, the Haar system or the one constructed by Daubechies). As shown in previous sections, the functions

$$
\phi _ { j l } ( x ) = 2 ^ { j / 2 } \phi ( 2 ^ { j } x - l ) \qquad \psi _ { j l } ( x ) = 2 ^ { j / 2 } \psi ( 2 ^ { j } x - l ) \qquad 
$$

are orthonormal bases for the spaces $V _ { j }$ and $W _ { j }$ , respectively. Moreover, each $\psi _ { j \ell }$ is orthogonal to all the $\phi _ { j l }$ . For each set of indices ${ \scriptstyle j , l , j ^ { \prime } , l ^ { \prime } }$ , define the functions

$$
\phi _ { j , l , j ^ { \prime } , l ^ { \prime } } ( x , y ) = \phi _ { j l } ( x ) \phi _ { j ^ { \prime } l ^ { \prime } } ( y ) \quad \mathrm { a n d } \quad \psi _ { j , l , j ^ { \prime } , l ^ { \prime } } ( x , y ) = \psi _ { j l } ( x ) \psi _ { j ^ { \prime } l ^ { \prime } } ( y ) .
$$

The indices $j$ and ${ \bf { \chi } } _ { j ^ { \prime } } ^ { \prime }$ vary between 0 and $\pmb { n }$ (the top level) as before. The indices $\iota$ and $\pmb { l ^ { \prime } }$ correspond to the translational components and depend on the domain of interest. For example, if the signal is defined on the unit square $\{ ( x , y ) ; 0 \leq x , y \leq 1 \}$ ,then $0 \leq l \leq 2 ^ { j } - 1$ and $\mathbf { 0 } \leq l ^ { \prime } \leq 2 ^ { j ^ { \prime } } - 1$ . As an easy exercise, you can show that for each pair of indices ${ \dot { \jmath } } , { \dot { \jmath } } ^ { \prime }$ , the sets of functions $\{ \phi _ { j , l , j ^ { \prime } , l ^ { \prime } } ( x , y ) ; \ l , l ^ { \prime } \in Z \}$ and $\left\{ \psi _ { j , l , j ^ { \prime } , l ^ { \prime } } ( x , y ) ; \ l , l ^ { \prime } \in Z \right\}$ are orthonormal bases for $V _ { j } \otimes V _ { j ^ { \prime } }$ and $W _ { j } \otimes W _ { j ^ { \prime } } \subset L ^ { 2 } ( R ^ { 2 } )$ .Here, $V _ { j } \otimes V _ { j ^ { \prime } }$ is called the tensor product of $V _ { j }$ and $V _ { j ^ { \prime } }$ and is the space generated by $\pmb { f } ( \pmb { x } ) \pmb { g } ( \pmb { y } )$ where $f \in V _ { j }$ and $g \in V _ { j ^ { \prime } }$ .

A signal $f \in L ^ { 2 } ( R ^ { 2 } )$ can be discretized in both dimensions. For example, if the domain of the signal is the unit square $\{ ( x , y ) \in R ^ { 2 } ; 0 \leq x , y \leq 1 \}$ , then we discretize by setting

$$
f _ { n , n } ( x , y ) = \sum _ { k , k ^ { \prime } } a _ { k , k ^ { \prime } } ^ { n , n } \phi ( 2 ^ { n } x - k ) \phi ( 2 ^ { n } y - k ^ { \prime } ) \quad \mathrm { w h e r e ~ } a _ { k , k ^ { \prime } } ^ { n , n } = f ( k / 2 ^ { n } , k ^ { \prime } / 2 ^ { n } ) .
$$

The decomposition and reconstruction algorithms are pieced together in each variable separately. Although a precise algorithm is somewhat tedious, the ideas can be simply explained. Equation (5.10) can be used to decompose the functions $\phi ( 2 ^ { n } x - k )$ and $\phi ( 2 ^ { n } y - k ^ { \prime } )$ into a linear combination of $\phi ( 2 ^ { n - 1 } x - l )$ , $\psi ( 2 ^ { n - 1 } x - l )$ , $\phi ( 2 ^ { n - 1 } y - l )$ and $\psi ( 2 ^ { n - 1 } x - l )$ The signal $\scriptstyle f _ { n , n }$ becomes

$$
f _ { n , n } = w _ { n - 1 , n - 1 } + f a b _ { n - 1 , n - 1 } + f b a _ { n - 1 , n - 1 } + f a a _ { n - 1 , n - 1 }
$$

where

$$
\begin{array} { r l r } & { } & { w _ { n - 1 , n - 1 } \mathrm { ~ i s ~ a ~ l i n e a r ~ c o m b i n a t i o n ~ o f ~ } \psi ( 2 ^ { n - 1 } x - l ) \psi ( 2 ^ { n - 1 } y - l ^ { \prime } ) } \\ & { } & { f a b _ { n - 1 , n - 1 } \mathrm { ~ i s ~ a ~ l i n e a r ~ c o m b i n a t i o n ~ o f ~ } \phi ( 2 ^ { n - 1 } x - l ) \psi ( 2 ^ { n - 1 } y - l ^ { \prime } ) } \\ & { } & { f b a _ { n - 1 , n - 1 } \mathrm { ~ i s ~ a ~ l i n e a r ~ c o m b i n a t i o n ~ o f ~ } \psi ( 2 ^ { n - 1 } x - l ) \phi ( 2 ^ { n - 1 } y - l ^ { \prime } ) } \\ & { } & { f a a _ { n - 1 , n - 1 } \mathrm { ~ i s ~ a ~ l i s e a r ~ c o m b i n a t i o n ~ o f ~ } \psi ( 2 ^ { n - 1 } x - l ) \phi ( 2 ^ { n - 1 } y - l ^ { \prime } ) . } \end{array}
$$

The terms, fab, fba, and faa are further decomposed until only $\psi ( { \pmb x } - { \pmb l } )$ or $\phi ^ { 0 } ( x - l )$ terms appear. After collecting terms,

$$
f _ { n , n } = \sum _ { j , k = - 1 } ^ { n - 1 } w _ { j , k }
$$

where $w _ { j , k } \in W _ { j } \otimes W _ { k }$ for $0 \leq j , k \leq n - 1$ , $w _ { j , - 1 } \in W _ { j } \otimes V _ { 0 }$ and ${ \pmb w } _ { - 1 , j } \in V _ { 0 } \otimes { \pmb W } _ { j }$ . Once decomposed, a signal can be filtered or compressed just as in the one-dimensional case. Reconstruction is accomplished by combining the reconstruction algorithms in both variables. The following equations

$$
\begin{array} { l } { { \phi ( x ) = \displaystyle \sum _ { k } p _ { k } \phi ( 2 x - k ) } } \\ { { \psi ( x ) = \displaystyle \sum _ { k } ( - 1 ) ^ { k } \overline { { { p } } } _ { 1 - k } \phi ( 2 x - k ) } } \end{array}
$$

along with the analogous equations in the $_ { \pmb { y } }$ -variable can be used to express $_ { w _ { - 1 , - 1 } }$ and ${ \pmb w _ { 0 , 0 } }$ in terms of $\phi ( 2 x - k ) \phi ( 2 y - k ^ { \prime } ) \in V _ { 1 } \otimes V _ { 1 }$ Replacing $\pmb { x }$ (and $^ { y ) }$ by ${ \bf 2 ^ { j } x }$ (and ${ \bf 2 ^ { \prime } } y )$ in the preceding equations allows any element in $W _ { j } \otimes W _ { j ^ { \prime } }$ . to be expressed in terms of elements in $V _ { j + 1 } \otimes V _ { j ^ { \prime } + 1 }$ .This process is continued until the signal is in the form

$$
f _ { n , n } ( x , y ) = \sum _ { k , k ^ { \prime } } a _ { k , k ^ { \prime } } ^ { n , n } \phi ( 2 ^ { n } x - k ) \phi ( 2 ^ { n } y - k ^ { \prime } )
$$

where, of couse, the $a _ { k , k ^ { \prime } } ^ { n , n }$ process. The value, $a _ { k , k ^ { \prime } } ^ { n , n }$ rerents t val  the filteo compressed signal at $x = k / 2 ^ { n }$ , $\pmb { y } = \pmb { k } ^ { \prime } / 2 ^ { n }$ , $0 \leq k , k ^ { \prime } \leq 2 ^ { n } - 1$ .

# 7.3 Relating Decomposition and Reconstruction

In this section we analyze the decomposition and reconstruction algorithms and we show that the latter involves the $\scriptstyle { l ^ { 2 } }$ -adjoint of the former. As before, we will assume that $\phi$ and $\psi$ are the scaling and wavelet functions associated to a multiresolution analysis. We rewrite the decomposition and reconstruction algorithms using the orthonormal bases $\phi _ { j k } ( x ) = 2 ^ { j / 2 } \phi ( 2 ^ { j } x - k ) \in V _ { j }$ and $\psi _ { j k } ( x ) = 2 ^ { j / 2 } \psi ( 2 ^ { j } x - k ) \in W _ { j }$

The decomposition algorithm (5.9) becomes the following:

THEOREM 7.1 (Decomposition) A function $\begin{array} { r } { f = \sum _ { l } a _ { l } ^ { n } \phi _ { n l } ( x ) } \end{array}$ can be decomposed as

with

$$
f = w _ { n - 1 } + w _ { n - 2 } + \cdots + w _ { 0 } + f _ { 0 }
$$

where

$$
\begin{array} { l } { { a _ { l } ^ { j - 1 } = \displaystyle \frac { 1 } { \sqrt { 2 } } \sum _ { k } \overline { { { p _ { k - 2 l } } } } a _ { k } ^ { j } } } \\ { { b _ { l } ^ { j - 1 } = \displaystyle \frac { 1 } { \sqrt { 2 } } \sum _ { k } ( - 1 ) ^ { k } p _ { 1 - k + 2 l } a _ { k } ^ { j } . } } \end{array}
$$

In terms of convolution and the downsampling operator $\pmb { D }$ ,

$$
\begin{array} { l l } { { a ^ { j - 1 } = D ( P * a ^ { j } ) } } & { { w h e r e ~ P _ { k } = \displaystyle \frac { 1 } { \sqrt { 2 } } \overline { { { p } } } _ { - k } } } \\ { { } } & { { } } \\ { { b ^ { j - 1 } = D ( Q * a ^ { j } ) } } & { { w h e r e ~ Q _ { k } = \displaystyle \frac { 1 } { \sqrt { 2 } } ( - 1 ) ^ { k } p _ { 1 + k } . } } \end{array}
$$

The reconstruction algorithm (5.11) can be restated as follows.

# THEOREM 7.2 (Reconstruction) Suppose

$$
f _ { j - 1 } ( x ) = \sum _ { l } a _ { l } ^ { j - 1 } \phi _ { j - 1 , l } ( x ) \qquad w _ { j - 1 } ( x ) = \sum _ { l } b _ { l } ^ { j - 1 } \psi _ { j - 1 , l } ( x )
$$

and let

$$
f _ { j } ( x ) = f _ { j - 1 } ( x ) + w _ { j - 1 } ( x ) = \sum _ { l } a _ { l } ^ { j } \phi _ { j l } ( x ) .
$$

Then the coefficients $\pmb { a } _ { l } ^ { j }$ can be computed from the sequences ${ \pmb a } ^ { j - 1 }$ and $b ^ { j - 1 } \cdot b y$

$$
a _ { l } ^ { j } = { \frac { 1 } { \sqrt { 2 } } } \sum _ { k } a _ { k } ^ { j - 1 } p _ { l - 2 k } + { \frac { 1 } { \sqrt { 2 } } } \sum _ { k } b _ { k } ^ { j - 1 } \overline { { { p } } } _ { 1 + 2 k - l } ( - 1 ) ^ { l } .
$$

In terms of convolution and the upsampling operation $\pmb { U }$ ,

$$
a ^ { j } = P ^ { * } * ( U a ^ { j - 1 } ) + Q ^ { * } * ( U b ^ { j - 1 } )
$$

where $\begin{array} { r } { P _ { k } ^ { * } = \frac { 1 } { \sqrt { 2 } } p _ { k } } \end{array}$ and $\begin{array} { r } { Q _ { k } ^ { * } = \frac { 1 } { \sqrt { 2 } } \overline { { p } } _ { 1 - k } ( - 1 ) ^ { k } } \end{array}$

Except for the factor of $\scriptstyle { \frac { 1 } { \sqrt { 2 } } }$ , which results from using the orthonormal bases $\phi _ { j l }$ and $\psi _ { j l }$ , these theorems are identical to the algorithms in (5.12) and (5.13) [or (5.17) and (5.22)].

Recall that $\scriptstyle { l ^ { 2 } }$ is the space of all sequences $\pmb { x } = ( \pmb { x } _ { j } )$ ; $j \in Z$ with $\sum _ { j } | x _ { j } | ^ { 2 } <$ $\infty$ In practical applications, there are only a finite number of nonzero $\pmb { x _ { j } }$ and so the condition $\textstyle \sum _ { j } | x _ { j } | ^ { 2 } < \infty$ is automatically satisfied. The key operators involved with decomposition algorithm are the downsampling operator $D : l ^ { 2 } \mapsto$ $\scriptstyle { l ^ { 2 } }$ and the operators $T _ { P } : l ^ { 2 } \mapsto l ^ { 2 }$ and $T _ { Q } : l ^ { 2 } \mapsto l ^ { 2 }$ :

$$
\begin{array} { r } { T _ { P } ( x ) = P * x \quad x \in l ^ { 2 } } \\ { T _ { Q } ( x ) = Q * x \quad x \in l ^ { 2 } } \end{array}
$$

where $\pmb { P }$ and $\pmb { Q }$ are the sequences defined in Theorem 7.1. Likewise, the key operators in the reconstruction algorithm are the upsampling operator, $\pmb { U }$ , and the operators $T _ { P ^ { * } } : l ^ { 2 } \mapsto l ^ { 2 }$ and $T _ { Q ^ { * } } : l ^ { 2 } \mapsto l ^ { 2 }$ :

$$
\begin{array} { c c } { { T _ { P ^ { * } } ( x ) = P ^ { * } * x } } & { { x \in l ^ { 2 } } } \\ { { } } & { { T _ { Q ^ { * } } ( x ) = Q ^ { * } * x } } & { { x \in l ^ { 2 } } } \end{array}
$$

where $P ^ { * }$ and $Q ^ { \ast }$ are the sequences defined in Theorem 7.2.

Our goal now is to show that the operators $\pmb { T _ { P } }$ and $\pmb { T _ { P } } \bullet$ are adjoints of one another and likewise for the operators involving Q. Recall that if $T \colon V \mapsto V$ is a linear operator on an inner product space, $\pmb { V }$ , then its adjoint $\pmb { T } ^ { \star }$ is defined by

$$
\langle T v , w \rangle = \langle v , T ^ { * } w \rangle .
$$

# LEMMA 7.3

The adjoint of $\pmb { T _ { P } }$ is $\pmb { T _ { P ^ { \star } } }$ .   
The adjoint of $\scriptstyle { \pmb { T _ { Q } } }$ is $T _ { Q ^ { * } }$ .   
The adjoint of $\pmb { D }$ (the downsampling operator) is $\pmb { U }$ (the upsampling operator).

Proof The first two properties follow from Theorem 3.14, which states that the adjoint of the operator associated with the convolution with a sequence $f _ { n }$ . is the convolution operator associated with the sequence $f _ { n } ^ { * } = { \overline { { f } } } - n$ Thus, the first property follows from the fact that $\begin{array} { r } { P _ { k } ^ { * } = \frac { 1 } { \sqrt { 2 } } p _ { k } = \overline { { P } } _ { - k } } \end{array}$ Likewise, $\begin{array} { r } { Q _ { k } ^ { * } = \frac { 1 } { \sqrt { 2 } } \overrightarrow { p } _ { 1 - k } ( - 1 ) ^ { k } = \overrightarrow { Q } _ { - k } } \end{array}$ and so the second property follows from Theorem 3.14.

For the third property, let $\pmb { x }$ and $\pmb { y }$ be sequences in $\scriptstyle { l ^ { 2 } }$ Using the definition of $\pmb { D }$

$$
\langle D x , y \rangle _ { l ^ { 2 } } = \sum _ { n } ( D x ) _ { n } { \overline { { y } } } _ { n } = \sum _ { n } x _ { 2 n } { \overline { { y } } } _ { n } .
$$

On the other hand, only the even entris of $U _ { \pmb { y } }$ are nonzero and $( U y ) _ { 2 n } = y _ { n }$ (by definition). Therefore,

$$
\langle x , U y \rangle = \sum _ { n } x _ { 2 n } \overline { { ( U y ) } } _ { 2 n } = \sum _ { n } x _ { 2 n } \overline { { y } } _ { n } .
$$

By comparing these two sets of equations, we conclude $\langle D x , y \rangle = \langle x , U y \rangle$ as desired. $\bullet$

Using the lemma and Theorems 7.1 and 7.2, the decomposition and reconstruction algorithms can be restated (essentially) as being adjoints of each other.

THEOREM 7.4 (Decomposition) Let $\begin{array} { r } { P _ { k } = \frac { 1 } { \sqrt { 2 } } \overline { { p } } _ { - k } } \end{array}$ and $\begin{array} { r } { Q _ { k } = \frac { 1 } { \sqrt { 2 } } ( - 1 ) ^ { k } p _ { 1 + k } } \end{array}$ Suppose

$$
T _ { 0 } = D \circ T _ { P } a n d T _ { 1 } = D \circ T _ { Q }
$$

where $\pmb { D }$ is the downsampling operator and $\scriptstyle \mathbf { \mathit { T } } _ { P } $ (respectively $\scriptstyle { T _ { Q } } )$ is the operator that convolves with the sequence $\pmb { P }$ (respectively $\pmb { Q }$ ). A function $\begin{array} { r } { f _ { j } = \sum _ { l } a _ { l } ^ { j } \phi _ { j l } ( x ) } \end{array}$ can be decomposed as

$$
f = w _ { j - 1 } + f _ { j - 1 }
$$

with

$$
w _ { j - 1 } ( x ) = \sum _ { l } b _ { l } ^ { j - 1 } \psi _ { j - 1 , l } ( x ) \quad a n d \quad f _ { j - 1 } = \sum _ { l } a _ { l } ^ { j - 1 } \phi _ { j - 1 , l } ( x )
$$

where

$$
a ^ { j - 1 } = T _ { 0 } ( a ^ { j } ) a n d b ^ { j - 1 } = T _ { 1 } ( a ^ { j } ) .
$$

Conversely, the sequence $\pmb { a } ^ { j }$ can be reconstructed from $\pmb { a } ^ { j - 1 }$ and $\scriptstyle { b ^ { j - 1 } }$ by

$$
a ^ { j } = T _ { 0 } ^ { * } ( a ^ { j - 1 } ) + T _ { 1 } ^ { * } ( b ^ { j - 1 } ) .
$$

Proof The decomposition formulas follow from Theorem 7.1. For the reconstruction formula, Theorem 7.2 implies

$$
\begin{array} { r l } { a ^ { j } = ( T _ { P ^ { \ast } } \circ U ) ( a ^ { j - 1 } ) + ( T _ { Q ^ { \ast } } \circ U ) ( b ^ { j - 1 } ) } \\ { = ( T _ { P } ^ { \ast } \circ D ^ { \ast } ) ( a ^ { j - 1 } ) + ( T _ { Q } ^ { \ast } \circ D ^ { \ast } ) ( b ^ { j - 1 } ) } & { ( \mathrm { u s i n g ~ L e m m a ~ 7 . 3 } ) } \\ { = ( D \circ T _ { P } ) ^ { \ast } ( a ^ { j - 1 } ) + ( D \circ T _ { Q } ) ^ { \ast } ( b ^ { j - 1 } ) } & { ( \mathrm { u s i n g ~ T h e o r e m ~ 0 . 3 2 } ) } \\ { = T _ { 0 } ^ { \ast } ( a ^ { j - 1 } ) + T _ { 1 } ^ { \ast } ( b ^ { j - 1 } ) . } \end{array}
$$

Equations (7.2) and (7.3) can be combined as

$$
a ^ { j } = ( T _ { 0 } ^ { \ast } \circ T _ { 0 } + T _ { 1 } ^ { \ast } \circ T _ { 1 } ) ( a ^ { j } ) , \cdot
$$

which is another way of stating that the reconstruction process is the adjoint of decomposition and that the reconstruction process inverts decomposition [because $( T _ { 0 } ^ { * } \circ T _ { 0 } + T _ { 1 } ^ { * } \circ T _ { 1 } )$ sends the sequence $\pmb { a } ^ { j }$ to itself]. Operators with this property have a special name.

DEFINITIoN 7.5 A pair of filters, $\scriptstyle \mathbf { { \mathit { T } } } _ { P } $ and $\scriptstyle { \pmb { T _ { Q } } }$ (i.e., convolution operators with the sequences $\pmb { P }$ and $\pmb { Q }$ , respectively), is called $\pmb { a }$ quadrature mirror filter if the associated maps $T _ { 0 } = D \circ T _ { P }$ and $\scriptstyle T _ { 1 } = D \circ T _ { Q }$ satisfy

$$
( T _ { 0 } ^ { * } \circ T _ { 0 } ) ( x ) + ( T _ { 1 } ^ { * } \circ T _ { 1 } ) ( x ) = x
$$

for all sequences $x = ( \ldots , x _ { - 1 } , x _ { 0 } , x _ { 1 } , \ldots ) \in l ^ { 2 } ( Z ) .$

An equivalent formulation of equation (7.4) is

$$
\| T _ { 0 } x \| ^ { 2 } + \| T _ { 1 } x \| ^ { 2 } = \| x \| ^ { 2 } .
$$

For if equation (7.4) holds, then

$$
\begin{array} { r l } & { \| x \| ^ { 2 } = \langle x , x \rangle \quad \mathrm { ( b y ~ d e f i n i t i o n ~ o f ~ \| \cdot \| ) } } \\ & { \qquad = \langle ( T _ { 0 } ^ { * } \circ T _ { 0 } + T _ { 1 } ^ { * } \circ T _ { 1 } ) ( x ) , x \rangle \quad \mathrm { ( b y ~ e q u a t i o n ~ ( 7 . 4 ) ) } } \\ & { \qquad = \langle T _ { 0 } x , T _ { 0 } x \rangle + \langle T _ { 1 } x , T _ { 1 } x \rangle \quad \mathrm { b y ~ d e f i n i t i o n ~ o f ~ a d j o i n t } } \\ & { \qquad = \| T _ { 0 } x \| ^ { 2 } + \| T _ { 1 } x \| ^ { 2 } . } \end{array}
$$

The $\imath ^ { 2 }$ -norm of a signal $\pmb { x } = ( \dots , \pmb { x } _ { - 1 } , \pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \dots )$ , (i.e., $\textstyle \sum _ { n } x _ { n } ^ { 2 } )$ is proportional to the energy of the signal. So a physical interpretation of equation (7.4) is that a quadrature mirror filter preserves the energy of a signal.

# 7.3.1 Transfer Function Interpretation

Our goal in this section is to transcribe the defining property of a quadrature mirror filter

$$
( T _ { 0 } ^ { * } \circ T _ { 0 } ) ( x ) + ( T _ { 1 } ^ { * } \circ T _ { 1 } ) ( x ) = x
$$

into a condition on the transfer functions of the filters $\pmb { T _ { P } }$ and $\scriptstyle { \pmb { T _ { Q } } }$ .

First, we recall the definition of a transfer function given in Chapter 3 (just after Theorem 3.13). A sequence $\pmb { x } = ( \dots , \pmb { x } _ { - 1 } , \pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \dots ) \in l ^ { 2 } ( Z )$ has a discrete Fourier transform $\widehat { \pmb { x } }$ that is a function on the interval $- \pi \leq \theta \leq \pi$ defined by

$$
{ \widehat { x } } ( \theta ) = \sum _ { n = - \infty } ^ { \infty } x _ { n } e ^ { - i n \theta } .
$$

If $\pmb { T _ { P } }$ is a convolution operator with the sequence $\scriptstyle P _ { n }$ —that is, $( T _ { P } x ) _ { n } =$ $\begin{array} { r } { \sum _ { k } P _ { n - k } x _ { k } } \end{array}$ —then the transfer function of $\pmb { T } _ { P }$ is the function $\widehat { T _ { P } }$ on the interval $- \pi \leq \theta \leq \pi$ defined by

$$
\widehat { T _ { P } } ( \theta ) = \sum _ { n } P _ { n } e ^ { - i n \theta } .
$$

As shown in Theorem 3.13,

$$
{ \widehat { T _ { P } ( x ) } } ( \theta ) = { \widehat { T _ { P } } } ( \theta ) { \widehat { x } } ( \theta ) .
$$

Another key property that we will use is the computation of the transfer function of the transpose of a convolution operator; that is,

$$
\widehat { F ^ { * } } ( \theta ) = \overline { { \widehat { F } } } ( \theta )
$$

which is established in Theorem 3.14.

To transcribe equation (7.5) into one involving transfer functions, we take the discrete Fourier transform (the hat of) both sides of this equation. In what follows, we use the notation $\mathcal { F } ( \boldsymbol { x } ) ( \theta ) = \widehat { \boldsymbol { x } } ( \theta )$ for expressions, $\pmb { x }$ ,that are long. We start with the $( T _ { 0 } ^ { \ast } \circ T _ { 0 } ) ( x )$ term on the left side,

$$
\begin{array} { r l } { \mathcal { F } ( ( T _ { 0 } ^ { * } \circ T _ { 0 } ) ( x ) ) ( \theta ) = \mathcal { F } ( T _ { P } ^ { * } \circ D ^ { * } \circ D \circ T _ { P } ) ( x ) ( \theta ) } & { } \\ { \qquad = \widehat { T _ { P } ^ { * } } ( \theta ) \cdot \mathcal { F } ( ( D ^ { * } \circ D \circ T _ { P } ) ( x ) ) ( \theta ) } & { } \\ { \qquad = \overline { { \widehat { T _ { P } } ( \theta ) } } \cdot \mathcal { F } ( ( D ^ { * } \circ D \circ T _ { P } ) ( x ) ) ( \theta ) } & { } \end{array}
$$

where the last two equalities use (7.6) and (7.7), respectively. Now if $\pmb { y }$ is the sequence ${ \pmb y } _ { n }$ , $\boldsymbol { \mathscr { n } } \in \boldsymbol { \mathscr { Z } }$ , then from the last section, $( D y ) _ { n } = y _ { n }$ for $\pmb { n } = 2 k$ an even integer. So

$$
( D ^ { * } D y ) _ { n } = { \left\{ \begin{array} { l l } { y _ { n } } & { { \mathrm { f o r ~ } } n { \mathrm { ~ e v e n , ~ i . e . , ~ } } n = 2 k } \\ { 0 } & { { \mathrm { f o r ~ } } n { \mathrm { ~ o d d . } } } \end{array} \right. }
$$

Therefore,

$$
\widehat { D ^ { * } D y } ( \theta ) = \sum _ { k } y _ { 2 k } e ^ { - i 2 k \theta }
$$

which can be redescribed as

$$
\widehat { D ^ { * } D y } ( \theta ) = \sum _ { n } y _ { n } ( e ^ { - i n \theta } + e ^ { - i n ( \theta + \pi ) } ) / 2
$$

(the terms when $\scriptstyle { \pmb { n } }$ is odd cancel since then $e ^ { - i n \pi } = - 1$ .Therefore,

$$
\widehat { D ^ { * } D y } ( \theta ) = \left( \widehat { y } ( \theta ) + \widehat { y } ( \theta + \pi ) \right) / 2 .
$$

Applying this equation to the sequence $y _ { n } = F _ { 0 } ( x ) _ { n }$ yields

$$
\begin{array} { r l } & { \mathcal { F } ( ( D ^ { * } \circ D \circ T _ { P } ) ( x ) ) ( \theta ) = \left( \widehat { T _ { P } ( x ) } ( \theta ) + \widehat { T _ { P } ( x ) } ( \theta + \pi ) \right) / 2 } \\ & { \qquad = \left( \widehat { T _ { P } } ( \theta ) \widehat { x } ( \theta ) + \widehat { T _ { P } } ( \theta + \pi ) \widehat { x } ( \theta + \pi ) \right) / 2 . } \end{array}
$$

Inserting this into the end of (7.10), we obtain

$$
\mathcal { F } ( ( T _ { 0 } ^ { * } \circ T _ { 0 } ) ( x ) ) ( \theta ) = \widehat { T _ { P } ( \theta ) } \left( \widehat { T _ { P } } ( \theta ) \widehat { x } ( \theta ) + \widehat { T _ { P } } ( \theta + \pi ) \widehat { x } ( \theta + \pi ) \right) / 2 .
$$

Similarly,

$$
\mathcal { F } ( ( T _ { 1 } ^ { * } \circ T _ { 1 } ) ( x ) ) ( \theta ) = \widehat { T _ { Q } ( \theta ) } \left( \widehat { T _ { Q } } ( \theta ) \widehat { x } ( \theta ) + \widehat { T _ { Q } } ( \theta + \pi ) \widehat { x } ( \theta + \pi ) \right) / 2 .
$$

Adding these two equations and setting the result equal to ${ \widehat { \pmb x } } ( \pmb \theta )$ [as required by equation (7.5)] yields

$$
\begin{array} { r l } & { \left( \frac { | \widehat { T _ { P } } ( \theta ) | ^ { 2 } + | \widehat { T _ { Q } } ( \theta ) | ^ { 2 } } { 2 } \right) \widehat { x } ( \theta ) } \\ & { + \left( \frac { \widehat { T _ { P } } ( \theta ) \widehat { T _ { P } } ( \theta + \pi ) + \widehat { T _ { Q } } ( \theta ) \widehat { T _ { Q } } ( \theta + \pi ) } { 2 } \right) \widehat { x } ( \theta + \pi ) = \widehat { x } ( \theta ) . } \end{array}
$$

Let $G ( \pmb \theta )$ be the term inside the first parenthesis on the left and let ${ \pmb H } ( \pmb \theta )$ be the term on the inside of the second parenthesis. The preceding equation now reads

$$
G ( \theta ) \widehat { x } ( \theta ) + H ( \theta ) \widehat { x } ( \theta + \pi ) = \widehat { x } ( \theta ) ,
$$

which must hold for all sequences $\pmb { x }$ We first apply this equation when ${ \widehat x } ( \theta ) = 1$ , which occurs when $\pmb { x }$ is the sequence given by ${ \pmb x } _ { 0 } = { \pmb 1 }$ and $\pmb { x _ { n } = 0 }$ for nonzero $\pmb { n }$ . We obtain

$$
G ( \theta ) + H ( \theta ) = 1 .
$$

Now apply the equation when ${ \widehat { \pmb { x } } } ( \pmb { \theta } ) = e ^ { i \pmb { \theta } }$ , which occurs when $\pmb { x }$ is the sequence given by $\pmb { x _ { 1 } } = \pmb { 1 }$ and $\pmb { x _ { n } = 0 }$ for all other $_ { \pmb { n } }$ After dividing by $e ^ { i \theta }$ , we obtain

$$
G ( \theta ) - H ( \theta ) = 1 .
$$

Adding these two equations, we obtain $G ( \theta ) = 1$ Subtracting these two equations yields $\mathbf { \mathcal { H } } ( \pmb { \theta } ) = \mathbf { 0 }$ Inserting the expressions for $\pmb { G }$ and $\pmb { H }$ , we obtain the following theorem

THeOREM 7.6 The filters $\scriptstyle \mathbf { { \mathit { T } } } _ { P } $ and $\scriptstyle { T _ { Q } }$ form a quadrature mirror filter if and only if

$$
\begin{array} { r l r } & { } & { | \widehat { T _ { P } } ( \theta ) | ^ { 2 } + | \widehat { T _ { Q } } ( \theta ) | ^ { 2 } = 2 } \\ & { } & { \widehat { T _ { P } } ( \theta ) \widehat { T _ { P } } ( \theta + \pi ) + \widehat { \widetilde { T _ { Q } } } ( \theta ) \widehat { T _ { Q } } ( \theta + \pi ) = 0 } \end{array}
$$

or, equivalently, the matrix

$$
\left( \begin{array} { c c } { { \widehat { T _ { P } } ( \theta ) / \sqrt { 2 } } } & { { \widehat { T _ { Q } } ( \theta ) / \sqrt { 2 } } } \\ { { \widehat { T _ { P } } ( \theta + \pi ) / \sqrt { 2 } } } & { { \widehat { T _ { Q } } ( \theta + \pi ) / \sqrt { 2 } } } \end{array} \right)
$$

is unitary.

When the quadrature mirror filters come from a scaling function and wavelet, then the (transpose of the) unitary matrix in the preceding theorem becomes

$$
\left( { \begin{array} { l l } { { \overline { { p ( \theta ) } } } } & { { \overline { { p ( \theta + \pi ) } } } } \\ { { \overline { { q ( \theta ) } } } } & { { \overline { { q ( \theta + \pi ) } } } } \end{array} } \right)
$$

with $p ( \theta ) = P ( e ^ { - i \theta } )$ and $q ( \theta ) = Q ( e ^ { - i \theta } )$ as defined in Section 5.3.3. This is the same matrix as that given after Theorem 5.21, and we saw that this matrix was unitary from the techniques given in that section.

# 7.4 Wavelet Transform

In Chapter 2 on the Fourier transform, we discussed the Fourier inversion formula. In this section, we develop an analogous wavelet transform and its associated inversion formula. Let us first review the Fourier transform. For a function, $f ,$ in $L ^ { 2 } ( R )$ , its Fourier transform is given by

$$
{ \mathcal { F } } ( f ) ( \lambda ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i \lambda t } d t .
$$

Another notation for the Fourier transform is $\widehat { f } ( \lambda )$ The inverse Fourier transform of a function $\pmb { \mathscr { g } } \in \pmb { L } ^ { 2 } ( R )$ is given by

$$
\mathcal { F } ^ { - 1 } ( g ) ( x ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } g ( \lambda ) e ^ { i \lambda x } d \lambda .
$$

The content of the Fourier inversion Theorem 2.1 is that $\mathcal { F } ^ { - 1 }$ , as defined previously, really is the inverse operator of $\pmb { \mathcal { F } }$ ;that is,

$$
f = { \mathcal { F } } ^ { - 1 } { \mathcal { F } } ( f ) .
$$

As discussed in Chapter 2, ${ \mathcal { F } } ( f ) ( \lambda )$ roughly measures the component of $\pmb { f }$ that oscillates with frequency $\lambda$ The inversion formula $f = \mathcal { F } ^ { - 1 } \mathcal { F } ( f )$ , when written as

$$
f ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } { \widehat { f } } ( \lambda ) e ^ { i \lambda x } d \lambda ,
$$

expresses the fact that $\pmb { f }$ can be written as a weighted sum (or integral) of its various frequency components.

# 7.4.1 Definition of the Wavelet Transform

The wavelet transform and its associated inversion formula also decompose a function into a weighted sum of its various frequency components. However, this time the weights involve a given wavelet rather than the exponential term $e ^ { i \lambda x }$ .

To introduce the wavelet transform, we assume that a wavelet function, $\psi ( { \pmb x } )$ is given that satisfies the following two requirements:

1. $\psi ( { \pmb x } )$ is continuous and has. exponential decay [i.e., $\psi ( x ) \leq M e ^ { - C | x | }$ for some constants $c$ and $M ]$ .   
2. The integral of $\psi$ is zero [i.e., $\textstyle \int _ { - \infty } ^ { \infty } \psi ( x ) d x = 0 ]$ .

An example of a suitable wavelet function is $\psi ( x ) = x e ^ { - x ^ { 2 } }$ , whose graph appears in Figure 1. Another example is the wavelet function of Daubechies constructed in the previous chapter. The Daubechies wavelet is only nonzero on a finite interval, so the first requirement is automatically satisfied (by taking the constant $\pmb { M }$ large enough). Note that no assumptions are made concerning orthogonality of the wavelet with its translates. The Daubechies wavelets are constructed so that their translates are orthogonal, but the preceding example $\psi ( x ) = x e ^ { - x ^ { 2 } }$ is not orthogonal to its translates.

In the derivations that follow, we assume that $\psi ( x )$ equals zero outside some fixed interval $- A \leq x \leq A$ , which is a stronger condition than the first condition just given. However, every derivation given can be modified to include wavelets with exponential decay.

We are now ready to state the definition of the wavelet transform.

DEFINITION 7.7 Given a wavelet $\psi$ satisfying the two requirements just given, the wavelet transform of $\pmb { a }$ function $f \in L ^ { 2 } ( R )$ is a function $W _ { f } : R ^ { 2 } \mapsto R$ given by

$$
W _ { f } ( a , b ) = { \frac { 1 } { \sqrt { | a | } } } \int _ { - \infty } ^ { \infty } f ( x ) \overline { { \psi \left( { \frac { x - b } { a } } \right) } } d x .
$$

From the preceding definition, it is not clear how to define the wavelet transform at ${ \pmb a = 0 }$ However, the change of variables ${ \pmb y } = ( { \pmb x } - { \pmb b } ) / { \pmb a }$ converts the wavelet transform into the following:

$$
W _ { f } ( a , b ) = { \sqrt { | a | } } \int _ { - \infty } ^ { \infty } f ( y a + b ) ) { \overline { { \psi ( y ) } } } d y .
$$

![](images/02d23ebf74d98041f42b8d48cf48ff5a6bf6fe2924aecba6ff3554e0127f75b9.jpg)  
Figure 1 Graph of $\psi _ { 1 , 0 } ( x ) = \psi ( x ) = x e ^ { - x ^ { 2 } }$

From this representation, clearly $W _ { f } ( a , b ) = 0$ when ${ \pmb a } = { \bf 0 }$ .

As $\pmb { a }$ gets small, the graph of

$$
\psi _ { a , b } ( x ) = { \frac { 1 } { \sqrt { | a | } } } \psi \left( { \frac { x - b } { a } } \right)
$$

becomes tall and skinny, as illustrated in the graphs of $\psi _ { 1 , 0 }$ and $\psi _ { 1 / 2 , 0 }$ with $\psi ( x ) = x e ^ { - x ^ { 2 } }$ ven  Fiure  eivelyThere, h of $\psi _ { a , b }$ increases as $\pmb { a }$ gets small. Also note that if most of the support of $\psi$ . (i.e., the nonzero part of the graph of $\psi$ ) is located near the origin (as with the preceding example), then most of the support of $\psi _ { a , b }$ will be located near ${ \pmb x } = { \pmb b }$ So $W _ { f } ( a , b )$ measures the frequency component of $\pmb { f }$ that vibrates with frequency proportional to $1 / a$ near the point ${ \pmb x } = { \pmb b }$ .

# 7.4.2 Inversion Formula for the Wavelet Transform

The inversion formula for the wavelet transform is given in the following theorem.

![](images/556903d0b91f5afef5c1ed90e544a4f5fda067558674e0afcb3f90a3e4cfcdc7.jpg)  
Figure 2 Graph of $\psi _ { 1 / 2 , 0 }$

THEOREM 7.8 Suppose $\psi$ is a continuous wavelet satisfying the following:

• $\psi$ has exponential decay at infinity. $\bullet \ \int _ { - \infty } ^ { \infty } \psi ( x ) d x = 0 . . .$

Then for any function $f \in L ^ { 2 } ( R )$ , the following inversion formula holds:

$$
f ( x ) = { \frac { 1 } { C _ { \psi } } } \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } | a | ^ { - 1 / 2 } \psi \left( { \frac { x - b } { a } } \right) W _ { f } ( a , b ) { \frac { d b d a } { a ^ { 2 } } }
$$

where

$$
C _ { \psi } = 2 \pi \int _ { - \infty } ^ { \infty } \frac { | \widehat { \psi } ( \lambda ) | ^ { 2 } } { | \lambda | } d \lambda .
$$

As with the Fourier inversion theorem, the preceding wavelet inversion theorem essentially states that a function $\pmb { f }$ can be decomposed as a weighted sum (or integral) of its frequency components, as measured by $W _ { f } ( a , b )$ . The difference is that with the wavelet inversion theorem, two parameters, $\pmb { a }$ and $\pmb { b }$ ,are involved since the wavelet transform involves a measure of the frequency (using the parameter $\pmb { a }$ of $\pmb { f }$ near the point ${ \pmb x } = { \pmb b }$ .

Before we start the proof, we should state why $c _ { \psi }$ is finite (since the integrand defining it appears to become infinite at $\lambda = 0$ . First, we split the integral that defines $c _ { \psi }$ into two pieces: one involving an integral over $| \lambda | \geq 1$ and a second involving the integral over $| \lambda | < 1$ For the first integral, we note that $\psi$ has exponential decay and so $\psi$ is a member of $L ^ { 2 } ( R )$ Therefore, its

Fourier transform also belongs to $L ^ { 2 } ( R )$ and so

$$
\begin{array} { r l r } {  { \int _ { | \lambda | \geq 1 } \frac { | \widehat { \psi } ( \lambda ) | ^ { 2 } } { | \lambda | } d \lambda \leq \int _ { | \lambda | \geq 1 } | \widehat { \psi } ( \lambda ) | ^ { 2 } d \lambda } } \\ & { } & { < \infty \quad \mathrm { s i n c c } ~ \widehat { \psi } \in L ^ { 2 } ( R ) . } \end{array}
$$

For the second integral, it is a fact that the exponential decay assumption on $\psi$ implies $\widehat { \psi }$ is differentiable. From a first-order (Taylor) expansion about $\lambda = 0$

$$
\widehat { \psi } ( \lambda ) = \widehat { \psi } ( 0 ) + { \cal O } ( \lambda ) \quad ( \mathrm { T a y l o r ^ { \prime } s \ t h e o r e m } )
$$

where $O ( \lambda )$ stands for terms that are bounded by $C 1 \lambda 1$ for some constant $c$ . We also have $\begin{array} { r } { \widehat { \psi } ( 0 ) = \int \psi ( x ) d x = 0 } \end{array}$ by the second assumption on $\psi$ stated in the theorem. Therefore, the second integral can be estimated by

$$
\int _ { | \lambda | < 1 } \frac { | \widehat { \psi } ( \lambda ) | ^ { 2 } } { | \lambda | } d \lambda \leq \int _ { | \lambda | < 1 } \frac { | C \lambda | ^ { 2 } } { | \lambda | } d \lambda < \infty .
$$

Since both integral pieces of $\boldsymbol { C } _ { \boldsymbol { \psi } }$ are finite, we conclude that $c _ { \psi }$ is finite as well.

Proof of the Wavelet Transform Theorem Let $\pmb { F } ( \pmb { x } )$ be the quantity given on the right of the main statement of the theorem; that is,

$$
F ( x ) = \frac { 1 } { C _ { \psi } } \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } | a | ^ { - 1 / 2 } \psi \left( \frac { x - b } { a } \right) W _ { f } ( a , b ) \frac { d b d a } { a ^ { 2 } } .
$$

We must show that ${ \pmb F } ( { \pmb x } )$ is equal to $\pmb { f } ( \pmb { x } )$ We accomplish this using the following two steps.

Step 1. We first show

$$
F ( x ) = { \frac { 1 } { C _ { \psi } } } \int _ { - \infty } ^ { \infty } { \frac { d a } { \sqrt { | a | a ^ { 2 } } } } \int _ { - \infty } ^ { \infty } { \overline { { \mathcal { F } _ { b } \left\{ { \overline { { \psi \left( { \frac { x - b } { a } } \right) } } } \right\} ( y ) } } } { \mathcal { F } } _ { b } \left\{ W _ { f } ( a , b ) \right\} ( y ) d y
$$

where $\mathcal { F } _ { b } \{ \cdot \}$ stands for the Fourier transform of the quantity inside the brackets $\{ , \}$ with respect to the variable $\pmb { b }$ .

This step follows by applying Plancherel's formula (Theorem 2.12), which states that $\begin{array} { r } { \int v u = \int \overline { { \mathcal { F } ( \overline { { v } } ) } } \mathcal { F } ( u ) } \end{array}$ . This theorem is applied to the $\scriptstyle \mathbf { b }$ -integral occurring in the definition of $\scriptstyle { F ( x ) }$ and where $v ( b ) = \psi ( ( x - b ) / a )$ and $u ( b ) = W _ { f } ( a , b )$ (with $\pmb { x }$ and $\pmb { a }$ constant). In order to apply the Plancherel theorem, both of these functions must belong to $L ^ { 2 } ( R )$ .If $\pmb { f }$ and $\psi$ have finite support, then the $\pmb { b }$ support of $W _ { f } ( a , b )$ will also be finite (as you can check) and so $W _ { f } ( a , b )$ and $\psi \left( { \frac { x - b } { a } } \right)$ are $L ^ { 2 }$ functions in $\pmb { b }$ .

Step 2. The next step is to evaluate the two Fourier $^ { b }$ -transforms occurring in the integrand of Step 1. We show

$$
\overline { { \mathcal { F } _ { b } \left\{ \psi \left( \frac { x - b } { a } \right) \right\} } } ( y ) = a e ^ { i y x } \widehat { \psi } ( a y )
$$

$$
{ \mathcal { F } } _ { b } \left\{ W _ { f } ( a , b ) \right\} ( y ) = a { \sqrt { \frac { 2 \pi } { | a | } } } { \widehat { \psi } } ( a y ) { \widehat { f } } ( y )
$$

We establish Step 2 later. Assuming this step for the moment, we proceed to the conclusion. Combining Steps 1 and 2, we obtain

$$
\begin{array} { r l r } & { } & { F ( x ) = \displaystyle \frac { 1 } { C _ { \psi } } \int _ { - \infty } ^ { \infty } \frac { \sqrt { 2 \pi } d a } { | a | } \int _ { - \infty } ^ { \infty } | \widehat { \psi } ( a y ) | ^ { 2 } \widehat { f } ( y ) e ^ { i y x } d y } \\ & { } & { \quad = \displaystyle \frac { 1 } { C _ { \psi } } \int _ { - \infty } ^ { \infty } \sqrt { 2 \pi } \widehat { f } ( y ) e ^ { i y x } d y \int _ { - \infty } ^ { \infty } \frac { | \widehat { \psi } ( a y ) | ^ { 2 } } { | a | } d a } \end{array}
$$

where the last equality follows by interchanging the order of the ${ \pmb y } -$ and $\pmb { a }$ integrals. To calculate the $\pmb { a }$ -integral on the right, we make a change of variables $\pmb { u } = \pmb { a } \pmb { y }$ (and so $d u = y d a$ provided that $y \neq 0$ to obtain

$$
\begin{array} { c } { { \displaystyle { \int _ { - \infty } ^ { \infty } \frac { | \widehat { \psi } ( a y ) | ^ { 2 } } { | a | } d a = \int _ { - \infty } ^ { \infty } \frac { | \widehat { \psi } ( u ) | ^ { 2 } } { | u | } d u } } } \\ { { { } } } \\ { { = \displaystyle { \frac { C _ { \psi } } { 2 \pi } } . } } \end{array}
$$

If $\pmb { y } = \mathbf { 0 }$ , then by assumption $\widehat { \psi } ( 0 ) = 0$ and so the rightmost integral in (7.12) is zero. Therefore, the rightmost integral in (7.12) is equal to $c _ { \psi } / 2 \pi$ for all values of ${ \pmb y }$ except $\pmb { y } = \pmb { 0 }$ Since the ${ \pmb y }$ -integral in (7.12) is not affected by the value of the integrand at the single point $\pmb { y } = \pmb { 0 }$ ,we can substitute (7.14) into (7.12) to obtain

$$
\begin{array} { l } { { \displaystyle { \cal F } ( x ) = \frac { 1 } { C _ { \psi } } \int _ { - \infty } ^ { \infty } \sqrt { 2 \pi } \widehat { f } ( y ) e ^ { i y x } \frac { C _ { \psi } } { 2 \pi } d y } } \\ { ~ } \\ { { \displaystyle ~ = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \widehat { f } ( y ) e ^ { i y x } d y } } \\ { ~ } \\ { { \displaystyle ~ = f ( x ) ~ } } \end{array}
$$

where the last equality follows from the Fourier inversion theorem. This finishes the proof, modulo the derivation of Step 2, which we present next.

Proof of Step 2 The first equality in Step 2 follows from the sixth property of Theorem 2.6. In more detail, we use the definition of the Fourier trans-

form to obtain

$$
{ \mathcal { F } } _ { b } \left( { \overline { { \psi \left( { \frac { x - b } { a } } \right) } } } \right) ( y ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } { \overline { { \psi \left( { \frac { x - b } { a } } \right) } } } e ^ { - i b y } d b
$$

After the change of variables ${ \pmb v } = ( { \pmb x } - { \pmb b } ) / a$ , this becomes

$$
\begin{array} { l } { \displaystyle \mathcal { F } _ { b } \left( \psi \left( \frac { x - b } { a } \right) \right) ( y ) = \frac { a } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \overline { { \psi ( v ) } } e ^ { - i y ( x - v a ) } d v } \\ { \displaystyle = a e ^ { - i y x } \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } \psi ( v ) e ^ { - i a y v } d v } \\ { \displaystyle = a e ^ { - i y x } \overline { { \widehat { \psi } ( a y ) } } . } \end{array}
$$

Taking conjugates of both sides of this equation establishes the first cquality in Step 2.

To establish the second equality, we use the definition of the wavelet transform

$$
\mathcal { F } _ { b } \left\{ W _ { f } ( a , b ) \right\} ( y ) = \mathcal { F } _ { b } \left\{ \frac { 1 } { \sqrt { | a | } } \int _ { - \infty } ^ { \infty } \overline { { \phi \left( \frac { x - b } { a } \right) } } f ( x ) d x \right\} ( y ) .
$$

The next step is to bring the Fourier transform operator $\mathcal { F } _ { b }$ under the integral sign. This can be accomplished by viewing thc intcgral as a sum and using the linearity of the Fourier transform operator. More precisely, wc approximate the integral on the right by the following Riemann sum:

$$
\begin{array} { r l r } {  { \mathcal { F } _ { b } \{ \frac { 1 } { \sqrt { | a | } } \int _ { - \infty } ^ { \infty } \overline { { \psi ( \frac { x - b } { a } ) } } f ( x ) d x \} ( y ) } } \\ & { } & { \approx \mathcal { F } _ { b } \{ \frac { 1 } { \sqrt { | a | } } \sum _ { j } \overline { { \psi ( \frac { x _ { j } - b } { a } ) } } f ( x _ { j } ) \Delta x \} ( y ) } \end{array}
$$

This approximation becomes more accurate as the partition gets finer (i.c., as $\Delta x \mapsto 0$ . The Fourier transform operator, $\mathcal { F } _ { b }$ ,is linear and can be brought inside the sum to obtain

$$
\begin{array} { r l r } {  { \mathcal { F } _ { b } \{ \frac { 1 } { \sqrt { \lvert a \rvert } } \int _ { - \infty } ^ { \infty } \overline { { \psi ( \frac { x - b } { a } ) } } f ( x ) d x \} ( y ) } } \\ & { } & { \approx \frac { 1 } { \sqrt { \lvert a \rvert } } \sum _ { j } \mathcal { F } _ { b } \{ \overline { { \psi ( \frac { x _ { j } - b } { a } ) } } \} ( y ) f ( x _ { j } ) \Delta x . } \end{array}
$$

Now we let the partition get finer and obtain (in the limit as $\Delta x \mapsto 0 .$

$$
\mathcal { F } _ { b } \left\{ W _ { f } ( a , b ) \right\} ( y ) = \frac { 1 } { \sqrt { | a | } } \int _ { - \infty } ^ { \infty } \mathcal { F } _ { b } \left\{ \overline { { \psi \left( \frac { x - b } { a } \right) } } \right\} ( y ) f ( x ) d x ,
$$

Inserting (7.17) into this equation, we obtain

$$
\begin{array} { l } { \displaystyle \mathcal { F } _ { b } \left\{ W _ { f } ( a , b ) \right\} ( \boldsymbol { y } ) = \frac { a } { \sqrt { | a | } } \int _ { - \infty } ^ { \infty } e ^ { - i y x } \widehat { \psi } ( a y ) f ( \boldsymbol { x } ) d x } \\ { \displaystyle \quad \quad = \frac { a } { \sqrt { | a | } } \widehat { \tilde { \psi } ( a y ) } \int _ { - \infty } ^ { \infty } f ( \boldsymbol { x } ) e ^ { - i y x } d x } \\ { \displaystyle \quad \quad = \frac { a \sqrt { 2 \pi } } { \sqrt { | a | } } \widehat { \tilde { \psi } ( a y ) } \widehat { f } ( \boldsymbol { y } ) } \end{array}
$$

as claimed in the second equation of Step 2. This completes the derivation in Step 2 and the proof of the theorem. $\bullet$

# Appendix A Technical Matters

# A.1 Proof of the Fourier Inversion Formula

In this section we give a rigorous proof of Theorem 2.1 (the Fourier inversion theorem), which states that for an integrable function $\pmb { f }$

$$
f = { \mathcal { F } } ^ { - 1 } \circ { \mathcal { F } } ( f ) .
$$

Inserting the definitions of $\mathcal { F }$ and $\mathcal { F } ^ { - 1 }$ , we must show

$$
f ( x ) = { \frac { 1 } { 2 \pi } } \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i ( t - x ) \lambda } d t d \lambda .
$$

We restrict our attention to functions, $\pmb { f }$ , which are nonzero only on some finite interval, to avoid the technicalities of dealing with convergent integrals over infinite intervals (for details, see Tolstov [22]). If $\pmb { f }$ is nonzero only on a finite interval, then the $\pmb { t }$ -integral occurs only on this finite interval (instead of $- \infty < t < \infty$ as it appears). The $\lambda$ -integral still involves an infinite interval and so this must be handled by integrating over a finite interval of the form $- l \leq \lambda \leq l$ and then letting $\pmb { l }  \infty$ . So we must show

$$
f ( x ) = { \frac { 1 } { 2 \pi } } \operatorname* { l i m } _ { l \to \infty } \int _ { - l } ^ { l } \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - i ( t - x ) \lambda } d t d \lambda .
$$

Using the definition of the complex exponential $( e ^ { i u } = \cos u + i \sin u )$ , the preceding limit is equivalent to showing

$$
f ( x ) = \frac { 1 } { 2 \pi } \operatorname* { l i m } _ { l  \infty } \int _ { - l } ^ { l } \int _ { - \infty } ^ { \infty } f ( t ) ( \cos ( ( t - x ) \lambda ) - i \sin ( ( t - x ) \lambda ) ) d t d \lambda
$$

Since sin is an odd function, the $\lambda$ integral involving $\sin ( ( t - x ) \lambda )$ is zero. Together with the fact that cos is an even function, the preceding limit is equivalent to

$$
f ( x ) = \frac { 1 } { \pi } \operatorname* { l i m } _ { l  \infty } \int _ { 0 } ^ { l } \int _ { - \infty } ^ { \infty } f ( t ) \cos ( ( t - x ) \lambda ) d t d \lambda .
$$

Now $\begin{array} { r } { \int _ { 0 } ^ { l } \cos ( ( t - x ) \lambda ) d \lambda = \frac { \sin ( ( t - x ) l ) } { t - x } } \end{array}$ By replacing $\mathbf { \Delta } _ { t }$ by $\pmb { x } + \pmb { u }$ , the preceding limit is equivalent to

$$
f ( x ) = { \frac { 1 } { \pi } } \operatorname* { l i m } _ { l \to \infty } \int _ { - \infty } ^ { \infty } f ( x + u ) { \frac { \sin ( l u ) } { u } } d u .
$$

To establish this limit, we must show that for any given $\epsilon > 0$ , the difference between $f ( x )$ and the integral on the right is less than e provided that $\iota$ is sufficiently large. For this given e, we choose a $\delta > 0$ so that

$$
\frac { 1 } { \pi } \int _ { - \delta } ^ { \delta } | f ( x + u ) | d u < \epsilon
$$

(geometrically, the integral on the left is the area under the graph of $\left| f \right|$ over an interval of width 2δ and by choosing $\delta$ small enough, we can arrange that the area of this sliver is less than e). We use this inequality at the end of our proof.

Now we need to use the Riemann-Lebesgue lemma (Theorem 1.21), which states

$$
\operatorname* { l i m } _ { l \to \infty } \int _ { a } ^ { b } g ( u ) \sin ( l u ) d u = 0
$$

where $\pmb { \mathscr { s } }$ is any piecewise continuous function. Here, $\pmb { a }$ or $\pmb { b }$ could be infinity if $\pmb { \mathscr { g } }$ . is nonzero only on a finite interval. By letting $g ( u ) = f ( x + u ) / u ,$ ,this lemma implies

$$
\frac { 1 } { \pi } \int _ { - \infty } ^ { - \delta } f ( x + u ) \frac { \sin ( l u ) } { u } d u \quad \mathrm { a n d } \quad \frac { 1 } { \pi } \int _ { \delta } ^ { \infty } f ( x + u ) \frac { \sin ( l u ) } { u } d u  0
$$

as $\ell \to \infty$ [the function $g ( u ) = f ( x + u ) / u$ is continuous on both intervals of integration]. Thus the limit in (A.1) is equivalent to showing

$$
f ( x ) = { \frac { 1 } { \pi } } \operatorname* { l i m } _ { l \to \infty } \int _ { - \delta } ^ { \delta } f ( x + u ) { \frac { \sin ( l u ) } { u } } d u .
$$

On the other hand, we know from Step 5 in the proof of the convergence theorem for Fourier series [see Equation (1.27)] that

$$
{ \frac { 1 } { \pi } } \operatorname* { l i m } _ { n \to \infty } \int _ { - \pi } ^ { \pi } f ( x + u ) { \frac { \sin ( ( n + 1 / 2 ) u ) } { 2 \sin ( u / 2 ) } } d u = f ( x ) \quad { \mathrm { ( h e r e ~ } } n { \mathrm { ~ i s ~ a n ~ i n t e g e r ) . } }
$$

So our proof of (A.3) will proceed in two steps.

Step 1. We show

$$
\frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } f ( x + u ) \frac { \sin ( ( n + 1 / 2 ) u ) } { 2 \sin ( u / 2 ) } d u - \frac { 1 } { \pi } \int _ { - \delta } ^ { \delta } f ( x + u ) \frac { \sin ( ( n + 1 / 2 ) u ) } { u } d u \ :  \ : 0
$$

as $\textstyle n \to \infty$ After this step has been established, it [together with (A.4)] shows that

$$
{ \frac { 1 } { \pi } } \int _ { - \delta } ^ { \delta } f ( x + u ) { \frac { \sin ( ( n + 1 / 2 ) u ) } { u } } d u \to f ( x ) { \mathrm { a s ~ } } n \to \infty ,
$$

which is the same as the limit in (A.3) for $\iota$ of the form $\scriptstyle { l = n + 1 / 2 }$ To establish the more general limit in (A.3), we need the following.

Step 2. Any $\iota > 0$ can be written as ${ \boldsymbol { l } } = { \boldsymbol { n } } + { \boldsymbol { h } }$ , where $\pmb { n }$ is an integer and $0 \leq h < 1$ We show

$$
\frac { 1 } { \pi } \int _ { - \delta } ^ { \delta } f ( x + u ) \left( \frac { \sin ( ( n + 1 / 2 ) u ) } { u } - \frac { \sin ( l u ) } { u } \right) d u < \epsilon / 2 .
$$

Once these steps have been established, the proof of (A.3) (and therefore the proof of the Fourier inversion theorem) is completed as follows. Using (A.5), we can choose $\pmb { N }$ large enough so that if $\pmb { n } > N$ , then

$$
| f ( x ) - { \frac { 1 } { \pi } } \int _ { - \delta } ^ { \delta } f ( x + u ) { \frac { \sin ( ( n + 1 / 2 ) u ) } { u } } d u | < \epsilon / 2 .
$$

This inequality, together with the one in Step 2, yields

$$
\begin{array} { r l } & { \left| f ( x ) - \displaystyle \frac { 1 } { \pi } \int _ { - \delta } ^ { \delta } f ( x + u ) \frac { \sin ( l u ) } { u } d u \right| } \\ & { \qquad \le \displaystyle \left| f ( x ) - \frac { 1 } { \pi } \int _ { - \delta } ^ { \delta } f ( x + u ) \frac { \sin \left( \left( n + 1 / 2 \right) u \right) } { u } d u \right| } \\ & { \qquad + \left| \displaystyle \frac { 1 } { \pi } \int _ { - \delta } ^ { \delta } f ( x + u ) \left( \frac { \sin \left( \left( n + 1 / 2 \right) u \right) } { u } - \frac { \sin \left( l u \right) } { u } \right) d u \right| } \\ & { \qquad < \epsilon / 2 ~ \mathrm { { i f } } ~ n > N } \end{array}
$$

and our proof is complete.

Proof of Step 1 The statement of Step 1 is equivalent to

$$
\frac { 1 } { \pi } \int _ { - \delta } ^ { \delta } f ( x + u ) \sin ( ( n + 1 / 2 ) u ) \left( \frac { 1 } { 2 \sin ( u / 2 ) } - \frac { 1 } { u } \right) d u \to 0 \quad \mathrm { a s ~ } n \to \infty .
$$

# Because

$$
\int _ { - \pi } ^ { - \delta } { \frac { f ( x + u ) } { 2 \sin ( u / 2 ) } } \sin ( ( n + 1 / 2 ) u ) d u \quad { \mathrm { a n d } } \quad \int _ { \delta } ^ { \pi } { \frac { f ( x + u ) } { 2 \sin ( u / 2 ) } } \sin ( ( n + 1 / 2 ) u ) d u \to 0
$$

$\pmb { n }  \infty$ $( \frac { f ( x + u ) } { 2 \sin ( u / 2 ) }$ is contimous over the intervals $- \pi \leq u \leq - \delta$ and $\delta \leq u \leq \pi$ In addition, the quantity

$$
\frac { 1 } { 2 \sin ( u / 2 ) } - \frac { 1 } { u }
$$

is continuous on the interval $- \delta \leq u \leq \delta$ because the only possible discontinuity occurs at ${ \pmb u } = { \bf 0 }$ and the limit of this expression as $\mathbf { \nabla } \pmb { u }  \mathbf { 0 }$ is zero (using L'Hôspital's rule or a Taylor expansion). Therefore, the Riemann-Lebesgue lemma implies that the limit in (A.6) holds and the derivation of Step 1 is complete.

Proof of Step 2 For any ${ \bf \zeta } _ { l } > { \bf \zeta } _ { 0 }$ ,we write $l = n + h$ ,where $\pmb { n }$ is an integer and $0 \leq h < 1$ . Using the mean value theorem [which states that $f ( x ) - f ( y ) = f ^ { \prime } ( t ) ( x - y )$ for some $\pmb { t }$ between $\pmb { x }$ and $\boldsymbol { y } \rvert$ , we have

$$
\begin{array} { r l } & { | \sin ( ( n + 1 / 2 ) u ) - \sin ( l u ) | = | \sin ( ( n + 1 / 2 ) u ) - \sin ( ( n + h ) u ) | } \\ & { \phantom { | } = | \cos ( t ) | | u / 2 - h u | } \\ & { \phantom { | } \le | u | / 2 \quad \sin \mathrm { c e ~ } 0 \le h < 1 . } \end{array}
$$

Therefore,

$$
\begin{array} { l } { { \displaystyle  \frac { 1 } { \pi } \int _ { - \delta } ^ { \delta } \lvert f ( x + u ) ( \frac { \sin ( ( n + 1 / 2 ) u ) } { u } - \frac { \sin ( l u ) } { u } ) \rvert d u } } \\ { { \le \displaystyle \frac { 1 } { \pi } \int _ { - \delta } ^ { \delta } \lvert f ( x + u ) \rvert \frac { \lvert u \rvert } { 2 \lvert u \rvert } } } \\ { { \le \displaystyle \frac { \epsilon } { 2 } \quad \mathrm { b y ~ e q u a t i o n ~ } ( \mathbb { A } . 2 ) . } } \end{array}
$$

This completes the proof of Step 2 and the proof of the theorem.

# A.2 Rigorous Proof of Theorem 5.17

We restate Theorem 5.17 as follows:

Suppose $\phi$ is a continuous function with compact support satisfying the orthonormality condition: that is, $\begin{array} { r } { \int \phi ( \boldsymbol { x } - \boldsymbol { k } ) \phi ( \boldsymbol { x } - \boldsymbol { l } ) d \boldsymbol { x } = \delta _ { \boldsymbol { k } \boldsymbol { l } } } \end{array}$ . Let $\begin{array} { r } { V _ { j } = \{ f = \sum _ { k } a _ { k } \phi ( 2 ^ { j } x - k ) ; ~ a _ { k } \in \tilde { R } \} } \end{array}$ Then the following hold.

1. The spaces $V _ { j }$ satisfy the separation condition . $\cap V _ { j } = \{ 0 \} )$ .

2. If the following additional conditions are satisfied by $\phi$

•normalization: $\textstyle \int \phi ( { \boldsymbol { \mathbf { \mathit { x } } } } ) d { \boldsymbol { \mathbf { \mathit { x } } } } = 1$   
scaling: $\begin{array} { r } { \phi ( { \boldsymbol x } ) = \sum _ { \boldsymbol k } p _ { \boldsymbol k } \phi ( 2 { \boldsymbol x } - { \boldsymbol k } ) } \end{array}$ for some finite number of constants ${ \pmb p } _ { \pmb k }$

then the associated $V _ { j }$ satisfy the density condition; that is, $\cup V _ { j } = L ^ { 2 } ( R )$ or, in other words, any element in $L ^ { 2 } ( R )$ can be approximated by elements in $V _ { j }$ for large enough $\pmb { j }$ .

In particular, if the function $\phi$ is continuous with compact support and satisfies the normalization, scaling, and orthonormality conditions listed previously, then the collection of spaces $\{ V _ { j } , j \in Z \}$ forms a multiresolution analysis.

Proof of Part 1 Note that the first part does not require the normalization or the the scaling conditions. The first part of the theorem is true under the following more general hypothesis: that there is a uniform constant $^ { c }$ such that

$$
\operatorname* { m a x } _ { x \in R } | f ( x ) | \leq C \| f \| _ { L ^ { 2 } } \quad { \mathrm { f o r ~ a l l ~ } } f \in V _ { 0 } .
$$

Following Strichartz [21], we clarify why this is a more general hypothesis than requiring $\phi$ to have compact support. If $f \in V _ { 0 }$ , then $\begin{array} { r } { f ( x ) = \sum _ { k } a _ { k } \phi ( x { - } k ) , } \end{array}$ . where the ${ \pmb a } _ { { \pmb k } }$ can be determined by taking the ${ \pmb L } ^ { 2 }$ inner product of $\pmb { f } ( \pmb { x } )$ with $\phi ( { \pmb x } - { \pmb k } )$ [since the $\phi ( { \pmb x } - { \pmb k } )$ are orthonormal]. We obtain

$$
f ( x ) = \left( \sum _ { k } \int f ( y ) { \overline { { \phi ( y - k ) } } } d y \right) \phi ( x - k ) = \int k ( x , y ) f ( y ) d y
$$

where $\begin{array} { r } { k ( x , y ) = \sum _ { k } \phi ( x - k ) \overline { { \phi ( y - k ) } } } \end{array}$ Using the Schwarz inequality for $L ^ { 2 }$ (often called Hölder's inequality), we obtain

$$
| f ( x ) | \leq \left( \int k ( x , y ) ^ { 2 } d y \right) ^ { 1 / 2 } \| f \| _ { L ^ { 2 } } = \left( \sum _ { k } | \phi ( x - k ) | ^ { 2 } \right) ^ { 1 / 2 } \| f \| _ { L ^ { 2 } }
$$

where the last equality again uses the orthonormality of the $\phi ( y - k )$ Since $\phi$ is assumed to vanish outside a finite interval, the sum on the right is over a fixed, finite number of indices and is therefore bounded above by some finite constant $^ { c }$ . Thus estimate (A.7) is satisfied by any compactly supported $\phi$ whose translates are orthonormal.

Now we establish the first part of the theorem assuming the inequality in (A.7). Suppose $\pmb { f }$ belongs to $V _ { - j }$ .Then $f ( 2 ^ { j } x )$ belongs to $V _ { 0 }$ and, using (Å.7), we have

$$
| f ( 2 ^ { j } x ) | \leq C \left( \int | f ( 2 ^ { j } y ) | ^ { 2 } d y \right) ^ { 1 / 2 } = C 2 ^ { - j / 2 } \left( \int | f ( t ) | ^ { 2 } d t \right) ^ { 1 / 2 }
$$

wher thea euality s e ang vbles $t = 2 ^ { j } y$ Since the preceding inequality holds for all $\pmb { x }$ we conclude

$$
\operatorname* { m a x } _ { x \in R } | f ( x ) | \leq C 2 ^ { - j / 2 } \| f \| _ { L ^ { 2 } } .
$$

If $\pmb { f }$ belongs to all $V _ { - j }$ , then this inequality holds for all $\dot { \pmb { \mathscr { I } } }$ Letting $j \to \infty$ , we conclude that $\pmb { f }$ must be zero everywhere.

Proof of Part 2 For the proof of the second part, we consider the orthogonal projection map $P _ { j } : L ^ { 2 } \to V _ { j }$ .Since $\{ \phi _ { j k } ( x ) = 2 ^ { j / 2 } \phi ( 2 ^ { j } x - k ) , k \in Z \}$ is an orthonormal basis for $V _ { j }$ ,

$$
\begin{array} { l l l } { { P _ { j } f ( x ) } } & { { = } } & { { \displaystyle \sum _ { k } \langle f , \phi _ { j k } \rangle \phi _ { j k } ( x ) } } \\ { { } } & { { = } } & { { \displaystyle 2 ^ { j } \sum _ { k } \left( \int f ( y ) { \overline { { { \phi ( 2 ^ { j } y - k ) } } } } d y \right) \phi ( 2 ^ { j } x - k ) } } \\ { { } } & { { . } } \end{array}
$$

for any $f \in L ^ { 2 }$ We must show that for each $f \in L ^ { 2 }$ , $P _ { j } f  f$ in $L ^ { 2 }$ as $j \to \infty$ . Equivalently, we must show that

$$
\| P _ { j } f \| \to \| f \| \quad \cdot
$$

(all norms are $L ^ { 2 }$ norms). This equivalence is seen as follows. Since $\pmb { f } =$ $( f - P _ { j } f ) + P _ { j } f$ and since $P _ { j } f$ is orthogonal to $\pmb { f } - \pmb { P } _ { j } \pmb { f }$ (by the definition of an orthogonal projection), we have

$$
\| f \| ^ { 2 } = \| f - P _ { j } f \| ^ { 2 } + \| P _ { j } f \| ^ { 2 } .
$$

Therefore, $\| P _ { j } f \| ^ { 2 } \to \| f \| ^ { 2 }$ if and only if $\| f - P _ { j } f \| ^ { 2 } \to 0$ .

We establish (A.10) in three steps.

Step 1. $\| P _ { j } f \| \to \| f \|$ for any characteristic function of the form

$$
\chi ( x ) = \left\{ { \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } a \leq x \leq b } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} } \right.
$$

for some numbers $a < b$ .

In view of (A.9),

$$
P _ { j } \chi ( x ) = 2 ^ { j } \sum _ { k } \left( \int _ { a } ^ { b } { \overline { { \phi ( 2 ^ { j } y - k ) } } } d y \right) \phi ( 2 ^ { j } x - k ) .
$$

Therefore,

$$
{ \begin{array} { l } { \| ^ { L } j ^ { \chi } \| } \\ { = 2 ^ { 2 j } \displaystyle \sum _ { k , k ^ { \prime } } \left( \int _ { a } ^ { b } { \overline { { \phi ( 2 ^ { j } y - k ) } } } d y \right) \left( \int _ { a } ^ { b } \phi ( 2 ^ { j } y - k ^ { \prime } ) d y \right) \displaystyle \int \phi ( 2 ^ { j } x - k ) { \overline { { \phi ( 2 ^ { j } x - k ^ { \prime } ) } } } d x } \\ { = 2 ^ { j } \displaystyle \sum _ { k } \left| \int _ { a } ^ { b } \phi ( 2 ^ { j } y - k ) d y \right| ^ { 2 } } \end{array} }
$$

whe hes eualityu he lit $2 ^ { j / 2 } \phi ( 2 ^ { j } x - k )$ in $L ^ { 2 } ( R )$ . Using the change of variables, $\pmb { t } = 2 ^ { j } \pmb { y }$

$$
\| P _ { j } \chi \| ^ { 2 } = 2 ^ { - j } \sum _ { k } \left| \int _ { 2 ^ { j } a } ^ { 2 ^ { j } b } \phi ( t - k ) d t \right| ^ { 2 } .
$$

When $j$ is large, the interval of integration $2 ^ { j } a \leq t \leq 2 ^ { j } b$ is very large and the support of $\phi$ (i.e., essentially the set where $\phi$ is nonzero) is small by comparison. Therefore, except for a few indices $\pmb { k }$ near the boundary of this interval, the indices fall into two categories: (1) The support of $\phi ( t - k )$ does not overlap the interval of integration $2 ^ { j } a \leq t \leq 2 ^ { j } b ,$ in which case the integral on the right is zero; (2) the support of $\phi ( t - k )$ is totally contained inside the interval of integration $2 ^ { j } a \leq t \leq 2 ^ { j } b$ ,in which case the integral on the right is 1 due to the normalization condition $\begin{array} { r } { \int \phi ( y ) d y = 1 } \end{array}$ Therefore,

$$
\begin{array} { l } { { \displaystyle \| P _ { j } \chi \| ^ { 2 } \approx 2 ^ { - j } \left( \mathrm { t h e } \qquad \right. } } \\ { { \displaystyle \approx ( b - a ) } } \\ { { \displaystyle \qquad = \int _ { a } ^ { b } 1 d y } } \\ { { \displaystyle \qquad = \| \chi \| ^ { 2 } . } } \end{array}
$$

The error in these approximations is due to the few indices $\pmb { k }$ when the support of $\phi ( { \pmb x } - { \pmb k } )$ overlaps the boundary of the interval $2 ^ { j } a \leq x \leq 2 ^ { j } b$ As $\dot { \pmb { \jmath } }$ gets large, the number of these indices gets smaller in comparison to the number of integers between ${ \pmb 2 } ^ { j } { \pmb a }$ and $2 ^ { j } b$ Therefore, the approximations get more accurate as $j \to \infty$ and so Step 1 is complete.

Step 2. $\| \pmb { P } _ { j } \pmb { s } \|  \| \pmb { s } \|$ as $j \to \infty$ ,where $\pmb { s }$ is asep cion; that , ae sum of the form

$$
s = \sum _ { k } \alpha _ { k } \chi _ { k } . \qquad . \qquad 
$$

Here, each $x _ { k }$ is a characteristic function of the type discussed in Step 1 (see Figure 1 for a graph of a typical step function).

We have

$$
\| P _ { j } ( s ) - s \| = \| \sum _ { k } \alpha _ { k } ( P _ { j } ( \chi _ { k } ) - \chi _ { k } ) \| \leq \sum _ { k } | \alpha _ { k } | \| P _ { j } ( \chi _ { k } ) - \chi _ { k } \| .
$$

Step 1 established $\| P _ { j } ( \chi _ { k } ) - \chi _ { k } \| \to 0$ as $j \to \infty$ for each $\pmb { k }$ Since there are only a finite number of indices, clearly $\| P _ { j } s - s \| \to 0$ as well.

Step 3. $P _ { j } f \to f$ for a general $f \in L ^ { 2 }$ This follows from Step 2 because an arbitrary function $f \in L ^ { 2 }$ can be approximated by step functions, as illustrated in Figure 1.

![](images/60f4b6010d285a839efffd409191edeeb33a66dfdfd72351d0127dea91eaadc4.jpg)  
Figure 1 Approximating by step functions

We proceed as follows. For a given e, choose a step function $\pmb { s }$ with $\| f - s \| <$ $\epsilon / 3$ Since an orthogonal projection operator does not increase norm, $\| P _ { j } ( f - s ) \|$ is also less than $\epsilon / 3$ From Step 2, $\| P _ { j } s - s \| < \epsilon / 3$ for $\pmb { j }$ large enough. Thus for large $\dot { \jmath }$ ,

$$
\begin{array} { c } { \| f - P _ { j } ( f ) \| = \| ( f - s ) + ( s - P _ { j } s ) + ( P _ { j } s - P _ { j } f ) \| } \\ { \leq \| f - s \| + \| s - P _ { j } s \| + \| P _ { j } ( s - f ) \| } \\ { < \epsilon / 3 + \epsilon / 3 + \epsilon / 3 . } \end{array}
$$

Step 3 and the proof of the second part of the theorem are now complete.

# A.2.1 Proof of Theorem 5.10

In Definition 5.1 (Chapter 5), we defined $V _ { 1 }$ to be the linear space spanned by $\phi ( 2 x - j ) , ~ j \in Z$ ,where $\phi$ is a scaling function satisfying

$$
\phi ( x ) = \sum _ { l } p _ { l } \phi ( 2 x - l )
$$

for some finite number of constants ${ \pmb p } _ { \pmb k }$ . The associated wavelet function is defined as

$$
\psi ( x ) = \sum _ { l } ( - 1 ) ^ { l } \overline { { p _ { 1 - l } } } \phi ( 2 x - l ) .
$$

In the proof of Theorem 5.10 given earlier, we have shown that the translates of $\psi$ are orthogonal to the translates of $\phi$ The goal of this section is to show that $V _ { 1 }$ is spanned by the translates of $\phi$ and the translates of $\psi$ This will imply that any element in $W _ { 0 }$ (the orthogonal complement of $V _ { 0 }$ in $V _ { 1 }$ )is a linear combination of the translates of $\psi$ This is the missing ingredient in our earlier proof of Theorem 5.10.

We must show that for each $j .$

$$
\phi ( 2 x - j ) = \sum _ { k } a _ { k } \phi ( x - k ) + b _ { k } \psi ( x - k )
$$

for some choice of constants ${ \pmb a } _ { \pmb k }$ and $\scriptstyle { b _ { k } }$ .Since $\{ \phi ( { \pmb x } - { \pmb k } ) , ~ { \pmb k } \in { \pmb Z } \}$ is orthonormal, the constants ${ \pmb a } _ { { \pmb k } }$ , if they exist, must be given by

$$
\begin{array} { l } { { a _ { k } = \displaystyle \int \phi ( 2 y - j ) \overline { { { \phi } } } ( y - k ) d y ~ } } \\ { { ~ = \displaystyle \int \sum _ { l } \phi ( 2 y - j ) \overline { { { p _ { l } } } } \overline { { { \phi ( 2 y - 2 k - l ) } } } ~ \mathrm { ~ b y ~ ( A . 1 1 ) } } } \\ { { ~ = ( 1 / 2 ) \overline { { { p _ { j - 2 k } } } } ~ } } \end{array}
$$

where the last equality again uses the fact that $\{ 2 ^ { ( 1 / 2 ) } \phi ( 2 y - j ) ; ~ j \in Z \}$ is orthonormal in ${ \pmb L } ^ { 2 }$ .Similarly, the constants $\scriptstyle b _ { k }$ , if they exist, must be given by

$$
b _ { k } = 2 ^ { - 1 } ( - 1 ) ^ { j } p _ { 1 - j + 2 k } .
$$

So we must show

$$
\phi ( 2 x - j ) = 2 ^ { - 1 } \sum _ { k } \overline { { { p _ { j - 2 k } } } } \phi ( x - k ) + ( - 1 ) ^ { j } p _ { 1 - j + 2 k } \psi ( x - k ) .
$$

Using (A.11) and (A.12), this equation is equivalent to

$$
\phi ( 2 x - j ) = ( 1 / 2 ) \sum _ { k , l } \left( ( - 1 ) ^ { j + l } p _ { 1 - j + 2 k } \overline { { p _ { 1 - l } } } + \overline { { p _ { j - 2 k } } } p _ { l } \right) \phi ( 2 x - 2 k - l ) .
$$

In order for this equation to hold, the coefficient of $\phi ( 2 x - 2 k - l )$ must be zero unless $2 k + l = j$ Therefore, we must show that if $\displaystyle { l = j - 2 k }$ , then

$$
\sum _ { k } p _ { 1 - j + 2 k } \overline { { p _ { 1 - j + 2 k } } } + \overline { { p _ { j - 2 k } } } p _ { j - 2 k } = 2
$$

and if $l = j - 2 k + t$ for $\mathbf { \boldsymbol { t } } \neq \mathbf { \boldsymbol { 0 } }$ , then

$$
\sum _ { k } ( - 1 ) ^ { t } p _ { 1 - j + 2 k } { \overline { { p _ { 1 - j + 2 k - t } } } } + \sum _ { k } { \overline { { p _ { j - 2 k } } } } p _ { j - 2 k + t } = 0
$$

for all $\pmb { t \neq 0 }$ .

By letting $\gamma = 1 - j + 2 k$ and then $\gamma = j - 2 k ,$ ,the left side of (A.13) can be condensed into

$$
\sum _ { \gamma } \overline { { p _ { \gamma } } } p _ { \gamma } ,
$$

which equals 2 by Theorem 5.9, as desired.

For (A.14), we need to handle the cases when $\pmb { t }$ is odd and even separately. If $\pmb { t }$ is odd, say $\pmb { t } = 2 s + 1$ , then the first sum in (A.14) can be transformed by a change of index $( k ^ { \prime } = s + j - k )$ into

$$
\sum _ { k ^ { \prime } } - p _ { j - 2 k ^ { \prime } + t } \overline { { p _ { j - 2 k ^ { \prime } } } } ,
$$

which cancels with the second sum. If $\pmb { t }$ is even, say $\pmb { t = 2 s }$ , then the change of index $\pmb { k } = - \pmb { k } ^ { \prime } + j + s$ brings the second sum to the form

$$
\sum _ { k ^ { \prime } } p _ { - j + 2 k ^ { \prime } } \overline { { p - j + 2 k ^ { \prime } - t } } \cdot 
$$

By letting $\gamma = - j + 2 k ^ { \prime }$ for this sum and then $\gamma = 1 - j + 2 k$ for the first sum in (A.14), the two sums in (A.14) can be combined as

$$
\sum _ { \gamma } p _ { \gamma } \overline { { p _ { \gamma - 2 s } } } ,
$$

which equals zero by Theorem 5.9. The proof of the theorem is now complete.

# A.2.2 Proof of the Convergence Part of Theorem 5.23

In this section, we prove the convergence part of the algorithm described in Theorem 5.23 used to construct the scaling function $\phi$ from the scaling equation

$$
\phi ( x ) = \sum _ { k } p _ { k } \phi ( 2 x - k ) .
$$

Recall that this algorithm starts by setting $\phi _ { 0 }$ equal to the Haar scaling function. Then we set

$$
\phi _ { n } ( x ) = \sum _ { k } p _ { k } \phi _ { n - 1 } ( 2 x - k )
$$

for ${ \pmb n = 1 , 2 , \dots }$ As explained in Section 5.3.3 on Fourier transform criteria, the Fourier transform of this equation is

$$
\widehat { \phi _ { n } } ( \xi ) = P ( e ^ { - i \xi / 2 } ) \widehat { \phi _ { n - 1 } } ( \xi / 2 ) .
$$

Iterating this equation $\pmb { n } - \pmb { 1 }$ times yields

$$
\widehat { \phi _ { n } } ( \xi ) = \prod _ { j = 1 } ^ { n - 1 } P ( e ^ { - i \xi / 2 ^ { j } } ) \widehat { \phi _ { 0 } } ( \xi / 2 ^ { n } ) .
$$

Our goal in this section is to show that the sequence $\phi _ { n }$ defined inductively by this procedure converges to a function $\phi$ in $L ^ { 2 }$ We do this in two steps. We first show that $\widehat { \phi _ { n } }$ converges uniformly on the compact subsets of $\scriptstyle { \pmb R }$ Then we show that $\phi _ { n }$ converges in the $L ^ { 2 }$ norm. As shown in Section 5.3.4, each $\phi _ { n }$ satisfies the orthonormality condition. If $\phi _ { n }$ and all its translates are orthonormal, then the same must be true of its $L ^ { 2 }$ limit.

For the first step, we need the following lemma.

LEMMA A.1 If $\boldsymbol { e } _ { j }$ is a sequence of functions such that $\sum _ { j } | e _ { j } |$ converges uniformly on a set $\kappa$ , then the infinite product $\Pi _ { j } ( 1 + e _ { j } )$ also converges uniformly on the set $\kappa$ .

A sketch of the proof of the lemma is as follows. Write the product as

$$
\prod _ { j } ( 1 + e _ { j } ) = e ^ { \ln \left( \Pi _ { j } ( 1 + e _ { j } ) \right) } = e ^ { \sum _ { j } \ln ( 1 + e _ { j } ) } .
$$

If the series $\sum _ { i } | e _ { j } |$ converges, then $e _ { j }$ must converge to zero. When $| x |$ is small, $| \ln ( 1 + x ) | \approx | x |$ (since by L'Höspital's rule $| \ln ( 1 + x ) | / | x | \to 1$ as $| x |  0 )$ . Therefore, the uniform convergence of $\textstyle \sum _ { j } | e _ { j } |$ on $\pmb { K }$ is equivalent to the uniform convergence of $\textstyle \sum _ { j } | \ln ( 1 + e _ { j } ) |$ which in turn implies the uniform convergence of $\Pi _ { j } ( 1 + e _ { j } )$ by the preceding equalities.

We want to apply the preceding lemma to the case $e _ { j } = p ( \xi / 2 ^ { j } ) - 1$ where $p ( \xi ) = P ( e ^ { - i \xi } )$ and where $\pmb { K }$ is any compact subset of $\scriptstyle { \pmb R }$ Since $\pmb { p }$ is differentiable (it is a polynomial), and since $p ( 0 ) = 1$ ,we have $| p ( t ) - 1 | \leq C | t |$ .Thus $| e _ { j } | \leq C | \xi / 2 ^ { j } |$ and so $\sum _ { j } | e _ { j } |$ converges uniformly on each compact subset of $\pmb { R }$ . By the lemma,

$$
\widehat { \phi _ { n } } ( \xi ) = \prod _ { j = 1 } ^ { n - 1 } p ( \xi / 2 ^ { j } ) \widehat { \phi _ { 0 } } ( \xi / 2 ^ { n } )
$$

also converges as $\textstyle n \to \infty$ uniformly on each compact set in $\scriptstyle { R }$ to a function we call

$$
g ( \xi ) = \prod _ { j = 1 } ^ { \infty } p ( \xi / 2 ^ { j } ) \widehat { \phi _ { 0 } } ( 0 ) .
$$

Now $\| \widehat { \phi _ { 0 } } \| _ { L ^ { 2 } } = 1$ (by construction) and $| \mathscr { p } ( \xi ) | \leq 1$ (by hypothesis). Therefore $\| \widehat { \phi _ { n } } \| _ { L ^ { 2 } } \leq 1$ for all $\pmb { n }$ . By Fatou's lemma, $\int \operatorname* { l i m } _ { n \to \infty } | { \widehat { \phi } } _ { n } | ^ { 2 } \leq \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } \int | { \widehat { \phi } } _ { n } | ^ { 2 } \leq 1$ and so $\pmb { g }$ belongs to $L ^ { 2 }$ By Theorem 2.1, $\pmb { \mathscr { g } }$ equals $\widehat { \phi }$ for some $\phi$ in $L ^ { 2 }$ .

We now show the sequence $\phi _ { n }  \phi$ in $L ^ { 2 }$ , or equivalently, that $\widehat { \phi _ { n } } \to \widehat { \phi }$ in $L ^ { 2 }$ To this end, we use the dominated convergence theorem, which states that if a sequence of functions $f _ { n }$ converges pointwise to a limit function, $\pmb { f } ,$ ,and if there is an integrable function $\pmb { F }$ that dominates the sequence (i.e., $\left| f _ { n } \right| \leq \left| F \right|$ for all $\pmb { n }$ )then $\int f _ { n }  \int f$ In our context, the $\widehat { \phi _ { n } }$ converges pointwise to $\hat { \phi }$ (in fact uniformly on each compact set). So we need only dominate all the $\widehat { \phi _ { n } }$ by a single function belonging to $L ^ { 2 }$ .

Now, by assumption, $P ( e ^ { - i \xi } ) \neq 0$ on the interval $- \pi / 2 \leq \xi \leq \pi / 2$ . Therefore, $P ( e ^ { - i \xi / 2 ^ { j } } ) \neq 0$ on the interval $- 2 ^ { j - 1 } \pi \leq \xi \leq 2 ^ { j - 1 } \pi$ and so

$$
\widehat { \phi } ( \xi ) = \prod _ { j = 1 } ^ { \infty } p ( \xi / 2 ^ { j } ) \widehat { \phi _ { 0 } } ( 0 ) \neq 0
$$

on $- \pi / 2 \leq \xi \leq \pi / 2$ Since this function is continuous, it is bounded away from zero (i.e., $\hat { \phi } \ge { \mathfrak { c } }$ on this compact set). This inequality implies

$$
| \widehat { \phi } ( \xi / 2 ^ { n - 1 } ) ) | = \prod _ { j = n } ^ { \infty } | p ( \xi / 2 ^ { j } ) \widehat { \phi _ { 0 } } ( 0 ) | \geq c \mathrm { ~ f o r ~ } | \xi | \leq 2 ^ { n - 2 } \pi .
$$

Using (A.15), (A.16), and (A.17),

$$
\begin{array} { r l } & { \displaystyle | \widehat { \phi _ { n } } ( \xi ) | = \frac { \prod _ { j = 1 } ^ { \infty } | P ( e ^ { - i \xi / 2 ^ { j } } ) \widehat { \phi _ { 0 } } ( \xi / 2 ^ { n } ) | } { \prod _ { k = n } ^ { \infty } | P ( e ^ { - i \xi / 2 ^ { k } } ) | } } \\ & { \qquad = \frac { | \widehat { \phi } ( \xi ) | } { | \widehat { \phi } ( \xi / 2 ^ { n } ) | } | \widehat { \phi } _ { 0 } ( \xi / 2 ^ { n } ) | } \\ & { \qquad \le \frac { 1 } { c } | \widehat { \phi } ( \xi ) | \widehat { \phi } _ { 0 } ( \xi / 2 ^ { n } ) . } \end{array}
$$

Now

$$
{ \widehat { \phi _ { 0 } } } ( \xi ) = { \frac { e ^ { - i \xi - 1 } } { - { \sqrt { 2 \pi } } i \xi } } ,
$$

as computed in (5.27). Note that $\widehat { \vert \phi _ { 0 } ( \xi ) \vert } \to 0$ as $| \pmb { \xi } |  \infty$ and $\widehat { \phi _ { 0 } } ( \xi )$ is bounded as $\lvert \xi \rvert \to 0$ (by L'Hopital's Rule). Therefore $\vert \widehat { \phi } _ { 0 } ( \xi ) \vert$ is a bounded function, and we have

$$
\vert \widehat { \phi } _ { n } ( \xi ) \vert \leq C \vert \widehat { \phi } ( \xi ) \vert
$$

for some uniform constant $c$ Since $\widehat { \phi }$ has already been shown to be an element of $L ^ { 2 }$ , the expression on the right can be used as our dominating function for use in the dominated convergence theorem for the sequence $\widehat { \phi _ { n } }$ .Thus, $\widehat { \phi _ { n } } \to \widehat { \phi }$ and so $\phi _ { n }  \phi$ in $L ^ { 2 }$ as $\pmb { \mathscr { n } }  \infty$ The proof of the $L ^ { 2 }$ convergence of our algorithm is complete.

# Appendix B

# MATLAB Routines

# B.1 General Compression Routine

The following MATLAB function compresses a given vector-zeroing out the terms falling below a user specified (percentage) threshold. This routine is used by all FFT and wavelet compression schemes that follow.

function wc=compress $( \pmb { \kappa } , \pmb { \tau } )$ .   
$\pmb { \mathscr { I } }$ Input is the array $\pmb { \kappa }$ and $\pmb { x }$ , which is a number   
% strictly between 0 and 1.   
% Output is the array wc where smallest $1 0 0 \pm \%$ of the   
$\%$ terms in $\pmb { \kappa }$ are set to zero (e.g $\mathtt { r } = . 7 5$ means the smallest 75% of % the terms are set to zero   
if $( \mathbf { r } { < } 0 ) \ \mid \ ( \mathbf { r } { > } 1 )$   
error('r should be between O and 1')   
end;   
$\aleph =$ length(w);Nr=floor(N\*r);   
ww=sort(abs(w));   
tol $\mathbf { \bar { \mathbf { \rho } } } =$ abs(ww(Nr+1));   
wc=(abs(w)>=tol).\*w;

# B.2 Use of MATLAB's FFT Routine for Filtering and Compression

Filtering with FFT. The following MATLAB commands are needed for Example 3.6, on filtering the high-frequency components from a given signal.

The key MaTLAB commands are fft and ifft, which compute the fast Fourier transform and its inverse, respectively.

>> t=linspace(0,2\*pi, $2 - 8$ ); % discretizes [0, 2pi] into 256 nodes >>y=exp(-(cos(t).2)). $\ast \left( \sin \left( 2 \ast \mathrm { t } \right) + 2 \ast \cos \left( 4 \ast \mathrm { t } \right) \right.$   
+0.4\*sin(t).\*sin(50\*t));   
>> plot(t,y) % generates the graph of the original signal   
>> fy=fft(y); % computes fft of $\mathbf { y }$ .   
> filterfy $\Bumpeq$ [fy(1:6)zeros( $1 , 2 8 - 1 2 )$ $\mathbf { f } \mathbf { y } ( 2 ^ { - } 8 \substack { - 5 : 2 ^ { - } 8 } ) ]$ ; % sets fft >>% coefficients to zero for $\$ 7$ \leq k \leq $2 5 6 \$ 8$   
>> filtery=ifft(filterfy); % computes inverse fft of the filtered >> % fft   
>> plot(t, filtery) % generates the plot of the compressed signal

Compression with the FFT. The following routine, called fftcomp.m, uses the FFT and the previous compress. m routine to compress a given signal. The compression rate is part of the input. The routine outputs the graph of the signal, the graph of the compressed signal, and the relative $\scriptstyle { \pmb { l } } ^ { 2 }$ error.

function error $\ Q$ fftcomp(t,y,r)   
% Input is an array $\mathbf { y }$ , which represents a digitized signal % associated with the discrete time array t.   
% Also input r which is a decimal   
% number between 0 and 1 representing the compression rate % e.g. 80 percent would be $\pmb { \tau = } 0 . 8$   
$\%$ Outputs are the graph of $\mathbf { y }$ and its compression as well as % the relative error. This routine uses compress.m   
%   
if $( \mathbf { r } { < } 0 ) \ \mid \ ( \mathbf { r } { > } 1 )$   
error( $\mathbf { \mu } _ { \mathbf { \mathcal { X } } }$ should be between O and 1')   
end;   
fy=fft(y);   
fyo $\Bumpeq$ compress(fy,r);   
yo $\Bumpeq$ ifft(fyc);   
plot(t,y,t,yc)   
error=norm(y-yc,2)/norm(y)

Use of fftcomp.m for Example 3.7 on compression with fft

>> t=linspace(0,2\*pi, $2 \sim 8 )$ ;   
>> y=exp(-t.2/10) $\mathbf { \lambda } \cdot \left( \sin \left( 2 * \mathbf { t } \right) + 2 * \cos \left( 4 * \mathbf { t } \right) + 0 . 4 * \sin \left( \mathbf { t } \right) \mathbf { \lambda } \cdot * \sin \left( 1 0 * \mathbf { t } \right) \right)$ >> fftcomp(t,y,0.8) % uses fftcomp with compression rate of % 80 percent

# B.3 Sample Routines Using MATLAB's Wavelet Toolbox

MATLAB commands needed for Compression and Filtering with Wavelets. The following MATLAB routine decomposes a signal into a wavelet decomposition using MATLAB's wavelet package. The routine compresses this decomposition and then reconstructs the compressed signal. This routine uses two key MATLAB commands, wavedec and waverec, for the decomposition and reconstruction. Different wavelets can be used with this routine. We use Daubechies 4-coefficient wavelets (indicated by the parameter db2). Higherorder wavelets can be used (denoted dbn where $\pmb { n }$ is an integer from 1 to $\mathbf { 5 0 - }$ $\mathbf { \lambda } _ { n } = 1$ denotes Haar wavelets). Inputs for this routine are the signal, ${ \pmb y } .$ ,the associated time nodes, $\mathbf { \Delta } _ { \mathbf { t } , \mathbf { \Omega } }$ , the number of levels, $\pmb { n }$ , in the discretization, and the compression rate, $\pmb { \tau }$ ,The routine outputs the graphs of the signal and the compressed signal as well as the relative $\scriptstyle { l ^ { 2 } }$ error.

function error=daubcomp $( \ t , \mathbf { y } , \mathbf { n } , \mathbf { r } )$

% Input is an array $\pmb { \ y }$ , which represents a digitized signal % associated with the vector $\pmb { \mathrm { \hat { \tau } } }$ ; $\mathbf { n } { = }$ the number of levels   
% (so the number of nodes is $2 \tt { \^ n } =$ length of t and the length % of y).   
% Also input r which is a decimal   
% number between 0 and 1 representing the compression rate % e.g. 80 percent would be $\scriptstyle x = 0 . 8$ .   
% Output is the graphs of $\mathbf { y }$ and its compression, as well as % the relative error. This routine uses compress.m   
% and the Daubechies - 4 wavelets.   
%   
if $( \mathbf { r } { < } 0 ) \ 1 ( \mathbf { r } { > } 1 )$   
error $\mathbf { \nabla } ^ { \mathbf { ^ { \circ } } } \mathbf { \mathbf { r } }$ should be between O and 1')   
end;   
[c,1]-wavedec(y,n, 'db2'); % Matlab's wave decomposition routine cc=compress(c,r); % compress the signal   
% (compress.m given above)   
yc=waverec(cc,1,'db2'); % Matlab's wave reconstruction   
% routine   
plot(t,y,t,yc) % plot of the signal and compressed % signal   
error=norm(y-yc,2)/norm(y) % relative $\tt { 1 } \tilde { \tt { 2 } }$ error

# MATLAB commands for Figure 14

>> $\scriptstyle \mathbf { t } = 1$ inspace $( 0 , 1 , 2 ^ { - } 8 )$ ; % discretizes [0,1] into 256 nodes   
>> $\mathbf { y } { = } \sin \left( 2 { * } \mathrm { p i } { * } \mathrm { t } \right) { + } \cos \left( 4 { * } \mathrm { p i } { * } \mathrm { t } \right) { + } \sin \left( 8 { * } \mathrm { p i } { * } \mathrm { t } \right)$ +4\*64\*(t-1/3). $* \mathrm { e x p } ( - ( ( \ t - 1 / 3 ) * 6 4 ) \cdot 2 )$ +512\*(t-2/3).\*exp(-((t-2/3)\*128).2);   
>> daubcomp(t,y,8,0.8)

The same routine with db2 replaced by db1 (for Haar) is used for Example 4.15.

# MATLAB Code for the Algorithms in Section 5.2

The following MaTLAB routine (called dec) will take a given signal, as input and return the plot of the $V _ { j }$ -component of the signal, where $\dot { \pmb { \mathscr { I } } }$ is prescribed by the user. The wavelet decomposition down to level $\pmb { j }$ is also returned. This is not intended to be a professional code (the MATLAB wavelet toolbox provides professional code). Rather, the intent here is to show how MaTLAB can be used to encode the decomposition and reconstruction algorithms given in Section 5.2.

# Decomposition

function w=dec(f,p,NJ, Jstop)

%Inputs: f $=$ data whose length is $\tt { 2 7 9 1 }$ , where NJ=number of scale % ${ \tt p } = { \tt { \tau } }$ scaling coefficients   
% Jstop $=$ stopping scale; program will decompose down % to scale level Jstop.   
%Outputs: w=wavelet coefficients down to level W-Jstop   
% the first $_ { 1 } \cdot 2 ^ { - }$ Jstop entries of $\mathbf { \delta } _ { \mathbf { w } }$ is the $\pmb { \nu } .$ -Jstop   
% projection   
% of f. The rest are the wavelet coefficients.   
$\aleph =$ length(f); $\mathbb { N } \bf { 1 } = \sf { 2 } \hat { \tau } \mathbb { N } \it { J }$ ;   
if $\widetilde { \mathbf { \Gamma } } ( \mathbb { N } { = } { = } \mathbb { N } 1$   
error('Length of f should be 2^NJ')   
end;   
if (Jstop <1)I(Jstop>NJ)   
error('Jstop must be at least 1 and $\angle = \mathrm { \ " { N J } } ^ { \prime }$ )   
end;   
L=length(p);   
pf=fliplr(p);   
q=p; ${ \bf q } ( 2 ; 2 ; \mathrm { L } ) = - { \bf q } ( 2 ; 2 ; \mathrm { L } ) ;$   
$\mathtt { a } \mathtt { = } \mathtt { f }$ ;   
$t = [ ]$ ;   
for j=NJ:-1:Jstop+1   
$\mathtt { n } =$ length(a);   
a=[a(mod((-L+1:-1),n)+1) a]; % make the data periodic   
b=conv(a,q); $b { = } \mathbf { b } ( \mathbf { L } { + } 1 { : } 2 { : } \mathbf { L } { + } \mathbf { n } { - } 1 ) / 2$   
a=conv(a,pf); $\mathsf { a } { = } \mathsf { a } \left( \mathsf { L } : \mathsf { L } + \mathsf { n } { - } 1 \right) / 2 ; \mathrm { ~ \% ~ }$ convolve   
ab=a(1:L); $a \mathbf { = } [ \mathbf { a } ( \mathbf { L } \mathbf { + } \mathbf { 1 } : \mathbf { n } )$ ab]; % periodize   
$\mathtt { a } = \mathtt { a } ( 2 : 2 : \mathtt { n } )$ ; % then down-sample   
t=[b,t]   
end   
$\forall = [ \mathsf { a } , \mathsf { t } ]$ ; $\scriptstyle { \mathbf { J } } = 2 ^ { - }$ (Jstop);   
$\scriptstyle { \mathsf { w a v } } = [ { \boldsymbol { \mathsf { w } } } ( { \boldsymbol { \mathsf { J } } } { \boldsymbol { \mathsf { J } } } )$ w(1:JJ)]; % returns a periodic graph   
tt $\mathbf { = } \mathbf { 1 }$ inspace(0,1,JJ+1);   
if $\scriptstyle 1 = = 2$ % for Haar, the following plot routine returns   
% a block graph $\mathbf { 1 1 = 1 }$ ength(tt); $\tan =$ [tt; tt]; $\mathtt { t t } = \mathtt { t a } ( 1 : 2 * 1 1 )$ ; wa=[ww;ww];ww=wa(1:2\*ll); ww=[ww $2 * 1 1$ ww(1:2\*11-1)];   
end; \*   
plot(tt,ww)

Here is the MATLAB session that generates Figure 11 on the $V _ { 4 }$ -component of a given signal.

>> t=linspace(0,1,2^8); % discretize the unit interval into $^ { 2 \cdot 8 }$   
% nodes   
>> y=sin(2\*pi\*t)+cos(4\*pi\*t)+sin(8\*pi\*t) +4\*64\*(t-1/3).\*exp(-((t-1/3) $\yen 64$ .2) +512\*(t-2/3).\*exp(-((t-2/3)\*128).2); % Sample signal   
>> p=[0.6830 1.1830 0.3170 -0.1830] % Coefficients for   
% Daubechies $- 4$ .   
>> $\mathbf { \nabla } _ { \mathbf { w } } =$ dec(y,p,8,4); % decomposes the signal y from level 8 down   
% to level 4

# Reconstruction

The following code takes the wavelet decomposition of a given signal down to level $j$ (where $j$ is prescribed by the user) and reconstructs the signal to top level.

function y=recon(w,p,NJ, Jstart)   
%Inputs: ${ \textbf { \em u } } =$ wavelet coefficients length is $\tt { 2 7 9 1 }$ , where   
$\%$ NJ=number of scales.   
$\%$ ordered by resolution (from lowest to highest). % $\boldsymbol { \textbf { p } } =$ scaling coefficients   
% Jstart $\mathbf { = }$ starting scale; program will reconstruct % starting with V_Jstart and ending with NJ %   
%Outputs: y=reconstructed signal at V_nJ with a corresponding % plot   
%   
N=length(w);Nj=(2^Jstart);   
if $- ( N = - 2 - N )$   
error('Length of $\pmb { \kappa }$ should be 2^NJ')   
end;   
if (Jstart $\mathbf { \check { \mathbf { \Lambda } } } ^ { \mathbf { \Lambda } }$ I(Jstart>NJ)   
error('Jstop must be at least 1 and $\angle = \mathrm { \Delta \ N J } ^ { \prime }$ ) end;   
L=length(p);   
q=fliplr(p);   
a=w(1:Nj);   
for j=Jstart:(NJ-1)   
$\scriptstyle \mathbf { b } = \mathbf { w } ( \mathbb { N } \mathbf { j } + \mathbf { 1 } : 2 * \mathbb { N } \mathbf { j } )$ ;   
m=mod((O:L/2-1),Nj)+1;   
$\mathtt { N j } = 2 { * } \mathtt { N j }$ ;   
$\mathtt { u a } ( 2 { : } 2 { : } \mathtt { N j } { + } \mathtt { L } ) = [ \mathtt { a } \ \mathtt { a } ( 1 , \mathtt { m } ) ] \ ; \ \mathtt { Y } _ { \mathtt { i } }$ periodize the data and upsample ub(2:2:Nj+L) $=$ [b b(1,m)]; % periodize the data and upsample ca=conv(ua,p); $\mathbf { c a } { = } [ \mathbf { c a ( N j : N j + L - 1 ) }$ ca(L:Nj-1)]; % convolve with p cb=conv(ub,q); cb=cb(L:Nj+L-1); % convolve with q   
$\mathbf { c b } ( \mathbf { 1 } : \mathbf { 2 } : \mathbf { N j } ) { \mathbf { = - c b } } ( \mathbf { 1 } : \mathbf { 2 } : \mathbb { N j } ) \ ; \ \ P _ { - }$ sign change on the odd entries   
$a = c a + c b$ ;   
end;   
$\scriptstyle \mathbf { y } = \mathbf { a }$ ;   
yy=[y(N) y]; % periodize the data   
$\scriptstyle \mathbf { t } = 1$ inspace $( 0 , 1 , \mathbb { N } { + } 1 )$ ;   
if $\scriptstyle { \mathbf { L } } = = 2$ % in the Haar case, return a block-style graph   
$\mathbf { 1 1 } =$ length(t);   
$\tan =$ [t; t]; $\pm = \mathtt { t a } ( 1 : 2 * 1 1 )$ ;   
$\mathbf { y } \mathbf { a } =$ [yy; yy]; yy=ya(1:2\*ll);   
yy $\Bumpeq$ [yy $( 2 * 1 1 )$ yy(1:2\*11-1)];   
end;   
plot(t,yy)

The following MATLAB session compresses the signal $\pmb { f }$ using $8 0 \%$ compression and reproduces Figure 14 in Chapter 5.

>> wc=compress(w,0.8);   
>> t=linspace(0,1,2^8); % discretize the unit interval into 2^8 % nodes   
>> y=sin(2\*pi\*t)+cos(4\*pi\*t)+sin(8\*pi\*t)   
+4\*64\*(t-1/3).\*exp(-((t-1/3)\*64).2)   
+512\*(t-2/3).\*exp(-((t-2/3)\*12g).^2); % Sample signal   
>> p=[0.6830 1.18300.3170 -0.1830] % Coefficients for   
% Daubechies -4.   
>> w=dec(y,p,8,1); %decomposes the signal y from level 8 down % to level 1   
>> wc=compress(w,0.8); %compresses the wavelet coefficients by % 80 percent   
>> %(compress is the routine given at the beginning of this   
% section)   
>> yc=recon(wc,p,8,1); % reconstructs from level 1 to level 8 % from the compressed wavelet coefficients wc

# Bibliography

[1] Benedetto, J. J., Harmonic Analysis and Applications, CRC Press, Boca Raton, FL, 1997.   
[2] Benedetto, J. J. and M. Frazier editors, Wavelets: Mathematics and Applications, CRC Press, Boca Raton, FL, 1993.   
[3} Boyce, W. E. and R. C. DiPrima, Elementary Differential Equations and Boundary Value Problems, 3rd edition, John Wiley & Sons, Inc., New York, 1977.   
[4] Burrus, S., R. Gopinath, and H. Guo, Introduction to Wavelets and Wavelet Transforms, A Primer, Prentice Hall, Upper Saddle River, NJ, 1998.   
[5] Chui, C., An Introduction to Wavelets, Volumes 1 and 2, Academic Press, San Diego, 1992.   
[6] Daubechies, I., Ten Lectures on Wavelets, SIAM, 1992.   
[7] Folland, G. B., Fourier Analysis and Its Applications, Wadsworth & Brooks/Cole, Pacific Grove, CA, 1992.   
[8] Hanselman, D. and B. Littlefield, Mastering MATLAB 5: A Comprehensive Tutorial and Reference, Prentice Hall, Upper Saddle River, NJ, 1998.   
[9] Hernandez, E. and G. Weiss, A First Course on Wavelets, CRC Press, Boca Raton, FL, 1996.   
[10] Mallat, S., "A theory for multi-resolution approximation: the wavelet approximation," IEEE Trans. PAMI 11 (1989), 674-693.   
[11] Mallat, S., A Wavelet Tour of Signal Processing, Academic Press, San Diego, 1998.   
[12] Marchuk, G. , Methods of Numerical Mathematics, Springer-Verlag, Berlin, 1975.   
[13] Meyer, Y., Wavelets & Applications, Society for Industrial and Applied Mathematics, Philadelphia, PA, 1993.   
[14] Papoulis, A., The Fourier Integral and its Applications, McGraw-Hill, New York, 1962.   
[15] Pratap, R., Getting started with MATLAB 5, Oxford University Press, New York, 1999.   
[16] Ralston, A. and P. Rabinowitz, A First Course in Numerical Analysis, McGraw-Hill, New York, 1978.   
[17] Royden, H., Real Analysis, 2nd edition, MacMillan, New York, 1968.   
[18] Rudin, W. Real and Complex Analysis,.   
[19] Stein, E. M. and G. Weiss, Fourier Analysis on Euclidean Spaces, Princeton University Press, Princeton, New Jersey, 1971.   
[20] Strang, G. and T. Nguyen, Wavelets and Filter Banks, Wellesley-Cambridge Press, Wellesley, MA, 1996.   
[21] Strichartz, R. S., "How To Make Wavelets," Amer. Math. Monthly, 100 (1993), 539-556.   
[22] Tolstov, G. P., Fourier Series, Dover, New York, 1962.

# Index

# B Bessel's Inequality, 82

#

via linear predictive coding, 29 32 with general wavelets, 197 with Haar wavelets, 178, 180 Daubechies scaling function, 227230 Daubechies wavelet, 230 decomposition algorithm, 200 summary, 179 via Daubechies wavelets, 277 via Haar, 165, 169 via multiresolution analysis, 197- 200 downsampling, 199

compact support definition, 158   
compression with Daubechies wavelets, 206 with FFT, 139, 274 with general wavelets, 201, 240, 274 with Haar wavelets, 170, 175, 182   
computational complexity (number of operations), 243   
convergence comparison between uniform and $L ^ { 2 }$ ,9 in ${ \pmb L } ^ { 2 }$ ,7 pointwise, 7 uniform, 8   
convergence in the mean, 7   
convergent sequence, 7   
convolution functions, 105 operator, 147 sequences, 136   
F   
Fast Fourier Transform, 136-141   
filtering via Fourier Series, 38, 88 via wavelets, 170, 179, 182, 201, 240   
filters, 108 causal, 115 low-pass, 113 time invariant, 109   
Fourier coefficients, 42   
Fourier inversion formula, 93   
Fourier Series complex form of, 5761 computation of, 4161 over other intervals, 4345

#

data compression via Fourier Series, 38. 88

convergence at a point of continuity, 64 convergence at a point of discontinuity, 70 convergence in the mean, 76 cosine and sine expansions, 45-57 data compression, 38 filtering with, 38 history of, 3738 partial differential equations, 39- 40 uniform convergence of, 7276 Fourier Transform adjoint of, 107 basic properties, 98104 convolution, 106 definition of, 93 discrete, 131136 discrete definition of, 133 properties of, 134136 inverse of, 99 Fredholm alternative, 35 frequency band-limited, 117

G Gibbs phenomenon, 51, 86 Gram-Schmidt orthogonalization, 19

H   
Haar scaling function, 13, 17, 156 definition, 157 properties, 161   
Haar wavelet, 163   
Haar wavelet function, 13, 17   
heat equation, 39   
high-pass filter, 245

# I

impulse response function, 113   
inner product general definition, 2 on $C ^ { n }$ ,2 on $\pmb { R } ^ { n }$ , 1   
inverse Fourier Transform

definition, 99 rigorous proof of, 261264 isometry between $L ^ { 2 }$ and $\scriptstyle { l ^ { 2 } }$ 149

I.2 convergence, 7 definition, 4 inner product, 5   
12 definition, 7 inner product, 7   
Laplace Transform, 100   
leastsquares method of, 2329   
left differentiable, 68   
length, 3   
linear operator adjoint, 21 bounded, 21 definition, 20   
linear predictive coding, 2932   
low-pass filter, 245   
M   
multiresolution analysis definition, 184 properties, 186190

norm, 3 Nyquist frequency definition, 118

# 0

orthogonal complement, 17 projection, 15, 17 subspaces, 12 vectors, 12   
orthonormal basis, 12 projection onto, 16 Fourier Transform criteria, 211 general definition, 12 system, 12   
P   
Parseval's equation Fourier series, 81 Fourier transform, 108 orthonormal basis, 222   
piecewise continuous, 62   
piecewise smooth, 73   
Plancherel formula, 107   
Poisson's formula, 90

Q quadrature mirror filter, 250

#

reconstruction algorithm, 204 summary, 180 via Daubechies, 278 via Haar, 174 via multiresolution analysis, 201 208   
relative error, 7   
relative $L ^ { 2 }$ error, 7 computation of, 274   
Riemann Lebesgue Lemma, 86   
Riemann-Lebesgue Lemma, 61   
right differentiable, 69

# s

sampling theorem, 118, 128   
scaling equation, 214 Fourier Transform criteria, 213   
scaling function dyadic values, 236239 iterative procedure for, 217220   
scaling relation, 187   
Schwarz inequality, 10   
$\mathrm { \bf S i ( z ) }$ , 114   
system function, 113   
T   
transfer function, 149 quadrature mirror interpretation, 251253   
triangle inequality, 11   
two-scale relation, 187

U uncertainty principle, 123 upsampling, 204

#

wavelet construction, 190   
wavelet packets, 244   
wavelet transform definition, 254 inversion formula, 256   
Weierstrass M-Test, 86   
Z   
$\pmb { z }$ -transform definition, 147 properties, 148151