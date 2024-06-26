

def make_push_message(author: str, branch: str, utc_time: str) -> str:
    """
    Makes formatted push message.
    """
    return f"<p><strong>{author}</strong> pushed changes to <strong>{branch}</strong> on <strong>{utc_time}</strong></p>"

def make_pr_message(author: str, from_branch: str, to_branch: str, utc_time: str) -> str:
    """
    Makes formatted pull request message.
    """
    return f"""
    <p><strong>{author}</strong> submitted a pull request from <strong>{from_branch}</strong> to 
    <strong>{to_branch}</strong> on <strong>{utc_time}</strong></p>
    """

def make_merge_message(author: str, from_branch: str, to_branch: str, utc_time: str) -> str:
    """
    Makes formatted merge message.
    """
    return f"""
    <p><strong>{author}</strong> merged branch <strong>{from_branch}</strong> to 
    <strong>{to_branch}</strong> on <strong>{utc_time}</strong></p>
    """

def make_last_updated_message(utc_time: str) -> str:
    """
    Makes formatted last updated message.
    """
    return f"Last updated at {utc_time}"
