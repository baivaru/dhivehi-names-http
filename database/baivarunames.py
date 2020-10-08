import re

from database import database

class BaivaruNames:
    def __init__(self):
        self.bnames = database()['names']
    
    def get_random(self):
        name = [d for d in self.bnames.aggregate([{'$sample': {'size': 1 }}])][0]
        name.pop('_id')
        return name

    def get_randoms(self, count):
        names = []
        for _ in range(count):
            name = [d for d in self.bnames.aggregate([{'$sample': {'size': 1 }}])][0]
            data = {
                "ar": name['ar'],
                "dv": name['dv'],
                "meaning" : name['meaning'],
                "gender" : name['gender']
            }
            names.append(data)
        return names

    def search(self, query):
        q = { "dv": { "$regex": query, "$options" :'i' } }
        data = self.bnames.find(q)
        names = [{
                "ar": d['ar'],
                "dv": d['dv'],
                "meaning" : d['meaning'],
                "gender" : d['gender']
            } for d in data
        ]
        return names

    def exact(self, query):
        name = self.bnames.find_one({'dv': query})
        name.pop('_id')
        
        return name