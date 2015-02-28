// This is replaced by libx32-jemalloc.
// Old file is renamed to jemalloc-64.h.

#if !defined __x86_64__
# include "jemalloc-64.h" // no such lib32-jemalloc yet
#endif
#if defined __x86_64__ && defined __LP64__
# include "jemalloc-64.h"
#endif
#if defined __x86_64__ && defined __ILP32__
# include "jemalloc-x32.h"
#endif

