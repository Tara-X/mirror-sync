# -*- coding: utf-8 -*-


import os
import codecs
import qiniu

from .exception import TemplateNotExistsException, QiniuTokenInvalidException
from .config import TEMPLATE_PATH, extract_args
from .logger import APP_LOG

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
    qiniu_args = extract_args(('qiniu_ak', 'qiniu_sk', 'qiniu_budget',))
    token = qiniu.Auth(qiniu_args['qiniu_ak'], qiniu_args['qiniu_sk']).upload_token(qiniu_args['qiniu_budget'])
    
    ret, info = qiniu.put_data(token, filepath, content)
    
    if info is not None:
        if info.status_code == 200:
            return u"http://mirror.tarax.cn/{0}".format(ret['key'])
        else:
            APP_LOG.error(u'qiniu upload error: {0} '.format(info['exception']))
    
    return None


class QiniuBudget(object):

    def __init__(self):
        qiniu_args = extract_args(('QINIU_AK', 'QINIU_SK', 'QINIU_BUDGET',))
        self._q = qiniu_args
        self._t = qiniu.Auth(qiniu_args['QINIU_AK'], qiniu_args['QINIU_SK'])
        self.bucket = qiniu.BucketManager(self._t)

    def resource_exists(self, key, budget = None):
        if budget is None:
            budget = self._q.get('QINIU_BUDGET')
        ret, info = self.bucket.stat(budget, key)
        return (ret is not None) and ('hash' in ret)
        
    def resource_remove(self, key, budget = None):
        if budget is None:
            budget = self._q.get('QINIU_BUDGET')
        if self.resource_exists(key, budget = budget):
            ret, info = self.bucket.delete(budget, key)
            return ret == {}
        return None
        
    def resource_sync(self, content, filepath, strategy = QiniuConflictStrategy.REPLACE):
        pass



    

    
    


