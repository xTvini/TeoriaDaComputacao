import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from matplotlib.ticker import ScalarFormatter
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

# Table: Dataset size, measured time, theoretical complexity, execution speed, language
summary_table = df_all[[COL_LANGUAGE, COL_INPUT_SIZE, COL_EXEC_TIME, COL_THEORY, COL_EXECSPEED]]
summary_table = summary_table.sort_values([COL_INPUT_SIZE, COL_LANGUAGE])
summary_table.to_csv(SUMMARY_CSV, index=False)

# Plot 1: Measured times
plt.figure(figsize=(10,6))
sns.lineplot(data=df_all, x=COL_INPUT_SIZE, y=COL_EXEC_TIME, hue=COL_LANGUAGE, marker='o')
plt.title(PLOT_TITLE_TIME)
plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL_TIME)
plt.legend(title=LEGEND_LANGUAGE)
plt.grid(True)
plt.xticks(df_all[COL_INPUT_SIZE].unique())
plt.xlim(0, max(df_all[COL_INPUT_SIZE]) * 1.05)
plt.ylim(0, max(df_all[COL_EXEC_TIME]) * 1.1)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
plt.tight_layout()
plt.savefig(TIME_COMPARISON_IMG)

# Plot 2: Measured time vs Theoretical complexity (normalized)
plt.figure(figsize=(10,6))
for lang, group in df_all.groupby(COL_LANGUAGE):
    plt.plot(group[COL_INPUT_SIZE], group[COL_EXEC_TIME]/group[COL_THEORY], marker='o', label=lang)
plt.title(PLOT_TITLE_THEORY)
plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL_THEORY)
plt.legend()
plt.grid(True)
plt.xticks(df_all[COL_INPUT_SIZE].unique())
plt.xlim(0, max(df_all[COL_INPUT_SIZE]) * 1.05)
plt.ylim(0, (df_all[COL_EXEC_TIME]/df_all[COL_THEORY]).max() * 1.1)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
plt.tight_layout()
plt.savefig(TIME_VS_THEORY_IMG)

# Plot 3: Execution speed
plt.figure(figsize=(10,6))
sns.lineplot(data=df_all, x=COL_INPUT_SIZE, y=COL_EXECSPEED, hue=COL_LANGUAGE, marker='o')
plt.title(PLOT_TITLE_SPEED)
plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL_SPEED)
plt.legend(title=LEGEND_LANGUAGE)
plt.grid(True)
plt.xticks(df_all[COL_INPUT_SIZE].unique())
plt.xlim(0, max(df_all[COL_INPUT_SIZE]) * 1.05)
plt.ylim(0, max(df_all[COL_EXECSPEED]) * 1.1)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
plt.tight_layout()
plt.savefig(EXECSPEED_IMG)

# Table for display (first 10 rows)
print(SUMMARY_PRINT)
print(summary_table.head(10).to_string(index=False))

print(CHARTS_SAVED_PRINT)
