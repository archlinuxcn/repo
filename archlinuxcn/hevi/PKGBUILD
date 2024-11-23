# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>

pkgname="hevi"
pkgver=1.1.0
pkgrel=2
pkgdesc="A modern hex viewer"
arch=('x86_64' 'aarch64' 'i686')
url="https://arnau478.github.io/${pkgname}"
_url="https://github.com/Arnau478/${pkgname}"
license=('GPL-3.0-or-later')
makedepends=('zig')
_zig_deps=("ziggy-ae30921d8c98970942d3711553aa66ff907482fe.tar.gz::https://github.com/kristoff-it/ziggy/archive/ae30921d8c98970942d3711553aa66ff907482fe.tar.gz"
           "known-folders-0ad514dcfb7525e32ae349b9acc0a53976f3a9fa.tar.gz::https://github.com/ziglibs/known-folders/archive/0ad514dcfb7525e32ae349b9acc0a53976f3a9fa.tar.gz"
           "zig-lsp-kit-1c07e3e3305f8dd6355735173321c344fc152d3e.tar.gz::https://github.com/MFAshby/zig-lsp-kit/archive/1c07e3e3305f8dd6355735173321c344fc152d3e.tar.gz"
           "zig-yaml-beddd5da24de91d430ca7028b00986f7745b13e9.tar.gz::https://github.com/kubkon/zig-yaml/archive/beddd5da24de91d430ca7028b00986f7745b13e9.tar.gz")
_pkgsrc="${pkgname}-${pkgver}"
source=("${_pkgsrc}.tar.gz::${_url}/archive/refs/tags/v${pkgver}.tar.gz"
        "${_zig_deps[@]}")
noextract=("${_zig_deps[@]}")
sha256sums=('d1c444301c65910b171541f1e3d1445cc3ff003dfc8218b976982f80bccd9ee0'
            'd00b839371b6ea996ed09e9116b55a7bb0acca361a2670d6736a5293f4f315f9'
            'a8457bc9d3ca509a1db8b46a0d402fecae2b17d4fe0f454f5d51a63cc2aa1a7b'
            'eaa00a7f51971d526532251606e11bd6c1acb9ef50745b6e2025b8d0ea8a2e69'
            '21df1918d1d200f376bca70ed1691def41b6380b0d7485dd39ffe186498ecedf')

prepare() {
  cd "${srcdir}/${_pkgsrc}"

  cd "${srcdir}"
  for dep in "${_zig_deps[@]}"; do
    zig fetch --global-cache-dir ./zig-global-cache "${dep%%::*}"
  done
}

build() {
  cd "${srcdir}/${_pkgsrc}"
  DESTDIR="build" zig build \
    --summary all \
    --prefix /usr \
    --search-prefix /usr \
    --global-cache-dir ../zig-global-cache \
    --system ../zig-global-cache/p \
    --verbose \
    -Dtarget=native-linux.6.1-gnu.2.38 \
    -Dpie \
    -Doptimize=ReleaseSafe
}

check() {
  cd "${srcdir}/${_pkgsrc}"
  DESTDIR="build" zig build test \
    --summary all \
    --prefix /usr \
    --search-prefix /usr \
    --global-cache-dir ../zig-global-cache \
    --system ../zig-global-cache/p \
    --verbose \
    -Dtarget=native-linux.6.1-gnu.2.38 \
    -Dpie \
    -Doptimize=ReleaseSafe
}

package() {
  cd "${srcdir}/${_pkgsrc}"
  cp -va build/* "${pkgdir}"

  install -vDm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -vDm644 "LICENSE"   "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  cd "doc"
  install -vDm644 "${pkgname}.1.man" "${pkgdir}/usr/share/man/man1/${pkgname}.1"
  install -vDm644 "${pkgname}.5.man" "${pkgdir}/usr/share/man/man5/${pkgname}.5"
}
