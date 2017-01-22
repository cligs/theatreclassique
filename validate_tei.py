# -*- coding: utf-8 -*-
# @date: April 27, 2016.
# @author: christof

import os
import glob
from lxml import etree

teipath = "./tei5/tc*.xml"
rngfile = "cligs.rng"

def validate_tei(teipath, rngfile):
    valid = 0
    invalid = 0
    for teifile in glob.glob(teipath): 
        idno = os.path.basename(teifile)
        print(idno)
        rngparsed = etree.parse("cligs.rng")
        rngvalidator = etree.RelaxNG(rngparsed)
        parser = etree.XMLParser(recover=True)
        teiparsed = etree.parse(teifile, parser)
        #teiparsed = etree.parse(teifile)
        validation = rngvalidator.validate(teiparsed)
        #log = rngvalidator.error_log
        if validation == True:
            valid +=1
            #print(idno, "valid!")
        else:
            invalid +=1
            print(idno, "sorry, not valid!")
            #print(log.last_error)
            #print(log.last_error.domain_name)
    print("valid:", valid, "-- invalid:", invalid)
    if invalid == 0: 
        print("Congratulations, all of your "+str(valid)+" files are valid!")

def main(teipath, rngfile):
    validate_tei(teipath, rngfile)

main(teipath, rngfile)
