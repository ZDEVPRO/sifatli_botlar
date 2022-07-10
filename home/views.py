from django.shortcuts import render, redirect
from home.models import HomeTitle, Customers, Faq, Projects, Contact
from home.forms import ContactForm
from django.contrib import messages
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    home_title = HomeTitle.objects.all().order_by('-id')[:1]
    customers = Customers.objects.all().order_by('id')[:22]
    faq = Faq.objects.all().order_by('id')[:50]

    context = {
        'home_title': home_title,
        'customers': customers,
        'faq': faq
    }
    return render(request, 'index/base.html', context)


def projects(request):
    projects_all = Projects.objects.all().order_by('-id')

    page = request.GET.get('page', 1)

    paginator = Paginator(projects_all, 9)
    try:
        page_number = paginator.page(page)
    except PageNotAnInteger:
        page_number = paginator.page(1)
    except EmptyPage:
        page_number = paginator.page(paginator.num_pages)

    context = {
        'projects_all': projects_all,
        'page_obj': projects_all,
        'page_number': page_number
    }
    return render(request, 'projects/base.html', context)


def projects_detail(request, id, slug):
    project = Projects.objects.get(pk=id)
    context = {
        'project': project,
    }
    return render(request, 'projects_detail/base.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.telegram = form.cleaned_data['telegram']
            data.message = form.cleaned_data['message']
            data.ip = get_client_ip(request)
            messages.success(request, 'Xabaringiz qabul qilindi! Sizga qisqa fursat ichida javob beramiz. Raxmat!')
            data.save()
            try:
                BOTTOKEN = "5521746341:AAGn0c2C1pQDdQcRIbU4n_XcaBwh78V1iCg"
                chat_id = "1038442571"

                text1 = f'🇺🇿 YANGI XABAR KELDI! 🇺🇿 \n' \
                        f'\n 👨  FISH: {data.first_name} {data.last_name}' \
                        f'\n 📲  Telefon raqam: {data.phone}' \
                        f'\n 📲  Telegram: {data.telegram}' \
                        f'\n 🌐  IP RAQAM: {data.ip}' \
                        f'\n 🕒  VAQT: {data.create_time.strftime("%-H:%M")}' \
                        f'\n 📆  SANA: {data.create_date.strftime("%d-%b, %Y-Yil")}' \
                        f'\n 📩  XABAR: {data.message}'
                text = "".join(text1)

                url = f"https://api.telegram.org/bot{BOTTOKEN}/sendMessage?chat_id={chat_id}&text={text}"

                r = requests.get(url)
                print(r)
            except:
                print('Funksiya ishlamadi!')

        return redirect('contact')
    form = ContactForm
    context = {'form': form}
    return render(request, 'contact/base.html', context)
