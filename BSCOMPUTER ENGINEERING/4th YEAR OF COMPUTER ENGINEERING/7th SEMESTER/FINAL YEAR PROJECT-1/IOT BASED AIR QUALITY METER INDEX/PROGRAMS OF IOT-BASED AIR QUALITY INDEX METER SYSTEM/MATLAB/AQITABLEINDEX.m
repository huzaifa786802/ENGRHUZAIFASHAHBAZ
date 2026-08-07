% MATLAB code to define AQI ranges and plot the graph
% Define AQI categories
AQI_Categories = {"Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"};
AQI_Ranges = [0 50; 51 100; 101 150; 151 200; 201 300; 301 500];
Health_Impacts = {"No threat", "Possibly concerning for sensitive individuals", ...
    "Unhealthy for sensitive groups", "Unhealthy for everyone", ...
    "Entire population likely to be affected", "Serious health effects"};
% Define colors corresponding to each AQI range
Colors = [0 1 0;     % Green
          1 1 0;     % Yellow
          1 0.5 0;   % Orange
          1 0 0;     % Red
          0.5 0 0.5; % Purple
          0.3 0 0.3];% Dark Purple
% Create a figure for the bar plot
figure;
hold on;
% Loop through AQI categories and plot bars
for i = 1:length(AQI_Categories)
    bar(i, AQI_Ranges(i, 2), 'FaceColor', Colors(i, :), 'EdgeColor', 'none');
end
% Customize the plot
set(gca, 'XTick', 1:length(AQI_Categories), 'XTickLabel', AQI_Categories);
xlabel('AQI Categories');
ylabel('AQI Range');
title('Air Quality Index (AQI) Categories');
grid on;
ylim([0 550]);
legend(AQI_Categories, 'Location', 'northwest');
% Display AQI table in the command window
disp('AQI Table:');
disp('----------------------------------------------');
for i = 1:length(AQI_Categories)
    fprintf('Category: %-30s | Range: %3d-%3d | Health Impact: %s\n', AQI_Categories{i}, AQI_Ranges(i, 1), AQI_Ranges(i, 2), Health_Impacts{i});
end
hold off;