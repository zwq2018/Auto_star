import requests
import re



def extract_github_urls(input_text):
    return re.findall(r"https://github\.com/[^/]+/[^/\s]+", input_text)


def parse(url):
    match = re.match(r"https://github\.com/([^/]+)/([^/]+)", url)
    if match:
        owner, repo = match.groups()
    else:
        owner, repo = None, None
    return owner, repo

def star_github_repo(token, owner, repo):
    """
    Star a GitHub repository using the GitHub API.

    :param token: Your personal GitHub token.
    :param owner: The owner of the repo you want to star.
    :param repo: The name of the repo you want to star.
    """
    url = f"https://api.github.com/user/starred/{owner}/{repo}"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.put(url, headers=headers)

    if response.status_code == 204:
        print(f"Successfully starred {owner}/{repo}!")
    else:
        print(
            f"Failed to star {owner}/{repo}. Response code: {response.status_code}, Response message: {response.text}")

# YOUR Repos want to star 
urls='''
1. https://github.com/xxx/xxx1
2. https://github.com/xxx/xxx2
3. https://github.com/xxx/xxx3
4. https://github.com/xxx/xxx4
5. https://github.com/xxx/xxx5
'''
urls_list = extract_github_urls(URLs)
# Replace 'YOUR_GITHUB_TOKEN' with your actual token
token = ''  # your github token


for i in range(len(urls_list)):
    url = urls_list[i]
    owner, repo = parse(url)
    star_github_repo(token, owner, repo)

