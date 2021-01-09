echo on
rem generate svg images from the sfd file
rem puts the 
set sfdin=sun7_8_1210.sfd

echo on
fontforge -quiet -script font2svg.py %sfdin% 
