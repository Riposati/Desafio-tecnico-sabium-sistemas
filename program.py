import collections
import string

def count_letters(text):
      cont = 0
      result = dict.fromkeys(string.ascii_lowercase, 0)
      #print(result)
      # Go through each letter in the text
      for letter in text:
        # Check if the letter needs to be counted or not
        if letter not in result and letter.isalpha():
          result[letter.lower()] = 1
          cont+=1
        # Add or increment the value in the dictionary
        else:
            if letter.isalpha():
                cont+=1
                result[letter.lower()] += 1

      for key in result:
        result[key] = str(round(((result[key] / cont) * 100),2)) + "%"

      print("Resultado\nTotal de letras: {}".format(cont))
      
      return collections.OrderedDict(sorted(result.items()))

arrV = []

file_input = input('Informe o nome do txt: ')
with open(file_input, 'r') as info:
    arrV.append(info.read().lower())

arrResp = count_letters(''.join(arrV))

print("Percentuais:")
for key in arrResp:
    print('"{}" = {}'.format(key, arrResp[key])) 
