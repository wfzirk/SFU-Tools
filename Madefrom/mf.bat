echo off
rem containing with primary list 
rem set primary="pw7251.csv"
rem containing xref
set xref=xref78_1210_0107.csv
set outfile=mf78_1210_0107.csv

rem print("\nsyntax: fontforge -script mergexref.py Masterfile.csv xreffile.csv outfile.csv")
rem print("   merges xref with  existing dictionary")
echo on
fontforge -quiet -script mf.py %xref% %outfile%