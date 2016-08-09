import os
import re
import sys
import pip


class Scanner:
    """
    Scanner class
    Looks through all python files to generate a list of unique
    third party libraries for use in
    """

    def __init__(self, options):

        # Compiled import regular expression
        self.import_statement = re.compile(r'(?:from|import) ([a-zA-Z0-9]+)(?:.*)')

        # List of pip distributions
        # Called once and then imported for performance
        self.libraries_installed = pip.get_installed_distributions()
        self.libraries_found = []

        # ArgumentParser options
        self.options = options

    def run(self):
        """
        Runs the scanner
        :return: void
        """

        # Normalize path
        self.options.path = os.path.expanduser(self.options.path)

        # Start scanning
        if os.path.isdir(self.options.path):
            self.search_script_directory(self.options.path)
        else:
            raise ScannerException("Unknown directory: %s" % self.options.path)

    def output(self):
        """
        Output the results to either STDOUT or
        :return:
        """
        if not self.options.out:
            self.output_to_fd(sys.stdout)
        else:
            with open(self.options.out, "w") as out:
                self.output_to_fd(out)

    def output_to_fd(self, fd):
        """
        Outputs the results of the scanner to a file descriptor (stdout counts :)
        :param fd: file
        :return: void
        """
        for library in self.libraries_found:
            fd.write("%s==%s\n" % (library.key, library.version))

    def search_script_directory(self, path):
        """
        Recursively loop through a directory to find all python
        script files. When one is found, it is analyzed for import statements
        :param path: string
        :return: generator
        """
        for subdir, dirs, files in os.walk(path):
            for file_name in files:
                if file_name.endswith(".py"):
                    self.search_script_file(subdir, file_name)

    def search_script_file(self, path, file_name):
        """
        Open a script file and search it for library references
        :param path:
        :param file_name:
        :return: void
        """
        with open(os.path.join(path, file_name), "r") as script:
            self.search_script(script.read())

    def search_script(self, script):
        """
        Search a script's contents for import statements and check
        if they're currently prevent in the list of all installed
        pip modules.
        :param script: string
        :return: void
        """
        if self.import_statement.search(script):
            for installed in self.libraries_installed:
                for found in set(self.import_statement.findall(script)):
                    if found == installed.key:
                        self.libraries_installed.remove(installed)
                        self.libraries_found.append(installed)


class ScannerException(Exception):
    """
    Custom exception type
    Prevents ambiguity errors
    """
