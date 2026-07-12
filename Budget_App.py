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
        lines = []
        lenght_name = len(self.name)
        rest_of_title_line = 30 - lenght_name
        if rest_of_title_line % 2 == 0:
            title_line = (rest_of_title_line // 2) * '*' + self.name + (rest_of_title_line // 2) * '*'
        else:
            title_line = (rest_of_title_line // 2) * '*' + self.name + (rest_of_title_line // 2 + 1) * '*'
        lines.append(title_line)
        for index, event in enumerate(self.ledger):
            line = event['description'][:23]
            lenght_description = len(line)
            if isinstance(event['amount'], float):
                price = str(event['amount'])
            else:
                price = str(float(event['amount']))
            if price[-2] == '.':
                price += '0'
            if not price[-3] == '.':
                price = price[:price.find('.')+3]
            lenght_price = len(price)
            line += (30 - lenght_description - lenght_price) * ' ' + price
            lines.append(line)
        end_line = f'Total: {self.get_balance()}'
        text = ''
        for line in lines:
            text += f'{line}\n'
        text += end_line
        return text

def create_spend_chart(categories):
    pass