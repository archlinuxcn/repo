# Maintainer: Manuel Hüsers <aur@huesers.de>
# Contributor: Nils Czernia <nils@czserver.de>

pkgname=prometheus-postgresql-exporter
pkgver=0.14.0
pkgrel=1
pkgdesc="Prometheus exporter for PostgreSQL"
arch=('x86_64')
url="https://github.com/prometheus-community/postgres_exporter"
license=('Apache')
makedepends=('git' 'go' 'make')
backup=('etc/conf.d/prometheus-postgresql-exporter')
source=("https://github.com/prometheus-community/postgres_exporter/archive/v${pkgver}/postgres_exporter-${pkgver}.tar.gz"
	"prometheus-postgresql-exporter.service"
	"prometheus-postgresql-exporter.conf")
sha512sums=('47a0aa844512d0a3d7853253ef9382ebb51514e02566bbac479cea0c5f20a4f03889fe56ff9cb37a85d75c18d5241764ec1113961759affdd07ae6f6b8152ce3'
            '598d201054de604ac78e2b335ad9a219c5d130de6901a6fe64643ac5c9d74314548b65ba2ee675095d8a140b0b48a896cadf6745848e210143761d81e2534402'
            '70e5f4a0a184322d21204a7a7a17fd604dc425b106e9ab1897c6805c52469ecad732e96f7b0f0d35763f6bc3945dc5562cd27459776e83c609834c931d09508f')

prepare() {
	cd "postgres_exporter-${pkgver}"

	export GOPATH="${srcdir}/gopath"
	mkdir -p "${GOPATH}/src/github.com/prometheus-community"
	ln -snf "${srcdir}/postgres_exporter-${pkgver}" "${GOPATH}/src/github.com/prometheus-community/postgres_exporter"
}

build() {
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
	export GOPATH="${srcdir}/gopath"
	cd "${GOPATH}/src/github.com/prometheus-community/postgres_exporter"
	make build
}

package() {
	install -Dm644 "prometheus-postgresql-exporter.service" \
	  "${pkgdir}/usr/lib/systemd/system/prometheus-postgresql-exporter.service"
	install -Dm644 "prometheus-postgresql-exporter.conf" \
	  "${pkgdir}/etc/conf.d/prometheus-postgresql-exporter"

	cd "postgres_exporter-${pkgver}"
	install -Dm755 "postgres_exporter" "${pkgdir}/usr/bin/prometheus_postgresql_exporter"
}
