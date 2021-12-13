from management.models import Treatment

#Treatment
t = Treatment.objects.all()
ft = Treatment.objects.first()
fl = Treatment.objects.last()
tn = Treatment.objects.get(name=' ')
tid = Treatment.objects.get(id=' ')

#_set
treatment_set.all()

#parent model
t = Treatment.objects.first()
parent = treatment.customer.name

#filter
treatment = Treatment.objects.filter(name="")

#sort
least = Treatment.objects.all().order_by('name')
greater = Treatment.objects.all().order_by('-name')

#tag search
filter = Treatment.objects.filter(treatment__name="")


