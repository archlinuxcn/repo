# Simple config

export CONFIG_APFS_FS        := m

SRC_DIRS := fs/apfs

modules: $(SRC_DIRS)

$(SRC_DIRS):
	# APFS_SUPER_MAGIC should be defined in include/uapi/linux/magic.h, but yeah we're building a out-of-tree module...
	$(MAKE) -C /lib/modules/`uname -r`/build M="$(M)/$@" subdir-ccflags-y=-DAPFS_SUPER_MAGIC=0x4253584E

.PHONY: $(SRC_DIRS) modules
