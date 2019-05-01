from conans import ConanFile, tools, CMake


class PyBind11Conan(ConanFile):
    name = "pybind11"
    version = "2.2.4"
    description = "Seamless operability between C++11 and Python"
    homepage = "https://github.com/pybind/pybind11"
    license = "Custom OpenSource License / BSD-alike"
    no_copy_sources = True

    author = "Henning Becker (henning.becker@gmail.com)"
    url = "https://github.com/beckerhe/conan_recipes/tree/master/pybind11"

    def source(self):
        tools.get("{}/archive/v{}.tar.gz".format(self.homepage, self.version))

    def build(self):
        cmake = CMake(self)
        cmake.definitions["PYBIND11_TEST"] = False
        cmake.configure(source_folder="pybind11-{}".format(self.version))
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        self.copy("pybind11-{}/LICENSE".format(self.version), keep_path=False)
  
    def package_id(self):
        self.info.header_only()
