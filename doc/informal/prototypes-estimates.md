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
   2. Read documentation: = 2 - 4
     3. [PLN](http://wiki.opencog.org/w/PLN)
     3. [PLN Details](http://wiki.opencog.org/w/PLN_Details)
     3. [Cookbook PLN section](http://wiki.opencog.org/w/Cookbook#Using_PLN)
     3. [PLN usage](http://wiki.opencog.org/w/PLN_usage)
     3. [PLN Scheme Wrapper](http://wiki.opencog.org/w/PLN_Scheme_Wrapper)
   2. Test PLN using following test data (see [NARS syntax](http://code.google.com/p/open-nars/wiki/InputOutputFormat)): = 4 - 8 [difficulties of the NARS -> PLN translation]
     3. [check linked modules example](http://code.google.com/p/menta/source/browse/lib/src/main/test2.narsese)
     3. [check operation to module duplicates, see simplified version](http://code.google.com/p/menta/source/browse/lib/src/main/test4.narsese)
   2. Search for following options:
     3. Simplification.
     3. Elevation .
     3. Reformulation.
     3. Contradiction.
     3. Simulation.
     3. Correlation.
     3. Logical Reasoning.

 1. [Bayesian Inference](http://en.wikipedia.org/wiki/Bayesian_inference)
   2. Find implementation or use [ci-bayes](https://github.com/jottinger/ci-bayes) and install them = 16 - 32 [possibly a lot of implementations]
   2. Compare implementations and PLN using following examples:
     3. [check linked modules example](http://code.google.com/p/menta/source/browse/lib/src/main/test2.narsese)
     3. [check operation to module duplicates, see simplified version](http://code.google.com/p/menta/source/browse/lib/src/main/test4.narsese)
   2. Comparison criteria:
     3. Performance
     3. Adapter development estimate
     3. Probabilistic logic options, use options of PLN analysis

 1. [MOSES](https://github.com/menta/menta-0.3/blob/master/doc/informal/openCog.md#MOSES)
   2. Read documentation: = 2 - 3
     3. [Main](http://wiki.opencog.org/w/MOSES)
     3. [Quick Start](http://wiki.opencog.org/wikihome/images/4/4a/MOSES-QuickGuide.pdf)
     3. [Tutorial](http://wiki.opencog.org/w/MOSES_Tutorial)
     3. [Examples](http://wiki.opencog.org/w/MOSES_example_programs)
   2. Search for following options: = 16 - 40 [difficulties in understanding of MOSES mechanisms]
     3. Reasoning By Analogy.
     3. Reformulation Way2Think.
     3. Use external representations.
     3. Simulation Way2Think.
     3. Correlation Way2Think.

 1. [Embodiment](https://github.com/menta/menta-0.3/blob/master/doc/informal/openCog.md#Embodiment)
   2. Read documentation = 8 - 16 [possibly further understanding of the Embodiment could be required to test it]
     3. [Main](http://wiki.opencog.org/w/Embodiment)
     3. [User manual](http://wiki.opencog.org/w/UserManual_(Embodiment))
   2. Test Embodiment system to simulate [Intellix]((https://github.com/menta/menta-0.3/blob/master/doc/informal/intellix.md)) with following components: = 40 - 80 [possibly difficulties with understanding of [Intellix world](https://github.com/menta/menta-0.3/blob/master/doc/informal/intellix.md)) simulation]
     3. Files
     3. Directories
     3. Operating system commands: copy file, move file, delete file, create file
     3. Program distributives
     3. Installed programs