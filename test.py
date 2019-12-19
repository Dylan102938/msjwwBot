import instabot
import time
import random
import os

def main():
	bot = instabot.Bot()
	bot.login()

	pauseseconds = random.randrange(60, 90, 1)
	os.system("cp /Users/dylanfeng/Documents/msjww.jpg ./pics/msjww.jpg")

	while(True):
		bot.upload_photo("./pics/msjww.jpg", caption="#msjww19")
		time.sleep(pauseseconds)
		pauseseconds = random.randrange(60, 90, 1)
		print("Waiting: ", pauseseconds)

		os.system("rm ./pics/msjww.jpg.REMOVE_ME")
		os.system("cp /Users/dylanfeng/Documents/msjww.jpg ./pics/msjww.jpg")



if __name__ == "__main__":
	main()
