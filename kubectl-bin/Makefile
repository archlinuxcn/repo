



PHOHY = clean release

BASEURL:=https://storage.googleapis.com/kubernetes-release/release


check:
ifndef VERSION
	@echo "Define version in ENV"
	@exit 1;
else
	@echo "Build version ${VERSION}"
endif


prepare: check
	@mkdir -p tmp
	curl -s ${BASEURL}/v${VERSION}/bin/linux/amd64/kubectl > tmp/kubectl_amd64
	curl -s ${BASEURL}/v${VERSION}/bin/linux/arm64/kubectl > tmp/kubectl_arm64
	curl -s ${BASEURL}/v${VERSION}/bin/linux/386/kubectl > tmp/kubectl_386

release: prepare
	set -e; \
	SHA256_AMD64=`sha256sum tmp/kubectl_amd64 | awk '{print $$1}'`; \
	SHA256_ARM64=`sha256sum tmp/kubectl_arm64 | awk '{print $$1}'`; \
	SHA256_386=`sha256sum tmp/kubectl_386 | awk '{print $$1}'`; \
	sed -i.bak -r -e "s/pkgver=.*/pkgver=$${VERSION}/g" \
        -e "s/sha256sums_i686=.*/sha256sums_i686=('$${SHA256_386}')/g" \
        -e "s/sha256sums_x86_64=.*/sha256sums_x86_64=('$${SHA256_AMD64}')/g" \
        -e "s/sha256sums_aarch64=.*/sha256sums_aarch64=('$${SHA256_ARM64}')/g" PKGBUILD; \
	makepkg --printsrcinfo > .SRCINFO; \
	makepkg; \
	sudo pacman -U kubectl-bin*; \


clean:
	rm -rf kubectl-* pkg src *.bak tmp
