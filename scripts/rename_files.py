#!/usr/bin/env python3
# Filename: rename_files.py
# Author: #cf

"""
# Rename files based on selected metadata from the metadata.csv file.
"""


import glob
import pandas
import os
import shutil

# ====================================
# PARAMETERS
# ====================================

wdir = ""
inpath = wdir + "txt/*.txt"
metadatafile = wdir + "metadata/metadata.csv"
category1 = "author-short"
category2 = "title-short"
category3 = "subgenre-simple"
category4 = "form"


def rename_files(inpath, metadatafile, category1, category2, category3, category4):
    outfolder = category1 +"/"
    # Generate outfolder name and create if necessary.
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)
    # Copy the original files to the new folder.
    counter = 0
    for file in glob.glob(inpath):
        shutil.copy(file, outfolder+file[-10:])
    # For each file in the new folder...
    for file in glob.glob(outfolder+"*.txt"):
        # Get labels from metadatafile for primary and secondary category.
        idno, extension = os.path.basename(file).split(".")
        metadata = pandas.read_csv(metadatafile)
        metadata = metadata.set_index('idno', drop=True)
        label1 = metadata.loc[idno, category1]
        label2 = metadata.loc[idno, category2]
        label3 = metadata.loc[idno, category3]
        label4 = metadata.loc[idno, category4]
        print(idno, label1, label2, label3, label4)
        # Construct new filename based on labels.
        newfilename = label1 + "_" + label2 + "_" + label3 + "_" + label4 + "_"+ idno + ".txt"
        newoutputpath = outfolder+newfilename
        os.rename(file, newoutputpath)
        counter +=1
    print("\nDone. Files treated: " + str(counter))

def main(inpath, metadatafile, category1, category2, category3, category4):
        rename_files(inpath, metadatafile, category1, category2, category3, category4)

main(inpath, metadatafile, category1, category2, category3, category4)