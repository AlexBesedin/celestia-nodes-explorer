import requests
from django.shortcuts import render

def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def nodes(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        url = f'https://leaderboard.celestia.tools/api/v1/nodes/{address}'
        try:
            data = fetch_data(url)
            return render(request, 'nodes.html', {'data': data})
        except Exception:
            return render(request, 'error.html')
    else:
        return render(request, 'nodes.html')


def validators(request):
    if request.method == 'POST':
        identity = request.POST.get('identity')
        url = f'https://leaderboard.celestia.tools/api/v1/validators/{identity}'
        data = fetch_data(url)
        return render(request, 'validator.html', {'data': data})
    else:
        return render(request, 'validator.html')


def home(request):
    return render(request, 'main.html')
