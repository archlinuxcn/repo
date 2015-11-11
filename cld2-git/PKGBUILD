# Maintainer: lilydjwg <lilydjwg@gmail.com>

_pkgname=cld2
pkgname=${_pkgname}-git
pkgver=20150820
pkgrel=1
pkgdesc='Compact Language Detector 2'
arch=('x86_64')
url='https://github.com/CLD2Owners/cld2'
license=('Apache')
provides=('cld2' 'cld2-hg' 'cld2-svn')
replaces=('cld2-hg' 'cld2-svn')
conflicts=('cld2-hg' 'cld2' 'cld2-svn')
makedepends=('git')
source=('git+https://github.com/CLD2Owners/cld2.git')
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  git log -1 --pretty='%cd' --date=short | tr -d '-'
}

build() {
  cd "$srcdir/$_pkgname"
  cd internal
  sh ./compile_libs.sh
}

package() {
  cd "$srcdir/$_pkgname"
  install -Dm755 internal/libcld2.so "${pkgdir}/usr/lib/libcld2.so"
  install -Dm755 internal/libcld2_full.so "${pkgdir}/usr/lib/libcld2_full.so"

  for header in internal/*.h public/*.h; do
    install -Dm644 "$header" "${pkgdir}/usr/include/cld2/$header"
  done

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

