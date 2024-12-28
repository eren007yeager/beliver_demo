#projects of python
#matlibs game
#word game where you create an story
#by filling in blanks with random word
adjective1 = input("enter an adjective (description):")
noun1 =  input("enter an noun (name,place thing)")
verb1 = input("enter an verb ending with ing")
adjective2 = input("enter an adjective (description):")
adjective3 = input("enter an adjective (description):")

print(f"today i went to a {adjective1} zoo")
print(f"in a exhibit i saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"i was {adjective3}!")

#weight convertor 
weight = float(input("enter your weight"))
unit=input("kilograms or pounds (k or L):")
if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
elif unit =="L":
    weight=weight / 2.205  
    unit = "kgs" 
else :
    print(f"{unit} is not valid")
print(f"your weight is {weight} in {unit}:")    

#python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("enter the value of principle:"))
    if principle <= 0:
        print("principle can't be less than or equal to zero : ")
        
while rate <= 0:
    rate = float(input("enter the value of rate of interest:"))
    if rate <= 0:
        print("rate of interest can't be less than or equal to zero : ")
        
while time <= 0:
    time = float(input("enter the value of time:"))
    if time <= 0:
        print("time can't be less than or equal to zero : ")

total_balance = principle * pow((1 + rate/100),time)
print(f"balance after {time} year/s: ${total_balance}:.2f")

 
#python quiz games
questions = ("how many elements are in an periodic table?:",
            "which animal lays the largest eggs?:",
            "which is the deepest point in the world?:",
            "how many bones are in human body?:"
            "which planet in the solar system is the hottest?")
Options =(("A.116","B.117","C.118","D.119"),
          ("A.whale","B.crocodile","C.elephant","D.ostrich"),
          ("A.mariana trench","B.venus","C.india","D.yataro"),
          ("A.206","B.287","C.298","D.289"),
          ("A.mercury","B.venus","C.earth","D.mars"))
answers =("C","D","A","A","B")
guesses =[]
score = 0
questions_num = 0  

for question in questions:
    print("----------------------")
    print(question)
for option in Options:
    print(option)
    guess = input("enter(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print("correct!")
    else:
        print("incorrect")
        print(f"{answers[quctions_num]} is the correct answers")
    questions_num += 1        
       
                   
            