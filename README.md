# Git Mastery

If you have some cool git manipulation Ideas create a PR and add them to the list of [future implementations](./todo.md).
Additionally we would love if you contributed and implemented any of the ideas on the [future implementation list](./todo.md) Please include a short explaination of your implementation on this README.md.

## PreRequisites:
 - [Python installation](https://www.python.org/downloads/)
 - GitPython package instalation. Use this command to install: `pip install gitpython`

## Retroactive Commits
This repo was originally created to make git commits retroactively starting from a given date back one year (365 days).

In order to use this repo 3 things must be changed.

 - Change the date on line 9 of [retroactive.sh](./committer.py) in format YYYY-MM-DD to todays date or date you wish to end the commits on.

 - Change repoPath variable on line 4 in [commiter.py](./committer.py) to the path of the git repository on your system.

 - Change the branch name on line 8 in [commiter.py](./committer.py) to change the branch you want the changes to be made on. 

- Once these are configured properly you can run the shell script by using the command `./retroactive.sh`

## Automatic Commits
This Repo also has a Script to make commits which can be made automated with [Task Scheduler](https://en.wikipedia.org/wiki/Windows_Task_Scheduler) (Windows) or a [Cron job](https://en.wikipedia.org/wiki/Cron) on (Linux/Mac). 
Two changes are required to configure for your machine. 

 - Change repoPath variable on line 4 in [autoGit.py](./autoGit.py) to the path of the git repository on your system.

- Change the branch name on line 8 in [autoGit.py](./autoGit.py) to change the branch you want the changes to be made on. 

- Once these are configured properly you can run the python script by using the command `python put/path/here/to/autoGit.py`. make sure the second argument is the path to the autoGit.py.