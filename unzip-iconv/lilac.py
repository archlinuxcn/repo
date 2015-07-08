#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'

def create_patch():
    f=open('10_fix_create_layout_unref.patch','w')
    f.write("Index: pygtk-2.24.0/pangocairo.override\n")
    f.write("===================================================================\n")
    f.write("--- pygtk-2.24.0.orig/pangocairo.override\t2012-04-14 01:40:59.568703232 +0800\n")
    f.write("+++ pygtk-2.24.0/pangocairo.override\t2012-04-14 01:41:05.792703324 +0800\n")
    f.write("@@ -119,10 +119,15 @@\n")
    f.write(" _wrap_pango_cairo_create_layout(PyGObject *self)\n")
    f.write(" {\n")
    f.write("     PangoLayout *ret;\n")
    f.write("+    PyObject *py_ret;\n")
    f.write(" \n")
    f.write("     ret = pango_cairo_create_layout(PycairoContext_GET(self));\n")
    f.write("     /* pygobject_new handles NULL checking */\n")
    f.write("-    return pygobject_new((GObject *)ret);\n")
    f.write("+    py_ret = pygobject_new((GObject *) ret);\n")
    f.write("+    if (ret) {\n")
    f.write("+\tg_object_unref(ret);\n")
    f.write("+    }\n")
    f.write("+    return py_ret;\n")
    f.write(" }\n")
    f.write(" \n")
    f.write(" static PyObject *\n")
    f.close()

def pre_build():
  # obtain base PKGBUILD, e.g.
  download_official_pkgbuild('unzip')
  #create_patch()

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'pkgname=unzip' in line:
        print('pkgname=unzip-iconv')
        print('_'+line)
    elif 'pkgdesc' in line:
        print('pkgdesc="Unpacks .zip archives such as those made by PKZIP. With iconv patch for -O / -I goodness."')
    elif 'depends=' in line:
        print('provides=(\'unzip\')')
        print('conflicts=(\'unzip\')')
    elif 'source=' in line:
        print(line.replace("${pkgname}","$_pkgname"))
        print('        \'unzip60-alt-iconv-utf8.patch\'')
    elif '${pkgname}' in line:
        print(line.replace("${pkgname}","$_pkgname"))
    elif 'sha1sums=' in line:
        print(line)
        print("          '7cb046b09becd96a3901b8ac35f77741695c4a8a'")
    elif 'patch -i ../crc32.patch' in line:
        print(line)
        print('\tpatch -Np1 -i "${srcdir}"/unzip60-alt-iconv-utf8.patch')
    else:
        print(line)

def post_build():
  # do something after the package has successfully been built
  git_add_files('PKGBUILD')
  git_add_files('unzip60-alt-iconv-utf8.patch')
  git_commit()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
  single_main()
