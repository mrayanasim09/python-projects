# This code is made by MRayan Asim
# Packages needed:
# pip install requests
import requests


def analyze_github_repository(owner, repo):
    # API endpoint for GitHub repository
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"

    # Send GET request to fetch repository data
    response = requests.get(repo_url)

    if response.status_code == 200:
        # Parse JSON response
        repository = response.json()

        # Extract desired information
        name = repository.get("name")
        description = repository.get("description")
        stars = repository.get("stargazers_count")
        forks = repository.get("forks_count")
        watchers = repository.get("subscribers_count")

        # API endpoint for repository views
        views_url = f"https://api.github.com/repos/{owner}/{repo}/traffic/views"

        # Send GET request to fetch repository views
        views_response = requests.get(views_url)
        if views_response.status_code == 200:
            views_data = views_response.json()
            views = views_data.get("count")
        else:
            views = "N/A"

        # Print repository information
        print(f"Repository: {name}")
        print(f"Description: {description}")
        print(f"Stars: {stars}")
        print(f"Forks: {forks}")
        print(f"Watchers: {watchers}")
        print(f"Views: {views}")
    else:
        print("Error: Repository not found or API request failed")


# usage
owner = input("Enter the name of the owner ")
repo = input("Enter the name of the repository: ")
analyze_github_repository(owner, repo)
