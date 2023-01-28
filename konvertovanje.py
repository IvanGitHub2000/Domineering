def slovo_u_int(kolonaString):
  kolona = ord(kolonaString) - (ord('A') if ord(kolonaString) >= ord('A') and ord(kolonaString) <= ord('Z') else ord('a'))
  return kolona

def int_u_slovo(broj):
  return chr(ord('A') + broj)

def int_u_vrstu(broj, brojVrsta):
  return brojVrsta - broj