# [Translate text and speech](https://learn.microsoft.com/en-gb/training/modules/translate-text-with-translation-service/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/translate-text-with-translation-service/1-introduction)

As organizations and individuals increasingly need to collaborate with people in other cultures and geographic locations, the removal of language barriers has become a significant problem.

One solution is to find bilingual, or even multilingual, people to translate between languages. However the scarcity of such skills, and the number of possible language combinations can make this approach difficult to scale. Increasingly, automated translation, sometimes known as machine translation, is being employed to solve this problem.

### Literal and semantic translation

Early attempts at machine translation applied literal translations. A literal translation is where each word is translated to the corresponding word in the target language. This approach presents some issues. For one case, there may not be an equivalent word in the target language. Another case is where literal translation can change the meaning of the phrase or not get the context correct.

For example, the French phrase "éteindre la lumière" can be translated to English as "turn off the light". However, in French you might also say "fermer la lumiere" to mean the same thing. The French verb fermer literally means to "close", so a literal translation based only on the words would indicate, in English, "close the light"; which for the average English speaker, doesn't really make sense, so to be useful, a translation service should take into account the semantic context and return an English translation of "turn off the light".

Artificial intelligence systems must be able to understand, not only the words, but also the semantic context in which they are used. In this way, the service can return a more accurate translation of the input phrase or phrases. The grammar rules, formal versus informal, and colloquialisms all need to be considered.

### Text and speech translation

Text translation can be used to translate documents from one language to another, translate email communications that come from foreign governments, and even provide the ability to translate web pages on the Internet. Many times you will see a Translate option for posts on social media sites, or the Bing search engine can offer to translate entire web pages that are returned in search results.

Speech translation is used to translate between spoken languages, sometimes directly (speech-to-speech translation) and sometimes by translating to an intermediary text format (speech-to-text translation).

## [Get started with translation in Azure](https://learn.microsoft.com/en-gb/training/modules/translate-text-with-translation-service/2-get-started-azure)

Microsoft Azure provides cognitive services that support translation. Specifically, you can use the following services:

- The Translator service, which supports text-to-text translation.
- The Speech service, which enables speech-to-text and speech-to-speech translation.

### Azure resources for Translator and Speech

Before you can use the Translator or Speech services, you must provision appropriate resources in your Azure subscription.

There are dedicated Translator and Speech resource types for these services, which you can use if you want to manage access and billing for each service individually.

Alternatively, you can create a Cognitive Services resource that provides access to both services through a single Azure resource, consolidating billing and enabling applications to access both services through a single endpoint and authentication key.

### Text translation with the Translator service

The Translator service is easy to integrate in your applications, websites, tools, and solutions. The service uses a Neural Machine Translation (NMT) model for translation, which analyzes the semantic context of the text and renders a more accurate and complete translation as a result.

#### Translator service language support

The Translator service supports text-to-text translation between more than 60 languages. When using the service, you must specify the language you are translating from and the language you are translating to using ISO 639-1 language codes, such as en for English, fr for French, and zh for Chinese. Alternatively, you can specify cultural variants of languages by extending the language code with the appropriate 3166-1 cultural code - for example, en-US for US English, en-GB for British English, or fr-CA for Canadian French.

When using the Translator service, you can specify one from language with multiple to languages, enabling you to simultaneously translate a source document into multiple languages.

#### Optional Configurations

The Translator API offers some optional configuration to help you fine-tune the results that are returned, including:

- Profanity filtering. Without any configuration, the service will translate the input text, without filtering out profanity. Profanity levels are typically culture-specific but you can control profanity translation by either marking the translated text as profane or by omitting it in the results.
- Selective translation. You can tag content so that it isn't translated. For example, you may want to tag code, a brand name, or a word/phrase that doesn't make sense when localized.

### Speech translation with the Speech service

The Speech service includes the following application programming interfaces (APIs):

- Speech-to-text - used to transcribe speech from an audio source to text format.
- Text-to-speech - used to generate spoken audio from a text source.
- Speech Translation - used to translate speech in one language to text or speech in another.

You can use the Speech Translation API to translate spoken audio from a streaming source, such as a microphone or audio file, and return the translation as text or an audio stream. This enables scenarios such as real-time closed captioning for a speech or simultaneous two-way translation of a spoken conversation.

#### Speech service language support

As with the Translator service, you can specify one source language and one or more target languages to which the source should be translated. You can translate speech into [over 60 languages](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#speech-translation).

The source language must be specified using the extended language and culture code format, such as es-US for American Spanish. This requirement helps ensure that the source is understood properly, allowing for localized pronunciation and linguistic idioms.

The target languages must be specified using a two-character language code, such as en for English or de for German.

## [Exercise - Explore translation](https://learn.microsoft.com/en-gb/training/modules/translate-text-with-translation-service/3-exercise-translate-text-use-azure)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/translate-text-with-translation-service/3a-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/translate-text-with-translation-service/4-summary)