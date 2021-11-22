#!/usr/bin/python3
import gmpy2

class RSA:
    def __init__(self) -> None:
        self.e = 65537

    def calculate_tot(self):
        tot = (self.p-1)*(self.q-1)
        return tot

    def str2number(self,message):
        s = 0
        multi = 1
        for i in range(len(message)-1, -1, -1):
            s += ord(message[i]) * multi
            multi *= 256
        return s

    def number2str(self,num):
        message = ""
        while num > 0:
            char = num % 256
            message = chr(char) + message
            num -= char
            num = int(num//256)
        return message

    def encode(self,plaintext):
        self.n = self.p * self.q
        self.m = self.str2number(plaintext)
        self.c = pow(self.m,self.e,self.n)
        return self.c

    def decode(self,c):
        self.tot = self.calculate_tot()
        self.d = pow(self.e, -1, self.tot)
        self.m = pow(c,self.d,self.n)
        self.message = self.number2str(self.m)
        return self.message

    def reverse_cube(self,n,c,e):
        gm = gmpy2.mpz(n)
        gs = gmpy2.mpz(c)
        ge = gmpy2.mpz(e)

        root, exact = gmpy2.iroot(gs, ge)
        print(self.number2str(root))

if __name__ == '__main__':
    rsa = RSA()
    '''
    encoding
    '''
    # rsa.p = 3
    # rsa.q = 7
    # rsa.encode('message')

    '''
    decoding
    '''
    # rsa.tot = rsa.calculate_tot()
    # rsa.decode(number)
    

    '''
    e = 3 attack
    '''
    n = 90853943628322295026593682475987617060873593704720419107522455730118510052263265463293746646770270649687914442326502298395536584315638883283598508714600968672217889495196802078585067900709511094279209391102167066735509213687150809291297894333497926049791571469926970525133534853823359619169977902549379766690271029677550623981924039537745336236460806578804468603462430628647190394537926168276717097453855467142322886378913606046349505735904238841871750986024415032881423400763965392179016644748395748894328459546597234450779143514757379951569086179358016591843479108891552906656123595991984678135372139
    c = 353690381812046953967046705467201123771968703796985157143856239677213620452330219172911759040152594421289421265846324253121362172623915294111963396504119782165935747889254103399163563246766329595499703665701197666661
    e = 3
    rsa.reverse_cube(n,c,e)


