
class Enployee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Enployee.num_of_emps += 1

    def fulname(self):
        return '{} {}'.format(self.first, self.last)

        def apply_raise(self): 
            self.pay = int(self.pay * self.raise_amount)


print(Enployee.num_of_emps)

emp_1 = Enployee('Corey', 'Schafter', 50000)
emp_2 = Enployee('Test', 'User', 60000)

print(Enployee.num_of_emps)
