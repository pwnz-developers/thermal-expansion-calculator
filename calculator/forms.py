from django import forms


class ThermalForm(forms.Form):
    L0 = forms.DecimalField(
        label="Начальная длина L₀ (мм)", min_value=0, decimal_places=6
    )
    S0 = forms.DecimalField(
        label="Начальная площадь S₀ (мм²)", min_value=0, decimal_places=6
    )
    V0 = forms.DecimalField(
        label="Начальный объём V₀ (см³)", min_value=0, decimal_places=6
    )
    alpha = forms.DecimalField(
        label="Коэффициент линейного расширения α (1/°C)", decimal_places=12
    )
    E = forms.DecimalField(label="Модуль упругости E (МПа)", decimal_places=6)
    delta_T = forms.DecimalField(
        label="Изменение температуры ΔT (°C)", decimal_places=6
    )
