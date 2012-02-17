# Way2Think design specification.

Way2Think is main operating unit of the [Critic](critics.md) -> [Selector](selector.md) -> Way2Think triple.
Way2Think is widely used to: update, transform, add knowledge in the system, and even Cry4Help.

## Inbound data

 1. Context:[SemanticNetwork with KLine](knowledge.md#KnowledgeBase_annotation) or
 1. Context:[SemanticNetwork](knowledge.md#Reformulation_Way2Think)

## <a name="Outbound_data">Outbound data</a>

 1. Delta of previous and current state:[TransFrame](knowledge.md)

## <a name="Interface">Interface</a>

![Way2Think interface](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/Way2ThinkInterface.png)

## Basic and compound Way2Think

The Way2Think is the workflow that could be represented as [SemanticNetwork](knowledge.md). There are two types of Way2Think: basic and compound.
Basic Way2Think listed below are implemented directly in the System, compounds are created combining [Critics](critics.md),
[Selectors](selector.md), and other Way2Think.


## Basic Ways to think:
From [Emotion Machine](http://web.media.mit.edu/~minsky/E7/eb7.html#_Toc508708573)

 1. _Knowing How_: The best way to solve a problem is to know how to solve it and use that solution. However, we may not know how to retrieve what we know, or even know that we know it.

 1. _Extensive Search_. When one knows no better alternative, one could search through all possible chains of actions—but this is usually impractical because that search grows exponentially.

 1. _Reasoning by Analogy_: When a problem reminds you of one that you solved in the past, you may be able to adapt that case to the present situation—if you have good ways to tell which similarities are most relevant.

 1. _Divide and Conquer_. If you can’t solve a problem all at once, then break it down into smaller parts. For example, every difference we recognize may suggest a separate sub-problem to solve.

 1. _Planning_. Consider the set of sub-goals you want to achieve and examine how they affect each other. Then, with those constraints in mind, propose an efficient sequence for achieving them.

 1. _Simplification_. Sometimes, a good way to make a plan is to make a simplified problem by ignoring some aspects of the original one. Then any solution to the simplified one may serve as a sequence of stepping-stones for solving the initial problem.

 1. _Elevation_. If you are bogged down in too many details, describe the situation in more general terms. But if your description seems too vague, switch to one that is more concrete.

 1. _Reformulation_. Find a different representation that highlights more relevant information. We often do this by making a verbal description—and then ‘understanding’ it in some different way!

 1. _Self-reflection_. Instead of pursuing a problem itself, ask what makes that problem seem hard, or what you might be doing wrong. This can lead to better ways to represent the problem.

 1. _Contradiction_. Try to prove that your problem cannot be solved, and then look for a flaw in that argument.

 1. _Use external representations_: If you find that you’re losing track of details, you can resort to keeping records and notes, or drawing suitable diagrams.

 1. _Simulation_. One can avoid taking physical risks if one can predict “what would happen if” by imagining possible actions inside the mental models that one has built.

 1. _Correlation_. When certain events seem to happen together, try to find ways in which they may be connected.

 1. _Logical Reasoning_. We sometimes make ‘logical chains of deductions,’ but those conclusions may be wrong because of exceptions to our assumptions.[4]

 1. _Wishful thinking_. Imagine having unlimited time and all the resources that you might want. If you still can’t envision solving the problem, then you should reformulate it.

 1. _Impersonation_. When your own ideas seem inadequate, imagine someone better at this, and try to do what that person would do.

 1. _Cry for help_. You can always resort to other techniques that most people would call “emotional.”

 1. _Resignation_. Whenever you find yourself totally stuck, you can shut down the resources you’re using now and relax, lay back, drop out, and stop. Then the ‘Rest of Your Mind’ may find an alternative—or conclude that you don’t have to do this at all.



