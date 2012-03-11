# Menta-0.3research Design Specification.

## Infrastructure Overview
![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/ThinkingLifeCycleOverview.png)

There are 5 main components:

1. MentaWebService - entry point for client requests
1. MessageBus - perform message processing between different instances
1. MentaCoreService - services or daemons on different machines (different Menta instances)
1. MentaDataService - Database for Menta
1. ClientAgents - utilities where executors will be running

## MentaWebService
Represents Web Service that server User requests. Requests contain subscription information (callbacks) of clients. All work will be processed by MentaCoresService

## MessageBus
3rd party component, that supports messaging functionality. (MSMQ for example in Windows and http://qpid.apache.org/ for Linux)

## MentaCoreService
[MentaCoreService](thinking-life-cycle.md)

## MentaDataService
Database services that will be shared across different instances

## ClientAgents
Software for service machines, that have access for different locations and hold some amounts of scripts. Contains Executor


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

