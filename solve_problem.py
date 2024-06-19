def to_base(number, base):
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = []
    while number != 0:
        r = number % base
        number = number // base
        digits.insert(0, r)
    #return digits
    return "".join([mapping[d] for d in digits])

print(to_base(17, 3))
print(to_base(23, 4))
print(to_base(255, 16))