# Maintainer: Andrew Rabert <ar@nullsum.net>
# Contributor: Stefan Tatschner <stefan@rumpelsepp.org>
# Contributor: Ian Beringer <ian@ianberinger.com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=lf
pkgver=23
pkgrel=1
license=('MIT')
pkgdesc="A terminal file manager inspred by ranger written in Go"
depends=('glibc')
makedepends=('go')
arch=('aarch64' 'armv7h' 'i686' 'x86_64')
url="https://github.com/gokcehan/lf"
source=("$pkgname-r$pkgver.tar.gz::https://github.com/gokcehan/$pkgname/archive/r$pkgver.tar.gz")
sha256sums=('ae3a7d11e0b87ddb9fef2dc61de4c6f648039138fc69975cbdbd9fe126daa71c')

prepare() {
  # prevent creation of a `go` directory in one's home.
  # this directory cannot be removed with even `rm -rf` unless one becomes root
  # or changes the write permissions.
  export GOPATH="${srcdir}/gopath"
  go clean -modcache
}

build() {
  cd "${pkgname}-r${pkgver}"
  go mod vendor
  version=r$pkgver ./gen/build.sh \
      -buildmode=pie \
      -mod=vendor \
      -modcacherw \
      -trimpath
  # clean now to ensure makepkg --clean works
  go clean -modcache
}

package() {
  cd "${pkgname}-r${pkgver}"
  install -Dm755 -t "${pkgdir}/usr/bin" \
      ./lf

  install -Dm644 -t "${pkgdir}/usr/share/applications" \
      ./lf.desktop

  install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
      ./LICENSE

  install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
      ./README.md \
      ./etc/lfrc.example
  install -Dm644 -t "${pkgdir}/usr/share/${pkgname}" \
      ./etc/lfcd.sh

  install -Dm644 -t "${pkgdir}/usr/share/man/man1" \
      ./lf.1

  # vim
  install -Dm644 -t "${pkgdir}/usr/share/vim/vimfiles/syntax" \
      ./etc/lf.vim
  install -Dm644 -t "${pkgdir}/usr/share/vim/vimfiles/ftdetect" \
      ./etc/lf.vim

  # fish
  install -Dm644 -t "${pkgdir}/usr/share/fish/vendor_completions.d" \
      ./etc/lf.fish
  install -Dm644 -t "${pkgdir}/usr/share/fish/vendor_functions.d" \
      ./etc/lfcd.fish

  # zsh
  install -Dm644 -T ./etc/lf.zsh "${pkgdir}/usr/share/zsh/site-functions/_lf"

  # tsch
  install -Dm644 -t "${pkgdir}/etc/profile.d" \
       ./etc/lf.csh \
       ./etc/lfcd.csh
}
