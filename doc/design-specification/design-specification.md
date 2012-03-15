# Menta-0.3research Design Specification.

## <a name="Use_cases">Use cases</a>

### Training use case
![Training use case](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/UseCaseTrain.png)

### Production use case
![Production use case](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/UseCaseProduction.png)

## <a name="Component_diagram">Component diagram</a>

![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/Component.png)

### Components list

 1. [MentaWebService](menta-web-service.md)
 1. CoreService
   2. [ThinkingLifeCycle](thinking-life-cycle.md)
   2. [Selector](selector.md)
   2. [Critics](critics.md)
   2. [Way2Think](way2Think.md)
   2. [PreliminaryAnnotator](preliminary-annotator.md)
   2. [KnowledgeBaseAnnotator](knowledge-base-annotator.md)
 1. DataService
   2. [KnowledgeBase](knowledge-base.md)
 1. [ClientAgent](client-agent.md)
 1. [MessageBus](message-bus.md)


## Knowledge data model
[Knowledge model](https://github.com/menta/menta-0.3/blob/master/doc/design-specification/knowledge.md)

## <a name="Activity_diagram">Activity diagram</a>

### Production
[Approximate workflow](https://github.com/menta/menta-0.3/blob/master/doc/informal/perceiving-modelling.md#Approximate_workflow)

[Lifecycle example activity diagram.](https://github.com/menta/menta-0.3/blob/master/doc/design-specification/lifecycle-activity.md)

### Training
[Training process description](training.md)

