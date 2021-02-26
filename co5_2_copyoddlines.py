 
fn = open ('text.txt', 'r')             # open a file in read mode

fn1 = open ('odd.txt', 'w')            # open other file in write mode

# read the content of the file line by line
content = fn. readlines ()
print ("content\n", content)   #print the content of 1st file

for i in range(0, len(content)):
    if ( i % 2 == 0 ):
        fn1.write(content[i])
    else:
        pass
fn1.close()
 
fn1 = open ('odd.txt', 'r') # open file in read mode
cont1 = fn1.read()  # read the content of the file
print("\n\n   odd lines \n\n",cont1) # print the content of the 2nd file
fn.close()
fn1.close()
