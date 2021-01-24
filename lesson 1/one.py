message = """
hi!
"""
print(message)
#start a vairiable
#starts from 1
e=1
#set the vairiable to score the sum 
#set to startfrom 0
total=0
#set while loop through each number
upto= int( input ("what is the number up to:"))
while e <= upto:
  #check if e is an even or odd number
  if e % 2 == 0: 
    #total += e
    total =total+e  
    e=e+1
  else:
    # e is an odd number
    e = e + 1
print (total) 
