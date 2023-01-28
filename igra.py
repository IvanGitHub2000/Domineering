import os
from enumeratori import TipIgraca
from konvertovanje import int_u_slovo, int_u_vrstu, slovo_u_int
from racunar import Racunar
from tabla import Tabla
from enumeratori import StanjePolja

class Igra:
  def __init__(this) -> None:
    this.odabir_igraca()
    this.tabla = Tabla()
    this.racunar = Racunar()
    this.tabla.stampaj()

  def odabir_igraca(this):
      this.ocisti_konzolu()
      print("Pravila igre Domineering:")
      print("Korisnik na pocetku bira da li zeli da bude X ili O.Njegove figure ce biti predstavljene na tabli u zavisnosti od njegovog izbora.")
      print("Dalje, korisnik je u mogucnosti da odabere dimenzije table na kojoj ce se ova igra igrati.")
      print("X uvek igra prvi i bira polje na kojoj ce postaviti figuru.")
      print("Figura je dimenzija 2x1 za X i 1x2 za O.")
      print("Primer postavljanja figure na tabli: Ukoliko korisnik koji je X unese polje [1 A], figura ce biti postavljena na polju [1 A] i polju [2 A].")
      print("Slicno i za O,ukoliko korisnik unese polje [1 A] figura ce biti postavljena na poljima [1 A] [1 B].")
      print("Ukoliko dodje do loseg unosa u konzoli,korisniku ce biti ispisano zbog cega je doslo do greske.")
      print("Dalje ako je potez od X-a validan, na potezu ce biti O,i obrnuto.")
      print("Igraci ce vuci poteze periodicno, sve dok se ne dodje do kraja igre,odnosno sve dok neki igrac ne bude bio u stanju da unese svoju figuru na tablu.")
      unos = input("Molimo izaberite koji igrac zelite da budete [X/0] \n==>(Ukoliko odaberete X bicete prvi na potezu)\n==>  ")
      while unos not in ['X', 'x', 'O','o']:
        unos = input("Pogresan unos! \nMolimo izaberite koji igrac zelite da budete [X/0] ")
      if(unos=='X' or unos == 'x'):
        this.tip_igraca = TipIgraca.X
      elif(unos=='O' or unos == 'o'):
        this.tip_igraca = TipIgraca.O
      print("Izabrali ste igraca " + ('X\n' if this.tip_igraca == TipIgraca.X else 'O\n'))
      dubinaString = input("Unesite maksimalnu dubinu: ")
      while not dubinaString.isdigit():
        dubinaString =  input("Pogresan unos, dubina se predstavlja cifrom! \nUnesite maksimalnu dubinu ")
      this.dubina = int(dubinaString)

  
  def zapocni_igru(this):
    while not this.kraj_igre():
      this.novi_potez()
    else:
      print("Kraj igre! \nPobednik je " + ("X" if this.nadji_pobednika() == TipIgraca.X else "O"))

  def novi_potez(this):
    print('Trenutno na potezu: ' + str(this.tabla.trenutno_igra))
    if this.tabla.trenutno_igra == this.tip_igraca:
      vrsta, kolona = this.unos_poteza()
      this.tabla.odigraj([vrsta,kolona], True)
    else:
      vrsta, kolona = this.racunar.minimax(this.tabla, this.dubina, this.tabla.trenutno_igra)
      this.tabla.odigraj([vrsta,kolona], True)
      
  def unos_poteza(this):
      print("Ukoliko zelite da vidite sve preostale moguce poteze unesite /h(elp)")
      vrstaString = input("Unesite vrstu u opsegu od [1-" + str(this.tabla.brojVrsta) + "]: ")
      while not vrstaString.isdigit():
        if(vrstaString == "/h" or vrstaString == "/help"):
          this.tabla.moguca_stanja(this.tabla.trenutno_igra, True)
          vrstaString = input("Unesite vrstu u opsegu od [1-" + str(this.tabla.brojVrsta) + "]: ")
        else:
          vrstaString =  input("Pogresan unos, vrsta se predstavlja cifrom! \nUnesite vrstu: [1-" + str(this.tabla.brojVrsta) + "] ")
      vrsta = int(vrstaString)
      vrsta = this.tabla.brojVrsta-vrsta
      kolonaString = input("Unesite kolonu u opsegu od [A-" + int_u_slovo(this.tabla.brojKolona-1) + "]: ")
      while not kolonaString.isalpha():
        kolonaString = input("Pogresan unos, kolona se predstavlja slovom! \nUnesite kolonu: [A-" + int_u_slovo(this.tabla.brojKolona-1) + "] ")
      kolona = slovo_u_int(kolonaString)
      return vrsta,kolona

  def kraj_igre(this):
    if(this.tabla.trenutno_igra == TipIgraca.X):
      for i in range(1,this.tabla.brojVrsta):
        for j in range(0,this.tabla.brojKolona):
          if(this.tabla.matrica[i][j]==StanjePolja.PRAZNO and this.tabla.matrica[i-1][j]==StanjePolja.PRAZNO):
            return False
    else:
      for i in range(0,this.tabla.brojVrsta):
        for j in range(0,this.tabla.brojKolona-1):
          if(this.tabla.matrica[i][j]==StanjePolja.PRAZNO and this.tabla.matrica[i][j+1]==StanjePolja.PRAZNO):
            return False
    return True

      
  def nadji_pobednika(this):
    if(this.tabla.trenutno_igra == TipIgraca.X):
      return TipIgraca.O
    else:
      return TipIgraca.X
      
  def ocisti_konzolu(this):
    os.system('cls')
  
