from yandex_tracker_client import TrackerClient
import argparse
import os


parser = argparse.ArgumentParser(description="Parsing parameters")
params = [
    (
        "--actor",
        {"dest": "actor", "type": str, "default": ""},
    ),
    (
        "--message",
        {"dest": "message", "type": str, "default": "1"},
    ),
]
for name, param in params:
    parser.add_argument(name, **param)

args = parser.parse_args()
args = args._get_kwargs()
args = {arg[0]: arg[1] for arg in args}

actor = args["actor"]
message = args["message"]

token = os.environ["TRACKER_TOKEN"]
org_id = os.environ["ORG_ID"]
issue_name = os.environ["ISSUE_NAME"]

client = TrackerClient(token=token, org_id=org_id)

issue = client.issues[issue_name]
comment_text = f"""
ответственный за релиз: {actor}
{message}
"""
comment = issue.comments.create(text=comment_text)
