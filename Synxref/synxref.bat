
set primary=pw77_810_EN.csv
set xrefin=synxref77_702_718.csv
set kmn="kmn77_810_EN.csv"
set outfile=synxref77.810.csv

pause besure %kmn% is sorted by unicode

cmd /c fontforge -quiet -script xref.py %xrefin%
::cmd /c fontforge -quiet -script verseref.py %kmn%

:syn
cmd /c fontforge -quiet -script synonyms.py %kmn%

cmd /c fontforge -script synxref.py %primary% xref.csv syn.csv  %outfile%
:end