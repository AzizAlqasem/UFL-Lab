"""Strong Field Physics
"""

def pondermotive_energy(I, wl):
    """Calculate the pondermotive energy of the laser field.

    Args:
        I (float): The intensity of the laser field (10^14 W/cm^2).
        wl (float): The wavelength of the laser field (um).

    Returns:
        float: The pondermotive energy of the field .
    """
    return 9.33 * I * wl** 2