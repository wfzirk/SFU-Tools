
#import fontforge
import sys
import csv

import os.path
#from os import walk


script = sys.argv[0]
#logname = script.split('.')[0]
#sys.stdout = open(logname+".log", "w",encoding="utf-8")


xsymbol = 0
xname = 1
xsynonym = 2
xunicode = 3
xxref = 4

def getXrefList(file, outfile):
    print('getXrefList',file)
    fr = open(file, encoding='utf8')
    reader = csv.reader(fr, delimiter=',', quotechar ='"')
    fw = open(outfile, 'w')

    namList = {}

    for row in reader:
        if len(row) > 1:
            ukey = row[3].strip()                   #key = unicode
            nfont = row[0].strip()                  # glyph
            nkey = row[1].strip()                   #nkey = name
            nxref = row[4].strip()                 #nvalue = unicode
            namList[nkey.lower()] = [nfont, nxref, ukey, nkey]

            wr = ' " '+nfont+' "," '+nkey+' "," '+nkey.lower()+' "," '+ukey+' "," '+nxref+' " '
            fw.write(wr+'\n')
              
    fr.close()    
    fw.close()
    #print('namList',namList)
    return namList
    
def basicSymbols(file, outfile):
    print('basicSymbols',file)
    fr = open(file, encoding='utf8')
    reader = csv.reader(fr, delimiter=',', quotechar ='"')
    fw = open(outfile, 'w')

    basicList = {}
    #try:
    for row in reader:
        if len(row) > 1:
            nfont = row[0].strip()                  # glyph
            nkey = row[1].strip()                   #nkey = name
            rsym = row[2].strip()                   # synonymn/ reference key    
            ukey = row[3].strip()                   #key = unicode
            nxref = row[4].strip()                  #xref list
            if len(nxref) > 0:
                continue
            if '(' in rsym:
                continue
            basicList[nkey.lower()] = ukey

            #wr = ' " '+nfont+' "," '+nkey+' "," '+ukey+' " '#," '+rsym+' "," '+str(len(nxref))+' " '
            wr = nfont+","+nkey+","+ukey
            #print(wr)
            fw.write(wr+'\n')
        
    #except:
        
    #    print('error the fields must be separated by "|"') 
    #    print('All fields must be quoted  with " ') 
    #    sys.exit(1)
        
    fr.close()    
    fw.close()
    #print('namList',namList)
    return basicList    
    
    
def priOnly(nList, basicSym):

    with open('mf1.csv', mode='w') as mf:
        #mfw = csv.writer(mf, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        outStr = ' " Font "," Word","Unicode"," Made From(unicode)","Made From(name) " '
        #nList structure
        # key =  [nfont, nxref, ukey]
        mf.write(outStr+'\n')
        print(nList.keys())
        for n in nList:
            pList = ""
            uList = ""
            xList = nList[n][1].split(':')               # xref list
            fnt = nList[n][0]                               # font
            #kwrd = nList[n][0]                            # original  key word keep case

            print(n, xList)
            for c in xList:
                ww = c.split(',')
                
                for w in ww:
                    ws = w.strip()
                    if ws.lower() in basicSym:
                        #if ws.lower() in map(str.lower, nList.keys()):
                        print(ws, ws.lower(), nList[ws.lower()])
                        pList = pList+': '+ws
                        uList = uList+': '+nList[ws.lower()][2]
      
            print(fnt, nList[n][3], pList, uList)
            outStr = ' " '+fnt+' "," '+nList[n][3]+' "," '+nList[n][2]+' "," '+uList.strip(':')+' "," '+pList.strip(':')+' " '.strip()
            mf.write(outStr+'\n')
 
 
if len(sys.argv) > 1: 
    xrefFile = sys.argv[1]
    basicSym = basicSymbols(xrefFile, "basicsymbols.csv")
    nl = getXrefList(xrefFile, "xr1.csv")
    print(nl)
    #priOnly(nl, basicSym)
    
else:
    print("\nsyntax: fontforge -script xref.py")
    print("  creates xref.csv from  existing xref dictionary")
    sys.exit()

print('Done')

    