#include <algorithm>
#include <cstddef>
#include <stdexcept>
#include <vector>
std::vector<double> moving_average(
    const std::vector<double>& samples,
    std::size_t window) {
    if (window == 0) {
        throw std::invalid_argument("window must be positive");
    }
    std::vector<double> result;
    result.reserve(samples.size());
    double running_sum = 0.0;
    for (std::size_t index = 0; index < samples.size(); ++index) {
        running_sum += samples[index];
        if (index >= window) {
            running_sum -= samples[index - window];
        }
        const auto count = std::min(index + 1, window);
        result.push_back(running_sum / static_cast<double>(count));
    }
    return result;
}
