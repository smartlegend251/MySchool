from django.shortcuts import *
from Accounts.models import *
from django.contrib.auth.decorators import login_required

from MySchool import settings

@login_required(login_url=settings.LOGIN_URL_BRANCH)
def branch_dashboard(request):
    user = request.user
    print('the output is : ', user)

    try:
        branch = BranchAdmin.objects.get(user=user)
        print('the output is : ', branch)
        image = branch.image
        print('the output is : ', image)
    except BranchAdmin.DoesNotExist:
        # Handle the case where the BranchAdmin instance doesn't exist for the user
        image = None

    return render(request, 'branch/dashboard.html', {'image': image})
