summary of a repository's manifest and lock files

Dependencies -> ecosystem and packages the repository depends on
Dependents are the repositories and packages that depend on the repository

uses the information from your lock and manifest files to provide a list of three kinds of dependencies:

1. direct dependencies explicitly defined in a manifest or lock file
2. indirect dependencies are dependencies used by packages that are dependencies of your project
3. vendored dependencies that are checked into a specific directory in your repository but aren't referenced in your manifest file (only available for some package managers).
