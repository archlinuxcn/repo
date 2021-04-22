# Maintainer: BlackEagle
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: ruario
# Contributor: RobertMe
# Contributor: Skunnyk
# Contributor: totoloco

pkgname=opera-beta
pkgver=76.0.4017.59
pkgrel=1
pkgdesc='A fast and secure web browser and Internet suite - beta stream'
arch=('x86_64')
url='https://www.opera.com/computer'
license=('custom:opera')
provides=('opera')
depends=('gtk3' 'alsa-lib' 'libnotify' 'curl' 'nss' 'libxss' 'ttf-font' 'desktop-file-utils' 'shared-mime-info' 'hicolor-icon-theme')
optdepends=(
    'opera-beta-ffmpeg-codecs: playback of proprietary video/audio'
    'upower: opera battery save'
)
source=(
    "https://get.geo.opera.com/pub/${pkgname}/${pkgver}/linux/${pkgname}_${pkgver}_amd64.rpm"
    "opera"
    "default"
)
sha256sums=('54182254528ddc0be864438a8e12f7e6369d031ffda8a2c3324c53e3f37226c7'
            '508512464e24126fddfb2c41a1e2e86624bdb0c0748084b6a922573b6cf6b9c5'
            '99fc0d2822edd14e234d451995db47148125e4580221a292598959421d131231')

prepare() {
    sed -e "s/%pkgname%/$pkgname/g" -i "$srcdir/opera"
    sed -e "s/%operabin%/$pkgname\/$pkgname/g" \
        -i "$srcdir/opera"

}

package() {
    install -dm755 "$pkgdir/usr"
    cp -a usr/share "$pkgdir/usr/"
    cp -a usr/lib64 "$pkgdir/usr/lib"

    # suid opera_sandbox
    chmod 4755 "$pkgdir/usr/lib/$pkgname/opera_sandbox"

	# install default options
    install -Dm644 "$srcdir/default" "$pkgdir/etc/$pkgname/default"

	# install opera wrapper
    #rm "$pkgdir/usr/bin/$pkgname"
    install -Dm755 "$srcdir/opera" "$pkgdir/usr/bin/$pkgname"

	# license
	#install -Dm644 \
        #"$pkgdir/usr/share/doc/$pkgname/copyright" \
        #"$pkgdir/usr/share/licenses/$pkgname/copyright"
}

