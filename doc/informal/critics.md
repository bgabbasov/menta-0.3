# Critics design specification

## Inbound data

 1. Context

## Outbound data

 1. Probability: Double
 1. Way2Think

## Class diagram

![Critics Class](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/criticClass.png)

## Main Critics links types.

 1. Include = One Critics include another, this way the enclosing Critics if triggered is more probable than the one included.
 1. Exclude = One Critics if triggered excludes another; If two mutually excluding Critics are triggered then Selector should
 mark this situation and return most probable if Critics are weighted or random if weights are equal if the check of
 Perceiving Way2Think invokes the reset() method should switch to the opposite Critic.


