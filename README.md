# Dataset Instructions

This contains instructions on how to install the dataset for study "A Corpus of Encoded Malware Byte Information as Images for Efficient Classification"

## BODMAS:
To recieve full-access to the BODMAS dataset, you must email Limin (liminy2@illinois.edu) and CC Gang (gangw@illinois.edu) and include your Gmail address in the body so that they can add you to the google drive folder where the dataset is stored.<br />You must also contact them using your institution email and provide them with a webpage registered at the university domain that contains your name and affiliation.<br />
***Keep in mind:*** This dataset should not be shared with other (except your co-authors for the project). The authors are however happy to share with other researchers based upon their requests.<br />
If you are not in academia, please view all of the other options for downloading the dataset here: https://whyisyoung.github.io/BODMAS/

## Benign Files and theZoo:
All of the benign files that have been converted to images as well as the executables used from theZoo dataset can be found here: 
https://drive.google.com/drive/folders/1nvCzAAGpywxO0DbOkW8EEZDuoyZkAurL?usp=sharing

The original theZoo dataset can be found here:
https://github.com/ytisf/theZoo

## DikeDataset:
The DikeDataset can be found here:
https://github.com/iosifache/DikeDataset

## Creating your own benign dataset:
To create a custom dataset of benign files, we have created the gather_files.py python script, which will search for every '.exe' files on your computer and copy those files to a given directory, while ensuring each file is unique.
