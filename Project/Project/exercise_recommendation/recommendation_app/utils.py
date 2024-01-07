def get_user_info(request):
    user_info = {}
    user_info['age'] = int(request.POST.get('age'))
    user_info['weight'] = float(request.POST.get('weight'))
    user_info['height'] = float(request.POST.get('height'))
    allergies = request.POST.get('allergies').split(',')
    user_info['allergies'] = [allergy.strip() for allergy in allergies]
    user_info['is_vegetarian'] = request.POST.get('is_vegetarian') == 'y'
    return user_info