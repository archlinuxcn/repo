# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=beancount
pkgdesc='Double-Entry Accounting from Text Files'
pkgver=2.3.1
pkgrel=1
arch=('i686' 'x86_64' 'armv7h')
url="http://furius.ca/beancount/"
license=('GPL')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('e12abfe0a6b38ce3525adb471ca5b8e3fa4056ff712108de48da53405c518a11')
depends=('python>=3.5' 'mpdecimal' 'python-dateutil' 'python-ply'
         'python-bottle' 'python-lxml' 'python-magic-ahupp' 'python-beautifulsoup4'
         'python-chardet' 'python-google-api-python-client' 'python-requests'
         'python-pytest')
conflicts=('beancount-hg')

package () {
  cd "${pkgname}-${pkgver}"
  python setup.py install --prefix=/usr --root="${pkgdir}"
}
