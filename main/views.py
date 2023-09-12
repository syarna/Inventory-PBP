from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Syarna Savitri',
        'class': 'PBP B',

        'barang': 'Palu Thor',
        'amount': '1',
        'description': 'Limited edition dari Asgard',
        'price':'1.000.000 Krona',
    }

    return render(request, "main.html", context)
