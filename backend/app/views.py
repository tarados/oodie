from django.shortcuts import render
from .form import ImageForm
from .models import ProductImage


# def home_view(request):
# 	context = {}
# 	if request.method == "POST":
# 		form = ImageForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			name = form.cleaned_data.get("name")
# 			img = form.cleaned_data.get("image_field")
# 			print(name, img)
# 			# obj = ProductImage(
# 			# 	product=name,
# 			# 	image=img
# 			# )
# 			# obj.save()
# 			# print(obj)
# 		else:
# 			form = ImageForm()
# 	context['form'] = form
# 	return render(request, "home.html", context)
