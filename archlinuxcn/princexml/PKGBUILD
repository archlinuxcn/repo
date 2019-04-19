# Current Maintainer: Harry Jeffery <harry|@|exec64|.|co|.|uk>
# Previous Maintainer: Chris Morgan <me@chrismorgan.info>

pkgname=princexml
pkgver=12.5
pkgrel=1
pkgdesc="Convert HTML documents to PDF with CSS"
arch=(i686 x86_64)
url="http://www.princexml.com/"
depends=(fontconfig libidn libxml2 ca-certificates-utils)
conflicts=(sdlpop)
license=(custom)

source_i686=(http://www.princexml.com/download/prince-${pkgver}-linux-generic-i686.tar.gz)
source_x86_64=(http://www.princexml.com/download/prince-${pkgver}-linux-generic-x86_64.tar.gz)
sha256sums_i686=('68bf1439a53efc26ac84e3fb3ded09c8cfa2a12d801a1a56d56a58ac7f183254')
sha256sums_x86_64=('463136f95962687d5a95b817c5218e25c2ed9fe9df8b158c0cb5a92adc8c675a')

package() {
	mkdir -p "$pkgdir/opt/prince"

	cd "${srcdir}/prince-${pkgver}-linux-generic-${CARCH}/lib/prince"
	for file in `find -type f`; do
		if [ -x "$file" ]; then
			install -D "$file" "$pkgdir/opt/prince/$file"
		else
			install -D -m 644 "$file" "$pkgdir/opt/prince/$file"
		fi
	done

	mkdir -p "$pkgdir/usr/bin"
	echo "#!/bin/sh" > "$pkgdir/usr/bin/prince"
	echo 'exec /opt/prince/bin/prince --prefix=/opt/prince "$@"' >> "$pkgdir/usr/bin/prince"
	chmod +x "$pkgdir/usr/bin/prince"

	# It provides its own CA certificates bundle, but we want to use our own one.
	# (This is the cause of the ca-certificates-utils dependency.)
	ln -sf ../../../etc/ssl/certs/ca-certificates.crt "${pkgdir}/opt/prince/etc/curl-ca-bundle.crt"

	cd ../..
	install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
