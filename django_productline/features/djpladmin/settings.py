#refinement for django_productline.settings

def refine_INSTALLED_APPS(original):
    return ['django_productline.features.djpladmin', 'django.contrib.admin', ] + list(original)


introduce_ADMIN_URL = 'admin/'

def refine_TEMPLATE_CONTEXT_PROCESSORS(original):
    return list(original) + []



def refine_TEMPLATES(original):
    OPTIONS = original[0]['OPTIONS']
    OPTIONS['context_processors'] += [
        'django_productline.features.djpladmin.context_processors.django_admin'
    ]
    return original



introduce_AUTH_GROUPS = {
    #{
    #    'name': 'Operator',
    #    'permissions': [
    #        ('add_mymodel', 'myapp'),
    #        ('change_my_model', 'myapp')
    #    ]
    #}
}
