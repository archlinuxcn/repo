# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=beancount
pkgdesc='Double-Entry Accounting from Text Files'
pkgver=2.3.4
pkgrel=2
arch=('i686' 'x86_64' 'armv7h')
url="http://furius.ca/beancount/"
license=('GPL')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('2bf08ce6a95d98000f4d73395985cd1deb81c0d52ed5a76e610bac77d82f86c0')
depends=('python>=3.5' 'mpdecimal' 'python-dateutil' 'python-ply'
         'python-bottle' 'python-lxml' 'python-magic-ahupp' 'python-beautifulsoup4'
         'python-chardet' 'python-google-api-python-client' 'python-requests'
         'python-pytest')
conflicts=('beancount-hg')

package () {
  cd "${pkgname}-${pkgver}"
  python setup.py install --prefix=/usr --root="${pkgdir}"
}
