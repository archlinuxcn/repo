pkgname='enpass-beta-bin'
_pkgname='enpass'
pkgver=6.0.0.228
pkgrel=1
pkgdesc='A multiplatform password manager'
arch=('x86_64')
url='http://enpass.io/'
license=('custom')
depends=('libxss' 'lsof')
provides=("${_pkgname}")
conflicts=('enpass-bin')
install='enpass-beta-bin.install'
source=("http://repo.sinew.in/testing/pool/beta/e/enpass/${_pkgname}_${pkgver}_amd64.deb")
sha256sums=('416838d5e40c25fc359e648af7373ef8d71d4fc87d6e6a10d6bac1f67961ac04')

# Disable strip as otherwise the browser extension will not work
#options=('!strip')

package() {
    # Extract data
    tar xfz "${srcdir}/data.tar.gz" -C "${pkgdir}"

    # Update permissions to match the default system ones
    chmod 755 "${pkgdir}/opt/"
    find "${pkgdir}/usr/" -type d -exec chmod 755 {} \;

    # Symlink "runenpass.sh" to "/usr/bin" so it is accessible via cli
    mkdir -p "${pkgdir}/usr/bin"
    ln -s '/opt/enpass/Enpass' "${pkgdir}/usr/bin/enpass"
}


# vim: set syntax=sh:
