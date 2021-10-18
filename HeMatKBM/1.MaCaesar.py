#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Caesar():
    # key = 'aáàạảãăắằặẳẵâấầậẩẫbcdđeéẹẻẽêếềệểễfghiíìịỉĩjklmnoóòọỏõôốồộổỗơớờợởỡpqrstuúùụủũưứừựửữvwxyýỳỵỷỹAÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪBCDĐEÉẸẺẼÊẾỀỆỂỄFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠPQRSTUÚÙỤỦŨƯỨỪỰỬỮVWXYÝỲỴỶỸ0123456789`~!@#$%^&*()'
    key = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def encrypt(self, n, plaintext):
        """Encrypt the string and return the ciphertext"""
        result = ''

        for l in plaintext:
            try:
                i = (self.key.index(l) + n) % len(self.key)
                result += self.key[i]
            except ValueError:
                result += l
        return result


    def decrypt(self, n, ciphertext):
        """Decrypt the string and return the plaintext"""
        result = ''

        for l in ciphertext:
            try:
                i = (self.key.index(l) - n) % len(self.key)
                result += self.key[i]
            except ValueError:
                result += l

        return result


    def show_result(self, plaintext, n):
        """Generate a resulting cipher with elements shown"""
        encrypted = self.encrypt(n, plaintext)
        decrypted = self.decrypt(n, encrypted)

        print('Rotation: ', n)
        print('Plaintext: ', plaintext)
        print('Encrytped: ', encrypted)
        print('Decrytped: ', decrypted)

if __name__ == '__main__':
    caesar = Caesar()
    caesar.show_result("d15J1I N1J 1 GFC9K9391E 1E4 75E5I1C F6 K85 C1K5 sFD1E I5GL2C93, N8F 7I51KCP 5OK5E454 K85 sFD1E 5DG9I5 256FI5 J59Q9E7 GFN5I 1E4 D1B9E7 89DJ5C6 493K1KFI F6 sFD5, G1M9E7 K85 N1P 6FI K85 9DG5I91C JPJK5", 35)