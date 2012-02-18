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

## Knowledge data model
[Knowledge model](https://github.com/menta/menta-0.3/blob/master/doc/design-specification/knowledge.md)

## <a name="Activity_diagram">Activity diagram</a>

[Approximate workflow](https://github.com/menta/menta-0.3/blob/master/doc/informal/perceiving-modelling.md#Approximate_workflow)

![Life cycle activity](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/LifecycleActivity.png)

## Main processes(Triplets Critic -> Selector -> Action[Critic|Way2Think]).

 1. Request description preprocessing.
 1. Incident classification.
 1. Solution generation.
 1. [Clarification request processing.](clarification-request-processing.md)
 1. Understood SemanticNetwork making sense analysis.

