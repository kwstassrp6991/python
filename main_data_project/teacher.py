class Teacher:

    def __init__(self,first_name="",last_name="",teacher_id=-1):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name


    def from_dict(self,dictionary):
        self.teacher_id = dictionary["teacher_id"]
        self.first_name = dictionary["first_name"]
        self.last_name = dictionary["last_name"]


    def to_dict(self):
        t_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "teacher_id": self.teacher_id
        }
        return t_dict

    def __str__(self):
        st = f"id:{self.teacher_id}\nfirst_name:{self.first_name}\nlast_name:{self.last_name}"
        return f"{str(st)}"

#--------------------------------------------------------------------