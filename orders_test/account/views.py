from django.shortcuts import render

from account.forms import ProfileForm, UserRegistrationForm


def register(request):
    template = 'account/register.html'
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()

            return render(request, 'orders/index.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, template, context)
