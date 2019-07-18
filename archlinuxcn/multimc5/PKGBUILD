# Maintainer: xiretza <xiretza+aur@gmail.com>
# Contributor: vorpalblade77@gmail.com
# Contributor: b.klettbach@gmail.com

pkgname=multimc5
pkgver=0.6.6
pkgrel=1
__pkgver_libnbtplusplus=multimc-0.6.1
__pkgver_quazip=multimc-3
pkgdesc="Minecraft launcher with ability to manage multiple instances."
arch=('i686' 'x86_64')
url="http://multimc.org/"
license=('Apache')
depends=('zlib' 'libgl' 'qt5-base' 'qt5-x11extras' 'java-runtime<12' 'qt5-svg' 'xorg-xrandr')
provides=('multimc')
conflicts=('multimc')
makedepends=('cmake' 'java-environment<12')
optdepends=('mcedit: Allows editing of minecraft worlds')

source=("https://github.com/MultiMC/MultiMC5/archive/${pkgver}.tar.gz"
        "https://github.com/MultiMC/libnbtplusplus/archive/${__pkgver_libnbtplusplus}.tar.gz"
        "https://github.com/MultiMC/quazip/archive/${__pkgver_quazip}.tar.gz"
        "quazip-fix-build-with-qt-511.patch"
)
sha512sums=('b948d18ba48fafae449682a60e47a22d280e2a5f7d5c0b3fae380246c770943f46891bfa36eda9dd875ea02b3bc92161bcfbb3d528173dedb4fd801243e769e0'
            '81a1640a069d88df7ba0abf72089aecbe1e9d791c88acaaa7e70c8f0bcd0512cf8698178342657e363524ce8488dd072368a0aa8cc091a24912d6f8b6b0f4f2d'
            '2e9074203c67bc7ad98621c551047e5367f06e54cacfecc755a5bf2c9f99266eab42ad972f86ae28ed7e1507f6d27d8d2680a87ce9fd5b1e93a18bcb627ec3f0'
            'ca7a350bdeecf65dbca7de8d6912c935c6ba603edcddcd4ffe71d8997e50e4046335dde6d1d7c629d35025073d18be4d112a960d43a8801de979687bc26e46d4')
prepare() {
  cd "${srcdir}/MultiMC5-${pkgver}"

  rmdir "libraries/libnbtplusplus"
  rmdir "libraries/quazip"
  cp --recursive "${srcdir}/libnbtplusplus-${__pkgver_libnbtplusplus}/" \
    "libraries/libnbtplusplus"
  cp --recursive "${srcdir}/quazip-${__pkgver_quazip}/" \
    "libraries/quazip"

  cd "libraries/quazip"
  # https://github.com/MultiMC/quazip/pull/1
  patch -p1 < "${srcdir}/quazip-fix-build-with-qt-511.patch"
}

build() {
  cd "${srcdir}/MultiMC5-${pkgver}"
  mkdir -p build

  cd build
  cmake -DCMAKE_BUILD_TYPE=Release \
	  -DMultiMC_UPDATER=OFF \
	  -DCMAKE_INSTALL_PREFIX="/usr" \
	  -DMultiMC_LAYOUT=lin-system \
	  ..
  make
}

check() {
  cd "${srcdir}/MultiMC5-${pkgver}/build"
  make test
}

package() {
  cd "${srcdir}/MultiMC5-${pkgver}/build"
  make install DESTDIR="${pkgdir}"
  install -D "${srcdir}/MultiMC5-${pkgver}/application/resources/multimc/scalable/multimc.svg" "${pkgdir}/usr/share/pixmaps/multimc.svg"
  install -D "${srcdir}/MultiMC5-${pkgver}/application/package/linux/multimc.desktop" "${pkgdir}/usr/share/applications/multimc.desktop"
  install -D "${srcdir}/MultiMC5-${pkgver}/build/libMultiMC_quazip.so" "${pkgdir}/usr/lib/libMultiMC_quazip.so"
  install -D "${srcdir}/MultiMC5-${pkgver}/build/libMultiMC_nbt++.so" "${pkgdir}/usr/lib/libMultiMC_nbt++.so"
}
