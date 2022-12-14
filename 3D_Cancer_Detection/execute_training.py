#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
from util.util import importstr
from util.logconf import logging
import os
import shutil

os.environ['KMP_DUPLICATE_LIB_OK']='True'
log = logging.getLogger('nb')

def run(app, *argv):
    argv = list(argv)
    argv.insert(0, '--num-workers=10')  # <1>
    log.info("Running: {}({!r}).main()".format(app, argv))
    
    app_cls = importstr(*app.rsplit('.', 1))  # <2>
    app_cls(argv).main()
    
    log.info("Finished: {}.{!r}).main()".format(app, argv))


# clean up any old data that might be around.
# We don't call this by default because it's destructive, 
# and would waste a lot of time if it ran when nothing 
# on the application side had changed.
def cleanCache():
    shutil.rmtree('data-unversioned/cache')
    os.mkdir('data-unversioned/cache')


if __name__ == "__main__":
    #cleanCache()
    run('prepcache.LunaPrepCacheApp')
    run('training.LunaTrainingApp', '--epochs=1')

