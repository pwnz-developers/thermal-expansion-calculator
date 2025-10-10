from decimal import Decimal, getcontext

getcontext().prec = 28


class ThermalExpansionCalculator:
    """
    High-precision Thermal Expansion Calculator using Decimal.
    Inputs:
      - L0: mm (Decimal)
      - S0: mm^2 (Decimal)
      - V0: cm^3 (Decimal)
      - alpha: 1/°C (Decimal)
      - E: MPa (Decimal)
      - delta_T: °C (Decimal)
    Outputs returned with Decimal precision.
    """

    def __init__(self, L0, S0, V0, alpha, E, delta_T):
        self.L0 = Decimal(L0)
        self.S0 = Decimal(S0)
        self.V0 = Decimal(V0)
        self.alpha = Decimal(alpha)
        self.E = Decimal(E)
        self.delta_T = Decimal(delta_T)

    def delta_L(self) -> Decimal:
        # ΔL = α * L0 * ΔT -> mm
        return (self.alpha * self.L0 * self.delta_T).normalize()

    def delta_S(self) -> Decimal:
        # ΔS = 2 * α * S0 * ΔT -> mm^2
        return (Decimal(2) * self.alpha * self.S0 * self.delta_T).normalize()

    def delta_V(self) -> Decimal:
        # ΔV = 3 * α * V0 * ΔT -> cm^3
        return (Decimal(3) * self.alpha * self.V0 * self.delta_T).normalize()

    def sigma(self) -> Decimal:
        # σ = E * α * ΔT -> MPa
        return (self.E * self.alpha * self.delta_T).normalize()

    def results(self, rounding_places: int = 6) -> dict:
        """
        Return results as dict with rounded strings.
        rounding_places: number of decimal places in output (default 6)
        """
        q = Decimal(10) ** (-rounding_places)
        return {
            "delta_L": str(self.delta_L().quantize(q)),
            "delta_S": str(self.delta_S().quantize(q)),
            "delta_V": str(self.delta_V().quantize(q)),
            "sigma": str(self.sigma().quantize(q)),
        }
