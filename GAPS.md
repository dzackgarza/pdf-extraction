# PDF Extraction Gaps

**Source:** `/home/dzack/Dropbox/Library/` on `dzack@ssh.dzackgarza.com`
**Total PDFs:** 615
**Generated:** Mon Mar 23 06:41:52 PM UTC 2026

## PDF Locations

All PDFs are stored on the remote SSH server:

- **SSH Host:** `dzack@ssh.dzackgarza.com`
- **PDF Directory:** `/home/dzack/Dropbox/Library/`
- **Input Staging:** `~/pdf-inputs/` (copy PDFs here before extraction)
- **Output Directory:** `~/pdf-outputs/<pdf-stem>/auto/<pdf-stem>.md`

## Extraction Workflow (CPU via tmux)

**Remote machine specs:**

- CPU: 4 cores
- RAM: 32 GB
- OS: Arch Linux
- Throughput: ~3-4 pages/min

### Step-by-Step Process

For each PDF in the checklist below:

```bash
# 1. Copy PDF to remote machine
scp /local/path/to/file.pdf dzack@ssh.dzackgarza.com:~/pdf-inputs/

# Or with rsync (resumable, shows progress)
rsync -av --progress /local/path/to/file.pdf dzack@ssh.dzackgarza.com:~/pdf-inputs/

# 2. Send extraction command to tmux session
tmux send-keys -t pdf-extraction 'uv run mineru -p ~/pdf-inputs/file.pdf -o ~/pdf-outputs/ -b pipeline -m auto -l en -d cpu -f true -t false' Enter
```

### Agent Monitoring Loop

```bash
# 3. Monitor progress until complete

# Run this loop:
tmux capture-pane -pt pdf-extraction

# Check if output shows completion:
# - "local output dir is" → job done, proceed to step 4
# - Shell prompt ($ or #) after mineru output → job done, proceed to step 4
# - Otherwise → sleep 300 seconds, repeat from step 1
```

**What to look for in the output:**

- **Progress indicators:** `Layout Predict: X/Y`, `MFD Predict: X/Y`, `OCR-det Predict: X/Y`, `Processing pages: X/Y`
- **Stage transitions:** `DocAnalysis init done`, model downloads, each predict phase
- **Errors:** Any line with `ERROR`, `Failed`, `Traceback`, or non-zero return codes
- **Completion:** `local output dir is /path/to/output` confirms success

**Sleep interval guidance:**

- Short jobs (<50 pages): 60-120s
- Medium jobs (50-200 pages): 300s
- Long jobs (>200 pages): 300-600s

**Runtime estimates:** ~3-4 pages/min on CPU

- 100 pages ≈ 30 min
- 500 pages ≈ 2.5 hr

### Step 4: Copy Markdown Back

```bash
# Copy only the markdown (recommended default)
scp dzack@ssh.dzackgarza.com:~/pdf-outputs/file/auto/file.md /local/path/to/
```

**When to copy additional files:**

- **Images (`images/`)**: Only if you need figures for RAG, documentation, or visual reference
- **Layout PDFs (`*_layout.pdf`)**: Only for debugging extraction quality
- **JSON files**: Only for analysis, debugging, or building custom tooling

### Step 5: Clean Up Remote Files

```bash
# SSH to remote
ssh dzack@ssh.dzackgarza.com

# Trash intermediate files (keeps only the .md file)
cd ~/pdf-outputs/file/auto/
gio trash images/ *_layout.pdf *_span.pdf *_origin.pdf *_middle.json *_model.json *_content_list.json

# Verify only .md remains
ls -la
```

## Checklist

**Mark each PDF as complete after extraction:**

