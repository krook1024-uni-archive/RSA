from random import randint


class MR:
    @staticmethod
    def test(n, k=3):
        """
        Megvizsgál egy számot összetettsége szempontjából.

        :param n a szám
        :param k a tesztek száma
        :return True, ha lehetséges, hogy n prím, False ha n biztosan összetett
        """
        if n < 6:  # 0-tól nagyobb és 6-nál kisebb esetekre egy shortcut
            return [False, False, True, True, False, True][n]
        elif n % 2 == 0:  # n páros
            return False
        else:
            s, d = 0, n - 1

            # n - 1 = 2 ^ s * d
            while d & 1 == 0:
                s += 1
                d >>= 1

            # k-szor választunk tetszőleges a-t, a < n
            for a in [randint(2, n - 2) for _ in range(k)]:
                x = pow(a, d, n)
                if x != 1 and x + 1 != n:
                    for r in range(s):  # 0 -> s-1
                        x = pow(x, 2, n)

                        if x == 1:
                            return False  # biztosan összetett
                        elif x == n - 1:
                            a = 0
                            break
                    if a != 0:
                        return False  # ha idáig eljut, összetett
            return True
