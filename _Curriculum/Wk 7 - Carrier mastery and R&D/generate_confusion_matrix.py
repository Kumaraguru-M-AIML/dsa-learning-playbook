import matplotlib.pyplot as plt
import numpy as np

# Set scientific styling
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "font.size": 10,
})

def generate_confusion_matrix():
    # Confusion Matrix Data (Normalized)
    # Rows: Actual (Real, Fake)
    # Columns: Predicted (Real, Fake)
    matrix = np.array([[0.941, 0.059], 
                       [0.076, 0.924]])
    
    fig, ax = plt.subplots(figsize=(3.5, 3.0))
    im = ax.imshow(matrix, cmap='Blues', alpha=0.8)

    # Labels
    ax.set_xticks(np.arange(2))
    ax.set_yticks(np.arange(2))
    ax.set_xticklabels(['Authentic', 'Manipulated'])
    ax.set_yticklabels(['Authentic', 'Manipulated'])
    
    ax.set_xlabel('Predicted Label')
    ax.set_ylabel('True Label')
    ax.set_title('Detection Confusion Matrix (XceptionNet)')

    # Add text annotations
    for i in range(2):
        for j in range(2):
            text = ax.text(j, i, f"{matrix[i, j]*100:.1f}%",
                           ha="center", va="center", color="black" if matrix[i, j] < 0.6 else "white")

    plt.tight_layout()
    plt.savefig('E:/Wk 7 - Carrier mastery and R&D/Career_Mastery_Hub/04_Experience_and_Projects/College_Projects/Decentralized_Social_Media_Project/Conferenece paper/fig5_confusion_matrix.png')
    print("Fig 5 generated.")

if __name__ == "__main__":
    generate_confusion_matrix()
