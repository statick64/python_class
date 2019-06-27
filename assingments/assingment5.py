import re
word = ("Floor Division The division of operands where the result is the quotient in which the digits after the decimal point are removed But if one of the operands is negative the result is floored ie rounded away from zero towards negative infinity")
words = word.split()
pe = sorted(words, key = len,reverse = False)
pom = sorted(words, key = len,reverse = True)
for i,j in zip(pe,pom):
        print(i,j)
word = ("Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)−")
pattern = '\W'
test_string = re.split(pattern,word)
test_string_set = set(test_string)
test_string_set.remove('')
test_string_list = list(test_string_set)
pe = sorted(test_string_list, key = len,reverse = False)
pom = sorted(test_string_list, key = len,reverse = True)
for i,j in zip(pe,pom):
        print(i,j)

