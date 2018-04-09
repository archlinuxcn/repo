# Maintainer: Trizen <echo dHJpemVuQHByb3Rvbm1haWwuY29tCg== | base64 -d>

pkgname=trizen
pkgver=1.47
pkgrel=1
epoch=1
pkgdesc="Trizen AUR Package Manager: A lightweight wrapper for AUR."
arch=('any')
url="https://github.com/trizen/${pkgname}"
license=('GPL3')

depends=(
         'git'
         'pacutils'
         'perl>=5.20.0'
         'perl-libwww'
         'perl-term-ui'
         'pacman'
         'perl-json'
         'perl-data-dump'
         'perl-lwp-protocol-https'
         'perl-term-readline-gnu'
        )

optdepends=(
            'perl-json-xs: faster JSON deserialization'
            #'perl-term-readline-gnu: better STDIN support'
           )

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/trizen/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('3fea8be81f2bff211f8539d274d048ac280dd5f840d8055438c131d4f83928ec')

package() {
  cd "$pkgname-$pkgver"
  install -m 755 -D $pkgname "$pkgdir/usr/bin/$pkgname"
  install -m 644 -D "zsh.completion" "$pkgdir/usr/share/zsh/site-functions/_trizen"
  install -m 644 -D "bash.completion" "$pkgdir/usr/share/bash-completion/completions/trizen"
}
