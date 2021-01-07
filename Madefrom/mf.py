
#import fontforge
import sys
import csv

import os.path



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
    fr = open(file, 'r', encoding='utf8')
    reader = csv.reader(fr, delimiter=',', quotechar ='"')
    fw = open(outfile, 'w')

    namList = {}

    for row in reader:
        if len(row) > 1:
            ukey = row[3].strip()                  #key = unicode
            nfont = row[0]                         # glyph
            nkey = row[1].strip()                  #nkey = name
            nxref = row[4].strip()                 #nvalue = unicode
            namList[nkey.lower()] = [nfont, nkey, ukey, nxref]

            wr = nfont+","+nkey+","+ukey+","+nxref
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

    fr.close()    
    fw.close()

    return basicList    

    
def madeFrom(nList, basicSym):
    # 'zuzites': ['\ueef7', 'Zuzites', 'eef7', 'Argument: mouth,said,speak,confession: wild: no,not: peace: sleep,rest,lie_down: love,compassion: people']
    mfList = []
    bsList = {}
    #for c in basicSym:
    #    bsList[c.lower] = basicSym[c]
        
    with open('madefrom.csv', mode='w') as mf:
        outStr = 'Font ,Word,Unicode,Made From unicode'
        mf.write(str(outStr)+'\n')
        
        for n in nList:
            #print('n',nList[n])
            xList = nList[n][3].replace(":",", ").replace('"',' ')  #.replace("  "," ")           # xref list
            
            fnt = nList[n][0].strip()
            name = nList[n][1].strip()            # original  key word keep case
            ucode = nList[n][2].strip()
            if name in basicSym:
                continue
                
            mfRow = []
            mfRow.append(fnt)
            mfRow.append(name)
            mfRow.append(ucode)

            ccs= xList.split(',')
            pList = ""
            uList = ""
            for cc in ccs:
                c = cc.replace("'"," ").replace(' ','').strip()
                if c.lower() in basicSym:
                    mfRow.append(basicSym[c.lower()])
                    uList = uList+'", "'+basicSym[c.lower()]
                    #pList = pList+','+c
            print(len(uList), uList)
            if len(uList) > 0:
                outStr = ' "'+fnt+'","'+name+'","'+ucode+'",'+uList[3:]+'"'.strip()
            else:
                outStr = ' "'+fnt+'","'+name+'","'+ucode+'"'.strip()

            print('outstr',outStr) 
            mf.write(outStr+'\n')
 
 
if len(sys.argv) > 1: 
    xrefFile = sys.argv[1]
    basicSym = basicSymbols(xrefFile, "basicsymbols.csv")
    nl = getXrefList(xrefFile, "xref.csv")
    #print(nl)
    #print(basicSym["man"])
    madeFrom(nl, basicSym)
    
else:
    print("\nsyntax: fontforge -script xref.py")
    print("  creates xref.csv from  existing xref dictionary")
    sys.exit()

print('Done')

    