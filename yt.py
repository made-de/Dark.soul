from os import system,remove
import os
os.system ('clear')
print('''\033[1;31m                                            oOOOOOOOOOOOOOOoo..
                                             ************OOOOOOOOo.
                                           ..oooooooo..    `""OOOOO.
                                       .oOOOOOOOOOOOOOOOOo     OOOOO
                     ..ooOOOOOOo..oooOOOOOOOOOOOOOOOOOOOOOOoooOOOOO`
            .Oo...ooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO``
        .oooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0~~
          \oO0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
           OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoOOOOOOOOOOOOOOO'
          __\OO/`    `OOOOOOOOOOOOOOOOOOOO`OOOOOOOOOOOOO`
            /|\   .oOOooo- `OOOOOOOO     .O`OOOOOOOOOO'
  oO--.        .oOOOO`~    .OOOOO'      QQOOO`OOOOOOOOOo
  +o--o`----QQOOO`~       .OOOOO'                 `OOOOO
                         .OOOO'                  QQQQO`
                       QQQQO`
 ____  __  ____  __  _  _   __
(  __)/ _\(_  _)(  )( \/ ) / _\
 ) _)/    \ )(   )( / \/ \/    \
\\
(__) \_/\_/(__) (__)\_)(_/\_/\_/
''')




file=input('File > ')
openfile=open(file, 'r')
readfile=openfile.read()
openfile.close()
newcode=readfile.replace('eval', 'echo')
outfile=input('Output > ')
newfile=open(outfile, 'w')
newfile.write(newcode)
newfile.close()
system('touch tools.sh')
system( 'bash '+outfile+'> tools.sh')
remove(outfile)
system( 'mv -f tools.sh '+outfile)
print('success decrypt | file save as ' +outfile)
