
rem containing with primary list 
rem set primary="pw7251.csv"
rem containing xref
set xrefin=synxref78_1210_0107.csv
set outfile=xref.csv

rem print("\nsyntax: fontforge -script mergexref.py Masterfile.csv xreffile.csv outfile.csv")
rem print("   merges xref with  existing dictionary")

fontforge -quiet -script xref.py %xrefin% 