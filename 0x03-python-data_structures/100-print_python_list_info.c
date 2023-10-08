#include <Python.h>

/**
 *print_python_list_info - prints python lists info
 *@p: python list PyObj
 */

void print_python_list_info(PyObject *p)
{
	int size, ext, i;
	PyObject *obj;

	size = Py_SIZE(p);
	ext = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", ext);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
