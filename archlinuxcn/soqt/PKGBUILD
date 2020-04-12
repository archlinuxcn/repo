# Maintainer:  Gabriel Souza Franco <Z2FicmllbGZyYW5jb3NvdXphQGdtYWlsLmNvbQ==>
# Contributor: Florian Pritz
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: mickele
# Contributor: marcus fritzsch <fritschy@googlemail.com>

pkgname=soqt
pkgver=1.6.0
_soanydata_commit=3ff6e9203fbb0cc08a2bdf209212b7ef4d78a1f2
_sogui_commit=100612bf4016916dd686e2b6fecf8ac23d3db14d
pkgrel=1
pkgdesc='A library which provides the glue between Coin and Qt'
arch=('i686' 'x86_64')
url='https://github.com/coin3d/soqt'
license=('GPL')
depends=('coin>=4.0.0' 'qt5-base')
makedepends=('cmake' 'doxygen')
source=("https://github.com/coin3d/soqt/archive/SoQt-$pkgver.tar.gz"
        "soanydata-$_soanydata_commit.tar.gz::https://github.com/coin3d/soanydata/archive/$_soanydata_commit.tar.gz"
        "sogui-$_sogui_commit.tar.gz::https://github.com/coin3d/sogui/archive/$_sogui_commit.tar.gz"
        "soqt-remove-cpack.patch::https://github.com/coin3d/soqt/commit/1318402.patch")
sha256sums=('80bbee01089af754380c48ea435008ea93465149999a545741c410efe8e9bef9'
            'ede29d60d1b35e66193aaf115784f87867ab1658cb1d977fe75dfc0d0ffb3241'
            '605c649902c7be3549b9df7bfdd11d80f13f3aa09b8f0654bf99bcf66a1ee914'
            '54df1238fbe412b470e13f2c2f94abba23a283dafb9ca8b14ea31ac348668db5')

prepare() {
    cd soqt-SoQt-$pkgver

    patch -Np1 -i ../soqt-remove-cpack.patch

    ln -rs ../soanydata-$_soanydata_commit data
    ln -rs ../sogui-$_sogui_commit src/Inventor/Qt/common
}

build() {
    mkdir -p build
    cd build

    cmake ../soqt-SoQt-$pkgver \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DSOQT_BUILD_DOC_MAN=ON \
        -DSOQT_BUILD_DOC_CHM=OFF

    make
}

package() {
    cd build

    make DESTDIR="$pkgdir" install

    # remove html help pages
    rm -rf "$pkgdir/usr/share/doc"
}

