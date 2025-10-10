from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import ThermalForm
from .calculator import ThermalExpansionCalculator


@csrf_exempt
def calculator_view(request):
    form = ThermalForm(request.POST or None)
    results = None

    if request.method == "POST" and form.is_valid():
        L0 = form.cleaned_data["L0"]
        S0 = form.cleaned_data["S0"]
        V0 = form.cleaned_data["V0"]
        alpha = form.cleaned_data["alpha"]
        E = form.cleaned_data["E"]
        delta_T = form.cleaned_data["delta_T"]

        calc = ThermalExpansionCalculator(
            L0=L0, S0=S0, V0=V0, alpha=alpha, E=E, delta_T=delta_T
        )

        results = calc.results(rounding_places=6)

    return render(
        request, "calculator/calculator.html", {"form": form, "results": results}
    )
