from app.extensions import mongo

def get_event() -> dict | None:
    """
    Gets the last occured event and returns it or None.
    """
    events = list(mongo.db.events.find().sort("$natural", -1).limit(2))

    if len(events) == 0:
        return None
    elif len(events) == 1:
        return events[0]
    
    last_event = events[0]
    second_last_event = events[1]
    
    if (
        last_event.get("action") == "PUSH" and 
        second_last_event.get("action") == "MERGE" and 
        last_event.get("timestamp") == second_last_event.get("timestamp")
    ):
        return second_last_event
    else:
        return last_event
