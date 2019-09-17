# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 04:35:28 2019

@author: Fatima
"""

# get gene values from each file for following patient ID's
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
    
if __name__ == "__main__":

    patient_list =  ['TCGA-2A-A8VT', 'TCGA-2A-A8W1', 'TCGA-2A-A8W3', 'TCGA-2A-AAYF', 'TCGA-CH-5737', 'TCGA-CH-5739', 'TCGA-CH-5740', 'TCGA-CH-5741', 'TCGA-CH-5743', 'TCGA-CH-5744', 'TCGA-CH-5745', 'TCGA-CH-5746', 'TCGA-CH-5748', 'TCGA-CH-5750', 'TCGA-CH-5753', 'TCGA-CH-5754', 'TCGA-CH-5762', 'TCGA-CH-5763', 'TCGA-CH-5764', 'TCGA-CH-5765', 'TCGA-CH-5766', 'TCGA-CH-5767', 'TCGA-CH-5771', 'TCGA-CH-5772', 'TCGA-CH-5788', 'TCGA-CH-5789', 'TCGA-CH-5790', 'TCGA-CH-5791', 'TCGA-CH-5792', 'TCGA-CH-5794', 'TCGA-EJ-5494', 'TCGA-EJ-5496', 'TCGA-EJ-5497', 'TCGA-EJ-5498', 'TCGA-EJ-5499', 'TCGA-EJ-5501', 'TCGA-EJ-5502', 'TCGA-EJ-5504', 'TCGA-EJ-5505', 'TCGA-EJ-5507', 'TCGA-EJ-5508', 'TCGA-EJ-5509', 'TCGA-EJ-5510', 'TCGA-EJ-5511', 'TCGA-EJ-5512', 'TCGA-EJ-5514', 'TCGA-EJ-5515', 'TCGA-EJ-5516', 'TCGA-EJ-5518', 'TCGA-EJ-5521', 'TCGA-EJ-5522', 'TCGA-EJ-5524', 'TCGA-EJ-5525', 'TCGA-EJ-5527', 'TCGA-EJ-5530', 'TCGA-EJ-5531', 'TCGA-EJ-5532', 'TCGA-EJ-5542', 'TCGA-EJ-7115', 'TCGA-EJ-7123', 'TCGA-EJ-7125', 'TCGA-EJ-7218', 'TCGA-EJ-7312', 'TCGA-EJ-7314', 'TCGA-EJ-7315', 'TCGA-EJ-7317', 'TCGA-EJ-7318', 'TCGA-EJ-7325', 'TCGA-EJ-7327', 'TCGA-EJ-7328', 'TCGA-EJ-7330', 'TCGA-EJ-7331', 'TCGA-EJ-7781', 'TCGA-EJ-7783', 'TCGA-EJ-7784', 'TCGA-EJ-7785', 'TCGA-EJ-7786', 'TCGA-EJ-7788', 'TCGA-EJ-7789', 'TCGA-EJ-7791', 'TCGA-EJ-7792', 'TCGA-EJ-7793', 'TCGA-EJ-7794', 'TCGA-EJ-7797', 'TCGA-EJ-8469', 'TCGA-EJ-8470', 'TCGA-EJ-A46H', 'TCGA-EJ-A46I', 'TCGA-EJ-A65B', 'TCGA-EJ-A65E', 'TCGA-EJ-A65F', 'TCGA-EJ-A65J', 'TCGA-EJ-A6RC', 'TCGA-EJ-A7NF', 'TCGA-EJ-A7NG', 'TCGA-EJ-A7NH', 'TCGA-EJ-A7NK', 'TCGA-EJ-A7NM', 'TCGA-EJ-A7NN', 'TCGA-EJ-A8FN', 'TCGA-EJ-A8FO', 'TCGA-EJ-A8FS', 'TCGA-FC-7708', 'TCGA-FC-7961', 'TCGA-FC-A5OB', 'TCGA-FC-A66V', 'TCGA-FC-A6HD', 'TCGA-G9-6329', 'TCGA-G9-6332', 'TCGA-G9-6333', 'TCGA-G9-6336', 'TCGA-G9-6338', 'TCGA-G9-6339', 'TCGA-G9-6343', 'TCGA-G9-6348', 'TCGA-G9-6351', 'TCGA-G9-6353', 'TCGA-G9-6354', 'TCGA-G9-6356', 'TCGA-G9-6361', 'TCGA-G9-6362', 'TCGA-G9-6363', 'TCGA-G9-6364', 'TCGA-G9-6365', 'TCGA-G9-6366', 'TCGA-G9-6367', 'TCGA-G9-6369', 'TCGA-G9-6370', 'TCGA-G9-6373', 'TCGA-G9-6377', 'TCGA-G9-6378', 'TCGA-G9-6379', 'TCGA-G9-6384', 'TCGA-G9-6385', 'TCGA-G9-6494', 'TCGA-G9-6496', 'TCGA-G9-6498', 'TCGA-G9-6499', 'TCGA-G9-7519', 'TCGA-G9-7522', 'TCGA-G9-7525', 'TCGA-H9-7775', 'TCGA-H9-A6BY', 'TCGA-HC-7078', 'TCGA-HC-7079', 'TCGA-HC-7080', 'TCGA-HC-7081', 'TCGA-HC-7210', 'TCGA-HC-7211', 'TCGA-HC-7212', 'TCGA-HC-7213', 'TCGA-HC-7230', 'TCGA-HC-7231', 'TCGA-HC-7232', 'TCGA-HC-7233', 'TCGA-HC-7736', 'TCGA-HC-7737', 'TCGA-HC-7738', 'TCGA-HC-7740', 'TCGA-HC-7741', 'TCGA-HC-7742', 'TCGA-HC-7744', 'TCGA-HC-7745', 'TCGA-HC-7747', 'TCGA-HC-7749', 'TCGA-HC-7750', 'TCGA-HC-7752', 'TCGA-HC-7817', 'TCGA-HC-7818', 'TCGA-HC-7820', 'TCGA-HC-8212', 'TCGA-HC-8216', 'TCGA-HC-8256', 'TCGA-HC-8257', 'TCGA-HC-8260', 'TCGA-HC-8261', 'TCGA-HC-8264', 'TCGA-HC-A631', 'TCGA-HC-A632', 'TCGA-HC-A6AL', 'TCGA-HC-A6AN', 'TCGA-HC-A6AO', 'TCGA-HC-A6AP', 'TCGA-HC-A6AQ', 'TCGA-HC-A6AS', 'TCGA-HC-A6HX', 'TCGA-HC-A6HY', 'TCGA-HC-A76W', 'TCGA-HC-A76X', 'TCGA-HC-A8D0', 'TCGA-HC-A8D1', 'TCGA-HI-7168', 'TCGA-HI-7169', 'TCGA-J4-8198', 'TCGA-J4-8200', 'TCGA-J4-A67K', 'TCGA-J4-A67L', 'TCGA-J4-A67M', 'TCGA-J4-A67N', 'TCGA-J4-A67O', 'TCGA-J4-A67R', 'TCGA-J4-A67S', 'TCGA-J4-A67T', 'TCGA-J4-A6M7', 'TCGA-J4-A83I', 'TCGA-J4-A83J', 'TCGA-J4-A83L', 'TCGA-J4-A83M', 'TCGA-J4-A83N', 'TCGA-J4-AATZ', 'TCGA-J9-A52C', 'TCGA-J9-A52D', 'TCGA-J9-A52E', 'TCGA-J9-A8CK', 'TCGA-J9-A8CL', 'TCGA-J9-A8CP', 'TCGA-KC-A4BL', 'TCGA-KC-A4BN', 'TCGA-KC-A4BO', 'TCGA-KC-A4BR', 'TCGA-KC-A4BV', 'TCGA-KC-A7F3', 'TCGA-KC-A7F5', 'TCGA-KC-A7F6', 'TCGA-KC-A7FA', 'TCGA-KC-A7FD', 'TCGA-KC-A7FE', 'TCGA-KK-A59V', 'TCGA-KK-A59Y', 'TCGA-KK-A59Z', 'TCGA-KK-A5A1', 'TCGA-KK-A6DY', 'TCGA-KK-A6E0', 'TCGA-KK-A6E1', 'TCGA-KK-A6E2', 'TCGA-KK-A6E3', 'TCGA-KK-A6E4', 'TCGA-KK-A6E5', 'TCGA-KK-A6E6', 'TCGA-KK-A6E8', 'TCGA-KK-A7AP', 'TCGA-KK-A7AQ', 'TCGA-KK-A7AU', 'TCGA-KK-A7AV', 'TCGA-KK-A7AW', 'TCGA-KK-A7AY', 'TCGA-KK-A7AZ', 'TCGA-KK-A7B0', 'TCGA-KK-A7B1', 'TCGA-KK-A7B2', 'TCGA-KK-A7B3', 'TCGA-KK-A7B4', 'TCGA-KK-A8I4', 'TCGA-KK-A8I5', 'TCGA-KK-A8I6', 'TCGA-KK-A8I7', 'TCGA-KK-A8I8', 'TCGA-KK-A8IA', 'TCGA-KK-A8IB', 'TCGA-KK-A8IC', 'TCGA-KK-A8IF', 'TCGA-KK-A8IG', 'TCGA-KK-A8IH', 'TCGA-KK-A8II', 'TCGA-KK-A8IJ', 'TCGA-KK-A8IK', 'TCGA-KK-A8IL', 'TCGA-KK-A8IM', 'TCGA-M7-A71Y', 'TCGA-M7-A71Z', 'TCGA-M7-A721', 'TCGA-M7-A723', 'TCGA-M7-A725', 'TCGA-MG-AAMC', 'TCGA-QU-A6IL', 'TCGA-QU-A6IM', 'TCGA-QU-A6IN', 'TCGA-TK-A8OK', 'TCGA-TP-A8TT', 'TCGA-TP-A8TV', 'TCGA-V1-A8MG', 'TCGA-V1-A8MJ', 'TCGA-V1-A8ML', 'TCGA-V1-A8MM', 'TCGA-V1-A8MU', 'TCGA-V1-A8WL', 'TCGA-V1-A8WV', 'TCGA-V1-A8WW', 'TCGA-V1-A8X3', 'TCGA-V1-A9OA', 'TCGA-V1-A9OY', 'TCGA-V1-A9Z9', 'TCGA-V1-A9ZG', 'TCGA-V1-A9ZI', 'TCGA-VN-A88L', 'TCGA-VN-A88M', 'TCGA-VN-A88N', 'TCGA-VN-A88O', 'TCGA-VN-A88P', 'TCGA-VP-A875', 'TCGA-VP-A878', 'TCGA-VP-A879', 'TCGA-VP-A87C', 'TCGA-VP-A87D', 'TCGA-VP-A87H', 'TCGA-VP-A87J', 'TCGA-X4-A8KQ', 'TCGA-X4-A8KS', 'TCGA-XA-A8JR', 'TCGA-XJ-A83F', 'TCGA-XJ-A83G', 'TCGA-XJ-A83H', 'TCGA-XK-AAJA', 'TCGA-XK-AAJP', 'TCGA-XK-AAJR', 'TCGA-XK-AAJT', 'TCGA-XK-AAJU', 'TCGA-XK-AAK1', 'TCGA-XQ-A8TB', 'TCGA-YL-A8HJ', 'TCGA-YL-A8HK', 'TCGA-YL-A8HL', 'TCGA-YL-A8HM', 'TCGA-YL-A8HO', 'TCGA-YL-A8S8', 'TCGA-YL-A8S9', 'TCGA-YL-A8SB', 'TCGA-YL-A8SC', 'TCGA-YL-A8SH', 'TCGA-YL-A8SI', 'TCGA-YL-A8SJ', 'TCGA-YL-A8SK', 'TCGA-YL-A8SO', 'TCGA-YL-A8SP', 'TCGA-YL-A8SQ', 'TCGA-YL-A8SR', 'TCGA-YL-A9WH', 'TCGA-YL-A9WI', 'TCGA-YL-A9WK', 'TCGA-YL-A9WL', 'TCGA-YL-A9WX', 'TCGA-ZG-A8QW', 'TCGA-ZG-A8QZ', 'TCGA-ZG-A9L1', 'TCGA-ZG-A9L2', 'TCGA-ZG-A9L9', 'TCGA-ZG-A9LM', 'TCGA-ZG-A9LY', 'TCGA-ZG-A9LZ'] 
    gene_list_top200 =['SPOP', 'TP53',  'FOXA1',  'CTNNB1',  'MED12',  'C16orf62',  'CLPTM1L',  'DPYSL2',  'NEIL1',  'SLC27A4',  'PITPNM2',  'PTEN', 'ATM',  'EMG1',  'ETV3',  'BRAF',  'NKX3-1',  'ZMYM3',  'OR4P4',  'SALL1',  'IDH1',  'KDM6A',  'LMOD2',  'MUC17',  'NTM',  'OR4D5',  'COL11A1',  'PIK3CA', 'CDKN1B',  'NBPF1',  'CANT1',  'OR5L2',  'BHLHE22',  'EPB41L3',  'LCE2D',  'ACTRT1',  'OR4C6',  'RAG1',  'TAF1L',  'SBNO1',  'ANO4',  'OR10G8',  'SORCS1', 'HSPA8',  'PRG4',  'HRAS',  'SMARCA1',  'HEPHL1',  'RPL11',  'AADACL4',  'LINGO2',  'MECOM',  'OR4N4',  'AGAP6',  'SMG7',  'KRTAP5-7',  'PLCB4',  'CDK12', 'KIDINS220',  'ITGA2B',  'HIST1H4B',  'ATP6V1C2',  'SMAD4',  'DDX50',  'GIGYF2',  'OR10R2',  'OR5L1',  'GJA8',  'OR5AS1',  'TBX3',  'HTR1E',  'POM121C', 'FLRT2',  'CD5L',  'OR10J1',  'BMP2K',  'C2orf73',  'CDH12',  'SEL1L3',  'SPIB',  'HOXB13',  'RYBP',  'TUBA3C',  'MUT',  'A1CF',  'PSG8',  'CCT8L2',  'APC', 'NUDT12',  'IRF4',  'GABRB1',  'KIRREL',  'LCE1F',  'LRRIQ3',  'TPTE',  'PDYN',  'RPL5',  'UBTF',  'IL6ST',  'MMACHC',  'IRAK3',  'EFCAB1',  'FAM47B',  'GATA6',  'KRT6C',  'STAT3',  'SLC10A2',  'OR6N2',  'EEF2K',  'MKRN1',  'CR1L',  'FILIP1',  'TBXA2R',  'DCDC1',  'CNTN6',  'ANKRD28',  'ZNF254',  'PATE2', 'DCAF4L2',  'DPY19L2',  'LCE1D',  'MYCT1',  'EMR2',  'AQP9',  'FMN1',  'OC90',  'ZNF679',  'MORN4',  'NCKAP1L',  'ZMYM1',  'LILRB5',  'RRP12',  'TNFRSF21', 'BAI3',  'CA8',  'OR4S2',  'NALCN',  'CLEC1A',  'CD48',  'NAA38',  'CUL3',  'OR52D1',  'HIST1H2BK',  'ZNF568',  'EFCAB7',  'HIST1H2BG',  'TAF1D', 'KRTAP3-3', 'SETD2', 'SPOPL', 'TP53I13', 'TP53RK', 'TP53I11', 'TP53I3', 'TP53INP1', 'TP53BP2', 'TP53TG1', 'TP53BP1', 'TP53INP2', 'TP53AIP1', 'CTNNB1', 'MED12L', 'ERGIC1', 'ERGIC2', 'ERGIC3', 'ERG', 'ETV1', 'ETV4', 'FLI1', 'IDH1'] 
    gene_list_top20 =['SPOP', 'TP53',  'FOXA1',  'CTNNB1',  'MED12',  'C16orf62',  'CLPTM1L',  'DPYSL2',  'NEIL1',  'SLC27A4',  'PITPNM2',  'PTEN', 'ATM',  'EMG1',  'ETV3',  'BRAF',  'NKX3-1',  'ZMYM3',  'OR4P4',  'SALL1']
    # Keeping only genes which are linked to each other 
    gene_list_frmNetwork11 =['SPOP','TP53','FOXA1','CTNNB1','MED12','PITPNM2','PTEN','ATM','NKX3-1','ZMYM3','SALL1']

    
    gene_list = gene_list_top20
    
    pathGE = "C:\\PR_Proj_Thesis\\PRAD\\data\\gene_expression.csv"
    pathCN = "C:\\PR_Proj_Thesis\\PRAD\\data\\cna_linear.csv"
    pathDM = "C:\\PR_Proj_Thesis\\PRAD\\data\\dna_methylation.csv"
    pathClinical = "C:\\PR_Proj_Thesis\\PRAD\\data\\clinical_data.csv"
    # Read file 
    df_GE = pd.read_csv(pathGE)
    case_ids = df_GE['case_id'].values
    
    df_GE = df_GE.set_index("case_id",drop = True)
    
    """ Adding code to scale just GE using std scaler  """
#    scaler = preprocessing.StandardScaler().fit(df_GE)
#    df_GE = pd.DataFrame(scaler.fit_transform(df_GE), columns=df_GE.columns)
    
    df_GE = df_GE.apply(np.log)
    df_GE['case_id']= case_ids
    
    
    df_CN = pd.read_csv(pathCN)
    df_CN = df_CN.set_index("case_id",drop = False)
    
    df_DM = pd.read_csv(pathDM)
    df_DM = df_DM.set_index("case_id",drop = False)
    
    df_Clinical = pd.read_csv(pathClinical)
    df_Clinical = df_Clinical.set_index("case_id",drop = False)
    
    # Fill na 
    df_GE.fillna(0,inplace = True)
    df_CN.fillna(0,inplace = True)
    df_DM.fillna(0,inplace = True)
    
    # get gene expression data for the list of patients and combine with other omics to form a merge file   
    # create column name list from gene list 
    features_selected_withprefix_GE = ['GE_' + feature for feature in gene_list]
    features_selected_withprefix_DM = ['DM_' + feature for feature in gene_list]
    features_selected_withprefix_CN = ['CNA_' + feature for feature in gene_list]  
    #Create column names list for Dataframe 
    column_list = df_Clinical.columns
    column_list = column_list.append(pd.Index(features_selected_withprefix_GE))
    column_list = column_list.append(pd.Index(features_selected_withprefix_CN))
    column_list = column_list.append(pd.Index(features_selected_withprefix_DM))
    #Index_for_df = pd.Index(column_list)
    df = pd.DataFrame(columns=column_list,dtype = int)
    
    for i in patient_list:
        stage = df_Clinical.loc[df_Clinical['case_id'] == i]
        #get top 1000 mutated genes from all genes 
#        ge = df_GE.loc[:,gene_list]
        ge = df_GE.reindex(columns = gene_list) # using this to avoid warning when using loc #ge = ge.loc[:,gene_list] #
        ge = ge.loc[df_GE['case_id'] == i] # get all gene values for given patient
#        ge = ge.loc[[i]] # get all gene values for given patient

        ## ge = df_GE.reindex(gene_list, axis='columns')
        cn = df_CN.reindex(columns = gene_list)
        cn = cn.loc[df_CN['case_id'] == i] # get all gene values for given patient
        #cn = cn.loc[:,gene_list] # get top 1000 mutated genes from all genes 
        
        dm=df_DM.reindex(columns = gene_list)
        dm = dm.loc[df_DM['case_id'] == i] # get all gene values for given patient
        #dm = dm.loc[:,gene_list] # get top 1000 mutated genes from all genes 
        
        if (stage.shape[0] & ge.shape[0] & cn.shape[0] & dm.shape[0]):# check if data is present for all omics got a given patient id
            arr = np.column_stack((stage,ge,cn,dm))
            temp_df = pd.DataFrame(np.array(arr),columns= column_list)
            #print("temp_df = ", temp_df)
            df = df.append(temp_df,ignore_index=True)
            

       
    print("df.shape = ", df.shape)
    df.fillna(0,inplace=True)
    df = df.loc[:, (df != 0).any(axis=0)]# delete columns which has all zero's
    print("df.shape after deleting zero columns= ", df.shape)
    
    """ Apply scaling to whole data; before tht delete case id and tumor id and add aftr scaling  """
    PATIENT_ID = df['case_id'].values # get values in an array 
    TUMOR_STAGE = df['TUMOR_STAGE'].values
    #Drop columns 
    df.drop('case_id',axis = 1,inplace = True)
    df.drop('TUMOR_STAGE',axis = 1,inplace = True)
    #Apply scaling 
    scaler = MinMaxScaler(copy=True, feature_range=(0, 1))    
    df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    # Add columns 
    df['PATIENT_ID']= PATIENT_ID
    df['TUMOR_STAGE']= TUMOR_STAGE
    

    
    df.to_csv("Mergefile_top20_v5.csv",index = 0)
    print("Done,writing to file!!")