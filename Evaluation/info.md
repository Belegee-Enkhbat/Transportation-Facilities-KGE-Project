This section aims at describing the evaluation performed at the end of the whole process (producer plus consumer) over the final outcome of the iTelos methodology. The criteria, described below, consider both the Knowledge and Data Layer.
The iTelos methodology provides a set of metrics to be used for the above evaluations. Between them one of the most useful is Coverage which describes how much a portion of knowledge is covered by a KG. The Coverage is used as follows, to evaluate the Knowledge Layer for two different objectives:


1. Primary objective based on the purpose satisfaction (Teleontology vs CQs): it is based on how much the final KG is able to satisfy the Competency Queries. So, this means how much the teleontolgy covers the entities and properties extracted from the CQs;

2. Second objective based on the reusability (Teleontology vs Reference Ontologies): how much the teleontology covers the etypes, and properties, extracted from the reference ontologies.

9.1.1 Teleontology

In the table below, there is a summary that takes into account the total number of etypes, object properties, and data properties, used for the calculation of the coverage

ETypes = 7
Object properties = 7
Data properties = 17

9.1.2 Teleontology vs CQs

Considering the table 2, and the Competency Questions 4.3, in reference to the final values obtained from the Teleontology’s table 13, the coverage of the etypes, object properties, and data properties is calculated as follows. For example, for the etype, given a set of (CQE), the etype coverage (CovE) of the Teleontology (T) is:

where CQE is the number of etypes extracted from the CQs, and TE is the number of etypes of the Teleontology.


table Teleontology vs Competency Questions Coverage

This table shows that for each criteria, the final Teleontology defines more etypes, data and object properties. This is due to the fact that during the initial phases of this project, the specific knowledge design choices and needs were not complete. They have been refined during the development of the project which lead to defining a better and complete knowledge structure to fulfil the purpose.

9.1.3 Teleontology vs Reference Ontologies

Considering the used ontologies (table 10), in reference to the final values obtained from the Teleontology’s table 13, the coverage of the etypes (CovE), object properties (CovOP ), and data properties (CovDP ) is calculated as follows. For example, for the etype, given a set of (RO), the etype coverage (CovE) of the Teleontology (T) is:

CovE(ROE) = |ROE ∩ TE|/|ROE|

 where ROE is the number of etypes extracted from the ROs, and TE is the number of etypes of the Teleontology. Below, there is a table with the final evaluation, considering the etypes, object properties, and data properties coverage.

 9.2 Data Layer Evaluations

 The Data Layer Evaluations is made only for the primary objective which is based on the purpose satisfaction and it aims to understand how the KG is dense and connected. The KG’s connectivity is evaluated in two different moments: 
 
 • on the final KG, to understand how much the KG is connected at the end of the process; 
 • during the KG’s construction, to understand how much each single dataset improves the connectivity of the final KG. 
 The connectivity of a KG can be evaluated over two dimensions: 
 
 1. entity connectivity which evaluates the grades of connection between the different entities in the KG; 
 
 2. property connectivity which evaluates the grades of connection between each single KG’s entity and its properties values. 
 
 The entity and property connectivity can be calculated by using the connectivity matrix, as represented in the table below.