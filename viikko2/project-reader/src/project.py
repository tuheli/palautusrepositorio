class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return f'\n- {"\n- ".join(dependencies)}' if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n"
            f"\nAuthors: {self.authors or '-'}"
            f"\n"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
