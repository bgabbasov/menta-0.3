# Selector design specification.

Selector is main component to switch Critics -> Way2Think pair.

## Interface

![Selector interface](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/SelectorInterface.png)

## Workflow

 1. [ThinkingLifeCycle](thinking-lifeCycle.md) starts inbound [Critics](critics.md) in parallel.
 1. As Critics returns their ActionProbabilityRuleTriple Selector
 starts [GetMostProbableWay2Think](design-specification.md#Activity_diagram) that takes in account following aspects:
   2. One Critic is the part of another.
   2. One Critic if triggered is more probable than another.
 1. Encapsulating KnowingHow of current Selector could trigger the Selector to choose less probable variant,
 this could be used in several cases:
   2. If Reflective Critics realises that current Way2Think does not leads to expected result.
   2. If User is not satisfied with the results.

## Start Request processing activity

![start Request processing activity](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/startRequestprocessingactivity.png)

## Action class

![Selector interface](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/ActionClass.png)
