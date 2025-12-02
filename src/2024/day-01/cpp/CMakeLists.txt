cmake_minimum_required(VERSION 3.10)
project(AdventOfCode)

set(CMAKE_CXX_STANDARD 23)

# Add executable with specific source files
add_executable(aoc
    src/main.cpp
    src/part1/part1.cpp
    src/part2/part2.cpp
)

# Add include directories for the target
target_include_directories(aoc PRIVATE src/part1 src/part2)

