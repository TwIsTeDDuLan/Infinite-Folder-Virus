import requests
from bs4 import BeautifulSoup

def get_facebook_comments(profile_url, friend_name):
    # Make a request to the Facebook profile page
    response = requests.get(profile_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        comments = []
        
        # Find all comments on the profile page
        for comment in soup.find_all('div', class_='comment'):
            commenter = comment.find('span', class_='commenter-name').text
            if commenter == friend_name:
                comment_text = comment.find('span', class_='comment-text').text
                comments.append(comment_text)
        
        return comments
    else:
        print('Failed to retrieve the page')
        return None

# Usage
profile_url = 'https://www.facebook.com/kavindu.chinthnana'
friend_name = 'Sandun Tharuka'
comments = get_facebook_comments(profile_url, friend_name)

if comments:
    for comment in comments:
        print(comment)
else:
    print('No comments found')
