"""
Segédosztály matematikai feladatok elvégézésére.
"""
class Math:
    @staticmethod
    def gcde(a, b):
        """
        A kiterjesztett euklideszi algoritmus.
        :param a: az egyik szám
        :param b:  a másik szám
        :return: gcd(a, b), x, y
        """
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0
