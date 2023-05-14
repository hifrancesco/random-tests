Code scanning is a [static analysis](./static-analysis.md) of every git push.

This ensures that you catch problems (e.g. misconfigurations, errors, vulnerabilities) before they make it into production. GitHub alerts the authorised members about the state of your code and guidance with suggestions on how to fix any errors. 

Code scanning also teaches you how to write code more securely.

To enable code scanning, you need to select **Code scanning alerts** in the **Security** tab and click on **Set up this workflow for CodeQL analysis**.

| Programming Language | Code Scanning Support |
|----------------------|----------------------|
| C                    | :white_check_mark:   |
| C++                  | :white_check_mark:   |
| C#                   | :white_check_mark:   |
| Java                 | :white_check_mark:   |
| JavaScript           | :white_check_mark:   |
| TypeScript           | :white_check_mark:   |
| Python               | :white_check_mark:   |
| Go                   | :white_check_mark:   |


Code scanning automatically analyzes your code for potential security vulnerabilities and coding errors. It helps you identify and address issues early in the development process, ensuring the security and quality of your code.

Code scanning in GitHub Advanced Security:

    Analyzes your code automatically
    Finds security vulnerabilities and coding errors
    Helps you catch issues early
    Ensures secure and high-quality code

By using code scanning, you can proactively identify and fix security vulnerabilities and coding mistakes before they become larger problems.

CodeQL is a static code analysis and query language that allows developers to write queries to analyze code and find potential vulnerabilities, bugs, and security issues in your projects. 

CodeQL treats code as data, enabling deep code analysis and uncovering complex code patterns that may lead to vulnerabilities.

    Static code analysis: CodeQL analyzes code without execution to find potential issues.
    Query language: It has its own expressive query language for code analysis.
    Pre-built queries: GitHub provides a library of queries for various security and quality issues.
    Integration with workflows: CodeQL seamlessly integrates with GitHub workflows and Actions.
    Language support: It supports multiple programming languages like C, C++, Java, Python, and more.
    Collaborative development: Users can share and collaborate on CodeQL queries within the GitHub community.