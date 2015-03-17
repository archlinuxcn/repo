# Contributor: BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: DonVla <donvla@users.sourceforge.net>
# Contributor: Reventlov <contact@volcanis.me>
# Maintainer: SanskritFritz (gmail)

pkgname=obapps
pkgver=0.1.7
pkgrel=4
pkgdesc="Graphical tool for configuring application settings in Openbox."
arch=('any')
url="http://obapps.sourceforge.net/"
license=('GPL')
depends=('wxpython2.8' 'python2-xlib')
options=(!docs)
source=("http://downloads.sourceforge.net/project/${pkgname}/${pkgname}-${pkgver}.tar.gz"
        "obapps-python2.patch")
md5sums=('de9fcc8430faa3ebeeaa4d4abf7aae17'
         '3a8055843a2d8ed6fa362f818f2337b6')

prepare() {
	cd ${pkgname}-${pkgver}
	patch < ${srcdir}/obapps-python2.patch
}

package() {
	cd ${pkgname}-${pkgver}
	python2 setup.py install --prefix=/usr --root=${pkgdir}
}
