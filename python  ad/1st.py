#ques1=how do you concatenate two string in python.
str1="hello "
str2="world"
str=str1+str2
print(str)

#ques2=what is the diffrence between the + operator and the join() method concatenating string
str1="hellow"
str2="world"
print("".join([str1,str2]))

#ques3=how do you access individual character in a python.
str="hello world"
print(str[4])

#ques4=what method is used to find the length of a string in python

str="hellow world"
print(len(str))

#ques5=how do you convert a string to uppercase in python.

str="hello world"
print(str.upper())

#ques6=how do you convert a string to lowercase in python.

str="HELLO WORLD"
print(str.lower())


#ques7=what method is uesd to replace substring within a string.

str="java is a high level programming language.java is a multipurpose programing language"
print(str.replace("java","python"))

#ques8=how do you split a string into a list of substring based on a delimeter.

str="aq02403@gmail.com"
print(str.split("@"))

#ques9= how do you check if a string starts with a particular substring.

str="python is a high level programming language"
print(str.startswith("python"))

#ques10= how do you check if a string ends with a particular substring.

str="python is a high level programming language"
print(str.endswith("language"))

#ques11=how do you remove leading and trailing whitespace from a string.
str="    python    "
print(str.split())

#ques12=what method is used to fing the index of the first occurence of a substring within a string.

str="this is a laptop"
print(str.find("laptop"))

#ques13= how can you count the number of occurence of a substring with in a string.

str="python is a high level programming language.python is a interpreter language"
print(str.count("python"))

#ques14= how do you check if a string contains only alphabetic character.

str="PYTHON"
print(str.isalpha())

#ques15=how do you check if a string contains only numbers character.

str="76347647374673847"
print(str.isdigit())

#ques16= how can you check if a string is palindrome.

str="121"
reversed_str=str[::-1]
print(reversed_str)
if(str==reversed_str):
    print("this is a palindrome")
else:
    print("this is not a palindrome")

#ques17=how can you reverse a string in python

str="python"
reversed_str=str[::-1]
print(reversed_str)

#ques18=how do you format a string with placeholder for variable values.
name="Abdullah"
age=21
msg="my name is {} and i am {} year old".format(name,age)
print(msg)

#ques19=how do you access a substring os a string using slicing.
str="python is a high level programming language"
print(str[12:22:])

#ques20=how can you remove specific character from a string in python.

str="hello world"
print(str.replace("o",""))










