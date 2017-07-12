import random

# current learning topics I want to focus on

topics = ["arduino", "fashion", "coding", "gaming"]

# code will randomly chose a topic for each week
# in a month, removing topics from the list
# until all have been used

random_topic = random.choice(topics)
print("Week 1 Topic:")
print(random_topic)
topics = topics.remove(random_topic)
print(topics)
print("Week 2 Topic:")
print(random_topic)
print(topics)

# no error message but did not give out desired result

# Week 1 Topic:
# fashion
# None
# Week 2 Topic:
# fashion
# None
