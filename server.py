import argparse
import cherrypy
import json
import os

from data.fetch_codes import write_codes, get_codes

location = "./data/"
filename = "industry-codes.json"
path = os.path.join(location, filename)

data = {}
reload_on_start = False
def reload_data(check_if_exists=True):
    global data
    global reload_on_start
    if not os.path.isfile(path) or not check_if_exists:
        write_codes(get_codes(), location)
        reload_on_start = True

    with open('./data/industry-codes.json') as f:
        data = json.load(f)

reload_data()

class CODE:
    exposed = True
    code = None
    @cherrypy.tools.json_out()
    def GET(self, id=None):
        if id == None:
            return self.code
        elif id in self.code:
            return self.code[id]
        else:
            return {}

class NAICS(CODE):
    code = data['naics_codes']

class SIC(CODE):
    code = data['sic_codes']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--reload', action='store_true')

    if parser.parse_args().reload and not reload_on_start:
        reload_data(check_if_exists=False)

    cherrypy.tree.mount(
        NAICS(), '/naics',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.tree.mount(
        SIC(), '/sic',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

