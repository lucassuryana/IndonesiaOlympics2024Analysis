import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle

def filter_years(years, rank):
    """Filter years based on rank data."""
    return [years[i] for i in range(len(rank)) if rank[i] > 0]

def filter_data(years, num_athletes, num_sports, rank, total_medals, gold, silver, bronze, sports_medals_gold , sports_medals_silver, sports_medals_bronze  ):
    """Filter data based on rank availability."""
    filtered_years = [years[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_num_athletes = [num_athletes[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_num_sports = [num_sports[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_rank = [rank[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_total_medals = [total_medals[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_gold = [gold[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_silver = [silver[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_bronze = [bronze[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_sports_medal_gold =    [sports_medals_gold[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_sports_medal_silver =  [sports_medals_silver[i] for i in range(len(rank)) if rank[i] > 0]
    filtered_sports_medal_bronze =  [sports_medals_bronze[i] for i in range(len(rank)) if rank[i] > 0]
    return filtered_years, filtered_num_athletes, filtered_num_sports, filtered_rank, filtered_total_medals, filtered_gold, filtered_silver, filtered_bronze, filtered_sports_medal_gold, filtered_sports_medal_silver, filtered_sports_medal_bronze

def plot_medals(ax, filtered_years, filtered_rank, filtered_gold, filtered_silver, filtered_bronze, filtered_sports_medal_gold, filtered_sports_medal_silver, filtered_sports_medal_bronze):
    """Plot medals on the provided axis."""
    # Overlay squares representing medals above the bars
    square_size_1 = 2  # Side length of the square
    square_size_2 = 5.5  # Side length of the square
    square_vertical_spacing = 8  # Vertical spacing between rows of squares
    for i in range(len(filtered_years)):
        y_base = filtered_rank[i] + 5
        for j in range(filtered_gold[i]):
            x_loc = filtered_years[i] - square_size_1 / 2
            y_loc = y_base + j * square_vertical_spacing - square_size_1 / 2
            ax.add_patch(Rectangle(
                (x_loc, y_loc),
                square_size_1,
                square_size_2,
                color='#FDC861',
                zorder=10
            ))

            sports_gold = filtered_sports_medal_gold[i][j]
            sports_logo = mpimg.imread('sports/'+sports_gold+'.png')
            if sports_gold == 'climbing':
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.026)
            elif sports_gold == 'badminton':
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.014)
            else:
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.015)
            ax.add_artist(AnnotationBbox(imagebox_sports_logo, (x_loc + square_size_1/2, y_loc + square_size_2/2), frameon=False, pad=0.1, xycoords='data', box_alignment=(0.5, 0.5), zorder=11))

        for j in range(filtered_silver[i]):
            x_loc = filtered_years[i] - square_size_1 / 2
            y_loc = y_base + (filtered_gold[i] + j) * square_vertical_spacing - square_size_1 / 2
            ax.add_patch(Rectangle(
                (x_loc, y_loc),
                square_size_1,
                square_size_2,
                color='#E5E5E5',
                zorder=10
            ))

            sports_silver = filtered_sports_medal_silver[i][j]
            sports_logo = mpimg.imread('sports/'+sports_silver+'.png')
            if sports_silver == 'climbing':
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.026)
            elif sports_silver == 'badminton':
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.014)
            elif sports_silver == 'archery':
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.008)
            else:
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.015)
            ax.add_artist(AnnotationBbox(imagebox_sports_logo, (x_loc + square_size_1/2, y_loc + square_size_2/2), frameon=False, pad=0.1, xycoords='data', box_alignment=(0.5, 0.5), zorder=11))


        for j in range(filtered_bronze[i]):
            x_loc = filtered_years[i] - square_size_1 / 2
            y_loc = y_base + (filtered_gold[i] + filtered_silver[i] + j) * square_vertical_spacing - square_size_1 / 2
            ax.add_patch(Rectangle(
                (x_loc, y_loc),
                square_size_1,
                square_size_2,
                color='#DCB486',
                zorder=10
            ))
            sports_bronze = filtered_sports_medal_bronze[i][j]
            sports_logo = mpimg.imread('sports/'+sports_bronze+'.png')
            if sports_bronze == 'climbing':
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.026)
            elif sports_bronze == 'badminton':
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.014)
            else:
                imagebox_sports_logo = OffsetImage(sports_logo, zoom=0.015)
            ax.add_artist(AnnotationBbox(imagebox_sports_logo, (x_loc + square_size_1/2, y_loc + square_size_2/2), frameon=False, pad=0.1, xycoords='data', box_alignment=(0.5, 0.5), zorder=11))

    # First plot: Number of athletes over the years without y-axis
    ax.plot(filtered_years, filtered_rank, color='#D3322A', marker='o', linestyle='-', linewidth=1)
    # Define an offset value for text annotation
    text_offset = 2  # Adjust this value based on how high you want the text to be
    
    # Annotate the rank on the plot
    for i in range(len(filtered_years)):
        ax.text(filtered_years[i], 
                 filtered_rank[i] - text_offset,  # Apply the offset here
                 f'{filtered_rank[i]}', 
                 ha='center', 
                 va='bottom', 
                 fontweight='bold',
                 fontsize=10)  # You can adjust the font size if needed
        
    ax.invert_yaxis()
    ax.grid(False)
    ax.text(
        filtered_years[-1] + 2.5, filtered_rank[-1] - 3.5,
        f'With {filtered_gold[-1]:.0f} golds and {filtered_bronze[-1]:.0f} bronze, \nIndonesia achieved \na ranking of {filtered_rank[-1]:.0f}th',
        ha='left', va='center', color='black', fontsize=10,
        bbox=dict(facecolor='none', alpha=0.7, edgecolor='none')
    )
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Rank', fontweight='bold')
    ax.xaxis.set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='y', labelsize=9)  # Adjust the font size

def plot_athletes(ax, filtered_years, filtered_num_athletes, average_num_athletes):
    """Plot the number of athletes on the provided axis."""
    bars = ax.bar(filtered_years, filtered_num_athletes, width=2.5, color='#FFFFFF', edgecolor='#D4D4D4')
    for i in range(len(filtered_years)):
        if filtered_num_athletes[i] > average_num_athletes:
            bars[i].set_color('#D9D9D9')
        else:
            bars[i].set_color('#F5CDCB')
    bars[-1].set_color('#FE0000')

    ax.set_xlabel('Olympic Year', fontweight='bold')
    ax.set_ylabel('Number of Athletes', fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(filtered_years)
    ax.set_xticklabels(filtered_years)
    ax.text(
        filtered_years[-1] + 4, average_num_athletes,
        f'Average Number of\nIndonesian Athletes \nof all Years: {average_num_athletes:.0f}',
        ha='left', va='center', color='black', fontsize=10,
        bbox=dict(facecolor='none', alpha=0.7, edgecolor='none')
    )

    ax.text(
        filtered_years[-1] + 4, average_num_athletes + 20,
        f'In the {filtered_years[-1]:.0f} Olympics, \nIndonesia sent \n{filtered_num_athletes[-1]:.0f} athletes',
        ha='left', va='center', color='black', fontsize=10,
        bbox=dict(facecolor='none', alpha=0.7, edgecolor='none')
    )

    ax.text(
        filtered_years[0] - 7 , -15,
        f'Data Source: Wikipedia - Indonesia \nat the 2024 Summer Olympics',
        ha='left', va='center', color='#C1C1C1', fontsize=10,
        bbox=dict(facecolor='none', alpha=0.7, edgecolor='none')
    )

    ax.text(
        filtered_years[-1] , -15,
        f'© 2024 Lucas Elbert Suryana',
        ha='left', va='center', color='#C1C1C1', fontsize=10,
        bbox=dict(facecolor='none', alpha=0.7, edgecolor='none')
    )
    
    ax.axhline(y=average_num_athletes, color='grey', linestyle='--', linewidth=1)
    # Annotate the number of athletes on the plot
    for i in range(len(filtered_years)):
        ax.text(filtered_years[i], filtered_num_athletes[i], f'{filtered_num_athletes[i]}', ha='center', va='bottom', fontweight='bold', fontsize=10)

def plot_sports(ax, filtered_years, filtered_num_sports, average_num_sports):
    """Plot the number of athletes on the provided axis."""
    bars = ax.bar(filtered_years, filtered_num_sports, width=2.5, color='#FFFFFF', edgecolor='#D4D4D4')

    for i in range(len(filtered_years)):
        if filtered_num_sports[i] > average_num_sports:
            bars[i].set_color('#D9D9D9')
        else:
            bars[i].set_color('#F5CDCB')
    bars[-1].set_color('#FE0000')

    ax.set_xlabel('Olympic Year', fontweight='bold')
    ax.set_ylabel('Number of Sports', fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(filtered_years)
    ax.set_xticklabels(filtered_years)
    ax.text(
        filtered_years[-1] + 4, average_num_sports,
        f'Average Number of\nSports Indonesia Competes \nIn Each Olympic Year: {average_num_sports:.0f}',
        ha='left', va='center', color='black', fontsize=10,
        bbox=dict(facecolor='none', alpha=0.7, edgecolor='none')
    )

    ax.text(
        filtered_years[-1] + 4, average_num_sports + 8,
        f'In the {filtered_years[-1]:.0f} Olympics, \nIndonesia participated in \n{filtered_num_sports[-1]:.0f} sports',
        ha='left', va='center', color='black', fontsize=10,
        bbox=dict(facecolor='none', alpha=0.7, edgecolor='none')
    )

    ax.text(
        filtered_years[0] - 7 , -5,
        f'Data Source: Wikipedia - Indonesia \nat the 2024 Summer Olympics',
        ha='left', va='center', color='#C1C1C1', fontsize=10,
        bbox=dict(facecolor='none', alpha=0.7, edgecolor='none')
    )

    ax.text(
        filtered_years[-1] , -5,
        f'© 2024 Lucas Elbert Suryana',
        ha='left', va='center', color='#C1C1C1', fontsize=10,
        bbox=dict(facecolor='none', alpha=0.7, edgecolor='none')
    )
    
    ax.axhline(y=average_num_sports, color='grey', linestyle='--', linewidth=1)
    # Annotate the number of athletes on the plot
    for i in range(len(filtered_years)):
        ax.text(filtered_years[i], filtered_num_sports[i], f'{filtered_num_sports[i]}', ha='center', va='bottom', fontweight='bold', fontsize=10)

def add_images(ax, flag_img_path, logo_img_path, filtered_years, filtered_num_athletes):
    """Add images and annotations to the plot."""
    indonesia_flag = mpimg.imread(flag_img_path)
    olympic_logo = mpimg.imread(logo_img_path)

    imagebox_flag = OffsetImage(indonesia_flag, zoom=0.02)
    imagebox_logo = OffsetImage(olympic_logo, zoom=0.04)

    ax.add_artist(AnnotationBbox(imagebox_flag, (0.969, 1.69), frameon=True, pad=0.1, xycoords='axes fraction', box_alignment=(1, 1)))
    ax.add_artist(AnnotationBbox(imagebox_logo, (0.99, 1.5), frameon=False, pad=0, xycoords='axes fraction', box_alignment=(1, 1)))

    # Define the arrow positions
    arrow_start = (0.926, 0.9)  # Position near the Olympic logo in axes fraction
    arrow_end = (filtered_years[-1], filtered_num_athletes[-1] + 4)  # Position at the top of the last bar in data space

    ax.annotate(
        '', 
        xy=arrow_end, 
        xytext=arrow_start,
        xycoords='data', 
        textcoords='axes fraction',
        arrowprops=dict(facecolor='black', edgecolor='red', arrowstyle='->', lw=2),
        annotation_clip=False
    )

    ax.tick_params(axis='x', labelsize=9)  # Adjust the font size
    ax.tick_params(axis='y', labelsize=9)  # Adjust the font size

def add_title_and_lines(fig):
    """Add title, horizontal line, and rectangle to the figure."""
    fig.add_artist(
        plt.Line2D(
            [0, 1],
            [1.07, 1.07],
            color='red',
            linewidth=1,
            transform=fig.transFigure
        )
    )

    fig.patches.append(
        Rectangle(
            (0, 1.07),
            0.1,
            0.02,
            transform=fig.transFigure,
            color='#C91E21',
            zorder=1
        )
    )

    fig.suptitle(
        "Indonesia Wins 2 Golds at the Olympics 2024 \nSetting a New Record with Medals in Three Sports",
        fontsize=20,
        fontweight='bold',
        color='red',
        ha='left',
        va='top',
        y=1.05,
        x=0
    )

    fig.text(
        0, 0.95,
        'Indonesia at the Olympics: Performance and Sports Participation \nOver the Years',
        fontsize=12,
        fontweight='bold',
        color='black',
        ha='left',
        va='top'
    )
