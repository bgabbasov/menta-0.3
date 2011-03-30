=====================
Perceiving algorithm.
=====================
The description of the perceiving algorithm.
-----------------
Introduction 
-----------------
This algorithm is based on machine learning and  stochastic search with probabilistic logic.

---------------------------------------
Requirement specification standard 
---------------------------------------
The standard for the requirement specification could be found here
[http://www.sqi.gu.edu.au/spice/suite/ SPICE Document suite]

---------------------------------------
Input and output of the Perceiving
---------------------------------------

 - Input: Set of predicates from Stanford nlp adapter.
 - Output: Acceptance criteria in the form of How-to.
---------------
Algorithm 
---------------
Perceiving component maps the parts of the predicates (outbound of the linguistic) to the meta-model of how-to. 
Consider the problem of the perceiving as the problem of the creation of the program that interprets the inbound predicates as meta-model of how-to. 
Stochastic search provides required flexibility for the perceiving.
Fitness function of the stochastic search is based on the [http://en.wikipedia.org/wiki/Conditional_random_field CRF] that calculates the probability of the generated mapping(perceiving) based on trained maps and the context.
Context includes:
 #. Predicates parts annotations
 #. Semantic annotations (previously trained terms)
 #. Analogy annotations
-----------------
Decomposition 
-----------------
 #. Analyser 
  #. Classifier
  #. Predicates annotator 
  #. Semantic annotator (trained terms and external dictionaries)
  #. Analogy annotator
 #. Mapping generator
  #. Mapping checker(Fitting function) based on CRF, answers question how probable mapping is.
 #. Memo (machine learning)
  #. Memorise
  #. Generalisation
  #. Specialisation

-----------------
Main work-flow
-----------------
Linguistic analysis -> Analysis(Predicates, Analogy and Semantic annotations) -> Search for the ready mapping `[`if not found Generation of mapping via stochastic search`]` -> Confirmation from human expert -> Create probability mapping rules (machine learning), updates machine learning Trainer run.

Analysis
===========
Is the pre-generation stage based on annotators: Classifier, Predicates annotator, Semantic annotator, Analogy 

Classifier
------------
Determines whether the inbound predicates are the instruction what should be done, or the description of the problem according to the annotated word contents.

==== Predicates annotator ====
Annotates the terms with the Typed dependencies tagging of the Lexical parser based on the structure of the predicate.

==== Semantic annotator ====
Annotates the terms of the predicates with the semantic tags(mappings to the concepts) that are already done.

==== Analogy annotator ====
Input Graph mapping could make use of the analogy based on context to set up the hypothesis of the semantics of the node.

=== Mapping generator  ===
Is main source of new solutions that could be saved(memorised). This could be understood as the base of the machine learning. After the idea(hypothesis) is been confirmed Memo operations: memorize, generalize, specialise are performed.

==== Fitting function ====
Fitting function is based on CRF that is based on the trained data, external dictionaries: [http://csc.media.mit.edu/conceptnet conceptNet], [http://ru.wikipedia.org/wiki/WordNet WordNet], [http://www.cyc.com/cyc/opencyc OpenCyc] that answers the question how probable is the generated mapping. All logical inference is done by [http://code.google.com/p/menta/wiki/ReasonerAdapter Reasoner].

==== Operation of the generator ====
{{{
addMapping($source, $destination) 
}}}

==== Probabilistic reasoning ====
 * Input constraints (all input nodes should have connections to domain nodes)
 * Domain constraints (structure of the how-to meta-model)
 * Learned constraints (mapping learned previously as probabilistic rules)
The set of constraints influences the fitting function during computation of the plausibility of the generated solution.

=== Memo ===
Memo is actually the machine learning based on [http://en.wikipedia.org/wiki/Bayesian_network Bayes network].

==== Memorizer ====
Is just store the mapping in the form of how-to individual for the [http://en.wikipedia.org/wiki/Bayesian_network Bayesian network] rule.

==== Generalizer ====
Create general mapping how-to based on several specific mappings.

==== Specializer ====
Create specific mapping how-to based on the several general how-tos.
