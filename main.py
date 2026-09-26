questions = ("what is the state of matter of water:" , "what star is in our galaxy:" , "second letter in the alphabet:")
options = (("A : solid" , "B : gaz" , "C = liquid") , ("A = the sun" , "B = pluto" , "C = mars") , ("A = a" , "B = o" , "C = b" ))
start = input("press y to start or n to cancel :").lower()
answers = ["C" , "A" , "C"]
num = 0
score = 0
ijabet = []
if start == "y":
    for question in questions :
        print("_________________________________")
        print(question)
        for option in options[num]:
            print(option,end=" ")
            print()
            continue
        ijeba = input("pls answer : ").upper()
        ijabet.append(ijeba)
        if answers[num] == ijeba :
          print("correct")
          num += 1
          score += 1
        else :
          print("incorrect")
          num += 1
else :
    print("cancelled")

print("__________________________")
print("          result")
print("__________________________")
print("your answers are :")
for i in ijabet :
    print(i,end=" ")


print()
print("the correct answers are:")

for answer in answers :
    print(answer,end=" ")

print()

score = round(score / len(questions) *100 , 2 )
print(f"your percentage is:{int(score)}%")