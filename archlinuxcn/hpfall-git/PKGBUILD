# Maintainer: Eric Waller <ewwaller+aur gmail com>

pkgname=hpfall-git
pkgver=r5.be24a8b
pkgrel=2
pkgdesc="Disk protection for HP machines."
arch=('x86_64' 'i686')
url="https://github.com/srijan/hpfall.git"
license=('GPL2')
depends=('glibc')
makedepends=('git')
md5sums=('SKIP'  3a6a193021fe5f3078f97b8c2a4c8538 ac946477d1996e68fa63792829fd8a97)

source=("git+${url}" 'log_to_syslog.patch' 'hpfall.service')

pkgver() {
  cd "${srcdir}/${pkgname%-git}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare(){
  cd "${srcdir}/${pkgname%-git}"
  patch -R hpfall.c < ../log_to_syslog.patch
}

build() {
  cd "${srcdir}/${pkgname%-git}"
  make
} 

package() {
  install -Dm755 "${pkgname%-git}/hpfall" "${pkgdir}/usr/bin/hpfall"
  install -Dm644 hpfall.service "${pkgdir}/usr/lib/systemd/system/hpfall.service"

}
