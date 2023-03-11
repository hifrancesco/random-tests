# [Use Automated Machine Learning in Azure Machine Learning](https://learn.microsoft.com/en-gb/training/modules/use-automated-machine-learning/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/use-automated-machine-learning/1-introduction)

Machine Learning is the foundation for most artificial intelligence solutions. Creating an intelligent solution often begins with the use of machine learning to train predictive models using historic data that you have collected.

Azure Machine Learning is a cloud service that you can use to train and manage machine learning models.

In this module, you'll learn to:

- Identify the machine learning process.
- Understand Azure Machine Learning capabilities.
- Use automated machine learning in Azure Machine Learning studio to train and deploy a predictive model.

## [What is machine learning?](https://learn.microsoft.com/en-gb/training/modules/use-automated-machine-learning/2-what-is-ml)

Machine learning is a technique that uses mathematics and statistics to create a model that can predict unknown values.

For example, suppose Adventure Works Cycles is a business that rents cycles in a city. The business could use historic data to train a model that predicts daily rental demand in order to make sure sufficient staff and cycles are available.

To do this, Adventure Works could create a machine learning model that takes information about a specific day (the day of week, the anticipated weather conditions, and so on) as an input, and predicts the expected number of rentals as an output.

### Types of machine learning

There are two general approaches to machine learning, supervised and unsupervised machine learning. In both approaches, you train a model to make predictions.

The supervised machine learning approach requires you to start with a dataset with known label values. Two types of supervised machine learning tasks include regression and classification.

- Regression: used to predict a continuous value; like a price, a sales total, or some other measure.
- Classification: used to determine a class label; an example of a binary class label is whether a patient has diabetes or not; an example of multi-class labels is classifying text as positive, negative, or neutral.

The unsupervised machine learning approach starts with a dataset without known label values. One type of unsupervised machine learning task is clustering.

- Clustering: used to determine labels by grouping similar information into label groups; like grouping measurements from birds into species.

## [What is Azure Machine Learning studio?](https://learn.microsoft.com/en-gb/training/modules/use-automated-machine-learning/3-what-is-azure-machine-learning-studio)

Training and deploying an effective machine learning model involves a lot of work, much of it time-consuming and resource-intensive. Azure Machine Learning is a cloud-based service that helps simplify some of the tasks it takes to prepare data, train a model, and deploy a predictive service.

Most importantly, Azure Machine Learning helps data scientists increase their efficiency by automating many of the time-consuming tasks associated with training models; and it enables them to use cloud-based compute resources that scale effectively to handle large volumes of data while incurring costs only when actually used.

### Azure Machine Learning workspace

To use Azure Machine Learning, you first create a workspace resource in your Azure subscription. You can then use this workspace to manage data, compute resources, code, models, and other artifacts related to your machine learning workloads.

After you have created an Azure Machine Learning workspace, you can develop solutions with the Azure machine learning service either with developer tools or the Azure Machine Learning studio web portal.

### Azure Machine Learning studio

Azure Machine Learning studio is a web portal for machine learning solutions in Azure. It includes a wide range of features and capabilities that help data scientists prepare data, train models, publish predictive services, and monitor their usage. To begin using the web portal, you need to assign the workspace you created in the Azure portal to Azure Machine Learning studio

### Azure Machine Learning compute

At its core, Azure Machine Learning is a service for training and managing machine learning models, for which you need compute on which to run the training process.

Compute targets are cloud-based resources on which you can run model training and data exploration processes.

