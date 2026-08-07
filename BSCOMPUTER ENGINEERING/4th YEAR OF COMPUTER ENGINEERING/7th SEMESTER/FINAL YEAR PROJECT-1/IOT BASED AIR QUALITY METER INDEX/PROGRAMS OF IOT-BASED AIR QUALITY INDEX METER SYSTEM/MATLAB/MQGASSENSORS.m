% MQ-5 and MQ-135 Gas Sensors Data and Plotting
clc;
clear;
close all;
% Constants (example calibration values from datasheets)
RL = 10; % Load resistance in kOhms
Vcc = 5; % Supply voltage in volts
% MQ-5 Sensor (SnO2, H2, LPG, CH4, CO, Alcohol)
MQ5_Ro = 10; % Sensor resistance in clean air (kOhms)
MQ5_Gases = {'SnO2', 'H2', 'LPG', 'CH4', 'CO', 'Alcohol'};
MQ5_Rs_Ro = [
    1.2, 1.1, 1.0, 0.9, 0.8, 0.7; % Rs/Ro for SnO2
    1.1, 0.9, 0.7, 0.6, 0.5, 0.4; % Rs/Ro for H2
    1.0, 0.8, 0.6, 0.5, 0.4, 0.3; % Rs/Ro for LPG
    0.9, 0.7, 0.5, 0.4, 0.3, 0.2; % Rs/Ro for CH4
    0.8, 0.6, 0.4, 0.3, 0.2, 0.1; % Rs/Ro for CO
    0.7, 0.5, 0.3, 0.2, 0.1, 0.05 % Rs/Ro for Alcohol
];
MQ5_PPM = [10, 50, 100, 200, 300, 400]; % Concentrations in ppm
% MQ-135 Sensor (SO2, NO2, O3, CO)
MQ135_Ro = 10; % Sensor resistance in clean air (kOhms)
MQ135_Gases = {'SO2', 'NO2', 'O3', 'CO'};
MQ135_Rs_Ro = [
    1.0, 0.9, 0.8, 0.7; % Rs/Ro for SO2
    0.9, 0.8, 0.7, 0.6; % Rs/Ro for NO2
    0.8, 0.7, 0.6, 0.5; % Rs/Ro for O3
    0.7, 0.6, 0.5, 0.4  % Rs/Ro for CO
];
MQ135_PPM = [20, 60, 120, 240]; % Concentrations in ppm
% Calculate Rs and voltage output for MQ-5
MQ5_Rs = MQ5_Ro * MQ5_Rs_Ro; % Sensor resistance for MQ-5
MQ5_Vout = MQ5_Rs ./ (MQ5_Rs + RL) * Vcc; % Voltage output for MQ-5
% Calculate Rs and voltage output for MQ-135
MQ135_Rs = MQ135_Ro * MQ135_Rs_Ro; % Sensor resistance for MQ-135
MQ135_Vout = MQ135_Rs ./ (MQ135_Rs + RL) * Vcc; % Voltage output for MQ-135
% Plotting MQ-5 Sensor Data
figure;
subplot(2, 1, 1);
hold on;
for i = 1:length(MQ5_Gases)
    plot(MQ5_PPM, MQ5_Vout(i, :), '-o', 'LineWidth', 1.5, 'DisplayName', MQ5_Gases{i});
end
title('MQ-5 Sensor (SnO2, H2, LPG, CH4, CO, Alcohol)');
xlabel('Gas Concentration (ppm)');
ylabel('Voltage Output (V)');
grid on;
legend('show');
hold off;
% Plotting MQ-135 Sensor Data
subplot(2, 1, 2);
hold on;
for i = 1:length(MQ135_Gases)
    plot(MQ135_PPM, MQ135_Vout(i, :), '-o', 'LineWidth', 1.5, 'DisplayName', MQ135_Gases{i});
end
title('MQ-135 Sensor (SO2, NO2, O3, CO)');
xlabel('Gas Concentration (ppm)');
ylabel('Voltage Output (V)');
grid on;
legend('show');
hold off;