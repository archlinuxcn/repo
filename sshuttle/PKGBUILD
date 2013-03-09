# Maintainer: Felix Yan <felixonmars@gmail.com>
# Contributor: alphazo <alphazo@gmail.com>

pkgname=sshuttle
pkgver=0.61
pkgrel=2
pkgdesc="Transparent proxy server that works as a poor man's VPN. Forwards all TCP packets over ssh (and even DNS requests when using --dns option). Doesn't require admin privileges on the server side."
arch=('any')
url="https://github.com/apenwarr/sshuttle"
license=('GPL')
depends=('python2' 'iptables')
optdepends=('openssh: Recommended and default ssh-cmd for sshuttle')
conflicts=('sshuttle-git')

source=("$pkgname.tar.gz::https://github.com/apenwarr/$pkgname/tarball/$pkgname-$pkgver"
        "arch-install.patch")
md5sums=('5b3d85c4edbb7382b16b67f004b49518'
         '15ed72e2b68dd07ef97abfdcb828d188')

build() {
  rm -rf "$srcdir"/$pkgname
  mv "$srcdir"/apenwarr-$pkgname-* "$srcdir"/$pkgname

  cd "$srcdir"/$pkgname

  # Patch launcher with files location (/usr/share/sshuttle)
  patch -p1 -i "$srcdir/arch-install.patch"
}

package() {
  install -Dm755 "$srcdir"/$pkgname/sshuttle "$pkgdir"/usr/bin/sshuttle
  mkdir -p "$pkgdir"/usr/share/sshuttle 
  cp -r "$srcdir"/$pkgname/* "$pkgdir"/usr/share/sshuttle
}
