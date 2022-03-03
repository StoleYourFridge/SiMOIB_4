import random


def nod_algorithm(first, second):
    while first != second:
        if first > second:
            first = first - second
        else:
            second = second - first
    return first


def find_amount_of_one_noded_operands(p_operand):
    current_amount = 0
    for example in range(1, p_operand):
        if nod_algorithm(p_operand, example) == 1:
            current_amount += 1
    return current_amount


def is_it_operand_checker(g_operand, p_operand, max_pow):
    if pow(g_operand, max_pow) % p_operand != 1:
        return False
    for example in range(max_pow - 1, 0, -1):
        if pow(g_operand, example) % p_operand == 1:
            return False
    return True


def find_g_operand(p_operand):
    g_operand = 1
    amount_of_one_noded_operands = find_amount_of_one_noded_operands(p_operand)
    while not is_it_operand_checker(g_operand, p_operand, amount_of_one_noded_operands):
        g_operand += 1
    return g_operand


class Human:
    def __init__(self, p_operand):
        self.p_operand = p_operand
        self.g_operand = find_g_operand(self.p_operand)
        self.own_secret_value = random.randrange(0, 1000)
        self.own_public_value = pow(self.g_operand, self.own_secret_value) % self.p_operand
        self.other_public_value = None
        self.general_key = None

    def share_public_value(self, other):
        other.other_public_value = self.own_public_value

    def __str__(self):
        return "p : {0}, g : {1}, secret : {2}, public : {3}, other values : {4}, general key : {5}".format(
                                                                                        self.p_operand,
                                                                                        self.g_operand,
                                                                                        self.own_secret_value,
                                                                                        self.own_public_value,
                                                                                        self.other_public_value,
                                                                                        self.general_key)

    def get_general_key(self):
        self.general_key = pow(self.other_public_value, self.own_secret_value) % self.p_operand


Alice, Bob = Human(5717), Human(5717)
Alice.share_public_value(Bob)
Bob.share_public_value(Alice)
Alice.get_general_key()
Bob.get_general_key()
print(Alice)
print(Bob)