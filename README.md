# Quant Puzzles

Python experiments for probability puzzles.

## Mutual nearest neighbors

This puzzle came from a T-shirt I picked up at a Jane Street campus info session. If ducks are scattered uniformly across a large pond, what is the probability that a duck and its closest neighbor are each other's closest neighbors?

I started by working out which regions of the pond had to be empty, then used a Monte Carlo simulation to estimate the probability across many random layouts.

### Run the simulation

The script uses only Python's standard library. From the repository root, run

```bash
python3 Adjacent-Duck.py
```

Each trial places duck A at the center of a unit square and scatters 1,000 other ducks uniformly at random. The script finds A's nearest neighbor, B, then checks whether A is B's nearest neighbor. Placing A at the center reduces the influence of the pond edges. The script uses a fixed seed of 40 so the run is reproducible.

```text
Mutual nearest neighbors in 62,149 out of 100,000 trials.
Estimated probability: 62.15%
```

The theoretical probability for independent, uniformly placed ducks in the large-pond limit is `6π / (8π + 3√3)`, or about 62.15%. [On Nearest-Neighbor Graphs, Lemma 1](https://ics.uci.edu/~eppstein/pubs/EppPatYao-DCG-97.pdf#page=6)
