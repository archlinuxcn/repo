# Maintainer: Versus Void <chaoskeeper &commat; mail FULL STOP ru>
# Maintainer: Mehmet Ozgur Bayhan <mozgurbayhan@gmail.com>
# Contributor: Vyacheslav Konovalov <echo dnlhY2hrb25vdmFsb3ZAZ21haWwuY29tCg== | base64 -d>

pkgname=redis-desktop-manager
pkgver=2019.5
pkgrel=2
pkgdesc='Open source cross-platform Redis Desktop Manager based on Qt 5'
arch=('x86_64')
url="https://redisdesktop.com/"
license=('GPL3')
depends=(
  'qt5-base'
  'qt5-imageformats'
  'qt5-tools'
  'qt5-declarative'
  'qt5-quickcontrols'
  'qt5-quickcontrols2'
  'qt5-charts'
  'qt5-graphicaleffects'
  'qt5-svg'
  'libssh2'
  'python')
makedepends=('git' 'gcc')
conflicts=('redis-desktop-manager-bin')
source=("rdm::git://github.com/uglide/RedisDesktopManager.git#tag=$pkgver"
        'rdm.sh'
        'rdm.desktop'
        'link-python.patch')
sha256sums=('SKIP'
            'f469d9a5adce723904efe0f1b1db5d79807410f90aafb117f18ae108d8b2d391'
            '9ca6cfe0fc1a050552ec2fa009a2d517de3b049ff6f379f0fda849e4dbca3f68'
            '428d2758345059f844dee05bbc6d06eecf82f6cbd3f1a8a308fe4f54cadb43ce')

prepare() {
  cd rdm/
  git apply ../link-python.patch
  git submodule update --init --recursive
  git submodule add https://chromium.googlesource.com/linux-syscall-support 3rdparty/linux-syscall-support

  python build/utils/set_version.py "$pkgver" > src/version.h

  _lssdir='3rdparty/gbreakpad/src/third_party/lss/'
  mkdir -p ${_lssdir}
  cp 3rdparty/linux-syscall-support/linux_syscall_support.h ${_lssdir}
  touch 3rdparty/gbreakpad/README
}

build() {
  rm -rf $srcdir/rdm/bin
  cd $srcdir/rdm/src
  lrelease resources/translations/*.ts
  qmake && make
}

package() {
  _instdir="$srcdir/rdm/bin/linux/release"
  _bindir="$pkgdir/usr/share/redis-desktop-manager/bin"

  mkdir -p "${_bindir}"
  mkdir "$pkgdir/usr/share/licenses"
  mkdir "$pkgdir/usr/share/pixmaps"
  mkdir "$pkgdir/usr/share/applications"

  install -Dm644 "$srcdir/rdm/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm755 "${_instdir}/rdm" "${_bindir}/rdm"
  install -Dm755 "$srcdir/rdm.sh" "${_bindir}/rdm.sh"
  install -Dm644 "$srcdir/rdm/src/resources/images/rdm.png" "$pkgdir/usr/share/pixmaps/rdm.png"
  install -Dm644 "$srcdir/rdm.desktop" "$pkgdir/usr/share/applications/rdm.desktop"

  mkdir "$pkgdir/usr/bin"
  ln -s '/usr/share/redis-desktop-manager/bin/rdm.sh' "$pkgdir/usr/bin/rdm"
}
