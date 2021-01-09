# create synonym list and merge with xref file
# 

import fontforge
import os
import sys
import csv
import logging


script = sys.argv[0]
logname = script.split('.')[0]
sys.stdout = open(logname+".log", "w",encoding="utf-8")
 
xuniCol = 2     # unicode column in xref
xnameCol = 1    # name column in xref 
xrefCol = 3     # xref column in xref
xglyphCol = 0     # fontforge glyph
puniCol = 2     # unicode column in primary
pnameCol = 1    # name column in primary

def getUnicode(str):
    a = chr(int(str,16)).encode('utf-8')
    #print('getunicode hex:',str,' unicode:', a.hex(), a.decode('utf-8'))
    return a.decode('utf-8')

# merge xref and ref  p=primary, x = xref, r = ref 
def mergeRefXref(p,r,x):
    print('mergeRefXref',type(p),type(r), type(x))
    data = []

    for uec in p:
        word = p[uec]
        item = []
       
        #print('mergexrefsyn',uec, 'in', uec in r, uec in x)
        #if x.get(uec) != None:
        item.append(uec)
        item.append(word)
        
        if uec in r:
            rList = r[uec]
            item.append(rList)
        else:
            item.append("")
                        
        if uec in x:
            item.append(x[uec])
        else:
            item.append("")
        print('mrx',item)
        data.append(item) 

    return(data)

def writeRefXref(outfile, ddata):
    print('wrtexref')
    with open(outfile, 'w', encoding='utf8') as f:
        for row in ddata:
            print('wrd',len(row), row)
            name = row[1].strip()
            uec = row[0].strip().lower()
            ref = '"'+row[2].strip()+'"'
            if len(row) < 4:
                xref = ""
            else:
                xref = row[3].strip()
            #print(uec, xref, type(xref))

            if "," in xref:
                xref = '"'+xref+'"'
            unicode = getUnicode(uec)
            print('uic',unicode,name,ref,uec,xref)
            f.write(unicode+','+name+','+ref+','+uec+','+xref+'\n')    

# e03e, persecution persecute tribulation
def read_ref(f):
    print('read_ref')
    rf = {}
    with open(f, encoding='utf8', newline='') as csvfile:
        data = list(csv.reader(csvfile))
        #print(data)
        for i in data:
            if len(i) > 1:
                unicode = i[0].strip().lower()
                rf[unicode] = i[1].strip()
            print('rr',unicode, rf[unicode])
    return rf
            
# "ea5b","man: king,master,ruler,lord: love,compassion" 
def read_xref(f):
    print('read_xref')
    xd = {}
    with open(f, encoding='utf8', newline='') as csvfile:
        data = list(csv.reader(csvfile))
        for i in data:
            unicode = i[0].strip().lower()
            xref = i[1]
            xd[unicode] = xref
        print('xr',unicode, xd[unicode])
    return xd

# ,eb78,Dionysius
def read_pri(f):
    print('read pri')
    pd = {}
    with open(f, encoding='utf8', newline='') as csvfile:
        data = list(csv.reader(csvfile))
        for i in data:
            symbol = i[xglyphCol]
            unicode = i[puniCol].strip().lower()
            name = i[pnameCol]
            pd[unicode] = name
    return pd
 
if len(sys.argv) > 3: 

    priData = read_pri(sys.argv[1])    #primary word list
    for r in priData:
        print('p',r)
    
    refData = read_ref(sys.argv[2])   # ref list
    for r in refData:
        print('r',r)
    xrefData = read_xref(sys.argv[3])   # xref list
    for r in xrefData:
        print('x',r)
    mergeData = mergeRefXref(priData, refData, xrefData)  
    for r in mergeData:
        print('m',r)
    writeRefXref(sys.argv[4], mergeData)    # outfile

else:
    print("\nsyntax: fontforge -script synxref.py primary.csv xref.csv output.csv")
    print("Creates a synonym file and a merged xref and synonym file")
    print("Also creates 'syn.csv' as a separate file")

print ('\n*** done ****')


