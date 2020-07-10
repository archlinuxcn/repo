# Maintainer: Hao Long <aur@esd.cc>

pkgname=lazynpm
pkgver=0.1.4
pkgrel=1
pkgdesc="A simple terminal UI for npm commands"
arch=("x86_64" "i686")
url="https://github.com/jesseduffield/lazynpm"
license=("MIT")
provides=('lazynpm')
conflicts=('lazynpm')
depends=("glibc")
makedepends=("go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('841583d686fa55872a4136627c0bed9d15edd6f87989a3a64ff7b28a0784254e')

build() {
  cd ${pkgname}-${pkgver}
  go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-extldflags \"${LDFLAGS}\"" \
    .
}

package() {
  cd ${pkgname}-${pkgver}
  install -Dm755 ${pkgname} ${pkgdir}/usr/bin/${pkgname}
  install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}
