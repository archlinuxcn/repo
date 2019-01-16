#!/usr/bin/make -f

MODULES = \
	vmmon \
	vmnet \
	#vmblock \
	#vmci \
	#vsock

all: $(foreach m, $(MODULES), $m.ko)

%.ko: %
	$(MAKE) KVERSION=$(KVERSION) VM_KBUILD=yes -C $*-only

$(MODULES): %:
	cp -r $(SRCDIR)/$*-only $*-only

vsock.ko: vmci.ko

clean:
	rm -rf $(MODULES)
	rm -rf $(foreach m, $(MODULES), $m-only)
	rm -f  $(foreach m, $(MODULES), $m.ko)
	rm -f  $(foreach m, $(MODULES), $m.o)
