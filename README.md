
## Retroactive Commits
This repo was created to make git commits retroactively starting from a given date back one year (365 days).

In order to use this repo 2 things must be changed.

 - Change the date on line 9 of gitManipulator.sh in format YYYY-MM-DD to todays date or date you wish to end the commits on.

 - Change repoPath variable on line 4 in commiter.py to the path of the git repository on your system.

- Change the branch name on line 8 in committer.py to change the branch you want the changes to be made on. 

## Automatic Commits
This Repo also has a Script to make commits which can be made automated with task scheduler (Windows) or a Chron job on (Linux/Mac). This script will require similar changes as committer.py to configure for your machine. 

 - Change repoPath variable on line 4 in autoGit.py to the path of the git repository on your system.

- Change the branch name on line 8 in autoGit.py to change the branch you want the changes to be made on. 