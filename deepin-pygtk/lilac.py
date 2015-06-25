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
  download_official_pkgbuild('pygtk')
  create_patch()

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'pkgname=pygtk' in line:
        print('pkgname=deepin-pygtk')
        print('_'+line)
    elif 'pkgdesc' in line:
        print('pkgdesc="Python bindings for the GTK widget set - with patches to fix memory leak for deepin-ui"')
    elif 'optdepends=' in line:
        print('provides=("pygtk=$pkgver")')
        print('conflicts=("pygtk")')
    elif 'source=' in line:
        print(line.replace("${pkgname}","$_pkgname"))
        print('        10_fix_create_layout_unref.patch')
    elif 'sha256sums=' in line:
        print(line)
        print("            '283836d6fe8eda2a1bd32f551b2677e1b9e6e3cee8e48e6c4b861375810d8712'")
    elif 'patch -Np1 -i' in line:
        print(line)
        print("  patch -Np1 -i \"${srcdir}/10_fix_create_layout_unref.patch\"")
    elif 'cd "${srcdir}/${pkgname}-${pkgver}"' in line:
        print(line.replace("${pkgname}","$_pkgname"))
    else:
        print(line)

def post_build():
  # do something after the package has successfully been built
  aur_post_build()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
  single_main()
