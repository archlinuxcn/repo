# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: John D Jones III (jnbek) <https://aur.archlinux.org/account/jnbek>

_npmname=jshint
pkgname=nodejs-"$_npmname"
pkgver=2.12.0
pkgrel=1
pkgdesc='Static analysis tool for JavaScript'
arch=('any')
url='https://jshint.com/'
license=('MIT')
depends=('nodejs')
makedepends=('npm' 'jq' 'moreutils')
source=("https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz")
sha256sums=('82a255d6580c17682f35da20bfa424299b3f9d7c734f02e97a0a32e8e1242f69')
noextract=("${source[@]##*/}")

package() {
    npm install -g --user root --cache "$srcdir/npm-cache" --prefix "$pkgdir/usr" "${source[@]##*/}"
    find "$pkgdir"/usr -type d -exec chmod 755 {} +
    find "$pkgdir" -type f -name package.json \
        -execdir sh -c "jq '. |= with_entries(select(.key | test(\"_.+\") | not))' {} | sponge {}" \;
    chown -R root:root "$pkgdir"
}
