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
             5. User has a goal to get rid of problem.
                 6. If ProblemSource mentioned explicitly (need Software) => DesiredState = Software installed.
                 6. Else initiate Deliberate Critics to find out the ProblemSource.
     3. Deliberate Critics selects ExtensiveSearch Way2Think.
     3. ExtensiveSearch searches for HowTo-s to get from CurrentState to DesiredState(_get rid of wrongly installed software, install desired software_).
         4. If found => reports success.
         4. If fails => activate Cry4Help Way2Think.
   2. Reflective Critics checks if the System goal reached (Problem is exterminated)
         4. If satisfied => reports success.
         4. If fails => activate Cry4Help Way2Think.


## PreliminaryAnnotator