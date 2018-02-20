#Maintainer : Sasasu <lizhaolong0123@gmail.com>
pkgname=uget-chrome-wrapper
pkgver=2.0.7
pkgrel=7
pkgdesc="Integrate uGet Download Manager with Google Chrome, Chromium, Vivaldi, Opera and Firefox"
arch=('any')
url="https://github.com/slgobinath/uget-chrome-wrapper"
license=('GPL3')
replaces=('uget-integrator')
conflicts=('uget-integrator')
depends=('python3' 'uget')
makedepends=()
source=("uget-chrome-wrapper-$pkgver::https://raw.githubusercontent.com/slgobinath/uget-chrome-wrapper/v$pkgver/uget-chrome-wrapper/bin/uget-chrome-wrapper"
        "ugetchromewrapper-$pkgver::https://raw.githubusercontent.com/slgobinath/uget-chrome-wrapper/v$pkgver/uget-chrome-wrapper/conf/com.javahelps.ugetchromewrapper.json"
        "ugetfirefoxwrapper-$pkgver::https://raw.githubusercontent.com/slgobinath/uget-chrome-wrapper/v$pkgver/uget-chrome-wrapper/conf/com.javahelps.ugetfirefoxwrapper.json")
md5sums=('3db3e88a3b9f9585ac66c6d13c5fc7b7'
         '7c185094db349599f8375866796db33a'
         '4806bc4553389cc0610e642b12510246')
install=uget-chrome-wrapper.install
build() {
	cd "$srcdir"/"$_pkgname"
}
package() {
	cd "$srcdir"/"$_pkgname"
	mkdir -p "$pkgdir/usr/bin"
	install -m755 "uget-chrome-wrapper-$pkgver" "$pkgdir"/usr/bin/uget-chrome-wrapper
	
	#for Google Chrome if you not use Google Chrome please delete them
	mkdir -p "$pkgdir/etc/opt/chrome/native-messaging-hosts"
	install -m644 "ugetchromewrapper-$pkgver" "$pkgdir"/etc/opt/chrome/native-messaging-hosts/com.javahelps.ugetchromewrapper.json
	
	#for Chromium and Vivaldi if you not use Chromium or Vivaldi please delete them
	mkdir -p "$pkgdir/etc/chromium/native-messaging-hosts"
	install -m644 "ugetchromewrapper-$pkgver" "$pkgdir"/etc/chromium/native-messaging-hosts/com.javahelps.ugetchromewrapper.json
	
	#for Opera if you not use Opera please delete them
	mkdir -p "$pkgdir/etc/opera/native-messaging-hosts"
	install -m644 "ugetchromewrapper-$pkgver" "$pkgdir"/etc/opera/native-messaging-hosts/com.javahelps.ugetchromewrapper.json

	#for Firefox if you not use Firefox please delete them
	mkdir -p "$pkgdir/usr/lib/mozilla/native-messaging-hosts"
	install -m644 "ugetfirefoxwrapper-$pkgver" "$pkgdir"/usr/lib/mozilla/native-messaging-hosts/com.javahelps.ugetfirefoxwrapper.json
}
