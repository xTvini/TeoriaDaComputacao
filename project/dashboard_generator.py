import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from project.constants.mergesort_comparison_constants import *

df_py = pd.read_csv(PYTHON_CSV)
df_c = pd.read_csv(C_CSV)

# Theoretical complexity: O(n log n)
def theoretical_complexity(n):
    return n * math.log2(n)

df_py['Theoretical_nlogn'] = df_py['InputSize'].apply(theoretical_complexity)
df_c['Theoretical_nlogn'] = df_c['InputSize'].apply(theoretical_complexity)

# Add language column
df_py[COL_LANGUAGE] = LANG_PYTHON
df_c[COL_LANGUAGE] = LANG_C

# Merge for comparison
df_all = pd.concat([df_py, df_c], ignore_index=True)

# Calculate execution speed (InputSize / ExecutionTime_ms)
df_all[COL_EXECSPEED] = df_all[COL_INPUT_SIZE] / df_all[COL_EXEC_TIME]

# Calculate stddev for execution speed (items/ms) if not present
if 'ExecSpeed_items_per_ms_stddev' not in df_all.columns:
    # Propagate stddev: stddev(items/ms) = (InputSize / ExecutionTime_ms^2) * ExecutionTime_ms_stddev
    df_all['ExecSpeed_items_per_ms_stddev'] = (
        df_all[COL_INPUT_SIZE] * df_all['ExecutionTime_ms_stddev'] / (df_all[COL_EXEC_TIME] ** 2)
    )

# Group and average by InputSize and Language, and also get stddev for each metric
agg_dict = {
    COL_EXEC_TIME: 'mean',
    COL_THEORY: 'mean',
    COL_EXECSPEED: 'mean',
    'ExecutionTime_ms_stddev': 'mean',
    'ExecSpeed_items_per_ms_stddev': 'mean',
}
# For C, stddev is always 0 in the CSV, but for Python it's meaningful
if 'ExecutionTime_ms_stddev' not in df_all.columns:
    df_all['ExecutionTime_ms_stddev'] = 0.0
if 'ExecSpeed_items_per_ms_stddev' not in df_all.columns:
    df_all['ExecSpeed_items_per_ms_stddev'] = 0.0

# Calculate stddev for execution speed (items/ms) if not present
if 'ExecSpeed_items_per_ms_stddev' not in df_all.columns:
    df_all['ExecSpeed_items_per_ms_stddev'] = 0.0

# Use stddev from the CSVs for time, and calculate for speed
for lang in [LANG_PYTHON, LANG_C]:
    mask = df_all[COL_LANGUAGE] == lang
    df_all.loc[mask, 'ExecSpeed_items_per_ms_stddev'] = (
        df_all.loc[mask, 'ExecutionTime_ms_stddev'] * df_all.loc[mask, COL_EXECSPEED] / df_all.loc[mask, COL_EXEC_TIME]
    )

# Group and aggregate
agg_dict = {
    COL_EXEC_TIME: 'mean',
    COL_THEORY: 'mean',
    COL_EXECSPEED: 'mean',
    'ExecutionTime_ms_stddev': 'mean',
    'ExecSpeed_items_per_ms_stddev': 'mean',
}
df_all_grouped = df_all.groupby([COL_LANGUAGE, COL_INPUT_SIZE], as_index=False).agg(agg_dict)

# Calculate execution speed (InputSize / ExecutionTime_ms)
df_all_grouped[COL_EXECSPEED] = df_all_grouped[COL_INPUT_SIZE] / df_all_grouped[COL_EXEC_TIME]

# Table: Dataset size, measured time, theoretical complexity, execution speed, language
summary_table = df_all_grouped[[COL_LANGUAGE, COL_INPUT_SIZE, COL_EXEC_TIME, COL_THEORY, COL_EXECSPEED]]
summary_table = summary_table.sort_values([COL_INPUT_SIZE, COL_LANGUAGE])
summary_table.to_csv(SUMMARY_CSV, index=False)
# Create separate plots for each language and metric

# Define color mapping for languages
LANG_COLORS = {LANG_PYTHON: '#FFD700', LANG_C: '#0072B2'}  # gold for Python, blue for C

# Plot 1: Measured times (log scale) - Separate plots
for lang, data in df_all_grouped.groupby(COL_LANGUAGE):
    plt.figure(figsize=(10,6))
    sns.lineplot(data=data, x=COL_INPUT_SIZE, y=COL_EXEC_TIME, marker='o', label=lang, color=LANG_COLORS[lang])
    plt.fill_between(data[COL_INPUT_SIZE],
                     data[COL_EXEC_TIME] - data['ExecutionTime_ms_stddev'],
                     data[COL_EXEC_TIME] + data['ExecutionTime_ms_stddev'],
                     color=LANG_COLORS[lang], alpha=0.2, label='Stddev')
    plt.title(f"{PLOT_TITLE_TIME} - {lang}")
    plt.xlabel(COL_INPUT_SIZE)
    plt.ylabel(Y_LABEL_TIME)
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.tight_layout()
    if lang == LANG_PYTHON:
        plt.savefig(TIME_COMPARISON_PYTHON_IMG)
    elif lang == LANG_C:
        plt.savefig(TIME_COMPARISON_C_IMG)

