# Semantic documents analysis/search vision.

Main concept of semantic analysis/search is cloud of trees.
*Cloud of trees* is used to describe searchable documents based on found terms and ontologies used to describe domains (ex.: Wikipedia in RDF, ConceptNet, WordNet?, Open CYC and so on). *Cloud of trees* is also used as intermediate representation of a user search request. An response document list is created based on relevance of the request to document. Request *cloud of trees* is infered as the result of an analysis of request triplets.

There are several use cases automated via approach described above:

## Analysis:

 1. Request analysis: Request is treated as virtual domain described as *cloud of trees*: system creates the list of documents references based on relevance to the virtual domain. User selecting the documents specifies additional descriptions to the request virtual domain.
 
 1. Domain analysis: damain name is treated as minimal description, an extra criterias are infered via domain *cloud of trees* constructed based on encyclopedical sources. System generates recommended list of references to start exploration of the domain staring from most simple and most trusted sources. System stores links of the virtual domain description and responses selected by user.
 
   2.	Генерация возможных доменов. Virtual domain could be created by the system via clastering. Virtual domains could be useful for further analysis and personalisation.
   2.	Генерация новых тем исследования
   2.	Кластеризация связей вопрос-ответ из разных доменов
   2.	Анализ текущих трендов и построение графиков
   2.	Генерация экстраполяции текущего тренда на будущее
   2.	Генерация «анти трендов»
   2.	Генерация гипотез
   2.	Использование обратной связи с пользователем для ускорения процесса генерации результатов поиска
   2.	Использование обобщения запрос-результат
 
 1. User checks the result of his/her experiments: System searches for analogies of result set and checks it's confidence.
   
 1. User analyse the problem: System searches for the previously described solutions, analogies of the problem.
  2.	Анализ абсурдности
  2.	Генерация основного тезиса из документа
  2.	Генерация рефератов
  2.	Генерация методических пособий
  2.	Генерация новых концепций (на основе данных из другого домена)
 
 1. User analyses an article of another author: User submits an article into the system. System crates semantic description of the article and searches for analogical articles.
 
## Search:
 
 1. User creates an article
   2. System searches for the most recent and most interesting articles of the created article domain.
   2. System creates the extracts of newest and most rated articles.

 1. User searches for unknown term: System searches for the documents that contains term first in their description cloud, then in their nearest neighbor terms, then in full text.
 
   2.	*Search types:*
      *	Семантический
      *	Поиск по тегам (термины)
      *	Полнотекстный
      *	Доп фильтрация (поиск в результатах)
         -	доменный (будут предлагаться близкие домены)
         -	тип документа
         -	язык
         -	автор
         
      *	Доп фичи
         -	Предложение информации из смежных доменов 
         -	Граф термов
         -	Поиск людей занимающихся этим
         -	Поиск людей, которые тоже это искали
         -	Подписка на новые результаты запроса (информация появляющаяся в будущем, отправка результата на почту)
 
   2. *Helpers:*
     *	Модуль помощи пользователю при составлении запросов к системе
     *	Подсказывание «Возможно вы имели ввиду»
     *	Запросы формата «Что если?»
 
 1. User searches for domain: System search for the domain terms and terms of nearest domains.
