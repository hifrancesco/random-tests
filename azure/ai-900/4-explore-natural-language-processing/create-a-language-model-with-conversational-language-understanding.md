# [Create a language model with Conversational Language Understanding](https://learn.microsoft.com/en-gb/training/modules/create-language-model-with-language-understanding/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/create-language-model-with-language-understanding/1-introduction)

In 1950, the British mathematician Alan Turing devised the Imitation Game, which has become known as the Turing Test and hypothesizes that if a dialog is natural enough, you may not know whether you're conversing with a human or a computer. As artificial intelligence (AI) grows ever more sophisticated, this kind of conversational interaction with applications and digital assistants is becoming more and more common, and in specific scenarios can result in human-like interactions with AI agents. Common scenarios for this kind of solution include customer support applications, reservation systems, and home automation among others.

To realize the aspiration of the imitation game, computers need not only to be able to accept language as input (either in text or audio format), but also to be able to interpret the semantic meaning of the input - in other words, understand what is being said.

On Microsoft Azure, conversational language understanding is supported through the Language Service. To work with Conversational Language Understanding, you need to take into account three core concepts: utterances, entities, and intents.

### Utterances

An utterance is an example of something a user might say, and which your application must interpret. For example, when using a home automation system, a user might use the following utterances:

```
    "Switch the fan on."

    "Turn on the light."
```

### Entities

An entity is an item to which an utterance refers. For example, fan and light in the following utterances:

```
    "Switch the fan on."

    "Turn on the light."
```

You can think of the fan and light entities as being specific instances of a general device entity.

### Intents

An intent represents the purpose, or goal, expressed in a user's utterance. For example, for both of the previously considered utterances, the intent is to turn a device on; so in your Conversational Language Understanding application, you might define a TurnOn intent that is related to these utterances.

A Language Understanding application defines a model consisting of intents and entities. Utterances are used to train the model to identify the most likely intent and the entities to which it should be applied based on a given input. The home assistant application we've been considering might include multiple intents, like the following examples:

| Intent         | Related Utterances                                      | Entities                          |
|----------------|---------------------------------------------------------|----------------------------------|
| Greeting       | "Hello"                                                 |                                  |
|                | "Hi"                                                    |                                  |
|                | "Hey"                                                   |                                  |
|                | "Good morning"                                          |                                  |
| TurnOn         | "Switch the fan on"                                     | fan (device)                     |
|                | "Turn the light on"                                     | light (device)                   |
|                | "Turn on the light"                                     | light (device)                   |
| TurnOff        | "Switch the fan off"                                    | fan (device)                     |
|                | "Turn the light off"                                    | light (device)                   |
|                | "Turn off the light"                                    | light (device)                   |
| CheckWeather   | "What is the weather for today?"                        | today (datetime)                 |
|                | "Give me the weather forecast"                          |                                  |
|                | "What is the forecast for Paris?"                       | Paris (location)                 |
|                | "What will the weather be like in Seattle tomorrow?"    | Seattle (location), tomorrow (datetime) |
| None           | "What is the meaning of life?"                           |                                  |
|                | "Is this thing on?"                                     |                                  |

In this table there are numerous utterances used for each of the intents. The intent should be a concise way of grouping the utterance tasks. Of special interest is the None intent. You should consider always using the None intent to help handle utterances that do not map any of the utterances you have entered. The None intent is considered a fallback, and is typically used to provide a generic response to users when their requests don't match any other intent.

> In a Conversational Language Understanding application, the None intent is created but left empty on purpose. The None intent is a required intent and can't be deleted or renamed. Fill it with utterances that are outside of your domain.

After defining the entities and intents with sample utterances in your Conversational Language Understanding application, you can train a language model to predict intents and entities from user input - even if it doesn't match the sample utterances exactly. You can then use the model from a client application to retrieve predictions and respond appropriately.

## [Getting started with Conversational Language Understanding](https://learn.microsoft.com/en-gb/training/modules/create-language-model-with-language-understanding/2-get-started)

Creating an application with Conversational Language Understanding consists of two main tasks. First you must define entities, intents, and utterances with which to train the language model - referred to as authoring the model. Then you must publish the model so that client applications can use it for intent and entity prediction based on user input.

### Azure resources for Conversational Language Understanding

For each of the authoring and prediction tasks, you need a resource in your Azure subscription. You can use the following types of resource:

- Language Service: A resource that enables you to build apps with industry-leading natural language understanding capabilities without machine learning expertise.
- Cognitive Services: A general cognitive services resource that includes Conversational Language Understanding along with many other cognitive services. You can only use this type of resource for prediction.

The separation of resources is useful when you want to track resource utilization for Language Service use separately from client applications using all Cognitive Services applications.

When your client application uses a Cognitive Services resource, you can manage access to all of the cognitive services being used, including the Language Service, through a single endpoint and key.

### Authoring

After you've created an authoring resource, you can use it to author and train a Conversational Language Understanding application by defining the entities and intents that your application will predict as well as utterances for each intent that can be used to train the predictive model.

Conversational Language Understanding provides a comprehensive collection of prebuilt domains that include pre-defined intents and entities for common scenarios; which you can use as a starting point for your model. You can also create your own entities and intents.

When you create entities and intents, you can do so in any order. You can create an intent, and select words in the sample utterances you define for it to create entities for them; or you can create the entities ahead of time and then map them to words in utterances as you're creating the intents.

You can write code to define the elements of your model, but in most cases it's easiest to author your model using the Language Understanding portal - a web-based interface for creating and managing Conversational Language Understanding applications.

#### Creating intents

Define intents based on actions a user would want to perform with your application. For each intent, you should include a variety of utterances that provide examples of how a user might express the intent.

If an intent can be applied to multiple entities, be sure to include sample utterances for each potential entity; and ensure that each entity is identified in the utterance.
Creating entities

There are four types of entities:

- Machine-Learned: Entities that are learned by your model during training from context in the sample utterances you provide.
- List: Entities that are defined as a hierarchy of lists and sublists. For example, a device list might include sublists for light and fan. For each list entry, you can specify synonyms, such as lamp for light.
- RegEx: Entities that are defined as a regular expression that describes a pattern - for example, you might define a pattern like [0-9]{3}-[0-9]{3}-[0-9]{4} for telephone numbers of the form 555-123-4567.
- Pattern.any: Entities that are used with patterns to define complex entities that may be hard to extract from sample utterances.

#### Training the model

After you have defined the intents and entities in your model, and included a suitable set of sample utterances; the next step is to train the model. Training is the process of using your sample utterances to teach your model to match natural language expressions that a user might say to probable intents and entities.

After training the model, you can test it by submitting text and reviewing the predicted intents. Training and testing is an iterative process. After you train your model, you test it with sample utterances to see if the intents and entities are recognized correctly. If they're not, make updates, retrain, and test again.

### Predicting

When you are satisfied with the results from the training and testing, you can publish your Conversational Language Understanding application to a prediction resource for consumption.

Client applications can use the model by connecting to the endpoint for the prediction resource, specifying the appropriate authentication key; and submit user input to get predicted intents and entities. The predictions are returned to the client application, which can then take appropriate action based on the predicted intent.

## [Exercise - Explore language understanding](https://learn.microsoft.com/en-gb/training/modules/create-language-model-with-language-understanding/3-exercise-create-language-understanding-application)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/create-language-model-with-language-understanding/3a-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/create-language-model-with-language-understanding/4-summary)