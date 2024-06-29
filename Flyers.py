class passengers:
    name = ""
    surname = ""
    date_of_birth = ""
    citizenship = ""
    passport = ""
    def __init__(self, name, surname,  date_of_birth, citizenship, passport_number):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.citizenship = citizenship
        self.passport_number = passport_number
        self.luggage = []

    def __str__(self):
        return f"Name: {self.name}' '{ self.surname}, Date of Birth: {self.date_of_birth}, Citizenship: {self.citizenship}, Passport Number: {self.passport_number}"


