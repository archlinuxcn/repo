# Maintainer: Sietse van der Molen <sietse@vdmolen.eu>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: pisuka <tekmon@gmail.com>
# Contributor: Estevao Valadao <estevao@archlinux-br.org>
# Contributor: Guten <ywzhaifei@gmail.com>
# Contributor: Lee.MaRS <leemars@gmail.com>

pkgname=google-appengine-python
pkgver=1.8.9
_zipver=$pkgver
pkgrel=1
arch=(any)
pkgdesc="Google App Engine SDK for Python."
url=https://developers.google.com/appengine/
license=(APACHE)
depends=(python2)
optdepends=(mysql-python
	python-imaging=1.1.7
	python2-numpy=1.6.1
	pycrypto=2.6
	python-lxml=2.3
	django=1.4
	python-jinja2=2.6
	python2-markupsafe=0.15
	python2-webapp2=2.3
	python2-webob=1.1.1
	python2-yaml=3.10)
makedepends=(unzip)
options=(!strip)
install=install
source=(http://googleappengine.googlecode.com/files/google_appengine_${_zipver}.zip)
noextract=(google_appengine_${_zipver}.zip)

package() {
  cd "$pkgdir"
  mkdir -p opt usr/bin

  # Extract with unzip as bsdtar screws up permissions
  unzip -q "$srcdir/google_appengine_${_zipver}.zip" -d opt
  
  mv opt/google_appengine opt/${pkgname}
  rm -rf opt/${pkgname}/php

  grep -r -l python "opt/${pkgname}" | xargs sed -i '/#!\/usr\/bin\/env python/s|python|python2|'

  find opt/${pkgname} -maxdepth 1 -type f -executable -printf "/opt/${pkgname}/%f\n" | xargs ln -st usr/bin/
}

sha1sums=('6a5a79a81bf0f1fccf5b56dac41be6174888983e')
