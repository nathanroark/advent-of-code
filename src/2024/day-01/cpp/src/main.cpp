#include <algorithm>
#include <cassert>
#include <chrono>
#include <fstream>
#include <iostream>
#include <vector>

#include "part1/part1.h"
#include "part2/part2.h"

std::string read_file(const std::string &file_path) {
  std::ifstream file(file_path);
  if (!file) {
    std::cerr << "Could not open file: " << file_path << std::endl;
    return "";
  }
  return std::string((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
}

std::string trim(const std::string &str) {
  std::string result = str;

  // Trim leading whitespace
  result.erase(result.begin(), std::find_if_not(result.begin(), result.end(), [](unsigned char c) {
                 return std::isspace(c);
               }));

  // Trim trailing whitespace
  result.erase(std::find_if_not(result.rbegin(), result.rend(),
                                [](unsigned char c) { return std::isspace(c); })
                 .base(),
               result.end());

  return result;
}

int main(void) {
  std::string input = trim(read_file("../data/input.txt"));
  std::string test1 = trim(read_file("../data/test1.txt"));
  std::string test2 = trim(read_file("../data/test2.txt"));

  // Test case with assertion
  assert(part_1_1(test1) == 142);
  std::cout << "Assertion passed for test1!" << std::endl;

  // Number of runs for averaging
  constexpr int num_runs = 1;

  // Struct to store timing results for each solution
  struct SolutionResult {
    std::string name;
    int result;
    double avg_time;
  };

  // Measure and store execution time for each solution
  auto run_and_measure = [&](const std::string &name, auto &&func, const std::string &input) {
    double total_time = 0;
    int result = 0;

    for (int i = 0; i < num_runs; ++i) {
      auto start = std::chrono::high_resolution_clock::now();
      result = func(input); // Run the function
      auto end = std::chrono::high_resolution_clock::now();
      total_time += std::chrono::duration<double, std::milli>(end - start).count();
    }

    double average_time = total_time / num_runs;
    return SolutionResult{name, result, average_time};
  };

  // Vectors to hold results for each part
  std::vector<SolutionResult> part1_results;
  std::vector<SolutionResult> part2_results;

  // Run and collect results for each Part 1 solution
  part1_results.push_back(run_and_measure("Solution 1 (fold_left)", part_1_1, input));
  part1_results.push_back(run_and_measure("Solution 2 (transform_reduce)", part_1_2, input));
  part1_results.push_back(
    run_and_measure("Solution 3 (split views with accumulate)", part_1_3, input));
  part1_results.push_back(
    run_and_measure("Solution 4 (transform and accumulate)", part_1_4, input));

  // Run and collect results for each Part 2 solution
  part2_results.push_back(run_and_measure("Traditional Strategy", part_2_1, input));
  part2_results.push_back(run_and_measure("Reusable Extraction Strategy", part_2_2, input));
  part2_results.push_back(
    run_and_measure("Streamed Accumulate Extraction Strategy", part_2_3, input));
  part2_results.push_back(
    run_and_measure("Streamed Built-in Extraction Strategy", part_2_4, input));

  // Sort results by average time for each part
  auto sort_by_time = [](const SolutionResult &a, const SolutionResult &b) {
    return a.avg_time < b.avg_time;
  };
  std::sort(part1_results.begin(), part1_results.end(), sort_by_time);
  std::sort(part2_results.begin(), part2_results.end(), sort_by_time);

  // Print sorted results for Part 1
  std::cout << "----------------------------------------------" << std::endl;
  std::cout << "Day 1, Puzzle 1 Solutions (Ranked by Average Execution Time):" << std::endl;
  std::cout << "----------------------------------------------" << std::endl;
  int rank = 1;
  for (const auto &res : part1_results) {
    std::cout << rank++ << ": " << res.name << ", Time: " << res.avg_time << " ms" << std::endl;
  }

  // Print sorted results for Part 2
  std::cout << "----------------------------------------------" << std::endl;
  std::cout << "Day 1, Puzzle 2 Solutions (Ranked by Average Execution Time):" << std::endl;
  std::cout << "----------------------------------------------" << std::endl;
  rank = 1;
  for (const auto &res : part2_results) {
    std::cout << rank++ << ": " << res.result << " " << res.name << ", Time: " << res.avg_time
              << " ms" << std::endl;
  }
  std::cout << "----------------------------------------------" << std::endl;

  return 0;
}
