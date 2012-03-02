# ThinkingLifeCycle specification

## Idea
Contains functionality that run workflow specified in design-specification.md. Will call selectors from https://github.com/menta/menta-0.3/blob/master/doc/informal/selector.md and run return actions in differet threads

In general ThinkingLifeCycle represents factory of Scala Actors (http://www.scala-lang.org/node/242). In common this is publisher subscriber pattern (http://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
Generally this is Service or Daemon (http://wrapper.tanukisoftware.com/doc/english/index.html) with Web Service  access point (http://docs.oracle.com/cd/E17802_01/webservices/webservices/docs/2.0/tutorial/doc/)

Service requirements:

1. Scalability
1. Stability

## Common Overview
![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/ThinkingLifeCycleOverview.png)

There are 5 main components:

1. MentaWebService - entry point for client requests
1. MessageBus - perform message processing between different instances
1. MentaCoreService - services or daemons on different machines (different Menta instances)
1. MentaDataService - Database for Menta
1. ClientAgents - utilities where executors will be running

## MentaWebService
Represents Web Service that server User requests. Requests contain subscription information (callbacks) of clients. All work will be processed by MentaCoresService

## MessageBus
3rd party component, that supports messaging functionality. (MSMQ for example in Windows and http://qpid.apache.org/ for Linux)

## MentaCoreService
Workers that hold functionality of system. Based on PubSub template.Using Scala Actor.

### Description
Objects that represents working threads used Scala Actor pattern.

1. ThinkingLifeCycle
1. SelectorImpl
1. CriticImpl

![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/ThinkingLifeCycle.png)


### Activity overview
When application starts it initialize thinking life cycle and all selectors and critics. Which run initialize Scala Actors
The same action when application stops.

![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/ThinkingLifeCycleInit.png)

### Communication
Every actor communicate with each other using messages
#### Messages Overview

#### Sample
TBD
#### Statistics
TBD

## MentaDataService
Database services that will be shared across different instances

## ClientAgents
Software for service machines, that have access for different locations and hold some amounts of scripts. Contains Executor

