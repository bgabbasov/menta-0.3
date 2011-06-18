#Formalisation approach in incident domain.

Formalisation consists of two parts:

 1. Structuration of unstructured information
 1. Formalisation translation in formal language description.

## Structuration
Structuration is projection of the unstructured text in to the graph of the domain concepts.

### Linguistic level
 1. All sentences in paragraphs are analysed by linguistic parsers ex: http://nlp.stanford.edu/software/lex-parser.shtml,
http://sourceforge.net/projects/seman/. Result of the parsers are links of 2 terms(words) with and their definitions.
This way sentences subjects and subject's objects are selected.


### Perceiving level.
  1. Domain ontology is created or imported for example as [RDF of wikipedia](http://labs.systemone.at/wikipedia3)
  1. Sentences subjects(terms) are mapped to concepts
   1. Links between a sentences subjects, objects (deictic stack) are selected in the way it was demonstrated in
   [MIT Metafor](http://citeseer.ist.psu.edu/viewdoc/download;jsessionid=A6CEE323C057C8DB70662860F87CD61C?doi=10.1.1.94.2569&rep=rep1&type=pdf).
   This way graphs of a paragraph are created.
   2. Terms and their annotations as well as context terms and annotations, produced by lexical parsers are used as the
   base for machine learning mapping(structuration).
    3. Scopes are selected in the sentences.
    3. Objects and possible actions are selected in the similar way it was done in
    [MIT Metafor](http://citeseer.ist.psu.edu/viewdoc/download;jsessionid=A6CEE323C057C8DB70662860F87CD61C?doi=10.1.1.94.2569&rep=rep1&type=pdf).
    3. Conditional constructs, negations and sets constructs are identified.
    3. Known concepts are identified in text too.
     4. Each concept could have multiple probable mappings into term space.
    3. Each term and it's link is mapped to concept space according to the dictionary and scope.
     4. Starting from first subject down to each leaf.
     4. Each link is interpreted as the part of the pattern V(action) -> S(subject) -> O(object) -> O(object).
     4. In case perceiving module fails interpretation, it rises clarification request.
   2. Structuration rules are stored as probabilistic implications, ex.: `[term, context, frequency, confidence] -> concept`.
   2. Generalisation is applied over a set of structuration implications.
   2. Further structuration are inferred via induction, see ex.: ['Socrates' PLN Logic Examples](http://wiki.opencog.org/w/Walkthrough)

## Formalisation
Structured information(fragments of domain graph) is projected into formal terms space.
Formal terms space in our system is represented as HowTo-s(recipe), for example the recipe from workbooks.
 1. Incident descriptions(fragments of domain graph) are classified into groups: requests or problem descriptions (according to main subjects) or compounds.
  2. Requests are interpreted in to direct HowTo-s (possibly scripts) that runs what requested, for example installs the Firefox.
  2. Problem descriptions:
   3. Main problem places are identified
   3. HowTo-s to solve the problem of this kind(type of device, operating system, application, server ...) is identified.
    4. If system fails to identify the HowTo it rises the clarification request.
   3. HowTo is run by means of script engine for example [Sikuli](http://sikuli.org/)

