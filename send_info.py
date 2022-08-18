from yandex_tracker_client import TrackerClient
import argparse
import os
import datetime
import requests
import json


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
    (
        "--release_tag",
        {"dest": "release_tag", "type": str, "default": "1"},
    ),
]
for name, param in params:
    parser.add_argument(name, **param)

args = parser.parse_args()
args = args._get_kwargs()
args = {arg[0]: arg[1] for arg in args}

actor = args["actor"]
message = args["message"]
release_tag = args["release_tag"]

token = os.environ["TRACKER_TOKEN"]
org_id = os.environ["ORG_ID"]
issue_name = os.environ["ISSUE_NAME"]


client = TrackerClient(token=token, org_id=org_id)
issue = client.issues[issue_name]
comment_text = f"""
ответственный за релиз: {actor}
{message}
Собрали docker image c тегом {release_tag}
"""
issue.comments.create(text=comment_text)
date = datetime.datetime.now()
summury = f"Релиз {release_tag} от {date}"
try:
    r = requests.patch(
        f"https://api.tracker.yandex.net/v2/issues/{issue_name}",
        headers={
            "Authorization": f"OAuth {token}",
            "X-Org-ID": org_id,
        },
        data=json.dumps(
            {
                "summary": summury,
                "description": comment_text,
            }
        ),
    )

    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
    print(r.text)
    raise e
