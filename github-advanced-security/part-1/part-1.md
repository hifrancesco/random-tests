# Introduction

GitHub Advanced Security is a suite of tools and faetures that gives you the ability to identify security vulnerabilities in your [codebase and environment.](./codebase-environment.md)

Benefits:
- stay ahead of threats and breaches
- use open-source software securely
- leverage expertise of the security community

GitHub Advanced Security promotes scurity best practices that help shape a security-minded culture. This focuses in 3 areas:

- **Supply Chain**: in the context of software development, this refers to the integration of any third-party or open-source software. You rely on many components you didn't produce. These components are called *dependencies*. You need to actively review them for vulnerabilities. 
- **Code**
- **Environments**

[**Dependency graphs**](./dependecy-graphs.md) provide insights into your project's [direct and indirect package dependencies](./direct-indirect-package-dependencies.md) and their current state. This graph displays a summary of manifest and lock files in the project's ecosystem, repository, and packages.


[**GitHub Advisory Database**]() is a dedicated team that lists security vulnerabilities mapped to packages tracked by dependency graphs. A threat is ranked by:

- critical
- high
- medium
- low

This database updates this list regularly using the *National Vulnerability Database* and the *npm* security advisory database.

Dependabot is part of the supply chain. It detects vulnerable dependencies by examing the manifest file (e.g. package.json). Then, it consults the GitHub Advisory Database to see if the detected dependencies have a flag that indicate if they're vulnerable or out-of-date. Dependanbot alerts the authorised members via email.

After security the *supply chain*, the next area is *code analysis* through [**code scanning**](./code-scanning.md), [**secret scanning**](./secret-scanning.md), [**push protection**](./push-protection.md).

- DEPENDABOT (Dependency Graph)
- CODE SCANNING [CodeQL](./code-scanning.md)
- SECRET SCANNING


## Features behind the scenes

They work behind the scenes to improve the performance of your platform.


| Feature | Description |
|-|-|
| CodeQL | CodeQL is the engine behind code scanning that treats code like data. When code scanning is active on your repository, CodeQL analyzes it without you needing to write any queries. Templates make it easy to output code scanning results on your repository. |
| Third-party tool integration | GitHub is flexible. You can integrate optional third-party analysis tools that output SARIF data.|

## Secure your workflow

- Protection rules
- Environment secrets
- Wait timers

---

- Do NOT use [structured data](./structured-data.md) as a secret. 
- Declare the secrets that your workflow uses. When you register a secret, you provide a name or identifier for it, which can be referenced within your workflow.

```yml
env:
  SECRET_ONE: ${{ secrets.MY_SECRET_ONE }}
  SECRET_TWO: ${{ secrets.MY_SECRET_TWO }}
```

- Use required reviewers to protect environment secrets

---

## Licenses

- Self-hosted runners only run on private repos
- Anyone with read access can compromise the runner environment and gain access to secrets

GitHub Advanced Security features are of charge for public repositories, so open-source projects can benefit. 

For private repos, you need a licence which is available by GitHub Enterprise Cloud/Server.

## Organisational Culture around security

Develop an understanding of *shifting left* in the SDLC by adopting a security mindset, adopting security practices early and integrate security into the design phase. 

| Facet                       | Comment                                                                             |
|-----------------------------|-------------------------------------------------------------------------------------|
| Scope of team involvement  | Teams shift left. Each role from design to deployment is concerned with security.    |
| Prioritization              | Throughout all stages of development, measures are in place to protect assets.       |
| Documentation               | Standards and guidelines are in writing. Teams know the process to report bugs.     |
| Tooling                     | The development platform enforces standards and keeps code and environments secure. |

### Security policies

You may want to specify who can push code to or delete a branch. Store policy detials in the SECURITY.md file. This is where you include instructions on how to report bugs. 

### Enforce policies

Administrators can set up protected branches at the organisational level and tests such as code scanning must pass before merging branches. 

A reviewer must approve PRs before it is merged to any environment (e.g. prod).

## [Use security advisory is powered by the GitHub Advisory Database](./security-advisory.md)

A security advisory is a notification or report that provides information about a vulnerability discovered in a project's dependencies or codebase.

When you use this, you ensure that any bug is not expoted to the public before you can fix it. After resolving the issue, the security advisory is published back into the GitHub Advisory Database so that affected external parties can take precautions too.


