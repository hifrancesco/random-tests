Depedabot uses the dependency graph and GitHub Advisory Database to provide 3 features:

- dependanbot alerts: notify you of vulnerabilities in public repos
- security updates: automatically generate PR 
- version updates: update all packages
in version updates, you need to create a `dependabot.yml` file. It tells dependanbot where to find the manifest or lock files.

Dependabot alerts are generated through:

- when a new vulnerability is added to the GitHub Advisory Databse
- the dependecy graph changes

These features are not substitutes for human review. Dependabots are enabled for public repos by default. You can set them for private ones too for GH cloud/sever. It has read-only analysis. 

Use GitHub Connect to set up alerts for GitHub Enterprise Server. 

