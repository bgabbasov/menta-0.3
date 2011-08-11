#Design specification.

## Introduction

That are formal methods in the context of natural language processing applied to requirement engineering, incident – problem solving.
Those methods are relatively cheap compared to the manual requirement – incident- problem engineering as a whole
(many human resources involved in that process).
The formal methods as such are not meant for creating (informal) requirements documents into formal documents, they are rather used
to gradually validate requirements - incidents (explicit and implicit),
explore essence of the matter of a requirements – incident documents
(problem-incident ticket, problem – incident report, analysis report and any).
The goal of this approach is to create a usable low-cost, automated analysis – problem solving – resolution mechanism
of natural language requirements.

## Main activities

1. Structuring:
  2. Classify(*select*) the *request* (requirement-incident) via linguistic, semantic parsing and semantic graph projection to multidimensional space of possible *models*(classes of *requests*).
  2. Select the core parts of the document and *map* them to the *model properties* selected in the previous step, via classification of *request* terms in the multidimensional space of *model parts* types.
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

# Example of method
For describing and elaborating the steps described in the main activities section a both, non-existent, (impartial, inconsistent, and implicit)   or decent on natural language requirements document for describing the requirements of incident, problem is used. This requirements document (trouble ticket, problem-incident report) can be used by a IS Monitoring, Operational team in order to check on fly and automate in accordance with SLA timeframe whether the all incoming incidents – reports IS team received via the applied system (sources) has met its requirements and solved.
In the first step, one defines the style, structure and English language specific domain vocabulary for the specific document which contains the requirements of the incoming document (Requirement Document, Problem – Incident ticket document). The document was written in a consistent style and structure, has a good structural quality and was written in English.
In the second step is determined what properties are to check and what possible needed for clarification, by applying to domain-project specific KB. As the requirements - incident document contains lots of technical details that cannot be checked in real time by the Monitoring operator, all properties should be externally observable and marked (sufficient or not) were selected.
In the third step, Menta select the models on the properties will be checked, created requests to KB for correction and for missing objectives; in this case it will use the Circe Menta AI environment to provide automated analysis of the incident requirements. The environment allows the extraction of models from the incoming incident requirements, their validation and the collection of technical -domain data about the requirements document, the system described in it and about the requirements writing process itself.
In step four the document will be pre-processed, parsed, analyzed for sufficiency   and ascertainment of all details, including project-domain specific, missing parts and ready to be translated to a canonical form so it can be used for further automatic processing (incident, change request realization mechanism ).
Step five consists of the parsing of the natural language text. The KB model from step three required a domain-specific term document (format, structure, content). This document -information was taken from the IS project SMDB-KB’s and covered all domain specific terms used in the incident-problem requirements document.
In step six, the building of the models was automatically done using the Menta AI Circe environment.
In step seven the properties that were selected in step two where finally checked. Each property was analyzed by the use of specialized validators (supported in the Menta Circe environment) and consisted of a logical model for incident-problem troubleshooting resolution, mainly focusing on consistency and feasibility by Menta itself. In step eight, the result such incident –problem either fixed and closed tickets or not fixed tickets send by system to operational expert.  On regular base not fixed tickets checked by an IS incident – problem knowledgeable requirement specialist, mainly for consistency errors to improve Menta performance.
