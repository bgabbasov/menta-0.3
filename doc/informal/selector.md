# Selector design specification.

Selector is main component to switch Critics -> Way2Think pair.

## Inbound data

  1. Critics list.
  1. Context[[K-lines](knowledge.md)]

## Workflow

  1. Selector starts inbound [Critics](critics.md) in parallel.
  1. As Critics returns their probabilities and recall Selector select the best variant ([Way2Think](way2think.md))
  taking in account following aspects (thees aspects could be stored in KB as [SemanticNetwork](knowledge.md)):
    2. One Critic is the part of another.
    2. One Critic if triggered is more probable than another.
  1. Encapsulating KnowingHow of current Selector could trigger the Selector to choose less probable variant, this could be used in several cases:
    2. If Reflective Critics realises that current Way2Think does not leads to expected result.
    2. If User is not satisfied with the results.

### Selector activity initiate

![Selector activity initiate](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/selectoractivityinitiate.png)

### Selector activity reset

![Selector activity reset](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/selectoractivityreset.png)