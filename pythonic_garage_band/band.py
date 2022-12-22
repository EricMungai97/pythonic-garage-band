class Band:
   instances = []

   def __init__(self, name, members="None"):
       self.name = name
       self.members = members
       self.instances.append(self)

   def __str__(self):
       return f"The band {self.name}"

   def __repr__(self):
       return f"Band instance. name={self.name}, members={self.members}"

   def play_solos(self):
       solos = []
       for member in self.members:
           solos.append(member.solo)
       return solos

class Musician:
    def __init__(self, name, member, instrument, solo):
        self.name = name
        self.type = member
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.type} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return f"{self.solo}"


class Guitarist(Musician):
    def __init__(self, name, member="Guitarist", instrument="guitar", solo="face melting guitar solo"):
        super().__init__(name, member, instrument, solo)


class Bassist(Musician):
    def __init__(self, name, member="Bassist", instrument="bass", solo="bom bom buh bom"):
        super().__init__(name, member, instrument, solo)


class Drummer(Musician):
    def __init__(self, name, member="Drummer", instrument="drums", solo="rattle boom crash"):
        super().__init__(name, member, instrument, solo)


# class Guitarist:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"My name is {self.name} and I play guitar"
#
#     def __repr__(self):
#         return f"Guitarist instance. Name = {self.name}"
#
#     def get_instrument(self):
#         return "guitar"
#
#
# class Drummer:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"My name is {self.name} and I play drums"
#
#     def __repr__(self):
#         return f"Drummer instance. Name = {self.name}"
#
#     def get_instrument(self):
#         return "drums"
#
#
# class Bassist:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"My name is {self.name} and I play bass"
#
#     def __repr__(self):
#         return f"Bassist instance. Name = {self.name}"
#
#     def get_instrument(self):
#         return "bass"


