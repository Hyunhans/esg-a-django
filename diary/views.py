from django.contrib import messages
from django.shortcuts import render, redirect

from diary.forms import MemoryForm
from diary.models import Memory


def memory_list(request):
    memory_qs = Memory.objects.all()  #.order_by("-id")
    return render(request, "diary/memory_list.html", {
        "memory_list": memory_qs,
    })


def memory_detail(request, pk):
    memory = Memory.objects.get(pk=pk)
    return render(request, "diary/memory_detail.html", {
        "memory": memory,
    })


def memory_new(request):
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()

            # 덕타이핑 관련 / 타입을 써주는 코드 예사
            # memory : Memory = form.save()

            messages.success(request, "메모리를 생성했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm()  # 실제로 db에 저장한후



    return render(request, "diary/memory_form.html", {
        "form": form,
    })

def memory_edit(request, pk):
    memory = Memory.objects.get(pk=pk)

    if request.method == "POST":
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "메모리를 저장했습니다.")

            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm(instance=memory)

    return render(request, "diary/memory_form.html", {
        "form": form,
    })

def memory_delete(request, pk):
    memory = Memory.objects.get(pk=pk)

    #TODO: delete momory
    if request.method == 'POST':
        memory.delete()
        messages.success(request, "메모리를 삭제했습니다.")  # 유저에게 1회성으로 보여주는거야

        return redirect("/diary/")  # 삭제해줬으니 어디로 이동시켜야 할거 아니야

    return render(request, "diary/memory_confirm_delete.html", {
        "memory" : memory,
})