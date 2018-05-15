1 - Install luigi:
```
$ pip install luigi
```

2 - Run the luigi daemon in background and output logs to the ./logs directory:
```
$ luigid --background --logdir=./logs
```

3 - Run the HelloWorldTask task:
```
$ python hello_world.py HelloWorldTask --workers=2
``` 

4 - (Optional) Visualise the pipeline in progress by opening `http://localhost:8082` in a web browser.
