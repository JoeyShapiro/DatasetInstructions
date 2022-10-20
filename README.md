# Dataset Instructions

This contains instructions on how to install the dataset for study "A Corpus of Encoded Malware Byte Information as Images for Efficient Classification"

All of the benign files that have been converted to images as well as the executables used from theZoo dataset can be found here: 
https://drive.google.com/drive/folders/1nvCzAAGpywxO0DbOkW8EEZDuoyZkAurL?usp=sharing

The DikeDataset can be found here:
https://github.com/iosifache/DikeDataset

To create a custom dataset of benign files, we have created the gather_files.py python script, which will search for any '.exe' files on your computer and copy that file to a given directory, while ensuring that file is unique.
