#!/usr/bin/env python3
"""
Détaille le poids total des fichiers et dossiers d'un répertoire

License Libre
rod.cat@free.fr
"""
import sys
from os import listdir, system, chdir

try:
    chdir(sys.argv[1])
except IndexError:
    pass
except PermissionError:
    print("\x1b[1;31mVous n'avez pas les droits sur ce répertoire.\x1b[0m")
    quit()
except FileNotFoundError:
    print("\x1b[1;31mCe répertoire semble ne pas exister.\x1b[0m")
    quit()
except NotADirectoryError:
    print("\x1b[1;31mCe fichier n'est pas un répertoire.\x1b[0m")
    quit()

test = system('touch poids_fichiers')
if test:
    print("\x1b[1;31mVous n'avez pas les droits sur ce répertoire.\x1b[0m")
    quit()

def str2float(poids_str):
    if ',' in poids_str:
        ps = poids_str.split(',')
        ps = ps[0] + '.' + ps[1]
    else:
        ps = poids_str
    return(float(ps))

def unit_strip(str_tp):
    poids = str2float(str_tp[0][:-1])
    unit = str_tp[0][-1]
    if unit == 'K':
        return(poids)
    elif unit == 'M':
        return(poids*1024)
    elif unit == 'G':
        return(poids*1024**2)
    else:
        return(poids*1024**3)

def set_unit(poids):
    if poids < 1024:
        return('\x1b[1;34m{}K\x1b[0m'.format(str(poids)))
    elif poids < 1024**2:
        return('\x1b[1;32m{}M\x1b[0m'.format(str(poids//1024)))
    elif poids < 1024**3:
        return('\x1b[1;33m{}G\x1b[0m'.format(str(poids//1024**2)))
    else:
        return('\x1b[1;31m{}T\x1b[0m'.format(str(poids//1024**3)))
    
contenu_du_rep = listdir()        
for fichier in contenu_du_rep:
    if fichier[0].isdigit():
        pass
    else:
        system('du "{}" | tail -n 1 >> poids_fichiers'.format(fichier))

liste_fichiers = []
with open('poids_fichiers') as pf:
    for line in pf:
        str_tp = line.split('\t',1)
        if str_tp[0].isdigit():
            int_tp = int(str_tp[0]), str_tp[1]
        else:
            int_tp = unit_stip(str_tp)
        
        if int_tp[1][-1:] == '\n':
            int_tp = int_tp[0], int_tp[1][:-1]
        liste_fichiers.append(int_tp)

liste_fichiers = sorted(liste_fichiers)
total = 0
for e in liste_fichiers:
    poids = e[0]
    total += poids
    print(set_unit(poids), e[1])
print('Total:', set_unit(total))
system('rm poids_fichiers')


