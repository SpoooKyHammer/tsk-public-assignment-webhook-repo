from datetime import datetime, timezone

def parse_date(iso_str: str) -> str:
    """
    Parse a ISO 8601 string to UTC string.
    """
    dtObj = datetime.fromisoformat(iso_str).astimezone(timezone.utc)
    return dtObj.strftime("%d %B %Y - %I:%M %p UTC")
