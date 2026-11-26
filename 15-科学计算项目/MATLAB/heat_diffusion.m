function [x, numerical, reference] = heat_diffusion()
% 一维热传导的显式有限差分，输出细网格结果与同一时刻的解析解。

    length_m = 1.0;
    diffusivity = 0.01;
    final_time_s = 2.5;

    [~, coarse, coarse_reference] = solve_mode(40, length_m, diffusivity, final_time_s);
    [x, numerical, reference] = solve_mode(80, length_m, diffusivity, final_time_s);
    coarse_error = max(abs(coarse - coarse_reference));
    fine_error = max(abs(numerical - reference));
    refinement_ratio = coarse_error / fine_error;

    fprintf('coarse maximum error: %.8g\n', coarse_error);
    fprintf('fine maximum error: %.8g\n', fine_error);
    fprintf('error reduction ratio: %.5f\n', refinement_ratio);

    assert(all(numerical([1, end]) == 0), 'Boundary temperature changed.');
    assert(fine_error < 1e-4, 'Fine-grid error exceeds the tolerance.');
    assert(refinement_ratio > 3.8 && refinement_ratio < 4.2, ...
        'Refinement check did not show the expected second-order rate.');
    fprintf('validation passed\n');
end

function [x, temperature, exact] = solve_mode(cells, length_m, diffusivity, final_time_s)
    dx = length_m / cells;
    steps = ceil(final_time_s * diffusivity / (0.4 * dx^2));
    dt = final_time_s / steps;
    ratio = diffusivity * dt / dx^2;

    x = linspace(0, length_m, cells + 1);
    temperature = sin(pi * x / length_m);
    temperature([1, end]) = 0;

    for step = 1:steps
        % 右侧先求值，邻点均取本步开始时的温度。
        temperature(2:end-1) = temperature(2:end-1) + ratio * ...
            (temperature(3:end) - 2 * temperature(2:end-1) + temperature(1:end-2));
    end

    exact = exp(-diffusivity * (pi / length_m)^2 * final_time_s) * sin(pi * x / length_m);
    exact([1, end]) = 0;
end
