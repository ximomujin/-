#include <math.h>
#include <stdint.h>
#include <stdio.h>

/* 固定非零种子使结果可复现，生成器仅用于教学模拟。 */
static uint32_t next_random(uint32_t *state)
{
    *state ^= *state << 13;
    *state ^= *state >> 17;
    *state ^= *state << 5;
    return *state;
}

int main(void)
{
    enum { walks = 60000, steps = 200 };
    const double step_length_m = 0.01;
    const double step_time_s = 0.02;
    uint32_t random_state = UINT32_C(20221126);
    double displacement_sum = 0.0;
    double squared_displacement_sum = 0.0;

    for (int trial = 0; trial < walks; ++trial) {
        int lattice_position = 0;
        for (int step = 0; step < steps; ++step) {
            if (next_random(&random_state) & UINT32_C(1)) {
                ++lattice_position;
            } else {
                --lattice_position;
            }
        }
        const double displacement = lattice_position * step_length_m;
        displacement_sum += displacement;
        squared_displacement_sum += displacement * displacement;
    }

    const double mean = displacement_sum / walks;
    const double mean_square = squared_displacement_sum / walks;
    const double theoretical_mean_square = steps * step_length_m * step_length_m;
    const double mean_standard_error = sqrt(theoretical_mean_square / walks);
    const double mean_square_standard_error =
        step_length_m * step_length_m * sqrt(2.0 * steps * (steps - 1) / walks);
    const double time_s = steps * step_time_s;
    const double estimated_diffusivity = mean_square / (2.0 * time_s);
    const double theoretical_diffusivity = theoretical_mean_square / (2.0 * time_s);

    printf("time: %.2f s\n", time_s);
    printf("mean displacement: %.7f m (theory 0)\n", mean);
    printf("mean square displacement: %.7f m^2 (theory %.7f)\n",
           mean_square, theoretical_mean_square);
    printf("estimated diffusivity: %.7f m^2/s (theory %.7f)\n",
           estimated_diffusivity, theoretical_diffusivity);

    if (fabs(mean) > 6.0 * mean_standard_error ||
        fabs(mean_square - theoretical_mean_square) > 6.0 * mean_square_standard_error) {
        fputs("validation failed: result differs by more than six standard errors\n",
              stderr);
        return 1;
    }

    puts("validation passed");
    return 0;
}
