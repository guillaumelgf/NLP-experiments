# NLP-for-fun
Simple NLP project

#### To Do:
- [X] Extract data from [Kaggle](https://www.kaggle.com/rmisra/news-category-dataset)
- [X] Use python script 1_json_to_csv_dataset to convert json to csv readable by pandas
- [ ] Create ML Model to predict article category from title
    - [ ] Remove stop words (NLTK)
    - [ ] Stemming (NLTK)
    - [ ] Bag of words
    - [ ] Random Forest (scikit-learn)
- [ ] Serving (Flask)
    - [ ] Basic
    - [ ] A/B Testing models
    - [ ] Load new models
  
#### Logs:
- [20/01/2021]: First quick model
  - Convert data from json to csv
  - Implementation of quick feature Engineering (bag of word)
  - DecisionTreeModel not tuned
  - First evaluation
  
BUG: Vocabulary list needs to be made before splitting

