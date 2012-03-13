# ThinkingLifeCycle specification

Runs workflow specified in [design specification](design-specification.md).
Invokes [Selectors](selector.md), [Critics](critics.md), [Way2Think](way2Think.md) and manages threads to run actions in parallel.

ThinkingLifeCycle represents factory of [Scala Actors](http://www.scala-lang.org/node/242), that uses
[publisher subscriber pattern](http://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)


## MentaCoreService
Workers that hold functionality of system. Based on PubSub template.Using Scala Actor.

### Description
Objects that represents working threads used Scala Actor pattern.

1. ThinkingLifeCycle
1. SelectorImpl
1. CriticImpl

![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/ThinkingLifeCycle.png)


### Activity overview

When application starts it initializes ThinkingLifeCycle that activates [Critics](critics.md) based on [Goal](goal.md) Critic is subscribed, as Scala actors.
When application stops it stops all Actions, Selectors and ThinkingLifeCycle.

![Component diagram](https://github.com/menta/menta-0.3/raw/master/doc/design-specification/uml/images/ThinkingLifeCycleInit.png)

### Communication

Every actor communicate with each other using messages

#### Messages Overview

#### Sample
When request come from [bus](message-bus.md) it will take by Thinking lifecycle and will be processed accroding to wrokflow.

#### Statistics
Statistics is a special critic that process SLA and other counters. (add link to Self Reflective)

