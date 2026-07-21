% Aproksymacja danych i eksport wykresu użytego w pracy.
rootDir = fileparts(fileparts(mfilename('fullpath')));
dataFile = fullfile(rootDir, 'data', 'aproksymacja.csv');
outputFile = fullfile(rootDir, 'figures', 'aproksymacja-matlab.pdf');

T = readtable(dataFile);
x = T.x;
y = T.measurement;

coefficients = polyfit(x, y, 1);
model = polyval(coefficients, x);
residuals = y - model;
rmse = sqrt(mean(residuals.^2));
rSquared = 1 - sum(residuals.^2) / sum((y - mean(y)).^2);

figure('Color', 'w');
scatter(x, y, 36, 'k', 'filled', 'DisplayName', 'Pomiary');
hold on;
plot(x, model, 'LineWidth', 2, 'Color', [0 70 125]/255, ...
    'DisplayName', 'Aproksymacja');
grid on;
xlabel('Wielkość wejściowa x');
ylabel('Wielkość wyjściowa y');
legend('Location', 'northwest');
exportgraphics(gcf, outputFile, 'ContentType', 'vector');

fprintf('a=%.6f, b=%.6f\n', coefficients(1), coefficients(2));
fprintf('RMSE=%.6f, R2=%.6f\n', rmse, rSquared);
