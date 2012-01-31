![Brain storm diagram](https://github.com/menta/menta-0.3/blob/master/doc/design-specification/images/inbound-representation-draft.JPG?raw=true)

h2.  Description

Divided in 4 modules.

*Workflow*

* SRC module create InformalRequest with different field and CustomAttributes which can be get directly from Request. (e.g. UserName) and create Request.
* Link Informal request to Request
TODO: Informal Request description
TODO: Request description with diagrams
* PREPROCESSING module perfroms additional checks:
** If this is generated request, skip NLP checking and load generated template
** Else run NLP to extract predicates
* NLP performs objects extraction and filled out CustomAttributes
* Translation take care on mapping to the internal format

*Custom Attributes*

Contains different custom information about request in key->value format. For using in Executor.

