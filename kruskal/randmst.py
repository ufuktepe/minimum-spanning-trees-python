import sys
import kruskal
import multiprocessing as mp


def randmst():

    n_args = len(sys.argv)

    if n_args < 4:
        print('Please provide the following parameters: numprocesses numpoints numtrials dimension')
        return

    numprocesses = int(sys.argv[1])
    numpoints = int(sys.argv[2])
    numtrials = int(sys.argv[3])
    dimension = int(sys.argv[4])

    n_list = [numpoints for i in range(numtrials)]

    if numprocesses > 1:
        # Use multiprocessing
        # Adjust number of processes if numtrials is smaller
        if numprocesses > numtrials:
            numprocesses = numtrials

        # Split n_list into parts
        list_of_n_lists = [n_list[i::numprocesses] for i in range(numprocesses)]

        pool = mp.Pool(processes=numprocesses)

        output_async = [pool.apply_async(func=kruskal.run, args=(n_sub_list, dimension)) for n_sub_list in
                        list_of_n_lists]

        try:
            output = [x.get() for x in output_async]
        except ValueError as ve:
            print(ve)
            return

        mst_weight_total = 0
        count = 0
        for weights in output:
            for weight in weights:
                mst_weight_total += weight
                count += 1
    else:
        # Do not use multiprocessing
        try:
            # Run Kruskal's algorithm
            weights = kruskal.run(n_list, dimension)
        except ValueError as ve:
            print(ve)
            return

        mst_weight_total = 0
        count = 0
        for weight in weights:
            mst_weight_total += weight
            count += 1

    avg_weight = mst_weight_total / count
    print(f'average: {avg_weight}, numpoints: {numpoints}, numtrials: {numtrials}, dimension {dimension}')


if __name__ == '__main__':
    randmst()