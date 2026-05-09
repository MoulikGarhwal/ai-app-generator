import time

request_count = 0
success_count = 0
failure_count = 0


def start_timer():
    return time.time()


def end_timer(start_time):
    return round(time.time() - start_time, 2)


def update_metrics(success=True):

    global request_count
    global success_count
    global failure_count

    request_count += 1

    if success:
        success_count += 1

    else:
        failure_count += 1


def get_metrics(latency):

    if request_count == 0:
        success_rate = 0

    else:
        success_rate = round(
            (success_count / request_count) * 100,
            2
        )

    return {
        "total_requests": request_count,
        "success_count": success_count,
        "failure_count": failure_count,
        "success_rate": f"{success_rate}%",
        "latency": f"{latency}s"
    }