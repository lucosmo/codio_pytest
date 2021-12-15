class InsufficientAmount(Exception): 

  pass 

   
class Wallet(object): 

  def __init__(self, initial_amount=0): 

    self.balance = initial_amount 

  

  def spend_cash(self, amount): 

    if self.balance < amount: 

      raise InsufficientAmount('Not enough available to spend {}'.format(amount)) 

  #  self.balance -= amount 
  #  changed to fail the test
    self.balance -= amount + 1
  

  def add_cash(self, amount): 

    self.balance += amount 

