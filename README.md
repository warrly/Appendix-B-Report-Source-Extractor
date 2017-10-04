<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Appendex B Report Source Extractor](#appendex-b-report-source-extractor)
      - [Current Status:](#current-status)
  - [Footnotes to Extracted Sources](#footnotes-to-extracted-sources)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Appendex B Report Source Extractor
Here you'll find code to automagically extract sources from reports.

#### Current Status:
- [ ] code to convert `.docx` files to a text file of footnotes
- [x] code to convert footnotes to extracted sources
- [ ] code to combine the two


## Footnotes to Extracted Sources
Run via the following to have the sources printed out to the terminal.
```bash
python3 source_extracter.py <input-file.txt>
```
Run via the following to have the sources saved to `<output-file.tsv>`
```bash
python3 source_extracter.py <input-file.txt> > <output-file.tsv>
```
