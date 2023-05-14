import requests

# Set up GitHub API authentication
username = 'YOUR_GITHUB_USERNAME'
token = 'YOUR_GITHUB_TOKEN'
headers = {'Authorization': f'token {token}'}

# Set the name of the organization and the team
org_name = 'YOUR_ORGANIZATION_NAME'
team_slug = 'YOUR_TEAM_SLUG'

# Make a GET request to the GitHub API to retrieve the list of members in the team
team_members_url = f'https://api.github.com/orgs/{org_name}/teams/{team_slug}/members'
response = requests.get(team_members_url, headers=headers)

# Loop through the list of members and extract their emails
team_emails = []
for member in response.json():
    member_url = member['url']
    response = requests.get(member_url, headers=headers)
    member_data = response.json()
    if member_data['email']:
        team_emails.append(member_data['email'])

print(team_emails)
