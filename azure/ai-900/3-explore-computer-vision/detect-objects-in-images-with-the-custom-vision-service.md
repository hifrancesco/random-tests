# [Detect objects in images with the Custom Vision service](https://learn.microsoft.com/en-gb/training/modules/detect-objects-images-custom-vision/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/detect-objects-images-custom-vision/1-introduction)

*Object detection* is a form of machine learning based computer vision in which a model is trained to recognize individual types of objects in an image, and to identify their location in the image.

### Uses of object detection

Some sample applications of object detection include:

- **Checking for building safety**: Evaluating the safety of a building by analyzing footage of its interior for fire extinguishers or other emergency equipment.
- **Driving assistance**: Creating software for self-driving cars or vehicles with lane assist capabilities. The software can detect whether there is a car in another lane, and whether the driver's car is within its own lanes.
- **Detecting tumors**: Medical imaging such as an MRI or x-rays that can detect known objects for medical diagnosis.

## [What is object detection?](https://learn.microsoft.com/en-gb/training/modules/detect-objects-images-custom-vision/1a-what-is-object-detection)

Notice that an object detection model returns the following information:

- The *class* of each object identified in the image.
- The probability score of the object classification (which you can interpret as the *confidence* of the predicted class being correct)
- The coordinates of a *bounding box* for each object.

### Object Detection vs. Image Classification

- [**Image classification**](ai-900/../../docs/image-classification.md) is a machine learning based form of computer vision in which a model is trained to categorize images based on the primary subject matter they contain. 
- [**Object detection**](ai-900/../../docs/object-detection.md) goes further than this to classify individual objects within the image, and to return the coordinates of a bounding box that indicates the object's location.

## [Get started with object detection on Azure](https://learn.microsoft.com/en-gb/training/modules/detect-objects-images-custom-vision/2-object-detection-azure)

You can create an object detection machine learning model by using advanced deep learning techniques. However, this approach requires significant expertise and a large volume of training data. The **Custom Vision** cognitive service in Azure enables you to create object detection models that meet the needs of many computer vision scenarios with minimal deep learning expertise and fewer training images.

### Azure resources for Custom Vision

Creating an object detection solution with Custom Vision consists of three main tasks. First you must use upload and tag images, then you can train the model, and finally you must publish the model so that client applications can use it to generate predictions.

For each of these tasks, you need a resource in your Azure subscription. You can use the following types of resource:

- Custom Vision: A dedicated resource for the custom vision service, which can be either a training, a prediction or a both resource.
- Cognitive Services: A general cognitive services resource that includes Custom Vision along with many other cognitive services. You can use this type of resource for training, prediction, or both.

The separation of training and prediction resources is useful when you want to track resource utilization for model training separately from client applications using the model to predict image classes. However, it can make development of an image classification solution a little confusing.

The simplest approach is to use a general Cognitive Services resource for both training and prediction. This means you only need to concern yourself with one endpoint (the HTTP address at which your service is hosted) and key (a secret value used by client applications to authenticate themselves).

If you choose to create a Custom Vision resource, you will be prompted to choose training, prediction, or both - and it's important to note that if you choose "both", then two resources are created - one for training and one for prediction.

It's also possible to take a mix-and-match approach in which you use a dedicated Custom Vision resource for training, but deploy your model to a Cognitive Services resource for prediction. For this to work, the training and prediction resources must be created in the same region.

### Image tagging

Before you can train an object detection model, you must tag the classes and bounding box coordinates in a set of training images. This process can be time-consuming, but the Custom Vision portal provides a graphical interface that makes it straightforward. The interface will automatically suggest areas of the image where discrete objects are detected, and you can apply a class label to these suggested bounding boxes or drag to adjust the bounding box area. Additionally, after tagging and training with an initial dataset, the Computer Vision service can use smart tagging to suggest classes and bounding boxes for images you add to the training dataset.

Key considerations when tagging training images for object detection are ensuring that you have sufficient images of the objects in question, preferably from multiple angles; and making sure that the bounding boxes are defined tightly around each object.

### Model training and evaluation

To train the model, you can use the Custom Vision portal, or if you have the necessary coding experience you can use one of the Custom Vision service programming language-specific software development kits (SDKs). Training an object detection model can take some time, depending on the number of training images, classes, and objects within each image.

Model training process is an iterative process in which the Custom Vision service repeatedly trains the model using some of the data, but holds some back to evaluate the model. At the end of the training process, the performance for the trained model is indicated by the following evaluation metrics:

- Precision: What percentage of class predictions did the model correctly identify? For example, if the model predicted that 10 images are oranges, of which eight were actually oranges, then the precision is 0.8 (80%).
- Recall: What percentage of the class predictions made by the model were correct? For example, if there are 10 images of apples, and the model found 7 of them, then the recall is 0.7 (70%).
- Mean Average Precision (mAP): An overall metric that takes into account both precision and recall across all classes.

### Using the model for prediction

After you've trained the model, and you're satisfied with its evaluated performance, you can publish the model to your prediction resource. When you publish the model, you can assign it a name (the default is "IterationX", where X is the number of times you have trained the model).

To use you model, client application developers need the following information:

- Project ID: The unique ID of the Custom Vision project you created to train the model.
- Model name: The name you assigned to the model during publishing.
- Prediction endpoint: The HTTP address of the endpoints for the prediction resource to which you published the model (not the training resource).
- Prediction key: The authentication key for the prediction resource to which you published the model (not the training resource).

## [Exercise - Explore object detection](https://learn.microsoft.com/en-gb/training/modules/detect-objects-images-custom-vision/3-create-object-detection-solution)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/detect-objects-images-custom-vision/3a-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/detect-objects-images-custom-vision/4-summary)