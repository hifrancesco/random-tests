# [Create a classification model with Azure Machine Learning designer](https://learn.microsoft.com/en-gb/training/modules/create-classification-model-azure-machine-learning-designer/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/create-classification-model-azure-machine-learning-designer/introduction)

Classification is an example of a supervised machine learning technique in which you train a model using data that includes both the features and known values for the label, so that the model learns to fit the feature combinations to the label. Then, after training has been completed, you can use the trained model to predict labels for new items for which the label is unknown.

You can use Microsoft Azure Machine Learning designer to create classification models by using a drag and drop visual interface, without needing to write any code.

In this module, you'll learn how to:

- Identify classification machine learning scenarios.
- Use Azure Machine Learning designer to train a classification model.
- Use a classification model for inferencing.
- Deploy and test a classification model.

## [Identify classification machine learning scenarios](https://learn.microsoft.com/en-gb/training/modules/create-classification-model-azure-machine-learning-designer/classification-scenarios)

*Classification* is a form of machine learning that is used to predict which category, or *class*, an item belongs to. This machine learning technique can be applied to binary and multi-class scenarios. For example, a health clinic might use the characteristics of a patient (such as age, weight, blood pressure, and so on) to predict whether the patient is at risk of diabetes. In this case, the characteristics of the patient are the *features*, and the *label* is a binary classification of either 0 or 1, representing non-diabetic or diabetic.

Like regression, classification is an example of a *supervised* machine learning technique in which you train a model using data that includes both the features and known values for the label, so that the model learns to *fit* the feature combinations to the label. Then, after training has been completed, you can use the trained model to predict labels for new items for which the label is unknown.

### Scenarios for classification machine learning models

Classification machine learning models are used in many industries. A few scenarios are:

- Using clinical data to predict whether a patient will become sick or not.
- Using historical data to predict whether text sentiment is positive, negative, or neutral.
- Using characteristics of small businesses to predict if a new venture will succeed.

## [What is Azure Machine Learning?](https://learn.microsoft.com/en-gb/training/modules/create-classification-model-azure-machine-learning-designer/what-is-azure-machine-learning)

Training and deploying an effective machine learning model involves a lot of work, much of it time-consuming and resource-intensive. Azure Machine Learning is a cloud-based service that helps simplify some of the tasks it takes to prepare data, train a model, and deploy a predictive service. Regression machine learning models can be built using Azure Machine Learning.

Most importantly, Azure Machine Learning helps data scientists increase their efficiency by automating many of the time-consuming tasks associated with training models. It enables them to use cloud-based compute resources that scale effectively to handle large volumes of data while incurring costs only when actually used.

### Azure Machine Learning workspace

To use Azure Machine Learning, you first create a workspace resource in your Azure subscription. You can then use this workspace to manage data, compute resources, code, models, and other artifacts related to your machine learning workloads.

After you have created an Azure Machine Learning workspace, you can develop solutions with the Azure machine learning service either with developer tools or the Azure Machine Learning studio web portal.

### Azure Machine Learning studio

Azure Machine Learning studio is a web portal for machine learning solutions in Azure. It includes a wide range of features and capabilities that help data scientists prepare data, train models, publish predictive services, and monitor their usage. To begin using the web portal, you need to assign the workspace you created in the Azure portal to Azure Machine Learning studio.

### Azure Machine Learning compute

At its core, Azure Machine Learning is a service for training and managing machine learning models, for which you need compute resources on which to run the training process. Compute targets are cloud-based resources on which you can run model training and data exploration processes.

In Azure Machine Learning studio, you can manage the compute targets for your data science activities. There are four kinds of compute resource you can create:

- Compute Instances: Development workstations that data scientists can use to work with data and models.
- Compute Clusters: Scalable clusters of virtual machines for on-demand processing of experiment code.
- Inference Clusters: Deployment targets for predictive services that use your trained models.
- Attached Compute: Links to existing Azure compute resources, such as Virtual Machines or Azure Databricks clusters.

