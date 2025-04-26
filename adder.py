mynums=[1,2,3,4,5] # list for testing
def adder(mylist):
  total=0 # Variable holding total value
  for i in mylist: # Loop through the list
    total+=i # Add the current element to the result
  print(total) # Display the total

adder(mynums) 
