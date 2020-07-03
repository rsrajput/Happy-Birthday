import time

def happy_birthday(name):
	name = name.capitalize()
	for x in range(2):
		print("Happy Birthday to you.")
		time.sleep(1)
		print("Happy Birthday to", name)
		time.sleep(1)
		print("Happy Birthday to you.")
		time.sleep(1)
		for x in range(3):
			print('Hip Hip Hooray!')

happy_birthday('Aditi')