# Maintainer : DigitOtter <digitotter@protonmail.com> 
# Contributor: Daniel Bermond <gmail-com: danielbermond>

pkgname=ffnvcodec-headers-12-1
srcname=ffnvcodec-headers
pkgver=12.1.14.0
pkgrel=1
pkgdesc='FFmpeg version of headers required to interface with Nvidias codec APIs Version 12.1 (for obs-studio-git)'
provides=('ffnvcodec-headers')
conflicts=('ffnvcodec-headers')
arch=(any)
url=https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
license=(MIT)
makedepends=(git)
_tag="n12.1.14.0"
source=("${srcname}::git+https://git.videolan.org/git/ffmpeg/nv-codec-headers.git#tag=${_tag}")
sha256sums=(SKIP)

pkgver() {
  cd "${srcname}"
  git describe --tags | sed 's/^n//'
}

prepare() {
  cd "${srcname}"

  # license
  sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE  # create file
  sed -i '1,22s/^.\{,3\}//' LICENSE # erase C comments
}

build() {
  cd "${srcname}"
  make PREFIX='/usr'
}

package() {
  cd "${srcname}"
  make PREFIX='/usr' DESTDIR="${pkgdir}" install
  install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

# vim: ts=2 sw=2 et:
