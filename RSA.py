from random import randint, randrange


class RSA:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.fin = 0

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a = b
            b = a % b
        return a

    @staticmethod
    def miller_rabin_test(self, n, k):
        s = 0
        d = n - 1

        while d % 2 == 0:
            d >>= 1
            s += 1

        # 2^s * d = n-1
        assert (2 ** s * d == n - 1)

        for i in range(k):
            a = randrange(2, n)
            if self.is_composite(a, d, n):
                return False

        return True

    @staticmethod
    def is_composite(self, a, d, n):
        if pow(a, d, n) == 1:
            return False

        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
            return True

    def keygen(self):
        while (self.miller_rabin_test(self.p, 3) and self.miller_rabin_test(self.p, 3)):
            self.p = randint(10000, 1000000)
            self.q = randint(10000, 1000000)

        self.n = self.p * self.q
        self.fin = (self.p - 1) * (self.p - 2)
