from random import randint 

class Player(object):
   def __init__(self, lifes):
      self.lifes = lifes
      self.scores = 0
      self.did_hit = False
      self.is_hitted = False

   def fire(self):
        sikta = randint(1, 5) 
        if sikta in {1,2,3}: 
            self.did_hit=True
        undvika = randint(1, 10)
        if undvika in {1,2,3}:
            self.is_hitted = True
     
   def inc_scores(self):
      self.scores= self.scores + 1
      self.did_hit= False

   def reduce_lifes(self):
      self.lifes = self.lifes - 1
      self.is_hitted = False

a_player = Player(3)     

while True:
    input('Tryck Enter för att skjuta')
    a_player.fire()
    if a_player.did_hit:
       print('Träff!')
       a_player.inc_scores() 
    else:
       print('Miss, sikta bättre')
    if a_player.is_hitted:
       print('Aaaaaah, du blev träffad')
       a_player.reduce_lifes() 
    else:
       print('Du klarade dig denna gång!')
    print(f"{a_player.scores} poäng")
    print(f"{a_player.lifes} liv")
    if a_player.lifes <= 0:
       print("du dog")
       break
