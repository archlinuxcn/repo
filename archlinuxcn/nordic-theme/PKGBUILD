# Maintainer: hamki <hamki.do2000@gmail.com>
pkgname=nordic-theme
_pkgname=Nordic
pkgver=1.9.0
pkgrel=1
epoch=
pkgdesc="Nordic is a Gtk3.20+ theme created using the awesome Nord color pallete."
arch=('i686' 'x86_64')
url="https://github.com/EliverLara/Nordic"
license=('GPL3')
groups=()
depends=()
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("https://github.com/EliverLara/Nordic/releases/download/v$pkgver/$_pkgname.tar.xz"
)
noextract=()
sha256sums=(c7ea5c4816ce6fb0c2763e77908485c2ee816790f727009429137bc2131ca18b)

package() {
  cd "${_pkgname}"
  mkdir -p "${pkgdir}/usr/share/themes/$_pkgname"
  cp -a "${srcdir}/${_pkgname}/"* "${pkgdir}/usr/share/themes/${_pkgname}/"
}
