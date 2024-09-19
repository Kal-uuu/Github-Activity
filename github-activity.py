import argparse

import requests


# fetches GitHub activity
def fetch_github_activity(users):
    try:
        url = 'https://api.github.com/users/' + users + '/events'
        response = requests.get(url)

        if response.status_code == 200:
            print("Request succeeded")
            # stores events
            events = response.json()
            return events

        else:
            print(f"Request failed: {response.status_code}")
            return None
    # checks for errors
    except requests.exceptions.HTTPError as e:
        print(f"Request failed: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def parse_events(events):
    if not events:
        print("No events found")
        return None

    else:
        for event in events:
            event_type = event['type']
            repo_name = event['repo']['name']
            print(f"{event_type} on repository: {repo_name}")


def main():
    # Give a brief description of the code
    # To use type "python github-activity.py --help"
    parser = argparse.ArgumentParser(description="Fetch GitHub Activity")
    parser.add_argument("username", help="GitHub Username to fetch activity for")
    args = parser.parse_args()

    events = fetch_github_activity(args.username)
    if not events:
        print("No events found")
    else:
        parse_events(events)


if __name__ == "__main__":
    main()
