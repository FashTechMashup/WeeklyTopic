import random

topics = ["Arduino", "Fashion", "Coding", "Gaming"]

random_topic = random.choice(topics)
i = []

while 1 == 1:
	print("Weekly Topic: " + random_topic)
	topics.remove(random_topic)
else:
	print("August Schedule" )


# when i made 1==3 got else statement
# 1==1 gave me a value error (run to see)
