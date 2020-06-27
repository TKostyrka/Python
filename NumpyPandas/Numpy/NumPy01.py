import numpy as np
np.__version__


def print_array(name, arr):
    print("<<<", name, ">>>")
    print("array:\n", arr)
    print("data:", arr.data)
    print("shape:", arr.shape)
    print("dtape:", arr.dtype)
    print("strides :", arr.strides)
    print("")


my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
print_array("my", my_array)

print_array("ones", np.ones((3,4)))
print_array("zeros", np.zeros((2,3,4),dtype=np.int16))
print_array("random", np.random.random((2,2)))
print_array("empty", np.empty((3,2)))
print_array("full", np.full((2,2),7))
print_array("arange", np.arange(10,25,5))
print_array("linspace", np.linspace(0,2,9))