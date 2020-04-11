# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 04:35:28 2019

@author: Fatima
"""

# get gene values from each file for following patient ID's
import pandas as pd
import numpy as np
#from sklearn.preprocessing import MinMaxScaler
    
if __name__ == "__main__":
	
    patient_list = ['TCGA-LQ-A4E4', 'TCGA-A2-A3KC', 'TCGA-A2-A3KD', 'TCGA-A7-A0D9', 'TCGA-A7-A0DA', 'TCGA-A7-A0CE', 'TCGA-A7-A0CH', 'TCGA-A7-A0CG', 'TCGA-A7-A0CJ', 'TCGA-D8-A145', 'TCGA-D8-A146', 'TCGA-D8-A143', 'TCGA-D8-A142', 'TCGA-D8-A140', 'TCGA-A7-A0DB', 'TCGA-BH-A0HX', 'TCGA-A2-A1FX', 'TCGA-A2-A1FW', 'TCGA-A2-A1FV', 'TCGA-BH-A0HK', 'TCGA-A2-A1FZ', 'TCGA-BH-A0HO', 'TCGA-A2-A1G1', 'TCGA-BH-A0HQ', 'TCGA-A2-A1G0', 'TCGA-BH-A0HP', 'TCGA-A2-A1G6', 'TCGA-A2-A1G4', 'TCGA-BH-A0H7', 'TCGA-BH-A0H9', 'TCGA-BH-A0GY', 'TCGA-BH-A0GZ', 'TCGA-C8-A26Z', 'TCGA-C8-A26Y', 'TCGA-C8-A27A', 'TCGA-C8-A273', 'TCGA-C8-A275', 'TCGA-AC-A23H', 'TCGA-C8-A274', 'TCGA-AC-A23G', 'TCGA-C8-A26V', 'TCGA-AC-A23E', 'TCGA-C8-A26X', 'TCGA-AC-A23C', 'TCGA-C8-A278', 'TCGA-C8-A26W', 'TCGA-A7-A26G', 'TCGA-A7-A26I', 'TCGA-A7-A26H', 'TCGA-A7-A26E', 'TCGA-C8-A27B', 'TCGA-A7-A26J', 'TCGA-AC-A3TN', 'TCGA-BH-A0W4', 'TCGA-BH-A0W3', 'TCGA-AC-A3TM', 'TCGA-AN-A0XU', 'TCGA-A7-A5ZV', 'TCGA-A7-A5ZW', 'TCGA-A7-A3RF', 'TCGA-BH-A0W5', 'TCGA-B6-A0WV', 'TCGA-B6-A0X4', 'TCGA-B6-A0WT', 'TCGA-B6-A0X5', 'TCGA-B6-A0WY', 'TCGA-B6-A0WX', 'TCGA-AC-A3W5', 'TCGA-AC-A3W7', 'TCGA-AC-A3W6', 'TCGA-GM-A3NY', 'TCGA-B6-A0RV', 'TCGA-AC-A5XS', 'TCGA-B6-A0RQ', 'TCGA-B6-A0RT', 'TCGA-BH-A0RX', 'TCGA-A1-A0SH', 'TCGA-AC-A3QP', 'TCGA-E2-A1B6', 'TCGA-A1-A0SJ', 'TCGA-A1-A0SI', 'TCGA-E2-A1AZ', 'TCGA-A1-A0SD', 'TCGA-AR-A0TS', 'TCGA-AR-A0U3', 'TCGA-A1-A0SF', 'TCGA-AR-A0U2', 'TCGA-AR-A0TX', 'TCGA-AR-A0TY', 'TCGA-E2-A1BD', 'TCGA-GM-A3NW', 'TCGA-EW-A2FS', 'TCGA-EW-A2FW', 'TCGA-AQ-A0Y5', 'TCGA-E2-A1B4', 'TCGA-E2-A1B5', 'TCGA-E2-A1B0', 'TCGA-E2-A1B1', 'TCGA-B6-A0RH', 'TCGA-B6-A0RG', 'TCGA-E9-A295', 'TCGA-E9-A1RB', 'TCGA-AO-A128', 'TCGA-E9-A1RD', 'TCGA-E9-A1RI', 'TCGA-E9-A1RE', 'TCGA-E9-A1RF', 'TCGA-E9-A1RH', 'TCGA-E9-A1R0', 'TCGA-E9-A1QZ', 'TCGA-E9-A1R6', 'TCGA-E9-A1R7', 'TCGA-A7-A3IZ', 'TCGA-E9-A24A', 'TCGA-E9-A245', 'TCGA-E9-A244', 'TCGA-E9-A243', 'TCGA-E9-A249', 'TCGA-A7-A3J0', 'TCGA-E9-A248', 'TCGA-AC-A3OD', 'TCGA-GI-A2C9', 'TCGA-E9-A1NF', 'TCGA-E9-A1NE', 'TCGA-E9-A1NH', 'TCGA-E9-A1NG', 'TCGA-E9-A1NA', 'TCGA-E9-A1ND', 'TCGA-E9-A1N9', 'TCGA-A2-A0ST', 'TCGA-A2-A0T5', 'TCGA-E9-A1N5', 'TCGA-A2-A0SU', 'TCGA-A2-A0T6', 'TCGA-A2-A0T7', 'TCGA-E9-A1N8', 'TCGA-A2-A0SY', 'TCGA-E9-A1N3', 'TCGA-E9-A1N4', 'TCGA-A2-A0T0', 'TCGA-A2-A0T4', 'TCGA-AC-A3HN', 'TCGA-E9-A1NI', 'TCGA-B6-A0IM', 'TCGA-B6-A0IO', 'TCGA-B6-A0IQ', 'TCGA-E9-A3X8', 'TCGA-BH-A18V', 'TCGA-BH-A18U', 'TCGA-B6-A0IE', 'TCGA-B6-A0IH', 'TCGA-B6-A0IG', 'TCGA-B6-A0IJ', 'TCGA-BH-A18L', 'TCGA-BH-A18I', 'TCGA-BH-A18F', 'TCGA-BH-A18T', 'TCGA-BH-A18Q', 'TCGA-BH-A18R', 'TCGA-BH-A18M', 'TCGA-BH-A18N', 'TCGA-E9-A22G', 'TCGA-E9-A22E', 'TCGA-E9-A22D', 'TCGA-A7-A13D', 'TCGA-A7-A13E', 'TCGA-A7-A13F', 'TCGA-E9-A22H', 'TCGA-A7-A13G', 'TCGA-A7-A13H', 'TCGA-E9-A22A', 'TCGA-E9-A226', 'TCGA-E9-A227', 'TCGA-AC-A62Y', 'TCGA-MS-A51U', 'TCGA-E9-A228', 'TCGA-B6-A0IA', 'TCGA-E2-A2P6', 'TCGA-B6-A0I5', 'TCGA-E2-A15R', 'TCGA-E2-A15S', 'TCGA-E2-A15T', 'TCGA-E2-A15M', 'TCGA-E2-A15I', 'TCGA-E2-A15K', 'TCGA-E2-A15L', 'TCGA-AR-A1AH', 'TCGA-AR-A1AV', 'TCGA-AR-A1AU', 'TCGA-AR-A1AW', 'TCGA-AR-A1AR', 'TCGA-AR-A1AQ', 'TCGA-AR-A1AS', 'TCGA-AR-A1AN', 'TCGA-AR-A1AM', 'TCGA-AR-A1AO', 'TCGA-AR-A1AI', 'TCGA-AR-A1AL', 'TCGA-AQ-A04L', 'TCGA-AQ-A1H2', 'TCGA-BH-A1EN', 'TCGA-BH-A1EO', 'TCGA-BH-A1F0', 'TCGA-E2-A14R', 'TCGA-E2-A153', 'TCGA-E2-A14Q', 'TCGA-E2-A14V', 'TCGA-E2-A158', 'TCGA-E2-A14W', 'TCGA-E2-A155', 'TCGA-E2-A14T', 'TCGA-BH-A1EY', 'TCGA-BH-A1EX', 'TCGA-BH-A1EW', 'TCGA-BH-A1EV', 'TCGA-E2-A14N', 'TCGA-E2-A150', 'TCGA-BH-A1F5', 'TCGA-E2-A14O', 'TCGA-BH-A1ES', 'TCGA-E2-A15D', 'TCGA-C8-A1HI', 'TCGA-C8-A1HJ', 'TCGA-A2-A0YH', 'TCGA-C8-A1HK', 'TCGA-E2-A15H', 'TCGA-BH-A1FM', 'TCGA-A2-A0YC', 'TCGA-E2-A15G', 'TCGA-BH-A1FN', 'TCGA-C8-A1HE', 'TCGA-AQ-A04H', 'TCGA-C8-A1HF', 'TCGA-A2-A0YD', 'TCGA-E2-A15E', 'TCGA-C8-A1HG', 'TCGA-BH-A1FL', 'TCGA-AQ-A04J', 'TCGA-BH-A1FJ', 'TCGA-E2-A14Y', 'TCGA-E2-A159', 'TCGA-E2-A14X', 'TCGA-C8-A1HL', 'TCGA-BH-A1FE', 'TCGA-A2-A0YK', 'TCGA-C8-A1HM', 'TCGA-C8-A1HN', 'TCGA-A2-A0YL', 'TCGA-BH-A1FC', 'TCGA-A2-A0YM', 'TCGA-E9-A5UP', 'TCGA-E9-A5UO', 'TCGA-E2-A105', 'TCGA-B6-A2IU', 'TCGA-E2-A107', 'TCGA-E2-A108', 'TCGA-E2-A109', 'TCGA-E2-A10A', 'TCGA-E2-A10B', 'TCGA-E2-A10C', 'TCGA-E2-A10F', 'TCGA-E2-A10E', 'TCGA-AC-A3BB', 'TCGA-E9-A3QA', 'TCGA-EW-A3U0', 'TCGA-AN-A0FV', 'TCGA-AN-A0FT', 'TCGA-AN-A0FZ', 'TCGA-AN-A0FW', 'TCGA-AN-A0FX', 'TCGA-AN-A0FL', 'TCGA-A8-A075', 'TCGA-A8-A06T', 'TCGA-A8-A06Q', 'TCGA-A8-A06R', 'TCGA-JL-A3YW', 'TCGA-A8-A06P', 'TCGA-JL-A3YX', 'TCGA-AC-A2QH', 'TCGA-EW-A423', 'TCGA-AC-A2QI', 'TCGA-A8-A083', 'TCGA-A8-A084', 'TCGA-AN-A0AT', 'TCGA-A8-A085', 'TCGA-AN-A0AS', 'TCGA-A8-A086', 'TCGA-A8-A07U', 'TCGA-A8-A07O', 'TCGA-A8-A07P', 'TCGA-A8-A081', 'TCGA-A8-A082', 'TCGA-AN-A0AM', 'TCGA-A8-A07J', 'TCGA-AN-A0AK', 'TCGA-A8-A07L', 'TCGA-AN-A0AJ', 'TCGA-A8-A07F', 'TCGA-EW-A1J1', 'TCGA-A8-A07G', 'TCGA-A8-A07I', 'TCGA-A8-A07B', 'TCGA-EW-A1IX', 'TCGA-EW-A1IW', 'TCGA-A8-A06Z', 'TCGA-A8-A06Y', 'TCGA-A8-A06U', 'TCGA-A8-A076', 'TCGA-D8-A1XZ', 'TCGA-D8-A1XY', 'TCGA-D8-A1XW', 'TCGA-D8-A1XV', 'TCGA-D8-A1XT', 'TCGA-GM-A2DA', 'TCGA-GM-A2DB', 'TCGA-GM-A2DC', 'TCGA-GM-A2DF', 'TCGA-GM-A2DM', 'TCGA-GM-A2DN', 'TCGA-D8-A27V', 'TCGA-A2-A0EN', 'TCGA-A2-A0EQ', 'TCGA-D8-A1XF', 'TCGA-A2-A0ES', 'TCGA-D8-A1XJ', 'TCGA-A2-A0ET', 'TCGA-D8-A1XL', 'TCGA-D8-A1XK', 'TCGA-A2-A0EY', 'TCGA-A2-A0EX', 'TCGA-D8-A1Y1', 'TCGA-D8-A1XO', 'TCGA-D8-A1Y0', 'TCGA-D8-A1XR', 'TCGA-D8-A1Y3', 'TCGA-D8-A1XQ', 'TCGA-D8-A1Y2', 'TCGA-D8-A1X6', 'TCGA-D8-A1X7', 'TCGA-D8-A1X8', 'TCGA-D8-A1X9', 'TCGA-D8-A1XB', 'TCGA-HN-A2NL', 'TCGA-EW-A1P7', 'TCGA-A2-A0D2', 'TCGA-EW-A1OV', 'TCGA-D8-A27F', 'TCGA-A2-A0D4', 'TCGA-EW-A1P5', 'TCGA-D8-A27H', 'TCGA-EW-A1P6', 'TCGA-A2-A0CR', 'TCGA-D8-A27G', 'TCGA-A2-A0CM', 'TCGA-EW-A1P3', 'TCGA-A2-A0CL', 'TCGA-EW-A1P4', 'TCGA-A2-A0D0', 'TCGA-A2-A0CO', 'TCGA-D8-A27N', 'TCGA-EW-A1P0', 'TCGA-AO-A1KT', 'TCGA-A2-A0CU', 'TCGA-AO-A1KR', 'TCGA-A2-A0CT', 'TCGA-D8-A27I', 'TCGA-AO-A1KS', 'TCGA-A2-A4S0', 'TCGA-A2-A0CW', 'TCGA-D8-A27L', 'TCGA-AO-A1KP', 'TCGA-A2-A4S3', 'TCGA-A2-A0CV', 'TCGA-D8-A27K', 'TCGA-A2-A4S2', 'TCGA-EW-A1PH', 'TCGA-AO-A1KO', 'TCGA-EW-A1PG', 'TCGA-EW-A1PE', 'TCGA-EW-A1PD', 'TCGA-EW-A1PC', 'TCGA-A2-A4RX', 'TCGA-EW-A1PB', 'TCGA-EW-A1PA', 'TCGA-A2-A0CK', 'TCGA-EW-A1OZ', 'TCGA-EW-A1OY', 'TCGA-EW-A1OX', 'TCGA-AR-A24O', 'TCGA-AR-A24Q', 'TCGA-AR-A24R', 'TCGA-AR-A24K', 'TCGA-AR-A24L', 'TCGA-AR-A24M', 'TCGA-A7-A2KD', 'TCGA-A7-A4SF', 'TCGA-A7-A4SE', 'TCGA-A7-A4SD', 'TCGA-A7-A4SB', 'TCGA-A7-A4SA', 'TCGA-C8-A133', 'TCGA-C8-A134', 'TCGA-C8-A12T', 'TCGA-C8-A135', 'TCGA-C8-A12U', 'TCGA-C8-A12N', 'TCGA-C8-A12O', 'TCGA-C8-A130', 'TCGA-C8-A12P', 'TCGA-C8-A131', 'TCGA-C8-A132', 'TCGA-C8-A12Q', 'TCGA-C8-A12Z', 'TCGA-C8-A12V', 'TCGA-C8-A137', 'TCGA-C8-A138', 'TCGA-C8-A12X', 'TCGA-C8-A12Y', 'TCGA-C8-A12M', 'TCGA-C8-A12L', 'TCGA-C8-A12K', 'TCGA-AR-A24H', 'TCGA-A8-A09Z', 'TCGA-EW-A3E8', 'TCGA-A8-A08B', 'TCGA-E2-A56Z', 'TCGA-A8-A08H', 'TCGA-A8-A08G', 'TCGA-A8-A08I', 'TCGA-A8-A08L', 'TCGA-E2-A574', 'TCGA-A8-A091', 'TCGA-AN-A04D', 'TCGA-A8-A090', 'TCGA-A8-A08R', 'TCGA-A8-A093', 'TCGA-A8-A092', 'TCGA-A8-A094', 'TCGA-A8-A08S', 'TCGA-A8-A097', 'TCGA-A8-A096', 'TCGA-A8-A09D', 'TCGA-A8-A09K', 'TCGA-A8-A09I', 'TCGA-A8-A09R', 'TCGA-E2-A1LB', 'TCGA-E2-A1LA', 'TCGA-E2-A1LG', 'TCGA-E2-A1LI', 'TCGA-E2-A1LL', 'TCGA-A1-A0SP', 'TCGA-A1-A0SQ', 'TCGA-A1-A0SK', 'TCGA-A1-A0SN', 'TCGA-A1-A0SM', 'TCGA-D8-A1JT', 'TCGA-D8-A1JL', 'TCGA-D8-A1JK', 'TCGA-D8-A1JJ', 'TCGA-D8-A1JI', 'TCGA-D8-A1JG', 'TCGA-D8-A1JF', 'TCGA-D8-A1JE', 'TCGA-D8-A1JB', 'TCGA-D8-A1JC', 'TCGA-D8-A1JD', 'TCGA-D8-A1J8', 'TCGA-AR-A2LJ', 'TCGA-AR-A2LO', 'TCGA-AR-A2LQ', 'TCGA-AR-A2LN', 'TCGA-B6-A1KF', 'TCGA-A2-A04T', 'TCGA-A2-A25E', 'TCGA-GM-A3XG', 'TCGA-A2-A25F', 'TCGA-A2-A04Y', 'TCGA-GM-A3XL', 'TCGA-A2-A25A', 'TCGA-GM-A3XN', 'TCGA-A2-A25B', 'TCGA-A2-A25C', 'TCGA-BH-A28Q', 'TCGA-A2-A04U', 'TCGA-A2-A04V', 'TCGA-A2-A04W', 'TCGA-A2-A04X', 'TCGA-E2-A1IE', 'TCGA-E2-A1IG', 'TCGA-E2-A1IL', 'TCGA-E2-A1IK', 'TCGA-OL-A66I', 'TCGA-OL-A66K', 'TCGA-B6-A1KC', 'TCGA-AC-A2B8', 'TCGA-A8-A0A7', 'TCGA-A8-A0A4', 'TCGA-E2-A1L8', 'TCGA-E2-A1L9', 'TCGA-A8-A0A2', 'TCGA-A8-A0A1', 'TCGA-E2-A1L6', 'TCGA-E2-A1L7', 'TCGA-AC-A2BK', 'TCGA-AC-A2BM', 'TCGA-A8-A0A9', 'TCGA-BH-A0BV', 'TCGA-BH-A0C7', 'TCGA-BH-A0C1', 'TCGA-BH-A0BS', 'TCGA-BH-A0BZ', 'TCGA-BH-A0DH', 'TCGA-BH-A0DI', 'TCGA-BH-A0DG', 'TCGA-BH-A0DD', 'TCGA-BH-A0DE', 'TCGA-BH-A0DP', 'TCGA-BH-A0E1', 'TCGA-BH-A0DQ', 'TCGA-BH-A0E2', 'TCGA-BH-A0DL', 'TCGA-BH-A0DK', 'TCGA-BH-A0DS', 'TCGA-AC-A2FB', 'TCGA-BH-A0DT', 'TCGA-AQ-A54O', 'TCGA-BH-A0E7', 'TCGA-BH-A0DV', 'TCGA-BH-A0E9', 'TCGA-BH-A42U', 'TCGA-BH-A0DZ', 'TCGA-BH-A42T', 'TCGA-AC-A2FM', 'TCGA-AQ-A54N', 'TCGA-AC-A2FG', 'TCGA-AC-A2FF', 'TCGA-BH-A0EA', 'TCGA-BH-A0EE', 'TCGA-BH-A0EI', 'TCGA-LL-A5YN', 'TCGA-LL-A5YL', 'TCGA-LL-A5YP', 'TCGA-AC-A2FO', 'TCGA-LL-A50Y', 'TCGA-E9-A2JS', 'TCGA-E9-A2JT', 'TCGA-A2-A3Y0', 'TCGA-A2-A3XU', 'TCGA-A2-A3XT', 'TCGA-A2-A3XS', 'TCGA-A2-A3XY', 'TCGA-A2-A3XX', 'TCGA-A2-A3XW', 'TCGA-A2-A3XV', 'TCGA-BH-A0AY', 'TCGA-BH-A0AZ', 'TCGA-BH-A0AW', 'TCGA-BH-A0B3', 'TCGA-BH-A0AU', 'TCGA-BH-A0B7', 'TCGA-BH-A0B4', 'TCGA-BH-A0B5', 'TCGA-BH-A0BJ', 'TCGA-BH-A0C0', 'TCGA-BH-A203', 'TCGA-BH-A0BM', 'TCGA-BH-A204', 'TCGA-BH-A0BF', 'TCGA-BH-A208', 'TCGA-BH-A0BD']
	gene_list_top20 = ['RUNX1', 'PIK3CA', 'TP53', 'GATA3', 'FOXA1', 'SF3B1', 'PTEN', 'CBFB', 'CDH1', 'TBX3', 'MAP2K4', 'MAP3K1', 'ERBB2', 'MLL3', 'NCOR1', 'FAM86B2', 'CDKN1B', 'HIST1H3B', 'THEM5']
    gene_list = gene_list_top20
    
    pathGE = "C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\data\\gene_expression.csv"
    pathCN = "C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\data\\cna_norm.csv"
    pathDM = "C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\data\\methylation.csv"
    pathClinical = "C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\data\\clinical_data.csv"
    # Read file 
    df_GE = pd.read_csv(pathGE)
    df_GE = df_GE.set_index("PATIENT_ID",drop = False)
    
    df_CN = pd.read_csv(pathCN)
    df_CN = df_CN.set_index("PATIENT_ID",drop = False)
    
    df_DM = pd.read_csv(pathDM)
    df_DM = df_DM.set_index("PATIENT_ID",drop = False)
    
    df_Clinical = pd.read_csv(pathClinical)
    df_Clinical = df_Clinical.set_index("PATIENT_ID",drop = False)
    
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
        stage = df_Clinical.loc[df_Clinical['PATIENT_ID'] == i]
        #get top 1000 mutated genes from all genes 
        ge = df_GE.reindex(columns = gene_list) # using this to avoid warning when using loc #ge = ge.loc[:,gene_list] #
        ge = ge.loc[df_GE['PATIENT_ID'] == i] # get all gene values for given patient
        
        ## ge = df_GE.reindex(gene_list, axis='columns')
        cn = df_CN.reindex(columns = gene_list)
        cn = cn.loc[df_CN['PATIENT_ID'] == i] # get all gene values for given patient
        #cn = cn.loc[:,gene_list] # get top 1000 mutated genes from all genes 
        
        dm=df_DM.reindex(columns = gene_list)
        dm = dm.loc[df_DM['PATIENT_ID'] == i] # get all gene values for given patient
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
    df.to_csv("Mergefile_top20_norm.csv",index = 0)
    print("Done,writing to file!!")