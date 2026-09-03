name = 'Satya'
age = 28

#print
print("my name is", name, " I am ", age, " years old")

#formatted string print statement
print(f"My name is {name} and I am {age} years old")

#dot format string
print("my name is {} and I am {} years old".format(name,age))

# you want to know from which line the statment is coming and there is library 

#pip install loguru
#importing logger method from loguru
from loguru import logger

logger.info("my name is {} and I am {} years old".format(name,age))