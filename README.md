# CSA: Farm to Consumer

This project's goal is to create an easy interface through which Community Supported Agriculture (CSA) consumers in the PNW area can be recommended a CSA farm which meets their needs. This project plays with different ML models to predict the best CSA farm for a consumer based on their desired attributes such as price, pickup location, and desired produce. Then based on the model results, the best one is used in a Flask application to suggest a CSA farm based on user inputs into a form.

### Current State
Currently, the Flask app has been created but is not hosted anywhere. At the moment the data set consists of 90 data points which results in fairly high accuracy (~93% using the KNN model). In the future, more data would be useful and more than 10 farms could be included in the data set. The results page could also be improved to provide a detailed description and contact information for the suggested farm. Also as the data set is improved, the model used could switch from the KNN model to the MLP Regressor model.
