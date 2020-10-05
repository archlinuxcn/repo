# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=beancount
pkgdesc='Double-Entry Accounting from Text Files'
pkgver=2.3.2
pkgrel=1
arch=('i686' 'x86_64' 'armv7h')
url="http://furius.ca/beancount/"
license=('GPL')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('0d6205a0882c3f9bc3ebfd642b329659412e10b36a3e0c7e2648410d9670d7f1')
depends=('python>=3.5' 'mpdecimal' 'python-dateutil' 'python-ply'
         'python-bottle' 'python-lxml' 'python-magic-ahupp' 'python-beautifulsoup4'
         'python-chardet' 'python-google-api-python-client' 'python-requests'
         'python-pytest')
conflicts=('beancount-hg')

package () {
  cd "${pkgname}-${pkgver}"
  python setup.py install --prefix=/usr --root="${pkgdir}"
}
