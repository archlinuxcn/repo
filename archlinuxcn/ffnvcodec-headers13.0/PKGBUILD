# Maintainer: 1F616EMO <root@1f616emo.xyz>
# Contributor: Karl Ludwig Brennan <karlludwigbrennan@outlook.com>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Daniel Bermond <danielbermond@yahoo.com>

pkgname=ffnvcodec-headers13.0
pkgver=13.0.19.1
pkgrel=1
pkgdesc='FFmpeg version of headers required to interface with Nvidias codec APIs (version 13.0)'
arch=(any)
url=https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
license=(MIT)
makedepends=(git)
conflicts=('ffnvcodec-headers')
provides=('ffnvcodec-headers')
source=(git+https://git.videolan.org/git/ffmpeg/nv-codec-headers.git#tag=n${pkgver})
sha256sums=('7016462c5bc737fdb4ac0fce51249447c48be59edfdf0f8bb0c668b357d38da6')

build() {
  make PREFIX=/usr -C nv-codec-headers
  sed -n '4,25p' nv-codec-headers/include/ffnvcodec/nvEncodeAPI.h > LICENSE # Extract license
  sed -i '1,22s/^.\{,3\}//' LICENSE # Delete C comments
}

package() {
  make PREFIX=/usr DESTDIR="${pkgdir}" -C nv-codec-headers install
  install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/ffnvcodec-headers13.0/
}

# vim: ts=2 sw=2 et:
