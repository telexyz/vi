# 2 (Crowd) Sourcing a Language Resource Catalogue

The first part of our corpus, accounting for 62% of the final dataset size (in bytes), was made up of a
collection of monolingual and multilingual language resources that were selected and documented
collaboratively through various efforts of the BigScience Data Sourcing working group.

This yielded a set of __252 sources__, including at least 21 per considered language category. We focused on metadata collection as a way to support selection of the sources for the final dataset
and documentation of the final dataset.

Pseudo-Crawled Data. để check xem page đó đã được cào chưa đã, cào rồi thì thôi.

## 2.2 Processing Pipeline for Quality Improvement on Crowdsourced Datasets
Once a text field was obtained, we attempted to improve the quality of that text. In the specific case of
text extraction from HTML, we observe that __not all text are relevant__ (menus, advertisements, repeated
text on each page etc ...). In order to remove noisy data from our dataset, we applied a processing
pipeline for each dataset consisting of a sequence of functions.

Functions were categorised as document-scoped or dataset-scoped functions. 
- Document-scoped functions are operations that modify a document independently of other documents and datasetscoped functions are operations that take into account the whole dataset. Orthogonal to this scope,
functions were also separated into cleaning and filtering functions. Cleaning functions aim to
remove text considered not part of the main document. Document-scoped cleaning functions can
for example target leftover HTML tags.

- On the other end, dataset-scoped cleaning functions need
the whole dataset to calculate a heuristic to determine how to modify each document. For instance,
advertisements vary across datasets, making it harder to define a dataset-agnostic classifier for
advertisement.

__Instead, we can index all the lines in a dataset and identify repeated lines on multiple
pages as likely advertisements__.

An example is displayed in Appendix B.2. Filtering functions aim
at removing an entire document from the corpus. The reasons for choosing to remove a document
completely are diverse: it may be because the document is considered to be of too poor quality, to be
too complex to automatically fix or too similar to other examples already present in the corpus. In
the latter case, we speak of deduplication.

