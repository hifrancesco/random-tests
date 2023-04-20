# github-actions-test

### ci-cd.yml
This template demonstrates a basic CI/CD pipeline that runs on every push to the main branch and every pull request to the main branch. The pipeline has two jobs: "build" and "deploy". The "build" job runs a series of steps that check out the code, set up Node.js, install dependencies, build the application, and run tests. The "deploy" job runs after the "build" job and deploys the application to production.

You can customize this template to suit your specific needs by modifying the on trigger events, adding more jobs or steps, and updating the commands in the run actions to match your project requirements.

You can also use this template as a starting point and refer to the official GitHub Actions documentation to learn more about the different options and configurations available for building and customizing your workflows.

### Test Test Test


```py
variable "instances" {
  type = list(string)
  default = ["instance1", "instance2"]
}

resource "aws_instance" "example" {
  dynamic "instance" {
    for_each = var.instances
    content {
      instance_id = instance.value
      ami = "ami-0ff8a91507f77f867"
      instance_type = "t2.micro"
    }
  }
}

```

https://dev.to/github/10-standout-github-profile-readmes-h2o