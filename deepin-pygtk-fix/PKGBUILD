# Maintainer: Xu Fasheng <fasheng.xu@gmail.com>

pkgname=deepin-pygtk-fix
_pkgname=pygtk
pkgver=2.24.0
pkgrel=3
pkgdesc="Python bindings for the GTK widget set - with patches to fix memory leak for deepin-ui"
arch=('i686' 'x86_64')
license=('LGPL')
depends=('libglade' 'python2-cairo' 'pygobject')
optdepends=('python2-numpy')
url="http://www.pygtk.org/"
pkgsite="http://packages.linuxdeepin.com"
# pkgsite="http://mirrors.ustc.edu.cn"
patchfile=pygtk_${pkgver}-3deepin3.debian.tar.gz
source=(${pkgsite}/deepin/pool/main/p/pygtk/pygtk_2.24.0.orig.tar.gz
        python27.patch
        ${pkgsite}/deepin/pool/main/p/pygtk/${patchfile})
md5sums=('d27c7f245a9e027f6b6cd9acb7468e36'
         '12acfacd26f19c504a0a2d0edeb66121'
         '9e513bdf36ba873030182d9d5092d08b')
provides=('pygtk=2.24.0')
conflicts=('pygtk')

build() {
    #unzip patches
    cd "$srcdir/"
    tar -xf ${patchfile}
    
    cd "${_pkgname}-${pkgver}"

    #apply python27 patch
    #https://bugzilla.gnome.org/show_bug.cgi?id=623965
    patch -Np1 -i "${srcdir}/python27.patch"
    
    #apply deepin patches
    patchdir=${srcdir}/debian/patches
    for f in `cat ${patchdir}/series`; do
        echo "==> patching: ${f##*/}"
        # ignore error if patch again
        patch -Np1 -i ${patchdir}/${f} || echo '==> patch error: ${f##*/}'
    done
    
    PYTHON=/usr/bin/python2 ./configure --prefix=/usr
    make
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  install -m644 gtk/gtk-extrafuncs.defs "${pkgdir}/usr/share/pygtk/2.0/defs/"

  sed -i -e 's#env python$#env python2#' "${pkgdir}"/usr/lib/pygtk/2.0/{,demos/}*.py
}
