### Example 1

```yml
name: Check Run Example
on:
  check_run:
    types: [completed]

jobs:
  notify_status:
    runs-on: ubuntu-latest
    steps:
    - name: Notify Check Status
      run: |
        echo "Check run for ${{ job.event.check_name }} has ${{ job.event.status }} with conclusion ${{ job.event.conclusion }}"
        if [ "${{ job.event.status }}" == "completed" ]; then
          if [ "${{ job.event.conclusion }}" == "success" ]; then
            echo "Check run was successful"
            # add commands to notify success
          else
            echo "Check run failed"
            # add commands to notify failure
          fi
        fi
```

In this example, the workflow is triggered whenever a check run is completed. The jobs section defines a single job called notify_status that runs on the latest version of Ubuntu. The job contains a single step that runs a command to print information about the check run status and conclusion. It also uses an if statement to check if the check run was successful or failed and notify the appropriate parties.

### Example 2

```yml
name: Check Run Example
on:
  check_run:
    types: [requested]

jobs:
  run_checks:
    runs-on: ubuntu-latest
    steps:
    - name: Run tests
      run: |
        echo "Running tests for ${{ job.event.check_name }}"
        # add commands to run tests
    - name: Run linting
      run: |
        echo "Running linting for ${{ job.event.check_name }}"
        # add commands to run linting
    - name: Run security scans
      run: |
        echo "Running security scans for ${{ job.event.check_name }}"
        # add commands to run security scans
```

In this example, the workflow is triggered whenever a check run is requested. The jobs section defines a single job called run_checks that runs on the latest version of Ubuntu. The job contains three steps that run commands to run tests, linting and security scans respectively.

You can customize these workflows according to your specific requirements.

It's worth noting that check_run event triggers are also available for check_suite events, which allows you to trigger workflows based on check_suite events such as requested, rerequested, completed and others, giving you more flexibility on how to automate your workflows.