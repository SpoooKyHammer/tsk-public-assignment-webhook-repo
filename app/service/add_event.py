from app.extensions import mongo 

def add_event(
        request_id: str, author: str, action: str,
        from_branch: str, to_branch: str, timestamp: str
    ) -> None:
    """
    Inserts a event doc into the events collection, with the following fields:

    - "request_id"
    - "author"
    - "action"
    - "from_branch"
    - "to_branch"
    - "timestamp"
    """

    event_doc = {
        "request_id": request_id,
        "author": author,
        "action": action,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }

    mongo.db.events.insert_one(event_doc)
