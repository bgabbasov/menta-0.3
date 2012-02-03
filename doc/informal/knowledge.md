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
  2. Description: StringResource
     3. Contains description of Incident
  2. IncidentCategory: Microneme
     3. Contains already defined category TODO:Add sample
  2. FormalizedDescription: SemanticNetwork
     3. Fornalized description of problem
  2. Solution: SemanticNetwork
     3. Solution of incident in formalized
  2. CustomAttributes:Dictionary
     3. Additional attributes of Request (already formalized)

#### Production mode
1. Inbound data: Frame
  2. Incident description text: StringResource
  2. Incident category: Microneme

### Preliminary annotation
SemanticNetwork of the Incident description.

### <a name="KnowledgeBase_annotation"> KnowledgeBase annotation</a>
SemanticNetwork of the Incident description with KLine-s that links to KnowledgeBase resources.

### <a name="Simulation_Way2Think">Simulation Way2Think</a>
SemanticNetwork that models the situation of the Incident description.

### <a name="Reformulation_Way2Think">Reformulation Way2Think = Formalisation result</a>
TransFrame in case of the UserProblem

### SolutionGeneration Way2Think
SemanticNetwork of HowTo-s
