#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * Prints information about a Python bytes object.
 * @param p: PyObject pointer assumed to be a bytes object.
 */
void print_python_bytes(PyObject *p) {
    size_t size, i;
    char *bytes_string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes_string = PyBytes_AS_STRING(p);
    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes_string);

    // Limit the output to 10 bytes or the size of the bytes object, whichever is smaller
    size = size < 10 ? size + 1 : 10;
    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++) {
        printf("%02x ", bytes_string[i] & 0xFF); // Print each byte as two hexadecimal digits
    }
    printf("\n");
}

/**
 * Prints information about a Python float object.
 * @param p: PyObject pointer assumed to be a float object.
 */
void print_python_float(PyObject *p) {
    double float_value;
    char *float_str;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    float_value = PyFloat_AsDouble(p);
    float_str = PyOS_double_to_string(float_value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", float_str);
    PyMem_Free(float_str); // Free memory allocated by PyOS_double_to_string
}

/**
 * Prints information about a Python list object, including details about its elements.
 * @param p: PyObject pointer assumed to be a list object.
 */
void print_python_list(PyObject *p) {
    PyListObject *list;
    size_t size, allocated, i;
    const char *item_type;

    printf("[*] Python list info\n");
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_GET_SIZE(p);
    allocated = list->allocated;
    printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GET_ITEM(list, i);
        item_type = item->ob_type->tp_name;
        printf("Element %li: %s\n", i, item_type);

        if (strcmp(item_type, "bytes") == 0) {
            print_python_bytes(item);
        } else if (strcmp(item_type, "float") == 0) {
            print_python_float(item);
        }
    }
}
