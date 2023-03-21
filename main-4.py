import requests
import csv

# Set up GitHub API authentication
username = 'YOUR_GITHUB_USERNAME'
token = 'YOUR_GITHUB_TOKEN'
headers = {'Authorization': 'token ' + token}

# Set the name of the organization and the team
org_name = 'YOUR_ORGANIZATION_NAME'
team_slug = 'YOUR_TEAM_SLUG'

# Get the list of team members from the GitHub API
members_url = f'https://api.github.com/orgs/{org_name}/teams/{team_slug}/members'
response = requests.get(members_url, headers=headers)
members = response.json()

# Create a list to store the GitHub handles, names, and emails
handles_names_emails = []

# Loop through the list of members and append their handles, names, and emails to the list
for member in members:
    member_url = member['url']
    response = requests.get(member_url, headers=headers)
    member_data = response.json()
    if member_data['email']:
        handles_names_emails.append([member_data['login'], member_data['name'], member_data['email']])
    else:
        handles_names_emails.append([member_data['login'], member_data['name'], ''])

# Write the data to a CSV file
with open('github_handles_names_emails.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['GitHub Handle', 'Name', 'Email'])
    writer.writerows(handles_names_emails)
