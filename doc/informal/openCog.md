#OpenCog
Analysis of [OpenCog project](http://opencog.org/projects/)

## OpenCog projects [see](http://opencog.org/projects/)

 1. [AtomSpace](http://wiki.opencog.org/w/AtomSpace) – an in-memory hypergraph store. Atoms, which can either be nodes or links, can be of a number of types and have a truth value associated with them.
 1. [PLN](http://wiki.opencog.org/w/PLN) – Probabilistic Logic Networks. An logic system for uncertain inference.
 1. [MOSES](http://wiki.opencog.org/w/MOSES) – Meta-Optimizing Semantic Evolutionary Search. Program evolution based on representation-building and probabilistic modeling.
 1. [Embodiment](http://wiki.opencog.org/w/Embodiment) – Modules to allow OpenCog to reason about being embodied within an avatar, be it a Nao robot or a game character inside a virtual world.
 1. [RelEx](http://wiki.opencog.org/w/RelEx) and [Linkgrammar](http://www.abisource.com/projects/link-grammar/) – Extract grammatical parses and semantic knowledge from natural language (in English).
 1. [NLGen](https://launchpad.net/nlgen) and [NLGen2](https://launchpad.net/nlgen2) – Do the inverse of RelEx. Convert semantic relationships to natural language.

## Solution overall

### Definitions
[See Emotion Machine Solution Definitions section.](https://github.com/menta/menta-0.3/blob/master/doc/informal/emotion-machine.md)

### Analysis scope
Could the Solution produce the formalisation starting from Text to AnnotatedText according to [formalisation criteria](https://github.com/menta/menta-0.3/blob/master/doc/informal/formalisation-criteria.md)?

## AtomSpace

### Analysis scope
Could the storage be reused in our project, are the AtomSpace is capable of storage Scala objects of our project: HowTo-s, Way2Think ...?

## [PLN](http://wiki.opencog.org/w/PLN)
Probabilistic logic network.

 1. Entry criteria = User provided new predicates and the request.
 1. Exit criteria = the Frequency Confidence pair found or the energy for the operation is exceeded.
 1. Inbound data = the AnnotatedText [see Component diagram section](https://github.com/menta/menta-0.3/blob/master/doc/informal/annotation-interpretation-validation.md)
 1. Outbound data = the Frequency Confidence pair of the predicates.

### Analysis scope
Could the project be used in:

 1. Deliberate Critics.
 1. ReasoningByAnalogy Way2Think.
 1. Planing Way2Think.
 1. Simplification Way2Think.
 1. Elevation Way2Think.
 1. Reformulation Way2Think.
 1. Contradiction Way2Think.
 1. Simulation Way2Think.
 1. Correlation Way2Think.
 1. Logical Reasoning Way2Think
 1. Wishful thinking.

## [MOSES](http://wiki.opencog.org/w/MOSES)
Meta-Optimizing Semantic Evolutionary Search.

 1. Entry criteria = User provided new request.
 1. Exit criteria = the formalisation found or the energy for the operation is exceeded.
 1. Inbound data = a AnnotatedText [see Component diagram section](https://github.com/menta/menta-0.3/blob/master/doc/informal/annotation-interpretation-validation.md)
 1. Outbound data = a formalised AnnotatedText.

### Analysis scope
Could the project be used in:

 1. Learned Critics.
 1. Deliberate Critics.
 1. Reflective Critics.
 1. Self-Reflective Critics.
 1. KnowingHow Way2Think.
 1. ExtensiveSearch Way2Think.
 1. ReasoningByAnalogy Way2Think.
 1. Divide and Conquer Way2Think.
 1. Reformulation Way2Think.
 1. Use external representations Way2Think.
 1. Simulation Way2Think.
 1. Correlation Way2Think.
 1. Wishful thinking.

## [Embodiment](http://wiki.opencog.org/w/Embodiment)
Modules to allow OpenCog to reason about being embodied within an avatar the program in the computer environment world(Intellix).

### Definitions
[See Emotion Machine Solution Definitions section.](https://github.com/menta/menta-0.3/blob/master/doc/informal/emotion-machine.md)

### Analysis scope
Could the OpenCog agent produce the formalisation starting from Text to AnnotatedText according to [formalisation criteria](https://github.com/menta/menta-0.3/blob/master/doc/informal/formalisation-criteria.md)?
Could the OpenCog agent learn, operate, experiment in the computer environment world(Intellix).

## [RelEx](http://wiki.opencog.org/w/RelEx) and [Linkgrammar](http://www.abisource.com/projects/link-grammar/)
RelEx Dependency Relationship Extractor

 1. Entry criteria = User provided new request.
 1. Exit criteria = Created structure of the text.
 1. Inbound data = a Text [see Component diagram section](https://github.com/menta/menta-0.3/blob/master/doc/informal/annotation-interpretation-validation.md)
 1. Outbound data = a AnnotatedText with word links.

### Analysis scope
Could the RelEx produce the proper links structure of the text, suitable for further formalisation?

## [NLGen](https://launchpad.net/nlgen) and [NLGen2](https://launchpad.net/nlgen2)

 1. Entry criteria = System generated request to User.
 1. Exit criteria = Created natural language request.
 1. Inbound data = a AnnotatedText [see Component diagram section](https://github.com/menta/menta-0.3/blob/master/doc/informal/annotation-interpretation-validation.md)
 1. Outbound data = a Text request.

### Analysis scope
Could the NLGen and/or NLGen2 produce the proper text of the request?


