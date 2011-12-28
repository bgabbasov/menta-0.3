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

 1. _Simplest case is the direct instruction processing._
The Learned Reactive Critics is activated and retrieve the Knowing How way of thinking.
 1. _Complex case is the problem description processing._
Ex.: Learned Reactive Critics activates ReasoningByAnalogy, DivideAndConquer WayToThink, then WayToThink activates Deliberate Critics,
that activates Reformulation WayToThink, Reformulation changes the representation of inbound data to proper way and activates Learned Critics then KnowHow WayToThink.

`Learned -> [ReasoningByAnalogy|DivideAndConquer] -> Deliberate -> Reformulation -> Learned -> KnowHow`
