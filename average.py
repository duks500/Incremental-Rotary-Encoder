import math 

newTxtFile = open('time_interval.txt','r')
content = newTxtFile.read().splitlines()
# content_list_str = content.split(",")
# content_list_float = map(float, content_list_str)
newTxtFile.close()

for x in range(len(content)):
    content[x] = float(content[x]) 

# print("The original list is : " + str(content))  


def Average(lst): 
    return sum(lst) / len(lst) 

# average = Average(content)

# Average of Float Numbers 
# using loop + formula  
sum = 0
for ele in content: 
  sum += ele 
res = sum / len(content)

print("The mean of float list elements is : " + str(res))  
