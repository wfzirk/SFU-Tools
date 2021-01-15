echo off
rem containing with primary list 
rem set primary="pw7251.csv"
rem containing xref
set xrefin=xref78_1210_0114.csv
set outfile=mf78_1210_0114.csv
::set xrefin=xref78_1210_0107.csv
::set outfile=mf78_1210_0107a.csv

rem print("\nsyntax: fontforge -script mf.py xrefin.csv   outfile.csv")
rem print("   converts xref words to hex unicode string")
echo on
fontforge -quiet -script mf.py %xrefin% %outfile%