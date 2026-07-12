class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description=''):        
        succeed = self.check_funds(amount)
        if not succeed:
            return False
        else:
            self.deposit(-amount, description)
            return True
        
    def get_balance(self):
        balance = 0
        for event in self.ledger:
            balance += event['amount']
        return balance
            
    def transfer(self, amount, other):       
        succeed = self.check_funds(amount)
        if not succeed:
            return False
        else:
            self.withdraw(amount, f'Transfer to {other.name}')
            other.deposit(amount, f'Transfer from {self.name}')
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
        for event in self.ledger:
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
    chart = 'Percentage spent by category'
    max_lenght_category = 0
    lenght_names = []
    spends = []
    line_ = '    '
    for category in categories:
        line_ += '---'
        spend = 0
        lenght_name = len(category.name)
        lenght_names.append(lenght_name)
        if lenght_name > max_lenght_category:
            max_lenght_category = lenght_name
        for event in category.ledger:
            if event['amount'] < 0 :
                spend += abs(event['amount'])
        spends.append(spend)
    all_spends = sum(spends)
    percent_spends = []
    for i in spends:
        if all_spends > 0:
            percent = i / all_spends * 100
        else:
            percent = 0
        percent_spends.append(percent//10 * 10)
    for i in range(11):
        line = f'{10 * (10 - i)}|'
        for j in percent_spends:
            if j >= 10 * (10 - i):
                line += ' o '
            else:
                line += '   '
        if i == 0:
            chart += f'\n{line} '
        elif i == 10:
            chart += f'\n  {line} '
        else:
            chart += f'\n {line} '
    line_ += '-'
    chart += f'\n{line_}'
    for i in range(max_lenght_category):
        line = 4 * ' '
        for index, category in enumerate(categories):
            if not lenght_names[index] < i + 1:
                line += ' ' + f'{category.name[i]}' + ' '
            else:
                line += '   '
        line += ' '
        chart += f'\n{line}'
    return chart