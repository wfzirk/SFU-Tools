#!/usr/bin/env fontforge -lang=py
# http://www.typophile.com/node/81351
# http://fontforge.github.io/scripting.html#Example
# https://fontforge.github.io/python.html
# https://stackoverflow.com/questions/14813583/set-baseline-with-fontforge-scriping
# https://www.reddit.com/r/neography/comments/83ovk7/creating_fonts_with_inkscape_and_fontforge_part10/
# http://designwithfontforge.com/en-US/Importing_Glyphs_from_Other_Programs.html
#https://pelson.github.io/2017/xkcd_font_raster_to_vector_and_basic_font_creation/

import fontforge
import sys
import os

#import os.path
#from os import walk

script = sys.argv[0]
logname = script.split('.')[0]
#sys.stdout = open('Log\\'+logname+".log", "w",encoding="utf-8")

def addFont(font, unicode, imagename):  #, mn, mx) :
    file = imagename
    exists = os.path.isfile(file)
    if exists:
        print('addFont file', file, unicode)
        if unicode == -1:
            glyph = font.createChar(-1, imagename)
        else:
            glyph = font.createChar(int(unicode, 16))
        glyph.importOutlines(file)  
        glyph.glyphname = imagename

    else:
        print("file ", file, " does not exist")
        sys.exit(0)

def createFont(backfont):    #, ver, section):
    #fontname = 'SUNBF'+ver+'_'+section
    f = backfont.split('.')
    fontname = f[0]
    ascent = 1000
    descent = 800
    em = 1000
    encoding = "Custom"
    weight = "Regular"
    font = fontforge.font()
    font.fontname = fontname
    font.familyname = fontname
    font.fullname = fontname
    font.ascent = ascent
    font.descent = descent
    font.em = em
    font.encoding = encoding
    font.weight = weight
    font.save(backfont)

    return font

def openFont():
  font = fontforge.open(fontname)
  return font

def genFont(fnt):
    font.generate(fnt) 

def read_list(font, txtFile, namelist=""):
    print('read_list',txtFile)
    f =  open(txtFile, "r")

    for line in f:
        #0xe021 eps\choose.103.eps
        l = line.rstrip("\n").split(' ')
        
        if len(l) < 2:
            continue
        unicode = l[0].replace('0x','').strip().lower()
        name = l[1].strip()
        #print('unu',unicode, name, namelist, unicode in namelist)
        if namelist:
            if unicode not in namelist:
                continue
        addFont(font, unicode, name)   #, float(mn), float(mx))

    f.close()
    
x = 0      
for arg in sys.argv:
    print( x,arg)
    x=x+1
print(len(sys.argv))
if len(sys.argv) > 2: 
    txtFile = sys.argv[1]
    fontname = sys.argv[2]
    font = createFont(fontname)     #, ver, section)
    
    if len(sys.argv) > 3:
        index = 0
        namelist = ""
        for arg in sys.argv:
            print(index, arg)
            if index > 2:
                print(index, arg)
                nl = arg.strip().lower()
                print(nl)
                namelist = namelist+'+'+nl
            index += 1
        print('namelist =',namelist)     
        #processUnnamedGlyphs(font, m, sct, namelist)
        read_list(font, txtFile, namelist)
    else:
        print('whole thing')
        read_list(font, txtFile, "")
    
    font.save(fontname)
    #genFont(fnt[0]+".ttf")
    
else:
    print("\nsyntax: fontforge -script svg2Font.py backFont.sfd csvfile fontfile  Language [unicode list]")
    print("   Creates a back font from the svg files in /svg directory")
    print("   using the names in the kmn file for font characteristics")
    print("   Optionally limits build to list of unicodes")
    print("   -script Python script file,  Fontforge file  csvfile( The dictionary file)")
    print("   language 2 character i.e. EN")
    print("   optional space separated unicode list i.e. e000 eda5")
    print("   The csv file is expected to have:")
    print("      symbol in column 0, unicode in column 1 english word in column 2 and")
    print("      language words in column 3. \n   Optionally limits build to list of unicodes")
    sys.exit()

print('done saved font',fontname)

    