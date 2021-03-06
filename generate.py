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
            'url': entry['url'],
            'fields': OrderedDict(),
            }
    renderedentries.append(rendered)
    for critkey, crit in criteria.items():
        if critkey not in entry['fields']:
            raise SystemExit("Missing field '{}' for entry '{}'"
                    .format(critkey, entryfile))
        entryvalue = entry['fields'][critkey]
        if 'values' in crit and entryvalue in crit['values']:
            renderedfield = crit['values'][entryvalue]
        else:
            renderedfield = str(entryvalue)
        rendered['fields'][critkey] = {'rendered': renderedfield}
    pprint(rendered)

# Load and render template
j2env = Environment(loader=FileSystemLoader(scriptrelpath("template")))
template = j2env.get_template("blobs.html.j2")

rendered = template.render(criteria=criteria, entries=renderedentries)
with open(scriptrelpath("blobs.html"), "w") as outfh:
    print(rendered, file=outfh)
