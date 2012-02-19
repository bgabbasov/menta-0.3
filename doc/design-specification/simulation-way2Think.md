# Simulation Way2Think design specification.

## Entry criteria

DirectInstruction, ProblemWithDesiredState, ProblemWODesiredState [Critics](critics.md) returned Simulation Way2Think.

## Exit criteria

Domain model of Incident description, partly or completely is created.

## Input

[SemanticNetwork](knowledge.md) with [KLine-s](knowledge.md) of Incident description.

## Output

Domain SemanticNetwork simulating current situation from Incident description.

## Workflow

For each node in inbound Incident description SemanticNetwork find the map to node in the Domain SemanticNetwork via(through) concepts
of the KnowledgeBase.


## OWL example

[Example in OWL](https://raw.github.com/menta/menta-0.3/master/doc/design-specification/owl/SemanticNetwork_UserReceivedWrongApplication.owl)