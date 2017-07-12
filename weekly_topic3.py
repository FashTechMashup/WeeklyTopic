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
print("Week 2 Topic:")
print(random_topic)
topics.remove(random_topic)
print(topics)

# error message

# Week 1 Topic:
# arduino
# Week 2 Topic:
# arduino
# Traceback (most recent call last):
#   File "weekly_topic4.py", line 17, in <module>
#     topics = topics.remove(random_topic)
# AttributeError: 'NoneType' object has no attribute 'remove'
# Crystals-MacBook-Pro:Messing Around kmist$
