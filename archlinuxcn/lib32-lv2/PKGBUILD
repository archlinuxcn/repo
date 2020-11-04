# Mantainer: Lorenzo Ferrillo <lorenzofer@live.it>
# Contributor: Ray Rashif <schiv@archlinux.org>

_basename=lv2
pkgname=lib32-${_basename}
pkgver=1.18.0
pkgrel=1
pkgdesc="Successor to the LADSPA audio plug-in standard"
url="http://lv2plug.in/"
license=('LGPL' 'custom')
arch=('x86_64')
depends=('lv2')
makedepends=('python' 'waf' 'lib32-libsndfile' 'lib32-gtk2')
optdepends=('lib32-libsndfile: Example sampler'
            'lib32-gtk2: Example sampler'
            )
provides=('lib32-lv2core')
conflicts=('lib32-lv2core')
replaces=('lib32-lv2core')

source=("http://lv2plug.in/spec/$_basename-$pkgver.tar.bz2")
sha512sums=('9e8dd9c1f30371260d21efc105b1d4d4ad03d9e332d4d3877d873f20b9527bcd0e917ff23fc6e0a9cc4337bda85882c742f225f7cf4fbc8a8a0964565c91f9d9')

build() {
  cd "$srcdir/$_basename-$pkgver"
  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
    
  # let wscript(s) find the custom waf scripts
  mkdir -pv tools
  touch __init__.py
  cp -v waflib/extras/{autowaf,lv2}.py tools/
  mkdir -pv plugins/tools/
  cp -v waflib/extras/{autowaf,lv2}.py plugins/tools/
  rm -rv waflib
  sed -e 's/waflib.extras/tools/g' \
      -e "s/load('autowaf'/load('autowaf', tooldir='tools'/g" \
      -e "s/load('lv2'/load('lv2', tooldir='tools'/g" \
      -i {,plugins/,plugins/*/}wscript

   # --docs is currently broken: https://gitlab.com/lv2/lv2/issues/28
  waf -vv configure --prefix=/usr \
                --libdir=/usr/lib32 \
                --test
  waf -vv build
}



check() {
  cd "$srcdir/$_basename-$pkgver"
  waf test
}

package() {
  cd "$srcdir/$_basename-$pkgver"
#REMOVE includes and others
  waf install --destdir="$pkgdir"
  rm ${pkgdir}/usr/bin ${pkgdir}/usr/include ${pkgdir}/usr/share -Rf
}

# vim:set ts=2 sw=2 et:
 
