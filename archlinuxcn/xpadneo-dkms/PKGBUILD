# Maintainer: marmis <tiagodepalves@gmail.com>
# Contributor: Benzy
# Contributor: Kudlaty
# Contributor: "marmis" Tiago de Paula <tiagodepalves@gmail.com>
# Contributor: vitor_hideyoshi <vitor.h.n.batista@gmail.com>
# Contributor: katt <magunasu.b97@gmail.com>
# Contributor: Yangtse Su <i@yangtse.me>

pkgname=xpadneo-dkms
pkgver=0.10.2
pkgrel=1
pkgdesc='Advanced Linux Driver for Xbox One Wireless Gamepad'
arch=('any')
url='https://github.com/atar-axis/xpadneo'
license=('GPL-2.0-only AND GPL-3.0-or-later')
depends=('dkms' 'bluez' 'bluez-utils')
source=("xpadneo-v${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
b2sums=('f822ad82e43df5af263cb76fd837e65931561c34ccd8cbb5fe0d93f9e7cf9903feeb65d0ac66749ae92371b40c2b0cc10d15bca502df36e6a611b9702d5ac81c')

package() {
  cd "${srcdir}/xpadneo-${pkgver}"

  # Add modprobe and udev files
  make VERSION="v${pkgver}" PREFIX="${pkgdir}" ETC_PREFIX=/usr/lib \
    install

  # License applicability
  LICENSE_DIR="${pkgdir}/usr/share/licenses/${pkgname}"
  install -Dm0644 -t "${LICENSE_DIR}" LICENSE.md LICENSES/*.txt

  # DKMS files
  TARGET_DIR="${pkgdir}/usr/src/hid-xpadneo-v${pkgver}"
  install -Dm0644 -t "${TARGET_DIR}" hid-xpadneo/{Makefile,dkms.conf}
  install -Dm0755 -t "${TARGET_DIR}" hid-xpadneo/dkms.post_{install,remove}

  # Module source
  cd hid-xpadneo
  find src/ -type d -exec install -d "${TARGET_DIR}/{}" \;
  find src/ -type f -not -name '.*' -exec install -T -m0644 '{}' "${TARGET_DIR}/{}" \;
}
