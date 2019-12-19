import instabot
import time
import random
import os


def main():
	bot = instabot.Bot()
	bot.login()

	pauseseconds = random.randrange(60, 90, 1)
	os.system("cp msjww.jpg msjwwcopy.jpg")

	while(True):
		bot.upload_photo("msjwwcopy.jpg", caption="#msjww19")
		print("Waiting: ", pauseseconds)

		time.sleep(pauseseconds)
		pauseseconds = random.randrange(60, 90, 1)

		os.system("rm msjwwcopy.jpg.REMOVE_ME")
		os.system("cp msjww.jpg msjwwcopy.jpg")



if __name__ == "__main__":
	main()