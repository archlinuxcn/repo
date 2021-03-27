# Maintainer: Michael Lass <bevan@bi-co.net>
# Contributor: Tolga HOŞGÖR <fasdfasdas@gmail.com>
# Contributor: Henning Mueller <henning@orgizm.net>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=fritzing

# We drop the "b" at the end of the version number. It probably means beta
# while there is also "d" for development versions. This would not be correctly
# parsed by `pkgver` anyway (d > b), so let's leave out the b suffix entirely.
pkgver=0.9.6
pkgrel=1

# Tag version can be obtained from github release page. Sometimes this is the
# version number itself, sometimes some CD-magicnumber thing. There can be
# multiple CD-magicnumberthings for the same version number so it's a bit of a
# guess what corresponds to the latest official release.
_tagver=0.9.6

# Parts come from a different respository and are not versioned anymore since
# 2016. Sometimes we can get the revision by downloading the release build,
# unpacking it and using `git show` on the resources/parts folder. Nowadays the
# release build seems to be hidden behind a paywall. Then we need to guess
# based on the master branch of the fritzing-parts repository and the date when
# the release archive was created.
_partsrev=e79a69765026f3fda8aab1b3e7a4952c28047a62

pkgdesc='PCB layout prototyping application'
arch=('i686' 'x86_64')
url=http://fritzing.org
license=(GPL3)
makedepends=('boost' 'git')
depends=('libgit2' 'qt5-serialport' 'qt5-svg')
source=(https://github.com/fritzing/fritzing-app/archive/${_tagver}.tar.gz
        "git+https://github.com/fritzing/fritzing-parts.git#commit=${_partsrev}"
        0001-don-t-scan-filesystem-for-application-directory-if-i.patch
        0002-allow-user-and-administrator-to-install-parts-librar.patch
        0003-provide-script-for-user-to-clone-parts-library.patch)
sha256sums=('eb4ebe461c5d42edb4b10f1f824e7c855ad54555e222c5999061dead09834491'
            'SKIP'
            '52b20ee77723f805c905dea49177931cfe681689e71b941ee35e2e302a83cf4c'
            '1e59cd5db471b60cd12b8d63510de442c883b3fa0f8d27532aa29bc81838fec1'
            'fb0d8fc6257f166ab77f99bbe32dff51bbdace7d5a3d4d9a789542a8e3fec540')

prepare() {
  cd "${srcdir}"/fritzing-app-${_tagver}

  # Dynamically link against system libgit2
  sed -i 's/LIBGIT_STATIC = true/LIBGIT_STATIC = false/' phoenix.pro

  # Disable broken font scaling (#3221)
  sed -i 's/Exec=Fritzing/Exec=env QT_AUTO_SCREEN_SCALE_FACTOR=0 Fritzing/' org.fritzing.Fritzing.desktop

  # Allow users to have their own updatable parts library. See #3238 and #3454 on this topic.
  patch -p1 < "${srcdir}"/0001-don-t-scan-filesystem-for-application-directory-if-i.patch
  patch -p1 < "${srcdir}"/0002-allow-user-and-administrator-to-install-parts-librar.patch
  patch -p1 < "${srcdir}"/0003-provide-script-for-user-to-clone-parts-library.patch
}

build() {
  cd "${srcdir}"/fritzing-app-${_tagver}

  mkdir build && cd build
  qmake-qt5 ..
  make
}

package() {
  cd "${srcdir}"/fritzing-app-${_tagver}/build
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

  # install partsdb clone script
  install -Dm755 "${srcdir}"/fritzing-app-${_tagver}/tools/user_parts_clone.sh "${pkgdir}"/usr/bin/fritzing_clone_parts
}
