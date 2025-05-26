# ASSIGNMENT 4
# TASK 1

print("READING  FILE CONTENT")
file1=open("sample.txt","r")
file_r=file1.read()
print(file_r)
file1.close()

try:
    file1 = open("sample.tx", "r")
    file_r = file1.read()
    file1.close()
except FileNotFoundError:
    print("the file 'sample.txt' does not exist")

#TASK 2

n=input("enter the text to write to the file :")
file1=open("output.txt","w")
file1.write(n)
file1.close()

m=input("Enter the additional text to Append: ")
file2=open("output.txt","a")
file2.write(m)
file2.close()

print("The final output of file output.txt is")
print(n)
print(m)

