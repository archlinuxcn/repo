pkgname='enpass-bin'
_pkgname='enpass'
pkgver=5.6.9
pkgrel=3
pkgdesc='A multiplatform password manager'
arch=('x86_64')
url='http://enpass.io/'
license=('custom')
depends=('libxss' 'lsof')
provides=("${_pkgname}")
install='enpass-bin.install'
source=("http://repo.sinew.in/pool/main/e/enpass/${_pkgname}_${pkgver}_amd64.deb")
sha256sums=('46f13df93ac8e0637428b86fa0fa6c2809dd1ff0b29a678d991f2cf5daed9e84')

# Disable strip as otherwise the browser extension will not work
options=('!strip')

package() {
    # Extract data
    tar xfz "${srcdir}/data.tar.gz" -C "${pkgdir}"

    # Remove unnecessary files which are included in the .deb
    find "${pkgdir}" -name '*~' -delete

    # Update permissions to match the default system ones
    chmod 755 "${pkgdir}/opt/"
    find "${pkgdir}/usr/" -type d -exec chmod 755 {} \;

    # Symlink "runenpass.sh" to "/usr/bin" so it is accessible via cli
    mkdir -p "${pkgdir}/usr/bin"
    ln -s '/opt/Enpass/bin/runenpass.sh' "${pkgdir}/usr/bin/enpass"
}


# vim: set syntax=sh:
