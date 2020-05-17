from math import gcd
from random import randint, sample


class RSA:
    def __init__(self):
        self.p = 3
        self.q = 3
        self.d = 0
        self.e = 0

        self.init()

    def init(self):
        self.find_primes()
        self.find_keys()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "<RSA object at {} (p: {}, q: {}, n: {}, phi(n): {}, d: {}, e: {})>" \
            .format(hex(id(self)), self.p, self.q, self.n, self.phin, self.d, self.e)

    @property
    def n(self):
        return self.p * self.q

    @property
    def phin(self):
        return (self.p - 1) * (self.q - 1)

    def find_primes(self):
        self.p = RSA.random_prime()
        self.q = RSA.random_prime()

    def find_keys(self):
        for e in range(3, self.phin, 2):
            if gcd(e, self.phin) == 1 and 1 < e < self.phin:
                self.e = e
                break

        _, self.d, _ = RSA.gcde(self.e, self.phin)

        while not 1 < self.d < self.phin:
            self.d += self.phin

    def encrypt(self, string):
        def str_to_int(m):
            return int("".join([str(ord(x) - 64) for x in m]))

        m = str_to_int(string)
        print(m)

        if m < self.n:
            return pow(m, self.e, self.n)
        else:
            raise ValueError("String too long for encryption (m >= n)")

    def decrypt(self, ciphertext):
        def int_to_str(c):
            cstr = str(c)
            return "".join([chr(int(cstr[i:i + 2]) + 64) for i in range(0, len(cstr), 2)])

        clear = pow(ciphertext, self.d, self.n)
        return int_to_str(clear)

    @staticmethod
    def random_prime():
        while True:
            p = randint(10000000, 100000000)

            if RSA.miller_rabin_test(p, 3):
                return p

    @staticmethod
    def gcde(a, b):
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    @staticmethod
    def miller_rabin_test(n, k=7):
        """use Rabin-Miller algorithm to return True (n is probably prime)
           or False (n is definitely composite)"""
        if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
            return [False, False, True, True, False, True][n]
        elif n & 1 == 0:  # should be faster than n % 2
            return False
        else:
            s, d = 0, n - 1
            while d & 1 == 0:
                s, d = s + 1, d >> 1
            # Use random.randint(2, n-2) for very large numbers
            for a in sample(range(2, min(n - 2, float("inf"))), min(n - 4, k)):
                x = pow(a, d, n)
                if x != 1 and x + 1 != n:
                    for r in range(1, s):
                        x = pow(x, 2, n)
                        if x == 1:
                            return False  # composite for sure
                        elif x == n - 1:
                            a = 0  # so we know loop didn't continue to end
                            break  # could be strong liar, try another a
                    if a:
                        return False  # composite if we reached end of this loop
            return True  # probably prime if reached end of outer loop


def main():
    for _ in range(30):
        rsa = RSA()

        clear = 'teszt'
        ciphertext = rsa.encrypt(clear)
        decrypted = rsa.decrypt(ciphertext)

        print("clear: {}, ciphertext: {}, decrypted: {}".format(clear, ciphertext, decrypted))


if __name__ == '__main__':
    main()
