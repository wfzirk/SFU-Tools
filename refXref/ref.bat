
set kmn="kmn7_8_1210_EN.csv"

rem print("\nsyntax: fontforge -script synonyms.py ")
rem print("   creates "ref.csv" - list of references the kmn file")

fontforge -quiet -script ref.py %kmn%