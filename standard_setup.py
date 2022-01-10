from pieces import Knight, Piece, Pawn, King, Rook, Bishop, Queen

wQRp = Pawn('wP', 275, 325)
wQNp = Pawn('wP', 325, 325)
wQBp = Pawn('wP', 375, 325)
wQp = Pawn('wP', 425, 325)
wKp = Pawn('wP', 475, 325)
wKBp = Pawn('wP', 525, 325)
wKNp = Pawn('wP', 575, 325)
wKRp = Pawn('wP', 625, 325)

bKRp = Pawn('bP', 275, 75)
bKNp = Pawn('bP', 325, 75)
bKBp = Pawn('bP', 375, 75)
bKp = Pawn('bP', 425, 75)
bQp = Pawn('bP', 475, 75)
bQBp = Pawn('bP', 525, 75)
bQNp = Pawn('bP', 575, 75)
bQRp = Pawn('bP', 625, 75)

wQR = Rook('wR', 275, 375)
wQN = Knight('wN', 325, 375)
wQB = Bishop('wB', 375, 375)
wQ = Queen('wQ', 425, 375)
wK = King('wK', 475, 375)
wKB = Bishop('wB', 525, 375)
wKN = Knight('wN', 575, 375)
wKR = Rook('wR', 625, 375)

bKR = Rook('bR', 275, 25)
bKN = Knight('bN', 325, 25)
bKB = Bishop('bB', 375, 25)
bK = Queen('bQ', 425, 25)
bQ = King('bK', 475, 25)
bQB = Bishop('bB', 525, 25)
bQN = Knight('bN', 575, 25)
bQR = Rook('bR', 625, 25)


standard_setup = [
  wQR,
  wQN,
  wQB,
  wQ,
  wK,
  wQRp,
  wQNp,
  wQBp,
  wQp,
  wKp,
  wKBp,
  wKNp,
  wKRp,
  bKRp,
  bKNp,
  bKBp,
  bKp,
  bQp,
  bQBp,
  bQNp,
  bQRp,
  wKB,
  wKN,
  wKR,
  bKR,
  bKN,
  bKB,
  bK,
  bQ, 
  bQB,
  bQN,
  bQR
]