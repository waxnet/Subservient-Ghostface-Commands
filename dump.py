import shutil
import json
import os

# get data
with open("commands.json", "r") as f:
    data = json.load(f)

# dump
if not os.path.exists("output"):
    os.mkdir("output")
else:
    shutil.rmtree("output")
    os.mkdir("output")

for commandData in data["commands"]:
    # raw commands
    with open("output/raw_commands.txt", "+a") as file:
        file.write("\n".join(commandData["examples"]) + "\n\n")
        file.close()

    # raw videos
    if not os.path.exists("output/raw_videos.txt"):
        with open("output/raw_videos.txt", "w") as file:
            file.write("TO VIEW VIDEOS : https://subservientghostface.com/clips/VIDEO_ID\n\n")
            file.close()
    with open("output/raw_videos.txt", "+a") as file:
        file.write("\n".join(commandData["videos"]) + "\n\n")
        file.close()

    # raw ids and labels
    with open("output/raw_ids_and_labels.txt", "+a") as file:
        file.write(commandData["id"] + "\n" + commandData["label"] + "\n\n")
        file.close()

    # non raw commands
    with open("output/commands_w_labels.txt", "+a") as file:
        wheelPrompt = commandData.get("wheelPrompt")
        if not wheelPrompt:
            wheelPrompt = max(commandData["examples"], key=len)

        file.write(commandData["label"] + "\n" + wheelPrompt + "\n\n")
        file.close()

# fallback videos
if not os.path.exists("output/fallback_videos.txt"):
    with open("output/fallback_videos.txt", "w") as file:
        file.write("TO VIEW VIDEOS : https://subservientghostface.com/clips/VIDEO_ID\n\n")
for category, videos in data["fallbackVideos"].items():
    with open("output/fallback_videos.txt", "a") as file:
        file.write(category + "\n")
        file.write("\n".join(videos))
        file.write("\n\n")
        file.close()
