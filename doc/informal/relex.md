[RelEx](http://wiki.opencog.org/w/RelEx) is an English-language semantic dependency relationship extractor. 

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