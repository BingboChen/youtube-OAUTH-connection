from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError


def is_refresh_token_valid(refresh_token, client_id, client_secret):
    credentials = Credentials(
        None,
        refresh_token=refresh_token,
        token_uri='https://oauth2.googleapis.com/token',
        client_id=client_id,
        client_secret=client_secret
    )

    try:
        credentials.refresh(Request())
        return True  # The refresh was successful, token is valid
    except RefreshError:
        return False  # The refresh failed, token is invalid


# Usage
refresh_token = ('1//09-r9n3ug2cirCgYIARAAGAkSNwF-L9IrCPIV5W5udQdZO4OemIV-AVXnENm_T2FCv1YnNaGmCI-1mcq0jR0btsBG'
                 '-9TojBM6rmY')
client_id = '25656108972-es4u4u7rvsckp1ronb8141898nk9apau.apps.googleusercontent.com'
client_secret = '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'
is_valid = is_refresh_token_valid(refresh_token, client_id, client_secret)
print("Is the refresh token valid?", is_valid)
