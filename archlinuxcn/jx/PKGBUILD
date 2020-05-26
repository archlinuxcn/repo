# Maintainer: David Birks <david@birks.dev>
# Contributor: Jacob Mason <jacob@jacobmason.net>

pkgname=jx
pkgver=2.1.46
pkgrel=1
pkgdesc='Command line tool for working with Jenkins X'
arch=('x86_64')
url='https://github.com/jenkins-x/jx'
license=('Apache')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/jenkins-x/jx/archive/v$pkgver.tar.gz")
sha256sums=('7e69544f2648c4e5d16805dd0efc9f8eab4f08c439ca2711d29a9ca3502358c6')

build() {
  cd $pkgname-$pkgver
  export VERSION=$pkgver
  make build
}

package() {
  install -Dm 755 "${srcdir}/$pkgname-$pkgver/build/jx" "${pkgdir}/usr/bin/jx"

  # Populate bash and zsh completions
  install -dm 755 "${pkgdir}/usr/share/bash-completion/completions"
  install -dm 755 "${pkgdir}/usr/share/zsh/site-functions"
  "${pkgdir}/usr/bin/jx" completion bash > "${pkgdir}/usr/share/bash-completion/completions/jx"
  "${pkgdir}/usr/bin/jx" completion zsh >  "${pkgdir}/usr/share/zsh/site-functions/_jx"
}