In [Azure Machine Learning studio](https://ml.azure.com/), you can manage the compute targets for your data science activities. There are four kinds of compute resource you can create:

- Compute Instances: Development workstations that data scientists can use to work with data and models.
- Compute Clusters: Scalable clusters of virtual machines for on-demand processing of experiment code.
- Inference Clusters: Deployment targets for predictive services that use your trained models.
- Attached Compute: Links to existing Azure compute resources, such as Virtual Machines or Azure Databricks clusters.

## [What is Azure Automated Machine Learning?](https://learn.microsoft.com/en-gb/training/modules/use-automated-machine-learning/4-what-is-automated-machine-learning)

Azure Machine Learning includes an *automated machine learning* capability that automatically tries multiple pre-processing techniques and model-training algorithms in parallel. These automated capabilities use the power of cloud compute to find the best performing supervised machine learning model for your data.

Automated machine learning allows you to train models without extensive data science or programming knowledge. For people with a data science and programming background, it provides a way to save time and resources by automating algorithm selection and hyperparameter tuning.

You can create an automated machine learning job in Azure Machine Learning studio.

In Azure Machine Learning, operations that you run are called *jobs*. You can configure multiple settings for your job before starting an automated machine learning run. The run configuration provides the information needed to specify your training script, compute target, and Azure ML environment in your run configuration and run a training job.

## [Understand the AutoML process](https://learn.microsoft.com/en-gb/training/modules/use-automated-machine-learning/5-machine-learning-steps)

You can think of the steps in a machine learning process as:

1. Prepare data: Identify the features and label in a dataset. Pre-process, or clean and transform, the data as needed.
2.  Train model: Split the data into two groups, a training and a validation set. Train a machine learning model using the training data set. Test the machine learning model for performance using the validation data set.
3. Evaluate performance: Compare how close the model's predictions are to the known labels.
4. Deploy a predictive service: After you train a machine learning model, you can deploy the model as an application on a server or device so that others can use it.

These are the same steps in the automated machine learning process with Azure Machine Learning.

### Prepare data

Machine learning models must be trained with existing data. Data scientists expend a lot of effort exploring and pre-processing data, and trying various types of model-training algorithms to produce accurate models, which is time consuming, and often makes inefficient use of expensive compute hardware.

In Azure Machine Learning, data for model training and other operations is usually encapsulated in an object called a *dataset*. You can create your own dataset in Azure Machine Learning studio.

### Train model

The automated machine learning capability in Azure Machine Learning supports supervised machine learning models - in other words, models for which the training data includes known label values. You can use automated machine learning to train models for:

- Classification (predicting categories or classes)
- Regression (predicting numeric values)
- Time series forecasting (predicting numeric values at a future point in time)

In Automated Machine Learning you can select from several types of tasks.

In Automated Machine Learning, you can select configurations for the primary metric, type of model used for training, exit criteria, and concurrency limits.

Importantly, AutoML will split data into a training set and a validation set. You can configure the details in the settings before you run the job.

### Evaluate performance

After the job has finished you can review the best performing model. In this case, you used exit criteria to stop the job. Thus the "best" model the job generated might not be the best possible model, just the best one found within the time allowed for this exercise.

The best model is identified based on the evaluation metric you specified, *Normalized root mean squared error.*

A technique called *cross-validation* is used to calculate the evaluation metric. After the model is trained using a portion of the data, the remaining portion is used to iteratively test, or cross-validate, the trained model. The metric is calculated by comparing the predicted value from the test with the actual known value, or label.

The difference between the predicted and actual value, known as the *residuals*, indicates the amount of *error* in the model. The performance metric *root mean squared error* (RMSE), is calculated by squaring the errors across all of the test cases, finding the mean of these squares, and then taking the square root. What all of this means is that smaller this value is, the more accurate the model's predictions. The *normalized root mean squared error* (NRMSE) standardizes the RMSE metric so it can be used for comparison between models which have variables on different scales.

The **Residual Histogram** shows the frequency of residual value ranges. Residuals represent variance between predicted and true values that can't be explained by the model, in other words, errors. You should hope to see the most frequently occurring residual values clustered around zero. You want small errors with fewer errors at the extreme ends of the scale.

The **Predicted vs. True** chart should show a diagonal trend in which the predicted value correlates closely to the true value. The dotted line shows how a perfect model should perform. The closer the line of your model's average predicted value is to the dotted line, the better its performance. A histogram below the line chart shows the distribution of true values.

After you've used automated machine learning to train some models, you can deploy the best performing model as a service for client applications to use.

### Deploy a predictive service

In Azure Machine Learning, you can deploy a service as an Azure Container Instances (ACI) or to an Azure Kubernetes Service (AKS) cluster. For production scenarios, an AKS deployment is recommended, for which you must create an inference cluster compute target. In this exercise, you'll use an ACI service, which is a suitable deployment target for testing, and does not require you to create an inference cluster.

## [Exercise - Explore Automated Machine Learning in Azure ML](https://learn.microsoft.com/en-gb/training/modules/use-automated-machine-learning/6-exercise)

In this exercise, you will use a dataset of historical bicycle rental details to train a model that predicts the number of bicycle rentals that should be expected on a given day, based on seasonal and meteorological features.

To complete this lab, you will need an Azure subscription in which you have administrative access.

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/use-automated-machine-learning/7-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/use-automated-machine-learning/8-summary)