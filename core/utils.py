from django.urls import reverse_lazy

software = {
    'Nmap': '#',
    'searchmap': reverse_lazy('core:searchmap:index'),
    'dirsearch': '#',
    'gobuster': '#',
    'amass': '#',
    'subfinder': '#',
    'whatweb': '#',
}
