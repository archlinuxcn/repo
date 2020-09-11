# Maintainer: Michael Lass <bevan@bi-co.net>
# Contributor: Tolga HOŞGÖR <fasdfasdas@gmail.com>
# Contributor: Henning Mueller <henning@orgizm.net>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=fritzing
pkgver=0.9.4b.CD498
pkgrel=2
# Tag version can be obtained from github release page. CAUTION: There may be multiple releases per version.
_tagver=CD-498
# Partsrev can only be determined by downloading release build, unpacking and using `git show` on the parts folder.
_partsrev=e79a69765026f3fda8aab1b3e7a4952c28047a62
pkgdesc='PCB layout prototyping application'
arch=('i686' 'x86_64')
url=http://fritzing.org
license=(GPL3)
makedepends=('boost' 'git')
depends=('desktop-file-utils' 'libgit2' 'qt5-serialport' 'qt5-svg')
source=(https://github.com/fritzing/fritzing-app/archive/${_tagver}.tar.gz
        "git+https://github.com/fritzing/fritzing-parts.git#commit=${_partsrev}"
        0001-don-t-scan-filesystem-for-application-directory-if-i.patch
        0002-allow-user-and-administrator-to-install-parts-librar.patch
        0003-provide-script-for-user-to-clone-parts-library.patch
        https://github.com/fritzing/fritzing-app/commit/472951243d70eeb40a53b1f7e16e6eab0588d079.patch)
sha256sums=('b8af09b44a1d79fc3ff86f4e0c6793cd4473baf052420b7e1f127f0aaa968167'
            'SKIP'
            '52b20ee77723f805c905dea49177931cfe681689e71b941ee35e2e302a83cf4c'
            '1e59cd5db471b60cd12b8d63510de442c883b3fa0f8d27532aa29bc81838fec1'
            'fb0d8fc6257f166ab77f99bbe32dff51bbdace7d5a3d4d9a789542a8e3fec540'
            'b8d33b1b1523c2038ba684f15f32a5311f0ae9592257c202b5b06cbedcc22757')

prepare() {
  cd "${srcdir}"/fritzing-app-${_tagver}

  # Dynamically link against system libgit2
  sed -i 's/LIBGIT_STATIC = true/LIBGIT_STATIC = false/' phoenix.pro

  # Disable broken font scaling (#3221)
  sed -i 's/Exec=Fritzing/Exec=env QT_AUTO_SCREEN_SCALE_FACTOR=0 Fritzing/' org.fritzing.Fritzing.desktop

  # Fix build against libgit2 >= 1.0
  patch -p1 < "${srcdir}"/472951243d70eeb40a53b1f7e16e6eab0588d079.patch

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
