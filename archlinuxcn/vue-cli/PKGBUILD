# Maintainer: Nick Boughton <nicholasboughton@gmail.com>
# Contributor: Jean Lucas <jean@4ray.co>

pkgname=vue-cli
pkgver=4.3.1
pkgrel=1
pkgdesc='Standard tooling for Vue.js development'
arch=(i686 x86_64)
url=https://cli.vuejs.org
license=(MIT)
depends=(nodejs)
makedepends=(npm)
optdepends=()
conflicts=(nodejs-vue-cli)
options=(!strip)

package() {
  npm install -g --prefix="$pkgdir"/usr @vue/cli@$pkgver
  find "$pkgdir"/usr -type d -exec chmod 755 {} +
}
