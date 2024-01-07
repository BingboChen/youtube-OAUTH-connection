from googleapiclient.discovery import build
from auth import get_authenticated_service


def main():
    # The scope required for YouTube Analytics API
    scopes = ['https://www.googleapis.com/auth/yt-analytics.readonly']

    # Get authenticated service
    credentials = get_authenticated_service(
        client_secrets_file='client_secrets.json',
        scopes=scopes,
        refresh_token_file='refresh_token.txt'
    )

    # Use the credentials to create a service object
    youtube_analytics = build('youtubeAnalytics', 'v2', credentials=credentials)

    request = youtube_analytics.reports().query(
        endDate="2024-05-01",
        ids="channel==MINE",
        metrics="views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration",
        startDate="2017-01-01"
    )
    response = request.execute()

    print(response)


if __name__ == '__main__':
    main()
