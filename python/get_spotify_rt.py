# Gets SPOTIFY_REFRESH_TOKEN via the Spotify API
import requests

# Constants
AUTH_TOKEN = "your_auth_token_here"  # Replace with actual AUTH_TOKEN
CODE = "your_code_here"  # Replace with actual CODE

# API endpoint
url = "https://accounts.spotify.com/api/token"

# Headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {AUTH_TOKEN}",
}

# Form data
data = {
    "grant_type": "authorization_code",
    "redirect_uri": "http://localhost/callback/",
    "code": CODE,
}

# Make the POST request
response = requests.post(url, headers=headers, data=data)

# Print the response (assuming JSON)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
