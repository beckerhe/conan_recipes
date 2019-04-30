cmake_minimum_required(VERSION 3.2)
include(GNUInstallDirs)

project(cppitertools CXX)
add_library(cppitertools INTERFACE)
target_include_directories(cppitertools INTERFACE $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

install(TARGETS cppitertools EXPORT cppitertools-config)
install(EXPORT cppitertools-config NAMESPACE cppitertools:: DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/cppitertools)

file(GLOB headers "${CMAKE_CURRENT_LIST_DIR}/*.hpp")
install(FILES ${headers} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/cppitertools)

file(GLOB internal_headers "${CMAKE_CURRENT_LIST_DIR}/internal/*.hpp")
install(FILES ${internal_headers} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/cppitertools/internal)
