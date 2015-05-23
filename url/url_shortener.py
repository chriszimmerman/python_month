class URLShortener:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    alphabet_length = len(alphabet)

    def encode_url(self, rowId):
        reverse_alphabet_digits = self.__get_alphabet_digits_from_rowid(rowId)[::-1]
        url_characters = map(self.__get_url_character, reverse_alphabet_digits)

        return ''.join(url_characters)

    def __get_alphabet_digits_from_rowid(self, rowId):
        alphabet_digits = []

        while rowId > 0:
            digit = rowId % self.alphabet_length
            alphabet_digits.append(digit)
            rowId = rowId // self.alphabet_length

        return alphabet_digits

    def __get_url_character(self, digit):
        return self.alphabet[digit]

    def decode_url(self, url):
        alphabet_digits = self.__get_alphabet_digits_from_url(url)
        digits_by_power = self.__convert_alphabet_digits_to_decimal(alphabet_digits) 
        return sum(digits_by_power) 

    def __get_alphabet_digits_from_url(self, url):
        return list(map(lambda char: self.alphabet.index(char), url))

    def __convert_alphabet_digits_to_decimal(self, digits):
        reverse_digits = digits[::-1]
        digits_by_power = [] 

        for digit in reverse_digits:
            digits_by_power.append(self.__to_decimal(digit, reverse_digits))

        return digits_by_power 

    def __to_decimal(self, digit, digits):
        return digit * self.alphabet_length ** digits.index(digit)

#create database - DONE
#take url and save in db
#get row id and convert id to string - DONE
#this string is the url shared
#when string is used as input, perform inverse function from string to row id - DONE
#get that row from the database
