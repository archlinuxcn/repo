# Maintainer: drakkan <nicola dot murino at gmail dot com>
# Contributor: XZS <d dot f dot fischer at web dot de>
# Contributor: Carl George < arch at cgtx dot us >
# Contributor: Janne Haapsaari <haaja@iki.fi>
# Contributor: Christopher Krooß <didi2002 at web.de>

pkgname=gnome-shell-extension-dash-to-dock
_pkgname=dash-to-dock-extensions.gnome.org-v
pkgver=65
pkgrel=1
pkgdesc="Move the dash out of the overview transforming it in a dock"
arch=('any')
url="https://micheleg.github.io/dash-to-dock/"
license=('GPL')
depends=('gnome-shell')
makedepends=('intltool' 'gettext')
source=("https://github.com/micheleg/dash-to-dock/archive/extensions.gnome.org-v${pkgver}.tar.gz")
sha256sums=('335a4f06ad076ec1129b018ed342e14c60da6d4501b98828dc21846d749d1507')

build() {
  cd "${srcdir}"/${_pkgname}${pkgver}
  make
}

package() {
  cd "${srcdir}"/${_pkgname}${pkgver}
  make DESTDIR="${pkgdir}" VERSION="${pkgver}" install
}

# vim:set ts=2 sw=2 et:
