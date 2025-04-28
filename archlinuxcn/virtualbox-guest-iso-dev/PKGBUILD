# Maintainer: heavysink

pkgname=virtualbox-guest-iso-dev
_pkgver=7.1.97-168625
pkgver=7.1.97.168625
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
sha256sums=('b3161d4f88e5a355992047a0b5f5b75659b1fd0a5bc5c9df199b2467a4f71b6c'
            'fbe9cd6288037bff44716642ee4bea9c42c2d60eb5ed86cb48fa95147d9e8623')

package() {
  install -D -m 0644 VBoxGuestAdditions_$_pkgver.iso \
    "$pkgdir/usr/lib/virtualbox/additions/VBoxGuestAdditions.iso"
  install -D -m 0644 "$srcdir/license" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
