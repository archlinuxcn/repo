# Maintainer: Giovanni Harting <539@idlegandalf.com>
# Contributor: Jonathan Steel <jsteel at archlinux.org>
# Contributor: Benjamin Klettbach <b.klettbach@gmail.com>

pkgname=obs-studio-vaapi
_srcname=obs-studio
pkgver=22.0.2
pkgrel=2
pkgdesc="Free, open source software for live streaming and recording"
arch=('x86_64')
url="https://obsproject.com"
license=('GPL2')
conflicts=('obs-studio' 'obs-studio-git')
provides=('obs-studio')
depends=('ffmpeg' 'jansson' 'libxinerama' 'libxkbcommon-x11'
         'qt5-x11extras' 'curl' 'jack' 'gtk-update-icon-cache'
         'libva')
makedepends=('cmake' 'libfdk-aac' 'libxcomposite' 'x264' 'vlc' 'swig' 'python' 'luajit')
optdepends=('libfdk-aac: FDK AAC codec support'
            'libxcomposite: XComposite capture support'
            'luajit: scripting support'
            'python: scripting support'
            'vlc: VLC Media Source support')
source=($_srcname-$pkgver.tar.gz::https://github.com/jp9000/obs-studio/archive/$pkgver.tar.gz
        "https://github.com/obsproject/obs-studio/commit/a64ae11bce8ed9a7c8f1deba3338f77595dba903.patch")
sha256sums=('8712becf41f6e4b801aeaea0ab2c3ec98da3356c60853971d0a9730d3281cebe'
            '0afe5444e5ab5514905f93b2758d525233e48b80463a51fabf44a5821265a6cd')

prepare() {
  cd $_srcname-$pkgver

  patch -Np1 -i "${srcdir}/a64ae11bce8ed9a7c8f1deba3338f77595dba903.patch"
}

build() {
  cd $_srcname-$pkgver

  mkdir -p build; cd build

  cmake -DCMAKE_INSTALL_PREFIX="/usr" \
    -DOBS_VERSION_OVERRIDE="$pkgver-$pkgrel" ..

  make
}

package() {
  cd $_srcname-$pkgver/build

  make install DESTDIR="$pkgdir"
}
