import git 
from git import Repo
repoPath = 'Your Repo Path Here'
  
repo = Repo(repoPath) 
origin = repo.remote(name='origin') 
  
existing_branch = repo.heads['master'] 
existing_branch.checkout() 
path = repoPath + '/autogit.txt'
file = open(path, "a")
file.write("\n0")
file.close()
repo.index.add(['autogit.txt'])

repo.index.commit('auto commit') 
print('Commited successfully') 
origin.push() 
print('Pushed changes to origin')

