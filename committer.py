import git 
from git import Repo
  
repo = Repo('C:/Users/amcmi/Documents/gitMastery') 
  
existing_branch = repo.heads['master'] 
existing_branch.checkout() 
path = 'C:/Users/amcmi/Documents/gitMastery/autogit.txt'
file = open(path, "a")
file.write("\n0")
file.close()
repo.index.add(['autogit.txt'])

repo.index.commit('auto commit') 
print('Commited successfully') 
