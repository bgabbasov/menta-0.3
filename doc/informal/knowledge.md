# Knowledge structure

Based on [Marvin Minsky: Emotion Machine: Hierarchy of Representations](http://web.media.mit.edu/~minsky/E8/eb8.html#_Toc518305131)

![Knowledge structure](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/knowledgeClass.png)

## Microneme
Then the present state of your micronemes could represent much of your current mental context—and the states of those fibers are changed, your far-reaching bundle of micronemes will broadcast that information to many other mental resources—so that this will change some of your attitudes, outlooks, and states of mind.
In other words, this system could switch you into other, different ways to think.
I think that this concept of micronemes could help to replace many old and vague ideas about ‘association of ideas.’
We could interpret Microneme as the domain.

## Data structures

Taking in account the main [Perceiving workflow](perceiving-modelling.md#Approximate_workflow). When the Incident comes in the System,
System crates KLine for the Conversation, Narrative to store each step of processing for machine learning and analysis.
Data structures listed below are parts of the Conversation KLine.

### <a name="Incident_inbound_data_structure">Incident inbound data structure</a>

#### Training mode
1. Inbound data: Frame
  2. Incident description text: StringResource
  2. Incident category: Microneme
  2. Incident formalized description: SemanticNetwork
  2. Incident solution: SemanticNetwork

#### Production mode
1. Inbound data: Frame
  2. Incident description text: StringResource
  2. Incident category: Microneme

### Preliminary annotation
SemanticNetwork of the Incident description.

### KnowledgeBase annotation
SemanticNetwork of the Incident description with KLine-s that links to KnowledgeBase resources.

### Simulation Way2Think
SemanticNetwork that models the situation of the Incident description.

### Reformulation Way2Think
TransFrame in case of the UserProblem

### SolutionGeneration Way2Think
SemanticNetwork of HowTo-s

## Formalization outbound data structure

The result of formalisation could be:
 1.Current situation model: SemanticNetwork
 1. Problem description: TransFrame.
