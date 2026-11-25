from concurrent.futures import ProcessPoolExecutor, as_completed
import time



MAX_WORKERS = 1


def _time_run(algorithm, *args):
    start = time.perf_counter()
    algorithm(*args)
    return time.perf_counter() - start


def time_algorithm(algorithm, sizes, get_args, runs_per_size=10):
    futures = {}
    total_times = {i: 0 for i in sizes}

    # Usa un ProcessPoolExecutor para ejecutar las mediciones en paralelo
    # (el ThreadPoolExecutor no sirve por el GIL de Python)
    with ProcessPoolExecutor(MAX_WORKERS) as p:
        for i in sizes:
            for _ in range(runs_per_size):
                futures[p.submit(_time_run, algorithm, *get_args(i))] = i

        for f in as_completed(futures):
            result = f.result()
            i = futures[f]
            total_times[i] += result

    return {s: t / runs_per_size for s, t in total_times.items()}
