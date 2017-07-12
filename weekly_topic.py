import random

# current learning topics I want to focus on

topics = ["Arduino", "Fashion", "Coding", "Gaming"]

# code will randomly chose a topic for each week
# in a month, removing topics from the list
# until all have been used

random_topic = random.choice(topics)
print("Week 1 Topic: " + random_topic)
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

# gave me the result I wanted but now I want to do it
# cleaner with less code

# Week 1 Topic:
# coding
# ['arduino', 'fashion', 'gaming']
# Week 2 Topic:
# fashion
# ['arduino', 'gaming']
# Crystals-MacBook-Pro:Messing Around kmist$ python3 weekly_topic.py
# Week 1 Topic:
# coding
# ['arduino', 'fashion', 'gaming']
# Week 2 Topic:
# gaming
# ['arduino', 'fashion']
# Week 3 Topic:
# fashion
# ['arduino']
# Week 4 Topic:
# arduino
# []
