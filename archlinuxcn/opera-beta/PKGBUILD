# Maintainer: BlackEagle
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: ruario 
# Contributor: RobertMe
# Contributor: Skunnyk
# Contributor: totoloco

pkgname=opera-beta
pkgver=62.0.3331.14
pkgrel=1
pkgdesc='A fast and secure web browser and Internet suite - beta stream'
arch=('x86_64')
url='https://www.opera.com/computer'
license=('custom:opera')
provides=('opera')
depends=('gtk3' 'alsa-lib' 'libnotify' 'curl' 'nss' 'libxss' 'ttf-font' 'desktop-file-utils' 'shared-mime-info' 'hicolor-icon-theme')
optdepends=(
    'opera-beta-ffmpeg-codecs: playback of proprietary video/audio'
    'pepper-flash: flash support'
    'upower: opera battery save'
)
source=(
    "http://deb.opera.com/opera/pool/non-free/o/${pkgname}/${pkgname}_${pkgver}_amd64.deb"
    "opera"
    "default"
)
sha256sums=('e42ec3077b1380588a56e1ebe3989a89c18e13a9bd86d5fdcb9b6a79cf376e12'
            '508512464e24126fddfb2c41a1e2e86624bdb0c0748084b6a922573b6cf6b9c5'
            '99fc0d2822edd14e234d451995db47148125e4580221a292598959421d131231')

prepare() {
    sed -e "s/%pkgname%/$pkgname/g" -i "$srcdir/opera"
    sed -e "s/%operabin%/$pkgname\/$pkgname/g" \
        -i "$srcdir/opera"

}

package() {
    tar -xf data.tar.xz --exclude=usr/share/{lintian,menu} -C "$pkgdir/"

	# get rid of the extra subfolder {i386,x86_64}-linux-gnu
	(
        cd "$pkgdir/usr/lib/"*-linux-gnu/
        mv "$pkgname" ../
	)
    rm -rf "$pkgdir/usr/lib/"*-linux-gnu

    # suid opera_sandbox
    chmod 4755 "$pkgdir/usr/lib/$pkgname/opera_sandbox"

	# install default options
    install -Dm644 "$srcdir/default" "$pkgdir/etc/$pkgname/default"

	# install opera wrapper
    rm "$pkgdir/usr/bin/$pkgname"
    install -Dm755 "$srcdir/opera" "$pkgdir/usr/bin/$pkgname"

	# license
	install -Dm644 \
        "$pkgdir/usr/share/doc/$pkgname/copyright" \
        "$pkgdir/usr/share/licenses/$pkgname/copyright"
}

