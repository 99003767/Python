import re
count = 0
software = []
license = []
lines = 0

inp=int(input("Enter number\n1.software\n2.License"))

if(inp==1):
  pattern = re.compile("Software",re.I)
  with open ('input.txt','rt') as file_info:
      for file_line in file_info:
        lines +=1
        if pattern.search(file_line) != None:
            software.append((lines,file_line.rstrip('\n')))
      for answer in software:
        count +=1
        with open("software.txt",'a') as file_answer:
            file_answer.writelines(str(count)+' :')
            file_answer.writelines(answer[1]+'\n')

     

if(inp==2):
  pattern = re.compile("license",re.I)
  with open ('input.txt','rt') as file_info:
      for file_line in file_info:
        lines +=1
        if pattern.search(file_line) != None:
            license.append((lines,file_line.rstrip('\n')))
      for answer in license:
        count +=1
        with open("license.txt",'a') as file_answer:
            file_answer.writelines(str(count)+' :')
            file_answer.writelines(answer[1]+'\n')   


    

                          

