# This code is made by MRayan Asim
# Packages needed:
# pip install requests
import requests

# Default timeout for HTTP requests (seconds)
DEFAULT_TIMEOUT = 10


def analyze_github_repository(owner, repo, timeout=DEFAULT_TIMEOUT):
    """
    Analyze a GitHub repository and display its statistics.

    Args:
        owner: GitHub repository owner
        repo: Repository name
        timeout: Request timeout in seconds (default: 10)
    """
    # API endpoint for GitHub repository
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        # Send GET request to fetch repository data with timeout
        response = requests.get(repo_url, timeout=timeout)

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

            try:
                # Send GET request to fetch repository views with timeout
                views_response = requests.get(views_url, timeout=timeout)
                if views_response.status_code == 200:
                    views_data = views_response.json()
                    views = views_data.get("count")
                else:
                    views = "N/A"
            except requests.Timeout:
                views = "Timeout"
            except requests.RequestException:
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
            print(f"Status code: {response.status_code}")
    except requests.Timeout:
        print(f"Error: Connection timed out after {timeout} seconds.")
    except requests.ConnectionError:
        print("Error: Unable to connect to GitHub API.")
    except requests.RequestException as e:
        print(f"Error: {e}")


# usage
if __name__ == "__main__":
    owner = input("Enter the name of the owner: ")
    repo = input("Enter the name of the repository: ")
    analyze_github_repository(owner, repo)
