This repo contains the .tex files from the Stacks project.

The original files are in texRaw.

The folder textFiles contains the files from texRaw, but with the headers, the preamble and the proofs deleted.
Thus it can act as a corpus of theorem statements and definitions written in LaTeX.

The folder mathCleaned contains files from the folder textFiles, but all the inline math and equations have been replaced by the keyword MATH.
Along with it, all the citations and references have been replaced with the keyword REF.
All enumarations have been placed inside <CASES> and </CASES>, with individual \item replaced with the keyword CASE.
It can act as a corpus of mathematical english.

Other than that, Stanford POS tagger has been run on all the statements from mathCleaned and a file Lexicon.txt has been generated.
Several other helper scripts are present as well.
