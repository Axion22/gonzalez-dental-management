from website.models import BookAppointment, VirtualConsult


def get_notification(request):
    count = BookAppointment.objects.filter(assign_doctor=None).count()
    countVC = VirtualConsult.objects.filter(assign_doctor=None).count()
    #user = request.user
    #countVCDoctor = None
    #if user.is_authenticated:
    #    countVCDoctor = VirtualConsult.objects.filter(assign_doctor=request.user.account, accepted=False).count()
       
    data = {
        "count":count,
        "countVC":countVC,
    #    "countVCDoctor":countVCDoctor
    }
    return data
