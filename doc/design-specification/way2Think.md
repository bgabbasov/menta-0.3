# Way2Think design specification.

Way2Think is main operating unit of the [Critic](critics.md) -> [Selector](selector.md) -> Way2Think triple.
Way2Think is widely used to: update, transform, add knowledge in the system, and even Cry4Help.

## Inbound data

 1. Context:[SemanticNetwork with KLine](knowledge.md#KnowledgeBase_annotation) or
 1. Context:[SemanticNetwork](knowledge.md#Reformulation_Way2Think)

## <a name="Outbound_data">Outbound data</a>

 1. Delta of previous and current state:[TransFrame](knowledge.md)

## <a name="Interface">Interface</a>

![Way2Think interface](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/Way2ThinkInterface.png)

## Basic and compound Way2Think

The Way2Think is the workflow that could be represented as [SemanticNetwork](knowledge.md). There are two types of Way2Think: basic and compound.
Basic Way2Think listed below are implemented directly in the System, compounds are created combining [Critics](critics.md),
[Selectors](selector.md), and other Way2Think. Basic way2Think rough descriptions could be found in: [Emotion Machine](http://web.media.mit.edu/~minsky/E7/eb7.html#_Toc508708573).

## Main Way2Think

 1. Create Context.
 1. Set Emotional State.
 1. Set Goal.
 1. Inbound description preprocessing.
 1. Cry4Help.
 1. Store less probable Way2Think.
 1. [Simulate.](simulation-way2Think.md)
 1. [Reformulate.](reformulate-way2Think.md)
 1. Extensive search.
 1. Return learned HowTo.
 1. Communicate to user.
 1. Stop lower processes.


