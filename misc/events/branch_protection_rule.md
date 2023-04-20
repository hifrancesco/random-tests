### Example 1

```yml
name: Branch Protection Rule Example
on:
  branch_protection_rule:
    types: [created, edited]

jobs:
  check_branch_protection:
    runs-on: ubuntu-latest
    steps:
    - name: Check Branch Protection
      run: |
        echo "Branch protection rule was ${{ job.event.action }}d for branch ${{ job.event.branch }}."
        echo "Required reviews: ${{ job.event.required_review_count }}"
        echo "Restrictions: ${{ job.event.restrictions }}"
```

In this example, the workflow is triggered whenever a branch protection rule is created or edited. The `jobs` section defines a single job called `check_branch_protection` that runs on the latest version of Ubuntu. The job contains a single step that runs a command to print information about the branch protection rule that was created or edited.

The `{{ job.event.action }}` variable is used to get the action that triggered the event (created or edited)
`{{ job.event.branch }}` variable is used to get the branch name.
`{{ job.event.required_review_count }}` variable is used to get the required number of reviews.
`{{ job.event.restrictions }}` variable is used to get the restrictions set for the branch.

This is a basic example, you can also use the branch protection rule event to trigger other actions, such as running tests or deploying code, depending on your specific requirements.

### Example 2

```yml
name: Branch Protection Rule Example
on:
  branch_protection_rule:
    types: [created, edited]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Check Branch
      run: |
        if [ "${{ job.event.branch }}" == "production" ]; then
          echo "Deploying to production"
          # add commands to deploy code to production
        else
          echo "Deployment not required"
        fi
    - name: Check Restrictions
      run: |
        if [ -n "${{ job.event.restrictions }}" ]; then
          echo "Restrictions set for branch ${{ job.event.branch }}: ${{ job.event.restrictions }}"
        else
          echo "No restrictions set for branch ${{ job.event.branch }}"
        fi
```

In this example, the workflow is triggered whenever a branch protection rule is created or edited. The jobs section defines a single job called deploy that runs on the latest version of Ubuntu. The job contains two steps:

1. The first step uses an if statement to check the branch name, if the branch name is "production" it will deploy the code to the production environment.

2. The second step uses an if statement to check if any restrictions have been set for the branch, if yes it will print the restrictions else it will print "No restrictions set for branch"

This is an example of how you can use the `branch_protection_rule` event to trigger specific actions like deploying code only to production environment if the branch name is p`roduction` and also check if there are any restrictions set for the branch.

You can customize this workflow according to your specific requirements.