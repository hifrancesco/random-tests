import requests
import csv

# Add your access token here
access_token = 'YOUR_ACCESS_TOKEN'

# The name of the organization and team whose members you want to list
org_name = 'ORGANIZATION_NAME'
team_name = 'TEAM_NAME'

# Get the team ID using the GitHub API
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(f'https://api.github.com/orgs/{org_name}/teams', headers=headers)
response.raise_for_status()
team_id = None
for team in response.json():
    if team['name'] == team_name:
        team_id = team['id']
        break
if not team_id:
    print('Team not found')
    exit()

# Get the members of the team using the GitHub API
response = requests.get(f'https://api.github.com/teams/{team_id}/members', headers=headers)
response.raise_for_status()
members = [member['login'] for member in response.json()]

# Write the members to a CSV file
with open('team_members.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['GitHub Handle'])
    for member in members:
        writer.writerow([f'{member}'])
