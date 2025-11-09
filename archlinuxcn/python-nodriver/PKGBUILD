# Maintainer: Kimiblock Moe
# Contributor: Junker

pkgname=python-nodriver
_name=nodriver
pkgver=0.48.1
pkgrel=1
pkgdesc='Successor of Undetected-Chromedriver. Providing a blazing fast framework for web automation, webscraping, bots and any other creative ideas which are normally hindered by annoying anti bot systems like Captcha / CloudFlare / Imperva / hCaptcha'
arch=('any')
url=https://github.com/UltrafunkAmsterdam/nodriver
license=('AGPL-3.0-only')
depends=('python-mss' 'python-deprecated' 'python-websockets')
makedepends=('python-build' 'python-installer' 'python-wheel' python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('4ac8cd88b6af133c26dc157fb78f5ab17462a59b4a0da3304e3af12bbe4b4343')

build() {
	cd $_name-$pkgver
	python -m build --wheel --no-isolation --skip-dependency-check
}

package() {
	cd $_name-$pkgver
	python -m installer --destdir="$pkgdir" dist/*.whl

	# Symlink license file
	local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
	install -d "$pkgdir"/usr/share/licenses/$pkgname
	ln -s "$site_packages"/$_name-$pkgver.dist-info/LICENSE \
	   "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
