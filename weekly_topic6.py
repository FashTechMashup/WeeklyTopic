import random

topics = ["Arduino", "Fashion", "Coding", "Gaming"]
i = []

random_topic = random.choice(topics)

if not i:
	print("Weekly Topic: " + random_topic)
	topics.remove(random_topic)
else:
	print("August Schedule" )


#so the code is not broken but it
#also is only putting out 1 result
