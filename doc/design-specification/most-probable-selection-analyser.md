# MostProbableSelectionAnalyser design specification

Is subclass of [Critic] (critics.md)

## Entry criteria

A list of actions with specified probabilities.

## Exit criteria

One critic with highest probability

## Rule

Should select an action with highest probability. If there are two or more actions with the same probability should select any of them.
Should store other actions to DB.
