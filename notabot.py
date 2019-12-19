import glob
import os
import sys
import time
from io import open
import random

sys.path.append(os.path.join(sys.path[0], "../../"))
from instabot import Bot  # noqa: E402

posted_pic_list = []
try:
    with open("pics.txt", "r", encoding="utf8") as f:
        posted_pic_list = f.read().splitlines()
except Exception:
    posted_pic_list = []

random = random.randrange(60, 90, 1)
timeout = random  # pics will be posted every 24 hours
print(random)

bot = Bot()
bot.login()

while True:

    folder_path = "./pics"
    pics = glob.glob(folder_path + "/*.jpg")
    pics = sorted(pics)

    try:
        for pic in pics:
            if pic in posted_pic_list:
                continue

            pic_name = pic[:-4].split("-")
            pic_name = "-".join(pic_name[1:])

            print("upload: " + pic_name)

            description_file = folder_path + "/" + pic_name + ".txt"

            if os.path.isfile(description_file):
                with open(description_file, "r") as file:
                    caption = file.read()
            else:
                caption = pic_name.replace("-", " ")

            bot.upload_photo(pic, caption=caption)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
                # snd msg
                break

            if pic not in posted_pic_list:
                posted_pic_list.append(pic)
                with open("pics.txt", "a", encoding="utf8") as f:
                    f.write(pic + "\n")

            time.sleep(timeout)
            random = random.randrange(60, 90, 1)
            timeout = random

    except Exception as e:
        print(str(e))

    time.sleep(60)