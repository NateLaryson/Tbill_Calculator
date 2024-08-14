from django.shortcuts import render
import pandas as pd
from .modules import util

def index(request):
    if request.method == 'POST':
        startdate = pd.to_datetime(request.POST.get('startdate'))
        
        tenor = request.POST.get('tenor')
        terms = request.POST.get('terms')
        principal = float(request.POST.get('principal'))
        rate = float(request.POST.get('rate'))
        est_years = request.POST.get('est_years')
        currency = request.POST.get('currency')
        
        if est_years == '':
            est_years = 0
            msg_years = 'First Term'
        else:
            est_years = int(est_years)
            msg_years = f'{est_years} Year(s) estimation'
        
        if tenor == '91days':
            result = util.t91days(principal, rate, terms, est_years)
            interest = result - principal
            if est_years == 0:
                enddate = pd.to_datetime(startdate) + pd.DateOffset(days=91)
            else:
                enddate = pd.to_datetime(startdate) + pd.DateOffset(days=(91 * 4) * est_years)
                
        elif tenor == '182days':
            result = util.t182days(principal, rate, terms, est_years)
            interest = result - principal
            if est_years == 0:
                enddate = pd.to_datetime(startdate) + pd.DateOffset(days=182)
            else:
                enddate = pd.to_datetime(startdate) + pd.DateOffset(days=(182 * 2) * est_years)
        else:
            result = util.t365days(principal, rate, terms, est_years)
            interest = result - principal
            if est_years == 0:
                enddate = pd.to_datetime(startdate) + pd.DateOffset(days=365)
            else:
                enddate = pd.to_datetime(startdate) + pd.DateOffset(days=(365) * est_years)
        
        if terms == 'PO':
            terms = 'Roll Over Principal Only'
        else:
            terms = "Roll Over Principal + Interest"
            
        return render(request, 'tbillapp/index.html', {
            'yield': f'{currency} {result:,.2f}',
            'interest': f'{currency} {interest:,.2f}',
            'principal': f'{currency} {principal:,.2f}',
            'enddate': enddate,
            'startdate': startdate,
            'tenor': f'{tenor} Tenor',
            'terms': terms,
            'years': msg_years
        })
        
    return render(request, 'tbillapp/index.html', {
        'yield': 'USD 0.0',
        'interest': 'USD 0.0',
        'principal': 'USD 0.0',
        'enddate': 'MM/DD/YYYY',
        'startdate': 'MM/DD/YYYY'
    })    
        
        
    
    