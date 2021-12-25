from django.contrib import admin
from .models import *
from django.contrib.admin import DateFieldListFilter
from .utils import ExportCsvMixin, ExportAllCsvMixin, BulkSaveMixin
from import_export import resources
from src.models import AxisCompleteDetail, CompleteDetail
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.instance_loaders import CachedInstanceLoader
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'aadhar', 'date_of_birth']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'aadhar', 'date_of_birth')}),
    )
    fieldsets = UserAdmin.fieldsets


class AxisCompleteDetailResource(resources.ModelResource):
    state = Field(attribute='state', column_name='STATE')
    final_city = Field(attribute='final_city', column_name='FINAL_CITY')
    account_ref = Field(attribute='account_ref', column_name='ACCOUNT_REF')
    full_name = Field(attribute='full_name', column_name='FULL_NAME')
    registration = Field(attribute='registration', column_name='REGISTRATION')
    manufacturer = Field(attribute='manufacturer', column_name='MANUFACTURER')
    chasis_number = Field(attribute='chasis_number', column_name='CHASSIS_NUMBER')
    pos = Field(attribute='pos', column_name='POS in Cr')
    bucket = Field(attribute='bucket', column_name='BUCKET')
    address = Field(attribute='address', column_name='ADDRESS')
    mobile_numer = Field(attribute='mobile_numer', column_name='MOBILE NUMBER')
    emi_amount = Field(attribute='emi_amount', column_name='EMI_AMOUNT')
    final_emi_amount = Field(attribute='final_emi_amount', column_name='Final EMI_AMT')
    emi_charges = Field(attribute='emi_charges', column_name='EMI + Charges')
    total_overdue = Field(attribute='total_overdue', column_name='TOTAL_OVERDUE')
    total_od_charges = Field(attribute='total_od_charges', column_name='TOTAL OD+ charges')
    engine_number = Field(attribute='engine_number', column_name='ENGINE_NUMBER')
    cm_name = Field(attribute='cm_name', column_name='CM Name')
    acm_name = Field(attribute='acm_name', column_name='ACM Name')

    class Meta:
        model = AxisCompleteDetail
        # fields = ('id', 'name', 'price',)  # to whitelist export fields


class AxisCompleteDetailAdmin(ImportExportModelAdmin):
    resource_class = AxisCompleteDetailResource
    show_full_result_count = False
    change_form_template = 'src/templates/admin/change_form.html'
    search_fields = ('chasis_number', 'registration', 'full_name', 'engine_number')
    list_display = ('chasis_number', 'state', 'full_name', 'manufacturer', 'address', 'mobile_numer', 'registration',
                    'engine_number', 'acm_name'
                    )
    list_per_page = 50
    readonly_fields = ('state', )
    list_max_show_all = False
    actions = (ExportCsvMixin.export_as_csv, ExportAllCsvMixin.export_all_as_csv, )

    def get_search_fields(self, request):
        if request.user.is_superuser:
            self.search_fields = ('chasis_number', 'state', 'full_name', 'manufacturer', 'address', 'mobile_numer',
                                  'registration', 'engine_number', 'acm_name'
                                  )
        return self.search_fields

    # def get_search_results(self, request, queryset, search_term):
    #     search_result = super().get_search_results(request, queryset, search_term)
    #     if not request.user.is_superuser:
    #         if len(search_term) != 7:
    #             search_result = (ProcedureForm.objects.none(), False)
    #     return search_result

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = super().get_readonly_fields(request)
        if not obj:
            read_only_fields = ()
            if not request.user.is_superuser:
                print(type(request.method))
        if request.user.is_superuser:
            read_only_fields = ()
        return read_only_fields

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'export_as_csv' in actions:
                del actions['export_as_csv']
            if 'export_all_as_csv' in actions:
                del actions['export_all_as_csv']
        return actions

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'result' in form.base_fields:
            form.base_fields['result'].widget.attrs['placeholder'] = "Did the patient get the results, etc.."
        if 'remark' in form.base_fields:
            form.base_fields['remark'].widget.attrs['placeholder'] = "e.g.: Burnt/Pain was not satisfied.."
        return form

    def get_list_display(self, request):
        listDisplay = super().get_list_display(request)
        if not request.user.is_superuser:
            self.list_per_page = 10
        else:
            self.list_per_page = 50
        return listDisplay


