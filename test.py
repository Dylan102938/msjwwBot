import instabot
import time
import random
import os

def main():
	bot = instabot.Bot()
	bot.login()

	pauseseconds = random.randrange(60, 90, 1)

	while(True):
		bot.upload_photo("pics/msjww2.jpg", caption="#msjww19 v2 shit oh yea yea")
		time.sleep(pauseseconds)
		pauseseconds = random.randrange(60, 90, 1)
		print("Waiting: ", pauseseconds)

		os.system("rm pics/msjww2.jpg.REMOVE_ME")
		os.system("cp pics/msjww1.jpg pics/msjww2.jpg")

if __name__ == "__main__":
	main()
