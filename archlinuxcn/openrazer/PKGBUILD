# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>
# Contributor: Gabriele Musco <emaildigabry@gmail.com>

pkgbase=openrazer
pkgname=('python-openrazer' 'openrazer-daemon' 'openrazer-driver-dkms' 'openrazer-meta')
pkgver=3.2.0
pkgrel=1
pkgdesc="An entirely open source driver and user-space daemon that allows you to manage your Razer peripherals on GNU/Linux."
arch=('any')
url="https://github.com/openrazer/openrazer"
license=('GPL2')
makedepends=('python-setuptools')
source=("https://github.com/openrazer/openrazer/releases/download/v$pkgver/openrazer-$pkgver.tar.xz")
sha256sums=('53d0ad9c7baae9d1b0d048b3368f338a55fd6713db325535290da1138255bc3e')

prepare() {
  # Do a sanity check in the environment of the builder so the build process doesn't place files into a wrong directory.
  # If you think this is incorrect you can always remove this from the PKGBUILD, but then please don't complain if it doesn't work.
  if [ "$(which python3)" != "/usr/bin/python3" ]; then
    echo "ERROR: Your 'python3' does not point to /usr/bin/python3 but to $(which python3), likely a custom environment like anaconda."
    echo "Please build this package in a clean chroot (e.g. with https://wiki.archlinux.org/title/DeveloperWiki:Building_in_a_clean_chroot) or point your PATH variable to prefer /usr/bin/ temporarily."
    return 1
  fi
}

package_python-openrazer() {
  pkgdesc="Python library for accessing the Razer daemon from Python."
  depends=('openrazer-daemon' 'python-numpy')

  cd "$pkgbase-$pkgver"
  make DESTDIR="$pkgdir" python_library_install
}

package_openrazer-daemon() {
  pkgdesc="Userspace daemon that abstracts access to the kernel driver. Provides a DBus service for applications to use."
  depends=('openrazer-driver-dkms' 'gtk3' 'python-dbus' 'python-gobject' 'python-setproctitle' 'python-daemonize' 'python-notify2' 'python-pyudev' 'xautomation')
  install=openrazer-daemon.install

  cd "$pkgbase-$pkgver"
  make DESTDIR="$pkgdir" daemon_install
}

package_openrazer-driver-dkms() {
  pkgdesc="Kernel driver for Razer devices (DKMS-variant)"
  depends=('dkms' 'udev')
  install=openrazer-driver-dkms.install

  cd "$pkgbase-$pkgver"
  make DESTDIR="$pkgdir" setup_dkms udev_install
}

package_openrazer-meta() {
  pkgdesc="Meta package for installing all required openrazer packages."
  depends=('openrazer-driver-dkms' 'openrazer-daemon' 'python-openrazer')
  optdepends=('polychromatic: frontend'
              'razergenie: qt frontend'
              'razercommander: gtk frontend')
}
