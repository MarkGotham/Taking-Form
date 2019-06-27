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

## Acknowledging and Contributing

Please feel free to use this code and corpus in your own work.
For research and other public-facing projects, please cite or otherwise acknowledge the above paper.

We welcome pull requests, including corrections and additions to the corpus. For any clear error there may be, please suggest a correction; for alternative readings, please submit a separate analysis.
