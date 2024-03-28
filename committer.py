import git 
from git import Repo

repoPath = 'C:/Users/amcmi/Documents/pythonScripts/gitMastery'

repo = Repo(repoPath) 
  
existing_branch = repo.heads['master'] 
existing_branch.checkout() 
path = repoPath + '/autogit.txt'
file = open(path, "a")
file.write("\n0")
file.close()
repo.index.add(['autogit.txt'])

repo.index.commit('auto commit') 
print('Commited successfully') 
