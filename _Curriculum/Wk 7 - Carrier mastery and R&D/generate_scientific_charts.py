import matplotlib.pyplot as plt
import numpy as np

# Set professional IEEE-style parameters
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "figure.figsize": (3.5, 2.5), # Column width for IEEE
    "savefig.dpi": 300,
})

def generate_performance_curves():
    # Data from v10 paper stats
    labels = ['Binary', 'pHash', 'Xception', 'BERT']
    accuracy = [100.0, 91.0, 92.1, 92.8]
    precision = [100.0, 88.5, 92.4, 93.1]
    recall = [100.0, 94.2, 91.8, 92.5]

    x = np.arange(len(labels))
    width = 0.25

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, accuracy, width, label='Accuracy', color='#2b6cb0')
    rects2 = ax.bar(x, precision, width, label='Precision', color='#4299e1')
    rects3 = ax.bar(x + width, recall, width, label='Recall', color='#90cdf4')

    ax.set_ylabel('Percentage (%)')
    ax.set_title('Pipeline Phase Performance')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc='lower right')
    ax.set_ylim(0, 115) # Room for labels

    plt.tight_layout()
    plt.savefig('E:/Wk 7 - Carrier mastery and R&D/Career_Mastery_Hub/04_Experience_and_Projects/College_Projects/Decentralized_Social_Media_Project/Conferenece paper/fig3_performance_metrics.png')
    print("Fig 3 generated.")

def generate_latency_chart():
    # Latency Data
    labels = ['Binary', 'pHash', 'Xception', 'BERT']
    latency = [2.1, 8.4, 118.5, 132.8]

    fig, ax = plt.subplots(figsize=(3.5, 2.0))
    ax.plot(labels, latency, marker='o', linestyle='-', color='#e53e3e', linewidth=1.5)
    
    ax.set_ylabel('Latency (ms)')
    ax.set_title('Inference Latency per Stage')
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig('E:/Wk 7 - Carrier mastery and R&D/Career_Mastery_Hub/04_Experience_and_Projects/College_Projects/Decentralized_Social_Media_Project/Conferenece paper/fig4_latency_trends.png')
    print("Fig 4 generated.")

if __name__ == "__main__":
    generate_performance_curves()
    generate_latency_chart()
