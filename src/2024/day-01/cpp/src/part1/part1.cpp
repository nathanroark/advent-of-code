#include "part1.h"

// left fold over the range solution
int part_1_1(const std::string &input) {
  return std::ranges::fold_left(
    input | std::views::split('\n') | std::views::transform([](auto &&line) {
      auto digits = line
        | std::views::filter([](char c) { return std::isdigit(c); })
        | std::views::transform([](char c) { return c - '0'; });

      return digits.empty() ? 0 : digits.front() * 10 + digits.back();
    }),
    0, std::plus{});
}

// transform reduce solution
int part_1_2(const std::string &input) {
  auto lines = input | std::views::split('\n') | std::ranges::to<std::vector>();

  return std::transform_reduce(
    lines.begin(), lines.end(), 0, std::plus{}, [](auto &&line) {
      auto digits = line
        | std::views::filter([](char c) { return std::isdigit(c); })
        | std::views::transform([](char c) { return c - '0'; });

      return digits.empty() ? 0 : digits.front() * 10 + digits.back();
    });
}

// transform split view adapters into an accumulate solution
int part_1_3(const std::string &input) {
  auto results =
    input | std::views::split('\n') | std::views::transform([](auto line) {
      auto digits = line
        | std::views::filter([](char c) { return std::isdigit(c); })
        | std::views::transform([](char c) { return c - '0'; });

      return digits.empty() ? 0 : digits.front() * 10 + digits.back();
    });

  return std::accumulate(results.begin(), results.end(), 0);
}

// transform accumulate solution
int part_1_4(const std::string &content) {
  std::vector<int> results;

  for (auto line_view : content | std::views::split('\n')) {
    std::string line(line_view.begin(), line_view.end());

    auto digits = line
      | std::views::filter([](char c) { return std::isdigit(c); })
      | std::views::transform([](char c) { return c - '0'; });

    if (std::ranges::empty(digits)) {
      continue;
    }

    int value = *digits.begin() * 10 + *std::ranges::prev(digits.end());
    results.push_back(value);
  }

  return std::accumulate(results.begin(), results.end(), 0);
}
