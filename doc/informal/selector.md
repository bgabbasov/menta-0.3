# Selector design specification.

Selector is main component to switch Critics -> Way2Think pair.
Selector is used to retrieve proper Actions from KBServer according to the inbound parameters that are treated as Selector request.

## Interface

![Selector interface](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/SelectorInterface.png)

## <a name="action">Action class</a>

![Action class](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/ActionClass.png)


## Workflow

### apply(request : Request) : Action

![apply(request : Request) : Action](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/applyrequestRequestActionActivity.png)

### apply(goal: Goal): Action

![apply(request : Request) : Action](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/applygoalGoalActionActivity.png)

### apply(criticResult : ActionProbabilityRule) : Action

![apply(criticResult : ActionProbabilityRule) : Action](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/applycriticResultActionProbabilityRulePairActionActivity.png)

### apply(criticResults : List[ActionProbabilityPair]) : Action

![apply(criticResults : List[ActionProbabilityPair]) : Action](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/applycriticResultsListofActionProbabilityRulePairActionactivity.png)

### apply(criteria : KLine) : Action

![apply(criteria: KLine) : Action](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/applycriteriaKLineActionActivity.png)


## Selector context Activity diagrams

### Classification Workflow

 1. [ThinkingLifeCycle](thinking-lifeCycle.md) starts inbound [Critics](critics.md) in parallel.
 1. When Critics returns their ActionProbabilityRuleTriple, ThinkingLifeCycle starts one Selector with the List of results.
 1. Selector starts [GetMostProbableWay2Think](design-specification.md#Activity_diagram) that takes in account following aspects:
   2. One Critic is the part of another.
   2. One Critic if triggered is more probable than another.
 1. Encapsulating KnowingHow of current Selector could trigger the Selector to choose less probable variant,
 this could be used in several cases:
   2. If Reflective Critics realises that current Way2Think does not leads to expected result.
   2. If User is not satisfied with the results.

### Start Request processing activity

![start Request processing activity](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/startRequestprocessingactivity.png)

Actions are started by ThinkingLifeCycle in parallel in different threads.

### Classify incident activity

![Classify incident activity](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/classifyIncidentActivity.png)

ThinkingLifeCycle start Critics in parallel with join and collect their results to process them by one Selector.

