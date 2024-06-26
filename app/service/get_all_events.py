from app.extensions import mongo

def get_all_events():
    """Retrives all events stored in database."""
    events = list(mongo.db.events.find())
    return events
