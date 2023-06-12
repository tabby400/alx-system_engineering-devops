#include <Python.h>

/**
 * print_python_list_info - function that is used to print
 *                     some basic info on python lists
 * @p: points to PyObject ehuich is a list in this case
 */

void print_python_list_info(PyObject *p)
{
	int list_size;
	int capacity;
        int x;
	PyObject *obj;

	list_size = Py_SIZE(p); /* macro for size of python object*/
	capacity = ((PyListObject *)p)->allocated; /*acess struct*/

	printf("[*] Size of  Python List = %d\n", list_size);
	printf("[*] Allocated size = %d\n", capacity);

	for (x = 0 ; x < list_size ; x++)
	{
		printf("Element %d: ", x);

		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
