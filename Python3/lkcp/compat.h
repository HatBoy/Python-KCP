#include "Python.h"

typedef void (*capsule_dest)(PyObject *);
typedef void (*cobj_dest)(void *);

#define CAP_NEW PyCapsule_New
#define DEST_FUNC_TYPE capsule_dest
#define CAP_GET_POINTER PyCapsule_GetPointer

PyObject* make_capsule(void *p, const char *name, capsule_dest dest) {
    return CAP_NEW(p, name, (DEST_FUNC_TYPE)dest);
}
void* get_pointer(PyObject *cap, const char *name) {
    return CAP_GET_POINTER(cap, name);
}
