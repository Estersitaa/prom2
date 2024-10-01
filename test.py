print("sveiki")
class Cilveks: 
    def __init__(self, vards, dzimums, vecums):
        self.name = vards
        self.age = vecums
        self.sex = dzimums
    
    def dz_diena(self):
        self.age +=1

    def dzzimums(self):
        self.sex = "virietis"

    def pastastit_par_sevi(self):
        if self.sex == "s":
            dzimums = "sieviete"
        elif self.sex == "v":
            dzimums = "virietis"
        else:
            dzimums = self.sex
        print("Sveiki, mani sauc {}. Man ir {} gadu. Es esmu {}".format(self.name, self.age, dzimums))
        
        
        
        
# person =Cilveks(20, "s")
# person.pastastit_par_sevi()
# person.name = "Katrina"
# person.pastastit_par_sevi()
# person.dz_diena()
# person.name = "Alise"
# person.pastastit_par_sevi()
# person.dzzimums()
# person.name = "Uldis"
# person.pastastit_par_sevi()


# from cilveks import cilveks, sieviete
# import tkinter as tk
# root = tk.Tk



