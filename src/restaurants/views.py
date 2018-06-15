from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

# Create your views here.
@login_required()
def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():
			instance = form.save(commit=False)
			# customize
			# like pre save
			instance.owner = request.user
			form.save()
			# like post save
			# obj = RestaurantLocation.objects.create(
			# 		name = form.cleaned_data.get('name'),
			# 		location = form.cleaned_data.get('location'),
			# 		category = form.cleaned_data.get('category')
			# 	)
			return HttpResponseRedirect("/restaurants/")
		else:
			return HttpResponseRedirect("/login/")
	if form.errors:
		errors = form.errors

	template_name = 'restaurants/form.html'
	context = {"form": form, "errors": errors}
	return render(request, template_name, context)

def restaurant_listview(request):
	template_name= 'restaurants/restaurant_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {"object_list": queryset}
	return render(request, template_name, context)

class RestaurantListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)
		# slug = self.kwargs.get("slug")
		# if slug:
		# 	queryset = RestaurantLocation.objects.filter(
		# 			Q(category__iexact=slug) |
		# 			Q(category__icontains=slug)
		# 		)
		# else:
		# 	queryset = RestaurantLocation.objects.all()
		# return queryset

class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

	# def get_context_data(self, *args, **kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation, id=rest_id)
	# 	return obj
	
class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	# login_url = '/login/'
	template_name = 'form.html'
	# success_url = '/restaurants/'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestaurantCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Restaurant'
		return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	# login_url = '/login/'
	template_name = 'restaurants/detail-update.html'
	# success_url = '/restaurants/'

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().name
		context['title'] = f'Update Restaurant: {name}'
		return context

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)
