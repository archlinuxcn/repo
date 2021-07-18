from lilaclib import aur_pre_build, aur_post_build, edit_file

def pre_build():
    aur_pre_build('pnglatex', maintainers=['Phaotee'])
    
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgname='):
            line += '-git'
        print(line)

def post_build():
    aur_post_build()
