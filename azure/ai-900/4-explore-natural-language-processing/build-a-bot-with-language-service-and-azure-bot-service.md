# [Build a bot with the Language Service and Azure Bot Service](https://learn.microsoft.com/en-gb/training/modules/build-faq-chatbot-qna-maker-azure-bot-service/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/build-faq-chatbot-qna-maker-azure-bot-service/1-introduction)

In today's connected world, people use a variety of technologies to communicate. For example:

- Voice calls
- Messaging services
- Online chat applications
- Email
- Social media platforms
- Collaborative workplace tools

We've become so used to ubiquitous connectivity, that we expect the organizations we deal with to be easily contactable and immediately responsive through the channels we already use. Additionally, we expect these organizations to engage with us individually, and be able to answer complex questions at a personal level.
Conversational AI

While many organizations publish support information and answers to frequently asked questions (FAQs) that can be accessed through a web browser or dedicated app. The complexity of the systems and services they offer means that answers to specific questions are hard to find. Often, these organizations find their support personnel being overloaded with requests for help through phone calls, email, text messages, social media, and other channels.

Increasingly, organizations are turning to artificial intelligence (AI) solutions that make use of AI agents, commonly known as bots to provide a first-line of automated support through the full range of channels that we use to communicate.

Conversations typically take the form of messages exchanged in turns; and one of the most common kinds of conversational exchange is a question followed by an answer. This pattern forms the basis for many user support bots, and can often be based on existing FAQ documentation. To implement this kind of solution, you need:

- A knowledge base of question and answer pairs - usually with some built-in natural language processing model to enable questions that can be phrased in multiple ways to be understood with the same semantic meaning.
- A bot service that provides an interface to the knowledge base through one or more channels.

## [Get started with the Language service and Azure Bot Service](https://learn.microsoft.com/en-gb/training/modules/build-faq-chatbot-qna-maker-azure-bot-service/2-get-started-knowledge-base)

You can easily create a user support bot solution on Microsoft Azure using a combination of two core services:

- Language service. The Language service includes a custom question answering feature that enables you to create a knowledge base of question and answer pairs that can be queried using natural language input. 
- Azure Bot service. This service provides a framework for developing, publishing, and managing bots on Azure.

### Creating a custom question answering knowledge base

The first challenge in creating a user support bot is to use the Language service to create a knowledge base. You can use the Language Studio's custom question answering feature to create, train, publish, and manage knowledge bases.

#### Provision a Language service Azure resource

To create a knowledge base, you must first provision a Language service resource in your Azure subscription.

### Define questions and answers

After provisioning a Language service resource, you can use the Language Studio's custom question answering feature to create a knowledge base that consists of question-and-answer pairs. These questions and answers can be:

- Generated from an existing FAQ document or web page.
- Entered and edited manually.

In many cases, a knowledge base is created using a combination of all of these techniques; starting with a base dataset of questions and answers from an existing FAQ document and extending the knowledge base with additional manual entries.

Questions in the knowledge base can be assigned alternative phrasing to help consolidate questions with the same meaning. For example, you might include a question like:

```
    What is your head office location?
```

You can anticipate different ways this question could be asked by adding an alternative phrasing such as:

```
    Where is your head office located?
```

#### Test the knowledge base

After creating a set of question-and-answer pairs, you must save it. This process analyzes your literal questions and answers and applies a built-in natural language processing model to match appropriate answers to questions, even when they are not phrased exactly as specified in your question definitions. Then you can use the built-in test interface in the Language Studio to test your knowledge base by submitting questions and reviewing the answers that are returned.

#### Use the knowledge base

When you're satisfied with your knowledge base, deploy it. Then you can use it over its REST interface. To access the knowledge base, client applications require:

- The knowledge base ID
- The knowledge base endpoint
- The knowledge base authorization key

### Build a bot with the Azure Bot Service

After you've created and deployed a knowledge base, you can deliver it to users through a bot.

#### Create a bot for your knowledge base

You can create a custom bot by using the Microsoft Bot Framework SDK to write code that controls conversation flow and integrates with your knowledge base. However, an easier approach is to use the automatic bot creation functionality, which enables you create a bot for your deployed knowledge base and publish it as an Azure Bot Service application with just a few clicks.

#### Extend and configure the bot

After creating your bot, you can manage it in the Azure portal, where you can:

- Extend the bot's functionality by adding custom code.
- Test the bot in an interactive test interface.
- Configure logging, analytics, and integration with other services.

For simple updates, you can edit bot code directly in the Azure portal. However, for more comprehensive customization, you can download the source code and edit it locally; republishing the bot directly to Azure when you're ready.

#### Connect channels

When your bot is ready to be delivered to users, you can connect it to multiple channels; making it possible for users to interact with it through web chat, email, Microsoft Teams, and other common communication media.

Users can submit questions to the bot through any of its channels, and receive an appropriate answer from the knowledge base on which the bot is based.

## [Exercise - Explore question answering](https://learn.microsoft.com/en-gb/training/modules/build-faq-chatbot-qna-maker-azure-bot-service/3-create-bot)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/build-faq-chatbot-qna-maker-azure-bot-service/3a-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/build-faq-chatbot-qna-maker-azure-bot-service/4-summary)