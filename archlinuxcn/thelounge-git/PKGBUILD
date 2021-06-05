# Maintainer: Reto Brunner <brunnre8@gmail.com>
pkgname=thelounge-git
_realname=thelounge
pkgver=v3.0.1.r240.g0a1d67bf
pkgrel=1
pkgdesc='Modern self-hosted web IRC client'
url='https://thelounge.chat/'
arch=('any')
license=('MIT')
depends=('nodejs')
makedepends=('yarn' 'git')
conflicts=('thelounge')
backup=('etc/thelounge/config.js')
source=(
    'git+https://github.com/thelounge/thelounge.git'
    'system.service'
    'user.service'
    'sysusers.d'
    'tmpfiles.d'
)
sha256sums=('SKIP'
            'c92210f6ac8f01c1cd01b6b26793094cd2feea583ed21fab3564d6bcafdc7a20'
            'c609f3309f54bd6285e99ff29ca2464828bec7bbbca67243ee688bd2d605dbf0'
            '30fab63b8a4ffcfdda4c5b8d7c66822a323c4f1de6ca62b77fe9500f4befc0a5'
            'df4f110f8457a6727b5d3d1fead19d01d754f92563952699c3ef413c72366446')

pkgver() {
    cd $_realname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare(){
    echo /etc/thelounge > "$_realname/.thelounge_home"
}

build() {
    cd $_realname
    yarn install
    export NODE_ENV=production
    yarn build
}


package() {
    export NODE_ENV=production
    yarn global add --prefix "$pkgdir/usr" --global-folder "$pkgdir/usr/lib/$_realname" file:$srcdir/$_realname

    # add default config
    install -Dm 644 "$srcdir/$_realname/defaults/config.js" "$pkgdir/etc/thelounge/config.js"

    # services
    install -Dm644 "$srcdir/system.service" "$pkgdir/usr/lib/systemd/system/$_realname.service"
    install -Dm644 "$srcdir/user.service" "$pkgdir/usr/lib/systemd/user/$_realname.service"

    # setting up system user
    install -Dm644 "${srcdir}/sysusers.d" "${pkgdir}/usr/lib/sysusers.d/thelounge.conf"
    install -Dm644 "${srcdir}/tmpfiles.d" "${pkgdir}/usr/lib/tmpfiles.d/thelounge.conf"
}
