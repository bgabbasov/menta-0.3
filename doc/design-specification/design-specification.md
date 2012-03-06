# Menta-0.3research Design Specification.

## <a name="Use_cases">Use cases</a>

### Training use case
![Training use case](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/UseCaseTrain.png)

### Production use case
![Production use case](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/UseCaseProduction.png)

## <a name="Component_diagram">Component diagram</a>

![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/Component.png)

### Components list

 1. [ThinkingLifeCycle](thinking-life-cycle.md)
 1. [Selector](selector.md)
 1. [Critics](critics.md)
 1. [Way2Think](way2Think.md)
 1. PreliminaryAnnotator
 1. KnowledgeBaseAnnotator
 1. KnowledgeBase

## Knowledge data model
[Knowledge model](https://github.com/menta/menta-0.3/blob/master/doc/design-specification/knowledge.md)

## Main Critics

 1. Learned:
   2. Preprocess manager.
   2. Incident classifier.
   2. Solution classifier.
 1. Deliberative:
   2. Most probable selection analyser.
 1. Reflective:
   2. Goal manager.
   2. Energy control.
   2. [Making sense analyser.](making-sense-analyser.md)
 1. SelfReflective:
   2. Context manager.
   2. Time control.
   2. "Do not understand" State Manager.
 1. SelfConscious:
   2. Emotional state manager.

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

## <a name="Activity_diagram">Activity diagram</a>

[Approximate workflow](https://github.com/menta/menta-0.3/blob/master/doc/informal/perceiving-modelling.md#Approximate_workflow)

[Lifecycle example activity diagram.](https://github.com/menta/menta-0.3/blob/master/doc/design-specification/lifecycle-activity.md)

## Main processes(Triplets Critic -> Selector -> Action[Critic|Way2Think]).

 1. Learned + Deliberative:
   2. Request description preprocessing.
   2. Incident classification.
   2. Solution generation.
 1. Reflective:
   2. [SemanticNetwork making sense analysis.](making-sense-analysis.md)
   2. Goal management.
   2. Energy control.
 1. Self reflective:
   2. Context management.
   2. Do not understand.
 1. Self conscious:
   2. Emotional state control.
 1. [Clarification request processing.](clarification-request-processing.md)

