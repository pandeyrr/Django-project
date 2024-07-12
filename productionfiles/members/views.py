
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

# Members page (All members )

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

# Member page view(individual member detail)

def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


# Main page view

def main(request):
   template = loader.get_template('main.html')
   return HttpResponse(template.render())

# Testing view

def testing(request):
   # mydata = Member.objects.all().values_list('firstname')
   # mydata = Member.objects.filter(firstname='Leanne', id=1).values()
   # mydata = Member.objects.filter(firstname='Leanne').values() | Member.objects.filter(firstname='Rav').values()
   # mydata = Member.objects.filter(firstname__startswith='L').values()
   # mydata = Member.objects.all().order_by('firstname').values()
   mydata = Member.objects.all().order_by('-firstname').values()
   # mydata = Member.objects.all().values()
   template = loader.get_template('template.html')
   context = {
      'mymembers': mydata,
   }
   return HttpResponse(template.render(context, request))
