#Introduction

## Description of use

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

 1. The first step is to classify the requirement-incident based on linguistic parsing and domain vocabulary for the document (Requirement Document, Problem – Incident document/ticket).
 1. The second step is to select the core parts of the document map to the Model of incident selected(classified) in the previous step.
 1. The third step is to look at which properties of the parts are satisfied for established accepting criteria’s or have missing some parts, require additional elucidation of the rule , of the text that have been selected in the second step, will be checked with which models approach.


Step four is the pre-processing step where the format, structure and ascertainment of all details, including project-domain specific, missing details (detected and added from KB) are translated to a canonical form so it can be used for further automatic processing.
Step five consists of the final parsing the natural language text into semantic content.
Step six is the step where the models that were chosen in step three are built (provided generated solution).
Step seven checks if the models and output result successfully check the properties of the content and sufficient for final acceptance.
And finally step eight, which is an ambitious step, consists of evaluating the findings and checking and correcting the requirement specification for incident fixing and delivering final report for incident realization by system itself or manually by assigned specialists.

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
