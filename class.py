import re


class Mini_project:

    def __init__(self, keyword, file):
        self.keyword = keyword
        self.file = file

    def keyword_find(self,):

        count = 0
        match = re.findall(self.keyword, self.file, re.M | re.I)
        extension = ".txt"
        file_name = str(self.keyword)+extension
        file_creation = open(file_name, "w+")
        file_creation.write("The number of occurrences of keyword is:" + str(len(match)))
        file_creation.write(str("\n\n"))
        split_file_text = self.file.split()
        f = open(file_name, "a+")
        for iteration in range(len(split_file_text)):
            matching = re.match(self.keyword, split_file_text[iteration], re.M | re.I)
            if matching:
                count += 1
                y = (split_file_text[iteration-1]+" "+split_file_text[iteration]+" "+split_file_text[iteration+1]+"\n")
                f.writelines(str(y))


if __name__ == '__main__':

    with open('input.txt') as input_file:
        read_file = input_file.read()
        print(read_file)
    for x in range(5):
        keywordd = input("Enter the keyword you wanted to search in file:")
        d = Mini_project(keywordd, read_file)
        d.keyword_find()