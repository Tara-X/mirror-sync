# -*- coding: utf-8 -*-


import os
import codecs
import qiniu

from .exception import TemplateNotExistsException
from .config import TEMPLATE_PATH

'''
    Persist file mode: append/replace, default mode is replace
'''
class PersistMode:
    REPLACE = 'rw'
    APPEND = 'a'

'''
    Persist content method
'''
def persist_file(content, filename, mode = PersistMode.REPLACE, encoding='utf-8'):

    if mode == PersistMode.REPLACE:
        if os.path.exists(filename):
            os.remove(filename)
        
    with codecs.open(filename, mode, encoding) as temp:
        temp.write(content) 


'''
    Render template
'''
def render_template(template, target=dict()):

    if template or (not os.path.exists(os.path.join(TEMPLATE_PATH, u'{0}.tmpl'.format(template)))):
        raise TemplateNotExistsException()
    


'''
    Strategies when qiniu upload filename occurs conflicts
'''
class QiniuConflictStrategy:
    REPLACE = 'replace'
    ABANDOM = 'abandon'

'''
    Upload file/content to QiniuStorage
'''
def sync_to_qiniu(content, filepath, strategy=QiniuConflictStrategy.REPLACE):
    
    qiniu_config = {
        'qiniu_ak' : os.environ.get('QINIU_AK'),
        'qiniu_sk' : os.environ.get('QINIU_SK'),
        'qiniu_budget' : os.environ.get('QINIU_BUDGET')
    }

    for k, v in qiniu_config.iteritems():
        print k, v
    

    
    


