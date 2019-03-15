# Maintainer: jjacky
# Contributor: Angel Velasquez <angvp@archlinux.org> 
# Contributor: tobias <tobias@archlinux.org>
# Contributor: dibblethewrecker dibblethewrecker.at.jiwe.dot.org

# clear.patch based on patch by rlblaster: https://bbs.archlinux.org/viewtopic.php?id=129302

_pkgname=rxvt-unicode
pkgname=${_pkgname}-better-wheel-scrolling
pkgver=9.22
pkgrel=5
pkgdesc="An unicode enabled rxvt-clone terminal emulator (urxvt) w/ better wheel scrolling (VTE-like) (& no utmp/wtmp support)"
arch=('i686' 'x86_64')
url="http://software.schmorp.de/pkg/rxvt-unicode.html"
license=('GPL')
depends=('rxvt-unicode-terminfo' 'gcc-libs' 'libxft' 'gdk-pixbuf2')
optdepends=('perl: lots of utilities') # 'gtk2-perl: to use the urxvt-tabbed')
provides=($_pkgname)
conflicts=($_pkgname)
source=(http://dist.schmorp.de/rxvt-unicode/${_pkgname}-${pkgver}.tar.bz2 \
        ${_pkgname}.desktop
        clear.patch secondaryWheel.patch)
md5sums=('93782dec27494eb079467dacf6e48185'
         'af8e6ad4cd2d33c26f8df6a838685332'
         'edeed8f00d5917bc002b2e10ba7e900c'
         'c73b3a470a02da0bf19ad6e9b83d0696')
sha1sums=('e575b869782fbfed955f84f48b204ec888d91ba1'
          '9a31b46324c0be44fb97be0828e1ead2311b3f9f'
          'fc77f75bd2d51baa4abef81983dab044d7f498ce'
          'e50503f786deb6d6c2b6b8bcf486bf509c14af71')

prepare() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  patch -p1 -i ../clear.patch
  patch -p1 -i ../secondaryWheel.patch
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  ./configure --prefix=/usr \
    --enable-256-color \
    --enable-font-styles \
    --enable-xim \
    --enable-keepscrolling \
    --enable-selectionscrolling \
    --enable-smart-resize \
    --enable-pixbuf \
    --enable-transparency \
    --disable-utmp \
    --disable-wtmp \
    --enable-lastlog \
    --disable-frills
  make alldoc
  make
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  export TERMINFO=/dev/null
  make DESTDIR="${pkgdir}" install
#  # for utmp/wtmp support
#  chgrp utmp $pkgdir/usr/bin/urxvt
#  chmod g+s $pkgdir/usr/bin/urxvt
# # install the tabbing wrapper ( requires gtk2-perl! )
#  sed -i 's/\"rxvt\"/"urxvt"/' doc/rxvt-tabbed
#  install -Dm 755 doc/rxvt-tabbed "${pkgdir}/usr/bin/urxvt-tabbed"
 # install freedesktop menu
  install -Dm644 ../${_pkgname}.desktop \
    "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
