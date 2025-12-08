# Maintainer: marmis <tiagodepalves@gmail.com>
# Contributor: Benzy
# Contributor: Kudlaty
# Contributor: marmis <tiagodepalves@gmail.com>
# Contributor: vitor_hideyoshi <vitor.h.n.batista@gmail.com>
# Contributor: katt <magunasu.b97@gmail.com>
# Contributor: Yangtse Su <i@yangtse.me>

pkgname=xpadneo-dkms
pkgver=0.9.7
pkgrel=2
pkgdesc='Advanced Linux Driver for Xbox One Wireless Gamepad'
arch=('any')
url='https://github.com/atar-axis/xpadneo'
license=('GPL-3.0-or-later')
depends=('dkms' 'bluez' 'bluez-utils')
source=("xpadneo-v${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        '0001-drop-etc-files.patch'
        '0002-hotfix-0.9.7.patch')
b2sums=('6715e684d046ad3162db65196896d23f0c70046d02adbf5886d849818120fb731acb86da0a9e18e54b56b31220911ea25c296f1b8473eb0f0fca4fe96b98712b'
        '72d59fc99c8fdd66b3b6bfa45a302114e54e7d1621addde8086723a7c18a6ecc080da7497ac7d43de19c460424a05bba35c51ea0d92cf86498fe9223aceba453'
        '90890f2db402b996a0a44291925b4684812a834c7dd8a9d0b0a8830283d223b1ec4b7c55166596d8773d0a767f36927cc9f01e049b72a6c07fe25794c7c735fa')

prepare() {
  cd "xpadneo-${pkgver}/hid-xpadneo"

  # Upstream uses dkms.post_install to create modprobe and udev files in
  # /etc. In Arch, it makes more sense to create these files in /usr/lib
  # and let pacman take care of them.
  patch -i "${srcdir}/0001-drop-etc-files.patch"

  # Hotfix for https://github.com/atar-axis/xpadneo/issues/575
  patch -Np2 -i "${srcdir}/0002-hotfix-0.9.7.patch"

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
