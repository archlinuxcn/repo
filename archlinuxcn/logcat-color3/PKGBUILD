# Maintainer: Chih-Hsuan Yen <base64_decode("eXUzYWN0eHQydHR0ZmlteEBjaHllbi5jYwo=")>
# Contributor: Thomas Weißschuh <thomas t-8ch de>

pkgname=logcat-color3
pkgver=0.11.0
pkgrel=1
pkgdesc='A colorful and highly configurable alternative to the standard "adb logcat" command from the Android SDK'
arch=(any)
url='https://github.com/yan12125/logcat-color3'
# https://github.com/yan12125/logcat-color3/blob/v0.10.0/setup.cfg#L11
license=('Apache-2.0')
depends=(python python-colorama python-pyasyncore python-pyasynchat)
makedepends=(git python-build python-installer python-setuptools python-setuptools-scm python-wheel openssh)
conflicts=(logcat-color)
source=("git+https://github.com/yan12125/logcat-color3#tag=v$pkgver"
        "ssh_allowed_signers")
sha256sums=('7665d5851cff42364586934d8921e14e085c6de6af763651f05f7458ff49e68e'
            'b83e8c654e3af93d6bb173db51d59f2f422fc5c777efe4253b26cfbaba6f0943')

# XXX: move to verify() when devtools supports it
# https://gitlab.archlinux.org/archlinux/devtools/-/issues/224
prepare() {
  cd logcat-color3
  git -c gpg.ssh.allowedSignersFile="$srcdir/ssh_allowed_signers" verify-tag v$pkgver
}

build() {
  cd logcat-color3
  python -m build --wheel --no-isolation
}

check() {
  cd logcat-color3
  python -m unittest discover ./test
}

package() {
  cd logcat-color3
  python -m installer --destdir="$pkgdir" dist/*.whl
}
