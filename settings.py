DATABASE = {
        'NAME': "fed_employment",
        'USER': "patrick",
        "PASSWORD": "pass",
        "HOST": "localhost",
        "PORT": "5432",
    }

DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (DATABASE['USER'],
        DATABASE['PASSWORD'],DATABASE['HOST'],DATABASE['PORT'],DATABASE['NAME'])
