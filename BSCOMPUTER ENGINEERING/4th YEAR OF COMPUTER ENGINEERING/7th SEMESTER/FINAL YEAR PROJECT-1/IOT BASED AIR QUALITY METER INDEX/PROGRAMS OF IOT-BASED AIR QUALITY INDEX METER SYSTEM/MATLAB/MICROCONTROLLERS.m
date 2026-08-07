% Define microcontroller specifications
microcontrollers = {'ESP32', 'ESP8266', 'Arduino UNO'};
% CPU Speed in MHz
cpu_speed = [240, 160, 16];
% RAM in KB
ram = [520, 160, 2];
% Flash Memory in MB
flash = [4, 4, 0.032];
% GPIO Pins
gpio = [36, 17, 14];
% ADC Resolution (bits)
adc = [12, 10, 10];
% Create figure with subplots
figure('Name', 'Microcontroller Comparison', 'Position', [100, 100, 1200, 800]);
% 1. CPU Speed Comparison
subplot(2,3,1)
bar(cpu_speed)
title('CPU Speed Comparison')
xlabel('Microcontrollers')
ylabel('Speed (MHz)')
set(gca, 'XTick', 1:3, 'XTickLabel', microcontrollers)
grid on
% 2. RAM Comparison
subplot(2,3,2)
bar(ram)
title('RAM Comparison')
xlabel('Microcontrollers')
ylabel('RAM (KB)')
set(gca, 'XTick', 1:3, 'XTickLabel', microcontrollers)
grid on
% 3. Flash Memory Comparison
subplot(2,3,3)
bar(flash)
title('Flash Memory Comparison')
xlabel('Microcontrollers')
ylabel('Flash (MB)')
set(gca, 'XTick', 1:3, 'XTickLabel', microcontrollers)
grid on
% 4. GPIO Pins Comparison
subplot(2,3,4)
bar(gpio)
title('GPIO Pins Comparison')
xlabel('Microcontrollers')
ylabel('Number of GPIO Pins')
set(gca, 'XTick', 1:3, 'XTickLabel', microcontrollers)
grid on
% 5. ADC Resolution Comparison
subplot(2,3,5)
bar(adc)
title('ADC Resolution Comparison')
xlabel('Microcontrollers')
ylabel('Resolution (bits)')
set(gca, 'XTick', 1:3, 'XTickLabel', microcontrollers)
grid on
% 6. Radar Chart for Overall Comparison
subplot(2,3,6)
% Normalize the data for radar chart
normalized_data = [
    cpu_speed./max(cpu_speed);
    ram./max(ram);
    flash./max(flash);
    gpio./max(gpio);
    adc./max(adc)
];
categories = {'CPU Speed', 'RAM', 'Flash', 'GPIO', 'ADC'};
spider_plot(normalized_data', categories, 'Microcontrollers', microcontrollers);
title('Overall Comparison (Normalized)')
% Add color to all plots
colormap('summer')
% Adjust layout
sgtitle('Microcontroller Specifications Comparison')
set(gcf, 'Color', 'white')
% Function for creating spider plot
function spider_plot(P, categories, legendTitle, legendLabels)
    % Number of variables
    num_vars = size(P, 2);
    % Angles for each axis
    angles = linspace(0, 2*pi, num_vars+1);
    % Plot data points
    colors = lines(size(P, 1));
    % Create the plot
    polarplot([angles(1:end-1), angles(1)], [P(1,:), P(1,1)], '-o', 'LineWidth', 2);
    hold on
    for i = 2:size(P, 1)
        polarplot([angles(1:end-1), angles(1)], [P(i,:), P(i,1)], '-o', 'LineWidth', 2);
    end
    % Fill in the plot
    pax = gca;
    pax.ThetaDir = 'clockwise';
    pax.ThetaZeroLocation = 'top';
    % Set the labels
    pax.ThetaTick = rad2deg(angles(1:end-1));
    pax.ThetaTickLabel = categories;
    % Add legend
    legend(legendLabels, 'Location', 'southoutside')
    grid on
end