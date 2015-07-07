fix_stevilke_od_1_do_50 = []
fix_stevilke_od_1_do_10 = []

vrste_dobitki = 0

zgodovina = open("zgodovina", "a")

import datetime as dt
import time

now = dt.datetime(1, 1, 1).now()

pet = []
dva = []
skupni_dva = []
skupni_pet = []

skupni_dva_test = []
skupni_pet_test = []
test = True
stevke = ''
st_ponovitev = 0
st_vrstic = 1
st_vejic = 0


napis = 'Vnesli ste napačen niz!'

with open("vplacilni_listki", "r") as ins:
    vplacani_listki = ins.readlines()
    vplacani_listki = [line.rstrip('\n') for line in open('vplacilni_listki')]

try:
    for vrstica in vplacani_listki:
        for crka in vrstica:

            if crka.isnumeric() == True:
                if crka == '0':
                    if stevke and not stevke.isspace():
                        stevke += crka
                    else: test = False; break
                else: stevke += crka

            elif crka.isnumeric() == False:
                if crka == ',':
                    st_vejic += 1
                    if st_vejic > 5:
                        test = False
                        break
                    elif int(stevke) <= 50:
                        if st_ponovitev < 5:
                            pet.append(int(stevke))
                            stevke = ''
                            st_ponovitev += 1
                        elif st_ponovitev >= 5:
                            if int(stevke) <= 10:
                                dva.append(int(stevke))
                                stevke = ''
                                st_ponovitev += 1
                        else: test = False
                    else: test = False

                elif crka == ' ':
                    if int(stevke) <= 50:
                        if st_ponovitev < 5:
                            pet.append(int(stevke))
                            stevke = ''
                            st_ponovitev += 1
                        elif st_ponovitev >= 5:
                            if int(stevke) <= 10:
                                dva.append(int(stevke))
                                st_ponovitev += 1
                            else: test = False; break 
                        else: test = False; break
                    else: test = False; break
                else: test = False; break

        if test == False:
            break

        if int(stevke) <= 10:
            dva.append(int(stevke))
        else: test = False; break

        if len(pet) != 5:
           test = False
           break

        elif len(dva) != 2:
          test = False
          break

        if len(set(dva)) != len(dva):
          test = False
          break

        if len(set(pet)) != len(pet):
          test = False
          break

        dva = sorted(dva)
        pet = sorted(pet)

        skupni_pet_test.append(' , '.join(str(number) for number in pet))
        skupni_dva_test.append(' , '.join(str(number) for number in dva))

        dva_2 = []
        for a in dva:
            dva_2.append(a)
            dva_2.append(',')
        del dva_2[-1]

        pet_2 = []
        for b in pet:
            pet_2.append(b)
            pet_2.append(',')
        del pet_2[-1]

        skupni_dva.append(dva_2)
        skupni_pet.append(pet_2)

        pet = []
        dva = []
        stevke = ''
        st_ponovitev = 0
        st_vejic = 0
       
        st_vrstic += 1

except ValueError:
    test = False
            

znesek = 2.20 * (st_vrstic-1)


import tkinter as tk

from tkinter import *


