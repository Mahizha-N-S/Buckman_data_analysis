# **Investment Decision Recommendation System Project**

We were provided with a data set containing information about individuals and their investment behavior.
The task is to build a recommendation system that can predict the best investment decision for new data based on various factors available in the dataset.

Detail Flow of my Findings and Approach is in the Presentation. ->Hope you look through that.


## 1.Data Exploration:

Data Cleaning and Understanding:
* Check for null values
* And to make it understandable , i have converted it to integral values
* Catgorical Values to numerical
* 
![image](https://github.com/Mahizha-N-S/Buckman_data_analysis/assets/102713447/3a433ab0-860a-429c-85da-7130f6cbfd54)

## 2.Best Investment Decision Identification:8 

* To choose the best features used Chi Square Test

![image](https://github.com/Mahizha-N-S/Buckman_data_analysis/assets/102713447/c3b20607-3f48-4ed0-85b8-ebaaac23da35)

* Determine which demographic, employment, and behavioral characteristics correlate with 
successful investment outcomes. : Correlation model is constructed

![image](https://github.com/Mahizha-N-S/Buckman_data_analysis/assets/102713447/aba08608-d101-41e5-889e-fda0ba1df3fe)

## 3.Recommendation System Development:
* Initially while reading the data set , i thought the main objective was to make the client get maximum profit , and used “Returns Earned” feature as the target variable.
* But on re analysing the data set and the problem statement, the main outcome is the recommendation system , so I have kept the Amount to invest as needed and , given the clients behaviour as my recommended value.
* “Percentage to Investment” as the target value, and proceeded my findings based on that.

  MODEL:
  * Have Build and trained for all the models
      + Random Forest
      + Decision Tree
      + Neural Networks
  * And choosed the model with best score
    ![image](https://github.com/Mahizha-N-S/Buckman_data_analysis/assets/102713447/b88d7698-0504-4d09-abb9-21ad92ad684a)
![image](https://github.com/Mahizha-N-S/Buckman_data_analysis/assets/102713447/7088b275-17f0-41ba-ae30-56509fb6c8f8)

## Model is trained and tested -> i have dumped the model which can be used for future use
```
 #Assuming rf_clf is your trained Random Forest model
dump(rf_clf, 'random_forest_model.joblib')

# Load the saved Random Forest model
loaded_rf_clf = load('random_forest_model.joblib')
```

## 4.Implementation:
* With the help of flask , i have created a user template which extracts user information and gives them the best recommendation percentage that they can invest
* **Clone the repository and run app.py**
  ![image](https://github.com/Mahizha-N-S/Buckman_data_analysis/assets/102713447/28360fa0-5493-4954-99b0-c2904c1cb928)


## 5. Usage of PowerBI to create a visual dashboard
![image](https://github.com/Mahizha-N-S/Buckman_data_analysis/assets/102713447/eb850346-7e59-461a-8bac-abe0fa114490)
![image](https://github.com/Mahizha-N-S/Buckman_data_analysis/assets/102713447/a806430d-708f-42cc-a1ec-ac2f7867f302)

## 6.Conclusion
**After analyzing the data and reviewing the results from the recommendation system, several insights and recommendations stand out to improve investment decisions:**

* **Knowledge is Power:** Individuals with a deeper understanding of the stock market and various investment products tend to make more informed decisions. It's crucial to educate investors about these aspects.
* **Income Matters:** Household income plays a pivotal role in investment decisions. Higher-income individuals often have more disposable income, allowing them to take on riskier investments.  
* **Enhancing the Recommendation System:**
    +To improve the system, consider adding more features that influence investment choices, such as investment goals, risk tolerance, and current market conditions.
    + Utilizing more advanced machine learning models and techniques could also enhance the system's accuracy and effectiveness.

* Future research could focus on integrating real-time market data and economic indicators into the recommendation system for more current and precise investment advice











