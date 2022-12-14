import subprocess
import argparse


# if __name__ == "__main__":
parser = argparse.ArgumentParser(description="Parsing parameters")
params = [
    (
        "--actor",
        {"dest": "actor", "type": str, "default": ""},
    ),
    (
        "--new_tag",
        {"dest": "new_tag", "type": str, "default": "1"},
    ),
]
for name, param in params:
    parser.add_argument(name, **param)

args = parser.parse_args()
args = args._get_kwargs()
args = {arg[0]: arg[1] for arg in args}

actor = args["actor"]
new_tag = args["new_tag"]

last_version = int(new_tag.split(".")[-1])
if last_version > 0:
    previous_version = last_version - 1
    tags_command = f"HEAD...rc-0.0.{previous_version}"
    print("Тег релиза:", f"rc-0.0.{last_version}")
    cmd = [
        "git",
        "log",
        "--oneline",
        "--pretty=format:'%h; author: %cn; date: %ci; commit message:%s'",
        tags_command,
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()

    print(output.decode("ascii"))
    print(error.decode("ascii"))
else:
    print("Тег релиза:", f"rc-0.0.0")
    cmd = [
        "git",
        "log",
        "--oneline",
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()

    print(output.decode("ascii"))
