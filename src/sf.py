"""Strong Field Physics
"""
import math

def pondermotive_energy(I, wl):
    """Calculate the pondermotive energy of the laser field.

    Args:
        I (float): The intensity of the laser field (10^14 W/cm^2).
        wl (float): The wavelength of the laser field (um).

    Returns:
        float: The pondermotive energy of the field .
    """
    return 9.33 * I * wl** 2


def keldysh_parameter(i_p, u_p):
    """ i_p is the ionization potential and u_p is the pondermotive energy.
    Both i_p and u_p must be in the same unit.
    """
    return math.sqrt(i_p /(2 * u_p))


def over_the_barrier_intensity(i_p, z):
    """ i_p is the ionization potental and z in the charge of the ion (after ionization).
    i_p in ev

    return unit (W/cm^2)
    """
    return 4*10**9 * i_p**4 / z**2
