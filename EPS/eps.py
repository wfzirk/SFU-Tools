'''
export_glyph.py

fontforge -script eps.py "Sun6_0 Font.sfd" ebcd ebda eps

'''

print('usage ', 'fontforge -script eps.py sfd file unicode-range ebcd ebda type') 
print(' i.e. ', 'fontforge -script eps.py "Sun6_0 Font.sfd" ebcd ebda eps >eps.txt') 
import fontforge
import sys

try:
	fontfile = sys.argv[1]
	hex_str = "0x"+sys.argv[2]
	int1 = int(hex_str, 16)
	hex_str = "0x"+sys.argv[3]
	int2 = int(hex_str, 16)
	ext = sys.argv[4]
	font = fontforge.open (fontfile)
except EnvironmentError:
    sys.exit (1)
	

for glyph in font:
	unicode = font[glyph].unicode
	if unicode >= int1 and unicode <= int2:
		name = font[glyph].glyphname
		filename = 'eps\\'+name + '.' + ext
		font[name].export(filename)
		print (hex(unicode), filename)

print ('done')

