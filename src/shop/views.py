from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from django.shortcuts import render
from forms import MessageForm

from . import models


class ShowShop(LoginRequiredMixin, generic.TemplateView):
    template_name = "shop/shop_show.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        print 111
        return super(ShowShop, self).get(request, *args, **kwargs)


class EditShop(LoginRequiredMixin, generic.TemplateView):
    
    template_name = "shop/shop_edit.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        print 22
        user = self.request.user
        return super(EditShop, self).get(request,
                                         form=MessageForm())

    def post(self, request, *args, **kwargs):
        print 33
        # user = self.request.user
        # user_form = forms.UserForm(request.POST, instance=user)
        # profile_form = forms.ProfileForm(request.POST,
        #                                  request.FILES,
        #                                  instance=user.profile)
        # if not (user_form.is_valid() and profile_form.is_valid()):
        #     messages.error(request, "There was a problem with the form. "
        #                    "Please check the details.")
        #     user_form = forms.UserForm(instance=user)
        #     profile_form = forms.ProfileForm(instance=user.profile)
        #     return super(EditShop, self).get(request,
        #                                         user_form=user_form,
        #                                         profile_form=profile_form)
        # Both forms are fine. Time to save!
        # user_form.save()
        # profile = profile_form.save(commit=False)
        # profile.user = user
        # profile.save()
        # messages.success(request, " details saved!")
        return redirect("shop:show_self")

        # return redirect("profiles:show_self")