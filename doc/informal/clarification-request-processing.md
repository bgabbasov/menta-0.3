# Clarification request processing specification.

## Workflow

When system needs help with understanding, see
[DoNotUnderstand](https://github.com/menta/menta-0.3/blob/master/doc/informal/design-specification.md#Activity_diagram) sub-process.

It stores the reference to clarification request subject node of model SemanticNetwork. This node defines the concept or template of an expected response.

There could be several types of reference:
 1. Lack of information reference = System miss mandatory information.
 1. Lack of understanding reference = System do not understand the term used in inbound Incident description or Clarification Request Response.
 1. SemanticNetwork structure does not make sense = System domain model do not mach the SemanticNetwork of inbound Incident description or Clarification Request Response

System creates the Clarification Request and sends it to a User. Clarification Request contains Context KLine URI.

User creates Clarification Request Response.

System runs Annotation process over the Clarification Response, then tries to match SemanticNetwork of Clarification Response with the SemanticNetwork of clarification request subject reference via Simulation Way2Think.
