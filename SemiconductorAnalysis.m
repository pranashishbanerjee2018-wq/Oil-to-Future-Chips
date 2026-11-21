%% SEMICONDUCTOR ANALYSIS & COMPUTATIONAL MICROELECTRONICS
% Project: "Semiconductors — The New Oil of the Future"
% Authors: Dr. Theodore Voss & Dr. Caleb Sterling
% Description: Rigorous engineering calculations and visualization for semiconductor physics,
%              transistor characteristics, CMOS power, fabrication yield, and scaling.

function SemiconductorAnalysis()
    fprintf('========================================================================\n');
    fprintf('  SEMICONDUCTOR COMPUTATIONAL ENGINEERING SUITE\n');
    fprintf('  "Semiconductors — The New Oil of the Future"\n');
    fprintf('  Authors: Dr. Theodore Voss & Dr. Caleb Sterling\n');
    fprintf('========================================================================\n\n');

    % Create output directories if they do not exist
    if ~exist('results', 'dir'), mkdir('results'); end
    if ~exist('data', 'dir'), mkdir('data'); end

    %% PHYSICAL CONSTANTS (CODATA 2018 Recommended Values)
    q = 1.602176634e-19;       % Elementary charge (Coulombs, C)
    k_B = 1.380649e-23;        % Boltzmann constant (J/K)
    T = 300.0;                 % Temperature in Kelvin (Nominal room temperature, K)
    V_T = (k_B * T) / q;       % Thermal voltage (V_T ~= 25.85 mV at 300 K)
    eps_0 = 8.8541878128e-14;  % Vacuum permittivity (F/cm)
    eps_si = 11.7 * eps_0;     % Silicon permittivity (F/cm)
    eps_ox = 3.9 * eps_0;      % SiO2 permittivity (F/cm)

    fprintf('[INFO] Thermal Voltage V_T at %.1f K: %.4f V (%.2f mV)\n', T, V_T, V_T * 1000);

    %% EXPERIMENT 1: PN JUNCTION DIODE CHARACTERISTICS (Shockley Equation)
    % Equation: I_D = I_S * [exp(q*V_D / (n*k*T)) - 1]
    % Realistic Parameters for a Silicon PN Diode:
    I_s = 1.0e-14;             % Reverse saturation current (A)
    n = 1.05;                  % Ideality factor for silicon junction
    V_D = linspace(-0.5, 0.85, 500); % Applied junction voltage (V)

    % Numerical safeguard against exponent overflow:
    arg = min(V_D ./ (n * V_T), 50.0);
    I_diode = I_s * (exp(arg) - 1.0);

    % Plot Experiment 1
    fig1 = figure('Visible', 'off', 'Position', [100, 100, 900, 600]);
    plot(V_D, I_diode * 1e3, 'LineWidth', 2.5, 'Color', [0.0, 0.45, 0.74]);
    grid on;
    xlabel('Applied Voltage V_D (V)', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel('Diode Current I_D (mA)', 'FontSize', 12, 'FontWeight', 'bold');
    title('Experiment 1: Shockley PN Junction Diode I-V Characteristics', 'FontSize', 14);
    subtitle(sprintf('I_S = %.1e A, n = %.2f, T = %.0f K, V_T = %.2f mV', I_s, n, T, V_T*1e3));
    ylim([-0.5, 35]);
    xlim([-0.5, 0.85]);
    yline(0, '--k', 'LineWidth', 1);
    xline(0.7, ':r', 'Threshold Knee (~0.7V)', 'LabelVerticalAlignment', 'bottom', 'FontSize', 10);
    saveas(fig1, 'results/plot1_diode_iv.png');
    close(fig1);
    fprintf('[DONE] Experiment 1: Shockley Diode characteristics computed and plotted.\n');

    %% EXPERIMENT 2: MOSFET OUTPUT CHARACTERISTICS (Long-Channel Model)
    % Educational model demonstrating Linear and Saturation regimes:
    % Linear:     I_D = mu_n * C_ox * (W/L) * [(V_GS - V_TH)*V_DS - (V_DS^2)/2]
    % Saturation: I_D = 0.5 * mu_n * C_ox * (W/L) * (V_GS - V_TH)^2 * (1 + lambda*V_DS)
    mu_n = 450;                % Electron mobility in inversion layer (cm^2 / V*s)
    t_ox = 3.0e-7;             % Oxide thickness (cm, 3 nm)
    C_ox = eps_ox / t_ox;      % Oxide capacitance per unit area (F/cm^2)
    W_over_L = 20.0;           % Transistor width to length ratio
    V_TH = 0.40;               % Threshold voltage (V)
    lambda = 0.04;             % Channel-length modulation parameter (V^-1)
    k_prime = mu_n * C_ox;     % Process transconductance parameter (A/V^2)

    V_GS_values = [0.6, 0.8, 1.0, 1.2, 1.4];
    V_DS = linspace(0, 1.8, 300);

    fig2 = figure('Visible', 'off', 'Position', [100, 100, 900, 600]);
    hold on;
    colors = [0.1 0.2 0.8; 0.0 0.6 0.5; 0.8 0.4 0.0; 0.8 0.1 0.2; 0.5 0.0 0.7];

    for idx = 1:length(V_GS_values)
        vgs = V_GS_values(idx);
        V_ov = max(0, vgs - V_TH);
        I_d = zeros(size(V_DS));
        for j = 1:length(V_DS)
            vds = V_DS(j);
            if vds < V_ov
                % Linear region
                I_d(j) = k_prime * W_over_L * (V_ov * vds - 0.5 * vds^2);
            else
                % Saturation region
                I_d(j) = 0.5 * k_prime * W_over_L * (V_ov^2) * (1 + lambda * (vds - V_ov));
            end
        end
        plot(V_DS, I_d * 1e3, 'LineWidth', 2.2, 'Color', colors(idx, :), ...
            'DisplayName', sprintf('V_{GS} = %.1f V (V_{OV}=%.1fV)', vgs, V_ov));
    end
    grid on;
    xlabel('Drain-Source Voltage V_{DS} (V)', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel('Drain Current I_D (mA)', 'FontSize', 12, 'FontWeight', 'bold');
    title('Experiment 2: Long-Channel nMOSFET Output (I_D - V_{DS}) Characteristics', 'FontSize', 14);
    subtitle(sprintf('W/L = %.0f, V_{TH} = %.2f V, t_{ox} = %.1f nm', W_over_L, V_TH, t_ox*1e7));
    legend('Location', 'northwest', 'FontSize', 10);
    saveas(fig2, 'results/plot2_mosfet_output.png');
    close(fig2);
    fprintf('[DONE] Experiment 2: MOSFET output characteristics computed and plotted.\n');

    %% EXPERIMENT 3: CMOS DYNAMIC POWER CONSUMPTION
    % Equation: P_dynamic = alpha * C_eff * V_DD^2 * f
    alpha = 0.15;              % Activity factor (fraction of nodes switching per cycle)
    C_eff = 2.5e-9;            % Switched effective capacitance (2.5 nF)
    frequencies = [1.0e9, 2.0e9, 3.0e9, 4.0e9]; % 1 to 4 GHz
    V_DD = linspace(0.6, 1.3, 100);             % Supply voltage range

    fig3 = figure('Visible', 'off', 'Position', [100, 100, 900, 600]);
    hold on;
    f_colors = [0.15 0.55 0.85; 0.2 0.7 0.3; 0.95 0.6 0.1; 0.85 0.2 0.2];

    for idx = 1:length(frequencies)
        f_val = frequencies(idx);
        P_dyn = alpha * C_eff * (V_DD.^2) * f_val;
        plot(V_DD, P_dyn, 'LineWidth', 2.4, 'Color', f_colors(idx, :), ...
            'DisplayName', sprintf('f = %.1f GHz', f_val / 1e9));
    end
    grid on;
    xlabel('Supply Voltage V_{DD} (V)', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel('Dynamic Power Consumption P_{dyn} (Watts)', 'FontSize', 12, 'FontWeight', 'bold');
    title('Experiment 3: CMOS Dynamic Power vs. Supply Voltage (P \propto V^2 \cdot f)', 'FontSize', 14);
    subtitle(sprintf('Switched Capacitance C = %.1f nF, Activity Factor \\alpha = %.2f', C_eff*1e9, alpha));
    legend('Location', 'northwest', 'FontSize', 10);
    saveas(fig3, 'results/plot3_cmos_power.png');
    close(fig3);
    fprintf('[DONE] Experiment 3: CMOS dynamic power scaling computed and plotted.\n');

    %% EXPERIMENT 4: CHIP MANUFACTURING YIELD VS. DIE AREA
    % Models:
    % Poisson Yield Model: Y_Poisson = exp(-D_0 * A)
    % Murphy Yield Model:  Y_Murphy  = ((1 - exp(-D_0 * A)) / (D_0 * A))^2
    % Parameters:
    % D_0 = Defect density (defects per cm^2)
    % A = Die area (cm^2)
    A_mm2 = linspace(20, 850, 200);   % Die area in mm^2 (e.g. from IoT chip to GPU reticle limit)
    A_cm2 = A_mm2 / 100.0;           % Convert mm^2 to cm^2
    D0_nominal = 0.08;               % 0.08 defects / cm^2 (Modern mature 300mm fab)
    D0_values = [0.04, 0.08, 0.15];   % Low, Medium, High defect densities

    fig4 = figure('Visible', 'off', 'Position', [100, 100, 900, 600]);
    hold on;
    y_styles = {'-', '--', '-.'};
    y_colors = [0.1 0.7 0.3; 0.0 0.45 0.85; 0.85 0.25 0.1];

    for idx = 1:length(D0_values)
        d0 = D0_values(idx);
        Y_poisson = exp(-d0 * A_cm2) * 100;
        Y_murphy = (((1 - exp(-d0 * A_cm2)) ./ (d0 * A_cm2)).^2) * 100;
        plot(A_mm2, Y_poisson, 'LineStyle', '-', 'LineWidth', 2.2, 'Color', y_colors(idx, :), ...
            'DisplayName', sprintf('Poisson: D_0 = %.2f def/cm^2', d0));
        plot(A_mm2, Y_murphy, 'LineStyle', ':', 'LineWidth', 1.8, 'Color', y_colors(idx, :), ...
            'DisplayName', sprintf('Murphy: D_0 = %.2f def/cm^2', d0));
    end
    grid on;
    xlabel('Die Area A (mm^2)', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel('Manufacturing Yield Y (%)', 'FontSize', 12, 'FontWeight', 'bold');
    title('Experiment 4: Silicon Wafer Fabrication Yield vs. Die Area', 'FontSize', 14);
    subtitle('Illustrative Comparison of Poisson and Murphy Defect Distribution Models');
    legend('Location', 'northeast', 'FontSize', 9);
    ylim([0, 100]);
    saveas(fig4, 'results/plot4_yield_model.png');
    close(fig4);
    fprintf('[DONE] Experiment 4: Chip yield models computed and plotted.\n');

    %% EXPERIMENT 5: TRANSISTOR SCALING AND HISTORICAL EVOLUTION (Moore's Law)
    years = [1971, 1974, 1978, 1982, 1985, 1989, 1993, 1997, 2000, 2006, 2012, 2017, 2020, 2022, 2024];
    names = {'Intel 4004', 'Intel 8080', 'Intel 8086', 'Intel 286', 'Intel 386', ...
             'Intel 486', 'Pentium', 'Pentium II', 'Pentium 4', 'Core 2 Duo', ...
             'Core i7 (Ivy)', 'AMD EPYC', 'Apple M1', 'Apple M2 Max', 'NVIDIA B200'};
    transistor_counts = [2.25e3, 6.0e3, 2.9e4, 1.34e5, 2.75e5, ...
                         1.18e6, 3.1e6, 7.5e6, 4.2e7, 2.91e8, ...
                         1.4e9, 1.92e10, 1.6e10, 6.7e10, 2.08e11];

    fig5 = figure('Visible', 'off', 'Position', [100, 100, 950, 620]);
    semilogy(years, transistor_counts, 'o-', 'LineWidth', 2.5, 'MarkerSize', 8, ...
             'Color', [0.0, 0.45, 0.74], 'MarkerFaceColor', [0.85, 0.33, 0.1]);
    grid on;
    xlabel('Year of Introduction', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel('Transistor Count (Logarithmic Scale)', 'FontSize', 12, 'FontWeight', 'bold');
    title('Experiment 5: Transistor Scaling Across Microprocessor Generations', 'FontSize', 14);
    subtitle('Historical Exponential Growth (Moore''s Law: Doubling approx. every 24 months)');
    
    % Label key milestones
    for i = [1, 3, 6, 7, 10, 13, 15]
        text(years(i) + 0.5, transistor_counts(i), names{i}, 'FontSize', 9, 'FontWeight', 'bold');
    end
    xlim([1969, 2027]);
    saveas(fig5, 'results/plot5_moores_law.png');
    close(fig5);
    fprintf('[DONE] Experiment 5: Historical Moore''s Law scaling plotted.\n');

    %% EXPORT SUMMARY DATA AS CSV AND JSON
    % Save key reference values to CSV
    fid = fopen('data/semiconductor_results.csv', 'w');
    fprintf(fid, 'Metric,Value,Units,Description\n');
    fprintf(fid, 'Thermal_Voltage_300K,%.5f,V,kT/q at 300 Kelvin\n', V_T);
    fprintf(fid, 'Diode_TurnOn_Knee,0.70,V,Nominal silicon PN forward voltage\n');
    fprintf(fid, 'MOSFET_VTH,%.2f,V,Long-channel threshold voltage\n', V_TH);
    fprintf(fid, 'MOSFET_Max_ID_1.4V,%.4f,mA,Saturation current at VGS=1.4V VDS=1.8V\n', max(I_d)*1e3);
    fprintf(fid, 'CMOS_Power_1V_3GHz,%.4f,W,Dynamic power at 1.0V and 3.0GHz\n', alpha * C_eff * (1.0^2) * 3.0e9);
    fprintf(fid, 'Yield_100mm2_D0_0.08,%.2f,%%,Poisson yield for 100mm2 die\n', exp(-0.08 * (100/100)) * 100);
    fprintf(fid, 'Modern_Max_Transistors,2.08e11,count,NVIDIA Blackwell B200 (2024)\n');
    fclose(fid);

    % Save JSON data for web visualization
    fid = fopen('data/semiconductor_data.json', 'w');
    fprintf(fid, '{\n');
    fprintf(fid, '  "metadata": {\n');
    fprintf(fid, '    "project": "Semiconductors — The New Oil of the Future",\n');
    fprintf(fid, '    "environment": "MATLAB 2024 / Scientific Engine",\n');
    fprintf(fid, '    "temperature_K": %.1f,\n', T);
    fprintf(fid, '    "thermal_voltage_V": %.5f\n', V_T);
    fprintf(fid, '  },\n');
    fprintf(fid, '  "experiment1_diode": {\n');
    fprintf(fid, '    "I_s_A": %.2e,\n', I_s);
    fprintf(fid, '    "n": %.2f,\n', n);
    fprintf(fid, '    "samples": %d\n', length(V_D));
    fprintf(fid, '  },\n');
    fprintf(fid, '  "experiment2_mosfet": {\n');
    fprintf(fid, '    "V_TH_V": %.2f,\n', V_TH);
    fprintf(fid, '    "W_over_L": %.1f,\n', W_over_L);
    fprintf(fid, '    "t_ox_nm": %.1f\n', t_ox * 1e7);
    fprintf(fid, '  },\n');
    fprintf(fid, '  "experiment3_power": {\n');
    fprintf(fid, '    "alpha": %.2f,\n', alpha);
    fprintf(fid, '    "C_eff_nF": %.2f\n', C_eff * 1e9);
    fprintf(fid, '  },\n');
    fprintf(fid, '  "experiment4_yield": {\n');
    fprintf(fid, '    "D0_nominal": %.2f\n', D0_nominal);
    fprintf(fid, '  },\n');
    fprintf(fid, '  "experiment5_scaling": {\n');
    fprintf(fid, '    "milestones_count": %d\n', length(years));
    fprintf(fid, '  }\n');
    fprintf(fid, '}\n');
    fclose(fid);

    fprintf('[SUCCESS] All computations completed and exported to data/ and results/.\n');
end
