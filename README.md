# Low Dimensional Spin Mapping (Lowdspin)

### Introduction
Lowdspin is a Python package for generating structural datasets of low-dimensional quantum simulator, including triangulene and related hexagon lattices. It maps charge and spin density distributions to investigate underlying electronic and magnetic properties. This tool is designed to automate and simplify the construction of diverse triangulene architectures, ranging from simple monomers to dimers and chain structures.

Key Outputs:
- Structure files: Ready-to-use geometry coordinates in .xyz and .dat formats.
- Electronic data: Calculated energy eigenvalues.
- Visualizations: Spatial maps of charge and spin density distributions.

![Triangulenes illustration](triangulene_chain.png)

### Methods
Hamiltonian:
$$\hat H = \hat H_{TB} + \hat H_U$$
<br>
Tight-Binding:
$$\hat H_{TB} = \Sigma_{ij,\sigma} t_{ij}\hat c_{i\sigma}^\dagger \hat c_{j \sigma}$$
<br>
Mean-field interaction on-site Hubbard U:
$$\hat H_U = U \Sigma_i \hat n_{i\uparrow}\hat n_{i\downarrow}$$
<br> Spin density: $$\frac{N_{\uparrow}-N_{\downarrow}}{2}$$
<br> <br>
Here's a reference to know more about triangulene chains:<br>
Experimental result of [Nanographene chains](https://www.nature.com/articles/s41586-021-03842-3)

### Draft
- The structure class will produce 2 types of datasets: (1) only consist of coordinates (x, y, z), and (2) coordinate with atom symbol, for now only Carbon (C, x, y, z). We can add such as hydrogen using other software like Avogadro
- Under consideration plan: In the beginning of installation the program will produce empty folder: structures, graphics, eigenvalues.

### How to install

### Example on how to run
- Prepare the design of triangulene you will make
- Open python create the sructure using structure class in the package, you will get coordinate files. 
- Next upload the coordinate files to your python code , create hamiltonian for tight binding, define your hopping t values. Output: Hamiltonian matrix, eigen values and eigen vectors
- go to mean-field function to update the hamiltonian from tight-binding, define U values for Hubard nearest neighbor cases. 
- you will get charge and densities array, create graphics using that by mapping the densities into your structure.

