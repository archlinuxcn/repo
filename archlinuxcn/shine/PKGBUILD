# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>
# Contributor: Dmitry Kharitonov <arch[at]nano-model[dot]com>
# Contributor: Matthias Grosser <mtgrosser at gmx dot net>
# Contributor: Leonard de Ruijter <leonard@aur.archlinux.org>

pkgname="shine"
_commit_rel="97f188efc3dc90315b79a2af1f477c0c18d85e82" # 3.1.1
_commit="ab5e3526b64af1a2eaa43aa6f441a7312e013519" # r59
pkgver="3.1.1+r59+g${_commit::7}"
pkgrel=2
pkgdesc="Super fast fixed-point MP3 encoder"
arch=('aarch64' 'i686' 'x86_64')
url="https://github.com/savonet/${pkgname}"
license=('LGPL-2.0-only')
depends=('glibc')
provides=("lib${pkgname}.so")
_pkgsrc="${pkgname}-${_commit}"
source=("${_pkgsrc}.tar.gz::${url}/archive/${_commit}.tar.gz")
sha256sums=('2c2f7e41c7c0f67079eb3882233cdc97e3d583e1985b558d4e847bd46285fbde')

prepare() {
  cd "${srcdir}/${_pkgsrc}"
  sed -i 's/-O2//g' 'Makefile.am'
}

build() {
  cd "${srcdir}/${_pkgsrc}"
  # ./bootstrap
  libtoolize
  autoreconf -vfi
  ./configure \
    --prefix='/usr'
  make all
}

package() {
  cd "${srcdir}/${_pkgsrc}"
  make DESTDIR="${pkgdir}" install

  install -vDm644 "ChangeLog" "${pkgdir}/usr/share/doc/${pkgname}/CHANGELOG" 
  install -vDm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md" 
  install -vDm644 "COPYING"   "${pkgdir}/usr/share/licenses/${pkgname}/COPYING" 
}

