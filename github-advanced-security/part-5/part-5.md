## Create a database by using CodeQL to extract a single relational representation of each source file in the codebase

## Run CodeQL in a database to find problems in your source code and find potential security vulnerabilities

## Understand CodeQL scan results using queries created by GitHub, or your own custom queries

---

How to prepare a database for CodeQL
•	CodeQL treats code like data and helps identify security vulnerabilities and errors.
•	To analyze code using CodeQL, you need to create a database containing the code's relational data.
•	The CodeQL CLI is used to analyze code and generate a database representation.
•	You need to install and set up the CodeQL CLI and check out the version of your codebase to be analyzed.
•	For compiled languages, the code directory should be ready to build with dependencies installed.
•	For interpreted languages, the extractor runs directly on the source code, capturing an accurate representation.
•	Set up the CodeQL CLI by downloading the zip package and creating a CodeQL directory.
•	Obtain a local copy of the CodeQL queries repository and extract the zip archive.
•	Launch the CodeQL CLI using the extracted files or by adding it to your PATH.
•	Verify the setup by executing CodeQL CLI subcommands to ensure languages and QL packs are available.
•	Create a CodeQL database using the CLI command: "codeql database create <database> --language=<language-identifier>"
•	Understand that databases contain relational data and have a specific schema for each language.
•	CodeQL databases have expressions and statements tables, providing an abstraction layer for analysis.
•	Consider potential shortfalls in database creation, such as using a language matrix and autobuild behavior.
•	Optionally, use the CodeQL extension in Visual Studio Code for compiling and running queries.

## Create a database

```bash
codeql database create <database> --language=<language-identifier>
```

## Extractors

An extractor is a tool that produces the relational data and source reference for each input file, from which a CodeQL database can be built.


# Run CodeQL in a database

There are two important types of queries:

- Alert queries: highlight issues in specific locations of your code.
- Path queries: describe the flow of information between a source and a sink in your code.

•	CodeQL queries have metadata properties that provide information about their purpose and how to interpret and display the results.
•	Queries are written in QL, a programming language similar to SQL, and support logical formulas, predicates, recursion, and aggregates.
•	Path queries are used to visualize the flow of information through a codebase and require defining path graph modules, source and sink nodes, and message explanations.
•	To analyze a CodeQL database, you can use the codeql database analyze command and obtain results in Static Analysis Results Interchange Format (SARIF) or another interpreted format.
•	SARIF files can be used to share static analysis results and can have categories to distinguish different analyses.
•	SARIF results can be uploaded to GitHub using the codeql github upload-results command, requiring authentication with a GitHub App or personal access token.
•	Third-party SARIF results can also be uploaded, but they need to follow the specific SARIF 2.1.0 JSON schema and include fingerprint data to avoid duplicate alerts in code scanning.
