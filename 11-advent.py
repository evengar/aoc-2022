# Part 1

with open("data/11-example.txt") as f:
    input_data = [line.strip() for line in f.readlines()]
    example_monkeys = [input_data[i:i+5] for i in range(1, len(input_data), 7)]

with open("data/11-input.txt") as f:
    input_data = [line.strip() for line in f.readlines()]
    monkeys = [input_data[i:i+5] for i in range(1, len(input_data), 7)]

print(monkeys)
expr = monkeys[0][1].split("= ")[1]
old = 2
print(eval(expr))
print([int(item) for item in monkeys[0][0].split(": ")[1].split(", ")])


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
        
    def item_value_new(self, old):
        result = eval(self.operation)
        return result % self.modulus
    
    def throw_dest_new(self, item):
        if self.item_value_new(item) == 0:
            return self.monkey_if
        else:
            return self.monkey_else
    
    def throw_item_new(self, receiving_monkey):
        item = self.item_value_new(self.items[-1])
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

testmonkey1 = Monkey_from_text(monkeys[0])
testmonkey2 = Monkey_from_text(monkeys[1])
print(testmonkey1)
testmonkey1.throw_item(testmonkey2)
print(testmonkey1.items)
print(testmonkey2.items)

def inspect_monkeybusiness(monkey_list):
    for monkey in monkey_list:
        while len(monkey.items) > 0:
            item = monkey.items[-1]
            receiving_monkey = monkey_list[monkey.throw_dest(item)]
            monkey.throw_item(receiving_monkey)



ex_monkey_list = [Monkey_from_text(monkey) for monkey in example_monkeys]
print([monkey.items for monkey in ex_monkey_list])
example_round = inspect_monkeybusiness(ex_monkey_list)
print([monkey.items for monkey in ex_monkey_list])

#print([monkey.monkeybusiness for monkey in inspect_monkeybusiness(ex_monkey_list)])


monkey_list = [Monkey_from_text(monkey) for monkey in monkeys]


for i in range(20):
    inspect_monkeybusiness(monkey_list)

final_monkeybusiness = [monkey.monkeybusiness for monkey in monkey_list]
final_monkeybusiness.sort()
print(final_monkeybusiness[-1] * final_monkeybusiness[-2])

# part 2

def inspect_monkeybusiness_new(monkey_list):
    for monkey in monkey_list:
        while len(monkey.items) > 0:
            item = monkey.items[-1]
            receiving_monkey = monkey_list[monkey.throw_dest_new(item)]
            monkey.throw_item_new(receiving_monkey)

ex_monkey_list = [Monkey_from_text(monkey) for monkey in example_monkeys]

# for i in range(10000):
#     inspect_monkeybusiness_new(ex_monkey_list)


print([monkey.monkeybusiness for monkey in ex_monkey_list])


# this is why it's wrong
orig = 1501


print((1501) % 23) # 6
print((1501 + 3) % 13) #9
print(((1501%13) + 3) % 13) #9
print((1501 + 3 + 6) % 19)
print(1501%19)
print((3 + 6) % 19)

print(1500 % 19, (1500 % 19) % 19)
print(1500 % 19, (1500 % 19) % 19)


print()



# print((1501 * 1501)%23)
# print((6*6) % 23)
# for i in range(10000):
#     inspect_monkeybusiness(ex_monkey_list)

# print([monkey.monkeybusiness for monkey in monkey_list])