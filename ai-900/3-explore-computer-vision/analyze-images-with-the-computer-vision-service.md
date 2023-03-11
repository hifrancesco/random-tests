# [Analyze images with the Computer Vision service](https://learn.microsoft.com/en-gb/training/modules/analyze-images-computer-vision/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/analyze-images-computer-vision/1-introduction)

*Computer vision* is one of the core areas of artificial intelligence (AI), and focuses on creating solutions that enable AI applications to "see" the world and make sense of it.

Of course, computers don't have biological eyes that work the way ours do, but they are capable of processing images; either from a live camera feed or from digital photographs or videos. This ability to process images is the key to creating software that can emulate human visual perception.

Some potential uses for computer vision include:

- **Content Organization**: Identify people or objects in photos and organize them based on that identification. Photo recognition applications like this are commonly used in photo storage and social media applications.
- **Text Extraction**: Analyze images and PDF documents that contain text and extract the text into a structured format.
- **Spatial Analysis**: Identify people or objects, such as cars, in a space and map their movement within that space.

To an AI application, an image is just an array of pixel values. These numeric values can be used as features to train machine learning models that make predictions about the image and its contents.

Training machine learning models from scratch can be very time intensive and require a large amount of data. Microsoft's Computer Vision service gives you access to pre-trained computer vision capabilities.

## [Get started with image analysis on Azure](https://learn.microsoft.com/en-gb/training/modules/analyze-images-computer-vision/2-image-analysis-azure)

The Computer Vision service is a cognitive service in Microsoft Azure that provides pre-built computer vision capabilities. The service can analyze images, and return detailed information about an image and the objects it depicts.

### Azure resources for Computer Vision(https://learn.microsoft.com/en-gb/training/modules/analyze-images-computer-vision/2-image-analysis-azure)

To use the Computer Vision service, you need to create a resource for it in your Azure subscription. You can use either of the following resource types:

- **Computer Vision**: A specific resource for the Computer Vision service. Use this resource type if you don't intend to use any other cognitive services, or if you want to track utilization and costs for your Computer Vision resource separately.
- **Cognitive Services**: A general cognitive services resource that includes Computer Vision along with many other cognitive services; such as Text Analytics, Translator Text, and others. Use this resource type if you plan to use multiple cognitive services and want to simplify administration and development.

Whichever type of resource you choose to create, it will provide two pieces of information that you will need to use it:

- A **key** that is used to authenticate client applications.
- An **endpoint** that provides the HTTP address at which your resource can be accessed.

## [Exercise - Explore Computer Vision](https://learn.microsoft.com/en-gb/training/modules/analyze-images-computer-vision/3-analyze-images)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/analyze-images-computer-vision/3a-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/analyze-images-computer-vision/4-summary)