example = {
            'app_url': '',
            'models': [
                {
                    'perms': {
                        'add': True, 
                        'change': True, 
                        'delete': True
                        }, 
                    'add_url': '/admin/cms/news/add/',
                    'admin_url': '/admin/cms/news/',
                    'name': ''
                }
            ],
            'has_module_perms': True,
            'name': 'CMS'
        }

i = 0

def find(dictData):
    global i
    i = i + 1
    for key, value in dictData.items():
        if not(isinstance(value, (str,bool,int,float))):
            if isinstance(value, (list)):
                for idx , val in enumerate(value):
                    find(val)
            if isinstance(value, (dict)):
                find(value)
        else:
            print('======>\tkey:'+str(key)+'\tvalue:'+str(value)+'<======')

find(example)