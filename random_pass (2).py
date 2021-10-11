import string
import random


class password_clarificataion:
    def special(self, a):
        self.a = a
        if a is True:
            print("your password has special character")
        elif a is False:
            print("your password doesn't have special character")
        else:
            print("unvalid input")
        # print("fdfd")
        return self

    def upper(self, b):
        self.b = b
        if b is True:
            print("your password has upper character")
        elif b is False:
            print("your password doesn't have upper character")
        else:
            print("unvalid input")
        return self

    def lower(self, c):
        self.c = c
        if c is True:
            print("your password has lower character")
        elif c is False:
            print("your password doesn't have lower character")
        else:
            print("unvalid input")
        return self

    def digits(self, d):
        self.d = d
        if d is True:
            print("your password has digits character")
        elif d is False:
            print("your password doesn't have digits character")
        else:
            print("unvalid input")
        return self

    def generate(self):
        return self


class password_generation:

    def special(self, a):
        self.a = a
        if type(a) == int:
            a = "".join(
                random.choice(string.punctuation) for i in range(int(a)))
            self.a = list(a)
        else:
            print("unvalid input")
        return self

    def upper(self, b):
        self.b = b
        if type(b) == int:
            b = "".join(
                random.choice(string.ascii_uppercase) for i in range(int(b)))
            self.b = list(b)
        else:
            print("unvalid input")
        return self

    def lower(self, c):
        self.c = c
        if type(c) == int:
            c = "".join(
                random.choice(string.ascii_lowercase) for i in range(int(c)))
            self.c = list(c)
        else:
            print("unvalid input")
        return self

    def digits(self, d):
        self.d = d
        if type(d) == int:
            d = "".join(
                random.choice(string.digits) for i in range(int(d)))
            self.d = list(d)
        else:
            print("unvalid input")
        return self

    def generate(self):
        if len(self.a) + len(self.b) + len(self.c) + len(self.d) >= 8:
            x = "".join(
                self.a + self.b + self.c + self.d)
            x = list(x)
            random.shuffle(x)
        # print(x)
            print("".join(x))
        else:

            self.a = "".join(
                random.choice(string.punctuation) for i in range(int(2)))
            self.a = list(self.a)            

            self.b = "".join(
                random.choice(string.ascii_uppercase) for i in range(int(2)))
            self.b = list(self.b)

            self.c = "".join(
                random.choice(string.ascii_lowercase) for i in range(int(2)))
            self.c = list(self.c)

            self.d = "".join(
                random.choice(string.digits) for i in range(int(2)))
            self.d = list(self.d)
            x = "".join(
                self.a + self.b + self.c + self.d)
            x = list(x)
            random.shuffle(x)
        # print(x)
            print("".join(x))

            return self


print(
    password_clarificataion().special(False)
    .upper(True).lower(True).digits(True).generate()
    )


print(
    password_generation().special(0)
    .upper(0).lower(0).digits(5).generate()
    )
