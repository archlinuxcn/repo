# Maintainer: Kimiblock Moe

_pkgname=pocket-id
pkgname="${_pkgname}"
pkgver=2.4.0
pkgrel=1
pkgdesc="A simple and easy-to-use OIDC provider that allows users to authenticate with their passkeys to your services."
arch=('x86_64')
url="https://github.com/pocket-id/pocket-id"
license=('BSD-2-Clause')
makedepends=('git' 'go' 'gcc' 'pnpm' 'nodejs')
depends+=(glibc)
conflicts=("${_pkgname}")
source=(
	"${_pkgname}::git+${url}.git#tag=v${pkgver}"
)
sha256sums=('f98d0e1473fc454e90ddfa9232511d6be7803db32cc10353869f797079ff57d3')

function prepare() {
	cd "${srcdir}/${_pkgname}"
	git reset --hard
	git clean -fdx
	pnpm --filter pocket-id-frontend install --frozen-lockfile
}

function build() {
	cd "${srcdir}/${_pkgname}"
	pnpm --filter pocket-id-frontend build
	output_dir=".bin/pocket-id-${target}${binary_ext}"
	export CGO_ENABLED=0
	cd backend
	mkdir -p .bin
	pocket_id_version=$(cat ../.version | sed 's/^\s*\|\s*$//g')
	export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
	go build -o build ./cmd/...
}

function package() {
	cd "$srcdir/${_pkgname}"
	pnpm --filter pocket-id-frontend install
	install -vDm755 "${srcdir}/pocket-id/backend/build" "${pkgdir}/usr/bin/pocket-id"
	install -vDm644 "${srcdir}/pocket-id/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
