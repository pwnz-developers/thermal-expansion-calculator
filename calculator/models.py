from decimal import Decimal, ROUND_HALF_UP

from django.db import models


class ThermalExpansionCalculator(models.Model):
    # inputs
    L0 = models.DecimalField(max_digits=1000, decimal_places=15)
    S0 = models.DecimalField(max_digits=1000, decimal_places=15)
    V0 = models.DecimalField(max_digits=1000, decimal_places=15)
    alpha = models.DecimalField(max_digits=1000, decimal_places=15)
    E = models.DecimalField(max_digits=1000, decimal_places=15)
    delta_T = models.DecimalField(max_digits=1000, decimal_places=15)

    # outputs
    delta_L = models.DecimalField(max_digits=1000, decimal_places=15)
    delta_S = models.DecimalField(max_digits=1000, decimal_places=15)
    delta_V = models.DecimalField(max_digits=1000, decimal_places=15)
    sigma = models.DecimalField(max_digits=1000, decimal_places=15)

    def __str__(self):
        return f"{self.L0} {self.S0} {self.V0} {self.alpha} {self.E} {self.delta_T} => {self.delta_L} {self.delta_S} {self.delta_V} {self.sigma}"

    class Meta:
        verbose_name = "ThermalExpansionCalculator"
        verbose_name_plural = "ThermalExpansionCalculators"
        ordering = ["-id"]
        db_table = "calculator_thermal_expansion_calculator"

    def save(self, *args, **kwargs):
        if ThermalExpansionCalculator.objects.filter(
            L0=self.L0,
            S0=self.S0,
            V0=self.V0,
            alpha=self.alpha,
            E=self.E,
            delta_T=self.delta_T,
        ).exists():
            return
        super().save(*args, **kwargs)

    def make_2(self):
        """
        Returns a new object with all Decimal fields rounded to 2 decimal places.
        Example: 10.0000 -> 10.00
        """

        def r(x):
            return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        return {
            "pk": self.pk,
            "L0": r(self.L0),
            "S0": r(self.S0),
            "V0": r(self.V0),
            "alpha": r(self.alpha),
            "E": r(self.E),
            "delta_T": r(self.delta_T),
            "delta_L": r(self.delta_L),
            "delta_S": r(self.delta_S),
            "delta_V": r(self.delta_V),
            "sigma": r(self.sigma),
        }
