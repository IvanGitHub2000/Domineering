
from enumeratori import StanjePolja, TipIgraca
from konvertovanje import int_u_slovo, int_u_vrstu


class Tabla:
  def __init__(this) -> None:
    print("Izbor parametara za tablu\n ")
    unos = int(input("Broj vrsta table: "))
    while unos < 1 or unos > 25:
      unos =  int(input("Pogresan unos! Tabla moze imati najmanje 1 a najvise 25 vrsti \nBroj vrsta table:"))
    this.brojVrsta = unos

    unos = int(input("Broj kolona table: "))
    while unos < 1 or unos > 25:
      unos =  int(input("Pogresan unos! Tabla moze imati najmanje 1 a najvise 25 kolona \nBroj kolona table:"))
    this.brojKolona = unos

    this.matrica = [[StanjePolja.PRAZNO for i in range(this.brojKolona)] for j in range(this.brojVrsta)]
    this.trenutno_igra = TipIgraca.X

  def stampaj(this):
    this.stampajKolone()

    print('  ',end ='') 
    for i in range(0, this.brojKolona):
      print(' =',end='')
    print('')

    for i in range(0 ,this.brojVrsta):
      print(str(this.brojVrsta-i)+"||",end='')
      for j in range(0,this.brojKolona):
        print(str(this.matrica[i][j])+'|',end='')
      print("|"+str(this.brojVrsta-i), end='\n')
      print('  ',end ='')
      if(i < this.brojVrsta - 1):
        for j in range(0,this.brojKolona):
          print(' -',end='')
        print('')

    for i in range(0, this.brojKolona):
      print(' =',end='')
    print('')

    this.stampajKolone()

  def stampajKolone(this):
    print('  ',end ='')
    for i in range(0, this.brojKolona):
      print(' ' + int_u_slovo(i) ,end='')
    print('')

  def moguca_stanja(this, trenutno_igra, stampanje):
    moguca_stanja_str = []
    moguca_stanja = []
    if(stampanje):
      print("-------------------- Prikaz svih mogucih poteza -----------------")
    if(trenutno_igra == TipIgraca.X):
      for i in range(1,this.brojVrsta):
        for j in range(0,this.brojKolona):
          if(this.validiraj_potez(i,j, trenutno_igra) == True):
            if(stampanje):
              this.promeni_stanje(i, j, StanjePolja.X, TipIgraca.X)
              this.stampaj()
              print("Potez: [" + str(int_u_vrstu(i, this.brojVrsta)) + " - " + int_u_slovo(j)+ "]", end ="\n\n")
              this.promeni_stanje(i, j, StanjePolja.PRAZNO, TipIgraca.X)
              moguca_stanja_str.append(str(int_u_vrstu(i, this.brojVrsta)) + " - " + int_u_slovo(j))
            moguca_stanja.append([i,j])
    else:
      for i in range(0,this.brojVrsta):
        for j in range(0,this.brojKolona-1):
          if(this.validiraj_potez(i, j, trenutno_igra) == True):
            if(stampanje):
              this.promeni_stanje(i, j, StanjePolja.O, TipIgraca.O)
              this.stampaj()
              print("Potez: [" +str(int_u_vrstu(i,this.brojVrsta)) + " - " + int_u_slovo(j) + "]", end ="\n\n")
              this.promeni_stanje(i, j, StanjePolja.PRAZNO, TipIgraca.O)
              moguca_stanja_str.append(str(int_u_vrstu(i, this.brojVrsta)) + " - " + int_u_slovo(j))
            moguca_stanja.append([i,j])
    if(stampanje):
      print("Mozete odigrati sledece poteze: ")
      for stanje in moguca_stanja_str:
        print("[" + stanje + "]")
    return moguca_stanja

  def promeni_stanje(this, vrsta, kolona, stanje, tip_igraca):
    if(tip_igraca == TipIgraca.X):
      this.matrica[vrsta][kolona] = stanje
      this.matrica[vrsta - 1][kolona] = stanje
    else:
      this.matrica[vrsta][kolona] = stanje
      this.matrica[vrsta][kolona+1] = stanje
  
  def validiraj_potez(this, vrsta, kolona, trenutno_igra):
    if(trenutno_igra == TipIgraca.X):
      if(vrsta-1 < 0 or vrsta >= this.brojVrsta or kolona < 0 or kolona>=this.brojKolona):
        return 'Van Table!'
      if(this.matrica[vrsta][kolona]==StanjePolja.PRAZNO and this.matrica[vrsta-1][kolona]==StanjePolja.PRAZNO):
        return True
      else:
        return 'Polje zauzeto!'
    else:
      if(vrsta < 0 or vrsta >= this.brojVrsta or kolona < 0 or kolona + 1>=this.brojKolona):
        return 'Van Table!'
      if(this.matrica[vrsta][kolona]==StanjePolja.PRAZNO and this.matrica[vrsta][kolona+1]==StanjePolja.PRAZNO):
        return True
      else:
        return 'Polje zauzeto!'
  
  def odigraj(this, pozicija, stampa):
    i = pozicija[0]
    j = pozicija[1]
    provera = this.validiraj_potez(i,j, this.trenutno_igra)
    if this.trenutno_igra == TipIgraca.X: # X
        if provera == True:
            this.matrica[i][j] = StanjePolja.X
            this.matrica[i-1][j] = StanjePolja.X
            if(stampa):
              this.stampaj()
              print("Igrac X je odigrao potez: [" + str(int_u_vrstu(i, this.brojVrsta)) + "," + int_u_slovo(j) + "]")
            this.promeni_trenutnog()
        elif(stampa):
            print(provera)
    else: # O
        if provera == True:
            this.matrica[i][j] = StanjePolja.O
            this.matrica[i][j+1] = StanjePolja.O
            if(stampa):
              this.stampaj()
              print("Igrac O je odigrao potez: [" + str(int_u_vrstu(i, this.brojVrsta)) + "," + int_u_slovo(j) + "]")
            this.promeni_trenutnog()
        elif(stampa):
            print(provera)
  
  def promeni_trenutnog(this):
    if(this.trenutno_igra == TipIgraca.X):
      this.trenutno_igra = TipIgraca.O
    else:
      this.trenutno_igra = TipIgraca.X