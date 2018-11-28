# Maintainer: Benoit Brummer < trougnouf at gmail dot com >
# Contributor: Remy Adriaanse <remy@adriaanse.it>

_gemname=nokogiri
pkgname="ruby-${_gemname}"
pkgver=1.8.4
pkgrel=1
pkgdesc='HTML, XML, SAX, and Reader parser'
arch=('any')
url='http://nokogiri.org'
license=('MIT')
depends=('libxml2' 'libxslt' 'ruby' 'ruby-mini_portile2')
makedepends=('ruby-pkg-config' 'ruby-rdoc')
options=('!emptydirs')
source=("https://rubygems.org/downloads/${_gemname}-${pkgver}.gem")
noextract=("${_gemname}-${pkgver}.gem")
sha256sums=('ecad8473fbaebaadd060eec15a872fb67c4bd7c6d64904ebbe15d40113ad36c1')

package() {
	local _gemdir="$(ruby -e'puts Gem.default_dir')"
	NOKOGIRI_USE_SYSTEM_LIBRARIES=1 gem install --ignore-dependencies --no-user-install -i "${pkgdir}/${_gemdir}" -n "${pkgdir}/usr/bin" "${_gemname}-${pkgver}.gem"
	rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"
}
