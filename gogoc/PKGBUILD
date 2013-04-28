# Maintainer: Ivan Gasperoni <gulpegaspe at gmail dot com>
pkgname=gogoc
pkgver=1.2
pkgrel=16
pkgdesc="Client to connect to the Freenet6 IPv6 tunnel broker service"
arch=('i686' 'x86_64')
url="http://www.gogo6.com/profile/gogoCLIENT"
license=('custom')
depends=('openssl' 'net-tools' 'patch' 'systemd')
conflicts=('gw6c')
backup=('opt/gogoc/bin/gogoc.conf')
options=(!makeflags)
source=(http://content.gogo6.com/gogoc-1_2-RELEASE.tar.gz
	gogocd
	gogoc
	gogoc.patch
	clientmsgsender.patch
	servermsgsender.patch
	tspauthpassdss.patch
	gogoc.service)
install=gogoc.install
md5sums=('41177ed683cf511cc206c7782c37baa9'
         '5fe3fd2b3d20eb08e2a0dede22ab8c67'
         'b1296b8b5adf195f13a581dcdfa6f889'
         'b40b3e2da5dafb5564a634b7867a9b69'
         '842b6ae576d2795d014971039aaa05cc'
         '4f6e69890161142220268181d4f915cf'
         '71ba26961540368c45df2630ce74a99a'
         '9ac7ae529a31a13855df7e03cf00940d')

build() {
	cd "$srcdir/gogoc-1_2-RELEASE/gogoc-messaging/src"
	patch -p0 < "$srcdir/../clientmsgsender.patch" || return 1
	patch -p0 < "$srcdir/../servermsgsender.patch" || return 1
	cd "$srcdir/gogoc-1_2-RELEASE/gogoc-tsp/src/tsp"
	patch -p0 < "$srcdir/../tspauthpassdss.patch" || return 1
	cd "$srcdir/gogoc-1_2-RELEASE"
	make platform=linux all || return 1
}
         
package() {
	cd "$srcdir/gogoc-1_2-RELEASE"
	make platform=linux installdir="$pkgdir/opt/$pkgname/" install
	sed -i -e "s/^gogoc_dir=.*/gogoc_dir=\/opt\/gogoc\//" "$pkgdir/opt/$pkgname/bin/gogoc.conf"
	sed -i -e "s/^gogoc_dir=.*/gogoc_dir=/" "$pkgdir/opt/$pkgname/bin/gogoc.conf.sample"
	sed -i -e "s/ipconfig=\/sbin\/ip/ipconfig=\/usr\/sbin\/ip/" "$pkgdir/opt/$pkgname/template/linux.sh"
	sed -i -e "s#rtadvd_pid=.*#rtadvd_pid=/var/run/radvd.pid#" "$pkgdir/opt/$pkgname/template/linux.sh"
	sed -i -e "s#/etc/init.d/radvd#/etc/rc.d/radvd#" "$pkgdir/opt/$pkgname/template/linux.sh"
	sed -i -e "s#Exec \$rtadvd -u radvd#Exec \$rtadvd#" "$pkgdir/opt/$pkgname/template/linux.sh"
	cd "$pkgdir/opt/$pkgname/bin"
	patch -p1 < "$srcdir/../gogoc.patch" || return 1
	mkdir -p "$pkgdir/usr/bin"
	mkdir -p "$pkgdir/etc/$pkgname"
	mkdir -p "$pkgdir/usr/share/licenses/$pkgname"
	mkdir -p "$pkgdir/usr/lib/systemd/system"
	ln -s "/opt/$pkgname/bin/gogoc.conf" "/$pkgdir/etc/$pkgname/"
	ln -s "/opt/$pkgname/bin/gogoc.conf.sample" "/$pkgdir/etc/$pkgname/"
	install -m 755 "$srcdir/gogoc" "$pkgdir/usr/bin/"
	install -m 644 "$srcdir/gogoc-1_2-RELEASE/CLIENT-LICENSE.TXT" "$pkgdir/usr/share/licenses/$pkgname/"
	install -m 644 "$srcdir/gogoc.service" "$pkgdir/usr/lib/systemd/system/"
}
