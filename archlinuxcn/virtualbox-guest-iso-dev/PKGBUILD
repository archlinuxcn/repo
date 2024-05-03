# Maintainer: heavysink

pkgname=virtualbox-guest-iso-dev
_pkgver=7.0.97-163021
pkgver=7.0.97.163021
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
sha256sums=('6ef7fc192c6f610e0d28d2947ce9d73a2b369495f7b30b9f4b9ba6d377af1e6a'
            'fbe9cd6288037bff44716642ee4bea9c42c2d60eb5ed86cb48fa95147d9e8623')

package() {
  install -D -m 0644 VBoxGuestAdditions_$_pkgver.iso \
    "$pkgdir/usr/lib/virtualbox/additions/VBoxGuestAdditions.iso"
  install -D -m 0644 "$srcdir/license" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
