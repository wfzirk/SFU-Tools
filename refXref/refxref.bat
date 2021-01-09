
set primary=pw7_8_1210_EN.csv
set xrefin=synxref78_1210_0107.csv
set kmn=kmn7_8_1210_EN.csv
set outfile=xref78_1210_0107.csv

pause besure %kmn% is sorted by unicode

::cmd /c fontforge -quiet -script xref.py %xref% 

::cmd /c fontforge -quiet -script ref.py %kmn%

cmd /c fontforge -script refxref.py %primary% ref.csv xref.csv %outfile%
