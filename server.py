import cherrypy
import json
import os

from data.fetch_codes import write_codes, get_codes

location = "./data/"
filename = "industry-codes.json"
path = os.path.join(location, filename)

if not os.path.isfile(path):
    write_codes(get_codes(), location)

with open('./data/industry-codes.json') as f:
    data = json.load(f)

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

