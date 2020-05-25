from math import gcd
from random import randint
from Math import Math
from MR import MR

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
        """
        Beállít egy-egy prímszámot p és q értékének a példányon belül.
        :return:
        """
        self.p = RSA.random_prime()
        self.q = RSA.random_prime()

    def find_keys(self):
        """
        Megkeresi a privát és nyílt kulcsokat.
        :return:
        """
        for e in range(3, self.phin, 2):
            if gcd(e, self.phin) == 1 and 1 < e < self.phin:
                self.e = e
                break

        _, self.d, _ = Math.gcde(self.e, self.phin)

        while not 1 < self.d < self.phin:
            self.d += self.phin

    def encrypt(self, string):
        """
        Titkosítja a stringet a példányváltozók segítségével.
        :param string: a titkos üzenet
        :return:
        """
        def str_to_int(m):
            return int("".join([str(ord(x) - 64) for x in m]))

        m = str_to_int(string)

        if m < self.n:
            return pow(m, self.e, self.n)
        else:
            raise ValueError("String too long for encryption (m >= n)")

    def decrypt(self, ciphertext):
        """
        Visszafejti a ciphertextet a példányváltozók segítségével
        :param ciphertext: a titkosított üzenet
        :return: a tiszta üzenet
        """
        def int_to_str(c):
            cstr = str(c)
            return "".join([chr(int(cstr[i:i + 2]) + 64) for i in range(0, len(cstr), 2)])

        clear = pow(ciphertext, self.d, self.n)
        return int_to_str(clear)

    @staticmethod
    def random_prime():
        """
        Véletlenszerűen választ egy prímet.
        :return: egy prímszám
        """
        while True:
            p = randint(10000000, 100000000)

            if MR.test(p):
                return p

def main():
    for _ in range(30):
        rsa = RSA()
        print(rsa)

        clear = 'teszt'
        ciphertext = rsa.encrypt(clear)
        decrypted = rsa.decrypt(ciphertext)

        print("clear: {}, ciphertext: {}, decrypted: {}".format(clear, ciphertext, decrypted))


if __name__ == '__main__':
    main()
