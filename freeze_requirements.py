# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 19:13
# @Author  : Howardhh
# @File    : freeze_requirements.py

import os
import sys

def _arg_check():
    if len(sys.argv) == 1:
        print('usage: python '+sys.argv[0]+' <your_target_dir>')
        sys.exit()
    else:
        if os.path.isdir(sys.argv[1]):
            pass
        else:
            print('[error] your_target_dir is invalid.')
            sys.exit()

# Install pipreqs if don't have
def _install_pipreqs():
    _pipreqs = os.popen('pip show pipreqs')
    if not _pipreqs.read().strip():
        os.system('pip install pipreqs')
    else:
        print('[warning] pipreqs is already installed in your environment.')

# Generate requirements.txt in your target directory
def _generate_requirements(path=''):
    os.system('pipreqs '+path+' --force --debug')

if __name__ == '__main__':
    print(sys.argv)
    _arg_check()
    _install_pipreqs()
    _generate_requirements(sys.argv[1])

