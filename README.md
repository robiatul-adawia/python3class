# Designing Triangulene Chains

### Introduction
What is Triangulene?
What for?
Why do we need to design? give picture as an example
To study the electronic and magnetic properties
### Method
rotation equation

- Structure class: create triangulene fragments, provide functions like 6-sites or benzene, 13-sites, 22-sites, etc. and what's the distance between nearest site, for now there are two option: distance = 1 and 1.42 for Carbon.
- In structure class we also have active function, such as to create benzene, add, rotate, function to decide which coordinate our fragments will be connected, etc
- last part of this class is group of functions to extract the positions, only consist of coordinates or with atom name such as Carbon thus we can add such as hydrogen using other software such as avogadro. In the beginning of installation the program will produce empty folder: structures, graphics, eigenvalues

-Analysis class: from here we start doing calculation, for TB, mean-field approximation, Hubbards. Visualizations function such as charge density and spin density. calculate expectation energy. asdd function to upload files that we already create. output: charge densities, spin densities, expectation energies

-visualizations: create graphics, is it necessary? 

### How to install

### How to run
Prepare the design of triangulene you will make, create the sructure using functions in structure class and extract files. Next upload files back, create hamiltonian for tight binding, define your t values. let's say you are doing mean field approx, then go to mean-field function to create the hamiltonian, define U values for Hubard nearest neighbor cases. create graphics

