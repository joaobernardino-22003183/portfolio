from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.register(Post)

from .models import Cadeira

admin.site.register(Cadeira)

from .models import Linguagem

admin.site.register(Linguagem)

from .models import Projeto

admin.site.register(Projeto)

from .models import Professor

admin.site.register(Professor)
