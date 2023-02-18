import requests
import os

# Replace ORGANIZATION_NAME with the name of your GitHub organization
# Replace ACCESS_TOKEN with your personal access token
org_name = "KPMG-UK"
access_token = os.environ.get("GITHUB_ACCESS_TOKEN")

# API endpoint for getting a list of all repositories for a particular organization
url = f"https://api.github.com/orgs/{org_name}/repos"

# Set the authorization header to include the personal access token
headers = {
    "Authorization": f"Token {access_token}"
}

# Make a GET request to the API endpoint with the authorization header
response = requests.get(url, headers=headers)

# Check if the API request was successful
if response.status_code == 200:
    # Parse the JSON data from the API response
    data = response.json()

    # Loop through the list of repositories
    for repo in data:
        # Display the name of each repository
        print(repo['name'])
else:
    # If the API request was not successful, display an error message
    print("An error occurred while retrieving the list of repositories:", response.status_code)
