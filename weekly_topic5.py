import random

topics = ["Arduino", "Fashion", "Coding", "Gaming"]
max_index = len(topics)
random_topic = random.choice(topics)
topics.remove(random_topic)

while topics > max_index:
	print("Weekly Topic: " + random_topic)