class CompleteDetailResource(resources.ModelResource):
    hpa_no = Field(attribute='hpa_no', column_name='HPA_NO')
    name = Field(attribute='name', column_name='NAME')
    brndes = Field(attribute='brndes', column_name='BRNDES')
    rgndes = Field(attribute='rgndes', column_name='RGNDES')
    state = Field(attribute='state', column_name='STATE_DES')
    emp_name = Field(attribute='emp_name', column_name='EMP_NAME')
    outstand = Field(attribute='outstand', column_name='OUTSTAND')
    age = Field(attribute='age', column_name='AGE')
    bill1 = Field(attribute='bill1', column_name='BILL1')
    soh = Field(attribute='soh', column_name='SOH')
    assdes = Field(attribute='assdes', column_name='ASSDES')
    status = Field(attribute='status', column_name='STATUS')
    branch = Field(attribute='branch', column_name='BRANCH')
    regno = Field(attribute='regno', column_name='REGNO')
    engno = Field(attribute='engno', column_name='ENGNO')
    chsno = Field(attribute='chsno', column_name='CHSNO')
    place = Field(attribute='place', column_name='PLACE')
    postoffice = Field(attribute='postoffice', column_name='POSTOFFICE')
    road_name = Field(attribute='road_name', column_name='ROAD_NAME')
    landmark = Field(attribute='landmark', column_name='LANDMARK')
    city_village = Field(attribute='city_village', column_name='CITY_VILLAGE')
    state_code = Field(attribute='state_code', column_name='STATE_CODE')
    district_code = Field(attribute='district_code', column_name='DISTRICT_CODE')
    taluk = Field(attribute='taluk', column_name='TALUK')
    website = Field(attribute='website', column_name='WEBSITE')
    pincode = Field(attribute='pincode', column_name='PIN_CODE')
    office_phone_no = Field(attribute='office_phone_no', column_name='OFFICE_PHONE_NO')
    resi_telephone = Field(attribute='resi_telephone', column_name='RESI_TELEPHONE')
    mobile_no = Field(attribute='mobile_no', column_name='MOBILE_NO')
    pager_no = Field(attribute='pager_no', column_name='PAGER_NO')
    gu_name = Field(attribute='gu_name', column_name='gu_name')
    gu_place = Field(attribute='gu_place', column_name='gu_place')
    gu_postoffice = Field(attribute='gu_postoffice', column_name='gu_postoffice')
    gu_road_name = Field(attribute='gu_road_name', column_name='gu_road_name')
    gu_landmark = Field(attribute='gu_landmark', column_name='gu_landmark')
    gu_city_village = Field(attribute='gu_city_village', column_name='gu_city_village')
    gu_state_des = Field(attribute='gu_state_des', column_name='gu_state_des')
    gu_district_des = Field(attribute='gu_district_des', column_name='gu_district_des')
    gu_taluk = Field(attribute='gu_taluk', column_name='gu_taluk')
    gu_pincode = Field(attribute='gu_pincode', column_name='gu_pincode')
    gu_office_phone_no = Field(attribute='gu_office_phone_no', column_name='gu_office_phone_no')
    gu_resi_telephone = Field(attribute='gu_resi_telephone', column_name='gu_resi_telephone')
    gu_mobile_no = Field(attribute='gu_mobile_no', column_name='gu_mobile_no')
    cust_fatherName = Field(attribute='cust_fatherName', column_name='cust_fatherName')
    priority_tag = Field(attribute='priority_tag', column_name='Priority Tag')
    october_handling_vertical_name = Field(attribute='october_handling_vertical_name', column_name='October Handling Vertical Name')
    acct_no = Field(attribute='acct_no', column_name='ACCT NO')
    pdt1 = Field(attribute='pdt1', column_name='PDT1')
    emi_amount = Field(attribute='emi_amount', column_name='EMI amount')
    pos = Field(attribute='pos', column_name='POS(CR)')


    class Meta:
        model = CompleteDetail
        use_bulk = True
        # batch_size = 1000
        # force_init_instance = True
        # skip_diff = True
        # chunk_size = 2000
        skip_unchanged = True
        instance_loader_class = CachedInstanceLoader


