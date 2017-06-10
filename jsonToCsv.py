# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 00:44:59 2017

@author: REd
Merge and convert JSON files to CSV file
"""
import json
import csv
import time
from path import path

class JsonToCsv:
    def __init__(self):
        self.path = 'data/'
        self.t_files = []
        
    def listFiles(self):
        "list au json files"
        for f in path(self.path).walkfiles():
            if f.endswith('.json'):
                self.t_files.append(f)
        
    def toCSV(self):
        "convert json files to csv file"
        all_entreprises_data = []
        nb_files = len(self.t_files)
        if nb_files > 0:
            #print self.t_files
            try:
                for f in self.t_files:
                    print "\n #Convert ",f        
                    with open(f) as data_file:    
                        data = json.load(data_file, 'cp1252')
                        if data.get('entreprises') and len(data['entreprises']) > 0:
                            all_entreprises_data.append(data['entreprises'])
                            #print entreprises_data
                #save csv file
                #"siren;localite;forme;rs;url;region;activite;code_activite;date;cp;proc;procedure"
                nowdate = time.ctime()
                score3_data = open('data/All_' + nowdate.replace(' ','_').replace(':','_') + '.csv', 'w')
                # create the csv writer object
                csvwriter = csv.writer(score3_data,dialect="excel")
                count = 0
                for entreprises_data in all_entreprises_data:
                    for emp in entreprises_data:
                        if count == 0:
                            header = emp.keys()
                            csvwriter.writerow(header)
                            count += 1
                        #values = self.rencode(emp.values())
                        values = emp.values()
                        csvwriter.writerow([unicode(s).encode("utf-8") for s in values])
                score3_data.close()
                print "\n Done"
            except IndexError:
                print 'NO data file'
        
if __name__ == '__main__': 
    trans = JsonToCsv()
    trans.listFiles()
    trans.toCSV()