## [What is Azure Machine Learning designer?](https://learn.microsoft.com/en-gb/training/modules/create-classification-model-azure-machine-learning-designer/what-is-azure-designer)

In Azure Machine Learning studio, there are several ways to author regression machine learning models. One way is to use a visual interface called designer that you can use to train, test, and deploy machine learning models. The drag-and-drop interface makes use of clearly defined inputs and outputs that can be shared, reused, and version controlled.

Each designer project, known as a pipeline, has a left panel for navigation and a canvas on your right hand side. To use designer, identify the building blocks, or components, needed for your model, place and connect them on your canvas, and run a machine learning job.

### Pipelines

Pipelines let you organize, manage, and reuse complex machine learning workflows across projects and users. A pipeline starts with the dataset from which you want to train the model. Each time you run a pipeline, the configuration of the pipeline and its results are stored in your workspace as a pipeline job.

### Components

An Azure Machine Learning component encapsulates one step in a machine learning pipeline. You can think of a component as a programming function and as a building block for Azure Machine Learning pipelines. In a pipeline project, you can access data assets and components from the left panel's Asset Library tab.

### Datasets

You can create data assets on the Data page from local files, a datastore, web files, and Open Datasets. These data assets will appear along with standard sample datasets in designer's Asset Library. 

### Azure Machine Learning Jobs

An Azure Machine Learning (ML) job executes a task against a specified compute target. Jobs enable systematic tracking for your machine learning experimentation and workflows. Once a job is created, Azure ML maintains a run record for the job. All of your jobs' run records can be viewed in Azure ML studio.

## [Understand steps for classification](https://learn.microsoft.com/en-gb/training/modules/create-classification-model-azure-machine-learning-designer/classification-steps)

You can think of the steps to train and evaluate a classification machine learning model as:

- Prepare data: Identify the features and label in a dataset. Pre-process, or clean and transform, the data as needed.
- Train model: Split the data into two groups, a training and a validation set. Train a machine learning model using the training data set. Test the machine learning model for performance using the validation data set.
- Evaluate performance: Compare how close the model's predictions are to the known labels.
- Deploy a predictive service: After you train a machine learning model, you need to convert the training pipeline into a real-time inference pipeline. Then you can deploy the model as an application on a server or device so that others can use it.

### Prepare data

Azure machine learning designer has several pre-built components that can be used to prepare data for training. These components enable you to clean data, normalize features, join tables, and more. 

### Train model

To train a classification model, you need a dataset that includes historical *features*, characteristics of the entity for which you want to make a prediction, and known *label* values. The label is the class indicator you want to train a model to predict.

It's common practice to train the model using a subset of the data, while holding back some data with which to test the trained model. This enables you to compare the labels that the model predicts with the actual known labels in the original dataset.

You will use *designer*'s **Score Model** component to generate the predicted class label value. Once you connect all the components, you will want to run an experiment, which will use the data asset on the canvas to train and score a model.

### Evaluate performance

After training a model, it is important to evaluate its performance. There are many performance metrics and methodologies for evaluating how well a model makes predictions. You can review evaluation metrics on the completed job page by right-clicking on the Evaluate model component.

#### Confusion matrix

The confusion matrix is a tool used to assess the quality of a classification model's predictions. It compares predicted labels against actual labels.

In a binary classification model where you're predicting one of two possible values, the confusion matrix is a 2x2 grid showing the predicted and actual value counts for classes **1** and **0**. It categorizes the model's results into four types of outcomes. Using our diabetes example these outcomes can look like:

- *True Positive*: The model predicts the patient has diabetes, and the patient does actually have diabetes.
- *False Positive*: The model predicts the patient has diabetes, but the patient does not actually have diabetes.
- *False Negative*: The model predicts the patient does not have diabetes, but the patient actually does have diabetes.
- *True Negative*: The model predicts the patient does not have diabetes, and the patient actually does not have diabetes.

