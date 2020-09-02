'''
export_glyph.py

fontforge -script eps.py "Sun6_0 Font.sfd" ebcd ebda eps

'''

print('usage ', 'fontforge -script export_eps.py "Sun6_0 Font.sfd" ebcd ebda eps') 
import fontforge
import sys




try:
    fontfile = sys.argv[1]
    hex_str = "0x"+sys.argv[2]
    int1 = int(hex_str, 16)
    hex_str = "0x"+sys.argv[3]
    int2 = int(hex_str, 16)
    ext = sys.argv[4]
    font = fontforge.open(fontfile)
    #font = fontforge.open (fontName)
    print(fontfile, int1, int2, ext)
except Esception as e:
    print('Exception',e)
    #sys.exit (1)
	
print('glyphs')
for glyph in font:
    unicode = font[glyph].unicode
    print(unicode, int1, int2)
    if unicode >= int1 and unicode <= int2:
        name = font[glyph].glyphname
        filename = name + '.' + ext
        font[name].export(filename)
        print (hex(unicode), filename)

print ('done')

