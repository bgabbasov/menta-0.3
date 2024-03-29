# Training mode design specification.

## Training incident description example
```
User had received wrong application.
User has ordered Wordfinder Business Economical.
However she received wrong version, she received Wordfinder Tehcnical instead of Business Economical.
Please assist
```

## <a name="Training_tree">Training tree</a>
```
 1. SubGoal = Resolve incident
   2. SubGoal = ParseIncidentDescription, Way2Think = ProcessText: KnowingHow, SemanticNetWorkWithKLines =
{
nsubj(received-3, User-1)
aux(received-3, had-2)
root(ROOT-0, received-3)
amod(application-5, wrong-4)
dobj(received-3, application-5)

advmod(received-3, However-1)
nsubj(received-3, user-2)
ccomp(received-8, received-3)
amod(version-5, wrong-4)
dobj(received-3, version-5)
nsubj(received-8, user-7)
root(ROOT-0, received-8)
nn(Tehcnical-10, Wordfinder-9)
dobj(received-8, Tehcnical-10)
advmod(of-12, instead-11)
prep(Tehcnical-10, of-12)
nn(Economical-14, Business-13)
pobj(of-12, Economical-14)
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
 1. Domain concepts dictionary = Comes from TSS training courses.
   2. User.
   2. Software.
   2. Installation(install).
 1. HowTo-s the incident solution algorithms = Comes from Project workbooks.
 1. Incident handling process, see [Goals data example](training.md#Goals_data_example) = Specified by Knowledge engineer.

## Train Goals

### Goals tree

![Goal](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/GoalConceptClass.png)

Goals could be infered from:

 1. Explicitly from Goals -> SubGoal-s structure
 1. Implicitly appended from Goals parameter of Incident handling training

### Training multiple goals on the same level

#### Training:
But if Training process finds several goals on the same level, when adds new subgoal, it should try to add classification as previous step.
Classification is delta data based. If there is no option to find delta(same data triggers two goals) then use MostProbableWay2Think. 

#### Production:
MostProbableWay2Think Critics returns most probable Way to think, all the rest are stored in MostProbableWay2Think: Frame according to probability. If on further steps of production process Reflective/SelfReflective Critics hits the failure of the choice, it should use MostProbableWay2Think: Frame to use less probable and recalculate probability of the goal.



## Train Domain concepts

 1. First explicitly from specified Domain SemanticNetWork
 1. SemanticNetWork could be appended by subsequent Domain training sessions.

## HowTo-s training

 1. Explicitly from HowTo functional description //TODO add example here
 1. Implicitly appended from Goals parameter of Incident handling training

### Train Incident handling process
_Please note that all data linked via Goal's KLine_

 1. Process Goals parameter
   2. Create Narrative of the Critics, Way2Think sequence.
   2. Connect all intermediate knowledge: SemanticNetWorkWithKLines, ProblemDescription with DesiredState, Model, Solution
   with KLine(context = Request)
   2. Connect all matching terms and concepts of intermediate knowledge with KLine-s
     3. Connect each parameter of Solution HowTo with Formal Model (of previous step)
     3. Set Formal Model as context of KLine and store Solution in frames parameter of KLine.

## Class description

![Goal](https://github.com/menta/menta-0.3/blob/master/doc/design-specification/uml/images/Training.png?raw=true)

 1. goal - link to goal assiciated with this training node
 1. ParentNode -reference to Parent Training Node 


## Example

### Domain Concept Training

Possible common object for domain concept

```
Action:{

}
Object:{

}
Link:{

}
```

Input:

```
Firefox is a soft. Soft can be installed, reinstalled, removed. Instead of soft term we can use application, program.
```

Domain Data:

```
Soft:Object {
 synonyms:[Application, Program]
 appliedActions:[Install, ReInstall]
}

Action:{
 LinkedLinguisticTerm:[
  verb
 ]
}

AppliedTo:Link{
  linguisticTerm:[
   dobj
  ]
}

Install:Action{
}

ReInstall:Action{
}

Remove:Action{
}

```

Possible Linguistic Data:

```

subject:Object{

}

verb:Object{

}

dobj:Link{

}
```

### How-tos training
3 incidents:

```
1.User is missing "Outlook pst file backup" icon on her desktopName
2.Users VPN client 4.0.4 is corrupt and needs to be reinstalled
3.User is unable to access external pages when connected via VPN,
IE just stops responding. Confirmed proxy settings, which seemed 
correct and cleared cookies/temp internet files, but problem persists.
Also tried to check "automatically detect settings", but it didn't 
solve the issue.Can you please assist?

```

After main cycle processing we have a goals structure for each incident from above. Also goals can be entered manually. Below an example of goals.

Example

1. ResolveIncident
  2. Missing backup link
1. ResolveIncident
  2. CorruptedSoftware
1. ResolveIncident
  2. AccessProblem
    3. VPN


Goals has solution KLines. For example for second incident and goals:

1. ResolveIncident
  2. CorruptedSoftware

```
Solution:{
 how-tos:[remove,install]
}

remove:howto{
  Parameters:[

    {Key:'SoftwareName',
    Value:'VPN'},
    {Key:'ServerName',
    Value:'TestServer'}
  ]

  InputParameters:[
    {Key:'SoftwareName',
    Value:'VPN'},
    {Key:'ServerName',
    Value:'TestServer'}
  ]

  OutputParameters:[
    {Key:'Result',
    Value:''},

  ]
}

install:howto{
  Parameters:[

    {Key:'SoftwareName',
    Value:'VPN'},
    {Key:'ServerName',
    Value:'TestServer'}
  ]

  InputParameters:[
    {Key:'SoftwareName',
    Value:'VPN'},
    {Key:'ServerName',
    Value:'TestServer'}
  ]

  OutputParameters:[
    {Key:'Result',
    Value:''},

  ]
}
```
