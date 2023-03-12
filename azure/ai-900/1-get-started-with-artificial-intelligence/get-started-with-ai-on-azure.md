# [Get started with AI on Azure](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/)

## [Introduction to AI](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/1-introduction)

### What is AI?

Simply put, AI is the creation of software that imitates human behaviors and capabilities. Key workloads include:

- Machine learning - This is often the foundation for an AI system, and is the way we "teach" a computer model to make prediction and draw conclusions from data.
- Anomaly detection - The capability to automatically detect errors or unusual activity in a system.
- Computer vision - The capability of software to interpret the world visually through cameras, video, and images.
- Natural language processing - The capability for a computer to interpret written or spoken language, and respond in kind.
- Knowledge mining - The capability to extract information from large volumes of often unstructured data to create a searchable knowledge store.

## [Understand machine learning](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/2-understand-machine-learn)

### How machine learning works

So how do machines learn?

The answer is, from data. In today's world, we create huge volumes of data as we go about our everyday lives. From the text messages, emails, and social media posts we send to the photographs and videos we take on our phones, we generate massive amounts of information. More data still is created by millions of sensors in our homes, cars, cities, public transport infrastructure, and factories.

Data scientists can use all of that data to train machine learning models that can make predictions and inferences based on the relationships they find in the data.

### Machine learning in Microsoft Azure

Microsoft Azure provides the Azure Machine Learning service - a cloud-based platform for creating, managing, and publishing machine learning models. Azure Machine Learning provides the following features and capabilities:

Feature | Capability
--------|-----------
Automated machine learning | This feature enables non-experts to quickly create an effective machine learning model from data.
Azure Machine Learning designer | A graphical interface enabling no-code development of machine learning solutions.
Data and compute management | Cloud-based data storage and compute resources that professional data scientists can use to run data experiment code at scale.
Pipelines | Data scientists, software engineers, and IT operations professionals can define pipelines to orchestrate model training, deployment, and management tasks.

## [Understand anomaly detection](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/3-understand-anomaly-detection)

Imagine you're creating a software system to monitor credit card transactions and detect unusual usage patterns that might indicate fraud. Or an application that tracks activity in an automated production line and identifies failures. Or a racing car telemetry system that uses sensors to proactively warn engineers about potential mechanical failures before they happen.

These kinds of scenario can be addressed by using anomaly detection - a machine learning based technique that analyzes data over time and identifies unusual changes.

## [Understand computer vision](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/4-understand-computer-vision)

### Computer Vision models and capabilities

Most computer vision solutions are based on machine learning models that can be applied to visual input from cameras, videos, or images. The following table describes common computer vision tasks.

Task | Description
---- | -----------
Image classification | Image classification involves training a machine learning model to classify images based on their contents. For example, in a traffic monitoring solution you might use an image classification model to classify images based on the type of vehicle they contain, such as taxis, buses, cyclists, and so on.
Object detection | Object detection machine learning models are trained to classify individual objects within an image, and identify their location with a bounding box. For example, a traffic monitoring solution might use object detection to identify the location of different classes of vehicle.
Semantic segmentation | Semantic segmentation is an advanced machine learning technique in which individual pixels in the image are classified according to the object to which they belong. For example, a traffic monitoring solution might overlay traffic images with "mask" layers to highlight different vehicles using specific colors.
Image analysis | You can create solutions that combine machine learning models with advanced image analysis techniques to extract information from images, including "tags" that could help catalog the image or even descriptive captions that summarize the scene shown in the image.
Face detection, analysis, and recognition | Face detection is a specialized form of object detection that locates human faces in an image. This can be combined with classification and facial geometry analysis techniques to recognize individuals based on their facial features.
Optical character recognition (OCR) | Optical character recognition is a technique used to detect and read text in images. You can use OCR to read text in photographs (for example, road signs or store fronts) or to extract information from scanned documents such as letters, invoices, or forms.

### Computer vision services in Microsoft Azure

Microsoft Azure provides the following cognitive services to help you create computer vision solutions:

Service | Capabilities
------- | ------------
Computer Vision | You can use this service to analyze images and video, and extract descriptions, tags, objects, and text.
Custom Vision | Use this service to train custom image classification and object detection models using your own images.
Face | The Face service enables you to build face detection and facial recognition solutions.
Form Recognizer | Use this service to extract information from scanned forms and invoices.

## [Understand natural language processing](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/5-understand-natural-language-process)

Natural language processing (NLP) is the area of AI that deals with creating software that understands written and spoken language.

NLP enables you to create software that can:

- Analyze and interpret text in documents, email messages, and other sources.
- Interpret spoken language, and synthesize speech responses.
- Automatically translate spoken or written phrases between languages.
- Interpret commands and determine appropriate actions.

### Natural language processing in Microsoft Azure

In Microsoft Azure, you can use the following cognitive services to build natural language processing solutions:

Service | Capabilities
------- | ------------
Language | Use this service to access features for understanding and analyzing text, training language models that can understand spoken or text-based commands, and building intelligent applications.
Translator | Use this service to translate text between more than 60 languages.
Speech | Use this service to recognize and synthesize speech, and to translate spoken languages.
Azure Bot | This service provides a platform for conversational AI, the capability of a software "agent" to participate in a conversation. Developers can use the _Bot Framework_ to create a bot and manage it with Azure Bot Service - integrating back-end services like Language, and connecting to channels for web chat, email, Microsoft Teams, and others.

## [Understand knowledge mining](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/6-understand-knowledge-mining)

Knowledge mining is the term used to describe solutions that involve extracting information from large volumes of often unstructured data to create a searchable knowledge store.

### Knowledge mining in Microsoft Azure

One of these knowledge mining solutions is Azure Cognitive Search, a private, enterprise, search solution that has tools for building indexes. The indexes can then be used for internal only use, or to enable searchable content on public facing internet assets.

Azure Cognitive Search can utilize the built-in AI capabilities of Azure Cognitive Services such as image processing, content extraction, and natural language processing to perform knowledge mining of documents. The product's AI capabilities makes it possible to index previously unsearchable documents and to extract and surface insights from large amounts of data quickly.

## [Challenges and risks with AI](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/7-challenges-with-ai)

Artificial Intelligence is a powerful tool that can be used to greatly benefit the world. However, like any tool, it must be used responsibly.

The following table shows some of the potential challenges and risks facing an AI application developer.

Challenge or Risk | Example
----------------- | --------
Bias can affect results | A loan-approval model discriminates by gender due to bias in the data with which it was trained
Errors may cause harm | An autonomous vehicle experiences a system failure and causes a collision
Data could be exposed | A medical diagnostic bot is trained using sensitive patient data, which is stored insecurely
Solutions may not work for everyone | A home automation assistant provides no audio output for visually impaired users
Users must trust a complex system | An AI-based financial tool makes investment recommendations - what are they based on?
Who's liable for AI-driven decisions? | An innocent person is convicted of a crime based on evidence from facial recognition – who's responsible?

## [Understand Responsible AI](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/8-understand-responsible-ai)

- Fairness
- Reliability and safety
- Privacy and security
- Inclusiveness
- Transparency
- Accountability

### [Further resources](https://www.microsoft.com/en-gb/ai/responsible-ai-resources?rtc=1)

## [Knowledge check](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/8a-knowledge-check)

## [Summary](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/9-summary)
