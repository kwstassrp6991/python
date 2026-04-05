class Pupil:
    def __init__(self, first_name='',last_name='',fathers_name='',age='',class_name='',id_number='',pupil_id =0):
        self.pupil_id = pupil_id
        self.first_name = first_name
        self.last_name = last_name
        self.fathers_name = fathers_name
        self.age = age
        self.class_name = class_name
        self.id_number = id_number

    def __str__(self):
        st = (f"pupil_id:{self.pupil_id}\nfirst_name:{self.first_name}\nlast_name:{self.last_name}"
              f"\nfathers_name:{self.fathers_name}\nage:{self.age}\n"
              f"class:{self.class_name}\nid_number{self.id_number}")

        return st


    def pfrom_dict(self,dictionary):
        self.pupil_id = dictionary['pupil_id']
        self.first_name = dictionary['first_name']
        self.last_name = dictionary['last_name']
        self.fathers_name = dictionary['fathers_name']
        self.age = dictionary['age']
        self.class_name = dictionary['class_name']
        for i in dictionary:
            if i == 'id_number':
                self.id_number = dictionary["id_number"]
            else:
                self.id_number = ""

    def pto_dict(self):
        dictionary={
            'pupil_id': self.pupil_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'fathers_name': self.fathers_name,
            'age': self.age,
            'class_name': self.class_name,
        }
        if self.id_number != '':
            dictionary['id_number'] = self.id_number
        else:
            dictionary['id_number'] = ''

        return dictionary

