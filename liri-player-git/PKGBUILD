# Maintainer: Riley Trautman <asonix.dev@gmail.com>

_pkgname=liri-player
pkgname=$_pkgname-git
pkgver=git
pkgrel=1
pkgdesc="A Web player using the QML Material framework from the Papyros Project"
arch=("i686" "x86_64")
url="https://github.com/pierremtb/liri-player"
license=("GPLv3")
depends=("qt5-base" "qml-material")
makedepends=("git")
provides=("$_pkgname" "$pkgname")
conflicts=("$_pkgname")
install=$pkgname.install
source=("$pkgname::git+https://github.com/pierremtb/liri-player.git"
        "qmlvlc::git+https://github.com/RSATom/QmlVlc.git"
        "yalibvlcwrapper::git+https://github.com/RSATom/ya-libvlc-wrapper.git"
        "libvlcsdk::git+https://github.com/RSATom/libvlc-sdk.git"
        "liri-player.desktop" "$pkgname.install")
sha256sums=("SKIP" "SKIP" "SKIP" "SKIP" "SKIP" "SKIP")

pkgver() {
    cd "$pkgname"
    # cutting off 'foo-' prefix that presents in the git tag
    git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  pushd $(pwd) >> /dev/null

  cd "$srcdir/$pkgname"
  git submodule init
  git config submodule.dependencies/QmlVlc.url "$srcdir/qmlvlc"
  git submodule update

  cd "dependencies/QmlVlc"
  git submodule init
  git config submodule.libvlc_wrapper.url "$srcdir/yalibvlcwrapper"
  git submodule update

  cd "libvlc_wrapper"
  git submodule init
  git config submodule.libvlc-sdk.url "$srcdir/libvlcsdk"
  git submodule update

  popd >> /dev/null

	mkdir -p build
	cd build
	qmake "$srcdir/$pkgname"
	make
}

package() {
	cd build
	make INSTALL_ROOT="$pkgdir" install

  mkdir -p "$pkgdir"/usr/bin
  mkdir -p "$pkgdir"/usr/share/applications

  # for i in 16x16 22x22 32x32 48x48 64x64 128x128 256x256; do
  #   install -Dm644 "$srcdir"/"$pkgname"/icons/liri-player.png \
  #                  "$pkgdir"/usr/share/icons/hicolor/$i/apps/liri-player.png
  # done

  # install -m755 ../liri-player.sh \
  #               "$pkgdir"/usr/bin/liri-player

  install -m755 liri-player \
                "$pkgdir"/usr/bin/liri-player
  install -m755 ../liri-player.desktop \
                "$pkgdir"/usr/share/applications/liri-player.desktop
}

# Additional functions to generate a changelog

changelog() {
    cd "$pkgname"
    git log $1..HEAD --no-merges --format=" * %s"
}

gitref() {
    cd "$pkgname"
    git rev-parse HEAD
}
