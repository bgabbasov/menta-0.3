# Menta 0.3 vision.
Problem/prototype centric view.

![Problems mind map](https://github.com/menta/menta-0.3/raw/master/doc/informal/mind-maps/problem%20highlevel.png)

## Overall

 1. *Fuzzy* system
  2. We face new kind of system with no crisp ages of the components.
  2. Inbound information could contain contradictions and different layers of abstraction.
 1. Perceiving mechanisms are close to thinking mechanisms and still not so formalized as should be.

### Mitigation

 1. At least knowledge of the components algorithms should be reused in several ways.


## Perceiving algorithms

 1. Lexical processing - depends on parser and trained data could be erroneous.
 1. Annotation depends on Knowledge base (KB), should have at least minimal trained knowledge of TSS + IT common sense.
 1. Interpretation by [LSA](http://en.wikipedia.org/wiki/Latent_semantic_analysis) is not ideal and could be replaced by other proper algorithm.
 1. Validation criteria still not clear and could be too detailed.

## Textual processing

 1. Word processing - NLP tool kits still need more analysis for: the applicability to SE domain.
 1. Synonym an Homonym problem still need industrial approach = possibly we could use some Knowledge Base see [solutions](https://github.com/menta/menta-0.3/blob/master/doc/informal/solution-ideas.md)

## Emotion machine Solution problems

 1. Problem and Solution description form - Solution should be formal in teh domain context, possibly in HowTo could be reused.
 1. The way TSS could monitor the System solutions.
 1. The textual pre-processing including auto-correct based on domain dictionary.
 1. Rules and mechanisms of Critics, see [§7-5. What are some useful Critics?](http://web.media.mit.edu/~minsky/E7/eb7.html)
 1. Rules and mechanisms of Selector(WayToThink) see [§7-4. What are some useful Ways to Think?](http://web.media.mit.edu/~minsky/E7/eb7.html)
 1. Inbound Critics data structure.
 1. Inbound WayToThink data structure.
 1. Outbound WayToThink data structure.
 1. Exit criteria of Critics->WayToThink loop.
 1. Clarification/Confirmation response processing.
 1. Context support.