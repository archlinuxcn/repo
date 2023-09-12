# Maintainer: HLFH <gaspard@dhautefeuille.eu>
# Contributor: Schnouki <schnouki@schnouki.net>

pkgname=hash-slinger
pkgver=3.2
pkgrel=1
pkgdesc="Tools to generate special DNS records (SSHFP, TLSA, OPENPGPKEY, IPSECKEY)"
arch=(any)
url="https://github.com/letoams/hash-slinger"
license=('GPL2')
depends=('python-dnspython' 'python-ipaddress' 'python-m2crypto' 'unbound')
makedepends=('xmlto')
optdepends=('openssh: for sshfp'
            'python-gnupg: for openpgpkey'
            'libreswan: for ipseckey (if not using openswan or strongswan)'
            'openswan: for ipseckey (if not using libreswan or strongswan)'
            'strongswan: for ipseckey (if not using libreswan or openswan)')
source=(https://github.com/letoams/${pkgname}/archive/${pkgver}.tar.gz)
b2sums=('8c89f9a372818166c862d97354a60dddc2795c70f23b39225ad0fc3a2657cc5e048dca228dc004db0240fcf80e74bc799528d3459a65e6de347a493df5abf7b3')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
}
