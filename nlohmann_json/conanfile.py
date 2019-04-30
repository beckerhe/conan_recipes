from conans import ConanFile, CMake, tools

class NlohmannJson(ConanFile):
    name = "nlohmann_json"
    version = "3.6.1"
    settings = "os", "compiler", "arch", "build_type"
    description = "JSON for Modern C++ parser and generator from https://github.com/nlohmann/json"
    license = "MIT"
    repo_url = "https://github.com/nlohmann/json"
    url = "https://github.com/beckerhe/conan_recipes/tree/master/nlohmann_json"
    author = "Henning Becker (henning.becker@gmail.com)"
    exports_sources = "fix_cmake_install.diff"

    def source(self):
        tools.get("{}/archive/v{}.tar.gz".format(self.repo_url, self.version))
        tools.patch(patch_file="fix_cmake_install.diff", base_path="json-{}".format(self.version), strip=1)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["JSON_BuildTests"] = False
        cmake.definitions["JSON_MultipleHeaders"] = True
        cmake.configure(source_folder="json-{}".format(self.version))

    def package(self):
        cmake = CMake(self)
        cmake.install()
        self.copy("LICENSE.MIT", src="json-{}".format(self.version))

    def package_id(self):
        self.info.header_only()


