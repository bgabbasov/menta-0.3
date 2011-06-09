# Main idea description.

Use the logical inference of the main idea of the document not statistical:
Currently all frameworks that came around our analysis were based on LSA - the statistical analysis of the terms in a document.
This approach is not really good, as people do not use it :-).
What people do:
 * Extract main subject of the sentence
 * Taking in account the sentences references extract main idea of the paragraph.

## Proposed approach:
### Main idea extraction:
 * Extract subject(key term) of sentences extracted by linguistic parser(for example: stanford parser)
 * Create deixis (references of subjects(key terms) between sentences)
 * Create graph of the key terms
 * Generalise(via probabilistic logic) key terms to most generic concepts based on encyclopedic ontology (wikipedia, openCyc, conceptNet)
 * Store semantic trees of most generic concepts, weighted by key terms references as the logical description of the document.
 * Add LSA based key phrases as frequency based description to the document.

### Search:
 * Request is generalised is similar approach as document.
 * Documents are searched according to generalised logical description via LSA,
 * Sorted from most specific to most generic concepts frequencies.