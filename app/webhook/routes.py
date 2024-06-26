from datetime import datetime

from flask import Blueprint, json, request, render_template
from bson import json_util

from app.service import add_event, get_all_events, get_event
from app.utils import (
    parse_date, make_push_message, make_pr_message,
    make_merge_message, make_last_updated_message
)

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    event = request.headers.get("X-GitHub-Event")
    request_body: dict = request.json

    if event == "push":
        head: dict = request_body.get("head_commit") 
        request_id: str = head.get("id")
        author: str = head.get("author").get("username")
        action = "PUSH"
        timestamp: str = parse_date(head.get("timestamp")) 
        from_brach: str = request_body.get("ref").split("/")[-1]
        to_branch = from_brach
        add_event(request_id, author, action, from_brach, to_branch, timestamp)

    elif event == "pull_request":
        # pull_request extraction login as well as check if its pr open or pr close if close check for merge
        action = request_body.get("action")
        pr_body: dict = request_body.get("pull_request")
        
        request_id = str(pr_body.get("id"))
        author: str = request_body.get("sender").get("login")
        from_brach: str = pr_body.get("head").get("ref")
        to_branch: str = pr_body.get("base").get("ref")

        event_action = "PULL_REQUEST"
        timestamp: str = parse_date(pr_body.get("created_at"))

        is_merge = pr_body.get("merged")
    
        if action == "closed" and is_merge:
            event_action = "MERGE"
            author = pr_body.get("merged_by").get("login")
            timestamp = parse_date(pr_body.get("merged_at"))
        
        add_event(request_id, author, event_action, from_brach, to_branch, timestamp)


    return {}, 200

@webhook.route("/", methods=["GET"])
def root():
    event: dict | None = get_event()
    current_time = datetime.utcnow().strftime("%H:%M:%S UTC")
    last_updated = make_last_updated_message(current_time)
    
    if event == None:
        return render_template("index.html", message="No action occured!", last_updated=last_updated)

    message = ""
    action = event.get("action")
    
    if action == "PUSH":
        message = make_push_message(event.get("author"), event.get("from_branch"), event.get("timestamp"))
    elif action == "PULL_REQUEST":
        message = make_pr_message(event.get("author"), event.get("from_branch"), event.get("to_branch"), event.get("timestamp"))
    elif action == "MERGE":
        message = make_merge_message(event.get("author"), event.get("from_branch"), event.get("to_branch"), event.get("timestamp"))
    
    return render_template("index.html", message=message, last_updated=last_updated)


@webhook.route('/all', methods=["GET"])
def all():
    events = get_all_events()
    
    return json.loads(json_util.dumps(events)), 200
