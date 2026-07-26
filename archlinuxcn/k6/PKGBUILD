# Maintainer: yetipaw
# Co-Maintainer: tuananh
# Old Maintainer: Jeff Henson <jeff@henson.io>
# Old Maintainer: Andy Nicholson <andrew@anicholson.net>
# Contributors: teutat3s

pkgname=k6
pkgver=2.1.0
pkgrel=2
pkgdesc="A modern load testing tool, using Go and JavaScript"
arch=('x86_64')
url="https://github.com/grafana/k6"
license=('AGPL3')
depends=('glibc')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('04d9a1586b23db9d1746aa61f29ae4aee4d2a5da7d5782e11f7530405b5f57ab')

build() {
	cd "${pkgname}-${pkgver}"
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	# -buildvcs=false: the build dir sits inside the AUR packaging repo, so Go
	# would otherwise stamp this repo's git HEAD (and a -dirty flag) into
	# `k6 version` instead of upstream's commit.
	export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw -buildvcs=false"
	go build -o ${pkgname}
}

package() {
	cd "${pkgname}-${pkgver}"
	install -vDm 755 ${pkgname} -t "${pkgdir}/usr/bin/"
	install -vDm 644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}/"
	install -vDm 644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}/"

	# build bash completions
	mkdir -p "${pkgdir}/usr/share/bash-completion/completions"
	./${pkgname} completion bash > "${pkgdir}/usr/share/bash-completion/completions/k6"

	# build zsh completions
	mkdir -p "${pkgdir}/usr/share/zsh/site-functions"
	./${pkgname} completion zsh > "${pkgdir}/usr/share/zsh/site-functions/_k6"

	# build fish completions
	mkdir -p "${pkgdir}/usr/share/fish/vendor_completions.d/"
	./${pkgname} completion fish > "${pkgdir}/usr/share/fish/vendor_completions.d/k6.fish"
}
