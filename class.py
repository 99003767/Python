'''
Miniproject for python
Author:Darpan Patil
PS no: 99003767
email: darpan.patil@ltts.com
date:25-02-2020
'''
import re                                                #importing regular expressions package


class Mini_project:                                      #declaring class

    def __init__(self, keyword, file):                    #initializing variables
        self.keyword = keyword
        self.file = file

    def keyword_find(self,):                             #Function to search 

        count = 0                                          #variable to keep the count
        match = re.findall(self.keyword, self.file, re.M | re.I)        #line used to find word
        extension = ".txt"                                              
        file_name = str(self.keyword)+extension                      #line to save the file
        file_creation = open(file_name, "w+")                          # open the file in write mode
        file_creation.write("The number of occurrences of keyword is:" + str(len(match)))       #line which prints the count
        file_creation.write(str("\n\n"))                                  #for next line
        split_file_text = self.file.split()                               #for splitting the lines
        f = open(file_name, "a+")                                         #opening file in append mode
        for iteration in range(len(split_file_text)):                     #for loop for appending       
            matching = re.match(self.keyword, split_file_text[iteration], re.M | re.I)
            if matching:
                count += 1
                y = (split_file_text[iteration-1]+" "+split_file_text[iteration]+" "+split_file_text[iteration+1]+"\n")  #finding the previous and next word
                f.writelines(str(y))                                       #writing those lines to file


if __name__ == '__main__':

    with open('input.txt') as input_file:                               #opening the input file
        read_file = input_file.read()                                   #reading the file   
        print(read_file)
    for x in range(5):                                                  #loop for searching the words
        keywordd = input("Enter the keyword you wanted to search in file:")       #user giving the input for the word to search
        d = Mini_project(keywordd, read_file)                                    #passing the parameters to function
        d.keyword_find()