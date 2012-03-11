# Critic design specification

Critic is main analysis element in the triple Critic -> [Selector](selector.md) -> [Way2Think](way2Think.md).
Critic is used to: choose way2Think, classify inbound information, reflection, self-analysis and so on.

## Entry criteria

[ThinkingLifeCycle](thinking-life-cycle.md) starts Critics according to [Goal](goal.md).

## Exit criteria

 1. Critic generates [Selector](selector.md) request: SelectorRequest.
 1. [ThinkingLifeCycle](thinking-life-cycle.md) invokes stop method.

## Input

 1. Critic Rules(see below).
 1. Incident description: [DomainModel](knowledge.md#domain) with KLine-s.
 1. Simulation Way2Think result: [DomainModel](knowledge.md#domain).

## Output: Pair

 1. [SelectorRequest](selector.md#action).
 1. Critic Rule = the logical predicate triggered(see below).

## Critic interface

![Critics Class](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/CriticInterface.png)

## Critic rules

![Critic Class](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/CriticRuleClass.png)

## Main Critic types

 1. Manager - most simple type of critic, works as [Goal](goal.md) trigger to start [Way2Think](way2Think.md), ex.: GoalManager, PreprocessManager.
 1. Control - listener that monitors some event: time exceeds, energy exceeds etc, usually starts [Cry4Help](cry4Help.md) [Way2Think](way2Think.md), ex.: TimeControl, EnergyControl.
 1. Analyser - most complex critic, exploits extensive analysis of the previous Actions results, usually used in classification:
 DirectInstructionAnalyser, ProblemWODesiredStateAnalyser, GetMostProbableActionAnalyser.

## Main Critic links types.

 1. Include = One Critics include another, this way the enclosing Critics if triggered is more probable than the one included.
 1. Exclude = One Critics if triggered excludes another; If two mutually excluding Critics are triggered then Selector should
 mark this situation and return most probable if Critics are weighted or random if weights are equal if the check of
 Perceiving Way2Think invokes the reset() method should switch to the opposite Critic.


