#Maintainer : Sasasu <lizhaolong0123@gmail.com>
pkgname=uget-chrome-wrapper
pkgver=2.0.5
pkgrel=1
pkgdesc="Integrate uGet Download Manager with Google Chrome, Chromium, Vivaldi, Opera and Firefox"
arch=('any')
url="https://github.com/slgobinath/uget-chrome-wrapper"
license=('GPL3')
depends=('python3' 'uget')
makedepends=()
source=("https://raw.githubusercontent.com/slgobinath/uget-chrome-wrapper/v$pkgver/uget-chrome-wrapper/bin/uget-chrome-wrapper"
        "https://raw.githubusercontent.com/slgobinath/uget-chrome-wrapper/v$pkgver/uget-chrome-wrapper/conf/com.javahelps.ugetchromewrapper.json"
        "https://raw.githubusercontent.com/slgobinath/uget-chrome-wrapper/v$pkgver/uget-chrome-wrapper/conf/com.javahelps.ugetfirefoxwrapper.json")
md5sums=('d824ef742a548a5613caadbad78475f2'
         '7c185094db349599f8375866796db33a'
         '4806bc4553389cc0610e642b12510246')
install=uget-chrome-wrapper.install
build() {
	cd "$srcdir"/"$_pkgname"
}
package() {
	cd "$srcdir"/"$_pkgname"
	mkdir -p "$pkgdir/usr/bin"
	install -Dm755 "uget-chrome-wrapper" "$pkgdir"/usr/bin
	
	#for Google Chrome if you not use Google Chrome please delete them
	mkdir -p "$pkgdir/etc/opt/chrome/native-messaging-hosts"
	install -Dm644 "com.javahelps.ugetchromewrapper.json" "$pkgdir"/etc/opt/chrome/native-messaging-hosts
	
	#for Chromium and Vivaldi if you not use Chromium or Vivaldi please delete them
	mkdir -p "$pkgdir/etc/chromium/native-messaging-hosts"
	install -Dm644 "com.javahelps.ugetchromewrapper.json" "$pkgdir"/etc/chromium/native-messaging-hosts
	
	#for Opera if you not use Opera please delete them
	mkdir -p "$pkgdir/etc/opera/native-messaging-hosts"
	install -Dm644 "com.javahelps.ugetchromewrapper.json" "$pkgdir"/etc/opera/native-messaging-hosts

	#for Firefox if you not use Firefox please delete them
	mkdir -p "$pkgdir/usr/lib/mozilla/native-messaging-hosts"
	install -Dm644 "com.javahelps.ugetfirefoxwrapper.json" "$pkgdir"/usr/lib/mozilla/native-messaging-hosts
}
