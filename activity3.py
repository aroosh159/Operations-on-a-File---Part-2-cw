output = open('debugger.txt','w')
input = open('condingaltext.txt','r')
line_seem_so_far = set()
for line in input:
    if line not in line_seem_so_far:
        output.write(line)
        line_seem_so_far.add(line)

input.close()
output.close()