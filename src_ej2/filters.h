#ifndef FILTERS_H
#define FILTERS_H

#include <iostream>
#include <cassert>

typedef unsigned char byte;

typedef struct _pixel {
	byte r;
	byte g;
	byte b;
} __attribute__((packed)) pixel_t;

using namespace std;

void blur_filter(float * im_res, float * im, int ii, int jj);
void gray_filter(float * gray, pixel_t * img, int ii, int jj);

#endif // FILTERS_H
