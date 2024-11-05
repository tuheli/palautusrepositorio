import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_dict = tomli.loads(content)
        poetry = toml_dict['tool']['poetry']
        name = poetry['name']
        description = poetry['description']
        license = poetry['license']
        authors = poetry['authors']
        dependencies = poetry['dependencies']
        dev_dependencies = poetry['group']['dev']['dependencies']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
