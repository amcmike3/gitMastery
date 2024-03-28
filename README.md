# Git Manipulator

If you have some cool Git manipulation Ideas create a PR and add them to the list of [future implementations](./todo.md).
Additionally we would love if you contributed and implemented any of the ideas on the [future implementation list](./todo.md) Please include a short explaination of it on this README.md.

## PreRequisites:
 - [Python instalation](https://www.python.org/downloads/)
 - GitPython package instalation. Use this command to install: `pip install gitpython`

## Retroactive Commits
This repo was originally created to make git commits retroactively starting from a given date back one year (365 days).

In order to use this repo 3 things must be changed.

 - Change the date on line 9 of [gitManipulator.sh](./committer.py) in format YYYY-MM-DD to todays date or date you wish to end the commits on.

 - Change repoPath variable on line 4 in [commiter.py](./committer.py) to the path of the git repository on your system.

 - Change the branch name on line 8 in [commiter.py](./committer.py) to change the branch you want the changes to be made on. 

- Once these are configured properly you can run the shell script by using the command `./gitManipulator.sh`

## Automatic Commits
This Repo also has a Script to make commits which can be made automated with task scheduler (Windows) or a Chron job on (Linux/Mac). This script will require similar changes as committer.py to configure for your machine. 

 - Change repoPath variable on line 4 in [autoGit.py](./autoGit.py) to the path of the git repository on your system.

- Change the branch name on line 8 in [autoGit.py](./autoGit.py) to change the branch you want the changes to be made on. 

- Once these are configured properly you can run the python script by using the command `python put/path/here/to/autoGit.py`. make sure the second argument is the path to the autoGit.py.