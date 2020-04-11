# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:20:11 2019
"""

if __name__ == "__main__":  
#    run_colorsExample()
    import pandas as pd
    import networkx as nx
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import MinMaxScaler
    import os, sys
    
#    pos = [[9.5, 7.794228634059948],  [0, 5.196152422706632],  [9.5, 2.598076211353316],  [9, 5.196152422706632],  [6.5, 2.598076211353316],  [4.5, 7.794228634059948],  [0, 3.4641016151377553],  [9, 0.0],  [2, 6.9282032302755105],  [5.5, 7.794228634059948],  [5, 0.0],  [4, 5.196152422706632],  [0, 6.9282032302755105],  [1, 1.7320508075688776],  [0, 6.9282032302755105]]
    pos = [[0.5, 7.794228634059948], [9, 6.9282032302755105], [3, 0.0], [5.5, 0.8660254037844388], [0, 5.196152422706632], [5, 5.196152422706632], [9, 5.196152422706632], [0.5, 2.598076211353316], [7.5, 7.794228634059948], [4.5, 7.794228634059948], [0, 0.0], [9, 0.0], [9.5, 7.794228634059948], [9.5, 2.598076211353316]]
#    gene_list_top20 =['SPOP', 'TP53',  'FOXA1',  'CTNNB1',  'MED12',  'C16orf62',  'CLPTM1L',  'DPYSL2',  'NEIL1',  'SLC27A4',  'PITPNM2',  'PTEN', 'ATM',  'EMG1',  'ETV3',  'BRAF',  'NKX3-1',  'ZMYM3',  'OR4P4',  'SALL1']
    gene_list_top14 = ['RUNX1', 'PIK3CA', 'GATA3', 'FOXA1', 'SF3B1', 'PTEN', 'CBFB', 'CDH1', 'MAP2K4', 'MAP3K1', 'ERBB2', 'NCOR1', 'FAM86B2', 'CDKN1B']  
    gene_list = gene_list_top14
#    features_selected_withprefix_GE = ['GE_' + feature for feature in gene_list]
#    features_selected_withprefix_DM = ['DM_' + feature for feature in gene_list]
#    features_selected_withprefix_CN = ['CNA_' + feature for feature in gene_list] 
#    column_list = ['']
#    column_list = column_list.append(pd.Index(features_selected_withprefix_GE))
#    column_list = column_list.append(pd.Index(features_selected_withprefix_DM))
#    column_list = column_list.append(pd.Index(features_selected_withprefix_CN))
    
    pathGE = "C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\Mergefile_top20_norm.csv"
    # Read file 
    df = pd.read_csv(pathGE)
    
    df1 = df.loc[df['TUMOR_STAGE'] == 'Stage IIIA']
#    labels = df1['TUMOR_STAGE'].values
#    
    df2 = df.loc[df['TUMOR_STAGE'] == 'Stage IIA']
#    labels2 = df2['TUMOR_STAGE'].values
#    
    df3 = df.loc[df['TUMOR_STAGE'] == 'Stage IIB']
#    labels3 = df3['TUMOR_STAGE'].values
    
    df1.drop(['TUMOR_STAGE','PATIENT_ID'],axis =1,inplace = True)
    df2.drop(['TUMOR_STAGE','PATIENT_ID'],axis =1,inplace = True)
    df3.drop(['TUMOR_STAGE','PATIENT_ID'],axis =1,inplace = True)
    
    # applying scaling to make values between some range 0-1/-1-2 ,as need for Kohens SOM
    scaler = MinMaxScaler(copy=True, feature_range=(0, 1))    
    df1 = pd.DataFrame(scaler.fit_transform(df1), columns=df1.columns)
    df2 = pd.DataFrame(scaler.fit_transform(df2), columns=df2.columns)
    df3 = pd.DataFrame(scaler.fit_transform(df3), columns=df3.columns)
        
    col_num = 14
    #Create node list of numbers then create lables and dict
    node_list = [i for i in range(col_num)]
    new_lbl = [str(j) for j in range(col_num)]
    new_lbl_dict = dict(enumerate(new_lbl))
    
    # loop through all rows and get RGB values for each patient  ----- 3A
    row_count = df1.shape[0]
    
    for i in range(row_count): #loop through all rows 
        nodecolor =[] 
        for j in range(len(gene_list)): # loop through all nodes (i.e 14 nodes)
            
            r_prefix = 'GE_'+gene_list[j]
            g_prefix = 'DM_'+gene_list[j]
            b_prefix = 'CNA_'+gene_list[j]
            
            #Check if tht column exixts 

            R =  round(df1[r_prefix][i],5) if (r_prefix in df1.columns) else 0.0
            G =  round(df1[g_prefix][i],5) if (g_prefix in df1.columns) else 0.0
            B =  round(df1[b_prefix][i],5) if (b_prefix in df1.columns) else 0.0

            nodecolor.append([R,G,B])
            
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
            path = "./training/3A"
            plt.savefig(os.path.join(path,filename))#, bbox_inches='tight', dpi=72)
        except:
            print("row = ",i," node_color = ",nodecolor)
        
        print(("\r Preparing Images... "+str(int(i*100.0/row_count))+"%" ), end=' ')
    print("Done ---- 3A!!")
# loop through all rows and get RGB values for each patient  ----- 2A
    row_count = df2.shape[0]
    
    for i in range(row_count): #loop through all rows 
        nodecolor =[] 
        for j in range(len(gene_list)): # loop through all nodes (i.e 14 nodes)
            
            r_prefix = 'GE_'+gene_list[j]
            g_prefix = 'DM_'+gene_list[j]
            b_prefix = 'CNA_'+gene_list[j]
            
            #Check if tht column exixts 

            R =  round(df2[r_prefix][i],5) if (r_prefix in df2.columns) else 0.0
            G =  round(df2[g_prefix][i],5) if (g_prefix in df2.columns) else 0.0
            B =  round(df2[b_prefix][i],5) if (b_prefix in df2.columns) else 0.0

            nodecolor.append([R,G,B])
            
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
            path = "./training/2A"
            plt.savefig(os.path.join(path,filename))#, bbox_inches='tight', dpi=72)
        except:
            print("row = ",i," node_color = ",nodecolor)
        print(("\r Preparing Images... "+str(int(i*100.0/row_count))+"%" ), end=' ')
    print("Done ---- 2A!!")
# loop through all rows and get RGB values for each patient  ----- 2B
    row_count = df3.shape[0]
    
    for i in range(row_count): #loop through all rows 
        nodecolor =[] 
        for j in range(len(gene_list)): # loop through all nodes (i.e 14 nodes)
            
            r_prefix = 'GE_'+gene_list[j]
            g_prefix = 'DM_'+gene_list[j]
            b_prefix = 'CNA_'+gene_list[j]
            
            #Check if tht column exixts 

            R =  round(df3[r_prefix][i],5) if (r_prefix in df3.columns) else 0.0
            G =  round(df3[g_prefix][i],5) if (g_prefix in df3.columns) else 0.0
            B =  round(df3[b_prefix][i],5) if (b_prefix in df3.columns) else 0.0

            nodecolor.append([R,G,B])
            
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
            path = "./training/2B"
            plt.savefig(os.path.join(path,filename))#, bbox_inches='tight', dpi=72)
        except:
            print("row = ",i," node_color = ",nodecolor)
        print(("\r Preparing Images... "+str(int(i*100.0/row_count))+"%" ), end=' ')   
        
print("Done ---- whole!!")