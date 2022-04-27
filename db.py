import random


skills = list(range(50))

profiles = {i: {'id': i, 'skills': random.sample(skills, random.randint(5, 20))} for i in range(1, 1001)}


if __name__ == '__main__':
    print(profiles[1])