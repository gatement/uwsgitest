import time

def application(env, start_response):
    time.sleep(10)
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"instance2, update2: ", str(time.time())]
