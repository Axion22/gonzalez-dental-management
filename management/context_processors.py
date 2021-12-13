from website.models import BookAppointment, VirtualConsult


def get_notification(request):
    count = BookAppointment.objects.filter(assign_doctor=None).count()
    countVC = VirtualConsult.objects.filter(assign_doctor=None).count()
       
    data = {
        "count":count,
        "countVC":countVC,

    }
    return data
