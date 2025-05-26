# assignment-4
# task 1

print("READING  FILE CONTENT")
file1=open("sample.txt","r")
file_r=file1.read()
print(file_r)
file1.close()

try:
    file1 = open("sample.txt", "r")
    file_r = file1.read()
    file1.close()
except FileNotFoundError:
    print("the file 'sample.txt' does not exist")

# task 2