class EuroJaskpot(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self)

        root.configure(background='light goldenrod')
        master.maxsize(width=393, height=480)

        logo = PhotoImage(file="euro_zacetna.gif")
        logo = logo.zoom(6,3)
        logo = logo.subsample(7,4)
        w1 = Label(master, image=logo, bg = 'light goldenrod')
        w1.image = logo
        w1.grid(column = 0, columnspan = 3)
        
        napis1 = Label(master, text = 'Vaše številke:    ', bg = 'light goldenrod')
        napis1.grid(row = 3, column = 0)
        
        self.napisane_stevilke1 = Label(master, text = '', bg = 'light goldenrod')
        self.napisane_stevilke1.grid(row = 1, column = 1)
        
        napisane_stevilke2 = Label(master, text = '', bg = 'light goldenrod')
        napisane_stevilke2.grid(row = 1, column = 2)
        
        napis2 = Label(master, text = 'Izžrebane številke:    ', bg = 'light goldenrod')
        napis2.grid(row = st_vrstic+5, column = 0)

        self.izzrebane_stevilke1 = Label(master,  text = '', bg = 'light goldenrod')
        self.izzrebane_stevilke1.grid(row = st_vrstic+5, column = 1)

        self.izzrebane_stevilke2 = Label(master, text = '', bg = 'light goldenrod')
        self.izzrebane_stevilke2.grid(row = st_vrstic +5, column = 2)

        prazno = Label(text = '', bg = 'light goldenrod')
        prazno.grid(row = st_vrstic+6)

        prazno = Label(master, text = '', bg = 'light goldenrod')
        prazno.grid(row = 2)

        prazno = Label(master, text = '', bg = 'light goldenrod')
        prazno.grid(row = 4)        
        
        self.vplacaj = Button(master, text = 'Vplačaj listke',bg = 'RoyalBlue1', bd = 10, command = self.vplacaj_fun, font = 'bold')
        self.vplacaj.grid(row = 1, column = 0)

        self.zrebanje = Button(master, text = 'Začni žrebanje!', bg = 'yellow', bd = 10, font = 'bold')
        self.zrebanje.grid(row=1, column = 1)

        self.dobitki= Button(master, text = 'Preveri dobitke', bg = 'chartreuse2', bd = 10, font = 'bold')
        self.dobitki.grid(row = 1, column = 2)


    def vplacaj_fun(self):

        zgodovina.write("EuroJackpot žrebanje"+"\n")
        zgodovina.write('Datum: {0}'.format(now.strftime('%d.%m.%Y, %H:%M'))+"\n")
        zgodovina.write("Vplačane kombinacije:"+"\n")

        stevilke1 = 1
        stevilke2 = 1

        if test == False:
            krneki = Label(text = 'Vnesli ste napačen niz!', bg = 'light goldenrod')
            krneki.grid(row = 3, column = 1)
            zgodovina.write('Vnesli ste napačen niz!'+"\n")
            zgodovina.write("\n")
            zgodovina.close()
            
        elif test == True:
            
            if st_vrstic > 6:
                krneki = Label(text = 'Vnesli ste preveliko število vplačilnih listkov!', bg = 'light goldenrod')
                krneki.grid(row = 3, column = 1, columnspan = 3)
                zgodovina.write('Vnesli ste preveliko število vplačilnih listkov!'+"\n")
                zgodovina.write("\n")
                zgodovina.close()
                
            elif st_vrstic <= 6:             

                izpis1 = 1
                izpis2 = 1
                element = 0

                peterica_racun = []
                dvojica_racun = []

                racun = Toplevel()
                racun.title("Potrdilo o vplačilu")
                racun.config(bg = 'white')

                racun.minsize(width=335, height=200)
                racun.maxsize(width=335, height = 1000000)

                logo = PhotoImage(file="euro_racun.gif")
                logo = logo.subsample(4,4)
                w1 = Label(racun, image=logo, bg = 'white')
                w1.image = logo
                w1.grid(column = 2, columnspan = 5)


                while izpis1 < st_vrstic:

                    dvojka = skupni_dva[element]
                    petka = skupni_pet[element]

                    listek1 = Label(text = '{0}. polje:'.format(izpis1), bg = 'light goldenrod')
                    listek1.grid(row = izpis1+3, column = 0)
                    listekk1 = Label(text =  petka, bg = 'light goldenrod')
                    listekk1.grid(row = izpis1+3, column = 1)

                    zgodovina.write('{0}. polje: '.format(izpis1))
                    zgodovina.write(''.join(str(number) for number in petka)+" ")

                    for petica in petka:
                       if petica == ',':
                          None
                       else: peterica_racun.append(str(petica).zfill(2))

                    sporocilo1 = Label(racun, text = '{0}. polje:'.format(izpis1), bg = 'white', font = 'Courier 10')
                    sporocilo1.grid(row = izpis1 + 3, column = 2)
                    sporociloo1 = Label(racun, text =  peterica_racun, bg = 'white', font = 'Courier 10 bold')
                    sporociloo1.grid(row = izpis1 + 3, column = 3)
                  
                    izpis1 += 1
                    peterica_racun = []
            
                    listekkk1 = Label(text = dvojka, bg = 'light goldenrod')
                    listekkk1.grid(row = izpis2+3, column = 2)

                    zgodovina.write(''.join(str(number) for number in dvojka)+"\n")

                    for dve in dvojka:
                       if dve == ',':
                          None
                       else: dvojica_racun.append(str(dve).zfill(2))

                    sporociloo1 = Label(racun, text = dvojica_racun, bg = 'white', font = 'Courier 10 bold')
                    sporociloo1.grid(row = izpis2 + 3, column = 5)
                    
                    izpis2 += 1
                    dvojica_racun = []

                    element += 1

                prazno = Label(text = '', bg = 'light goldenrod')
                prazno.grid(row = izpis2+3)            

                vrste = 4

                potrdilo = Label(racun, text='POTRDILO O VPLAČILU', bg = 'white', font = 'Courier 10 bold')
                potrdilo.grid(row = 1, column = 2, columnspan = 4)

                prazno = Label(racun, text = '', bg = 'white')
                prazno.grid(row = 2)

                prazno = Label(racun, text = '', bg = 'white')
                prazno.grid(row = izpis2 + vrste , column = 4)
                vrste += 1

                prazno = Label(racun, text = 'Vplačano za naslednja žrebanja:', bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste , column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = 'ko pritisneš na gumb :)', bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste , column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = '----------------------------------------------', bg = 'white')
                prazno.grid(row = izpis2 + vrste, column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = '{0}, plačano {1:.2f} EUR.'.format(now.strftime('%d.%m.%Y'), znesek), bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste, column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = 'Fakulteta za Matematiko in Fiziko', bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste , column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = 'Uvod v programiranje', bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste , column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = '', bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste , column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = 'Oproščeno plačila.', bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste , column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = 'Loterija Bingl Bongl', bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste , column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = '{0}'.format(now.strftime('%d.%m.%Y, %H:%M')), bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste , column = 2, columnspan = 4)
                vrste += 1

                prazno = Label(racun, text = '', bg = 'white', font = 'Courier 9')
                prazno.grid(row = izpis2 + vrste , column = 2, columnspan = 4)
                vrste += 1

                button = Button(racun, text="Zapri", command=racun.destroy)
                button.grid(row = izpis2 + vrste)

                self.zrebanje.config(command = self.zrebanje_fun)

                vrste_dobitki = vrste

        self.vplacaj.config(state=DISABLED)

        
    def zrebanje_fun(self):
        import random

        i = 1
        j = 1

        stevilke_od_1_do_50 = []
        stevilke_od_1_do_10 = []

        while i < 6:
            izzrebana_stevilka1 = random.randrange(1,50)
            if izzrebana_stevilka1 not in stevilke_od_1_do_50:
                stevilke_od_1_do_50.append(izzrebana_stevilka1)                
                i += 1

        while j < 3:
            izzrebana_stevilka2 = random.randrange(1,10)
            if izzrebana_stevilka2 not in stevilke_od_1_do_10:
                stevilke_od_1_do_10.append(izzrebana_stevilka2)
                j += 1
                
        stevilke_od_1_do_50 = sorted(stevilke_od_1_do_50)
        stevilke_od_1_do_10 = sorted(stevilke_od_1_do_10)

        zgodovina.write('Izžrebane številke:'+"\n")
        zgodovina.write(','.join(str(number) for number in stevilke_od_1_do_50)+' ')
        zgodovina.write(','.join(str(number) for number in stevilke_od_1_do_10)+"\n")

        stevilke_od_1_do_50_2 = []
        for c in stevilke_od_1_do_50:
            stevilke_od_1_do_50_2.append(c)
            fix_stevilke_od_1_do_50.append(c)
            stevilke_od_1_do_50_2.append(',')
        del stevilke_od_1_do_50_2[-1]
        
        stevilke_od_1_do_10_2 = []
        for d in stevilke_od_1_do_10:
            stevilke_od_1_do_10_2.append(d)
            fix_stevilke_od_1_do_10.append(d)
            stevilke_od_1_do_10_2.append(',')
        del stevilke_od_1_do_10_2[-1]

        self.izzrebane_stevilke1.config(text=stevilke_od_1_do_50_2, bg = 'yellow')
        self.izzrebane_stevilke2.config(text=stevilke_od_1_do_10_2, bg = 'yellow')

        self.dobitki.config(command = self.dobitki_fun)

        self.zrebanje.config(state=DISABLED)


    def dobitki_fun(self):

        zgodovina.write('Dobitki:'+"\n")

        prazno = Label(text = ' ', bg = 'light goldenrod')
        prazno.grid(row = st_vrstic + 6 , column = 0)

        prazno = Label(text = 'Dobitki:', bg = 'light goldenrod')
        prazno.grid(row = st_vrstic + 7 , column = 0)

        element = 0
        polozaj = 1

        zadetek_1 = 0
        zadetek_2 = 0

        while polozaj < st_vrstic:
            
           dvojka = skupni_dva[element]
           petka = skupni_pet[element]

           dobitek_5 = 0
           dobitek_2 = 0
           skupni_dobitek = 0

           for due in dvojka:
              if due in fix_stevilke_od_1_do_10:
                 dobitek_2 += 1

           for cinque in petka:
              if cinque in fix_stevilke_od_1_do_50:
                 dobitek_5 += 1

           prazno = Label(text = '{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2), bg = 'light goldenrod')
           prazno.grid(row = st_vrstic + 7 + element, column = 0)

           if dobitek_5 == 0:
               zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 0,00 EUR'+"\n")
               prazno = Label(text = 'Znesek za izplačilo: 0,00 EUR', bg = 'light goldenrod')
               prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
    
           elif dobitek_5 == 1:
               if dobitek_2 == 0:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 0,00 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 0,00 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
               elif dobitek_2 == 1:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 0,00 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 0,00 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
               elif dobitek_2 == 2:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 10,80 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 10,80 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)

           elif dobitek_5 == 2:
               if dobitek_2 == 0:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 0,00 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 0,00 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
               elif dobitek_2 == 1:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 9,10 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 9,10 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
               elif dobitek_2 == 2:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 24,30 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 24,30 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)

           elif dobitek_5 == 3:
               if dobitek_2 == 0:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 18,80 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 18,80 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
               elif dobitek_2 == 1:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 22,60 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 22,60 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
               elif dobitek_2 == 2:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 70,60 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 70,60 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)

           elif dobitek_5 == 4:
               if dobitek_2 == 0:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 149,80 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 149,80 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
               elif dobitek_2 == 1:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 329,80 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 329,80 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
               elif dobitek_2 == 2:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 6.624,20 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 6.624,20 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
                   
           elif dobitek_5 == 5:
               if dobitek_2 == 0:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 417.329,60 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 417.329,60 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)
               elif dobitek_2 == 1:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 1.180.434,00 EUR'+"\n")
                   prazno = Label(text = 'Znesek za izplačilo: 1.180.434,00 EUR', bg = 'light goldenrod')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 2)

               elif dobitek_2 == 2:
                   zgodovina.write('{0}. polje: {1} + {2}'.format(polozaj, dobitek_5, dobitek_2)+'  '+'Znesek za izplačilo: 23.251.598 EUR'+"\n")
                   prazno = Label(text = 'ZADELI STE EUROJACKPOT!!!', bg = 'gold')
                   prazno.grid(row = st_vrstic + 7 + element, column = 1, columnspan = 3)

                   win = Toplevel()
                   win.title('Pa spala bi cel dan')
                   win.config(bg = 'light goldenrod')
                   stric = PhotoImage(file="stric_skopusnik.gif")
                   w2 = Label(win, image=stric, bg = 'light goldenrod')
                   w2.win = stric
                   w2.grid()

           polozaj += 1
           element += 1

        prazno = Label(text = '', bg = 'light goldenrod')
        prazno.grid()
       
        self.dobitki.config(state=DISABLED)
        zgodovina.write("\n")
        zgodovina.close()

root = Tk()
root.title("EuroJackpot")
aplikacija = EuroJaskpot(root)
root.mainloop()
