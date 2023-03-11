# [Create a regression model with Azure Machine Learning designer](https://learn.microsoft.com/en-gb/training/modules/create-regression-model-azure-machine-learning-designer/]

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/create-regression-model-azure-machine-learning-designer/1-introduction)

You can use Microsoft Azure Machine Learning designer to create regression models by using a drag and drop visual interface, without needing to write any code.

In this module, you'll learn how to:

- Identify regression machine learning scenarios.
- Use Azure Machine Learning designer to train a regression model.
- Use a regression model for inferencing.
- Deploy a regression model as a service.

## [Identify regression machine learning scenarios](https://learn.microsoft.com/en-gb/training/modules/create-regression-model-azure-machine-learning-designer/2-regression-scenarios)

Regression is a form of machine learning used to understand the relationships between variables to predict a desired outcome. Regression predicts a numeric *label* or outcome based on variables, or *features*. For example, an automobile sales company might use the characteristics of a car (such as engine size, number of seats, mileage, and so on) to predict its likely selling price. In this case, the characteristics of the car are the features, and the selling price is the label.

Regression is an example of a *supervised* machine learning technique in which you train a model using data that includes both the features and known values for the label, so that the model learns to *fit* the feature combinations to the label. Then, after training has been completed, you can use the trained model to predict labels for new items for which the label is unknown.

### Scenarios for regression machine learning models

Regression machine learning models are used in many industries. A few scenarios are:

- Using characteristics of houses, such as square footage and number of rooms, to predict home prices.
- Using characteristics of farm conditions, such as weather and soil quality, to predict crop yield.
- Using characteristics of a past campaign, such as advertising logs, to predict future advertisement clicks.

## [What is Azure Machine Learning?](https://learn.microsoft.com/en-gb/training/modules/create-regression-model-azure-machine-learning-designer/3-what-is-azure-machine-learning)

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

## [What is Azure Machine Learning designer?](https://learn.microsoft.com/en-gb/training/modules/create-regression-model-azure-machine-learning-designer/4-what-is-azure-designer)

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

## [Understand steps for regression](https://learn.microsoft.com/en-gb/training/modules/create-regression-model-azure-machine-learning-designer/5-regression-steps)

You can think of the steps to train and evaluate a regression machine learning model as:

- Prepare data: Identify the features and label in a dataset. Pre-process, or clean and transform, the data as needed.
- Train model: Split the data into two groups, a training and a validation set. Train a machine learning model using the training data set. Test the machine learning model for performance using the validation data set.
- Evaluate performance: Compare how close the model's predictions are to the known labels.
- Deploy a predictive service: After you train a machine learning model, you need to convert the training pipeline into a real-time inference pipeline. Then you can deploy the model as an application on a server or device so that others can use it.

### Prepare data

Azure machine learning designer has several pre-built components that can be used to prepare data for training. These components enable you to clean data, normalize features, join tables, and more.

### Train model

To train a regression model, you need a dataset that includes historical *features*, characteristics of the entity for which you want to make a prediction, and known *label* values. The label is the quantity you want to train a model to predict.

It's common practice to train the model using a subset of the data, while holding back some data with which to test the trained model. This enables you to compare the labels that the model predicts with the actual known labels in the original dataset.

You will use *designer*'s Score Model component to generate the predicted class label value. Once you connect all the components, you will want to run an experiment, which will use the data asset on the canvas to train and score a model.

### Evaluate performance

After training a model, it is important to evaluate its performance. There are many performance metrics and methodologies for evaluating how well a model makes predictions. You can review evaluation metrics on the completed job page by right-clicking on the Evaluate model component.

- **Mean Absolute Error** (MAE): The average difference between predicted values and true values. This value is based on the same units as the label, in this case dollars. The lower this value is, the better the model is predicting.
- **Root Mean Squared Error** (RMSE): The square root of the mean squared difference between predicted and true values. The result is a metric based on the same unit as the label (dollars). When compared to the MAE (above), a larger difference indicates greater variance in the individual errors (for example, with some errors being very small, while others are large).
 - **Relative Squared Error** (RSE): A relative metric between 0 and 1 based on the square of the differences between predicted and true values. The closer to 0 this metric is, the better the model is performing. Because this metric is relative, it can be used to compare models where the labels are in different units.
- **Relative Absolute Error** (RAE): A relative metric between 0 and 1 based on the absolute differences between predicted and true values. The closer to 0 this metric is, the better the model is performing. Like RSE, this metric can be used to compare models where the labels are in different units.
- **Coefficient of Determination** (R2): This metric is more commonly referred to as R-Squared, and summarizes how much of the variance between predicted and true values is explained by the model. The closer to 1 this value is, the better the model is performing.

### Deploy a predictive service

You have the ability to deploy a service that can be used in real-time. In order to automate your model into a service that makes continuous predictions, you need to create and deploy an inference pipeline.

#### Inference pipeline

To deploy your pipeline, you must first convert the training pipeline into a real-time inference pipeline. This process removes training components and adds web service inputs and outputs to handle requests.

The inference pipeline performs the same data transformations as the first pipeline for *new* data. Then it uses the trained model to *infer*, or predict, label values based on its features. This model will form the basis for a predictive service that you can publish for applications to use.

#### Deployment

After creating the inference pipeline, you can deploy it as an endpoint. In the endpoints page, you can view deployment details, test your pipeline service with sample data, and find credentials to connect your pipeline service to a client application.

It will take a while for your endpoint to be deployed. The Deployment state on the **Details** tab will indicate *Healthy* when deployment is successful.

On the **Test** tab, you can test your deployed service with sample data in a JSON format. The test tab is a tool you can use to quickly check to see if your model is behaving as expected. Typically it is helpful to test the service before connecting it to an application.

You can find credentials for your service on the **Consume** tab. These credentials are used to connect your trained machine learning model as a service to a client application.

## [Exercise - Explore regression with Azure Machine Learning designer](https://learn.microsoft.com/en-gb/training/modules/create-regression-model-azure-machine-learning-designer/6-exercise)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/create-regression-model-azure-machine-learning-designer/7-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/create-regression-model-azure-machine-learning-designer/8-summary)