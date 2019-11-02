# Taking Form

## About

This repo provides the code and corpus for processing machine- and human-readable human analyses of musical form as reported in:

Gotham, Mark and Matthew T. Ireland: 'Taking Form: A Representation Standard, Conversion Code, and Example Corpus for Recording, Visualizing, and Studying Analyses of Musical Form', in the Proceedings of the 20th International Society for Music Information Retrieval Conference, Delft, The Netherlands, 2019.

## Instructions for use

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
- [Mozart piano sonatas](/corpus/Mozart_Sonatas/): complete (17 sonatas, 51 movements) [Coming soon]
- ['NBN-Examples'](/corpus/NBN-Examples/): proof of concept examples of the nested bracket notation as discussed in the paper

## Tabular Format Documentation

Users may input rows for every measure or just the ones with annotations as they prefer:
- Rows with with no formal annotation are ignored;
- Comparative deductions are made directly from the measure number of the relevant rows;
- Row 0 may be a header, or just proceed directly to the first measure in the piece (put another way, if it is text, it will be taken as a header and ignored).

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
