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
 1. KnowledgeBaseAnnotator creates concept references.
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
[compact version](https://github.com/menta/menta-0.3/blob/master/doc/analysis/incident_7.compact.txt).

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

## [KnowledgeBaseAnnotator](https://github.com/menta/menta-0.3/blob/master/doc/informal/prototypes-estimates.md#KnowledgeBaseAnnotator)

### [WolframAlpha](http://www.wolframalpha.com/input/?i=what+is+the+meaning+of+life)

```
Request = what is user
Response =
1 | noun | a person who makes use of a thing; someone who uses or employs something
2 | noun | a person who uses something or someone selfishly or unethically
3 | noun | a person who takes drugs
```
```
Request = what is received
Response =
1 | adjective | conforming to the established language usage of educated native speakers
2 | adjective | widely accepted as true or worthy
```
```
Request = what is Wordfinder Business Economical
Response =
noun | a thesaurus organized to help you find the word you want but cannot think of
```

### [TrueKnowledge](http://www.trueknowledge.com/q/what_is_the_meaning_of_life)

```
Request = what is user
Response =
user, a computer identity used to access a particular computer network
class
Parent Class = technology, object, computing concept, concept that can be classified by sector of human endeavor, conceptual object,  …
```
```
Request = what is received
Response =
is someone who won as prize money
relation
```
```
Request = what is Wordfinder Business Economical
Response =
The term 'wordfinder' means a thesaurus organized to help you find the word you want but cannot think of
```

### [ConceptNet](http://csc.media.mit.edu/conceptnet)

```
Request = what is user
Response =
	a user is a kind of person.
	users can use.
	A user is someone who takes drugs
	Users can train Open Mind
	users can explain that verb
	software is used for users.
	a user can complete a form
	A user can mine a database
```
```
Request = what is received
Response =
	Beggers are used to recieving
	getting something requires being there to receive it
	The effect of getting something is receiving
	Something that might happen when you get something is receiving it
	receive is action
	opening a gift requires receiving one
```
```
Request = what is Wordfinder Business Economical
Response =
Hmm. I don't know anything about that concept.
```

### [ConceptNet5](http://conceptnet5.media.mit.edu/)

```
Request = user
Response =
...
    {
      "end": "/concept/en/user",
      "weight": 1,
      "start": "/concept/en/user/n/one_who_uses_something,_a_consumer",
      "score": 1257.3005135859114,
      "key": "senseOf /concept/en/user/n/one_who_uses_something,_a_consumer /concept/en/user",
      "start_url": "http://conceptnet5.media.mit.edu/data/concept/en/user/n/one_who_uses_something,_a_consumer",
      "type": "senseOf"
    },
...
```
```
Request = receive
Response =
...
    {
      "end": "/concept/en/receive",
      "weight": 1,
      "start": "/assertion/[/relation/Causes/,/concept/en/get_something/,/concept/en/receive/]",
      "score": 250.98328321790424,
      "key": "arg2 /assertion/[/relation/Causes/,/concept/en/get_something/,/concept/en/receive/] /concept/en/receive",
      "start_url": "http://conceptnet5.media.mit.edu/data/assertion/[/relation/Causes/,/concept/en/get_something/,/concept/en/receive/]",
      "position": 2,
      "type": "arg"
    },
...
```
```
Request = Wordfinder
Response =
{"error": "invalid uri /concept/en/Wordfinder"}
```

### [WordNet](http://wordnet.princeton.edu/)

```
Request = user
Response =
S: (n) user (a person who makes use of a thing; someone who uses or employs something)
S: (n) exploiter, user (a person who uses something or someone selfishly or unethically)
S: (n) drug user, substance abuser, user (a person who takes drugs)
```
```
Request = receive
Response =
S: (v) receive, have (get something; come into possession of) "receive payment"; "receive a gift"; "receive letters from the front"
S: (v) receive, get, find, obtain, incur (receive a specified treatment (abstract)) "These aspects of civilization do not find expression or receive an interpretation"; "His movie received a good review"; "I got nothing but trouble for my good intentions"
S: (v) pick up, receive (register (perceptual input)) "pick up a signal"
S: (v) experience, receive, have, get (go through (mental or physical states or experiences)) "get an idea"; "experience vertigo"; "get nauseous"; "receive injuries"; "have a feeling"
S: (v) receive, take in, invite (express willingness to have in one's home or environs) "The community warmly received the refugees"
S: (v) receive (accept as true or valid) "He received Christ"
S: (v) welcome, receive (bid welcome to; greet upon arrival)
S: (v) receive (convert into sounds or pictures) "receive the incoming radio signals"
S: (v) meet, encounter, receive (experience as a reaction) "My proposal met with much opposition"
S: (v) receive (have or give a reception) "The lady is receiving Sunday morning"
S: (v) get, receive (receive as a retribution or punishment) "He got 5 years in prison"
S: (v) receive (partake of the Holy Eucharist sacrament)
S: (v) receive (regard favorably or with disapproval) "Her new collection of poems was not well received"
```
```
Request = Wordfinder
Response =
S: (n) word finder, wordfinder (a thesaurus organized to help you find the word you want but cannot think of)
```

### [OpenCyc](http://www.opencyc.org/)

```
Request = user-theprogram
Response =
GAF Arg : 1

Mt : UniversalVocabularyMt
isa :	Individual

Mt : ComputerSoftwareDataMt
isa :	UserInterfaceProgram MicrosoftComputerProgram UnversionedProgram LocalProgram MSWindowsApplication
comment :	"The Win16 User for Win16 application compatibility."

Mt : EnglishMt
prettyString :	"Windows User-interface core component"
prettyString-Canonical :	"User"
```
```
Request = receive
Response =
---> 	toreceive would be here.
```
```
Request = Wordfinder
Response =
---> 	Wordfinder would be here.
```