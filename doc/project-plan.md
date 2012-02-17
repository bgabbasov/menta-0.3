#Menta 0.3 prototype project plan.

## Sunny day scenario.

### Project plan in CVS

```
0,"  Analysis",16/01/12,31/01/12,11,0,"","","",
1,"    Incidents",16/01/12,21/01/12,5,0,"","Renat;Adel;Alex;Artem;Bulat","",
2,"    Workbook articles",23/01/12,31/01/12,6,0,"","Renat;Adel;Alex;Artem;Bulat","",
5,"  Design Emotion Machine",23/01/12,15/03/12,38,0,"","","",
6,"    Inbound textual description",23/01/12,24/01/12,1,0,"","Alex","",
7,"    Internal knowledge(atom) representations",23/01/12,02/02/12,8,0,"","Max","",
8,"    Formalization outbound structures",02/02/12,10/02/12,6,0,"","Max","",
9,"    Design Solution HowTo-s",24/01/12,15/02/12,16,0,"","Alex","",
10,"    Design Critics",10/02/12,28/02/12,12,0,"","Max","",
11,"    Design Selector",15/02/12,02/03/12,12,0,"","Alex","",
12,"    Design Way2Think",28/02/12,15/03/12,12,0,"","Max","",
13,"  Analysis and design",15/03/12,16/03/12,1,0,"","Alex","",
15,"  OpenCog prototype",31/01/12,14/03/12,31,0,"","","",
16,"    CogBuntu",31/01/12,03/02/12,3,0,"","","",
17,"      Red documentation",31/01/12,01/02/12,1,0,"","Renat;Adel;Alex;Artem;Bulat","",
18,"      Install CogBuntu",01/02/12,03/02/12,2,0,"","Renat;Adel;Alex;Artem;Bulat","",
19,"    AtomSpace Analysis",03/02/12,06/03/12,22,0,"","Artem","",
20,"      Read documentation",03/02/12,07/02/12,2,0,"","Artem","",
21,"      Test storage using Cookbook",07/02/12,11/02/12,4,0,"","","",
22,"      Test storage usability for knowledge representation",13/02/12,06/03/12,16,0,"","","",
23,"    Probability Logic Engines analysis",03/02/12,06/03/12,22,0,"","Renat","",
24,"      PLN analysis",03/02/12,11/02/12,6,0,"","","",
25,"        Read documentation",03/02/12,07/02/12,2,0,"","","",
26,"        Test PLN using NARS data",07/02/12,11/02/12,4,0,"","","",
27,"      Bayesian inference",13/02/12,06/03/12,16,0,"","","",
28,"    Embodiment",03/02/12,14/03/12,28,0,"","Adel","",
29,"      Read documentation",03/02/12,15/02/12,8,0,"","","",
30,"      Test embodiment system to simulate Intellix",15/02/12,14/03/12,20,0,"","","",
32,"    Natural language processors",03/02/12,29/02/12,18,0,"","Bulat","",
31,"      RelEx",03/02/12,15/02/12,8,0,"","","",
33,"      Stanford Parser",15/02/12,21/02/12,4,0,"","","",
34,"      OpenNLP",21/02/12,29/02/12,6,0,"","","",
183,"  OpenCog analysis",14/03/12,15/03/12,1,0,"","","",
35,"  System Training prototype",29/02/12,23/05/12,60,0,"","","",
36,"    MOSES",29/02/12,24/03/12,18,0,"","Bulat","",
37,"    Bayesian network",06/03/12,28/03/12,16,0,"","Artem","",
38,"    Training",02/03/12,29/03/12,19,0,"","","",
39,"      Training data structures",02/03/12,29/03/12,19,0,"","","",
40,"        Incident description",02/03/12,03/03/12,1,0,"","Alex","",
41,"        Incident category",05/03/12,06/03/12,1,0,"","Alex","",
42,"        Incident formalized description",15/03/12,29/03/12,10,0,"","Max","",
44,"          Model",15/03/12,29/03/12,10,0,"","Max","",
46,"        Incident solution(Migrate HowTo approach",06/03/12,20/03/12,10,0,"","Alex","",
47,"    Create formalized description generalisation mechanism",06/03/12,27/04/12,38,0,"","","",
48,"      Create common parts selector and variable introducer",06/03/12,27/04/12,38,0,"","","",
49,"        Comparator",06/03/12,14/03/12,6,0,"","Renat","",
50,"        Recursive runner",14/03/12,24/03/12,8,0,"","Renat","",
51,"        Variable introducer",29/03/12,27/04/12,21,0,"","","",
52,"          Design variable structure",29/03/12,04/04/12,4,0,"","Max","",
53,"          Implement and test variable",04/04/12,14/04/12,8,0,"","Max","",
54,"          Named variables builder",16/04/12,26/04/12,8,0,"","Max","",
55,"          Unnamed variables builder",17/04/12,27/04/12,8,0,"","Adel","",
56,"    Incident classification algorithm",14/03/12,05/04/12,16,0,"","","",
57,"      Create test data for KnowledgeBaseAnnotator ",14/03/12,05/04/12,16,0,"","","",
58,"        Allowed Software list",14/03/12,22/03/12,6,0,"","Adel","",
59,"        Over software actions",26/03/12,30/03/12,4,0,"","Bulat","",
60,"        Software attributes",26/03/12,05/04/12,8,0,"","Renat","",
61,"        Software states",20/03/12,24/03/12,4,0,"","Alex","",
62,"    Create validation criteria inference approach",20/03/12,23/05/12,46,0,"","","",
63,"      Analyse validation criteria types",22/03/12,05/04/12,10,0,"","Adel","",
64,"      Create descriptions via predicates (logical operations)",20/03/12,07/04/12,14,0,"","Alex;Artem","",
65,"      Create validation mechanism possibly via PLN",30/03/12,17/04/12,12,0,"","","",
66,"        Design adapter",05/04/12,17/04/12,8,0,"","Adel","",
67,"        Implement adapter",30/03/12,17/04/12,12,0,"","Renat;Bulat","",
68,"      Create Solution generation prototype ",09/04/12,23/05/12,32,0,"","","",
69,"        HowTo types = 16 - 40",09/04/12,01/05/12,16,0,"","Alex","",
70,"        Solution description language = 32 - 40",09/04/12,23/05/12,32,0,"","Artem","",
71,"        Create 10 Solution descriptions = 16 - 32",17/04/12,09/05/12,16,0,"","Bulat","",
72,"        Train Solutions",17/04/12,18/05/12,23,0,"","","",
73,"          Analyse machine learning algorithms (C 4.5, Bayes network) = 16 - 24",17/04/12,09/05/12,16,0,"","Renat","",
74,"          Train 10 Solutions (in: formalised problem description, out Solution) = 16 - 24",26/04/12,18/05/12,16,0,"","Max","",
143,"  Training prototype milestone",23/05/12,24/05/12,1,0,"","","",
144,"  AIV Solution, for the specification see page.",24/05/12,13/07/12,36,0,"","","",
147,"    Auto-correct analysis should use measures: precision, recall and F-measure",29/06/12,07/07/12,6,0,"","","",
148,"      AbiWord",24/05/12,01/06/12,6,0,"","","",
149,"        Read Syntax check module documentation = 1",24/05/12,25/05/12,1,0,"","Max","",
150,"        Install AbiWord = 1 - 2",25/05/12,26/05/12,1,0,"","Max","",
151,"        Test 10 incidents descriptions = 3.5 - 4",28/05/12,01/06/12,4,0,"","Max","",
152,"      OpenOffice(LibreOffice)",24/05/12,01/06/12,6,0,"","","",
153,"        Read Auto-correct module documentation OpenOffice LibreOffice = 1",24/05/12,25/05/12,1,0,"","Alex","",
154,"        Install OpenOffice or LibreOffice = 1 - 2",25/05/12,26/05/12,1,0,"","Alex","",
155,"        Test 10 incidents descriptions = 3.5 - 4",28/05/12,01/06/12,4,0,"","Alex","",
156,"      OpenCog",24/05/12,01/06/12,6,0,"","","",
157,"        Read Auto-correct module documentation Grammatical correction = 1 - 2",24/05/12,25/05/12,1,0,"","Adel","",
158,"        Install OpenCog = 1 - 2",25/05/12,26/05/12,1,0,"","Adel","",
159,"        Test 10 incidents descriptions = 3.5 - 4",28/05/12,01/06/12,4,0,"","Adel","",
160,"      KOffice",24/05/12,01/06/12,6,0,"","","",
161,"        Read Auto-correct module documentation = 1 - 2",24/05/12,25/05/12,1,0,"","Bulat","",
162,"        Install KOffice = 1 - 4 [Could be not strait forward under Win]",25/05/12,26/05/12,1,0,"","Bulat","",
163,"        Test 10 incidents descriptions = 3.5 - 4",28/05/12,01/06/12,4,0,"","Bulat","",
165,"    KnowledgeBaseAnnotator, see specification. knowledge base integration analysis.",24/05/12,13/07/12,36,0,"","","",
166,"      WolframAlpha",24/05/12,05/07/12,30,0,"","","",
167,"        Explore API to integrate = 10 - 20 [could be not strait forward]",24/05/12,07/06/12,10,0,"","Renat","",
168,"        Test information retrieval and annotation options = 20 - 30 [could contain information not from SE domain]",07/06/12,05/07/12,20,0,"","Renat","",
169,"      TrueKnowledge",24/05/12,05/07/12,30,0,"","","",
170,"        Explore API to integrate = 10 - 20 [could be not strait forward]",24/05/12,07/06/12,10,0,"","Artem","",
171,"        Test information retrieval and annotation options = 20 - 30 [could contain information not from SE domain]",07/06/12,05/07/12,20,0,"","Artem","",
172,"      ConceptNet",01/06/12,13/07/12,30,0,"","","",
173,"        Explore API to integrate = 10 - 20 [could be not strait forward]",01/06/12,15/06/12,10,0,"","Max","",
174,"        Test information retrieval and annotation options = 20 - 30 [could contain information not from SE domain]",15/06/12,13/07/12,20,0,"","Max","",
175,"      ConceptNet5",01/06/12,13/07/12,30,0,"","","",
176,"        Explore API to integrate = 10 - 20 [could be not strait forward]",01/06/12,15/06/12,10,0,"","Alex","",
177,"        Test information retrieval and annotation options = 20 - 30 [could contain information not from SE domain]",15/06/12,13/07/12,20,0,"","Alex","",
178,"      WordNet, is integrated in ConceptNet5 but could be useful standalone",01/06/12,13/07/12,30,0,"","","",
179,"        Explore API to integrate = 10 - 20 [could be not strait forward]",01/06/12,15/06/12,10,0,"","Adel","",
180,"        Test information retrieval and annotation options = 20 - 30 [could contain information not from SE domain]",15/06/12,13/07/12,20,0,"","","",
182,"  AIV Solution",13/07/12,14/07/12,1,0,"","","",
75,"  Emotion Machine Soltion",17/07/12,05/09/12,36,0,"","","",
76,"    Prototype Critics, Way2Think, Selector",17/07/12,04/08/12,14,0,"","","",
77,"      Implement Critics",17/07/12,04/08/12,14,0,"","","",
78,"        Deliberative Critics",17/07/12,27/07/12,8,0,"","","",
79,"          Current activity goal representation = 6 - 8 [possibly should try several approaches]",17/07/12,25/07/12,6,0,"","Max","",
80,"          Current task state representation = 4 - 6 [possibly should try several representations]",17/07/12,21/07/12,4,0,"","Alex","",
81,"          Reasoning over current state with Reasoner adapter development = 8 - 10",17/07/12,27/07/12,8,0,"","Adel","",
82,"        Reflective Critic",17/07/12,25/07/12,6,0,"","","",
84,"          Develop Energy control mechanism.",17/07/12,25/07/12,6,0,"","","",
85,"            Design Energy concept = 4",17/07/12,21/07/12,4,0,"","Artem","",
86,"            Design Energy assignment mechanism during training = 2",17/07/12,19/07/12,2,0,"","Bulat","",
87,"            Implement Energy concept = 2",23/07/12,25/07/12,2,0,"","Renat","",
88,"            Implement Energy assignment mechanism = 4",19/07/12,25/07/12,4,0,"","Bulat","",
89,"        Develop Sub-goal control mechanism.",23/07/12,02/08/12,8,0,"","","",
90,"          Design sub-goal control mechanism = 4",23/07/12,27/07/12,4,0,"","Alex","",
91,"          Implement sub-goal control mechanism = 4",27/07/12,02/08/12,4,0,"","Alex","",
92,"        Develop Evidence control mechanism.",25/07/12,04/08/12,8,0,"","","",
93,"          Design Evidence control mechanism = 4 - 10 [no clear understanding of evidence control mechanism, possibly further research required]",25/07/12,31/07/12,4,0,"","Max","",
94,"          Implement Evidence control mechanism = 4 - 10",31/07/12,04/08/12,4,0,"","Max","",
97,"    Prototype Selector = 6 - 8",23/07/12,31/07/12,6,0,"","Artem","",
98,"    Prototype Way2Think",25/07/12,05/09/12,30,0,"","","",
99,"      Create base constructs(HowTo-s) = 2 - 4",25/07/12,27/07/12,2,0,"","Renat","",
107,"      Knowing How (select from KB) = 4 - 8",25/07/12,31/07/12,4,0,"","Bulat","",
108,"      Extensive Search (search in KB) = 12 - 24 [graph search could be not strait-forward]",27/07/12,14/08/12,12,0,"","Renat","",
109,"      Reasoning by Analogy = 32 - 40 [graph analogy API could be not strait forward]",31/07/12,15/08/12,11,0,"","Adel;Alex;Artem","",
110,"      Divide and Conquer",31/07/12,01/09/12,24,0,"","","",
111,"        Add analytical HowTo-s to basic set:",31/07/12,10/08/12,8,0,"","","",
112,"          Wrong software was installed = 4",06/08/12,10/08/12,4,0,"","Max","",
113,"          Two direct instructions in one incident description = 4",31/07/12,04/08/12,4,0,"","Bulat","",
114,"        Add Interpretation mechanism over current state of the system",06/08/12,01/09/12,20,0,"","","",
115,"          Variable and current state addressing = 12 - 16",06/08/12,22/08/12,12,0,"","Bulat","",
116,"          Logical operation execution = 16",10/08/12,01/09/12,16,0,"","Max","",
129,"      Simulation (build the model based on inbound information) =",14/08/12,05/09/12,16,0,"","","",
130,"        Search for concept in the KB. = 16",14/08/12,05/09/12,16,0,"","Renat","",
131,"        Search for properties in KB. = 4",15/08/12,21/08/12,4,0,"","Artem","",
132,"        Create connections of found concepts. = 2",15/08/12,17/08/12,2,0,"","Alex","",
133,"        Support context. = 2",22/08/12,24/08/12,2,0,"","Bulat","",
140,"    Test main perceiving workflow",24/08/12,31/08/12,5,0,"","","",
142,"      Prototype Main Workflow. = 10 - 14 [some not well tested bugs could slow down the development]{Models, Critics, Way2Think ready to use}",24/08/12,31/08/12,5,0,"","Alex;Bulat","",
181,"  Emotion machine solution",05/09/12,06/09/12,1,0,"","","",
```

![Menta 0.3 research project plan](https://github.com/menta/menta-0.3/raw/master/doc/informal/gantt/research.png)

### Main milestones:

 1. Analysis and design 15/03/12
 1. OpenCog analysis 14/03/12
 1. Training prototype 23/05/12
 1. AIV prototype 13/07/12
 1. Emotion machine prototype 05/09/12

## Rainy day scenario.

![Menta 0.3 research project plan rainy day](https://github.com/menta/menta-0.3/raw/master/doc/informal/gantt/research-pessimistic.png)

### Main milestones:

 1. Analysis and design 23/03/12
 1. OpenCog analysis 25/07/12
 1. Training prototype 21/05/13
 1. AIV prototype 03/12/13
 1. Emotion machine prototype 08/05/14

