Push protection lets you find and remove secrets before the code is even added to your repositories. 

When you do a `git push`, GitHub scans the code to be added to your repository for secrets. If the code contains a secret, then it blocks the code from being committed and prompts the developer to take action. 

You can remove the secret, identify the detected secret as a false positive or a test key, or bypass the arlet. 

Administrators can configure Githbu push protection to send alert notifications if a developer bypasses the block.