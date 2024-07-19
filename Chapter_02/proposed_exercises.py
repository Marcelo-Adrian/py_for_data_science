from collections import Counter

def exp_01():
    test = [1, 2, 3, 4, 5]
    print(f'Second elment = {test[1]}')
    print(f'Complete list = {test}')

def exp_02():
    test = [1, 2, 3, 4, 5]
    test2 = [6, 7, 8, 9, 10]
    test.extend(test2)
    print(f'Complete list = {test}')

def exp_03():
    prime = {2, 3, 5, 7, 11, 13, 17, 19}
    even = {0, 2, 4, 8, 10}
    odd = {11, 13, 15, 17, 19}
    print(f'Even union (prime intersection odd) = {even.union(prime.intersection(odd))}')

def exp_04():
    dna = "CGCGGACCTTTCCCAAA"
    print(Counter(dna))

def main():
    exp_01()
    exp_02()
    exp_03()
    exp_04()

if __name__ == "__main__":
    main()