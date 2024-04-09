import requests


def number_of_subscribers(subreddit):
    # Construct the URL for the subreddit's information endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Reddit's API restrictions
    headers = {'User-Agent': 'MyBot/0.0.1'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the number of subscribers from the response
        subscribers = data['data']['subscribers']

        # Return the number of subscribers
        return subscribers
    else:
        # If the subreddit is invalid or not found, return 0
        return 0


# Test the function
if __name__ == '__main__':
    subreddit = input("Enter subreddit: ")
    print(number_of_subscribers(subreddit))
