import sah
from aton.call import here

# Run in the current folder
here()

# Define the Spectra data and Plotting options
ins = sah.Spectra(
    type     = 'ins',
    files    = ['example_spx_2.02g.csv', 'example_spx_ND_1.284g.csv'],
    units_in = 'cm-1',
    units    = 'meV',
    plotting = sah.Plotting(
        title      = 'Example spectra',
        xlim       = [8, 1000],
        offset     = True,
        scaling    = 0.9,
        margins    = [0.2, 0.2],
        xlabel     = 'Energy / meV',
        ylabel     = 'S(Q,E)',
        legend     = ['example 1', 'example 2'],
        log_xscale = True
    ),
)

# To fit a plateau
plateau, plateau_error = sah.fit.plateau(spectra=ins, cuts=[33, 36])
print(f'Calculated plateau: {plateau} +- {plateau_error}\n')

# To fit the area under a peak
area, area_error = sah.fit.area_under_peak(spectra=ins, peak=[36, 39, plateau, plateau_error])
print(f'Calculated peak area: {area}, {area_error}\n')

# Calculate the total neutron bound scattering cross section of a material
material_H = sah.Material(elements = {'C': 1, 'N': 1, 'H': 6, 'Pb': 1, 'I': 3})
material_D = sah.Material(elements = {'C': 1, 'N': 1, 'H': 3, 'H2': 3, 'Pb': 1, 'I': 3})
material_H.set()
material_D.set()
print('Calculated total neutron bound scattering cross sections:')
print(f'Protonated: {material_H.cross_section}')
print(f'Deuterated: {material_D.cross_section}')

# Estimate the deuteration with the Impulse Approximation
material_H.grams = 2.02
material_D.grams = 1.284
sah.deuterium.impulse_approx(ins, material_H, material_D)

# Normalise the spectra to the same height inside a given range
ins = sah.normalize.height(spectra=ins, range=[5, 500])

# Plot the normalised spectra
sah.plot(ins)

