from enum import Enum

# TipIgraca = Enum('TipIgraca', ['X', 'O'])
#StanjePolja = Enum('StanjePolja', ['PRAZNO' ' ', 'X', 'O'])

class StanjePolja(Enum):
  PRAZNO = ' '
  X = 'X'
  O = 'O'

  def __str__(self) -> str:
    return str(super().value)

class TipIgraca(Enum):
  X = 'X'
  O = 'O'

  def __str__(self) -> str:
    return str(super().value)