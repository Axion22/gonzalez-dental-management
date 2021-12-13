from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
  def wrapper_func(request, *args, **kwargs):
    
    if request.user.is_authenticated:
      return redirect('dashboardAdmin')
    else:
      return view_func(request, *args, **kwargs)

  
    
  return wrapper_func 


def allowed_users(allowed_roles=[]):
  def decorator(view_func):
    def wrapper_func(request, *args, **kwargs):

      group = None
      if request.user.groups.exists():
        group=request.user.groups.all()[0].name

      if group in allowed_roles:
        return view_func(request, *args, **kwargs)
      else:
        return HttpResponse('<center style="position:fixed;top: 50%; left: 50%;margin-top: -100px;margin-left: -250px;"><h1>You are Not authorized to view this page</h1><p style="color:red;">Back from Privious Page</p></center>')

    return wrapper_func
  return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
      group = None
      if request.user.groups.exists():
        group=request.user.groups.all()[0].name

      if group == 'doctor':
        return redirect ('dashboardDoctor')

      if group == 'staff':
        return redirect ('dashboardStaff')

      if group == 'admin':
        return view_func(request, *args, **kwargs)
      else:
        return view_func(request, *args, **kwargs)

    return wrapper_func

