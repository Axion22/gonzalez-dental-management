from website.models import BookAppointment, VirtualConsult


def get_notification(request):
    countVC = VirtualConsult.objects.filter(assign_doctor=None).count()
       
    data = {
        "countVC":countVC,

    }
    return data
