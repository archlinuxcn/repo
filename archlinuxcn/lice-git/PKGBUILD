# Maintainer: Gabriele Fulgaro <gabriele.fulgaro@gmail.com>
# Contributor: wangjiezhe <wangjiezhe AT yandex DOT com>
# Contributor: Shengyu Zhang <la@archlinuxcn.org>

_pkgname=lice
pkgname="${_pkgname}-git"
pkgver=0.4.64.g9940116
pkgrel=1
pkgdesc='Generate license files for your projects'
arch=('any')
url="https://github.com/licenses/${_pkgname}"
license=('custom:BSD3')
depends=('python')
makedepends=('git' 'python-setuptools')
checkdepends=('python-pytest')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("git+${url}.git")
md5sums=('SKIP')

pkgver() {
	cd "${srcdir}/${_pkgname}"
	git describe | sed 's/-/./g'
}

build() {
	cd "${srcdir}/${_pkgname}"
	python setup.py build
}

check() {
	cd "${srcdir}/${_pkgname}"
	pytest
}

package() {
	cd "${srcdir}/${_pkgname}"
	python setup.py install --root="${pkgdir}/" --optimize=1 --skip-build
	install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
