# Training mode design specification.

## Training incident description example
```
User had received wrong application.
User has ordered Wordfinder Business Economical.
However she received wrong version, she received Wordfinder Tehcnical instead of Business Economical.
Please assist
```

## Goals data used for training

 1. SubGoal = Resolve incident
   2. SubGoal = UnderstandIncidentType, Critics = Deliberative, Type = ProblemDescription with DesiredState
     3. SubGoal = ModelCurrentSituation using ProjectDomain Model, Way2Think = Simulate, Model =
```
User Desired(ordered) Soft(Wordfinder Business Economical)
Operator Installed Soft(Wordfinder Tehcnical) - wrongly
```
     3. SubGoal = FormalizeProblemDescription using ProblemModel(Wrong state, Desired state), Way2Think = Reformulate, Model=
```
WrongState = Soft.installed(Wordfinder Tehcnical), Soft.notInstalled(Wordfinder Business Economical)
DesiredState = Soft.installed(Wordfinder Business Economical), Soft.unInstalled(Wordfinder Tehcnical)
```
     3. SubGoal = Find solution, Way2Think = ExtendedSearch, Solution = Install(Wordfinder Business Economical), UnInstall(Wordfinder Tehcnical)