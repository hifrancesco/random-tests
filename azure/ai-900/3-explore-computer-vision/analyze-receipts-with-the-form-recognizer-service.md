# [Analyze receipts with the Form Recognizer service](https://learn.microsoft.com/en-gb/training/modules/analyze-receipts-form-recognizer/)

## [Introduction](https://learn.microsoft.com/en-gb/training/modules/analyze-receipts-form-recognizer/1-introduction)

A common problem in many organizations is the need to process receipt or invoice data. For example, a company might require expense claims to be submitted electronically with scanned receipts, or invoices might need to be digitized and routed to the correct accounts department. Typically after a document is scanned, someone will still need to manually enter the extracted text into a database.

Increasingly, organizations with large volumes of receipts and invoices to process are looking for artificial intelligence (AI) solutions that can not only extract the text data from receipts, but also intelligently interpret the information they contain.

Azure's Form Recognizer service can solve for this issue by digitizing fields from forms using optical character recognition (OCR). Azure's OCR technologies extract the contents and structure from forms, such as key, value pairs (eg. Quantity: 3).

Using the Form Recognizer service, we can input an image of a receipt like the one above, and return useful information that might be required for an expense claim, including:

- The name, address, and telephone number of the merchant.
- The date and time of the purchase.
- The quantity and price of each item purchased.
- The subtotal, tax, and total amounts.

## [Get started with receipt analysis on Azure](https://learn.microsoft.com/en-gb/training/modules/analyze-receipts-form-recognizer/2-receipts-azure)

The Form Recognizer in Azure provides intelligent form processing capabilities that you can use to automate the processing of data in documents such as forms, invoices, and receipts. It combines state-of-the-art optical character recognition (OCR) with predictive models that can interpret form data by:

- Matching field names to values.
- Processing tables of data.
- Identifying specific types of field, such as dates, telephone numbers, addresses, totals, and others.

Form Recognizer supports automated document processing through:

- A pre-built receipt model that is provided out-of-the-box, and is trained to recognize and extract data from sales receipts.
- Custom models, which enable you to extract what are known as key/value pairs and table data from forms. Custom models are trained using your own data, which helps to tailor this model to your specific forms. Starting with only five samples of your forms, you can train the custom model. After the first training exercise, you can evaluate the results and consider if you need to add more samples and re-train.

### Azure resources to access Form Recognizer services

To use the Form recognizer, you need to either create a Form Recognizer resource or a Cognitive Services resource in your Azure subscription. Both resource types give access to the Form Recognizer service.

After the resource has been created, you can create client applications that use its key and endpoint to connect submit forms for analysis.

### Using the pre-built receipt model

Currently the pre-built receipt model is designed to recognize common receipts, in English, that are common to the USA. Examples are receipts used at restaurants, retail locations, and gas stations. The model is able to extract key information from the receipt slip:

- time of transaction
- date of transaction
- merchant information
- taxes paid
- receipt totals
- other pertinent information that may be present on the receipt
- all text on the receipt is recognized and returned as well

Use the following guidelines to get the best results when using a custom model.

- Images must be JPEG, PNG, BMP, PDF, or TIFF formats
- File size must be less than 50 MB
- Image size between 50 x 50 pixels and 10000 x 10000 pixels
- For PDF documents, no larger than 17 inches x 17 inches

There is a free tier subscription plan for the receipt model along with paid subscriptions. For the free tier, only the first two pages will be processed when passing in PDF or TIFF formatted documents.

## [Exercise - Explore form recognition](https://learn.microsoft.com/en-gb/training/modules/analyze-receipts-form-recognizer/3-analyze-receipts)

## [Knowledge check](https://learn.microsoft.com/en-gb/training/modules/analyze-receipts-form-recognizer/3a-knowledge-check)

## [Summary](https://learn.microsoft.com/en-gb/training/modules/analyze-receipts-form-recognizer/4-summary)