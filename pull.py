import os
from github import Github
user=input("enter user name : ")
Password=input("enter password : ")
repoName=input("enter repository name : ")
source_branch=input("enter source branch master/main : ")
target_branch=input("enter branch name :")
token= input("enter token :")
url= input("enter url :")
path = "pull.py"

os.system("git init")
os.system(f"git clone {url}")

g=Github(token)
repo=g.get_user().get_repo(repoName)
sb=repo.get_branch(source_branch)
repo.create_git_ref(ref='refs/heads/' + target_branch,sha=sb.commit.sha)
print("branch created successfully")
os.system(f"git remote add {url}")
os.system(f"git add origin {path}")
os.system("git commit -m 'new_file' ")
os.system(f"git push origin --all")

