# Training mode design specification.

## Training incident description example
```
User had received wrong application.
User has ordered Wordfinder Business Economical.
However she received wrong version, she received Wordfinder Tehcnical instead of Business Economical.
Please assist
```

## <a name="Goals_data_example">Goals data example used for training</a>
```
 1. SubGoal = Resolve incident
   2. SubGoal = ParseIncidentDescription, Way2Think = ProcessText: KnowingHow, SemanticNetWorkWithKLines =
{
TODO: Add processed example here.
}
   2. SubGoal = UnderstandIncidentType, Critics = Deliberative, Type = ProblemDescription with DesiredState
     3. SubGoal = ModelCurrentSituation using ProjectDomain Model, Way2Think = Simulate, Model =
{
User Desired(ordered) Soft(Wordfinder Business Economical)
Operator Installed Soft(Wordfinder Tehcnical) - wrongly
}
     3. SubGoal = FormalizeProblemDescription using ProblemModel(Wrong state, Desired state), Way2Think = Reformulate, Model=
{
WrongState = Soft.installed(Wordfinder Tehcnical), Soft.notInstalled(Wordfinder Business Economical)
DesiredState = Soft.installed(Wordfinder Business Economical), Soft.unInstalled(Wordfinder Tehcnical)
}
     3. SubGoal = Find solution, Way2Think = ExtendedSearch, Solution =
     { Install(Wordfinder Business Economical), UnInstall(Wordfinder Tehcnical)}
```

## Information to be trained

 1. Goals structure, could be defined explicitly or inferred during Incident handling training = Specified by Knowledge engineer and Project induction.
 1. Incident handling process, see [Goals data example](training.md#Goals_data_example) = Specified by Knowledge engineer.
 1. Domain concepts dictionary = Comes from TSS training courses.
   2. User.
   2. Software.
   2. Installation(install).
 1. HowTo-s the incident solution algorithms = Comes from Project workbooks.

 ## Workflow

 ### Train incident handling process

  1. Process Goals parameter
    2. Create Narrative of the Critics, Way2Think sequence.
    2. Connect all intermediate knowledge: SemanticNetWorkWithKLines, ProblemDescription with DesiredState, Model, Solution
    with KLine(context = Request)
    2. Connect all matching terms and concepts of intermediate knowledge with KLine-s
      3. Connect each parameter of Solution HowTo with Formal Model (of previous step)
      3. Set Formal Model as context of KLine and store Solution in frames parameter of KLine.