# Maintainer: marmis <tiagodepalves@gmail.com>
# Contributor: Benzy
# Contributor: Kudlaty
# Contributor: marmis <tiagodepalves@gmail.com>
# Contributor: vitor_hideyoshi <vitor.h.n.batista@gmail.com>
# Contributor: katt <magunasu.b97@gmail.com>
# Contributor: Yangtse Su <i@yangtse.me>

pkgname=xpadneo-dkms
pkgver=0.9.8
pkgrel=1
pkgdesc='Advanced Linux Driver for Xbox One Wireless Gamepad'
arch=('any')
url='https://github.com/atar-axis/xpadneo'
license=('GPL-3.0-or-later')
depends=('dkms' 'bluez' 'bluez-utils')
source=("xpadneo-v${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        '0001-drop-etc-files.patch')
b2sums=('1cddb91cdd4b055fda5c09112af5441da621c07b14f61a0094cbfffa9a7b746491bff6ea0858a28b1e91a204af2822d005a28ed3b1354b6a367a3eee0fc7250c'
        '72d59fc99c8fdd66b3b6bfa45a302114e54e7d1621addde8086723a7c18a6ecc080da7497ac7d43de19c460424a05bba35c51ea0d92cf86498fe9223aceba453')

prepare() {
  cd "xpadneo-${pkgver}/hid-xpadneo"

  # Upstream uses dkms.post_install to create modprobe and udev files in
  # /etc. In Arch, it makes more sense to create these files in /usr/lib
  # and let pacman take care of them. Won't be needed on v0.10+
  patch -i "${srcdir}/0001-drop-etc-files.patch"

  # Set the current version in DKMS config file.
  sed "s/@DO_NOT_CHANGE@/v${pkgver}/" dkms.conf.in > dkms.conf
}

package() {
  cd "xpadneo-${pkgver}/hid-xpadneo"

  # Module source
  install -Dm0644 -t "${pkgdir}/usr/src/hid-xpadneo-v${pkgver}/src" src/*

  # DKMS files
  install -Dm0644 -t "${pkgdir}/usr/src/hid-xpadneo-v${pkgver}" Makefile dkms.conf
  install -Dm0755 -t "${pkgdir}/usr/src/hid-xpadneo-v${pkgver}" dkms.post_install dkms.post_remove

  # Module dependencies
  install -Dm0644 -t "${pkgdir}/usr/lib/modprobe.d" etc-modprobe.d/*
  install -Dm0644 -t "${pkgdir}/usr/lib/udev/rules.d" etc-udev-rules.d/*
}
