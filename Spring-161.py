import os  


from time import time


import binascii


import math


import os.path





long_1=0


name=""


add_bits=""


Make_togher=""








name_input = input("c,  compress or e, extract? ")





#@Author Jurijus Pacalovas


class compression:


       


        def cryptograpy_compression4(self):


                


                self.name = "Written: Jurijus pacalovas"





                if name_input!="c" and name_input!="e":


                        print("The wrong letter")


                        raise SystemExit


                if name_input=="c" or name_input=="e":        


                    if name_input=="c":





                        i=1





                    if name_input=="e":


                        i=2


                 


                    Number_add_plus_one=""


                 


                    Clear=""


                  


                      


                    name = input("What is name of file?")


                   


                       


                 





                    if os.path.exists(name):


                            print('Path is exists!')


                    else:


                            print('Path is not exists!')


                            raise SystemExit





                    x=0


                    C1=1


                    x1=0


                    x2=0


                    x3=0


                    


                    X2=0


                    C1=0


                    C2=0


                    C3=0


                    C4=0


                    C5=0


                    


                    


                    n=0


                    x = time()


                    File_information6_Times2_1=0


                   


                   


                    


                            


                    


                   


                    


        


                    name_2=name


                    Long_Change=len(name_2)


                    


                    compress_or_not_compress=1


                    File_information6_Times3=0


                    


                  


                                            


                     


                                            	


                    


              


                    


                


                      


                            


     





                    if i==2:





                        


               


                         


                       


                        C=1








         


                           


                                


                        


                                            


                    


                        


                      





                    


                    	


                    Long_Change=len(name_2)


                    


                   


                    s=""





                    File_information5=""


                    File_information5_2=""





                  


                    Clear=""





                    Translate_info_Decimal=""





                    D=0


                    





                    


                    


                        





                    


                         


                    


                    





                    long_name=len(name)


                   


                    if i==2:
                        C=1




                            


                    with open(name, "rb") as binary_file:





                       # Read the whole file at once


                        data = binary_file.read()





                        


                     


                            


                         


      


                        s=str(data)





                        long_11=len(data)


                        long_17=len(data)


                        if long_17==0:


                        	 raise SystemExit


                        


                        END_working=0


                        File_information6_Times2=0


                                   


                        File_information5_23=""


 


                        INFO18=""


                        File_information5_29=""


                        


                        SpinS=0


                        while END_working<10:


                       


                            File_information6_Times3=File_information6_Times3+1


                            D=1


                            if D==1:


                                if File_information6_Times3==1:





                                 


                                    INFO=bin(int(binascii.hexlify(data),16))[2:]#data to binary


                                    long_1=len(INFO)


                                    long_11=len(data)


                                


                                    count_bits=(long_11*8)-long_1


                                    z=0


                                    if count_bits!=0:


                                        while z<count_bits:


                                            INFO="0"+INFO


                                            z=z+1


                                            


                                    





                                    if File_information6_Times3==1:


                                        File_information5_2=INFO


                            


                                    n = int(File_information5_2, 2)


                                


                                    width_bits=len(File_information5_2)


                                    width_bits=(width_bits/8)*2


                                    width_bits=str(width_bits)


                                    width_bits="%0"+width_bits+"x"


                             


                                    width_bits3=binascii.unhexlify(width_bits % n)                                    


                                    width_bits2=len(width_bits3)


                                    


                                    data=width_bits3


                                  


                                    long_15=len(data)





                                    INFO=bin(int(binascii.hexlify(data),16))[2:]


                                    long_1=len(INFO)





                                    long_11=len(data)


                                


                                    count_bits=(long_11*8)-long_1


                                    z=0


                                    if count_bits!=0:


                                        while z<count_bits:


                                            INFO="0"+INFO


                                            z=z+1





                                    File_information5_2=INFO


                                   


                                    


                                    


                                    Extact=File_information5_2


                                    A=int(Extact,2)


                                    





                                    long_13=len(File_information5_2)


                                long_12=len(File_information5_2)


                                #print(long_12)


                                if i==1:


                                    if long_17>=(2**26)-1 and i==1:


                                        print("print file is too big!")


                                        raise SystemExit





                                #########################################################################################################################################################


                                


                                


                                if i==1:
                                    
                                    
                                    
                                    long_file1=len(INFO)
                                    Times=0
                                    Count=-1
                                    Times_count=0
                                    while Times!=1:
                                        INFO=INFO[44:46]+INFO[0:44]+INFO[46:]
                                        long_file=len(INFO)
                                        Times_count+=1
                                        #print(long_file)
                                        if long_file<=8 or Times_count==(2**24)-1:
                                            Times=1
                                        Count+=1
                                        if Count==4:
                                            Count=0
                                        C=format(Count,'02b')
                                    
                                        if INFO[:2]==C:
                                            INFO="0"+INFO[2:]
                                        elif INFO[:2]=="00":
                                            INFO="10"+INFO[2:]
                                        else:
                                            INFO="11"+INFO[2:]
                                       
                                    Extract1=1                               
                                    if Extract1==1:
                                            
                                            
                                        File_information5_17=INFO
                                        
                                        long_1=len(File_information5_17)
                                        #print(long_1)
                                        add_bits=""
                                        count_bits=8-long_1%8
                                        z=0
                                        if count_bits!=0:


                                                                   if count_bits!=8:


                                                                       while z<count_bits:


                                                                               add_bits="0"+add_bits


                                                                               z=z+1





                                    long_file=len(INFO)
                                    C1=format(Times_count,'024b')
                                    File_information5_17=C1+add_bits+File_information5_17
                                    L=len(File_information5_17)
                                    #print(C1)
                                    #print(L)
                                    n=int(File_information5_17, 2)
                                    width_bits=len(File_information5_17)
                                    width_bits=(width_bits//8)
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                                    width_bits3=binascii.unhexlify(width_bits % n)
                                    width_bits2=len(width_bits3)
                                    #print(width_bits2)
                                    name_2+=".bin"
                                    with open(name_2, "wb") as f2:
                                        f2.write(width_bits3)
                                    x2 = time()
                                    x3=x2-x
                                    xs=float(x3)
                                    xs=str(xs)
                                    return xs;




   


d=compression()





xw1=d.cryptograpy_compression4()


print(xw1)
