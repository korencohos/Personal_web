from .models import Profile

def profile_info(request):
    profile = Profile.objects.first()
    return {'profile_info': profile}
