X = done
- = still to do

Things to address in simulation:

- compare with background selection to neutral
- variation in recombination rate

Things to describe in simulation results:

- what weighting fixes
- what trace normalization fixes 
    (mutation density - choose windows with different numbers of snps)

Simulations:

All on a 10x10 grid (square to induce PC switching),
subpopulation size N of 1000, for 32K generations.
Chromosome length 1 morgan, 4e7 bp, neutral mutation rate 1e-7 (to get diversity like 0.01).

Output SNPs, for 1,000 individuals.

Scenarios:

X Neutral, flat recombination.
X Neutral, with recombination rate increasing linearly from 0 to 2.
X Neutral, with recombination hot spots.
X Flat recombination, with selection against mutants with s=.01 at 1,000 sites
    distributed with decreasing density linearly along the chromosome.


To do on the data:

- Re-run with k=5, and add plots to supplement
- Include plots for different size windows
- Add Figure 2 equivalent to supplement for Drosophila, window length=10,000.
- Add Figure 6 equivalent to supplement for Medicago, window length=10,000. (maybe switch?)
- Include plots for Medicago with window size in bp
- Include a plot about missing data 
    (maybe density of missing sites or correlation of missingness with genome-wide PC1?)


Other points to discuss:

- quantify percent variation explained: ratio of eigenvalues, same as in PCA (cite Cox & Cox)
- relate to PCAdmix, explain difference in introduction
- show different window choice results we reference
- clarify we checked for variation in missingness, provide plot of MDS against missingness
- could neutrality + admixture explain drosophila and medicago? reference recent Neanderthal papers.
- make simple description of "weighted PCA" and decide what to do about it 
- clarify that block jackknife is approximately OK even though adjacent blocks are correlated
- clarify why didn't use recomb rates in medicago
- say something about the need to check for patterns in missingness
- PC switching

    * PC1/2 switching: make more clear in the paper that we take care of this with the math
    * PC2/3 switching: re-run with more PCs to check things don't change

- Reviewer suggests comparing Drosophila MDS also to diversity, etcetera;
    looking at Langley et al it looks like expected heterozygosity is pretty well correlated too;
    we think we want to maybe say something about this but not include this in the figure
    (which will make it too busy)

