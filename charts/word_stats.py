import os
from collections import Counter
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import patheffects
import numpy as np

def generate_word_stats(text):
    """
    Generate basic word statistics.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Dictionary containing word statistics
    """
    words = re.findall(r'\w+', text.lower())
    word_count = len(words)
    unique_words = len(set(words))
    word_freq = dict(Counter(words).most_common(5))
    
    return {
        'total_words': word_count,
        'unique_words': unique_words,
        'most_common': word_freq
    }

def generate_wordcount_chart(original_text, summarized_text, output_dir='static'):
    """
    Generate and save a bar chart comparing word counts between original and summarized text.
    
    Args:
        original_text (str): The original input text
        summarized_text (str): The summarized version of the text
        output_dir (str): Directory to save the output image (default: 'static')
        
    Returns:
        str: Path to the generated chart image
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Count words
    original_word_count = len(re.findall(r'\w+', original_text))
    summary_word_count = len(re.findall(r'\w+', summarized_text))
    
    # Calculate reduction percentage
    reduction = ((original_word_count - summary_word_count) / original_word_count) * 100
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    # Data for plotting
    labels = ['Original', 'Summary']
    counts = [original_word_count, summary_word_count]

    # Neon accent colors
    neon_blue = '#00e6ff'
    neon_magenta = '#ff3cac'
    neon_cyan = '#50fae6'
    dark_bg = '#181a20'
    white = '#f8fafd'
    gray = '#bfc9d1'

    # Create bar chart with dark background
    fig, ax = plt.subplots(figsize=(5, 3), facecolor=dark_bg)
    fig.patch.set_facecolor(dark_bg)
    ax.set_facecolor(dark_bg)
    bars = ax.bar(labels, counts, color=[neon_blue, neon_magenta], width=0.5, edgecolor=neon_cyan, linewidth=3, zorder=3)

    # Add value labels (glow effect)
    for bar, color in zip(bars, [neon_blue, neon_magenta]):
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 8),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=14, color=white, fontweight='bold',
                    path_effects=[patheffects.withStroke(linewidth=5, foreground=dark_bg)])

    # Add reduction percentage as annotation (neon cyan box)
    ax.text(0.5, 0.93, 
            f'Reduction: {reduction:.1f}%',
            transform=ax.transAxes,
            ha='center', va='center',
            fontsize=13, color=dark_bg,
            bbox=dict(facecolor=neon_cyan, alpha=0.18, edgecolor=neon_cyan, boxstyle='round,pad=0.5'))

    # Style axes
    ax.tick_params(axis='x', colors=white, labelsize=14, length=0)
    ax.tick_params(axis='y', colors=gray, labelsize=12)
    ax.spines['bottom'].set_color(neon_cyan)
    ax.spines['left'].set_color(neon_cyan)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.grid(True, color='#23293d', linestyle='--', linewidth=1, alpha=0.25, zorder=0)
    ax.set_axisbelow(True)
    ax.set_ylabel('Word Count', color=gray, fontsize=13, labelpad=10)
    ax.set_title('Word Count Comparison', color=white, fontsize=16, weight='bold', pad=18)

    # Remove chart frame
    ax.set_frame_on(False)

    # Adjust layout and save
    plt.tight_layout(pad=2)
    output_path = os.path.join(output_dir, 'word_stats.png')
    plt.savefig(output_path, dpi=120, bbox_inches='tight', transparent=True)
    plt.close()
    return output_path
