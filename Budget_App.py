class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description=''):
        self.deposit(-amount, description)
        succeed = self.check_funds(amount)
        if not succeed:
            return False
        else:
            return True
        
    def get_balance(self):
        balance = 0
        for index, event in enumerate(self.ledger):
            balance += event['amount']
        return balance
            
    def transfer(self, amount, other):
        self.withdraw(amount, f'Transfer to {other.name}')
        other.deposit(amount, f'Transfer from {self.name}')
        succeed = self.check_funds(amount)
        if not succeed:
            return False
        else:
            return True
       
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True        
        
    def __str__(self):
        pass

def create_spend_chart(categories):
    pass