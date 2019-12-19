import instabot
import time
import random
import os


def main():
	bot = instabot.Bot()
	bot.login()

	pauseseconds = random.randrange(60, 90, 1)
	os.system("copy msjww.jpg msjwwcopy.jpg")

	while(True):
		bot.upload_photo("msjwwcopy.jpg", caption="#msjww19")
		print("Waiting: ", pauseseconds)

		time.sleep(pauseseconds)
		pauseseconds = random.randrange(60, 90, 1)

		os.system("del \\f msjwwcopy.jpg.REMOVE_ME")
		os.system("copy msjww.jpg msjwwcopy.jpg")



if __name__ == "__main__":
	main()