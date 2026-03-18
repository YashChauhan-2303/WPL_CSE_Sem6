from django.db.models import F
from django.shortcuts import redirect, render

from .forms import VoteForm
from .models import VoteCounter


def _get_counter() -> VoteCounter:
    counter, _ = VoteCounter.objects.get_or_create(pk=1)
    return counter


def vote_view(request):
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            selected = form.cleaned_data["choice"]
            VoteCounter.objects.get_or_create(pk=1)
            VoteCounter.objects.filter(pk=1).update(**{selected: F(selected) + 1})
            return redirect("result")
    else:
        form = VoteForm()

    return render(request, "voting/vote.html", {"form": form})


def result_view(request):
    counter = _get_counter()
    total = counter.total_votes()

    if total == 0:
        percentages = {"good": 0, "satisfactory": 0, "bad": 0}
    else:
        percentages = {
            "good": round(counter.good * 100 / total, 2),
            "satisfactory": round(counter.satisfactory * 100 / total, 2),
            "bad": round(counter.bad * 100 / total, 2),
        }

    context = {
        "good_percent": percentages["good"],
        "satisfactory_percent": percentages["satisfactory"],
        "bad_percent": percentages["bad"],
        "total_votes": total,
    }
    return render(request, "voting/result.html", context)
