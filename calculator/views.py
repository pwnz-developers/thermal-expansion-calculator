from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from .forms import ThermalForm
from .calculator import ThermalExpansionCalculator
from .models import ThermalExpansionCalculator as T_Model


@ensure_csrf_cookie
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

        t_model = T_Model(
            L0=L0,
            S0=S0,
            V0=V0,
            alpha=alpha,
            E=E,
            delta_T=delta_T,
            delta_L=results["delta_L"],
            delta_S=results["delta_S"],
            delta_V=results["delta_V"],
            sigma=results["sigma"],
        )
        t_model.save()
    m = T_Model.objects.all()
    contents = [i.make_2() for i in m]
    return render(
        request,
        "calculator/calculator.html",
        {"form": form, "results": results, "contents": contents},
    )


@ensure_csrf_cookie
def calculator_detail_view(request, pk):
    calc = get_object_or_404(T_Model, pk=pk)
    return render(request, "calculator/detail.html", {"calc": calc})