class CompleteDetailAdmin(ImportExportModelAdmin):
    resource_class = CompleteDetailResource
    skip_admin_log = True  #
    change_list_template = 'src/templates/admin/change_list_import_export.html'
    # use_bulk = True
    batch_size = 2000
    chunk_size = 2000
    show_full_result_count = False
    change_form_template = 'src/templates/admin/change_form.html'
    search_fields = ('regno', )
    list_display = (
        'hpa_no', 'name', 'chsno', 'engno', 'regno', 'brndes', 'rgndes', 'outstand'
    )
    list_per_page = 200
    readonly_fields = ('state', )
    list_max_show_all = False
    exclude = ()
    actions = (ExportCsvMixin.export_as_csv, ExportAllCsvMixin.export_all_as_csv, )

    def get_search_fields(self, request):
        if request.user.is_superuser:
            self.search_fields = ('hpa_no', 'name', 'emp_name', 'chsno', 'engno', 'regno', 'brndes', 'assdes', 'place',
                                  'mobile_no', 'outstand', 'rgndes', 'cust_fatherName')
        return self.search_fields

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = super().get_readonly_fields(request)
        if not obj:
            read_only_fields = ()
            if not request.user.is_superuser:
                print(type(request.method))
        if request.user.is_superuser:
            read_only_fields = ()
        return read_only_fields

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     if not request.user.is_superuser:
    #         x = list(form.base_fields.keys())
    #         print(len(x))
    #         # print(form.base_fields[x[0]])
    #     return form

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            self.exclude = (
                'emp_name', 'age', 'bill1', 'soh', 'assdes', 'status', 'branch',
                'place', 'postoffice', 'road_name', 'landmark', 'city_village', 'state_code', 'district_code',
                'taluk', 'website', 'pincode', 'office_phone_no', 'resi_telephone', 'mobile_no', 'pager_no', 'gu_name', 'gu_place',
                'gu_postoffice', 'gu_road_name', 'gu_landmark', 'gu_city_village', 'gu_state_des', 'gu_district_des',
                'gu_taluk', 'gu_pincode', 'gu_office_phone_no', 'gu_resi_telephone', 'gu_mobile_no', 'cust_fatherName',
                'priority_tag', 'october_handling_vertical_name', 'acct_no', 'pdt1', 'emi_amount', 'pos'
            )
        else:
            self.exclude = ()
        return self.exclude

    def get_list_display(self, request):
        listDisplay = super().get_list_display(request)
        if request.user.is_superuser:
            print('superuser', str(request.user))
            self.list_display = ('hpa_no', 'name', 'emp_name', 'chsno', 'engno', 'regno', 'brndes', 'assdes', 'mobile_no',
                                 'place', 'mobile_no', 'outstand', 'rgndes', 'cust_fatherName')
        if not request.user.is_superuser:
            self.list_per_page = 10
        else:
            self.list_per_page = 50
        return listDisplay


admin.site.base_template = 'src/templates/admin/base.html'
admin.site.login_template = 'src/templates/admin/login.html'
admin.site.index_template = 'src/templates/admin/index.html'
admin.site.base_site_template = 'src/templates/admin/base_site.html'
admin.site.site_header = "Radha Krishna Repo Agency"
admin.site.site_title = "Radha Krishna Repo Agency"
admin.site.index_title = "Welcome to Radha Krishna Repo Agency"
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AxisCompleteDetail, AxisCompleteDetailAdmin)
admin.site.register(CompleteDetail, CompleteDetailAdmin)
