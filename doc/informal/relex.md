[RelEx](http://wiki.opencog.org/w/RelEx) 
=======

RelEx is an English-language semantic dependency relationship extractor. 

#Issues parsing result

    + RelEx determines net paths and file paths and doesn't try to analyse them.
    + RelEx try to determine mistakes, and excludes them from analysis
    - Sometimes RelEx assumes important words as mistakes.
    - Usually fails on complicated sentences.
    - Fails on bad english sentences.

RelEx did not recognized most of issues. 

#Statistic

    121: Ok
    221: Ok. But "user" word was excluded from "Mapping of shared drive W:\ fails, user is using...", parser recognized it as mistake.
    321: Don't recognized.
    421: empty phrase, ok
    521: Don't recognized. Complicated sentence. "!PLEASE NOTE!" used but it's not part of sentence. "She" was recognized as mistake and was excluded from "since she's doing some imporant work business".
    621: Don't recognized. There is grammatic mistake in "Seems to CatiaV5 aren't installed correcly.", and RelEx couldn't make tree for it.
    721: Bad. "Flash Player - User reports problems with his current version of flash player...". It's recognize as "user reports with Flash player" :).
    821: Ok.
    921: Don't recognized. "Connect" was recognized as mistake and was excluded from "Hi NAS Admin,Please connect following groups..."
    1021: Bad. "Please see if you can fix the problem with the ip phone..." is recognized as "to fix problem using phone".
    1121: Ok, was recognized. Simple sentence, but "using" was exclused from "Using VCC proxy." as mistake.
    1221: Don't recognized. Complicated sentence: there is implicit verb.
    1321: Don't recognized. Bad sentence.
    1421: Don't recognized. "Failed" was recognized as mistake and was excluded from  "Failed LOT OrderReciever: gfgdf5"
    1521: "User needs document portal update" wasn't recognized as a sentence at all.
    1621: Bad. "user is" was recognized as mistake and was excluded from "user is not able to use the wirelsess function on his laptop."
    1721: Problem was recognized. But "change" was determined as noun in "User cannot access external sites, please change proxy settings".
    1821: Problem was recognized. But it assumes that VPN is not responding in "User is unable to access external pages when connected via VPN, IE just stops responding".


#Additional:

Sample of use RelEx:

    #!/bin/bash
    #
    # relation-extractor.sh: example relationship extractor.
    # Parses a simple sentence about dinosaurs.
    # This provides a basic demo of the RelEx abilities.
    #
    # Flags:
    # RelationExtractor [-s Sentence (in quotes)] [-h (show this help)]
    # [-t (show parse tree)] [-l (show parse links)]
    # [-o (show opencog XML output)] [-v verbose]
    # [-n parse-number] [--maxParses N] [--maxParseSeconds N]
    
    export LANG=en_US.UTF-8
    
    VM_OPTS="-Xmx1024m -Djava.library.path=/usr/lib:/usr/local/lib:/usr/lib/jni"
    
    # By default, these resources are read from the relex jar file.
    # Alternately, they are taken from the default paths, which are the
    # same as those immediate below.
    RELEX_OPTS="\
    -Drelex.algpath=data/relex-semantic-algs.txt \
    -Dwordnet.configfile=data/wordnet/file_properties.xml \
    "
    
    CLASSPATH="-classpath \
    jwnl.jar:\
    linkgrammar-4.5.5.jar:\
    relex-1.1.1.jar:\
    commons-logging.jar\
    "
    
    # Read a sentence from stdin:
    echo "Alice wrote a book about dinosaurs for the University of California in Berkeley." | \
    java $VM_OPTS $RELEX_OPTS $CLASSPATH  relex.RelationExtractor -n 4 -l -t -f
    
RelEx uses LinkGrammar notation in the tree output, which can be found [here](http://www.abisource.com/projects/link-grammar/dict/index.html)

# Comments

Have you used WordNet?

Please add statistical analysis: Precision, Recall, F-measure http://en.wikipedia.org/wiki/Recall_(information_retrieval)