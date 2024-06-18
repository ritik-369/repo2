#                                                                 JUDGE


import os,random
from unittest import TestCase

class data:
    file_checked=0
    
    input_file="io_files/input.txt"

    main_code_file="user_code/main_code.cpp"
    main_modified_code_file="user_code/main_code_modified.cpp"
    output_main_code="io_files/output_main_code.txt"

    brute_code_file="user_code/brute_code.cpp"
    brute_modified_code_file="user_code/brute_code_modified.cpp"
    output_brute_code="io_files/output_brute_code.txt"
 
    count=0

    def __init__(self):

        if self.file_checked==0:
            if not os.path.exists("io_files"):
                os.system("mkdir io_files")

            if not os.path.exists("user_code"):
                os.system("mkdir user_code")

            data.file_checked=1

class Engine:

    def __init__(self,type):

        self.type=type
        self.code=[]
        self.modified_code=[]
        self.files=data()
        self.input_file=self.files.input_file
        if self.type=="Main":
            self.code_file=self.files.main_code_file
            self.modified_code_file=self.files.main_modified_code_file
            self.output_file=self.files.output_main_code
        else:
            self.code_file=self.files.brute_code_file
            self.modified_code_file=self.files.brute_modified_code_file
            self.output_file=self.files.output_brute_code
        self.code_submit()
    
    def is_contain(self,line,part):
        line=line.split()
        part=part.split()
        line=[word for word in line if word != " "]
        part=[word for word in part if word != " "]
        ln=len(line)
        pr=len(part)
        cur=0
        for i in range(0,ln,1):
            if part[cur]==line[i]:
                cur+=1
            if cur==pr:
                return 1
        return 0
    
    def modify_code(self):
        new_code=[]
        ok =1
        found=0
        for line in self.code:
            if self.is_contain(line,"main()") and ok==1:
                found=1
                ok=0

            if self.is_contain(line,"{") and found==1:
                found=0
                new_code.append(line)
                new_code.append(f'''\n    freopen("{self.input_file}","r",stdin);''')
                new_code.append(f'''    freopen("{self.output_file}","w",stdout);\n''')
                continue
            new_code.append(line)
        return new_code
    
    def code_input(self):
        # os.system("cls")
        print(f"Write {self.type} Code Here ====>>>>")
        line=input()
        while(line!="ok"):
            self.code.append(line)
            line=input()
        self.modified_code=self.modify_code()
        # os.system("cls")
    def transfer_to_text(self):

        main_code=open(self.code_file,"w")
        modified_code=open(self.modified_code_file,"w")

        main_code.truncate(0)
        modified_code.truncate(0)

        main_code.write(f"//{self.type}\n")
    
        for line in self.code:
            line+="\n"
            main_code.write(line)

        for line in self.modified_code:
            line+="\n"
            modified_code.write(line)

        modified_code.close()
        main_code.close()

    def run_code(self):
        statement=f'''g++ {self.modified_code_file}'''
        os.system(statement)
        os.system("a.exe")
    
    def code_submit(self):
        self.code_input()
        self.transfer_to_text()
        self.run_code()