# Plot 1 Combined: Measured times (log scale)
plt.figure(figsize=(10,6))
for lang, data in df_all_grouped.groupby(COL_LANGUAGE):
    sns.lineplot(data=data, x=COL_INPUT_SIZE, y=COL_EXEC_TIME, marker='o', label=lang, color=LANG_COLORS[lang])
    plt.fill_between(data[COL_INPUT_SIZE],
                     data[COL_EXEC_TIME] - data['ExecutionTime_ms_stddev'],
                     data[COL_EXEC_TIME] + data['ExecutionTime_ms_stddev'],
                     color=LANG_COLORS[lang], alpha=0.15)
plt.title(PLOT_TITLE_TIME)
plt.xlabel(COL_INPUT_SIZE)
plt.ylabel(Y_LABEL_TIME)
plt.legend(title=LEGEND_LANGUAGE)
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.savefig(TIME_COMPARISON_IMG)

# Plot 2: Measured time vs Theoretical complexity - Separate plots
for lang, data in df_all_grouped.groupby(COL_LANGUAGE):
    plt.figure(figsize=(10,6))
    y = data[COL_EXEC_TIME]/data[COL_THEORY]
    yerr = data['ExecutionTime_ms_stddev']/data[COL_THEORY]
    plt.plot(data[COL_INPUT_SIZE], y, marker='o', label=lang, color=LANG_COLORS[lang])
    plt.fill_between(data[COL_INPUT_SIZE], y - yerr, y + yerr, color=LANG_COLORS[lang], alpha=0.2, label='Stddev')
    plt.title(f"{PLOT_TITLE_THEORY} - {lang}")
    plt.xlabel(COL_INPUT_SIZE)
    plt.ylabel(Y_LABEL_THEORY)
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.tight_layout()
    if lang == LANG_PYTHON:
        plt.savefig(TIME_VS_THEORY_PYTHON_IMG)
    elif lang == LANG_C:
        plt.savefig(TIME_VS_THEORY_C_IMG)

# Plot 2 Combined: Measured time vs Theoretical complexity (normalized, log scale)
plt.figure(figsize=(10,6))
for lang, data in df_all_grouped.groupby(COL_LANGUAGE):
    y = data[COL_EXEC_TIME]/data[COL_THEORY]
    yerr = data['ExecutionTime_ms_stddev']/data[COL_THEORY]
    plt.plot(data[COL_INPUT_SIZE], y, marker='o', label=lang, color=LANG_COLORS[lang])
    plt.fill_between(data[COL_INPUT_SIZE], y - yerr, y + yerr, color=LANG_COLORS[lang], alpha=0.15)
plt.title(PLOT_TITLE_THEORY)
plt.xlabel(COL_INPUT_SIZE)
plt.ylabel(Y_LABEL_THEORY)
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.tight_layout()
plt.savefig(TIME_VS_THEORY_IMG)

# Plot 3: Execution speed - Separate plots
for lang, data in df_all_grouped.groupby(COL_LANGUAGE):
    plt.figure(figsize=(10,6))
    sns.lineplot(data=data, x=COL_INPUT_SIZE, y=COL_EXECSPEED, marker='o', label=lang, color=LANG_COLORS[lang])
    plt.fill_between(data[COL_INPUT_SIZE],
                     data[COL_EXECSPEED] - data['ExecSpeed_items_per_ms_stddev'],
                     data[COL_EXECSPEED] + data['ExecSpeed_items_per_ms_stddev'],
                     color=LANG_COLORS[lang], alpha=0.2, label='Stddev')
    plt.title(f"{PLOT_TITLE_SPEED} - {lang}")
    plt.xlabel(COL_INPUT_SIZE)
    plt.ylabel(Y_LABEL_SPEED)
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    if lang == LANG_PYTHON:
        plt.savefig(EXECSPEED_PYTHON_IMG)
    elif lang == LANG_C:
        plt.savefig(EXECSPEED_C_IMG)

# Plot 3 Combined: Execution speed (log scale)
plt.figure(figsize=(10,6))
for lang, data in df_all_grouped.groupby(COL_LANGUAGE):
    sns.lineplot(data=data, x=COL_INPUT_SIZE, y=COL_EXECSPEED, marker='o', label=lang, color=LANG_COLORS[lang])
    plt.fill_between(data[COL_INPUT_SIZE],
                     data[COL_EXECSPEED] - data['ExecSpeed_items_per_ms_stddev'],
                     data[COL_EXECSPEED] + data['ExecSpeed_items_per_ms_stddev'],
                     color=LANG_COLORS[lang], alpha=0.15)
plt.title(PLOT_TITLE_SPEED)
plt.xlabel(COL_INPUT_SIZE)
plt.ylabel(Y_LABEL_SPEED)
plt.legend(title=LEGEND_LANGUAGE)
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.savefig(EXECSPEED_IMG)

# Table for display (first 10 rows)
print(SUMMARY_PRINT)
print(summary_table.head(10).to_string(index=False))

print(CHARTS_SAVED_PRINT)



