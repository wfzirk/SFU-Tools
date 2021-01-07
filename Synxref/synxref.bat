
set primary=pw7_8_1210_EN.csv
set xrefin=synxref78_909_1206.csv
set kmn="kmn7_8_1210_EN.csv"
set outfile=synxref78_1210.csv

pause besure %kmn% is sorted by unicode

cmd /c fontforge -quiet -script xref.py %xrefin%
::cmd /c fontforge -quiet -script verseref.py %kmn%

:syn
cmd /c fontforge -quiet -script synonyms.py %kmn%

cmd /c fontforge -script synxref.py %primary% xref.csv syn.csv  %outfile%
:end