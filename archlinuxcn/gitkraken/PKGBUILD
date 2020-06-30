# Maintainer: Tim Kleinschmidt <tim.kleinschmidt@gmail.com>
# Contributor: Marcin Wieczorek <marcin@marcin.co>
# Contributor: Jean-Pier Brochu <jeanpier.brochu@gmail.com>
# Contributor: Samuel Littley <samuel@samuellittley.me>
# Contributor: KillWolfVlad <github.com/KillWolfVlad>
# Contributor: Victor Hugo Souza <vhbsouza@gmail.com>
# Contributor: William Penton <william@penton.us>
# Contributor: Jeff Moody <jeff@fifthecho.com>
# Contributor: KokaKiwi <kokakiwi+aur@kokakiwi.net>

pkgname=gitkraken
pkgrel=2
pkgver=7.0.1
pkgdesc="The intuitive, fast, and beautiful cross-platform Git client."
url="https://www.gitkraken.com/"
provides=('gitkraken')
arch=('x86_64')
license=('custom')
depends=('nss' 'libxtst' 'org.freedesktop.secrets' 'alsa-lib' 'libxss')
optdepends=('git-lfs: git-lfs support')
makedepends=()
backup=()
install=''
source=(
    "${pkgname}-${pkgver}.tar.gz::https://release.axocdn.com/linux/GitKraken-v${pkgver}.tar.gz"
    "GitKraken.desktop"
    "eula.html"
    "gitkraken.sh"
)
sha256sums=('0d0cb27e7daad4ca08e70c773181e89b7a0241041f6024ddfad4e21fa13ec027'
            '81b32ad2fae47fcdf8adb4fdb5c734430ed993f712e75bd62297ae8540fdf889'
            '9566342308bf35b56e626fa1b0d716eb16991712cc43b617c4f0d95e005311d1'
            '6e6c6ac37287e1ec5d5266689a49d18899488be901b21f5cb9749f545453626f')

package() {
    install -d "$pkgdir"/opt
    cp -R "$srcdir"/gitkraken "$pkgdir"/opt/gitkraken

    find "$pkgdir"/opt/gitkraken/ -type f -exec chmod 644 {} \;
    chmod 755 "$pkgdir"/opt/gitkraken/gitkraken
    chmod 755 "$pkgdir"/opt/gitkraken/resources/app.asar.unpacked/src/js/redux/domain/AskPass/AskPass.sh
    chmod 4755 "$pkgdir"/opt/gitkraken/chrome-sandbox

    install -d "$pkgdir"/usr/bin

    install -D -m755 "./gitkraken.sh" "${pkgdir}/usr/bin/gitkraken"
    install -D -m644 "./eula.html" "${pkgdir}/usr/share/licenses/${pkgname}/eula.html"
    install -D -m644 "./GitKraken.desktop" "${pkgdir}/usr/share/applications/GitKraken.desktop"
    install -D -m644 "$pkgdir/opt/gitkraken/gitkraken.png" "$pkgdir/usr/share/pixmaps/gitkraken.png"
}
