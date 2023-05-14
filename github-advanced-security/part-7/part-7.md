## GitHub Advanced Security features

| Feature                | Public repository                      | Private repository without Advanced Security | Private repository with Advanced Security |
|------------------------|----------------------------------------|---------------------------------------------|-------------------------------------------|
| Code scanning          | Yes                                    | No                                          | Yes                                       |
| Secret scanning        | Yes (limited functionality only)       | No                                          | Yes                                       |
| Dependency review      | Yes                                    | No                                          | Yes                                       |
| Security Overview      | No                                     | No                                          | Yes                                       |


- Code scanning: Automatically detect common vulnerabilities and coding errors
- Secret scanning: Receive alerts when secrets or keys are checked in, exclude files from scanning, and define up to 100 custom patterns
- Dependency review: Show the full impact of changes to dependencies and see details of any vulnerable versions before you merge a pull request
- Security Overview: Review the security configuration and alerts for an organization and identify the repositories at greatest risk

## Set a security policy at the repository level

When setting up a GitHub project is to document how to report security vulnerabilities for the project. To do so, you can add a SECURITY.md file to the project repositories' root, docs, or .github folders.


    In your repository, navigate to Security > Security policy.
    Click Start setup.
    In the new SECURITY.md file, add information about supported versions of your project and how to report a vulnerability.
    Commit the change to the repository.

## Use the Security Overview


    At the organization level, the Security Overview displays aggregate and repository-specific security information for repositories owned by your organization. You can also filter information per security feature.
    At the team level, the Security Overview displays repository-specific security information for repositories that the team has admin privileges for.
    At the repository level, the Security Overview shows which security features are enabled for the repository and offers the option to configure any available security features not currently in use.
