import db
import random


class Model:
    def __init__(self):
        self.profiles = self.get_profiles()
        self.skills = self.get_skills()
    
    def get_skills(self):
        return db.skills
    
    def get_profiles(self):
        return db.profiles
    
    def distance(self, profile, job_offer):
        return 1 - len(set(profile['skills']) & set(job_offer)) / len(job_offer)
    
    def avg_score(self, job_offer):
        return sum(self.distance(profile, job_offer) for profile in self.profiles.values()) / len(self.profiles)
    
    def get_best_profiles(self, job_offer):
        return sorted(self.profiles.values(), key=lambda profile: self.distance(profile, job_offer))
    
if __name__ == '__main__':
    
    job_offer = random.sample(db.skills, random.randint(5, 20))
    model = Model()
    print(job_offer)
    print(model.get_best_profiles(job_offer)[:5])