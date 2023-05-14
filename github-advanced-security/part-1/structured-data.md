Structured data refers to data that is organized and formatted in a specific way, usually following a predefined schema or data model.

In the context of secrets and workflows, structured data typically refers to secrets that are stored in a structured format, such as JSON or YAML. This means that the secret itself contains multiple fields or attributes with associated values.

The statement "Do not use structured data as a secret" advises against storing secrets in a format where the secret itself is structured data. For example, if you have a secret that contains sensitive information like API keys, usernames, or passwords, it is recommended to store each piece of sensitive information as separate secrets rather than storing them all together as structured data.

Storing secrets as structured data can cause issues with secret redaction within logs. Secret redaction is a security feature that automatically hides sensitive information, replacing it with asterisks or other masking characters, to prevent accidental exposure in logs or other output.

To ensure proper security and avoid issues with secret redaction, it is best practice to store secrets as individual, separate values rather than as structured data. This allows for more effective management and redaction of sensitive information within workflows and logs.