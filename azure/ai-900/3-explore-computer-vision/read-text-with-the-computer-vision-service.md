# [Read text with the Computer Vision service](https://learn.microsoft.com/en-gb/training/modules/read-text-computer-vision/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/read-text-computer-vision/1-introduction)

The ability for computer systems to process written or printed text is an area of artificial intelligence (AI) where computer vision intersects with natural language processing. You need computer vision capabilities to "read" the text, and then you need natural language processing capabilities to make sense of it.

The basic foundation of processing printed text is optical character recognition (OCR), in which a model can be trained to recognize individual shapes as letters, numerals, punctuation, or other elements of text. Much of the early work on implementing this kind of capability was performed by postal services to support automatic sorting of mail based on postal codes. Since then, the state-of-the-art for reading text has moved on, and it's now possible to build models that can detect printed or handwritten text in an image and read it line-by-line or even word-by-word.

In this module, we'll focus on the use of OCR technologies to detect text in images and convert it into a text-based data format, which can then be stored, printed, or used as the input for further processing or analysis.

### Uses of OCR

The ability to recognize printed and handwritten text in images, is beneficial in many scenarios such as:

- note taking
- digitizing forms, such as medical records or historical documents
- scanning printed or handwritten checks for bank deposits

## [Get started with the Read API on Azure](https://learn.microsoft.com/en-gb/training/modules/read-text-computer-vision/2-ocr-azure)

The ability to extract text from images is handled by the Computer Vision service, which also provides image analysis capabilities.

### Azure resources for Computer Vision

The first step towards using the Computer Vision service is to create a resource for it in your Azure subscription. You can use either of the following resource types:

- Computer Vision: A specific resource for the Computer Vision service. Use this resource type if you don't intend to use any other cognitive services, or if you want to track utilization and costs for your Computer Vision resource separately.
- Cognitive Services: A general cognitive services resource that includes Computer Vision along with many other cognitive services; such as Text Analytics, Translator Text, and others. Use this resource type if you plan to use multiple cognitive services and want to simplify administration and development.

Whichever type of resource you choose to create, it will provide two pieces of information that you will need to use it:

- A key that is used to authenticate client applications.
- An endpoint that provides the HTTP address at which your resource can be accessed.

### Use the Computer Vision service to read text

Many times an image contains text. It can be typewritten text or handwritten. Some common examples are images with road signs, scanned documents that are in an image format such as JPEG or PNG file formats, or even just a picture taken of a white board that was used during a meeting.

The Computer Vision service provides one application programming interface (APIs) that you can use to read text in images: the Read API.

### The Read API

The Read API uses the latest recognition models and is optimized for images that have a significant amount of text or has considerable visual noise.

The Read API can handle scanned documents that have a lot of text. It also has the ability to automatically determine the proper recognition model to use, taking into consideration lines of text and supporting images with printed text as well as recognizing handwriting.

Because the Read API can work with large documents, it works asynchronously so as not to block your application while it is reading the content and returning results to your application. This means that to use the Read API, your application must use a three-step process:

1. Submit an image to the API, and retrieve an operation ID in response.
2. Use the operation ID to check on the status of the image analysis operation, and wait until it has completed.
3. Retrieve the results of the operation.

The results from the Read API are arranged into the following hierarchy:

- Pages - One for each page of text, including information about the page size and orientation.
- Lines - The lines of text on a page.
- Words - The words in a line of text, including the bounding box coordinates and text itself.

Each line and word includes bounding box coordinates indicating its position on the page.

## [Exercise - Explore optical character recognition with the Read API](https://learn.microsoft.com/en-gb/training/modules/read-text-computer-vision/3-read-text-computer-vision)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/read-text-computer-vision/3a-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/read-text-computer-vision/4-summary)