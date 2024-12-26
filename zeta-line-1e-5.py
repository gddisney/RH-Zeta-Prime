import sympy
import math

def calculate_resonance(prime_list, zeta_zeros, tolerance=1e-3):
    """
    Calculate the tangent and cosine of each prime in prime_list,
    then measure the distance from the critical line (1/2) and target zeta zeros.
    Only collect primes whose tangent is close to the imaginary parts of zeta zeros.
    """
    results = []
    for prime in prime_list:
        cosine = math.cos(prime)
        try:
            tangent = math.tan(prime)
        except:
            continue  # Undefined tangent, skip
        
        for zero in zeta_zeros:
            tangent_diff = abs(tangent - zero)
            if tangent_diff <= tolerance:  # Check if tangent is close to the zeta zero
                results.append({
                    "prime": prime,
                    "tangent": tangent,
                    "cosine": cosine,
                    "target_zero": zero,
                    "tangent_difference": tangent_diff
                })
    return results

def generate_primes(count, start):
    """
    Generate a list of primes starting from a specific value.
    """
    primes = []
    current = start
    while len(primes) < count:
        if sympy.isprime(current):
            primes.append(current)
        current = sympy.nextprime(current)
    return primes

# Settings
zeta_zeros = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719, 43.3270732, 48.0051508, 49.7738324, 52.9703214, 56.44624769, 59.347044002, 60.83177852, 65.1125440, 67.07981052, 69.5464017, 72.067157, 75.7046906, 77.14484006]  
prime_start = 3  # Starting point for prime generation
prime_count = 100000000  # Number of primes to generate in each iteration
tolerance = 1e-5  # Tolerance for resonance matching

# Generate primes
primes = generate_primes(prime_count, prime_start)

# Calculate resonance
resonances = calculate_resonance(primes, zeta_zeros, tolerance)

# Print results
print("\nPrimes Closest to Zeta Zeros:")
if resonances:
    for r in resonances:
        print(
            f"Prime: {r['prime']}, Tangent: {r['tangent']:.6f}, Cosine: {r['cosine']:.6f}, "
            f"Target Zero: {r['target_zero']}, Tangent Difference: {r['tangent_difference']:.6f}"
        )
else:
    print("No primes found with resonance close to zeta zeros.")

