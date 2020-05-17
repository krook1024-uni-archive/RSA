from RSA import RSA

if __name__ == '__main__':
    rsa = RSA()

    while True:
        inp = input("uzenet: ")

        choice = 999
        while not int(choice) in range(1, 2 + 1):
            print("1) visszafejtes")
            print("2) titkositas")
            choice = input()

        if int(choice) == 1:
            print(rsa.decrypt(int(inp)))
        else:
            print(rsa.encrypt(inp))
