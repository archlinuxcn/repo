# Maintainer: Zhang Hai <dreaming.in.code.zh@gmail.com>
# Contributor: Star Brilliant <echo bTEzMjUzQGhvdG1haWwuY29tCg== | base64 -d>

_pkgname=danmaku2ass
pkgname="${_pkgname}-git"
pkgver=r214.3dd20e4
pkgrel=1
epoch=1
pkgdesc="Convert comments from Niconico/AcFun/bilibili to ASS format"
arch=('any')
url="https://github.com/m13253/danmaku2ass"
license=('GPL3')
depends=('python>=3')
makedepends=('git')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("${_pkgname}::git+https://github.com/m13253/danmaku2ass.git")
sha256sums=('SKIP')

pkgver() {
  cd "${srcdir}/${_pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "${srcdir}/${_pkgname}"
  make
}

package() {
  cd "${srcdir}/${_pkgname}"
  make install DESTDIR="${pkgdir}" PREFIX='/usr'
}
