import matplotlib.pyplot as plt

def plot_chromosome_lengths(genome):
    # Print chromosome lengths
    print("Real Human Chromosomes\n")

    for chromosome in genome:
        print(chromosome, ":", len(genome[chromosome]))

    sizes = []
    for chromosome in genome:
        length = len(genome[chromosome])
        sizes.append(length)

    # Bar Chart
    plt.figure(figsize=(10, 5))
    plt.bar(genome.keys(), sizes)
    plt.xticks(rotation=90)
    plt.title("Chromosome Lengths")
    plt.xlabel("Chromosomes")
    plt.ylabel("Length")
    plt.tight_layout()
    plt.show()

    # Pie Chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes,
        labels=genome.keys(),
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Genome Percentage by Chromosome")
    plt.show()