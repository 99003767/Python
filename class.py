import re
count = 0
input_file = open("input.txt", 'r')
read_file = input_file.read()
main_file = read_file.split()
find_word = input("Enter the word to be search:")
word = re.findall(find_word, read_file, re.M | re.I)
print(len(word))
file_save = find_word+'.txt'

write_file = open(file_save, 'w+')
for x in range(len(main_file)):
    matching_done = re.match(find_word,  main_file[x], re.M | re.I)
    if matching_done:
        count += 1
        y = (main_file[x-1] + ' ' + main_file[x]+' '+main_file[x+1] + '\n')
        write_file.writelines(str(y))
write_file.writelines("the Total count of words :"+str(count))