# git

* `git add .`: Ading all unwatched/changed files to the git staging area
* `git commit -m "my comment"`: Writes staged files into the git repo
* `git push`: pushes current version to a remote repo (e.g. github)
* `git status`:  Show curent status of the git repo
* `git clone {url}`: clone a github repository to local machine, see [docs.github.com](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
* `git branch dev`: Adds a new branch 'dev' derived from the current working branch (e.g. main)
* `git checkout {branchname}`: changes current branch to {branchname}
* `git merge {branchname}`: merges {branchname} into current branch (usually checkout main branch and merge dev branch into main branch)
* `git rm {filename}`: deletes file from index/repository