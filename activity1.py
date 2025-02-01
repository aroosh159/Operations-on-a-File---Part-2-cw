with open('codingaltext.txt','w') as file:
 file.write("Hello my name is Aroosh and i am  13 years old")
 file.close()
with open('codingaltext.txt','r') as file:
  data = file.readlines()
  for line in data:
    word = line.split()
    print(word)
file.close()