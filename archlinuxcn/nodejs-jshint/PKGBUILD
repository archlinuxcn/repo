# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: John D Jones III (jnbek) <https://aur.archlinux.org/account/jnbek>

_npmname=jshint
pkgname=nodejs-"$_npmname"
pkgver=2.13.0
pkgrel=1
pkgdesc='Static analysis tool for JavaScript'
arch=(any)
url='https://jshint.com/'
license=(MIT)
depends=(nodejs)
makedepends=(npm jq moreutils)
source=("https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz")
sha256sums=('94c400d53a7247b6408bf26e22a809496f3677cce2b6a9c40528a5639e535c2d')
noextract=("${source[@]##*/}")

package() {
    npm install -g --user root --cache "$srcdir/npm-cache" --prefix "$pkgdir/usr" "${source[@]##*/}"
    find "$pkgdir"/usr -type d -exec chmod 755 {} +
    find "$pkgdir" -type f -name package.json \
        -execdir sh -c "jq '. |= with_entries(select(.key | test(\"_.+\") | not))' {} | sponge {}" \;
    chown -R root:root "$pkgdir"
}
