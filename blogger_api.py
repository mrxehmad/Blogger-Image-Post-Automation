from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

def authenticate_blogger_api():
    SCOPES = ['https://www.googleapis.com/auth/blogger']
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('blogger', 'v3', credentials=creds)
    return service

def create_blogger_post(service, blog_id, post_title, content, image_url, labels, alt_text, img_title):
    post_body = {
        'kind': 'blogger#post',
        'title': post_title,
        'content': f'''
                <img src="{image_url}" alt="{alt_text}" title="{img_title}"/>
                <br/>
                <div style="text-align: center; margin-top: 10px;">
                <a href="{image_url}" download style="display:inline-block; padding: 10px 15px; background-color: #007BFF; color: white; text-decoration: none; border-radius: 5px;">
                Download Image
                </a>
                </div>
                <br/><br/>
                <div style="font-family: Arial, sans-serif;">
                    {content}
                </div>
        ''',
        'labels': labels,
        'status': 'live'
    }

    posts = service.posts()
    post = posts.insert(blogId=blog_id, body=post_body).execute()
    return post