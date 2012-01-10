# Menta 0.3 vision.
Problem/prototype centric view.

![Problems mind map](https://github.com/menta/menta-0.3/raw/master/doc/informal/mind-maps/problem%20highlevel.png)

## Overall

 1. *Fuzzy* system
  2. We face new kind of system with no crisp ages of the components.
  2. Inbound information could contain contradictions and different layers of abstraction.
 1. Perceiving mechanisms are close to thinking mechanisms and still not so [formalised as should be](https://github.com/menta/menta-0.3/blob/master/doc/informal/formalisation-criteria.md).

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

 1. Problem and Solution description structure - Solution should be formal in the domain context, possibly HowTo approach could be reused.
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

## Annotation interpretation validation Solution problems

Emotion machine +

 1. [Knowledge Base annotator is dependant on current KB available.](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#KnowledgeBaseAnnotator)
 1. Domain KB creation could be expensive.
 1. [Validation mechanisms still obscure.](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#Test_data)

## OpenCog Solution problems

 Emotion machine, Annotation interpretation validation +

  1. OpenCog is created on C++, could be hard to integrate with Scala application, see [JCog](https://launchpad.net/jcog), see [PLN](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#PLN) and [MOSES](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#MOSES) prototypes
    2. Some parts of OpenCog is in Java: RelEx, NLGen2.
  1. [OpenCog is the framework, we have to understand how do we integrate and implement parts of Menta-0.3 perceiving system.](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#OpenCog)
  1. AtomSpace could be not usable for our [knowledge representation](http://web.media.mit.edu/~minsky/E8/eb8.html#_Toc518305130), see [prototype](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#AtomSpace)
  1. [PLN could be hard to integrate in Scala project.](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#PLN)
  1. [MOSES could be not usable for our knowledge](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#MOSES).
  1. Embodiment could be not capable of expressing [Intellix](https://github.com/menta/menta-0.3/blob/master/doc/informal/intellix.md), see [prototype](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#Embodiment).
  1. [RelEx could be not so good to be used in the project.](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#Natural_language_processors)
  1. [NLGen2 could be not good enough to generate the clarification requests.](https://github.com/menta/menta-0.3/blob/master/doc/informal/intellix.md#NLGen)