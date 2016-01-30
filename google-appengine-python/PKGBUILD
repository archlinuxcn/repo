# Maintainer: Raphaël Doursenaud <rdoursenaud@gpcsolutions.fr>
# Contributor: Sietse van der Molen <sietse@vdmolen.eu>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: pisuka <tekmon@gmail.com>
# Contributor: Estevao Valadao <estevao@archlinux-br.org>
# Contributor: Guten <ywzhaifei@gmail.com>
# Contributor: Lee.MaRS <leemars@gmail.com>
# Contributor: Mikkel Oscar Lyderik <mikkeloscar@gmail.com>

pkgname=google-appengine-python
pkgver=1.9.31
_zipver=${pkgver}
pkgrel=1
arch=(any)
pkgdesc="Google App Engine SDK for Python"
url=https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python
license=('APACHE')
depends=('python2>=2.7')
optdepends=('mysql-python: MySQL DB API'
  'python2-crypto=2.6: cryptography functions'
  'python2-crcmod=1.7: generating CRC'
  'python2-django=1.4: full-featured web framework'
  'python2-jinja=2.6: templating'
  'python2-lxml=2.3: python binding to libxml2 and libxslt'
  'python2-matplotlib=1.2.0: 2D plotting'
  'python2-markupsafe=0.15: XML/HTML/XHTML markup safe string'
  'python2-numpy=1.6.1: array-processing'
  'python2-pillow=1.1.7: creating and transforming images'
  'python2-protorpc=1.0: framework for implementing HTTP-based RPC services'
  'python2-pyamf=0.6.1: Action Message Format'
  'python2-setuptools=0.6c11: package and module discovery'
  'python2-webapp2=2.3: lightweight web framework'
  'python2-webob=1.2.3: wrappers around WSGI request environment'
  'python2-yaml=3.10: YAML serialization and deserialization')
options=(!strip)
install=install
source=(https://storage.googleapis.com/appengine-sdks/featured/google_appengine_${_zipver}.zip)
sha1sums=('b0981b32bffc06f7fd6d67651ef5e2aa027ccf65')
noextract=(google_appengine_${_zipver}.zip)

prepare() {
  cd ${srcdir}

  # Extract with unzip as bsdtar screws up permissions
  unzip -qq "google_appengine_${_zipver}.zip" -d "${pkgname}-${pkgver}"

  # Cleanup PHP files
  rm -rf php
  rm -rf demos/php
  rm -f _php_runtime.py
  rm -f php_cli.py

  # Fix python binary
  grep -r -l python | xargs sed -i '/#!\/usr\/bin\/env python/s|python|python2|'
  grep -r -l python | xargs sed -i '/#!\/usr\/bin\/python$/s|python|python2|'
}

package() {
  cd "${pkgdir}"
  mkdir -p opt usr/bin

  # Install
  mv "${srcdir}/${pkgname}-${pkgver}/google_appengine" "opt/${pkgname}"

  # Move main binary
  find opt/${pkgname} -maxdepth 1 -type f -executable -printf "/opt/${pkgname}/%f\n" | xargs ln -st usr/bin/
}
