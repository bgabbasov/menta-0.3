# Design specification.

## Introduction

There are formal methods in the context of natural language processing applied to requirement engineering, incident – problem solving.
Those methods are relatively cheap compared to the manual requirement – incident- problem engineering as a whole
(many human resources involved in that process).
The formal methods as such are not meant for creating (informal) requirements documents into formal documents, they are rather used
to gradually validate requirements - incidents (explicit and implicit),
explore essence of the matter of a requirements – incident documents
(problem-incident ticket, problem – incident report, analysis report and any).
The goal of this approach is to create a usable low-cost, automated analysis – problem solving – resolution mechanism
of natural language requirements.

## Model driven understanding

### Main activities

1. Training:
  2. One defines domain model, vocabulary for the specific document set which contains the requirements of the incoming document (Requirement Document, Problem – Incident ticket document).
1. Structuring:
  2. Classify(*select*) the *request* (requirement-incident) via linguistic, semantic parsing and semantic graph projection to multidimensional space of possible *models*(classes of *requests*).
  2. Interpret document parts as properties of selected model: select the core parts of the document and *map* them to the *model properties* selected in the previous step, via classification of *request* terms in the multidimensional space of *model parts* types.
  2. *Validate* mapped *model properties* according to *model accepting criteria*, in the following way:
     3. Create set of *predicates* representing *model* and *properties*.
     3. Using *reasoner* check *model predicates* over *domain model* facts in *KB*.
  2. If validation fails *recalculate weights* of *models* and select most probable once again.
  2. If there are no more not tried models *request* additional *clarification* of the previous *request*.

All steps until eight are the production steps according SLA OLA procedures and project agreements, and can be iterated on at any stage. It should be noted that all those steps, are completely automatic.

1. Formalisation:
  2. Create *HowTo* dictionaries using generalised *concepts* of *domain model*.
  2. Select most probable *HowTo* via classification of *model* in the space of *HowTo symptoms* and selecting nearest (most probable).
  2. Map parameters of *model* over *HowTo* in the same vay as it was described in Structuring section.
  2. Validate *HowTo* instance filled in with *model* parameters in the same vay as it was described in Structuring section.
  2. If validation fails *recalculate weights* of *HowTo-s* and select most probable once again.
  2. If there are no more not tried *HowTo-s*, goto *recalculate weights* of *model*.

![Main activity diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/images/BackTrackeractivity1.png)

## Example of method

1. Training:
  2. One defines the style, structure and English language specific domain vocabulary for the specific document which contains the requirements of the incoming document (Requirement Document, Problem – Incident ticket document).
 The document was written in a consistent style and structure, has a good structural quality and was written in English.
1. Structuring:
  2. Classify: Most probable model of the problem description is selected.
  2. Interpret: Menta maps parts of the request to the model properties.
  2. Validate: Menta validates the model, if validation fails creates clarification request to the user;
   in this case it will use the **Menta Circe** environment to provide automated analysis of the incident requirements.
   The environment allows the extraction of models from the incoming incident requirements, their validation and the collection of technical-domain
   data about the requirements document, the system described in it.
1. Formalisation:
  2. Train: One crate HowTo dictionaries and domain models to be used in HowTo selection and validation.
  2. Classify: The model with parameters is represented as graph in the space of HowTo symptoms and nearest HowTo is selected.
 The building of the models was automatically done using the Menta AI Circe environment.
  2. Validate: The properties that were selected are finally checked.
  Each property is analyzed by the use of specialized validators (supported in the **Menta Circe** environment) and consisted of a logical domain model for
  incident-problem troubleshooting resolution, mainly focusing on consistency and feasibility by Menta itself.
  2. The result such incident –problem either fixed and closed tickets or not fixed tickets send by system to operational expert.
  On regular base not fixed tickets checked by an IS incident – problem knowledgeable requirement specialist, mainly for consistency errors to improve Menta performance.

## Main components
![Main components used in activity](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/images/Component.png)

## Main use cases

![Main use cases](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/images/UseCase.png)

### UC-1 Request to process  problem
#### Preconditions
 User must have an access to the system and system must be operational.
#### Input
Textual Problem – Incident ticket document provided by TSS into the system.
#### Workflow
Please refer to Main activities section.
#### Alternative workflow
If system fails to interpret the inbound document it rises *clarification request*.
#### Output
Result of HowTo application to the *target system*.
#### Post conditions
**Menta Cycle** is done and HowTo is applied to the *target system*. Incident closed
