from website.models import BookAppointment, VirtualConsult


def get_notification(request):
    count = BookAppointment.objects.filter(assign_doctor=None).count()
    countVC = VirtualConsult.objects.filter(assign_doctor=None).count()
    user = request.user
    countVCDoctor = None
    countAppoint = None
    if user.groups.filter(name='doctor'):
        countVCDoctor = VirtualConsult.objects.filter(assign_doctor=request.user.account, accepted=False).count()
        countAppoint = BookAppointment.objects.filter(assign_doctor=request.user.account, done=False).count()
       
    data = {
        "count":count,
        "countVC":countVC,
        "countVCDoctor":countVCDoctor,
        "countAppoint":countAppoint
    }
    return data
