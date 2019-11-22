#include "filters.h"

void blur_filter(float * im_res, float * im, int ii, int jj)
{
    /* for que recorre el "centro" de la matriz im y va completando im_res */
    for (int i = 1, i < ii - 1, i++){
        for (int j = 1, j < jj -1, j++){
            im_res[((i * ii) + j)] = (im[((i * ii) + j + 1)] + im[((i * ii) + j - 1)] + im[(((i - 1) * ii) + j)] + im[(((i + 1) * ii) + j)]) / 4
        }
     }

     /*este for recorre los bordes izquierdo y derecho y les asigna valor 0 */
     for (int i = 0, i < ii, i++){
        im_res[(i * ii)] = 0
        im_res[(i * ii) + jj] = 0
     }
     /*este for recorre los bordes superior e inferior y les asigna valor 0 */
     for (int j = 0, j < jj, j++){
        im_res[j] = 0
        im_res[(ii * (ii - 1)) + j] = 0
     }
}
