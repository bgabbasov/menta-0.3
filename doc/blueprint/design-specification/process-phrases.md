# Lexical level phrases processing.

## Problem
Current technical approach is based on semantic domain model of incident type. Example:
```Install
  Product vendor:
  Product name:
  Product version:
  Destination:
```
The model is selected based on LSA algorithm (Luminoso), but this approach is not good in case the system does not have
actual model for the incident description, ex.: Wrong version of software was installed.
For this kind of incidents new model should be inferred via logical methods.

## Possible solution
 1. Extend knowledge base for the domain to include all most common concepts that are included in incidents descriptions.
 1. Create phrases dictionaries (based on terms links, see stanford-parser) to identify concepts in textual incident descriptions.
 1. Via LSA match parsed links of the incident descriptions to the concepts of the domain.
 1. Via probabilistic reasoning and set of reflective rules infer main problem symptoms and then find(generate) the solution.