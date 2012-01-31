
![Brain storm diagram](https://github.com/menta/menta-0.3/blob/master/doc/design-specification/images/inbound-representation-draft.JPG?raw=true)

Divided in 4 modules. SRC - source request. Preprocessing perform additional operation on inbound information. NLP translate to objects. Translator bound to internal objects info.
SRC module create InformalRequest with different field and CustomAttributes - custom defined fields (special structure for non-hardcoded additional info for solution execution,
such as machine name e.t.c ,actually this will be populated from inbound text, but some time it possible to collect this information from request data)
