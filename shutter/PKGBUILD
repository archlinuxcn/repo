# $Id: PKGBUILD 195553 2016-11-14 01:48:18Z anthraxx $
# Maintainer: PhotonX <photon89 [at] gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Caleb Maclennan <caleb@alerque.com>
# Contributor: Shanto <shanto@hotmail.com>
# Contributor: Athurg <athurg@gooth.cn>
# Contributor: TDY <tdy@gmx.com>

pkgname=shutter
pkgver=0.93.1
pkgrel=11
pkgdesc="A featureful screenshot tool (formerly gscrot)"
arch=('any')
url="http://shutter-project.org/"
license=('GPL3')
depends=(xdg-utils imagemagick procps librsvg gnome-perl gtk2-perl desktop-file-utils
         perl-{gnome2-wnck,gtk2-{imageview,unique},x11-protocol}
         perl-{proc-{simple,processtable},net-dbus}
         perl-{sort-naturally,json,json-xs,xml-simple,www-mechanize,locale-gettext}
         perl-{file-{which,basedir,copy-recursive},xml-simple})
optdepends=('gnome-web-photo: web screenshot support'
		'perl-image-exiftool: read and write EXIF data'
		'nautilus-sendto: send screenshots via mail'
		'perl-goo-canvas: editing screenshots'
		'perl-gtk2-appindicator: AppIndicators support'
		'perl-path-class: Imgur and Dropbox upload support'
		'perl-lwp-protocol-https: Imgur and Dropbox upload support'
		'perl-net-oauth: Imgur and Dropbox upload support'
		'bc: 3D Rotate and 3D Reflection plugins support')
source=("http://shutter-project.org/wp-content/uploads/releases/tars/$pkgname-$pkgver.tar.gz"
        CVE-2015-0854.patch
        fix-dropbox.patch
        fix-unicode.patch
	  fix-second-instance-crash.patch
	  fix-imgur.patch
	  fix-mail-sendto.patch)
sha512sums=('50a635fdf73454b15351a7e2c4507bf0f9fd816273affbed412f42b1032087304ecf1fb4a4b655bc056820f267b98214ff5104f4fcd9e843f78e70ac4a7a4a04'
            '4307cdfe9409e3ff66c74730caa99932e1b8a2698012e948b974157219f4fc572117dd1968b29f6ea08736c0fa44a62cdb11855456cff8c280f4cd60edbc1ed6'
            '88fe92c33ba2e580328589d0f1f5639aa40580f96fbc92d05903167f87053d02f472d6afcc839ca18029df6fac065c108c440da551d86494c70b1219b0b032dc'
            '9fe445552ba530358a31c4ab1b03bf4e20f626f138b30e40a948340ce7de0a6549694b84e984dfd3a06b48eac94e9575fe6e6332b1af5cd92bf439bfa448b95d'
		'3b0fb654fb3338ea51cc9c1413b03186557eda54743333a36ff9ca2ffd40cdc6b3cfe58f8f7dd377351ec8e114d0ebf5c79ada8d1034375d4d5e1866114bcd4b'
		'7c7ff590237bb2bd5b54aeec7ad013542d6f64624fa16c0f129875cca908f6d8666328edd2ebf1fa80bdedc683785ba75516d8fdee9ca25b48aca117fb89baf6'
		'fe3906073b0fa0dcd5468a8ae16181d959edb691ae7c722aa4139e11baaa130fd79939162199cda09c43b5fb29d0690b602932dcaaebbea53730f5acbd89e9a1')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"

  # Fix tray icon under many icon themes, from Gentoo
  sed -e "/\$tray->set_from_icon_name/s:set_from_icon_name:set_from_file:" \
      -e "s:shutter-panel:/usr/share/icons/hicolor/scalable/apps/&.svg:" \
      -i bin/shutter
  patch -p0 < "${srcdir}/CVE-2015-0854.patch"
  patch -p0 < "${srcdir}/fix-dropbox.patch"
#  patch -p0 < "${srcdir}/fix-unicode.patch"
  patch ${srcdir}/$pkgname-$pkgver/bin/shutter < "${srcdir}/fix-unicode.patch"
#  patch -p0 < "${srcdir}/fix-second-instance-crash.patch"
  patch ${srcdir}/$pkgname-$pkgver/bin/shutter < "${srcdir}/fix-second-instance-crash.patch"
  patch -p0 < "${srcdir}/fix-imgur.patch"
  patch ${srcdir}/$pkgname-$pkgver/bin/shutter < "${srcdir}/fix-mail-sendto.patch"
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  install -Dm755 bin/$pkgname "$pkgdir/usr/bin/$pkgname"
  cp -a share "$pkgdir/usr/"
}

