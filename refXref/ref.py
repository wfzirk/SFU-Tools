# create bible reference list from kmn*.csv
# 
#

import sys
import csv
# to do sort list 
# todo sorted(list, key=lambda x: x[1])
script = sys.argv[0]
logname = script.split('.')[0]
#sys.stdout = open(logname+".log", "w",encoding="utf-8")

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r', encoding='utf8') as fr:
        csv_reader = csv.reader(fr, skipinitialspace=True)
        #with open('ref.csv', 'w') as fw
        prevuec = '***'
        prevname = '***'
        count = 0
        refList = {}
        for line in csv_reader:
            print(line)
            #ln = line.split(",")
            ref = line[3].strip()
            #if len(ref) > 0:
            #    ref = '('+ref+')'
                
            name = line[1].strip()+' '+ref
            uec = line[2].strip()
            if uec in refList:
                refList[uec] = refList[uec]+' '+ref 
            else:
                refList[uec] = ref
            
            #print(uec,refList[uec])
          
    with open('ref.csv', 'w', encoding='utf8') as fw:        
        for u in refList:  
            line = u +',"'+refList[u].strip()+ '"\n'
            print(line)
            fw.write(line)
    '''
    with open('ref.csv', 'wt', encoding='utf8') as fw:  
        csv_writer = csv.writer(fw, csv.QUOTE_ALL)
        for u in refList:  
            line = u +','+refList[u]
            csv_writer.writerow(line)
    '''
    print ('\n*** done ****')
else:
    print("\nsyntax: fontforge -script synonyms.py kmn.csv")
    print("   i.e. fontforge -script synonyms.py kmnSUN7_6.csv")
    print(" NOTE: must be sorted by unicode column")
    print("   creates 'syn.csv' - list of synonyms in the kmn file")
