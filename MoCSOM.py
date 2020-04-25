# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 02:15:56 2020

@author: Fatima
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:02:47 2019

@author: Fatima
"""
# One code file to do the following actions:
# Create template Map 
# Create RGB Images 
# Randomly distribute files
# Apply CNN 

import pandas as pd
import networkx as nx
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import os,random,shutil
import pathlib
count = 0

def createTemplate():
    import SimpSOM as sps
    path = pathlib.Path().absolute()
    path = str(path) + '\\GE_withstage_20.csv'
    #path = "C:\\PR_Proj_Thesis\\PRAD\\SOM_template\\GE_withstage_20.csv"
    # Read file 
    df = pd.read_csv(path)
    # Fill na 
    df.fillna(0,inplace = True)
    print("df shape = ", df.shape)
#    labels_old = df['TUMOR_STAGE'].values
    df.drop(['TUMOR_STAGE','PATIENT_ID'],axis =1,inplace = True)
    raw_data = df.values
    #Create transpose ; such that each column is one patient
    raw_data = raw_data.T
    # applying scaling to make values between some range 0-1/-1-2 ,as need for Kohens SOM
    scaler = MinMaxScaler(copy=True, feature_range=(0, 1))    
    scaler.fit(raw_data)    
    raw_data= scaler.transform(raw_data)
    
    ht = 10
    wd = 10
    no_of_epocs =1000
    
    net = sps.somNet(ht,wd, raw_data, PBC=False)
    net.colorEx=False
    
    Learning_rate = 0.05
    net.PCI = True #The weights will be initialised with PCA.
    """ Switch to activate periodic boundary conditions. """
    net.PBC = True
    net.train(Learning_rate,no_of_epocs)   
    col_num = raw_data.shape[0]
    
    node_list = [i for i in range(col_num)]
    new_lbl = [str(j) for j in range(col_num)]
    bmu = net.project(raw_data, labels=new_lbl)
    pos = bmu 
    G=nx.chvatal_graph() 
    nx.draw_networkx_nodes(G,pos,
                       nodelist=node_list,
                       node_color = 'w',
                       edgecolors = [0,0,0],
                       node_size=500,
                       alpha=0.8)

    new_lbl_dict = dict(enumerate(new_lbl))
    
    nx.draw_networkx_labels(G,pos,new_lbl_dict,font_size=10)
    
    plt.axis('on')
    plt.savefig(str(count)+'_Template.png')#, bbox_inches='tight', dpi=72)
#    plt.show()
    return pos;

def create_RGB_Images(pos,classlbl):
    gene_list_top14 = ['SPOP', 'FOXA1', 'CTNNB1', 'CLPTM1L', 'DPYSL2', 'NEIL1', 'PITPNM2', 'ATM', 'EMG1', 'ETV3', 'BRAF', 'NKX3-1', 'ZMYM3', 'SALL1'] 
    gene_list = gene_list_top14
    path = pathlib.Path().absolute()
    pathGE = str(path) + '\\Mergefile_top20.csv'
    # Read file 
    df = pd.read_csv(pathGE)
    df = df.loc[df['TUMOR_STAGE'] == classlbl]
    df.drop(['TUMOR_STAGE','PATIENT_ID'],axis =1,inplace = True)
    col_num = len(gene_list)#14
    #Create node list of numbers then create lables and dict
    node_list = [i for i in range(col_num)]
    new_lbl = [str(j) for j in range(col_num)]
    new_lbl_dict = dict(enumerate(new_lbl))
    # loop through all rows and get RGB values for each patient 
    row_count = df.shape[0]
    
    df.reset_index(inplace=True)
    for i in range(row_count): #loop through all rows 
        nodecolor =[] 
        for j in range(len(gene_list)): # loop through all nodes (i.e 14 nodes)
            
            r_prefix = 'GE_'+gene_list[j]
            g_prefix = 'DM_'+gene_list[j]
            b_prefix = 'CNA_'+gene_list[j]
            
            #Check if tht column exixts 
            
            R =  round(df[r_prefix][i],5) if (r_prefix in df.columns) else 0.0
            G =  round(df[g_prefix][i],5) if (g_prefix in df.columns) else 0.0
            B =  round(df[b_prefix][i],5) if (b_prefix in df.columns) else 0.0

            nodecolor.append([R,G,B])
            
#        print("node_color size = " ,len(nodecolor))
        G=nx.chvatal_graph()
        try:
            nx.draw_networkx_nodes(G,pos,
                               nodelist=node_list,
                               edgecolors = [0,0,0],
                               node_color = nodecolor,
                               node_size=500,
                               alpha=0.8)

            nx.draw_networkx_labels(G,pos,new_lbl_dict,font_size=10)
            
            plt.axis('on')
            filename = str(i)+'_Template.png'
            path = "./training/" +str(classlbl)
            plt.savefig(os.path.join(path,filename))
        except:
            print("row = ",i," node_color = ",nodecolor)
#        print(("\r Preparing Images... "+str(int(i*100.0/row_count))+"%" ), end=' ')
    print("\r Done Preparing Training Images ....for :",classlbl)
    return;
def Movefiles(source,destination,num):
    # get list of files from Source(training) folder 
    list_of_file = [os.path.abspath(os.path.join(source,x)) for x in os.listdir(source)]#os.path.abspath(x)
    #Randomly select files and put it in test folder 
    for i in range(num):
        cut = random.choice(list_of_file)
        shutil.move(cut, destination)
        list_of_file = [os.path.abspath(os.path.join(source,x)) for x in os.listdir(source)]#os.path.abspath(x)
    print ('Done moving '+ str(num) +' files from source : ' ,source, ' to destination :',destination)
    
def randomly_distribute_files(num):
#    num = 30
    import pathlib
    path = pathlib.Path().absolute()
    path = str(path)
    src_2A = path + '\\training\\34'
    dst_2A =  path + '\\test\\34'

    src_2B =  path + '\\training\\43'
    dst_2B =  path + '\\test\\43'
    
    src_3A =  path + '\\training\\45'
    dst_3A =  path + '\\test\\45'
    
    Movefiles(src_2A,dst_2A,num)
    Movefiles(src_2B,dst_2B,num)
    Movefiles(src_3A,dst_3A,num)
    
    print('****DONE Moving files****')
    return;
def apply_CNN():
    # Importing the Keras libraries and packages
    from keras.models import Sequential
    from keras.layers import Convolution2D,BatchNormalization,Dropout
    from keras.layers import MaxPooling2D
    from keras.layers import Flatten
    from keras.layers import Dense
    #Imports for collecting metrics
    import keras_metrics as km
    import tensorflow as tf
    #import tensorflow.keras as keras
    
    # Initialising the CNN
    classifier = Sequential()
    
    # Step 1 - Convolution
    classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))
    classifier.add(BatchNormalization())
    # Step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size = (2, 2),strides = (2,2)))
    classifier.add(Dropout(0.2))
    # Adding a second convolutional layer
    classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
    classifier.add(BatchNormalization())
    classifier.add(MaxPooling2D(pool_size = (2, 2),strides = (2,2)))
    classifier.add(Dropout(0.5))
    classifier.add(Flatten())
    # Step 4 - Full connection
    classifier.add(Dense(output_dim = 128, activation = 'relu'))
    classifier.add(BatchNormalization())
    classifier.add(Dropout(0.2))
    classifier.add(Dense(output_dim =3, activation = 'softmax')) # catgorical 
    # SET METRICS 
    precision = km.categorical_precision()
    recall = km.categorical_recall()
    f1= km.categorical_f1_score()
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy',precision,recall,f1])

    # Part 2 - Fitting the CNN to the images
    from keras.preprocessing.image import ImageDataGenerator
    train_datagen = ImageDataGenerator()
    test_datagen = ImageDataGenerator()
    seed =7
    training_set = train_datagen.flow_from_directory('training',
                                                     target_size = (64, 64),
                                                     batch_size = 32,
                                                     class_mode = 'categorical',
                                                     shuffle =True,
                                                     seed =seed)#,save_to_dir = 'generatedimages') #categorical,binary
    
    test_set = test_datagen.flow_from_directory('test',
                                                target_size = (64, 64),
                                                batch_size =32,
                                                class_mode = 'categorical',
                                                shuffle =True,
                                                seed =seed)#categorical,binary
    with tf.Session() as s:
        s.run(tf.global_variables_initializer())
        classifier.fit_generator(training_set,
                             samples_per_epoch = 250,
                             nb_epoch =35,
                             validation_data = test_set,
                             nb_val_samples = 90,
                             shuffle =True,
                             verbose = 2)
    return;

def delete_recreate_dirStructure():
    import pathlib
    path = pathlib.Path().absolute()
    path = str(path)
    src_C1 = path + '\\training\\34'
    dst_C1 =  path + '\\test\\34'

    src_C2 =  path + '\\training\\43'
    dst_C2 =  path + '\\test\\43'
    
    src_C3 =  path + '\\training\\45'
    dst_C3 =  path + '\\test\\45'
    
#    try:  
#        shutil.rmtree(src_C1)#Delete files n then folder recursively
#        shutil.rmtree(dst_C1)
#        shutil.rmtree(src_C2)
#        shutil.rmtree(dst_C2)
#        shutil.rmtree(src_C3)
#        shutil.rmtree(dst_C3)
        
#    except OSError:  
#       print ("Deletion of the directory failed")
    
    try:  
        os.makedirs(src_C1)
        os.makedirs(dst_C1)
        os.makedirs(src_C2)
        os.makedirs(dst_C2)
        os.makedirs(src_C3)
        os.makedirs(dst_C3)
        
    except OSError:  
        print ("Creation of the directory failed")
    return;        


if __name__ == "__main__":  
    delete_recreate_dirStructure()
    pos= [[4.5, 4.330127018922194], [9.5, 4.330127018922194], [9.5, 6.062177826491071], [6.5, 7.794228634059948], [0, 3.4641016151377553], [1.5, 7.794228634059948], [0, 6.9282032302755105], [0, 1.7320508075688776], [3, 6.9282032302755105], [0, 6.9282032302755105], [0.5, 7.794228634059948], [9, 0.0], [2.5, 2.598076211353316], [0, 6.9282032302755105]]
 #   print("POS = " , pos)
    create_RGB_Images(pos,34)
    create_RGB_Images(pos,43)
    create_RGB_Images(pos,45)
    randomly_distribute_files(30)
    apply_CNN()
    print("*****************Done!!*****************")
