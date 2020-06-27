
# print a text

text1 = """Spune-mi, daca te-as prinde-ntr-o zi
si ti-as saruta talpa piciorului,
nu-i asa ca ai schiopata putin, dupa aceea,
de teama sa nu-mi strivesti sarutul?"""

text2 = """Spune-mi,\n  daca te-as prinde-ntr-o zi
si ti-as saruta\n  talpa piciorului,
nu-i asa ca ai schiopata\n  putin, dupa aceea,
de teama sa nu-mi\n  strivesti sarutul?"""

print(text1)
print(text2)


nr_de_caractere1 = len(text1)
print(nr_de_caractere1)

nr_de_caractere2 = len(text2)
print(nr_de_caractere2)

print(text1[-152:-115])
print(text1[0:36])

print(text2[-160:-121])
print(text2[0:39])

join_text = " \n ".join([text1,text2])
print(join_text)



print(text1.replace("mi", "Hi", 1), "\n")

print(text1.replace("i", "o", 5), "\n")


print(text1 * 2, "\n")
print(text1.__mul__(2), "\n")

print(text1[::-1])

print(id(text2))


text3 = 'This text is' \
r' an example!'

print(text3 * 2)
print(text3 * 2)