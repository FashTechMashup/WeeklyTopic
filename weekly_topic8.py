import random

topics = ["Arduino", "Fashion", "Coding", "Gaming"]

random_topic = random.choice(topics)
i = []

while 1 == 1:
	print("Weekly Topic: " + random_topic)
	topics.remove(random_topic)
else:
	print("August Schedule" )


	random_topic = random.choice(topics)
print("Week 1 Topic: ")
print(random_topic)
topics.remove(random_topic)
print(topics)

random_topic = random.choice(topics)
print("Week 2 Topic:")
print(random_topic)
topics.remove(random_topic)
print(topics)

if not i:
	print("Weekly Topic: " + random_topic)
	else:
		print("August Schedule" )




# when i made 1==3 got else statement
# 1==1 gave me a value error (run to see)
