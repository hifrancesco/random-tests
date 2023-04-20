Here is an example of a workflow.yml file that uses the discussion_comment event trigger and performs different actions based on the type of activity:

```yml
name: Discussion Comment Workflow

on:
  discussion_comment:
    types: [created, edited, deleted]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Check activity type
      if: ${{ toJson(github.event.action) == 'created' }}
      run: echo "Comment created"

    - name: Check activity type
      if: ${{ toJson(github.event.action) == 'edited' }}
      run: echo "Comment edited"

    - name: Check activity type
      if: ${{ toJson(github.event.action) == 'deleted' }}
      run: echo "Comment deleted"
```

In this example, the workflow is triggered whenever a comment is created, edited, or deleted in a discussion. The job build runs on the latest version of Ubuntu and has 3 steps. The first step checks if the activity type is created, the second step checks if the activity type is edited, and the third step checks if the activity type is deleted. If the condition is true, it will run the corresponding command. This is just an example, you can replace the echo command with the desired action you want to perform based on the activity type.