# Dogshit = "very poor quality"
# Bullshit = "Not true"
# Horseshit = "Nonsense"
# Apeshit = "Rambunctious"
# Batshit = "Insane"
# Holy_Shit = "WTF"
# No_Shit = "Duh"
# Dipshit = "Idiot"
# Jackshit = "Nothing"
# Shitstorm = "A very bad situation"





### using the requests library to make a GET request to the GitHub API ###
import requests

username = "CloudFrancesco"

response = requests.get(f"https://api.github.com/users/{username}/repos")

if response.status_code == 200:
    repositories = response.json()
    for repo in repositories:
        print(repo["name"])
else:
    print(f"Error: {response.status_code}")