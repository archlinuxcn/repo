#include <stdio.h>
#include <stdlib.h>
#define CL_TARGET_OPENCL_VERSION 300
#include <CL/cl.h>
#include <math.h>

static const char *kernel_source="\n"
"__kernel\n"
"void square(__global float *input, __global float *output, uint n)\n"
"{\n"
"	uint id = get_global_id(0);\n"
"   if(id < n){\n"
"	    output[id] = input[id]*input[id];\n"
"   }\n"
"}\n";

int main(int argc, char *argv[])
{
    size_t n = 1024;

    float *xin = malloc(sizeof *xin * n);
    for(size_t i = 0; i < n; i++){
        xin[i] = -1.0f + 2.0f * i / n;
    }

    cl_platform_id platform_id;
    cl_uint n_platforms;
	cl_int err = clGetPlatformIDs(1,&platform_id, &n_platforms);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Unable to get platforms\n");
        return 1;
    }

    cl_device_id device_id;
    cl_uint n_devs;
	err = clGetDeviceIDs(platform_id, CL_DEVICE_TYPE_GPU, 1, &device_id, &n_devs);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Unable to get device id\n");
        return 1;
    }

    cl_context_properties properties[3];
	properties[0] = CL_CONTEXT_PLATFORM;
	properties[1] = (cl_context_properties) platform_id;
	properties[2] = 0;

	cl_context context = clCreateContext(properties, 1, &device_id, NULL, NULL, &err);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Creating context failed with error %d\n", err);
        return 1;
    }

    cl_command_queue command_queue = clCreateCommandQueueWithProperties(context, device_id, NULL, &err);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Creating command queue failed with error %d\n", err);
        return 1;
    }

	cl_program program = clCreateProgramWithSource(context, 1, &kernel_source, NULL, &err);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Creating program from source failed with error %d\n", err);
        return 1;
    }

	err = clBuildProgram(program, 0, NULL, NULL, NULL, NULL);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Compiling program failed with error %d\n", err);
        return 1;
    }

	cl_kernel kernel = clCreateKernel(program, "square", &err);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Creating kernel failed with error %d\n", err);
        return 1;
    }

	cl_mem x = clCreateBuffer(context, CL_MEM_READ_ONLY, sizeof *xin * n, NULL, &err);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Allocating read-only memory failed with error code %d\n", err);
        return 1;
    }
	cl_mem y = clCreateBuffer(context, CL_MEM_WRITE_ONLY, sizeof *xin * n, NULL, &err);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Allocating write-only memory failed with error code %d\n", err);
        return 1;
    }

	err = clEnqueueWriteBuffer(command_queue, x, CL_TRUE, 0, sizeof *xin * n, xin, 0, NULL, NULL);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Command queue finished with error code: %d\n", err);
        return 1;
    }

    cl_uint dim = n;
	clSetKernelArg(kernel, 0, sizeof x, &x);
	clSetKernelArg(kernel, 1, sizeof y, &y);
    clSetKernelArg(kernel, 2, sizeof dim, &dim);

	err = clEnqueueNDRangeKernel(command_queue, kernel, 1, NULL, &n, NULL, 0, NULL, NULL);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Cannot queue kernel for execution. Error code: %d\n", err);
        return 1;
    }
	err = clFinish(command_queue);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Command queue finished with error code: %d\n", err);
        return 1;
    }

    float *yout = malloc(sizeof *yout * n);
	err = clEnqueueReadBuffer(command_queue, y, CL_TRUE, 0, sizeof *yout * n, yout, 0, NULL, NULL);
    if(err != CL_SUCCESS){
        fprintf(stderr, "Could not copy memory from device: %d\n", err);
        return 1;
    }

    float tol = 0.001f;
    for(size_t i = 0; i < n; i++){
        if(fabsf(yout[i] - xin[i] * xin[i]) > tol){
            printf("Mismatch at index %zu:\n", i);
            printf("Desired: %f\n", xin[i] * xin[i]);
            printf("Actual : %f\n", yout[i]);
            return 1;
        }
    }
    printf("TESTS PASSED!\n");

    free(xin);
    free(yout);
	clReleaseMemObject(x);
	clReleaseMemObject(y);
	clReleaseProgram(program);
	clReleaseKernel(kernel);
	clReleaseCommandQueue(command_queue);
	clReleaseContext(context);
}
