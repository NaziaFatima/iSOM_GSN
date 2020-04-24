# iSOM_GSN
An Integrative Approach for Transforming Multi-omic Data into Gene Similarity Networks via Self-organizing Maps

To replicate the algorithm use the following steps:

Step 1 (1_PreProcessing.py)- Process the data using pre-processing template provided. To use this template;create three different files of each type of omic data; for a set of samples(Patient id) and a set of common genes. Replace the patient id's with patient_list and gene_list. As a result of the preprocessing script the result will be a merge file which has all three omic data for a set of patients/samples

Step 2 (2_CreateTemplate.py)- Once the data is pre-processed proceed with the creation of template file; we conside only gene expression data for this step. replace the path of the file at "pathGE" variable. As a result of this script we get coordinates or mapping of genes. i.e., (x,y) coordinates for each gene; make a note of this to use in next step.

Step 3 (3_CreateRGBImages.py)- replace the mappings or cordinates obtained in previous step with "pos" variable in this script. replace the path variable "pathGE" with the file generated at the first step. At the end of this script you have an image for each patient.

Step 4 (4_MoveFilesRandomly.py)- This file is optional; this is used to randomly divide the images into test and training set

Step 5 (5_Apply_cnn-metrics.py)- Use this file to run CNN algorithm on the images generated in the previous step; replace the path of reflect the actual paths.

Input Files: As we use three types of Omic data, Initially the data from cbioPortal is process and formatted into 3 files. They are gene_expression.csv, cna_norm.csv and dna_methylation.csv.
After applying Step 1 of script it generates a merged file with all three omics of the shortlisted genes. This sample file for 20 gnees is attached which is called Mergefile_top20.csv. This file is used as input for step 2 and so on.

Note: To include more than three omic data the code needs modification. 
The pre-processing file is created to process the data of formats mentioned in gene_expression.csv, cna_norm.csv and dna_methylation.csv. If the format is changed then the pre-processing file need to be adjusted accordingly.

