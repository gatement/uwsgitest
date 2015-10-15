import time

def application(env, start_response):
    time.sleep(30)
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Instance[3-2]: ", str(time.time())]
