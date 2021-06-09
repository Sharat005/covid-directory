from screen.models import Screen
from userprofile.models import PatientInfo
from zipanalytics.models import ZipcodeStats
from django.db.models import Sum

# Method to compute Dashboard Summary Stats


def get_dashboard_stats():
    stats = {'users_count': 'NA', 'screening_count': 'NA',
             'tests_count': 'NA', 'positive_cases': 'NA'}
    # users_count =
    users_count = PatientInfo.objects.all().count()
    screening_count = Screen.objects.all().count()

    if(users_count != 0):
        stats['users_count'] = users_count
    if(screening_count != 0):
        stats['screening_count'] = screening_count

    total_tests = ZipcodeStats.objects.aggregate(Sum('tests'))
    if(total_tests != 0):
        stats['tests_count'] = total_tests['tests__sum']

    positive_cases = ZipcodeStats.objects.aggregate(Sum('cases'))
    if(positive_cases != 0):
        stats['positive_cases'] = positive_cases['cases__sum']
    return stats


def fetch_data_for_zip(form):
    zip = form.cleaned_data['zipcode']
    queryset = ZipcodeStats.objects.filter(zipcode=zip).order_by('-week')[:10]
    summary = {}
    summary['tests'] = ZipcodeStats.objects.filter(zipcode=zip).aggregate(Sum('tests'))['tests__sum']
    summary['cases'] = ZipcodeStats.objects.filter(zipcode=zip).aggregate(Sum('cases'))['cases__sum']
    summary['deaths'] = ZipcodeStats.objects.filter(zipcode=zip).aggregate(Sum('deaths'))['deaths__sum']

    data = []
    for each in queryset:
        data.append({'zipcode': each.zipcode, 'week': each.week,
                    'tests': each.tests, 'cases': each.cases, 'deaths': each.deaths})
    
    prev = []
    eq, up, down = '10608', '8593', '8595'
    for each in data[::-1]:
        icons = [eq, eq, eq]
        color = ["", "", ""]
        if(prev != []):
            if(each['tests'] > prev[0]):
                icons[0] = up
                color[0] = "green"
            else: 
                icons[0] = down
                color[0] = "red"
            if(each['cases'] > prev[1]):
                icons[1] = up
                color[1] = "green"
            else: 
                icons[1] = down
                color[1] = "red"
            if(each['deaths'] > prev[2]):
                icons[2] = up
                color[2] = "green"
            else: 
                icons[2] = down
                color[2] = "red"
        prev = [each['tests'], each['cases'], each['deaths']]
        each['icons'] = icons
        each['color'] = color
    return (data, summary)
