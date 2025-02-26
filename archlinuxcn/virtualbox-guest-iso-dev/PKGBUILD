# Maintainer: heavysink

pkgname=virtualbox-guest-iso-dev
_pkgver=7.1.97-167740
pkgver=7.1.97.167740
pkgrel=1
pkgdesc='The official VirtualBox Guest Additions ISO image for virtualbox dev version'
arch=('any')
url='https://www.virtualbox.org/'
license=('custom:PUEL')
install=virtualbox-guest-iso-dev.install
replaces=('virtualbox-additions' 'virtualbox-iso-additions')
provides=('virtualbox-guest-iso')
conflicts=('virtualbox-additions' 'virtualbox-iso-additions')
noextract=(VBoxGuestAdditions_$pkgver.iso)
source=("https://www.virtualbox.org/download/testcase/VBoxGuestAdditions_$_pkgver.iso"
        'license')
sha256sums=('d6c3432901e8578a0b7ae196dfdee8b670c06b9382a492f228ace9632bfb8592'
            'fbe9cd6288037bff44716642ee4bea9c42c2d60eb5ed86cb48fa95147d9e8623')

package() {
  install -D -m 0644 VBoxGuestAdditions_$_pkgver.iso \
    "$pkgdir/usr/lib/virtualbox/additions/VBoxGuestAdditions.iso"
  install -D -m 0644 "$srcdir/license" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
