from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    views = get_linkedin_profile_views(data['access_token'])
    filtered_views = filter_views(views)
    
    if filtered_views:
        for view in filtered_views:
            message = f"Your LinkedIn profile was viewed by {view['name']} from {view['company']} for a GenAI role. LinkedIn ID: {view['linkedin_id']}, Email: {view['email']}"
            send_email_notification(data['email'], "LinkedIn Profile View Notification", message)
    
    return jsonify({"status": "Notification sent"})

if __name__ == '__main__':
    app.run(port=5000)
