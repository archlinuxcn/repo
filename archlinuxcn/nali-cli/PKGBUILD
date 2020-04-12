# Maintainer: Hao Long <aur@esd.cc>

pkgname=nali-cli
pkgver=2.1.2
pkgrel=1
pkgdesc="Parse geoinfo of IP Address without leaving your terminal"
arch=('any')
url="https://nali.skk.moe/"
license=('GPL')
depends=('nodejs')
optdepends=('bind-tools: nali-dig / nali-nslookup support'
            'iputils: nali-ping / nali-tracepath support'
            'traceroute: nali-traceroute support')
makedepends=('npm')
source=("https://registry.npmjs.org/$pkgname/-/$pkgname-$pkgver.tgz"
        "https://github.com/SukkaW/nali-cli/raw/master/LICENSE")
noextract=($pkgname-$pkgver.tgz)
sha256sums=('48f48419fcda4c64048cdf2a9d30e25ed1d42cda363ee6317b784d5ab4decb65'
            '3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986')

package() {
  npm install -g --user root --prefix "$pkgdir"/usr "$srcdir"/$pkgname-$pkgver.tgz

  # Non-deterministic race in npm gives 777 permissions to random directories.
  # See https://github.com/npm/npm/issues/9359 for details.
  find "${pkgdir}"/usr -type d -exec chmod 755 {} +

  # npm installs package.json owned by build user
  # https://bugs.archlinux.org/task/63396
  chown -R root:root "$pkgdir"

  install -Dm644 "$srcdir"/LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
