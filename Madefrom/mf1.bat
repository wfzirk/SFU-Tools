echo off
rem containing with primary list 
rem set primary="pw7251.csv"
rem containing xref
set xref=synxref78_1210_0103.csv
set outfile=mf.csv

rem print("\nsyntax: fontforge -script mergexref.py Masterfile.csv xreffile.csv outfile.csv")
rem print("   merges xref with  existing dictionary")
echo on
fontforge -quiet -script mf1.py %xref% 