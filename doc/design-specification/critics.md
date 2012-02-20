# Critic design specification

Critic is main analysis element in the triple Critic -> [Selector](selector.md) -> [Way2Think](way2Think.md).
Critic is used to: choose way2Think, classify inbound information, reflection, self-analysis and so on.

## Inbound data

 1. Rules.
 1. Incident description: SemanticNetwork with KLine-s or
 1. Simulation Way2Think result: SemanticNetwork

## Outbound data: Triple

 1. [Action](selector.md#action)
 1. Probability: Double
 1. Rule = the logical predicate triggered

## Critic interface

![Critics Class](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/criticClass.png)

## Main Critics links types.

 1. Include = One Critics include another, this way the enclosing Critics if triggered is more probable than the one included.
 1. Exclude = One Critics if triggered excludes another; If two mutually excluding Critics are triggered then Selector should
 mark this situation and return most probable if Critics are weighted or random if weights are equal if the check of
 Perceiving Way2Think invokes the reset() method should switch to the opposite Critic.


