# Way2Think design specification.

Way2Think is main operating unit of the [Critic](critics.md) -> [Selector](selector.md) -> Way2Think triple.
Way2Think is widely used to: update, transform, add knowledge in the system, and even Cry4Help.

## Entry criteria

[ThinkingLifeCycle](thinking-life-cycle.md) starts Way2Think according to [Selector](selector.md) request result.

## Exit criteria

 1. Way2Think completes its workflow.
 1. [ThinkingLifeCycle](thinking-life-cycle.md) invokes stop method.

## <a name="input">Input</a>

 1. Context:[DomainModel](knowledge.md#KnowledgeBase_annotation) or
 1. [DomainModel](knowledge.md#Reformulation_Way2Think) in Context

## <a name="output">Output</a>

 1. Delta of previous and current state:[TransFrame](knowledge.md)

## <a name="Interface">Interface</a>

![Way2Think interface](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/Way2ThinkInterface.png)

## Basic and compound Way2Think

The Way2Think is the workflow that could be represented as [SemanticNetwork](knowledge.md). There are two types of Way2Think: basic and compound.
Basic Way2Think listed below are implemented directly in the System, compounds are created combining [Critics](critics.md),
[Selectors](selector.md), and other Way2Think.


## Basic Ways to think used in the project.
From [Emotion Machine](http://web.media.mit.edu/~minsky/E7/eb7.html#_Toc508708573)

 1. [_Knowing How_](knowingHow.md): The best way to solve a problem is to know how to solve it and use that solution. However, we may not know how to retrieve what we know, or even know that we know it.

 1. [_Extensive Search_](extensiveSearch.md). When one knows no better alternative, one could search through all possible chains of actions—but this is usually impractical because that search grows exponentially.

 1. [_Reformulation_](reformulation.md). Find a different representation that highlights more relevant information. We often do this by making a verbal description—and then ‘understanding’ it in some different way!

 1. [_Simulation_](simulation.md). One can avoid taking physical risks if one can predict “what would happen if” by imagining possible actions inside the mental models that one has built.

 1. [_Cry for help_](cry4Help.md). You can always resort to other techniques that most people would call “emotional.”



