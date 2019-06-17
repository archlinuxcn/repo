# Maintainer: Guillaume Hayot <ghayot@postblue.info>
# Contributor: Arvedui <arvedui@posteo.de>
# Contributor: Marc Plano-Lesay <marc.planolesay@gmail.com>
# Contributor: Joost Bremmer <toost.b@gmail.com>

pkgname=python-discogs-client
pkgver=2.2.1
pkgrel=3
pkgdesc="This is the official Discogs API client for Python. You can use it to query the Discogs music database for metadata on artists, releases, and more."
depends=('python-six' 'python-requests' 'python-oauthlib')
makedepends=('python-setuptools')
arch=('any')
# PyPI doesn't ship a license so we have to get it from GitHub
source=(discogs-client-$pkgver.tar.gz::https://pypi.python.org/packages/1f/1f/62a8cee111ff72c5ad379039adef8c872813602ffd516ba35368726f14c2/${pkgname#python-}-${pkgver}.tar.gz
        LICENSE::https://raw.githubusercontent.com/discogs/discogs_client/v2.2.0/LICENSE)
md5sums=('c82be8006e1c02fcfc2bb42a2e312151'
         'c1e6695335325feb11337315fb930f21')
url="https://github.com/discogs/discogs_client"
license=('custom')

package() {
  cd $srcdir/${pkgname#python-}-$pkgver
  python setup.py install --root=$pkgdir --optimize=1

  cd $srcdir
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim: set ts=2 sw=2 et:
