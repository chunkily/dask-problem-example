from .foo import inc

import os

from dask.distributed import Client
from dask import delayed

if __name__ == '__main__':
    dask_scheduler_address = os.getenv('DASK_SCHEDULER_ADDRESS')
    client = Client(dask_scheduler_address)
    tasks = [delayed(inc)(i) for i in range(100)]

    futures = client.compute(tasks)
    results = client.gather(futures)
    print(results)
