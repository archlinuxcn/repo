# Maintainer: Posi<posi1981@gmail.com>
pkgname=betterbird-bin
_pkgname=betterbird
pkgver=140.9.0esr
_build=bb20
pkgrel=1
pkgdesc="EN-US // Betterbird is a fine-tuned version of Mozilla Thunderbird, Thunderbird on steroids, if you will."
arch=('x86_64')
url="https://www.betterbird.eu/index.html"
license=('MPL2')
depends=('dbus-glib' 'hunspell')
optdepends=('hunspell-en_US')
provides=("betterbird=${pkgver}")
conflicts=()
source=(
    "https://www.betterbird.eu/downloads/LinuxArchive/${_pkgname}-${pkgver}-${_build}.en-US.linux-x86_64.tar.xz"
    "eu.betterbird.Betterbird.desktop"
    "vendor-prefs.js"
)

package() {
    install -d "${pkgdir}/opt"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/applications"

    cp -r "${srcdir}/${_pkgname}/" "${pkgdir}/opt/${_pkgname}"
    install -m644 "${srcdir}/eu.${_pkgname}.Betterbird.desktop" "${pkgdir}/usr/share/applications/eu.${_pkgname}.Betterbird.desktop"
    install -m644 "${srcdir}/vendor-prefs.js" -t "${pkgdir}/opt/${_pkgname}/defaults/pref"
    ln -s /opt/$_pkgname/betterbird "$pkgdir"/usr/bin/$_pkgname
    ln -s /usr/share/hunspell "${pkgdir}/opt/${_pkgname}/dictionaries"

    echo     "

	  >>>>>    Please don't forget to cast a vote for this package. THANKS
	  >>>>>    https://aur.archlinux.org/packages/betterbird-bin

	  "

    #icons
    for i in 16 22 24 32 48 64 128 256; do
        install -d "$pkgdir"/usr/share/icons/hicolor/${i}x${i}/apps/
        ln -s /opt/$_pkgname/chrome/icons/default/default$i.png \
            "$pkgdir"/usr/share/icons/hicolor/${i}x${i}/apps/$_pkgname.png
    done
}
sha256sums=('62d040cb5bf3e7d35ece4d26700f9324f3e17367648421e5e177c7d19a393024'
            '60045ec0138ad4c01546df596b97016e467bec6d69c7e4e4c7bdb85e91a31bc2'
            'b11745416d2b2f8bac1ccd3dcb99411c7239b067adf9eb973903c448f8747d09')
