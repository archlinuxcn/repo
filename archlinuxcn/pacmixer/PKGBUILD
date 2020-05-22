# Maintainer: Karol "Kenji Takahashi" Woźniak <kenji.sx>

pkgname=pacmixer
pkgver=0.6.3
pkgrel=3
pkgdesc="alsamixer alike for PulseAudio."
arch=('i686' 'x86_64' 'armv7h')
url="https://github.com/KenjiTakahashi/pacmixer"
license=('GPL3')
depends=(
    'ncurses'
    'libpulse'
    'gnustep-base'
)
makedepends=(
    'gcc-objc'
    'gnustep-make'
    'ninja'
)
source=("https://github.com/KenjiTakahashi/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('ad37c17e67994c9a123563092ac841c3')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    ./mk
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    DESTDIR="${pkgdir}" PREFIX="/usr" ./mk install
}
