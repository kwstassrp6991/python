class Lesson:
    def __init__(self,name=None):
        self.name = name
        self.pupils_ids = []

    def __str__(self):
        st = f"{self.name}:[{self.pupils_ids}]"
        return st

    def lto_dict(self):
        my_dict = {
            "name": self.name,
            "pupils_ids": self.pupils_ids
        }
        return my_dict

    def change_from_ldict_to_object(self,dictionary):
        self.name = dictionary["name"]
        self.pupils_ids = dictionary["pupils_ids"]

