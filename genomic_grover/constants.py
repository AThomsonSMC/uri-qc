import random

# util to convert random ints to sequences
def _to_nuc(i):
    try:
        return ['A','C','G','T'][i]
    except IndexError:
        raise Exception('Invalid nucleotide index')

# Generates a random genomic sequence of an input length
def generate_random_sequence(l):
    return ''.join([_to_nuc(random.randint(0,3)) for _ in range(l)])

REFERENCE_GENOMES = {
    'test0': "GCAT",
    'test1': "GATTACA",
    'test2': "GCCCACGACTTAGCTA",
    'test32': generate_random_sequence(2**5),
    'test64': generate_random_sequence(2**6),
    'test256': generate_random_sequence(2**8),
    # Approximately the size of a small viral genome
    'test1K': generate_random_sequence(2**10),
    # Be careful past here
    # Approximately the size of a bacterial genome
    'test1M': generate_random_sequence(2**20),
    # Approximately the minimum size of a mammalian genome
    'test2B': generate_random_sequence(2**31)
}