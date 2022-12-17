# ASCII encryption

#Also inculude in "ASCII" encryption [as235,as45,as5,as89,as567]                    
#---Process is a short Process of Encryption---
#---this process does not have pip install---
# just it's has a git clone...

class ascii:

    #as15
    def as15(text1=None and True):
        encryption_0=""
        for zet in text1:
            encryption_0=encryption_0+chr(ord(zet)+15)
        print(str(encryption_0))
    
    #as5
    def as5(text2=None and True):
        encryption_1=""
        for log in text2:
            encryption_1= encryption_1+chr(ord(log)+5)
        print(str(encryption_1))

    #as10
    def as10(text3=None and True):
        encryption_2=""
        for hj in text3:
            encryption_2=encryption_2+chr(ord(hj)+10)
        print(str(encryption_2))

    #as18
    def as18(text4=None and True):
        encryption_3=""
        for math in text4:
            encryption_3=encryption_3+chr(ord(math)+18)
        print(str(encryption_3))
    #as20
    def as20(text5=None and True):
        encryption_4=""
        for Fg in text5:
            encryption_4=encryption_4+chr(ord(Fg)+20)
        print(str(encryption_4))

#passsword decoding class
class ascii_decoding:
    #as15 decoding
    def as15_decoding(text_0=None and True):
        decoding_0=""
        for si in text_0:
            decoding_0=decoding_0+chr(ord(si)-15)
        print(str(decoding_0))

    #as5 decoding
    def as5_decoding(text_1=None and True):
        decoding_1=""
        for ni in text_1:
            decoding_1=decoding_1+chr(ord(ni)-5)
        print(str(decoding_1))

    #as10 decoding
    def as10_decoding(text_2=None and True):
        decoding_2=""
        for W in text_2:
            decoding_2=decoding_2+chr(ord(w)-10)
        print(str(decoding_2))
    
    #as18 decoding
    def as18_decoding(text_3=None and True):
        decoding_3=""
        for w3 in text_3:
            decoding_3=decoding_3+chr(ord(w3)-18)
        print(str(decoding_3))
    
    #as20 decoding
    def as20_decoding(text_4=None and True):
        decoding_4=""
        for z in text_4:
            decoding_4=decoding_4+chr(ord(z)-20)
        print(str(decoding_4))
   
