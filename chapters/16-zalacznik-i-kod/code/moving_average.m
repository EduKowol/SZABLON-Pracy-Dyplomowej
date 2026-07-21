function filtered = moving_average(samples, window)
%MOVING_AVERAGE Causal moving average with a shortened initial window.

arguments
    samples (1,:) double
    window (1,1) double {mustBeInteger, mustBePositive}
end

filtered = zeros(size(samples));

for k = 1:numel(samples)
    first = max(1, k - window + 1);
    filtered(k) = mean(samples(first:k));
end
end
