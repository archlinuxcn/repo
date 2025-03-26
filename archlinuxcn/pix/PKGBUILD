# Maintainer: Nate Simon <njsimon10@gmail.com>

pkgname=pix
pkgver=3.4.5
pkgrel=1
pkgdesc="Image viewer and browser based on gthumb. X-Apps Project."
arch=('i686' 'x86_64' 'armv7h')
license=('GPL-2.0-or-later')
depends=(
    'desktop-file-utils'
    'librsvg'
    'gst-plugins-base-libs'
    'gsettings-desktop-schemas'
    'libwebp'
    'webkit2gtk'
    'xapp'
)
makedepends=(
    'meson'
    'intltool'
    'itstool'
    'liboauth'
    'exiv2'
    'glib2-devel'
)
optdepends=(
    'gstreamer: Video support'
    'gst-plugin-gtk: Video support'
    'gst-libav: Video support'
    'exiv2: Embedded metadata support'
    'libjpeg-turbo: Jpeg writing support'
    'libtiff: Tiff writing support'
    'dcraw: Support for RAW photos'
    'brasero: Burn discs'
    'liboauth: Web albums'
    'libchamplain: Map Viewer'
    'libheif: heif/heic/avif file support'
    'yelp: View help and documentation from the app'
)
provides=($pkgname)
conflicts=('pix-git')
url='https://github.com/linuxmint/pix'

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/linuxmint/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('92dbc1958e19cec44966bd39f3f48f8e')

prepare() {
    cd "${srcdir}"/${pkgname}-${pkgver}

    #patch --forward --strip=1 --input=../0001-fix-gcc-errors.patch
}

build() {
    mkdir -p "${srcdir}"/${pkgname}-${pkgver}/build
    cd "${srcdir}"/${pkgname}-${pkgver}/build

    meson --prefix=/usr \
          --libexecdir=lib/${pkgname} \
          --buildtype=plain \
          ..

    ninja
}

package(){
    cd ${srcdir}/${pkgname}-${pkgver}/build
    DESTDIR="$pkgdir/" ninja install
}
