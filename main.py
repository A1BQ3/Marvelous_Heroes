Superhero={'BBB':'Ironman', 'ABB':'Superman', 'BAB':'Spiderman', 'BBA':'Batman', 'AAA': 'Captain America', 'BAA':'Thor', 'ABA':'Hulk', 'AAB':'Hawkeye'}
print('What color would you choose?')
print('A.Red B.Blue')
var1=input()
print('What game would you play?')
print('A.Minecraft B.Fortnite')
var2=input()
print('What sport would you prefer?')
print('A.Tennis B.Basketball')
var3=input()
print('Do you want to know your superhero?[y/n]')
var4=input()
if var4=='n':
    print("Goodbye")
else:
    print(Superhero[var1+var2+var3])
