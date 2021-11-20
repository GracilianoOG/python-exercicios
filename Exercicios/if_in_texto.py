# Números não são iteráveis, mas texto sim
num = '0'
nums = '1234506789'

if num in nums:
    print("Encontramos o ovo na posição {}".format(nums.index(num)))
else:
    print("Continue procurando!")
