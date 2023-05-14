    git init - Initializes a new Git repository in the current directory.
    git clone <repository> - Clones a Git repository from a remote location.
    git add <file> - Adds a file to the staging area.
    git add . - Adds all changes to the staging area.
    git commit -m "<message>" - Commits the changes in the staging area with a commit message.
    git status - Shows the status of the working directory and staging area.
    git diff - Shows the differences between the working directory and staging area.
    git diff <commit> - Shows the differences between the working directory and a specific commit.
    git log - Shows the commit history.
    git log --oneline - Shows the commit history in one-line format.
    git log --graph - Shows the commit history with a graph of branch and merge history.
    git branch - Shows a list of local branches.
    git branch <branch-name> - Creates a new branch.
    git branch -d <branch-name> - Deletes a branch.
    git checkout <branch-name> - Switches to a different branch.
    git checkout -b <branch-name> - Creates a new branch and switches to it.
    git merge <branch-name> - Merges changes from a different branch into the current branch.
    git remote - Shows a list of remote repositories.
    git remote add <name> <url> - Adds a new remote repository.
    git push <remote> <branch> - Pushes changes to a remote repository.
    git push --all <remote> - Pushes all local branches to a remote repository.
    git push --force <remote> <branch> - Forces a push to a remote repository, overwriting existing history.
    git pull <remote> <branch> - Fetches changes from a remote repository and merges them into the current branch.
    git fetch <remote> - Fetches changes from a remote repository without merging them.
    git diff HEAD - Shows the differences between the working directory and the last commit.
    git blame <file> - Shows who last modified each line of a file, and when.
    git remote show <remote> - Shows information about a remote repository.
    git config --global user.name "<name>" - Sets the username to be used for all Git repositories.
    git config --global user.email "<email>" - Sets the email address to be used for all Git repositories.
    git config --global core.editor <editor> - Sets the text editor to be used for commit messages.
    git config --list - Shows a list of all Git configuration settings.
    git fetch --prune - Fetches changes from a remote repository and removes any branches that no longer exist on the remote.
    git checkout <commit> - Checks out a specific commit, creating a detached HEAD state.
    git checkout -- <file> - Discards changes to a specific file in the working directory.
    git rm <file> - Removes a file from the working directory and the repository.
    git mv <old-file> <new-file> - Renames a file in the working directory and the repository.
    git tag <tag-name> - Creates a new lightweight tag.
    git show <commit> - Shows the changes
    git stash - Saves changes that are not yet committed in a "stash," allowing you to work on something else without committing unfinished changes.
    git stash apply - Applies the most recently created stash to the working directory.
    git stash list - Lists all stashes.
    git stash drop - Deletes the most recently created stash.
    git stash pop - Applies and deletes the most recently created stash.
    git reset <file> - Unstages changes to a specific file in the staging area.
    git reset --soft <commit> - Resets the current branch to a specific commit, leaving changes in the staging area and working directory.
    git reset --mixed <commit> - Resets the current branch to a specific commit, leaving changes in the working directory but removing changes from the staging area.
    git reset --hard <commit> - Resets the current branch to a specific commit, discarding all changes in the staging area and working directory.
    git revert <commit> - Reverts changes from a specific commit by creating a new commit that undoes the changes.
    git cherry-pick <commit> - Applies changes from a specific commit to the current branch.
    git bisect - Binary searches the commit history to find a specific commit that introduced a bug.
