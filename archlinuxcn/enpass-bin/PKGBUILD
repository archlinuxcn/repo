pkgname='enpass-bin'
_pkgname='enpass'
pkgver=6.4.1.643
pkgrel=2
pkgdesc='A multiplatform password manager'
arch=('x86_64')
url='http://enpass.io/'
license=('custom')
depends=('libxss' 'lsof' 'curl' 'libxkbcommon-x11')
optdepends=('libxdg-basedir: Open links in the default browser.'
            'libqtxdg: Open links in the default browser (Qt implementation)')
provides=("${_pkgname}")
install='enpass-bin.install'
source=("https://apt.enpass.io/pool/main/e/enpass/${_pkgname}_${pkgver}_amd64.deb")
sha256sums=('c44ec92302775d86ccde48d91f0f0e7c0228b720be61e54299e1be4bc0c06268')

# Disable strip as otherwise the browser extension will not work
options=('!strip')

package() {
    # Extract data
    tar xfz "${srcdir}/data.tar.gz" -C "${pkgdir}"

    # Remove unnecessary files which are included in the .deb
    # find "${pkgdir}" -name '*~' -delete

    # Update permissions to match the default system ones
    chmod 755 "${pkgdir}/opt/"
    find "${pkgdir}/usr/" -type d -exec chmod 755 {} \;

    # Symlink "runenpass.sh" to "/usr/bin" so it is accessible via cli
    mkdir -p "${pkgdir}/usr/bin"
    ln -s '/opt/enpass/Enpass' "${pkgdir}/usr/bin/enpass"
}


# vim: set syntax=sh:
