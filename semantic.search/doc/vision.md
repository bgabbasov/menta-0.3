# Semantic documents analysis/search vision.

Main concept of semantic analysis/search is cloud of trees.
*Cloud of trees* is used to describe searchable documents based on found terms and ontologies used to describe domains (ex.: Wikipedia in RDF, ConceptNet, WordNet?, Open CYC and so on). *Cloud of trees* is also used as intermediate representation of a user search request. An response document list is created based on relevance of the request to document. Request *cloud of trees* is infered as the result of an analysis of request triplets.

There are several use cases automated via approach described above:

1. Analysis

 1. Request analysis:
Request is treated as virtual domain described as *cloud of trees*: system creates the list of documents references based on relevance to the virtual domain. User selecting the documents specifies additional descriptions to the request virtual domain.
 
 1. Domain analysis:
Damain name is treated as minimal decription, an extra criterias are infered via domain *cloud of trees* constructed based on ecyclopedical sources. System stores links of the virtual domain description and responces selected by user.

 1. User checks the result of his/her experiments
System searches for analogies of result set and checks it's confidence.  

 1.User analyse the problem
System searches for the previously described solutions, analogies of the problem.

 1. User analyses an article of another author 
User submits an article into the system. System crates semantic description of the article and searches for analogical articles.
 
1. Search 
 1. User creates an article
  1. System searches for the most recent and most interesting articles of the created article domain.
  1. System creates the extracts of newest and most rated articles.

 1. User searches for unknown term
 System searches for the documents that contains term first in their description cloud, then in their nearest neighbor terms, then in full text.

 1. User analyses domain.
 System generates recommended list of references to start exploration of the domain staring from most simple and most trusted sources.
