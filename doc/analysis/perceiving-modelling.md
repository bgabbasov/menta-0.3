# Simple machine perceiving process modelling.

## Inbound data
```
User had received wrong application.
User has ordered Wordfinder Business Economical. However she received wrong version, she received Wordfinder Tehcnical instead of Business Economical.
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
     3. Critic ... selects Reformulation Way2Think.
     3. Reformulation according to UserProblem template creates UserProblem model(CurrentState and DesiredState delta(_software wrongly installed, software lack on the User computer_)).
     instance from CurrentSituation model.
     3. Critic ... selects ExtensiveSearch Way2Think.
     3. ExtensiveSearch searches for HowTo-s to get from CurrentState to DesiredState(_get rid of wrongly installed software, install desired software_).
       4. If found => reports success.
       4. If fails => activate Cry4Help Way2Think.

