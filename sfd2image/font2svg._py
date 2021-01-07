#  https://tex.stackexchange.com/questions/298063/convert-latex-symbols-into-svg-files-using-font-files-directly
#!/usr/bin/env python
import argparse
import fontforge

def parse_command_line_options():
    parser = argparse.ArgumentParser(
        description='Export font glyphs as SVG files via fontforge.')
    parser.add_argument(
        'font_file_name',
        metavar='FONT',
        help='SFD file name')
    return parser.parse_args()
    
def generate_file_name(glyph):
    sep = '-'
    # Font name
    file_name = glyph.font.fontname
    file_name += sep
    # Unicode or encoding number
    if glyph.unicode >= 0:
        file_name += 'U+' + format(glyph.unicode, '04X')
        file_name += sep
    elif glyph.encoding >= 0:
        file_name += '0x' + format(glyph.encoding, '02X')
        file_name += sep
    # Glyph name
    file_name += glyph.glyphname
    # Extension
    file_name += '.svg'
    return file_name

def export_glyphs(font_file_name):
    font = fontforge.open(font_file_name)
    glyphs = font.selection.byGlyphs.all()
    for glyph in glyphs:
        #svg_file_name = generate_file_name(glyph)
        if glyph.isWorthOutputting:
            if glyph.unicode > 57343:
                svg_file_name = 'svg/'+format(glyph.unicode, '04X')+'.svg'
                sf = svg_file_name.lower()
                glyph.export(sf, usetransform=True)
                print(sf, glyph.glyphname, glyph.unicode)
            
            
            
            
def main():
    args = parse_command_line_options()
    export_glyphs(args.font_file_name)

if __name__ == "__main__":
    main()