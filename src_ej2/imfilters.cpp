/*****************************************************************************
 *  Utilizar ./setup.py build_ext --inplace para generar el modulo en Python *
 *                                                                           *
 *****************************************************************************/

#include "Python.h"
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "numpy/arrayobject.h"

#include "filters.h"

/* Codigo para definir el modulo en Python2 y Python3 */
#if PY_MAJOR_VERSION >= 3
    #define MOD_DEF(ob, name, doc, methods) \
	        static struct PyModuleDef moduledef = { \
				            PyModuleDef_HEAD_INIT, name, doc, -1, methods, NULL, NULL, NULL, NULL}; \
        ob = PyModule_Create(&moduledef);
    #define MOD_INIT(name) PyMODINIT_FUNC PyInit_##name(void)
#else
    #define MOD_DEF(ob, name, doc, methods) \
	        ob = Py_InitModule3(name, methods, doc);
    #define MOD_INIT(name) PyMODINIT_FUNC init##name(void)
#endif

/* Prototipos de las funciones */
static PyObject *blur_filter_wrapper(PyObject *self, PyObject *args);
static PyObject *gray_filter_wrapper(PyObject *self, PyObject *args);

/* Docstrings */
static char module_docstring[] = "Aplicación de filtros sobre imágenes digitales";
static char blur_filter_docstring[] =
	"Toma una imagen en escala de grises a y le aplica un filtro de difuminado utilizando una matriz de convolución de 3 x 3.\n\n"
	"out[i,j] = (a[i-1,j] + a[i+1,j] + a[i,j-1] + a[i,j+1])/4";
static char gray_filter_docstring[] =
	"Toma una imagen en 24 bits RGB a y le aplica una transformación al espacio de colores YUV, quedándose únicamente con el parámetro Y (luma).\n\n"
	"out[i,j] = 0.3 * a[i,j].r + 0.6 * a[i,j].g + 0.11 * a[i,j].b\n\n"
	"El resultado es una imagen en escala de grises.";

/* Metodos del modulo */
static PyMethodDef module_methods[] = {
	{"gray_filter", gray_filter_wrapper, METH_VARARGS, gray_filter_docstring},
	{"blur_filter", blur_filter_wrapper, METH_VARARGS, blur_filter_docstring},
	{NULL, NULL, 0, NULL}
};

MOD_INIT(imfilters)
{
	PyObject *m = NULL;

	MOD_DEF(m, "imfilters", module_docstring, module_methods)
	import_array();

	return m;
}

/* Genero la matriz con ceros de tama~no ii x jj */
static PyArrayObject *matriz_float_ceros(int ii, int jj)
{
	npy_intp dims[2] = {ii, jj};

	PyArrayObject *out = (PyArrayObject*)PyArray_ZEROS(2, dims, NPY_FLOAT32, 0);
	assert(out);

	return out;
}

static PyObject *blur_filter_wrapper(PyObject *, PyObject *args)
{
	PyArrayObject *img_obj;

	/* Parsear argumentos de entrada */
	if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &img_obj))
		return NULL;
	assert(PyArray_ISCONTIGUOUS(img_obj));

	/* Construyo matriz en la que se van a guardar los datos de salida */
	PyArrayObject *out = matriz_float_ceros(
			PyArray_DIM(img_obj, 0), 
			PyArray_DIM(img_obj, 1));

	/* Datos de entrada y de salida en formato array de C para pasar a la funcion */
	float *img_data = (float*)PyArray_BYTES(img_obj);
	assert(img_data);
	float *out_data = (float*)PyArray_BYTES(out);
	assert(out_data);

	blur_filter(out_data, img_data, 
		PyArray_DIM(img_obj, 0),
		PyArray_DIM(img_obj, 1));

	return PyArray_Return(out);
}

static PyObject *gray_filter_wrapper(PyObject *, PyObject *args)
{
	PyArrayObject *img_obj;

	/* Parsear argumentos de entrada */
	if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &img_obj))
		return NULL;
	assert(PyArray_ISCONTIGUOUS(img_obj));
	assert(PyArray_DIM(img_obj, 2) == 3); // 3 canales

	/* Construyo matriz en la que se van a guardar los datos de salida */
	PyArrayObject *out = matriz_float_ceros(
			PyArray_DIM(img_obj, 0), 
			PyArray_DIM(img_obj, 1));

	/* Datos de entrada y de salida en formato array de C para pasar a la funcion */
	pixel_t *img_data = (pixel_t*)PyArray_BYTES(img_obj);
	assert(img_data);
	float *out_data = (float*)PyArray_BYTES(out);
	assert(out_data);

	gray_filter(out_data, img_data,
		PyArray_DIM(img_obj, 0),
		PyArray_DIM(img_obj, 1));

	return PyArray_Return(out);
}
