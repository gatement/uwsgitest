http://uwsgi-docs.readthedocs.org/en/latest/WSGIquickstart.html

pip install uwsgi

uwsgi --http :9090 --wsgi-file foobar.py
uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2
uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191 (use 'uwsgitop' to access the stats)
