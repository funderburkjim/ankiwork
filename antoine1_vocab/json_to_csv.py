""" json_to_csv.py  Conversion for anki basic deck import
 ref: https://medium.com/@gabrielpires/how-to-convert-a-json-file-to-csv-python-script-a9ff0a3f906e
 12-29-2019
 python3 json_to_csv.py tag json/x.json csv/x.csv
 Normally, tag is identical to x
"""
import csv, json, sys
#if you are not using utf-8 files, remove the next line
# setdefaultencoding not python3
#sys.setdefaultencoding("UTF-8") #set the encode to utf8
#check if you pass the input file and output file
if __name__ == "__main__":
 filetag = sys.argv[1]
 fileInput = sys.argv[2]
 fileOutput = sys.argv[3]
 with open(fileInput) as f:
  data = json.load(f) #load json content
 with open(fileOutput, 'w',newline='') as f:
  output = csv.writer(f,delimiter='\t') #create a csv.write
  #output.writerow(data[0].keys())  # header row not used
  for row in data:
   # row is a dictionary
   text = row['text']
   key = row['key']
   tag = filetag
   values = [key,text,tag]
   output.writerow(values) #values row
 print(len(data),'records loaded from',fileInput,'and written to',fileOutput)

