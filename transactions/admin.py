from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render
from django import forms


from .models import Transaction

from utils.cnab_parser import CnabParser

import ipdb


class CNABImportForm(forms.Form):
    cnba_upload = forms.FileField()


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("shop_name", "type", "value")

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("cnab_upload/", self.cnab_upload),
        ]
        return new_urls + urls

    def cnab_upload(self, request):
        if request.method == "POST":

            try:
                CNAB_file = request.FILES["cnba_upload"]
                file_data = CNAB_file.read().decode("utf-8")
                cnab_normalized = CnabParser.normalize_str_cnab(file_data)
                CnabParser.add_to_db(cnab_normalized)
                messages.success(request, "File uploaded successfully")

            except UnicodeDecodeError:
                messages.error(
                    request,
                    "File can't be read. (not able to decode using utf-8) It needs to be a .txt file",
                )
            except ValueError:
                messages.error(request, "File is in wrong format. Check cnab settings")

        form = CNABImportForm()
        data = {"form": form}
        return render(request, "admin/cnab_upload.html", data)


admin.site.register(Transaction, TransactionAdmin)
