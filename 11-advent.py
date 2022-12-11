# Part 1




class Monkey:
    
    def __init__(self, starting_items, operation, modulus, monkey_if, monkey_else):
        self.items = starting_items
        self.operation = operation
        self.modulus = modulus
        self.monkey_if = monkey_if
        self.monkey_else = monkey_else
        self.monkeybusiness = 0
    
    def __str__(self):
        return f"Monkey with {len(self.items)} items who wants to divide by {self.modulus}"
    
    def item_value(self, old):
        result = eval(self.operation)
        result = int(result / 3)
        return result

    
    def throw_dest(self, item):
        if self.item_value(item) % self.modulus == 0:
            return self.monkey_if
        else:
            return self.monkey_else
    
    def catch_item(self, item):
        self.items.append(item)
    
    def throw_item(self, receiving_monkey):
        item = self.item_value(self.items[-1])
        receiving_monkey.catch_item(item)
        self.items.pop()
        self.monkeybusiness += 1
    
    # new methods for part 2!
    # if the number is larger than the product of all
    # moduli (all primes), reduce the number by that product
    # new methods should also work for part 1
    
    def item_value_new(self, old, prime_prod):
        result = eval(self.operation)
        return result % prime_prod
    
    def throw_dest_new(self, item, prime_prod):
        if self.item_value_new(item, prime_prod) % self.modulus == 0:
            return self.monkey_if
        else:
            return self.monkey_else
    
    def throw_item_new(self, receiving_monkey, prime_prod):
        item = self.item_value_new(self.items[-1], prime_prod)
        receiving_monkey.catch_item(item)
        self.items.pop()
        self.monkeybusiness += 1

def Monkey_from_text(text):
    starting_items = [int(item) for item in text[0].split(": ")[1].split(", ")]
    operation = text[1].split("= ")[1]
    modulus = int(text[2].split("by ")[1])
    monkey_if = int(text[3].split("monkey ")[1])
    monkey_else = int(text[4].split("monkey ")[1])
    return Monkey(starting_items, operation, modulus, monkey_if, monkey_else)

def inspect_monkeybusiness(monkey_list):
    for monkey in monkey_list:
        while len(monkey.items) > 0:
            item = monkey.items[-1]
            receiving_monkey = monkey_list[monkey.throw_dest(item)]
            monkey.throw_item(receiving_monkey)

with open("data/11-example.txt") as f:
    input_data = [line.strip() for line in f.readlines()]
    example_monkeys = [input_data[i:i+5] for i in range(1, len(input_data), 7)]

with open("data/11-input.txt") as f:
    input_data = [line.strip() for line in f.readlines()]
    monkeys = [input_data[i:i+5] for i in range(1, len(input_data), 7)]

monkey_list = [Monkey_from_text(monkey) for monkey in monkeys]


for i in range(20):
    inspect_monkeybusiness(monkey_list)

final_monkeybusiness = [monkey.monkeybusiness for monkey in monkey_list]
final_monkeybusiness.sort()
print(final_monkeybusiness[-1] * final_monkeybusiness[-2])

# part 2

def inspect_monkeybusiness_new(monkey_list, prime_prod):
    for monkey in monkey_list:
        while len(monkey.items) > 0:
            item = monkey.items[-1]
            receiving_monkey = monkey_list[monkey.throw_dest_new(item, prime_prod)]
            monkey.throw_item_new(receiving_monkey, prime_prod)

def get_prime_prod(monkey_list):
    prod = 1
    for monkey in monkey_list:
        prod *= monkey.modulus
    return prod

ex_monkey_list = [Monkey_from_text(monkey) for monkey in example_monkeys]

ex_prime_prod = get_prime_prod(ex_monkey_list)

for i in range(10000):
    inspect_monkeybusiness_new(ex_monkey_list, ex_prime_prod)

ex_business = [monkey.monkeybusiness for monkey in ex_monkey_list]
ex_business.sort()
print(ex_business[-1]*ex_business[-2])

#with full input

monkey_list = [Monkey_from_text(monkey) for monkey in monkeys]
prime_prod = get_prime_prod(monkey_list)
for i in range(10000):
    inspect_monkeybusiness_new(monkey_list, prime_prod)

too_much_monkey_business = [monkey.monkeybusiness for monkey in monkey_list]
too_much_monkey_business.sort()
print(too_much_monkey_business)
print(too_much_monkey_business[-1] * too_much_monkey_business[-2])
