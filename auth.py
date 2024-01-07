from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from icecream import ic
import json


def get_authenticated_service(client_secrets_file, scopes, refresh_token_file):
    credentials = None

    # Load client ID and client secret from the client_secrets_file
    with open(client_secrets_file) as file:
        client_secrets = json.load(file)
        client_id = client_secrets['installed']['client_id']
        client_secret = client_secrets['installed']['client_secret']

    # Try to load the refresh token from a file
    try:
        with open(refresh_token_file, 'r') as token_file:
            refresh_token = token_file.read().strip()
            credentials = Credentials(
                None,
                refresh_token=refresh_token,
                token_uri='https://oauth2.googleapis.com/token',
                client_id=client_id,
                client_secret=client_secret
            )
    except Exception as e:
        print("Error reading the refresh token from file:", e)

    # Refresh the access token
    if credentials:
        credentials.refresh(Request())

    # If credentials are not available or invalid, go through the authorization flow
    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        flow.run_local_server(port=8080)
        credentials = flow.credentials

        # Save the refresh token for future use
        with open(refresh_token_file, 'w') as token_file:
            token_file.write(credentials.refresh_token)

    return credentials