Suppose you have data for 100 patients. You create a model that predicts a patient does not have diabetes 15% of the time, so it *predicts* 15 people have diabetes and predicts 85 people do not have diabetes. In actuality, suppose 25 people actually do have diabetes and 75 people actually do not have diabetes. This information can be presented in a confusion matrix such as the one below:

For a multi-class classification model (where there are more than two possible classes), the same approach is used to tabulate each possible combination of actual and predicted value counts - so a model with three possible classes would result in a 3x3 matrix with a diagonal line of cells where the predicted and actual labels match.

Metrics that can be derived from the confusion matrix include:

- **Accuracy**: The number of correct predictions (true positives + true negatives) divided by the total number of predictions.
- **Precision**: The number of the cases classified as positive that are actually positive: the number of true positives divided by (the number of true positives plus false positives).
- **Recall**: The fraction of positive cases correctly identified: the number of true positives divided by (the number of true positives plus false negatives).
- **F1 Score**: An overall metric that essentially combines precision and recall.

Of these metric, accuracy may be the most intuitive. However, you need to be careful about using accuracy as a measurement of how well a model performs. Using the model that predicts 15% of patients have diabetes, when actually 25% of patients have diabetes, we can calculate the following metrics:

The *accuracy* of the model is: (10+70)/ 100 = 80%.

The *precision* of the model is: 10/(10+5) = 67%.

The *recall* of the model is 10/(10+15) = 40%

#### Choosing a threshold

A classification model predicts the probability for each possible class. In other words, the model calculates a likelihood for each predicted label. In the case of a binary classification model, the predicted probability is a value between 0 and 1. By default, a predicted probability *including* or above 0.5 results in a class prediction of 1, while a prediction below this threshold means that there's a greater probability of a negative prediction (remember that the probabilities for all classes add up to 1), so the predicted class would be 0.

Designer has a useful *threshold* slider for reviewing how the model performance would change depending on the set threshold.

#### ROC curve and AUC metric

Another term for *recall* is **True positive rate**, and it has a corresponding metric named **False positive rate**, which measures the number of negative cases incorrectly identified as positive compared the number of actual negative cases. Plotting these metrics against each other for every possible threshold value between 0 and 1 results in a curve, known as the **ROC curve** (ROC stands for *receiver operating characteristic*, but most data scientists just call it a ROC curve). In an ideal model, the curve would go all the way up the left side and across the top, so that it covers the full area of the chart. The larger the *area under the curve*, of **AUC** metric, (which can be any value from 0 to 1), the better the model is performing. You can review the ROC curve in **Evaluation Results**.

### Deploy a predictive service

You have the ability to deploy a service that can be used in real-time. In order to automate your model into a service that makes continuous predictions, you need to create and deploy an inference pipeline.

#### Inference pipeline

To deploy your pipeline, you must first convert the training pipeline into a real-time inference pipeline. This process removes training components and adds web service inputs and outputs to handle requests.

The inference pipeline performs the same data transformations as the first pipeline for new data. Then it uses the trained model to *infer*, or predict, label values based on its features. This model will form the basis for a predictive service that you can publish for applications to use.

You can create an inference pipeline by selecting the menu above a completed job.

#### Deployment

After creating the inference pipeline, you can deploy it as an endpoint. In the endpoints page, you can view deployment details, test your pipeline service with sample data, and find credentials to connect your pipeline service to a client application.

It will take a while for your endpoint to be deployed. The Deployment state on the **Details** tab will indicate Healthy when deployment is successful.

On the **Test** tab, you can test your deployed service with sample data in a JSON format. The test tab is a tool you can use to quickly check to see if your model is behaving as expected. Typically it is helpful to test the service before connecting it to an application.

You can find credentials for your service on the **Consume** tab. These credentials are used to connect your trained machine learning model as a service to a client application.

## [Exercise - Explore classification with Azure Machine Learning designer](https://learn.microsoft.com/en-gb/training/modules/create-classification-model-azure-machine-learning-designer/exercise)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/create-classification-model-azure-machine-learning-designer/knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/create-classification-model-azure-machine-learning-designer/summary)