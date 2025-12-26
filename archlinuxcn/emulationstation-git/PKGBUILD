# Maintainer: Lubosz Sarnecki <lubosz at gmail dot com>
# Contributor : Johnathan Jenkins <twodopeshaggy@gmail.com>
# Contributor: Drew Liszewski <drew dot liszewski at gmail dot com>
# Contributor: Daniel Varga <varga dot daniel at gmx dot de>

pkgname=emulationstation-git
pkgrel=1
epoch=1
pkgver=2.4.1.r866.ga72ca013
pkgdesc="Flexible emulator front-end supporting keyboardless navigation and custom system themes. Active fork by the RetroPie project."
arch=(x86_64 i686 armv6h armv7h)
url="https://github.com/RetroPie/EmulationStation"
license=(MIT)
depends=(freeimage libvlc curl pugixml freetype2 sdl2 alsa-lib glibc gcc-libs libglvnd)
makedepends=(git cmake rapidjson)
provides=(emulationstation)
conflicts=(emulationstation)
source=('git+https://github.com/RetroPie/EmulationStation.git')
sha256sums=('SKIP')

pkgver() {
  cd EmulationStation
  git describe --long | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  local _flags=(

  )

  cmake -B build -S "EmulationStation" -Wno-dev \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    "${_flags[@]}"

  cmake --build build
}

package() {
    cd EmulationStation
    # No install target..., should be fixed upstream
    # make DESTDIR="$pkgdir" install
    install -Dm755 "emulationstation" -t "${pkgdir}/usr/bin/"
    install -Dm644 "LICENSE.md" -t "$pkgdir/usr/share/licenses/${pkgname}/"
}
