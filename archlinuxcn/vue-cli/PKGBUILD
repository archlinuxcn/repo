# Maintainer: Nick Boughton <nicholasboughton@gmail.com>
# Contributor: Jean Lucas <jean@4ray.co>
# Contributor: GFdevelop

_npmscope=vue
_npmname=cli
_npmid="@$_npmscope/$_npmname"

pkgname="${_npmscope}-${_npmname}"
pkgver=4.5.12
pkgrel=2
pkgdesc='Standard tooling for Vue.js development'
arch=('any')
url='https://cli.vuejs.org'
license=('MIT')
depends=('nodejs')
makedepends=('npm')
optdepends=()
conflicts=('nodejs-vue-cli' 'vue')
source=("$pkgname-$pkgver.tar.gz::https://registry.npmjs.org/$_npmid/-/$_npmname-$pkgver.tgz")
noextract=("${source[@]%%::*}")
sha1sums=($(curl -s "https://registry.npmjs.org/@vue/cli" | jq ".versions.\"${pkgver}\".dist.shasum" | sed s/\"//g))

package() {
  mkdir -p "${pkgdir}"/usr/lib

  # Setting temporary cache
  npm install -g --cache "$srcdir/npm-cache" --prefix "$pkgdir/usr" "${source[@]%%::*}"

  # Non-deterministic race in npm gives 777 permissions to random directories.
  # See https://github.com/npm/npm/issues/9359 for details.
  find "${pkgdir}"/usr -type d -execdir chmod 755 {} \+

  # npm gives ownership of ALL FILES to build user
  # https://bugs.archlinux.org/task/63396
  chown -R root:root $pkgdir

  # Package contains reference to $srcdir/$pkgdir
  find "${pkgdir}" -type f -name package.json -execdir sed -i '/_where/d' {} \+

  sed -i "s|$pkgdir||" "$pkgdir"/usr/lib/node_modules/"$_npmid"/node_modules/sshpk/package.json

  # Add license
  install -Dm644 "$pkgdir/usr/lib/node_modules/$_npmid/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
