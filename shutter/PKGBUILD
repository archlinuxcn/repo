# Maintainer: Caleb Maclennan <caleb@alerque.com>
#
# Contributor: Shanto <shanto@hotmail.com>
# Contributor: Athurg <athurg@gooth.cn>
# Contributor: TDY <tdy@gmx.com>
#
# Any suggestions welcome; please submit paches via Github:
# https://github.com/alerque/aur/tree/master/git-annex-bin

pkgname=shutter
pkgver=0.91
pkgrel=1
pkgdesc="a featureful screenshot tool (formerly gscrot)"
arch=('i686' 'x86_64')
url="http://shutter-project.org/"
license=('GPL3')
depends=(
	xdg-utils libxml-perl imagemagick bc procps librsvg gnome-perl
	perl-{gnome2-wnck,gtk2-{imageview,unique,appindicator},x11-protocol,image-exiftool}
	perl-{proc-{simple,processtable},net-{dbus,dropbox-api},goo-canvas}
	perl-{sort-naturally,json,json-xs,xml-simple,www-mechanize,locale-gettext}
	perl-{file-{which,basedir,copy-recursive},path-class}
)
optdepends=(
	'nautilus-sendto: "Send To" functionality in right-click and main menu'
	'perl-net-dbus-glib: Upload support for Ubuntu One'
	'gnome-web-photo: Support for capturing websites'
)
    #'perl-gtk2-appindicator: AppIndicator support'
source=("http://shutter-project.org/wp-content/uploads/releases/tars/$pkgname-$pkgver.tar.gz")

package() {
	cd "$srcdir/$pkgname-$pkgver"
	install -Dm755 bin/$pkgname "$pkgdir/usr/bin/$pkgname"
	cp -r share "$pkgdir/usr/"

	find "$pkgdir/usr/share" -type d -exec chmod 755 '{}' \;
	find "$pkgdir/usr/share" -type f -exec chmod 644 '{}' \;
	find "$pkgdir" -path '*plugins*' -type f ! -name '*.*' -exec chmod 755 '{}' \;
	find "$pkgdir" -path '*/upload_plugins/*' -type f -name '*.pm' -exec chmod 755 '{}' \;
}

md5sums=('9775b904dd4e75b87f5e51bb861c74ad')
