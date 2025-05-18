#Maintainer:    mumi jim <echo "=02bj5yav9Gb0V3bA1Waq9VatVXb" | rev | base64 -d>
# Contributor: Klaus Alexander Seiﬆrup <$(echo 0x1fd+d59decfa=40 | tr 0-9+a-f=x ka-i@p-u.l)>

#Thanks Klaus Alexander Seistrup :)
#this PKGBUILD of Keypunch
#github Repo: https://github.com/bragefuglseth/keypunch/

pkgname="keypunch-git"
_appname="keypunch"
pkgver=6.3
pkgrel=1
pkgdesc='Practice your typing skills'
url='https://github.com/bragefuglseth/keypunch'
_app_website='https://apps.gnome.org/Keypunch'
arch=('aarch64' 'x86_64')
license=('GPL-3.0-or-later')
source=("https://github.com/bragefuglseth/keypunch/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('63edd187becde410750779d053252897bc1ce31d03fd8dd682b6aac85f55e0e22ca9cbf1fb75518036f36cadd64fe73a7b7001a7ec99703b5840cae14423fad7')
provides=('keypunch')
conflicts=('keypunch')
depends=('gtk4' 'libadwaita')
makedepends=('blueprint-compiler' 'gettext' 'git' 'meson' 'ninja' 'pkgconf' 'rust')

#pkgver() {
#   cd "${srcdir}/${_appname}-${pkgver}"
#   git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
#}

build() {
    cd "${srcdir}/${_appname}-${pkgver}"
    export RUSTUP_TOOLCHAIN=stable
    meson setup -Dprefix=/usr build
    meson compile -C build
}

package() {
    cd "${srcdir}/${_appname}-${pkgver}"
    meson install -C build --destdir "$pkgdir"
}