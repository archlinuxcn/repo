// This is replaced by libx32-e2fsprogs.
// Old file is renamed to ext2_types-64.h.

#if !defined __x86_64__
# include "ext2_types-64.h" // lib32-e2fsprogs did not deliver ext2_types-32.h yet
#endif
#if defined __x86_64__ && defined __LP64__
# include "ext2_types-64.h"
#endif
#if defined __x86_64__ && defined __ILP32__
# include "ext2_types-x32.h"
#endif

