% MATLAB Code for Simulating and Plotting PM2.5 and PM10 Data
% Clear workspace and command window
clear;
clc;
% Simulate time (in seconds)
simulationTime = 0:1:100; % 100 seconds at 1-second intervals
% Simulate PM2.5 and PM10 sensor data (randomly generated for this example)
% Replace this with real sensor data if available
PM2_5 = 10 + 5*randn(1, length(simulationTime)); % Mean 10, std deviation 5
PM10 = 20 + 8*randn(1, length(simulationTime));  % Mean 20, std deviation 8
% Ensure no negative values in simulated data
PM2_5(PM2_5 < 0) = 0;
PM10(PM10 < 0) = 0;
% Plot the data
figure;
plot(simulationTime, PM2_5, '-o', 'LineWidth', 1.5, 'MarkerSize', 6, 'Color', [0, 0.4470, 0.7410]); % PM2.5 plot
hold on;
plot(simulationTime, PM10, '-s', 'LineWidth', 1.5, 'MarkerSize', 6, 'Color', [0.8500, 0.3250, 0.0980]); % PM10 plot
hold off;
% Add title and labels
title('PM2.5 and PM10 Concentration Over Time', 'FontSize', 14);
xlabel('Time (seconds)', 'FontSize', 12);
ylabel('Concentration (\mug/m^3)', 'FontSize', 12);
legend({'PM2.5', 'PM10'}, 'FontSize', 12, 'Location', 'northwest');
% Add grid for better visualization
grid on;
% Highlight thresholds (if required)
hold on;
yline(35, '--', 'PM2.5 Threshold', 'Color', [0, 0.4470, 0.7410], 'LineWidth', 1);
yline(50, '--', 'PM10 Threshold', 'Color', [0.8500, 0.3250, 0.0980], 'LineWidth', 1);
hold off;
% Display summary statistics
disp('Summary of PM2.5 and PM10 Data:');
disp(['Mean PM2.5: ', num2str(mean(PM2_5)), ' \mug/m^3']);
disp(['Mean PM10: ', num2str(mean(PM10)), ' \mug/m^3']);
disp(['Max PM2.5: ', num2str(max(PM2_5)), ' \mug/m^3']);
disp(['Max PM10: ', num2str(max(PM10)), ' \mug/m^3']);
disp(['Min PM2.5: ', num2str(min(PM2_5)), ' \mug/m^3']);
disp(['Min PM10: ', num2str(min(PM10)), ' \mug/m^3']);