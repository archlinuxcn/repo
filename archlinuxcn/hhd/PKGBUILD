# Maintainer: Antheas Kapenekakis <aur at antheas dot dev>
pkgname=hhd
pkgver=3.7.0
pkgrel=1
pkgdesc='Handheld Daemon. A tool for managing the quirks of handheld devices.'
arch=('x86_64')
url='https://github.com/hhd-dev/hhd'
license=('GPL-3.0-or-later' 'MIT')
depends=('python' 'python-setuptools' 'python-evdev' 'python-rich' 'python-yaml' 'python-xlib' 'libusb' 'python-pyserial' 'lsof')
optdepends=('hhd-user: allows running hhd as a user service.')
makedepends=('python-'{'build','installer','setuptools','wheel'})
source=("https://pypi.python.org/packages/source/h/hhd/hhd-${pkgver}.tar.gz")
sha512sums=('c6867bf25b0eb7be6673675c88054bd9f42c7ea01a59e042390eb8b2eac933fa3cc68c59b92a438274c372051f1c2505c35df98cddddaea6e82ccfdfedc69104')

build() {
  cd "hhd-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "hhd-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
  
  # Install minimally necessary rules for running as a system service
	mkdir -p ${pkgdir}/usr/lib/udev/rules.d/
  install -m644 usr/lib/udev/rules.d/83-hhd.rules ${pkgdir}/usr/lib/udev/rules.d/83-hhd.rules
	mkdir -p ${pkgdir}/usr/lib/udev/hwdb.d/
  install -m644 usr/lib/udev/hwdb.d/83-hhd.hwdb ${pkgdir}/usr/lib/udev/hwdb.d/83-hhd.hwdb
	mkdir -p ${pkgdir}/usr/lib/systemd/system/
  install -m644 usr/lib/systemd/system/hhd@.service ${pkgdir}/usr/lib/systemd/system/hhd@.service
}
