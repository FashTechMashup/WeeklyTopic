import random

# current learning topics I want
# to focus on

topics = ["Arduino", "Fashion", "Coding", "Gaming"]
empty = []

# code will randomly chose a topic for each # week in a month, removing topics
# from the list until all have been used


def topic_loop():
	weeks = 1
	while topics != empty:
		random_topic = random.choice(topics)
		print("Week {} Topic: ".format(weeks) + random_topic)
		topics.remove(random_topic)
		weeks = weeks + 1

topic_loop()
