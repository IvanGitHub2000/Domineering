import copy
import math
import random
from tabla import Tabla
from enumeratori import StanjePolja, TipIgraca

class Racunar:

    def minimax(this, tabla: Tabla, dubina, trenutno_igra):

        alpha = (tabla.moguca_stanja(tabla.trenutno_igra, False)[0], -math.inf)
        beta = (tabla.moguca_stanja(tabla.trenutno_igra, False)[0], math.inf)
        for s in tabla.moguca_stanja(tabla.trenutno_igra, False):
            nova_tabla = copy.deepcopy(tabla)
            nova_tabla.odigraj(s, False)
            alpha = max(alpha,
                    this.min_value(s, dubina - 1, trenutno_igra, alpha, beta, nova_tabla),
                    key=lambda x: x[1])
        return alpha[0]
    

    def max_value(this, stanje, dubina, trenutno_igra, alpha, beta, tabla: Tabla):
        if dubina == 0:
            return (stanje, this.heuristika(tabla, trenutno_igra,stanje))
        else:
            for s in tabla.moguca_stanja(tabla.trenutno_igra, False):
                nova_tabla = copy.deepcopy(tabla)
                nova_tabla.odigraj(s, False)
                alpha = max(alpha,
                        this.min_value(stanje, dubina - 1, trenutno_igra, alpha, beta, nova_tabla),
                        key=lambda x: x[1])
                if alpha[1] >= beta[1]:
                    return beta
        return alpha


    def min_value(this, stanje, dubina, trenutno_igra, alpha, beta, tabla: Tabla):
        if dubina == 0:
            return (stanje, this.heuristika(tabla, trenutno_igra,stanje))
        else:
            for s in tabla.moguca_stanja(tabla.trenutno_igra, False):
                nova_tabla = copy.deepcopy(tabla)
                nova_tabla.odigraj(s, False)
                beta = min(beta,
                        this.max_value(stanje, dubina - 1, trenutno_igra, alpha, beta, nova_tabla),
                        key=lambda x: x[1])
                if beta[1] <= alpha[1]:
                    return alpha
        return beta

    def heuristika(this, tabla: Tabla, trenutno_igra,stanje):

        tabla.odigraj(stanje, False)
        prvi=len(tabla.moguca_stanja(trenutno_igra, False))
        drugi=len(tabla.moguca_stanja(TipIgraca.X if trenutno_igra == TipIgraca.O else TipIgraca.O, False))#svei potezi pre nego da odigram
        
        potezi_oks=0
        potezi_iks=0
        if trenutno_igra==TipIgraca.O:
            for vrsta in range(0,tabla.brojVrsta):
             for kolona in range(0,tabla.brojKolona-1):
                if tabla.matrica[vrsta][kolona]==StanjePolja.O and tabla.matrica[vrsta][kolona+1]==StanjePolja.O:
                    if tabla.validiraj_potez(vrsta+2,kolona,trenutno_igra)=="Van Table!" or tabla.validiraj_potez(vrsta+2,kolona,trenutno_igra)=="Polje zauzeto!":
                      if tabla.validiraj_potez(vrsta+2,kolona+1,trenutno_igra)=="Van Table!" or  tabla.validiraj_potez(vrsta+2,kolona+1,trenutno_igra)=="Polje zauzeto!":
                        if tabla.validiraj_potez(vrsta+1,kolona,trenutno_igra)==True and tabla.validiraj_potez(vrsta+1,kolona+1,trenutno_igra)==True:#slobodna polja
                             potezi_oks+=5
                             break
                    if tabla.validiraj_potez(vrsta-2,kolona,trenutno_igra)=="Van Table!" or tabla.validiraj_potez(vrsta-2,kolona,trenutno_igra)=="Polje zauzeto!":
                      if tabla.validiraj_potez(vrsta-2,kolona+1,trenutno_igra)=="Van Table!" or  tabla.validiraj_potez(vrsta-2,kolona+1,trenutno_igra)=="Polje zauzeto!":      
                        if tabla.validiraj_potez(vrsta-1,kolona,trenutno_igra)==True and tabla.validiraj_potez(vrsta-1,kolona+1,trenutno_igra)==True:
                           potezi_oks+=5
                           break

        elif trenutno_igra==TipIgraca.X:
         for vrsta in range(1,tabla.brojVrsta):
          for kolona in range(0,tabla.brojKolona):
            if tabla.matrica[vrsta][kolona]==StanjePolja.X and tabla.matrica[vrsta-1][kolona]==StanjePolja.X:
                if tabla.validiraj_potez(vrsta,kolona-2,trenutno_igra)=="Van Table!" or tabla.validiraj_potez(vrsta,kolona-2,trenutno_igra)=="Polje zauzeto!": 
                    if tabla.validiraj_potez(vrsta-1,kolona-2,trenutno_igra)=="Van Table!" or  tabla.validiraj_potez(vrsta-1,kolona-2,trenutno_igra)=="Polje zauzeto!":
                        if tabla.validiraj_potez(vrsta,kolona-1,trenutno_igra)==True and tabla.validiraj_potez(vrsta-1,kolona-1,trenutno_igra)==True:
                          potezi_iks+=5
                          break
                if tabla.validiraj_potez(vrsta,kolona+2,trenutno_igra)=="Van Table!" or tabla.validiraj_potez(vrsta,kolona+2,trenutno_igra)=="Polje zauzeto!":
                   if tabla.validiraj_potez(vrsta-1,kolona+2,trenutno_igra)=="Van Table!" or tabla.validiraj_potez(vrsta-1,kolona+2,trenutno_igra)=="Polje zauzeto!": 
                    if tabla.validiraj_potez(vrsta,kolona+1,trenutno_igra)==True and tabla.validiraj_potez(vrsta-1,kolona+1,trenutno_igra)==True:
                        potezi_iks+=5
                        break

        if trenutno_igra==TipIgraca.O:
            return prvi - drugi + potezi_oks
        elif trenutno_igra==TipIgraca.X:
            return  prvi - drugi + potezi_iks   
