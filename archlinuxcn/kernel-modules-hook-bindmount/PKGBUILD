# Maintainer: Jerry Xiao <aur at mail.jerryxiao.cc>
# Contributor: Max Gautier <mg+archlinux@max.gautier.name>
# Contributor: Artoria Pendragon <saber-nyan@ya.ru>
_pkgname=kernel-modules-hook
pkgname=${_pkgname}-bindmount
pkgver=0.2.4
pkgrel=1
pkgdesc="Keeps your system fully functional after a kernel upgrade"
arch=('any')
provides=("$_pkgname")
conflicts=("$_pkgname" "${_pkgname}-hardlinks")
url="https://github.com/archlinux-jerry/pkgbuilds/tree/master/kernel-modules-hook-bindmount"
license=('GPL3')
source=("linux-modules-cleanup.conf"
        "10-linux-modules-pre.hook"
        "61-linux-modules-post.hook"
        "linux-modules-restore"
        "linux-modules-save"
)
sha256sums=('cfc97c05f0a178574505f2c31b30b2e771546e8223e58a37d9273793faa484b8'
            'c3f75396f98caf9b13511290e29ce9d1d6827999ca49f0eca6c44a6702fd8d70'
            'fc4d53dec520c80fe97dfda65b238c7d678e7ef26aaebffc5b43f924477ea4f4'
            '21883cfc1c282c927353d0246021fd57697ab8d6c2cc1980108772ee03e5ba3d'
            '97a140062df7b3d1ec5b5c51190dfd8a0a79e65db87aba97a97e886cc2733569')

package() {
	install -Dm644 'linux-modules-cleanup.conf' "${pkgdir}/usr/lib/tmpfiles.d/linux-modules-cleanup.conf"
	install -Dm644 10-linux-modules-pre.hook 61-linux-modules-post.hook -t "${pkgdir}/usr/share/libalpm/hooks/"
	install -Dm755 linux-modules-{save,restore} -t "${pkgdir}/usr/share/libalpm/scripts/"
}