class generator:

    input_file=data.input_file
    testcase={}
    particular_testcase=""
    prints=0
    file_ptr=0
    file=0

    def __init__(self,testcase):
        file=open(self.input_file,"a")
        file.truncate(0)
        self.generate_testcases(testcase,prints=0,file_ptr=file)
        file.close()

    def number(self,start=0,end=1e9,ends="\n",prints=1,files=1):
        self.prints=prints
        self.file=files
        num=random.randint(start,end)
        if self.prints==1:
            print(num,end=ends)
        if self.file==1:
            self.file_ptr.write(str(num)+ends)
            net=str(num)+ends
            self.particular_testcase+=net
        return num

    def float_number(self,start=0,end=1e9,ends="\n",prints=1,files=1):
        self.prints=prints
        self.file=files
        num=random.randint(start,end)+random.random()
        if self.prints==1:
            print(num,end=ends)
        if self.file==1:
            self.file_ptr.write(str(num)+ends)
            net=str(num)+ends
        return num
    
    def small_character(self,start='a',end='z',ends="\n",prints=1,files=1):
        self.prints=prints
        self.file=files
        char=chr(ord('a')+random.randint(ord(start)-ord('a'),ord(end)-ord('a')))
        if self.prints==1:
            print(char,end=ends)
        if self.file==1:
            self.file_ptr.write(char+ends)
            net=char+ends
            self.particular_testcase+=net
        return char
    
    def capital_character(self,start='A',end='Z',ends="\n",prints=1,files=1):
        self.prints=prints
        self.file=files
        char=chr(ord('a')+random.randint(ord(start)-ord('a'),ord(end)-ord('a')))
        if self.prints==1:
            print(char,end=ends)
        if self.file==1:
            self.file_ptr.write(char+ends)
            net=char+ends
            self.particular_testcase+=net
        return char
    
    def mixed_character(self,start_small='a',end_small='z',start_cap='A',end_cap='Z',ends="\n",prints=1,files=1):
        char=[self.small_character(start_small,end_small,prints=0,files=0),self.capital_character(start_cap,end_cap,prints=0,files=0)]
        char=char[self.number(0,1,prints=0,file=0)]
        self.prints=prints
        self.file=files
        if self.prints==1:
            print(char,end=ends)
        if self.file==1:
            self.file_ptr.write(char+ends)
            net=char+ends
            self.particular_testcase+=net
        return char
    
    def vector(self,function,length,start=0,end=1e9,ex_start=-1,ex_end='Z',ends="\n",prints=1,files=1):
        vectors=[]
        for i in range(length):
            if ex_start==-1:
                vectors.append(function(start,end,prints=0,files=0))
            else:
                vectors.append(function(start,end,ex_start,ex_end,prints=0,files=0))

        self.prints=prints
        self.file=files
        if self.prints==1:
            for num in vectors:
                print(num,end=" ")
            print(ends)
        if self.file==1:
            for num in vectors:
                num=str(num)+" "
                self.file_ptr.write(num)
                net=num
                self.particular_testcase+=net
            self.file_ptr.write(ends)
        return vectors
    
    def string(self,function,length,start='a',end='z',ex_start=-1,ex_end='Z',ends="\n",prints=1,files=1):
        vector=self.vector(function,length,start,end,ex_start,ex_end,prints=0,files=0)
        self.prints=prints
        self.file=files
        string=""
        for token in vector:
            token=str(token)
            string+=token
        if self.prints==1:
            print(string,end=ends)
        if self.file==1:
            self.file_ptr.write(string+ends)
            net=string+ends
            self.particular_testcase+=net
        return string

    def special_function(self,function,length,start='a',end='z',ex_start=-1,ex_end='Z',ends="\n"):
        pass

    def generate_testcases(self,testcase,file=1,prints=1,file_ptr=0):

        self.prints=prints
        self.file_ptr=file_ptr
        self.file=file

        if self.prints==1:
            print(testcase)
        if self.file==1:
            self.file_ptr.write(str(testcase)+"\n")
        for test in range(testcase):
            self.particular_testcase=""
            # WRITE FROM HERE
            a=self.number(start=1,end=100,ends=" ",prints=0)
            b=self.number(start=1,end=100,ends="\n",prints=0)
            c=self.vector(self.number,length=a*b,start=1,end=100000,ends="\n",prints=0)
            
                
            #ENDS HERE
            self.testcase[test+1]=self.particular_testcase
        
        self.file_ptr.close()

class JUDGE:

    files=data()
    generator=""
    count=0
    testcases=0
    
    def process(self):

        self.generator=generator(self.testcases)
        main_code=Engine("Main")
        brute_code=Engine("Brute")
        main_output_file=self.files.output_main_code
        brute_output_file=self.files.output_brute_code
        main_data=[]
        brute_data=[]
        file=open(main_output_file,"r")
        for data in file:
            main_data.append(data)
        file.close()

        file=open(brute_output_file,"r")
        for data in file:
            brute_data.append(data)
        file.close()
        if len(brute_data)!=len(main_data):
            return 0
        self.count=1
        for (brute,main) in zip(brute_data,main_data):
            if brute != main:
                return 0
            self.count+=1
        return 1
    
    def __init__(self,testcases):
        self.testcases=testcases
        res=self.process()
        if res==1:
            print(''' 

             _______
            |  A C  |
            |_______|

            ''')
        else:
            print(''' 

             _______
            |  W A  |
            |_______|

            ''')
            print("At Testcase ",self.count)
            print("\n")
            print(self.generator.testcase[self.count])




JUDGE(100)

