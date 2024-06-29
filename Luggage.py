class Luggage:
    luggage_id = 0
    owner_name = ""
    owner_surname = ""
    passport = ""
    weight = 0
    type = ""
    destination = ""

    def __init__(self, luggage_id,owner_name,owner_surnname, passport, weight,destination,type):
         self.luggage_id=luggage_id
         self.owner_name=owner_name
         self.owner_surnname=owner_surnname
         self.passport=passport
         self.weight=weight
         self.destination=destination
         self.type=type

    def __str__(self):
        return f"Luggage ID: {self.luggage_id}, Owner: {self.owner_name} {self.owner_surnname},Owner Passport Number: {self.passport}, Weight: {self.weight}kg, Destination: {self.destination}, Type: {self.type}"

