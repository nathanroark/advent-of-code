#include "part2.h"

static const std::unordered_map<std::string, int> word_to_digit = {
  {"one", 1}, {"two", 2},   {"three", 3}, {"four", 4}, {"five", 5},
  {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}};

// Traditional Strategy
int part_2_1(const std::string &input) {
  int sum = 0;

  auto input_view = input | std::views::split('\n');

  for (auto line_view : input_view) {
    std::string line(line_view.begin(), line_view.end());
    std::vector<int> digits;

    for (size_t i = 0; i < line.size(); ++i) {
      if (std::isdigit(line[i])) {
        digits.push_back(line[i] - '0');
        continue;
      }

      for (auto &[word, digit] : word_to_digit) {
        if (line.substr(i, word.size()) == word) {
          digits.push_back(digit);
          // skip over without missing possible overlap (eightwo == 82)
          i += word.size() - 2;
          break;
        }
      }
    }

    sum += digits.empty() ? 0 : digits.front() * 10 + digits.back();
  }

  return sum;
}

// Reusable Extraction Strategy
int part_2_2(const std::string &input) {
  auto extract_digits = [&](const std::string &line) {
    std::vector<int> digits;

    for (size_t i = 0; i < line.size(); ++i) {
      if (std::isdigit(line[i])) {
        digits.push_back(line[i] - '0');
        continue;
      }

      for (const auto &[word, digit] : word_to_digit) {
        if (line.substr(i, word.size()) == word) {
          digits.push_back(digit);
          // skip over  without missing possible overlap (eightwo == 82)
          i += word.size() - 2;
          break;
        }
      }
    }

    return digits.empty() ? 0 : digits.front() * 10 + digits.back();
  };

  return std::ranges::fold_left(
    input | std::views::split('\n') | std::views::transform([&](auto &&line_range) {
      return extract_digits(std::string(line_range.begin(), line_range.end()));
    }),
    0, std::plus{});
}

// Streamed Accumulate Extraction Strategy
int part_2_3(const std::string &input) {
  return std::ranges::fold_left(input | std::views::split('\n'), 0, [](int acc, auto &&line_range) {
    std::vector<int> digits;
    std::string_view line(&*line_range.begin(), std::ranges::distance(line_range));

    for (size_t i = 0; i < line.size(); ++i) {
      if (std::isdigit(line[i])) {
        digits.push_back(line[i] - '0');
        continue;
      }

      for (const auto &[word, digit] : word_to_digit) {
        if (line.substr(i, word.size()) == word) {
          digits.push_back(digit);
          // skip over without missing possible overlap (eightwo == 82)
          i += word.size() - 2;
          break;
        }
      }
    }

    return digits.empty() ? acc : acc + digits.front() * 10 + digits.back();
  });
}

// Streamed Built-in Extraction Strategy
int part_2_4(const std::string &input) {
  return std::ranges::fold_left(
    input | std::views::split('\n') | std::views::transform([](auto &&line_range) {
      std::vector<int> digits;
      std::string_view line(&*line_range.begin(), std::ranges::distance(line_range));

      for (size_t i = 0; i < line.size(); ++i) {
        if (std::isdigit(line[i])) {
          digits.push_back(line[i] - '0');
          continue;
        }

        for (const auto &[word, digit] : word_to_digit) {
          if (line.substr(i, word.size()) == word) {
            digits.push_back(digit);
            // skip over  without missing possible overlap (eightwo == 82)
            i += word.size() - 2;
            break;
          }
        }
      }

      return digits.empty() ? 0 : digits.front() * 10 + digits.back();
    }),
    0, std::plus{});
}
