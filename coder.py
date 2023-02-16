import string

def generate_square(keyword):
    #square is a blank array. keyword+alaphabet. For each letter in that add it to square, don't duplicate. 
    #If keyword is lune would return luneabcdfghijkmopqrstvwxyz
    square = []
    for c in keyword + 'abcdefghijklmnopqrstuvwxyz':
        if c not in square:
            square.append(c)
    square = ''.join(square)
    return square

def decode_square(list_of_nums, square):
    plain = []
    for i in range(len(list_of_nums)):
        #Row and col takes the first and last number, so 45 has row=4 and column = 5
        col = int(list_of_nums[i][0])
        row = int(list_of_nums[i][1])
        #square is a string. So 11 if key is sigtora would return A. So row-1*5=0 + col(1)-1=0, so it all equals 0 
        # so it returns the first item in the square list which is S.
        letter = square[(row-1)*5 + col-1]
        #Appending the letter to a list. 
        plain.append(letter)
        output= (''.join(plain))
       
    return plain

 
# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(string, key):
    #If key is lune and there are 20 letters in the cipher it will return lunelunelunelunelune
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #print(key)
    #print(cipher_text)
    orig_text = []
    #if first leter in cipher is a, we wil have 0 + 12(L for Lune) + 26 = 38 % 26 = 12. So it would return L.
    for i in range(len(cipher_text)):
        current_letter =cipher_text[i].lower()
        #print(current_letter)
        #print(alpha.index(current_letter))
        #print(key[i])
        #print(alpha.index(key[i]))
        x=(alpha.index(current_letter) - alpha.index(key[i]) + 26) % 26
        #print(x)
        #print(alpha[x])
        
        """for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        print(x)
        #turns remainder into unicode so it can easily be turned into a character later with (ch)
        x += ord('A')
         """
        orig_text.append(alpha[x])
    return("" . join(orig_text))

#copies and pasted the pdf from the Introductory Primer To the Realm of Sigtoria into a text document. 
#Doing the really long way of ceaning it up and making it into a list of string.
#Going to go through each one and see which one returns the words Rian said were in the answer.
def open_string_text():
    with open('string_from_doc.txt', 'r') as file:
        data = file.read().replace('\n', ' ')
    import string
    #filtering to just letters of the alphabets, gets rid of symbols and numbers
    printable = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    data = ''.join(filter(lambda x: x in printable, data))
    result = data
    #lower case, and then using split to get rid of weird spaceing issues and to make a list
    result = result.lower()
    result_list = result.split()
    #removing duplicates
    final_result  = list(set(result_list))
    print(final_result)
    return(final_result)


#the code rian original gave us
initial_coder = ("""45 51 25 41 44 44 24 45 31 22 44 11 31 35 54 13 12 52 34 54 12 52 51 52 14 43 43 52 43 12 
                23 23 52 51 54 55 55 25 14 53 14 55 11 21 54 43 53 33 53 13 31 14 25 14 13 23 21 51 53 43 
                23 24 45 54 13 31 11 31 44 15 33 54 33 14 53 14 32 33 35 51 45 51 45 43 24 51 23 13 35 51
                35 25 52 34 53 45 11 52 33 35 22 54 13 24 45 22 43 11 43 53 14 35 53 53 54 12 54 11 53 43 23 14 25 24 15 12 32 25 23 35 44 12 31 31 22 31 43
                35 54 22 45 35 25 52 13 35 22 43 31 12 11 24 13 35 51 13 11 51 53 22 45 51 25 34 14 44 24 25 51 34 35 54 12 31 42 23 52 51 34 
                53 35 21 33 53 13 35 11 52 33 35 55 12 45 31 13 31 43 31 34 11 44 24 31 51 54 12 24 35 
                22 54 12 54 11 33 54 41 43 31 43 11 23 23 23 14 55 23 21 42 21 44 44 24 15 51 54 51 45 
                15 53 43 23 55 42 23 44 51 23 14 31 41 35 14 25 53 43 23 33 23 14 13 13 51 35""")


list_of_nums =initial_coder.split()
#Takes a keyword and creates a string, so abcde or sigtorabd. This is the order the string appears in the square.
list_of_keys = open_string_text()

for i in list_of_keys:
    #keyword = 'lune'
    keyword = i
    square = generate_square(keyword)
    coded_string = decode_square(list_of_nums, square)
    #coded_string = coded_string.lower()
    key = generateKey(coded_string, keyword)
    #coded_string=['L','V','P']
    decoded_string= originalText(coded_string,key)
    #print(decoded_string)
    if 'the' in decoded_string:
        if 'is' in decoded_string:
            if 'in' in decoded_string:
                print("")
                print("")
                print(keyword)
                print("Decoded String :", decoded_string)
                print("")
                print("")

