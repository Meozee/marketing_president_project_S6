from django.shortcuts import render
import pandas as pd

def home(request):
    context = {}

    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        try:
            df = pd.read_csv(csv_file)
            context['columns'] = df.columns
            context['rows'] = df.head(10).to_dict(orient='records')
            context['success'] = "File berhasil dibaca!"
        except Exception as e:
            context['error'] = f"Gagal membaca CSV: {e}"

    return render(request, 'home.html', context)
