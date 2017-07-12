import random

# current learning topics I want to focus on

topics = ["arduino", "fashion", "coding", "gaming"]

# code will randomly chose a topic for each week
# in a month, removing topics from the list
# until all have been used

random_topic = random.choice(topics)
print("Week 1 Topic:")
print(random_topic)
topics.remove(random_topic)
print(topics)
random_topic = random.choice(topics)
print("Week 2 Topic:")
print(random_topic)
topics.remove(random_topic)
print(topics)
random_topic = random.choice(topics)
print("Week 3 Topic:")
print(random_topic)
topics.remove(random_topic)
print(topics)
random_topic = random.choice(topics)
print("Week 4 Topic:")
print(random_topic)
topics.remove(random_topic)
print(topics)
