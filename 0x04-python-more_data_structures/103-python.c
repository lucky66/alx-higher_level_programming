#include <stdio.h>
#include <Python.h>
/**
 *print_python_bytes - prints bytes info.
 *@p: python obj.
 *Return: void.
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, x;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size >= 10)
		x = 10;
	else
		x = size + 1;
	printf("  first %ld bytes:", x);
	for (i = 0; i < x; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);

