# $Id: PKGBUILD 248282 2015-10-02 19:22:55Z bpiotrowski $
# Maintainer: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Maintainer: Sébastien Luttringer
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Miroslaw Szot <mss@czlug.icis.pcz.pl>
# Contributor: Daniel Micay <danielmicay@gmail.com>

_pkgbasename=nginx
pkgname=libx32-nginx
pkgver=1.8.0
pkgrel=2.1
pkgdesc='Lightweight HTTP server and IMAP/POP3 proxy server (x32 ABI)'
arch=('x86_64')
url='http://nginx.org'
license=('custom')
depends=('libx32-pcre' 'libx32-zlib' 'libx32-openssl' 'libx32-geoip' 'nginx')
backup=('etc/nginx-x32/fastcgi.conf'
        'etc/nginx-x32/fastcgi_params'
        'etc/nginx-x32/koi-win'
        'etc/nginx-x32/koi-utf'
        'etc/nginx-x32/mime.types'
        'etc/nginx-x32/nginx.conf'
        'etc/nginx-x32/scgi_params'
        'etc/nginx-x32/uwsgi_params'
        'etc/nginx-x32/win-utf'
        'etc/logrotate.d/nginx-x32')
source=($url/download/nginx-$pkgver.tar.gz
        service
        logrotate)
md5sums=('3ca4a37931e9fa301964b8ce889da8cb'
         'a10624df3b2749a592948f5911ad4466'
         '9cd74ddc8fa6cdd67d8056b713ae9970')

build() {
  cd $_pkgbasename-$pkgver
	export CC="gcc -mx32"
	export CXX="g++ -mx32"
	#export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure \
    --prefix=/etc/nginx-x32 \
    --conf-path=/etc/nginx-x32/nginx.conf \
    --sbin-path=/usr/bin/nginx-x32 \
    --pid-path=/run/nginx-x32.pid \
    --lock-path=/run/lock/nginx-x32.lock \
    --user=http \
    --group=http \
    --http-log-path=/var/log/nginx-x32/access.log \
    --error-log-path=stderr \
    --http-client-body-temp-path=/var/lib/nginx-x32/client-body \
    --http-proxy-temp-path=/var/lib/nginx-x32/proxy \
    --http-fastcgi-temp-path=/var/lib/nginx-x32/fastcgi \
    --http-scgi-temp-path=/var/lib/nginx-x32/scgi \
    --http-uwsgi-temp-path=/var/lib/nginx-x32/uwsgi \
    --with-imap \
    --with-imap_ssl_module \
    --with-ipv6 \
    --with-pcre-jit \
    --with-file-aio \
    --with-http_addition_module \
    --with-http_auth_request_module \
    --with-http_dav_module \
    --with-http_degradation_module \
    --with-http_flv_module \
    --with-http_geoip_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_mp4_module \
    --with-http_realip_module \
    --with-http_secure_link_module \
    --with-http_spdy_module \
    --with-http_ssl_module \
    --with-http_stub_status_module \
    --with-http_sub_module \

  make
}

package() {
  cd $_pkgbasename-$pkgver
  make DESTDIR="$pkgdir" install

  sed -e 's|\<user\s\+\w\+;|user html;|g' \
    -e '44s|html|/usr/share/nginx/html|' \
    -e '54s|html|/usr/share/nginx/html|' \
    -i "$pkgdir"/etc/nginx-x32/nginx.conf

  rm "$pkgdir"/etc/nginx-x32/*.default

  install -d "$pkgdir"/var/lib/nginx-x32
  install -dm700 "$pkgdir"/var/lib/nginx-x32/proxy

  chmod 750 "$pkgdir"/var/log/nginx-x32
  chown http:log "$pkgdir"/var/log/nginx-x32

  rm -rf "$pkgdir"/etc/nginx/html/

  install -Dm644 ../logrotate "$pkgdir"/etc/logrotate.d/nginx-x32
  install -Dm644 ../service "$pkgdir"/usr/lib/systemd/system/nginx-x32.service
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$_pkgbasename/LICENSE

  rm -rf "$pkgdir"/{run,usr/share}
	mkdir -p "$pkgdir/usr/share/licenses"
	ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

# vim:set ts=2 sw=2 et:
