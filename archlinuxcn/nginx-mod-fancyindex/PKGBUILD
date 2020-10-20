# Maintainer: Mark Weiman <mark.weiman@markzz.com>
# Contributor: hdhoang <arch@hdhoang.space>

pkgname=nginx-mod-fancyindex
pkgver=0.4.4
pkgrel=2

_modname="${pkgname#nginx-mod-}"
_nginxver=1.18.0

pkgdesc='Fancy indexes module for the Nginx web server'
arch=('i686' 'x86_64')
depends=('nginx')
url="https://github.com/aperezdc/ngx-fancyindex"
license=('BSD')

source=(https://nginx.org/download/nginx-$_nginxver.tar.gz{,.asc}
        https://github.com/aperezdc/ngx-$_modname/archive/v$pkgver.tar.gz
)
validpgpkeys=(B0F4253373F8F6F510D42178520A9993A1C052F8) # Maxim Dounin <mdounin@mdounin.ru>
md5sums=('b2d33d24d89b8b1f87ff5d251aa27eb8'
         'SKIP'
         'dfd302335124520de95a7028f56d657b')

build() {
  cd "$srcdir"/nginx-$_nginxver
  ./configure --with-compat --add-dynamic-module=../ngx-$_modname-$pkgver
  make modules
}

package() {
  install -Dm644 "$srcdir/"ngx-$_modname-$pkgver/LICENSE \
                 "$pkgdir"/usr/share/licenses/$pkgname/LICENSE

  cd "$srcdir"/nginx-$_nginxver/objs
  for mod in *.so; do
    install -Dm755 $mod "$pkgdir"/usr/lib/nginx/modules/$mod
  done
}

