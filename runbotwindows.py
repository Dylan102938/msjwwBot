import instabot
import time
import random
import os


def main():
	bot = instabot.Bot()
	bot.login()

	pauseseconds = random.randrange(60, 90, 1)

	while(True):
		bot.upload_photo("pics\msjww2.jpg", caption="#msjww19 maybe windows will work")
		print("Waiting: ", pauseseconds)

		time.sleep(pauseseconds)
		pauseseconds = random.randrange(60, 90, 1)

		os.system("del \\f \pics\msjww2.jpg.REMOVE_ME")
		os.system("copy pics\msjww1.jpg pics\msjww2.jpg")

if __name__ == "__main__":
	main()