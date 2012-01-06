#Prototypes and estimates
The list of prototypes with WBS and estimates in man/hours with following layout.

```1. Prototype name = sunny day estimate m/h - rainy day estimate m/h [risks]{preconditions}```

## [OpenCog Solution](https://github.com/menta/menta-0.3/blob/master/doc/informal/openCog.md)

 1. [CogBuntu](http://wiki.opencog.org/w/CogBuntu)
   2. [Read documentation](http://wiki.opencog.org/w/CogBuntu) = 0.5 - 1 [need further reading]
   2. [Install CogBuntu](http://wiki.opencog.org/w/CogBuntu#How_to_Get_cogbuntu) = 1 - 4 [problems with iso installation on virtual machine]

 1. [AtomSpace](https://github.com/menta/menta-0.3/blob/master/doc/informal/openCog.md#AtomSpace)
   2. [Read documentation](http://wiki.opencog.org/w/AtomSpace), [Cookbook](http://wiki.opencog.org/w/Cookbook) = 2 - 4 [need further reading]
   2. Test the storage using [Cookbook](http://wiki.opencog.org/w/Cookbook#Importing_Data)
   and [test data to be loaded and requested](http://menta.googlecode.com/hg/test/OwlTest/src/main/resources/preload/storage.test.0.2.owl)
   =  4 - 8 [possible additional setup of the AtomSpace server and TCP connection]{CogBuntu is operational}

 1. [PLN](https://github.com/menta/menta-0.3/blob/master/doc/informal/openCog.md#PLN)
   2. Read documentation: [PLN](http://wiki.opencog.org/w/PLN),
   [PLN Details](http://wiki.opencog.org/w/PLN_Details), [Cookbook PLN section](http://wiki.opencog.org/w/Cookbook#Using_PLN), [PLN usage](http://wiki.opencog.org/w/PLN_usage),
   [PLN Scheme Wrapper](http://wiki.opencog.org/w/PLN_Scheme_Wrapper) = 2 - 4
   2. Test PLN using: [check linked modules example](http://code.google.com/p/menta/source/browse/lib/src/main/test2.narsese),
   [check operation to module duplicates, see simplified version](http://code.google.com/p/menta/source/browse/lib/src/main/test4.narsese),
   see [NARS syntax](http://code.google.com/p/open-nars/wiki/InputOutputFormat) = 4 - 8 [difficulties of the NARS -> PLN translation]

 1. [Bayes Network](http://en.wikipedia.org/wiki/Bayesian_network)