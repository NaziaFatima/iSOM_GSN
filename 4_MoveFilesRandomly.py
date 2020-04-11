# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 04:46:46 2019

"""

import shutil
import os
import random
def Movefiles(source,destination,num):
    #source = 'C:\\PR_Proj_Thesis\\BRCA\\brca_tcga_pub_2015\\training\\2A'
    #destination = 'C:\\PR_Proj_Thesis\\BRCA\\brca_tcga_pub_2015\\test\\2A'
    # get list of files from Source(training) folder 
    list_of_file = [os.path.abspath(os.path.join(source,x)) for x in os.listdir(source)]#os.path.abspath(x)
    #Randomly select files and put it in test folder 
    for i in range(num):
        cut = random.choice(list_of_file)
        shutil.move(cut, destination)
        list_of_file = [os.path.abspath(os.path.join(source,x)) for x in os.listdir(source)]#os.path.abspath(x)
    print ('Done moving '+ str(num) +' files from source : ' ,source, ' to destination :',destination)

if __name__ == "__main__":  
    num = 30
    src_2A = 'C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\training\\2A'
    dst_2A = 'C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\test\\2A'

    src_2B = 'C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\training\\2B'
    dst_2B = 'C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\test\\2B'
    
    src_3A = 'C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\training\\3A'
    dst_3A = 'C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\test\\3A'
    
    Movefiles(src_2A,dst_2A,num)
    Movefiles(src_2B,dst_2B,num)
    Movefiles(src_3A,dst_3A,num)
    
    print('*****************************DONE*************************************')