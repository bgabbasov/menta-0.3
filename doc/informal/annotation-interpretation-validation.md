# Annotation interpretation validation.
Solution description.

## Definitions

### Production mode.

1. Entry criteria
  2. User provided new incident Text.
1. Exit criteria.
 2. System found proper formalisation for the inbound Text.
 2. System exceeded maximum energy allowed for the perceiving operation of the incident type.
 2. System needs further clarifications: if the inbound information is not sufficient.
1. Inbound data is Text
  2. Incidents description text.
  2. Incident category.
1. Outbound is AnnotatedText with formalisation results.

### Training mode.

1. Entry criteria
  2. User provided new incidents Texts.
1. Exit criteria.
 2. System found proper formalisation workflow of the Interpreter for inbound Text and incident category, and found validation criteria.
 2. System fails to find proper formalisation workflow.
1. Inbound data is Text
  2. Incidents description text.
  2. Incident category.
  2. Incident formalized description.
  2. Incident solution.
1. Outbound is formalisation workflow of the Interpreter steps, validation criteria.

## Use cases

See https://github.com/menta/menta-0.3/blob/master/doc/informal/emotion-machine.md

## Components

### Collaboration diagram

![Collaboration](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/AIVCollaboration.png)

 1. TextProcessor (one of Lexical parsers) creates the structure of the text as a links of words. Inbound: Text, outbound Word links tree.
 1. Preliminary Annotator adds using data of the TextProcessor adds the annotation to the inbound Text to indicate the sentence structure. Inbound: Text, outbound AnnotatedText.
 1. KnowledgeBaseAnnotator using KnowledgeBase add the semantic annotations of the words found in KnowledgeBase. Inbound: AnnotatedText, outbound AnnotatedText.
 1. Interpreter adds annotations to formalize the inbound AnnotatedText. Inbound: AnnotatedText, outbound AnnotatedText.
 1. Validator checks annotations of the Interpreter to match formalisation criteria if formalisation criteria fails return to KnowledgeBaseAnnotator.

Interpreter and Validator could be expressed via Emotion Machine Solution [see section Workflow](https://github.com/menta/menta-0.3/blob/master/doc/informal/emotion-machine.md) with
[LSA](http://en.wikipedia.org/wiki/Latent_semantic_analysishttp://en.wikipedia.org/wiki/Latent_semantic_analysis) as main interpretation algorithm.

### Component diagram

![Component](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/AIVComponent.png)

Component diagram is supplemental to the Collaboration diagram.

## Formalisation Production Workflow.

See Collaboration diagram description.

## Formalisation Training Workflow.

See section [Formalisation Training Workflow](https://github.com/menta/menta-0.3/blob/master/doc/informal/emotion-machine.md).