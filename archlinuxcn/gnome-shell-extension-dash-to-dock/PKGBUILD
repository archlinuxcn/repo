# Maintainer: drakkan <nicola dot murino at gmail dot com>
# Contributor: XZS <d dot f dot fischer at web dot de>
# Contributor: Carl George < arch at cgtx dot us >
# Contributor: Janne Haapsaari <haaja@iki.fi>
# Contributor: Christopher Krooß <didi2002 at web.de>

pkgname=gnome-shell-extension-dash-to-dock
_pkgname=dash-to-dock-ubuntu-dock-
pkgver=66
pkgrel=2
pkgdesc="Move the dash out of the overview transforming it in a dock"
arch=('any')
url="https://micheleg.github.io/dash-to-dock/"
license=('GPL')
depends=('gnome-shell')
makedepends=('intltool' 'gettext')
source=("https://github.com/micheleg/dash-to-dock/archive/ubuntu-dock-${pkgver}ubuntu19.10.2.tar.gz")
sha256sums=('e5d8f50b26422e26c71d5a906b6e72a553e09bcee21bad8e6796055b294bcfa5')

build() {
  cd "${srcdir}"/${_pkgname}${pkgver}ubuntu19.10.2
  make
}

package() {
  cd "${srcdir}"/${_pkgname}${pkgver}ubuntu19.10.2
  make DESTDIR="${pkgdir}" VERSION="${pkgver}" install
}

# vim:set ts=2 sw=2 et:
