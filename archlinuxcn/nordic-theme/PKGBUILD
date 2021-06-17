# Maintainer: hamki <hamki.do2000@gmail.com>
pkgname=nordic-theme
_pkgname=Nordic
pkgver=2.0.0
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
source=("https://github.com/EliverLara/Nordic/releases/download/$pkgver/$_pkgname.tar.xz"
)
noextract=()
sha256sums=(c6c75f9474568c2b7a0067490d6a76427b9c2ff9fc6963dd3878efa9c4a24543)

package() {
  cd "${_pkgname}"
  mkdir -p "${pkgdir}/usr/share/themes/$_pkgname"
  cp -a "${srcdir}/${_pkgname}/"* "${pkgdir}/usr/share/themes/${_pkgname}/"
}
