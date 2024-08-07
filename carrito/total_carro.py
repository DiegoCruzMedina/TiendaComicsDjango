def total(request):
    total = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:
            for key, value in request.session["carro"].items():
                total += float(value["precio"])  
    return {
        "total": total
    }
