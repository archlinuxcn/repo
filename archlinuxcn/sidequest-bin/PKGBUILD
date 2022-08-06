# Maintainer: Adam Goldsmith <contact@adamgoldsmith.name>
# Former Maintainer: BeeJay

pkgname=sidequest-bin
_pkgname=sidequest
pkgver=0.10.31
pkgrel=1
pkgdesc="Easily sideload apps onto your standalone android VR headset"
arch=('x86_64')
url="https://github.com/SideQuestVR/SideQuest"
license=('MIT')
depends=(gtk3 libxss nss android-udev)
provides=("$_pkgname")
conflicts=("$_pkgname")
source=("https://github.com/SideQuestVR/SideQuest/releases/download/v${pkgver}/SideQuest-${pkgver}.tar.xz"
        "SideQuest.desktop")
sha256sums=('31762ea9c06f7a6ff7399660889baae403f882c94c361972e6c64bfd8695c5a3'
            '312c6258c15e3c87e0fdad6f46537c98f0cc6aa364405858a0190ad2c8f5fa2d')

package() {
	cd "$srcdir/SideQuest-${pkgver}"

	install -dm755 "$pkgdir/opt/$_pkgname"
	cp -r -t "$pkgdir/opt/$_pkgname" .

	install -dm755 "$pkgdir/usr/bin"
	ln -s /opt/$_pkgname/sidequest "$pkgdir/usr/bin/sidequest"

    for res in 256x256 16x16 1024x1024 32x32 48x48 128x128 24x24 64x64 512x512
    do
        install -dm755 "${pkgdir}/usr/share/icons/hicolor/$res/apps/"
        ln -s "/opt/$_pkgname/resources/app.asar.unpacked/build/icons/$res.png" "${pkgdir}/usr/share/icons/hicolor/$res/apps/${_pkgname}.png"
    done

    install -Dm644 -t "$pkgdir/usr/share/licenses/$_pkgname" LICENSE*

    install -Dm644 "$srcdir/SideQuest.desktop" "${pkgdir}/usr/share/applications/SideQuest.desktop"
}
