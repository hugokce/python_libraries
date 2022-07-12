Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello,World!")
Hello,World!
>>> 2+
SyntaxError: invalid syntax
>>> 2
2
>>> 2+2
4
>>> 21%7
0
>>> 21%8
5
>>> 2*2*2
8
>>> 2**3
8
>>> 2**5
32
>>> x = input("Enter the number: ")
Enter the number: 1
>>> x
'1'
>>> x = int(input("Enter the number: "))
Enter the number: 5
>>> x+10
15
>>> x*2
10
>>> pow(2,2)
4
>>> import math
>>> math.sqrt(81)
9.0
>>> math.factorial(5)
120
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/hey.py 
hey,there
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/hey.py 
hey,there
Enter name: Gautom
Hey Gautom
>>> print("The GCD of 60 and 48 is: ",math.gcd(60,48)
      )
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print("The GCD of 60 and 48 is: ",math.gcd(60,48)
NameError: name 'math' is not defined
>>> print(math.gcd(60,48))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(math.gcd(60,48))
NameError: name 'math' is not defined
>>> import math
>>> print(math.gcd(60,48))
12
>>> print("The GCD of 60 and 48 is :",math.gcd(60,48))
The GCD of 60 and 48 is : 12
>>> lcm = (60*48)/math.gcd(60,48)
>>> lcm
240.0
>>> 'he\'s a good person'
"he's a good person"
>>> a = "first name "
>>> b = "last name"
>>> a+b
'first name last name'
>>> a = 18
>>> "he is" +a
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    "he is" +a
TypeError: must be str, not int
>>> a = str(18)
>>> "he is "+a
'he is 18'
>>> animals = ["dog","cat","lion","tiger"]
>>> animals[2]
'lion'
>>> animals[-2]
'lion'
>>> example = [0,1,2,3,4,5,6,7,8,9]
>>> example[2:8]
[2, 3, 4, 5, 6, 7]
>>> example[-5:-1]
[5, 6, 7, 8]
>>> example[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> example[:5]
[0, 1, 2, 3, 4]
>>> example[5:]
[5, 6, 7, 8, 9]
>>> a = [0,1,2,3]
>>> b = [4,5,6,7]
>>> a+b
[0, 1, 2, 3, 4, 5, 6, 7]
>>> name = "gautam"
>>> 'k' in name
False
>>> 'g' in name
True
>>> numbers = [21,30,51,87,65,40]
>>> len(numbers)
6
>>> max(numbers)
87
>>> min(numbers)
21
>>> list("gautam")
['g', 'a', 'u', 't', 'a', 'm']
>>> numbers[2]=40
>>> numbers
[21, 30, 40, 87, 65, 40]
>>> example=list('simplebook')
>>> example
['s', 'i', 'm', 'p', 'l', 'e', 'b', 'o', 'o', 'k']
>>> len(example)
10
>>> example[6:] = list('mike')
>>> example
['s', 'i', 'm', 'p', 'l', 'e', 'm', 'i', 'k', 'e']
>>> example[6:] = list('baloon')
>>> example
['s', 'i', 'm', 'p', 'l', 'e', 'b', 'a', 'l', 'o', 'o', 'n']
>>> example[5:] = []
>>> example
['s', 'i', 'm', 'p', 'l']
>>> example = ['computer','random','keyboard']
>>> example.append('random')
>>> example
['computer', 'random', 'keyboard', 'random']
>>> numbers = [1,1,2,2,3,3,4,5]
>>> numbers = [1,1,2,2,3,3,3,4,5]
>>> numbers.count(1)
2
>>> numbers = example + numbers
>>> numbers
['computer', 'random', 'keyboard', 'random', 1, 1, 2, 2, 3, 3, 3, 4, 5]
>>> numbers.extend(example)
>>> numbers
['computer', 'random', 'keyboard', 'random', 1, 1, 2, 2, 3, 3, 3, 4, 5, 'computer', 'random', 'keyboard', 'random']
>>> string_main = list("helloworld")
>>> string_reverse=string_main[::-1]
>>> string_reverse
['d', 'l', 'r', 'o', 'w', 'o', 'l', 'l', 'e', 'h']
>>> list(string_reverse)
['d', 'l', 'r', 'o', 'w', 'o', 'l', 'l', 'e', 'h']
>>> str(string_reverse)
"['d', 'l', 'r', 'o', 'w', 'o', 'l', 'l', 'e', 'h']"
>>> string_main.reverse
<built-in method reverse of list object at 0x035B3E18>
>>> string_main.reverse()
>>> string_main.reverse(string_main)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    string_main.reverse(string_main)
TypeError: reverse() takes no arguments (1 given)
>>> string = "".join(reversed(string_main))
>>> string
'helloworld'
>>> string_main = "".join(reversed(string_main))
>>> string_main
'helloworld'
>>> string = "Example String"
>>> string.find(S)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    string.find(S)
NameError: name 'S' is not defined
>>> string.find("S")
8
>>> String = "helloworld"
>>> string = string[::-1]
>>> string = "helloworld"
>>> string = string[::-1]
>>> string
'dlrowolleh'
>>> string = input("Enter a long string \n") 
key = input("Enter the letter to search for: \n")
if(key in string):  #Checks if key is in the string
    print("Letter found in string") 
#If the Bool value is TRUE
else:
    print("Letter not found in string \n")
input("Press enter \n")

SyntaxError: multiple statements found while compiling a single statement
>>> string = input("Enter a long string \n")
Enter a long string 
"Example String"
>>> key = input("Enter the letter to search for: \n")
Enter the letter to search for: 
"S"
>>> string = input("Enter a long string \n") 
key = input("Enter the letter to search for: \n")
if(key in string):  #Checks if key is in the string
    print("Letter found in string") 
#If the Bool value is TRUE
else:
    print("Letter not found in string \n")
input("Press enter \n")
SyntaxError: multiple statements found while compiling a single statement
>>> if(key in string):  #Checks if key is in the string
    print("Letter found in string") 
#If the Bool value is TRUE
else:
    print("Letter not found in string \n")
input("Press enter \n")
SyntaxError: invalid syntax
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/simple.py 
Its true
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/nestedif.py 
Traceback (most recent call last):
  File "C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/nestedif.py", line 4, in <module>
    if item == "fruits":
NameError: name 'item' is not defined
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/nestedif.py 
This fruit is an apple
>>> a = 1
>>> a
1
>>> while a<=10:
	print(a)
	a = a+1

	
1
2
3
4
5
6
7
8
9
10
>>> example = ["book","pen","water","notebooks"]
>>> for item in example:
	print("I have "+ item)

	
I have book
I have pen
I have water
I have notebooks
>>> while True:
    text = input("Enter something: ")
    if(text=="quit"):break

    
Enter something: aa
Enter something: bb
Enter something: cc
Enter something: 11
Enter something: qq
Enter something: quit
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/functions.py 
I am a function
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/functions.py 
I am a function
7.5
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/functions.py 
I am a function
7.5
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/functions.py 
I am a function
7.5
7.800000000000001
15.0
>>> def printname(name):
	print(name)

	
>>> printname("Gautam")
Gautam
>>> def printname(*name):
	print(name)

	
>>> printname("gautam","tom","1")
('gautam', 'tom', '1')
>>> def printname(*name):
	print(name[0])

	
>>> printname("gautam","1",2,3)
gautam
>>> def printname(name,age):
	print(name)
	print(age)

	
>>> printname("gautam",22)
gautam
22
>>> calc = calculator()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    calc = calculator()
NameError: name 'calculator' is not defined
>>> 
 RESTART: C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/class.py 
>>> calc = calculator()
>>> result = calc.add(5,2)
>>> print(result)
7
>>> result = calc.sub(5,2)
>>> result
3
>>> class class1:
	var1 = "i am class1"

	
>>> class class2:
	var2="i am class2"

	
>>> class class3(class1,class2):
	var3="i am class3"

	
>>> example = class3()
>>> example.var
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    example.var
AttributeError: 'class3' object has no attribute 'var'
>>> example.var1
'i am class1'
>>> example.var2
'i am class2'
>>> example.var3
'i am class3'
>>> file = open('C:\Users\Selma\Desktop\UDEMY_EGITIMLERI\Python_from_Beginner_to_Intermediate_in_30_min/test.txt','w')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> file = open('C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/test.txt','w')
>>> file.write("this is my first file")
21
>>> file.close()
>>> file = open('C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/test.txt','r')
>>> file.read(10)
'this is my'
>>> file.read()
' first file'
>>> file = open('C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/test.txt','r')
>>> file.read()
'this is my first file'
>>> file.readline()
''
>>> file.seek(0)
0
>>> file.readline()
'this is my first file'
>>> file.close()
>>> file = open('C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/test.txt','r')
>>> file.readline()
'this is my first file\n'
>>> file.seek(0)
0
>>> file.readlines()
['this is my first file\n', 'this is my second line\n', 'third line\n', 'fourth line\n']
>>> file.seek(0)
0
>>> listdata = file.readlines()
>>> listdata
['this is my first file\n', 'this is my second line\n', 'third line\n', 'fourth line\n']
>>> listdata[2] = "third line edited"
>>> file.close()
>>> file = open('C:/Users/Selma/Desktop/UDEMY_EGITIMLERI/Python_from_Beginner_to_Intermediate_in_30_min/test.txt','w')
>>> file.writelines(listdata)
>>> listdata[2]
'third line edited'
>>> file.close()
>>> 
