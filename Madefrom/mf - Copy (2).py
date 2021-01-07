
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
            
            #wr = ' " '+nfont+' "," '+nkey+' "," '+nkey.lower()+' "," '+ukey+' "," '+nxref+' " '
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
    
def xgetUnicode(str):

    '''
    unicode = hex(font[glyph].unicode)[2:]
    uic = getUnicode(unicode)
    '''
    try:
        a = chr(int(str,16)).encode('utf-8')
        return a.decode('utf-8')
    except Exception as  e:
        logger.error("fatal error getUnicode %s",e)
        return 1   
    
    
    
def getUnicode(ustr):
    '''
    unicode = hex(font[glyph].unicode)[2:]
    uic = getUnicode(unicode)
    '''
    uint = int(ustr, 16)
    print('getunicode', type(ustr), ustr)
    print('uint',type(uint), uint)
    
    byte_string = ustr.encode('utf-8')
    print('bytestr',byte_string)
    
    unicode_text = byte_string.decode('utf-8')
    print('unicodetext',unicode_text)
    hint = hex(uint)
    print('hint',type(hint), hint)
    
    #unicode = hex(font[glyph].unicode)[2:]
    unicode = hex(hint.unicode)[2:]
    print('getunicode',hint, unicode)
    
    
    #a = unicode.encode('utf-8')
    #print(a, a.decode('utf-8'))
    #return a.decode('utf-8')

    
def madeFrom(nList, basicSym):
    # 'zuzites': ['\ueef7', 'Zuzites', 'eef7', 'Argument: mouth,said,speak,confession: wild: no,not: peace: sleep,rest,lie_down: love,compassion: people']
    mfList = []
    with open('madefrom.csv', mode='w') as mf:
        #outStr = 'Font','Word','Unicode','Made From unicode'
        outStr = 'Font ,Word,Unicode,Made From unicode'
        mf.write(str(outStr)+'\n')
        
        for n in nList:
            print('n',nList[n])
            xList = nList[n][3].replace(":",", ").replace('"',' ')  #.replace("  "," ")           # xref list
            
            fnt = nList[n][0]
            
            
            
            #fnt = getUnicode(nList[n][2])         # font
            name = nList[n][1]            # original  key word keep case
            ucode = nList[n][2]
            #fnt = ucode.encode('utf-8')
            mfRow = []
            mfRow.append(fnt)
            mfRow.append(name)
            mfRow.append(ucode)

            ccs= xList.split(',')
            pList = ""
            uList = ""
            for cc in ccs:
                c = cc.replace("'"," ").replace(' ','').strip()
                #print('c',c)
                if c.lower() in basicSym:
                    #print('c |'+c+'|', basicSym[c.lower()])
                    mfRow.append(basicSym[c.lower()])
                    uList = uList+'", "'+basicSym[c.lower()]
                    #pList = pList+','+c
            print('ulist',uList)
            outStr = ' "'+fnt+'","'+name+'","'+ucode+'",'+uList[3:]+'"'.strip()
            #outStr = fnt, name,ucode, uList, pList
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

    