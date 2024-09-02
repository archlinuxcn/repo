# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>

pkgname="hevi"
pkgver=1.1.0
pkgrel=1
pkgdesc="A modern hex viewer"
arch=('x86_64')
url="https://arnau478.github.io/${pkgname}"
_url="https://github.com/Arnau478/${pkgname}"
license=('GPL-3.0-or-later')
makedepends=('zig')
_pkgsrc="${pkgname}-${pkgver}"
source=("${_pkgsrc}.tar.gz::${_url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('d1c444301c65910b171541f1e3d1445cc3ff003dfc8218b976982f80bccd9ee0')

build() {
  cd "${srcdir}/${_pkgsrc}"
  zig build
}

check() {
  cd "${srcdir}/${_pkgsrc}"
  zig build test
}

package() {
  cd "${srcdir}/${_pkgsrc}"
  install -Dm755 "zig-out/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -Dm644 "LICENSE"   "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  cd "doc"
  install -Dm644 "${pkgname}.1.man" "${pkgdir}/usr/share/man/man1/${pkgname}"
  install -Dm644 "${pkgname}.5.man" "${pkgdir}/usr/share/man/man5/${pkgname}"
}
