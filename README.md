# The Quiet Theorems

*Theorems from probability, statistics and machine learning that deserve to be better known: one a week, stated with minimal conditions, proved in full, and checked in code.*

Each post takes one result (a classical identity, an inequality, a characterisation, or a theorem behind a modern machine-learning method) and works through it properly:

- the setting and notation, and the precise statement under the weakest conditions that make it true;
- a complete proof, with every exchange of limits, integrals and derivatives justified;
- what the result means, and the consequences that follow from it, each with its own proof;
- a fully explicit worked example with a figure;
- a numerical check whose code you can run;
- where the result came from, with references to the original scientific literature only.

## Where to read

- **Substack**, free, with new posts by email: <https://omidsolari.substack.com>
- **Website**, with every post and its PDFs and notebooks: <https://osolari.github.io/the-quiet-theorems/>

Every post comes as an article, a PDF with the full derivations (A4 for print, a narrow layout for phones and tablets) and a Jupyter notebook with the numerical check.

## Posts

**No. 00. Hoeffding's covariance identity** (9 Nov 2026). The covariance of two random variables is the integral of the gap between their joint distribution function and the product of their marginals.
[Substack](https://omidsolari.substack.com/p/probability-notes-no-00-hoeffdings) · [web](https://osolari.github.io/the-quiet-theorems/posts/00-hoeffding/) · PDF ([A4](docs/posts/00-hoeffding/pdf/qt-00-hoeffding.pdf), [screen](docs/posts/00-hoeffding/pdf/qt-00-hoeffding-screen.pdf)) · [notebook](docs/posts/00-hoeffding/notebook.ipynb) ([open in Colab](https://colab.research.google.com/github/osolari/the-quiet-theorems/blob/main/docs/posts/00-hoeffding/notebook.ipynb))
*First published under the series' earlier name, Probability Notes; a revised edition with every proof written out step by step is awaiting approval.*

## Run the checks yourself

Every number in a post's numerical check is printed by a short Python script. To reproduce it:

```sh
git clone https://github.com/osolari/the-quiet-theorems.git
cd the-quiet-theorems
python3 -m pip install -r requirements.txt
python3 docs/posts/00-hoeffding/code/check.py
```

Or open the post's notebook, locally or in Colab, and run it top to bottom. The scripts need only NumPy and SciPy; `requirements.txt` pins the exact versions the published numbers were produced with.

The LaTeX source of each post is in its folder, `docs/posts/NN-slug/main.tex`.

## Corrections and suggestions

Found an error, a missing condition or a better reference? Want a theorem covered? [Open an issue](https://github.com/osolari/the-quiet-theorems/issues).

## Citing a post

```bibtex
@misc{solari2026hoeffding,
  author       = {Omid Shams Solari},
  title        = {Hoeffding's covariance identity},
  howpublished = {The Quiet Theorems No. 00 (first published as Probability Notes No. 00)},
  year         = {2026},
  month        = nov,
  url          = {https://omidsolari.substack.com/p/probability-notes-no-00-hoeffdings}
}
```

Please also cite the original work the post is about; each post lists it.

## About

Written by Omid Shams Solari, Ph.D. (sAIm Labs). The posts are written to be collected into a book of the same name.

How the series is built (templates, scripts, toolchain, publishing): [`docs/DEVELOPING.md`](docs/DEVELOPING.md).
