# Maintainer: Jakub Szymański <jakubmateusz@poczta.onet.pl>
pkgname=woeusb-ng
pkgver=0.2.12
pkgrel=3
pkgdesc="Simple tool that enable you to create your own usb stick with Windows installer."
arch=('any')
url="https://github.com/WoeUSB/WoeUSB-ng"
license=('GPL3')
depends=(
    'parted'
    'dosfstools'
    'ntfsprogs'
    'grub'
    'p7zip'
    'python'
    'python-pip'
    'python-wxpython'
    'xdg-utils'
    'python-termcolor'
)

makedepends=(
    'python-build'
    'python-installer'
    'python-wheel'
    'python-setuptools'
)

provides=('woeusb')

conflicts=(
    'woeusb'
    'woeusb-git'
)

source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/WoeUSB/WoeUSB-ng/archive/v$pkgver.tar.gz"
    "pr79.patch"
)

sha256sums=('64b9346490e88c627f0034973771620474acb9482bb6a5045c27e52d23987779'
            '848e56d1b377a46bba6f8c400f7b7aea18aba263f6c795158e219fbad9c87ed6')

prepare() {
    cd WoeUSB-ng-$pkgver
    patch --forward --strip=1 --input="${srcdir}/pr79.patch"
}

build() {
    cd WoeUSB-ng-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd WoeUSB-ng-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    # shortcut
    cp miscellaneous/WoeUSB-ng.desktop $pkgdir/usr/share/applications/WoeUSB-ng.desktop
    chmod 755 $pkgdir/usr/share/applications/WoeUSB-ng.desktop

    # policy
    cp miscellaneous/com.github.woeusb.woeusb-ng.policy $pkgdir/usr/share/polkit-1/actions/com.github.woeusb.woeusb-ng.policy
}
