from django.db import models


class ThermalExpansionCalculator(models.Model):
    # inputs
    L0 = models.DecimalField(max_digits=10, decimal_places=6)
    S0 = models.DecimalField(max_digits=10, decimal_places=6)
    V0 = models.DecimalField(max_digits=10, decimal_places=6)
    alpha = models.DecimalField(max_digits=10, decimal_places=6)
    E = models.DecimalField(max_digits=10, decimal_places=6)
    delta_T = models.DecimalField(max_digits=10, decimal_places=6)

    # outputs
    delta_L = models.DecimalField(max_digits=10, decimal_places=6)
    delta_S = models.DecimalField(max_digits=10, decimal_places=6)
    delta_V = models.DecimalField(max_digits=10, decimal_places=6)
    sigma = models.DecimalField(max_digits=10, decimal_places=6)

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
