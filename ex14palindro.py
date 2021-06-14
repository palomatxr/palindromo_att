def palindromo (palavra):
  for i in range(len(palavra) // 2 ) :
    if palavra[i] !=  palavra[len(palavra)-1-i] :
      return False

    return True


palavra = str(input("Ecreva uma palavra :")).strip().lower()


print(palindromo(palavra))
