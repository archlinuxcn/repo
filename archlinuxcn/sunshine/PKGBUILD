pkgname=sunshine
pkgver=0.22.0
pkgrel=3
pkgdesc="A self-hosted GameStream host for Moonlight."
arch=('x86_64' 'aarch64')
url=https://app.lizardbyte.dev
license=('GPL3')
install=sunshine.install

depends=('avahi'
         'boost-libs'
         'curl'
         'libayatana-appindicator'
         'libevdev'
         'libmfx'
         'libnotify'
         'libpulse'
         'libva'
         'libvdpau'
         'libx11'
         'libxcb'
         'libxfixes'
         'libxrandr'
         'libxtst'
         'miniupnpc'
         'numactl'
         'openssl'
         'opus'
         'udev')
makedepends=('boost'
             'cmake'
             'git'
             'make'
             'nodejs'
             'npm')
optdepends=('cuda: NvFBC capture support'
            'libcap'
            'libdrm')

provides=()
conflicts=()

source=("$pkgname::git+https://github.com/LizardByte/Sunshine.git#tag=v${pkgver}")
sha256sums=('SKIP')

prepare() {
    cd "$pkgname"
    git submodule update --recursive --init
}

build() {
    export BRANCH="master"
    export BUILD_VERSION="${pkgver}"
    export COMMIT="$(git rev-parse HEAD)"

    export CFLAGS="${CFLAGS/-Werror=format-security/}"
    export CXXFLAGS="${CXXFLAGS/-Werror=format-security/}"

    cmake \
        -S "$pkgname" \
        -B build \
        -Wno-dev \
        -D BUILD_WERROR=ON \
        -D CMAKE_INSTALL_PREFIX=/usr \
        -D SUNSHINE_EXECUTABLE_PATH=/usr/bin/sunshine \
        -D SUNSHINE_ASSETS_DIR="share/sunshine"

    make -C build
}

package() {
    make -C build install DESTDIR="$pkgdir"
}
