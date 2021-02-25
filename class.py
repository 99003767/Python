import re


class SearchWord:

    def __init__(self, keyword_given, file_text):
        self.keyword_given = keyword_given
        self.file_text = file_text

    def keyword_search(self,):

        counting = 0
        match = re.findall(self.keyword_given, self.file_text, re.M | re.I)
        extension = ".txt"
        file_name = str(self.keyword_given)+extension
        file_creation = open(file_name, "w+")
        file_creation.write("The number of occurrences of keyword is:" + str(len(match)))
        file_creation.write(str("\n\n"))
        split_file_text = self.file_text.split()
        f = open(file_name, "a+")
        for iteration in range(len(split_file_text)):
            matching = re.match(self.keyword_given, split_file_text[iteration], re.M | re.I)
            if matching:
                counting += 1
                y = (split_file_text[iteration-1]+" "+split_file_text[iteration]+" "+split_file_text[iteration+1]+"\n")
                f.writelines(str(y))


if __name__ == '__main__':

    with open('input.txt') as input_file:
        read_file = input_file.read()
        print(read_file)
    for x in range(5):
        keyword = input("Enter the keyword you wanted to search in file:")
        d = SearchWord(keyword, read_file)
        d.keyword_search()