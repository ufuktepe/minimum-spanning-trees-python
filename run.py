import kruskal
import prim
import multiprocessing as mp


if __name__ == '__main__':
    # n_values = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
    # n_values = [128, 256, 512, 1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336,
    #             15360, 16384, 32768, 65536, 131072, 262144]

    n_values = [128, 256, 512, 1024, 2048, 4096]
    # n_values = [128]

    n_list = []

    iter = 1
    n_process = 1

    for n in n_values:
        for i in range(iter):
            n_list.append(n)

    # Print header for the comma separated table
    print('n,m,Graph Creation Runtime,MST Weight,Max Edge Weight,MST Runtime')

    # Split n_list into parts
    list_of_n_lists = [n_list[i::n_process] for i in range(n_process)]

    pool = mp.Pool(processes=n_process)

    dim = 1

    output_async = [pool.apply_async(func=kruskal.run, args=(n_sub_list, dim)) for n_sub_list in list_of_n_lists]

    output = [x.get() for x in output_async]

    print('DONE!')