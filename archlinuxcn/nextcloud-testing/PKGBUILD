# Submitter: Grey Christoforo <first name [at] last name [dot] net>
# Maintainer: Colin Arnott <colin@urandom.co.uk>

srcname=nextcloud
pkgname=${srcname}-testing
pkgver=18.0.0beta2
pkgrel=1
pkgdesc="Testing Release -- A cloud server to store your files centrally on a hardware controlled by you"
arch=('any')
url="https://nextcloud.com"
provides=('nextcloud')
conflicts=('nextcloud' 'owncloud')
license=('AGPL')
depends=('php-gd')
optdepends=('php-apache: to use the Apache web server'
            'php-sqlite: to use the SQLite database backend'
            'php-pgsql: to use the PostgreSQL database backend'
            'php-ldap: LDAP authentication'
            'php-intl'
            'php-apcu'
            'php-xcache'
            'mariadb: to use the MySQL database backend'
            'smbclient: to mount SAMBA shares'
            'php-mcrypt'
            'ffmpeg: file preview'
            'libreoffice: file preview')
options=('!strip')
backup=('etc/webapps/nextcloud/apache.example.conf')
validpgpkeys=('28806A878AE423A28372792ED75899B9A724937A')
source=("https://download.nextcloud.com/server/prereleases/nextcloud-${pkgver}.tar.bz2"{,.asc}
        'apache.example.conf'
        'nextcloud.hook')
sha512sums=('7d42201e28f9d2aa70e395dea4de24f55ef48d4d0f6dbcc46a7eba04959cf96a1fcaf3fb85fcadac8018f7d5d54bb161e356600b3987d1eeafe9aa0665cd067c'
            'SKIP'
            '2fd1bf60b1e28e5dfeb1783a576ae728dc549ad517ebabc8048f566381b14ea316c69b2ea24336666d5e96e92d014d43f5163da16deb157a040909c4b190d2db'
            'e1a522965872ab3bad951daa0e24a3d281652bd6ce44a4337af1975808d86b1552c76f4a1216ac30f5e46c2f3da43e264afa61a6b422ff7241e55c14c3097a64')

package() {
    # install project
    install -d "$pkgdir"/usr/share/webapps/
    cp -R "$srcdir"/${srcname} "$pkgdir"/usr/share/webapps/.

    # install apache config file
    install -d  "$pkgdir"/etc/webapps/${srcname}
    install -m 644 "$srcdir"/apache.example.conf  "$pkgdir"/etc/webapps/${srcname}

    # move config to /etc
    install -d  "$pkgdir"/etc/webapps/${srcname}
    mv "$pkgdir"/usr/share/webapps/${srcname}/config "$pkgdir"/etc/webapps/${srcname}/config
    chown -R http:http "$pkgdir"/etc/webapps/${srcname}
    ln -s /etc/webapps/${srcname}/config "$pkgdir"/usr/share/webapps/${srcname}/config
    chown -R root:http "$pkgdir"/usr/share/webapps/${srcname}

    find "$pkgdir"/usr/share/webapps/${srcname} -type f -exec chmod 0644 {} \;
    find "$pkgdir"/usr/share/webapps/${srcname} -type d -exec chmod 0755 {} \;

    chmod a+x "$pkgdir"/usr/share/webapps/${srcname}/occ

#    install -Dm0644 "$srcdir"/nextcloud.hook "$pkgdir"/usr/share/libalpm/hooks/nextcloud.hook
}
