from conans import ConanFile, CMake, tools

class CppIterToolsConan(ConanFile):
    name = "cppitertools"
    version = "20190208-24fb7df"
    description = "Implementation of python itertools and builtin iteration functions for C++17"
    repo_url = "https://github.com/ryanhaining/cppitertools"
    license = "BSD 2-Clause"

    author = "Henning Becker (henning.becker@gmail.com)"
    url = "https://github.com/beckerhe/conan_recipes/cppitertools"
    exports_sources = "CMakeLists.txt"

    def source(self):
        git = tools.Git(folder="cppitertools")
        git.clone("https://github.com/ryanhaining/cppitertools.git")
        git.checkout("24fb7df23e207e725c621b694af6a73f950b6515")
        tools.save("cppitertools/CMakeLists.txt", tools.load("CMakeLists.txt"))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cppitertools")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        self.copy("LICENSE.md", src="cppitertools")

    def package_id(self):
        self.info.header_only()