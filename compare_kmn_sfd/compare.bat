set version=7_8_909
set primary=pw7_8_1210_EN.csv
set kmn=kmn7_8_1210_EN.csv
set out=compare%version%.txt
fontforge -script compare.py %primary% %kmn% %out% 