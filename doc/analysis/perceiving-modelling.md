# Simple machine perceiving process modelling.

## Inbound data
```
User had received wrong application.
User has ordered Wordfinder Business Economical.
However she received wrong version, she received Wordfinder Tehcnical instead of Business Economical.
Please assist
```

## Approximate workflow
See [Ways to think](http://web.media.mit.edu/~minsky/E7/eb7.html#_Toc451324833)

 1. PreliminaryAnnotator creates word links.
 1. KnowledgeAnnotator creates concept references.
 1. EmotionMachine runs:
   2. Reflective Critics selects KnowingHow(Perceiving) Way2Think:
   2. KnowingHow(Perceiving) Way2Think:
     3. Deliberate Critics selects Simulation Way2Think.
     3. Simulation crates model of CurrentSituation:
         4. User,
         4. Software,
         4. ...
     3. Deliberate Critics selects Reformulation Way2Think.
     3. Reformulation according to UserProblem template creates UserProblem model(CurrentState and DesiredState delta(_software wrongly installed, software lack on the User computer_)).
     instance from CurrentSituation model.
         4. DesiredState if not mentioned explicitly could be inferred as following:
             5. System has a goal to help User.
             5. To help user System has to satisfy User needs:
             5. User has a goal to get rid of problem.(If ProblemSource mentioned explicitly (need Software) => DesiredState = Software installed, Else initiate Deliberate Critics to find out the ProblemSource.)
     3. Deliberate Critics selects ExtensiveSearch Way2Think.
     3. ExtensiveSearch searches for HowTo-s to get from CurrentState to DesiredState(_get rid of wrongly installed software, install desired software_).
         4. If found => reports success.
         4. If fails => activate Cry4Help Way2Think.
   2. Reflective Critics checks if the System goal reached (Problem is exterminated)
         4. If satisfied => reports success.
         4. If fails => activate Cry4Help Way2Think.


## PreliminaryAnnotator

### [Stanford Parser](http://nlp.stanford.edu:8080/parser/index.jsp)

Typed dependencies, collapsed

```
nsubj(received-3, User-1)
aux(received-3, had-2)
root(ROOT-0, received-3)
amod(application-5, wrong-4)
dobj(received-3, application-5)

nsubj(ordered-3, User-1)
aux(ordered-3, has-2)
root(ROOT-0, ordered-3)
nn(Economical-6, Wordfinder-4)
nn(Economical-6, Business-5)
dobj(ordered-3, Economical-6)

advmod(received-3, However-1)
nsubj(received-3, she-2)
ccomp(received-8, received-3)
amod(version-5, wrong-4)
dobj(received-3, version-5)
nsubj(received-8, she-7)
root(ROOT-0, received-8)
nn(Tehcnical-10, Wordfinder-9)
dobj(received-8, Tehcnical-10)
nn(Economical-14, Business-13)
prep_instead_of(Tehcnical-10, Economical-14)

root(ROOT-0, Please-1)
dep(Please-1, assist-2)
```

### [RelEx](http://wiki.opencog.org/w/Walkthrough#Natural_Language_Processing)

See [XML Semantic parsing results](https://github.com/menta/menta-0.3/blob/master/doc/analysis/incident_7.res.xml) and
[compact version](https://github.com/menta/menta-0.3/blob/master/doc/analysis/incident_7.compact.txt)

Examples of SemanticRelation-s

```
<BinaryRelation leftWord="receive" rightWord="User" label="_subj" />
<UnaryRelation label="verb" word="receive" type="" />
```

### Data structures:

```
SemanticLink {
  name,
  probability,
}

BinaryRelation extends SemanticLink {
  _1,
  _2
}

UnaryRelation extends SemanticLink {
  _1,
  type
}
```