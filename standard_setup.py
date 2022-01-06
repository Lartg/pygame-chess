from pieces import Knight, Piece, Pawn, King, Rook, Bishop, Queen

wQR = Rook('wR', 275, 375)
wQN = Knight('wN', 325, 375)
wQB = Bishop('wB', 375, 375)
wQ = Queen('wQ', 425, 375)
wK = King('wK', 475, 375)

standard_setup = [
  wQR,
  wQN,
  wQB,
  wQ,
  wK
]