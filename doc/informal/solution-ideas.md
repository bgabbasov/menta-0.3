# Problems solution ideas list.
Problems from [Informal vision](https://github.com/menta/menta-0.3/blob/master/doc/informal/vision-informal.md) solutions list.

## Naive (kids) perception
When people start to communicate they start using words to denote real world objects. This way words are references to
the objects that we already know. When kid do not understand some phrases, adults explains the logical connections and
logical operations to understand and process the phrase correctly. This way we learn to think logically during understanding process.

### Self learning common sense knowledge
From the program perspective the incident world is completely visible, regardless to access right of the system user.
This way the system could learn some common sense knowledge based on it's own experiments.
For example: system could/should try to copy then move files from source to destination directory,
this way it should learn that copying files creates one more instance in destination directory, but moving does not.

This way we need:

 1. Some system understandable *flexible* descriptions of words/phrases in common IT lexicon.
 1. Some logical mechanism to infer.
