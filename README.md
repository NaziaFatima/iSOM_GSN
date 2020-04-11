# iSOM_GSN
An Integrative Approach for Transforming Multi-omic Data into Gene Similarity Networks via Self-organizing Maps

To replicate the algorithm use the following steps:

1(1_PreProcessing.py)- Process the data using pre-processing template provided.To use this template;create 3 different files of each type of omic data; for a set of samples(Patient id) and a set of common genes.Replace the patient id's with patient_list and gene_list. As a result of the preprocessing script the result will be a merge file which has all 3 omic data for a set of patients/samples
2(2_CreateTemplate.py)- Once the data is pre-processed proceed with the creation of template file; we conside only gene expression data for this step.
replace the path of the file at "pathGE" variable. As a result of this script we get coordinates or mapping of genes. i.e x,y coordinates for each gene; make a note of this to use in next step.
3(3_CreateRGBImages.py)- replace the mappings or cordinates obtained in previous step with "pos" variable in this script. replace the path variable "pathGE" with the file generated at the first step. At the end of this script you have an image for each patient.
4(4_MoveFilesRandomly.py)- This file is optional; this is used to randomly divide the images into test and training set
5(5_Apply_cnn-metrics.py)- Use this file to run CNN algorithm on the images generated in the previous step; replace the path of reflect the actual paths.
