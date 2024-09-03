# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Jelle van der Waa <jelle vdwaa nl>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Dale Blount <dale@archlinux.org>
# Contributor: Michael Düll <mail@akurei.me>
# Contributor: Luca Corbatto <lucaatcorbatto.de>

# I would just like to take a minute here and state that synergy is
# some of the worst packaged software ever. They BUNDLE a fucking
# zip for cryptopp and do not provide an option to use a system-
# installed version of that library. They change around paths every
# update and just generally don't seem to care much.
pkgname=synergy
_tag=1.15.1+r1
pkgver=${_tag/-}
pkgrel=2
pkgdesc='Share a single mouse and keyboard between multiple computers'
url='https://symless.com/synergy/'
arch=('x86_64')
# https://github.com/symless/synergy-core/blob/1.15.0.16-snapshot/LICENSE indicates GPLv2, and only one C++ file says "any later"
license=('GPL-2.0-only')
depends=('gcc-libs' 'libxtst' 'libxinerama' 'libxkbfile' 'openssl' 'libxrandr' 'hicolor-icon-theme' 'libnotify' 'pugixml')
makedepends=('git' 'libxt' 'cmake' 'qt6-base' 'qt6-tools' 'gmock' 'gtest')
optdepends=('qt6-base: gui support')
checkdepends=('xorg-server-xvfb')
source=("git+https://github.com/symless/synergy-core.git#tag=${_tag}"
        use-system-libs.patch
        synergys.socket
        synergys.service)
sha512sums=('fade9a617621f44c0698ac3f3cede86067f24c122612687dd00d8cc2e360b89ab0d1403bf16e3385d86ef9a5d337f80af35f2c96e14308980ecf28b99b20f632'
            'fd521ed2464d91fe20576b51060224bc402489d5c08c13a34122f573ab4c77812c289ad09258829e190cbe2533dd170fd636587f68751965cbcc6039be5b6859'
            'f9c124533dfd0bbbb1b5036b7f4b06f7f86f69165e88b9146ff17798377119eb9f1a4666f3b2ee9840bc436558d715cdbfe2fdfd7624348fae64871f785a1a62'
            '9663a11b915e10e60317e732a4d1191e8f8ff19176994c27dd20aa445daab7565bd624e5575c9c639d144293879fbe8376834a076723f778fd322ebd1c9f2029')

prepare() {
  cd synergy-core

  # get rid of shitty bundled gtest and gmock
  patch -Np1 < "${srcdir}/use-system-libs.patch"
}

build() {
  cd synergy-core
  cmake -B build -S . \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DGIT_SUBMODULE=OFF \
    -DSYSTEM_PUGIXML=ON
  make -C build
}

check() {
  cd synergy-core/build
  xvfb-run --auto-display ./bin/unittests
  xvfb-run --auto-display ./bin/integtests
}

package() {
  cd synergy-core

  # install binary
  install -Dm 755 build/bin/{synergy,synergyc,synergyd,synergys,syntool} -t "${pkgdir}/usr/bin"

  # install config
  install -Dm 644 doc/${pkgname}.conf* -t "${pkgdir}/etc"

  # install systemd service and socket
  install -Dm 644 "${srcdir}"/synergys.{service,socket} -t "${pkgdir}/usr/lib/systemd/user"

  # install desktop/icon stuff
  install -Dm 644 res/synergy.svg -t "${pkgdir}/usr/share/icons/hicolor/scalable/apps/"
  install -Dm 644 res/dist/linux/synergy.desktop -t "${pkgdir}/usr/share/applications"
}

# vim:set ts=2 sw=2 et:
