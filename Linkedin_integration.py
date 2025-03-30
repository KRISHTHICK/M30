import requests

def get_linkedin_profile_views(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
    return response.json()

def filter_views(views):
    maang_companies = ["Meta", "Apple", "Amazon", "Netflix", "Google"]
    filtered_views = [view for view in views if view['company'] in maang_companies and 'GenAI' in view['role']]
    return filtered_views
