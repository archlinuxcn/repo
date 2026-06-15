# Maintainer: liolok <aur@liolok.com>
# Maintainer: Mike Yuan <me@yhndnzj.com>

pkgname=hexo-cli
pkgver=4.3.2
pkgrel=1
pkgdesc="Command line interface for Hexo"
arch=('any')
url="https://www.npmjs.com/package/$pkgname"
license=('MIT')
depends=('nodejs')
makedepends=('npm')
optdepends=('git: initialize and deploy websites'
            'npm: initialize websites, install plugins'
            'pnpm: npm alternative'
            'yarn: npm alternative'
            'rsync: deploy websites')
conflicts=('nodejs-hexo' 'nodejs-hexo-cli')
replaces=('nodejs-hexo-cli')
install=newbie-hint.install
source=(https://registry.npmjs.org/$pkgname/-/$pkgname-$pkgver.tgz)
noextract=($pkgname-$pkgver.tgz)
sha256sums=('c52c27f5847579e6e57086681951c4ac9922445316c5a6ad03a8415b0846faf6')

package() {
    npm install --global "$srcdir/$pkgname-$pkgver.tgz" \
        --prefix "$pkgdir/usr" \
        --cache "$srcdir/npm-cache"

    license_file='package/LICENSE'
    tar --extract --file="$srcdir/$pkgname-$pkgver.tgz" "$license_file"
    install -Dm644 "$license_file" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    
    # Non-deterministic race in npm gives 777 permissions to random directories.
    # See https://github.com/npm/cli/issues/1103 for details.
    find "${pkgdir}/usr" -type d -exec chmod 755 {} +

    # npm gives ownership of ALL FILES to build user
    # https://bugs.archlinux.org/task/63396
    chown --recursive root:root "${pkgdir}"
}
