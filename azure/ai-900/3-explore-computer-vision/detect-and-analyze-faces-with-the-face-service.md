# [Detect and analyze faces with the Face service](https://learn.microsoft.com/en-gb/training/modules/detect-analyze-faces/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/detect-analyze-faces/1-introduction)

Face detection and analysis is an area of artificial intelligence (AI) in which we use algorithms to locate and analyze human faces in images or video content.

### Face detection

Face detection involves identifying regions of an image that contain a human face, typically by returning bounding box coordinates that form a rectangle around the face.

### Facial analysis

Moving beyond simple face detection, some algorithms can also return other information, such as facial landmarks (nose, eyes, eyebrows, lips, and others).

These facial landmarks can be used as features with which to train a machine learning model.

### Facial recognition

A further application of facial analysis is to train a machine learning model to identify known individuals from their facial features. This usage is more generally known as facial recognition, and involves using multiple images of each person you want to recognize to train a model so that it can detect those individuals in new images on which it wasn't trained.

### Uses of face detection and analysis

There are many applications for face detection, analysis, and recognition. For example,

- Security - facial recognition can be used in building security applications, and increasingly it is used in smart phones operating systems for unlocking devices.
- Social media - facial recognition can be used to automatically tag known friends in photographs.
- Intelligent monitoring - for example, an automobile might include a system that monitors the driver's face to determine if the driver is looking at the road, looking at a mobile device, or shows signs of tiredness.
- Advertising - analyzing faces in an image can help direct advertisements to an appropriate demographic audience.
- Missing persons - using public cameras systems, facial recognition can be used to identify if a missing person is in the image frame.
- Identity validation - useful at ports of entry kiosks where a person holds a special entry permit.

When used responsibly, facial recognition is an important and useful technology that can improve efficiency, security, and customer experiences. Face is a building block for creating a facial recognition system.

## [Get started with Face analysis on Azure](https://learn.microsoft.com/en-gb/training/modules/detect-analyze-faces/2-face-analysis-azure)

Microsoft Azure provides multiple cognitive services that you can use to detect and analyze faces, including:

- Computer Vision, which offers face detection and some basic face analysis, such as returning the bounding box coordinates around an image.
- Video Indexer, which you can use to detect and identify faces in a video.
- Face, which offers pre-built algorithms that can detect, recognize, and analyze faces.

Of these, Face offers the widest range of facial analysis capabilities.

### Face

Face can return the rectangle coordinates for any human faces that are found in an image, as well as a series of attributes related to those faces such as:

- **Blur**: how blurred the face is (which can be an indication of how likely the face is to be the main focus of the image)
- **Exposure**: aspects such as underexposed or over exposed and applies to the face in the image and not the overall image exposure
- **Glasses**: if the person is wearing glasses
- **Head pose**: the face's orientation in a 3D space
- **Noise**: refers to visual noise in the image. If you have taken a photo with a high ISO setting for darker settings, you would notice this noise in the image. The image looks grainy or full of tiny dots that make the image less clear
- **Occlusion**: determines if there may be objects blocking the face in the image

### Responsible AI use

Anyone can use the Face service to:

- Detect the location of faces in an image
- Determine if a face is wearing glasses
- Determine if there's occlusion, blur, noise, or over/under exposure for any of the faces
- Return the head pose coordinates for each face in an image

The Limited Access policy requires customers to submit an intake form to access additional Face service capabilities including:

- The ability to compare faces for similarity
- The ability to identify named individuals in an image

### Azure resources for Face

To use Face, you must create one of the following types of resource in your Azure subscription:

- Face: Use this specific resource type if you don't intend to use any other cognitive services, or if you want to track utilization and costs for Face separately.
- Cognitive Services: A general cognitive services resource that includes Computer Vision along with many other cognitive services; such as Custom Vision, Form Recognizer, Language, and others. Use this resource type if you plan to use multiple cognitive services and want to simplify administration and development.

Whichever type of resource you choose to create, it will provide two pieces of information that you will need to use it:

- A key that is used to authenticate client applications.
- An endpoint that provides the HTTP address at which your resource can be accessed.

### Tips for more accurate results

There are some considerations that can help improve the accuracy of the detection in the images:

- image format - supported images are JPEG, PNG, GIF, and BMP
- file size - 6 MB or smaller
- face size range - from 36 x 36 up to 4096 x 4096. Smaller or larger faces will not be detected
- other issues - face detection can be impaired by extreme face angles, occlusion (objects blocking the face such as a hand). Best results are obtained when the faces are full-frontal or as near as possible to full-frontal.

## [Exercise - Explore face detection](https://learn.microsoft.com/en-gb/training/modules/detect-analyze-faces/3-create-face-solutions)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/detect-analyze-faces/3a-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/detect-analyze-faces/4-summary)