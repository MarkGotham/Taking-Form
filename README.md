# Taking Form

## About

This repo provides the code and corpus for processing machine- and human-readable human analyses of musical form as reported in:

[Gotham, Mark and Matthew T. Ireland: 'Taking Form: A Representation Standard, Conversion Code, and Example Corpus for Recording, Visualizing, and Studying Analyses of Musical Form', in the Proceedings of the 20th International Society for Music Information Retrieval Conference, Delft, The Netherlands, 2019.](http://archives.ismir.net/ismir2019/paper/000084.pdf)

## Code

To process one conversion from music xml to tabular formats:
```
cd Taking-Form
python markup/xml2table.py op2no1movt1.mxl op2no1movt1.csv
```

Alternatively, use the scripts (scripts/table2brackets, scripts/xml2brackets and scripts/xml2table).

To batch process every .mxl file in a 'corpus' folder (paths are relative to the root directory of the repository):
```
for mxlFile in ../path/to/corpus/*.mxl; do scripts/xml2table "$mxlFile" "${mxlFile%.mxl}.csv"; done
```

## Corpus

The corpus folder contains:
- [Beethoven piano sonatas](/corpus/Beethoven_Sonatas/): complete (32 sonatas, 103 movements)
- [Mozart piano sonatas](/corpus/Mozart_Sonatas/): 17 sonatas. Currently first movements only; complete 51 movements coming soon]. For encoded scores and clarity wrt the complex catalogue numbers, we recommend [Craig Sapp's Digital edition](https://github.com/craigsapp/mozart-piano-sonatas) and the [Verovio humdrum viewer](http://verovio.humdrum.org/).
- ['NBN-Examples'](/corpus/NBN-Examples/): proof of concept examples of the nested bracket notation as discussed in the paper

## On-score markup

- First, click on any note at the right measure and beat position for the marking you want to enter.
- Enter a new textual marking at that position (most software provide CMD+T (Mac) / CNTRL+T (Windows) as a shortcut for this).
- Begin each on-score mark-up with an initial character to specify a 'level number' for the marking in question, followed by a colon. For instance, 'Exposition', 'Development' and 'Recapitulation' will all be on the top level of division (number 1) in sonata form movements, so '1: Exposition'. All other levels continue the divisions from here, (e.g. '2: First Subject Group').
- Where you wish to indicate a division, but have no name for the span in question, use the correct level number and a placeholder text like '4: X'.
- In practice, many entries like '1: Exposition' and '2: First Subject Group' will begin at the same time. To indicate these multiple, simultaneous level entries, insert one text entry with all the component parts divided by a comma (','). For instance, many sonatas will begin with the long string: '1: Exposition, 2: First Subject Group, 3: Theme a, 4: Sentence, 5: Presentation, 6: Basic Idea'.

All entries are relative to each other, so level numbers are given by finding the directly relevant parallel. These will fall into a few basic types of comparison:

- A span and its first phrase-division will generally be used together, with the division at +1 level. For a phrase, we might have '4: Period, 5: Antecedent'.
- The next division of that phrase ('Consequent') is at the same level of the first division ('Antecedent'), thus '5: Consequent'.
- The next phrase outside of this span returns to the initial level, so '4: Period'.
- When we eventually get to larger structural boundary then we have to find an entry at a comparable level, which will involve proportionately wider view. For the 'Recapitulation' we're starting again from the top level (so '1: Recapitulation'), while for the second subject group it's level 2 ('2: Second Subject Group').

Note that while the numbers assigned to the top levels will be consistent within and even across pieces ('Exposition', 'Development' and 'Recapitulation' will almost always appear as a set at level 1), those at lower levels will vary depending on the number of level divisions above them.
For instance, the same phrase grouping structure may appear at multiple levels across a piece: at lower levels in a long and richly-structured exposition, but at nominally 'higher' levels in a short Coda with fewer divisions.

## Tabular Format

Users may input rows for every measure or just the ones with annotations as they prefer:
- Rows with with no formal annotation are ignored;
- Comparative deductions are made directly from the measure number of the relevant rows;
- The first row may be a header, or just proceed directly to the first measure in the piece (put another way, if it is text, it will be taken as a header and ignored).

With or without the headers, the columns correspond to:
- Measure (column 0);
- Beat (column 1, expressed as beats in the prevailing time signature. Negative beat numbers to indicate anacruses are permitted in manual entry, but the automated score extraction always assumes positive position);
- Form (columns 2-, from the largest to smallest units across any number of columns from left to right)

Shorthands for repeats:
- The 'Repeat:' marking may be used to indicate repeats marked in the score (e.g. ```Repeat: 1-8```)
- Likewise, we support the shorthand ```9-16=1-8```) for a passage which is fully written out in the score, but formally identical to one given above (e.g. in the case of variations or equivalent passages in Recapitulation-Exposition);
- In both cases, users can provide exceptions to the initial line by entering formal labels into that line. For instance, ```11-206=1-196,,Recapitulation``` will replace the top-level formal annotation with 'Recapitulation' and otherwise repeat the entries of that line and all subsequent lines exactly.

Constraints:
- Measures must be in order (monotonically increasing);
- 'In order' can accommodate written out repeated passages indicated by letters such that letter trumps number: '9a' > '16', for instance;
- We support up 26 repeats of the same passage (a-z, which really ought to be enough!);
- If using the shorthand to omit some rows, and the shorthand for repeats, the row before a repeat must be the previous measure (even if there is no annotation);
- Likewise, the last row must correspond to the final measure of the piece (either alone, or as the latter value of a repeat/comparator entry).

## Acknowledging and Contributing

Please feel free to use this code and corpus in your own work.
For research and other public-facing projects, please cite or otherwise acknowledge the above paper.

We welcome pull requests, including corrections and additions to the corpus. For any clear error there may be, please suggest a correction; for alternative readings, please submit a separate analysis.
