# Contributor: John Regan <john@jrjrtech.com>
pkgname=libvgm-git
pkgver=r578.798cb20
pkgrel=2
pkgdesc="Library for decoding and playing VGM files"
arch=(x86_64 i686)
url="https://github.com/ValleyBell/libvgm"
# https://github.com/ValleyBell/libvgm/issues/129
license=('LicenseRef-Unknown')
provides=('libvgm')
conflicts=('libvgm')
replaces=('libvgm-player-git' 'libvgm-emu-git' 'libvgm-utils-git' 'libvgm-audio-git' 'libvgm-common-git'
          'vgm2wav-git' 'vgmplayer-git')
conflicts+=("${replaces[@]}")
provides+=("${replaces[@]}")
depends=('gcc-libs' 'glibc' 'zlib' 'alsa-lib' 'libpulse' 'libao')
makedepends=('git' 'cmake')

source=('git+https://github.com/ValleyBell/libvgm.git'
        '0001-rename-player-to-vgmplayer.diff')
md5sums=('SKIP'
         '5cbf065cbb21468139a4eb8b87dd1d88')

pkgver() {
	cd "$srcdir/${pkgbase%-git}"

	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
    cd "$srcdir/libvgm"
    patch -Np1 -i ../0001-rename-player-to-vgmplayer.diff
}

build() {
    cmake -B build -S "$srcdir/libvgm" \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_SKIP_BUILD_RPATH=ON \
        -DLIBRARY_TYPE=SHARED 
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
