#[Emotion machine](http://en.wikipedia.org/wiki/Emotion_machine)
Solution is based on Marvin Minsky [Emotion machine/7. Thinking chapter.](http://web.media.mit.edu/~minsky/E7/eb7.html)

## Use cases

### Training

![Train](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/UseCaseTrain.png)

Train mainly is supervised automatic with the Request and Solution pairs provided by TSS. After some essential learning
TSS monitors the Solution-s of the system.

### Production
![Production](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/UseCaseProduction.png)
System supports the dialog with a customer starting with Request then through the clarifications/confirmations to Solution
applied to the target environment.

## Components

![Critics with Selectors](http://web.media.mit.edu/~minsky/E7/eb7_files/image003.png)

Mainly the Thinking is split on two sections Critics and Selectors(Way to Think):

Critics are applied sequentially and selects proper Selector(Way to Think).

## Component diagram

![Component](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/Component.png)

 1. Simplest case is the direct instruction processing.
The Learned Reactive Critics is activated and retrieve the Knowing How way of thinking.
 1. Complex case is the problem description processing.
Ex.: Learned Reactive Critics activates ReasoningByAnalogy, DivideAndConquer WayToThink, then WayToThink activates Deliberate Critics,
that activates Reformulation WayToThink, Reformulation changes the representation of inbound data to proper way and activates Learned Critics then KnowHow WayToThink.

`Learned -> [ReasoningByAnalogy|DivideAndConquer] -> Deliberate -> Reformulation -> Learned -> KnowHow`

## Formalisation Production Workflow.

 1. Preliminary annotation:
  2. Lexical parser one of (see list below) creates the lexical structure of the sentences, that are added as annotations to inbound text.

    - [StanfordParser](http://nlp.stanford.edu/software/lex-parser.shtml)
    - [OpenCog](http://opencog.org/projects/)
    - [OpenNLP](http://incubator.apache.org/opennlp/index.html)
  2. Knowledge Base ([see KB list on Wikipedia page and the list below](http://en.wikipedia.org/wiki/Commonsense_knowledge_bases)) concepts are added to annotated text on the step above.
    - [ConceptNet5](http://conceptnet5.media.mit.edu/)
    - [NELL](http://rtw.ml.cmu.edu/rtw/resources)
    - [WolframAlpha](http://www.wolframalpha.com/)
    - [TrueKnowledge](http://www.trueknowledge.com/)
    - [ConceptNet](http://csc.media.mit.edu/conceptnet)
    - [Freebase](http://www.freebase.com/apps)
    - [YAGO2](http://www.mpi-inf.mpg.de/yago-naga/yago/)
    - [DBPedia](http://dbpedia.org/About)
 1. Self Conscious Critics start the Perceiving WayToThink that controls following Critics-WayToThink pairs
  2. Activates Critics from lower to upper level one by one to find proper WayToThink (if no WayToThink found activates Critics on the level above).
  2. Runs found WayToThink that produces some additional annotations(ex.: some inference results could be added).
  2. Validate the WayToThink annotations, if annotations conforms the formalisation criteria stops the process, if not activates proper Critics again.
  2. Controls the number of cycles performed by the system, if exceeded maximum available for the perceiving operation stops.
