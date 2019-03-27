# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Copyright (C) 2019 Nicolàs Palacio-Escat
Contact: nicolas.palacio@bioquant.uni-heidelberg.de

The following script walks down the subdirectories of the current folder
and creates a README.md file inside each one of them containing a
preview of all the graphics in that subfolder.

This way I don't have to bother myself to do it manually every time I
add/remove/modify one or more of them. Neat right!?
'''

import os

for sdir, folders, files in os.walk('.'):

    if (sdir == '.' or sdir == './.git'):
        continue

    else:
        images = sorted([f for f in files if f.endswith('.svg')])

        with open(os.path.join(sdir, 'README.md'), 'w') as rdm:
            rdm.write('# %s\n\n' % sdir.split('/')[-1])

            for i in images:
                rdm.write('## %s\n' % i.split('.')[0])
                rdm.write('<img src="%s" height="150"/>\n\n' % i)
