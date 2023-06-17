# Maintainer: Manuel Hüsers <aur@huesers.de>
# Contributor: Nils Czernia <nils@czserver.de>

pkgname=prometheus-postgresql-exporter
pkgver=0.12.1
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
sha256sums=('4287e58e04bcd5399784ba7d2608e881f5e95da60a6021597b99a5d4c07b7a24'
            '0d86e650d88c8d4a8bc5b26faecb75023e069eaf29582135bcb0202e4a69a9b9'
            '5436ad34fbcd6faab69da8675631f3eb5b89d964682eb23164bf4bb816ad1897')

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
