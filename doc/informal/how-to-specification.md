# How-to specification
![Knowledge structure](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/HowTo.png)

# Idea
There are 2 types of HowTo:

1. ValueHowTo
1. FunctionalHowTo

## ValueHowTo
Holds simple value. Such as string, integer e.t.c.

## FunctionalHowTo 
Holds script execution

1. ScriptName is a name of executable script
1. InputParameters - obfuscate input parameters for script
1. OutputParameters - pbfuscate output data from script

## Mapping mechanism
Each action from fromalized data map directly to FunctionalHowTo, each single node point to value how-to and holds description of entity. Actually input parameters of how-to indicates how-to, that applicable to this script

```
[18:12:43] Talanov Max: let's do it flexible

[18:13:12] Talanov Max: for example each how to should have some formalized decription of the situation it could be used

[18:13:31] Talanov Max: and then extended search could find it using this parameter

[18:13:40] Talanov Max: what about ithis?

[18:13:59] Talanov Max: for example using K-line
```