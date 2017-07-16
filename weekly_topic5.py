import random

topics = ["Arduino", "Fashion", "Coding", "Gaming"]
max_index = len(topics)
random_topic = random.choice(topics)
topics.remove(random_topic)

while topics > max_index:
	print("Weekly Topic: " + random_topic)

# error message

# File "weekly_topic5.py", line 8, in <module>
#     while topics > max_index:
# TypeError: '>' not supported between instances of 'list' and 'int'
