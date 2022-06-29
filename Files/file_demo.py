"""
File I/O
'w' -> Write-only mode
'r' -> Read-only mode
'r+' -> Read and Write mode
'a' -> Append mode
"""

my_list = [1, 2, 3]
my_file = open("firstfile.txt", 'w')

for item in my_list:
    my_file.write(str(item) + "\t")

my_file.close()