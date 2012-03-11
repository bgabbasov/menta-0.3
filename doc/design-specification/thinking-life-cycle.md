# ThinkingLifeCycle specification

## Idea
Contains functionality that run workflow specified in design-specification.md. Will call selectors from https://github.com/menta/menta-0.3/blob/master/doc/informal/selector.md and run return actions in differet threads

In general ThinkingLifeCycle represents factory of Scala Actors (http://www.scala-lang.org/node/242). In common this is publisher subscriber pattern (http://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
Generally this is Service or Daemon (http://wrapper.tanukisoftware.com/doc/english/index.html) with Web Service  access point (http://docs.oracle.com/cd/E17802_01/webservices/webservices/docs/2.0/tutorial/doc/)

Service requirements:

1. Scalability
1. Stability


## MentaCoreService
Workers that hold functionality of system. Based on PubSub template.Using Scala Actor.

### Description
Objects that represents working threads used Scala Actor pattern.

1. ThinkingLifeCycle
1. SelectorImpl
1. CriticImpl

![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/ThinkingLifeCycle.png)


### Activity overview
When application starts it initialize thinking life cycle and all critics as SCALA's actors.
When application stops it shuwtdowns all selectors and thinking life cycle.  

![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/ThinkingLifeCycleInit.png)

### Communication
Every actor communicate with each other using messages
#### Messages Overview

#### Sample
When request come from bus it will take by Thinking lifecycle and will be processed accroding to wrokflow.

#### Statistics
Statistics is a special critic that runs after request coming and threat SLA and other counters.

