import random

LOWER=[
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z'
]
UPPER=[
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
MARK=[
    '!', '#', '$', '*', ',', '-', '.', '/', '@', '^', '_', '|', '~'
]
NUMBERS=[
    '1','2','3','4','5','6','7','8','9','0'
]



def get_pass(pass_length):
    phrases=LOWER
    phrases.extend(UPPER)
    phrases.extend(NUMBERS)
    #phrases.extend(MARK)
    n=len(phrases)-1
    ret = ''
    for i in range(pass_length):
        ret += phrases[random.randint(0, n)]
    return ret



def main():
    N=int(raw_input())
    print(get_pass(N))

if __name__ == '__main__':
    main()
