# 5. Write a python program to send request to a web page, and print the JSON value of the resopnse. Print each key value in the response

import requests
r = requests.get('https://api.github.com/')
response = r.json()
print("JSON value of the said response:")
print(r.json())
print("\nEach key of the response:")
print("Current user url:",response['current_user_url'])
print("Current user authorizations html url:",response['current_user_authorizations_html_url'])
print("Authorizations url:",response['authorizations_url'])
print("code_search_url:",response['code_search_url'])
print("commit_search_url:",response['commit_search_url'])
print("Emails url:",response['emails_url'])
print("Emojis url:",response['emojis_url'])
print("Events url:",response['events_url'])
print("Feeds url:",response['feeds_url'])
print("Followers url:",response['followers_url'])
print("Following url:",response['following_url'])
print("Gists url:",response['gists_url'])
print("Issue search url:",response['issue_search_url'])
print("Issues url:",response['issues_url'])
print("Keys url:",response['keys_url'])
print("label search url:",response['label_search_url'])
print("Notifications url:",response['notifications_url'])
print("Organization url:",response['organization_url'])
print("Organization repositories url:",response['organization_repositories_url'])
print("Organization teams url:",response['organization_teams_url'])
print("Public gists url:",response['public_gists_url'])
print("Rate limit url:",response['rate_limit_url'])
print("Repository url:",response['repository_url'])
print("Repository search url:",response['repository_search_url'])
print("Current user repositories url:",response['current_user_repositories_url'])
print("Starred url:",response['starred_url'])
print("Starred gists url:",response['starred_gists_url'])
print("User url:",response['user_url'])
print("User organizations url:",response['user_organizations_url'])
print("User repositories url:",response['user_repositories_url'])
print("User search url:",response['user_search_url'])