# [Introduction to Azure OpenAI Service](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/)

## [Introduction](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/1-introduction)

| Capability | Examples |
|------------|----------|
| Generating natural language | Summarizing complex text for different reading levels, suggesting alternative wording for sentences, generating product descriptions for e-commerce sites, generating news articles, and more. |
| Generating code | Translating code from one programming language into another, identifying and troubleshooting bugs in code, generating code snippets for specific tasks, generating code for machine learning models, and more. |
| Generating images | Generating images for publications from text descriptions, generating artwork for video games, generating realistic images of products for e-commerce sites, generating custom avatars for social media, and more. |

## [What is generative AI](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/2-what-is-generative-ai)

OpenAI makes its AI models available to developers to build powerful software applications, such as ChatGPT. There are tons of [other examples of OpenAI](https://platform.openai.com/examples) applications on the OpenAI site, ranging from practical, such as generating text from code, to purely entertaining, such as making up scary stories.

Let's identify where OpenAI models fit into the AI landscape.

- Artificial Intelligence imitates human behavior by relying on machines to learn and execute tasks without explicit directions on what to output.
- Machine learning models take in data like weather conditions and fit the data to an algorithm, to make predictions like how much money a store might make in a given day.
- Deep learning models use layers of algorithms in the form of artificial neural networks to return results for more complex use cases. Azure AI services are built on deep learning models. You can check out this article to learn more about the [difference between machine learning and deep learning.](https://learn.microsoft.com/en-us/azure/machine-learning/concept-deep-learning-vs-machine-learning)
- Generative AI models are a subset of deep learning models that can produce new content based on what is described in the input. The OpenAI models are a collection of generative AI models that can produce language, code, and images.

## [Describe Azure OpenAI](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/3-describe-azure-openai)

Microsoft has partnered with OpenAI to deliver on three main goals:

- To utilize Azure's infrastructure, including security, compliance, and regional availability, to help users build enterprise-grade applications.
- To deploy OpenAI AI model capabilities across Microsoft products, including and beyond Azure AI products.
- To use Azure to power all of OpenAI's workloads.

### [Introduction to Azure OpenAI Service]

Azure OpenAI Service is a result of the partnership between Microsoft and OpenAI. The service combines Azure's enterprise-grade capabilities with OpenAI's generative AI model capabilities.

Azure OpenAI is available for Azure users and consists of four components:

- Pre-trained generative AI models
- Customization capabilities; the ability to fine-tune AI models with your own data
- Built-in tools to detect and mitigate harmful use cases so users can implement AI responsibly
- Enterprise-grade security with role-based access control (RBAC) and private networks

Using Azure OpenAI allows you to transition between your work with Azure services and OpenAI, while utilizing Azure's private networking, regional availability, and responsible AI content filtering.

### Understand Azure OpenAI workloads

Azure OpenAI supports many common AI workloads and solves for some new ones.

Common AI workloads include machine learning, computer vision, natural language processing, conversational AI, anomaly detection, and knowledge mining.

Other AI workloads Azure OpenAI supports can be categorized into three groups:

- Generating Natural Language
	- Text completion: generate and edit text
	- Embeddings: search, classify, and compare text
- Generating Code: generate, edit, and explain code
- Generating Images: generate and edit images

Azure's AI services are categorized into three main groups:

1. Azure's Machine Learning platform - this provides tools and services for building, training, and deploying machine learning models at scale. 

2. Cognitive Services - a collection of pre-built APIs that allow developers to easily add intelligent features to their applications, such as natural language processing, computer vision, speech recognition, and more. 

3. Applied AI Services - these services provide domain-specific AI solutions for industries such as healthcare, finance, and retail, and are designed to address specific use cases, such as fraud detection, predictive maintenance, and more. 

Azure Cognitive Services has five pillars: vision, speech, language, decision, and the Azure OpenAI Service. The services you choose to use depend on what you need to accomplish. In particular, there are several overlapping capabilities between the Cognitive Service's Language service and OpenAI's service, such as translation, sentiment analysis, and keyword extraction.

While there's no strict guidance on when to use a particular service, Azure's existing Language service can be used for widely known use-cases that require minimal tuning, the process of optimizing a model's performance. Azure OpenAI's service may be more beneficial for use-cases that require highly customized generative models, or for exploratory research.

## [How to use Azure OpenAI](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/4-how-to-use-azure-openai)

Azure APIs are designed to provide a simple and standardized way for developers to access and use Azure's various services. These APIs are typically exposed through RESTful web services, which use the HTTP protocol to exchange data between client applications and Azure's services.

To use an Azure API, a developer typically needs to obtain an API key or authentication token, which grants them access to the service. The developer can then make HTTP requests to the API, passing in any necessary data as query parameters or in the request body. The API then processes the request, performs any necessary computations or data processing, and returns a response to the client application.

For example, if a developer wanted to use Azure's Computer Vision API to analyze an image, they would first obtain an API key for the service. They could then make an HTTP request to the API, passing in the image data as a binary file or URL parameter. The API would then analyze the image, using machine learning algorithms to identify objects, people, text, and other features. Finally, the API would return a response to the client application, containing the results of the analysis in a structured format such as JSON.

Overall, Azure APIs provide a powerful and flexible way for developers to build intelligent applications on the Azure platform, leveraging the latest AI technologies to solve complex problems and create new opportunities for innovation.

### Azure OpenAI Studio

In the Azure OpenAI Studio, you can build AI models and deploy them for public consumption in software applications. Azure OpenAI's capabilities are made possible by a few specific generative AI models. Different models are optimized for different tasks; some models excel at simple summarization tasks, some are great at general unstructured responses, and still others are built to generate unique images from text input.

These OpenAI models fall into a few main families:

- Generative Pre-trained Transformer (GPT)
- Codex
- DALL-E

[Embeddings](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/understand-embeddings) are also available on Azure OpenAI. Embedding models are specifically created to be good at a particular task.

Azure OpenAI's AI models can all be trained and customized with fine-tuning. We won't go into custom models here, but you can learn more on the [fine-tuning your model](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/fine-tuning?pivots=programming-language-studio%3Fazure-portal%3Dtrue) Azure documentation.

### Playground

In the Azure OpenAI Studio, you can experiment with OpenAI models in a text box user interface called the GPT-3 Playground. You can type in prompts, and see responses without having to code.

## [Understand OpenAI's natural language capabilities](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/5-understand-openai-natural-language)

Azure OpenAI's natural language models are able to take in natural language and generate responses.

Natural language learning models are trained on words or chunks of characters known as tokens. For example, the word "hamburger" gets broken up into the tokens ham, bur, and ger, while a short and common word like "pear" is a single token. These tokens are mapped into vectors for a machine learning model to use for training. When a trained natural language model takes in a user's input, it also breaks down the input into tokens.

### Understanding GPT models for natural language generation

Generative pre-trained transformer (GPT) models are excellent at both understanding and creating natural language. If you've seen recent news around AI answering questions or writing a paragraph based on a prompt, it likely could have been generated by a GPT model. GPT models often have the version appended to the end, such as GPT-2 or GPT-3. Azure OpenAI offers access to GPT-3, and will provide access to GPT-3.5 soon.

### What does GPT-3 look like?

A key aspect of OpenAI's generative AI is that it takes an input, or prompt, to return a natural language, visual, or code response. GPT tries to infer, or guess, the context of the user's question based on the prompt.

GPT models are great at completing several natural language tasks, some of which include:

| Task | Prompt |
| --- | --- |
| Summarizing text | "Summarize this text into a short blurb" |
| Classifying text | "What genre of book is this?" |
| Generating names or phrases | "Write a tagline for my flower company" |
| Translation | "Translate 'How are you' to French" |
| Answering questions | "What does Azure OpenAI do?" |
| Suggesting content | "Give me the five best wedding songs" |

### How models are applied to new use cases

ChatGPT is chatbot built on the GPT-3.5 generative AI model. You may have tried out ChatGPT's predictive capabilities in a chat portal similar to this screenshot, where you can type prompts and receive automated responses. The portal consists of the front-end user interface (UI) users see, and a back-end that includes the GPT-3.5 model. The combination of the front and back end can be described as a chatbot. The model provided on the back end is what is available as a building block with the OpenAI API. When you see ChatGPT-like capabilities in other applications, developers have taken the building blocks, customized them to a use case, and built them into the back end of new front-end user interfaces.

## [Understand OpenAI code generation capabilities](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/6-understand-openai-code-generation)

Code generation AI models are able to take natural language or code snippets and translate them into code. The OpenAI code generation model family, Codex, is proficient in over a dozen languages, such as C#, JavaScript, Perl, PHP, and is most capable in Python.

### Codex

Codex models are based off of GPT-3 and are optimized to understand and write code. These models have been trained on both natural language and billions of lines of code from public repositories. Codex is able to generate code from natural language instructions such as code comments, and can suggest ways to complete code functions.

Code generation models can help developers code faster, understand new coding languages, and focus on solving bigger problems in their application. Developers can break down their goal into simpler tasks and use Codex to help build those out tasks using known patterns.

Codex can also summarize functions that are already written, explain SQL queries or tables, and convert a function from one programming language into another.

When interacting with Codex models, you can specify libraries or language specific tags to make it clear to Codex what we want. 

### GitHub Copilot

OpenAI partnered with GitHub to create GitHub Copilot, which they call an AI pair programmer. GitHub Copilot integrates the power of OpenAI Codex into a plugin for developer environments like Visual Studio Code.

Once the plugin is installed and enabled, you can start writing your code, and GitHub Copilot starts automatically suggesting the remainder of the function based on code comments or the function name. For example, we have only a function name in the file, and the gray text is automatically suggested to complete it.

GitHub Copilot offers multiple suggestions for code completion, which you can tab through using keyboard shortcuts. When given informative code comments, it can even suggest a function name along with the complete function code.

## [Understand OpenAI's image generation capabilities](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/7-understand-openai-image-generation)

Image generation models can take a prompt, a base image, or both, and create something new. These generative AI models can create both realistic and artistic images, change the layout or style of an image, and create variations on a provided image.

### DALL-E

In addition to natural language capabilities, these generative AI models can edit and create images. The model that works with images is called DALL-E. Much like GPT models, subsequent versions of DALL-E are appended onto the name, such as DALL-E 2. Image capabilities generally fall into the three categories of image creation, editing an image, and creating variations of an image.

### Image generation

Original images can be generated by providing a text prompt of what you would like the image to be of. The more detailed the prompt, the more likely the model will provide a desired result.

With DALL-E, you can even request an image in a particular style, such as "a dog in the style of Vincent van Gogh". Styles can be used for edits and variations as well.

For example, given the prompt "an elephant standing with a burger on top, style digital art", the model generates digital art images depicting exactly what is asked for.

When asked for something more generic like "a pink fox", the images generated are more varied and simpler while still fulfilling what is asked for.

However when we make the prompt more specific, such as "a pink fox running through a field, in the style of Monet", the model creates much more similar detailed images.

### Editing an image

When provided an image, DALL-E can edit the image as requested by changing its style, adding or removing items, or generating new content to add. Edits are made by uploading the original image and specifying a transparent mask that indicates what area of the image to edit. Along with the image and mask, a prompt indicating what is to be edited instructs the model to then generate the appropriate content to fill the area.

When given one of the above images of a pink fox, a mask covering the fox, and the prompt of "blue gorilla reading a book in a field", the model creates edits of the image based on the provided input.

### Image variations

Image variations can be created by providing an image and specifying how many variations of the image you would like. The general content of the image will stay the same, but aspects will be adjusted such as where subjects are located or looking, background scene, and colors may change.

For example, if I upload one of the images of the elephant wearing a burger as a hat, I get variations of the same subject.

## [Describe Azure OpenAI's access and responsible AI policies](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/8-describe-openai-responsible-ai)

It's important to consider the ethical implications of working with AI systems. Azure OpenAI provides powerful natural language models capable of completing various tasks and operating in several different use cases, each with their own considerations for safe and fair use. Teams or individuals tasked with developing and deploying AI systems should work to identify, measure, and mitigate harm.

Usage of Azure OpenAI should follow the six Microsoft [AI principles](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai):

- Fairness: Al systems shouldn't make decisions that discriminate against or support bias of a group or individual.
- Reliability and Safety: Al systems should respond safely to new situations and potential manipulation.
- Privacy and Security: Al systems should be secure and respect data privacy.
- Inclusiveness: Al systems should empower everyone and engage people.
- Accountability: People must be accountable for how Al systems operate.
- Transparency: AI systems should have explanations so users can understand how they're built and used.

Responsible AI principles guide [Microsoft's Transparency Notes on Azure OpenAI](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/transparency-note), as well as explanations of other products. Transparency Notes are intended to help you understand how Microsoft's AI technology works, the choices system owners can make that influence system performance and behavior, and the importance of thinking about the whole system, including the technology, the people, and the environment.

### Limited access to Azure OpenAI

As part of Microsoft's commitment to using AI responsibly, access to Azure OpenAI is currently limited. Customers that wish to use Azure OpenAI must submit a registration form for both initial experimentation access, and again for approval for use in production.

Additional registration is required for customers who want to modify content filters and abuse monitoring.

To apply for access and learn more about the limited access policy, see the [Azure OpenAI limited access](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/limited-access) documentation.

## [Knowledge check](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/9-knowledge-check)

## [Summary](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/10-summary)