- [ ] `Rings, Modules, and Algebras in Stable Hom - A. D. Elmendorf.pdf`
- [ ] `An Introduction to Lie Groups and Lie Alge - ALEXANDER KIRILLOV, Jr_.pdf`
- [ ] `Lectures on Kahler Geometry - ANDREI MOROIANU.pdf`
- [ ] `Smooth Compactifications of Locally Symmet - AVNER ASH, DAVID MUMFORD, MICHAEL RAPOPORT.pdf`
- [ ] `Complex Analysis - Ahlfors.pdf`
- [ ] `Proofs from the Book - Aigner, Ziegler.pdf`
- [ ] `A First Course in Wavelets With Fourier An - Albert Boggess.pdf`
- [ ] `Classification of Fiber Bundles, Gauge The - Alexander Wijins.pdf`
- [ ] `The Wild World of 4-Manifolds - Alexandru Scorpan.pdf`
- [ ] `Algebraic Topology - Allen Hatcher.pdf`
- [ ] `Vector Bundles and K Theory - Allen Hatcher.pdf`
- [ ] `A Term of Commutative Algebra - Altman, Kleiman.pdf`
- [ ] `Lectures on Symplectic Geometry - Ana Cannas da Silva.pdf`
- [ ] `Functional Analysis ( (Stein and Shakarchi - Analysis Introduction to Further Topics in.pdf`
- [ ] `Homotopical Topology - Anatoly Fomenko.pdf`
- [ ] `Adeles & Algebraic Groups - Andre Weil.pdf`
- [ ] `Algebraic Geometry - Andreas Gathmann.pdf`
- [ ] `Plane Algebraic Curves - Andreas Gathmann.pdf`
- [ ] `A Concise Handbook of Mathematics, Physics - Andrei D. Polyanin.pdf`
- [ ] `Elementary Differential Geometry - Andrew Pressley.pdf`
- [ ] `Homotopy Groups of Spheres and Low-Dimensi - Andrew Putman.pdf`
- [ ] `Modular Elliptic Cuves and Fermat's Last T - Andrew Wiles.pdf`
- [ ] `Lie Groups, Lie Algebras, and Cohomology - Anthony Knapp.pdf`
- [ ] `Puzzles in geometry that I know and love - Anton Petrunin.pdf`
- [ ] `An Excursion through Elementary Mathematic - Antonio Caminha Muniz Neto.pdf`
- [ ] `An Excusrion through Elementary Mathematic - Antonio Caminha Muniz Neto.pdf`
- [ ] `Introduction to Analytic Number Theory - Apostol.pdf`
- [ ] `Complex Algebraic Surfaces, 2nd ed_ - Arnaud Beauville.pdf`
- [ ] `Geometry of Yang-Mills Fields - Atiyah.pdf`
- [ ] `Morse Theory and Floer Homology - Audin.pdf`
- [ ] `Engineering Mathematics - Babu Ram.pdf`
- [ ] `Algebraic Number Theory (Course Notes) - Baker.pdf`
- [ ] `Foundations of Stable Homotopy Theory - Barnes, Roitzheim.pdf`
- [ ] `Mirror Symmetry and Toric Geometry - Batyrev.pdf`
- [ ] `Pervers Faisceaux - Beilinson, Bernstein, Deligne.pdf`
- [ ] `Introduction to Soergel Bimodules - Ben Elias, Shotaro Makisumi, Ulrich Thiel,.pdf`
- [ ] `A Primer on Mapping Class Groups - Benson Farb, Dan Margalit.pdf`
- [ ] `Problems in Analysis - Bernard Gelbaum.pdf`
- [ ] `p-adic Hodge Theory - Bhatt.pdf`
- [ ] `Complex Abelian Varieties - Birkenhake-Lange.pdf`
- [ ] `A Probability Path - Birkhauser Basel.pdf`
- [ ] `Gelfand Mathematical Seminars 1990-1992 - Birkhauser.pdf`
- [ ] `Probability and Mathematical Statistics - Birnbaum.pdf`
- [ ] `Lectures on rational points on curves - Bjorn Poonen.pdf`
- [ ] `Rational points on varieties - Bjorn Poonen.pdf`
- [ ] `Lie Groups - Borcherds.pdf`
- [ ] `Differential Forms in Algebraic Topology - Bott.pdf`
- [ ] `Lie Groups & Lie Algebras. Chapters 7-9 - Bourbaki N_.pdf`
- [ ] `Panorama of Pure Mathematics - Bourbaki.pdf`
- [ ] `Quantum Theory for Mathematicians - Brian C. Hall.pdf`
- [ ] `The Symmetric Group_ Representations - Bruce E. Sagan.pdf`
- [ ] `On Thom Spectra, Orientability, and Cobord - Budyak.pdf`
- [ ] `Automorphic Forms and Representations - Bump.pdf`
- [ ] `A User's Guide to Algebraic Topology - C. T. Dodson.pdf`
- [ ] `Mathematical Analysis 1 - Canuto, Tabacco.pdf`
- [ ] `K3 Surfaces & Their Moduli - Carel Faber, Gavril Farkas, Gerard van der.pdf`
- [ ] `Hyperbolic Geometry - Caroline Series.pdf`
- [ ] `Finite groups of Lie type conjugacy classe - Carter, Roger W_.pdf`
- [ ] `Algebraic number theory; proceedings of an - Cassel Frolich.pdf`
- [ ] `Principles of Real Analysis - Charalambos D. Aliprantis, Owen Burkinshaw.pdf`
- [ ] `An Introduction to Homological Algebra - Charles A. Weibel.pdf`
- [ ] `Elliptic Cohomology - Charles B. Thomas.pdf`
- [ ] `A Book of Abstract Algebra_ Second Edition - Charles C Pinter.pdf`
- [ ] `Real Mathematical Analysis - Charles Chapman Pugh.pdf`
- [ ] `Grinstead and Snell's Introduction to Prob - Charles M. Grinstead.pdf`
- [ ] `Braid Groups - Christian Kassel, Vladimir Turaev.pdf`
- [ ] `Abstract and Concrete Categories - The Joy - Christoph Schubert.pdf`
- [ ] `Pattern Recognition and Machine Learning - Christopher M. Bishop.pdf`
- [ ] `An Introduction to Intersection Homology - Clare.pdf`
- [ ] `The Topology of Fiber Bundles Notes - Cohen.pdf`
- [ ] `The arithmetic of hyperbolic 3-manifolds - Colin Maclachlan, Alan W. Reid.pdf`
- [ ] `Sphere Packings, Lattices, and Groups - Conway, Sloane.pdf`
- [ ] `Mirror Symmetry - Cox Sheldon.pdf`
- [ ] `Topological Methods in Algebra - Craven.pdf`
- [ ] `Representations and Cohomology_ Volume 1, - D. J. Benson.pdf`
- [ ] `Representations and Cohomology_ Volume 2, - D. J. Benson.pdf`
- [ ] `EM and Langlands - DBZ.pdf`
- [ ] `Toric Varieties - Daivd Cox, John Little, Hal Schenck.pdf`
- [ ] `Knots & Links - Dale Rolfsen.pdf`
- [ ] `Lie Groups - Daniel Bump.pdf`
- [ ] `Geometric Intro to K-Theory - Daniel Dugger.pdf`
- [ ] `QFT for Topologists - Daniel Dugger.pdf`
- [ ] `Bordism Old and New - Daniel Freed.pdf`
- [ ] `Complex Geometry_ An Introduction - Daniel Huybrechts.pdf`
- [ ] `Ideals, Varieties, and Algorithms - David A Cox.pdf`
- [ ] `Ideals, Varieties, and Algorithms - David A Cox.pdf`
- [ ] `Computer Vision_ A Modern Approach_ A Mode - David A. Forsyth.pdf`
- [ ] `Cech and Steenrod Homotopy Theories with A - David Edwards, Harold Hastings.pdf`
- [ ] `Commutative Algebra With a View Toward Alg - David Eisenbud.pdf`
- [ ] `Intersection Theory in Algebraic Geometry - David Eisenbud.pdf`
- [ ] `The Geometry of Schemes - David Eisenbud.pdf`
- [ ] `Abelian Varieties - David Mumford.pdf`
- [ ] `The Red Book of Varieties and Schemes - David Mumford.pdf`
- [ ] `Abstract Algebra - David Steven Dummit.pdf`
- [ ] `Geometric Topology_ Localization, Periodic - Dennis Sullivan.pdf`
- [ ] `Singularities of Hypersurfaces - Dimca, Alexandru.pdf`
- [ ] `An Invitation to Arithmetic Geometry - Dino Lorenzini.pdf`
- [ ] `Classical Algebraic Geometry_ A Modern Vie - Dolgachev.pdf`
- [ ] `Riemannian Holonomy Groups and Calibrated - Dominic D. Joyce.pdf`
- [ ] `Complex Cobordism and Stable Homotopy Grou - Douglas C. Ravenel.pdf`
- [ ] `Riemann Surfaces By Way of Analytic Geomet - Dror Varolin.pdf`
- [ ] `Modern Geometry - Methods and Applications - Duborivin, Fomenko, Novikov.pdf`
- [ ] `J-Holomorphic Curves and Symplectic Topolo - Dusa McDuff, Dietmar Salamon.pdf`
- [ ] `Introduction to Symplectic Topology - Dusa McDuff.pdf`
- [ ] `Probability Theory The Logic of Science - E. T. Jaynes.pdf`
- [ ] `Complex Analysis - Eberhard Freitag, Rolf Busam.pdf`
- [ ] `Group Actions on Manifolds - Eckhard Meinrenken.pdf`
- [ ] `Algebraic Topology - Edwin H. Spanier.pdf`
- [ ] `Analytic Function Theory - Einar Hille.pdf`
- [ ] `3264 and All That - Eisenbud.pdf`
- [ ] `Complex Analysis (Stein and Shakarchi II) - Elias M. Stein, Rami Shakarchi.pdf`
- [ ] `Fourier Analysis ( (Stein and Shakarchi I) - Elias M. Stein, Rami Shakarchi.pdf`
- [ ] `Commutative Algebra - Ellengsrud.pdf`
- [ ] `Galois Theory - Emil Artin.pdf`
- [ ] `Categorical Homotopy Theory - Emily Riehl.pdf`
- [ ] `Category Theory in Context - Emily Riehl.pdf`
- [ ] `Category Theory in Context - Emily Riehl.pdf`
- [ ] `Elements of Infty-Category Theory - Emily Riehl.pdf`
- [ ] `Survey of Categorical Concepts - Emily Riehl.pdf`
- [ ] `Introductory Functional Analysi - Erwin Kreyszig.pdf`
- [ ] `Tensor Categories - Etingof.pdf`
- [ ] `Higher-Dimensional Categories - Eugenia Cheng.pdf`
- [ ] `Conceptual Mathematics A First Introductio - F. William Lawvere.pdf`
- [ ] `Fractal Geometry Mathematical - Falconer Kenneth.pdf`
- [ ] `Fundamental AG_ FGA Explained - Fantechi.pdf`
- [ ] `Handbook of Moduli - Farkas, Morrison.pdf`
- [ ] `Analytic Combinatorics - Flajolet, Sedgewick.pdf`
- [ ] `Visual Geometry and Topology - Fomenko.pdf`
- [ ] `Stein Manifolds and Holomorphic Mappings - Franc Forstneric.pdf`
- [ ] `On the Compactification of Moduli Spaces f - Francesco Scattone.pdf`
- [ ] `Handbook of Categorical Algebra_ Volume 3, - Francis Borceux.pdf`
- [ ] `Foundations of Differentiable Manifolds an - Frank W. Warner.pdf`
- [ ] `A First Course in Modular Forms - Fred Diamond.pdf`
- [ ] `Etale Cohomology and Weil Conjectures - Freitag-Kiehl.pdf`
- [ ] `Algebraic Topology I-VI - Friedl.pdf`
- [ ] `Complex Algebraic Geometry - Gallier Shatz.pdf`
- [ ] `A Survey of Modern Algebra - Garrett Birkhoff.pdf`
- [ ] `Fibrations and Sheaves - Garth Warner.pdf`
- [ ] `Illustrated Guide to Perverse Sheaves - Geordie Williamson.pdf`
- [ ] `An Invitation to General Algebra and Unive - George M. Bergman.pdf`
- [ ] `Elements of Homotopy Theory - George W. Whitehead.pdf`
- [ ] `Real Analysis Modern Techniques and Their - Gerald B. Folland.pdf`
- [ ] `Sheaf Theory - Glen E. Bredon.pdf`
- [ ] `Differential Equations and Linear Algebra - Goode, Annin.pdf`
- [ ] `Goode Solution Manual - Goode, Annin.pdf`
- [ ] `Basic Structures of Function Field Arithme - Goss.pdf`
- [ ] `Topology, Geometry and Gauge Fields_ Found - Gregory L. Naber.pdf`
- [ ] `Introduction to Quantum Mechanics - Griffith.pdf`
- [ ] `Introduction to Algebraic Curves - Griffiths.pdf`
- [ ] `Discrete and Combinatorial Mathematics_ An - Grimaldi Ralph P_.pdf`
- [ ] `Calabi-Yau Manifolds and Their Friends - Gross, Huybrechts, Joyce.pdf`
- [ ] `A Journey Through Representation Theory - Gruson.pdf`
- [ ] `Riemann's Zeta Function - H. M. Edwards.pdf`
- [ ] `An Introduction to Contact Topology - HANSJORG GEIGES.pdf`
- [ ] `Real Analysis (4th Edition) - Halsey Royden, Patrick Fitzpatrick.pdf`
- [ ] `Inequalities - Hardy, Littlewood, Polya.pdf`
- [ ] `An Introduction to Quiver Representations - Harm Derksen,Jerzy Weyman.pdf`
- [ ] `Deformation Theory - Hartshorne.pdf`
- [ ] `Calculus Book - Hass, Weir, Thomas.pdf`
- [ ] `Elliptic Cohomology_ Geometry, Application - Haynes R. Miller.pdf`
- [ ] `Algebraic Function Fields and Codes - Henning Stichtenoth.pdf`
- [ ] `Elements of set theory vol 1-Academic Pres - Herbert B. Enderton.pdf`
- [ ] `Generatingfunctionology - Herbert S. Wilf.pdf`
- [ ] `Geometry of Coxeter Groups - Hiller.pdf`
- [ ] `Model Categories - Hovey.pdf`
- [ ] `Elementary Linear Algebra_ Applications Ve - Howard Anton.pdf`
- [ ] `Vector Calculus, Linear Algebra - Hubbard; Barbara Burke Hub John.pdf`
- [ ] `Coxeter Groups - Humphreys.pdf`
- [ ] `Algebra - Hungerford.pdf`
- [ ] `Fiber Bundles - Husemoller.pdf`
- [ ] `Applications of functional analysis and op - Hutson, Pym, Cloud.pdf`
- [ ] `Lectures on K3 surfaces - Huybrechts, Daniel.pdf`
- [ ] `Finite Group Theory - I Martin Isaacs.pdf`
- [ ] `Algebra - A Graduate Course - I. Martin Isaacs.pdf`
- [ ] `Abstract Algebra - I. N. Herstein.pdf`
- [ ] `Galois Theory, Fourth Edition - Ian Nicholas Stewart.pdf`
- [ ] `The Foundations of Mathematics - Ian Stewart.pdf`
- [ ] `Igusa Theta Functions - Igusa.pdf`
- [ ] `Real Analysis Theory of Measure - J Yeh.pdf`
- [ ] `A Course in Combinatorics - J. H. van Lint.pdf`
- [ ] `The Cauchy-Schwarz Master Class_ An Introd - J. Michael Steele.pdf`
- [ ] `More Concise Algebraic Topology Localizati - J. P. May.pdf`
- [ ] `A Concise Course in Algebraic Topology - J. Peter May.pdf`
- [ ] `Algebraic Groups_ The Theory of Group Sche - J. S. Milne.pdf`
- [ ] `Algebraic Number Theory - J. S. Milne.pdf`
- [ ] `Introduction to Lie Algebras and Represent - J.E. Humphreys.pdf`
- [ ] `Abelian Varieties - J.S. Milne.pdf`
- [ ] `Class Field Theory - J.S. Milne.pdf`
- [ ] `String Theory_ Volume 1, an Introduction t - JOSEPH POLCHINSKI.pdf`
- [ ] `Lecture Notes in Algebraic Topology - James Davis, Paul Kirk.pdf`
- [ ] `Linear Algebraic Groups - James E. Humphreys.pdf`
- [ ] `Representations and Characters of Groups - James G., Liebeck M. W_.pdf`
- [ ] `Representations of Semisimple Lie Algebras - James Humphreys.pdf`
- [ ] `Advanced Calculus A Geometric View - James J. Callahan.pdf`
- [ ] `Harmonic Analysis - James Murphy.pdf`
- [ ] `Analysis on Manifolds - James R. Munkres.pdf`
- [ ] `Topology - James R. Munkres.pdf`
- [ ] `A Primer of Commutative Algebra - James S. Milne.pdf`
- [ ] `Complex Variables and Applications - James Ward Brown.pdf`
- [ ] `Categories and Haskell - Jan-Willem Buurlage.pdf`
- [ ] `Birational Geometry of Algebraic Varieties - Janos Kollar, Shigefumi Mori.pdf`
- [ ] `Famlies of Varieties of General type - Janos Kollar.pdf`
- [ ] `Representations of Algebraic Groups - Jantzen.pdf`
- [ ] `Stacks and Moduli - Jaord Alpers.pdf`
- [ ] `Introduction to Stacks and Moduli - Jarod Alper.pdf`
- [ ] `Introduction to PDEs - Jason Murphy.pdf`
- [ ] `Hilbert Modular Forms With Coefficients in - Jayce Getz.pdf`
- [ ] `A Gentle Introduction to Homology, Cohomol - Jean Gallier.pdf`
- [ ] `Coherent Algebraic Sheaves - Jean Pierre Serre.pdf`
- [ ] `Linear Representations of Finite Groups - Jean Pierre Serre.pdf`
- [ ] `Local Fields - Jean Pierre Serre.pdf`
- [ ] `A Course in Arithmetic - Jean-Pierre Serre.pdf`
- [ ] `Groups_ An Introduction - Jean-Pierre Serre.pdf`
- [ ] `Basic Complex Analysis - Jerrold E. Marsden.pdf`
- [ ] `Probability - Jim Pitman.pdf`
- [ ] `An Invitation to Quantum Cohomology - Joachim Kock, Israel Vainsencher.pdf`
- [ ] `Div Grad Curl - Joao.pdf`
- [ ] `Geometry_ A First Course - Joe Harris.pdf`
- [ ] `Moduli of Curves - Joe Harris.pdf`
- [ ] `Abstract Algebra_ Third Edition - John A. Beachy.pdf`
- [ ] `A Course in Functional Analysis - John B. Conway.pdf`
- [ ] `Function of One Complex Variable I - John B. Conway.pdf`
- [ ] `A First Course in Abstract Algebra Solutio - John B. Fraleigh.pdf`
- [ ] `Theta Functions on Riemann Surfaces - John Fay.pdf`
- [ ] `Infinite Loop Spaces - John Frank Adams.pdf`
- [ ] `Stable Homotopy Theory - John Frank Adams.pdf`
- [ ] `Characteristic Classes - John Milnor, James D. Stasheff.pdf`
- [ ] `Intro to Algebraic K-theory - John Milnor.pdf`
- [ ] `Classical Mechanics - John Robert Taylor.pdf`
- [ ] `Lecture Notes on Algebraic Topology II - John Rognes.pdf`
- [ ] `Cookbook of a Level Statistics_ Descriptiv - John Sensele.pdf`
- [ ] `Mathematics and Its History - John Stillwell.pdf`
- [ ] `Naive Lie Theory - John Stillwell.pdf`
- [ ] `The Four Pillars of Geometry - John Stillwell.pdf`
- [ ] `Collected Papers of John Milnor_ Homotopy, - John W. Milnor.pdf`
- [ ] `Lectures on the h-Cobordism Theorem - John W. Milnor.pdf`
- [ ] `Morse Theory - John W. Milnor.pdf`
- [ ] `Morse Theory - John W. Milnor.pdf`
- [ ] `On the h-Cobordism Theorem - John W. Milnor.pdf`
- [ ] `The Seiberg-Witten Equations & Application - John W. Morgan.pdf`
- [ ] `Morse Theory - John Willard Milnor.pdf`
- [ ] `Singular points of complex hypersurfaces - John Willard Milnor.pdf`
- [ ] `Topology From the Differentiable Viewpoint - John Willard Milnor.pdf`
- [ ] `Trees - John-Pierre Serre.pdf`
- [ ] `Contemporary Abstract Algebra - Joseph Gallian.pdf`
- [ ] `An Introduction to Homological Algebra - Joseph J. Rotman.pdf`
- [ ] `Modern Algebra - Joseph J. Rotman.pdf`
- [ ] `Gamma Exploring Euler's Constant - Julian Havil.pdf`
- [ ] `Mathematical Game Theory - Julio Gonzalez-Diaz, Ignacio Garcia-Jurado.pdf`
- [ ] `Compact Riemann Surfaces_ An Introduction - Jurgen Jost.pdf`
- [ ] `Algebraic Number Theory - Jurgen Neukirch.pdf`
- [ ] `Knotes - Justin Roberts.pdf`
- [ ] `From Stein to Weinstein and Back_ Symplect - Kai Cieliebak, Yakov Eliashberg.pdf`
- [ ] `An Invitation to Algebraic Geometry - Karen Smith.pdf`
- [ ] `String Theory and M-Theory_ A Modern Intro - Katrin Becker.pdf`
- [ ] `Moduli of Elliptic Curves - Katz-Mazur.pdf`
- [ ] `Rigid Local Systems - Katz.pdf`
- [ ] `Introduction to the Minimal Model Program - Kawamata, Matsuki.pdf`
- [ ] `Elementary Analysis_ The Theory of Calculu - Kenneth A. Ross.pdf`
- [ ] `A Classical Introduction to Modern Number - Kenneth Ireland.pdf`
- [ ] `Discrete Mathematics and Its Applications - Kenneth Rosen.pdf`
- [ ] `Putnam Mathematical Competition 1985-2000 - Kiran S. Kedlaya, Bjorn Poonen, Ravi Vakil.pdf`
- [ ] `Intro to Lie Groups and Lie Algebras - Kirillov.pdf`
- [ ] `Vector Bundles and K-Theory Lecture Notes - Klaus Wirthmuller.pdf`
- [ ] `Mathematical Writing - Knuth.pdf`
- [ ] `A course in number theory and cryptography - Koblitz, Neal.pdf`
- [ ] `Families of Varieties of General Type - Kollar.pdf`
- [ ] `Introductory Complex Analysis - Kolmogorov.pdf`
- [ ] `Measures, Lebesgue Integrals, and Hilbert - Kolmogorov.pdf`
- [ ] `Differential Manifolds - Kosinski, Antoni A_.pdf`
- [ ] `Singularities of the Minimal Model Program - Kovacs, Sandor, Kollar, Janos.pdf`
- [ ] `Lectures on Quantum Mechanics for Mathemat - L. D. Faddeev.pdf`
- [ ] `Elliptic Curves and Modular Forms - Landweber.pdf`
- [ ] `Elliptic Curves and Modular Forms in Algeb - Landweber.pdf`
- [ ] `Functions for Engineers Special & Applied - Larry C. Andrews.pdf`
- [ ] `Spin Geometry - Lawson H.B., Michelsohn M.L_.pdf`
- [ ] `Introduction to Smooth Manifolds (2012) - Lee.pdf`
- [ ] `Topological Manifolds - Lee.pdf`
- [ ] `Problem Solving Through Problems - Loren C. Larson.pdf`
- [ ] `Differential Geometry - Connections, Curva - Loring W. Tu.pdf`
- [ ] `Lectures and Surveys on G2 Manifolds - Lotay, Leung, Karigiannis.pdf`
- [ ] `HTT - Lurie.pdf`
- [ ] `Basic Topology - M. A. Armstrong.pdf`
- [ ] `Commutative Algebra - M. F. Atiyah, I. G. MacDonald.pdf`
- [ ] `Problems in Algebraic Number Theory - M. Ram Murty.pdf`
- [ ] `Introduction to K-theory for C-star-algebr - M. Rordam, F. Larsen, N. Laustsen.pdf`
- [ ] `From Calculus to Cohomology - de Rham Coho - Madsen.pdf`
- [ ] `A Wavelet Tour of Signal Processing - Mallat Stephane.pdf`
- [ ] `Differential Forms - Manfredo P. Do Carmo.pdf`
- [ ] `Geometry I - Marcel Berger.pdf`
- [ ] `Geometry II - Marcel Berger.pdf`
- [ ] `Calabi-Yau Manifolds and Related Geometrie - Mark Gross.pdf`
- [ ] `(Category Theory) From a Geometrical Point - Marquis.pdf`
- [ ] `Subgroups of free products - Marshall Hall.pdf`
- [ ] `Stable Mappings & Their Singularities - Martin Golubitsky, Victor Guillemin (auth.pdf`
- [ ] `Number Theory - Martin H. Weissman.pdf`
- [ ] `Mathematical Methods in the Physical Scien - Mary L. Boas.pdf`
- [ ] `Equivariant Homotopy and Homology Theory - May.pdf`
- [ ] `Noncommutative Noetherian Rings - McConnell, Robson.pdf`
- [ ] `Introduction to Numerical Analysis - Mehrdad.pdf`
- [ ] `Clifford Algebras and Lie THeory - Meinrenken.pdf`
- [ ] `Algorithmic and Symbolic Combinatorics, An - Melczer.pdf`
- [ ] `Quantum Computation & Quantum Information - Michael A. Nielsen, Isaac L. Chuang.pdf`
- [ ] `Algebra - Michael Artin.pdf`
- [ ] `K-Theory - Michael Atiyah.pdf`
- [ ] `Introduction to the Theory of Computation - Michael Sipser.pdf`
- [ ] `A Comprehensive Introduction to Differenti - Michael Spivak.pdf`
- [ ] `Calculus on Manifolds A Modern Approach to - Michael Spivak.pdf`
- [ ] `Complex Analysis - Michael Taylor.pdf`
- [ ] `A Walk Through Combinatorics An Introducti - Miklos Bona.pdf`
- [ ] `Undergraduate Algebraic Geometry - Miles Reid.pdf`
- [ ] `Undergraduate Commutative Algebra - Miles Reid.pdf`
- [ ] `Class Field Theory - Milne.pdf`
- [ ] `Symmetric Bilinear Forms - Milnor, Husemoller.pdf`
- [ ] `Smart Words_ Vocabulary for the Erudite - Mim Harrison.pdf`
- [ ] `An Introduction to Kolmogorov Complexity a - Ming Li.pdf`
- [ ] `Algebraic curves and Riemann surfaces - Miranda.pdf`
- [ ] `0-387-21577-8_20.pdf`
- [ ] `0306256.pdf`
- [ ] `1005.2346.pdf`
- [ ] `1103.4674.pdf`
- [ ] `110830_btheses_hulst_fwn_math.pdf`
- [ ] `1112.5706.pdf`
- [ ] `1209.4708.pdf`
- [ ] `1310.4721.pdf`
- [ ] `1405.3035.pdf`
- [ ] `1410.6938.pdf`
- [ ] `1412.6194.pdf`
- [ ] `1506.06200.pdf`
- [ ] `1511.04265.pdf`
- [ ] `1703.03545.pdf`
- [ ] `1703.09855.pdf`
- [ ] `1810.08953.pdf`
- [ ] `1903.09742.pdf`
- [ ] `2021_Topology_I.pdf`
- [ ] `2022-09-20.pdf`
- [ ] `2022EischenNotes.pdf`
- [ ] `2022GanNotes (1).pdf`
- [ ] `2022GanNotes.pdf`
- [ ] `2022YunNotes (1).pdf`
- [ ] `2022YunNotes.pdf`
- [ ] `2022YunOutline.pdf`
- [ ] `2102.13459.pdf`
- [ ] `2109.08788.pdf`
- [ ] `2109.14594.pdf`
- [ ] `2111.04694.pdf`
- [ ] `2112.10456.pdf`
- [ ] `2201.09445.pdf`
- [ ] `2202.02473.pdf`
- [ ] `2203.01690.pdf`
- [ ] `2207.02276.pdf`
- [ ] `2208.10383 (1).pdf`
- [ ] `60688861.pdf`
- [ ] `9702155.pdf`
- [ ] `AN06.pdf`
- [ ] `ANTBook.pdf`
- [ ] `Apr 26 15h45yyyyy.pdf`
- [ ] `CV_DZackGarza.pdf`
- [ ] `CZ_syllabus_2022.pdf`
- [ ] `ComplexAnalysis_Qual_Spring2021.pdf`
- [ ] `Condensed.pdf`
- [ ] `Cursillo2.pdf`
- [ ] `DZG CRAG Weil Conjectures.pdf`
- [ ] `Disc3.pdf`
- [ ] `Final_Mtg_Slides.pdf`
- [ ] `GSS Talk.pdf`
- [ ] `Grawe, Nathan D - Demographics and the demand for higher education-Johns Hopkins University Press (2018) (1).pdf`
- [ ] `HomotopyGroupsOfSpheres.pdf`
- [ ] `Kujawa.pdf`
- [ ] `LPP01-254-940.pdf`
- [ ] `LectureVII-Stacks.pdf`
- [ ] `MonRC.pdf`
- [ ] `NABDofficial.pdf`
- [ ] `Notes Talk 2.pdf`
- [ ] `Proposed Events Schedule (2).pdf`
- [ ] `S0273-0979-2021-01748-4.pdf`
- [ ] `Schedule QFT 2022 School.pdf`
- [ ] `Schedule_Deformations.pdf`
- [ ] `Scissors.pdf`
- [ ] `Spectra Are Your Friends.pdf`
- [ ] `String Theory - Townsend.pdf`
- [ ] `Talk1-1.pdf`
- [ ] `Talk1.pdf`
- [ ] `Tickets-21618903.pdf`
- [ ] `Topology_Qual_Spring2022.pdf`
- [ ] `UGA Hoodie or Crew 2022.pdf`
- [ ] `Winter 2022 Reading Group Talk Final.pdf`
- [ ] `ZFD-CBG-20220718-TRC4Y4JP6BN (1).pdf`
- [ ] `anab-hotype.pdf`
- [ ] `ant-v1-n1-p01-p.pdf`
- [ ] `bezout.pdf`
- [ ] `day1class.pdf`
- [ ] `dissertation.pdf`
- [ ] `einffinal.pdf`
- [ ] `etale (1).pdf`
- [ ] `faberpandharipande.pdf`
- [ ] `getting_to_brasenose_hires.pdf`
- [ ] `homotopy-sheaves.pdf`
- [ ] `i2.pdf`
- [ ] `icm.pdf`
- [ ] `mfikki.pdf`
- [ ] `mixedLSGNT.pdf`
- [ ] `oguz.pdf`
- [ ] `onlineTicket.pdf`
- [ ] `recentdevelopments.pdf`
- [ ] `rnoti-p241.pdf`
- [ ] `rnoti-p663.pdf`
- [ ] `rnoti-p950.pdf`
- [ ] `scholze-berkeley.pdf`
- [ ] `thesis-augmented.pdf`
- [ ] `thhmusigma.pdf`
- [ ] `toric.pdf`
- [ ] `tx080500586p.pdf`
- [ ] `adic notes - Morel, Sophie.pdf`
- [ ] `Representation Theory - Morel.pdf`
- [ ] `Ordinary Differential Equations_ An Elemen - Morris Tenenbaum.pdf`
- [ ] `Differential Topology - Morris W. Hirsch.pdf`
- [ ] `Cohomology Operations and Applications in - Mosher R.E., Tangora M.C_.pdf`
- [ ] `A Course in Hodge Theory - Movasati.pdf`
- [ ] `Basic Algebra II 2nd edition - Nathan Jacobson.pdf`
- [ ] `Smooth Manifolds and Observables - Nestruev, Jet.pdf`
- [ ] `Algebraic Number Theory - Neukirch.pdf`
- [ ] `Lipschitz Singularities - Neumann.pdf`
- [ ] `The prince - Niccolo Machiavelli.pdf`
- [ ] `Lectures on the Topology of 3-Manifolds an - Nikolai Saviliev.pdf`
- [ ] `Graph Theory - Norman Biggs.pdf`
- [ ] `Theoretical Computer Science for the Worki - Noson S. Yanofsky.pdf`
- [ ] `Topological Library Part 3_ Spectral Seque - Novikov, Taimanov.pdf`
- [ ] `Lectures on Riemann Surfaces - Otto Forster, Bruce Gilligan.pdf`
- [ ] `Projective Differential Geometry - Ovsienko.pdf`
- [ ] `MANIFOLDS, TENSORS, AND FORMS - PAUL RENTELN.pdf`
- [ ] `Monopoles and Three-Manifolds - PETER KRONHEIMER.pdf`
- [ ] `Algebra Chapter 0 - Paolo Aluffi.pdf`
- [ ] `Advanced Calculus - Patrick Fitzpatrick.pdf`
- [ ] `Field & Galois Theory - Patrick Morandi.pdf`
- [ ] `Simplicial Homotopy Theory - Paul G. Goerss, John F. Jardine.pdf`
- [ ] `A Conversational Introduction to Algebraic - Paul Pollack.pdf`
- [ ] `Naive Set Theory - Paul R. Halmos.pdf`
- [ ] `Introduction to Homotopy Theory - Paul Selick.pdf`
- [ ] `The Road to Reality - Penrose Roger.pdf`
- [ ] `Algebraic Number Theory - Pete Clark.pdf`
- [ ] `Commutative Algebra - Pete Clark.pdf`
- [ ] `An Introduction to Mathematical Reasoning_ - Peter J. Eccles.pdf`
- [ ] `Algebraic Geometry I - Peter Scholze.pdf`
- [ ] `Rational Homotopy Theory and Differential - Philip Griffiths, John Morgan.pdf`
- [ ] `Principles of Algebraic Geometry - Philip Griffiths, Joseph Harris.pdf`
- [ ] `Eisenstein series and automorphic represen - Philipp Fleig, Henrik P. A. Gustafsson, Ax.pdf`
- [ ] `Analytic Combinatorics - Philippe Flajolet.pdf`
- [ ] `String Theory (Solutions) - Polchanski.pdf`
- [ ] `A Conversationsal Introduction to ALgebrai - Pollack.pdf`
- [ ] `Not Always Buried Deep - Pollack.pdf`
- [ ] `Cracking the GRE Math Subject Test - Princeton Review.pdf`
- [ ] `Homotopical Algebra - Quillen.pdf`
- [ ] `Enumerative Combinatorics, Volume 1_ Secon - RICHARD P. STANLEY.pdf`
- [ ] `Elementary Number Theory - Raji.pdf`
- [ ] `Bundles, Homotopy, and Manifolds - Ralph Cohern.pdf`
- [ ] `Foundations of Algebraic Geometry - Ravi Vakil-pdfjam.pdf`
- [ ] `Foundations of Algebraic Geometry - Ravi Vakil.pdf`
- [ ] `The Rising Sea Foundations of Algebraic Ge - Ravi Vakil.pdf`
- [ ] `Physics for Scientists and Engineers with - Raymond A. Serway.pdf`
- [ ] `Putnam and Beyond - Razvan Gelca.pdf`
- [ ] `Weil Conjectures, Perverse Sheaves, & l'ad - Reinhardt Kiehl.pdf`
- [ ] `Measures, Integrals, and Martingales - Rene Schilling.pdf`
- [ ] `Catalan's Conjecture - Rene Schoof.pdf`
- [ ] `Projective Geometry_ An Introduction - Rey Casse.pdf`
- [ ] `Introduction to Calculus and Analysis Vol. - Richard Courant, Fritz John.pdf`
- [ ] `Essentials of Stochastic Processes - Richard Durrett.pdf`
- [ ] `Multiple View Geometry in Computer Vision - Richard Hartley, Andrew Zisserman.pdf`
- [ ] `Numerical Analysis - Richard L. Burden.pdf`
- [ ] `Algebraic Combinatorics Walks, Trees, Tabl - Richard Stanley.pdf`
- [ ] `Gauge Theory & the Topology of Four-Manifo - Robert Friedman, John Morgan.pdf`
- [ ] `Holomorphic Surfaces Algebraic & Vector Bu - Robert Friedman.pdf`
- [ ] `4-Manifolds and Kirby Calculus - Robert Gompf, Andas Stipsicz.pdf`
- [ ] `Algebraic Topology - Homotopy and Homology - Robert M. Switzer.pdf`
- [ ] `Algebraic Geometry - Robin Hartshorne.pdf`
- [ ] `Encyclopedia of Mathematics and its Applic - Robin Ticciati.pdf`
- [ ] `Complex Analysis - Rodriguez, Kra, Gilman.pdf`
- [ ] `Concrete Mathematics - Ronald L. Graham.pdf`
- [ ] `General Topology - Ryszard Engelking.pdf`
- [ ] `Homological Algebra - S. I. Gelfand.pdf`
- [ ] `Topological Library_ Part 2_ Characteristi - S. P. Novikov, I. A. Taimanov.pdf`
- [ ] `Topological Library_ Part 1 - S. P. Novikov.pdf`
- [ ] `Riemann Surfaces - S.K. Donaldson.pdf`
- [ ] `3D Computer Graphics - Sam Buss.pdf`
- [ ] `Complex Function Theory - Sarason.pdf`
- [ ] `Some applications of modular forms - Sarnak, Peter.pdf`
- [ ] `Algebraic Topology_ An Intuitive Approach - Sato.pdf`
- [ ] `Categories for the Working Mathematician-S - Saunders Mac Lane.pdf`
- [ ] `Homology - Saunders Mac Lane.pdf`
- [ ] `Work of Scholze - Scholze.pdf`
- [ ] `Introduction to 3 Manifolds - Schultens.pdf`
- [ ] `Divisors and Sandpiles - Scott Corry, David Perkinson.pdf`
- [ ] `A Mathematical Introduction to Conformal F - Scottenloher.pdf`
- [ ] `Algebra - Serge Lang.pdf`
- [ ] `Complex Analysis - Serge Lang.pdf`
- [ ] `Introduction to Linear Algebra - Serge Lang.pdf`
- [ ] `Methods of Homological Algebra - Sergei I. Gelfand.pdf`
- [ ] `Deformations of Algebraic Schemes - Sernesi.pdf`
- [ ] `Deformations of Algebraic Schemes - Sernesi.pdf`
- [ ] `Abelian l-Adic Representations and Ellipti - Serre.pdf`
- [ ] `Lie Groups and Lie Algebras - Serre.pdf`
- [ ] `Linear Algebra Done Right - Sheldon Axler.pdf`
- [ ] `Measure, Integration & Real Analysis - Sheldon Axler.pdf`
- [ ] `Algebraic Mirror symmetry and Geometry - Sheldon Katz David A. Cox.pdf`
- [ ] `Enumerative Geometry and String Theory - Sheldon Katz.pdf`
- [ ] `A First Course in Probability - Sheldon Ross.pdf`
- [ ] `An Introduction to Invariants and Moduli ( - Shigeru Mukai.pdf`
- [ ] `Arithmetic & Geometry of K3 Surfaces & Cal - Shigeyuki Kondo (auth.), Radu Laza, Matthi.pdf`
- [ ] `K3 Surfaces - Shigeyuki Kondo.pdf`
- [ ] `Geometry of Differential Forms - Shigeyuki Morita.pdf`
- [ ] `Map of my Life - Shimura.pdf`
- [ ] `DG Modules and HZ Spectra - Shipley.pdf`
- [ ] `p-Adic Lie Groups - Shneider.pdf`
- [ ] `Kac-Moody, their Flag Varieties and Repres - Shrawan Kumar.pdf`
- [ ] `Differential Geometry, Lie Groups, and Sym - Sigurdur Helgason.pdf`
- [ ] `Berkeley Problems in Mathematics - Silva Souza.pdf`
- [ ] `Calculus Made Easy - Silvanus P. Thompson.pdf`
- [ ] `The Arithmetic of Dynamical Systems - Silverman.pdf`
- [ ] `The Arithmetic of Elliptic Curves - Silverman.pdf`
- [ ] `Linear Algebra - Simon Plouffe - Hoffman.pdf`
- [ ] `Representation Theory - Sophie Morel.pdf`
- [ ] `Elementary Mechanics From a Mathematician' - Spivak.pdf`
- [ ] `Linear Algebraic Groups - Springer.pdf`
- [ ] `Cohomology Operations - Steenrod.pdf`
- [ ] `Real Analysis (Stein and Shakarchi III) - Stein.pdf`
- [ ] `Mathematical Foundations of Quantum Mechan - Stephan Fackler.pdf`
- [ ] `Understanding Analysis - Stephen Abbott.pdf`
- [ ] `Differential Equations and Linear Algebra - Stephen W. Goode.pdf`
- [ ] `Category Theory - Steve Awodey.pdf`
- [ ] `Point Set Topology - Steven A. Gaal.pdf`
- [ ] `Linear Algebra With Applications - Steven J. Leon.pdf`
- [ ] `A Mathematician's Survival Guide - Steven Krantz.pdf`
- [ ] `Advanced Linear Algebra - Steven Roman.pdf`
- [ ] `Lectures on Quantum Mechanics - Steven Weinberg.pdf`
- [ ] `Lectures in Modules and Rings - T. Y. Lam.pdf`
- [ ] `Exercises in Classical Ring Theory - T.Y. Lam.pdf`
- [ ] `Convex Bodies & Algebraic Geometry_ An int - Tadao Oda.pdf`
- [ ] `Galois Groups and Fundamental Groups - Tamas Szamuely.pdf`
- [ ] `Complex Analysis - Taylor.pdf`
- [ ] `Problems in Real Analysis_ Advanced Calcul - Teodora-Liliana Radulescu.pdf`
- [ ] `An Introduction to Measure Theory - Terrence Tao.pdf`
- [ ] `Representations of Compact Lie Groups - Theodor Brocker, Tammo Tom Diec.pdf`
- [ ] `Complex Analysis - Theodore W. Gamelin.pdf`
- [ ] `All the Mathematics You Missed_ But Need t - Thomas A. Garrity.pdf`
- [ ] `Introduction to Algorithms - Thomas H. Cormen.pdf`
- [ ] `The Princeton Companion to Math - Timothy Gowers.pdf`
- [ ] `Calculus, Vol. 1_ One-Variable Calculus Wi - Tom M. Apostol.pdf`
- [ ] `Calculus_ Multi-Variable Calculus and Line - Tom M. Apostol.pdf`
- [ ] `Hodge-Tate Theory - Tony Feng.pdf`
- [ ] `Contact Topology Notes - Torres.pdf`
- [ ] `Manifolds, Sheaves & Cohomo - Torsten Wedhorn.pdf`
- [ ] `The Elements of Statistical Learning Data - Trevor Hastie.pdf`
- [ ] `Visual Complex Analysis - Tristan Needham.pdf`
- [ ] `classics revisited_ EGA - Ulrich Gortz.pdf`
- [ ] `Homotopy Type Theory_ Univalent Foundation - Univalent Foundations Program.pdf`
- [ ] `Algebra, Topology, Calculus for CS and ML - Unknown.pdf`
- [ ] `Algebraic Geometry over the Complex Number - Unknown.pdf`
- [ ] `An Introduction to Stable Homotopy Theory - Unknown.pdf`
- [ ] `Arithmetic and Geometry of CY Surfaces - Unknown.pdf`
- [ ] `Cohomology Operations and Applications in - Unknown.pdf`
- [ ] `DAG-I - Unknown.pdf`
- [ ] `Fiber Bundles Basics - Unknown.pdf`
- [ ] `Fields Medallists Lectures - Unknown.pdf`
- [ ] `Frobenius Manifolds, Quantum Cohomology, a - Unknown.pdf`
- [ ] `Fukaya Categories and Picard Lefschetz the - Unknown.pdf`
- [ ] `Galois Theory Lecture Notes - Unknown.pdf`
- [ ] `Homological Algebra - Unknown.pdf`
- [ ] `Introduction to Quantum Cohomology Kontsev - Unknown.pdf`
- [ ] `Model Theory - Unknown.pdf`
- [ ] `Motivic Cohomology - Unknown.pdf`
- [ ] `Neron Model - Unknown.pdf`
- [ ] `Notes on Representation Stability - Unknown.pdf`
- [ ] `Principal Bundles and Classifying Spaces - Unknown.pdf`
- [ ] `Putnam and Beyond - Unknown.pdf`
- [ ] `Sheaves and Cohomology - Unknown.pdf`
- [ ] `Simple Singularities and Simple Algebraic - Unknown.pdf`
- [ ] `The Geometry and Topology of Coxeter Group - Unknown.pdf`
- [ ] `The Matrix Cookbook - Unknown.pdf`
- [ ] `Theory of Rings - Unknown.pdf`
- [ ] `Lie Algebras Lie Groups & Representations - V. S. Varadarajan.pdf`
- [ ] `Supersymmetry for Mathematicians_ An Intro - V. S. Varadarajan.pdf`
- [ ] `Mathematical Methods Of Classical Mechanic - V.I. Arnold.pdf`
- [ ] `Vakil Foundations of Algebraic Geometry - Vakil.pdf`
- [ ] `Del Pezzo and K3 Surfaces - Valery Alexeev.pdf`
- [ ] `Moduli of Weighted Hyperplane Arrangements - Valery Alexeev.pdf`
- [ ] `Picard Lefschetz Theory - Vassilliev.pdf`
- [ ] `Differential Topology - Victor Guillemin, Alan Pollack.pdf`
- [ ] `Differential Topology - Victor Guillemin.pdf`
- [ ] `Hodge Theory and Complex Algebraic Geometr - Voisin, C_.pdf`
- [ ] `HODGE THEORY AND COMPLEX ALGEBRAIC GEOMETR - Voisin, Claire.pdf`
- [ ] `HODGE THEORY AND COMPLEX ALGEBRAIC GEOMETR - Voisin, Claire.pdf`
- [ ] `Partial Differential Equations An Introduc - Walter A. Strauss.pdf`
- [ ] `Functional Analysis - Walter Rudin.pdf`
- [ ] `Principles of Mathematical Analysis - Walter Rudin.pdf`
- [ ] `Real and Complex Analysis - Walter Rudin.pdf`
- [ ] `Solutions Manual to Walter Rudin's _Princi - Walter Rudin.pdf`
- [ ] `Cohomology and Poincare Duality - Weiyi Zhang.pdf`
- [ ] `Functions of Several Variables - Wendell Fleming.pdf`
- [ ] `Connections, Curvature, and Cohomology. Vo - Werner Hildbert Greub.pdf`
- [ ] `Representation Theory_ A First Course - William Fulton, Joe Harris.pdf`
- [ ] `Algebraic Curves An Introduction to Algebr - William Fulton.pdf`
- [ ] `Introduction to toric varieties - William Fulton.pdf`
- [ ] `First Concepts of Topology - William G. Chinn.pdf`
- [ ] `Fundamentals of Number Theory - William Judson LeVeque.pdf`
- [ ] `The Geometry and Topology of 3-Manifolds - William P. Thurston.pdf`
- [ ] `Algebraic Number Theory_ A Computational A - William Stein.pdf`
- [ ] `Multivariable mathematics - Williamson, Richard Edmund;Trotter, Hale F.pdf`
- [ ] `Hochschild Cohomology - Witherspoon.pdf`
- [ ] `Compact Complex Surfaces - Wolf P. Barth, Klaus Hulek, Chris A. M. Pe.pdf`
- [ ] `Course Notes on Intersection Theory - Yichao Tian.pdf`
- [ ] `An Introduction to Harmonic Analysis - Yitzhak Katznelson.pdf`
- [ ] `Riemannian Geometry - do Carmo.pdf`
- [ ] `PROBLEMS AND SOLUTIONS IN MATHEMATICS - lsr.pdf`
- [ ] `Handbook of Homotopy Theory - of Homotopy Theory-Chapman Handbook.pdf`
- [ ] `Milne Etale Cohomology - on Etale Cohomology (1998) Lectures.pdf`
