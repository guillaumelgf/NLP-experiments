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
    - [X] Basic
    - [ ] A/B Testing models
    - [ ] Load new models
  
#### Logs:
- [20/01/2021]: First quick model
  - Convert data from json to csv
  - Implementation of quick feature Engineering (bag of word)
  - DecisionTreeModel not tuned
  - First evaluation
  
BUG: Vocabulary list needs to be made before splitting

### How to make it work ?

#### Installing
```
git clone https://github.com/guillaumelgf/NLP-for-fun.git
cd NLP-for-fun
pip -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
#### Training
```
python train.py
```
#### Starting flask app
```
set FLASK_APP=flask_app.py
set FLASK_ENV=devlopment
flask run
```
Then go to localhost:5000