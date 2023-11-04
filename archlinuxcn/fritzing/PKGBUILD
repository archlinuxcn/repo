# Maintainer: Michael Lass <bevan@bi-co.net>
# Contributor: Tolga HOŞGÖR <fasdfasdas@gmail.com>
# Contributor: Henning Mueller <henning@orgizm.net>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=fritzing

# We drop the "b" at the end of the version number. It probably means beta
# while there is also "d" for development versions. This would not be correctly
# parsed by `pkgver` anyway (d > b), so let's leave out the b suffix entirely.
pkgver=1.0.1
pkgrel=1

# Tag version can be obtained from github release page. Sometimes this is the
# version number itself, sometimes some CD-magicnumber thing. There can be
# multiple CD-magicnumberthings for the same version number so it's a bit of a
# guess what corresponds to the latest official release.
#_tagver=0.9.8

# This is probably closest to what has been released as 1.0.1.
_gitrev=8f5f1373835050ce014299c78d91c24beea9b633

# Parts come from a different respository and are not versioned anymore since
# 2016. Sometimes we can get the revision by downloading the release build,
# unpacking it and using `git show` on the resources/parts folder. Nowadays the
# release build seems to be hidden behind a paywall. Then we need to guess
# based on the master branch of the fritzing-parts repository and the date when
# the release archive was created.
_partsrev=1c7fb3ee5db8480956c157355fb4e5a7169ff865

pkgdesc='PCB layout prototyping application'
arch=('aarch64' 'i686' 'x86_64')
url=http://fritzing.org
license=(GPL3)
install=fritzing.install
makedepends=('boost' 'git')
depends=('libgit2' 'qt6-serialport' 'qt6-svg' 'quazip-qt6' 'ngspice')
source=("git+https://github.com/fritzing/fritzing-app.git#commit=${_gitrev}"
        "git+https://github.com/fritzing/fritzing-parts.git#commit=${_partsrev}"
        svgpp-1.3.0.tar.gz::https://github.com/svgpp/svgpp/archive/refs/tags/v1.3.0.tar.gz
        0001-Quick-Dirty-patch-to-allow-finding-quazip-qt6-on-Arc.patch
        0002-Quick-Dirty-patch-to-allow-finding-ngspice-on-Arch-L.patch
        0003-ParseResult-operator-bool-in-explicit.patch)
sha256sums=('SKIP'
            'SKIP'
            'cb14e9de41994e3451aaee61d8284848bfccc7f9a5bf1873a76f199ff0c20b74'
            '26c20d2dcebc99e70bf1db839d1b716ac552dad20592ff7f650069317fe38b5d'
            '1aff8495da53f223857e48f12a149ccd3c20472e9d12399d916b723eaf052bfa'
            '4319035727c74c59298aeb18e579201ee5a8c26edd413e6e1bc1b6d0a58aa5ed')

prepare() {
  cd "${srcdir}"/fritzing-app

  # Allow finding quazip-qt6 on Arch Linux
  patch -p1 < "${srcdir}/0001-Quick-Dirty-patch-to-allow-finding-quazip-qt6-on-Arc.patch"

  # Allow finding ngspice on Arch Linux
  patch -p1 < "${srcdir}/0002-Quick-Dirty-patch-to-allow-finding-ngspice-on-Arch-L.patch"

  # Fix error caused by implicit call to ParseResult::operator bool()
  patch -p1 < "${srcdir}/0003-ParseResult-operator-bool-in-explicit.patch"

  # Dynamically link against system libgit2
  sed -i 's/LIBGIT_STATIC = true/LIBGIT_STATIC = false/' phoenix.pro

  # Disable broken font scaling (#3221)
  sed -i 's/Exec=Fritzing/Exec=env QT_AUTO_SCREEN_SCALE_FACTOR=0 Fritzing/' org.fritzing.Fritzing.desktop
}

build() {
  cd "${srcdir}"/fritzing-app

  mkdir build && cd build
  qmake6 ..
  make
}

package() {
  cd "${srcdir}"/fritzing-app/build
  make INSTALL_ROOT="${pkgdir}" install

  # We want a system-wide installation of the parts library. Following steps are
  # derived from tools/linux_release_script/release.sh. However, we drop the .git
  # subfolder afterwards as it is not required at runtime.
  cp -dr "${srcdir}"/fritzing-parts "${pkgdir}"/usr/share/fritzing/
  "${pkgdir}"/usr/bin/Fritzing \
    -db "${pkgdir}"/usr/share/fritzing/fritzing-parts/parts.db \
    -pp "${pkgdir}"/usr/share/fritzing/fritzing-parts \
    -f  "${pkgdir}"/usr/share/fritzing \
    -platform offscreen
  rm -rf "${pkgdir}"/usr/share/fritzing/fritzing-parts/.git{,ignore}
}
