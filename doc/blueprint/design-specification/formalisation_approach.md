#Formalisation or generalisation in predefined ontology terms

## Linguistic level
 1. All sentences in paragraphs are analysed by linguistic parsers ex: http://nlp.stanford.edu/software/lex-parser.shtml,
http://sourceforge.net/projects/seman/. Result of the parsers are links of 2 terms(words) with and their definitions.
This way sentences subjects and subject's objects are selected.
 1. Links between a sentences subjects, objects (deictic stack) are selected in the way it was demonstrated in
 [MIT Metafor](http://citeseer.ist.psu.edu/viewdoc/download;jsessionid=A6CEE323C057C8DB70662860F87CD61C?doi=10.1.1.94.2569&rep=rep1&type=pdf).
 This way the graphs of the paragraph are created.

## Perceiving level.
  1. Domain ontology is created or imported for example as [RDF of wikipedia](http://labs.systemone.at/wikipedia3)
  1. Sentences subjects(terms) are mapped to concepts
   2. Terms are stemmed
   2. Terms and their annotations as well as context terms and annotations, produced by lexical parsers are used as the
   base for machine learning mapping(formalisation).
   2. Formalisations are stored as probabilistic implications, ex.: `function(subject, noun, ...) -> method`.
   2. Generalisation is applied over a set of formalisation predicates.
   2. Further formalisations are inferred via induction, see ex.: ['Socrates' PLN Logic Examples](http://wiki.opencog.org/w/Walkthrough)