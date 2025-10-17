from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP

getcontext().prec = 100


class ThermalExpansionCalculator:
    def __init__(self, L0, S0, V0, alpha, E, delta_T):
        self.L0 = Decimal(str(L0))
        self.S0 = Decimal(str(S0))
        self.V0 = Decimal(str(V0))
        self.alpha = Decimal(str(alpha))
        self.E = Decimal(str(E))
        self.delta_T = Decimal(str(delta_T))

    def delta_L(self) -> Decimal:
        return (self.alpha * self.L0 * self.delta_T).normalize()

    def delta_S(self) -> Decimal:
        return Decimal(2) * self.alpha * self.S0 * self.delta_T

    def delta_V(self) -> Decimal:
        return Decimal(3) * self.alpha * self.V0 * self.delta_T

    def sigma(self) -> Decimal:
        return self.E * self.alpha * self.delta_T

    def results(self, rounding_places: int = 6) -> dict:
        q = Decimal(10) ** (-rounding_places)
        try:
            return {
                "delta_L": str(self.delta_L().quantize(q, rounding=ROUND_HALF_UP)),
                "delta_S": str(self.delta_S().quantize(q, rounding=ROUND_HALF_UP)),
                "delta_V": str(self.delta_V().quantize(q, rounding=ROUND_HALF_UP)),
                "sigma": str(self.sigma().quantize(q, rounding=ROUND_HALF_UP)),
            }
        except InvalidOperation as e:
            # good idea to log this if needed
            print("❌ Invalid Decimal Operation:", e)
            raise
