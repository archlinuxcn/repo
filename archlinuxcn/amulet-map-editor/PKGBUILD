# Maintainer: Kimiblock Moe

pkgname=amulet-map-editor

pkgdesc="The new age Minecraft world editor and converter that supports every version since Java 1.12 and Bedrock 1.7"
url="https://www.amuletmc.com/"
license=(LicenseRef-none MIT)

arch=(any)
pkgver=0.10.45
pkgrel=1
makedepends=(python-build python-installer python-wheel python-cython-lint python-versioneer git python-packaging)

depends=(python python-numpy python-wxpython python-opengl python-amulet-nbt python-pymctranslate python-minecraft-model-reader python-amulet-core python-lz4 python-amulet-leveldb python-pillow glibc hicolor-icon-theme python-platformdirs)

source=(
	amulet.desktop
	"git+https://github.com/Amulet-Team/Amulet-Map-Editor.git#tag=${pkgver}"
)

sha256sums=('724383fa0a28be2ab92785365b7a3695aae5ee7849fc7841b492da73ce60c829'
            '6fd3ca7f9a2515af00b8d0e2f469f81b104864d7d881279780a3bbaa82b33b89')

function prepare() {
	sed -i 's/versioneer-518/versioneer/g' "${srcdir}/Amulet-Map-Editor/pyproject.toml"
	sed -i 's|numpy ~= 1.17|numpy|g' "${srcdir}/Amulet-Map-Editor/pyproject.toml"
}

function build() {
	cd "${srcdir}/Amulet-Map-Editor"
	python -m build --wheel --no-isolation
}

function package() {
	install -Dm755 "${srcdir}/Amulet-Map-Editor/amulet_map_editor/api/image/logo/amulet_logo.png" "${pkgdir}/usr/share/icons/hicolor/256x256/apps/amulet.png"
	install -Dm644 "${srcdir}/amulet.desktop" "${pkgdir}/usr/share/applications/amulet.desktop"
	cd "${srcdir}/Amulet-Map-Editor"
	python -m installer --destdir="${pkgdir}" dist/*.whl
	rm -rf "${pkgdir}/usr/bin/amulet_map_editor_no_console"
}
