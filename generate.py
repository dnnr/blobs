from collections import OrderedDict
from jinja2 import Template, Environment, FileSystemLoader
from pprint import pprint
import os
import yaml

def scriptrelpath(path):
    return os.path.join(os.path.dirname(__file__), path)

def loadcriteria(frompath):
    """ Load criteria as ordered dictionary.
    """
    criteria = OrderedDict()
    with open(frompath, "r") as fh:
        y = yaml.load(fh)
        for c in y:
            critname = list(c.keys())[0]
            critparams = c[critname]
            criteria[critname] = critparams
    return criteria


def loadentries(fromdir):
    """ Load entries from given directory.
    """
    entries = []
    datadir = scriptrelpath("data")
    for filename in sorted(os.listdir(datadir)):
        filepath = os.path.join(datadir, filename)
        if os.path.isfile(filepath) and filename.endswith(".yml"):
            with open(filepath, "r") as fh:
                y = yaml.load(fh)
                entries.append((filename, y))
    return entries

criteria = loadcriteria(scriptrelpath("criteria.yml"))
entries = loadentries("data")

# Render entries
renderedentries = []
for entryfile, entry in entries:
    rendered = {
            'name': entry['name'],
            'fields': {},
            }
    renderedentries.append(rendered)
    for fieldname, fieldvalue in entry['fields'].items():
        if fieldname not in criteria:
            raise SystemExit("Unknown field '{}' used in '{}'"
                             .format(fieldname, entryfile))
        crit = criteria[fieldname]
        if fieldvalue is True:
            renderedfield = 'Yes'
        elif fieldvalue is False:
            renderedfield = 'No'
        else:
            renderedfield = str(fieldvalue)
        rendered['fields'][fieldname] = {'rendered': renderedfield}

# Load and render template
j2env = Environment(loader=FileSystemLoader(scriptrelpath("template")))
template = j2env.get_template("blobs.html.j2")

rendered = template.render(criteria=criteria, entries=renderedentries)
with open(scriptrelpath("blobs.html"), "w") as outfh:
    print(rendered, file=outfh)
